## Summary

This paper introduces Maximum Entropy Model Correction (MoCo), a framework that corrects an approximate transition model $\hat{P}$ in model-based RL by incorporating moment constraints from the true dynamics $P$. For each state-action pair, a minimum-KL divergence optimization adjusts $\hat{P}(\cdot|x,a)$ so that expectations of chosen basis functions match their true values, yielding a corrected distribution $\bar{P}$ that is provably closer to $P$ in KL divergence. Two algorithms are built on this: MoCoVI (an iterative planning algorithm with convergence guarantees) and MoCoDyna (a sample-based Dyna-style variant). The theoretical analysis shows that if the true value function lies approximately in the span of the basis functions, the value-function error scales with the *product* of model error and value-function approximation error — a strict improvement over standard MBRL bounds — and that the convergence rate of MoCoVI depends on model accuracy rather than the fixed discount factor $\gamma$.

## Strengths

- **Strictly improved error bounds (Proposition 1, lines 159–170).** Standard MBRL (Lemma 1) gives $\|V^\pi - \hat{V}^\pi\|_\infty \le c_1 \|\varepsilon_{\text{model}}\|_\infty \cdot \|V^\pi\|_\infty$. MoCo replaces $\|V^\pi\|_\infty$ with $\inf_{w \in \mathbb{R}^d} \|V^\pi - \sum w_i \phi_i\|_\infty$, which can be substantially smaller when the value function is well-approximated by the basis span. This directly supports the claim that MoCo reduces the adverse impact of model error.

- **KL divergence Pythagorean improvement (Eq. 9, lines 151–156).** The corrected dynamics satisfy $\operatorname{KL}(P\|\bar{P}) \le \operatorname{KL}(P\|\hat{P})$ — the correction never increases the KL divergence to the true dynamics, and since $\bar{P}$ is not constrained to a model class, this improvement can go beyond what MLE model learning achieves.

- **MoCoVI convergence rate depends on model accuracy (Theorem 2, lines 232–250).** The rate $\gamma' = 3c_1 \|\varepsilon_{\text{model}}\|_\infty \cdot (\text{fraction})$ can be much smaller than the fixed discount factor $\gamma$ governing standard VI's rate, and improves with more accurate models. The comparison with VI and OS-VI (lines 249–253) is correctly drawn and makes the theoretical advantage concrete.

- **Non-divergence guarantee (lines 252–253).** Unlike OS-VI, which can diverge when the model is too inaccurate, MoCoVI's bounds hold for all $k$ even when $\gamma' > 1$. This robustness property is backed by the regularization analysis in Theorem 1 and is experimentally visible in the $\lambda=1$ case.

- **Principled handling of noisy queries (Theorem 1, lines 186–196).** The $\ell_2^2$-regularized MaxEnt formulation provides an explicit error bound trading off model error, query error, and basis-function approximation quality, with the analysis-grounded choice $\beta = \|\varepsilon_{\text{query}}\|_\infty / \|\varepsilon_{\text{model}}\|_\infty$.

## Weaknesses

### Major

- **Experimental validation is far too limited to support the practical claims made.** The method is tested on a single 6×6 gridworld (36 states, 4 actions) with synthetic model error constructed by uniform smoothing. The conclusion states the experiments "confirm the practical relevance of our theoretical findings" (line 335), but a tabular toy domain does not establish practical relevance — it serves as a sanity check for the theory. All computational challenges that arise in practice (solving per-state-action MaxEnt optimizations, importance sampling variance, sampling from the tilted distribution $\bar{P}$, scaling to continuous spaces) are entirely absent from this setting. The paper's framing would be more accurate as "illustrative verification of the theoretical guarantees" rather than confirmation of practical relevance.

### Minor

- **MoCoDyna is presented without convergence analysis.** MoCoVI has a full convergence theorem (Theorem 2), but MoCoDyna (Section 5) is described only as an algorithm sketch with no theoretical guarantees for the sample-based setting. The stochastic approximation update for $\psi_i$ (line 286) is stated without convergence properties. This asymmetry leaves the MoCoDyna results interpretable only as empirical demonstrations, not backed by the same theoretical rigor as MoCoVI.

- **Key experimental details are missing.** (a) The initial basis functions $\phi_1,\ldots,\phi_d$ used in the gridworld experiments are never specified — the paper says "an arbitrary initial set" (line 213) but does not state what was chosen. (b) The hyperparameter $\beta$ selection in experiments is not described; the theory-motivated formula $\beta = \|\varepsilon_{\text{query}}\|_\infty / \|\varepsilon_{\text{model}}\|_\infty$ depends on unknown quantities and no practical selection method is given. (c) MoCoDyna's model updates for $\hat{r}$ and $\hat{P}$ are indicated as "Update" (Algorithm 1, line 269) without specifying the update rule.

- **The convergence rate improvement in Theorem 2 requires a joint condition beyond model accuracy alone.** The paper correctly states that $\gamma'$ depends on $3c_1\|\varepsilon_{\text{model}}\|_\infty$ multiplied by a fraction that is $\le 1$ (lines 236–237, 219). However, the claim that "the rate of MoCoVI improves with more accurate models" (line 250) is incomplete: the fraction term encodes the quality of the basis function span, and there is no guarantee that past value functions provide progressively better approximations for general MDPs. The rate improvement depends on both model accuracy and the representation power of the basis functions — a point the paper acknowledges mathematically but understates in its narrative.

### Trivial

None beyond the missing details listed above.

## Nice-to-Haves

- An analysis of the computational cost of the MaxEnt correction subroutine would help scope practical applicability. The paper assumes operations involving $\hat{P}$ are "free" (lines 24, 112), but in continuous settings the planning algorithm might query $\bar{P}$ at many state-action pairs, each requiring solving a separate $d$-dimensional convex optimization. A brief characterization of how many such optimizations are needed per planning step and when the cost remains acceptable would strengthen the paper without requiring additional experiments.

## Removed Points

- **Computational cost as a major weakness.** The harsh critic argued the MaxEnt correction subroutine "may be prohibitive" in practice and that the paper conflates cheap $\hat{P}$ evaluation with cheap optimization. **Removed** because the paper explicitly adopts a standard theoretical modeling assumption (operations involving $\hat{P}$ are "considered free"/"cheap" relative to querying $P$ — lines 24, 112, 140). The cost concern is a practical implementation question beyond the paper's stated scope as a theoretical analysis. Moved to Nice-to-Haves.
- **Claim about missing related work section.** **Removed** per instructions: the paper integrates relevant citations throughout (OS-VI, value-aware model learning, MaxEnt density estimation) and a dedicated section is not required.
- **Reproducibility concerns about undisclosed supplementary details.** **Removed** per hard rules: the parser strips supplementary material and appendix sections; they exist in the original submission.
- **Criticism that "the fraction in $\gamma'$ is not guaranteed to be small" was presented as a major weakness.** **Demoted to Minor.** The paper transparently displays this dependence (Theorem 2, lines 236–238) and discusses it (lines 216–219). The criticism is correct that the narrative could be more cautious, but the mathematics is honest.
- **Strength Finder's claim that empirical validation "covers the full range of model errors" and "corroborates theoretical claims."** **Weakened.** The experiments exist and show positive results, but the limited scope (single gridworld) means they corroborate the theory only in the simplest possible setting. The Major weakness above captures this limitation.
- **Generic/superficial strengths from Strength Finder.** Any strength that merely stated "this paper addresses an important problem" or similar platitudes has been removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Reframe the experimental section to describe the gridworld results as "illustrative verification of theoretical guarantees" rather than "confirmation of practical relevance." This aligns the claims with the evidence and lets the strong theoretical contribution stand on its own.
2. Specify the initial basis functions used in the gridworld experiments, the $\beta$ selection procedure, and the model update rule for MoCoDyna. These missing details hinder reproducibility.
3. Either add a convergence analysis for MoCoDyna or explicitly characterize it as a preliminary algorithmic sketch whose theoretical study is left to future work. The disparity in rigor between MoCoVI (Theorem 2) and MoCoDyna (no theorem) is noticeable.
4. Consider adding at least one additional experiment on a slightly larger domain (e.g., a random MDP with more states, or a simple continuous navigation task) to demonstrate that the method works beyond the 36-state tabular case. This would substantially strengthen the empirical component without requiring a full deep RL benchmark.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>