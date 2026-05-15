I have now read the full paper and verified the reviewer claims against the text. Let me synthesize the final review.

---

## Summary

This paper proposes MADCluster, a model-agnostic anomaly detection framework that uses self-supervised clustering to dynamically update cluster centers, addressing the "hypersphere collapse" problem in deep one-class classification. The method consists of a Base Embedder (D-RNN), a Cluster Distance Mapping module that minimizes distances to a learnable center, and a Sequence-wise Clustering module with a novel "One-directed Adaptive loss" designed to force similarity scores toward 1 while increasing a threshold parameter. Experiments on four time-series datasets (MSL, SMAP, SWaT, PSM) with 11 baseline models report F1 improvements after applying MADCluster.

## Strengths

- **Empirically demonstrated performance gains across multiple deep learning baselines**: Table 1 shows consistent F1 improvements when MADCluster is applied to 11 different models, including deep architectures such as USAD, Anomaly Transformer, DCdetector, DeepSVDD, THOC, and D-RNN. Improvements are nontrivial (e.g., D-RNN on MSL goes from 81.24% to 94.84% F1; USAD on PSM from 73.21% to 89.86%). This provides evidence that the framework can augment various deep anomaly detectors.

- **Novel adaptation of self-supervised clustering to the single-cluster anomaly detection setting**: The paper correctly identifies that standard DEC-style clustering with student's t-distribution yields constant similarity
  for k=1, making it unsuited for anomaly detection. Replacing it with cosine similarity and a learnable one-directed threshold ν (Section 3.1.3) is a principled modification that addresses a genuine limitation.

- **Qualitative evidence of dynamic center learning preventing degenerate solutions**: Figure 4 shows that DeepSVDD's embeddings form multi-cluster distributions away from a fixed center, whereas MADCluster concentrates data around a single dynamic center (82.4% within 3σ by epoch 300, per line 180). Figure 5 shows ν increasing during training, consistent with the design goal. While not conclusive, these visualizations support the method's intended behavior.

## Weaknesses

### Fatal
None. No single weakness invalidates the paper's core claims entirely, though several weaken them significantly.

### Major

- **The integration mechanism for non-deep baselines is unspecified, undermining the model-agnostic claim for those models.** The paper reports results "before and after MADCluster" for LOF, OC-SVM, and Isolation Forest in Table 1, yet it never explains how these non-neural methods are integrated with MADCluster—which requires a Base Embedder that outputs `h_t^f` (Equation 1). The paper states "In the Base Embedder, we use the Dilated Recurrent Neural Network (D-RNN) as the base model" (line 48). Were these non-deep baselines wrapped in a D-RNN? Were they used as standalone scorers on D-RNN embeddings? The reader cannot determine what the "after MADCluster" column means for these models. The conclusion implicitly acknowledges this gap: "future research should focus on developing methodologies that increase applicability not only to traditional machine learning techniques but also to deep learning models" (line 189). This makes the results for LOF, OC-SVM, and Isolation Forest uninterpretable and weakens the claimed universality of the approach. **This is a structural gap in the evaluation, not a minor omission.**

- **No ablation studies isolate the contribution of individual components.** The method has three distinct modules: Base Embedder, Cluster Distance Mapping (ℒ_distance), and Sequence-wise Clustering with the One-directed Adaptive loss (ℒ_cluster). Without ablations (e.g., ℒ_distance only, ℒ_cluster only, fixed vs. dynamic center, standard cross-entropy vs. the proposed loss), it is impossible to attribute the reported improvements to any specific design choice. The paper claims the adaptive loss and dynamic center prevent hypersphere collapse, but no experiment separates their effects. For a method paper whose contributions are modular, this is a significant evidential gap.

### Minor

- **The point adjustment strategy inflates absolute F1 scores and is not acknowledged as potentially problematic.** The paper adopts a widely-used adjustment (line 154): if any time point in a contiguous abnormal segment is detected, the entire segment is considered correctly detected. This practice is known to produce inflated precision/recall (Wu & Keogh, 2020). While relative comparisons (before vs. after MADCluster) under the same protocol retain internal validity, the paper presents these F1 scores as absolute performance indicators without discussing the limitation. A brief caveat and/or a sensitivity analysis with unadjusted metrics would significantly strengthen the paper's empirical credibility.

- **The hard-threshold assignment p_t = 1[q_t ≥ ν] (Equation 5) creates a non-differentiable dependence that is not discussed in the method section.** The loss (Equation 6) involves p_t, which is a step function of ν. While label smoothing (Section 4.2) is introduced as an implementation detail that softens p_t, the formal method description presents the loss as though it operates on hard assignments. The paper does not explain how gradients flow through this discontinuity or whether the straight-through estimator or the softening (τ) resolves it. This gap between the formal presentation and the actual implementation is confusing.

- **No error bars, standard deviations, or confidence intervals are reported for any experiment in Table 1.** Without multiple trials, the reader cannot assess whether the reported improvements are statistically significant or within the range of run-to-run variation. This is standard for large-benchmark evaluations in this field, so it is a notable omission.

- **"Description of the five experiment datasets" (line 150) but only four datasets are listed (PSM, MSL, SMAP, SWaT) and used in Table 1.** The abstract and conclusion correctly say "four." This is a minor inconsistency.

### Trivial

- The hyperparameter τ (label smoothing factor) is mentioned but its value used in experiments is not reported.
- The description of R^2 determination ("based on a specific quantile of the neural network outputs") is vague; the quantile value is not specified.

## Nice-to-Haves

- Reporting unadjusted (pointwise) precision/recall/F1 alongside adjusted metrics would allow the field to calibrate the impact of the adjustment on these specific datasets.
- Ablation of the three components (Base Embedder choices, whether ℒ_cluster alone suffices, whether a fixed center with the same loss works) would clarify which part of the design drives improvements.
- Analyzing the norm of learned embeddings and center during training would quantitatively verify that hypersphere collapse (all values → 0) does not occur.

## Removed Points

- **Missing mathematical proof of the One-directed Adaptive loss**: The paper claims "the optimization of this loss is mathematically proven" (abstract, contributions). The proof does not appear in the main text. Per review guidelines, the parser strips appendix sections from all papers; the proof may exist in the original submission. This point is therefore removed as unverifiable from the parsed text. However, the related concerns about the loss's discontinuity (addressed in Minor Weaknesses above) are independent and remain.

- **Criticism about DeepSVDD collapse analysis not checking embedding scale**: The reviewer argued no quantitative check of embedding scale. This is a reasonable suggestion but is subsumed by the missing ablation / verification concern above. It is moved here as a less central point.

- **Strength about "mathematical foundation for single-cluster optimization"**: Since the proof is not visible in the parsed text, this claimed strength is weakened and moved here. The methodological novelty of adapting self-supervised clustering to k=1 is retained as a separate strength.

- **Generic strengths from Strength Finder** (e.g., "this paper addressed an important problem") and generic criticisms about minor presentation issues are removed.

## Novel Insights

The most interesting observation to emerge across the reviews is the tension between the paper's broad "model-agnostic" framing and the empirical opacity of how non-deep models were integrated. The paper explicitly builds on DEC's self-learning framework but modifies it for the single-cluster case by replacing student's t-distribution with cosine similarity and a learnable threshold. This is a genuinely non-obvious modification—standard DEC fails for k=1 because the soft assignment becomes constant—and it represents the paper's clearest conceptual contribution. However, the evaluation design (no ablations, no integration details for non-deep baselines, reliance on point-adjusted metrics without caveats) prevents the reader from isolating whether this contribution is actually responsible for the observed gains. The convergence visualization (Figure 5) showing ν increasing during training is the best evidence that the loss behaves as designed, but it remains qualitative.

## Suggestions

1. **Clarify the integration protocol for all baselines.** For each model in Table 1, specify: (a) what serves as the Base Embedder, (b) whether the model's original scoring function is retained or replaced by MADCluster's anomaly score (Equation 7), and (c) how non-neural baselines (LOF, OC-SVM, IF) were handled. If these models were not genuinely integrated, remove them from the comparison or clearly label them as "not applicable."

2. **Add ablation experiments.** At minimum compare: (a) ℒ_distance alone (static center), (b) ℒ_cluster alone, (c) both losses with a fixed center, (d) both losses with the proposed dynamic center and One-directed Adaptive loss, and (e) a baseline using standard binary cross-entropy instead of the proposed loss on the same soft assignments. This would directly test the claimed benefits.

3. **Report unadjusted pointwise metrics alongside adjusted ones**, or add a paragraph explaining why the adjustment is appropriate and discussing its limitations (citing Wu & Keogh 2020). Provide error bars (mean ± std over multiple runs with different seeds) for at least the main results.

4. **Address the hard-threshold discontinuity explicitly** in the method section: state whether gradients flow through p_t via the straight-through estimator, whether the label smoothing (τ) resolves it, or whether the hard threshold is used only at test time.

5. **Fix the "five datasets" / four datasets inconsistency** in Section 4.1.

## Score and Decision

The paper presents a genuinely motivated modification to self-supervised clustering for anomaly detection (adapting DEC-style clustering to the k=1 case via cosine similarity and a learnable threshold), and Table 1 shows consistent improvements across several deep architectures. However, the evaluation has significant gaps that prevent the authors from cleanly supporting their claims: the integration mechanism for non-deep baselines is unexplained, no component ablations exist, no error bars are reported, and the point-adjustment strategy's known limitations are not acknowledged. These issues are addressable but would require substantial revisions to the experimental section. In its current form, the paper's evidence does not meet the bar for acceptance at a competitive venue.

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**