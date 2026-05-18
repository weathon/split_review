Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper introduces *amicable perturbations*, a framework for finding efficient real-world changes to achieve more favorable classification outcomes. The framework formalizes three components — actionability (what changes are feasible), efficiency (domain-specific cost), and desirability (a target probability set with an $f$-divergence distance to it) — and generates perturbations by minimizing $d_{\mathcal{Y}}(M(\tilde{\mathbf{x}}),T) + \lambda d_{\mathcal{X}}(\tilde{\mathbf{x}},\mathbf{x})$ subject to actionable constraints. A novel verification procedure uses a pairwise classifier $V(\mathbf{x},\tilde{\mathbf{x}})$ (trained to predict whether two points share the same true class) and compares it against a product-of-probabilities estimate from $M$ to flag perturbations that may fool the classifier without changing the true underlying class. Experiments on four tabular datasets show that amicable perturbations achieve higher success rates at lower costs than counterfactual and adversarial baselines, and the verifier eliminates 100% of Carlini-Wagner adversarial examples.

---

## Strengths

- **Principled optimization framework with explicit cost, feasibility, and desirability.** The paper formally defines $(\epsilon,\delta)$-Amicable Perturbations using an actionable set $\mathcal{A}(\mathbf{x})$, a domain-specific cost $d_{\mathcal{X}}$, a target set $T$ (specified via probability thresholds on desirable/undesirable classes), and a continuously differentiable $f$-divergence distance $d_{\mathcal{Y}}$ (Theorem 1). This enables gradient-based optimization with precise goal specification, going beyond counterfactual methods that typically use $\ell_p$ norms and hard class-flip objectives.

- **Novel verification procedure that detects adversarial-like perturbations.** The verifier $V$ exploits access to both the original and perturbed points (unavailable in standard adversarial detection) and uses the discrepancy $\Delta = |V(\mathbf{x},\tilde{\mathbf{x}}) - \sum_i M_i(\mathbf{x})M_i(\tilde{\mathbf{x}})|$ as a test. The paper demonstrates that this procedure eliminates **100% of Carlini-Wagner adversarial examples** and rejects 14–27% of counterfactuals that appeared effective based on $M$ alone (Figure 5c), providing evidence that verification catches perturbations that change the classifier's output without genuinely altering the class.

- **Consistent empirical outperformance over counterfactuals and adversarial attacks.** Across all four datasets and multiple $\delta$ thresholds (Figure 5), amicable perturbations achieve higher success rates at lower costs. On German Credit with $\delta=0.5$, amicable perturbations move 73% of individuals within goal at **zero cost** (by closing empty accounts), whereas counterfactuals require 7,000 DM to reach comparable success rates. This supports the paper's claim that the framework finds more efficient real-world changes.

- **Concrete illustrations of the effort-reward trade-off.** Figure 4 provides case studies from Law School and Adult Income showing that amicable perturbations offer a spectrum from low-cost/low-reward to high-cost/high-reward options (e.g., $AP_1$: +11% success with mild changes; $AP_4$: +71% with substantial changes), while counterfactuals only produce high-cost options that often overshoot the goal.

---

## Weaknesses

### Fatal

None.

### Major

1. **The verification procedure lacks direct ground-truth validation against true class probabilities.** The paper claims the verifier detects perturbations that "fool the classifier without changing true class probabilities," but this claim is not directly tested. The evidence provided is: (a) 100% elimination of CW adversarial examples, and (b) removal of 14–27% of counterfactuals. Both are indirect. CW attacks are a specific type of perturbation optimized against $M$, not $V$ — their elimination does not guarantee that perturbations passing the verifier actually change $\tilde{\mathbf{y}}$ rather than just $M(\tilde{\mathbf{x}})$. The paper calibrates $\gamma$ to a 10% false rejection rate on *natural* different-class pairs from the test set, but never evaluates precision/recall on a held-out set of perturbations where the true class change is known (e.g., synthetic data with known ground-truth probabilities). Without this, the core claim that verification "helps ensure that changes will have the intended effect on the real world" (Section 2, end) is not convincingly supported. **Why this matters:** The verifier is a central claimed contribution; its reliability is essential to distinguish amicable perturbations from counterfactuals/adversarial examples.

2. **The verifier $V$ is trained on dataset pairs but applied to optimized perturbations that may be out-of-distribution.** $V$ is trained on pairs $(\mathbf{x}^{(i)},\mathbf{x}^{(j)})$ drawn from the original dataset. However, amicable perturbations $\tilde{\mathbf{x}}$ are optimized points that may not resemble any existing data point. The pair $(\mathbf{x},\tilde{\mathbf{x}})$ is thus potentially OOD for $V$. The threshold $\gamma$ is calibrated on test-set pairs (in-distribution), and there is no analysis of how $V$ behaves on OOD inputs or any use of calibration/rejection techniques for $V$ itself. **Why this matters:** It weakens confidence that the verification step is meaningful for the very perturbations it is meant to validate.

### Minor

3. **The experimental comparison conflates differences in objective function with differences in cost function design.** Amicable perturbations minimize $d_{\mathcal{Y}}(M(\tilde{\mathbf{x}}),T) + \lambda d_{\mathcal{X}}(\tilde{\mathbf{x}},\mathbf{x})$, where $d_{\mathcal{X}}$ is a domain-specific cost. Counterfactuals (Wachter et al., DICE) minimize a hard-class-flip loss plus $\ell_1$ penalty. The paper attributes the performance advantage to the target-set formulation, but part of the advantage may simply come from using better cost functions. A controlled ablation — holding $d_{\mathcal{X}}$ and the optimization procedure fixed and varying only the objective (target-set distance vs. hard-class flip) — would isolate the contribution of the soft-target formulation. **Why this matters:** The paper's claim that amicable perturbations "balance the effort-reward trade-off more effectively than counterfactuals" is somewhat confounded.

4. **Classifier accuracy for $M$ (and $V$) is not reported.** The paper states that neural networks are "tuned until they provide accuracy on par with gradient boosted tree models" but does not report actual accuracy numbers for any dataset. Since $M(\tilde{\mathbf{x}})$ serves as the surrogate for $\tilde{\mathbf{y}}$ throughout the optimization and evaluation, readers cannot assess whether $M$ is adequate for this role. **Why this matters:** If $M$ is a poor classifier, the entire pipeline (including the comparison with counterfactuals) rests on a weak foundation.

5. **No sensitivity analysis on the cost function and actionable set design choices.** Cost functions and actionable sets are defined ad hoc per dataset (e.g., moving to an adjacent region "weighted the same as increasing grades by one standard deviation"). The paper does not discuss how sensitive results are to these choices or whether alternative reasonable specifications would change the conclusions. **Why this matters:** The claimed superiority over counterfactuals could partly reflect favorable design choices rather than intrinsic advantages of the framework.

6. **The success metric after verification still uses $M(\tilde{\mathbf{x}})$ as the measure of success.** After the verifier filters perturbations with $\Delta > \gamma$, the reported success rates (green values in Figure 5c) still evaluate $d_{\mathcal{Y}}(M(\tilde{\mathbf{x}}),T) \leq \delta$. The verifier is assumed to catch cases where $M(\tilde{\mathbf{x}}) \neq \tilde{\mathbf{y}}$, but since the verifier itself is not directly validated against ground truth (Weakness 1), this creates a circular reliance on $M$'s outputs for both generation and evaluation.

### Trivial

- Theorem 1 is straightforward but useful — a closed-form differentiable expression for $f$-divergence to a linearly-constrained target set. The paper does not overclaim its novelty, stating it enables gradient-based optimization. This is not a real weakness.

---

## Nice-to-Haves

- **Validate the verifier against known ground truth.** A synthetic setting with known class probabilities (e.g., a generative model with known causal structure) where genuine amicable perturbations and adversarial examples are both generated, and the verifier's precision/recall is measured.
- **Controlled ablation isolating the target-set formulation.** Compare amicable perturbations against a version of the same optimization that replaces the target set $T$ with a hard class threshold, keeping $d_{\mathcal{X}}$ and the optimization method fixed.
- **Report accuracy of $M$ and $V$ for each dataset.**
- **Analyze $V$'s OOD behavior**, e.g., by measuring $\Delta$ on random perturbations of increasing magnitude to see how it degrades.
- **Compute and report the computational cost** of training $V$ and the iterative $\lambda$ adjustment loop.

---

## Removed Points

The following points from the harsh critic were removed after verification against the paper:

- **"Theorem 1 is not novel"** — This is an opinion about degree of novelty, not a factual weakness. The paper presents it as a building block, which is appropriate.
- **"The paper should also cover causality / SCMs"** — The paper explicitly scopes this as future work. Demanding this is scope creep.
- **"The argument that V learns different features is not justified"** — While the paper's justification is heuristic, this is a standard argument in adversarial robustness (different tasks learn different features). The critic does not provide evidence that this claim is false; it is a reasonable design motivation, not an unsupported empirical claim.
- **Formatting/typo criticisms** — Parser artifacts, not author errors.
- **"Counterfactuals and adversarial examples are created using similar methods" criticism** — The paper itself makes this point (citing Pawelczyk et al. 2022) as motivation for verification. The critic appears to have misread this as an inconsistency rather than the paper's own argument.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

- Add a synthetic experiment where true class probabilities are known (e.g., sampled from a Gaussian mixture with known class-conditional densities). Generate both genuine class-changing perturbations and adversarial perturbations that fool $M$ without changing the true label. Report the verifier's precision and recall on these held-out cases. This would directly address the most significant weakness.
- Add a controlled experiment: keep the cost function $d_{\mathcal{X}}$ and optimization algorithm fixed, and compare two objectives — (a) distance to target set $T$ vs. (b) hard class-flip loss. This isolates the benefit of the soft-target formulation from the benefit of the cost function.
- Report accuracy of $M$ and $V$ for all datasets, and include a brief analysis comparing $M$'s accuracy to gradient-boosted tree baselines.
- Discuss the computational overhead of the verification loop (training $V$, computing $\Delta$, iterative $\lambda$ adjustment) and its practical feasibility.

---

## Score and Decision

The paper introduces a well-motivated and principled framework for generating recourse recommendations with flexible goal specification, and the verification procedure is a novel attempt to address a real concern about classifier trustworthiness. The empirical results across four datasets are consistently positive. However, the verification procedure — a central claimed contribution — is not directly validated against ground-truth class probabilities, and the experimental comparison with counterfactuals is partially confounded by differences in cost function design. These issues are addressable with additional experiments but weaken the paper in its current form.

**Score:** 6.0  
**Decision:** Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>