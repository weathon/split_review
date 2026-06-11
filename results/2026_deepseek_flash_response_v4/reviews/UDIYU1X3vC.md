## Summary

This paper introduces Proper Velocity Neural Networks (PVNNs), grounding deep learning in the unconstrained Proper Velocity (PV) model of hyperbolic geometry from special relativity. It derives the complete Riemannian toolkit (exponential/logarithmic maps, parallel transport, geodesic distance) for the PV manifold via proven isometries to the Poincaré ball (Theorem 4.2), then constructs MLR, FC, convolutional, activation, and batch normalization layers using these operators. Experiments across numerical stability, image classification, graph node classification, and genomic sequence learning demonstrate that PV avoids the numerical failure modes of the Poincaré ball and hyperboloid model while achieving competitive or superior task performance.

## Strengths

1. **First complete closed-form Riemannian toolkit for the PV manifold**: The paper derives explicit closed-form expressions for the exponential map (Eq. 10), logarithmic map (Eq. 11), parallel transport (Eq. 12), and geodesic distance (Eq. 13) on PV space. These are obtained by proving the mappings in Eq. (4) are Riemannian isometries (Theorem 4.2) via explicitly computed differentials (Lemma 4.1), then transferring the known Poincaré-ball operators through the isometry. Prior work only used the algebraic gyrovector structure of PV space; this paper provides the Riemannian operators needed to build neural networks.

2. **Quantitatively demonstrated numerical stability across three independent metrics**: Section 6.1 evaluates gyromultiplication failure rates (Table 1), Exp/Log round-trip error (Table 2), and gradient magnitude range (Table 3). PV maintains 0% failure at r=1000 in FP32 while the hyperboloid model reaches 100% failure by r=200. PV's round-trip error is 2.1×10⁻⁷ in FP32, two orders of magnitude better than Poincaré (2.1×10⁻⁴) and seven orders better than hyperboloid (1.0×10⁰). PV's gradients stay in [1.1×10⁻⁴, 2.1×10⁻⁶] while Poincaré gradients vanish to ~10⁻¹³ and hyperboloid gradients explode to NaN.

3. **Theoretically grounded normalization with provable statistic-correcting properties**: Theorem 5.4 establishes two homogeneity properties (Eq. 26 for gyroaddition biasing; Eq. 27 for gyromultiplication scaling) that explicitly guarantee the PV GyroBN pipeline in Eq. (25)—centering, scaling, then biasing—normalizes the Fréchet mean to the target β and the dispersion to s². This directly addresses the limitation noted in Section 2 that prior manifold BN approaches "often lack theoretical guarantees to normalize sample statistics."

4. **Reparameterization that avoids O(b×C×n) intermediate tensors in MLR**: Theorem 5.2 reduces the PV MLR score to Eq. 19, which depends only on inner products ⟨x, z_k⟩ expressible as a single matrix multiplication. Section 5.1 explicitly contrasts this with the naive formulation (Eq. 18) that would require explicit gyroaddition -p_k ⊕ x per class, producing a b×C×n intermediate tensor that risks out-of-memory errors in high dimensions.

5. **Euclidean recovery as curvature → 0⁻**: Theorem 5.2 shows v_k(x) → ⟨x, z_k⟩ + b_k for MLR, and Theorem 5.3 (Eq. 22) shows y_k → ⟨x, z_k⟩ + b_k for the FC layer, both recovering the standard Euclidean forms. This smooth interpolation between hyperbolic and Euclidean behavior is a practical advantage for initialization and for datasets where the optimal geometry may be near-Euclidean.

6. **Extensive ablation studies on graph learning**: Tables 6–9 systematically ablate tangent-space vs. Riemannian FC, tangent vs. GyroBN, the effect of the exponential map lifting, and different activation variants, providing a nuanced picture of where each design choice matters.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The extremely large improvement on Airport (97.96% vs. 88.40% best neural baseline) is not adequately explained.** Table 6 shows that switching from tangent-space FC (86.99%) to the Riemannian PV FC accounts for virtually the entire ~11-point gain. The paper attributes this to "PV geometry is more effective on strongly hyperbolic graphs," but does not analyze why the Riemannian formulation so dramatically outperforms the tangent-space one—a standard and well-understood way to build hyperbolic layers. The result is likely real given the consistent pattern across multiple datasets and ablations, but the magnitude of the gap invites more scrutiny than the paper provides.

2. **Framing slightly overstates the geometric novelty.** The paper acknowledges the Riemannian isometry with the Poincaré ball (Theorem 4.2) and uses it to derive all operators. However, it repeatedly describes PV as a "new alternative" and "stable alternative geometry," which could imply a geometrically distinct space rather than a different coordinate chart of the same constant-negative-curvature space. The genuine contribution—better numerical conditioning via an unconstrained coordinate system—is real but the paper would be strengthened by being more explicit that PV does not enable representations that Poincaré cannot; it enables those representations to be trained without hitting numerical boundaries in FP32.

3. **The KNN baseline in Table 5 is not a direct architectural comparison.** The paper states "All models share the same architecture consisting of two FC layers with nonlinear activations followed by an MLR classifier; they differ only in the underlying hyperbolic model," but KNN (Mao et al., 2024) is a non-parametric nearest-neighbor classifier that does not use FC layers or backpropagation. A footnote clarifying that KNN does not share the same architecture would resolve this.

4. **Genomic experiments only include one hyperboloid baseline.** Table 10 compares PVCNN against Euclidean CNN and HCNN-S (hyperboloid), but no Poincaré-based convolutional network is included. Since the paper claims PV is a better alternative to both established models, including a Poincaré convolutional baseline would strengthen the comparison.

5. **Direct Euclidean activation can fail badly, but this is under-discussed.** Section 5.3 presents the direct PV-space activation (x → σ(x)) as an efficient option, but Table 9 shows it drops to 38.10% on Cora (vs. 52.26% for tangent activation). This large degradation is noted but not discussed as a limitation of bypassing the manifold structure.

6. **End-to-end computational cost is not compared.** The paper reports timing for GyroBN variants (Table 7) but does not report end-to-end training time or throughput for PVNN vs. Poincaré/hyperboloid baselines on any task. Since PV operations involve mapping to/from the Poincaré ball (via π and dπ), efficiency comparisons would be informative.

### Trivial
None.

## Nice-to-Haves
- Test whether PVNN's task improvements stem from numerical stability by training Poincaré/hyperboloid models in FP64 (where numerical issues are reduced) and comparing to PVNN in FP32. If the gap narrows, the advantage is predominantly numerical.
- Add synthetic data with controlled tree-likeness to systematically characterize when PV helps most.

## Removed Points

- **Criticism about curvature hyperparameter not being reported**: The paper references experimental details in Appendices C.2–C.4, which are stripped by the parser. This information is assumed to exist in the original submission.
- **Criticism about hyperparameter search ranges and trials**: Likewise assumed to be in the appendix.
- **Criticism about Riemannian optimization confound**: Optimizer details would be in the appendix; the paper states "all models share the same architecture... they differ only in the underlying hyperbolic model," implying consistent optimization setup.
- **Criticism about missing numerical stability end-to-end analysis**: The isolated operator tests in Section 6.1 are a standard and valid methodology for numerical stability evaluation.
- **Criticism that "first systematic study" is overclaimed**: The paper credits Ungar (2022) for the algebraic structure and notes prior ML work has not explored PV. This claim is reasonable.
- **Criticism about activation not respecting manifold structure**: The paper presents the direct activation as an efficiency option and provides experimental comparison showing its trade-offs. This is transparent reporting.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add a brief analysis section discussing why the Riemannian PV FC so dramatically outperforms the tangent-space FC on Airport, perhaps examining the role of the specific nonlinearity in Eqs. (22)–(23) versus the standard tangent-space formulation.
- Clarify in Table 5 that KNN uses a different architecture (non-parametric, no FC layers) from the neural baselines.
- Add a Poincaré-based convolutional baseline to the genomic experiments.
- Discuss the failure mode of the direct Euclidean activation (Table 9 on Cora) as a limitation and provide guidance on when to prefer tangent vs. direct activation.
- Be more precise in the framing: describe PV as a "numerically stable coordinate representation" of hyperbolic space rather than a "new alternative geometry."

## Calibration

**Round 1 bracket**: [6, 8]

**Round 1 anchors**:
- **b2FFWnwZxl** (avg 3.40, sim 0.71): HVT — rejected hyperbolic vision transformer. PVNN is substantially stronger in every dimension.
- **xA25Ib7H8U** (avg 2.33, sim 0.71): Continuous-depth Ricci flows — rejected. Not comparable; PVNN is much more rigorous.
- **ekz1hN5QNh** (avg 6.00, sim 0.79): Fully Hyperbolic CNN — accepted. Very similar type of contribution (layer toolkit on a hyperbolic model). PVNN has stronger numerical evidence, more task domains, and better ablations. → PVNN is stronger.
- **bwOndfohRK** (avg 6.00, sim 0.78): Symmetric Spaces — accepted. Broad theoretical contribution but weaker empirical validation. → PVNN is stronger.
- **jzneu6AO2x** (avg 4.25, sim 0.77): Hyperbolic Prototypical Networks — rejected. Limited scope and weaker evidence. → PVNN is stronger.
- **3i13Gev2hV** (avg 8.00, sim 0.69): Compositional Entailment — accepted. Application-focused, different type of contribution.
- **Xo0Q1N7CGk** (avg 8.00, sim 0.69): Conformal Isometry — accepted. Different area entirely.

**Round 2 anchors (narrowing within [6, 8])**:
- **TTonmgTT9X** (avg 6.60, sim 0.71): Fast Hyperboloid Decision Tree — accepted. Clean focused contribution but narrower scope. → PVNN has broader impact and stronger empirical validation.
- **30aSE3FB3L** (avg 5.67, sim 0.74): Matrix Manifold Neural Networks++ — accepted. Mixed reviews, weaker experiments, narrower contribution. → PVNN is substantially stronger.
- **zbKcFZ6Dbp** (avg 6.33, sim 0.71): Shadow Cones — accepted. Partial order embeddings with limited empirical validation. → PVNN has stronger empirical scope.

**Final score determination**: The paper clearly sits above the 6.00 anchors (Fully Hyperbolic CNN, Symmetric Spaces) due to stronger numerical evidence, broader task coverage, and more thorough ablations. It also outperforms the 6.60 anchor. However, it does not reach the 8.00 level of top papers, which address more fundamental questions or achieve larger empirical impact. The weaknesses (overstated framing, Airport gap, missing baselines) are real but do not undermine the core contribution.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>