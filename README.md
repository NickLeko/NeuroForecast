# NeuroForecast
## A Governance-First Probabilistic Forecasting System for Parkinson’s Clinical Trials

NeuroForecast is a version-controlled probabilistic forecasting system for Phase 2 and Phase 3 Parkinson’s Disease clinical trials.

It is designed as a governance-first decision-support prototype for high-uncertainty healthcare environments.

The system prioritizes calibration discipline, explicit assumptions, version control, and outcome accountability over narrative confidence or model complexity.

---

## Problem

Clinical trials operate under extreme uncertainty.

Yet most decision systems — whether clinical, financial, or AI-driven — often prioritize:

- Confidence over calibration  
- Narrative over base rates  
- Complexity over governance  

In healthcare, poor calibration is not just a modeling flaw — it is a safety risk.

NeuroForecast explores how to design a structured, auditable forecasting system where:

- Probabilities are locked and immutable  
- Assumptions are explicitly defined  
- Outcomes are objectively scored  
- Model updates are version-controlled  
- Errors are visible and measurable  

---

## What This Project Demonstrates

This repository intentionally showcases:

- Probabilistic reasoning under uncertainty  
- Healthcare domain modeling  
- Explicit assumption management  
- Version-controlled model governance  
- Deterministic evaluation via Brier scoring  
- Transparent error visibility  

## Status & Scope

- Research / learning mode  
- N = 23 predictions (10 resolved, 13 active)  
- Not statistically validated  
- Not investment advice  
- Not regulatory decision support  

This system demonstrates probabilistic reasoning discipline and governance-first AI design.  
Statistical calibration assessment requires 50+ outcomes minimum.


## Design Philosophy & Governance

NeuroForecast is built on four core governance principles.

### 1. Immutable Prediction Locking

Once a probability is assigned to a trial, it is never edited.

No retroactive changes.  
No silent revisions.  
No narrative adjustments.

Predictions are stored in:

`data/locked_predictions.csv`

This enforces auditability and eliminates hindsight bias.


---

## Initial Calibration Validation

Before prospective locking began, the model was stress-tested using a historical backfill set of completed trials.

- 10+ completed Phase 2/3 trials evaluated
- Predictions assigned using model rules
- Outcomes scored using Brier metric
- No retroactive edits permitted

This validation phase surfaced systematic underestimation of Phase 3 symptomatic programs, leading to mechanism-specific baseline separation.

Full details available in:

docs/CALIBRATION_SUMMARY.md

---

### 2. Explicit Model Versioning

All baselines and structural rules are defined in:

`model/WEIGHTS.md`  
`model/VERSION.md`

Any structural modification requires:

- A version bump  
- A calibration log entry  
- A traceable Git commit  

This mirrors governance standards used in regulated healthcare AI systems.

---

### 3. Deterministic Evaluation

Performance is measured using the Brier Score:

`Brier = (p_locked − outcome)^2`

Lower scores indicate better calibration.

Scoring is reproducible via:

`scripts/compute_brier.py`

There are no hidden adjustments.

---

### 4. Safety-Aware Outcome Classification

Trial outcomes are classified conservatively:

- **Success** = Primary endpoint met AND development continued  
- **Failure** = Primary endpoint not met OR safety/futility termination  

Safety signals are treated as failures because development cannot proceed.

---

## Current Scope (v1.0)

Focus area:

- Parkinson’s Disease  
- Phase 2 and Phase 3 interventional trials  
- Clinical efficacy primary endpoints  
- Enrollment ≥ 30  

Mechanism categories:

- Dopaminergic symptomatic  
- Non-dopaminergic symptomatic  
- Disease-modifying  

Scope discipline preserves calibration integrity.

---

## Model Structure (v1.0)

### Phase 2 Baseline

0.15

### Phase 3 Baselines

- Tier 3 Dopaminergic Symptomatic: 0.55  
- Non-Dopaminergic Symptomatic: 0.30  
- Disease-Modifying: 0.20  

Additive adjustments apply for:

- Sample size  
- Evidence tier  
- Endpoint fragility  
- Operational risk  
- Mechanism-specific penalties  

Probability constraints:

- Floor: 0.10  
- Ceiling: 0.50  

Full model specification:

`model/WEIGHTS.md`

---

## Repository Structure

data/
- locked_predictions.csv  
- outcomes.csv  
- outcomes_scored.csv  
- monitor_log.csv  

model/
- WEIGHTS.md  
- VERSION.md  
- CALIBRATION_LOG.md  

scripts/
- compute_brier.py  

docs/
- GLOSSARY.md  
- PD_CALIBRATION_SPEC_v1.0.pdf  

---

## What This Is Not

- Not financial advice  
- Not an optimized trading system  
- Not a machine learning black box  
- Not curve-fitted historical modeling  
- Not narrative-driven biotech speculation  

This is a structured calibration system.

---

## Relevance to Healthcare AI

Many healthcare AI failures stem from:

- Poor calibration  
- Silent assumption drift  
- Unversioned model updates  
- Lack of outcome accountability  

NeuroForecast embeds:

- Transparent assumptions  
- Explicit version control  
- Deterministic scoring  
- Governance before optimization  

These principles transfer directly to:

- Clinical decision support systems  
- AI model oversight environments  
- Safety-critical ML deployments  

---

## Future Roadmap

Planned expansions include:

- Logging market-implied probabilities  
- Calibration curves and reliability diagrams  
- Comparative forecasting (model vs. market)  
- Broader neurodegenerative indications  
- Structured monitoring dashboard  

All expansions will follow versioned governance discipline.

---

## Status

Research / personal-use mode.  
Public-facing flagship project.  
Prospective prediction locking active.  
Model version: v1.0  

The project prioritizes disciplined iteration over rapid expansion.