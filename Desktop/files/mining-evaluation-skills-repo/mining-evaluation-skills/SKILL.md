---
name: mining-evaluation-skills
description: Use for any mining/mineral project evaluation task, including resource estimation, grade-tonnage analysis, economic feasibility (PEA/PFS/FS), geological modeling, cut-off grade sensitivity, risk assessment (geological, technical, market, environmental), or reporting against NI 43-101/JORC/CRIRSCO standards. Trigger when the user is an exploration geologist, mining investor, or analyst asking Claude to interpret drill/assay/geological data, evaluate a mining project's viability, draft or review a technical/investment report on a deposit, compare resource categories (Measured/Indicated/Inferred), estimate NPV/IRR for a mine plan, or discuss copper, gold, lithium, cobalt, lead, zinc, niobium, tantalum, nickel, or rare earths. Also trigger for ESG/sustainability and mining method questions tied to a specific project. Do not trigger for generic investing questions unrelated to mining, or pure geology trivia with no evaluation angle.
---

# Mining Evaluation Skills

## What this skill is for

This skill turns Claude into a working aid for **exploration geologists and mining investors** who need to interpret mineral project data and produce evaluation outputs that hold up against industry-standard frameworks (CRIRSCO-family codes: NI 43-101, JORC, SAMREC, etc.).

The core job is almost always the same shape: the user hands you raw or partially-processed data (assay tables, drill logs, a PEA cash-flow summary, a resource statement, a risk register) and wants either (a) an interpretation of what it means, or (b) a structured report/section built from it. Treat this as **data interpretation first, document generation second** — a sharp reading of the numbers is worth more to these users than a polished template with generic filler.

## Language

Respond in the language the user is writing in (the skill defaults to English internally, but adapt output — including report headers — to match the user's query language). If the user mixes languages or asks for a specific report language, follow that instruction over the query language.

## Step 1: Figure out what's actually being asked

Before producing anything, identify:

1. **Evaluation focus** — which of these is the actual ask (often more than one):
   - Resource estimation / grade-tonnage → `references/resource-estimation.md`
   - Economic feasibility (PEA/PFS/FS) → `references/economic-feasibility.md`
   - Risk assessment → `references/risk-assessment.md`
   - Reporting/compliance (NI 43-101, JORC, CRIRSCO) → `references/reporting-standards.md`
   - ESG / sustainability / mining method choice → `references/esg-sustainability.md`
2. **Commodity** — if the user names or implies a specific metal, check `references/metals/` for a file matching it (copper, gold, lithium, cobalt, lead-zinc, niobium-tantalum, nickel, rare-earth). These give you commodity-specific benchmarks (typical grades, cut-offs, deposit types, processing routes, market drivers) so your interpretation isn't generic. If no specific metal is named, work generically and note that assumptions are commodity-agnostic.
3. **Project stage** — grassroots exploration vs. resource definition vs. PEA vs. PFS/FS vs. operating mine. This changes what data confidence and precision is reasonable to expect (see `references/economic-feasibility.md` for the accuracy bands of each stage).
4. **Audience** — a geologist wants technical precision and defensible methodology language; an investor wants risk-adjusted takeaways and comparability to peers. Calibrate the report's tone and level of jargon accordingly, but never fabricate confidence the data doesn't support — both audiences are worse served by false precision.

## Step 2: Interpret the data

Default mode is interpretation, not computation. Read what the user gives you (tables, CSVs, pasted assay results, cash-flow assumptions, drill spacing descriptions) and explain what it means, what's strong, what's missing, and what a reviewer (a Qualified/Competent Person, or an investor doing diligence) would flag.

**Only reach for a calculation script when the user has actually supplied the underlying data needed to compute something concrete** — e.g., a composite/block table with grades and tonnages, or cash-flow assumptions (capex, opex, price, recovery, discount rate). If the data isn't there, don't fabricate numbers to run a script against — ask for the missing inputs or clearly flag the gap, and give a qualitative read instead. This matters because a wrong or invented number in a mining evaluation report can materially mislead an investor.

Available scripts (see `scripts/README.md` for exact usage):
- `scripts/grade_tonnage_calculator.py` — tonnage/grade above a cut-off, and a cut-off sensitivity table, from a composite/block dataset.
- `scripts/financial_model.py` — NPV, IRR, and payback period from a cash-flow assumption set.
- `scripts/resource_classification_checklist.py` — a structured checklist (not an authoritative classifier) that walks through CRIRSCO-style confidence criteria to flag what supports/undermines a Measured/Indicated/Inferred claim.

Resource classification and geostatistical estimation (kriging, variography) are technical disciplines that legally require a Qualified/Competent Person sign-off — this skill helps interpret and structure, but always note where professional certification would be required for a real filing.

## Step 3: Choose the output format for the scenario

Don't default to one format — match it to what's actually needed:

| Scenario | Format | How |
|---|---|---|
| Quick question, data interpretation, back-and-forth analysis | Markdown, inline in chat | Just respond directly |
| Formal report/section for investors, regulators, or a data room (e.g., "draft the resource estimation section", "write a PEA summary memo") | Word document (.docx) | Use the `docx` skill |
| Numeric model the user will want to manipulate — grade-tonnage curves, NPV/IRR sensitivity tables, resource category rollups | Excel (.xlsx) | Use the `xlsx` skill |
| Slide-style summary for a board/investor pitch | PowerPoint (.pptx) | Use the `pptx` skill |

If it's ambiguous, ask — but a reasonable default is: if the user says "report", "memo", "for investors/regulators", or references a filing standard, go formal (docx/xlsx); otherwise stay conversational.

When producing a formal report, use `assets/templates/` as a structural starting point (see below), not a form to fill mechanically — cut sections that don't apply and add ones the specific project needs.

## Step 4: Reporting standards and templates

`references/reporting-standards.md` covers what NI 43-101, JORC, and CRIRSCO actually require, how they differ, and where they converge (they're all CRIRSCO-family codes). Consult it whenever the user references a standard by name, or when producing anything that resembles a technical report — get the section structure and disclosure language right rather than inventing generic headers.

`assets/templates/` has generic, standards-informed starting structures:
- `resource_estimation_report.md`
- `pea_pfs_fs_summary.md`
- `risk_assessment_matrix.md`

These are public-framework-based skeletons, not copies of any real company's filing — always adapt them to the actual project and flag that a real NI 43-101/JORC filing requires sign-off from a Qualified/Competent Person and full compliance with the code's disclosure rules, which this skill does not substitute for.

## A note on rigor

These outputs get used by people making capital allocation decisions. Where the data is thin, say so plainly rather than smoothing it over — a good risk section or a caveat about resource confidence is more valuable to this audience than an optimistic-sounding paragraph. Flag red flags (e.g., inferred-only resources being used in an FS-level economic case, missing metallurgical recovery data, single-drill-hole grade claims) proactively even if not asked.
