## Summary

The paper proposes an adaptive correction mechanism to enforce conservation laws (mass/momentum and norm/energy) in neural operator outputs. The method introduces a lightweight learnable correction operator that modifies the base model's output to exactly satisfy the target conservation law. For linear conservation laws, the correction takes the form \( \mathbf{U}_{\text{new}} = \mathbf{U} + (m_0 - \sum U_i)\mathbf{A} \) with a learnable vector \(\mathbf{A}\); for quadratic laws, a rescaling plus shift with a learnable component is used. A theoretical result shows that this method can achieve lower reconstruction loss than directly constrained neural operators. Experiments on three architectures (UNet, GTNO, FNO) and six PDEs demonstrate exact conservation and improved accuracy compared to original models, loss-based penalties, and projection methods.

## Strengths

- **Architecture-agnostic and lightweight** – The correction operator adds only a single learnable vector (or a small network to generate it) and can be attached to any neural operator without modifying its core architecture.
- **Exact conservation with improved accuracy** – The method drives conservation error to machine precision while also reducing prediction error across all tested PDEs and architectures (Table 1, Table 2). This is a clear advance over loss-based methods that require careful tuning and cannot guarantee conservation.
- **Consistent and thorough empirical evaluation** – Comparisons span three leading neural operator families (UNet, GTNO, FNO), six PDEs with linear and quadratic conservation laws, and two baseline enforcement methods. An ablation study (Table 5) confirms that gains are not merely from added parameters.
- **Demonstrated long-term stability** – Figure 2 shows that the correction prevents error accumulation over ten rollout steps for the nonlinear Schrödinger equation, a practically important benefit.

## Weaknesses

### Fatal
None.

### Major
- **Quadratic correction relies on a restrictive assumption** – The derivation forces \(\lambda_1^2 S_{U^2} = c_0\) to obtain a closed-form solution. The authors do not justify why this choice is near-optimal or how much it deviates from the minimal-modification correction. Without analysis, the quadratic correction may distort the output more than necessary, even though empirical results are positive.
- **Theoretical guarantee (Theorem 1) is not fully substantiated** – The proof is relegated to the appendix (removed), and the claim compares against an idealized constrained operator \(\mathcal{N}_F^*\) that enforces conservation exactly with infinite penalty. The practical relevance of this bound to actual training (finite \(\lambda\)) is unclear. Moreover, the definition of \(\mathcal{N}_F^*\) conflates model class limitation with optimization difficulty.
- **Single conservation law at a time** – The paper explicitly acknowledges this limitation, but many physical systems require simultaneous conservation of multiple quantities (e.g., mass and momentum). The framework currently does not address this, which significantly restricts its applicability.

### Minor
- **Comparison with projection method is incomplete** – Implementation details of the projection baseline (e.g., solver type, convergence tolerance, computational cost) are not provided. The severe failure on the conservative Allen–Cahn equation (error increases to 99.7%) suggests a poor implementation rather than an intrinsic limitation of projection methods. A more careful baseline would strengthen the comparison.
- **No quantitative long-term evaluation for most PDEs** – Long-term stability is shown visually only for the Schrödinger equation (Figure 2). Tables report only one-step prediction errors. The paper would benefit from multi-step rollout errors (e.g., RMSE over 10–50 steps) for all benchmarks.
- **Choice of \(\mathbf{A}\) generator is justified only loosely** – Convolutional layers for UNet/GTNO and MLP for FNO are used without ablation or explanation of how this choice affects performance. The impact of the \(\mathbf{A}\) generator architecture on the method’s adaptability is unclear.

### Trivial
- In Table 4, the norm conservation case shows a huge error (90.1%) at \(\lambda = 10^{-3}\), likely a typo or result of unstable training. The paper should clarify whether this is a genuine outcome or an outlier run.

## Nice-to-Haves

- An extension to simultaneously enforce multiple conservation laws (e.g., mass and momentum together).
- A principled method for the quadratic correction (e.g., solving a constrained least-squares problem per sample with the learnable \(\mathbf{A}\) as a soft prior) that relaxes the \(\lambda_1^2 S_{U^2} = c_0\) assumption.
- Computational cost comparison (wall-clock time or FLOPs) between the proposed method, projection, and loss-based approaches.

## Novel Insights

The paper’s core insight is that a learnable convex combination of local correction operators yields a global correction that exactly satisfies linear conservation laws while remaining fully differentiable and lightweight. This idea bridges traditional hand-crafted post-processing and fully architecture-constrained methods, offering flexibility without sacrificing conservation. For quadratic laws, the rescaling-plus-shift formulation with a learnable vector is also novel, though the justification is less rigorous. The theoretical argument that such learnable corrections can match or outperform fixed hard constraints by avoiding the loss function trade-off in training is conceptually interesting and, if proven rigorously, would provide strong motivation for the approach.

## Suggestions

1. Provide a detailed derivation or justification for the quadratic correction assumption \(\lambda_1^2 S_{U^2} = c_0\) – for example, by showing that it minimizes the perturbation to \(\mathbf{U}\) under the quadratic constraint, or by comparing with a least-squares optimal solution.
2. Add quantitative long-term rollout metrics (e.g., relative L2 error at \(t=10\Delta t\)) for all PDEs in tabular form.
3. Improve the projection baseline by using a standard iterative projection (e.g., fixing the conservation constraint via a linear or quadratic solver) and reporting its convergence properties and cost.
4. Discuss how the method could be extended to multiple simultaneous conservation laws (e.g., by cascading correction operators or using a vector-valued correction).

## Score and Decision

MY FINAL SCORE: 8
MY FINAL DECISION: Accept