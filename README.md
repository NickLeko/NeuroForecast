# NeuroForecast

A transparent forecasting and calibration framework for Parkinson’s disease clinical trials.

---

## Overview

NeuroForecast is a structured probabilistic engine that assigns and tracks success probabilities for Phase 2 and Phase 3 Parkinson’s disease (PD) trials.

The goal is not narrative commentary.

The goal is calibration.

Every included trial receives:
- A pre-locked probability of success
- A clearly defined mechanism classification
- Explicit weighting logic
- A binary outcome (success/failure)
- A Brier score

Predictions are immutable once locked.

---

## Why This Exists

Biotech discourse is dominated by:

- Post-hoc rationalization
- Mechanism storytelling
- Selective memory of failures
- Overfitting to small sample anecdotes

Very few public systems:
- Explicitly quantify probability
- Lock predictions before outcomes
- Track calibration over time
- Separate symptomatic vs disease-modifying risk
- Incorporate safety-driven failures correctly

NeuroForecast is designed to do exactly that.

---

## Scope Rules (v6.0)

Trials are included if:

- Phase 2, Phase 2/3, or Phase 3
- Randomized and controlled
- Clinical efficacy primary endpoint
- Enrollment ≥ 30
- Status:
  - Completed
  - Terminated for safety
  - Terminated for futility

Trials terminated for operational, funding, or enrollment issues are excluded.

Safety terminations are counted as failures.

---

## Baseline Structure

### Phase 2 Baseline
Low base rate reflecting historical attrition.

### Phase 3 Baseline (Mechanism-Stratified)

- Tier 3 Dopaminergic (class-proven symptomatic): High baseline
- Non-Dopaminergic Symptomatic: Moderate baseline
- Disease-Modifying: Lower baseline

Adjustments applied for:
- Sample size
- Endpoint fragility
- Operational risk
- Biological plausibility tier

Weights are versioned and documented in the Model Card.

---

## Definitions

### Success
Primary efficacy endpoint met with statistical significance.

### Failure
- Primary endpoint not met
- Terminated for futility
- Terminated for safety

### Brier Score
\[
(p - o)^2
\]

Where:
- p = predicted probability
- o = binary outcome (1 or 0)

Lower is better. Calibration matters more than accuracy on any single trial.

---

## Current Dataset Snapshot

- Total trials evaluated: [update dynamically]
- Overall observed success rate: [update]
- Phase 3 Tier 3 empirical rate: [update]
- Phase 3 Disease-Modifying empirical rate: [update]

All raw data available in `/data/locked_predictions.csv`.

---

## What This Is Not

- Not investment advice
- Not a trading model
- Not a narrative biotech blog
- Not mechanism hype

It is a structured forecasting log.

---

## Limitations

- Small sample size (current N < 100)
- Parkinson’s-specific (for now)
- Does not model subgroup enrichment strategies explicitly
- Does not incorporate adaptive trial design complexity
- Does not price in commercial viability

This is strictly a clinical efficacy probability engine.

---

## Future Expansion

Potential extensions:

- Alzheimer’s disease
- ALS
- Platform trial modeling
- Time-to-readout hazard modeling
- Bayesian updating framework

Expansion will only occur after stable calibration in Parkinson’s.

---

## Transparency Policy

- Predictions are locked before outcome review.
- Weights are versioned.
- Historical predictions are never edited.
- Recalibration requires documented version bump.

No retroactive optimization.

---


## Contact

This project is maintained as a research artifact.
Discussion and critique welcome via Issues.