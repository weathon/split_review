- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 3, 6, 6, 6
Now I have all the information needed. Let me produce the consolidated review.

## Summary

The paper introduces Bisection Projection (BP), a post-processing framework to ensure NN-generated solutions for constrained optimization are feasible over general compact constraint sets with non-empty interior. The key idea is to train an auxiliary "Interior Points Neural Network" (IPNN) that maps problem parameters to carefully chosen interior points, then use bisection along the line from an infeasible prediction to an interior point to find a feasible boundary solution. The paper provides theoretical guarantees on feasibility, optimality loss (via a novel eccentricity measure connecting interior point quality to projection distance), and computational complexity (O(mKG) for m interior points, K bisection steps, G constraint-check cost). Experiments on convex QCQP, SOCP, non-convex AC-OPF, and joint chance-constrained inventory management show 100% feasibility rates with significant speedups over solver-based and homeomorphic projection baselines.

## Strengths

- **First theoretical framework for feasibility guarantees over general compact sets (beyond ball-homeomorphic).** The paper explicitly contrasts with prior work in Table 1: projection/warm-start methods are slow; penalty/sampling approaches lack guarantees; gauge functions only work on convex sets; homeomorphic projection (H-Proj) is restricted to ball-homeomorphic sets. BP works under Assumption 1 (compact, non-empty interior) which covers strictly broader classes including non-convex sets. This is a genuinely novel contribution to the NN-based constrained optimization literature.

- **Proposition 4.1: worst-case bound on bisection-induced projection distance via eccentricity.** This proposition establishes $\max\|\tilde{x}_\theta - \text{BP}(\tilde{x}_\theta, X_{\theta,m}^\circ)\| \leq \epsilon_{\text{pre}} + \mathcal{E}(X_{\theta,m}^\circ, \Gamma_\theta)$, directly tying optimality loss to the eccentricity of interior points modulated by the NN infeasibility region. This is a novel theoretical connection for general compact sets without any homeomorphism assumption.

- **Theorem 2: end-to-end guarantee with convergence and complexity.** Proves that after K bisection steps, the solution is guaranteed feasible, optimality loss is bounded by $\epsilon_{\text{pre}} + \mathcal{E} + 2^{-K}\text{diam}(\mathcal{C}_\theta)$, and complexity is O(mKG). The linear convergence in K is a concrete advantage over solver-based methods.

- **Principled IPNN training design.** The loss function (Eq. 6) combines adversarial Gaussian noise penalty (Eq. 7) to keep predictions away from boundaries with a log-sum-exp smoothed eccentricity loss (Eq. 8). Proposition 4.2 gives an explicit approximation gap $\hat{\mathcal{E}} - \log(mb^2)/\beta \le \bar{\mathcal{E}} \le \hat{\mathcal{E}} + \log(m)/\beta$, enabling differentiable optimization with controlled error.

- **Proposition 5.1: theoretical scaling of eccentricity with number of interior points.** Proves the minimum eccentricity decays as $\min\{\epsilon_{\text{pre}}, \mathcal{O}(m^{-1/(n-1)})\}$, providing a rigorous justification for using multiple interior points.

- **Strong empirical results across diverse problems.** BP achieves 100% feasibility on all four test problems with up to 10–150× speedup over solver-based methods. The AC-OPF experiment with >2,000 variables demonstrates scalability to high-dimensional non-convex settings. Table 3's sensitivity analysis directly validates the eccentricity design: ME-IPNN with 1 IP outperforms vanilla IPNN with 8 IPs.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The paper does not clarify whether its test problems (especially non-convex AC-OPF and JCCIM) are ball-homeomorphic.** H-Proj reports 100% feasibility on all four problems. If these problems happen to be ball-homeomorphic, the key claimed advantage over H-Proj in the experiments is speed, not generality—which is still a valid contribution but weaker than the paper's framing. If they are not ball-homeomorphic, the paper should explain how H-Proj was applied. Either way, the current presentation makes it impossible for the reader to assess how the experiments support the central generality claim.

- **The indicator function $\mathbf{1}_{\psi(\theta)\subset\mathcal{C}_\theta}$ in the IPNN loss (Eq. 6) is non-differentiable, and the paper does not explain how it is handled during gradient-based training** (e.g., via straight-through estimator, two-stage training where it is dropped once predictions are feasible, or simply ignoring gradients through it). This is a practical gap that affects reproducibility.

- **The bisection framework's behavior on disconnected feasible sets is not discussed.** Assumption 1 (non-empty interior) does not imply connectedness. If the constraint set has multiple disconnected components, an interior point in one component and an infeasible prediction near an optimal solution in another component could lead to bisection identifying a boundary point far from the true optimal solution, potentially invalidating the optimality bound. This limitation is not acknowledged.

- **No statistical uncertainty reported.** Tables 2 and 3 do not include confidence intervals, standard deviations, or run-to-run variation metrics. Given the stochasticity in NN training and boundary sampling, some measure of variance would strengthen the empirical claims.

- **The sufficient conditions in Theorem 1 (universal validity of IPNN) are acknowledged as hard to verify in practice.** The sample-based condition requires bounding $C_0$ (which may be infinite) and the verification-based condition is NP-hard. The paper is transparent about this limitation, but this means the theoretical conditions for universal validity are not practically actionable for most problems.

### Trivial
- None of note.

## Nice-to-Haves

- A synthetic experiment on a provably non-ball-homeomorphic set (e.g., non-simply-connected with a hole, or a set where the ball-homeomorphism property can be ruled out) would cleanly demonstrate the claimed generality advantage over H-Proj.

- A brief proof sketch of Proposition 4.1 in the main paper (e.g., the geometric intuition for how eccentricity bounds the projection distance) would help readers build trust without consulting the appendix.

- An ablation of boundary sample size $b$ during IPNN training on eccentricity approximation quality would strengthen the empirical section.

## Removed Points

- **"IPNN training appears circular" (Harsh Critic):** The paper explicitly states (line 182) that "the second eccentricity loss becomes active once IPNN outputs IPs under the first penalty loss," describing a phased, bootstrapped training pipeline. The critic's circularity concern stems from overlooking this description. **Removed** — the critic's claim does not match the paper content.

- **"Theoretical claims cannot be assessed without appendix":** Deferring proofs to an appendix is standard practice in conference submissions. The parser strips appendices from all papers. This is a formatting artifact, not a paper weakness. **Removed** per formatting-artifact rule.

- **"The comparison against H-Proj undermines the paper's core novelty claim (structural)":** The critic frames this as a fatal flaw. However, the paper's claim is that BP can handle general compact sets (theoretical property under Assumption 1), not that H-Proj fails on these specific benchmarks. H-Proj working on the tested problems does not contradict BP's greater generality—it just means these test problems may be ball-homeomorphic. The critic's framing as a "structural flaw that should prevent acceptance" is too harsh. The point is retained as a **Minor** weakness (about clarity and experimental design), not a fatal one.

- **Generic/superficial strengths from the Strength Finder:** None were present; all listed strengths are specific and evidence-backed. No removals needed.

## Novel Insights

Both reviewers converge on a useful observation: the paper's strongest contribution may not be "breakthrough in generality" as framed, but rather a **practical, fast, and theoretically grounded feasibility correction method** for general compact sets. The speed advantage over H-Proj (20× on AC-OPF) and the connection between eccentricity and optimality loss (Proposition 4.1) are independently valuable, even if the "generality" framing is partly aspirational given the experimental test problems. The disconnected-set issue is a genuine limitation not discussed in the paper: for multi-component feasible regions, the bisection procedure could land on a boundary point far from the optimal solution, and the eccentricity bound would not capture this failure mode.

## Suggestions

1. **Address the H-Proj comparison head-on.** Explicitly state for each test problem whether it is ball-homeomorphic. If the non-convex problems are provably not ball-homeomorphic, explain how H-Proj was applied (or if H-Proj results used some approximation). If they are ball-homeomorphic, acknowledge this and reframe the contribution around the speed/runtime advantage of BP on large-scale problems.

2. **Explain how the indicator function in Eq. (6) is handled during training.** A brief note about whether gradients flow through it, or whether training proceeds in two phases (first penalty-only then add eccentricity), would resolve the ambiguity.

3. **Add a brief discussion of disconnected feasible sets.** Acknowledge that for multi-component sets under Assumption 1, the optimality bound may be loose, and note whether the test problems satisfy connectedness.

4. **Include standard deviations or confidence intervals for the main metrics** (feasibility rate, optimality gap) across multiple training runs or data splits.

5. **Provide a proof sketch of Proposition 4.1** in the main paper (2–3 lines of geometric intuition) to make the eccentricity–projection distance link self-contained.
