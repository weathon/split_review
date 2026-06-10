Now I have enough calibration data. Let me synthesize the final review and score.

**Round 1 bracket:** The paper falls between the weak anchors (avg 2.5–3.4, all rejected) and strong anchors (avg 8.0, all accepted with strong empirical/theoretical contributions). The most relevant comparators are the middle band papers: HCNN (avg 6.00), Symmetric Spaces (avg 6.00), and Fast Hyperboloid DT (avg 6.60) — all accepted. This places the paper plausibly in the 5.5–8.0 range.

**Round 2 narrowing:** Within the bracket, I compared against:
- **HCNN (6.00)**: PVNN is clearly stronger — more complete Riemannian toolkit, more thorough ablations, stronger numerical stability evidence, broader experimental scope. HCNN was criticized for marginal improvements and limited ablation.
- **Symmetric Spaces (6.00)**: Comparable theoretical depth, but PVNN has much stronger empirical validation.
- **Fast Hyperboloid DT (6.60)**: Different contribution type, but PVNN's contribution is more complete on both theoretical and empirical fronts.
- **Local Loss Optimization (7.00)**: Comparable level of contribution quality.
- **Matrix Manifold++ (5.67)**: PVNN is clearly stronger.

PVNN sits above all the 6.00 hyperbolic-geometry anchors and comparable to the 7.00 anchors. Its framing weakness is real but not fatal, and the numerical stability + theoretical completeness + ablations make it a solid paper.

---

## Summary
This paper introduces Proper Velocity Neural Networks (PVNNs), using the Proper Velocity (PV) model of hyperbolic space — an unconstrained representation from special relativity — as an alternative to the Poincaré ball and hyperboloid models. The authors derive the complete Riemannian toolkit for PV space via an isometry with the Poincaré ball, build fundamental neural network layers (MLR, FC, convolution, activation, GyroBN), and evaluate on numerical stability, image classification, graph node classification, and genomic sequence learning.

## Strengths
- **Complete Riemannian toolkit for PV space (Theorems 4.2–4.4):** The paper derives closed-form exponential map, logarithmic map, parallel transport, and geodesic distance for PV space, grounded in a rigorous Riemannian isometry proof to the Poincaré ball (Theorem 4.2). This had been previously unexplored despite the model's known algebraic (gyrovector) properties from Ungar (2022).
- **Clear numerical stability advantages over Poincaré and hyperboloid models (Tables 1–3):** PV yields zero failure rates for scalar gyromultiplication up to r=1000 in FP32 (Table 1), round-trip log-exp errors three orders of magnitude smaller than Poincaré in FP32 (2.1×10⁻⁷ vs 2.1×10⁻⁴, Table 2), and stable gradient magnitudes without vanishing or exploding (Table 3). These are controlled quantitative experiments directly supporting the core motivation.
- **Efficient PV MLR parameterization (Theorem 5.2, Eq. 19):** By parameterizing hyperplane anchors via Exp₀ and PT, the PV MLR score reduces to inner products ⟨x, zₖ⟩, enabling matrix-multiplication rather than per-class gyroaddition that would produce O(b×C×n) intermediate tensors.
- **Principled PV GyroBN with theoretical guarantees (Theorem 5.4):** The homogeneity proofs (Eqs. 26–27) guarantee that centering–scaling–biasing correctly normalizes batch statistics, going beyond prior heuristic Riemannian normalization approaches.
- **Practical simplifications from unconstrained representation:** PV concatenation coincides with Euclidean concatenation (Section 5.3), enabling straightforward convolution; direct PV-space activations avoid expensive exp/log maps; both PV MLR and FC layers recover Euclidean counterparts as K→0⁻.
- **Thorough ablation studies (Tables 6–9):** Systematic ablations of tangent-space vs. Riemannian FC, tangent BN vs. GyroBN, Fréchet iteration counts, Exp₀ lifting vs. direct input, and activation strategies provide actionable guidance on design choices.
- **Consistent empirical gains on strongly hyperbolic tasks:** PVNN improves over the strongest baseline on Airport by 5.86% (Table 5, comparing to KNN), and PVCNN shows substantial gains on all TEB genomic tasks (Table 10), especially ~9 MCC points on SINEs.

## Weaknesses

### Fatal
None

### Major
- **Framing conflates numerical stability with accuracy improvements.** The abstract claims PVNNs demonstrate "the stability and effectiveness" as though these flow from the same source. However, Theorem 4.2 establishes that PV and Poincaré are Riemannially isometric — they have identical representational capacity, geodesic structure, and expressiveness. Any accuracy differences cannot stem from the geometry itself but must arise from numerical/optimization effects of the coordinate representation. The paper never addresses this tension, consistently framing accuracy gains as though they follow from the geometry. This invites the criticism that PV is "just a reparameterization" and weakens the narrative. The authors should explicitly explain why an isometric space can yield different empirical results (optimization landscape, Jacobian conditioning, parameterization efficiency).

### Minor
- **Large unexplained performance gap on Airport graph learning.** In Table 5, PVNN achieves 97.96% on Airport vs. 88.40% for HNN++ (Poincaré) — a ~9.5 percentage point gap. On Disease and PubMed the gaps are only ~0.6 and ~0.65 points. Given the isometry, this dramatic discrepancy demands explanation. Without analysis (e.g., optimization trajectories, effective learning rates, interaction between parameterization and dataset characteristics), the reader cannot distinguish a genuine advantage from a confound. The paper acknowledges PV is more effective on strongly hyperbolic data, but this doesn't explain why the gap is so large specifically on Airport (δ=1) vs. Disease (δ=0, even more hyperbolic).
- **Implicit sinh nonlinearity in PV FC layer not discussed.** Theorem 5.3 (Eq. 22) shows y_k = (1/√(-K)) sinh(√(-K) v_k(x)), introducing a curvature-dependent nonlinearity before any activation. The paper does not analyze how this interacts with downstream activations, and it means PV FC is not a direct analogue of Euclidean FC. This is an important architectural choice that deserves explicit discussion.

### Trivial
- **No curvature sensitivity analysis.** All experiments use fixed K=-1 (or a single shared curvature for genomics). If PV is less sensitive to curvature tuning than the Poincaré ball, that would be a meaningful advantage to demonstrate.
- **No wall-clock training time comparison to baselines.** Table 7 reports time for different Fréchet mean computation methods, but total training time comparison between PVNN and Poincaré/Hyperboloid baselines is absent. Given practical advantage claims, wall-clock comparisons would be informative.

## Nice-to-Haves
- An experiment isolating the coordinate-change effect from the specific layer design choices (e.g., Poincaré layers implemented via PV-to-Poincaré maps and back) would clarify what is gained by the PV representation vs. specific implementation choices.
- Deeper analysis of the Airport outlier would turn a suspicious result into a compelling finding.

## Removed Points
These points are flagged to be removed, treat them with caution.
- None needed; all criticisms were verified against the paper text.

## Novel Insights
The paper's genuinely novel contribution is bringing the Proper Velocity model — well-known in special relativity but unexplored in machine learning — into the deep learning toolkit. The rigorous proof that PV and Poincaré are not merely algebraically isomorphic (gyrovector isomorphism, known from Ungar 2022) but Riemannially isometric (Theorem 4.2) is a clean mathematical result that enables direct transfer of all Riemannian tools. The practical insight that unconstrained representations eliminate boundary numerical issues while recovering Euclidean operations in the zero-curvature limit is well-supported and provides a coherent design rationale.

## Suggestions
- Add a discussion section explicitly addressing why an isometric space can yield different empirical results (optimization landscape, Jacobian conditioning of the coordinate map, parameterization efficiency).
- Provide deeper analysis of the Airport outlier to strengthen the most striking result.
- Add a curvature sensitivity ablation to demonstrate generality.
- Discuss the implicit sinh nonlinearity in the PV FC layer and its interaction with activations.

## Calibration Report

**Anchors retrieved:**

| Round | Paper | Avg Score | Path | Comparison |
|-------|-------|-----------|------|------------|
| 1 | H2GNN (Knowledge Hypergraph) | 3.00 | q6WtaLj8O1 | Weaker: rejected, no Riemannian toolkit, limited contribution |
| 1 | HVT (Vision Transformer non-Euclidean) | 3.40 | b2FFWnwZxl | Weaker: rejected, less rigorous mathematical framework |
| 1 | PDE solver hyperbolic | 2.50 | HDmmwwTIlf | Weaker: entirely different domain, rejected |
| 1 | Hyperdimensional Computing | 3.00 | NYPJz0CL5X | Weaker: unrelated topic, rejected |
| 1 | HCNN (Fully Hyperbolic CNN) | 6.00 | ekz1hN5QNh | PVNN stronger: more complete toolkit, better ablations, stronger stability evidence |
| 1 | Symmetric Spaces NN | 6.00 | bwOndfohRK | PVNN stronger: comparable theory, much stronger experiments |
| 1 | Riemannian Hyperbolic Prototypical | 4.25 | jzneu6AO2x | PVNN stronger: rejected paper, narrower contribution |
| 1 | CHNNet | 3.75 | CBGdLyJXBW | PVNN stronger: unrelated, rejected |
| 1 | Conformal Isometry Grid Cells | 8.00 | Xo0Q1N7CGk | PVNN weaker: very strong accepted paper, different topic |
| 1 | Compositional Entailment | 8.00 | 3i13Gev2hV | PVNN weaker: very impactful VL contribution |
| 1 | Deep Orthogonal Hypersphere | 8.00 | cJs4oE4m9Q | PVNN weaker: strong anomaly detection paper |
| 1 | Holder Stability GNN | 8.00 | P7KIGdgW8S | PVNN weaker: strong theoretical GNN paper |
| 2 | Symmetric Spaces NN | 6.00 | bwOndfohRK | Same as round 1 |
| 2 | HCNN | 6.00 | ekz1hN5QNh | Same as round 1 |
| 2 | Matrix Manifold NN++ | 5.67 | 30aSE3FB3L | PVNN stronger: better theory, experiments, and presentation |
| 2 | Fast Hyperboloid DT | 6.60 | TTonmgTT9X | PVNN comparable/slightly stronger: more complete contribution |
| 2 | Conformal Isometry | 8.00 | Xo0Q1N7CGk | Same as round 1 |
| 2 | Associative Memory | 6.67 | mkNVPGpEPm | Different topic, comparable contribution quality |
| 2 | Local Loss Optimization | 7.00 | g6syfIrVuS | Comparable: solid theory + empirical contribution |
| 2 | Task Structure & Nonlinearity | 6.75 | k9t8dQ30kU | Different topic, comparable quality |

**Bracketing:** Round 1 placed the paper in the 5.5–8.0 range, clearly above the weak/rejected anchors and below the strong 8.0 anchors. Round 2 narrowed this to 6.5–7.5, as the paper is clearly stronger than the 6.00 HCNN and Symmetric Spaces papers (both accepted at ICLR) but below the 8.00 papers.

**Final positioning:** PVNN sits above all the 6.00–6.60 hyperbolic-geometry anchors due to its more complete Riemannian toolkit, stronger numerical stability evidence, and more thorough ablations. It is comparable to the 7.00 anchors in contribution quality. The framing weakness (isometry tension) is the main factor preventing a higher score. **Final score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>