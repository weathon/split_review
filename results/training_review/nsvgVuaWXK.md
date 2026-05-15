Now I have a thorough understanding of the paper and can verify all the reviewer claims. Let me produce the consolidated final review.

## Summary

This paper studies transfer learning in partially observable contextual bandits (POCB), where expert and agent agents have different observation capabilities. The authors convert the problem into one of identifying (or partially identifying) causal effects via constrained optimization, then use the resulting causal bounds to shrink the action/function space in bandit algorithms. For computing bounds, they propose a sequential LP sampling algorithm that achieves 100% valid samples (vs. <10⁻⁴ for prior methods). They provide regret analyses across three tasks—MAB, finite-context CB, and CB with function approximation—with matching lower bounds, and demonstrate improved dependence on function class size (√log|ℱ| vs. √|ℱ| in prior work).

## Strengths

- **Novel problem formulation connecting causal inference with transfer learning in POCB**: The paper formalizes three transfer learning tasks as causal effect identification/partial identification problems (Section 3), incorporating estimation error ε into the optimization constraints (Theorem 1). This generalizes prior work (e.g., CEbound) that assumed no error.

- **Sequential LP sampling algorithm with 100% valid samples and convergence guarantees**: Algorithm 1 sequentially solves LPs to sample valid causal models from the constrained simplex, empirically achieving 100% valid samples (Table 2) compared to <10⁻⁴ for prior sampling bounds (CEbound). Propositions 4.1 and 4.2 provide formal convergence in probability and almost sure convergence under mild assumptions.

- **Improved regret dependence for function approximation**: Theorem 7.1 establishes regret O(√(𝔼_W[|𝒜^*(W)|] T log(δ⁻¹|ℱ^*| log T))), improving the dependence on function class size from √|Π| (as in boundingCE_continuous_IV) to √log|Π|. This improvement is in the functional form — even when |ℱ^*| = |ℱ|, the bound is √log|ℱ| vs. √|ℱ| — and is a genuine theoretical contribution.

- **Comprehensive regret analysis with matching lower bounds across all three tasks**: The paper provides both gap-dependent and minimax regret bounds for MAB (Theorem 5.1), finite-context CB (Theorems 6.2–6.3, with matching lower bound), and function-approximation CB (Theorems 7.1, 7.3). The lower bounds formally demonstrate near-optimality within the problem class.

- **Numerical validation confirming tighter bounds and faster convergence**: Experiments show the proposed causal bounds are tighter than those from non-linear optimization (Table 3: [0.371,0.466] vs. [0.283,0.505] for E[Y|do(A=0)]), and causally-enhanced algorithms achieve faster convergence than standard UCB and naive transfer.

## Weaknesses

### Fatal
None.

### Major

- **Discretization convergence for continuous variables is an open problem, narrowing the scope of theoretical guarantees**: The paper explicitly states (lines 586–588): "For general random variables, it is still an open problem that whether the solution to [the discretized optimization] will converge to the solution to [the original optimization] as the discretization becomes finer." Yet the abstract and introduction claim the paper handles "general context and reward distributions, whether discrete or continuous" (line 59). The convergence guarantees (Propositions 4.1, 4.2) are for the discretized problem only; extending to continuous settings requires convergence proof that the authors themselves identify as open. This means that, rigorously, the theoretical guarantees apply to discrete settings, not the full continuous setting advertised. The paper is transparent about this gap, but it materially reduces the scope of the claimed contribution.

### Minor

- **Full-support condition for the sampling measure is assumed but not verified for the sequential procedure**: Propositions 4.1 and 4.2 assume the sampling measure ℙ_s has full support on the feasible set (∀𝐱∈𝒟, ∀δ>0: ℙ_s(ℬ(𝐱,δ)∩𝒟) > 0). The paper states this "can be satisfied by various continuous distributions such as the uniform distribution, truncated Gaussian distribution, and others" (line 608), but does not prove that the sequential conditional sampling procedure (which fixes variables one by one) induces a joint distribution satisfying this condition. The feasible set is a convex polytope, so the claim is plausible, but a formal argument is absent.

- **Propagation of estimation error into bandit regret is not analyzed**: The paper incorporates estimation error ε into the causal bound computation (constraints |F−F̂| ≤ ε in Theorem 1), but the bandit regret analyses (Theorems 5.1, 6.2, 6.3, 7.1) assume the resulting bounds l(·), h(·) provably contain the true causal effect. There is no analysis of how finite-sample estimation error propagates into the regret bounds or whether the elimination/truncation steps remain valid when bounds are estimated rather than known exactly. For Task 2, a sample complexity bound for ε-identification is provided (Proposition 6.1), but not for Tasks 1 and 3.

- **Limited experimental scope**: The MAB experiment uses a single instance (5-armed Bernoulli with one probability configuration). The function approximation experiment uses a synthetic function class of only 50 functions and compares only against FALCON, not against other transfer learning baselines (e.g., TLinCB, TLinMAB, warm-start methods). No ablation study examines sensitivity to the discretization resolution or estimation error magnitude.

- **Near-duplicate presentation**: The "Infinite function classes" discussion appears nearly verbatim at lines 1028–1058 and again at lines 1062–1092. "Implementation details" (lines 1094–1112) largely repeats content from lines 971–987. This suggests insufficient final editing.

### Trivial
- No guidance is given for choosing discretization resolution to achieve a target approximation error, even for discrete variables.
- Minor grammatical issues (e.g., "we can tight obtain bounds" on line 336).

## Nice-to-Haves

- An analysis of how estimation error ε propagates into the bandit regret guarantees would significantly strengthen the paper.
- Ablation experiments varying the discretization resolution and showing how bound tightness changes would provide useful empirical guidance.
- Comparison against alternative transfer learning methods for bandits (TLinMAB, TLinCB) would better contextualize the empirical contribution.

## Removed Points

- **"The claim of improving order dependence from √|Π| to √log|Π| may be misleading"**: REMOVED — This criticism is factually incorrect. The paper's regret bound scales as √log|ℱ^*| while the comparison work bounds scale as √|Π|. Even if |ℱ^*| = |ℱ| = |Π|, the improvement from √ to √log in the dependence on function class size is genuine. The critic incorrectly claimed the improvement "depends on causal bounds substantially shrinking the function class," but the improvement is in the functional form (√log vs. √), not the cardinality. The paper explicitly explains the methodological difference (lines 1004–1008): the cited work treats each policy as an independent arm, preventing information sharing across similar policies.

- **"The sampling algorithm's convergence is not rigorously established" (as a structural gap)**: REMOVED from the major category — The paper states the full-support condition as an *assumption* and notes it "can be satisfied by various continuous distributions." While a more detailed justification would be welcome, stating a clear assumption and claiming it is satisfiable is standard in theoretical work. Moved to Minor as the unverified nature of the claim for the *specific sequential procedure* is a real but modest gap.

- **"Writing quality complaints about tables/grammar"**: REMOVED — Formatting artifacts are parser issues, not author errors. Minor grammar issues exist but do not impede understanding.

- **"Section-by-section notes about unclear information transfer / F(u) assumption"**: REMOVED — The paper clearly states that the expert provides F̂(a,y,w) and the agent has access to F̂(u) (lines 315–316, 328–330). The discussion of estimating F(u) from a subpopulation is explicit.

- **"Orders of magnitude claim not supported by experiments"**: REMOVED — The MAB experiments show approximately 5–7× regret improvement, which is significant. The phrase "orders of magnitude" in the abstract is rhetorical but typical for conference papers, and the experiments do demonstrate substantially faster convergence.

- **"Only one set of arm probabilities"**: REMOVED as a standalone weakness — noted instead within the broader "limited experimental scope" minor weakness; a single configuration is common for theory-heavy papers.

## Novel Insights

None beyond the paper's own contributions. The paper's honest disclosure of the discretization convergence gap (lines 586–588) is noteworthy as intellectual candor uncommon in the ML literature — it clearly delineates what is proved and what remains open. The modular separation between causal bound computation (via sequential LP sampling) and bandit algorithm design (using bounds as input) is methodologically clean, allowing each component to be improved independently. This design pattern could be useful for future work combining causal inference with online learning.

## Suggestions

1. Either prove discretization convergence for continuous variables (potentially under smoothness assumptions on the true distributions) or explicitly restrict the paper's theoretical claims to discrete/known-finite settings and clearly delineate continuous extensions as heuristic with empirical support.
2. Provide a proof or detailed argument that the sequential LP sampling procedure with typical truncated distributions (e.g., uniform, truncated Gaussian) induces a sampling measure satisfying the full-support condition on the convex polytope feasible set.
3. Analyze how the estimation error ε propagates into the bandit regret: e.g., if bounds are (1−δ)-valid with probability ≥ 1−δ, what is the resulting regret bound?
4. Expand the numerical experiments to include at least one additional MAB configuration, an ablation on discretization resolution, and a comparison with a simple transfer learning baseline (e.g., warm-start UCB).
5. Remove the near-duplicate "Infinite function classes" and "Implementation details" sections.

## Score and Decision

This paper makes meaningful contributions: a clean formalization of transfer learning in POCB as a causal inference problem, an efficient sequential LP sampling algorithm achieving 100% valid samples, and comprehensive regret analysis with matching lower bounds. The main concern — the unproven discretization convergence for continuous variables — is honestly disclosed but does limit the scope of the theoretical guarantees. The remaining issues (unverified sampling coverage condition, unanalyzed estimation error propagation, limited experiments) are addressable. The paper advances the state of the art in connecting causal inference with bandit transfer learning.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>