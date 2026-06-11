Now I have a clear picture. Let me finalize the calibration and write the review.

**Final calibration synthesis:**

| Anchor | Score | Decision | Comparison to our paper |
|--------|-------|----------|------------------------|
| WOopKWDWtS | 4.40 | Reject | Our paper is clearly stronger — better theory, experiments, motivation |
| bwOndfohRK | 6.00 | Accept | Unified framework, strong theory but presentation issues. Our paper is more focused but more thorough empirically. Comparable-to-stronger. |
| ekz1hN5QNh | 6.00 | Accept | Most similar anchor (fully hyperbolic CNNs). Our paper has broader experiments, more thorough ablations, clearer theory. Clearly stronger. |
| YcaFqY8LWD | 6.25 | Reject | Gyro framework for attention. Rejected due to presentation and motivation issues despite 6.25. Our paper is cleaner and better-motivated. Slightly stronger. |
| TTonmgTT9X | 6.60 | Accept | Clean, innovative contribution. Our paper is somewhat weaker — less focused, less elegant. |
| 7PLpiVdnUC | 6.50 | Accept | Different domain (Lie algebra/PDEs). Comparable score range. |
| 3i13Gev2hV | 8.00 | Accept | Far stronger — highly innovative compositional VL. Our paper doesn't approach this level. |

**Round 1 Bracket: 5.5–7.0 → narrowed to 6.0–6.5 based on Round 2.**

The paper is clearly stronger than the 6.00 accepted anchors (ekz1hN5QNh, bwOndfohRK), comparable to or slightly stronger than the 6.25 rejected anchor (YcaFqY8LWD), and clearly weaker than the 6.60+ anchors. **Final score: 6.5.** This is a solid accept — rigorous theory, comprehensive experiments, genuine empirical gains — held back from 7+ by marginal CIFAR gains and an incomplete discussion of the isometry–performance relationship.

---

## Summary
This paper introduces Proper Velocity Neural Networks (PVNNs), adopting the unconstrained PV model of hyperbolic geometry as a stable alternative to the constrained Poincaré ball and hyperboloid models. The authors prove that the known gyro-isomorphism between PV and Poincaré spaces is a Riemannian isometry (Theorem 4.2), derive the complete Riemannian toolkit by pullback, and build a suite of neural layers (MLR, FC, convolution, activation, GyroBN). Experiments across numerical stability, image classification, graph node classification, and genomic sequence learning demonstrate PVNN's stability advantages and competitive or superior empirical performance compared to strong hyperbolic baselines.

## Strengths
- **Complete Riemannian toolkit via isometry (Theorems 4.2, 4.3):** The proof that the PV–Poincaré gyro-isomorphism is a Riemannian isometry (Theorem 4.2) is the pivotal theoretical result. It enables closed-form Riemannian operators (Exp, Log, parallel transport, geodesic distance) to be obtained by pullback rather than ground-up derivation. Lemma 4.1 (differentials of the isometry maps) is non-trivial and correctly derived. Theorem 4.4 further unifies gyrovector and Riemannian perspectives.
- **Compelling numerical stability evidence, especially gradient behavior (Tables 1–3):** Table 1 shows PV maintains 0% failure under scalar gyromultiplication up to r=1000 (FP32) while the hyperboloid completely collapses starting at r=20. Table 2 shows PV's round-trip Log∘Exp error is 2.1×10⁻⁷ in FP32 — three orders better than Poincaré (2.1×10⁻⁴). Most importantly, Table 3 demonstrates PV gradients remain in a stable, non-vanishing band [1.1×10⁻⁴, 2.1×10⁻⁶] versus Poincaré's vanishing gradients (~10⁻¹¹–10⁻¹³) and hyperboloid's NaN explosions. This three-pronged analysis directly validates the paper's core thesis.
- **Strong downstream performance on hyperbolic-structured data (Tables 5, 10):** On graph node classification, PVNN achieves best accuracy on all three strongly hyperbolic datasets, with a 5.86-point gain on Airport over the strongest baseline (97.96% vs. 92.10%). On genomic sequence learning, PVCNN outperforms Euclidean CNN and hyperboloid HCNN-S on all five TEB tasks, with gains up to ~9 MCC points on SINEs. This breadth across graph learning and genomics demonstrates practical value.
- **Memory-efficient MLR parameterization (Theorem 5.2, Eq. 19):** The reformulation from gyroaddition-based MLR (requiring b×C×n intermediate tensors that risk out-of-memory errors) to a pure inner-product form ⟨x, zₖ⟩ is a practical contribution that recovers Euclidean MLR in the K→0⁻ limit, confirming theoretical continuity.
- **GyroBN with theoretical homogeneity guarantees (Theorem 5.4):** Unlike many Riemannian normalization methods that lack guarantees, PV GyroBN is backed by explicit homogeneity theorems: after centering the Fréchet mean shifts to the origin, after biasing to β, and after scaling the variance becomes s². This is non-trivial for a non-Euclidean space.
- **Thorough ablation studies (Tables 6–9):** The paper systematically ablates tangent vs. Riemannian FC, batch statistics computation methods (tangent, Euclidean, Fréchet with varying iterations), embedding strategies (with/without Exp₀), and activation types. These ablations provide convincing evidence that Riemannian PV constructions are genuinely beneficial, especially on strongly hyperbolic graphs.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Isometry–performance connection not explicitly discussed:** Theorem 4.2 proves PV and Poincaré ball are the same Riemannian manifold, yet PVNN consistently outperforms Poincaré networks. The paper's core argument (unconstrained coordinates → better numerical stability → better optimization) is present throughout but never stated as an explicit bridge between the isometry result and the empirical results. A dedicated paragraph connecting these dots would strengthen the paper's internal coherence and preempt reader questions. This does not undermine the paper's claims — the numerical stability evidence in Section 6.1 provides the mechanism — but the paper would benefit from making the connection explicit.
- **CIFAR gains are within overlapping standard deviations:** The improvements on CIFAR-10 (+0.18% over best baseline) and CIFAR-100 (+0.24%) are marginal and fall within overlapping error bars. Additionally, the experiment only replaces the final MLR classification head (the backbone is Euclidean ResNet-18), which limits what can be concluded about PV geometry in vision tasks. The graph learning and genomics results carry much more weight.
- **Airport result is a standout outlier without investigation:** PVNN achieves 97.96% on Airport versus 88.40% for HNN++ — a 9.56 percentage-point gap that dwarfs all other comparisons. The paper notes Airport is strongly hyperbolic (δ=1) but provides no further analysis of why this dataset in particular benefits so dramatically. A brief investigation would turn this from an unexplained outlier into an illuminating case study.

### Trivial
None.

## Nice-to-Haves
- A curvature sweep (e.g., K ∈ {−0.1, −0.5, −1, −2, −5}) on at least the graph learning tasks would address whether the fixed K=−1 choice interacts with model comparisons.
- Including a Poincaré-based convolutional baseline in the genomics experiment (currently only Euclidean CNN and hyperboloid HCNN-S) would help distinguish PV-specific benefits from hyperbolic-geometry benefits in general.
- Reporting computational cost (FLOPs or wall-clock time) of PV operations relative to Poincaré and hyperboloid would help practitioners assess the practical trade-off.
- The gradient stability experiment (Table 3) tests an isolated synthetic operator; extending it to track gradient statistics during actual network training would connect the synthetic probe to practical training dynamics.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *"The paper never discusses the isometry paradox" (Harsh Critic):* The paper's entire thesis — unconstrained PV → better numerical stability → better optimization — is the explanation. It is stated in the abstract (line 8-9: "their constrained nature potentially leads to numerical instabilities"), introduction (lines 13-15), and validated in Section 6.1. The paper does discuss it; only an explicit connecting paragraph is missing. Demoted from "fatal/structural" to Minor.
- *"Numerical stability argument is overstated" (Harsh Critic):* The paper accurately reports Poincaré's 0% failure on gyro ops (line 237) and uses "potentially" as a qualifier in the abstract. The gradient vanishing evidence (Table 3) is a genuine and significant difference. Demoted to Minor as a framing precision issue.
- *"Missing hyperparameter tuning discussion" (Harsh Critic):* Appendix C likely contains these details; parser strips appendices. Removed per hard rules.
- *"Curvature treated as constant is a methodological gap" (Harsh Critic):* Most hyperbolic papers fix curvature at K=−1. Moved to Nice-to-Haves as a standard limitation, not a gap.

## Novel Insights
The paper's key practical insight — that switching to an unconstrained coordinate representation of hyperbolic space (PV) preserves all geometric properties (via isometry) while improving optimization dynamics — is genuinely useful. The gradient analysis (Table 3) provides concrete, quantitative evidence: Poincaré gradients collapse to ~10⁻¹¹–10⁻¹³ near the boundary while PV gradients remain in a healthy 10⁻⁴–10⁻⁶ band. This quantifies a problem that many practitioners have likely observed anecdotally and provides a principled reason to prefer PV coordinates for hyperbolic deep learning. The isometry proof itself (Theorem 4.2) also bridges the algebraic gyrovector literature (Ungar) with Riemannian geometry in a way that hadn't been formalized before.

## Suggestions
- Add a paragraph in Section 4.2 or early in Section 6 explicitly stating: "Although PV and Poincaré are isometric (same representational capacity), the unconstrained PV parameterization yields better-conditioned optimization because parameters are unconstrained Euclidean vectors, gradients don't vanish near any boundary, and the coordinate representation avoids numerical pathologies when embeddings approach the Poincaré boundary during training."
- Investigate the Airport result: a brief analysis comparing PVNN and HNN++ embedding norms, gradient statistics, or learned decision boundaries on Airport would turn this standout result into an informative case study.
- Consider a small curvature ablation (even just K ∈ {−0.5, −1, −2}) on graph learning to demonstrate robustness to curvature choice.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>