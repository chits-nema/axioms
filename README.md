# Axioms, by UdonEaters

Axioms is an AI purchasing engine that allows B2B buyers select the best vendor. The website allows them to either upload quotations for products. They could also specify the product they are looking for, where the engine will then look for a similar product offered by a vendor available in our database. 

Axioms is a multi-part repository containing:

- `DataNova/` — a modern Astro frontend website template.
- `backend_stuff/` — a Python FastAPI backend for vendor quotation processing and ranking.
- `frontend_stuff/` — a small static frontend demo with `index.html`, `app.js`, and `styles.css`.
- `lovable/` — a Vite-based React/TanStack frontend app. Included for website design.

## Project structure

### `DataNova/`

This is the main frontend project. It is an Astro application with support for React, Svelte, Tailwind CSS, Keystatic CMS, and Astro DB.

Key files:
- `DataNova/package.json`
- `DataNova/astro.config.mjs`
- `DataNova/src/pages/`
- `DataNova/src/layout/`
- `DataNova/src/components/`
- `DataNova/README.md` (project-specific frontend docs)

### `backend_stuff/`

A FastAPI backend service for vendor decision support and document handling.

Key files:
- `backend_stuff/requirements.txt`
- `backend_stuff/app/main.py`
- `backend_stuff/app/routes/`
- `backend_stuff/app/services/`

### `frontend_stuff/`

A simple static frontend demo.

Key files:
- `frontend_stuff/index.html`
- `frontend_stuff/app.js`
- `frontend_stuff/styles.css`

### `lovable/`

A standalone Vite-based frontend app built with React, Tailwind, and TanStack libraries.

Key files:
- `lovable/package.json`
- `lovable/vite.config.ts`
- `lovable/src/`

## How to run each project

### 1. Run the backend

From the repo root:

```bash
cd backend_stuff
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

The backend exposes a health endpoint at `http://127.0.0.1:8000/health`.

> Note: `backend_stuff/app/main.py` registers FastAPI routers for upload, normalise, metrics, requirements, catalogue, and evaluation.

### 2. Run the DataNova frontend

This is the main website frontend. It requires Node.js `>=22.12.0`.

```bash
cd DataNova
npm install
npm run dev
```

Then open the local Astro dev URL shown in the terminal.

If you need to install a newer Node version, use a version manager (like `nvm`, `volta`, or your distro package manager).

### 3. Run the backend with Docker

There is a `Dockerfile` at the repo root that builds the FastAPI backend with Python 3.12.

From the repo root, build and run the container:

```bash
docker build -t axioms-backend .
docker run -p 8000:8000 axioms-backend
```

Then open `http://127.0.0.1:8000/health` to verify the containerized backend.

## Notes

- There is no single root install command. Each subproject is independent.
- `DataNova/README.md` contains more details specific to the Astro frontend.
- `backend_stuff` loads environment variables via `.env` if present, so add config there as needed.

## Recommended order for first exploration

1. Start `backend_stuff` to verify the API works.
2. Start `DataNova` to preview the main frontend.
3. Optionally open `frontend_stuff` and `lovable` for the extra frontend demos.

