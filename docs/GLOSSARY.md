# NeuroForecast — Glossary

This document defines terminology used throughout the NeuroForecast project.

The goal is precision, not marketing language.

---

## Core Concepts

### Locked Prediction
A probability (P(success)) assigned before outcome data is known.
- Stored in `data/locked_predictions.csv`
- Immutable after commit
- Expressed as decimal (0.23 = 23%)

### Outcome
Binary result of the primary efficacy endpoint.
- 1 = Primary endpoint met AND development continued
- 0 = Primary endpoint not met OR terminated for safety/futility

Business or operational terminations are excluded unless efficacy or safety data justifies classification.

### Brier Score
Primary calibration metric.

Formula:

Brier = (p_locked − outcome_binary)^2

Range:
- 0.0 = perfect calibration
- 1.0 = maximum error

Lower is better.

---

## Trial Structure Terms

### Phase 2
Exploratory efficacy stage.
Higher biological and endpoint uncertainty.

### Phase 3
Confirmatory efficacy stage.
Typically larger N, regulatory-grade endpoints.

---

## Mechanism Classes

### Dopaminergic Symptomatic
Direct or indirect dopamine pathway modulation.

Examples:
- Levodopa formulations
- Dopamine agonists
- MAO-B inhibitors
- COMT inhibitors

High historical success rate in Phase 3.

---

### Non-Dopaminergic Symptomatic
Improves motor or non-motor symptoms without direct dopamine receptor stimulation.

Examples:
- A2A antagonists
- GPR6 inverse agonists
- Circuit-based modulation
- Microbiome modulation (if symptomatic endpoint)

Moderate historical success rate.

---

### Disease-Modifying (DM)
Intended to slow progression or alter underlying pathology.

Examples:
- Anti-alpha-synuclein antibodies
- GCase enhancers
- Kinase inhibitors
- Mitochondrial/metabolic agents

Historically low success rate in Parkinson’s Phase 3.

---

## Evidence Tiers

Tier 0  
Purely theoretical or epidemiological rationale.

Tier 1  
Preclinical or biomarker support; no replicated motor efficacy.

Tier 2  
Human target engagement demonstrated; early efficacy signals plausible.

Tier 3  
Class-proven symptomatic mechanism with prior regulatory success.

Note:
Baselines sometimes incorporate Tier implicitly (see `model/WEIGHTS.md`).

---

## Endpoint Fragility

Qualitative assessment of noise sensitivity.

Low  
Objective, short-window motor change (e.g., OFF time, 30-min UPDRS III).

Medium  
Diary-based or moderate variability scales.

High  
Long-duration progression slope or highly placebo-sensitive endpoints.

Penalty applied in additive model.

---

## Operational Risk

Qualitative downgrade applied for:
- Academic-led networks
- Smaller biotech sponsors
- Complex multi-center execution

Large pharma generally considered lower operational risk.

---

## Safety Termination

Trial stopped due to adverse events or mortality signals.

Counted as:
Outcome = 0

Because development cannot proceed.

---

## Futility Stop

Stopped early due to interim analysis showing low probability of success.

Counted as:
Outcome = 0

---

## Platform Trial

Multi-arm, multi-stage trial structure testing several agents simultaneously.
E.g., ACT-PD.

Each arm treated as separate predictive unit if independent.

---

## Prospective-Only Mode

NeuroForecast does not backfill predictions for historical trials unless explicitly conducting retrospective calibration analysis.

Public flagship mode = prospective locks only.

---

## Versioning

Model changes require:
- Version bump in `model/VERSION.md`
- Entry in `model/CALIBRATION_LOG.md`
- No silent rule edits

---

## Calibration Discipline

Model changes occur only after:
- ≥10 new outcomes, OR
- Sustained worsening Brier across evaluation window

No reactive overfitting.

---

## Philosophy

The system prioritizes:
- Calibration over conviction
- Base rates over narrative
- Structure over intuition
- Transparency over cleverness

This repository is a reasoning artifact, not a trading system.