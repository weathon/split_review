## Summary

This paper proposes TGeo-KD, a method for learning sample-wise knowledge fusion ratios in knowledge distillation by exploiting trilateral geometric relations among the student prediction (S), teacher prediction (T), and ground truth (G). The method captures both intra-sample relations (the S–T–G triplet) and inter-sample relations (using the teacher's class-wise average prediction as an additional vertex), then feeds these geometric features into a small MLP trained via bilevel optimization to produce adaptive fusion ratios. Experiments are conducted on image classification (CIFAR-100, ImageNet), attack detection (HIL), and CTR prediction (Criteo), showing consistent improvements over prior re-weighting baselines.

## Strengths

- **Motivation experiment directly validates the overlooked ST discrepancy signal.** The controlled experiment (Section 1, Figure 1) partitions CIFAR-100 samples by teacher correctness and ST discrepancy, then trains students with different fixed α values. The results cleanly show that samples with high ST benefit from larger α when the teacher is correct, and smaller α when the teacher is incorrect — confirming that ST carries information orthogonal to SG and TG for determining α.

- **Inter-sample relations via the teacher's class-wise average provide a principled mechanism for handling outliers.** The method introduces the teacher's global average prediction T̄ as an additional vertex (Eq. 9), creating inter-sample geometric relations that anchor outlier samples to the class consensus. The analysis in Section 4.4 (Figure 5) shows TGeo-KD assigns fusion ratios below 0.3 to Gaussian-noise outliers while normal samples receive ratios in the 0.4–0.6 range, demonstrating that the mechanism functions as intended.

- **Ablation study cleanly isolates each component's contribution.** Table 5 shows a clear monotonic progression: SG+TG only (73.92%) → adding intra-sample ST edge (75.28%) → further adding inter-sample relations (76.83%). This provides direct causal evidence that each geometric term the paper introduces yields a measurable accuracy gain.

- **Fusion ratio dynamics match the paper's intuitive claims in detail.** Table 4 tracks average α across 400 epochs under four conditions. With ST incorporated, α correctly increases (0.59→0.73) when the teacher is correct with large ST, and decreases (0.52→0.27) when the teacher is correct with small ST — exactly matching the prescription from the motivation experiment. Without ST, α drifts monotonically upward, confirming the method's qualitative behavior.

## Weaknesses

### Fatal

None.

### Major

- **The HIL experiment's "student outperforms teacher" claim is confounded by an asymmetry in training data.** On HIL, TGeo-KD achieves 92.39% with a 4-layer BERT student while the 12-layer BERT teacher achieves only 88.19% (Table 3). The paper states that "the original HIL and Criteo are imbalanced" and that "we conduct oversampling on the minority class of training set as the data pre-processing procedure" (line 194). The teacher is described as a pre-trained BERT model (Table 3 caption) — it is not stated whether the teacher was also trained or fine-tuned on the oversampled data. If the student (and all KD baselines) train on oversampled data while the teacher's numbers come from a model not exposed to oversampling, the comparison is not apples-to-apples. The student-beats-teacher result is highlighted in the text (line 351: "better than the deeper teacher with the increasing ACC of 4.20%"), yet the paper provides no discussion of whether this advantage stems from the oversampling rather than from TGeo-KD's geometric mechanism. *This does not invalidate the comparison against other KD baselines (all trained under the same oversampling regime), but it undermines the paper's secondary claim of surpassing the teacher, and it raises broader questions about whether the oversampling setup interacts with the learned fusion ratios in ways not controlled for.*

- **The SG+TG-only ablation underperforms vanilla KD without explanation.** In Table 5, the configuration using only SG+TG relations (matching the information used by WLS-KD and similar methods) achieves 73.92% on CIFAR-100, which is *worse* than vanilla KD's 74.07%. Since SG+TG captures both student correctness and teacher correctness — information that prior work shows is valuable — this result is anomalous. The paper does not discuss why a learned α using SG+TG degrades performance below a fixed α. This is concerning because it suggests the MLP f_ω may not be learning effectively from SG+TG alone, which in turn raises the question of whether TGeo-KD's advantage when ST is added comes from the MLP learning something meaningful or from some other aspect of the bilevel optimization setup.

### Minor

- **The bilevel optimization procedure is critically underspecified.** Equations 5–6 (lines 117–120) formulate learning ω as a bilevel problem, but the paper provides no details on how it is solved in practice. Bilevel optimization with neural-network inner and outer objectives is non-trivial; typical approaches include unrolling through the inner loop, implicit differentiation, or approximation heuristics. The paper cites Franceschi et al. (2018) but does not state which method is used, how many inner steps are taken, whether the inner optimization is run to convergence or truncated, what learning rates are used for inner/outer loops, or what fraction of data is held out as the validation set for the outer objective. Without these details the method cannot be faithfully reproduced.

- **Comparison against WLS-KD (the strongest baseline on most settings) is not under controlled conditions.** On CIFAR-100 (Table 1) and ImageNet (Table 2), WLS-KD results are cited from prior work without standard deviations or re-implementation under the same experimental conditions. The paper's re-implemented baselines (ANL-KD, ADA-KD, RW-KD) are all outperformed by WLS-KD on nearly every setting, making WLS-KD the primary competitor. Yet no statistical significance test can be computed against it, and differences in training recipes, hyperparameters, or data splits could affect the comparison. This is a standard limitation in many KD papers, but given that the paper's strongest claims are relative to WLS-KD, a controlled re-implementation would substantially strengthen the evidence.

- **The statistical significance claim is imprecise.** Line 331 states: "All computed t-scores surpass the threshold value t_{0.05,5}." The notation t_{0.05,5} is ambiguous (mixing significance level and what appears intended as degrees of freedom); with 5 runs the degrees of freedom for a paired t-test should be 4. More importantly, the t-test can only be applied to baselines that were re-implemented with multiple runs (those marked with *). Against WLS-KD — the strongest baseline on most settings — no standard deviations are reported, so the claim of "statistical significance level of 5.0%" does not extend to the most important comparisons.

- **The outlier analysis uses only Gaussian noise, which is an artificial and limited proxy.** The paper evaluates robustness against outliers by injecting synthetic Gaussian-noise samples (line 422–423). Real outliers in classification (adversarial examples, domain-shifted samples, label errors) are more varied. While Gaussian noise is a standard sanity check, the claim that inter-sample relations "protect the student training from being disrupted" (which is a notable qualitative claim) would be stronger with at least one additional, more realistic outlier type.

- **No computational cost analysis is provided.** Bilevel optimization with extra forward/backward passes through the MLP and validation loss evaluation typically increases training time. The paper does not report training time relative to vanilla KD or the closest baselines, making it difficult for practitioners to assess the cost of the improvement.

## Nice-to-Haves

- Re-implementing WLS-KD under the same controlled conditions (with standard deviations) would allow direct statistical comparison and strengthen the paper's strongest claims.
- An analysis of which features the learned MLP assigns weight to (since the input is interpretable — edges and vertices of the trilateral geometry) could provide insight into what the method is actually learning.
- Clarifying whether the teacher on HIL/Criteo was also trained with oversampling would resolve the confound.

## Removed Points

- *RW-KD re-implementation performs unusually poorly compared to original paper*: Removed because the asserted inconsistency with the original RW-KD paper cannot be verified from the paper under review alone.
- *Missing related works*: Removed per instructions — I cannot verify completeness of related work coverage without exhaustive external knowledge.
- *Formatting/style nitpicks and typo-level issues*: Removed per instructions (these are parser artifacts, not author errors).
- *Reproducibility concerns about undisclosed hyperparameters (beyond bilevel optimization)*: Removed per instructions — trivial implementation details are not required to be in the paper.
- *Strength: "the paper addressed an important problem"*: Removed as generic/superficial.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight an interesting tension: the ablation study reveals that using only the SG+TG relations (which prior work WLS-KD and RW-KD rely on) yields performance *worse* than a fixed α when fed through a learned MLP. This suggests that the advantage of methods like WLS-KD may come as much from their *heuristic decision rules* as from the information in SG+TG — and that simply feeding the same information into a learned function does not automatically recover those benefits. This observation, if substantiated, would be a useful caution for future work in learned fusion ratios.

## Suggestions

1. Re-implement WLS-KD under the same conditions (with standard deviations over multiple runs) for the main CIFAR-100 table so that the comparison against the strongest baseline is controlled and statistically testable.
2. Either (a) clarify that the teacher on HIL was also trained with the oversampled data, or (b) remove or explicitly qualify the "student beats teacher" claim, or (c) conduct an experiment isolating the effect of oversampling from the effect of TGeo-KD.
3. Provide the missing bilevel optimization details: number of inner steps, learning rates for inner/outer loops, train/validation split ratio, and the specific technique used to compute the outer gradient.
4. Discuss the SG+TG-only ablation's underperformance relative to vanilla KD.
5. Add training time comparison against vanilla KD and the closest baselines.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>