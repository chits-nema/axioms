const state = {
  uploadedFile: null,
  extractedDocument: null,
  normalisedResult: null,
  criteria: [],
  questions: [],
  catalogMetrics: [],
  catalogResult: null,
};

const els = {
  apiBaseUrl: document.querySelector("#apiBaseUrl"),
  fileKind: document.querySelector("#fileKind"),
  pdfFile: document.querySelector("#pdfFile"),
  fileLabel: document.querySelector("#fileLabel"),
  pipelineButton: document.querySelector("#pipelineButton"),
  uploadButton: document.querySelector("#uploadButton"),
  extractButton: document.querySelector("#extractButton"),
  normaliseButton: document.querySelector("#normaliseButton"),
  normaliseOutput: document.querySelector("#normaliseOutput"),
  purchase: document.querySelector("#purchase"),
  organisationContext: document.querySelector("#organisationContext"),
  successFactors: document.querySelector("#successFactors"),
  constraints: document.querySelector("#constraints"),
  discoverButton: document.querySelector("#discoverButton"),
  criteriaList: document.querySelector("#criteriaList"),
  maxQuestions: document.querySelector("#maxQuestions"),
  tradeoffsButton: document.querySelector("#tradeoffsButton"),
  tradeoffForm: document.querySelector("#tradeoffForm"),
  handoffButton: document.querySelector("#handoffButton"),
  handoffOutput: document.querySelector("#handoffOutput"),
  catalogProduct: document.querySelector("#catalogProduct"),
  catalogCategory: document.querySelector("#catalogCategory"),
  catalogVendors: document.querySelector("#catalogVendors"),
  catalogMetrics: document.querySelector("#catalogMetrics"),
  catalogMetricWeights: document.querySelector("#catalogMetricWeights"),
  catalogEvaluateButton: document.querySelector("#catalogEvaluateButton"),
  catalogClearMetricsButton: document.querySelector("#catalogClearMetricsButton"),
  catalogResult: document.querySelector("#catalogResult"),
  uploadStatus: document.querySelector("#uploadStatus"),
  extractStatus: document.querySelector("#extractStatus"),
  normaliseStatus: document.querySelector("#normaliseStatus"),
  criteriaStatus: document.querySelector("#criteriaStatus"),
  tradeoffStatus: document.querySelector("#tradeoffStatus"),
  handoffStatus: document.querySelector("#handoffStatus"),
  catalogStatus: document.querySelector("#catalogStatus"),
};

els.catalogMetrics.addEventListener("input", () => {
  state.catalogMetrics = parseCatalogMetrics();
  renderCatalogMetricWeights();
});

els.catalogClearMetricsButton.addEventListener("click", () => {
  els.catalogMetrics.value = "";
  state.catalogMetrics = [];
  renderCatalogMetricWeights();
});

els.pdfFile.addEventListener("change", () => {
  const file = els.pdfFile.files[0];
  els.fileLabel.textContent = file ? file.name : "Choose a PDF";
  state.uploadedFile = null;
  state.extractedDocument = null;
  state.normalisedResult = null;
  updateWorkflow();
});

els.pipelineButton.addEventListener("click", async () => {
  await withLoading(els.pipelineButton, "Running...", els.normaliseOutput, async () => {
    await uploadPdf();
    await extractText();
    await normaliseUploadedPdf();
    showJson(els.normaliseOutput, {
      message: "PDF pipeline complete. Requirements discovery will include the normalised quotation.",
      uploaded_file: state.uploadedFile,
      normalised_storage_path: state.normalisedResult.normalised_storage_path,
      normalised: state.normalisedResult.normalised,
    });
  });
});

els.uploadButton.addEventListener("click", async () => {
  await withLoading(els.uploadButton, "Uploading...", els.normaliseOutput, async () => {
    const result = await uploadPdf();
    showJson(els.normaliseOutput, {
      message: "Upload complete. Extract Text is now connected to this file.",
      uploaded_file: result,
    });
  });
});

els.extractButton.addEventListener("click", async () => {
  await withLoading(els.extractButton, "Extracting...", els.normaliseOutput, async () => {
    const result = await extractText();
    showJson(els.normaliseOutput, result);
  });
});

els.normaliseButton.addEventListener("click", async () => {
  await withLoading(els.normaliseButton, "Normalising...", els.normaliseOutput, async () => {
    const result = await normaliseUploadedPdf();
    showJson(els.normaliseOutput, result);
  });
});

els.discoverButton.addEventListener("click", async () => {
  const body = {
    purchase: els.purchase.value.trim(),
    organisation_context: els.organisationContext.value.trim(),
    success_factors: lines(els.successFactors.value),
    constraints: lines(els.constraints.value),
    normalised_quotations: state.normalisedResult ? [state.normalisedResult.normalised] : [],
  };

  await withLoading(els.discoverButton, "Discovering...", els.handoffOutput, async () => {
    const result = await apiFetch("/requirements/discover", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    state.criteria = result.criteria ?? [];
    state.questions = [];
    renderCriteria();
    renderTradeoffMessage("Generate tradeoffs from the discovered criteria.");
    els.handoffOutput.textContent = `Criteria stored at:\n${result.requirements_storage_path}`;
    updateWorkflow();
  });
});

els.tradeoffsButton.addEventListener("click", async () => {
  if (!state.criteria.length) {
    renderTradeoffMessage("Discover criteria first.");
    return;
  }

  const body = {
    criteria: state.criteria,
    max_questions: Number(els.maxQuestions.value || 8),
  };

  await withLoading(els.tradeoffsButton, "Generating...", els.handoffOutput, async () => {
    const result = await apiFetch("/requirements/tradeoffs", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    state.questions = result.questions ?? [];
    renderTradeoffs();
    updateWorkflow();
  });
});

els.handoffButton.addEventListener("click", async () => {
  const tradeoffAnswers = collectTradeoffAnswers();
  if (!state.criteria.length || !state.questions.length) {
    showJson(els.handoffOutput, { error: "Discover criteria and answer tradeoffs first." });
    return;
  }

  const unanswered = tradeoffAnswers.filter((answer) => !answer.selected_key);
  if (unanswered.length) {
    showJson(els.handoffOutput, {
      error: "Answer every tradeoff question first.",
      unanswered,
    });
    return;
  }

  const body = {
    criteria: state.criteria,
    tradeoff_answers: tradeoffAnswers,
  };

  await withLoading(els.handoffButton, "Creating...", els.handoffOutput, async () => {
    const result = await apiFetch("/requirements/weighting-input", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    showJson(els.handoffOutput, result);
    els.handoffStatus.textContent = "Handoff: ready";
    els.handoffStatus.classList.add("done");
  });
});

els.catalogEvaluateButton.addEventListener("click", async () => {
  const product = els.catalogProduct.value.trim();
  if (!product) {
    renderCatalogError("Describe what you want to purchase first.");
    return;
  }

  const metrics = state.catalogMetrics.map((metric) => metric.name);
  const metricWeights = Object.fromEntries(
    state.catalogMetrics.map((metric) => [metric.name, metric.weight]),
  );
  const body = {
    product,
    metrics,
    metric_weights: metricWeights,
    category: els.catalogCategory.value || null,
    vendors: commaList(els.catalogVendors.value),
  };

  await withLoading(els.catalogEvaluateButton, "Evaluating...", els.catalogResult, async () => {
    els.catalogResult.innerHTML = `<div class="empty-state">Searching catalogue and scoring vendors...</div>`;
    const result = await apiFetch("/catalog/evaluate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    state.catalogResult = result;
    renderCatalogResult(result);
    updateWorkflow();
  });
});

async function uploadPdf() {
  const file = els.pdfFile.files[0];
  if (!file) {
    throw new Error("Choose a PDF first.");
  }

  const formData = new FormData();
  formData.append("kind", els.fileKind.value);
  formData.append("files", file);

  const result = await apiFetch("/upload", {
    method: "POST",
    body: formData,
  });

  state.uploadedFile = result?.[0] ?? null;
  state.extractedDocument = null;
  state.normalisedResult = null;
  updateWorkflow();
  return state.uploadedFile;
}

async function extractText() {
  if (!state.uploadedFile) {
    throw new Error("Upload a PDF first.");
  }

  const result = await apiFetch("/normalise/extract", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(uploadedFilePayload()),
  });

  state.extractedDocument = result;
  updateWorkflow();
  return result;
}

async function normaliseUploadedPdf() {
  if (!state.uploadedFile) {
    throw new Error("Upload a PDF first.");
  }

  const result = await apiFetch("/normalise", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(uploadedFilePayload()),
  });

  state.normalisedResult = result;
  updateWorkflow();
  return result;
}

function uploadedFilePayload() {
  return {
    file_id: state.uploadedFile.file_id,
    kind: state.uploadedFile.kind,
    storage_path: state.uploadedFile.storage_path,
  };
}

function renderCriteria() {
  if (!state.criteria.length) {
    els.criteriaList.innerHTML = `<div class="criterion">No criteria yet.</div>`;
    return;
  }

  els.criteriaList.innerHTML = state.criteria
    .map(
      (criterion) => `
        <div class="criterion">
          <span class="tag">${escapeHtml(criterion.category)}</span>
          <div>
            <strong>${escapeHtml(criterion.label)}</strong>
            <span>${escapeHtml(criterion.description ?? "")}</span>
            <label class="score-control">
              <span>Importance <strong id="score_${escapeHtml(criterion.key)}">${escapeHtml(criterion.score ?? 3)}</strong>/5</span>
              <input
                type="range"
                min="1"
                max="5"
                step="1"
                value="${escapeHtml(criterion.score ?? 3)}"
                data-criterion-key="${escapeHtml(criterion.key)}"
              />
            </label>
          </div>
        </div>
      `,
    )
    .join("");

  document.querySelectorAll("[data-criterion-key]").forEach((slider) => {
    slider.addEventListener("input", (event) => {
      const key = event.target.dataset.criterionKey;
      const score = Number(event.target.value);
      const criterion = state.criteria.find((item) => item.key === key);
      if (criterion) {
        criterion.score = score;
      }

      const label = document.querySelector(`#score_${CSS.escape(key)}`);
      if (label) {
        label.textContent = String(score);
      }
    });
  });
}

function renderTradeoffs() {
  if (!state.questions.length) {
    renderTradeoffMessage("No tradeoff questions generated.");
    return;
  }

  els.tradeoffForm.innerHTML = state.questions
    .map(
      (question) => `
        <fieldset class="tradeoff">
          <legend>${escapeHtml(question.prompt)}</legend>
          <div class="tradeoff-options">
            <label>
              <input type="radio" name="${escapeHtml(question.question_id)}" value="${escapeHtml(question.left_key)}" />
              ${escapeHtml(question.left_label)}
            </label>
            <label>
              <input type="radio" name="${escapeHtml(question.question_id)}" value="${escapeHtml(question.right_key)}" />
              ${escapeHtml(question.right_label)}
            </label>
          </div>
        </fieldset>
      `,
    )
    .join("");
}

function renderTradeoffMessage(message) {
  els.tradeoffForm.innerHTML = `<div class="tradeoff">${escapeHtml(message)}</div>`;
}

function collectTradeoffAnswers() {
  return state.questions.map((question) => {
    const selected = document.querySelector(`input[name="${question.question_id}"]:checked`);
    return {
      question_id: question.question_id,
      selected_key: selected?.value ?? "",
    };
  });
}

function parseCatalogMetrics() {
  return lines(els.catalogMetrics.value)
    .map((line) => {
      const separator = line.lastIndexOf(":");
      if (separator === -1) {
        return { name: line, weight: 3 };
      }

      const name = line.slice(0, separator).trim();
      const rawWeight = Number(line.slice(separator + 1).trim());
      return {
        name,
        weight: clampWeight(Number.isFinite(rawWeight) ? rawWeight : 3),
      };
    })
    .filter((metric) => metric.name);
}

function renderCatalogMetricWeights() {
  if (!state.catalogMetrics.length) {
    els.catalogMetricWeights.innerHTML = `<div class="empty-state">Leave metrics empty to let the backend generate them from the purchase request.</div>`;
    return;
  }

  els.catalogMetricWeights.innerHTML = state.catalogMetrics
    .map(
      (metric, index) => `
        <label class="metric-weight">
          <span>${escapeHtml(metric.name)}</span>
          <strong id="catalog_weight_${index}">${escapeHtml(metric.weight)}</strong>
          <input
            type="range"
            min="1"
            max="5"
            step="1"
            value="${escapeHtml(metric.weight)}"
            data-catalog-metric-index="${index}"
          />
        </label>
      `,
    )
    .join("");

  document.querySelectorAll("[data-catalog-metric-index]").forEach((slider) => {
    slider.addEventListener("input", (event) => {
      const index = Number(event.target.dataset.catalogMetricIndex);
      const weight = clampWeight(Number(event.target.value));
      state.catalogMetrics[index].weight = weight;
      const label = document.querySelector(`#catalog_weight_${index}`);
      if (label) {
        label.textContent = String(weight);
      }
    });
  });
}

function renderCatalogResult(result) {
  const recommendation = result.recommendation ?? {};
  const rows = result.evaluation_results ?? [];
  const metrics = result.metrics_used ?? [];

  els.catalogResult.innerHTML = `
    <section class="recommendation">
      <span class="tag">Recommendation</span>
      <h3>${escapeHtml(recommendation.recommend_vendor ?? recommendation.vendor ?? "Review ranking")}</h3>
      <p>${escapeHtml(recommendation.reasoning ?? recommendation.summary ?? "The backend returned a ranking without a narrative recommendation.")}</p>
      ${recommendation.trade_offs ? `<p><strong>Trade-off:</strong> ${escapeHtml(recommendation.trade_offs)}</p>` : ""}
    </section>

    <section class="ranking">
      <div class="ranking-head">
        <strong>Vendor ranking</strong>
        <span>${escapeHtml(metrics.length)} metrics</span>
      </div>
      ${renderRankingRows(rows, metrics)}
    </section>

    ${result.generated_metrics_template ? `<details class="catalog-details"><summary>Generated metrics template</summary><pre class="output">${escapeHtml(JSON.stringify(result.generated_metrics_template, null, 2))}</pre></details>` : ""}
  `;
}

function renderRankingRows(rows, metrics) {
  if (!rows.length) {
    return `<div class="empty-state">No vendors were returned.</div>`;
  }

  return rows
    .map(
      (row, index) => `
        <article class="ranking-row">
          <div class="ranking-title">
            <span>${escapeHtml(index + 1)}</span>
            <strong>${escapeHtml(row.vendor ?? row.index ?? "Unknown vendor")}</strong>
            <b>${escapeHtml(row.weighted_score ?? row.final_weighted_score ?? "n/a")}</b>
          </div>
          <div class="metric-score-grid">
            ${metrics.map((metric) => renderMetricScore(row, metric)).join("")}
          </div>
        </article>
      `,
    )
    .join("");
}

function renderMetricScore(row, metric) {
  const score = row[metric] ?? "n/a";
  const reasoning = row[`${metric}_reasoning`] ?? "";
  return `
    <div class="metric-score">
      <span>${escapeHtml(metric)}</span>
      <strong>${escapeHtml(score)}</strong>
      ${reasoning ? `<small>${escapeHtml(reasoning)}</small>` : ""}
    </div>
  `;
}

function renderCatalogError(message) {
  els.catalogResult.innerHTML = `<div class="empty-state error-state">${escapeHtml(message)}</div>`;
}

function updateWorkflow() {
  setStatus(els.uploadStatus, "Upload", Boolean(state.uploadedFile));
  setStatus(els.extractStatus, "Extract", Boolean(state.extractedDocument));
  setStatus(els.normaliseStatus, "Normalise", Boolean(state.normalisedResult));
  setStatus(els.criteriaStatus, "Criteria", Boolean(state.criteria.length));
  setStatus(els.tradeoffStatus, "Tradeoffs", Boolean(state.questions.length));
  setStatus(els.catalogStatus, "Catalog RAG", Boolean(state.catalogResult));

  els.extractButton.disabled = !state.uploadedFile;
  els.normaliseButton.disabled = !state.uploadedFile;
  els.discoverButton.disabled = !state.normalisedResult;
  els.tradeoffsButton.disabled = !state.criteria.length;
  els.handoffButton.disabled = !state.questions.length;
}

function setStatus(element, label, done) {
  element.textContent = `${label}: ${done ? "done" : "waiting"}`;
  element.classList.toggle("done", done);
}

async function apiFetch(path, options) {
  let response;
  try {
    response = await fetch(`${els.apiBaseUrl.value}${path}`, options);
  } catch (error) {
    throw new Error(
      `Could not reach the backend at ${els.apiBaseUrl.value}.\n\nMake sure FastAPI is running and restart it after code changes.\n\n${error.message}`,
    );
  }

  const text = await response.text();
  const payload = safeJson(text);

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}\n${JSON.stringify(payload, null, 2)}`);
  }

  return payload;
}

async function withLoading(button, label, outputElement, callback) {
  const previous = button.textContent;
  button.disabled = true;
  button.textContent = label;
  try {
    await callback();
  } catch (error) {
    outputElement.textContent = error.message;
  } finally {
    button.disabled = false;
    button.textContent = previous;
    updateWorkflow();
  }
}

function lines(value) {
  return value
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean);
}

function commaList(value) {
  return value
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function clampWeight(value) {
  return Math.min(5, Math.max(1, Math.round(value)));
}

function showJson(element, value) {
  element.textContent = JSON.stringify(value, null, 2);
}

function safeJson(text) {
  if (!text) {
    return null;
  }

  try {
    return JSON.parse(text);
  } catch {
    return { raw_response: text };
  }
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

renderCriteria();
renderTradeoffMessage("Discover criteria first.");
state.catalogMetrics = parseCatalogMetrics();
renderCatalogMetricWeights();
updateWorkflow();
