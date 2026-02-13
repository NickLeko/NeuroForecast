# Calibration Summary (v1.0)

## Purpose

Before initiating prospective prediction locking, the NeuroForecast model was stress-tested using a historical backfill set of completed Parkinson’s Phase 2 and Phase 3 trials.

This validation step was performed to:

- Evaluate baseline calibration
- Identify systematic under/overconfidence
- Stress-test mechanism-specific baselines
- Surface high Brier misses transparently

This dataset is not used for optimization.
It exists to demonstrate calibration governance.

---

## Historical Backfill Dataset

Scope:

- Parkinson’s Disease
- Phase 2 and Phase 3
- Randomized, controlled trials
- Clinical efficacy primary endpoints
- Enrollment ≥ 30
- Completed or terminated for safety/futility

Total Trials: 10  
Locked Predictions: 10  
Retroactive edits: 0  

---

## Sample Results Snapshot

| Trial | Phase | Mechanism | Prediction | Outcome | Brier |
|-------|-------|-----------|------------|----------|--------|
| Rotigotine | P3 | Tier 3 Dopaminergic | 0.32 | 1 | 0.46 |
| Istradefylline | P3 | A2A Antagonist | 0.23 | 1 | 0.59 |
| CVT-301 | P3 | Levodopa Rescue | 0.33 | 1 | 0.45 |
| Tozadenant | P3 | A2A Antagonist | 0.23 | 0 | 0.05 |
| Inosine | P3 | Disease-Modifying | 0.23 | 0 | 0.05 |
| Creatine | P3 | Disease-Modifying | 0.18 | 0 | 0.03 |
| SPM 962 | P3 | Dopaminergic | 0.55 | 0 | 0.30 |

Note: High Brier scores are intentionally preserved.  
They demonstrate underestimation bias in early Phase 3 symptomatic modeling.

---

## Observed Structural Signals

Early validation revealed:

- Phase 3 dopaminergic symptomatic programs were materially underweighted.
- Disease-modifying strategies showed low empirical success.
- Phase-specific baselines were required to prevent systematic underprediction.

This led to:

- Phase 3 baseline separation
- Mechanism-stratified baselines
- Version bump to v1.0

All changes documented in `model/VERSION.md`.

---

## Calibration Philosophy

Calibration is treated as a governance metric, not a performance metric.

The objective is:

- Transparent probabilistic reasoning
- Visible error exposure
- Version-controlled iteration
- No hindsight bias correction

Prospective predictions are now locked in real-time.
