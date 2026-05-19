Now I have all the information I need. Let me synthesize the final review, cross-verifying each claim.

---

## Summary

This paper proposes a convex, equivalent reformulation of variational image reconstruction problems where the regularizer is an input-convex neural network (ICNN). The key idea is to eliminate the nested structure of the ICNN by introducing auxiliary variables for layer-wise activations and replacing equality constraints with epigraphical inequality constraints, which preserves convexity. The resulting problem is then solved via the Primal-Dual Hybrid Gradient (PDHG) algorithm. Experiments on denoising, inpainting, and sparse-view CT reconstruction show faster and more stable convergence than subgradient methods.

## Strengths

- **Theoretically sound convex reformulation with provable equivalence (Theorem 3)**. The paper proves that replacing equality constraints with epigraphical inequality constraints yields a convex problem whose minimizers correspond exactly to those of the original (non-convex) variational problem. Proposition 2 and Theorem 3 are correctly argued under the stated assumptions, and the illustrative 1D example in Section 2 effectively motivates why the epigraph constraint is needed.

- **First application of a primal-dual algorithm to ICNN-regularized variational problems**. The paper derives a specific PDHG instantiation (Section 3.2) with tailored step-size formulas (Equations 10, 13) that respect the convergence condition of Pock & Chambolle (2011). The algorithm handles non-smooth activations (ReLU, leaky ReLU) exactly via epigraphical projections, which is a principled alternative to the subgradient methods used in prior work (Mukherjee et al., 2020).

- **General architecture formulation (EQ-G) extends beyond standard ICNNs**. The reformulation is derived for a general class of convex nested functionals (Eq. EQ-G, Assumption 1) that subsumes residual connections and general convex non-decreasing activations (Proposition 1), widening the applicability beyond the specific ICNN used in the experiments.

- **Empirical evidence of faster convergence across three tasks**. The results consistently show that the proposed method converges in fewer iterations with smoother energy/PSNR trajectories than both constant-step-size and diminishing-step-size subgradient methods (Figures 3, 5, 7). Table 1 reports mean speedups of 28× and 31× over SM-C and SM-D respectively in terms of iterations to convergence.

## Weaknesses

### Fatal
None.

### Major

- **Narrow comparison baseline limits the strength of the experimental claims.** The paper compares only against two subgradient methods (constant step-size and diminishing step-size). While subgradient methods are the default approach in prior ICNN-based reconstruction work (Mukherjee et al., 2020), they are well-known to be among the slowest first-order methods for non-smooth optimization. The paper's headline speedups (28×–31×) are measured against these baselines. To establish the method as genuinely practically useful—rather than simply "better than the worst option"—the experiments should include at least one more competitive baseline that also exploits structure (e.g., ADMM applied to the reformulation, or an accelerated proximal method). Without such a comparison, it is difficult to assess how much of the gain comes from the reformulation itself versus from the fact that any structured optimizer beats the simplest possible baseline.

- **No wall-clock runtime comparison.** The paper reports speedup exclusively in iteration counts (Table 1). Because the proposed method has higher per-iteration cost (multiple operator applications, dual variable updates, projections), iteration gains do not automatically translate to runtime gains. The paper mentions "potential for parallel computation" (Section 3.2, conclusion) but does not demonstrate it. A practical claim of efficiency requires at least a runtime comparison on comparable hardware, even if single-threaded.

### Minor

- **The convergence condition for PDHG is stated but not verified for the chosen step-size hyperparameters.** The paper correctly states the condition $\|\mathbf{S}^{1/2}\mathbf{K}\mathbf{T}^{1/2}\| < 1$ (line 151) and provides step-size formulas parameterized by $c_1,c_2$ (Equations 10, 13). However, it never checks whether the chosen values (e.g., $c_1=0.1, c_2=5\times10^{-5}$ for denoising) actually satisfy the condition. The ablation study (Figure 2) shows that some combinations lead to poor convergence, but this is an indirect remedy. A direct computation or bound on the spectral norm would clarify whether the method operates within its convergence guarantee.

- **Statistical evaluation is incomplete.** Only the inpainting experiment reports mean and standard deviation over multiple test images (20 images, Table 1). The denoising and CT experiments show results for a single image each (Figures 3, 7). Without variance across images, the reader cannot assess whether the observed behavior is typical or selected to favor the method.

### Trivial

- **The stopping criterion is specified only for the inpainting experiment** ("relative objective error below 1e-3", line 215). For denoising and CT, the number of iterations is implicitly fixed (200 and 500–1000), but it is not stated whether the objective had converged at that point. Adding the convergence criterion for all experiments would improve replicability.

- **The derivation of step-size formulas from the convergence condition is not shown.** The reader is left to infer that the formulas in (10) and (13) satisfy $\|\mathbf{S}^{1/2}\mathbf{K}\mathbf{T}^{1/2}\| < 1$ for the given ranges of $c_i$, which is not immediate from the formulas as written.

## Nice-to-Haves

- **Comparison with a line-search subgradient method** (e.g., Polyak step-size) would be more informative than the two fixed heuristics (constant and 1/k diminishing) currently used. The CT experiment (Figure 7) shows that the constant-step-size subgradient makes fast early progress, suggesting that better-tuned subgradient variants might narrow the gap.

- **A simple additional application** demonstrating the claimed generality to non-ICNN convex regularizers (beyond the EQ-G architecture used) would strengthen the scope claim.

- **Discussion of parameter sensitivity**: The ranges for $c_1,c_2$ seem task-dependent (differing by orders of magnitude across denoising, inpainting, and CT), but the paper does not discuss why these choices are appropriate or how to set them in new applications.

## Removed Points

*These points are flagged to be removed. Treat them with caution.*

- **"Code and trained regularizers are not made available"** — REMOVED. Per policy, concerns about availability of cited/code artifacts reflect reviewer knowledge gaps, not author errors.

- **"Step-size condition not verified — some combinations lead to poor objective values, likely because the condition is violated"** — This claim was demoted from Major to Minor. The paper does not compute the spectral norm, but the ablation study (Figure 2) empirically validates the chosen parameters, providing indirect evidence. The core point (lack of formal verification) is retained as Minor.

- **"The paper does not discuss stopping criteria"** — This is partially incorrect: the stopping criterion is stated for the inpainting experiment (relative objective error < 1e-3). The point is retained as Trivial but corrected to note that the criterion is given for inpainting only.

- **"The generalization to other convex regularizers is claimed but not demonstrated"** — REMOVED. This asks the paper to address a direction outside its stated scope. The paper's scope is ICNN regularizers, with the general formulation as supporting theory; demonstrating non-ICNN regularizers is a nice-to-have, not a flaw.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **(Essential)** Add at least one stronger baseline: ADMM applied to the reformulation (3) or an accelerated gradient method on a smooth approximation. This is needed to determine whether the observed gains reflect the reformulation's value or merely the weakness of the subgradient baselines.
2. **(Essential)** Report wall-clock runtime in seconds for all experiments, ideally with and without parallelization, to ground the efficiency claims.
3. **(Recommended)** Verify the PDHG convergence condition $\|\mathbf{S}^{1/2}\mathbf{K}\mathbf{T}^{1/2}\| < 1$ for the chosen $c_i$ values (either analytically or numerically) and report the bound.
4. **(Recommended)** Add multi-image statistics (mean ± std) to the denoising and CT experiments so the reader can assess result variability.
5. **(Minor)** Explicitly state the convergence criterion (or maximum iterations) for all experiments, not just inpainting.

## Score and Decision

**Overall assessment**: The paper makes a theoretically sound and potentially useful contribution: a convex reformulation of ICNN-regularized variational problems that enables the use of efficient primal-dual algorithms. The theoretical development is clean and correctly argued. However, the experimental validation is too narrow to fully substantiate the practical claims. The baselines are the weakest possible, and the evaluation lacks runtime comparisons and statistical rigor for two of three tasks. These gaps do not invalidate the core idea—the theory stands regardless—but they weaken the demonstration of practical significance. With expanded experiments (stronger baselines, runtime data, multi-image statistics), the paper would be a solid contribution. In its current form, the contribution is more conceptual than convincingly demonstrated.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>