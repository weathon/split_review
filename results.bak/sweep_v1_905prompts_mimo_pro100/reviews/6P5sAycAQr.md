Now I have enough data. Let me write the final review.

## Summary

This paper introduces DefNTaxS (Defined Taxonomic Stratification), a training-free framework that uses LLMs to discover taxonomic subcategories among classes and integrates this context into CLIP prompts for zero-shot image classification. Evaluated across seven standard benchmarks with ViT-B/32, DefNTaxS achieves gains of up to +12.96% over vanilla CLIP and +9.86% over the D-CLIP baseline, with extensive ablations decomposing the contributions of descriptors, taxonomic context, and their combination.

## Strengths

- **Well-controlled, comprehensive evaluation against strong baselines.** Table 1 compares against eight baselines (CLIP, E-CLIP, D-CLIP, W-CLIP, W-CLIP+conc., CuPL, CGPT-P, CHiLS), all re-implemented under identical hardware/software conditions on a single RTX 4090 (Section 4.3). This is a meaningful improvement over the prior version of this paper, which lacked several of these baselines.

- **Systematic ablations isolating the contribution of each component.** Tables 3–5 provide informative decompositions: Table 3 separates class descriptors from taxonomic context; Table 4 uses WaffleTaxS/TaxCLIP (random-character substitutions) to isolate semantic content from structural differentiation; Table 5 compares LLM-based vs. k-means clustering. These ablations are genuinely informative about the method's mechanism.

- **Extremely low computational cost.** Total text generation cost is $0.38 across all datasets and experiments (Section 4.1), making the method immediately deployable without model modification or training.

- **Consistent wins on 5 of 7 benchmarks.** DefNTaxS achieves the highest accuracy on ImageNet, CUB, Pets, DTD, and EuroSAT, demonstrating broad applicability across fine-grained, texture, satellite, and general object domains.

## Weaknesses

### Fatal
None

### Major

- **Factual error in the headline claim: DefNTaxS wins 5 of 7 benchmarks, not 6.** The paper states "Table 1 shows DefNTaxS achieving the highest accuracy across six of seven benchmarks" (Section 5). Reading Table 1: on Food101, CHILS scores 83.53 vs. DefNTaxS 81.48; on Places365, CHILS scores 40.45 vs. DefNTaxS 40.00. Both are clear losses. This is a material misreporting of the paper's core empirical contribution.

- **The "disambiguation" framing is asserted but never experimentally validated.** The paper's central motivation is resolving label ambiguity (e.g., "boxer" as dog vs. sport, "crane" as bird vs. equipment). However, none of the seven benchmarks tested contain such ambiguous classes — these are curated datasets with well-differentiated classes. The paper never quantifies how many classes are ambiguous in any benchmark, nor demonstrates that improvements concentrate on ambiguous classes. The method may instead be working through general prompt enrichment and inter-class differentiation rather than disambiguation specifically, and the ablation in Table 3 (removing descriptors barely hurts) partially supports this alternative explanation.

- **No variance or significance testing in the main results table.** Table 1 reports single-point accuracy without any error bars. Table 4 in the ablation section shows standard errors over 5 runs, with values on the order of 0.1–0.8 on most benchmarks but up to 2.54 on EuroSAT. Given that several gains over D-CLIP are tiny (Places: +0.16, ImageNet: +0.48, CUB: +0.79), these improvements may fall within noise. The authors have the infrastructure to report this (they do so in Table 4) but chose not to for the main comparison.

- **The +13.0% headline gain is driven by an anomalous dataset.** EuroSAT shows the largest improvement, but baselines behave anomalously there: E-CLIP drops from 44.26 (vanilla CLIP) to 33.44, and W-CLIP drops to 31.49 — simple prompt engineering *hurts* on this dataset, suggesting dataset-specific sensitivity to prompt formatting rather than taxonomic understanding. Excluding EuroSAT, the average gain over vanilla CLIP drops from +5.44% to approximately +4.3%, and the gain over D-CLIP drops from +2.44% to approximately +1.5%.

### Minor

- **The "no descriptors" ablation (Table 3) undermines the combined approach.** Removing all class-level descriptors and keeping only taxonomic context produces near-identical performance: Food 81.35 vs. 81.26 (slightly *better*), CUB 53.76 vs. 54.00, DTD 44.49 vs. 45.89. If taxonomic context alone achieves most of the gain, the paper's value proposition shifts substantially. The paper acknowledges this briefly but does not adequately investigate why descriptors are largely dispensable.

- **Incorrect explanation for k-means vs. LLM performance difference.** Section 6.2 states "we expect this is due to the high dimensional embedding space of the CLIP backbones, which allows for better separation of the subcategory labels, where a small, simple k-means approach would struggle to differentiate between the classes." This is incorrect — k-means has no inherent difficulty in high dimensions. The actual interesting difference (LLM-generated semantic subcategory names vs. numeric cluster indices) is not discussed.

- **EuroSAT improvement mechanism is speculative.** The paper attributes EuroSAT's +12.96% gain to "taxonomic context helps distinguish land use categories that share visual similarities but differ in satellite imagery context" (Section 5), but provides no evidence that this is the actual mechanism.

- **Only ViT-B/32 is evaluated.** Prompt engineering effects can vary substantially across model scales, so results on at least one additional backbone (e.g., ViT-L/14) would substantially strengthen the generality of the claims.

- **LLM prompts not shown in main paper.** For a method that is entirely prompt-driven, the actual prompts used for subcategory generation, class assignment, and refinement are never shown in the main text. While presumably in an appendix, reproducibility would be strengthened by including at least the core prompt templates.

### Trivial
None

## Nice-to-Haves
- Design an experiment directly testing the disambiguation thesis: construct a dataset subset with genuinely ambiguous classes and show that DefNTaxS's improvement concentrates there.
- Investigate and embrace the "no descriptors" result as potentially a cleaner, more interesting finding.
- Report ImageNetV2 results discussion (the INV2 column appears in Table 1 but is not mentioned in the datasets section).

## Removed Points
These points are flagged to be removed, treat them with caution:
- Formatting artifacts, typos, or parser issues — not author errors.
- Missing appendix content (proofs, prompts, etc.) — stripped by the parser, exist in original submission.
- Criticisms questioning the existence or release status of cited models, benchmarks, or references.

## Novel Insights

The ablation showing that taxonomic context alone (without class-level descriptors) achieves most of the improvement is a genuinely interesting finding that the paper does not fully capitalize on. This suggests the core contribution is the subcategory/clustering structure itself, not the descriptor-augmented prompts. If reframed around this insight, the paper's story would be cleaner and more novel — taxonomic context as a distinct signal for inter-class differentiation, independent of fine-grained descriptors.

## Suggestions
1. Correct the win count from "six" to "five" throughout the paper and temper the abstract's framing.
2. Report Table 1 with mean ± standard error across multiple runs, as already done in Table 4.
3. Reframe the contribution around the finding that taxonomic context is the primary driver, with descriptors playing a secondary role. This is cleaner and more interesting than the current combined-system framing.
4. Add at least one additional backbone (e.g., ViT-L/14) to strengthen generalizability claims.
5. Either validate the disambiguation thesis experimentally or reframe the motivation away from "disambiguation" toward "taxonomic context as inter-class differentiation."

## Anchor Comparison Report

**Round 1 (bracketing):**
| Anchor ID | Topic | Avg Score | Round | Comparison |
|-----------|-------|-----------|-------|------------|
| FwkYeLovHk | Weak-to-strong CLIP | 3.33 | 1 | Weaker — narrower scope, fewer datasets |
| B2ChNpcEzZ | **Previous version of this paper** | 4.00 | 1 | Prior version — this revision is stronger with more baselines and better presentation |
| WqeRtP2T3R | Zero-shot CLIP diversity | 4.67 | 1 | Similar — LLM-augmented zero-shot, marginal gains, similar concerns |
| mLTbDVzHVh | Hierarchical taxonomy CL | 5.25 | 1 | Similar — taxonomy + learning, better writing but different setting |
| AhMEkBSdIV | LCA taxonomies OOD | 5.33 | 1 | Stronger — clearer novelty with LCA metric, more impactful contribution |

**Round 2 (narrowing):**
| Anchor ID | Topic | Avg Score | Round | Comparison |
|-----------|-------|-----------|-------|------------|
| t84UBRhhvp | LLM descriptors zero-shot | 4.75 | 2 | Similar — LLM descriptor augmentation, marginal gains, similar issues |
| w49jlMWDSA | GIST fine-grained descriptors | 5.33 | 2 | Similar — LLM descriptors for classification, image-specific though |
| UyBMzsFThf | CLIP pairwise differences | 5.25 | 2 | Similar — CLIP embedding structure, different approach |
| usrChqw6yK | LLMs + VLMs open-vocab detection | 6.00 | 2 | This paper is weaker — DVDet has clearer gains, more robust evaluation |
| NDLmZZWATc | DeMul description-free prompting | 6.40 | 2 | This paper is weaker — DeMul addresses reliability more cleanly |

**Round 1 bracket: 4.0–5.5.** The previous version scored 4.0, and the paper sits clearly above it due to improved baselines and presentation, but below the 5.25–5.33 range anchors due to the factual error, missing variance, and framing concerns.

**Round 2 narrowing: 4.5–5.5.** Compared to the 4.75 anchor (similar topic, similar marginal gains), DefNTaxS has a more comprehensive evaluation but also more significant overclaiming. Compared to the 5.25–5.33 anchors, it has less clear novelty. The paper sits around 5.0: below the 5.25 anchors (which have cleaner contributions) but above the previous version at 4.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>