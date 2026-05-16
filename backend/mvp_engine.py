"""Core MVP planning logic."""

from __future__ import annotations

from typing import Any


def build_demo_plan(idea: str, features: list[str]) -> dict[str, Any]:
    return {
        'idea': idea,
        'features': features,
        'next_actions': [
            'Validate the highest-risk user workflow.',
            'Review generated data model before wiring persistence.',
            'Run the demo with one realistic intake.',
        ],
    }


def summarize_intake(payload: dict[str, Any]) -> dict[str, Any]:
    goal = str(payload.get('user_goal') or '').strip()
    urgency = str(payload.get('urgency') or 'normal').strip().lower()
    priority = 'high' if urgency in {'urgent', 'high', 'critical'} else 'normal'
    return {
        'summary': goal or "build me a clean personal portfolio",
        'priority': priority,
        'recommended_first_step': 'Create the first tracked work item.',
    }