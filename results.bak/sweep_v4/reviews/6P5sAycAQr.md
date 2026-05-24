## Summary

DefNTaxS proposes a fully automated, training-free framework that uses LLMs to discover taxonomic subcategories among a dataset's classes and integrates this context into CLIP prompts (e.g., "turkey, which has dark wings, and is a species of farm bird"). The method aims to disambiguate semantically similar classes that current descriptor-based and hierarchy-based methods handle poorly. Across seven benchmarks, DefNTaxS achieves an average +5.44% gain over vanilla CLIP and +2.44% over D-CLIP, with the largest gain on EuroSAT (+12.96%).

## Strengths

1. **Well-motivated core idea with clear limitations of prior work** – The paper articulates three specific shortcomings of existing methods (contextual blindness, incomplete disambiguation, semantic isolation) with concrete ambiguous-label examples (e.g., "boxer" as dog breed vs. combat sport). The proposed solution of integrating taxonomic context directly addresses these gaps.

2. **Fully automated, low-cost pipeline** – The method requires no training, no manual prompt engineering, and costs <$0.40 in API calls for all seven datasets (Section 4.2). This is a genuine practical advantage for deployment.

3. **Consistent gains across diverse benchmarks** – Table 1 shows DefNTaxS achieves the highest accuracy on 6 of 7 datasets. The improvement is particularly pronounced on ambiguity-prone datasets like EuroSAT (+12.96% over CLIP) and Oxford Pets (+8.21% over CLIP), supporting the paper's core thesis.

4. **Informative ablation study design** – The paper makes a genuine effort to disentangle factors: comparing taxonomic context alone vs. descriptors alone (Table 3), and comparing LLM-generated subcategories against random character baselines (WaffleTaxS/TaxCLIP, Table 4) and k-means clustering (Table 5). Even when results are mixed, the experimental design is thoughtful.

## Weaknesses

### Fatal

None.

### Major

1. **E-CLIP baseline on EuroSAT is internally inconsistent, undermining confidence in the evaluation protocol** – In Table 1, E-CLIP achieves 33.44% on EuroSAT while vanilla CLIP achieves 44.26%. Since E-CLIP uses an ensemble of 80 hand-crafted prompt templates (as the paper itself states in the Related Work, line 41), it should produce accuracy *at least* as high as plain CLIP's "{class}" format. An 11-percentage-point *drop* is highly aberrant. The paper provides no explanation for this. Because EuroSAT is the dataset where DefNTaxS claims its largest gain (+12.96%), this anomaly directly affects the paper's headline result. It suggests a possible evaluation error (wrong data split, incorrect templates, or preprocessing mismatch) that could affect all baselines on this dataset. At minimum, the authors must explain this discrepancy and verify that the evaluation protocol is correct.

2. **Modified D-CLIP baseline is insufficiently documented** – Section 4.1 states that D-CLIP descriptors were generated via a "modified version of D-CLIP's generation pipeline" because the original GPT-3 API is deprecated. The modifications are not described. If the descriptors differ from the original D-CLIP in quality or quantity, comparisons may not be apples-to-apples. Since one of the paper's main claims is improvement over D-CLIP (average +2.44%), this is a significant documentation gap.

### Minor

1. **Main results lack variance or significance measures** – Table 1 reports single-run accuracy. Given small margins on several benchmarks (e.g., +0.48% over D-CLIP on ImageNet, +0.16% on Places365), these differences could fall within run-to-run variation. Variance is only reported in the ablation (Table 4, 5 iterations). This limits the reader's ability to assess whether claimed improvements are reliable.

2. **Token-length confound is acknowledged but not investigated** – Section 6.1.2 notes that adding taxonomic subcategory descriptors reduces performance, and speculates this may be due to CLIP's effective ~20-token context window (citing Zhang et al., 2024). However, the paper provides no prompt-length statistics, no truncation analysis, and no experiment controlling for token count. The central mechanism — that taxonomic context helps — could partially be confounded by prompt length effects.

3. **Misleading bolding in Table 1** – DefNTaxS entries are bolded on *every* dataset in Table 1, including on Food101 (81.48 vs. CHiLS 83.53) and Places365 (40.00 vs. CHiLS 40.45) where DefNTaxS is *not* the best. The best baseline values (CHiLS) are also bolded. This makes it difficult for a reader to quickly identify the top performer and visually overstates DefNTaxS's dominance. The paper text correctly says "six of seven benchmarks," so this is a presentation issue rather than a factual error, but it should be fixed.

4. **Subcategory count heuristic lacks sensitivity analysis** – The 20-class-per-subcategory heuristic (Section 3.3) is presented as crucial but is not systematically validated. No experiments vary this threshold (e.g., 10, 30, 50 classes per subcategory) to show performance sensitivity.

### Trivial

None.

## Nice-to-Haves

- Report confidence intervals or bootstrapped estimates for the main results in Table 1.
- Include examples of LLM-generated subcategories and context phrases for different datasets (e.g., a table showing actual outputs).
- Analyze prompt length distributions for all prompt variants in the ablation (Table 3) to address the token-limit confound.

## Removed Points

- **"Table 1 boldening is a structural issue with reporting integrity"** — Downgraded from Structural/Fatal to Minor. The paper text accurately states "six of seven benchmarks" where DefNTaxS is best, so the text is not deceptive. The bolding is a presentation issue that should be corrected but does not threaten the paper's core claims.
- **"CLIP on EuroSAT at 44.26% vs Radford et al.'s 55.8%"** — Partially removed as a standalone point and folded into the E-CLIP anomaly (Major weakness #1). The Radford et al. 55.8% figure uses the 80-template ensemble (E-CLIP), not vanilla CLIP, so comparing it to the paper's CLIP "{class}" baseline of 44.26% is not apples-to-apples. However, the internal inconsistency of E-CLIP (33.44%) < CLIP (44.26%) remains the real concern.
- **"Class assignment edge-case handling is vague"** — Removed. The description of the edge-case handling (line 88-89) is a reasonable high-level description for a methodological section; details belong in the appendix (which was stripped by the parser).
- **"The ablation shows taxonomic context without descriptors retains most gains, weakening the core claim"** — Weakened and folded into minor weaknesses. The ablation results are informative and the paper honestly reports them; they show that both components contribute differently across datasets rather than one being unnecessary.
- **Strength Finder strengths about "important problem" and "well-motivated limitation"** — Generic praise; these are subsumed into the first bullet under Strengths.

## Novel Insights

None beyond the paper's own contributions. The two reviews provided do not surface a perspective that the paper itself does not already contain or imply.

## Suggestions

1. **Investigate and explain the EuroSAT E-CLIP anomaly** — Verify whether the evaluation protocol (data split, preprocessing, templates) matches the D-CLIP benchmark exactly. If the single template "a photo of {class}" was used instead of the 80-template ensemble, clarify this and report results with both settings. Resolving this will either strengthen or refute the paper's strongest empirical claim.

2. **Document the modified D-CLIP descriptor generation pipeline** — Describe what changed from the original pipeline and provide evidence that the generated descriptors are of comparable quality (e.g., similarity in descriptor count, correlation with original D-CLIP results on a held-out dataset).

3. **Add variance measures to the main results table** — Report means and standard errors over at least 3 runs for the central comparison (Table 1), or use bootstrapping.

4. **Fix the bolding in Table 1** — Bold only the single best entry per column, or use a convention that clearly distinguishes the proposed method from best-performing baselines.

5. **Include a sensitivity analysis for the subcategory count heuristic** — Vary the target number of classes per subcategory (e.g., 10, 20, 30, 50) on at least 2–3 datasets to validate the 20-class heuristic.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `B2ChNpcEzZ.md` (same paper, earlier cycle) | 4.00 | Same core method; this version has more ablations but identical baseline issues. Score consistent. |
| `2Oiee202rd.md` (PerceptionCLIP) | 6.00 | Similar training-free prompting idea; better evaluation hygiene and clearer baselines. Stronger paper. |
| `WqeRtP2T3R.md` (Embracing Diversity) | 4.67 | Rejected; similar domain and similar concerns about marginal gains and limited novelty. Comparable quality. |
| `5Ca9sSzuDp.md` (CLIP Decomposition) | 8.00 | Significantly stronger contribution with deep analysis and multiple applications. Not comparable. |
| `DPp5GSohht.md` (Unclipping CLIP's Wings) | 4.25 | Rejected; similar pattern of an interesting idea undermined by evaluation concerns. |
| `HfJxXbXlYJ.md` (LLM2CLIP) | 3.00 | Weaker presentation and more overclaimed results. This paper is better. |
| `ZVOGMy8Sd8.md` (Fashion Captioning) | 3.00 | Weaker novelty and outdated baselines. This paper has more current relevance. |
| `t84UBRhhvp.md` (SLR-AVD) | 4.75 | Similar descriptor-based approach with better evaluation hygiene; accepted to a different venue. Slightly stronger. |

The paper proposes a genuinely useful idea with a clean, automated pipeline. However, the unexplained E-CLIP anomaly on EuroSAT (the paper's headline dataset) is a significant evaluation concern that requires resolution before the empirical claims can be trusted. The modified D-CLIP baseline is insufficiently documented. These issues, combined with the lack of variance reporting on small-margin gains, place this below the acceptance threshold despite the strengths of the core idea and ablation design.

**MY FINAL SCORE: <score>4.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**