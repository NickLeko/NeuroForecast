# NeuroForecast — Model Card (v1.0)

## 1. Model Purpose

NeuroForecast is a probabilistic calibration framework for forecasting binary clinical trial outcomes in Parkinson’s disease.

It assigns pre-locked probabilities of success to Phase 2 and Phase 3 randomized controlled trials and tracks long-term calibration using Brier scores.

The objective is:
- Calibration over time
- Mechanism-stratified base rates
- Explicit structural assumptions
- Transparent probability assignment

This model is not intended for:
- Investment advice
- Regulatory decision support
- Clinical treatment decisions

It is a research forecasting artifact.

---

## 2. Target Prediction

Binary Outcome:

1 = Primary efficacy endpoint met  
0 = Primary efficacy endpoint not met, terminated for futility, or terminated for safety  

Prediction Output:

P(Success) ∈ [0, 1]

---

## 3. Inclusion Criteria (Scope v6.0)

Trials are included if:

- Phase 2 / Phase 2/3 / Phase 3
- Randomized and controlled
- Clinical efficacy primary endpoint
- Enrollment ≥ 30
- Status:
  - Completed
  - Terminated for safety
  - Terminated for futility

Excluded:
- Operational termination
- Funding termination
- Enrollment failure
- Non-efficacy biomarker-only trials

Safety terminations are counted as failures.

---

## 4. Mechanism Classification

Each trial is categorized into one of the following archetypes:

### Tier 3 — Class-Proven Symptomatic (Dopaminergic Pathway)
Examples:
- Levodopa optimization
- Dopamine agonists
- COMT inhibitors
- MAO-B inhibitors

These have established historical efficacy in PD motor symptoms.

---

### Tier 2 — Non-Dopaminergic Symptomatic
Examples:
- A2A antagonists
- GPR6 inverse agonists
- Circuit modulation strategies

Mechanistically plausible but not gold-standard.

---

### Tier 1 — Disease-Modifying
Examples:
- Anti-alpha-synuclein antibodies
- Metabolic modifiers
- Neuroinflammation modulators
- Lysosomal / mitochondrial strategies

Historically high failure rate in PD.

---

## 5. Baseline Structure (v6.0)

### Phase 2 Baseline
Low base rate reflecting high attrition.

### Phase 3 Baselines (Mechanism-Specific)

- Tier 3 Dopaminergic: 55%
- Non-Dopaminergic Symptomatic: 30–35%
- Disease-Modifying: 20%

These baselines are empirical within the current dataset and version-controlled.

---

## 6. Adjustment Factors

Adjustments are additive modifiers applied to baseline.

### Sample Size
- ≥150 participants: +3%
- 80–149: 0%
- <80: -2%

### Endpoint Fragility
- Hard objective motor endpoint: 0%
- Diary-based / scale-based: -3%
- Disease progression slope: -4%

### Operational Risk
- Large pharma: 0%
- Mid-size sponsor: -1%
- Academic network: -1 to -2%

### Biological Plausibility Tier
Embedded within baseline selection.

---

## 7. Locking Protocol

- Probability assigned before reviewing outcome.
- Prediction logged.
- Outcome evaluated.
- Brier score computed.
- Record appended to dataset.

No retroactive edits allowed.

Recalibration requires:
- Version bump (e.g., v6.0 → v7.0)
- Justification
- Documented empirical trigger

---

## 8. Evaluation Metric

Primary metric: Brier Score

\[
(p - o)^2
\]

Lower is better.

Secondary:
- Stratified calibration by mechanism
- Phase-specific calibration
- Reliability over time

---

## 9. Known Structural Biases

- Small N (<100 trials currently)
- Parkinson’s-specific
- Does not model adaptive designs
- Does not incorporate enrichment biomarkers explicitly
- Does not model time-to-readout hazard
- Does not incorporate regulatory nuance

---

## 10. Calibration Philosophy

The objective is not to predict every trial correctly.

The objective is:

- Long-term probabilistic calibration
- Correct base rate separation
- Mechanism-stratified realism
- Structural transparency

Overconfidence is penalized.
Narrative bias is penalized.
Retrospective adjustment is prohibited.

---

## 11. Version History

v1.0 — Initial public release  
- Mechanism-stratified Phase 3 baseline  
- Safety termination inclusion  
- Brier tracking formalized  

Future versions will be documented here.

---

## 12. Future Extensions

Planned but not yet implemented:

- Bayesian updating
- Hierarchical modeling
- Time-to-event modeling
- Cross-indication expansion (AD, ALS)
- Prior predictive validation

Expansion will occur only after stable PD calibration.

---

## 13. Responsible Use

NeuroForecast is a research experiment in public calibration.

It is not:
- Financial advice
- Clinical advice
- Regulatory guidance

All outputs should be interpreted as probabilistic estimates under defined structural assumptions.