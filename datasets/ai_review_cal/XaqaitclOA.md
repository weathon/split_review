- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 5, 6, 6
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper derives theoretical risk bounds for Physics-Informed Neural Networks (PINNs) solving Burgers' PDE near finite-time blow-up. Theorem 1 gives a bound in arbitrary dimensions; Theorem 2 provides a bound for a specific 1+1D blow-up scenario with explicit constants and a stability guarantee. The paper then demonstrates empirically that these bounds are strongly correlated with the true L² error of PINN solutions as the PDE approaches its blow-up time, for both 1D and 2D blow-up examples.

## Strengths

- **Novel generalization bounds for Burgers' PDE accommodating finite-time blow-up**: Theorems 1 and 2 provide the first (to the authors' knowledge) PINN generalization bounds that apply to zero-viscosity Burgers' solutions that can become singular. Prior PINN theory (Siddhartha et al., De et al., Karniadakis et al.) either required viscosity, periodicity, divergencelessness, or linearity —none of which hold for the blow-up setting considered here.

- **Strong empirical correlation between bounds and true L² error as blow-up is approached**: In the 1+1D case (Fig. 3), the correlation between the bound's RHS and the true risk remains near 1 across all tested values of the proximity parameter δ, up to δ=0.998 (extremely close to blow-up at δ=1). In the 2+1D case (Fig. 4), correlation of ≈0.80 is maintained for width-100 networks up to δ≈0.65. These results show that the bounds capture error dynamics near singularities.

- **Stability of the 1+1D bound in the sense of Wang et al. (2022)**: Theorem 2 is proven to be (L₂,L₂,L₂,L₂)-stable (line 170 and footnote), meaning that small PINN residuals guarantee small L₂ error. This property holds in the blow-up setting and is not derivable from prior PINN stability results.

- **Clear demonstration of inapplicability of classical numerical-analysis bounds**: Section 3.1 explains why existing error estimates for Burgers' equation (Corollary 3.5 in Tadmor, Theorem 2.1 in Tadmor) cannot be applied to PINN surrogates—they require properties (conservativeness, specific regularity) that neural nets are not guaranteed to satisfy.

- **Generality to multiple spatial dimensions**: Theorem 1 is proven for arbitrary dimension d, and the paper provides a concrete test case for d=2 with a known O(1/t²) blow-up solution (Sec. 4.3.2), extending validation beyond 1D.

## Weaknesses

### Fatal
None.

### Major

- **Bounds rely on properties of the true solution, limiting practical applicability**: For Theorem 1, the constants C₁ and C₂ involve ‖∇u‖_{L∞(Ω)} and ∫_Ω ‖u‖² — norms of the true solution. For Theorem 2, the constants depend on ‖u_x‖_{L∞} = 1/(1-δ) (line 157) and boundary L∞ norms of the true solution. The paper is transparent about this being an unusual kind of bound (lines 123–125), and for Theorem 2 claims it is "evaluable without exactly knowing the exact true solution" (line 164). However, the needed quantities (gradient supremum, boundary value supremum) are still nontrivial to estimate when the true solution is unknown, and the paper offers no discussion of how they might be obtained in practice (e.g., via asymptotic blow-up scaling, coarse numerical simulation, or physical priors). This significantly constrains the bound's use as a diagnostic tool.

- **No assessment of bound tightness**: The paper reports only correlation between the bound and the true L² error. Since both quantities increase monotonically with δ (closer to blow-up → larger error → larger bound), high correlation could partly reflect shared monotonicity. The paper does not report the ratio (bound value)/(true error), so the reader cannot judge whether the bound is within an order of magnitude or orders of magnitude larger. Without this, the practical informativeness of the bound is unclear. A bound that is 10¹⁰× the true error but correlated would be far less useful than one within 10×.

- **No baselines or comparisons**: The paper does not compare the derived bound against simpler alternatives (e.g., the empirical training loss, a naive Lipschitz bound, or the residual norm directly). Demonstrating that the bound provides insight beyond what a trivial baseline offers is important for establishing its value, especially given the dependence on true-solution quantities.

### Minor

- **Limited experimental scope**: Only two blow-up scenarios are tested (one 1D, one 2D), with a single network depth (6 layers) and two widths per experiment. No variation in architecture, activation function, optimization method, or different blow-up profiles/nonlinearities is explored. The experimental evidence for generality is consequently thin.

- **No analysis of discretization effects on bound evaluation**: The bound is stated in terms of continuous integrals and supremum norms, but its evaluation uses finite collocation points, Monte Carlo integral approximations, and supremum norms estimated over finite grids. The paper does not discuss how these approximations affect the reliability of the computed bound values.

### Trivial
None.

## Nice-to-Haves

- Report the ratio of bound value to true error for each experiment, to clarify tightness.
- Compare the bound against a simple baseline (e.g., training loss magnitude, a naive Lipschitz bound) to demonstrate added value.
- Discuss strategies for estimating the true-solution-dependent constants (e.g., ‖∇u‖_{L∞}) in practice, such as from asymptotic blow-up scaling laws or coarse reference solutions.
- Test on at least one additional blow-up scenario (different PDE or different mechanism) to strengthen generality claims.
- Some figures lack detailed numerical axis labels; adding explicit scales would help readability.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Bound derivation not verifiable (proof in appendix)**: The critic noted the proof is relegated to the appendix. Per the instructions, the parser strips appendices from all papers; this is not a valid criticism of the submission.
- **Axes not labeled with numerical values**: This is a formatting/presentation nitpick. The figures are present as images; labeling concerns are minor and do not affect evaluation.
- **Bound "only applicable before blow-up"**: The paper explicitly states the bounds apply to solutions with continuous first derivatives "as would be true for the situations very close to blow-up as we would consider" (line 119). This is not a weakness — the bound is designed for pre-blow-up regimes, which is the relevant setting.
- **Stability claim is misleading because constants blow up**: The stability definition (footnote, line 170) uses O()-notation, which permits large constants. The paper's claim that Theorem 2 is (L₂,L₂,L₂,L₂)-stable is technically correct. The constant scaling is a separate issue from the existence of stability.
- **"Not truly generalization bounds" framing**: The paper explicitly distinguishes its bounds from usual generalization bounds (lines 123–125) and explains why the PDE context motivates a different structure. This is a framing difference, not a factual error.
- **"Missing comparison to classical blow-up detection methods"**: The paper's scope is generalization bounds for PINNs and their correlation with error — not blow-up detection per se. Blindly adding this comparison without a clear research question is scope creep.

## Novel Insights

The two reviews diverge on the severity of the bound's dependence on true-solution quantities. The harsh critic treats this as a potentially fatal flaw, framing the bound as "circular." However, the reviewed paper is unusually transparent about this limitation (lines 123–125 explicitly acknowledge the bound is "not like usual generalization bounds"). Moreover, the 1+1D bound (Theorem 2) requires only coarse properties of the true solution (gradient supremum and boundary supremum), not the full solution field — a distinction the harsh critic conflates. The strength finder correctly identifies that the stability result for Theorem 2 (line 170) circumvents the true-solution dependence at test time for the 1+1D case, a nuance the harsh critic underplays. The true tension in the paper is less about whether the bounds are "valid" (they are mathematically sound) and more about whether their demonstrated value (correlation with error) is sufficient to justify the overhead of needing estimates of true-solution properties. This is an honest methodological trade-off, not a fatal flaw.

## Suggestions

1. **For the experimental section**: Add a table reporting the (bound value)/(true error) ratio for several δ values and both widths. This single addition would address the most serious gap in the experimental validation.
2. **For the theory**: Add a brief discussion (even 2–3 sentences) on how ‖∇u‖_{L∞} and related true-solution quantities could be estimated in practice — e.g., from asymptotic blow-up scaling, from a coarse finite-volume simulation, or from the PDE structure itself (e.g., the known 1/(1-δ) scaling in the 1D example).
3. **For the experiments**: Include a simple baseline — for instance, plot the training loss alongside the bound and true error — to demonstrate that the bound captures more than what is already observable from the loss.
4. **Clarify the bound's purpose**: The paper would benefit from a sentence explicitly stating what the bound is good *for* given its structure: e.g., as a theoretical tool to prove stability and to derive scaling laws, rather than as a practical error estimator.
