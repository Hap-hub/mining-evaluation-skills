#!/usr/bin/env python3
"""
Resource classification checklist.

This is NOT an authoritative classifier -- CRIRSCO-family resource classification
(Measured / Indicated / Inferred) is a Qualified/Competent Person judgment call
based on geological understanding, not a formula. This script structures the
common criteria a QP/CP would weigh, and flags where the inputs given look
inconsistent with the classification claimed, so Claude can have a grounded
conversation about it rather than asserting a category itself.

Usage:
    python resource_classification_checklist.py <input.json>

Input JSON example:
{
  "claimed_category": "Indicated",
  "avg_drill_spacing_m": 50,
  "deposit_type": "porphyry copper",
  "geological_continuity": "moderate",   // "high" | "moderate" | "low"
  "qaqc_program": true,                   // standards/blanks/duplicates in place?
  "geological_model_confidence": "moderate" // "high" | "moderate" | "low"
}
"""
import argparse
import json
import sys


CATEGORY_EXPECTATIONS = {
    "Measured": {
        "continuity": {"high"},
        "geological_model_confidence": {"high"},
        "qaqc_required": True,
    },
    "Indicated": {
        "continuity": {"high", "moderate"},
        "geological_model_confidence": {"high", "moderate"},
        "qaqc_required": True,
    },
    "Inferred": {
        "continuity": {"high", "moderate", "low"},
        "geological_model_confidence": {"high", "moderate", "low"},
        "qaqc_required": False,
    },
}


def evaluate(data):
    claimed = data.get("claimed_category")
    if claimed not in CATEGORY_EXPECTATIONS:
        sys.exit(f"Error: 'claimed_category' must be one of {list(CATEGORY_EXPECTATIONS)}, got {claimed!r}.")

    expectations = CATEGORY_EXPECTATIONS[claimed]
    flags = []

    continuity = data.get("geological_continuity")
    if continuity not in expectations["continuity"]:
        flags.append(
            f"Claimed '{claimed}' but geological continuity is reported as '{continuity}', "
            f"which is generally considered insufficient for {claimed} classification. "
            f"A QP/CP would need to justify this explicitly."
        )

    confidence = data.get("geological_model_confidence")
    if confidence not in expectations["geological_model_confidence"]:
        flags.append(
            f"Claimed '{claimed}' but geological model confidence is reported as '{confidence}', "
            f"which is generally considered insufficient for {claimed} classification."
        )

    if expectations["qaqc_required"] and not data.get("qaqc_program", False):
        flags.append(
            f"'{claimed}' classification generally expects a documented QA/QC program "
            f"(standards, blanks, duplicates, independent lab checks); none was indicated here."
        )

    spacing = data.get("avg_drill_spacing_m")
    deposit_type = data.get("deposit_type", "unspecified deposit type")
    if spacing is not None:
        flags.append(
            f"Drill spacing of {spacing}m was given for a {deposit_type} -- appropriate spacing "
            f"for {claimed} classification is deposit-specific (depends on geological continuity "
            f"and variability) and is a QP/CP judgment call, not a fixed number. Don't treat any "
            f"generic spacing rule of thumb as authoritative; ask what spacing precedent exists "
            f"for comparable {deposit_type} deposits."
        )

    return flags


def main():
    parser = argparse.ArgumentParser(description="Run a CRIRSCO-style resource classification sanity checklist.")
    parser.add_argument("input_json", help="Path to JSON file with classification inputs.")
    args = parser.parse_args()

    with open(args.input_json) as f:
        data = json.load(f)

    flags = evaluate(data)

    print(f"Claimed category: {data.get('claimed_category')}")
    print(f"Deposit type: {data.get('deposit_type', 'unspecified')}\n")
    if flags:
        print("Points worth raising with the user / a QP-CP:")
        for i, flag in enumerate(flags, 1):
            print(f"{i}. {flag}")
    else:
        print("No obvious inconsistencies flagged based on the inputs given -- but this checklist "
              "covers common criteria only and is not a substitute for an actual QP/CP review.")

    print(
        "\nReminder: this checklist structures a conversation, it does not certify a classification. "
        "Any public resource statement requires sign-off from an actual Qualified/Competent Person."
    )


if __name__ == "__main__":
    main()
