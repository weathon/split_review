I have verified all claims against the paper. Let me now construct the final consolidated review.

## Summary

This paper introduces NCSBAD (Noise Conditional Score-Based Anomaly Detection), which adapts Noise Conditional Score Networks (NCSNs) to tabular anomaly detection in a one-class classification setting. The method derives an anomaly score directly from a simplified denoising score-matching loss, using an MLP-based network trained on normal data only. The paper evaluates on an extensive benchmark of 57 datasets (121 sub-datasets) with 49 baseline methods, reporting competitive results.

## Strengths

- **First principled adaptation of NCSN to tabular anomaly detection.** The paper introduces a score-based framework that directly uses a simplified denoising score-matching loss as an anomaly score (Section 3, Eq. 3). This provides a self-contained, mathematically grounded alternative to reconstruction- or contrastive-learning methods. The derivation from the score function is clearly linked to the underlying data distribution, making the approach novel in the tabular domain.

- **Comprehensive evaluation on the largest tabular anomaly detection benchmark.** The evaluation spans 57 datasets (121 sub-datasets) and 49 baselines (Section 4), including both classical and deep-learning methods. The paper provides extensive per-dataset results (Tables 9–48), box plots with 5-seed runs, and comparisons across multiple metrics (AUC-ROC, AUC-PR, F1). This is among the most thorough benchmark evaluations for a score-based anomaly detector on tabular data.

- **Efficient parallel inference.** Unlike DDPMs that require sequential Markov-chain denoising, the NCSN framework allows multiple perturbed samples to be scored in parallel (Section 3, "Efficient Implementation and Inference"). This is a concrete architectural advantage for real-time or large-scale deployment, and the paper measures it against baselines.

- **Inherent feature-level interpretability.** The anomaly score can be decomposed into element-wise errors (Eq. 4), enabling per-feature attribution. Section 5 demonstrates this on MNIST-C with a visual example, and the paper is transparent that this is a toy illustration (acknowledging the challenge of visual interpretability for tabular data, citing Shenkar & Wolf 2022).

- **Transparent presentation of both validation and no-validation variants.** The paper presents both NCSBADVAL (with validation-based epoch selection) and NCSBAD (fixed 200 epochs, no validation), allowing readers to assess the contribution of validation data.

## Weaknesses

### Fatal
None.

### Major

- **Unfair comparison for NCSBADVAL due to validation-based model selection.** The validation set (line 89) contains both normal samples and anomalies, and NCSBADVAL selects the training epoch that maximizes AUC-ROC on this validation set (line 78). None of the 49 baseline methods receive an analogous benefit—all are run with "default hyperparameters provided by the authors" without validation-based epoch selection (line 93). This protocol mismatch inflates the apparent advantage of NCSBADVAL. The paper's headline claim of "state-of-the-art performance" (Abstract) largely rests on NCSBADVAL. While NCSBAD (without validation) also performs competitively (1st in mean AUC-ROC, 2nd in F1 and AUC-PR behind LUNAR), the SOTA claim in the abstract is unqualified and overstates what the evidence supports. **To fix**: either apply the same validation-based selection to all deep baselines, or present NCSBAD as the primary method and treat validation as a separate add-on experiment.

### Minor

- **Anomaly score design narrows the multi-scale advantage the method is motivated by.** The paper argues that multi-scale noise perturbation is crucial for capturing low-density regions (§3, "Noise Scale Selection"). Yet the anomaly score uses a single, fixed, very small noise level (t_fix corresponding to the first time step, line 62). While the network is trained on multiple scales, the scoring discards multi-scale information at inference. The justification that "perturbations should be small… still sufficient for a neural network" is a plausibility argument, not a rigorous one. A sensitivity study exploring whether aggregating denoising errors across multiple noise levels improves detection would substantially strengthen the method's grounding.

- **No statistical significance testing.** Results are reported as means over 5 seeds with box plots showing considerable overlap between many methods. The paper concludes superiority based on mean ranking without paired significance tests. Given the variance visible in the box plots, it is unclear whether the differences between top methods are meaningful. A critical difference diagram or Wilcoxon signed-rank tests would substantiate the ranking claims.

- **Interpretability evidence is limited to a vision toy example.** The interpretability demonstration (Section 5) uses MNIST-C, which is explicitly acknowledged as non-tabular. While the paper is transparent about this being a toy illustration, the resulting claim that the method "can localized anomaly detection at the feature level" in tabular data is unsupported by direct evidence. A synthetic tabular experiment with known anomalous features would make the claim credible.

- **Key hyperparameters deferred to the appendix.** The values of T, optimizer, learning rate, batch size, and the exact t_fix are not stated in the main text. The paper references supplementary sections (line 153), but readers relying solely on the main text cannot reproduce the method.

- **NUM=70 and noise schedule choices lack sensitivity analysis.** The number of noise samples (NUM=70) for the anomaly score and the noise schedule parameter (σ=0.01) are presented as fixed constants with limited justification. No ablation study shows how performance varies with these choices.

### Trivial

- The paper states "if we assume 1000 time steps for t" (line 62) as an aside, but the formal parameter T in the noise schedule formula is never given an explicit numeric value in the main text.

## Nice-to-Haves

- **Runtime comparison in the main paper.** The paper mentions efficient parallel inference but does not include a runtime comparison table or figure in the main body (only a textual claim in §4). A timing table would strengthen the practical argument.
- **Apply validation-based early stopping to deep baselines** for a fully fair comparison. Alternatively, the paper could use a fixed-number-of-epochs setup for all methods including NCSBAD, and treat the validation variant as an additional experiment.
- **Multi-scale anomaly score.** Exploring whether aggregating the denoising error across several noise levels (instead of just the smallest) improves detection would directly address the gap between motivation and implementation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic: "Data split is unconventional"** — The paper explicitly states this split follows prior work (Bergman & Hoshen 2020; Shenkar & Wolf 2022; Livernoche et al., 2024). However, the implication for the fairness of NCSBADVAL vs. baselines is already covered in the Major weakness above.
- **Harsh critic: "Box plots ordering by mean performance not enough... no single best method"** — The paper itself acknowledges this ("no single method universally dominates") and recommends practitioners evaluate multiple algorithms. The paper's claim is about mean rankings, not universal dominance, so this is not a contradiction.
- **Harsh critic: "Inference time comparison missing from main body"** — Moved to Nice-to-Haves.
- **Harsh critic: Dynamic about LUNAR baseline** — The paper acknowledges LUNAR's strong performance; this is a strength of the evaluation, not a weakness.
- **Strength Finder: Generic reframing of strengths as "SOTA"** — Weakened to "comprehensive evaluation" to account for the fairness issue.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper motivates NCSNs through their multi-scale noise handling but uses only a single small noise scale for scoring, which is an interesting methodological question the paper does not resolve. The validation-selection fairness issue is also a useful observation for the broader anomaly detection benchmarking literature.

## Suggestions

1. **Separate the validation issue clearly.** Restructure the paper so NCSBAD (fixed 200 epochs) is the primary proposed method. Present NCSBADVAL as a separate study showing the potential benefit of validation-based selection, with an explicit caveat that baselines were not given this advantage.

2. **Add a multi-scale ablation.** Study whether aggregating the denoising error across 2–3 noise levels improves or harms detection. This would either validate the current design or point toward a better one.

3. **Add pairwise significance tests** (e.g., critical difference diagram, Wilcoxon signed-rank test) to support claims that differences between top methods are meaningful.

4. **Add a quantitative interpretability experiment** on tabular data (e.g., synthetic anomaly injection with known feature-level ground truth).

## Score and Decision

This paper proposes a novel adaptation of NCSNs to tabular anomaly detection—a sensible and well-motivated idea—and evaluates it on an impressively large benchmark. The core method (NCSBAD without validation) appears competitive, ranking 1st in mean AUC-ROC and 2nd in F1 and AUC-PR. However, the headline "state-of-the-art" claim rests primarily on the NCSBADVAL variant, which benefits from validation-based epoch selection that no baseline receives. This is a significant fairness gap. Additionally, the single-noise-level scoring design is in tension with the paper's stated motivation for using NCSNs, and the lack of significance testing weakens the ranking claims. These issues are fixable and do not invalidate the core contribution, but they prevent acceptance in the current form. The paper would benefit from addressing the fairness issue, adding ablations, and tempering its claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>