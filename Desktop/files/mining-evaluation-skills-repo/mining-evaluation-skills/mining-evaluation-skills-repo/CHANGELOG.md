# Changelog

All notable changes to `mining-evaluation-skills` are documented here.

## v1.1 — Metals expansion, regional standards, terminology fixes

**Added — 5 new metal reference files** (`references/metals/`):
- `molybdenum.md` — mostly a porphyry Cu-Mo by-product; standalone porphyry Mo deposits also covered.
- `tungsten.md` — wolframite-focused general tungsten reference (market/strategic context shared with scheelite).
- `scheelite.md` — kept separate from `tungsten.md` because scheelite's skarn setting and flotation-based processing route differ materially from wolframite's typical quartz-vein/gravity-circuit case.
- `zirconium.md` — heavy mineral sands context, co-produced with titanium minerals.
- `titanium.md` — mineral sands (ilmenite/rutile/leucoxene) vs. hard-rock sources, and the rutile/ilmenite value distinction.

**Added — regional reporting standards** (merged into `references/reporting-standards.md` rather than split into separate files):
- Brazil — notes on CRIRSCO-aligned disclosure practice and the absence of a single dedicated Brazilian code; points to whichever home-listing code actually applies.
- Russia — GKZ classification (A/B/C1/C2) described as a standalone, historically independent system. Deliberately does **not** include a GKZ-to-CRIRSCO equivalence table: the mapping is genuinely contested industry-wide, and publishing an approximate conversion risked implying a false equivalence. Any real cross-system reclassification is flagged as requiring actual Qualified/Competent Person review, not a lookup table.
- South Africa — SAMREC code, noted as a close CRIRSCO-family cousin of JORC/NI 43-101, with the practical differences (JSE listing, local Competent Person qualification) called out.

**Added** — `references/terminology-glossary-zh.md`: a Chinese/English terminology reference correcting common mistranslation issues, specifically:
- 边界品位 / 截止品位 / 最低工业品位 — three terms often used interchangeably in Chinese that have distinct technical meanings; the file specifies which one corresponds to the English "cut-off grade."
- 资源量 vs. 储量 (Resource vs. Reserve) — flagged as a legally material distinction, not a stylistic one.
- Standard Chinese terms for Measured/Indicated/Inferred (探明/控制/推断资源量) and Proved/Probable Reserve.
- PEA/PFS/FS naming — specifically flags that Chinese "预可行性" corresponds to PFS, not PEA, a common mistranslation.
- Grade-tonnage curve and sensitivity analysis terminology.

SKILL.md updated to point to the new metal files and to direct Claude to consult the terminology glossary before finalizing Chinese-language responses.

**Not included in this release** (deliberately deferred):
- No metal-specific cost/payability figures were added beyond qualitative ranges — consistent with the skill's existing approach of not asserting numbers the user hasn't supplied.
- No GKZ↔CRIRSCO conversion table — see above.
- No USGS/BGS or other external geological-data integration — out of scope for this release.

## v1.0 — Initial release

- Core evaluation domains: resource estimation, economic feasibility (PEA/PFS/FS), risk assessment, reporting standards (NI 43-101/JORC/CRIRSCO), ESG/sustainability.
- 8 metal reference files: copper, gold, lithium, cobalt, lead-zinc, niobium-tantalum, nickel, rare-earth.
- Scripts: grade-tonnage calculator, financial model (NPV/IRR/payback), resource classification checklist.
- Report templates: resource estimation report, PEA/PFS/FS summary, risk assessment matrix.
