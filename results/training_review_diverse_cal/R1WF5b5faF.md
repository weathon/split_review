I now have all the information needed to produce a thorough, verified review.

---

## Summary

This paper proposes a Learning to Optimize (L2O) framework for the Majorized Proximal Augmented Lagrangian Method (MPALM), a convergent multi-block ADMM-type method for solving linearly constrained composite convex optimization problems. The key idea is to unroll the MPALM iterations and learn its penalty parameters via supervised empirical risk minimization. The method is instantiated on two applications — the Lasso problem (via its dual) and discrete optimal transport — and evaluated against fixed-parameter MPALM, LISTA, and Sinkhorn's algorithm.

## Strengths

- **First L2O framework targeting multi-block ADMM-type methods.** While L2O has been extensively applied to two-block ADMM and ISTA, the paper correctly identifies that "results on combining L2O with multi-block ADMM-type methods, including MPALM, remain limited" (Related work). Extending L2O to MPALM opens a new direction for learning-based acceleration of convergent multi-block algorithms, which are important for large-scale problems with separable structure.

- **Convergence guarantees carried over from the base algorithm.** The learned algorithm inherits the convergence properties of MPALM (Theorem 1). Because the adaptive penalty scheme (Algorithm 2) still satisfies Assumption \ref{pdQ}, the unrolled algorithm retains provable convergence — a meaningful advantage over black-box L2O approaches that sacrifice guarantees.

- **Small-scale hyperparameter learning problem.** The number of learnable parameters is at most \(J = \lfloor K/K_0 \rfloor + 1\), making the ERM a "small-scale optimization problem" solvable by standard optimizers (Section 4). This is a practical design choice that keeps training lightweight.

- **Directly addresses a documented weakness of MPALM.** The paper clearly motivates the work by noting that MPALM's "performance is highly sensitive to the choice of the penalty parameter" and that heuristic adjustment "requires advanced domain knowledge" (Introduction, Section 4). The data-driven approach provides a principled alternative.

## Weaknesses

### Fatal
None.

### Major

- **Experimental evaluation is critically under-specified, making the central empirical claims unverifiable.** The entire results section (Section 5) spans roughly two paragraph-length descriptions and four figure references. The paper does **not** report:
  - Training set size \(N\)
  - Number of penalty segments \(J\) used
  - How penalty parameters were initialized
  - Which optimizer (SGD, Adam, or otherwise) was used to solve the ERM
  - Training hyperparameters (learning rate, number of epochs, batch size)
  - Whether validation was used to avoid overfitting
  - Standard deviations, error bars, or multiple-seed statistics for any result
  - Numerical NMSE values (only plots are provided)
  - Computational cost (training vs. inference runtime)

  Without these details, the reported convergence curves in Figures 1 and 2 cannot be assessed for statistical significance or reproduced. This is a serious deficiency for an empirical paper claiming that LMPALM "outperforms popular alternatives" and "consistently shows faster convergence." The results as presented are suggestive but not conclusive.

### Minor

- **The ERM requires ground-truth optimal solutions \(x^*(\xi)\) without discussing how they are obtained.** For Lasso, \(x^*\) must be computed by some solver, but none is specified or its accuracy reported. For optimal transport, computing the exact optimal coupling requires solving a linear program, which can be computationally expensive. The paper does not acknowledge this cost or discuss whether approximate solutions could serve as training targets. This limits the practical appeal of the approach.

- **The treatment of gradient computation is too brief.** The paper states "Obviously, the backpropagation with respect to \(\{\sigma_j\}\) can be done in a straightforward manner" (line 294) but does not elaborate on how gradients flow through the SGS-operator, the linear system solves, or the projection onto the \(\ell_\infty\) ball. While modern autograd tools can handle these operations, the paper should explicitly note which operations are differentiable and whether any subgradient or smoothing techniques are needed. The conclusion acknowledges that exact subproblem solutions were required for autograd (line 333), but this limitation is not discussed in the main method section where it belongs.

- **The phrase "admit linear convergence" in the results section is imprecise.** The theory section correctly states that linear convergence is only empirically observed and would require an error-bound condition to be proven. However, the results section says "all MPALM-based algorithms admit linear convergence" without qualification, which could mislead readers into thinking this is a proven theoretical property of the learned variant. The paper should either qualify this statement or replace it with "exhibit" / "show empirically."

### Trivial

- The acronym "LMPALM" is used throughout the results section (line 300 onward) but never explicitly defined. It is clear from context (Learned MPALM), but a definition at first use would improve readability.

- The notation \(x^*(\xi)\) for the ground-truth optimal solution and \(x^K(\xi,\{\sigma_j\})\) for the algorithm output could cause confusion since \(x\) is used both as the primal variable (Lasso, OT) and as the dual multiplier (MPALM framework). Clarifying this distinction would help.

## Nice-to-Haves

- **Additional baselines would strengthen the "outperforms popular alternatives" claim.** For Lasso, including FISTA as a standard non-learned baseline would help benchmark against classical solvers. For OT, comparing against a linear programming solver (e.g., network simplex) would demonstrate whether LMPALM achieves near-exact solutions.

- **Comparison against a simple adaptive heuristic.** A natural baseline is MPALM with \(\sigma\) set by a simple schedule (e.g., increasing geometrically) or by cross-validation over a grid. This would isolate the benefit of learning from the benefit of adaptation itself.

- **Ablation on the number of penalty segments \(J\).** Does more flexibility (\(J\) large) always help, or is there overfitting? An ablation would provide practical guidance.

- **Generalization experiment.** Testing the learned parameters on a different distribution (e.g., different SNR for Lasso, different marginal distributions for OT) would directly substantiate the "learning to optimize" claim beyond in-distribution performance.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Algorithm \ref{lasso-pALM} and \ref{ot-pALM} are referenced but not shown."* — These algorithms could be in the appendix (which is stripped by the parser). The mathematical content of the updates is already given in Sections 4.1 and 4.2. Per hard rules, criticisms about missing appendix content are removed.

- *"The related work does not clearly distinguish the L2O contribution from standard hyperparameter optimization."* — The paper does distinguish its approach: it frames it as supervised learning via unrolling (algorithm unrolling / L2O) as opposed to generic hyperparameter tuning. This criticism misreads the paper's positioning.

- *"Missing comparison to FISTA/coordinate descent for Lasso."* — The paper's L2O framing makes LISTA the natural learned baseline. FISTA would be a useful additional baseline but its absence is not a flaw — the paper is not claiming to beat all possible solvers, but to outperform "popular alternatives" in the L2O / MPALM context. (Moved to Nice-to-Haves.)

## Novel Insights

None beyond the paper's own contributions. The reviews surface the experimental under-specification as the main concern but do not add a perspective that the paper's own analysis lacks.

## Suggestions

1. **Substantially expand the experimental section.** Provide: training set size \(N\), number of penalty segments \(J\), initialization strategy, optimizer and hyperparameters used for the ERM, and validation protocol. Report all results as numerical tables with means and standard deviations over multiple random seeds.

2. **Include a comparison against MPALM with a simple adaptive/heuristic schedule for \(\sigma\).** This is the most direct ablation to isolate the benefit of learning.

3. **Add a discussion of how ground-truth solutions \(x^*(\xi)\) are obtained for training.** For OT in particular, address the computational cost of generating these solutions and whether cheaper approximations could be used.

4. **Clarify the gradient computation.** State whether the subgradient through the \(\ell_\infty\) projection (Lasso dual) or through the positive orthant projection (OT dual) is handled by autograd's automatic differentiation or whether a custom implementation is needed.

5. **Add a computational complexity analysis.** Report per-iteration cost, total wall-clock time, and training time to allow practitioners to assess the practical trade-off.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>