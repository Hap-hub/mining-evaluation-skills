# Resource Estimation & Grade-Tonnage Modeling

## Core concepts to get right

**Resource vs. Reserve.** A Mineral Resource is a concentration of material with reasonable prospects for economic extraction, known from geological evidence. A Mineral Reserve is the economically mineable part of a Measured/Indicated Resource, after applying modifying factors (mining, metallurgical, economic, marketing, legal, environmental, social, governmental). Inferred Resources can never be converted directly to Reserves — they must first be upgraded to Indicated or Measured. If a user's numbers treat Inferred material as if it were mineable, that's a red flag worth calling out.

**The CRIRSCO confidence categories:**
- **Measured** — highest confidence; drill/sample spacing close enough that grade continuity is established with high confidence; typically used to support FS-level economics.
- **Indicated** — reasonable confidence in grade continuity; adequate for PFS-level economics; too uncertain to be classed as Measured but geological continuity is reasonably assumed.
- **Inferred** — lowest confidence; inferred from limited sampling; can support PEA-level (conceptual) economics only, and even then must be clearly flagged as non-reserve, speculative material under CRIRSCO-family codes.

Classification is a function of geological confidence (continuity, structural complexity) AND data density (drill spacing, QA/QC), not just a statistical output — it's ultimately a Qualified/Competent Person judgment call, not a formula. When interpreting a user's classification claims, ask: what's the drill spacing relative to the deposit's geological continuity? What QA/QC (assay standards, blanks, duplicates) supports the assay data?

## Grade-tonnage relationships

A grade-tonnage curve shows, for each candidate cut-off grade, the tonnage of material above that cut-off and the average grade of that material. As cut-off rises, tonnage falls and average grade rises — the relationship is inherently inverse, and the *shape* of the curve (how steeply tonnage drops as cut-off rises) tells you how sensitive the resource is to price/cost assumptions.

**Cut-off grade** is the minimum grade at which material is economic to mine and process, given current costs and metal price. It's not fixed — it should be recalculated whenever costs or prices move materially, and different cut-offs are appropriate for open pit (lower, due to lower mining cost) vs. underground (higher, due to higher mining cost) portions of the same deposit.

Basic cut-off grade logic (per tonne):
```
cut-off grade = (mining cost + processing cost + G&A) / (metal price × recovery × payability)
```
This is a simplification — real cut-offs also account for opportunity cost, stockpiling strategy, and marginal vs. breakeven definitions — but it's the right first-order sanity check when reviewing a user's stated cut-off.

Use `scripts/grade_tonnage_calculator.py` when the user provides an actual composite/block dataset (grade + tonnage per sample/block) and wants tonnage-above-cutoff figures or a sensitivity table across several cut-offs. Don't estimate these numbers from a verbal description — they need the underlying data.

## Estimation methods (context for interpretation, not for Claude to perform)

- **Nearest neighbor / polygonal** — simplest, used early-stage; tends to overstate local precision.
- **Inverse distance weighting (IDW)** — weights samples by distance; better than nearest-neighbor but doesn't account for spatial correlation structure.
- **Kriging (ordinary/simple/indicator)** — geostatistical method that models the spatial correlation (variogram) of grades; industry standard for Measured/Indicated categories at PFS/FS level because it also produces an estimate of local/global estimation error.

If a user asks Claude to "run a kriging estimate," be direct that this requires specialized geostatistical software (e.g., Leapfrog, Datamine, Vulcan, GSLIB-based tools) and a proper variogram model built from the actual drill data — it's not something to approximate from a text description. What Claude *can* do well: help interpret existing kriging/variogram outputs, sanity-check whether reported estimation variance is reasonable, and flag common pitfalls (e.g., insufficient composites for a robust variogram, ignoring domain boundaries, smoothing effect underweighting local grade variability).

## Common red flags when reviewing a resource claim

- High-grade intercepts reported without corresponding tonnage/continuity context ("headline grade" without drill spacing).
- Resource statement with no effective date or no stated cut-off grade.
- Inferred-heavy resource base being used to support PFS/FS-level (not PEA-level) economics.
- No mention of QA/QC program (standards, blanks, duplicates, independent lab checks).
- Metal price or recovery assumptions used for cut-off calculation not disclosed.
