export const apiBaseUrl = import.meta.env.PUBLIC_API_BASE_URL ?? 'http://127.0.0.1:8000';

export const backendRoutes = [
  {
    label: 'Health check',
    path: '/health',
    description: 'Confirms the FastAPI backend is reachable from DataNova.',
  },
  {
    label: 'Upload quotations',
    path: '/upload',
    description: 'Stores uploaded quotation PDFs for normalisation.',
  },
  {
    label: 'Extract and normalise',
    path: '/normalise',
    description: 'Parses quotation files and produces structured vendor data.',
  },
  {
    label: 'Discover requirements',
    path: '/requirements/discover',
    description: 'Generates criteria from the purchase context and uploaded inputs.',
  },
  {
    label: 'Tradeoff questions',
    path: '/requirements/tradeoffs',
    description: 'Builds the prompts that help users choose between criteria.',
  },
  {
    label: 'Weighting handoff',
    path: '/requirements/weighting-input',
    description: 'Writes the final weighting input used by evaluation.',
  },
  {
    label: 'Catalogue evaluation',
    path: '/catalog/evaluate',
    description: 'Evaluates catalogue vendors when no quotation file is available.',
  },
  {
    label: 'Vendor evaluation',
    path: '/evaluate',
    description: 'Scores vendors once the weighting input and normalised quotations exist.',
  },
];
