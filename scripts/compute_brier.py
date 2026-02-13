#!/usr/bin/env python3
"""
NeuroForecast — Brier Scoring Utility

Reads:
  - data/locked_predictions.csv  (immutable; contains p_locked)
  - data/outcomes.csv            (append-only; contains outcome_binary + metadata)

Writes:
  - data/outcomes_scored.csv     (derived; includes p_locked + brier_score)
Optionally updates:
  - data/outcomes.csv            (fills brier_score if empty and match is unambiguous)

Usage:
  python3 scripts/compute_brier.py --repo-root .
  python3 scripts/compute_brier.py --repo-root . --update-outcomes

Notes:
  - p_locked must be in [0,1]
  - outcome_binary must be 0 or 1
  - For non-NCT ids (e.g., ACT-PD, ASAP-PD), matching is by exact nct_id string.
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


LOCKED_PATH = os.path.join("data", "locked_predictions.csv")
OUTCOMES_PATH = os.path.join("data", "outcomes.csv")
OUTCOMES_SCORED_PATH = os.path.join("data", "outcomes_scored.csv")


def die(msg: str, code: int = 1) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def parse_float(s: str, field: str, row_id: str) -> float:
    try:
        x = float(s)
    except Exception:
        die(f"Invalid float for {field} in id={row_id}: {s!r}")
    if not (0.0 <= x <= 1.0):
        die(f"{field} out of range [0,1] in id={row_id}: {x}")
    return x


def parse_int01(s: str, field: str, row_id: str) -> int:
    try:
        x = int(s)
    except Exception:
        die(f"Invalid int for {field} in id={row_id}: {s!r}")
    if x not in (0, 1):
        die(f"{field} must be 0 or 1 in id={row_id}: {x}")
    return x


def brier(p: float, o: int) -> float:
    return (p - float(o)) ** 2


@dataclass(frozen=True)
class LockedRow:
    id: str
    nct_id: str
    p_locked: float


@dataclass
class OutcomeRow:
    nct_id: str
    outcome_binary: Optional[int]
    outcome_date: str
    outcome_source: str
    termination_reason: str
    brier_score: Optional[float]
    adjudication_notes: str
    _raw: Dict[str, str]


def read_csv_dict(path: str) -> List[Dict[str, str]]:
    if not os.path.exists(path):
        die(f"File not found: {path}")
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            die(f"Missing header row in {path}")
        rows = []
        for r in reader:
            # Normalize keys/values (strip whitespace)
            rows.append({k.strip(): (v.strip() if isinstance(v, str) else v) for k, v in r.items()})
        return rows


def write_csv_dict(path: str, fieldnames: List[str], rows: List[Dict[str, str]]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def load_locked(repo_root: str) -> Dict[str, LockedRow]:
    path = os.path.join(repo_root, LOCKED_PATH)
    rows = read_csv_dict(path)

    required = {"id", "nct_id", "p_locked"}
    if not required.issubset(set(rows[0].keys()) if rows else required):
        die(f"{LOCKED_PATH} missing required columns: {sorted(required)}")

    locked: Dict[str, LockedRow] = {}
    for r in rows:
        rid = r.get("id", "").strip()
        nct = r.get("nct_id", "").strip()
        p = r.get("p_locked", "").strip()
        if not rid or not nct or not p:
            # Allow partially filled metadata but not missing core fields
            die(f"{LOCKED_PATH} has a row missing id/nct_id/p_locked: {r}")

        p_val = parse_float(p, "p_locked", rid)

        if nct in locked:
            die(f"Duplicate nct_id in {LOCKED_PATH}: {nct}")
        locked[nct] = LockedRow(id=rid, nct_id=nct, p_locked=p_val)

    return locked


def load_outcomes(repo_root: str) -> Tuple[List[str], List[OutcomeRow]]:
    path = os.path.join(repo_root, OUTCOMES_PATH)
    rows = read_csv_dict(path)

    # If outcomes.csv is empty except header, DictReader returns [].
    # We still need headers.
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            die(f"Missing header row in {OUTCOMES_PATH}")
        headers = [h.strip() for h in reader.fieldnames]

    required = {"nct_id", "outcome_binary", "outcome_date", "outcome_source", "termination_reason", "brier_score", "adjudication_notes"}
    if not required.issubset(set(headers)):
        die(f"{OUTCOMES_PATH} missing required columns: {sorted(required)}")

    parsed: List[OutcomeRow] = []
    for r in rows:
        nct = r.get("nct_id", "").strip()
        if not nct:
            die(f"{OUTCOMES_PATH} has a row missing nct_id: {r}")

        ob_raw = r.get("outcome_binary", "").strip()
        ob = None if ob_raw == "" else parse_int01(ob_raw, "outcome_binary", nct)

        bs_raw = r.get("brier_score", "").strip()
        bs = None
        if bs_raw != "":
            try:
                bs = float(bs_raw)
            except Exception:
                die(f"Invalid brier_score in {OUTCOMES_PATH} for {nct}: {bs_raw!r}")
            if not (0.0 <= bs <= 1.0):
                die(f"brier_score out of range [0,1] in {OUTCOMES_PATH} for {nct}: {bs}")

        parsed.append(
            OutcomeRow(
                nct_id=nct,
                outcome_binary=ob,
                outcome_date=r.get("outcome_date", "").strip(),
                outcome_source=r.get("outcome_source", "").strip(),
                termination_reason=r.get("termination_reason", "").strip(),
                brier_score=bs,
                adjudication_notes=r.get("adjudication_notes", "").strip(),
                _raw=r,
            )
        )

    return headers, parsed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".", help="Path to repo root (default: .)")
    ap.add_argument("--update-outcomes", action="store_true", help="Fill brier_score in outcomes.csv when computable")
    args = ap.parse_args()

    repo_root = os.path.abspath(args.repo_root)

    locked = load_locked(repo_root)
    headers, outcomes = load_outcomes(repo_root)

    # Build scored output rows
    scored_rows: List[Dict[str, str]] = []
    updated_outcome_rows: List[Dict[str, str]] = []

    computed = 0
    skipped_missing = 0
    skipped_no_outcome = 0
    skipped_not_locked = 0

    for row in outcomes:
        nct = row.nct_id
        lock = locked.get(nct)

        out_raw = dict(row._raw)  # preserve unknown columns
        # Normalize required columns to exist
        for col in headers:
            out_raw.setdefault(col, "")

        if lock is None:
            # outcome exists but wasn't locked — keep it but report
            skipped_not_locked += 1
            scored_rows.append({
                "nct_id": nct,
                "p_locked": "",
                "outcome_binary": "" if row.outcome_binary is None else str(row.outcome_binary),
                "brier_score": "" if row.brier_score is None else f"{row.brier_score:.6f}",
                "outcome_date": row.outcome_date,
                "outcome_source": row.outcome_source,
                "termination_reason": row.termination_reason,
                "adjudication_notes": row.adjudication_notes,
                "warning": "No matching locked prediction found for nct_id",
            })
            updated_outcome_rows.append(out_raw)
            continue

        if row.outcome_binary is None:
            skipped_no_outcome += 1
            scored_rows.append({
                "nct_id": nct,
                "p_locked": f"{lock.p_locked:.6f}",
                "outcome_binary": "",
                "brier_score": "" if row.brier_score is None else f"{row.brier_score:.6f}",
                "outcome_date": row.outcome_date,
                "outcome_source": row.outcome_source,
                "termination_reason": row.termination_reason,
                "adjudication_notes": row.adjudication_notes,
                "warning": "Outcome missing; cannot compute Brier",
            })
            updated_outcome_rows.append(out_raw)
            continue

        # Compute brier
        bs = brier(lock.p_locked, row.outcome_binary)
        computed += 1

        # Update outcomes.csv row if requested and brier_score is empty or mismatched
        if args.update_outcomes:
            out_raw["brier_score"] = f"{bs:.6f}"
        else:
            # keep original
            pass

        scored_rows.append({
            "nct_id": nct,
            "p_locked": f"{lock.p_locked:.6f}",
            "outcome_binary": str(row.outcome_binary),
            "brier_score": f"{bs:.6f}",
            "outcome_date": row.outcome_date,
            "outcome_source": row.outcome_source,
            "termination_reason": row.termination_reason,
            "adjudication_notes": row.adjudication_notes,
            "warning": "",
        })
        updated_outcome_rows.append(out_raw)

    # Write outcomes_scored.csv (derived)
    scored_fieldnames = [
        "nct_id",
        "p_locked",
        "outcome_binary",
        "brier_score",
        "outcome_date",
        "outcome_source",
        "termination_reason",
        "adjudication_notes",
        "warning",
    ]
    write_csv_dict(os.path.join(repo_root, OUTCOMES_SCORED_PATH), scored_fieldnames, scored_rows)

    # Optionally update outcomes.csv (fill brier_score)
    if args.update_outcomes:
        write_csv_dict(os.path.join(repo_root, OUTCOMES_PATH), headers, updated_outcome_rows)

    # Print summary
    print("NeuroForecast — Brier Scoring Summary")
    print(f"Repo root: {repo_root}")
    print(f"Locked predictions: {len(locked)}")
    print(f"Outcomes rows: {len(outcomes)}")
    print(f"Brier computed: {computed}")
    print(f"Skipped (missing outcome): {skipped_no_outcome}")
    print(f"Rows with no locked match: {skipped_not_locked}")
    print(f"Wrote: {OUTCOMES_SCORED_PATH}")
    if args.update_outcomes:
        print(f"Updated: {OUTCOMES_PATH} (brier_score filled where computable)")


if __name__ == "__main__":
    main()