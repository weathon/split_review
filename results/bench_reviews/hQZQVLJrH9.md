Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper proposes a first-order theoretical framework that unifies activation steering and influence functions, two previously separate paradigms in neural network interpretability. The key result is a duality: any steering vector can be represented as a signed influence weighting over training data (Theorem 4.2), and vice versa. The paper introduces Influence-Aligned Steering (IAS), a principal-angle diagnostic γ that bounds steering fidelity, a spectral-optimality recipe for choosing steering directions, and generalization bounds for low-rank steering. Experiments on GPT-2 Medium and ResNet-50 provide partial validation of the first-order theory but do not test the paper's central practical claim — that IAS enables tracing steering vectors back to causal training examples.

## Strengths

- **Steering–influence duality (Theorem 4.2):** The paper proves a constructive first-order equivalence between activation-space interventions and training-data influence weightings. This is a genuinely novel conceptual bridge between two active but previously disconnected areas of interpretability research — it is the paper's strongest contribution.

- **Alignment diagnostic γ (Theorem 5.1):** The cosine of the smallest principal angle between the activation-Jacobian and parameter-Jacobian subspaces provides a tight bound (√(1−γ²)) on steering fidelity. γ is computable from two small SVDs, making it a practical, principled criterion for deciding whether to steer or retrain. This is a well-motivated and useful theoretical tool.

- **First-order linearity validation (Figure 1):** Across 5,000 prompt–token pairs, the IAS-predicted logit shift is nearly collinear with the actual shift (cosine 0.978). This empirically confirms that the first-order theory holds at real model scale, which is a necessary foundation for all subsequent theoretical claims.

- **Layer-depth analysis of alignment (Figure 2):** The median γ increases monotonically from 0.64 to 0.94 across GPT-2 Medium layers, directly supporting the theory and giving practitioners an actionable layer-selection heuristic (pick later layers for better steering fidelity).

## Weaknesses

### Fatal
None.

### Major

- **The central practical claim is entirely untested.** The paper's abstract, introduction, and Section 4.1 promise that IAS provides "a constructive algorithm for mapping undesired behaviors back to causal training examples" and that practitioners can "pinpoint the fewest training examples to relabel/remove/examine." Despite this being the headline practical contribution, the paper presents *no experiment* that computes ρ_s for any steering direction, retrieves top-weighted training examples, inspects their content, or validates their causal relevance. The linearity check in Figure 1 only verifies that the first-order IAS logit shift is accurate; it does not test whether the data-level mapping is meaningful. This is a substantial gap between what the paper claims to deliver and what it actually demonstrates.

- **The generalization bound (Theorem 6.1) models a weight-space intervention, not activation steering.** The theorem states `f̃ = f_θ + αUV^⊤` as "the model obtained by adding a rank-k IAS correction at layer ℓ" and derives a Rademacher complexity bound by citing Pinto et al. (2024) on neural networks with low-rank layers. But IAS operates by adding a vector to *activations* during the forward pass — it does not modify weight matrices. The function class change under activation steering (where the perturbation can be input-dependent through the downstream layers) is fundamentally different from appending a fixed low-rank matrix to the output. Consequently, the risk bounds in Eq. (4) and the practical guidance to "prefer low ranks k" do not directly apply to the steering method introduced in the paper. This invalidates that portion of the paper's theoretical contribution.

### Minor

- **The spectral optimality experiment (Figure 3) does not fully validate Theorem 5.3.** The experiment shows that the spectral direction's spectral radius is statistically significant compared to random-label directions (p ≈ 0.005). However, this is a feature-salience significance test, not a validation that steering with the leading eigenvector of Σ maximizes expected logit change under an ℓ₂ budget. The paper never compares actual logit changes produced by the spectral direction against alternative candidate directions, nor demonstrates that the steering vector satisfies the norm budget while achieving the claimed optimum. The experiment provides suggestive evidence for Theorem 5.3 but does not constitute a proper validation.

- **Implausible detoxification perplexity numbers.** Table 1 reports baseline perplexity of 14,333 on WikiText for GPT-2 Medium. Standard GPT-2 Medium perplexity on WikiText is roughly 20–35; numbers three orders of magnitude higher suggest an unusual measurement protocol (e.g., per-character rather than per-token perplexity, or a highly non-standard subset). While the *relative* comparison between Baseline, CAA, and IAS may still be informative, the anomalous absolute values undermine confidence in the experimental setup.

### Trivial

- The subset-inclusion condition Im(J_{θ→y}) ⊆ Im(J_{h→y}) required for exact matching in Theorem 5.2 is never directly verified; only the principal-angle diagnostic γ is reported, which measures overlap but does not confirm subset containment.

- The explicit construction of ρ_s (the signed measure that maps a steering vector to data weights) is stated to exist in Theorem 4.2 but its formula is not provided in the main text — Corollary 1 refers to "the measure ρ_s constructed in Eq. 4" without giving the construction.

## Nice-to-Haves

- Comparison with additional activation-steering methods beyond CAA (e.g., Representation Engineering, STAR) would better contextualize IAS's detoxification performance.
- An analysis of how Hessian approximation and damping errors propagate through the IAS equivalence and diagnostics would strengthen the practical guidance.
- A more realistic cost model: the claim of "two backward passes per input" is accurate for IAS computation once Δθ is known, but Δθ itself requires influence computation over the training set, which is the dominant cost.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"No empirical evidence for the steering–data influence equivalence" as a fatal criticism:** The harsh critic correctly identifies this gap, but calling it "fatal" overstates the case. The theoretical results (Theorems 4.2, 5.1) have independent value and the linearity experiment (Fig. 1) validates the first-order framework. The data-tracing gap is a major weakness, not a fatal one — the theory is not invalidated, merely unvalidated at the data level.

- **Strength Finder's generalization guarantee as a strength:** This is removed because Theorem 6.1 models a weight-space intervention incorrectly under the IAS paradigm. The claimed generalization benefit is not reliably supported for activation steering.

- **Strength Finder's "the paper is well-written" and similar generic claims:** Removed as too generic.

- **Harsh critic's formatting/style nitpicks and demands for appendix material:** Removed per hard rules. The appendix was stripped by the parser and formatting artifacts are not author errors.

- **Harsh critic's "cost model" criticism about the claim of two backward passes:** Weakened rather than fully adopted, since the paper's claim is technically correct for the IAS step itself — it's the prerequisite influence computation that is expensive. Moved to Nice-to-Haves as a clarification suggestion.

## Novel Insights

The principal insight that activation-steering Jacobians and parameter-influence Jacobians are projections of the same underlying sensitivity tensor — and that a single principal-angle scalar γ characterizes when one can substitute for the other — is genuinely novel and provides conceptual clarity that neither the steering nor influence literatures had individually. The dual-view formulation (primal projection for minimum-norm steering, dual certificate for effort) connects these practical tools to convex analysis in a way that may inspire similar bridges in other interpretability subfields.

## Suggestions

1. The highest-impact addition would be a data-tracing case study: take a concrete steering vector (e.g., from the detoxification experiment), compute ρ_s, retrieve the top-k weighted training examples, and qualitatively assess whether they are semantically related to toxicity. Even a small-scale demonstration (e.g., on a subset of the training data) would substantially strengthen the paper.

2. Either remove Theorem 6.1 entirely or reformulate it to properly model activation-space interventions. A bound that accounts for input-dependent perturbation propagation through downstream layers would be a genuine contribution; the current weight-space formulation is misleading.

3. Clarify the perplexity metric in Table 1 — specify whether it is per-token or per-character, and which WikiText subset is used. If the numbers are correct under an unusual protocol, explain why the protocol was chosen.

4. For the spectral optimality experiment, add a direct comparison: measure the actual logit change produced by the spectral direction vs. the CAA direction vs. random directions, all under the same ℓ₂ norm budget.

---

### Anchor Comparison and Score Justification

| Anchor | Avg Score | Decision | Comparison |
|--------|-----------|----------|------------|
| COLD-Steer (afV4qzquBN) | 6.00 | Accept | Strong method with extensive empirical validation across tasks. Our paper has comparable theoretical ambition but far weaker empirical support for its central claim. |
| Bayesian IF (YEBpZVm70i) | 5.50 | Accept | Method paper with strong theory validated on retraining experiments. Our paper's theory is comparably interesting but empirical validation of the central claim is absent. |
| Influence Dynamics (8epkNiuAQC) | 4.67 | Accept | Theoretical framework with toy-model validation and LLM-scale evidence. Our paper has more theoretical machinery but less validation of its headline claim. |
| AUSteer (guSVafqhrB) | 4.67 | Accept | Method paper with extensive experiments. Our paper is more theoretically novel but empirically thinner. |
| Belief Dynamics (XyQ5ui62mm) | 4.50 | Reject | Theoretical unification paper that validates its predictions empirically. Our paper shares a similar theory-first profile but does not validate its main practical prediction. |
| Rogue Scalpel (uXecy0nKiJ) | 4.50 | Reject | Empirical paper with clear findings. Our paper is more theoretical but has a significant gap between claims and evidence. |
| Theorem Proving Steering (Gq7cBZC04L) | 3.50 | Reject | Application with minimal novelty. Our paper has substantially more theoretical novelty. |
| Painless AS (I3IeAZvxB4) | 3.33 | Reject | Good experiments, limited novelty. Our paper has the opposite profile — stronger theory, weaker experiments. |

The paper's genuine theoretical contributions — the steering–influence duality (Theorem 4.2), the γ diagnostic (Theorem 5.1), and the spectral optimality result (Theorem 5.3) — lift it above the 3.5-level rejected papers that offer primarily incremental applications. However, the central practical claim (data tracing) is entirely unsubstantiated, and the generalization bound (Theorem 6.1) is applied to a setting it does not cover. The linearity check (Fig. 1) validates the first-order framework but does not compensate for the absence of data-level validation. The paper reads as a theoretically promising manuscript whose empirical story is incomplete. Relative to the anchors, it sits below the accepted papers at 4.67–6.0 and near the rejected papers at 4.50, but its theoretical novelty is stronger than the 3.33–3.50 cluster. I assign a score of **4.0**.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>