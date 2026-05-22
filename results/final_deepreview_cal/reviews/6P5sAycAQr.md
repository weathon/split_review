## Summary

DefNTaxS introduces a fully automated, training-free framework that uses LLMs to discover taxonomic subcategories among classes and integrates this context into CLIP prompts for zero-shot image classification. On seven standard benchmarks, it achieves the best average accuracy (61.17%), with a 5.5% average gain over vanilla CLIP and a notable 13.0% absolute gain on EuroSAT. The paper includes thorough ablation studies comparing random-character baselines (WaffleTaxS/TaxCLIP), LLM vs. k-means clustering, and varying descriptor configurations.

## Strengths

- **Comprehensive and automated pipeline**: The method requires no manual prompt engineering, no model retraining, and costs only $0.38 in LLM API fees across all seven datasets (Section 4.2). This practical deployability is a genuine strength.

- **Strong empirical coverage**: The evaluation spans seven diverse benchmarks (ImageNet, CUB, Pets, DTD, Food-101, Places365, EuroSAT) plus ImageNetV2, covering fine-grained recognition, texture, scene, and satellite imagery. DefNTaxS achieves the highest mean accuracy (61.17%) and wins on 6 of 8 metrics (Table 1).

- **Informative ablation design**: The paper proactively investigates the role of semantic content by comparing against WaffleTaxS (random subcategory labels) and TaxCLIP (random descriptors) in Table 4, and tests reduced taxonomic refinement (Table 2) and descriptor variants (Table 3). This goes beyond what most prompt-engineering papers provide.

- **Cost-aware methodology**: Generating all text across all datasets for under $0.40 (Section 4.2) makes the approach accessible and reproducible.

## Weaknesses

### Major

- **Central claim is not well-supported by the ablation evidence**: The paper asserts that *semantic* taxonomic context is "essential" (Abstract, Section 1, Section 7). However, Table 4 shows that WaffleTaxS (random characters replacing subcategory labels) outperforms DefNTaxS on 3 of 7 datasets (ImageNet: +0.28, CUB: +0.06, Places: +0.71) and is within 0.2 pp on a fourth (Food). The paper acknowledges "differentiation alone has an effect" (Section 6.1.3) but does not reconcile this with the strong "essential" framing. The evidence is more consistent with an incremental, partially-semantic benefit rather than the claimed fundamental necessity. Either the claim should be tempered or a control experiment that isolates the effect of semantic content from differentiation should be provided.

### Minor

- **Results slightly overstated**: The paper claims "consistent improvement over other recent SOTA" and "establishing new state-of-the-art results" (Abstract, Section 1). Table 1 shows CHiLS outperforms DefNTaxS on Food-101 (83.53 vs. 81.48) and Places365 (40.45 vs. 40.00). "SOTA on most benchmarks" is accurate; "consistent SOTA" is not. The phrasing should be adjusted to match the evidence.

- **Headline results lack error bars**: Table 1 reports single accuracy values with no variance. Given that many margins over baselines are small (e.g., +0.48 pp over D-CLIP on ImageNet), the reader cannot assess statistical reliability. The ablation section (Table 4) does provide standard errors over 5 runs, so this standard should extend to the main results.

- **Motivation–evaluation disconnect**: The opening examples (boxer/crane/mouse homonyms, Section 1) motivate the method via cross-domain ambiguity, but the evaluation is entirely on standard single-domain benchmarks where this type of label ambiguity does not arise (no dataset contains both "boxer the dog" and "boxer the sport"). The paper would be stronger if it included a targeted test of genuine homonym resolution, or if it reframed its motivation around fine-grained inter-class confusion (which the benchmarks do contain).

### Trivial

- **"Reasonable margin" (Section 5)**: On Food-101, the gap between DefNTaxS (81.48) and the third-place CGPT-P (80.98) is 0.5 pp — not a "reasonable margin" by most standards. Minor phrasing imprecision.

## Nice-to-Haves

- **Analysis of the EuroSAT outlier**: DefNTaxS gains +13.0% absolute over CLIP on EuroSAT, far more than on any other dataset. A brief analysis of why taxonomic context helps so dramatically here (low class count? high inter-class visual similarity? satellite domain characteristics?) would strengthen the paper.
- **Error bars on main results (Table 1)**, even if computed over a smaller number of runs.
- A test on a constructed ambiguity-prone dataset (mixing homonym classes from different domains) would directly validate the motivating scenario.

## Removed Points

These points were flagged in reviewer input but are removed after verification against the paper:

1. *"D-CLIP reproduction confound — comparison may reflect LLM choice"*: The paper states (Section 4.1) that GPT-3 API was deprecated, so all baselines were recreated with GPT-4o-mini using original code. All methods use the same LLM; this is transparent and properly controlled.
2. *"'20 classes per subcategory' justification deferred to appendix"*: The appendix exists in the original submission; the parser stripped it. This is not an author error.
3. *"k-means comparison is unsurprising since LLM generates names"*: This is a methodological opinion, not a concrete flaw. The comparison shows LLM clustering is more effective, which is a valid empirical finding.
4. *Missing related works*: Cannot be verified without external sources; not included.
5. *Formatting/typo nitpicks*: Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Temper the central claim from "taxonomic context is *essential*" to "taxonomic context provides meaningful improvement" and acknowledge that some gains come from differentiation rather than semantics alone.
2. Add error bars or confidence intervals to Table 1.
3. Construct a small homonym test set (e.g., repurposing classes from domain-specific datasets where labels overlap) to directly validate the motivating scenario.
4. Include a brief analysis of why EuroSAT benefits so disproportionately.

## Score and Decision

**Calibration Report:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| B2ChNpcEzZ (same paper, earlier version) | 4.00 | R1 | Current version is improved (more baselines, better ablations) but retains core weaknesses → above 4.00 |
| t84UBRhhvp (Text Descriptions as Representations) | 4.75 | R1 | Similar LLM-augmented CLIP method; this paper has more thorough evaluation → comparable or slightly above |
| WqeRtP2T3R (Embracing Diversity) | 4.67 | R2 | Similar idea (LLM subclasses for CLIP); reviewers noted "performance improvement is far from substantial" — similar critique applies here → comparable at 4.67–5.0 |
| fRpAUgKJhT (CARPRT) | 5.75 | R2 | Cleaner central claim, well-supported; DefNTaxS is weaker on claim-evidence alignment → below 5.75 |
| w49jlMWDSA (GIST) | 5.33 | R2 | Similar LLM-for-CLIP paper with questioned novelty; DefNTaxS has more comprehensive ablations → comparable around 5.0–5.3 |

**Bracket (Round 1):** 4.0–6.0. The earlier version of this same paper scored 4.00; the current version is improved but retains structural weaknesses.

**Narrowing (Round 2):** Comparing against CARPRT (5.75) and GIST (5.33), DefNTaxS's core claim-evidence mismatch (WaffleTaxS partially contradicts the "essential" framing) is a structural weakness that the cleaner contributions of CARPRT do not share. Against the 4.67 anchor, the current paper has stronger evaluation. The paper sits near the lower middle of the band.

**Final:** 5.0

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>