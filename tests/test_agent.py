import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/main/money_maker_agent.py"

class AgentTest(unittest.TestCase):
    def test_draft_run(self):
        with tempfile.TemporaryDirectory() as path:
            env = os.environ.copy()
            env["AGENT_OUTPUT_DIR"] = path
            env["AI_CONFIG_PATH"] = str(Path(path) / "absent.json")
            result = subprocess.run([sys.executable, str(SCRIPT)], env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            root = Path(path)
            self.assertTrue((root / "content/affiliate_page_draft.html").exists())
            self.assertTrue((root / "content/email_funnel_draft.json").exists())
            stats = json.loads((root / "stats.json").read_text())
            self.assertEqual(stats["revenue_generated"], 0)
            self.assertEqual(stats["leads_collected"], 0)
            self.assertEqual(stats["emails_sent"], 0)
