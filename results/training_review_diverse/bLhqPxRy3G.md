Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper studies gradient descent on diagonal linear networks (quadratic reparametrization x = u∘u) for solving linear programs of the form min cᵀx s.t. Ax=b, x≥0. The core contributions are: (1) a rigorous discrete-time convergence analysis showing global linear convergence under mild assumptions, (2) characterization of the limit point as an entropy-regularized LP solution whose regularization strength is controlled by the initialization, and (3) connections to mirror descent and the Sinkhorn algorithm. The analysis goes beyond prior gradient-flow analyses by handling finite step sizes without infinitesimal limits.

## Strengths

- **Global linear convergence for discrete-time GD (Theorem 3):** The paper proves that f(uᵏ) ≤ (1-ρ)ᵏ f(u⁰) under strictly feasible LPs and properly chosen step sizes. This is a non-trivial guarantee for a non-convex problem and goes well beyond existing gradient-flow characterizations.

- **Characterization of the limit as an entropy-regularized LP (Theorems 1 and 4):** The gradient-flow limit solves an entropy-regularized LP with regularization controlled by initialization (Theorem 1). Theorem 4 extends this to the discrete-time setting, showing the limit solves the regularized problem plus an error term proportional to the step size η. This directly links the implicit bias of DLNs to a broad class of regularized LPs.

- **Rigorous analysis without infinitesimal-stepsize assumptions:** The paper provides a self-contained convergence theory for discrete GD, including per-iteration decrease guarantees (Lemma 1) with explicit step-size conditions, boundedness of iterates (Lemma 2), and a Lojasiewicz-type gradient inequality (Lemma 9). This fills a genuine gap in the literature where only gradient flow analyses were available.

- **Experimental confirmation of initialization effects:** Figure 2 shows that smaller initialization α yields smaller relative gap to the true LP solution (left panel) while slowing convergence (right panel), directly supporting the theoretical predictions of Theorems 1 and 4.

- **Connections to mirror descent and Sinkhorn:** Sections 3.2 and 3.3 explicitly derive relationships between reparametrized GD and existing algorithms, clarifying where they coincide (infinitesimal steps) and diverge (finite steps).

## Weaknesses

### Fatal

None.

### Major

- **Experiments do not match the paper's claimed scope.** The abstract and introduction claim the framework solves "linear programming problems" including optimal transport, and claim a "comparative analysis...supported by simulations" with the Sinkhorn algorithm (line 45). Yet all experiments only test the special case c = 1ₙ (basis pursuit / minimum ℓ₁-norm feasibility). No experiment uses a non-trivial cost vector, no optimal transport problem is solved, no comparison with the Sinkhorn algorithm is performed, and the theoretical limit characterization (Theorem 4) is not directly verified (e.g., by comparing the obtained solution to the entropy-regularized LP for a known λ). The experimental evidence supports only the basis-pursuit subcase, not the full "comprehensive framework for solving linear programming problems" claimed in the abstract. This is the paper's most significant weakness: the theory is broader than what is validated.

- **Strict feasibility assumption (Assumption 2) limits practical generality.** The entire convergence analysis (Lemmas 3, 4, Theorems 3, 4) depends on the existence of a strictly interior feasible point x>0 with Ax=b. The paper acknowledges this assumption but asserts it is "mild" and "satisfied for most LP problems in practice" (line 318) without elaboration or discussion of mitigation strategies. For LPs that are feasible only on the boundary (e.g., when all feasible solutions have some zero coordinates), the results do not apply. Since the paper claims to be "a comprehensive framework," this gap in generality warrants explicit discussion of limitations or potential workarounds (e.g., constraint perturbation).

### Minor

- **The discrete-time limit characterization (Theorem 4) is qualitative, not fully explicit.** The extra error term in the limit involves a vector w that depends on the entire trajectory (def-w) and is not expressed purely in terms of problem data. While the paper bounds ‖w‖₁ by a constant C, the result is weaker than the clean gradient-flow characterization (Theorem 1). The paper could strengthen this by showing w→0 as η→0 (which it does) or providing a more interpretable bound.

- **The Lojasiewicz constant τ = 8·9^{-(n-1)} is astronomically small for moderate n** (e.g., n=3000 in experiments). This means the theoretical local sublinear rate (Theorem 5) is essentially flat in the worst case, and the linear rate constant ρ depends on a lower bound σ of uᵏ that could be exponentially small. While this is a standard issue with Lojasiewicz-based analyses (constants are typically very loose), the paper should acknowledge that the theoretical rates are far more pessimistic than the empirical convergence, and that observed fast convergence likely arises from favorable problem structure not captured by these constants.

- **No error bars or variation across random instances in experiments.** The experiments use a single configuration (m=300, n=3000) with one random draw. While acceptable for a theory-focused paper, adding multiple trials or additional problem dimensions would strengthen the empirical claims.

- **The claim that the paper "uniquely enables us to elucidate the influence of gradient descent initialization" (line 42) is overstated.** Prior work (Woodworth et al. 2020) already demonstrated initialization-dependent convergence for the basis pursuit case. The paper's unique contribution is the discrete-time analysis, not the observation of initialization effects per se.

- **No discussion of computational complexity or comparison to standard LP solvers.** Each GD iteration costs O(mn), but the paper does not discuss how this compares to modern LP solvers (e.g., PDLP, simplex, interior-point methods), nor does it provide wall-clock time comparisons. This makes it difficult to assess the method's practical value.

### Trivial

- The stepsize rule (stepsize-condition-1) requires computing ‖Aᵀrᵏ‖∞ and ‖uᵏ‖∞ at each iteration. The paper does not discuss an adaptive/backtracking procedure or report how often the condition is checked in experiments.

## Nice-to-Haves

- **Direct validation of Theorem 4:** An experiment that varies λ via initialization (αᵢ = exp(-cᵢ/(2λ))) and checks whether the limit matches the entropy-regularized LP solution for that λ would directly confirm the central theoretical prediction.
- **An optimal transport example** (even small) would substantiate the claimed versatility.
- **A discussion of how strict feasibility might be circumvented** (e.g., constraint perturbation, barrier methods) would increase practical relevance.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. *"The paper uses the ground truth x̄ (which is feasible but not necessarily the minimum ℓ₁-norm solution) to compute the relative gap"* — Factually incorrect. The paper clearly defines x* as "an optimal solution of (1) with c = 1ₙ" (line 431), separate from x̄ which is used only to generate b. The paper does not conflate the two.
2. *"No experiments on optimal transport"* — Kept as a Major weakness above (experiments don't match scope). The specific OT complaint is subsumed by the broader scope-mismatch criticism.
3. *"The experiments do not verify the theoretical limit characterization"* — Kept as a Minor weakness (within the broader experimental scope criticism).
4. *"Only one random seed"* — Kept as a Minor weakness above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Temper the scope claims** to match what is experimentally validated, or add experiments on general cost vectors (e.g., non-trivial c > 0 and a small optimal transport example) to support the claimed breadth.
2. **Add a limitations paragraph** discussing the strict feasibility assumption, the pessimistic theoretical constants, and when the method might be practically useful compared to standard LP solvers.
3. **Directly validate Theorem 4** by comparing the obtained solution to the entropy-regularized LP for a known λ.
4. **Acknowledge the looseness of the theoretical constants** and note that the fast empirical convergence may be due to favorable problem structure.

## Score and Decision

This paper makes genuine and non-trivial theoretical contributions — the discrete-time convergence analysis of reparametrized GD for LPs fills a real gap in the literature. The mathematical work is substantial and the proof techniques are clever. However, the paper overclaims its experimental scope, and the strict feasibility assumption is a structural limitation. The theoretical results are sound within their stated assumptions; the core issue is that the paper claims to be a "comprehensive framework for solving linear programming problems" but only validates it on a single special case. This gap is significant but not fatal to the theoretical contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>