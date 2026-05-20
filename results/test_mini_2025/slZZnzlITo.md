Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces Multimodal Open Set Recognition (MMOSR), a new task extending OSR to multimodal data, and proposes the Multimodal Representation Reactivation Network (MRN) using cross-attention and mixture-of-experts to improve multimodal fusion under OSR constraints. Experiments across four datasets (image-text, audio-visual, RGB-depth) show MRN outperforming several baselines, with the largest OSCR gain of 5.23% on Flower-102.

## Strengths

- **Task formalization.** The paper provides a clear problem definition for MMOSR (Section 3.1), establishing training/testing protocols, evaluation metrics (AUROC, OSCR), and a reproducible benchmark across four diverse multimodal datasets. This fills a genuine gap — existing OSR work is almost entirely single-modal.
- **Consistent improvements across most settings.** MRN (as a standalone fusion method) achieves the best or near-best results on 3 of 4 datasets, with notable gains on Flower-102 (2.47 AUROC, 5.23 OSCR over the best fusion baseline MLA). The ARPL-MRN and CSRR-MRN variants also consistently outperform the corresponding ADD/CAT/GQA variants (Table 2).
- **Ablation validates cross-attention.** Table 4 shows that adding both C1 and C2 cross-attention modules improves AUROC from 89.93→92.16 on Food-101 and 74.28→76.23 on Flower-102, with intermediate gains from single modules. This provides clear evidence that the cross-modal interaction component contributes to performance.
- **Hyperparameter sensitivity analysis.** Figures 4–5 demonstrate that varying expert count (10–20) and selected expert count (2–7) produces only small fluctuations, indicating the method is not brittle to these choices.
- **General-purpose fusion component.** MRN improves both ARPL and CSRR across datasets (Table 2), showing it serves as a reusable fusion module rather than only working with a single OSR head.

## Weaknesses

### Major

- **The central "fusion degradation" claim is substantially overstated relative to the evidence.** The paper asserts in the abstract, introduction, and conclusion that "simply combining OSR and multimodal fusion methods faces the challenge of fusion degradation" as a general finding. The evidence for this is Table 1, which tests only **one** OSR method (OpenAUC) with **one** naive fusion strategy (addition). The paper's own Table 2 then shows that ARPL+ADD achieves 90.45 AUROC on Food-101 and CSRR+ADD achieves 91.41 — both competitive with multimodal fusion methods (MLA: 91.44) and close to the Table 1 "Fusion" baseline (90.48). These results directly undercut the claim that combining OSR with fusion generally causes degradation. The phenomenon exists for OpenAUC+addition but does not generalize to other OSR methods (ARPL, CSRR) or fusion strategies (concatenation). The paper never acknowledges or discusses this inconsistency, which weakens the central motivation.

- **CREMA-D results contradict the "consistently" outperform claim.** MRN's AUROC on CREMA-D (66.78) is *lower* than MLA (67.83), yet the paper bolds MRN as the best in Table 2 and states "MRN consistently demonstrates exceptional MMOSR performance across various datatypes" (line 388). The gain row correctly shows negative deltas (−1.05 AUROC, −0.18 OSCR), but bolding and phrasing it as "consistent" is misleading. This undermines the claim of universal superiority.

- **Unfair comparison with CLIP/CoOp/MaPLe.** In Table 3, MRN is trained from scratch on the known classes, while CLIP is evaluated zero-shot and CoOp/MaPLe are fine-tuned with only 16 shots per class. The paper concludes "MRN outperforms across scenarios" and claims significance "no matter how much data a model has learned" (line 505). These are apples-to-oranges comparisons — a task-specific model trained on in-distribution data should be expected to outperform a zero-shot general-purpose model. A fair comparison would require fine-tuning CLIP on the known classes under the same conditions. The current framing inflates the apparent contribution.

- **No standard deviations or confidence intervals for any reported result.** Several gains in Tables 2 and 3 are very small (e.g., CSRR-MRN over CSRR-CAT on Food-101: 0.26 AUROC; MRN over MLA on SUN RGB-D: 0.37 AUROC). Without error bars, it is impossible to determine whether these improvements are statistically significant or within noise.

### Minor

- **Ambiguity in single-modal baseline application.** The paper does not explicitly state which modality single-modal OSR methods (ARPL, OpenAUC, CSRR, ASH) are applied to in Table 2. The scores (e.g., ARPL at 62.19 AUROC on Food-101, matching Image-OSR in Table 1) suggest image-only, but this is not specified. The paper should clarify this, as different interpretations change how the reader evaluates MRN's contribution.

- **Ablation does not fully isolate the adaptive fusion (MoE) component.** Table 4 compares the full model (C1+C2+adaptive fusion) against variants without one or both cross-attention modules. However, the "no cross-attention" baseline (first row) **still includes adaptive fusion** (per the caption: "the first line refers to the results obtained only with encoders and adaptive fusion"). There is no baseline with only cross-attention and no MoE, making it impossible to attribute improvements to the MoE component individually. The paper also does not test E=1 (single expert) to show the effect of having multiple experts.

- **No diagnostic evidence for the claimed mechanism.** The paper claims that MRN "reactivates suppressed representations" and produces "more comprehensive" representations, but does not directly measure representation compactness, diversity, or feature suppression before and after applying MRN. The evidence is limited to t-SNE visualizations (Figures 2, 6) and Grad-CAM heatmaps (Figure 7), which are qualitative. Quantitative diagnostics (e.g., intra-class variance, singular value spectrum, feature entropy) would strengthen the mechanistic claims.

### Trivial

- The CREMA-D bolding error in Table 2 — MRN is bolded as best despite being outperformed by MLA (67.83 vs 66.78 AUROC). This appears to be a formatting oversight.

## Nice-to-Haves

- Include experiments with E=1 (single expert) to quantify the benefit of multiple experts.
- Vary the threshold setting (currently fixed at 95% known sample recall) to show sensitivity.
- Discuss why MRN underperforms on CREMA-D — the paper currently omits failure case analysis.
- Extend to >2 modalities, since the method is described as extensible.

## Removed Points

- **Criticism that the fusion degradation experiment uses only one OSR method/fusion strategy (Harsh Critic).** This is valid and retained as a Major weakness above — it is not removed.
- **Criticism about missing related work.** Removed per instructions (cannot confirm existence of missing references).
- **Criticism about presentation/style/formtting.** Removed per instructions (parser artifacts).
- **Criticism about missing appendix content/ablation/implementation details.** Removed per instructions.
- **"The paper's own results contradict the degradation narrative" framing.** This is a valid criticism and is retained in the Major section, but softened from the critic's claim of a "structural flaw" — the paper still shows degradation for a specific combination (OpenAUC+add), and the contribution does not entirely depend on the degradation claim being universal.
- **Strength about "empirical demonstration of fusion degradation" from Strength Finder.** Partially valid but conflicts with the retained weakness about overclaiming — the demonstration is limited to one method combination, so it is presented as qualified evidence rather than a standalone strength.
- **Strength about "consistent gains across multiple modality types."** This conflicts with the CREMA-D weakness and is therefore qualified.
- **Generic strengths about "addressing an important problem" (from Strength Finder).** Removed as generic/superficial per instructions.

## Novel Insights

The reviews surface a tension that the paper does not directly address: the "fusion degradation" phenomenon it identifies is method-specific rather than universal. OpenAUC + additive fusion degrades, but ARPL/CSRR + additive fusion does not. This suggests the interaction between OSR regularization type and fusion strategy is the actual research question worth exploring — a systematic study across OSR methods and fusion strategies would be more valuable than a single proposed solution. The paper's framing would benefit from acknowledging this contingency rather than asserting a monolithic challenge.

## Suggestions

1. **Re-frame the motivation.** Rather than claiming "fusion degradation" as a general phenomenon, position the contribution as: multimodal OSR is challenging because different OSR methods interact differently with multimodal fusion; MRN is a fusion architecture robust to this variation. This would honestly represent the evidence in Tables 1 and 2.
2. **Fix the CREMA-D presentation.** Either remove the bolding on metrics where MRN is not best, or add a discussion explaining why MRN underperforms MLA on this dataset.
3. **Add standard deviations** across at least 3 random seeds for the main results (Table 2, Table 3). With gains as small as 0.26 AUROC, significance is essential.
4. **Either fine-tune CLIP/CoOp/MaPLe properly or move that comparison to the appendix** with a clear caveat that these are reference points, not controlled baselines.
5. **Add an ablation with MoE alone (C1/C2 removed) vs cross-attention alone (MoE removed)** to isolate each component's contribution.
6. **Add quantitative diagnostic measures** (e.g., feature diversity, intra-class variance) to support the claim that MRN actually produces less compact/more diverse representations.

## Score and Decision

**Initial bracket from Round 1:** Papers in this space (multimodal + OSR/OOD) typically score from ~2–3 (weak/rejected) to ~8 (strong accepted). The paper's topic similarity aligns most closely with middle-band papers scoring 4–6.

**Narrowing from Round 2:** I examined 7 anchor papers spanning the bracket. The paper is stronger than "Open-Set Domain Adaptation Under Background Distribution Shift" (avg 4.6, rejected) — the current paper has broader experimental evaluation and a clearer task definition. It is weaker than "Modulated Phase Diffusor" (avg 5.0, accepted poster) — that paper had a more novel technical contribution despite limited theoretical depth. It is substantially weaker than "Test-time Adaptation against Multi-modal Reliability Bias" (avg 8.0, accepted) — that paper had a clean problem statement, rigorous evaluation, and well-supported claims. The paper is comparable to "Style-Coherent Multi-Modality Image Fusion" (avg 5.5, rejected) — both have reasonable methods but suffer from overclaiming, unclear details, and evaluation gaps.

The overclaiming of "fusion degradation" and the CREMA-D inconsistency are the deciding factors. These are not fatal to the paper's core contribution (the MMOSR task is valuable), but they are significant enough in the current framing that the paper does not meet the bar for a top venue.

**Anchor table:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| OSF in Multimodal Learning | /home/wg25r/review_agent/human_reviews/XuNkuoihgG.md | 3.00 | 1 | Lower quality, less experimental breadth |
| MIMOSA | /home/wg25r/review_agent/human_reviews/uffmkDtlR2.md | 2.60 | 1 | Less empirical substance |
| OmniBind | /home/wg25r/review_agent/human_reviews/l2izo0z7gu.md | 6.25 | 1 | Stronger — more thorough evaluation, clearer contribution |
| X-Fi | /home/wg25r/review_agent/human_reviews/b42wmsdwmB.md | 6.40 | 1 | Stronger — cleaner problem framing, better supported claims |
| VisionFuse | /home/wg25r/review_agent/human_reviews/2jEiFTLRwX.md | 5.00 | 1 | Similar quality — reasonable idea, evaluation gaps |
| Style-Coherent MMIF | /home/wg25r/review_agent/human_reviews/1waeKNeQzG.md | 5.50 | 1 | Similar — overclaiming and unclear details |
| Test-time Adapt (READ) | /home/wg25r/review_agent/human_reviews/TPZRq4FALB.md | 8.00 | 1 | Much stronger — rigorous evaluation, well-supported |
| NegLabel | /home/wg25r/review_agent/human_reviews/xUO1HXz4an.md | 7.50 | 2 | Much stronger — clean problem framing, theoretical grounding |
| HamOS | /home/wg25r/review_agent/human_reviews/N6ba2xsmds.md | 6.75 | 2 | Stronger — innovative method, more rigorous evaluation |
| Open-Set Domain Adapt | /home/wg25r/review_agent/human_reviews/Yd2GeHRSlJ.md | 4.60 | 2 | Slightly weaker — narrower evaluation, but stronger theory |
| Modulated Phase Diffusor | /home/wg25r/review_agent/human_reviews/gHAr7ZA1OL.md | 5.00 | 2 | Similar — accepted but with limitations |

**Final assessment:** The paper has a genuine contribution in defining the MMOSR task and providing a reasonably comprehensive evaluation framework. However, the overclaiming of "fusion degradation" as a general phenomenon (when evidence shows it is method-specific), the misleading CREMA-D presentation, the unfair CLIP comparison, and the lack of statistical rigor for small gains are significant issues. The paper is below the acceptance threshold for a top venue in its current form but could be viable after substantial revision.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>