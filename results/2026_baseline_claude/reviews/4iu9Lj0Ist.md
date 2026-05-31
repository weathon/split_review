---

## Summary

The paper introduces a theoretical framework for **certified machine unlearning within continual learning (CL)**, termed "continual learning-unlearning." It formalizes (ε,δ)-certified unlearning in the CL setting, provides new excess-risk bounds for ℓ₂-regularized CL extending prior linear results to nonlinear convex models, and adapts two canonical unlearning paradigms—gradient-based (natural forgetting, Alg. 1) and Hessian-based (Alg. 2)—to the CL framework. Theoretical guarantees on both the unlearning loss and the CL excess risk are derived, and their combination determines the post-unlearning excess risk. Experiments on MNIST with a linear model validate the trade-off between λ, excess risk, and unlearning loss.

---

## Strengths

- **First formal framework for CL-unlearning**: The two-stage formulation (Stage I: ℓ₂-CL, Stage II: certified unlearning) with Definition 2.1 and the post-unlearning excess risk decomposition into equations (6)+(7) is clean and principled. Prior work in this space (Liu et al. 2022, Chatterjee et al. 2024) lacks any formal guarantee; this paper closes that gap.

- **Extension of excess-risk bounds from linear to convex nonlinear models (Theorem 3.1)**: Extending Lin et al.'s linear-model bounds to general strongly convex and smooth losses with non-i.i.d. sequential tasks is a genuine theoretical advance. The resulting bound correctly characterizes how task heterogeneity (‖w*_i − w*_j‖) and data sizes interact, and shows that the bound does not vanish even with infinite data—a key insight absent from prior work.

- **Two complementary algorithms with clear trade-offs**: Alg. 1 is zero-storage and leverages natural forgetting to achieve small unlearning loss for early-task deletions. Alg. 2 stores Hessians and model updates for more accurate second-order approximations. The forgetting-enhanced variant of Alg. 2 (Section 5.3) partially bridges the gap. The theoretical analysis cleanly exposes the λ trade-off: large λ helps unlearning but hurts CL excess risk.

- **Order-sensitivity of Hessian unlearning (Proposition 5.1 and Lemma 5.4)**: The result showing that out-of-order unlearning requests introduce additional error terms in (14), while a well-ordered retirement pattern simplifies the correction to a single product chain, is a novel and practically actionable insight. It motivates regulating request arrival order and has no analog in prior unlearning theory.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **Disconnect between theoretical assumptions and experiments.** All theoretical results (Theorems 3.1, 4.1; Propositions 5.1–5.2) require μ-strong convexity (Assumption 2.1). The experiment section explicitly states this assumption is *relaxed*—the linear softmax+cross-entropy model used is **not** strongly convex. As a result, none of the theoretical bounds are directly applicable to the experimental setting, and it is unclear whether the experiments are validating the theory or simply providing empirical observations in a related but different regime. This gap significantly weakens the claim that theory is "validated" by experiments.

2. **Table 1 anomaly: unlearning algorithm outperforms oracle.** At λ=30, the Hessian-based unlearning achieves 71.59% test accuracy while "perfect retraining" achieves 71.05%. The post-unlearning excess risk is defined as the gap relative to the oracle retrained model; a negative gap means the unlearning algorithm somehow outperforms perfect retraining. This is either a finite-sample artifact, a measurement issue, or an inconsistency in the experimental setup. The paper provides no explanation, which undermines confidence in the experimental results.

3. **Storage of Alg. 2 scales as O(td² + 2td).** For the Hessian-based algorithm, storage grows linearly with the number of tasks t and quadratically with model dimension d. The forgetting-enhanced variant reduces this to O((t_i − t_{i-1})(d² + 2d)) proportional to the inter-request gap, but this is discussed only briefly and no experiments quantify how large this gap needs to be in practice for the storage to be manageable. For any moderately sized model, this renders Alg. 2 impractical, a gap not adequately bridged.

### Minor

1. **The approximation error bound (14) in Proposition 5.1 is very complex.** While the claim that Hessian-based achieves a tighter bound than natural forgetting (9) is stated throughout, the actual comparison of formulas (9) vs. (14) is never made explicit—(14) involves three nested summation terms with different exponential factors. It is non-trivial to see why (14) is uniformly tighter, and no lemma/corollary establishes this comparison formally.

2. **Algorithm 1 privacy of internal model.** Section 4 acknowledges that the internal (secret) model w_t still retains information from deleted tasks. While an extension is noted in Appendix C.2, this is a fundamental concern for the primary algorithm: the published model is (ε,δ)-certified but the model used for future training is not. Real-world CL deployments may require the stronger guarantee.

3. **Only one dataset (MNIST) and one architecture (linear).** A theory paper may naturally focus on linear/convex settings, but having any additional experiment (e.g., Fashion-MNIST, simple MLP) would strengthen the empirical story. Appendix E with "sequence patterns" analysis is referenced but not accessible from the main text.

### Trivial

- Table 2 (referenced in Section 6.1 for the unlearning sequence) is never shown in the main body, only referenced. This is likely a formatting artifact.

---

## Nice-to-Haves

- A formal comparison theorem (or even a corollary) directly showing when γ_t in (14) is tighter than γ_t in (9) would significantly strengthen the "Hessian-based largely outperforms gradient-based" claim made in the abstract.
- Adding a strongly convex experimental setup (e.g., ridge regression with known μ) would make the empirical validation directly applicable to the theoretical bounds.
- A concrete discussion of how to choose λ in practice (given the trade-off between CL excess risk and unlearning loss) would improve the paper's utility to practitioners.

---

## Novel Insights

The paper's most genuinely novel insight is the **order-sensitivity of Hessian-based continual unlearning**: when unlearning requests arrive out of chronological order (e.g., requesting deletion of task 1 at time t=5 when task 3 was deleted at t=3), the second-order correction involves non-trivial interference terms that can substantially inflate the approximation error. This stands in sharp contrast to standard (non-CL) unlearning, where request order is irrelevant. The converse—that a "well-ordered retirement pattern" where each new request covers only tasks trained since the last unlearning event eliminates the interference—is a structurally clean result (Lemma 5.4) that could motivate request scheduling strategies in real systems.

---

## Suggestions

- Provide a direct analytical comparison between bounds (9) and (14) to formally justify why Hessian-based is tighter, rather than relying solely on qualitative argument.
- Include at least one experiment under strong convexity (e.g., ℓ₂-regularized logistic regression with explicit μ) to close the gap between Assumption 2.1 and the experimental setting.
- Clarify the Table 1 anomaly (unlearning > oracle accuracy at λ=30) with either an explanation or acknowledgment of finite-sample noise.
- Discuss a practical strategy for choosing λ given joint excess-risk/unlearning-loss objectives, ideally with a worked example.

---

## Score and Decision

The paper makes a genuine and timely theoretical contribution—the first formal framework for certified unlearning in the CL setting, with non-trivial bounds and novel insights on request-order sensitivity. The proofs appear technically sound for the convex setting, and the framework is well-motivated. However, the major mismatch between theoretical assumptions (strong convexity) and experiments (non-strongly-convex), the unexplained performance anomaly in Table 1, and the impractical storage of the Hessian method limit confidence in the completeness of the contribution. For a theory paper, stronger alignment between theory and experiments would substantially increase the score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>