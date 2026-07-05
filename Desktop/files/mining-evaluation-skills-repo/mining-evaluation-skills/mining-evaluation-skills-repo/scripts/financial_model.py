#!/usr/bin/env python3
"""
Simple mine economics calculator: NPV, IRR, payback period, and an optional
one-variable sensitivity sweep.

Only use this when the user has supplied concrete cash-flow assumptions.
Do not invent capex/opex/price/recovery figures to make this script runnable --
if inputs are missing, ask the user for them instead.

Input: a JSON file describing the project, e.g.:

{
  "initial_capex": 500000000,
  "discount_rate": 0.08,
  "years": [
    {"year": 1, "revenue": 0,         "opex": 0,          "sustaining_capex": 0},
    {"year": 2, "revenue": 180000000, "opex": 90000000,   "sustaining_capex": 10000000},
    {"year": 3, "revenue": 200000000, "opex": 95000000,   "sustaining_capex": 5000000}
  ]
}

Usage:
    python financial_model.py <input.json> [--sensitivity revenue --range -0.2,-0.1,0,0.1,0.2]

The sensitivity flag re-runs NPV/IRR while scaling the named field (revenue, opex,
initial_capex, or sustaining_capex) by each multiplier in --range (as fractional
deltas, e.g. -0.2 = -20%).
"""
import argparse
import json
import sys


def npv(discount_rate, cash_flows):
    """cash_flows[0] is year 0 (typically -initial_capex), cash_flows[1] is year 1, etc."""
    return sum(cf / ((1 + discount_rate) ** t) for t, cf in enumerate(cash_flows))


def irr(cash_flows, guess=0.1, tol=1e-6, max_iter=1000):
    """Newton's method IRR solver with a bisection fallback."""
    rate = guess
    for _ in range(max_iter):
        value = sum(cf / ((1 + rate) ** t) for t, cf in enumerate(cash_flows))
        deriv = sum(-t * cf / ((1 + rate) ** (t + 1)) for t, cf in enumerate(cash_flows))
        if abs(deriv) < 1e-12:
            break
        new_rate = rate - value / deriv
        if abs(new_rate - rate) < tol:
            return new_rate
        rate = new_rate
        if rate <= -0.999:
            rate = -0.99  # keep it in a sane domain

    # Fallback: bisection over a wide range
    lo, hi = -0.99, 10.0
    f_lo = sum(cf / ((1 + lo) ** t) for t, cf in enumerate(cash_flows))
    f_hi = sum(cf / ((1 + hi) ** t) for t, cf in enumerate(cash_flows))
    if f_lo * f_hi > 0:
        return None  # no sign change; IRR not found in range
    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = sum(cf / ((1 + mid) ** t) for t, cf in enumerate(cash_flows))
        if abs(f_mid) < tol:
            return mid
        if f_lo * f_mid < 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
    return mid


def payback_period(cash_flows):
    """Simple (undiscounted) payback in years, with linear interpolation within the payback year."""
    cumulative = 0
    for t, cf in enumerate(cash_flows):
        prev_cumulative = cumulative
        cumulative += cf
        if cumulative >= 0 and prev_cumulative < 0:
            fraction = -prev_cumulative / cf if cf != 0 else 0
            return t - 1 + fraction
    return None  # never pays back within the given horizon


def build_cash_flows(data, scale_field=None, scale_delta=0.0):
    initial_capex = data["initial_capex"] * (
        1 + scale_delta if scale_field == "initial_capex" else 1
    )
    flows = [-initial_capex]
    for y in data["years"]:
        revenue = y.get("revenue", 0) * (1 + scale_delta if scale_field == "revenue" else 1)
        opex = y.get("opex", 0) * (1 + scale_delta if scale_field == "opex" else 1)
        sustaining = y.get("sustaining_capex", 0) * (
            1 + scale_delta if scale_field == "sustaining_capex" else 1
        )
        flows.append(revenue - opex - sustaining)
    return flows


def main():
    parser = argparse.ArgumentParser(description="Compute NPV, IRR, and payback for a mine cash-flow model.")
    parser.add_argument("input_json", help="Path to JSON file with project cash-flow assumptions.")
    parser.add_argument(
        "--sensitivity",
        choices=["revenue", "opex", "initial_capex", "sustaining_capex"],
        help="Optional: run a one-variable sensitivity sweep on this field.",
    )
    parser.add_argument(
        "--range",
        default="-0.2,-0.1,0,0.1,0.2",
        help="Comma-separated fractional deltas for sensitivity (default: -0.2,-0.1,0,0.1,0.2).",
    )
    args = parser.parse_args()

    with open(args.input_json) as f:
        data = json.load(f)

    if "initial_capex" not in data or "years" not in data or "discount_rate" not in data:
        sys.exit("Error: input JSON must include 'initial_capex', 'discount_rate', and 'years'.")

    discount_rate = data["discount_rate"]
    base_flows = build_cash_flows(data)

    base_npv = npv(discount_rate, base_flows)
    base_irr = irr(base_flows)
    base_payback = payback_period(base_flows)

    print("=== Base case ===")
    print(f"Discount rate: {discount_rate:.1%}")
    print(f"NPV: {base_npv:,.0f}")
    print(f"IRR: {base_irr:.1%}" if base_irr is not None else "IRR: could not be solved (check cash flow signs)")
    print(f"Payback: {base_payback:.2f} years" if base_payback is not None else "Payback: not achieved within the horizon given")

    if args.sensitivity:
        deltas = [float(d.strip()) for d in args.range.split(",")]
        print(f"\n=== Sensitivity on '{args.sensitivity}' ===")
        print("| Delta | NPV | IRR |")
        print("|---|---|---|")
        for delta in deltas:
            flows = build_cash_flows(data, scale_field=args.sensitivity, scale_delta=delta)
            n = npv(discount_rate, flows)
            r = irr(flows)
            r_str = f"{r:.1%}" if r is not None else "n/a"
            print(f"| {delta:+.0%} | {n:,.0f} | {r_str} |")

    print(
        "\nNote: this is a simplified single-currency, pre/post-tax-agnostic model based only on "
        "the inputs given. Confirm with the user whether figures are pre-tax or post-tax, real or "
        "nominal, and in what currency, before presenting results as decision-ready."
    )


if __name__ == "__main__":
    main()
