Now I have a thorough understanding of the paper and all the reviews. Let me produce the final consolidated review.

---

## Summary

This paper proposes a framework for transfer learning in partially observable contextual bandits. It converts the transfer problem into computing causal bounds (confidence intervals for causal effects) via optimization, develops a Monte Carlo algorithm with sequential LP solving that achieves 100% valid samples, and then uses these bounds to improve bandit algorithms across three tasks: MAB, contextual bandits with finite contexts, and contextual bandits with function approximation. The main theoretical contribution is improving the regret dependence on the policy space from √|Π| to √log|Π| in the function approximation setting, supported by matching lower bounds.

## Strengths

- **Novel improvement in regret dependence on policy space size**: The paper proves that in the function approximation task (Task 3), regret scales as √(𝔼_W[𝒜^*(W)] T log(δ⁻¹|ℱ^*|log T)), reducing dependence on policy space size from √|Π| (prior work, e.g., boundingCE_continuous_IV) to √log|Π|. This is stated in the abstract, elaborated after Theorem 4, and discussed in the "Discussion" section.

- **100% valid sample proportion in causal bound estimation**: The proposed Monte Carlo algorithm (Algorithm 1) with sequential LP solving achieves 100% valid sample proportion for the feasible region (Table 1, fourth row), dramatically outperforming prior methods (e.g., CEbound's <10⁻⁴ and direct sampling ≈0). This directly supports the claim of more reliable causal bound estimation.

- **Incorporation of estimation error into causal bounds**: The optimization problem in Theorem 1 explicitly includes a discrepancy parameter ε for estimation error, and the algorithm samples θ from distributions accounting for uncertainty (Eq. 13). The paper notes this is neglected in prior literature (e.g., boundingCE_continuous_IV, CEbound), making the bounds more practical for finite-sample settings.

- **Matching lower bounds for multiple settings**: The paper provides minimax lower bounds for contextual bandits with finite contexts (Theorem 3) and with function approximation (Theorem 5), demonstrating near-optimality of the proposed algorithms up to logarithmic factors. The lower bounds depend on the reduced action set, confirming the theoretical advantage of using causal bounds.

- **Systematic handling of three transfer learning tasks**: The paper structures the problem into three increasingly challenging tasks (MAB, partially observable contextual bandit with full identification, and partially observable contextual bandit with partial identification), each with tailored algorithms and theoretical guarantees.

- **Numerical validation showing improvements**: Experiments demonstrate that the proposed algorithms outperform classical UCB and naive transfer (UCB-) in MAB (Figure 1), and outperform the state-of-the-art FALCON in function approximation (Figure 2), with results averaged over 50 repetitions with error bars.

## Weaknesses

### Fatal
None.

### Major

- **Discretization gap for continuous variables is unresolved**: The paper admits (lines 586–588) that "it is still an open problem whether the solution to the discretized problem will converge to the solution to the original functional optimization problem as the discretization becomes finer." Despite this, the entire bandit improvement argument (Theorems 7–13) assumes the true expected reward lies within the computed interval [l(a), h(a)] or [l(w,a), h(w,a)]. The convergence results (Propositions 4 and 5) establish convergence to the *discretized* solutions only, not to the true continuous bounds. For discrete variables the discretization is exact, which covers the experiments, but the paper's framing and title claim generality to continuous variables. Without a convergence guarantee or finite-sample error bounds on the discretization error, the regret theorems for continuous settings are conditional on an unverified assumption. The paper also says (line 411) that "the approximation error converges to zero for good distributions," which is not formalized. This gap needs to be resolved (e.g., by providing Lipschitz/Hölder regularity conditions under which convergence is guaranteed) or the paper's scope should be explicitly restricted to discrete settings.

- **Estimation error handling is heuristic, not rigorous**: In Algorithm 1, parameters θ_{ijk} and θ_l are sampled from uniform distributions over ε-balls. Only a finite number B of samples are drawn, and the resulting bounds l(a) and h(a) are the minimum and maximum over these B sampled parameter values. This does *not* produce an interval that provably contains the true causal effect with high probability, because one would need to take the infimum/supremum over the *entire* ε-ball, not just over a finite set of sampled points. Propositions 4 and 5 set the discrepancy parameter to 0, so they do not address this. The claim of having "incorporated estimation error" is therefore imprecise — the method provides a heuristic approximation rather than a rigorous confidence bound. The paper would benefit from replacing this with a rigorous procedure (e.g., using concentration inequalities to construct a set Θ that contains the true θ with probability 1−δ, then optimizing over Θ via the LP-based method).

- **Choice of the linearly independent variable set S is underspecified**: The algorithm requires selecting a linearly independent index set S of the linear constraints (Eq. 77). The paper does not explain how to construct such a set in practice or whether the results are sensitive to this choice. Since different choices of S could lead to different induced sampling distributions, this is a meaningful implementation concern that merits discussion.

### Minor

- **No evaluation of sensitivity to discretization resolution**: The numerical experiments use binary variables (natural discretization), so they do not test how bounds and regret change with discretization granularity. For the paper to support its claim of handling continuous variables, experiments showing convergence of bounds as the number of bins increases would be valuable.

- **Sample size calculation in Task 2 (Proposition 2) is limited**: The ε-identification result assumes all variables are discrete with bounded support and requires a constant lower bound κ on the fraction of samples containing each (y,u) tuple. The sample size bound scales with |𝒰|²|𝒴|²/κ, which can be large. This is not a fatal issue but reduces the practical applicability of the result for settings with many categories.

- **Gap-dependent and minimax bounds contain unexplained constants**: The UCB algorithms use specific constants (√(2log T / n_a(t)) in MAB versus √(log t / n_{w,a}(t)) in CB) with no justification for the change. The constant 8 appears in Theorem 8 without derivation. While common in the bandit literature, the discrepancy is worth clarifying.

### Trivial
None that survive filtering — the minor formatting issues in the paper are typical of submitted manuscripts.

## Nice-to-Haves

- **Computational complexity analysis**: The sequential LP sampling solves O(n_𝒜 n_𝒴 n_𝒲 n_𝒰) LPs per sample, which could be prohibitive for moderate discretization sizes. A discussion of computational cost and possible approximations would help practitioners.
- **Guidance on choosing the discrepancy parameter ε**: The paper suggests ε = 1/(2√n) but does not discuss how to set ε when n varies across different marginals or when the sampling distribution for θ is chosen differently (e.g., truncated Gaussian vs. uniform).
- **Extension to handle estimation error rigorously**: As described in the Major weaknesses, replacing the heuristic ε-ball sampling with a procedure that provides formal confidence sets (e.g., using concentration inequalities and optimizing over the full confidence region) would significantly strengthen the paper.

## Removed Points

The following points from the reviews are removed per policy:

- **"The 100% valid sample proportion is trivial because the algorithm ensures feasibility"**: This misunderstands the contribution. The method is *designed* to achieve 100% validity via LP-based sequential sampling, and the comparison with prior methods (<10⁻⁴ and ≈0) demonstrates the practical significance. This is a strength, not a weakness.

- **"The comparison to boundingCE_continuous_IV is unfair"**: The paper explicitly discusses the differences (different inference strategies, IV requirements). The improvement in regret order is a genuine contribution; the reviewer's concern reflects a disagreement about framing, not a flaw in the paper.

- **"The connection to POMDP literature is tenuous"**: The paper uses "partially observable" in the literal sense (hidden confounders/contexts), not claiming to use POMDP techniques. The framing is reasonable.

- **"The example's independence assumption is inconsistent with the general model"**: The example chooses U ⟂ W as a specific case for clarity. The general model allows arbitrary dependence. A specific illustrative example need not cover all cases.

- **Typographical issues (e.g., "max" vs "min" in Algorithm 1, line 567)**: Per hard rules, formatting/typo criticisms are removed as parser artifacts that do not appear in the original submission.

- **Missing appendix/proofs**: Per hard rules, these sections are stripped by the parser and exist in the original submission.

## Novel Insights

The reviews reveal that the paper's core tension lies between the heuristic/engineering contributions (the sequential LP sampling algorithm achieving 100% valid samples, the practical framework connecting causal bounds to bandit algorithms) and the theoretical guarantees (which are fully rigorous only for discrete variables). The harsh critic correctly identifies that the discretization gap and the non-rigorous confidence-set construction are the paper's two "Achilles heels." However, neither of these invalidates the contributions for discrete settings, where the experiments operate. The reviewers converge on the same assessment: the paper's ideas are interesting and the regret improvement from √|Π| to √log|Π| is a genuine advance, but the theory overreaches into continuous settings without the necessary guarantees.

## Suggestions

1. **Restrict the scope or prove convergence.** Either (a) restrict the paper's theoretical claims to discrete random variables where the discretization is exact, or (b) provide Lipschitz/Hölder regularity conditions under which the discretized solution provably converges to the continuous solution at a controlled rate. The latter would substantially strengthen the paper.

2. **Replace the heuristic ε-ball sampling with a rigorous confidence procedure.** Use concentration inequalities to construct a set Θ containing the true θ with probability 1−δ, then optimize over Θ (via the LP-based method) to obtain provably valid outer bounds on the causal effect. This would make the "incorporation of estimation error" claim precise.

3. **Add experiments with discretization sensitivity.** Show how the bounds and regret change as the number of bins increases for continuous or finely-discrete variables, demonstrating that the improvement over baselines is robust to discretization granularity.

4. **Clarify the construction of the independent variable set S.** Provide guidance or a systematic method for selecting a linearly independent index set, and discuss whether results are sensitive to this choice.

## Score and Decision

The paper presents an interesting and potentially impactful framework, with genuine theoretical contributions (improved regret bounds, matching lower bounds) and practical algorithmic innovations (100% valid LP-based sampling). However, the two major weaknesses — the unresolved discretization gap for continuous variables and the non-rigorous handling of estimation error — undermine the central claim of "provably efficient learning" in the general continuous setting. The paper's contributions are solid for discrete settings, which cover the experiments, but the title and framing overclaim generality. The paper requires substantial revision to address these issues or to honestly scope its claims to discrete settings.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>