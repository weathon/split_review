Now I have all the data I need. Let me write the consolidated review.

## Summary
This paper proposes quantum algorithms for Frank-Wolfe optimization over sparse vector constraints (ℓ₁-ball, simplex, latent group norms) and nuclear-norm matrix constraints. For the vector domain, it achieves query complexity Õ(√d/ε) via quantum maximum finding applied to finite-difference gradient components, and O(1/ε) under Lipschitz continuity via Jordan's gradient algorithm. For the matrix domain, it gives two methods—one using quantum top singular value extraction (QTSVE, Õ(rd/ε²) per iteration) and one using a quantum power method (QPM, Õ(√rd/ε³) per iteration)—both targeting the FW linear subproblem over nuclear-norm balls. The claimed speedups are polynomial improvements in the dimension d over classical FW baselines.

## Strengths
- **Systematic application of quantum primitives to the FW linear subproblem.** The paper correctly identifies that the FW subproblem over ℓ₁ balls reduces to finding the maximum absolute gradient component (solvable by quantum maximum finding with Õ(√d) queries), and over nuclear-norm balls reduces to extracting the top singular vectors of the gradient matrix (solvable by QSVE or quantum power method). This connection is clearly articulated and the error propagation analysis ties approximation errors from the quantum subroutines back to the FW convergence guarantee (Lemma 1 and the analyses in Section 3 & 4).

- **Complete error accounting through the FW iterations.** The paper tracks how errors from finite-difference gradient estimation (vector case) or top-singular-vector approximation (matrix case) propagate, and provides explicit parameter choices (σ_t, δ_t, ε_t) that maintain the O(C_f/ε) iteration count. The use of Hölder's inequality to bound the linear subproblem accuracy under ℓ∞ gradient error is clean and appropriate.

- **Includes both vector and matrix domains with multiple algorithmic variants.** Covering ℓ₁, simplex, latent group norms, and nuclear-norm constraints gives the paper breadth. The two matrix-domain algorithms (QTSVE and QPM) target different gradient matrix structures (high-rank vs. low-rank), and the paper acknowledges tradeoffs between rank dependence and ε dependence.

- **Transparent comparison tables.** Tables 1 and 2 clearly juxtapose classical and quantum complexities side by side, with explicit notation for the gradient evaluation time T_∇, singular values, curvature constants, rank, and other parameters.

## Weaknesses

### Fatal
None.

### Major
- **The claimed speedup in the matrix case depends on favorable parameter regimes that are not fully characterized.** The abstract claims "reducing at least a factor of O(√d) over the best classical algorithm" for the matrix domain. However, comparing the QTSVE complexity Õ(σ₁²d/(σ₁−σ₂)ε²) against the Lanczos baseline O(√σ₁ d²/√(σ₁−σ₂)ε) (Table 2) shows the ratio is O(d ε √(σ₁−σ₂)/σ₁^{1.5}) — which has worse ε-dependence and depends on singular value gaps. The speedup is not uniformly O(√d); it degrades with small ε and small spectral gaps. The paper should provide explicit phase diagrams or characterize the regimes (ε, gap, rank, d) where a genuine speedup materializes, rather than making blanket claims. Similarly, the QPM complexity in Theorem 4 contains the parameter γ′_min (the lower bound of ‖(M_t^T M_t)^i b‖ for all i), which depends on the random initialization of the power method and is not guaranteed a priori. The paper does not discuss how to estimate or ensure this parameter.

- **The quantum data structure loading cost for the matrix case is not accounted for in the comparison.** The paper states it follows the classical convention of excluding gradient evaluation time (T_∇), and Table 2 includes T_∇ for both classical and quantum entries. However, the quantum algorithms under Assumption 4 require the gradient matrix M to be stored in a specific quantum-accessible data structure (from Kerenidis & Prakash 2020b). Building this data structure for a freshly computed gradient at each iteration incurs an additional classical preprocessing cost of O(d² log d) — a cost that has no classical analogue (classical methods simply compute and directly use the gradient). While this assumption is standard in the quantum algorithms literature, the paper's presentation of the speedup as a direct comparison of "complexity of update computing" (Table 2) without flagging this added overhead is misleading. At minimum, the paper should explicitly discuss whether and how this data structure cost is amortized or shared across iterations.

### Minor
- **The vector-domain speedup is demonstrated in a function-value-oracle model that differs from the classical baseline's gradient-oracle model.** Classical FW algorithms assume access to the gradient ∇f(x_t) (cost T_∇). The quantum algorithms (Theorems 1, 2) use a weaker function-value oracle (Assumption 3) to estimate gradients via finite differences. The query complexity comparison in Table 1 (classical O(d) vs. quantum O(√d)) pits a gradient-scan cost against a function-value-query cost, which are different resources. The paper should clarify this asymmetry more prominently rather than presenting the query numbers as directly comparable.

- **The origin of the rank r in Theorem 3's complexity is not clearly derived.** The QTSVE complexity in Lemma 7 depends on p = σ₁²/∑σ_i², not on r. Theorem 3's complexity Õ(rd/ε²) implicitly assumes a particular relationship between r and the singular value distribution (e.g., roughly equal singular values giving p ≈ r/d). This substitution and its justification should be made explicit rather than opaque.

- **No experimental validation, even on small simulated instances.** While the paper is primarily theoretical, numerical experiments (e.g., simulating the quantum subroutines on small matrices using classical computers) would substantially strengthen confidence that the error accumulation across FW iterations does not cause instability. This is standard for quantum algorithms papers at top venues.

### Trivial
- The abstract states "reducing at least a factor of O(√d)" — the "at least" is ambiguous since the speedup can be smaller or larger depending on parameters; "up to" or a more precise characterization would be clearer.
- The claim that results "can be applied to non-square matrices" (Remark 1) is mentioned but the complexity expressions are all in terms of d×d matrices; a note on how complexities change for m×n matrices would improve completeness.

## Nice-to-Haves
- A phase diagram or regime analysis showing (ε, gap, r, d) regions where the quantum matrix algorithms actually beat classical Lanczos/power methods.
- Discussion of whether the quantum data structure for the gradient can be incrementally updated across FW iterations rather than rebuilt from scratch each time, which could amortize the preprocessing cost.

## Removed Points
These points are flagged to be removed; treat them with caution:
- *"The paper never accounts for [gradient] preprocessing cost"* — Factually wrong; T_∇ is explicitly included for both quantum and classical entries in Table 2.
- *"Table 1 hides gate/qubit costs for Theorem 5"* — Factually wrong; the table has separate columns for Qubits and Gates, showing O(d log d) for both.
- *"The classical Lanczos method is [complexity]. The quantum speedup factor claimed is [ratio] — this can be less than 1"* — Partially inaccurate; the speedup factor expression given by the critic does not match the paper's stated factor of O(dε/rσ₁²(M)), and the quantum complexity has better d-dependence (d vs d²).
- *"The paper's technical core is a straightforward composition... The novelty lies entirely in recognizing that the FW subproblem reduces to finding the maximum absolute gradient component"* — Opinion presented as fact; the error propagation analysis and parameter selection for maintaining FW convergence across iterations with inexact quantum subroutines is non-trivial.
- *"Missing numerical experiments"* in the critic's framing as a fatal flaw — Noted above as a minor weakness (not fatal).

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective that the authors themselves have not already expressed.

## Suggestions
1. Explicitly state the oracle asymmetry (function-value vs. gradient) in the vector-domain comparison and explain why query complexity to different oracles is a meaningful comparison.
2. For the matrix case, provide a parameter regime analysis showing where genuine speedup occurs. Include the quantum data structure construction cost in the comparison, or justify why it can be amortized.
3. Clarify the derivation of r in Theorem 3's complexity — explain the relationship between rank r and the factor p used in Lemma 7.
4. Add small-scale numerical simulations (e.g., for d=4–8 matrices) demonstrating that the quantum subroutines work as claimed and error accumulation is controlled.
5. Discuss how γ′_min in Theorem 4 can be bounded or estimated in practice, acknowledge its dependence on random initialization, and state whether the algorithm's complexity is expected or worst-case with respect to this quantity.
6. Soften the blanket "at least O(√d)" claim to reflect the parameter-dependent nature of the speedup.

## Score and Decision

**Calibration anchors** (all from /home/wg25r/review_agent/human_reviews_2026/):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| XBz6cMlv8Z (quantum optimization framework) | 2.00 | Much weaker — pseudo-scientific claims with no rigorous technical content. Current paper is far more rigorous. |
| NMV0XdGnaP (quantum variance reduction for sampling) | 3.50 | Weaker — had fundamental issues with the algorithm design. Current paper's theory is more complete. |
| 4irIRIxhs2 (quantum speedups for sampling/optimization) | 5.00 | Comparable — both rely on oracle models with realism concerns, both have solid analysis but limited practical applicability. |
| 8slDXCAVXS (quantum sensitivity sampling) | 5.00 | Comparable — similar quality of applying quantum primitives to classical problems with thorough analysis. |
| 0CZAimzcVr (DR-submodular maximization, quantum) | 6.00 | Slightly stronger — includes numerical experiments and tackles a broader setting (biased gradients). |
| HBmZlcD8Ue (Beyond Short Steps in Frank-Wolfe) | 6.00 | Stronger — has numerical experiments on realistic problems and the contributions are purely algorithmic, not relying on oracle-model assumptions. |
| 248ysaRatx (quantum neural network universality) | 8.00 | Much stronger — deeper theoretical contribution with broader implications. |

The paper makes a legitimate theoretical contribution by systematically connecting quantum search/SVD primitives to the FW linear subproblem. The vector-domain results are solid but the speedup applies only in the function-value-oracle model, which is not how gradients are typically computed in ML. The matrix-domain results have genuine issues with parameter-dependent speedup claims and unaccounted data structure costs. Overall the paper is a competent technical work but falls short of the bar for a top venue due to overstated claims, opaque parameter regimes, and the absence of any experimental validation.

**Score: 5.0**

**Decision: Reject**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>