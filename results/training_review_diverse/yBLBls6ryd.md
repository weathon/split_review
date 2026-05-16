Here is my final consolidated review.

---

## Summary

This paper proposes a Riemannian optimization framework to learn spectral factorizations of preconditioning matrices on the fly, enabling cheap application of arbitrary fractional powers without matrix decompositions. The core idea is to directly update the orthogonal matrix **B** and eigenvalues **d** of a curvature estimate **S** = **B** diag(**d**) **B**^T using local coordinate transformations that diagonalize the Fisher-Rao metric. The method is extended to Kronecker-factorized structures (with determinant constraints to resolve redundancy) and uses truncated Cayley/exponential maps for computational efficiency and half-precision stability. Empirical validation includes synthetic curvature tracking, a positive-definite matrix optimization problem, and half-precision training of three vision transformers on ImageWoof.

## Strengths

- **Novel framework for learning spectral factorizations without eigendecompositions.** The paper introduces a principled Riemannian approach to directly adapt the orthogonal matrix **B** and eigenvalues **d** using Cayley and exponential maps. This avoids matrix decompositions entirely, which is a prerequisite for stable low-precision operation. The synthetic validation (Figs. 2–3) confirms that the spectral update scheme closely tracks the iterates and fixed point of the standard exponential-average update under i.i.d. Gaussian gradients.

- **Rigorous Riemannian derivation with closed-form metric diagonalization.** Section 3 derives the update scheme from first principles by constructing local coordinates that diagonalize/block-diagonalize the Fisher-Rao metric. Claims 4 and 5 provide exact closed forms for the metric in full-matrix and Kronecker-factorized cases respectively, making the inverse metric computation trivial and avoiding expensive line searches or iterative inversions. This theoretical contribution is technically sound and clean.

- **Resolution of Kronecker redundancy.** The paper correctly identifies and resolves the non-uniqueness of Kronecker factorization by imposing determinant constraints on each factor and introducing a learnable scalar α (Section 2.2). This removes a degeneracy that would otherwise make the metric singular.

- **Half-precision training across multiple ViT architectures.** The method is demonstrated on three vision transformers (ViT, FocalNet, FlattenViT) in half-precision on ImageWoof, showing that — when updated every 10 iterations matching AdamW's wall time — it achieves lower test error than both AdamW and Shampoo (which must update every 100 iterations). The experiments also show that alternative fractional powers (e.g., \(p=1\)) can outperform the default square root.

- **Connections to existing methods and positive-definite matrix optimization.** Section 2.3 shows the framework recovers RMSprop, PAdam, and root-free RMSprop as special cases. The full-matrix scheme is additionally validated on a metric nearness problem, matching standard Riemannian gradient descent while handling noisy observations that can be negative-definite.

## Weaknesses

### Fatal
None.

### Major
- **No wall-clock runtime numbers.** The paper repeatedly states that the method matches AdamW's runtime when updating every 10 iterations, and that Shampoo must update every 100 iterations to match. However, no actual wall-clock measurements are reported. Without timing data, the efficiency claim is unsubstantiated — the reader cannot verify that the 10-iteration and 100-iteration schedules are indeed runtime-equivalent, what precisions each method uses, or what the overhead of the truncated Cayley map actually is. This is the most significant evidential gap in the paper.

### Minor
- **NN evaluation limited to ImageWoof (10-class subset).** The vision experiments are restricted to ImageWoof with batch size 128. While the method is shown to work on three architectures, the paper motivates the problem by citing transformers broadly (including language tasks) and claims "effectively trains transformers with low-precision." The lack of experiments on ImageNet-1K, language tasks, or larger-scale settings weakens the evidence for practical utility. The paper acknowledges this in the conclusion as future work, which is honest but does not fill the gap.

- **Missing ablation studies on core components.** The method has several moving parts (spectral parametrization, local coordinate transformations, Cayley map with Skew/Tril constraints, truncated Cayley series, determinant constraints, exponential map truncation). No ablation study isolates which components matter or quantifies the cost–accuracy trade-off of the truncated Cayley map (e.g., number of Neumann terms vs. precision vs. time). This makes it difficult to attribute the reported performance to specific contributions.

- **Synthetic validation uses i.i.d. Gaussian gradients only.** Figures 2–3 validate that the spectral scheme matches the default scheme when gradients are i.i.d. Gaussian. While useful for method validation, this does not establish that the equivalence holds under realistic gradient distributions (non-i.i.d., heavy-tailed, anisotropic). The paper does not acknowledge this limitation or include any validation on real gradient sequences from a trained model.

- **Shampoo baseline comparison details are underspecified.** The paper uses grafting to improve Shampoo with infrequent updates (every 100 iterations) and explains why, which is appropriate. However, it does not state (a) what fractional power Shampoo uses (default is 1/4), (b) whether Shampoo is also run in half precision (the method is, but it is unclear about Shampoo), or (c) what the impact of using a more recent efficient Shampoo variant would be on the runtime comparison.

- **No error bars or standard deviations reported for test accuracy.** Though the paper uses 200-run random search for hyperparameter tuning, the reported test error curves do not include variance estimates. Given the small 10-class setting, variance could be non-negligible, and the claim that \(p=1\) outperforms \(p=2\) for ViT appears to be based on a single run without statistical significance.

### Trivial
- The content of "Claim 1" (line 77) appears to be missing — it reads "Claim 1." followed immediately by "Empirical validation..." This may be a parser artifact but should be checked.
- The number of Neumann series terms used for the truncated Cayley map in experiments is not stated in the main text (though the approximation in Section 2.4 implies terms up to \((\beta N)^4\)).

## Nice-to-Haves
- A systematic study of fractional powers (\(p = 1, 2, 4, 8\)) on a single architecture with multiple seeds, reporting convergence speed and final accuracy, would directly demonstrate the value of the spectral parametrization over fixed-root methods.
- A stability comparison in half precision plotting loss curves for Shampoo (full vs. half precision, with and without SVD) and the proposed method in half precision would concretely demonstrate the low-precision stability advantage.
- An ablation of truncation order in the Cayley map (e.g., 2 terms vs. 4 terms vs. exact) with wall-clock timing would help understand the cost–accuracy trade-off.

## Removed Points
These points are flagged to be removed — treat them with caution:

1. **"vecTril(C) is used without definition"** — The paper explicitly defines it at the introduction of Claim 4: "vecTril(C) represents the low-triangular half of C excluding diagonal entries." This criticism is factually wrong and is removed.
2. **"Claim 1 is mentioned but never stated — formatting gap"** — The content of Claim 1 may have been stripped by the parser (as happens with proven claim blocks); the empirical validation that follows provides the evidence. Removed per parser-artifact rule.
3. **"Should cite recent works on efficient matrix roots"** — The hard rule prohibits mentioning missing related works. Removed.
4. **"Missing hyperparameters for AdamW and Shampoo — the paper should report which hyperparameters matter most"** — The paper covers hyperparameter tuning via 200-run random search. The request for "which matter most" is a wishlist item, not a core flaw. Moved here.
5. **"K-FAC SVD is also expensive"** — This is acknowledged by the paper's framing; the critic's expansion on this point adds no new information. Removed.

## Novel Insights

The most striking meta-observation is that the harsh critic's core complaints are about experimental completeness (scale, ablations, wall-clock numbers) rather than about the method's correctness or theoretical soundness. The strength finder's praise centers on the theoretical rigor. This divergence suggests the paper has a genuinely novel and well-derived idea that is currently under-supported by experiments. The review would be meaningfully different — likely acceptance — if the authors added wall-clock timing, ImageNet-1K results, and basic ablations. The paper is not fatally flawed; it is incomplete in its empirical validation for the breadth of its claims.

## Suggestions

1. **Add wall-clock timing.** Measure end-to-end runtime on a representative benchmark (e.g., ViT-B/16 on ImageNet-1K for a fixed number of iterations) for AdamW, Shampoo, and the proposed method, reporting both per-iteration cost and total convergence time. This single addition would address the most serious weakness.
2. **Run at least one experiment on ImageNet-1K** or a similarly standard large-scale benchmark to substantiate the claim of practical utility for transformer training.
3. **Report error bars** (e.g., across 3–5 seeds) for the NN experiments, especially when comparing \(p=1\) vs. \(p=2\).
4. **Add an ablation** that varies the number of Neumann terms in the truncated Cayley map and reports test accuracy vs. wall-clock time, to validate the approximation choice.
5. **Explicitly state** the fractional power used for Shampoo and whether it is run in half precision or full precision, to clarify the fairness of the comparison.

## Score and Decision

The paper presents a novel, theoretically well-grounded framework for learning spectral factorizations of preconditioning matrices. The Riemannian derivation is a genuine contribution, and the synthetic validation confirms the update scheme's correctness. However, the experimental evaluation is too limited in scale and completeness to fully substantiate the claimed advantages over strong baselines. The lack of wall-clock timing, the restriction to a single 10-class dataset, and the absence of ablations are significant gaps. The contribution is promising but not yet ready for publication at a top-tier venue.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>