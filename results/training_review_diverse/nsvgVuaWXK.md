I now have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper studies transfer learning in partially observable contextual bandits, where agents have incomplete contextual information and access to expert data with hidden confounders. It makes three main contributions: (1) formulating the estimation of causal effect bounds as functional optimization problems and developing a sequential LP Monte-Carlo sampling algorithm with convergence guarantees; (2) incorporating these causal bounds into classical bandit algorithms (MAB, contextual bandit, function approximation) and proving improved regret bounds — most notably improving the dependence on policy space size from √|Π| to √log|Π|; (3) proving near-optimal lower bounds and providing experimental validation.

## Strengths

1. **Tighter causal bounds via sequential LP with guaranteed validity.** The sampling algorithm (Alg. 1) sequentially solves linear programs to enforce all joint-distribution constraints, achieving 100% valid samples compared to <10⁻⁴ for prior LP-based methods (CEbound). Numerical experiments confirm the resulting bounds are narrower (e.g., E[Y|do(A=0)] shrinks from [0.283,0.505] to [0.371,0.466]). This is a concrete algorithmic improvement over prior work in causal bound computation.

2. **Improved regret dependence from √|Π| to √log|Π| in function approximation.** Theorem 12 (and the summary in Table 1) shows that by using causal bounds to shrink the function class from ℱ to ℱ* and the action set to 𝒜*(w), the regret improves from 𝒪(√(|𝒜| T log(|ℱ|))) to 𝒪(√(𝔼_W[|𝒜*(W)|] T log(|ℱ*|))). Since |ℱ*| ≤ |ℱ| and 𝔼_W[|𝒜*(W)|] ≤ |𝒜|, this is a clear theoretical improvement with qualitatively better dependence on the function class size (logarithmic vs. linear in |Π|).

3. **Provable convergence of the Monte-Carlo sampling algorithm.** Proposition 1 establishes convergence in probability under mild coverage assumptions on the sampling distribution, and Proposition 2 strengthens this to almost-sure convergence when augmented with a local optimization oracle. These provide theoretical justification that the algorithm can recover the optimal discretized bounds.

4. **Near-optimal minimax lower bounds.** Theorems 11 and 13 prove lower bounds matching the upper bounds up to logarithmic factors (e.g., Ω(√(𝔼_W[|𝒜*(W)|] log|ℱ*| T)) in Theorem 13), showing the algorithms are essentially optimal within the problem class.

5. **Incorporation of estimation error into the optimization formulation.** The constraints in Theorem 1 explicitly include |F(a,y,w)−F̂(a,y,w)| ≤ ε and |F(u)−F̂(u)| ≤ ε, and Proposition 7 provides an ε-identification sample-size bound for the fully identifiable case (Task 2). This treats a practical issue that prior literature (CEbound, boundingCE_continuous_IV) often neglects.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Limited connection between estimated bounds and regret analysis.** The regret theorems (Thms 3, 5, 7) assume the causal bounds [l(a),h(a)] are known exactly and deterministically. In practice, these bounds are estimated via the sampling algorithm, which introduces random error due to finite samples, discretization, and the Monte-Carlo procedure. The paper discusses estimation error in the optimization (the ε parameter) and samples θ from intervals of width 2ε, but the regret analysis never formally accounts for how uncertainty in the bounds propagates to regret. If estimated bounds are too wide, the regret improvement degrades; if too narrow, bounds may not contain the true causal effect. A high-probability guarantee connecting the bound estimation procedure to the regret would significantly strengthen the work.

2. **Discretization gap for continuous random variables.** Propositions 1 and 2 establish convergence of the sampling algorithm to the solutions of the *discretized* optimization problem (Eq. 10). The paper explicitly acknowledges "it is still an open problem whether the solution to the discretized problem converges to the solution of the original functional optimization problem as the discretization becomes finer" (line 587). While the paper mentions that discretization error converges to zero "for good distributions" (line 411), no formal conditions or proof are provided. This limits the scope of the theoretical guarantees to discrete settings.

3. **Computational cost of sequential LP sampling is unanalyzed.** Algorithm 1 solves up to |S| linear programs per sample, where |S| = n_𝒜 n_𝒴 n_𝒲 n_𝒰 − n_𝒜 n_𝒴 n_𝒲 − n_𝒰 + 1. For moderate discretization grids this becomes large, and the paper does not report wall-clock time, discuss scaling to larger variable domains, or provide guidance on choosing the independent variable index set S (whose choice affects the induced sampling distribution).

4. **Empirical evaluation is limited.** The function approximation experiment (Fig. 2) uses a single synthetic quadratic function class of size 50 with one random instantiation. No comparison with other transfer-learning baselines (beyond FALCON) is provided, and no real-world dataset is used to demonstrate practicality. For a paper making strong claims about "orders of magnitude faster convergence rates," the experimental validation is too narrow.

5. **Illustrative example contains a computational error.** In the running example (lines 246–254), the paper computes E[Y|do(A=0),W] = 10×0.1 + 0.9×0.9 = 1.81. However, from the reward table (Table 1), do(A=0) yields reward 0 (U=0) or 1 (U=1), so the correct value is 0×0.1 + 1×0.9 = 0.9. The computation 10×0.1 + 0.9×0.9 = 1.81 corresponds to do(A=1). The values for the two arms are swapped. This does not affect the core technical contributions but should be corrected.

### Trivial

- The objective in Eq. (6) involves division by Σ_{j'} x_{ij'kl}, which can be zero when no probability mass falls in a discretization cell. The paper does not address this degenerate case.
- The constraint set in Theorem 1 is partially redundant (some constraints are implied by others). While this does not cause inconsistency, a cleaner formulation would improve readability.

## Nice-to-Haves

- A formal analysis integrating the bound-estimation uncertainty (ε, sampling noise) into the bandit regret, showing how the regret degrades gracefully with estimation quality.
- A discussion or simple experiment on how the choice of S (the linearly independent variable index set) affects the induced sampling distribution and the resulting bounds.
- Reporting wall-clock time per sample for the sequential LP algorithm to help readers assess practical feasibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Regret bound for arms with h(a) < μ^* appears incorrect."** After careful analysis, this bound is correct. The algorithm truncates the UCB of each arm at h(a). For arms with h(a) < μ^*, the truncated UCB never exceeds h(a). The optimal arm's UCB is at least μ^* with probability ≥ 1−1/t² (standard UCB confidence bound), and its truncated UCB is min{U_{a^*}(t), h(a^*)} ≥ μ^* since h(a^*) ≥ μ^*. Therefore, arm a is only pulled when the confidence bound fails (probability ≤ 1/t²), yielding expected pulls ≤ Σ 1/t² = π²/6. The critic's claim that Ω(1/(μ^*−h(a))²) samples are needed misunderstands how the truncation operates: the causal bound *pre-emptively* caps exploration — no learning of the gap is required.

- **Missing appendix / proofs.** The parser strips appendix content from all papers. The original submission contains these proofs.

- **"The regret comparisons... improvement is not 'orders of magnitude' as claimed."** Going from √|Π| to √log|Π| is an exponential improvement in the dependence on the function class size, which plausibly justifies "orders of magnitude" in the relevant regime.

- **"Theorem 1 constraint set is over-specified... could lead to inconsistencies."** Redundancy among constraints does not cause inconsistency; the feasible region is simply defined by a subset of the listed constraints. This is standard in causal inference formulations.

- **"Figure x-axis label is missing."** The TikZ code clearly includes `xlabel = time $t$` (lines 1180, 1249).

- **"Plot appears to show only 10,000 steps."** The paper states T = 10^5 (line 1157). The critic appears to misread the plot scale.

- **"Least squares oracle over the entire function class each epoch is computationally heavy."** This is standard practice in the IGW literature (FALCON, instanceCB_RL) and is not a weakness of this paper specifically.

- **"Almost sure convergence condition on OPT is strong."** The paper acknowledges this (line 649: "the assumption on OPT is not so strict") and presents the result as what is achievable under ideal conditions.

## Novel Insights

The key insight from the reviews is that the paper's two halves — causal bound estimation and bandit regret minimization — operate at different levels of analysis. The estimation side provides Monte-Carlo samples with convergence guarantees to optimal *discretized* bounds, while the regret side assumes exact deterministic bounds. This gap is not currently bridged by formal guarantees. However, the paper does partially address it by incorporating ε-estimation error into the optimization constraints and by showing empirically that the estimated bounds are tighter than prior methods. A deeper insight is that the truncation mechanism (capping UCBs at h(a)) is what makes the regret analysis work for the intermediate case without needing to learn gaps — this is a genuinely clever algorithmic design that pre-emptively avoids exploration rather than relying on data-driven elimination.

## Suggestions

1. Correct the swapped arm indices in the illustrative example (lines 248–252) and verify the conclusion.
2. Add a short discussion or formal statement linking the ε-estimation error in the bound computation to the regret bound — even if only under simplifying assumptions (e.g., if bounds are correct with probability 1−δ, regret degrades by at most an additive term).
3. Report the wall-clock time for the sequential LP algorithm and discuss how it scales with discretization fineness.
4. Strengthen the experiments with at least one additional instantiation or a real-world partially observable bandit problem to demonstrate practicality beyond synthetic data.

## Score and Decision

This paper makes solid theoretical contributions to an important and understudied problem — transfer learning in partially observable bandits via causal bounds. The main results (improved regret dependence from √|Π| to √log|Π|, near-optimal lower bounds, convergence of the sampling algorithm) are novel and significant. The weaknesses are primarily about incomplete integration between the two halves of the paper and limited experimental validation, rather than structural flaws in the core claims. The paper is a clear contribution to the theory of causally-informed bandit learning.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>