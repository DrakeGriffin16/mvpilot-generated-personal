# Personal Portfolio

A clean, modern personal portfolio built with a full‑stack MVP using Next.js (frontend) and FastAPI (backend). The site showcases projects, skills, and contact information while demonstrating integration with Supabase Postgres, pgvector for embeddings, and optional AI enhancements via NVIDIA Nemotron.

## Tech Stack

- **Frontend**: Next.js, React, TypeScript, Tailwind CSS
- **Backend**: Python 3.12, FastAPI, Uvicorn
- **Database**: Supabase Postgres with pgvector extension
- **AI / LLM**: NVIDIA Nemotron (accessed via a client protocol)
- **Testing**: pytest (backend), npm test / Jest (frontend)
- **Build**: `npm run build` for frontend, standard Python packaging for backend

## Project Structure

```
repo/
├── README.md
├── requirements.txt          # Python dependencies
├── src/
│   ├── app.py                # FastAPI entrypoint
│   └── core/
│       └── agent.py          # MVPilot agent logic (portfolio data handling)
├── tests/
│   └── test_app.py           # Smoke tests for API and agent
├── docs/
│   ├── ARCHITECTURE.md
│   ├── IMPLEMENTATION_PLAN.md
│   └── BUILD_LOG.md
├── demo/
│   └── demo_script.md
└── .env.example
```

## Getting Started

### Prerequisites
- Node.js >= 18
- Python 3.12
- A Supabase project with Postgres and pgvector enabled
- (Optional) Access to NVIDIA Nemotron API

### Backend Setup
1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the example environment file and fill in your values:
   ```bash
   cp .env.example .env
   ```
   Required variables (placeholders in `.env.example`):
   - `SUPABASE_URL`
   - `SUPABASE_SERVICE_ROLE_KEY`
   - `NEMOTRON_API_KEY` (if using Nemotron)
5. Run the FastAPI server:
   ```bash
   uvicorn src.app:app --reload
   ```
   The API will be available at `http://localhost:8000`.

### Frontend Setup
1. Navigate to the `frontend` directory (if you add one later) or create a Next.js app:
   ```bash
   npx create-next-app@latest frontend --typescript --tailwind
   cd frontend
   ```
2. Install any additional packages (e.g., axios for API calls).
3. Set up environment variables in `.env.local` mirroring the backend values needed for API calls.
4. Start the development server:
   ```bash
   npm run dev
   ```
   Visit `http://localhost:3000` to see the portfolio.

### Building for Production
- Frontend: `npm run build` then `npm start`
- Backend: Deploy the FastAPI app via your preferred platform (Docker, Vercel, Render, etc.) ensuring environment variables are set securely.

## API Overview

- `GET /health` – returns service health.
- `GET /projects` – list portfolio projects (supports filtering, search via pgvector).
- `GET /projects/{id}` – get a single project.
- `POST /projects` – create a new project (protected).
- `PUT /projects/{id}` – update a project.
- `DELETE /projects/{id}` – delete a project.

## Testing
Run the backend smoke tests:
```bash
pytest
```
Frontend tests can be added with Jest or React Testing Library as the project grows.

## Documentation
- [Architecture](./docs/ARCHITECTURE.md)
- [Implementation Plan](./docs/IMPLEMENTATION_PLAN.md)
- [Build Log](./docs/BUILD_LOG.md)
- [Demo Script](./demo/demo_script.md)

## License
This project is open source and available under the MIT License.