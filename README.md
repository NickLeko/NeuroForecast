# NeuroForecast  
## A Governed Probabilistic Forecasting System for Parkinson’s Clinical Trials

NeuroForecast is a version-controlled probabilistic forecasting system for Phase 2 and Phase 3 Parkinson’s Disease trials.

It is designed as a governance-first decision-support prototype for high-uncertainty healthcare environments.

The system emphasizes calibration discipline, transparent assumptions, and outcome accountability.

---

## Problem

Clinical trials operate under extreme uncertainty.

Yet most decision systems — whether clinical, financial, or AI-driven — prioritize confidence, narrative, or model complexity over calibration and governance.

In healthcare AI, poor calibration is not just a modeling issue — it is a safety issue.

NeuroForecast explores how to design a structured, versioned forecasting system where:

- Probabilities are locked and immutable
- Assumptions are explicitly defined
- Outcomes are objectively scored
- Model updates are governed and auditable

---

## What This Project Demonstrates

This repository is intentionally structured to showcase:

- Probabilistic reasoning under uncertainty  
- Healthcare domain modeling  
- Explicit assumption management  
- Version-controlled model governance  
- Deterministic evaluation via Brier scoring  
- Transparent error visibility  

It functions as a public research artifact and a governance-first modeling system.

---

## System Design Principles

### 1. Immutable Prediction Locking

Once a probability is assigned to a trial, it is never edited.

No retroactive adjustments.  
No silent revisions.

Predictions are stored in:

data/locked_predictions.csv

This enforces auditability and prevents hindsight bias.

---

### 2. Explicit Model Versioning

All baselines and adjustment rules are defined in:

model/WEIGHTS.md  
model/VERSION.md  

Any structural change requires:

- A version bump  
- A calibration log entry  
- A traceable Git commit  

This mirrors model governance standards in healthcare AI systems.

---

### 3. Deterministic Evaluation

Performance is measured using the Brier Score:

Brier = (p_locked − outcome)^2

Lower scores indicate better calibration.

Scoring is deterministic and reproducible via:

scripts/compute_brier.py

---

### 4. Safety-Aware Outcome Classification

- Success = Primary endpoint met AND development continued  
- Failure = Primary endpoint not met OR safety/futility termination  

Safety signals are explicitly treated as failures because development cannot proceed.

---

## Current Scope (v1.0)

Focus:

- Parkinson’s Disease  
- Phase 2 and Phase 3 interventional trials  
- Clinical efficacy primary endpoints  
- Enrollment ≥ 30  

Mechanism classes:

- Dopaminergic symptomatic  
- Non-dopaminergic symptomatic  
- Disease-modifying  

---

## Model Structure (v1.0)

### Phase 2 Baseline
0.15

### Phase 3 Baselines
- Tier 3 dopaminergic symptomatic: 0.55  
- Non-dopaminergic symptomatic: 0.30  
- Disease-modifying: 0.20  

Additive adjustments apply for:

- Sample size  
- Evidence tier  
- Endpoint fragility  
- Operational risk  
- Mechanism-specific penalties  

Probability caps:
- Floor: 0.10  
- Ceiling: 0.50  

Full specification available in:

model/WEIGHTS.md

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
- Unclear versioning  
- Silent assumption drift  
- Lack of outcome accountability  

NeuroForecast intentionally embeds:

- Transparent assumptions  
- Explicit version control  
- Deterministic evaluation  
- Governance before optimization  

These principles are directly transferable to clinical decision support and AI model oversight environments.

---

## Status

Active research mode.  
Prospective prediction locking ongoing.  
Model version: v1.0  

This repository prioritizes disciplined iteration over rapid expansion.