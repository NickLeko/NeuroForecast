# NeuroForecast — Calibration Log

This file documents all model changes. No silent edits.

## v1.0 — 2026-02-12
- Public release.
- Prospective-only operating mode.
- Locked predictions immutable.
- Phase 3 baselines stratified by mechanism class.
- Safety/futility terminations counted as failures.
- Brier score used as primary metric.

Change triggers for future versions:
- ≥10 new outcomes, OR
- worsening average Brier across two consecutive evaluation periods.