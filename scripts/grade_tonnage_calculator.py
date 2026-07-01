#!/usr/bin/env python3
"""
Grade-tonnage calculator.

Given a composite/block dataset (grade + tonnage per sample or block), computes
tonnage and average grade above a set of cut-off grades, i.e. a grade-tonnage
sensitivity table. Only use this when the user has supplied real block/composite
data -- this script does not estimate or interpolate grades, it only aggregates
data that's already there.

Input: CSV with at minimum two columns: `grade` and `tonnage` (one row per
sample/block/domain). Extra columns are ignored.

Usage:
    python grade_tonnage_calculator.py <input.csv> [--cutoffs 0.2,0.3,0.5,1.0] [--grade-unit "% Cu"]

Output: a markdown table printed to stdout with, for each cut-off:
    - tonnage above cut-off
    - average grade of material above cut-off
    - contained metal (tonnage x grade, in the same grade unit)
    - % of total tonnage retained
"""
import argparse
import csv
import sys


def load_data(path):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames_lower = {name.lower(): name for name in reader.fieldnames or []}
        if "grade" not in fieldnames_lower or "tonnage" not in fieldnames_lower:
            sys.exit(
                f"Error: input CSV must have 'grade' and 'tonnage' columns. "
                f"Found columns: {reader.fieldnames}"
            )
        grade_col = fieldnames_lower["grade"]
        tonnage_col = fieldnames_lower["tonnage"]
        for i, row in enumerate(reader, start=2):
            try:
                grade = float(row[grade_col])
                tonnage = float(row[tonnage_col])
            except (ValueError, TypeError):
                sys.exit(f"Error: could not parse grade/tonnage as numbers on row {i}: {row}")
            rows.append((grade, tonnage))
    if not rows:
        sys.exit("Error: no data rows found in input CSV.")
    return rows


def grade_tonnage_table(rows, cutoffs):
    total_tonnage = sum(t for _, t in rows)
    results = []
    for cutoff in sorted(cutoffs):
        above = [(g, t) for g, t in rows if g >= cutoff]
        tonnage_above = sum(t for _, t in above)
        contained_metal = sum(g * t for g, t in above)
        avg_grade = (contained_metal / tonnage_above) if tonnage_above > 0 else 0.0
        pct_retained = (tonnage_above / total_tonnage * 100) if total_tonnage > 0 else 0.0
        results.append(
            {
                "cutoff": cutoff,
                "tonnage_above": tonnage_above,
                "avg_grade": avg_grade,
                "contained_metal": contained_metal,
                "pct_retained": pct_retained,
            }
        )
    return results, total_tonnage


def main():
    parser = argparse.ArgumentParser(description="Compute a grade-tonnage sensitivity table.")
    parser.add_argument("input_csv", help="Path to CSV with 'grade' and 'tonnage' columns.")
    parser.add_argument(
        "--cutoffs",
        default="0.2,0.3,0.5,0.75,1.0",
        help="Comma-separated list of cut-off grades to evaluate (default: 0.2,0.3,0.5,0.75,1.0).",
    )
    parser.add_argument(
        "--grade-unit",
        default="grade unit",
        help='Label for the grade unit, e.g. "% Cu" or "g/t Au" (for display only).',
    )
    args = parser.parse_args()

    cutoffs = [float(c.strip()) for c in args.cutoffs.split(",") if c.strip()]
    rows = load_data(args.input_csv)
    results, total_tonnage = grade_tonnage_table(rows, cutoffs)

    print(f"Total samples/blocks: {len(rows)}")
    print(f"Total tonnage (no cut-off applied): {total_tonnage:,.0f}\n")
    print(f"| Cut-off ({args.grade_unit}) | Tonnage above cut-off | Avg. grade ({args.grade_unit}) | Contained metal | % of total tonnage |")
    print("|---|---|---|---|---|")
    for r in results:
        print(
            f"| {r['cutoff']:.3g} | {r['tonnage_above']:,.0f} | {r['avg_grade']:.3g} "
            f"| {r['contained_metal']:,.0f} | {r['pct_retained']:.1f}% |"
        )

    print(
        "\nNote: this is a simple aggregation of the supplied composite/block data, not a "
        "geostatistical estimate. Real cut-off selection should also weigh mining/processing "
        "cost, metal price, and recovery -- see references/resource-estimation.md."
    )


if __name__ == "__main__":
    main()
