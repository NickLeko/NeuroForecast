# Contributing to NeuroForecast

Thank you for your interest.

This repository is a probabilistic forecasting system for Parkinson’s clinical trials.
It prioritizes calibration discipline over opinion.

Because of that, contribution rules are strict.

---

## Core Principles

1. Locked predictions are immutable.
2. No retrospective probability edits.
3. Model changes require version bumps.
4. All changes must be traceable in Git history.

This project values structural integrity over velocity.

---

## What CAN Be Contributed

The following types of contributions are welcome:

- Documentation improvements
- Typos and formatting fixes
- Script improvements (non-breaking)
- New utility scripts (analysis, monitoring)
- Clarification of glossary terms
- Improvements to data validation

---

## What CANNOT Be Contributed

The following are prohibited:

- Editing `data/locked_predictions.csv` probabilities after lock
- Retroactively changing `p_locked`
- Quiet edits to baselines or weights
- Changing outcome classifications without documentation
- Deleting historical rows

If a locked prediction was incorrect, it remains incorrect.
Calibration requires permanent error visibility.

---

## Adding New Predictions

When adding a new trial prediction:

1. Ensure the trial meets scope criteria (see `model/WEIGHTS.md`)
2. Compute probability using current version rules
3. Apply floor/ceiling caps
4. Add row to `data/locked_predictions.csv`
5. Commit with message:

   Lock NCTXXXXXXX at 0.XX (v1.0 rules)

6. Do NOT edit after commit

---

## Adding Outcomes

When outcome becomes known:

1. Append row to `data/outcomes.csv`
2. Set:
   - outcome_binary = 1 (success) OR 0 (failure)
   - termination_reason if applicable
3. Run:

   python3 scripts/compute_brier.py --repo-root . --update-outcomes

4. Commit with message:

   Outcome added for NCTXXXXXXX — Brier computed

---

## Proposing Model Changes

Model changes require:

1. Version bump in `model/VERSION.md`
2. Update to `model/WEIGHTS.md`
3. Entry in `model/CALIBRATION_LOG.md`
4. Clear rationale in commit message

Reactive adjustments after a single surprising outcome are discouraged.

---

## Branch Policy

- No direct commits to `main`
- All changes via Pull Request
- No force pushes
- No history rewrites

---

## Decision Authority

Final decision authority rests with the repository owner.

This is not a consensus-driven model.
It is a governed calibration system.

---

## Philosophy

NeuroForecast is built on:

- Base rates over narrative
- Discipline over confidence
- Transparency over optimization
- Long-term calibration over short-term accuracy

If contributing improves structural integrity, it is welcome.

If contributing improves persuasion but weakens discipline, it is rejected.