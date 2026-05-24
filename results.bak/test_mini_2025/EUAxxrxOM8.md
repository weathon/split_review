Now I'll write the final consolidated review.

## Summary

The paper proposes an MPC-based policy (called LP-update) for infinite-horizon average-reward restless bandits, where at each time step the policy solves a τ-horizon linear program. The core theoretical contribution is a sub-optimality gap of O(1/√N) under a mild coupling assumption (Assumption 1: ρ_k > 0) and exponential convergence O(e^{-cN}) under additional local stability conditions. The proof introduces dissipativity — a framework from the MPC literature — to the RMAB setting, connecting the finite-horizon and infinite-horizon problems. Experiments on three examples show the method performs well against the LP-priority (Gast et al., 2023a) and FTVA (Hong et al., 2023) baselines.

## Strengths

1. **Weakest theoretical assumptions among comparable guarantees.** Theorem 4.1 requires only Assumption 1 (ρ_k > 0 for some k), which is strictly weaker than the synchronization assumption of Hong et al. (2023) and avoids indexability or UGAP required by Whittle-index methods. The paper makes this explicit (Section 4.1, page 5) and provides intuition for why the condition is mild (e.g., satisfied when P^0 is ergodic).

2. **Novel use of dissipativity to bridge finite- and infinite-horizon RMAB.** The paper introduces a dissipativity framework (Section 5.1, Part 2) to show that the rotated-cost finite-horizon value function L_τ(x) is monotone in τ. This enables bounding the sub-optimality gap via the inequality L_τ(x) - L_{τ-1}(x) < ε. This is a fresh technical approach for the RMAB literature, and importantly it does not require steering towards a fixed point or UGAP.

3. **Consistent practical superiority over FTVA across diverse settings.** Figures 4(b) and 4(c) demonstrate that LP-update maintains near-optimal normalized gain as the state space grows and as the budget α increases, while FTVA degrades in both cases. This robustness is a clear practical advantage over a state-of-the-art competitor.

4. **Practical insensitivity to the planning horizon τ.** Figure 4(a) shows that the normalized gain is nearly identical for τ = 3, 5, 10, making the algorithm computationally efficient with short horizons. This is explicitly noted: "the influence of the parameter τ is marginal" (Section 6).

5. **Exponential convergence under local stability.** Theorem 4.2 provides a sub-optimality gap of ε + C' e^{-C'' N} under Assumptions 2–4, matching the best-known exponential rates in the literature (Gast et al., 2023a; Hong et al., 2024a) but with a simpler algorithmic construction.

## Weaknesses

### Fatal
None.

### Major

1. **The λ disconnect between theory and practice is not adequately addressed.** The paper states (Section 3.1, line 115) that "our proofs will hold with minor modification by replacing λ by 0 and in practice we do not use this multiplier for our algorithm." However, the entire dissipativity argument (Section 5.1, Part 2) uses λ·x as the storage function to ensure the rotated cost l̃(x,u) is non-negative, which in turn establishes the monotonicity of L_τ and the key inequality (17). The paper provides no sketch in the main text — and, from what is available, no justification at all — for why setting λ = 0 would preserve the proof. Without λ, the storage function vanishes and proving l̃(x,u) ≥ 0 is no longer straightforward (since transient (x,u) may have R(x,u) > g* in the absence of the dual correction). This creates real uncertainty about whether the theoretical guarantee in Theorem 4.1 actually applies to the algorithm that was evaluated. Either the theory should cover the implemented algorithm (requiring λ to be used or a modified proof), or the paper should clearly delineate which claims are theoretically proven and which are empirically observed.

Note: If the appendix (which is stripped in this extract) provides the "minor modification" proof for λ = 0, this concern would be substantially alleviated, but the main text should at minimum sketch the modification.

### Minor

2. **The bound constants in Theorem 4.1 are not quantified.** The sub-optimality gap (11) involves k/ρ_k, C_λ, C_Φ, and C_ψ. As the paper acknowledges, ρ_k could be arbitrarily small (e.g., near-zero coupling probability), making k/ρ_k arbitrarily large. The bound therefore guarantees an O(1/√N) rate but does not provide a practically meaningful numerical gap. This is a limitation shared with many such theoretical results and should be acknowledged candidly, along with a discussion of when the constants could be large in practice.

3. **The experiments lack error bars or measures of variance.** Figure 1 shows single-trace performance curves without confidence intervals. Figure 4 aggregates 20 random instances into a single average line with no indication of spread. Given that RMAB is a stochastic problem and the plots are central to the practical claims, reporting variance (e.g., standard deviation or percentile bands) would significantly strengthen the evidence.

4. **No discussion of computational cost.** The algorithm solves an LP of size O(τ|S|) at each time step. The paper should report typical solve times (e.g., in milliseconds) and compare them to the baselines, especially since FTVA and LP-priority are cheaper (LP-priority solves a single LP once). For practitioners evaluating the method, this information is directly relevant to whether the performance gains justify the additional computation.

5. **The role of randomized rounding in preserving the per-step budget constraint is not checked.** The paper introduces rounding error analytically but does not verify that the rounding procedure never produces a flagrant budget violation (e.g., pulling more than αN arms in a time step). A brief check in the experiments would be useful.

### Trivial

6. The dependence of τ(ε) on ε is stated as O(1/ε) in the text following Theorem 4.1 but the bound itself would benefit from making this more explicit.

## Nice-to-Haves

- An explicit worked example (e.g., two-state arms) with concrete numerical values for the constants in the bound would illustrate that the bound is not vacuous.
- The paper could explicitly state why Whittle index is not compared as a baseline (e.g., because the examples are not guaranteed to be indexable, or because LP-priority serves as the natural LP-based analogue).
- A limitations paragraph acknowledging when Assumption 1 might be hard to verify or when the constants could be large would strengthen the paper.

## Removed Points

- **Missing Whittle index baseline** (Harsh Critic point #2): Removed. LP-priority (Gast et al., 2023a) is a priority-index policy derived from the same LP relaxation — it does not require indexability and serves as the natural modern baseline. The paper compares against it and finds LP-update comparable or better. Whittle index requires indexability, a strong condition not needed by the paper's method, so its absence is not an evidential gap.
- **Reproducibility details** (Harsh Critic point): Removed. The paper states code is in supplementary material, which is the standard for this venue.
- **Criticism about the bound's rate presentation** (Harsh Critic point #3): The critic's framing that constants "could absorb the entire sub-optimality gap" is overwrought; the bound guarantees a rate, which is standard for such results. Demoted to Minor point #2 above.
- **"Strawman" about Section 5 circularity** (Harsh Critic): The claim that the reasoning is circular is incorrect — dissipativity gives non-negative rotated cost, non-negative cost implies monotonicity, and the proof is standard in MPC literature. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Resolve the λ disconnect: either (a) include λ in the practical implementation and add a brief note on how it affects the solution, or (b) if the appendix already contains a proof for λ = 0, state the modification explicitly in the main text (even a one-paragraph sketch). Without this, readers cannot judge whether Theorem 4.1 applies to the evaluated algorithm.
2. Add standard deviation or percentile bands to the experimental plots, especially Figure 4.
3. Add a brief computational cost comparison (solve time per step for LP-update vs. baselines).
4. Acknowledge the potential size of the bound constants explicitly in the main text, not just implicitly.

## Score and Decision

**Calibration anchors:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Continuous-time Linear Systems (rejected) | 5.5 | R1 | Similar level of theory + experiments; current paper has stronger proof novelty but a concerning unresolved gap |
| Burning RED (rejected) | 4.5 | R1 | Had derivation errors; current paper is cleaner and more sound |
| Optimal Sample Complexity for AMDP (poster) | 6.5 | R1 | Tighter, cleaner result; current paper less impactful |
| Pairwise Elimination Bandits (poster) | 5.75 | R2 | Accepted despite moderate novelty; current paper stronger novelty but significant unresolved concern |
| Lasso Bandit (poster) | 6.33 | R2 | Similar "weaker assumptions" contribution; current paper more novel technique but weaker on the λ gap |
| Action-Constrained RL (poster) | 6.5 | R2 | Clean theory + experiments; current paper has less experimental rigor |

**Round 1 bracket:** 3.5–7.5. The paper is clearly above the low-band anchors (~3.0) but below the high-band ones (~8.0).  
**Round 2 narrowing:** Anchors in (4.5, 6.5) suggest the paper sits between the rejected Continuous-time Linear Systems (5.5) and the accepted Pairwise Elimination (5.75). The genuine theoretical novelty (dissipativity for RMAB) pushes it upward, but the unaddressed λ disconnect pulls it down, as this gap raises questions about whether the core theoretical claim applies to the evaluated algorithm.

**Final score: 5.0.** The paper makes a genuine theoretical contribution by introducing dissipativity to RMAB and obtaining clean sub-optimality bounds under weak assumptions. However, the λ disconnect is a significant unresolved issue: the paper claims the proof works with λ = 0 (as used in practice) but provides no justification, and the dissipativity argument structurally depends on λ. This undermines confidence in whether Theorem 4.1 covers the implemented algorithm. The experiments are informative but would benefit from variance reporting and computational cost analysis. With the λ gap resolved, the paper could become a solid contribution in the 6+ range.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>