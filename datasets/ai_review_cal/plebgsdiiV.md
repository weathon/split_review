- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6
Now I have a thorough understanding of the paper and have verified the reviewer claims. Let me write the final consolidated review.

## Summary

This paper proposes KMIFQE, a method for off-policy evaluation (OPE) of deterministic policies in continuous action spaces. The core idea is to relax the deterministic target policy with a Gaussian kernel so that importance resampling—otherwise inapplicable to deterministic policies—can estimate the TD update vector in an in-sample manner, avoiding extrapolation error. The paper derives the bias-variance trade-off of the kernel-relaxed estimator, provides closed-form solutions for the optimal bandwidth (Proposition 1) and optimal metric (Proposition 2), offers an error-bound analysis (Theorem 2), and evaluates on Pendulum, MuJoCo, and D4RL domains.

## Strengths

- **Closed-form optimal metric via Hessian-based analysis (Proposition 2):** The paper derives an analytic solution for the optimal metric $A^*(\mathbf{s}')$ that minimizes an upper bound on the bias constant vector, using the Hessian of the learned Q-function. This is a non-trivial theoretical contribution that goes beyond straightforward adaptation of bandit results and directly supports the claim of providing analytic solutions for the optimal kernel metric.

- **Explicit bias-variance decomposition for the IR-based TD update (Theorem 1, Corollary 1):** Theorem 1 derives the leading-order bias (Eq. 6) and variance (Eq. 7) of the kernel-relaxed TD update vector and combines them into an MSE (Eq. 9). This enables the subsequent optimal bandwidth derivation in Proposition 1 and provides a formal understanding of the trade-off specific to this setting, which was not done in prior in-sample learning works for deterministic policies.

- **Error-bound analysis linking relaxation to the evaluation gap (Theorem 2):** Theorem 2 provides a bound on $\|Q^\pi - \lim_{m\to\infty} T_K^m Q\|_\infty$ that depends on the bandwidth $h$ and metric $A(\mathbf{s}')$, and shows that the optimal metric from Proposition 2 reduces this gap. This extends the theoretical guarantee beyond the contextual-bandit setting to MDPs.

- **Empirical validation of bias dominance and metric effectiveness (Figure 1):** Figure 1(a) shows that as dummy action dimensions increase, bias dominates variance, validating Proposition 3. Figure 1(b) shows that learned metrics reduce bias across all bandwidths and that the learned bandwidth balances bias and variance near the MSE minimum, validating both Propositions 1 and 2.

- **Competitive performance on controlled MuJoCo tasks (Table 1, known $\mu$):** On MuJoCo domains with a known behavior policy—where the comparison is clean—KMIFQE achieves the lowest RMSE on 4 out of 5 environments (Hopper, Walker2d, Ant, Humanoid), with large margins on Walker2d and Humanoid where FQE produces high errors due to extrapolation.

## Weaknesses

### Fatal
None.

### Major

- **Practical estimation of the optimal bandwidth and metric is underspecified, making the method irreproducible in its current form.** The optimal bandwidth $h^*$ (Eq. 14) involves constants $\mathbf{b}$ and $v$ that depend on expectations over the data distribution of terms involving the *unknown true* $Q^\pi$ (via $\|\nabla_\theta Q_\theta\|^2$, Hessians of $Q_{\bar{\theta}}$, etc.). The paper states only (line 195) that "the actual algorithm iterates between learning $h^*$, $A^*$, and learning $Q_\theta$" but provides no detail on how these constants are estimated from data, how the Hessian is computed (e.g., through automatic differentiation or finite differences), how the bias and variance constants are approximated without access to the true TD update vector, or what the convergence criteria for the iterative procedure are. Similarly, the optimal metric $A^*$ requires computing eigendecompositions of Hessian matrices for each state, but no sample-based estimation procedure is given. Without this detail, the claimed theoretical optimality cannot be verified by practitioners, and the method cannot be implemented from the paper alone. This is the single most significant gap in the present manuscript.

### Minor

- **The metric optimization minimizes an upper bound on bias, not the bias itself, and the gap is unquantified.** The paper correctly notes (line 172) that directly minimizing the squared bias $\|\mathbf{b}_A\|_2^2$ is intractable and shifts to minimizing the upper bound $U(A)$ (Eq. 13). The solution in Proposition 2 makes this upper bound zero for states where the Hessian has both positive and negative eigenvalues, but the tightness of the bound relative to the true bias is not analyzed. The paper should either bound the gap or discuss conditions under which the bound is tight.

- **No discussion of computational cost.** The method requires: (a) computing Hessians of $Q_\theta$ with respect to actions for every transition (or state in a mini-batch), (b) performing eigendecompositions of these Hessians for each state where the metric is learned, and (c) iterating between metric learning and Q-learning. For high-dimensional action spaces and neural-network Q-functions, this is expensive. The paper provides no runtime comparison to baselines, which would be informative for practitioners.

- **Assumption 1 (support coverage) may be violated in practice, with no discussion of how it is handled.** Assumption 1 (line 111–114) requires that the behavior policy's support covers the kernel's support. In the D4RL experiments, KMIFQE uses a tanh-squashed mixture-of-Gaussians as the estimated behavior policy (line 300), which has bounded support (due to tanh), while the Gaussian kernel has unbounded support. This violation can produce extreme or undefined importance weights. The paper does not discuss how this is handled (e.g., clipping, truncation, density estimation adjustments).

- **D4RL experiments compare KMIFQE (using an MLE behavior policy) against behavior-agnostic baselines, introducing a confound.** As noted in the paper (line 195, line 229, line 300), KMIFQE uses a maximum likelihood estimated behavior policy for D4RL experiments, while SR-DICE and FQE are behavior-agnostic. Prior work (Hanna et al., 2019) shows that using an estimated behavior policy can itself improve IS-based OPE. The known-behavior-policy experiments (Section 4.2) provide a controlled comparison and partially address this, but the D4RL results—presented in the same table as a head-to-head comparison—do not cleanly isolate whether gains come from the kernel metric method or from the behavior policy estimation. A baseline that also uses the same estimated behavior policy (e.g., an FQE variant with behavior-policy-weighted TD targets) would resolve this.

- **The evaluation metric (RMSE) is not explicitly defined.** The paper reports "root mean squared errors (RMSEs)" (line 262) but does not specify the quantity over which RMSE is computed (presumably RMSE of the estimated $V^\pi$ against the true $V^\pi$). This should be stated explicitly for clarity.

### Trivial

- **Typo in the stationary distribution definition (line 57):** $d^\mu(\mathbf{s})$ is defined with $\mathbf{a}_t \sim \pi(\mathbf{a}_t \mid \mathbf{s}_t)$ in the last subscript; it should be $\mu$, not $\pi$, since $d^\mu$ is the stationary distribution induced by the behavior policy.

- **No limitations section.** The paper would benefit from a brief discussion of key limitations (need for differentiable Q-function, support coverage assumption, computational overhead, reliance on behavior policy estimation when the true behavior is unknown).

## Nice-to-Haves

- A dedicated subsection describing the sample-based estimators for $\mathbf{b}$ and $v$ (e.g., using current $Q$-network approximations, Monte Carlo averages over mini-batches, and automatic differentiation for Hessians), along with the iterative procedure's convergence criteria.
- An experiment (synthetic or on Pendulum) comparing the upper-bound-minimizing metric with a metric found by direct (expensive) minimization of the empirical bias, to validate the bound's usefulness.
- A baseline on D4RL that uses the same estimated behavior policy (e.g., IS-weighted FQE) to isolate the effect of the behavior model from the effect of metric learning.
- A brief runtime comparison against baselines.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Figure 1a is missing error bars"** — REMOVED. The caption explicitly states "The shaded area is the region within one standard error" and "All experiments are repeated for 10 trials." The error visualization is present.
- **"Abstract overclaims by not acknowledging the upper-bound nature"** — REMOVED. The abstract states the paper's contributions at an appropriate level of generality; it does not misrepresent the method.
- **"Section 4.1 should clarify that MSE is the expected squared Euclidean norm"** — REMOVED. The paper defines $\operatorname{Var}[\mathbf{z}] := \operatorname{tr}[\operatorname{Cov}(\mathbf{z}, \mathbf{z})]$ and the MSE in Eq. (9) as the sum of squared bias and variance, which makes the interpretation clear.
- **"Missing related works"** — REMOVED. Cannot be verified without external sources.
- **"Missing appendix/proofs"** — REMOVED. The parser strips these sections from all papers; they exist in the original submission.
- **"Proposition 2 should note that $|M(\mathbf{s}')| > 0$"** — REMOVED. The reviewer's own analysis confirms the matrix is positive definite; this is a minor clarification, not a weakness.
- **"HalfCheetah explanation is not tested"** — REMOVED. The explanation is a plausible qualitative observation; testing it is beyond the paper's scope.
- **"The error bound is a worst-case bound and likely loose"** — REMOVED. The paper already acknowledges this (line 222: "While $h=0$ seems to be always preferred in Theorem 3, it is because it only considers the exact policy evaluation without any estimation error by using finite samples.").

## Novel Insights

None beyond the paper's own contributions. The paper's core novelty—applying kernel metric learning with closed-form solutions for bandwidth and metric to the in-sample OPE of deterministic policies in MDPs—is well articulated by the authors themselves. The reviewer inputs did not surface any genuinely novel observation about the paper that was not already present in the paper's own framing.

## Suggestions

1. **Add an implementation subsection** (in the main paper or a clearly referenced appendix) that describes how $\mathbf{b}$ and $v$ are estimated from data: which approximations are used for the unknown $Q^\pi$, how the Hessian is computed (e.g., `torch.autograd`), how mini-batch Monte Carlo averages replace the population expectations, and how the iterative procedure between learning $h^*$, $A^*$, and $Q_\theta$ is scheduled and when it converges. This is essential for reproducibility.

2. **Acknowledge the upper-bound nature explicitly** and, if feasible, add a small-scale experiment that compares the upper-bound-minimizing metric to a directly optimized (expensive) metric to validate the bound's practical usefulness.

3. **Add a controlled D4RL baseline** that uses the same MLE behavior policy (e.g., an IS-weighted variant of FQE) to separate the benefit of the behavior model from the benefit of metric learning.

4. **Define the RMSE metric explicitly** (e.g., "RMSE of the estimated $V^\pi$ across 10 seeds relative to the true $V^\pi$ computed by Monte Carlo rollouts").

5. **Discuss the practical handling of Assumption 1** when the behavior policy has bounded support (e.g., tanh squashing) and the kernel has unbounded support.

6. **Fix the typo in Eq. (3)** ($\pi$ should be $\mu$ in the definition of $d^\mu$).
