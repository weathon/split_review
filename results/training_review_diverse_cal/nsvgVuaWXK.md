Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual paper content.

## Summary

This paper studies transfer learning in partially observable contextual bandits (TLPOCB), where the agent has limited knowledge from other agents and only partial information about hidden confounders. The authors formulate the problem of bounding causal effects under partial observability as a functional optimization problem, discretize it into linear constraints, and develop a Monte Carlo sequential-LP sampling algorithm to compute these bounds. They then show how the resulting causal bounds can be used to improve classical bandit algorithms (MAB, contextual bandits with finite contexts, and contextual bandits with function approximation), proving regret bounds that scale with the reduced effective action set $\tilde{\mathcal{A}}^*$ rather than the full set $\mathcal{A}$, and improving dependence on function space size from $\sqrt{|\Pi|}$ to $\sqrt{\log|\Pi|}$ compared to prior work.

## Strengths

1. **Novel framework connecting causal bounds to bandit regret.** The paper establishes a principled link between partial identification of causal effects and regret minimization in bandits. This is a creative synthesis of two literatures (causal inference and bandit theory) that yields provable improvements: Theorems 4.1, 5.1, and 6.1 show that using causal bounds reduces effective action sets and thus improves regret, with matching lower bounds (Theorems 5.2, 6.3) demonstrating near-optimality.

2. **Improved regret dependence on function space size.** In the function approximation setting (Task 3), the paper achieves $\mathcal{O}(\sqrt{\mathbb{E}_W[|\mathcal{A}^*(W)|] T \log(\delta^{-1}|\mathcal{F}^*|\log T)})$ regret (Theorem 6.1), improving the dependence on the policy space from $\sqrt{|\Pi|}$ to $\sqrt{\log|\Pi|}$ relative to $\texttt{\cite{boundingCE\_continuous\_IV}}$. This improvement is non-trivial: it substitutes data-driven bounds on the policy space with causal-bound-based elimination of incompatible functions.

3. **Sequential LP sampling with 100% valid sample rate.** Algorithm 1 and Proposition 3.1 provide a principled Monte Carlo method that guarantees all samples satisfy the model constraints, with convergence in probability to the discretized optimum. The empirical demonstration (Table 3) that this method achieves 100% valid samples versus <0.3% for LP support and near-zero for naive bounds is compelling.

4. **$\epsilon$-identification result for the fully identified case.** Proposition 4.1 provides finite-sample guarantees for Task 2 (where identification is achieved), giving a concrete sample complexity for achieving $\epsilon$-accurate causal effect estimates.

5. **Matching lower bounds.** The paper proves minimax lower bounds (Theorems 5.2, 6.3) that match the upper bounds up to logarithmic factors, demonstrating the near-optimality of the proposed algorithms.

## Weaknesses

### Major

1. **Causal bound algorithm's theoretical guarantees are limited to discrete variables.** The paper acknowledges (lines 586-588) that for general (continuous) random variables, "it is still an open problem whether the solution to the discretized optimization problem will converge to the solution to the original functional optimization problem as the discretization becomes finer." This means the core technical machinery (Algorithm 1, Propositions 3.1/3.2) is only fully justified for discrete random variables. The paper claims to handle "general context and reward distributions, whether discrete or continuous" (line 59), but the theory does not support the continuous case. This is a significant gap between the paper's stated scope and what is actually proven.

2. **Proposition 3.2's assumption on OPT is unrealistic.** The assumption requires that for each local optimum $\mathbf{x}_{loc}$, there exists a ball such that *any* initial guess in that ball leads to *that exact* local optimum via OPT. The objective in Eq. (7) is a rational function of $x_{ijkl}$, making it non-convex. The paper provides no concrete example of an optimization procedure that satisfies this condition for the given feasible set and claims "the assumption on OPT is not so strict" (line 649) without justification. As stated, this theoretical result is essentially vacuous — it asserts convergence under conditions that are not shown to be realizable.

3. **Estimation error is not integrated into the main results.** The paper prominently claims to "incorporate estimation error, which is often neglected" (line 69). However:
   - The convergence guarantees (Propositions 3.1, 3.2) explicitly assume $\epsilon=0$.
   - The regret theorems assume the true causal effect lies within the computed bounds, but no high-probability guarantee is provided that the Monte Carlo bounds (with $\epsilon$ perturbation) actually contain the true effect.
   - The sampling of $\theta_x$ from $[\hat{\theta}_x-\epsilon, \hat{\theta}_x+\epsilon]$ (Algorithm 1, line 567) is a heuristic — no justification is given that this produces valid confidence sets for the expected reward bounds.
   - The $\epsilon$-identification result (Proposition 4.1) applies only to Task 2 (full identification case), not to the partial identification settings where the main bandit results reside.
   
   The paper's handling of estimation error is limited to a sensitivity-analysis-style perturbation of the constraints, without theoretical guarantees that propagate through to the bandit regret.

4. **Function approximation algorithm's $\mathcal{A}^*(w)$ computation is under-specified.** Algorithm 6 requires computing $\mathcal{A}^*(w)$ per round — i.e., checking which actions could be optimal under some $f \in \mathcal{F}^*$ for the given context $w$. The paper references Section 4 of $\texttt{\cite{instanceCB\_RL}}$ for this, but that work addresses action elimination in *linear* bandits, not general function classes with causal bound constraints. The paper does not provide an algorithm or complexity guarantee for computing $\mathcal{A}^*(w)$ in polynomial time for general $\mathcal{F}^*$. This is a significant implementation gap for the key algorithmic component of Task 3.

### Minor

1. **Narrow experimental evaluation.**
   - The causal bound comparison (Table 4) uses a single randomly generated distribution with binary variables, with no standard errors, multiple runs, or sensitivity analysis.
   - The MAB experiment (Figure 1) evaluates one 5-armed Bernoulli problem with one set of probabilities.
   - The function approximation experiment (Figure 2) does not describe how $l(w,a)$ and $h(w,a)$ are computed in the continuous setting; these appear to be derived from the known generative model, which sidesteps the hard part of the pipeline.
   - No experiments evaluate sensitivity to discretization granularity, sample size $B$, estimation error $\epsilon$, or the computational cost of the sequential LP method.
   - The experiments therefore validate the bandit component in isolation but do not validate the full pipeline from raw data through causal bound computation to bandit learning.

2. **Scalability concern for the sequential LP method.** Algorithm 1 requires solving $O(n_{\mathcal{A}} n_{\mathcal{Y}} n_{\mathcal{W}} n_{\mathcal{U}})$ linear programs per sample. The paper acknowledges this as "the most computationally extensive step" but provides no wall-clock times. For non-trivial discretizations, this could be prohibitive. Since these bounds are computed once (offline), the concern is somewhat mitigated, but the paper should provide scaling analysis.

3. **Duplicated section.** The "Infinite function classes" and "Discussion" subsections (lines 1028–1058 and 1061–1092) contain near-identical content, with slight differences in wording. This appears to be a genuine writing artifact (not a parser error) and should be cleaned up.

4. **Proposition numbering.** The Propositions in the extracted text lack visible numbers; they are referenced externally as Proposition 3.1 and 3.2 but this numbering is not visible in the paper body.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- A concrete example of an optimization procedure OPT that satisfies the assumption of Proposition 3.2, or a relaxation of that assumption to something more standard (e.g., convergence to a stationary point).
- Experimental evaluation of sensitivity to discretization granularity, estimation error $\epsilon$, and computational cost.
- Wall-clock times for the sequential LP method on the binary example, with scaling projections.
- An explicit finite-sample concentration bound (rather than only asymptotic convergence) for the Monte Carlo bounds, which would allow clean integration into the bandit regret analysis.

## Removed Points

- **Criticism about missing appendix/proofs** (e.g., "the appendix (not available) likely contains the proofs"): Removed because the parser strips appendix sections from all papers.
- **Claim that the lower bound "seems too clean" / "tailored to match the upper bound"**: This is speculation without evidence. Matching upper and lower bounds are standard in bandit theory and the paper cites a construction that would be in the (stripped) appendix.
- **Claim that the comparison with [boundingCE_continuous_IV] is "unsubstantiated" / "conflates different settings"**: The paper explicitly acknowledges the different assumptions (lines 1001-1008: "the method in [boundingCE_continuous_IV] relies on instrumental variables") and frames the improvement in terms of regret scaling, which is a legitimate algorithmic comparison. The reviewer's demand for a method "that also works under the same partial observability and no-IV assumptions" is a request for a different paper, not a valid criticism of this one.
- **"No experiments evaluate... computational cost"**: While partly true, the reviewer's framing exaggerated the gap. The paper does report valid sample proportions (Table 3) which directly measures one aspect of computational efficiency.
- Various minor rewordings of the above criticisms.

## Novel Insights

None beyond the paper's own contributions. The reviewer analysis does not surface a genuinely novel observation about the paper that the authors themselves did not articulate.

## Suggestions

1. Restrict the theoretical claims about the causal bound algorithm to discrete variables, or prove convergence of the discretized solution to the original functional problem under appropriate smoothness conditions.
2. Replace or substantially weaken the assumption in Proposition 3.2 — either provide a concrete OPT that satisfies it (e.g., a trust-region method under a KL-regularized feasible set) or rephrase as a heuristic justification rather than a formal proposition.
3. Provide a high-probability guarantee that the Monte Carlo bounds (with estimation error $\epsilon$) contain the true causal effect, and propagate this guarantee into the bandit regret analysis. This would turn the $\epsilon$ perturbation step from heuristic to rigorous.
4. Expand the experiments to include: (a) multiple random seeds/instances with error bars for the causal bound comparison; (b) sensitivity analysis for discretization granularity; (c) wall-clock time for the sequential LP method; (d) an end-to-end evaluation on a continuous-variable example where bounds are estimated from real finite data (not derived from a known generative model).
5. Clarify how $\mathcal{A}^*(w)$ can be computed efficiently for general function classes $\mathcal{F}^*$, or provide a relaxation (e.g., approximate action elimination) with a guarantee.

## Score and Decision

**Originality**: Good — the combination of partial identification causal bounds with bandit algorithms is novel.  
**Importance of question**: High — transfer learning under partial observability is practically important.  
**Claims support**: Moderate — the bandit regret theory is solid given valid bounds, but the bound computation theory has gaps for continuous variables, and the estimation error handling is not integrated into guarantees.  
**Soundness of experiments**: Weak — too narrow to validate the full pipeline.  
**Clarity**: Adequate but has duplicated content and dense notation.  
**Value to community**: Moderate — the framework and regret analysis are potentially influential, but the practical toolchain is underdeveloped.

The paper has real theoretical contributions (the bandit regret analysis with causal bounds, the improved dependence on function space size, matching lower bounds) but is significantly weakened by: (1) the causal bound algorithm's theory not covering the continuous case that the paper claims to address, (2) an unrealistic assumption in Proposition 3.2, (3) estimation error integrated only heuristically, and (4) experiments that are too narrow to validate the full pipeline. These are addressable in a revision but constitute genuine gaps in the current submission.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>