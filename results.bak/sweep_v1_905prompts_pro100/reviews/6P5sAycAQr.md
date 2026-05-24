Now I have a thorough understanding of the paper. Let me compile the final review.

---

## Summary

DefNTaxS introduces a fully automated, training-free framework that uses an LLM (GPT-4o-mini) to partition dataset classes into semantic subcategories and augment CLIP zero-shot prompts with both per-class descriptors and taxonomic context phrases (e.g., "boxer, which has a muscular build, commonly found among dog breeds"). Evaluated across seven standard benchmarks, DefNTaxS reports an average +5.5% gain over vanilla CLIP and +2.4% over D-CLIP, with the largest single-dataset gain on EuroSAT (+13.0% over CLIP).

## Strengths

- **Well-motivated problem with clear exposition**: The paper identifies a genuine limitation in existing zero-shot prompt methods — lateral semantic relationships among classes are underexploited — and the "boxer" running example (Introduction, Figure 1) makes the disambiguation problem concrete and accessible.

- **Comprehensive and fair baseline comparison**: Eight baselines (E-CLIP, D-CLIP, WaffleCLIP, WaffleCLIP+Conc., CuPL, CGPT-P, CHiLS, and vanilla CLIP) are re-evaluated under a single setup, with all methods using GPT-4o-mini for text generation (Table 1). DefNTaxS achieves the best accuracy on six of seven datasets.

- **Informative ablation of semantic content vs. differentiation**: The WaffleTaxS/TaxCLIP comparison (Table 4, Section 6.1.3) cleanly isolates the roles of taxonomic semantic content and mere class differentiation, showing that both contribute and that DefNTaxS usually achieves the best trade-off. The k-means vs. LLM clustering comparison (Table 5) also provides useful evidence that LLM-based grouping is more effective than embedding-space clustering.

- **Practical and deployable**: The method is fully automated, training-free, and costs under $0.40 total across all datasets (Section 4.2), making it immediately usable with existing CLIP models.

## Weaknesses

### Fatal

None.

### Major

- **The EuroSAT result undermines the central claim about taxonomic context.** Section 3.3 states that for datasets with fewer than 20 classes, "we use the dataset name as the single subcategory context (e.g., 'EuroSAT dataset')." EuroSAT has 10 classes, so no real taxonomic clustering is performed — the "context" is merely the dataset name. Yet Table 1 reports a +9.86% gain over D-CLIP and +12.96% over CLIP on EuroSAT, which is the largest single-dataset improvement in the paper. The paper then claims (Section 5) that this gain shows "taxonomic context helps distinguish land use categories." This is incorrect: on EuroSAT, the gain cannot come from meaningful taxonomic disambiguation. It likely arises from other uncontrolled factors in the prompt structure (different format, connecting phrases, descriptor differences). This single data point disproportionately inflates the mean improvement and weakens the paper's thesis that taxonomic context is "essential." The authors should either (a) explain exactly what drives the EuroSAT gain if not taxonomic context, or (b) redesign the small-dataset protocol so it does not rely on a trivial dataset-name stand-in.

### Minor

- **The "reduced taxonomic refinement" ablation is too vague to interpret.** Section 6.1.1 and Table 2 report results under "reduced taxonomic refinement" but never explain what was changed — fewer subcategories? no refinement? forced single flat category? The text only notes "lack of differentiation between classes" without specifying the experimental manipulation. Since this ablation is central to the claim that refinement matters, the lack of detail prevents the reader from evaluating it.

- **No systematic qualitative examples of generated taxonomies for large datasets.** Figure 1 shows a three-class toy illustration, and scattered phrase examples appear in Section 3.4. But for datasets like ImageNet (1000 classes) and Places (365 classes), the reader cannot judge whether the LLM produces sensible groupings or noisy clusters. The claim of "enhanced semantic interpretability" (Abstract) is asserted without evidence. Including a table of 5–10 representative subcategories and their member classes from ImageNet would substantially strengthen the paper.

- **Ambiguity in baseline prompt regeneration.** Section 4.3 states baselines were "recreated using the setup described in 4.1 and the code provided for each study," and Section 4.1 notes GPT-4o-mini was used. For D-CLIP this is explicit (the pipeline was modified). For CuPL, CGPT-P, and CHiLS — which also use LLM-generated content — it is unclear whether prompts were regenerated with GPT-4o-mini or whether cached prompts from the original papers (using older LLMs) were used. Clarifying this would remove any doubt about whether DefNTaxS benefits from a stronger underlying LLM rather than taxonomic context.

### Trivial

- **"Training split" wording error.** Section 4.1 reports evaluation "on each dataset's standard training split." The CLIP baseline numbers (e.g., 58.89 on ImageNet) match standard validation-set evaluation following D-CLIP's protocol, so this is clearly a typo for "validation split."

- **Overclaim language in places.** Describing the contribution as "a paradigm shift" (Section 7) and taxonomic context as "essential" (Abstract, Section 5) is stronger than the evidence warrants, particularly given the EuroSAT issue.

## Nice-to-Haves

- It would strengthen the paper to generate all baseline prompts from scratch using GPT-4o-mini (if not already done) and document this explicitly, so the comparison is unambiguously controlled for LLM quality.
- Expanding the "reduced taxonomic refinement" ablation to all datasets with a clear description of the manipulation would isolate the effect of the actual taxonomic structure more convincingly.
- An error analysis showing which classes benefit most from taxonomic context, and whether confusion matrices shift in interpretable ways, would add depth.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **HC Point about confounded comparison being "structural" and "fatal."** Removed. The paper does state baselines were recreated under the same setup and D-CLIP was explicitly regenerated with GPT-4o-mini. The remaining ambiguity is a Minor documentation issue, not a fatal confound.

- **HC Point about "evaluation split" potentially invalidating results.** Demoted to Trivial. The reported CLIP numbers match standard validation-set evaluation (e.g., 58.89 on ImageNet matches D-CLIP's protocol), confirming this is a wording error.

- **HC Point about "LLM reliability taken on faith" and "connecting phrases only sketched."** Demoted/removed. The method description is adequate for understanding; detailed prompts are deferred to Appendix A (stripped in this version). This is a presentation preference, not a weakness.

- **HC Point about "context-window discussion deserves more thorough treatment."** Removed. The paper already discusses the 77-token CLIP limit and cites Zhang et al. (2024) on effective context windows (Section 6.1.2). The treatment is adequate.

- **SF strength about "strong empirical evidence for taxonomic context."** Partially qualified. The improvement pattern is real but the EuroSAT result inflates the mean and cannot be attributed to taxonomic disambiguation. The strength is retained with this caveat.

- **SF strength about "ablation validates taxonomic refinement."** Partially qualified. Table 2 is too vague to strongly validate refinement; Tables 4 and 5 provide better evidence. The strength is retained but narrowed.

## Novel Insights

The WaffleTaxS/TaxCLIP comparison (Table 4) provides a genuinely useful methodological insight: substituting taxonomic subcategory labels with random characters (WaffleTaxS) sometimes *outperforms* the full DefNTaxS (ImageNet, Places), while substituting class descriptors with random characters (TaxCLIP) consistently underperforms. This suggests that, analogous to WaffleCLIP's finding about descriptors, the differentiation function of taxonomic labels may matter more than their semantic content in some settings — a nuance the paper acknowledges but could explore more deeply.

## Suggestions

- Redesign the small-dataset protocol for EuroSAT so it does not rely on a trivial dataset-name stand-in, or explicitly report results with and without EuroSAT so readers can assess the contribution of real taxonomic clustering separately.
- For the "reduced taxonomic refinement" ablation, specify exactly what was changed (e.g., number of subcategories, forced flat structure) and report on all datasets, not just ImageNet and Places.

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| B2ChNpcEzZ (earlier DefNTaxS) | 4.00 | R1 | Current version is substantially improved: clearer methodology, full baseline suite, better presentation |
| WqeRtP2T3R (Embracing Diversity) | 4.67 | R1/R2 | DefNTaxS has larger gains, more baselines, and a cleaner story |
| t84UBRhhvp (SLR-AVD) | 4.75 | R1 | Similar scope; DefNTaxS shows larger improvements and is training-free |
| w49jlMWDSA (GIST) | 5.33 | R1/R2 | Comparable quality; GIST has more thorough ablations but requires fine-tuning |
| mLTbDVzHVh (Hierarchical Taxonomies) | 5.25 | R2 | Similar hierarchical theme; DefNTaxS has stronger empirical gains |
| fRpAUgKJhT (CARPRT) | 5.75 | R2 | CARPRT has stronger theoretical grounding; DefNTaxS has larger empirical gains |
| wFs2E5wCw6 (TAP) | 6.40 | R2 | TAP has broader evaluation (11 datasets), learned components, and more rigorous ablations |

**Round 1 bracket:** 4.0–6.0. The paper clearly improves on the earlier 4.00 version and is stronger than the 4.67 "Embracing Diversity" paper, but does not reach the polish and evaluation breadth of the 6.40 TAP paper.

**Round 2 narrowing:** Compared to GIST (5.33), DefNTaxS has comparable empirical strength but weaker ablations and the EuroSAT confound. Compared to CARPRT (5.75), DefNTaxS lacks the theoretical depth but shows larger absolute gains. The paper sits between these, closer to GIST given the EuroSAT issue that weakens the central taxonomic claim.

**Final score justification:** The paper presents a reasonable idea with decent empirical support (consistent gains on 6/7 datasets, useful ablations in Tables 4–5, practical and cheap method). However, the largest reported gain (EuroSAT) cannot be attributed to taxonomic context, which directly weakens the paper's core narrative, and the most important ablation (refinement) is too vaguely described to evaluate. These are fixable issues but they prevent the paper from being clearly above the acceptance threshold. Score: 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>