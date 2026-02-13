# NeuroForecast — Model Versioning

This file defines the active model version and the rules for advancing versions.

Versioning applies to:
- Baselines
- Additive weights
- Caps
- Inclusion/exclusion criteria
- Outcome adjudication rules
- Scoring metric

---

## Current Version

### v1.0  
Released: 2026-02-12  
Status: Active  

### Characteristics
- Prospective-first operating mode
- Mechanism-stratified Phase 3 baselines
- Additive scoring system
- Floor: 0.10
- Ceiling: 0.50
- Safety/futility terminations counted as failures
- Brier score as primary calibration metric
- No regression or automated fitting

Full rule set defined in:
`model/WEIGHTS.md`

---

## Version Advancement Rules

A version bump is required if ANY of the following change:

1. Baseline probabilities
2. Additive adjustment values
3. Floor or ceiling caps
4. Inclusion/exclusion scope criteria
5. Outcome classification policy
6. Scoring metric

Minor documentation edits do NOT require a version bump.

---

## Version Numbering Convention

Format:

vMAJOR.MINOR

### MAJOR bump (v2.0, v3.0)

Triggered by:
- Structural model change
- Introduction of regression or statistical fitting
- New mechanism taxonomy
- Shift from additive to multiplicative model
- Change in calibration metric

### MINOR bump (v1.1, v1.2)

Triggered by:
- Baseline adjustments after sufficient data
- Additive weight recalibration
- Scope refinement

---

## Governance Rule

No silent modifications.

Every version change requires:
- Update to `model/WEIGHTS.md`
- Entry in `model/CALIBRATION_LOG.md`
- Git commit message referencing version bump

Example commit message:

v1.1 — Increased Phase 3 Tier 3 baseline from 0.55 to 0.60 after 10 additional outcomes

---

## Calibration Trigger Policy

Model recalibration should only occur when:

- At least 10 new scored outcomes accumulated  
OR
- Mean Brier worsens over two consecutive evaluation windows

Avoid reactive overfitting.

---

## Long-Term Roadmap (Not Active Yet)

Planned but not implemented:

- Archetype-specific empirical baselines
- Bayesian updating framework
- Logistic regression exploration (n ≥ 50 outcomes)
- Public dashboard of rolling Brier

Until then:
Model remains additive and manually governed.

---

## Integrity Statement

NeuroForecast prioritizes:

- Calibration over narrative
- Transparency over opacity
- Version control over intuition
- Prospective discipline over retrospective fitting

If the model changes, the history must show it.