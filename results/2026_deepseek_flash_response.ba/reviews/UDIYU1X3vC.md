Here is the final consolidated review:

---

## Summary

This paper introduces Proper Velocity Neural Networks (PVNNs), which use the Proper Velocity (PV) space — an unconstrained representation of hyperbolic geometry — as the foundation for building hyperbolic neural networks. The authors derive the complete Riemannian toolkit (exponential/logarithmic maps, parallel transport, geodesic distance) for PV space, prove it is isometric to the Poincaré ball, and construct neural network layers (MLR, FC, convolution, activation, batch normalization) in this space. Experiments across numerical stability, image classification, graph learning, and genomics show that PVNNs improve numerical stability — particularly over the hyperboloid model — and achieve competitive performance.

## Strengths

1. **Complete Riemannian toolkit for PV space**: The paper derives closed-form Exp/Log/PT operators (Theorem 4.3), geodesic distance, and establishes the isometry between PV and the Poincaré ball (Theorem 4.2). This foundational mathematical development enables PV space to be used systematically for representation learning.

2. **Efficient closed-form MLR (Theorem 5.2)**: The reparameterization avoids costly per-class gyrooperations by expressing the score function purely in terms of inner products ⟨x, z_k⟩, enabling matrix-multiplication-level efficiency. This is a practical engineering contribution that makes PV MLR scalable.

3. **Thorough ablation studies**: Tables 6–9 systematically compare Riemannian vs. tangent-space variants, different activation strategies, and batch-statistic approximations for GyroBN. This level of ablation is more detailed than many prior hyperbolic network papers and provides practical design guidance.

4. **Strong results on specific tasks**: Airport graph classification (+5.86% over strongest baseline, Table 5) and genomics (up to +9 MCC points over hyperboloid CNN, Table 10) provide concrete evidence of practical advantage in specific settings.

5. **Normalization with theoretical guarantees**: Theorem 5.4 proves homogeneity of Fréchet mean and dispersion under gyro operations, matching the guarantees of Euclidean Batch Normalization.

## Weaknesses

### Fatal
None.

### Major

1. **Numerical stability advantage over Poincaré ball is overstated**: Table 1 shows the Poincaré ball has **zero failures AND zero constraint violations** at all tested radii up to r=1000 — identical to PV. The genuine numerical advantage is against the hyperboloid model, not the Poincaré ball. The paper's framing (abstract: "constrained nature potentially leads to numerical instabilities") implicitly targets all constrained models, but the evidence only supports this for the hyperboloid. Tables 2–3 show marginal improvements over Poincaré (round-trip error 2.1×10⁻⁷ vs 2.1×10⁻⁴; gradient range [1.1×10⁻⁴, 2.1×10⁻⁶] vs [1.1×10⁻¹¹, 7.6×10⁻¹³]), but the practical significance of these differences is not demonstrated — there is no evidence that the Poincaré gradient level actually causes training problems on real tasks.

2. **Downstream task improvements over Poincaré baselines are small and not statistically assessed**: On image classification (Table 4), PV MLR improves over Unidirectional MLR by +0.18% on CIFAR-10 (95.30 vs 95.12, overlapping error bars) and +1.01% on CIFAR-100 (78.20 vs 77.19). On graph learning (Table 5), improvements over HNN++ are +0.58% on Disease and +0.65% on PubMed. No statistical significance tests are reported. The Airport result (+5.86%) and genomics results are genuine bright spots, but the overall pattern is that improvements over Poincaré are often within noise range.

### Minor

1. **Missing Euclidean baselines in two experiments**: Table 4 compares hyperbolic MLR heads on ResNet-18 but omits the standard Euclidean MLR (the default ResNet-18 classification head). Table 5 compares hyperbolic GNNs without a Euclidean GNN baseline. While the paper's scope is comparing hyperbolic models, adding these baselines would contextualize whether hyperbolic geometry itself provides benefits on these specific tasks. (The genomics experiments in Table 10 do include a Euclidean baseline.)

2. **No computational cost comparison**: The PV operators involve sinh/sinh⁻¹ computations. The paper does not report wall-clock time or throughput comparisons between PVNN and equivalent Poincaré/hyperboloid networks. Table 7 reports fitting times for different GyroBN variants but does not compare across different hyperbolic models.

3. **Curvature sensitivity unexplored**: All experiments use K=−1. Whether results are sensitive to curvature, and whether curvature was tuned per method/dataset, is not discussed.

### Trivial
None.

## Nice-to-Haves

- Adding a Poincaré-based CNN baseline in the genomics experiments would complete the picture, since the comparison is only against hyperboloid-based HCNN-S.
- A controlled experiment directly comparing PV and Poincaré networks under identical training conditions (same architecture, same hyperparameters) showing training dynamics, convergence speed, and sensitivity to hyperparameters would strengthen the case that the PV parameterization helps optimization.
- Reporting curvature sensitivity analysis.
- Including wall-clock training time comparison between PVNN and Poincaré networks.

## Removed Points

These points were considered during review but removed per filtering rules:

- "Isometry undermines novelty" — removed because this criticism applies equally to the Lorentz model vs. Poincaré ball (both are isometric). The Lorentz model is a standard accepted formulation in hyperbolic neural networks despite this fact. The isometry is openly acknowledged and used for derivations, and the contribution is about numerical/optimization convenience, which is a legitimate form of contribution.
- "Code not released" reproducibility concern — removed per policy on reproducibility nitpicks (standard "code upon acceptance" statement).
- Strength finder's generic strengths about "addressing an important problem" — removed as insufficiently specific.
- "Derivations involve dπ_x(v) which requires computing the differential at each point" as a computational concern — the paper provides the efficient reparameterization (Theorem 5.2) that avoids this overhead in practice.

## Novel Insights

None beyond the paper's own contributions. The paper's key insight — that PV space offers the same geometric structure as the Poincaré ball but in an unconstrained coordinate system that avoids certain numerical pathologies — is transparently presented and valid.

## Suggestions

1. Add a Euclidean MLR baseline to Table 4 and a Euclidean GNN baseline to Table 5 to contextualize the absolute performance of all hyperbolic methods.
2. Add reporting of wall-clock training time for PVNN vs. Poincaré networks.
3. Provide statistical significance indicators (e.g., confidence intervals via bootstrapping) for main results.
4. Calibrate the numerical stability claims: clarify that the primary advantage is over the hyperboloid model, while the advantage over Poincaré is marginal on the tested metrics.
5. Include a sensitivity analysis for curvature K across at least one task.

## Score and Decision

**Calibration Anchors Used:**

Round 1 (bracketing):
- `b2FFWnwZxl.md` (HVT, avg 3.40, Reject) — Hyperbolic vision transformer. Low scores for lack of novelty and insufficient experiments. PVNN is substantially stronger.
- `q6WtaLj8O1.md` (avg 3.00, Reject) — Fully hyperbolic knowledge hypergraph learning. PVNN stronger.
- `ekz1hN5QNh.md` (Fully Hyperbolic CNN, avg 6.00, Accept) — Lorentz model CNN layers. Very similar paper type and quality. PVNN has better ablations but weaker baseline coverage and overstated numerical claims. PVNN is slightly weaker overall.
- `bwOndfohRK.md` (Symmetric Spaces, avg 6.00, Accept) — General neural network framework on symmetric spaces. More theoretically ambitious; PVNN is more focused.
- `KmdwGYbMv0.md` (Binary Hyperbolic Embeddings, avg 4.50, Reject) — Hyperbolic embedding compression for search.
- `jzneu6AO2x.md` (Riemannian Hyperbolic Prototypical Networks, avg 4.25, Reject) — Poincaré prototype learning.

Round 2 (narrowing):
- `83le3arfeA.md` (Balanced Hyperbolic Embeddings, avg 5.50, Reject) — Hyperbolic OOD detection. PVNN has stronger theoretical contribution.
- `30aSE3FB3L.md` (Matrix Manifold NN++, avg 5.67, Accept) — SPD/Grassmann neural net layers. Similar type of contribution; PVNN is of comparable quality.
- `okYdj8Ysru.md` (Lie Group RBN, avg 5.20, Accept) — Unified BN on Lie groups. PVNN is more comprehensive (covers multiple layer types).
- `WOopKWDWtS.md` (Optimizing Curvature, avg 4.40, Reject) — Multiple scattered improvements with marginal gains. PVNN has clearer, more focused contribution.
- `IUmDBY4NOQ.md` (Geometry-aware Distance, avg 4.75, Reject) — Adaptive distances in hyperbolic space. PVNN has stronger, more rigorous theoretical presentation.

Round 1 bracket: 5.0–6.0. Round 2 narrowing: compared against the 5.2–6.0 anchors, PVNN is stronger than Lie Group RBN (5.20) and comparable to Matrix Manifold NN++ (5.67), but slightly weaker than Fully Hyperbolic CNN (6.00) due to missing Euclidean baselines and overstated numerical claims.

**Score:** This paper makes a solid theoretical contribution (Riemannian toolkit for PV space, isometry proof, efficient MLR, normalization with guarantees) with thorough empirical evaluation including ablation studies. The main weaknesses are (1) the numerical stability advantage over Poincaré is overstated — Table 1 shows Poincaré is equally stable — and (2) downstream improvements over Poincaré are small and not statistically assessed. The strong Airport and genomics results are genuine highlights. The paper would be strengthened by adding Euclidean baselines, calibrating the numerical claims, and including significance testing.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>