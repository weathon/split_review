## Summary

This paper introduces Proper Velocity Neural Networks (PVNNs), a hyperbolic neural network framework built on the Proper Velocity (PV) model — an unconstrained coordinate representation of hyperbolic geometry rooted in Einstein's special relativity. The paper establishes the complete Riemannian toolkit for PV space (exponential/logarithmic maps, geodesic distance, parallel transport) by proving it is isometric to the Poincaré ball, then derives core neural network layers (MLR, FC, convolutional, activation, batch normalization). Experiments across numerical stability, image classification, graph learning, and genomic sequence learning demonstrate that PVNNs provide practical numerical stability advantages and competitive or superior performance compared to existing hyperbolic models.

## Strengths

- **Riemannian isometry proven and exploited (Theorem 4.2).** The paper proves that PV space and the Poincaré ball are Riemannian isometric — extending the previously known algebraic gyrovector isomorphism to a full geometric isometry — and uses this result to derive closed-form Riemannian operators (Exp, Log, parallel transport, geodesic distance) on PV space. This is a clean theoretical result that turns an abstract algebraic construction into a usable geometric toolkit.

- **Clear and well-measured numerical stability advantage (Section 6.1, Tables 1–3).** The paper provides direct empirical evidence across three metrics (gyro operator failure rate, Riemannian round-trip error, gradient magnitude) that PV's unconstrained representation avoids the boundary-related pathologies of the Poincaré ball (vanishing gradients ~1e-12) and hyperboloid model (NaN gradients). In FP32, PV achieves round-trip error 2.1×10⁻⁷ versus 2.1×10⁻⁴ for Poincaré and 1.0×10⁰ for hyperboloid. These are concrete, measurable improvements that stem directly from the unconstrained geometry.

- **Simplified PV MLR avoiding O(b×C×n) intermediate tensors (Theorem 5.2).** The paper derives a closed-form expression for PV MLR (Eq. 19) that depends only on inner products ⟨x, z_k⟩ implementable as a single matrix multiplication, avoiding the per-class gyroaddition that would produce b×C×n intermediate tensors. This is a genuine practical engineering contribution that makes PV NN training feasible at scale.

- **Strong graph learning results on highly hyperbolic datasets (Table 5).** On Airport (δ=1, strongly hyperbolic), PVNN achieves 97.96% accuracy, improving over the strongest baseline (KNN at 92.10%) by 5.86 absolute points — a substantial and convincing margin. On Disease (δ=0) and PubMed (δ=3.5), PVNN also leads all prior hyperbolic models. The ablation study (Table 6) confirms the Riemannian PV FC layer itself drives these gains, outperforming a tangent-space variant by 10.94 points on Airport.

- **Consistent gains across all five genomic sequence learning tasks (Table 10).** PVCNN outperforms both Euclidean CNN and hyperboloid-based HCNN-S on all TEB datasets, with the largest gain on SINEs (+8.33 MCC points over HCNN-S, +8.63 over Euclidean). The breadth across diverse transposable element types (retrotransposons, DNA transposons, pseudogenes) demonstrates generalizability beyond a single domain.

- **Extensive ablations.** The paper includes thorough ablations on tangent vs. Riemannian FC (Table 6), different normalization variants including computational cost analysis (Table 7), the effect of Exp₀ lifting (Table 8), and activation choices (Table 9), giving readers a clear picture of which design choices matter and at what computational cost.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Image classification gains are modest and may not be statistically significant.** In Table 4, the best PV MLR achieves 95.30±0.18 on CIFAR-10 versus 95.12±0.20 for Unidirectional MLR (0.18pp) and 78.20±0.37 on CIFAR-100 versus 77.96±0.09 for Lorentz MLR (0.24pp). These differences are within overlapping error bars. Additionally, the Poincaré MLR baseline on CIFAR-10 has a standard deviation of ±1.51 — roughly ten times larger than all other methods (±0.12 to ±0.20) — which may indicate tuning issues with that baseline that could affect the comparison. The paper's claim that PV "matches or outperforms" is accurate but the abstract and introduction could be more precise about the size of these gains.

- **Connection between numerical stability and downstream performance is not established.** Section 6.1 convincingly demonstrates PV's numerical superiority in isolation, but the paper does not clarify whether any baseline runs in the downstream experiments (image, graph, genomics) actually encountered training failures (NaN/Inf, gradient clipping) that PV avoided. If the baselines trained successfully without numerical issues, the stability advantage, while real, may not explain the performance differences in Tables 4, 5, and 10. The paper should clarify this relationship.

- **The role of PV geometry vs. other factors is somewhat unclear given the "without Exp₀" results.** The paper shows that directly treating Euclidean features as PV coordinates (skipping the Exp₀ lift) performs nearly as well as the full geometric lifting in both image (Table 4) and graph (Table 8) settings. The paper discusses this briefly but does not fully address the implication: if simply using Euclidean features as PV coordinates works as well as explicitly mapping them via the exponential map, then how much of the observed improvement is attributable to the PV geometry versus other factors (e.g., the specific parameterization of the MLR/FC layers)?

- **No analysis of learned representations.** The paper does not visualize or analyze what the PV embeddings actually learn (e.g., via the isometry mapping to the Poincaré ball) to demonstrate that PVNN captures hierarchical structure. Without this, it is difficult to confirm that PVNN succeeds for the geometric reasons claimed rather than for auxiliary reasons (e.g., different optimization dynamics).

### Trivial
None.

## Nice-to-Haves
- A dedicated limitations section discussing when PVNN might not be the best choice (e.g., the Cora result where PVNN underperforms LNN) and the fact that PV is isometric to the Poincaré ball (so the contribution is representational, not geometric) would improve candor.
- A discussion of sensitivity to the curvature value (fixed at K=-1 in all experiments) would be informative, especially since the isometry holds only when curvature is fixed.

## Removed Points

The following points from the inputs were removed after verification against the paper:

1. **Complaint about Theorem 5.4 not guaranteeing centering produces Fréchet mean 0.** This follows directly from Eq. (26): FM({-μ⊕ᵤ x_i}) = -μ⊕ᵤ FM({x_i}) = -μ⊕ᵤ μ = 0. The critic misread the theorem.

2. **Reproducibility concern about code not being available for review.** The paper states "code will be released upon acceptance," which is standard for submissions. Removed per guidelines.

3. **Concern about the paper "not discussing whether this results in noticeable overhead" for the exponential map operator.** This is speculative without implementation comparison; the paper's focus is on correctness and stability, not runtime benchmarking of individual operators.

4. **Request for "large-scale experiments" (ImageNet, OGBN-Products).** This goes beyond the paper's stated scope, which covers four specific task families with standard benchmarks.

5. **Complaint about missing limitations section.** Moved to Nice-to-Haves as it does not threaten the core contribution.

6. **Complaint about "no analysis of learned representations."** Moved to Minor as a genuine but non-fatal concern.

7. **Generic concern about "curvature fixed at K=-1."** Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. An interesting observation that emerges from the reviews is that the "without Exp₀" variant — which treats Euclidean features directly as PV coordinates — performs comparably to the geometrically-principled variant, raising an underexplored question about how much of PVNN's performance comes from the geometry versus the specific parameterization of its layers.

## Suggestions

1. Clarify whether any baseline runs in the downstream experiments encountered training failures (NaN/Inf, gradient clipping) and how such runs were handled in the reported results. This would connect the stability analysis to the performance results.
2. Add a brief discussion about the "without Exp₀" results and what they imply about the role of PV geometry vs. the specific layer parameterization.
3. Calibrate language about image classification results to precisely reflect the modest gains observed (e.g., "comparable performance" rather than implying clear superiority).
4. Consider adding a visualization of learned embeddings mapped to the Poincaré ball via isometry to demonstrate that PVNN captures hierarchical structure.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| ekz1hN5QNh (Fully HCNN) | 6.00 | 1,2 | Very similar paper (hyperbolic NN layers); PV paper has broader experiments and stronger theory |
| bwOndfohRK (Symmetric Spaces NN) | 6.00 | 1,2 | Comparable mathematical depth; PV paper has more extensive experiments |
| MEnPLXJNng (Riemannian Transform Layers) | 4.75 | 1 | More general but weaker experiments; PV paper is clearly stronger |
| WOopKWDWtS (Robust Hyperbolic Learning) | 4.40 | 1 | Similar marginal gains but less coherent contribution; PV paper is stronger |
| TTonmgTT9X (Fast Hyperboloid Decision Trees) | 6.60 | 2 | Different task (decision trees vs. NNs); comparable rigor but different evaluation criteria |
| zbKcFZ6Dbp (Shadow Cones) | 6.33 | 2 | Comparable theoretical depth; different application domain |
| 83le3arfeA (Balanced Hyperbolic Embeddings) | 5.50 | 2 | Different task (OOD detection); PV paper has stronger theory |
| fJNnerz6iH (Magnitude Invariant Hypernetworks) | 6.25 | 2 | Not directly comparable (hypernetworks); similar score band |
| IUmDBY4NOQ (Geometry-aware Distance, Hyperbolic) | 4.75 | 3 | PV paper is clearly stronger in both theory and experiments |

**Round 1 bracket:** 5.5 – 7.5. The paper is clearly stronger than the 4.4–4.75 anchors (robust hyperbolic learning, Riemannian transform layers) and comparable in quality but broader in scope than the 6.0 anchors (HCNN Lorentz, Symmetric Spaces).

**Round 2 narrowing:** Compared against the 6.0–6.6 anchors, the PV paper has stronger theory (proven isometry explicitly exploited to derive all operators), broader experiments (4 task families), and more thorough ablations. However, the image classification gains are modest (a known pattern among hyperbolic NN papers at this score level) and the connection between stability and downstream performance is not established. These limitations prevent the paper from reaching the 7+ range but place it comfortably above 6.0.

**Final score: 6.5** — a solid, well-executed paper with a clear theoretical contribution and strong experimental evidence in two of four task domains.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>