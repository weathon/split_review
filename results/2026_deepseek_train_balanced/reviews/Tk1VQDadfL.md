Now let me write the final consolidated review.

## Summary

This paper proposes UTILITY, a framework that uses explainable RL (XRL) to improve a suboptimal RL agent. It first generates a two-level explanation of *why* the agent is suboptimal — a high-level explanation via IRL (comparing the learned reward function to the ground truth) and a low-level explanation identifying "misleading" state-action pairs via a Q-value gap metric. It then formalizes using these explanations for improvement as a constrained bi-level optimization problem, solved by a triple-loop algorithm with convergence analysis.

## Strengths

1. **A feasible, mathematically grounded metric for identifying misleading state-action pairs.** Definition 1 ($l(s,a) = \max_{a'}Q_r^{\pi_A}(s,a') - Q_r^{\pi_A}(s,a)$) provides a principled way to pinpoint which specific *actions at which states* lead to suboptimality, using only quantities that are accessible (via IRL-imitated policies and environment interaction). This goes beyond prior XRL-based improvement methods (Guo et al., 2021b; Cheng et al., 2023, 2024) that identify influential *states* but do not isolate the problematic actions or explain *why* the agent is non-optimal.

2. **A dual-based transformation that converts a non-convex constrained bi-level problem into an equivalent unconstrained problem with a convex lower level.** Section 4.2.1 introduces the dual function $G(\lambda;\theta)$ and Theorem 2 establishes that the lower-level solution is uniquely characterized by the constrained soft policy $\pi_{\lambda^*(\theta);\theta}$ where $\lambda^*(\theta)$ solves a convex dual problem. This is a non-trivial theoretical contribution given that existing constrained bi-level optimization methods (Xu & Zhu, 2023; Khanduri et al., 2023) require strongly convex lower-level problems, while this one is non-convex (explicitly acknowledged in lines 20, 73).

3. **End-to-end convergence guarantees with explicit approximation error bounds at each of the three loops.** Lemma 3 bounds inner-loop soft-policy-iteration error as $O(\gamma^{\tilde{N}_{\bar{n}}})$. Lemma 4 bounds middle-loop dual-variable error as $O(1/\bar{N}^{1-\bar{\eta}})$ and policy error as $O(1/\bar{N}^{1-\bar{\eta}} + \gamma^{\bar{N}})$. Theorem 3 bounds outer-loop stationarity as $O(1/N^{1-\eta} + 1/\bar{N}^{2-2\bar{\eta}} + \gamma^{2\bar{N}})$. This stacked-error quantification for a triple-loop RL optimization algorithm is rare in the literature.

## Weaknesses

### Fatal

1. **The experiment section contains zero results, leaving the paper's central empirical claims entirely unsupported.** Section 5 (lines 143–144) describes three baselines (RICE, SIL, LIR) and states that SAC is the base algorithm, then terminates mid-sentence: "We aim to show the..." — followed immediately by the conclusion section. There are no tables, figures, learning curves, numerical results, error bars, or any other form of experimental evidence. Yet the abstract claims "We use MuJoCo experiments to show that our method outperforms state-of-the-art baselines," and the contribution statement (line 22) claims "Experiments show that UTILITY outperforms state-of-the-art baselines." These claims are central to the paper's contribution and are entirely unsubstantiated in the submitted manuscript. This is not a missing-ablation or limited-benchmarks issue; it is the complete absence of the experiments that the paper promises. No amount of theoretical contribution can substitute for the missing empirical validation of a claimed practical improvement.

### Major

2. **The "global optimality" claim is misleadingly framed.** The abstract and contribution statement assert that the algorithm "theoretically guarantees... global optimality" and "attains global optimality." However, the general result (Theorem 3, lines 139–140) only proves convergence to a *stationary point*: $\frac{1}{N}\sum_{n=0}^{N-1}||\nabla J_r(\pi_{\lambda^*(\theta_n);\theta_n})||^2 \leq O(\dots)$. The stronger global optimality result (Theorem 4, lines 141–142) requires that "the state-action space is finite and $r_\theta$ is linear" — conditions that do not hold for the MuJoCo continuous-control tasks the paper claims to evaluate on. The paper presents this as a general theoretical strength ("the algorithm attains global optimality") when the general guarantee is strictly convergence to stationarity, and the global optimality guarantee applies only under assumptions that exclude the paper's own claimed experimental domain.

3. **The meaningfulness of the high-level explanation is not adequately justified.** The high-level explanation learns a reward function $\hat{r}$ via IRL such that the agent's policy $\pi_A$ is optimal with respect to $\hat{r}$, then compares $\hat{r}$ to the ground truth $r$ to explain *why* the agent is suboptimal. However, a basic property of IRL is that *any* policy can be made optimal for *some* reward function — the IRL objective is precisely to find a reward function that rationalizes the observed behavior. The paper does not address the question of whether the learned $\hat{r}$ captures something causal about the agent's misconception or is merely an artifact of IRL's non-identifiability (i.e., the specific reward function found depends on the IRL algorithm's inductive bias). The illustrative drone example (Figure 1) is hand-crafted in 2D where $\hat{r}$ is human-interpretable, but the paper explicitly acknowledges (line 41) that in high dimensions $\hat{r}$ is no longer interpretable and "it is difficult to straightforwardly compare $\hat{r}$ to $r$." This undermines the claimed generality of the high-level explanation.

### Minor

4. **The practical feasibility of the black-box assumption is somewhat overstated.** The paper claims to treat the RL agent as a black box with "no access to its internal structure" and only $m$ trajectories available. Yet the method requires: (a) the ground truth reward function $r$ (often unavailable in pure black-box settings); (b) learning a precise $Q$-function $Q_r^{\hat{\pi}_A}$ by sampling the environment extensively; (c) running IRL to recover $\hat{r}$ and $\hat{\pi}_A$; and (d) training a new policy from scratch via the triple-loop algorithm (Algorithm 1). The paper acknowledges (line 47) that precise $Q$-function learning is "sample inefficient and computationally expensive" but dismisses this because only one $Q$-function is needed. The aggregate sample cost is nevertheless substantial, and the paper provides no analysis of it. This is a practical concern rather than a theoretical flaw.

5. **The inner-loop approximation error propagation is acknowledged but its practical implications are not discussed.** The inner loop uses $\tilde{N}_{\bar{n}} = \bar{n}+1$ iterations (line 121), meaning early middle-loop iterations have very few inner-loop steps and thus large approximation error (Lemma 3 bound $O(\gamma^{\tilde{N}_{\bar{n}}})$ is loose when $\tilde{N}_{\bar{n}}$ is small). While the analysis stacks these errors asymptotically (Lemmas 3–4, Theorem 3), the paper does not discuss how many total inner steps are needed for the bounds to become meaningful, nor whether this is computationally feasible for continuous-control tasks.

6. **The exact functional form of the shaping reward $r_\theta$ and the budget $b$ are unspecified.** The shaping reward is described as $r_\theta(r(s,a), r(s,a) - \hat{r}(s,a))$ but no specific parameterization is given. The cost budget $b$ and how it is chosen are not discussed. These are implementation-critical details that would be needed for reproducibility.

### Trivial

None that survive filtering. (The remaining parser artifacts and formatting issues are not author errors.)

## Nice-to-Haves

- **Ablation isolating the two explanation levels:** A natural experiment would compare the full UTILITY framework against variants using only the low-level explanation (cost constraint on misleading (s,a) pairs without reward shaping) and only the high-level explanation (reward shaping without the cost constraint). This would directly test whether the two-level structure provides additive value.
- **Sample complexity or wall-clock analysis:** The triple-loop algorithm is potentially expensive; reporting runtime or environment steps would help assess practical viability.
- **Sensitivity analysis for budget $b$:** The choice of $b$ controls how aggressively the agent avoids misleading (s,a) pairs, and its impact on final performance should be studied.

## Removed Points

These points appeared in the inputs but were removed or demoted for the following reasons:

- **Harsh Critic point #4 ("justification for constraining misleading (s,a) pairs is logically unsound"):** The critic argues that constraining specific (s,a) pairs does not eliminate actions from the action set. However, with budget $b=0$, the constraint forces avoidance of those (s,a) pairs, effectively removing those specific actions at those states. The paper's remark is informal but not unsound; the logic is a plausible heuristic motivation. Demoted from a claimed flaw to at most a minor imprecision, subsumed by other weaknesses.

- **Harsh Critic point #5 (black-box assumption) and #6 (inner-loop error propagation):** These are retained but demoted to Minor (see Weaknesses #4 and #5 above). The critic framed them as critical issues but they are practical caveats, not fatal theoretical errors.

- **Strength Finder strength #5 (remark about "sound justification grounded in monotonic policy improvement theorem"):** This strength partially conflicts with the verified weakness about loose reasoning in the remark. The remark is motivational, not a rigorous proof, so overstating it as "sound justification" is inappropriate. Removed to avoid inconsistency.

- **Strength Finder's framing of "principled handling of black-box assumption":** The paper's handling of the black-box assumption is reasonable but partial (as noted in Minor weakness #4). Kept as a supporting strength but downgraded from the Strength Finder's framing.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between ambitious theoretical claims and missing empirical validation, but do not produce a novel analysis that the paper itself lacks.

## Suggestions

1. **Provide complete experimental results.** This is non-negotiable. The paper must include: learning curves and final returns across multiple MuJoCo environments (HalfCheetah, Walker2d, Ant, Hopper) with multiple seeds, comparisons against all three baselines (RICE, SIL, LIR), and statistical significance measures. The current submission is structurally incomplete.

2. **Fix the "global optimality" framing.** Distinguish clearly in the abstract and contribution statement between the general result (convergence to stationarity, Theorem 3) and the restricted result (global optimality under finite state-action spaces and linear $r_\theta$, Theorem 4). Do not claim "the algorithm attains global optimality" as a general statement.

3. **Address the meaningfulness of the high-level explanation.** Either provide a theoretical argument that the IRL-learned $\hat{r}$ captures causally meaningful information about the agent's suboptimality (beyond the trivial fact that IRL always finds some reward function), or present synthetic experiments where the ground truth reward structure is known and the comparison $r - \hat{r}$ can be validated.

4. **Specify the functional form of $r_\theta$ and the choice of budget $b$.** These are necessary for reproducibility.

5. **Add ablation experiments** isolating the contribution of the high-level explanation (reward shaping) from the low-level explanation (cost constraint) to demonstrate that the two-level structure provides additive value over simpler alternatives.

## Score and Decision

**MY FINAL SCORE: <score>2.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**