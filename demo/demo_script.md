# Demo Script – Clean Personal Portfolio

## Overview
This script guides judges through a live demonstration of the **Clean Personal Portfolio** built with Next.js, React, TypeScript, Tailwind CSS, and a Python/FastAPI backend.

---

## Prerequisites
- The repository is cloned and dependencies installed (`npm install` && `pip install -r requirements.txt`).
- Environment variables are set via `.env.example` (placeholders only).
- The development servers are running:
  - Frontend: `npm run dev` (http://localhost:3000)
  - Backend: `uvicorn src.app:app --reload` (http://localhost:8000)

---

## Walkthrough Steps

### 1. Landing Page
1. Open the browser to **http://localhost:3000**.
2. Verify the hero section displays:
   - Your name / tagline.
   - A brief intro paragraph.
   - A call‑to‑action button linking to the *Projects* section.
3. Confirm the layout is responsive by resizing the window or toggling device toolbar.

### 2. Navigation
1. Click the **About**, **Projects**, **Skills**, and **Contact** links in the header.
2. Ensure smooth scroll to each section and URL hash updates.
3. On mobile, open the hamburger menu and verify each link works.

### 3. About Section
1. Observe the profile picture (placeholder) and bio.
2. Check that the text is styled with Tailwind utilities (font‑size, leading, spacing).
3. Validate that any external links (e.g., LinkedIn, GitHub) open in a new tab.

### 4. Projects Section
1. Scroll to the **Projects** grid.
2. Each card should show:
   - Project title.
   - Short description.
   - Tech stack icons (React, Tailwind, etc.).
   - Live demo and source buttons (links point to placeholders).
3. Hover over a card to see the lift shadow effect.
4. Click **Live Demo** – it opens a new tab to the placeholder URL.
5. Click **Source** – it opens the GitHub placeholder.

### 5. Skills Section
1. Verify skill icons are displayed in rows with appropriate spacing.
2. Ensure the icons scale correctly on different screen sizes.

### 6. Contact Section
1. Observe the form with fields: Name, Email, Message.
2. Fill out the form and click **Send**. 
   - The frontend sends a POST request to `http://localhost:8000/api/contact`.
   - The FastAPI endpoint returns a JSON success message (mocked).
3. Confirm a toast or alert appears indicating submission status.

### 7. Backend API Check
1. Open **http://localhost:8000/docs** to view the auto‑generated Swagger UI.
2. Explore the `/api/contact` POST endpoint; try a request with sample data.
3. Verify the response matches the expected schema (`{ "status": "success", "message": "Message received" }`).

### 8. Build & Production Preview
1. Stop the dev servers.
2. Run the production build: `npm run build`.
3. Start the Next.js preview: `npm start`.
4. Verify the landing page loads correctly at http://localhost:3000.
5. Ensure the API server is still running (or start it with `uvicorn src.app:app`).

---

## Success Criteria
- All navigation links work and produce smooth scrolling.
- Responsive design holds at widths ≥320px.
- Form submission reaches the backend and returns a success payload.
- No console errors in the browser dev tools.
- Production build completes without errors and the preview runs.

---

## Notes for Judges
- This demo uses placeholder data and external links; replace them with your actual portfolio items.
- The backend is intentionally minimal; extend it with database calls to Supabase if desired.
- Feel free to explore the source code in `src/` and `src/core/` to see how the MVPilot agent logic is structured.

---

*End of script.*