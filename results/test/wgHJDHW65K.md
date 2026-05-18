## Summary

This paper introduces a fully unsupervised representational knowledge distillation framework that transfers information from a high-fidelity PPG (photoplethysmography) teacher encoder to an accelerometer student encoder, using 20 million minutes of paired sensor data from ~172K participants in the Apple Heart and Movement Study. The key contribution is demonstrating that a low-power, ubiquitously available accelerometer can be trained to produce embeddings that closely match those of a PPG encoder, yielding 99.2% top-1 cross-modal retrieval accuracy and 23–49% improvements over both self-supervised and supervised baselines for predicting heart rate and heart rate variability, while also being label-efficient and amenable to simultaneous model compression.

## Strengths

- **Large-scale, fully unsupervised cross-modal distillation with strong empirical results.** Using 20M minutes of paired PPG-accelerometer data from ~172K participants (Section 4.1), the framework achieves 99.2% top-1 retrieval accuracy and mean rank 1.02 for matching accelerometer to PPG embeddings (Table 1), and the paper reports standard deviations across 100 bootstrap samples for this analysis — a rigorous statistical treatment. The distilled encoder consistently and substantially outperforms both self-supervised (Accel-MAE, Accel-CL) and supervised baselines by 23–49% for HR, SDNN, and RMSSD across all label regimes from 0.1% to 100% (Section 5.2).

- **Label efficiency critical for health applications.** The distilled encoder maintains strong downstream performance even with only 0.1% of labeled data (a 1000× reduction), a regime where supervised encoders collapse (Section 5.2). This directly supports the value proposition of fully unsupervised distillation for domains where labeled medical data is scarce.

- **Thorough and informative ablations.** The paper verifies that: (a) removing augmentations during distillation increases HR MAE by 45% (Section 5.5); (b) freezing the teacher is critical — joint multi-modal training degrades accelerometer HR performance by >95% (Table 3); (c) the framework generalizes across architectures (Transformer and EfficientNet) and teacher pre-training strategies (MAE and contrastive learning); (d) simultaneous model compression to 5× fewer parameters still outperforms uni-modal baselines (Table 7, Figure 3).

- **Demonstrated breadth of predictive capability.** Beyond HR/HRV, the distilled accelerometer encoder predicts 46 health-related targets including demographic variables, health conditions, medication use, and lifestyle habits (Section 5.3) — substantially broader than prior work on single-modality accelerometer models.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the evidence presented.

### Minor

- **Missing uncertainty quantification for downstream linear probing results.** The paper reports standard deviations for retrieval metrics across 100 bootstrap samples (Table 1), which is commendable. However, the downstream linear probing comparisons that constitute the paper's central evidence (23–49% improvements over baselines in Section 5.2, Figure 2a) are reported without confidence intervals, error bars, or specification of the number of random seeds. While the improvements are large and consistent across all label regimes (mitigating the concern that noise could flip the conclusion), the absence of variance reporting prevents readers from assessing the statistical robustness of the claimed improvements over supervised training — a strong claim that warrants rigorous support.

- **The near-perfect retrieval results (99.2% top-1) could benefit from deeper analysis.** The paper reports strong cross-modal alignment with rigorous bootstrap-based standard deviations, which already goes beyond what many comparable papers provide. However, the paper does not analyze the <1% of failure cases where the correct pair is not ranked first. Characterizing these (e.g., whether they come from specific participants, segments with higher residual motion, or particular time periods) would help calibrate reader confidence and provide practical guidance on when the distilled encoder is trustworthy. Similarly, ablating the candidate pool size (e.g., reporting retrieval accuracy for pool sizes of 100, 1K, 10K, 100K) would clarify whether the near-perfect performance degrades gracefully under more challenging conditions. These are strengthening analyses rather than corrections to any identified error.

### Trivial
None.

## Nice-to-Haves

- The paper notes that joint multi-modal training degrades performance and offers a plausible explanation (asymmetric information leading the PPG encoder to converge to trivial solutions), but does not verify this mechanism (e.g., by analyzing the PPG encoder's retrieval performance or embedding entropy in the joint setting). Verifying the explanation would strengthen the argument for two-stage distillation.
- An ablation of which individual augmentations matter most during distillation (temporal warping vs. channel permutation vs. noise addition) could improve practical guidance and method interpretability.
- A comparison to an L2-based distillation variant (training the student to directly regress to the teacher's embeddings) would help isolate the contribution of the contrastive objective, though the existing multi-modal joint-training ablation already provides a meaningful counterfactual.

## Removed Points

- **"The paper does not compare to any other knowledge distillation method for biosignals."** — The paper compares against uni-modal self-supervised baselines (Accel-MAE, Accel-CL), supervised baselines, and the critical multi-modal joint-training ablation. This list of comparisons is defensible for the paper's scope. The specific comparison suggested (L2-based distillation) is a variant within the method class, not a missing baseline.
- **"Potential data bias and generalizability concerns"** (demographics, single device) — The paper explicitly scopes its work to low-motion periods recorded on Apple Watch, acknowledges the dataset's demographic limitations by citing prior publications, and lists these as areas for future work in Section 6. The claim about "any wearable device" appears in the abstract as an aspirational statement about the framework's potential, not a demonstrated result. The paper is adequately transparent about its limitations.
- Generic strengths from Strength Finder that lacked specific content or conflicted with verified weaknesses were dropped.
- Concerns about "tension between near-perfect retrieval and imperfect downstream performance" were removed because this is not actually a tension: retrieval measures alignment to the teacher's embedding space (directly optimized by the distillation loss), while linear probing measures the ability to extract specific target information from that embedding space — fundamentally different tasks with different expected performance ceilings.

## Novel Insights

The harsh reviewer raises a point that is worth highlighting: the paper's multi-modal joint-training ablation (Table 3) shows that simultaneously training both PPG and accelerometer encoders via contrastive learning degrades accelerometer performance by 95% for HR. This is framed as a negative result demonstrating the importance of two-stage distillation, but it also reveals something deeper about the information asymmetry between modalities. When the stronger modality (PPG) is allowed to update, the contrastive objective can be satisfied without the PPG encoder maintaining a rich representation — it only needs to be distinguishable from other samples in the batch. This suggests that multi-modal contrastive learning with highly asymmetric modalities may actively harm the weaker modality's representations, and that freezing the stronger modality is not just beneficial but necessary. This insight has implications beyond the specific PPG-accelerometer setting: any multi-modal learning setup with substantial information asymmetry (e.g., video + audio where video dominates, clinical text + tabular data) should consider whether joint training might degrade the weaker modality's representations.

## Suggestions

1. **Add uncertainty quantification for downstream linear probing.** Report the mean and standard deviation across at least 3–5 random seeds for the key HR, SDNN, and RMSSD comparisons in Section 5.2. If multiple seeds are infeasible due to compute constraints, state this explicitly and add bootstrap confidence intervals over the held-out test set.
2. **Add a brief failure-case analysis for retrieval.** Characterize the <1% of queries where the correct pair is not ranked first — e.g., do these come from particular participants, segments with higher accelerometer variance, or specific time periods? Even a short paragraph would substantially strengthen confidence in the 99.2% top-1 result.
3. **Include a table of exact downstream numbers with standard deviations** in addition to Figure 2, since figures can be hard to read, and include the number of independent runs/repetitions for each evaluation.

## Score and Decision

This paper presents a well-motivated, carefully executed framework for cross-modal knowledge distillation across biosignals. The scale of the dataset, the breadth of downstream evaluation, and the thorough ablations are clear strengths. The paper makes a genuine contribution by showing that a ubiquitously available low-fidelity sensor (accelerometer) can, through unsupervised distillation from PPG, produce representations competitive with and often superior to those from supervised training on the target tasks. The main weakness — missing uncertainty quantification for downstream comparisons — is addressable and does not undermine the core conclusions given the large and consistent improvements. The paper should be accepted.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>