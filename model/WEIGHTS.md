# NeuroForecast — Weights (v1.0)

This document defines the numeric probability assignment rules.
It is immutable per version. Changes require a version bump and a CALIBRATION_LOG entry.

## 1) Output
Model outputs P(success) as a decimal in [0,1], with caps.

- Floor: 0.10
- Ceiling: 0.50

## 2) Baselines
Baseline depends on phase + archetype.

### Phase 2
- Default Phase 2 baseline: 0.15

### Phase 3 (mechanism-stratified)
- Tier 3 dopaminergic symptomatic baseline: 0.55
- Non-dopaminergic symptomatic baseline: 0.30
- Disease-modifying baseline: 0.20

## 3) Additive Adjustments (percent-points)

### Sample size
- N ≥ 150: +0.03
- 80 ≤ N < 150: +0.00
- 40 ≤ N < 80:  -0.05
- N < 40:       -0.10

### Trial design
- Randomized + double-blind + controlled: +0.02
  (If not double-blind but controlled: +0.01)

### Evidence tier modifier (if baseline does NOT already encode it)
- Tier 2 (human target engagement plausible): +0.03
- Tier 3 (class-proven symptomatic): +0.12
- Tier 1: +0.00

### Endpoint fragility
- Medium fragility: -0.03
- High fragility:   -0.05

### Operational risk
- Mid-size sponsor: -0.01
- Academic/network: -0.01 to -0.02

### Mechanism penalty
- Alpha-syn disease-modifying: -0.03

## 4) Calculation Procedure
1. Choose baseline (phase/archetype).
2. Apply additive adjustments.
3. Apply caps (floor/ceiling).
4. Lock.

No manual overrides.