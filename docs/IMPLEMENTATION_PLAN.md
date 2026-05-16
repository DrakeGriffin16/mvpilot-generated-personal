# Implementation Plan

## Overview
This document outlines the step‑by‑step implementation for a clean personal portfolio using the resolved tech stack: Next.js, React, TypeScript, Tailwind CSS, Python 3.12, FastAPI, Uvicorn, Supabase Postgres, pgvector, NVIDIA Nemotron, pytest, and npm run build.

## Phase 0 – Project Setup
1. Initialize repository with README, .env.example, and license.
2. Set up frontend: `npx create-next-app@latest portfolio-frontend --ts --tailwind`.
3. Set up backend: create `src/` directory, add `requirements.txt`, initialize FastAPI app.

## Phase 1 – Backend Core
1. Create `src/app.py` as FastAPI entrypoint.
2. Define routers for portfolio data (projects, about, contact).
3. Integrate Supabase Postgres client; expose health check.
4. Add pgvector extension for future AI‑powered search (placeholder).
5. Write unit tests in `tests/test_app.py` using pytest.
6. Add Dockerfile (optional) and ensure `uvicorn src.app:app --host 0.0.0.0 --port 8000` works.

## Phase 2 – Agent Logic (MVPilot core)
1. Implement `src/core/agent.py` that encapsulates the deterministic agent:
   - Load configuration from environment.
   - Provide `generate_portfolio_data()` returning mock data.
   - Include a method to call NVIDIA Nemotron via a client protocol (mocked for now).
2. Wire agent into FastAPI routes to serve dynamic content.
3. Write tests for agent functions.

## Phase 3 – Frontend Integration
1. Create pages: `pages/index.tsx` (home), `pages/projects.tsx`, `pages/about.tsx`, `pages/contact.tsx`.
2. Use Tailwind CSS for clean, responsive layout.
3. Fetch data from backend API using `fetch` or SWR.
4. Add TypeScript interfaces matching backend models.
5. Implement dark mode toggle (optional).

## Phase 4 – Vector Search & AI Enhancements (Future)
1. Set up pgvector extension in Supabase.
2. Create a route `/search` that accepts query, uses Nemotron embeddings (via client protocol) and pgvector similarity search.
3. Frontend adds a search bar to filter projects.

## Phase 5 – Testing & CI
1. Configure pytest to run on push (GitHub Actions placeholder).
2. Add npm test script for frontend linting and type checking.
3. Ensure `npm run build` produces a production Next.js bundle.
4. Write smoke test in `tests/test_app.py` that hits health endpoint.

## Phase 6 – Documentation & Demo
1. Update `docs/ARCHITECTURE.md` with component diagram.
2. Fill `docs/BUILD_LOG.md` with steps taken.
3. Create `demo/demo_script.md` walkthrough for judges.
4. Ensure `.env.example` contains placeholders for SUPABASE_URL, SUPABASE_ANON_KEY, NEMOTRON_API_KEY.

## Phase 7 – Final Review
1. Run full test suite locally.
2. Verify no secrets are committed (check .gitignore).
3. Prepare GitHub repo for submission.

## Timeline (suggested)
- Day 0: Setup repos and basic scaffolding.
- Day 1‑2: Backend API and agent core.
- Day 2‑3: Frontend pages and styling.
- Day 3‑4: Integration testing and vector search stub.
- Day 4: Documentation, demo script, final polish.

## Success Criteria
- Portfolio site loads and displays personal info.
- API returns JSON data without errors.
- Agent core can be invoked and returns deterministic output.
- All tests pass.
- No real secrets in repository.
- Build artifacts (`npm run build`, `pytest`) succeed.