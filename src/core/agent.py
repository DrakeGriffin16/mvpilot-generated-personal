"""MVPilot agent logic for personal portfolio generation."""

import json
import os
from typing import Dict, Any

class PortfolioAgent:
    def __init__(self):
        # Placeholder for Supabase configuration; actual credentials should be set via environment.
        self.supabase_url = os.getenv("SUPABASE_URL", "")
        self.supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")

    def _fetch_from_supabase(self) -> Dict[str, Any] | None:
        """
        Attempt to fetch portfolio data from Supabase.
        Returns None if configuration is missing or on error.
        """
        if not self.supabase_url or not self.supabase_key:
            return None
        try:
            # Import inside method to avoid hard dependency if not installed.
            from supabase import create_client, Client
            supabase: Client = create_client(self.supabase_url, self.supabase_key)
            # Example table: portfolio_items
            response = supabase.table("portfolio_items").select("*").execute()
            data = response.data
            if data:
                # Transform raw rows into expected structure.
                return self._transform_supabase_data(data)
        except Exception as e:
            # Log error in real implementation; here we just ignore and fallback.
            print(f"Warning: Supabase fetch failed: {e}")
        return None

    def _transform_supabase_data(self, rows: list[dict]) -> Dict[str, Any]:
        """
        Convert raw Supabase rows into a portfolio dict.
        Expected columns: section, title, description, url, order.
        """
        portfolio: Dict[str, Any] = {
            "about": {},
            "projects": [],
            "skills": [],
            "contact": {}
        }
        for row in rows:
            section = row.get("section", "").lower()
            item = {
                "title": row.get("title", ""),
                "description": row.get("description", ""),
                "url": row.get("url", "")
            }
            if section == "about":
                portfolio["about"][row.get("title", "").lower()] = item["description"]
            elif section == "projects":
                portfolio["projects"].append(item)
            elif section == "skills":
                portfolio["skills"].append(item)
            elif section == "contact":
                portfolio["contact"][row.get("title", "").lower()] = item["description"]
        return portfolio

    def generate_portfolio(self) -> Dict[str, Any]:
        """
        Generate the portfolio data.
        Tries to fetch from Supabase; falls back to static mock data.
        """
        data = self._fetch_from_supabase()
        if data is not None:
            return data
        # Fallback mock data
        return {
            "about": {
                "name": "Your Name",
                "title": "Software Engineer",
                "bio": "Passionate about building clean, user‑focused applications."
            },
            "projects": [
                {
                    "title": "Personal Portfolio",
                    "description": "A clean, responsive portfolio showcasing work and skills.",
                    "url": "https://github.com/yourname/portfolio"
                }
            ],
            "skills": [
                {"title": "Python", "description": "", "url": ""},
                {"title": "TypeScript", "description": "", "url": ""},
                {"title": "React", "description": "", "url": ""},
                {"title": "Tailwind CSS", "description": "", "url": ""},
                {"title": "FastAPI", "description": "", "url": ""},
                {"title": "Supabase", "description": "", "url": ""}
            ],
            "contact": {
                "email": "you@example.com",
                "github": "https://github.com/yourname",
                "linkedin": "https://linkedin.com/in/yourname"
            }
        }

def main() -> None:
    """Entry point for running the agent directly."""
    agent = PortfolioAgent()
    portfolio = agent.generate_portfolio()
    print(json.dumps(portfolio, indent=2))

if __name__ == "__main__":
    main()