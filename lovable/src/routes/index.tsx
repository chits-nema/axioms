import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Axiom — Procurement decisions you can defend" },
      {
        name: "description",
        content:
          "Axiom compares vendor quotations, weighs tradeoffs, and produces explainable procurement recommendations.",
      },
      { property: "og:title", content: "Axiom — Procurement decisions you can defend" },
      {
        property: "og:description",
        content:
          "Compare vendor quotations or explore trusted catalogue options. Axiom normalises inputs, discovers decision criteria, and produces an explainable recommendation.",
      },
    ],
    links: [
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&display=swap",
      },
    ],
  }),
  component: Index,
});

const serif = { fontFamily: "'Instrument Serif', serif" };
const sans = { fontFamily: "'Inter', system-ui, sans-serif" };

function Index() {
  return (
    <div className="min-h-screen bg-background text-foreground" style={sans}>
      {/* Top nav */}
      <header className="mx-auto flex max-w-7xl items-center justify-between px-6 pt-6 sm:px-10">
        <div className="flex items-center gap-2">
          <div className="h-2 w-2 rounded-full bg-primary" aria-hidden />
          <span className="text-xl tracking-tight italic" style={serif}>
            Axiom
          </span>
        </div>
        <nav className="hidden items-center gap-8 text-sm md:flex">
          <a href="#product" className="hover:text-primary transition-colors">
            Product
          </a>
          <a href="#how" className="hover:text-primary transition-colors">
            How it works
          </a>
          <a href="#tracks" className="hover:text-primary transition-colors">
            Tracks
          </a>
          <a href="#contact" className="hover:text-primary transition-colors">
            Contact
          </a>
        </nav>
        <a
          href="#start"
          className="rounded-full bg-primary px-5 py-2.5 text-sm font-medium text-primary-foreground transition-opacity hover:opacity-90"
        >
          Start decision
        </a>
      </header>

      {/* Hero */}
      <section className="mx-auto max-w-7xl px-6 pt-16 pb-10 sm:px-10 sm:pt-24">
        <div className="mx-auto max-w-4xl text-center">
          <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-border bg-card px-4 py-1.5 text-xs tracking-[0.18em] uppercase text-muted-foreground">
            <span className="h-1.5 w-1.5 rounded-full bg-primary" />
            Axiom procurement analyst
          </div>
          <h1
            className="text-5xl leading-[1.02] tracking-tight text-foreground sm:text-7xl md:text-8xl"
            style={serif}
          >
            Procurement decisions
            <br />
            <em className="not-italic text-primary">you can defend.</em>
          </h1>
          <p className="mx-auto mt-8 max-w-2xl text-base leading-relaxed text-muted-foreground sm:text-lg">
            Compare vendor quotations or explore trusted catalogue options. Axiom normalises inputs,
            discovers decision criteria, weighs tradeoffs, and produces an explainable recommendation.
          </p>
          <div className="mt-10 flex flex-wrap items-center justify-center gap-3">
            <a
              href="#start"
              className="rounded-full bg-primary px-6 py-3 text-sm font-medium text-primary-foreground transition-opacity hover:opacity-90"
            >
              Upload quotations
            </a>
            <a
              href="#tracks"
              className="rounded-full border border-border bg-card px-6 py-3 text-sm font-medium text-foreground transition-colors hover:bg-accent"
            >
              Use catalogue
            </a>
          </div>
        </div>

        {/* Hero video */}
        <div className="relative mx-auto mt-20 max-w-6xl overflow-hidden rounded-2xl border border-border bg-card shadow-[0_30px_80px_-30px_oklch(0.62_0.12_180_/_0.25)]">
          <video
            src="/axiom-hero.mp4"
            autoPlay
            muted
            loop
            playsInline
            className="block w-full"
            aria-label="Axiom abstract motion identity"
          />
          <div className="pointer-events-none absolute inset-x-0 bottom-0 flex items-end justify-between px-6 py-4 text-[10px] tracking-[0.3em] uppercase text-muted-foreground">
            <span>Study № 01</span>
            <span>Clarity · by design</span>
          </div>
        </div>
      </section>

      {/* Steps */}
      <section id="how" className="mx-auto max-w-7xl px-6 py-24 sm:px-10">
        <div className="mb-14 flex items-end justify-between gap-6">
          <h2 className="max-w-xl text-4xl tracking-tight sm:text-5xl" style={serif}>
            A structured path from inputs to defensible output.
          </h2>
          <div className="hidden text-xs tracking-[0.3em] uppercase text-muted-foreground md:block">
            How it works
          </div>
        </div>
        <div className="grid gap-px overflow-hidden rounded-2xl border border-border bg-border md:grid-cols-3">
          {[
            { n: "Step 01", t: "Understand options", d: "Normalise uploaded PDFs into structured vendor facts." },
            { n: "Step 02", t: "Discover priorities", d: "Surface the decision criteria that actually matter." },
            { n: "Step 03", t: "Defend recommendation", d: "Weighted scoring with an explainable tradeoff view." },
          ].map((s) => (
            <div key={s.n} className="bg-card p-8">
              <div className="text-[10px] tracking-[0.3em] uppercase text-muted-foreground">{s.n}</div>
              <div className="mt-4 text-xl text-foreground" style={serif}>
                {s.t}
              </div>
              <p className="mt-3 text-sm leading-relaxed text-muted-foreground">{s.d}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Tracks */}
      <section id="tracks" className="mx-auto max-w-7xl px-6 pb-24 sm:px-10">
        <div className="grid gap-6 md:grid-cols-2">
          {[
            {
              tag: "Track A",
              title: "Upload vendor quotations",
              body: "Normalise uploaded PDFs into structured vendor facts, then score each quote against the same criteria and tradeoffs.",
              link: "Start with quotations",
            },
            {
              tag: "Track B",
              title: "Use catalogue RAG",
              body: "Start without quotations. Retrieve relevant vendor context from the catalogue and run it through the same metrics pipeline.",
              link: "Explore the catalogue",
            },
          ].map((t) => (
            <div
              key={t.tag}
              className="group relative overflow-hidden rounded-2xl border border-border bg-card p-8 transition-colors hover:border-primary/40"
            >
              <div className="text-[10px] tracking-[0.3em] uppercase text-muted-foreground">{t.tag}</div>
              <div className="mt-4 text-2xl text-foreground" style={serif}>
                {t.title}
              </div>
              <p className="mt-3 max-w-md text-sm leading-relaxed text-muted-foreground">{t.body}</p>
              <a href="#start" className="mt-8 inline-flex items-center gap-2 text-sm font-medium text-primary">
                {t.link}
                <span aria-hidden>→</span>
              </a>
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer id="contact" className="border-t border-border">
        <div className="mx-auto grid max-w-7xl gap-10 px-6 py-14 sm:px-10 md:grid-cols-4">
          <div className="md:col-span-2">
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-primary" />
              <span className="text-lg italic" style={serif}>
                Axiom
              </span>
            </div>
            <p className="mt-4 max-w-sm text-sm leading-relaxed text-muted-foreground">
              An explainable procurement analyst. Clarity, by design.
            </p>
          </div>
          <div>
            <div className="text-[10px] tracking-[0.3em] uppercase text-muted-foreground">Product</div>
            <ul className="mt-4 space-y-2 text-sm">
              <li><a href="#how" className="hover:text-primary">How it works</a></li>
              <li><a href="#tracks" className="hover:text-primary">Tracks</a></li>
            </ul>
          </div>
          <div>
            <div className="text-[10px] tracking-[0.3em] uppercase text-muted-foreground">Company</div>
            <ul className="mt-4 space-y-2 text-sm">
              <li><a href="#contact" className="hover:text-primary">Contact</a></li>
            </ul>
          </div>
        </div>
        <div className="border-t border-border">
          <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-5 text-[10px] tracking-[0.3em] uppercase text-muted-foreground sm:px-10">
            <span>© MMXXVI Axiom</span>
            <span>Clarity · by design</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
