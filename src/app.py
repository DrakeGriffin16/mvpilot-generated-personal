"""
FastAPI entrypoint for the personal portfolio.
Provides health check and portfolio data endpoints.
"""
import os
from fastapi import FastAPI

app = FastAPI(title="Personal Portfolio API")

# Supabase configuration (placeholders – actual values should be set via environment variables)
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://your-project.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "your-anon-key")


@app.get("/", tags=["Health"])
async def root():
    """Root health check."""
    return {
        "message": "Personal Portfolio API is running",
        "status": "healthy"
    }


@app.get("/portfolio", tags=["Portfolio"])
async def get_portfolio():
    """Return static portfolio information."""
    # In a real implementation, this data would be fetched from Supabase.
    return {
        "name": "Your Name",
        "title": "Software Developer & Designer",
        "bio": "Passionate about building clean, user‑focused applications with modern web technologies.",
        "skills": ["TypeScript", "React", "Next.js", "Tailwind CSS", "Python", "FastAPI"],
        "projects": [
            {
                "id": 1,
                "title": "Personal Portfolio",
                "description": "A clean, responsive portfolio showcasing work and skills.",
                "url": "https://github.com/yourname/portfolio",
                "technologies": ["Next.js", "React", "TypeScript", "Tailwind CSS"]
            },
            {
                "id": 2,
                "title": "AI‑Powered Blog",
                "description": "Blog platform using NVIDIA Nemotron for content generation.",
                "url": "https://github.com/yourname/ai-blog",
                "technologies": ["Python", "FastAPI", "NVIDIA Nemotron", "Supabase"]
            }
        ],
        "contact": {
            "email": "you@example.com",
            "linkedin": "https://linkedin.com/in/yourname",
            "github": "https://github.com/yourname"
        }
    }


if __name__ == "__main__":
    # Uvicorn is used as the ASGI server.
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
"