# Architecture Overview

## Project Goal
Create a clean, modern personal portfolio that showcases projects, skills, and contact information while leveraging AI‑enhanced content generation via NVIDIA Nemotron.

## High‑Level Layers
1. **Frontend (Client)**
   - **Framework**: Next.js 13+ (App Router) with React 18
   - **Styling**: Tailwind CSS for utility‑first, responsive design
   - **Language**: TypeScript for static type safety
   - **Features**:
     - Static generation of portfolio pages (projects, bio, blog)
     - Client‑side interactivity (theme toggle, smooth scroll, modal forms)
     - SEO‑friendly metadata via `next/head`

2. **Backend (API)**
   - **Framework**: FastAPI (Python 3.12) served by Uvicorn
   - **Purpose**:
     - Expose REST endpoints for dynamic data (e.g., contact form submissions, project analytics)
     - Provide AI‑powered content generation via Nemotron (text summarization, tagline creation)
     - Handle Supabase Postgres interactions (pgvector for embeddings)
   - **Security**:
     - No secrets in repo; `.env.example` only shows placeholder keys
     - CORS restricted to frontend domain
     - Input validation with Pydantic models

3. **Data & Storage**
   - **Primary DB**: Supabase Postgres (managed)
   - **Extension**: `pgvector` for storing vector embeddings of project descriptions, enabling semantic search or AI‑driven recommendations
   - **Schema Highlights**:
     - `projects` table (id, title, description, tech_stack, embeddings vector)
     - `skills` table (name, proficiency)
     - `contacts` table (form submissions)

4. **AI Integration**
   - **Model**: NVIDIA Nemotron (accessed via a secure API key stored server‑side)
   - **Use Cases**:
     - Auto‑generate project taglines from descriptions
     - Summarize long‑form blog posts for preview cards
     - Suggest skill improvements based on project history
   - **Protocol**: Backend defines a thin client protocol (`src/core/agent.py`) that isolates AI calls, making them mockable for tests.

5. **Development & CI**
   - **Package Management**: npm for frontend, pip (`requirements.txt`) for backend
   - **Build**: `npm run build` produces optimized Next.js static output
   - **Testing**:
     - Backend unit tests with `pytest` (`tests/test_app.py`)
     - Frontend type checking via `tsc` (implicit in Next.js dev)
   - **Linting/Formatting**: ESLint + Prettier (frontend), Ruff/Black (backend) – configured via repo configs (not shown here)

## Data Flow
1. User visits portfolio → Next.js serves static pages (SSG).
2. Interactive components (e.g., contact form) send POST requests to FastAPI endpoints.
3. FastAPI validates input, writes to Supabase, optionally calls Nemotron for AI‑enhanced responses.
4. For admin/content updates, a separate protected route can trigger re‑generation of static pages (via Next.js incremental static regeneration) or direct DB updates.

## Why This Stack?
- **Next.js + React + Tailwind** gives a performant, SEO‑friendly UI with minimal configuration.
- **TypeScript** reduces runtime bugs and improves developer experience.
- **FastAPI** offers rapid API development with automatic OpenAPI docs and strong validation.
- **Supabase** provides a scalable Postgres backend with built‑in auth and storage, plus the `pgvector` extension for AI‑ready vector search.
- **NVIDIA Nemotron** supplies cutting‑edge language generation for dynamic content without exposing model weights.
- **pytest** ensures backend reliability; the frontend benefits from Next.js built‑in testing utilities.
- All secrets are kept out of the repository; only example files are committed.

## Scalability Considerations
- The API layer is stateless; horizontal scaling behind a load balancer is straightforward.
- Supabase handles DB scaling; vector indexes can be added as the project collection grows.
- Static frontend can be served via a CDN (Vercel, Netlify, or AWS CloudFront) for global low‑latency delivery.

## Conclusion
This architecture balances simplicity with extensibility: a clean, visually appealing portfolio frontend backed by a robust, AI‑augmented API and a modern Postgres database. It adheres to the submitted idea while satisfying the resolved tech stack and MVPilot’s safety and reproducibility constraints.