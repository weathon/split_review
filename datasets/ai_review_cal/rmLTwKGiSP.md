- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3
Now I have a thorough understanding of the paper and both reviews. Let me produce the final consolidated review.

## Summary

This paper proposes semi-anchored (SA) gradient methods for structured nonconvex-nonconcave minimax problems whose saddle-subdifferential operator satisfies the weak Minty variational inequality (MVI) condition. The core technical contribution is constructing a specific Legendre function \( h(u,v)=\frac{1}{2\tau}(\|u\|^2+\|v\|^2)-\phi(u,v) \) that directly generalizes the linear preconditioner of the classical PDHG method within a Bregman proximal point (BPP) framework. This yields two methods: SA-GDmax (requires an exact max-oracle) and SA-MGDA (uses inner gradient steps for the max-player). The paper proves \( O(1/k) \) convergence in terms of a new Bregman-distance optimality measure, and provides numerical experiments on a toy problem and a fair classification task showing SA-GDmax outperforming CEG+ and GDmax.

## Strengths

1. **Novel nonlinear extension of PDHG to nonconvex-nonconcave problems.** The construction of the Legendre function \( h \) in Equation (5) is clever and principled — it directly nonlinearizes the linear preconditioner that makes PDHG work on bilinear problems. This yields a method that reduces to PDHG on bilinear problems (Section 5.1, citing He & Yuan, 2012) while extending to the nonconvex-nonconcave weak-MVI regime, which PDHG had not been studied in. The connection between PDHG, BPP, and weak MVI is a genuine theoretical contribution.

2. **New optimality measure with \( O(1/k) \) rate under weak MVI.** Theorem 3 proves an \( O(1/k) \) rate for the Bregman distance \( D_h(x_k, x_{k-1}) \), which is shown to upper-bound the squared subgradient norm (the standard measure used by EG+/CEG+). Because the Bregman distance can be smaller, the SA-GDmax rate is at least as good as the squared-gradient-norm rates of extragradient variants. The optimality measure in Equation (6) is new to the minimax literature.

3. **Projection variant extends the range of usable \( \rho \).** Theorem 4 (and Theorem 6 for SA-MGDA) provide convergence for \( \rho < \frac{2}{2L+\hat{L}} \), which is twice the range \( \rho < \frac{1}{2L+\hat{L}} \) of the standard SA-GDmax (analogous to CEG+'s improvement over EG+). This is achieved via a separating-hyperplane projection step described in Section 4.3.

4. **Numerical outperformance on both synthetic and real tasks.** The toy example (Section 7.1, Figure 1) satisfies weak MVI and shows SA-GDmax converging faster than CEG+ and regularized GDmax. The fair classification experiment on Fashion MNIST (Section 7.2, Figure 2, 50 trials) reports higher worst-category test accuracy for SA-GDmax over both baselines across two learning rates.

## Weaknesses

### Fatal
None.

### Major
1. **SA-MGDA is not experimentally evaluated.** The paper frames SA-MGDA as a "first attempt to making the SA gradient method more practical" and devotes significant theoretical analysis to it (Section 6.2, Theorems 5-6), yet every experiment in Section 7 uses only SA-GDmax (the exact max-oracle version). The fair classification problem admits an efficient max-oracle because the max over the simplex is an extreme point — this is a special case. The inexact variant that would be needed for general problems without an efficient max-oracle is entirely untested. This weakens the paper's claim of delivering a practical method: the experiments validate only the least general version, and there is no empirical evidence that inner-gradient iterations (the defining feature of SA-MGDA) converge in practice, or any study of how the number of inner iterations \( J \) affects performance.

### Minor
2. **No direct comparison of total gradient complexity between SA-MGDA and EG+/CEG+.** The paper states that SA-MGDA has \( O(\varepsilon^{-1}\log\varepsilon^{-1}) \) total gradient complexity (Section 6.2) and that EG+/CEG+ have \( O(1/k) \) rates (Section 6.1). However, it does not explicitly compare the total gradient-evaluation complexity: EG+/CEG+ achieve \( O(\varepsilon^{-1}) \) without a log factor (2 gradient evaluations per outer iteration, no inner loop), while SA-MGDA has an extra logarithmic factor from inner iterations. The paper should discuss whether this log factor is benign in practice or creates a meaningful gap, and should report per-iteration gradient costs in experiments.

3. **SA-MGDA implementation details are underspecified for practical use.** Algorithm 1 presents the update in a dense format. The choice of \( \eta = \frac{\tau}{1+2\tau L_{vv}} \) is given, but there is no practical guidance on how to set \( J \) (the number of inner iterations) beyond the asymptotic \( J = O(\log\varepsilon^{-1}) \) bound — no discussion of termination criteria or finite-time heuristics. The paper acknowledges this limitation by stating "We leave making a more practical version...as future work," but this deferral makes the practical contribution of SA-MGDA feel incomplete.

### Trivial
4. Algorithm 1 is very densely formatted and hard to parse. The combination of inline pseudocode and mathematical notation makes it difficult to separate the standard and projection variants.

## Nice-to-Haves
- Test SA-MGDA on the same problems with varying \( J = 1, 3, 5 \) to empirically validate the inexact variant and calibrate inner-iteration cost.
- Provide a direct table comparing total gradient evaluations to reach \( \varepsilon \)-stationarity for SA-GDmax, SA-MGDA, EG+, and CEG+.
- Plot \( D_h(x_k, x_{k-1}) \) alongside \( \|s_k\|^2 \) in experiments to show empirically whether the Bregman-distance measure is indeed tighter.
- Evaluate the projection variant experimentally.
- Discuss limitations more explicitly: SA-GDmax requires an efficient max-oracle; SA-MGDA's inner loop adds complexity; weak MVI restricts the problem class.

## Removed Points

These points were raised by the reviewers but are removed after verification against the paper:

- **"GDmax comparison is unfair"** (Harsh Critic). The paper's Section 7.2 is transparent: GDmax needs explicit regularization to converge (as in Nouiehed et al., 2019), while SA-GDmax does not. The comparison shows SA-GDmax solving the original (harder) problem and outperforming GDmax even with optimally-tuned regularization — this is a strength of SA-GDmax, not an unfair comparison. The same regularization approach is standard in the literature the paper builds on.

- **"Theoretical advantage over extragradient is overstated"** (Harsh Critic). The paper uses carefully hedged language: "can be superior" (Section 1) and "it is possible that we have a gain" (Section 6.1). The upper-bound relationship (Bregman distance ≥ squared gradient norm / 2L_h) is mathematically proven in Theorem 1. The paper does not claim the bound is always tighter — it correctly notes the constant depends on \( D_h(x_*, x_0) \) and that the claim is conditional. This is not overstatement.

- **"Abstract claims experiment on fair classification without noting only exact-oracle version tested"** (Harsh Critic). The abstract says "providing a numerical experiment on fair classification" and the introduction (line 19) explicitly says "where the proposed SA-GDmax outperforms extragradient, given an efficient max-oracle." The paper is transparent about which variant is tested.

- **"SA-MGDA under-specified" framed as near-fatal** (Harsh Critic). The paper provides Algorithm 1, specifies \( \tau \) bounds in Theorem 3, gives \( \eta \) in the algorithm, and provides \( J = O(\log\varepsilon^{-1}) \). The under-specification is a real but minor issue (addressed above as Minor #3). It does not make the method "a theoretical construct" since the algorithm is concretely given and the asymptotic guarantee is provided.

- **Missing related works, formatting nitpicks, speculation about stripped appendix** — all removed per hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add an experiment testing SA-MGDA (with \( J = 1, 3, 5 \)) on at least one problem, ideally both the toy example and a variant of the fair classification where the max-oracle is not trivial. This is the single highest-leverage improvement.
2. Report total gradient evaluations per iteration for each method and include a complexity comparison table.
3. Add a brief limitations paragraph that explicitly states the conditions under which SA-GDmax and SA-MGDA are practical.
