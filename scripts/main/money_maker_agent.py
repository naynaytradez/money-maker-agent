#!/usr/bin/env python3
"""Produce reviewable marketing drafts; no external sales or email actions."""
import json
import logging
import os
from datetime import datetime, timezone
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path(os.environ.get("AGENT_OUTPUT_DIR", str(ROOT)))
CONFIG_PATH = Path(os.environ.get("AI_CONFIG_PATH", str(ROOT / ".ai_config.json")))

def load_config():
    if CONFIG_PATH.is_file():
        with CONFIG_PATH.open(encoding="utf-8") as handle:
            result = json.load(handle)
        if not isinstance(result, dict):
            raise ValueError("Config must be a JSON object")
    else:
        result = {}
    result["lead_magnet_title"] = os.environ.get("LEAD_MAGNET_TITLE") or result.get("lead_magnet_title", "AI Productivity Toolkit 2026")
    return result

class MoneyMakerAgent:
    def __init__(self):
        self.config = load_config()
    def run_once(self):
        (OUTPUT / "content").mkdir(parents=True, exist_ok=True)
        title = escape(self.config["lead_magnet_title"])
        tools = [("Jasper", "Writing assistance"), ("Copy.ai", "Marketing automation"), ("Surfer", "Content optimization"), ("ClickFunnels", "Funnel software"), ("Notion", "Knowledge and productivity")]
        reviews = "".join("<article><h2>" + escape(name) + "</h2><p>" + escape(description) + "</p><p>Draft: verify current features and pricing before publication.</p></article>" for name, description in tools)
        html = "<!doctype html><html lang='en'><meta charset='utf-8'><title>" + title + "</title><main><h1>" + title + "</h1><p>Editorial draft. No affiliate links have been verified.</p>" + reviews + "</main></html>"
        (OUTPUT / "content" / "affiliate_page_draft.html").write_text(html, encoding="utf-8")
        funnel = [{"day": 0, "subject": "Welcome to your AI productivity toolkit"}, {"day": 2, "subject": "Three practical AI workflows"}, {"day": 4, "subject": "How to evaluate AI tools"}, {"day": 7, "subject": "Common AI workflow mistakes"}, {"day": 14, "subject": "Build your own productivity system"}]
        (OUTPUT / "content" / "email_funnel_draft.json").write_text(json.dumps(funnel, indent=2), encoding="utf-8")
        stats = {"last_run": datetime.now(timezone.utc).isoformat(), "status": "drafts_generated", "email_platform_connected": False, "affiliate_programs_verified": 0, "leads_collected": 0, "emails_sent": 0, "revenue_generated": 0.0, "note": "Draft generation only. No integrations or sales."}
        (OUTPUT / "stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
        logging.info("Created editorial drafts and stats; no emails, affiliate registrations or revenue.")

def main():
    (OUTPUT / "logs").mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", handlers=[logging.StreamHandler(), logging.FileHandler(OUTPUT / "logs" / "automation.log", encoding="utf-8")])
    MoneyMakerAgent().run_once()

if __name__ == "__main__":
    main()
