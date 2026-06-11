Now I'll write the final consolidated review.

## Summary

This paper proposes CCAT, a two-stage framework for mitigating modality imbalance in multimodal learning. Stage 1 pretrains a shared classifier with bidirectional cross-attention and a contribution-disparity regularization term. Stage 2 freezes this classifier as a stable decision anchor during modality-alternating training, using per-modality LoRA adapters to handle feature distribution mismatch and sample-level secondary updates for severely imbalanced samples. Experiments on CREMA-D, Kinetic-Sound, and MVSA show consistent improvements over prior methods.

## Strengths

1. **Ablation cleanly isolates the frozen-classifier contribution (Table 2).** On CREMA-D, removing classifier freezing drops multimodal accuracy from 85.89% to 82.80% (−3.09%), while keeping all other components. This directly validates the paper's core claim that classifier-level bias is a separate, addressable bottleneck beyond the encoder-level interference already targeted by alternating training.

2. **Substantial unimodal gains on weaker modalities (Table 1).** CCAT raises CREMA-D Video accuracy from MLA's 68.01% to 73.79% (+5.78%) and Kinetic-Sound Audio from MMPareto's 56.40% to 61.65% (+5.25%). These unimodal improvements are stronger evidence of genuine imbalance mitigation than fusion-accuracy gains alone, because they show the weaker modality's representation quality has improved independently.

3. **Complementary clustering metrics (Figure 5).** Beyond accuracy, CCAT achieves higher Calinski-Harabasz (242.55 vs. 198.98/200.01), Silhouette (0.24 vs. 0.19/0.20), and lower Davies-Bouldin (1.28 vs. 1.42/1.46) scores on t-SNE projections, providing converging evidence that the frozen-classifier strategy yields more discriminative feature representations.

4. **LoRA addresses a principled distribution-mismatch problem.** The paper identifies that a frozen classifier trained on fused features must now process unimodal features, creating a distribution mismatch P(z^m|y) ≠ P(f|y). Attaching modality-specific LoRA modules as low-rank residual corrections (Eq. 9–10) directly addresses this, and the ablation (LoRA=✗ row, −1.21% on CREMA-D) confirms the practical value.

## Weaknesses

### Major

1. **Factual inconsistency in the abstract's headline quantitative claim.** The abstract states CCAT achieves "+1.35% on CREMA-D over state-of-the-art methods," but Table 1 shows the best prior SOTA (LFM) at 83.62% and CCAT at 85.89% — a +2.27% gain. The +6.76% (KS) and +1.92% (MVSA) numbers in the abstract correctly match Table 1, so CREMA-D is the sole discrepancy. This is a verifiable factual error in the paper's most prominent result sentence. The authors must correct and explain which number is correct.

2. **MVSA unimodal Image accuracy under CCAT is lower than under MMPareto (Table 1).** CCAT achieves 55.30% Image accuracy vs. MMPareto's 59.54%, even though CCAT's multimodal result (80.73%) is higher. The paper's central framing is about "liberating weaker modalities," yet on MVSA the weaker modality performs worse under CCAT than under a prior method. This pattern is not discussed and undercuts the balancing narrative. The authors should address whether this reflects a trade-off between unimodal representation quality and multimodal fusion robustness.

### Minor

3. **No variance or confidence intervals reported.** The paper states "average test accuracy of three random seeds" (Table 1 caption) but provides no standard deviations. Several gains are modest (+1.92% on MVSA), and without variance estimates the reader cannot assess statistical reliability. This is a standard expectation for experimental work at this venue.

4. **The β threshold for sample-level updates requires dataset-specific tuning without guidance.** The optimal β varies substantially across datasets (0.05–0.30), and the KS validation accuracy varies by ~1.35 points across the β grid. While the plateau is relatively flat near the optimum, the paper offers no practical guidance on how to set β for a new dataset beyond exhaustive grid search.

5. **The mutual information estimator in Eq. (5) lacks full notational clarity.** Variables f̄ and z̄ are not explicitly defined (presumably normalized versions of f and z^m), and the summation index l is ambiguous (over samples or modalities?). The formula is cited from prior work (Zhou et al., 2025b), but as it underpins both the regularization (Eq. 7) and imbalance detection (Algorithm 1), a self-contained definition would improve reproducibility.

6. **Figure 1 caption describes the Ours lines as showing "a more pronounced imbalance,"** but the table shows Ours at 65:35 vs. MLA at 90:10 — Ours is *less* imbalanced. The intended meaning is "more pronounced correction of imbalance." This wording is misleading as printed.

### Trivial

7. **None beyond the items above** — the presentation is otherwise clear and the figures are well-designed.

## Nice-to-Haves

- **Directly measure classifier bias evolution** (e.g., per-modality gradient norms at the classifier layer over training) to more directly support the claim that the frozen classifier prevents bias entrenchment, rather than relying on modality contribution scores as an indirect measure.
- **Validate that the pretrained classifier is indeed unbiased** by comparing its modality contribution scores against an off-the-shelf jointly trained classifier.
- **Report training time / FLOPs** compared to baselines, since the secondary updates (Algorithm 1, lines 10–15) add extra forward/backward passes.
- **Add a limitations section** acknowledging the MVSA unimodal result, β sensitivity, and the restriction to 2-modality datasets.

## Removed Points

*"Code release is not mentioned"* — Removed per hard rules: do not question the existence or release status of cited artifacts.

*"Section 3.1 is an analogy not a proof"* — Removed. The gradient derivation (Eqs. 1–3) draws a meaningful structural parallel between class and modality imbalance. The paper's characterization ("similarity," "theoretical isomorphism in gradient dynamics") is defensible; the harsh critic overstates the gap.

*"Missing related works"* — Removed per hard rules.

*"Unimodal results from decision-level fusion may disadvantage baselines"* — Removed. The paper states *all* compared methods (MLA, MMPareto, LFM, CCAT) use the same decision-level extraction protocol ("unimodal results are directly acquired from decision-level fusion outputs," Section 4.2). The comparison is consistent.

*"Formatting/style nitpicks about broken characters, typos, missing symbols"* — Removed per hard rules (parser artifacts).

*"Strength: β grid search shows flat plateau"* — Moved to Minor weakness #4 instead, as the variation is non-negligible (~1.35 points on KS), and the conflict between the strength and the critic's reading is resolved by acknowledging the partial sensitivity.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the abstract's CREMA-D number** to match Table 1 (+2.27% vs LFM). Verify all other abstract numbers match their corresponding table entries.
2. **Add a discussion** of why CCAT's unimodal Image accuracy on MVSA (55.30%) trails MMPareto (59.54%), even though the multimodal result is better. This could be framed as a trade-off between unimodal representation quality and decision-level fusion robustness.
3. **Report standard deviations** for the three random seeds, at least for the main results in Table 1 and the ablation in Table 2.
4. **Clarify Eq. (5):** Define f̄ and z̄, and specify whether the denominator sum over l is over modalities or samples, so the formula is self-contained.
5. **Fix the Figure 1 caption** to read "more pronounced correction of imbalance" or "more balanced outcome."
6. **Add practical guidance** on setting β, or show that defaulting to a mid-range value (e.g., 0.15–0.20) yields reasonable performance across datasets.

---

**Calibration Report**

*Round 1 bracket:* The paper sits between weak anchors (avg 2.33–3.33) and strong anchors (avg 8.00). Middle-band anchors (3.5–7.5) included: CagdoUkvvl (4.50, multimodal continual learning with limited novelty), Pa6SiS66p0 (4.33), XTwwtlEfTF (4.50, missing modality adaptation with unclear math), 5BXWhVbHAK (6.33, multimodal synergy with theory + experiments). Initial bracket: [4.5, 6.5].

*Round 2 narrowing (4.5–7.5):* ul1cjLB98Y (5.25, unimodal bias theory — theoretical but limited to linear networks, mixed reviews 3/5/5/8), BZWssJoYEv (5.50, holistic multimodal interaction — good theory but marginal improvements), IT7LSnBdtY (5.00, missing modality SURE — unclear motivation, novelty concerns), 19ufhreGTj (5.80, dimensional collapse in CMKD — solid analysis, incremental contribution), uV9KFBVaFI (6.25, visual instruction tuning with fewer params — more mature domain), aPTGvFqile (6.29, cross-modal alignment in CLIP).

*Final placement:* CCAT is stronger than the 5.00 SURE paper (which had unclear motivation and baseline inconsistencies) and comparable to the 5.25 unimodal bias theory paper (which had narrower scope but no factual errors). It is weaker than the 5.80 dimensional collapse paper (which had cleaner claims and no factual discrepancies) and clearly below the 6.3+ papers (which had stronger theoretical foundations or broader evaluations). The CREMA-D abstract discrepancy is the primary factor preventing a higher score; the method itself is sound and the ablation is well-designed. Score: **5.0**.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>