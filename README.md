# Money Maker Agent

This version repairs the original configuration crash, runs every six hours through GitHub Actions, and generates reviewable content drafts. The job reports only actual actions performed and has an automated smoke test.

**Not yet connected:** email platform, opt-in subscriber collection, affiliate program accounts, published landing page, commission reporting, and AI model APIs. Generated drafts and zero-value sales metrics are not evidence of revenue.

Run locally: `python -m unittest discover -s tests -v` then `python scripts/main/money_maker_agent.py`.

To inspect scheduled runs, open GitHub Actions and download the `money-maker-output-<run number>` artifact containing `content/`, `logs/`, and `stats.json`. No API keys are required for the draft-generation workflow. Never commit keys or log their contents.

Before launching: apply to affiliate partners, verify offers and disclosures, connect consent-based email marketing with unsubscribe options, and host a real website. Scheduled GitHub Actions runs are not continuous hosting.
