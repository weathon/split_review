Now I have enough evidence. Let me compose the final consolidated review.

## Summary

The paper proposes OBCD, a block coordinate descent method for nonsmooth composite optimization with orthogonality constraints (Stiefel manifold). The algorithm updates k rows per iteration via a constraint-preserving transformation, solving small subproblems on St(k,k). The theoretical contributions include: (i) the notion of block-k stationary points (BS_k-points) that are stronger than standard critical points, with a hierarchy relating them; (ii) ergodic O(1/ε) convergence to ε-BS_k-points; (iii) non-ergodic convergence rates under the KL inequality; and (iv) an exact breakpoint-searching subproblem solver for k=2. Experiments on ℓ0-norm sparse PCA are reported.

## Strengths

- **Novel BCD algorithm design with constraint preservation (Sections 2, Lemma 2.1).** The row-wise update scheme X^{t+1} = X^t + U_B(V - I_k)U_B^⊤ X^t exactly preserves orthogonality for any V ∈ St(k,k). This is a clean extension over prior column-wise BCD methods (Shalit & Chechik, 2014; Massart & Abrol, 2022) that were limited to smooth objectives with k=2 and r=n.

- **BS_k-point optimality hierarchy (Theorem 3.6).** The paper establishes that critical points ⊇ BS_2-points ⊇ global minima, with BS_{k+1} ⊆ BS_k. This is a genuinely novel structural result — it characterizes a family of increasingly stringent stationarity conditions that interpolate between standard critical points and global optimality. Remark 3.7 correctly identifies that BS_2-points are strictly stronger than critical points.

- **Non-ergodic convergence rates under KL (Theorems 4.10-4.11).** Establishing finite, linear, or sublinear last-iterate convergence depending on the KL exponent σ is a nontrivial extension of the KL machinery to the BCD-on-manifold setting. The sufficient decrease condition (Theorem 4.2(a)) and the Riemannian subgradient bound (Lemma 4.4) together provide the building blocks for this result, which goes beyond what most BCD papers on manifolds provide.

- **Exact subproblem solver for k=2 (Section 5, Lemma 5.1).** The Breakpoint Searching Method (BSM) reduces the 2×2 subproblem to a one-dimensional search over at most 2r+4 breakpoints, yielding the global optimum even with ℓ0-norm regularization. This is a practical algorithmic contribution — it avoids approximate subproblem solves for the most common k=2 setting.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-algorithm gap for BS_k-point guarantees with general k and h.** Definition 3.5 and Theorem 4.2 assume that I_k is a **global** minimizer of the subproblem K(V;·,·) for every block. However, as Algorithm 1 (Step S3) and Remark 2.4(b) acknowledge, for general k > 2 and general h(·) the subproblem may only be solved locally, yielding a solution that improves over I_k but is not necessarily global. The paper states that "strong optimality may be compromised" (Remark 2.4) but Theorem 4.2 — the advertised O(1/ε) convergence to ε-BS_k-points — applies only to the global-solution case. Theorem 4.6 provides convergence to ε-critical points under local solutions, which partially mitigates this gap. Nevertheless, the paper's central optimality claim ("stronger than standard critical points") is only provably valid for the practical algorithm when k=2 (where the exact BSM solver is available). For k>2 or general h, the practical algorithm's guarantees reduce to critical-point convergence, which is what standard methods already provide. This disconnect between the advertised theory and the implementable algorithm is a significant limitation that should be either resolved or transparently scoped.

2. **Insufficient experimental baselines and evaluation.** The experiments compare OBCD only against LADMM (2014) and SPM (2012) — two operator-splitting methods. The paper's own related work section (lines 44-45) cites Riemannian proximal gradient methods (Chen et al., 2020; Li et al., 2024) and BMM methods on manifolds (Li et al., 2023; Gutman & Ho-Nguyen, 2023; Cheung et al., 2024) as relevant approaches. None of these are compared against. Without comparisons to methods specifically designed for nonsmooth orthogonality-constrained optimization from the last five years, the claim that OBCD achieves "superior performance" is unsupported. The empirical evidence is further limited by: (a) only one problem class (ℓ0 SPCA) presented in the main paper, with additional applications deferred to the appendix; (b) no ablation studies for the choice of k, α, or the two Q-selection strategies (8 vs. 9); and (c) no analysis of how the greedy working-set strategies affect convergence.

### Minor

3. **Theory-experiment link not validated.** The paper argues that OBCD's better empirical performance stems from finding "stronger stationary points" (BS_k-points) than critical points. However, no experiment verifies this claim — e.g., by checking whether OBCD's solutions satisfy the BS_k condition or whether baseline solutions are merely critical points. The claim remains a plausible interpretation rather than a demonstrated fact.

4. **ℓ0 handling with threshold 10⁻⁶.** The paper replaces the ℓ0 norm with a count of entries above 10⁻⁶ for numerical stability. This approximation is not equivalent to the ℓ0 problem analyzed theoretically; a brief comment on how this affects the theory (subdifferential computation, stationarity conditions) would be helpful.

5. **Missing complexity analysis for the BSM subproblem solver.** Section 5 derives the quartic equation for breakpoints but does not analyze the solver's computational complexity or compare it against alternatives (e.g., grid search, generic optimizer for 2×2 problems).

### Trivial
None.

## Nice-to-Haves

- **Ablation studies for k, α, and Q-selection strategies.** Showing how these choices affect per-iteration cost, overall convergence speed, and solution quality would help users apply the method.
- **Variance estimates or multiple runs.** For stochastic working-set selection, reporting variability over random seeds would strengthen the empirical claims.
- **Discussion of limitations.** The paper could explicitly discuss: (a) the restriction to coordinate-wise separable h (excluding e.g., ℓ2 or trace norm); (b) the fact that BS_k is strongest when k is large but subproblems are hardest; (c) the requirement for an initial feasible point.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"tilde{c} is reused with different definitions" (Harsh Critic).** The definition in Theorems 4.2 (line 214) and 4.6 (line 234) is identical: \tilde{c} = (2/α)·(F(X^0)-F(\tilde{X})). There is also a local constant called \tilde{c} in the majorization bound (line 111, 113), but these are clearly different contexts — standard benign notation reuse. Factually incorrect criticism; removed.
- **"Q ⪯ Q appears to be a tautology" (Harsh Critic).** The text on line 103 is a formatting artifact. The intended meaning is Q ⪯ Q + αI (as the subsequent line makes clear). Parser artifact, not an author error. Removed.
- **"Relative objective values F - F_min are misleading" (Harsh Critic).** This is standard practice in optimization comparisons. F_min is reported explicitly (Table 1, column 2), allowing readers to reconstruct absolute values. Removed.
- **"Missing running times for individual components" (Harsh Critic).** A nice-to-have, not a core weakness. Demoted to Nice-to-Haves.
- **"No variance/uncertainty estimates" (Harsh Critic).** Single-run evaluation on deterministic optimization benchmarks is the norm in this subfield. Removed.

## Novel Insights

The harsh critic raises a genuinely insightful point about the theory-algorithm gap that the strength finder completely misses: the BS_k-point theory promises stronger optimality than critical points, but this promise is only backed by the exact subproblem solver for k=2. For k>2 and general h, the practical algorithm only guarantees critical-point convergence (Theorem 4.6), which is what standard methods already achieve. Neither reviewer integrates this with the experimental claims — the experiments use only k=2 (the case where the theory is tight), so the practical relevance of the gap is smaller than the harsh critic suggests. However, the paper does not make this connection explicit; it mentions k=2 as the subproblem solver setting but does not clearly state that the BS_k-point guarantees are proven only when global subproblem solutions are available.

## Suggestions

1. **Scope the theory claims transparently.** Either (a) provide convergence guarantees for local subproblem solutions to BS_k-points (even a relaxed notion), or (b) explicitly scope the BS_k-point optimality claims to the k=2 case and the exact-solver setting, and reframe the general case as converging to critical points (which Theorem 4.6 already establishes).

2. **Add modern baselines.** Compare OBCD against at least Riemannian proximal gradient (Chen et al., 2020) or a recent BMM method (Li et al., 2024; Cheung et al., 2024) on at least one problem class. Without this, the empirical contribution is not competitive with the current state of the art.

3. **Validate the optimality claim experimentally.** On a small problem where the gap between critical points and BS_2-points can be characterized, demonstrate that OBCD reaches a BS_2-point while baselines get stuck at a non-BS_2 critical point. This would directly connect theory to experiments.

4. **Add ablations for k, α, and Q-selection strategy (8 vs. 9).** These are natural design choices that readers need guidance on.

Based on calibration against human-reviewed anchors: this paper has genuinely novel theory (comparable to accepted poster papers in the 5-6 range) but experimental validation that is substantially weaker than those anchors. The theory-algorithm gap is a real concern that needs addressing but is not fatal (for k=2 the theory is fully operational). The insufficient baselines are the binding constraint.

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/6w9qffvXkq.md | 2.60 | R1-weak | Much weaker — poorly motivated application, no convergence theory |
| /home/wg25r/review_agent/human_reviews/F5UgXkPgSn.md | 3.00 | R1-weak | Much weaker — local convergence only, narrower scope |
| /home/wg25r/review_agent/human_reviews/xVw8YNEtH3.md | 3.00 | R1-weak | Much weaker — heuristic method, weak theory |
| /home/wg25r/review_agent/human_reviews/e0bdvNsgcF.md | 2.50 | R1-weak | Much weaker — different problem, simpler analysis |
| /home/wg25r/review_agent/human_reviews/5mtwoRNzjm.md | 6.50 | R1-middle | Stronger experiments but less novel theory; paper under review has stronger theory but weaker experiments — comparable overall |
| /home/wg25r/review_agent/human_reviews/c2OtbtZXFC.md | 4.75 | R1-middle | Weaker — limited novelty (incremental over Ablin & Peyré), unclear contribution |
| /home/wg25r/review_agent/human_reviews/n2RIkaf1S4.md | 4.00 | R1-middle | Weaker — BCD for neural networks with different analysis framework |
| /home/wg25r/review_agent/human_reviews/ntxoThl1Zp.md | 3.67 | R1-middle | Weaker — Grassmannian averaging, simpler problem |
| /home/wg25r/review_agent/human_reviews/xGvPKAiOhq.md | 8.00 | R1-strong | Stronger — impactful lower bound results, extensive experiments |
| /home/wg25r/review_agent/human_reviews/P1aobHnjjj.md | 7.75 | R1-strong | Stronger — deep theoretical analysis with strong experiments |
| /home/wg25r/review_agent/human_reviews/MHjigVnI04.md | 7.67 | R1-strong | Stronger — rigorous dynamical analysis, strong experiments |
| /home/wg25r/review_agent/human_reviews/jj5ZjZsWJe.md | 8.00 | R1-strong | Stronger — different subarea (federated learning), strong theory+experiments |
| /home/wg25r/review_agent/human_reviews/ROYSNn3vvB.md | 5.00 | R2-narrow | Comparable — both have mixed reviews, similar theoretical depth |
| /home/wg25r/review_agent/human_reviews/6YZmkpivVH.md | 5.50 | R2-narrow | Comparable — similar level of theory, also rejected |
| /home/wg25r/review_agent/human_reviews/RNGUbTYSjk.md | 6.00 | R2-narrow | Comparable — accepted poster with clean theory |
| /home/wg25r/review_agent/human_reviews/ogKE7LcvW6.md | 7.00 | R2-narrow | Stronger — accepted poster with well-developed stationary point theory |
| /home/wg25r/review_agent/human_reviews/JyQYYjtO88.md | 6.67 | R2-narrow | Stronger — clear theoretical contribution, accepted |
| /home/wg25r/review_agent/human_reviews/YwJkv2YqBq.md | 6.75 | R2-narrow | Stronger — accepted spotlight, clean theoretical analysis |
| /home/wg25r/review_agent/human_reviews/DcZpQhVpp9.md | 6.67 | R2-narrow | Stronger — accepted poster, strong theory with experiments |

**Round 1 bracket:** 4–7 (paper is clearly above weak anchors at ~3 and clearly below strong anchors at ~8).  
**Round 2 narrowing:** Compared against anchors at 5.00–6.67, the paper has genuine theoretical novelty (BS_k hierarchy, KL rates) that places it above the 4.75 and 5.00 anchors, but the experimental evaluation is weaker than all accepted papers in this range. The narrowness of the baselines is the binding constraint. The paper sits closest to the 5.5 anchor (TpopT, Reject with mixed scores) and is marginally weaker than the accepted-poster benchmarks at 6.00.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>