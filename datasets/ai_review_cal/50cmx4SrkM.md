- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 8, 5, 5
## Summary

This paper presents Bayesian regret bounds for three GP-based bandit algorithms (GP-UCB, GP-BayesUCB, and GP-TS) in the combinatorial volatile Gaussian process semi-bandit setting. The key theoretical contributions are: (1) extending previous Bayesian regret bounds for GP-UCB and GP-TS to simultaneously handle *infinite*, *volatile*, and *combinatorial* arm sets — prior work covered at most two of these three dimensions; and (2) providing the first regret bound for GP-BayesUCB (GP-BUCB). The paper also applies this framework to online energy-efficient navigation on real-world road networks of Luxembourg and Monaco, using a rectified Gaussian trick to enable Dijkstra's algorithm with GP-derived edge weights.

---

## Strengths

1. **First regret bounds for GP-BayesUCB.** The paper provides the first Bayesian regret bound for GP-BayesUCB, even in the non-combinatorial setting (stated in Section 1, Lemma 1, Theorems 1(ii) and 2(ii)). The analysis uses a novel inverse error-function inequality (Lemma 1) to handle the quantile-based confidence parameter, which is technically non-trivial and represents a clear advance over the existing literature.

2. **Unified theoretical extension to the combinatorial+volatile+infinite setting.** Table 1 cleanly demonstrates that prior work (Srinivas 2012, Russo 2014, Kandasamy 2018, Takeno 2023, Nika 2022) covers at most two of the three dimensions (infinite, volatile, combinatorial), whereas this paper covers all three for all three algorithms. The infinite-arm analysis introduces a new discretization error lemma (Lemma 3) that handles volatile arms — a genuinely new technical step required for the more general problem formulation.

3. **Practical rectified Gaussian adaptation for shortest paths.** Algorithm 2 provides a principled way to handle potentially negative edge-energy estimates by taking expectations under a rectified Gaussian distribution, enabling the use of Dijkstra's algorithm instead of slower alternatives. This is a clean engineering contribution that makes the experimental framework viable at scale.

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing existence argument for the discretization constraints (Assumption 2).** Theorem 2 (infinite-case regret bounds) is conditional on Assumption 2, which imposes four simultaneous inequalities involving τ\_t and β\_t. Since β\_t itself depends on τ\_t (β\_t = 2 log(τ\_t^d t^2 / √(2π)) for GP-UCB, and similarly for GP-BUCB), it is not obvious that a sequence {τ\_t} exists satisfying all four constraints. The paper provides no argument — not even a sketch — that such τ\_t can be chosen as a function of the problem parameters (d, K, L, C₁, C₂, C₃, ς, t). While this is likely fixable (e.g., τ\_t = Θ(t^c) with explicit constants), the current statement is a gap: the infinite-case bounds are presented as a main contribution but rest on an assumption whose feasibility is unverified.

2. **Experimental parametrization of GP-BUCB does not satisfy the theory's conditions.** The finite-case theorem (Theorem 1) requires ξ > ω > 1 for GP-BUCB; the infinite-case theorem (Theorem 2) inherits the same condition. Yet the experiments (Sections 4.3–4.4) use ω = 1, ξ = 1 and ω = 1, ξ = 0.5 — both violating ω > 1. The paper acknowledges this in a footnote but dismisses it by saying "one could choose δ small enough such that GP-BUCB would select the exact same routes." This reasoning is circular: if δ is small enough that the behavior is indistinguishable, then the theoretical guarantee requires ω ≥ 1+δ, not ω = 1. The paper calls these "theoretically valid choices" (line 363), which is inaccurate. Consequently, the claim that "GP-BUCB gains more control without sacrificing theoretical guarantees" (line 303–305) is not supported by the experiments as presented. The authors should either (a) run experiments with parameters satisfying ξ > ω > 1 (e.g., ω = 1.1, ξ = 1.2) and confirm the same behavior, or (b) clearly separate the theoretical claim from the exploratory empirical demonstration.

### Minor

3. **Limited statistical evidence.** All experiments use only 5 replications per condition with ±1 standard error bars that are wide and overlapping. No significance tests are performed. The sample size is too small to support the paper's empirically-loaded claims about relative algorithm performance. While this is not fatal (the paper's primary contribution is theoretical), the authors should at minimum acknowledge the limited inferential power and avoid strong comparative language (e.g., "GP-TS has significantly lower regret").

4. **Unexplained counterintuitive lengthscale result.** The paper reports (Section 4.5, Figure 6) that increasing the kernel lengthscale *increases* cumulative regret for GP-based methods — the opposite of what the authors expected (they state "a large lengthscale increases correlation, which should lower regret"). The paper notes this is counterintuitive but provides no explanation or investigation. This suggests potential issues with the kernel design, the rectified Gaussian procedure, the SVGP inducing-point selection, or some other confound. Without understanding this, the experimental results are difficult to interpret.

5. **Gap between theory and experiments: the rectified Gaussian modification is unanalyzed.** The regret theory assumes the agent selects super arms based on unrectified GP posterior indices (μ + √β σ or a posterior sample). The experiments use a different selection rule that rectifies these indices to ensure non-negativity. The paper does not analyze how this rectification affects the regret bounds — i.e., whether the theory still applies. This should be explicitly discussed as a limitation.

6. **Discretization coupling makes the bound hard to interpret.** In the infinite case (Theorem 2), β\_T for GP-UCB and GP-BUCB depends on τ\_T (the discretization density), which itself must satisfy Assumption 2. Since τ\_T and β\_T are mutually constrained, the final bound is not expressed purely in terms of problem parameters (d, K, γ\_T), making it difficult to extract the actual rate. Providing an explicit τ\_t construction (see weakness #1) would resolve this.

### Trivial
None.

---

## Nice-to-Haves

- The paper would benefit from a brief limitations paragraph in the conclusion, noting strong assumptions (Lipschitz continuity, derivative tail bound, compactness) and the gap between theoretical parametrization and experimental practice.
- A comparison with simple non-GP baselines (e.g., ε-greedy on aggregated features) would help contextualize the value added by the GP framework, though this is not required.
- The lengthscale anomaly (weakness #4) merits at least a speculation or a diagnostic experiment (e.g., does the same pattern occur with exact inference?).

---

## Removed Points

These points were flagged by the reviewers but are removed or demoted from the main weaknesses with justification:

- **"Discretization coupling makes the bound hard to interpret"** from the harsh critic's section-by-section notes — this is a minor interpretability issue rather than a weakness; kept in minor at #6 above.
- **"No comparison with non-GP baselines"** — scope creep; the paper is not claiming to be a comprehensive empirical benchmark.
- **"The appendix is not available"** — the parser strips appendices from all submissions; this reflects a parser artifact, not an author failure. Removed per Hard Rules.
- **"The improved IRGP-UCB and GP-TS bound of Takeno et al. suggests a √β_T improvement is possible"** (mentioned as a comparison point in the paper itself, not a weakness) — this is the paper's own acknowledgment of a known gap, not a reviewer-discovered flaw.
- Several generic "area-of-concern" speculations from the harsh critic's sweep (e.g., "could the metric be measuring a proxy?") that lack concrete textual anchors in the paper.

---

## Novel Insights

The most interesting tension emerging from the review is the interplay between the discretization density τ\_t and the confidence parameter β\_t in the infinite-arm analysis. In prior work (Srinivas 2012, Takeno 2023) with *static* arms, one can choose τ\_t freely and then set β\_t = 2 log(τ\_t^d t^2 / √(2π)) as a function of τ\_t. Here, because volatile arms force a finer discretization that couples τ\_t and β\_t through multiple inequality constraints (Assumption 2, Eqs. 1–4), the mutual dependence becomes circular in a way that prior static-arm work did not encounter. This coupling is a genuine technical consequence of the more general setting, but resolving it — even with a straightforward polynomial τ\_t = Θ(t^c) construction — would significantly strengthen the paper. Similarly, the GP-BUCB parametrization mismatch (ω=1 in experiments vs. ω>1 required by theory) highlights a broader challenge in GP bandit theory: theoretically justified confidence parameters often over-explore, and bridging that gap requires either tighter analysis or a clean separation between "theoretically valid" and "empirically useful" regimes.

---

## Suggestions

1. Provide an explicit construction for τ\_t (e.g., τ\_t = C·t^c with constants derived from the problem parameters d, K, L, C₁, C₂, C₃, ς) and verify that all four inequalities in Assumption 2 are satisfied. Turn Assumption 2 from a conditional statement into a theorem.

2. Rerun the GP-BUCB experiments with parameters satisfying ξ > ω > 1 (e.g., ω = 1.1, ξ = 1.2) and report results. If these valid parameters produce similar behavior, the claim about retaining guarantees while controlling exploration is supported. If not, weaken the claim.

3. Increase the number of experimental replications (at least 10–20, ideally 30+) or use bootstrapping to provide more reliable error estimates. Investigate and explain the lengthscale reversal — this may indicate kernel misspecification, a confound from the SVGP inducing-point selection heuristic, or an interaction with the rectified Gaussian procedure.

4. Acknowledge the gap between the theory (unrectified selection) and practice (rectified selection) explicitly, and discuss under what conditions the rectification would or would not affect the regret bounds.

---
