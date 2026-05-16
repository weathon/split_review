Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper provides Bayesian regret bounds for GP-UCB, GP-BayesUCB (GP-BUCB), and GP-TS in the combinatorial, volatile, and infinite-arm Gaussian process semi-bandit setting. The bounds unify three dimensions (infinite arms, volatile availability, combinatorial selection) that prior work only covered piecewise, and include the first theoretical regret bounds for GP-BayesUCB. The paper also applies the framework to online energy-efficient navigation on real-world road networks.

## Strengths

1. **First regret bounds for GP-BayesUCB (non-combinatorial and combinatorial).** The paper provides explicit Bayesian regret bounds for GP-BayesUCB (Theorems 1(ii) and 2(ii)), which prior work introduced without guarantees. This is a genuine theoretical contribution — Lemma 1's Chernoff-type bound on erf⁻¹ is the key technical enabler.

2. **Unified Bayesian regret bounds for GP-UCB and GP-TS in the most general setting considered (infinite × volatile × combinatorial).** Table 1 situates the contribution clearly: Takeno et al. (2023) covers infinite + static, Russo & Van Roy (2014) covers finite + volatile, Nika et al. (2022) covers infinite + volatile but uses frequentist bounds. This paper delivers Bayesian bounds for all three simultaneously. The bounds are Õ(√(TK β_T γ_{TK})), matching the non-combinatorial result of Takeno et al. when K=1.

3. **Novel discretization analysis for volatile arms in the infinite setting.** Prior discretization arguments (Takeno et al.) assumed static arm sets, where the discretized optimal arm remains feasible. With volatile arms this fails. Lemma 4 bounds the discretization error U_t([a]_{D_t}) - U_t(a) via Cholesky decomposition (for the posterior mean) and Lipschitz properties of the kernel (for the posterior standard deviation). The three new discretization inequalities (Assumption 3, eqs. 1-3) are tailored to this analysis.

4. **Practical demonstration on a real-world problem.** The energy-efficient navigation experiments use real road networks (Luxembourg and Monaco from OpenStreetMap/SUMO), vehicle-physics-based priors, and a combined graph Matérn + feature kernel. The paper handles the practical challenge of negative energy consumption via rectified Gaussians for Dijkstra compatibility.

## Weaknesses

### Fatal
None.

### Major

1. **Experimental GP-BUCB parameters violate the theoretical conditions.** Theorems 1(ii) and 2(ii) require ξ > ω > 1 for GP-BUCB. The main experiment (§4.4) uses ω = 1, ξ = 1, which falls outside this regime. The BUCB parametrization experiment uses ω = 1, ξ = 1 and ω = 1, ξ = 0.5 — both with ω = 1. The paper acknowledges this in a footnote but hand-waves it: "we could choose δ to be small enough such that GP-BUCB would select the exact same routes in all experiments." This is not a formal justification — the Chernoff bound in Lemma 1 explicitly requires ω > 1, so the theoretical guarantees do not apply to the reported configurations. Since the paper claims GP-BUCB's parametrization "retains theoretical guarantees while being more flexible," this directly contradicts the evidence presented.

### Minor

2. **Asymmetric baseline comparison.** The Bayesian inference (BI) baseline of Akerblom et al. assumes independence across edges and does not use contextual features (§4.3). The GP methods use both a graph Matérn kernel (capturing edge correlations) and a feature kernel over three contextual features (length, speed limit, incline). The paper states it "extend[s] the framework to incorporate contextual information" (§4), which means the comparison conflates two differences: (i) GP covariance modeling vs. independent BI, and (ii) contextual features vs. no context. The results in Figure 3 therefore reflect the combined advantage, not the superiority of GP bandit algorithms per se. The paper would benefit from ablating these factors (e.g., a GP baseline without the feature kernel) or clearly separating the claims.

3. **Gap between theory and experimental protocol not fully addressed.** The rectified Gaussian heuristic (§4.2) is a practical modification for Dijkstra compatibility, but the paper neither analyzes its effect on regret nor explicitly states that the regret bounds do not cover the rectified variant. The experiments are motivated as an application of "the framework," but the framework's theoretical guarantees apply to the unrectified algorithms. This disconnect, while common in applied papers, deserves explicit acknowledgment and ideally informal justification.

4. **Lengthscale experiment result unexplained.** The paper finds that for GP methods, "increasing the lengthscale increases the cumulative regret overall" (§4.4), which is counterintuitive (larger lengthscale should increase correlation and help learning). The paper presents this without explanation or discussion, leaving the reader uncertain whether this is a genuine phenomenon or an artifact of the approximate inference (SVGP optimization may deteriorate at large lengthscales).

5. **Limited experimental scale.** Evaluations use 5 runs per configuration with horizon T = 500. Standard errors are shown but with 5 runs they are unreliable. The short horizon may not reveal asymptotic behavior.

6. **No ablation of kernel components.** The combined kernel k_{G·f + f} uses a graph Matérn and two feature kernels, but there is no ablation isolating the contribution of each component.

7. **No discussion of limitations.** The paper does not discuss the dependence of bounds on λ_K^* (which can be Θ(K) in the worst case, as noted in Nika et al. 2022) nor the practical implications of the heavy discretization requirements (Assumption 3 forces τ_t to grow polynomially in t, implying exponentially fine discretization in dimension d).

### Trivial
None.

## Nice-to-Haves

- Add a synthetic experiment that validates the regret scaling directly (regret vs. T on a known GP prior with controlled arm sets), which would strengthen the paper in its own theoretical direction without the confounding factors of the real-world application.
- Compare GP-BUCB with ω = 1.1, ξ = 1.2 (satisfying ω > 1, ξ > ω) against the current ω = 1 results to confirm that the empirical behavior is similar while retaining formal guarantees.
- Include a GP baseline without the feature kernel (graph kernel only) to isolate the value of contextual features.

## Removed Points

*(These points were identified by the reviewers but are removed or downgraded per the review guidelines. Treat with caution.)*

1. **Criticism that the theoretical contribution is "incremental."** Removed — the paper is transparent about its relationship to prior work (Table 1, §3) and provides the first GP-BUCB bounds and the first unified Bayesian bounds for the infinite+volatile+combinatorial setting. Incremental progress is normal and acceptable in theory papers; the reviewer's characterization is a matter of opinion, not a verifiable weakness.

2. **Criticism that the "volatile arms encompass contextual bandits" claim is not formalized.** The paper states this as a standard observation from the literature (Russo & Van Roy 2014) — context determines which arms are available. This is well-established and does not require additional formalization from this paper.

3. **Criticism that the paper does not compare against Takeno et al. or Nika et al. on synthetic data.** This is scope creep — the experiments are an applied demonstration on a specific real-world problem, not a synthetic benchmark comparison. Adding synthetic comparisons would be a nice-to-have, not a weakness.

4. **Criticism that "GP-BUCB is simply BayesUCB applied to GPs, not a new algorithm."** The paper does not claim to invent GP-BUCB as a new algorithm; it claims to provide the *first regret bounds* for it, which is a different and valid contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm that the main technical novelty is the discretization analysis for volatile combinatorial arms (Lemma 4) and the first GP-BUCB bounds, but no reviewer identified an unexpected implication or cross-connection that the paper itself missed.

## Suggestions

1. Re-run the GP-BUCB experiments with parameters satisfying ξ > ω > 1 (e.g., ω = 1.1, ξ = 1.2), or explicitly separate the "theoretically valid" and "heuristic" experiment sections with different claims attached to each.

2. Add a non-contextual GP baseline (graph Matérn kernel only, no feature kernel) to the main comparison so the reader can distinguish the benefit of GP covariance modeling from the benefit of contextual features.

3. Add a brief paragraph in §4.2 transparently stating that the rectified Gaussian modification is heuristic and the theoretical regret bounds do not directly apply to this variant, while noting that the experiment is intended as a demonstration of applicability rather than a validation of the bounds.

4. Discuss the counterintuitive lengthscale result — is this an artifact of SVGP optimization or a genuine property of the problem?

5. Add a limitations paragraph in the conclusion covering the λ_K^* dependence, the discretization requirements, and the gap between theory and the rectified experiment.

## Score and Decision

**Originality:** 2.5/5 — The paper extends existing techniques to a broader setting; the GP-BUCB bounds are genuinely new but the overall proof technique follows established frameworks.

**Importance of research question:** 4/5 — The combinatorial volatile GP bandit setting is practically relevant and theoretically interesting.

**Claims supported:** 2.5/5 — The theoretical claims are supported by the proofs within their assumptions. However, the experimental claims are undermined by the ω=1 parameter violation and asymmetric baseline comparison.

**Soundness of experiments:** 2/5 — The ω=1 violation is a direct contradiction between the experimental protocol and the theoretical conditions. The BI baseline comparison conflates multiple factors. Only 5 runs.

**Clarity of writing:** 4/5 — The paper is generally well-structured and clear about its contributions and their relationship to prior work.

**Value to the community:** 3.5/5 — The first GP-BUCB bounds and the unified analysis are useful contributions. The experimental application is secondary.

The paper's core theoretical contribution is technically sound and fills a genuine gap (unified Bayesian bounds for the infinite+volatile+combinatorial setting + first GP-BUCB bounds). However, the experimental section contains a significant flaw: the GP-BUCB parameters used in all experiments (ω = 1) violate the ξ > ω > 1 condition required by the theorems, and the paper's justification is insufficient. Additionally, the asymmetric baseline comparison makes it difficult to interpret the empirical results. While these issues do not invalidate the theoretical contribution, they weaken the paper as a whole. The paper would benefit from cleaning up the experimental protocol to align with the theory.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>