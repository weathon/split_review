## Summary
# Final Review Report

## Summary

This paper studies distributed temporal-difference (TD) learning for networked multi-agent Markov decision processes (MAMDPs) from a primal-dual perspective. The authors propose a distributed TD-learning algorithm inspired by the control-theoretic distributed optimization framework of Wang and Elia (2011), which does not require a doubly stochastic consensus matrix — a restrictive assumption in prior distributed TD theory. The paper makes four main contributions: (C1) an improved exponential convergence rate for continuous-time primal-dual gradient dynamics with null-space constraints under specific conditions (symmetric, rank-deficient constraint matrix and linear gradient structure); (C2) a new distributed TD-learning algorithm derived from this primal-dual ODE; (C3) finite-time mean-squared error bounds under both i.i.d. and Markovian observation models with constant and diminishing step-sizes; and (C4) empirical validation on synthetic MAMDPs.

The paper is technically solid: the Lyapunov-based analysis is rigorous, and the elimination of the doubly stochastic matrix is a genuine practical advantage. However, the paper has several significant weaknesses: the experimental validation is minimal (3 states, 2 features), the important baseline comparison is relegated to the appendix, the dual variable mechanism lacks intuitive explanation, the O()-notation hides potentially large dependencies on graph spectral properties, and the introduction does not clearly articulate the research gap. The novelty of C1 relative to prior primal-dual analysis (Ozaslan and Jovanovic 2023, Gokhale et al. 2023) needs external verification, which is deferred due to retrieval constraints in this review.

## Strengths
1. **Novel algorithmic advantage**: The key strength is the elimination of the doubly stochastic matrix requirement, which is a genuine practical improvement over existing distributed TD methods (Doan et al., 2019; Sun et al., 2020; Wang et al., 2020). The PI (proportional-integral) consensus mechanism via an auxiliary dual variable provides an elegant control-theoretic solution to the multi-agent consensus problem in policy evaluation.

2. **Rigorous theoretical analysis**: The paper provides finite-time MSE bounds for both i.i.d. and Markovian observation models, under both constant and diminishing step-sizes. The Lyapunov-based proof framework is sound, and the use of the projected iterate (L L^\dagger on the dual variable) to handle the null-space of the graph Laplacian is a clean technical contribution. The exponential convergence and O(1/k) rates match the best-known rates in the single-agent TD setting.

3. **N-independence**: The bounds do not explicitly depend on the number of agents N, which is an improvement over Doan et al. (2019) and Sun et al. (2020) where the bias/rate scales with N. This is a meaningful theoretical advantage for large-scale multi-agent systems.

4. **Transparent graph-dependency**: The bounds explicitly involve lambda^+_min(L) (graph connectivity) and lambda_max(L) (maximum degree), providing theoretical guidance for how graph topology affects convergence.

5. **Comprehensive appendix**: The appendix (42 pages) contains detailed proofs of all lemmas and theorems, the Markovian observation model analysis, additional experiments, and a comparison with doubly-stochastic-based methods that demonstrates the practical fragility of prior approaches.

## Weaknesses
1. **Minimal experimental validation (major)**: The experiments use a synthetic MAMDP with only 3 states and 2 features. This toy setup is insufficient to demonstrate practical relevance or scalability. Baseline comparisons with existing distributed TD methods (Doan et al., 2019; Wang et al., 2020) are confined to Appendix A.13, even though they strongly support the paper's core thesis. No error bars or standard deviations are reported despite averaging over 50 runs.

2. **Missing intuitive explanation for dual variable (major)**: The dual variable w and its update (Eq 8) are introduced without intuitive motivation. Readers unfamiliar with the Wang-Elia (2011) framework will not understand why this variable is needed or how it eliminates the doubly stochastic matrix requirement. The proportional-integral (PI) consensus interpretation is never mentioned.

3. **O-notation obscures critical dependencies (major)**: The convergence bounds in Theorems 4.2 and 4.3 rely heavily on the condition number of the Lyapunov matrix G, which in turn depends on lambda_max(L_bar)^2 / ((1-gamma) w). For ill-conditioned features (small w) or poorly connected graphs (small lambda^+_min), the effective convergence rate can be extremely slow. This is not discussed.

4. **Restrictive assumptions for Section 3 (major)**: The analysis of primal-dual gradient dynamics assumes a linear gradient structure (grad f = U*theta) and symmetric M. These assumptions are technically satisfied by the TD setting but limit the generality claimed in Contribution 1.

5. **Weak introduction storyline (major)**: The introduction fails to clearly articulate the specific limitations of prior work before presenting the paper's approach. The research gap ("theoretical understanding...has not been fully explored") is stated too vaguely. The doubly stochastic matrix limitation should be the centerpiece of the opening narrative.

6. **Conclusion is inadequate (major)**: The conclusion (9 lines) merely recaps the paper and mentions one vague future direction. There is no discussion of limitations, no empirical summary, and no roadmap for practical deployment.

7. **Novelty verification deferred**: Due to runtime retrieval constraints in this review, the claimed improvement over Ozaslan and Jovanovic (2023) and Gokhale et al. (2023) cannot be independently verified against external literature. The convergence rate comparison in Appendix A.6 appears to show improvement (O(exp(-lambda_min(U)*t)) vs O(exp(-lambda_min(U)^3*t))) but needs manual literature verification.

8. **Reproducibility concern**: The algorithm's stability depends sensitively on eta (Section 5 shows divergence for eta=0.5 and eta=1 on a random graph). No procedure for selecting eta is provided beyond a heuristic guidance about lambda_max(L).

## Key Issues
The following ranked error board prioritizes defects by severity, research-value impact, validity risk, fixability, and confidence.

| Rank | Issue | Severity | Validity Risk | Research-Value Impact | Fixability | Confidence |
|------|-------|----------|--------------|----------------------|------------|------------|
| 1 | Minimal experiments (3 states, 2 features); baselines in appendix | Major | High | High | Fixable | High |
| 2 | No intuitive explanation of dual variable / PI structure | Major | Medium | High | Fixable | High |
| 3 | O()-notation hides condition number & graph dependency | Major | High | Medium | Partially fixable | High |
| 4 | Missing limitations and practical guidance (eta selection) | Major | Medium | High | Fixable | High |
| 5 | Weak introduction narrative: gap not clearly stated | Major | Low | Medium | Fixable | High |
| 6 | Novelty verification deferred (external lit unavailable) | Verification | Medium | High | Requires external check | Medium |
| 7 | Conclusion is too brief, no practical discussion | Minor | Low | Medium | Fixable | High |
| 8 | No statistical variability (error bars) in experiments | Minor | Medium | Medium | Fixable | High |

**Detailed issue explanations:**

**Issue 1 (Experiments insufficient)**: The MAMDP has 3 states and 2 features, which is too small to establish any meaningful claim about scalability or practical applicability. The comparison with Doan et al. (2019) and Wang et al. (2020) in Appendix A.13 is informative and should be in the main paper. No standard deviations or confidence intervals are reported. *Fix:* Expand to at least one standard benchmark (chain MDP, grid-world), report mean +/- std over 50 seeds, and move baseline comparisons to the main paper.

**Issue 2 (Dual variable motivation)**: The dual update (Eq 8) integrates consensus error but this PI control interpretation is never stated. This makes Algorithm 1 appear ad hoc. *Fix:* Add 2-3 sentences explaining that the dual variable acts as an integral controller that accumulates consensus errors, eliminating the need for a doubly stochastic mixing matrix.

**Issue 3 (Hidden constants)**: The convergence rate expression "O(exp(-alpha0 k) + bias)" hides that the decay rate constant is proportional to min{1, eta*lambda^+_min^2} * (1-gamma)*w / (lambda_max^2 * (8/eta + 4*eta*lambda_max^2)). For graphs with small lambda^+_min (poor connectivity) or features with small w (near-collinear), the effective rate can degrade severely. The paper should explicitly bound this constant. *Fix:* Add a remark after Theorem 4.2 that provides the explicit decay constant and discusses its dependence on problem parameters.

**Issue 4 (No practical guidance)**: The algorithm requires tuning eta, and the experiments show sensitivity (divergence for eta=0.5 or eta=1 on a random graph). The paper gives no procedure for selecting eta beyond a heuristic involving lambda_max(L). *Fix:* Add a paragraph on eta selection: suggest using the heuristic eta ~ 1/lambda_max(L) with a safety margin, and describe the trade-off between convergence speed and stability.

**Issue 5 (Introduction narrative)**: The introduction skips directly from generic RL background to listing contributions without clearly articulating why the doubly stochastic matrix is restrictive. The gap statement is too generic. *Fix:* Restructure the introduction to: (i) motivate distributed policy evaluation, (ii) identify the doubly stochastic assumption as the key limitation, (iii) explain why removing it matters, (iv) present the primal-dual solution, (v) state contributions.

**Issue 6 (Novelty verification)**: The comparison with Ozaslan and Jovanovic (2023), Cisneros-Velarde et al. (2020), and Gokhale et al. (2023) in Appendix A.6 appears favorable, but external literature was not retrievable in this review session. *Fix:* Authors should provide a dedicated comparison table with explicit convergence rate formulas from each prior work to facilitate reviewer verification.

## Actionable Suggestions
### S1: Expand Experimental Validation (Must)

**Problem**: The current experimental setup (3 states, 2 features) is insufficient to support the paper's claimed practical significance.

**Action**: 
1. Increase the state space size to at least 10-20 states and use random feature matrices to test robustness.
2. Include at least one standard benchmark (e.g., chain MDP from Sutton and Barto or a simple grid-world).
3. Report mean $\pm$ standard deviation over 50 independent runs with different random seeds.
4. **Critical**: Move Figures 3 and 4 from Appendix A.13 into the main paper. These figures demonstrate that Wang et al. (2020) diverges under least-squares doubly stochastic construction, which is strong evidence for the paper's main claim.
5. Include a convergence trajectory plot with multiple eta values for at least one benchmark setting to demonstrate stability sensitivity.

**Acceptance criteria**: A reader (reviewer) can independently verify that the algorithm converges in a practically meaningful setting and that it outperforms or matches existing methods on at least one non-toy problem.

### S2: Add Intuitive Explanation of Dual Variable (Must)

**Problem**: The dual variable $w_i$ and its update rule lack intuitive motivation.

**Action**: Add a paragraph after Algorithm 1 explaining:
"The dual variable $w_i$ accumulates the consensus error (difference between $\theta_i$ and its neighbors' parameters) over time. This creates a proportional-integral (PI) control structure: the primal update (7) contains a proportional consensus penalty $\eta(|N_i|\theta_i - \sum_{j\in N_i}\theta_j)$, while the dual update (8) integrates this error. The integral action ensures that all agents' parameters converge to a common value without requiring the normalization enforced by a doubly stochastic matrix."

### S3: Make Hidden Constants Explicit (Must)

**Problem**: The O()-notation in Theorems 4.2 and 4.3 hides critical dependencies.

**Action**: After each theorem, add a remark of the form:
"The exponential decay constant $c$ in Theorem 4.2 satisfies
$$c = \Theta\left(\frac{\min\{1, \eta\lambda^+_{\min}(\bar{L})^2\}(1-\gamma)w}{\lambda_{\max}(\bar{L})^2(8/\eta + 4\eta\lambda_{\max}(\bar{L})^2)}\right).$$
This shows that the convergence rate degrades with poor graph connectivity (small $\lambda^+_{\min}$) and ill-conditioned features (small $w$). The bias term scales as $O(\alpha_0 R_{\max}^2 / (w^3(1-\gamma)^3))$, which can be large when the feature covariance is near-singular."

### S4: Improve Introduction Narrative (Nice-to-have)

**Problem**: The introduction does not clearly articulate the research gap.

**Action**: Restructure the introduction paragraphs as follows:
- **P1 (Current)**: Generic TD background. → Replace with specific motivation for distributed policy evaluation in multi-agent systems.
- **P2 (Current)**: List of existing distributed TD works. → Replace with focused critique: all existing methods require doubly stochastic matrices, which creates sensitivity to graph structure and construction method.
- **P3 (Current)**: Contribution list. → Keep but sharpen the wording.
- **New P4**: Introduce the primal-dual control-theoretic approach as a natural solution.

### S5: Expand Conclusion (Nice-to-have)

**Problem**: The conclusion is only 4 lines and lacks discussion of limitations.

**Action**: Write a conclusion with three paragraphs:
1. **Validated findings**: What rates were proved, under what assumptions, and the key advantage (no doubly stochastic matrix).
2. **Limitations**: eta sensitivity, linear approximation only, synthetic experiments, graph connectivity dependence.
3. **Future work**: Adaptive eta selection, extension to directed/time-varying graphs, nonlinear function approximation, and benchmark evaluations.

### S6: Provide Dataset/Runtime Specifications (Minor)

**Problem**: No information about computation time, hardware used, or memory requirements.

**Action**: Add one sentence: "All experiments were run on [hardware], with average wall-clock time per 40,000-iteration run of approximately [time] seconds for N=[number] agents." Also provide the peak memory per agent.

## Storyline Options + Writing Outlines
### Abstract Outline (Revised)

**S1** (Problem): "This paper studies distributed temporal-difference (TD) learning for networked multi-agent Markov decision processes."

**S2** (Challenge): "Existing distributed TD algorithms require a doubly stochastic consensus matrix, which is restrictive for directed or time-varying communication graphs and introduces sensitivity to the matrix construction method."

**S3** (Approach): "We propose a distributed TD-learning algorithm derived from primal-dual ordinary differential equation (ODE) dynamics, equipped with an auxiliary dual variable that eliminates the need for a doubly stochastic matrix."

**S4** (Key Result 1): "For the continuous-time primal-dual ODE with symmetric rank-deficient constraints, we establish exponential convergence with a rate that improves on prior bounds when the strongly-convex parameter is small."

**S5** (Key Result 2): "For the discrete-time stochastic algorithm, we prove finite-time mean-squared error bounds under both i.i.d. and Markovian observations: exponential convergence to a small bias under constant step-sizes and O(1/k) under diminishing step-sizes. The bounds depend on graph connectivity but not on the number of agents."

**S6** (Validation): "Experiments on synthetic MAMDPs validate the theory and demonstrate that careful tuning of the variance-control parameter eta prevents divergence."

### Introduction Outline (Paragraph-by-Paragraph)

**P1 — Practical Motivation and Gap (Revised)**
- Role: Establish why distributed policy evaluation matters and identify the key limitation of prior work.
- Claim: Existing distributed TD methods rely on doubly stochastic matrices, which are fragile in practice.
- Transition: "This limitation motivates a fundamentally different approach."

**P2 — Proposed Solution (Revised)**
- Role: Introduce the primal-dual control-theoretic perspective.
- Claim: By adopting the Wang-Elia (2011) framework, we can design a distributed algorithm that avoids the doubly stochastic assumption and admits finite-time analysis.
- Transition: "Our main contributions are as follows."

**P3 — Contribution List (Keep but sharpen)**
- Role: List the four contributions with precise, testable claims.
- Key improvement: Replace "improved or comparable" with specific condition-dependent claim.

**P4 — Related Works Overview (Revised)**
- Role: Position the paper within the distributed optimization and distributed TD literature.
- Structure: Organized by (a) optimization framework (consensus vs. control-theoretic vs. primal-dual) and (b) application to TD learning.
- Key improvement: Explicitly state how this paper differs from each category.

### Alternative Storyline Candidates

**Candidate A (Current):** Primal-Dual ODE Theory → Discretization → Distributed TD Algorithm → Finite-Time Bounds → Experiments. 
- *Strength*: Logically clean, theory-first structure.
- *Weakness*: The connection between Section 3 (abstract ODE) and Section 4 (practical algorithm) is weak. The reader must wait until Section 4 to understand why the ODE analysis matters.

**Candidate B (Recommended):** Distributed TD Problem → Doubly Stochastic Limitation → PI Control Intuition → Algorithm → ODE Model for Analysis → Finite-Time Bounds → Experiments.
- *Strength*: Problem-first structure keeps the reader engaged. The PI intuition is explained before the abstract ODE analysis.
- *Alignment check*: 
  - (a) Problem alignment: The practical limitation (doubly stochastic requirement) → PI solution is clear.
  - (b) Variable alignment: The dual variable w is introduced with intuitive purpose before the abstract analysis.
  - (c) Contribution-evidence alignment: Experiments directly test the algorithm, and the comparison with baselines validates the core claim.

**Recommended abstract writing blueprint:**
"Distributed temporal-difference (TD) learning enables multiple agents to cooperatively evaluate a value function using local rewards and neighbor communication. A significant practical limitation of existing methods is their reliance on doubly stochastic consensus matrices, which are difficult to construct for directed or time-varying graphs and sensitive to the construction method. We develop a distributed TD algorithm that removes this requirement by adopting a primal-dual control-theoretic framework, where an auxiliary dual variable accumulates consensus errors to drive parameter agreement. The underlying continuous-time dynamics are analyzed through a novel Lyapunov function that exploits the symmetry and rank-deficiency of the graph Laplacian, yielding an exponential convergence rate that improves on prior bounds under small strong-convexity parameters. Discretizing these dynamics gives a practical algorithm for which we prove finite-time mean-squared error bounds: O(exp(-c k) + bias) under constant step-sizes and O(1/k) under diminishing step-sizes, covering both i.i.d. and Markovian observation models. The bounds are independent of the number of agents and depend explicitly on graph spectral properties. Experiments on synthetic MAMDPs validate the theory, showing that careful tuning of a variance-control parameter is crucial for stability."

## Priority Revision Plan
### P0 Items (Critical for Publication)

| Item | Priority | Effort | Impact | Action |
|------|----------|--------|--------|--------|
| Expand experimental validation | P0 | High | High | Add benchmark MDP, report mean±std, move baseline comparison (Appendix A.13) to main text |
| Add intuitive explanation of dual variable | P0 | Low | High | Add 3 sentences after Algorithm 1 explaining PI control interpretation |
| Make hidden constants explicit | P0 | Low | Medium | Add remark after Theorem 4.2 with explicit decay rate constant and dependence on w, λ_min, λ_max |

### P1 Items (Strongly Recommended)

| Item | Priority | Effort | Impact | Action |
|------|----------|--------|--------|--------|
| Improve introduction narrative | P1 | Medium | High | Restructure to problem-first: doubly stochastic limitation → PI solution → contributions |
| Expand conclusion | P1 | Low | High | Add limitations, practical guidance, and specific future directions |
| Add eta selection guidance | P1 | Low | Medium | Provide heuristic rule and discuss stability-accuracy trade-off |
| Add statistical variability reporting | P1 | Low | Medium | Add std/confidence intervals to all plots |

### P2 Items (Quality Improvements)

| Item | Priority | Effort | Impact | Action |
|------|----------|--------|--------|--------|
| Augment Table 1 | P2 | Low | Medium | Add convergence rate and per-iteration communication cost columns |
| Add runtime/memory specifications | P2 | Low | Low | Report hardware, wall-clock time, and peak memory per agent |
| Stylistic polish | P2 | Low | Low | Remove "improved or comparable" hedge; use specific condition-dependent wording |

### Revision Workflow

```text
ASCII Diagram — Revision Strategy Roadmap

[P0: Expand Experiments]
    → Move baseline comparison (App A.13) to main text
    → Add benchmark MDP + error bars
    → Expected: Stronger empirical support for core claim

[P0: Add Dual Variable Intuition]
    → Insert PI control explanation after Algorithm 1
    → Expected: Reader can understand algorithm without reading Wang & Elia (2011)

[P0: Make Constants Explicit]
    → Add remark after Theorem 4.2 with explicit decay constant
    → Expected: Reviewers can assess practical convergence speed

[P1: Restructure Introduction]
    → Problem-first narrative: doubly stochastic limitation → PI solution
    → Expected: Clearer contribution positioning

[P1: Expand Conclusion]
    → Add limitations + eta guidance + specific future work
    → Expected: Paper feels complete and self-critical

[P2: Augment Table 1 + Polish]
    → Add comparison axes, fix hedging language
    → Expected: Ready for submission
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|--------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Test convergence vs graph size (cycle graph) | 3-state MDP, 2-d features, N ∈ {8,16,32}, cycle graph, constant α ∈ {2^-3,2^-4,2^-5}, η=1, 40k iters, 50 runs | MSE(θ_k - 1_N⊗θ_c) | MSE increases with N (smaller λ+_min) | C3 (graph connectivity affects bias) | Tiny MDP, no comparison baselines |
| E2 | Test effect of λ_max (star graph) | Same MDP, star graph, N ∈ {8,16,32}, η=1 | MSE | Bias increases with N (larger λ_max) | C3 | Only shown in appendix; diverging cases omitted |
| E3 | Test effect of η (random graph) | Same MDP, N=32, random graph, α=0.1, varying η | MSE trajectory | η too large (0.5,1) diverges; optimal η ≈ √2/λ_max(L) | C3 (η controls variance) | No guidance for η selection |
| E4 | Diminishing step-size (cycle/star) | Same MDP, α_k = N²/(N³+k) | MSE | O(1/k)-like decay observed | C3 | No rate comparison |
| E5 | Baseline comparison (Appendix) | Same MDP, N∈{8,16,32}, least-squares and Sinkhorn-Knopp doubly stochastic constructions, α=1/2³ | MSE | Wang et al. diverges under least-squares; Doan et al. shows sensitivity | C2 (no doubly stochastic needed) | Only in appendix, limited N values |

### Research-Theme Gap Diagnosis

1. **New Knowledge (partially supported)**: The theoretical bounds (C3) are novel in their explicit handling of the null-space constraint and elimination of the doubly stochastic requirement. However, the claimed improvement in convergence rate (C1) requires external verification.
2. **Reproducibility (partially supported)**: The algorithm is described in detail, but the eta sensitivity and lack of selection procedure make reproduction fragile. No code is provided.
3. **Impact on Practice/Understanding (weakly supported)**: The minimal experiments do not demonstrate impact on any practically relevant problem. The baseline comparison showing divergence of Wang et al. (2020) under poor doubly stochastic construction is potentially impactful but relegated to the appendix.

### Proposed Research Experiments

**P0 — Benchmark MDP Evaluation**
- Target Claim: C3 (finite-time bounds hold in practice), C2 (algorithm works without doubly stochastic matrix)
- Hypothesis: The algorithm converges on a standard benchmark with performance comparable to or better than existing methods
- Minimal Design: 10-state chain MDP, 4-dimensional Fourier features, N=16 agents on a cycle graph. Compare with Doan et al. (2019) and Wang et al. (2020) (with Sinkhorn-Knopp doubly stochastic matrix).
- Controls/Baselines: Same MDP, same initializations, same compute budget. Report mean ± std over 50 seeds.
- Metrics: MSE(θ_k - θ_c), wall-clock time to convergence threshold.
- Success Criterion: Algorithm converges for all seeds; median MSE comparable to or lower than baselines.
- Cost/Time: Low-Medium (1-2 days of coding + running).
- Expected Quality Gain: High — addresses the most critical weakness.

**P1 — eta Sensitivity Study**
- Target Claim: C3 (η controls variance), practical guidance
- Hypothesis: The optimal η scales as 1/λ_max(L) with constant factor C
- Minimal Design: Vary graph type (cycle, star, random, complete) and N ∈ {8,16,32,64}. For each, sweep η ∈ {0.001, 0.01, 0.046, 0.1, 0.5, 1, 5}. Record convergence success rate and final MSE.
- Metrics: Convergence flag (MSE < threshold), final MSE, number of diverging seeds.
- Success Criterion: Identify stable η range as function of λ_max(L) and λ+_min(L).
- Cost/Time: Low (can be automated).
- Expected Quality Gain: High — provides practical η selection rule.

**P1 — Statistical Reliability Analysis**
- Target Claim: C3 (tightness of bounds)
- Hypothesis: The empirical MSE decay rate is consistent with the theoretical rate constant
- Minimal Design: Extract empirical decay rate from log(MSE) vs iteration slope; compare with predicted lower bound from Theorem 4.2.
- Metrics: Empirical rate constant, ratio of empirical to theoretical rate.
- Success Criterion: Empirical rate is within a constant factor of the theoretical bound.
- Cost/Time: Low (post-processing of existing data).
- Expected Quality Gain: Medium — strengthens confidence in bounds.

**P2 — Scalability Test**
- Target Claim: C3 (N-independence of bounds)
- Hypothesis: For a fixed graph topology, increasing N does not degrade per-agent MSE
- Minimal Design: Cycle graph with N ∈ {8,16,32,64,128}, same MDP, fixed α and η.
- Metrics: Per-agent MSE after T iterations.
- Success Criterion: MSE ≤ C * (theoretical bias) for all N, with C independent of N.
- Cost/Time: Medium (need larger experiments).
- Expected Quality Gain: Medium — validates the N-independence claim.

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2)

Stage 1 (P0 - Before Resubmission):
    [Benchmark MDP] → [Compare with baselines in main text]
    → [Report mean±std] → [Move App A.13 to main paper]
    → Expected: Strong empirical section

Stage 2 (P1 - Before Resubmission):
    [eta sensitivity sweep] → [Derive practical heuristic]
    → [Statistical reliability analysis]
    → Expected: Reproducible, well-understood algorithm

Stage 3 (P2 - Next Revision):
    [Scalability test up to 128 agents]
    → Expected: Validate N-independence claim
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

*Evidence-grounded score emphasizing research value + novelty:*

The paper presents a theoretically rigorous framework for distributed TD-learning without doubly stochastic matrices, which is a genuine algorithmic advantage. The Lyapunov-based analysis is technically sound and the finite-time bounds are meaningful. However, the score is reduced by:
- Minimal experimental validation (3-state MDP), which limits the demonstrated research value (weakness #1).
- The claimed improvement in convergence rate (C1) requires external literature verification that was unavailable in this review session (deferred).
- The introduction and conclusion do not effectively communicate the paper's significance.
- The O()-notation obscures potentially large constants, making it hard to assess practical relevance.
- The algorithm's sensitivity to eta without selection guidance raises reproducibility concerns.

**Post-Revision Target: [6.5, 7.5]/10**

If all P0 and P1 items are addressed — specifically, experimental validation on a benchmark MDP with baseline comparisons in the main text, explicit decay constants, intuitive explanation of the dual variable, expanded conclusion with limitations, and improved introduction narrative — the paper would provide a solid theoretical contribution with demonstrated practical relevance. The upper bound of 7.5 assumes that the novelty claims in C1 are externally verifiable and that the experimental results are favorable.

**Score Breakdown:**
- Novelty: 6/10 (dual variable approach is novel; rate improvement needs verification)
- Research Value: 5/10 (strong theory, weak empirical demonstration)
- Validity/Soundness: 7/10 (proofs appear correct; experiments lack statistical rigor)
- Reproducibility: 4/10 (eta sensitivity without selection guidance; no code; minimal setup)
- Presentation: 5/10 (intro needs restructuring; conclusion too brief; notation heavy)