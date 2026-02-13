# Scripts

This folder contains small utilities for deterministic scoring and bookkeeping.

## compute_brier.py

Computes Brier scores for completed/terminated trials where outcomes are known.

### Inputs

- `data/locked_predictions.csv` (immutable)
  - must contain: `nct_id`, `p_locked`
- `data/outcomes.csv` (append-only)
  - must contain: `nct_id`, `outcome_binary`, and metadata fields

### Output

- `data/outcomes_scored.csv` (derived)
  - includes `p_locked` and computed `brier_score`
  - includes a `warning` column for rows that cannot be scored

### Usage

From repo root:

```bash
python3 scripts/compute_brier.py --repo-root .
'''
