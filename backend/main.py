"""FastAPI surface for the generated MVP."""

from fastapi import FastAPI
from pydantic import BaseModel

from backend.mvp_engine import build_demo_plan, summarize_intake


app = FastAPI(title="Personal Portfolio")


class Intake(BaseModel):
    user_goal: str
    urgency: str = 'normal'
    notes: str | None = None


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok', 'service': "Personal Portfolio"}


@app.get('/api/demo-plan')
def demo_plan() -> dict[str, object]:
    return build_demo_plan("build me a clean personal portfolio", ["Capture intake details for the target workflow.", "Generate a prioritized MVP action plan.", "Expose demo data through a small FastAPI surface."])


@app.post('/api/intake')
def intake(payload: Intake) -> dict[str, object]:
    return summarize_intake(payload.model_dump())