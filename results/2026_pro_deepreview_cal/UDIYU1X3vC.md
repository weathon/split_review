Now I have a thorough understanding of the paper and the calibration anchors. Let me compose the final review.

---

## Summary

This paper introduces Proper Velocity Neural Networks (PVNNs), leveraging the Proper Velocity (PV) model of hyperbolic space — an unconstrained representation rooted in special relativity — as a numerically stable alternative to the Poincaré ball and hyperboloid models. The authors first derive the complete Riemannian toolkit for PV space (exponential/logarithmic maps, parallel transport, geodesic distance) via its isometry to the Poincaré ball, then develop fundamental neural network layers (MLR, FC, convolution, activation, batch normalization) in PV geometry. Experiments across numerical stability, image classification, graph node classification, and genomic sequence learning demonstrate that PVNNs match or outperform existing hyperbolic baselines while avoiding the numerical pitfalls of constrained representations.

## Strengths

- **Complete Riemannian toolkit for a previously unexplored model:** The paper derives closed-form Riemannian operators (Exp, Log, PT, distance) for the PV manifold (Theorem 4.3, Eqs. 10–13), exploiting the isometry to the Poincaré ball (Theorem 4.2). This is the first systematic treatment of PV geometry for machine learning, providing a genuinely new alternative to the standard Poincaré and hyperboloid models.

- **Efficient and well-engineered neural layer formulations:** The PV MLR (Theorem 5.2, Eq. 19) reduces to inner-product computations that avoid explicit gyroaddition, enabling efficient batched processing and recovering Euclidean MLR as \(K \to 0^-\). The PV FC layer (Theorem 5.3) and GyroBN (Eq. 25, with formal normalization guarantees in Theorem 5.4) are similarly well-derived. The unconstrained nature of PV space simplifies convolution concatenation (Section 5.3) compared to boundary-avoidance strategies needed in the Poincaré ball.

- **Convincing numerical stability demonstration:** Tables 1–3 provide clear, controlled evidence: PV maintains zero failure rate for scalar gyromultiplication up to \(r = 1000\) where the hyperboloid fails at \(r = 20\); round-trip error of Exp/Log is near machine precision in FP32 (\(2.1 \times 10^{-7}\)) vs. \(2.1 \times 10^{-4}\) for Poincaré and \(1.0 \times 10^0\) for hyperboloid; and gradient magnitudes remain in a stable band without vanishing or NaN.

- **Strong empirical results on graph and genomic tasks:** On graph node classification (Table 5), PVNN achieves the highest accuracy on the three most hyperbolic datasets, with a 5.86% absolute gain on Airport over the best prior method. On genomic sequence learning (Table 10), PVCNN achieves the top Matthews correlation coefficient on all five TEB tasks, with particularly large margins on SINEs (~9 MCC points over HCNN-S).

- **Thorough ablation studies:** The paper systematically ablates tangent vs. Riemannian layers (Table 6), batch statistic approximations (Table 7), input lifting strategies (Table 8), and activation schemes (Table 9), providing clear evidence that the Riemannian PV constructions and GyroBN contribute meaningfully to performance.

## Weaknesses

### Fatal

None.

### Major

- **Stability-to-training causal link is not empirically validated.** Section 6.1 convincingly demonstrates operator-level numerical stability (no NaN, low round-trip error, stable gradients), and Sections 6.3–6.4 show PVNN outperforms baselines. However, the paper does not directly test whether the *stability advantage* — rather than other properties of PV geometry — drives the improved task performance. No training dynamics are reported (gradient norms during training, loss curves, convergence speed, embedding norm evolution) that would isolate stability as the causal mechanism. The graph and genomic gains could plausibly arise from architectural differences or the specific parameterization rather than from stability alone. This weakens the paper's central narrative that stability is the key differentiator.

### Minor

- **The image classification experiment tests only a PV MLR head, not a complete PVNN.** Section 6.2 replaces only the final classification layer of a Euclidean ResNet-18 with a PV MLR; the backbone remains entirely Euclidean. This does not evaluate whether the PV FC, convolutional, or normalization layers are effective for vision. The paper implicitly acknowledges this limitation by contrasting it with the full PVCNN in the genomic experiment (Section 6.4), but the claim of a "general neural network framework" would be strengthened by a vision experiment using PV layers throughout. The CIFAR gains are also within overlapping error bars (CIFAR-100: 78.20±0.37 vs. 77.96±0.09).

### Trivial

- **The δ-hyperbolicity values in Table 4 are cited from prior work but not connected to the classification results in an explanatory way,** making their inclusion feel somewhat decorative rather than analytically motivated.

## Nice-to-Haves

- Adding a training-dynamics experiment (e.g., monitoring gradient norms and loss curves for PV vs. Poincaré models on a boundary-stressing task like the Airport graph) would close the stability-to-performance loop and substantially strengthen the paper's narrative.

- Extending the vision experiment to a shallow fully-hyperbolic PV convolutional network (e.g., on MNIST or Fashion-MNIST) would test whether PV layers — not just the MLR head — confer advantages in visual domains.

- Reporting wall-clock training time or per-epoch overhead of PV operators relative to Poincaré and hyperboloid baselines would help practitioners assess the practical cost-benefit tradeoff.

- A brief remark clarifying that PV is a reparameterization of the Poincaré hyperboloid (same intrinsic geometry, different coordinate chart) would help readers understand the nature of the novelty: the contribution is in the coordinate representation and its computational consequences, not in discovering a new manifold.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The Poincaré ball shows zero failure rate for gyromultiplication, which appears to contradict anecdotal reports of boundary failures"* — REMOVED. This is not a weakness of the paper but a question about the authors' implementation; the paper reports what it observes under its experimental conditions. The Poincaré ball's gyromultiplication involves a different algebraic structure (Möbius gyromultiplication), and the zero failure rate in Table 1 is plausible under the tested radii. This is not a contradiction requiring resolution.

- *"Baseline tuning in the graph experiments is not fully documented"* — DEMOTED from Major to not listed as a main weakness. The authors state that experimental details are in Appendix C.3; since the appendix is stripped by the parser, we cannot verify the claim of missing tuning details. This is a documentation concern whose resolution lies in the supplementary material, not a confirmed flaw.

- *"The computational overhead of PV operators is not reported"* — MOVED to Nice-to-Haves. Runtime comparison is useful but not essential for validating the paper's core claims.

## Novel Insights

The reviews do not surface genuinely novel insights beyond the paper's own contributions. The paper itself offers the insight that an unconstrained coordinate chart for hyperbolic space (the PV model) can serve as a drop-in replacement for constrained models in hyperbolic neural networks, providing numerical stability without sacrificing closed-form Riemannian operators. The key observation — that the PV model's isometry to the Poincaré ball enables transferring the entire Riemannian toolkit while gaining the practical benefits of an unconstrained domain — is the paper's own contribution and is well-articulated.

## Suggestions

- The paper would benefit from explicitly positioning PV as a coordinate reparameterization rather than a new manifold. A sentence after Theorem 4.2 noting that PV shares the same intrinsic hyperbolic geometry as the Poincaré ball and hyperboloid — differing only in its coordinate chart — would preempt confusion about the nature of the novelty.

- In the graph experiments (Table 5), the Cora result shows PVNN underperforming LNN (51.42 vs. 53.34). The paper notes Cora is "weakly hyperbolic" (\( \delta = 11 \)) but does not explain why the hyperboloid model might be more suitable in this regime. A brief discussion would strengthen the analysis.

## Score and Decision

### Calibration Summary

**Round 1 — Bracketing:**
- Weak band: `b2FFWnwZxl` (3.40, reject — hyperbolic ViT), `kkVTeMvC9D` (3.40, reject — training Jacobian), `xA25Ib7H8U` (2.33, reject — Ricci flows), `HDmmwwTIlf` (2.50, reject — hyperbolic conservation laws). All clearly below this paper.
- Middle band: `ekz1hN5QNh` (6.00, accept — HCNN, fully hyperbolic CNN on Lorentz), `30aSE3FB3L` (5.67, accept — Matrix Manifold NN++), `bwOndfohRK` (6.00, accept — neural networks on symmetric spaces), `MEnPLXJNng` (4.75, reject — Riemannian transformation layers). This paper is stronger than all of these.
- Strong band: `Xo0Q1N7CGk` (8.00, accept — conformal isometry), `3i13Gev2hV` (8.00, accept — compositional VL), `GRMfXcAAFh` (8.00, accept — oscillatory SSM), `d8w0pmvXbZ` (8.00, accept — training instability proxies). This paper is below these.

**Bracket:** between 6.0 and 7.5.

**Round 2 — Narrowing:**
- `ZkBg5D2lgT` (6.25, reject — GPLVM on hyperbolic manifolds). This paper is stronger (more complete contribution, better experiments).
- `TTonmgTT9X` (6.60, accept — HyperDT, hyperbolic decision trees). This paper is comparable. HyperDT has a clever novel idea but narrow scope and limited ablations; PV paper has broader scope, more rigorous derivations, and more comprehensive experiments.
- `OwpLQrpdwE` (7.40, accept — kernel ODEs on manifolds). This paper is weaker. The kernel ODE paper has deeper theoretical contributions (error bounds, novel solver) and is more methodologically innovative.
- `AP0ndQloqR` (7.50, accept — geometry of neural RL). This paper is weaker. More theoretical depth and broader implications.
- `cmXWYolrlo` (7.50, accept — geometric inductive biases). This paper is weaker. More fundamental theoretical contribution.

This paper sits between HyperDT (6.60) and the 7.40+ anchors, landing at **6.5**. It is clearly stronger than HCNN (6.00), offering a more novel contribution (new model vs. new layers on existing model), broader experimental coverage, better ablation, and stronger results on graph/genomics. It falls short of the 7.40+ tier because the vision experiment is limited, the stability-to-training link is not directly validated, and the contribution — while solid and well-executed — is primarily a practical reparameterization rather than a deep theoretical advance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>