- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper proposes a Learning to Optimize (L2O) framework that learns the penalty parameter sequence for the Majorized Proximal Augmented Lagrangian Method (MPALM), a provably convergent multi-block ADMM-type method. The approach unrolls MPALM for a fixed number of iterations, treats the penalty parameter σ as a learnable scalar (updated at intervals of K₀ iterations), and minimizes a supervised loss via backpropagation through the unrolled computation graph. The framework is instantiated on Lasso (via its dual) and discrete optimal transport problems, showing improved convergence over fixed-parameter MPALM and comparisons against LISTA and Sinkhorn's algorithm.

## Strengths

1. **Principled integration of L2O into a convergent multi-block ADMM framework**: The paper correctly identifies that standard multi-block ADMM lacks convergence guarantees, and MPALM's symmetric Gauss-Seidel structure provides a theoretically sound base. The SGS-operator construction (Theorem 4.1) allows the ALM subproblem to be solved exactly via block updates, which is what makes end-to-end backpropagation feasible. This connection is non-obvious and is a genuine enabler.

2. **Computationally efficient learning objective**: The ERM problem involves only J = ⌊K/K₀⌋ + 1 scalar parameters (the σⱼ values), which is an unusually small search space for an L2O method. This means training can be done with standard optimizers (SGD, Adam) without needing bespoke architectures or large models, making the approach lightweight.

3. **Empirical improvement over fixed-parameter MPALM is clearly demonstrated**: Across all tested settings for both Lasso (Figure 1, four problem sizes) and optimal transport (Figure 2, two settings), the learned-σ MPALM consistently achieves lower NMSE than any fixed-σ variant at the same iteration count. This validates the core premise that adaptive penalty parameters improve MPALM's practical convergence.

## Weaknesses

### Fatal
None.

### Major

1. **Experimental evaluation is limited in scope and rigor**: The Lasso problems tested (m ≤ 20, n ≤ 200) are very small compared to typical L2O benchmarks for LISTA (where m=250, n=1000 is common). The paper's own text acknowledges that at larger sizes "K=64 is not sufficient and more iterations are needed" — this suggests the method has not been demonstrated at practically relevant scales. Additionally, no wall-clock time is reported anywhere; since LMPALM requires backpropagation through 64 iterations of block-Gauss-Seidel solves (including linear system solves with (Iₘ+σDDᵀ)), its per-iteration cost may be substantially higher than LISTA or fixed MPALM, making "iterations to convergence" an incomplete comparison. Finally, no variance, error bars, or multiple-seed runs are reported for any experiment — the figures show single traces, making it impossible to assess whether the improvements are statistically reliable.

2. **Comparison against Sinkhorn for OT conflates exact vs. regularized objectives**: The paper compares LMPALM (which solves the exact OT linear program via MPALM) against Sinkhorn's algorithm (which solves entropy-regularized OT). The paper acknowledges this, but then plots NMSE against the exact OT solution. Since Sinkhorn's algorithm is designed for a different (regularized) objective, the comparison is structurally unfavorable to Sinkhorn — it is expected that an exact solver achieves better exact-OT accuracy. A more informative comparison would include other exact OT solvers (e.g., network simplex from POT, or other ADMM-based exact OT solvers). The comparison as presented does not demonstrate that LMPALM is a competitive OT solver; it merely shows that exact solvers beat approximate solvers at exact accuracy.

3. **Reproducibility details are missing**: The paper does not specify training hyperparameters (learning rate, optimizer choice, number of training epochs, initialization of the σⱼ parameters, batch size, train/test splits, number of test samples M, K₀ values used, or random seeds). Without these, the experiments cannot be reproduced or compared against.

4. **Convergence under the learned schedule is not examined**: Theorem 1 (convergence guarantee) applies to Algorithm 1 with a fixed σ. The learned σⱼ sequence used in Algorithm 2 is arbitrary (subject to positivity). The paper does not verify whether the learned parameters satisfy the conditions needed for convergence (Assumption pdQ involves σ), nor does it test whether the algorithm continues to converge if run beyond K=64 iterations. This leaves open the possibility that the learned schedule accelerates initial iterations at the cost of long-term divergence.

### Minor

1. **Novelty is incremental**: The learning mechanism itself — unroll iterations, treat a scalar hyperparameter as learnable, minimize a supervised loss via backprop — is identical to standard algorithm unrolling for two-block ADMM and ISTA. The paper's distinctive contribution is enabling this for MPALM specifically, which is a useful but modest increment. The framing in the Introduction and Related Work ("remains largely unexplored") overstates the gap.

2. **Only two applications, both with exactly solvable subproblems**: The Conclusion acknowledges that all ALM subproblems are solved exactly via elementary linear algebra. This restriction excludes many important multi-block problems where subproblems lack closed-form solutions. The paper does not discuss how to handle inexact subproblem solves, which limits the claimed generality of the framework.

3. **No comparison against simple adaptive heuristics**: The paper compares learned σ against fixed σ but does not compare against any simple heuristic schedule (e.g., increasing σ by a constant factor every K₀ iterations, or using a predefined sequence). Showing that learned σ outperforms such simple baselines would substantially strengthen the case for learning.

4. **K₀ sensitivity not studied**: The choice of K₀ (the period after which σ can change) is a design parameter that could significantly affect both trainability and performance. The paper does not ablate or discuss its selection.

### Trivial
- The NMSE formula on line 302 uses the notation ‖x_i - x^*_i‖₂/‖x^*_i‖₂, but note that this is a per-sample normalized error; the exact definition of M (number of test samples) is not stated.

## Nice-to-Haves
- Add wall-clock timing comparisons to complement iteration-count comparisons.
- Compare against other exact OT solvers (e.g., network simplex in the POT library) as a baseline.
- Provide ablation of K₀ and the number of σⱼ parameters.
- Compare against simple heuristic σ schedules (e.g., geometric increase).
- Verify that the learned schedule preserves convergence (run for 200+ iterations and show no divergence).
- Add error bars and multiple-seed results.

## Removed Points

These points from the inputs were excluded after verification against the paper:

- **"LISTA appears to actually converge faster in later iterations for some settings"** — This claim cannot be verified from the paper text alone; the figures are not provided as data tables. The paper's description states LMPALM "consistently shows faster convergence rate" and that LISTA shows slow early convergence followed by speed-up. Without the actual figure data, I cannot confirm or refute this. Removed as unverifiable from the text.

- **"The paper does not specify how the optimization over {σⱼ} is performed (learning rate, optimizer, number of epochs, initialization)"** — This is factually correct and is kept under **Major** weakness 3 (reproducibility). Moved there.

- **"The paper states 'All MPALM-based algorithms admit linear convergence' but provides no rate analysis or empirical verification beyond visual inspection"** — The paper on line 112 says "we decide not to present the result here for simplicity. However, such a linear convergence is empirically observed based on numerical experience." The paper is upfront about the lack of formal rate analysis. This is a valid observation but is better captured under the general point about limited empirical rigor. Subsumed by Major weakness 1.

- **"The title and abstract suggest a general framework, but only two specific applications are shown"** — Two applications is a reasonable demonstration for a conference paper; this is not a weakness per se. The claim of generality is supported by the formulation (generic multi-block composite convex optimization) and the two applications are diverse (sparse regression and OT). Removed as overreach.

- **"The description of L2O is generic and spends many sentences on basic optimization concepts"** — Style nitpick. Removed per formatting/style rule.

- **Strength Finder claim about "superior empirical performance on Lasso" being a core strength** — This is kept, but tempered by the limited problem sizes and lack of error bars.

- **"The backpropagation through the linear system solve for y₂ in Lasso is not trivial if D is large"** — The paper explicitly notes that the linear system involves (Iₘ+σDDᵀ) which is m×m (line 252). For the tested m=10-20, this is trivial. For larger m, the paper doesn't discuss it, which is a scope limitation but not a specific weakness since the paper doesn't claim to handle large D. Demoted.

- **Various purely speculative convergence concerns** — The harsh critic's point about divergence is speculative since the paper's algorithmic framework preserves the structure that guarantees convergence (σⱼ are positive, SGS-operator construction is the same). The real issue is that the paper doesn't verify or discuss this, which is kept as a Major weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Scale up the Lasso experiments to dimensions at least m=250, n=1000 (standard LISTA benchmarks) and include wall-clock time.
2. Add proper OT baselines: compare against exact OT solvers (network simplex) and at least one other first-order exact method.
3. Report statistics over multiple training runs and test samples (mean ± std over at least 5 seeds).
4. Add an ablation study: compare learned σ against simple heuristic schedules (e.g., σ increasing geometrically with k).
5. Study and report sensitivity to K₀.
6. Provide full training details (learning rate, optimizer, epochs, σ initialization, K₀, train/test split sizes) to ensure reproducibility.
7. Run the learned algorithm for more iterations (e.g., 200+) and verify no divergence.
8. Tone down the novelty claims in the title/abstract — "first L2O for multi-block ADMM" is defensible but the framing should match the modest scope of the experiments.
