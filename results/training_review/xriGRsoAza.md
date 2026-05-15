No human review file found for this paper — proceeding without calibration.

---

## Summary

This paper proposes MILLET, a framework that reinterprets time series classification (TSC) as a multiple instance learning (MIL) problem. By replacing global average pooling (GAP) with MIL-based pooling methods (attention, instance, additive, and a novel pADDitive pooling) in standard deep learning TSC architectures (FCN, ResNet, InceptionTime), the models become inherently interpretable — producing time-point-level saliency maps in a single forward pass. The paper evaluates 12 new models on 85 UCR datasets and a new synthetic dataset (WeeklyAnomalies), showing competitive predictive performance and improved AOPCR interpretability scores over GAP-based models with CAM post-hoc explanations.

## Strengths

- **Clean, plug-and-play framework for inherent interpretability.** The core idea — replacing GAP with MIL pooling in existing DL-TSC architectures — is simple and practically useful. Any model using GAP can be upgraded to produce inherent saliency maps with minimal architectural change. The four pooling methods (attention, instance, additive, pADDitive) are clearly described and implemented across three backbones (FCN, ResNet, InceptionTime), yielding 12 new models.

- **Novel pADDitive pooling is an effective contribution.** pADDitive pooling (independently applying attention and classification to time-point embeddings, then combining them) achieves the best average accuracy across backbones on UCR (0.846 ± 0.009 vs. GAP's 0.841 ± 0.009) and the best balanced accuracy (0.834) among compared methods, competitive with SOTA methods like Hydra-MR (0.831) and HC2 (0.830). It also achieves the best AOPCR of 6.00 across backbones on UCR, compared to GAP's 5.71.

- **Large-scale evaluation across 85 UCR datasets with three backbones.** The breadth of evaluation supports generalizability. Results are presented via critical difference diagrams, summary tables with four metrics (accuracy, balanced accuracy, AUROC, NLL), and an interpretability-predictive performance Pareto analysis.

- **WeeklyAnomalies synthetic dataset enables ground-truth interpretability evaluation.** This dataset with known discriminatory time points is a useful community resource, allowing use of NDCG@n alongside AOPCR. The paper shows MILLET achieves AOPCR 17.531 (mean across backbones) vs. CAM 15.415 and SHAP –0.692, and is over 800× faster than SHAP.

- **Qualitative interpretability examples are compelling.** The LargeKitchenAppliances case study (Figure 11) visually demonstrates that MILLET produces sparser, more interpretable heatmaps than CAM or SHAP, identifying class-specific motifs (e.g., "long periods just above zero → Washing Machine") that align with human intuition.

## Weaknesses

### Fatal
None.

### Major

- **Interpretability evaluation does not fully support the claim of "higher quality" explanations.** The paper's central claim rests on two metrics: AOPCR and NDCG@n.
  - AOPCR (used on all 85 UCR datasets) measures how fast the model's prediction decays when time points are removed in the order suggested by the explanation. This is a valid faithfulness/self-consistency metric, but it does not measure whether explanations identify the **true** class-discriminatory motifs. On UCR, where ground truth is unknown, AOPCR is the only metric available.
  - On the synthetic dataset where ground truth is known (NDCG@n), MILLET's advantage over CAM is **marginal**: mean NDCG 0.612 vs. CAM's 0.607. For the InceptionTime backbone specifically, CAM outperforms MILLET (0.707 vs. 0.704). The paper attributes this to sparsity reducing coverage, which is a plausible explanation but also an admission that MILLET's explanations can be incomplete.
  - The claim that MILLET explanations are of "higher quality than other well-known interpretability methods" is overstated given that comparison is limited to only CAM and SHAP, and the ground-truth improvement over CAM is within rounding error on the best backbone.

- **Only two interpretability baselines are compared (CAM and SHAP).** CAM is the most natural single-forward-pass baseline, but the paper's broad claims about "well-known methods" would benefit from comparison to additional single-pass methods such as gradient-based saliency (e.g., Integrated Gradients, DeepLIFT) or attention-based explanations from recurrent models. The narrow comparison set weakens the generality of the quality claim.

- **No ablation of the three introduced enhancements.** The paper introduces positional encoding, replicate padding, and dropout (§3.4) as important design choices for MILLET, but their individual contributions are never isolated. Without ablation, it is unclear which components drive the observed improvements and whether the method would work without them. In particular, the claim that replicate padding "alleviated the start/end bias" in interpretability is not systematically validated.

### Minor

- **Predictive performance improvements are small and not statistically tested.** The average accuracy improvement from GAP (0.841) to pADDitive (0.846) is 0.005, and for InceptionTime it is 0.853→0.856. No statistical significance tests (e.g., Wilcoxon signed-rank) are reported. While the paper claims MILLET "improves" predictive performance, the evidence is weak and the emphasis on "improving" in the abstract is exaggerated given the magnitude.

- **The sparsity vs. coverage trade-off is acknowledged but not systematically analyzed.** The paper notes that sparsity benefits AOPCR but can hurt NDCG. However, there is no analysis of when sparsity helps vs. hurts across datasets or classes. The paper treats sparsity as self-evidently beneficial ("especially important for long time series") without task-specific evidence that practitioners prefer sparser explanations.

- **Runtime comparison with CAM is missing.** SHAP is orders of magnitude slower than any single-forward-pass method, so the "800× faster than SHAP" statistic is not informative for comparing MILLET to CAM (also a single-forward-pass method). A runtime comparison with CAM would be more relevant for assessing MILLET's practical advantage.

- **No explicit validation that time-point instance predictions correspond to meaningful class-conditional motifs.** The paper frames each time point as a MIL instance, but in many TSC tasks the discriminatory pattern is a subsequence, not a single time point. While convolutional feature extractors provide some local context through receptive fields, the paper does not systematically validate that the resulting instance-level predictions correspond to human-interpretable motifs (beyond a few qualitative examples). A quantitative analysis on the synthetic dataset (e.g., pointwise intersection-over-union between explanation and injected motif) would strengthen this.

- **The conclusion does not discuss limitations.** The paper reads as overly positive. Explicitly acknowledging the limitations of AOPCR as a metric, the potential mismatch between time-point instances and subsequence-based motifs, and the narrow baseline comparison would strengthen the paper's credibility.

### Trivial

- Minor notation inconsistency: The paper uses both "Conj." and "pADDitive" to refer to the same pooling method across tables and text.

## Nice-to-Haves

- Additional qualitative examples from UCR datasets beyond LargeKitchenAppliances, including failure cases where MILLET's explanations are misleading.
- Comparison to additional interpretability methods (e.g., Integrated Gradients, DeepLIFT) for a broader evaluation.
- Quantitative analysis on the synthetic dataset using pointwise overlap metrics (e.g., IoU between explanation and injected signature region) to complement NDCG.
- Analysis of the effect of ensembling on interpretability quality (the paper notes MILLET struggles with ensemble ResNet but does not analyze why).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"AOPCR is circular"** — This characterization is inaccurate. AOPCR measures explanation faithfulness (does the explanation identify points the model cares about?), which is a valid and standard property. The real issue is that it does not measure correctness against ground truth, which the paper acknowledges. The criticism has been rephrased accurately above.

- **"The paper does not discuss why the standard MIL assumption is appropriate for TSC"** — The paper explicitly states it does not constrain to any specific MIL assumption (§2, line 57-58), which is a deliberate design choice. This is a strawman.

- **"The paper should include a user study"** — User studies are not standard practice in TSC interpretability evaluation and represent a high bar not expected for this type of contribution.

- **"Missing related works"** — Per policy, missing related work criticisms cannot be confirmed without external sources.

- **"Formatting/presentation nitpicks"** — Pure style issues removed per policy.

- **"The synthetic dataset has only 500 training samples"** — This is a design property of the dataset, not a weakness. The dataset serves its purpose.

## Novel Insights

The most important observation emerging from these reviews is the tension between MILLET's two advertised virtues: sparsity and completeness. The paper simultaneously praises sparsity as a desirable property ("especially important for long time series") while acknowledging it can reduce NDCG by missing parts of discriminatory regions. This trade-off is never systematically characterized — the paper does not establish when sparsity is beneficial vs. harmful, nor does it validate that practitioners prefer sparser explanations. This gap between claimed benefit and measured behavior is the paper's central weakness. The AOPCR vs. NDCG discrepancy on the synthetic dataset (MILLET wins on AOPCR, CAM wins on NDCG for InceptionTime) concretely illustrates this tension, but the analysis remains at the level of speculation rather than systematic investigation.

## Suggestions

1. **Temper the claims about explanation "quality."** The paper's strongest contribution is providing **inherent** interpretability (explanations come for free with predictions) without sacrificing accuracy. The evidence does not convincingly show that these explanations are of "higher quality" than CAM's. Reframe the central claim around inherent interpretability rather than quality superiority.

2. **Add ablation experiments** for the three enhancements (positional encoding, replicate padding, dropout) on at least a subset of UCR datasets. This is essential for understanding which components drive the improvements.

3. **Report statistical significance tests** (e.g., Wilcoxon signed-rank test comparing MILLET to GAP across the 85 UCR datasets) to support the claim of predictive improvement.

4. **Systematically analyze the sparsity trade-off** on the synthetic dataset: for which classes/types of signatures does sparsity help AOPCR and hurt NDCG? Characterize when practitioners should expect each behavior.

5. **Add a runtime comparison with CAM** alongside the existing SHAP comparison to give a complete efficiency picture.

6. **Include a limitations section** in the conclusion that explicitly acknowledges the reliance on AOPCR for UCR interpretability evaluation and the potential mismatch between time-point and subsequence-level interpretability.

## Score and Decision

The paper presents a clean, well-motivated idea with extensive empirical evaluation. The MILLET framework, pADDitive pooling, and WeeklyAnomalies dataset are genuine contributions. However, the paper's central claim — that MILLET provides "higher quality" explanations — is not proportionally supported by the evidence. The interpretability evaluation relies heavily on a self-consistency metric (AOPCR), and the only ground-truth comparison shows marginal improvement over CAM. The predictive improvements are small and unvalidated for significance. The lack of ablation studies further limits mechanistic understanding. These are real but not fatal weaknesses — none invalidate the core contribution of enabling inherent interpretability via MIL pooling. The paper would be strengthened by toning down its strongest claims and addressing the evaluation gaps. As submitted, it is a borderline paper with contributions worth publishing but with significant room for improvement in the interpretability evaluation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>