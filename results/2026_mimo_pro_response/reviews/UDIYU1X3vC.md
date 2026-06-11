Now I have enough calibration data. Let me finalize my assessment.

**Round 1 bracket:** Based on the initial search, this paper clearly sits above the rejected hyperbolic papers (HVT at 3.4, Binary Hyperbolic Embeddings at 4.5, Optimizing for Robust Hyperbolic DL at 4.4) and is comparable to or stronger than the accepted papers in the 6.0-6.6 range (HCNN at 6.0, Symmetric Spaces at 6.0, Shadow Cones at 6.33, Fast Hyperboloid Decision Tree at 6.6). It's well below the 8.0 papers. **Initial bracket: 6.0-7.0.**

**Round 2 narrowing:** HCNN (6.0) is the most directly comparable paper — both build fundamental neural layers for a hyperbolic model. Our paper has substantially stronger numerical stability evidence, thorough ablations (HCNN had none per R3), and strong genomics results. Shadow Cones (6.33) and Fast Hyperboloid Decision Tree (6.6) are in the same range but with different focus areas. **Narrowed bracket: 6.0-7.0, settling at 6.5.**

Now let me write the final review.

---

## Summary
This paper introduces Proper Velocity Neural Networks (PVNNs), constructing a complete Riemannian toolkit and neural network layers (MLR, FC, convolution, activation, batch normalization) on the Proper Velocity (PV) model of hyperbolic space. The PV model is an unconstrained representation (ℝⁿ) proven isometric to the Poincaré ball, and its practical advantage is avoiding the numerical instabilities that plague constrained models. The framework is validated on four tasks: synthetic numerical stability tests, image classification, graph node classification, and genomic sequence learning.

## Strengths
- **Compelling numerical stability evidence (Tables 1–3):** The paper systematically validates PV's stability across three independent failure modes — operator failure (PV 0% at r=1000 in FP32 vs. hyperboloid 100% by r=200), round-trip map error (PV 2.1×10⁻⁷ vs. Poincaré 2.1×10⁻⁴ and hyperboloid 1.0 in FP32), and gradient behavior (PV maintains a safe band [10⁻⁶, 10⁻⁴] vs. Poincaré vanishing to [10⁻¹¹, 10⁻¹³] and hyperboloid exploding to NaN). This is strong, direct evidence for the paper's central claim.
- **Clean mathematical derivation via isometry (Theorems 4.2–4.4):** Proving PV-to-Poincaré is a Riemannian isometry enables transferring all closed-form operators in a principled way. The gyro-by-Riemannian connection (Theorem 4.4) linking gyro operations to Exp/Log/PT is elegant and theoretically clean.
- **Efficient MLR formulation (Theorem 5.2):** The (zₖ, rₖ) parameterization reduces the C-class MLR score to inner products implementable as matrix multiplication, avoiding the O(b×C×n) intermediate tensor of per-class gyroaddition (lines 162–163). This is a concrete computational contribution.
- **Strong genomic results (Table 10):** PVCNN outperforms both Euclidean CNN and HCNN-S across all five TEB tasks, with gains of 5–9 MCC points (e.g., 93.78 vs. 85.45 on SINEs, 81.83 vs. 76.12 on LINEs). These are substantial and consistent improvements.
- **Thorough ablations (Tables 6–9):** The paper provides meaningful ablations comparing tangent vs. Riemannian FC/BN (Table 6), Fréchet iteration counts with runtime profiling (Table 7), with/without Exp₀ lifting (Table 8), and activation strategies (Table 9). These go well beyond what most HNN papers offer and provide practical design guidance. Table 7 is particularly informative for practitioners.

## Weaknesses
### Fatal
None

### Major
- **Isometry undercuts the "alternative geometry" framing — the contribution is a better coordinate system, not new geometry:** Theorem 4.2 establishes PV and the Poincaré ball are Riemannian isometric, meaning geodesic distances, curvature, and expressivity are identical. Yet the abstract calls PV "a stable alternative," the introduction motivates "exploration as a stable alternative geometry for HNNs" (line 15), and the conclusion positions PVNN as "a stable and practical geometry" (line 383). This oscillation between acknowledging the isometry ("geometrically isometric," line 64) and framing PV as a fundamentally different geometry is misleading. The contribution is an unconstrained chart with superior numerical properties — not a new geometric inductive bias. Readers should understand they're gaining numerical stability, not different expressivity. The paper would be stronger if it committed clearly to the "better coordinate system" framing.

### Minor
- **Image classification gains are within noise margins (Table 4):** CIFAR-10: 95.30 ± 0.18 vs. 95.12 ± 0.20 (best baseline), CIFAR-100: 78.20 ± 0.37 vs. 77.96 ± 0.09. These are marginal improvements with overlapping confidence intervals. The paper should describe these as "comparable" rather than implying superiority.
- **PVNN underperforms on weakly hyperbolic data (Table 5):** On Cora (δ=11), PVNN (51.42) loses to LNN (53.34) and KNN (52.26). Combined with marginal image classification gains, this suggests PV's advantages are dataset-dependent. The paper partially acknowledges this ("PV geometry is more effective on strongly hyperbolic graphs," line 307) but could more explicitly characterize when PV helps and when it doesn't, guiding practitioners on model selection.
- **No training dynamics evidence for stability claims:** Tables 1–3 test operators in isolation (synthetic experiments), not during actual downstream training. Showing gradient norms, NaN frequency, or loss curves during training would more directly validate the practical stability advantage. The Fréchet mean iteration analysis (Table 7) partially addresses this by showing GyroBN behavior during training, but gradient-level stability during full training remains unexplored.

### Trivial
None

## Nice-to-Haves
- Computational cost comparison (FLOPs, wall-clock training time) of PVNN vs. Poincaré/Lorentz networks would quantify whether PV is also faster, not just more stable. Table 7 shows Fréchet computation times but no overall comparison.
- Analysis of gradient norms during downstream training to complement the synthetic stability tests.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Graph learning baseline comparability** — The paper explicitly states all models share the same architecture differing only in hyperbolic model (line 305). Without evidence that baselines are unfairly configured, this concern is speculative.
- **Missing related works** — Per rules, cannot verify external references.
- **Formatting/style nitpicks** — Parser artifacts, not author errors.

## Novel Insights
The paper's genuinely novel insight is that the PV model's unconstrained nature (ℝⁿ = PV space) enables Euclidean concatenation for convolution and direct-space activations without exponential/logarithmic map overhead — a practical advantage that follows naturally from the coordinate choice but hasn't been systematically exploited. The systematic demonstration across three independent failure modes (operator, round-trip, gradient) that this unconstrained representation yields measurable, large-magnitude stability advantages is a valuable empirical contribution to the hyperbolic deep learning community. The correlation between dataset hyperbolicity (δ) and PV advantage is informative for practitioners.

## Suggestions
- Reframe the contribution explicitly as "an unconstrained coordinate system for hyperbolic space with superior numerical properties" rather than "an alternative geometry." This is more precise and defensible given the isometry.
- Add a brief discussion in Section 6.3 characterizing when PV helps (strongly hyperbolic data) vs. when it doesn't (weakly hyperbolic data), rather than just noting the Cora result in passing.
- Consider adding training-time gradient monitoring experiments to complement Tables 1–3.

## Calibration Report

**All anchors retrieved:**

*Round 1:*
- nSDOkm0SKo (1.00) — Financial market analysis. Irrelevant.
- P49gSPmrvN (1.00) — Scientific discourse UMAP. Irrelevant.
- gwZ90hFSL2 (1.00) — Cross-lingual robots. Irrelevant.
- Uj0h13lVrR (1.00) — GFlowNets. Irrelevant.
- q6WtaLj8O1 (3.00) — Fully Hyperbolic Knowledge Hypergraph. Rejected HNN; less rigorous.
- b2FFWnwZxl (3.40) — HVT Hyperbolic Vision Transformer. Rejected; marginal results, weak motivation.
- NYPJz0CL5X (3.00) — Hyperdimensional Representation. Different area, rejected.
- A1JdcLawSu (3.00) — Hyperspherical replay. Different area, rejected.
- jzneu6AO2x (4.25) — Riemannian Hyperbolic Prototypical Networks. Rejected hyperbolic work.
- 2DJUXmHZ2O (4.75) — Poincaré Policy for MARL. Rejected.
- KmdwGYbMv0 (4.50) — Binary Hyperbolic Embeddings. Rejected.
- WOopKWDWtS (4.40) — Optimizing Robust Hyperbolic DL. Rejected; marginal improvements, unclear motivation.
- ekz1hN5QNh (6.00) — **Fully Hyperbolic CNN.** Most comparable: builds CNN layers for Lorentz model. Our paper is clearly stronger (better stability evidence, ablations, genomics results).
- bwOndfohRK (6.00) — **Neural networks on Symmetric Spaces.** Unified framework; our paper is more focused with stronger empirical evidence.
- k9t8dQ30kU (6.75) — Task structure and representational geometry. Less relevant.
- zbKcFZ6Dbp (6.33) — **Shadow Cones.** Geometric contribution with strong results; comparable quality.
- 3i13Gev2hV (8.00) — Compositional Entailment Learning. More impactful; our paper is below this.
- Xo0Q1N7CGk (8.00) — Grid cells. Less relevant.
- agPpmEgf8C (8.00) — Predictive auxiliary objectives. Less relevant.
- cJs4oE4m9Q (8.00) — Deep Orthogonal Hypersphere. Less relevant.

*Round 2:*
- ekz1hN5QNh (6.00) — HCNN (same as above).
- fJNnerz6iH (6.25) — Magnitude Invariant Parametrizations. Accepted; different area.
- bwOndfohRK (6.00) — Symmetric Spaces (same as above).
- NLbRvr840Q (6.00) — Hypergraph Dynamic System. Accepted; different area.
- TTonmgTT9X (6.60) — **Fast Hyperboloid Decision Tree.** Accepted; novel approach with strong results, good presentation.
- YcaFqY8LWD (6.25) — GyroAtt. Rejected; gyro attention framework.
- ZkBg5D2lgT (6.25) — Robotics taxonomies hyperbolic. Rejected.
- fJNnerz6iH (6.25) — (duplicate)

**Bracket and narrowing:**
- Round 1 bracket: 6.0–7.0. The paper is clearly above rejected hyperbolic DL papers (3.0–4.5) and at least as strong as accepted 6.0 papers (HCNN, Symmetric Spaces), given its superior stability evidence and ablations. It's below the 8.0 tier (Compositional Entailment Learning).
- Round 2 narrowed to 6.0–7.0. The paper is comparable to Shadow Cones (6.33) and Fast Hyperboloid Decision Tree (6.6) but with a different profile: stronger stability evidence, similar or better downstream results, but a framing issue.
- Final score: **6.5** — stronger than HCNN (6.0) due to much better evidence, comparable to Shadow Cones (6.33) and Hyperboloid Decision Tree (6.6), with the framing issue preventing a higher score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>