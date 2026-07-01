# Economic Feasibility: PEA / PFS / FS

## The three stages and what confidence each implies

| Stage | Full name | Resource basis | Cost accuracy | Purpose |
|---|---|---|---|---|
| **PEA** | Preliminary Economic Assessment | Can include Inferred Resources | ±35–50% | Conceptual — tests whether a project is worth further spend. Cannot be the basis of a construction decision. Under most CRIRSCO-family codes (e.g., NI 43-101), a PEA must be explicitly labeled as preliminary and must disclose that it includes Inferred material if it does, with a statement that there's no certainty the PEA will be realized. |
| **PFS** | Pre-Feasibility Study | Measured + Indicated only (no Inferred in the economics) | ±20–25% | Selects a preferred development option among alternatives; enough rigor to support continued investment and permitting groundwork. |
| **FS** | Feasibility Study (a.k.a. Definitive/Bankable FS) | Measured + Indicated Reserves converted from Resources | ±10–15% | Investment-grade study used to support project financing and a construction decision. |

When a user shares a study, first identify which stage it claims to be and check whether the resource basis matches — a "PFS" built on mostly Inferred material, or an "FS" without converted Reserves, is a compliance and credibility problem worth flagging immediately.

## Key economic outputs and how to read them

- **NPV (Net Present Value)** — discounted value of the project's free cash flows at a chosen discount rate. Always check: what discount rate was used (mining projects commonly use 5–10% real, higher for higher jurisdictional/technical risk), and is it pre-tax or post-tax (post-tax is the more decision-relevant number, but pre-tax is often quoted alongside it — make sure you know which one you're looking at).
- **IRR (Internal Rate of Return)** — discount rate at which NPV = 0. Compare against the company's hurdle rate/cost of capital, not against IRR in isolation.
- **Payback period** — years to recover initial capex from cash flow; useful risk-communication metric but ignores cash flows after payback, so don't treat it as a standalone investment criterion.
- **CAPEX** — initial (pre-production) vs. sustaining (post-production) capital should be distinguished; a headline capex number that's actually just initial capex, with sustaining capex ignored, understates the real capital intensity.
- **AISC (All-In Sustaining Cost)** — the standard cost-per-ounce/tonne metric used to compare mining operations; includes sustaining capex, so it's more comparable across projects than cash cost alone.

## Sensitivity analysis

A credible feasibility study shows how NPV/IRR move with metal price, capex, opex, exchange rate, and discount rate — usually as a tornado chart or a sensitivity table. When reviewing a study (or building one with `scripts/financial_model.py`), the most useful thing to surface for an investor is: which variable is the project most sensitive to, and how far can that variable move before NPV goes negative? That's often more decision-useful than the base-case NPV alone.

Use `scripts/financial_model.py` when the user supplies concrete cash-flow assumptions (capex schedule, opex per tonne/unit, throughput, metal price, recovery, discount rate, mine life). It computes NPV, IRR, and payback, and can run a simple one-variable sensitivity sweep. If the user hasn't given enough inputs to build a real cash-flow model, don't fabricate assumptions to fill gaps — list what's missing and, if helpful, discuss directionally how the missing variable would move the result.

## Common red flags when reviewing an economic study

- PFS/FS-labeled economics that lean on Inferred Resources.
- No sensitivity analysis, or sensitivity limited only to metal price (ignoring capex/opex risk, which is often the bigger swing factor for development-stage projects).
- Discount rate not disclosed, or unusually low for the jurisdiction/technical risk profile.
- Recovery rate assumptions not backed by metallurgical testwork (especially for PFS/FS — testwork-derived recovery is expected by that stage).
- Capex estimate with a stated accuracy class inconsistent with the claimed study stage (e.g., "FS-level" capex quoted with PEA-level ±40% accuracy).
