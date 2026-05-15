Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper proposes DefNTaxS (Defined Taxonomic Stratification), a training-free framework that uses an LLM to automatically group class labels into semantic subcategories and then integrates both taxonomic context (e.g., "commonly found among kitchen utensils") and class-specific descriptors into CLIP text prompts for zero-shot classification. The method is evaluated on seven standard benchmarks and achieves an average +5.5% gain over vanilla CLIP and +2.4% over D-CLIP, with a particularly striking +13.0% improvement on EuroSAT, all at a total text-generation cost of $0.38.

## Strengths

- **Consistent accuracy gains across diverse benchmarks.** DefNTaxS achieves the highest accuracy on six of seven datasets (Table 1), with average improvements of +5.5% over CLIP and +2.44% over D-CLIP. The gains are especially large on ambiguity-prone datasets (EuroSAT +13.0%, Oxford Pets +8.21%).

- **Fully automated, training-free, and near-zero cost.** The entire pipeline requires no manual prompt engineering, no model retraining, and no additional optimization data. The total API cost for text generation across all datasets is $0.38 (Section 4.2), making the method immediately deployable.

- **LLM-based subcategory discovery outperforms embedding-based clustering.** Section 6.2 (Table 5) directly compares LLM-assigned subcategories against a k-means variant on CLIP text embeddings; the LLM approach yields higher accuracy on every benchmark (mean +0.92%), confirming that semantic understanding of class relationships, not just geometric proximity, drives the improvement.

- **Thorough ablation study.** Section 6 systematically investigates the contribution of each component: reduced taxonomic refinement (Table 2), adding/removing descriptors and subcategories (Table 3), differentiation vs. semantic content via random-character variants (Table 4), and clustering method (Table 5). This provides a nuanced picture of where and why the method works.

- **Strong performance on fine-grained and high-ambiguity datasets.** The large gains on EuroSAT (+9.86% over D-CLIP) and Oxford Pets (+4.25% over D-CLIP) directly validate the method's core motivation: taxonomic context helps disambiguate classes with high visual and semantic overlap.

## Weaknesses

### Fatal

None.

### Major

- **The central claim that taxonomic context is "essential" is contradicted by the paper's own ablation data.** The abstract and conclusion assert that taxonomic context is "not merely helpful but *essential*" for robust zero-shot classification. Yet Table 4 shows that **WaffleTaxS** — which replaces subcategory labels with *random characters* — matches or outperforms the full DefNTaxS on ImageNet (+0.28), Places (+0.71), and CUB (+0.06, within error). The paper acknowledges that "differentiation alone, without semantic content, has an effect" (Section 6.1.3) but never reconciles this with the "essential" framing. This is not a minor overstatement: the results demonstrate that on several datasets, taxonomic *semantics* provide no benefit beyond mere differentiation. The paper's core narrative needs substantial revision to match its evidence.

- **Unexplained discrepancy between headline results and ablation results for EuroSAT, the paper's strongest dataset.** Table 1 reports DefNTaxS on EuroSAT as **57.22%**, while Table 4 (means over 5 iterations) reports **55.99 ± 0.36%** for the identical method and dataset. The paper does not explain whether Table 1 is a single best run, a different random seed, or a different configuration. Since the +13.0% gain over CLIP on EuroSAT is the paper's flagship result (highlighted in the abstract, introduction, and conclusion), this inconsistency makes the primary quantitative claim unverifiable and raises concerns about the reliability of every other number in Table 1.

- **Main results (Table 1) lack any measure of variance.** Every number is a single accuracy value with no standard error or confidence interval. Given that Table 4 shows non-negligible variances on some datasets (e.g., ESAT σ=2.54 for TaxCLIP), it is impossible to assess whether the reported improvements over baselines are statistically significant. The discrepancy between Tables 1 and 4 further underscores the need for variance reporting.

### Minor

- **The "reduced taxonomic refinement" ablation (Table 2) shows DefNTaxS underperforming D-CLIP on both ImageNet and Places.** While the paper discusses this briefly ("lack of differentiation between classes damages the ability of the VLM to distinguish between them"), this result raises the question of how sensitive the method is to the subcategory refinement process, and whether the refinement heuristic (≈20 classes per subcategory) is robust across datasets.

- **The addition of taxonomic *subcategory descriptors* (Table 3, "tax. desc." row) causes a clear performance drop across all datasets.** The paper speculates about CLIP's effective context window but offers no definitive analysis. This limits the reader's understanding of whether the method has reached saturation in semantic content or whether there is a deeper issue with how CLIP processes multi-level taxonomic information.

- **No qualitative analysis of why EuroSAT gains are so large.** The +13.0% over CLIP (9.86% over D-CLIP) on EuroSAT is an outlier compared to the other datasets. The paper offers no confusion matrices, class-wise breakdowns, or qualitative examples to demonstrate that the improvement comes from genuine taxonomic disambiguation rather than spurious correlations or subcategory-label leakage.

### Trivial

- None.

## Nice-to-Haves

- Reporting inference-time cost or runtime alongside the $0.38 text-generation cost would strengthen the practical-viability narrative.
- An explicit baseline using *only* the subcategory name (without D-CLIP-style descriptors) would help isolate the contribution of taxonomic context versus descriptors.
- A sensitivity analysis of the "≈20 classes per subcategory" heuristic would improve methodological clarity.

## Removed Points

- *D-CLIP baseline regeneration concern*: The paper explicitly states (Section 4.1 and Section 4.3) that all baselines were recreated using the same modified pipeline. This criticism is factually incorrect.
- *Missing appendix/implementation details*: Per instructions, these sections exist in the original submission; parser artifacts are not author errors.
- *Formatting/style nitpicks, typos, grammar issues*: Per instructions, these are parser artifacts and not author errors.
- *Missing related work*: Per instructions, I cannot verify the existence of omitted references.
- *Reproducibility nitpicks about undisclosed hyperparameters*: Per instructions, these are typical for conference submissions.

## Novel Insights

None beyond the paper's own contributions. However, the reviewers collectively surface a valuable tension that the paper itself under-explores: the WaffleTaxS results suggest that CLIP-based zero-shot classification benefits primarily from *differentiation* (any distinct token attached to each class) rather than specifically from *semantic* taxonomic context. This echoes findings from WaffleCLIP (Roth et al., 2023) and raises deeper questions about whether VLMs actually process fine-grained semantics or simply benefit from increased token-level discriminability. The paper's attempt to straddle both explanations is its most interesting unresolved thread.

## Suggestions

1. **Reconcile the "essential" claim with the WaffleTaxS evidence.** The paper should either (a) moderate its conclusion to reflect that taxonomic semantics are *helpful but not essential* (since random subcategory labels produce competitive results on several datasets), or (b) provide evidence that distinctiveness deteriorates on datasets where WaffleTaxS fails (e.g., DTD, ESAT, Pets) specifically because semantic content matters.

2. **Explain the EuroSAT discrepancy.** Clarify whether Table 1 reports a single run, the best run, or a different configuration from Table 4. Report variance for the main results in Table 1 (or at minimum for the strongest claims).

3. **Add qualitative analysis for EuroSAT.** Show confusion matrices or class-wise accuracy comparisons between DefNTaxS and D-CLIP on EuroSAT to demonstrate that taxonomic disambiguation is actually happening (e.g., distinguishing "Forest" from "HerbaceousVegetation" via taxonomic context like "natural land cover types") rather than relying on spurious correlations.

## Score and Decision

**Calibration anchors** (all from /home/wg25r/review_agent/human_reviews_2026/):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| I3Ct1eDmVI (PHyCLIP) | 6.50 | Stronger theoretical contribution (hyperbolic embedding) with accepted-level score. This paper has more tangible empirical gains but weaker claims-to-evidence alignment. |
| TQkFiW3AEX (MRAD) | 6.00 | Clean CLIP-based zero-shot method on anomaly detection, accepted. The paper under review has comparable breadth but more significant framing issues. |
| phRRjC0Da6 (BayesCZSL) | 6.00 | Rejected despite high variance in scores. Our paper has more consistent empirical results but suffers from claim-evidence mismatch. |
| hUtTGobe1r (EVA) | 5.00 | Accepted CZSL paper with solid empirical results. Comparable in contribution level, but EVA's claims are better matched to its evidence. |
| QGXVZ0OPLy (DualPrompt) | 5.00 | Accepted CLIP prompt-engineering method. Similar in being training-free and practical, but DualPrompt's claims are more circumspect. |
| AScQDQqVXY (CARPRT) | 4.00 | Accepted with an incremental contribution. Our paper has a more novel method but more serious claim-evidence problems. |
| i0zjotaTnv (Decoupling Perception) | 2.00 | Rejected with fundamental methodological flaws. Our paper is significantly stronger — it has a clear method and reproducible results. |
| IWer3Ciqkp (PG-VLM) | 1.50 | Rejected with severe clarity and evaluation issues. Not comparable in quality to the paper under review. |

Relative to these anchors, the paper under review sits in the 4–5 band. It has a genuinely novel method with strong empirical results that clearly advance the state of the art in zero-shot CLIP prompting. However, the mismatch between its central "essential" claim and its own ablation evidence, combined with the unexplained EuroSAT number discrepancy, prevents it from reaching the acceptance-level scores of papers like PHyCLIP (6.50) or MRAD (6.00). These issues are addressable with revisions to the paper's framing and reporting, but in their current form they substantially weaken the contribution.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>