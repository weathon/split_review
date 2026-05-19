- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6
Here is my consolidated review.

---

## Summary

This paper introduces a multiobjective optimization framework (MGF-IMM) for diverse human motion in-betweening. The key idea is to formulate the task as a bi-objective problem (diversity + smoothness) and use a non-dominated sorting evolutionary algorithm (NSGA-II) integrated with a pretrained generative model (VAE/GAN/DDPM) to produce a Pareto-optimal batch of motion sequences in a single pass. The method claims to improve intra-batch diversity without retraining the generator.

## Strengths

1. **Novel connection between multiobjective optimization and batch diversity for generative models.** The idea of framing batch diversity as an explicit optimization objective and leveraging NSGA-II's inherent population-based parallelism is creative and well-motivated. The paper correctly identifies that existing generative models can produce diverse samples through different noise seeds but lack a mechanism to *guarantee* diversity across a batch, and the EA framework provides a natural solution. This direction is underexplored in the motion generation literature.

2. **Consistent empirical improvement across multiple backbones and datasets.** Table 1 (reported) shows that MGF-IMM improves the diversity metric (APD) compared to baselines on all four datasets (BABEL, HumanAct12, NTU RGB-D, GRAB) and across three generative backbones (VAE, GAN, DDPM). The improvement is maintained while also matching or improving accuracy metrics.

3. **Ablation studies that isolate the framework's contribution.** Table 3 compares each generative model "with" vs. "without" the multiobjective framework and shows consistent gains. Table 4 further ablates the intra-class term P_c(Y). These ablations provide evidence that the performance improvement is attributable to the specific framework design rather than unrelated factors.

4. **Adaptive sequence-length mechanism with empirical validation.** Equation (6) determines motion length based on cosine similarity between keyframes, and Table 2 shows this variable-length scheme outperforms fixed-length alternatives across RMI, MITT, MultiAct, and CMIB baselines. This is a practical improvement.

## Weaknesses

### Major

1. **The evolutionary conditioning mechanism is underspecified to the point of non-reproducibility.** Equation (5) defines offspring generation as `Y_i^{[n]} ~ G(Y_i^{[n]} | Y_{i-1}^{[n]}, X₁, X₂)` — the generator is conditioned on the previous population member. However, Section 4.2 describes the VAE architecture as having an encoder `q_θ(Z|Y, X₁, X₂)` and a decoder `G(Ŷ|Z, X₁, X₂)`, with no component that accepts a motion sequence `Y_{i-1}^{[n]}` as conditioning input. The paper simply asserts that the generator "is conditioned not only by the user-provided sequences but also by the sequences already generated" (line 109) without specifying the mechanism (e.g., latent-space interpolation, cross-attention injection, separate encoder for the previous solution). Since this conditioning is a core algorithmic step that drives the evolutionary search across iterations, its underspecification prevents independent implementation and verification. **This is the most critical weakness.**

2. **The classifier `C(Y)` is a black box.** The entire diversity component depends on a classifier that provides both the discrete class label `C(Y)` and the softmax probability `P_c(Y)` for a motion sequence. The paper merely says "We assume the availability of a classifier" (line 47) and provides no information about: the classifier's architecture, training data, accuracy on each dataset, or how its quality affects the optimization. The classifier could introduce significant bias — if it mislabels motions, the objective will reward incorrect diversity. Without any characterization, the evaluation results are uninterpretable and the method cannot be reproduced.

3. **The objective `α₁ = (C + P_c)/D` adds quantities on incompatible scales without justification.** `C(Y)` is an integer class label ∈ {0, …, D−1}, and `P_c(Y)` is a softmax probability ∈ [0, 1]. Their sum has no clear physical meaning — the integer label dominates the probability except when D is very small (and both sum to a range [0, D] which is then normalized to [0, 1]). The paper never justifies why this specific mixture represents "diversity" or why adding a discrete label to a probability is meaningful. While this does not necessarily invalidate the empirical results (the method may still work in practice), it undermines the claimed theoretical foundation and raises questions about what the objective is actually optimizing.

### Minor

4. **The multiobjective framework improves accuracy metrics (FID, ACC, ADE) as well as diversity (APD), but this is not explained.** Table 3 shows that adding the framework consistently improves FID and ACC alongside APD. Since the framework is designed to promote diversity rather than per-sample quality, this simultaneous improvement requires justification. Possible explanations exist (e.g., the Pareto selection may filter out poor-quality samples) but the paper offers none, leaving readers to wonder whether the classifier inadvertently acts as a quality oracle that provides an unfair advantage over baselines.

5. **No variance or statistical testing is reported.** Table 1 reports single numbers without standard deviations, confidence intervals, or number of runs. Given the stochastic nature of both generative models and evolutionary algorithms (initialization, mutation, selection), the reliability of the claimed improvements cannot be assessed.

6. **FID computation details are entirely absent.** The paper defines `FID_tr` and `FID_te` but never describes: which feature extractor is used, how reference statistics are computed, or how many samples are drawn. Without these details, the reported values (e.g., 0.31–0.48 on BABEL) are unverifiable. The paper should also clarify whether baselines use the same FID computation protocol.

7. **APD (Average Pairwise Distance) is never formally defined.** The metric is mentioned by name only (Section 5.3); no formula, distance measure (e.g., joint-position Euclidean?), or averaging procedure is provided. This makes the primary diversity metric ambiguous.

8. **Theorems 1 and 2 are technically correct but their practical significance is limited.** Theorem 1 states that any minimizer of β (smoothness) is Pareto optimal — this is a direct algebraic consequence of the formulation `F₁=α₁+β, F₂=(1-α₁)+β` and does not provide non-trivial insight into why the multiobjective framework yields diverse motions. Theorem 2 shows that distant points in objective space correspond to different class labels, which confirms that the objective separates motions by category but does *not* guarantee diverse motions *within* the same category (the "intra-class" diversity that the P_c term is meant to address). The theorems support the framing correctly but are shallower than the paper's tone suggests.

### Trivial

- None that survive filtering beyond the above.

## Nice-to-Haves

- Include a limitations section discussing dependence on the classifier, computational cost (400 generator forward passes per batch + classifier evaluations), and scope of intra-class vs. inter-class diversity.
- Report the effect of varying population size and max iterations on the trade-off between diversity and computational cost.
- Clarify whether baselines like ACTOR and MultiAct (originally text-to-motion models) were adapted for the in-betweening task, and if so, how.

## Removed Points

These points were raised by reviewers but are removed (with brief justification):

- **"FID values are implausibly low (0.31)"** — Removed. Without knowing the specific FID setup (feature extractor, reference statistics), these values cannot be declared implausible. Motion generation FID can vary widely depending on the feature space used; some action-recognition-based FIDs are naturally lower than ImageNet-based FIDs. The missing-details concern (retained as Minor weakness #6) is sufficient.
- **"Baseline comparison is unfair (single-sample APD vs. batch APD)"** — Removed. The paper does not describe how baseline APD was computed, so this is speculative. The critic assumes unfairness without evidence from the paper.
- **"No additional training claim is misleading"** — Removed. The paper's claim refers specifically to the generator not requiring retraining. The classifier is a separate pretrained component, and its use does not contradict the stated claim.
- **"ACTOR and MultiAct are text-to-motion, not in-betweening models"** — Removed per rule: if the asymmetry in baseline comparison favors the author's method (which it does here — text-to-motion models would naturally perform worse on in-betweening), this criticism should not be retained.
- **"Smoothness only measures boundaries, not internal motion"** — Removed. This is a design choice, not a flaw. The generator itself produces internally smooth motions; β intentionally measures only the transition to user-provided keyframes, which is exactly what an in-betweening smoothness metric should capture.
- **"No code or supplementary material"** — Removed. This is a reproducibility nitpick that does not address a specific scientific gap. The underspecified classifier and conditioning mechanism (kept as Major weaknesses) capture the substantive reproducibility concerns.
- **"Population size and EA hyperparameters require tuning"** — Removed. This is a generic concern applicable to any EA-based method and does not constitute a specific weakness of this paper.

## Novel Insights

None beyond the paper's own contributions. The three reviewer perspectives (harsh criticism, strength enumeration, human calibration) converged on identifying the same core tension: the paper's central idea — using multiobjective optimization to improve batch diversity — is genuinely novel and supported by positive empirical evidence, but the execution has significant gaps in specification (the conditioning mechanism, the classifier, the metric definitions) that prevent full validation. No novel synthesis emerged beyond this tension.

## Suggestions

1. **Specify the conditioning mechanism in full detail.** Provide the exact architectural change that allows the generator to accept `Y_{i-1}^{[n]}` as conditioning input (e.g., encoding it to condition the latent prior, using it as a cross-attention key/value in the decoder, or concatenating it with the noise input). Without this, the core algorithm cannot be implemented.

2. **Document the classifier completely.** Report its architecture, training procedure, dataset splits, accuracy per action class, and an ablation comparing a perfect oracle vs. the learned classifier to assess its impact on the optimization.

3. **Reformulate or justify the diversity objective.** Either replace `(C + P_c)/D` with a more interpretable diversity measure (e.g., pairwise MMD, repulsive loss, or explicit within-class variation via latent-space distances) or provide a clear justification for why adding an integer class label to a softmax probability is meaningful for the optimization.

4. **Provide standard deviations and metric definitions.** Run multiple seeds and report means ± std. Define APD with its exact formula and distance metric. Describe the FID computation (feature extractor, reference set, number of samples).
