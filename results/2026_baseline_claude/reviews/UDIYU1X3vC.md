## Summary

This paper introduces Proper Velocity Neural Networks (PVNNs), which exploit the Proper Velocity (PV) model of hyperbolic geometry as a numerically stable alternative to the Poincaré ball and hyperboloid models. The authors first establish that PV space is Riemannian isometric to the Poincaré ball, then derive closed-form expressions for all key Riemannian operators (exponential/logarithmic maps, parallel transport, geodesic distance). Building on this toolkit, they construct core neural layers — MLR, fully connected, convolutional, activation, and batch normalization — and validate the framework on four tasks: numerical stability tests, image classification, graph node classification, and genomic sequence learning.

---

## Strengths

- **First systematic treatment of PV for ML**: To the authors' knowledge, the PV manifold has not been studied for deep learning. The isometry derivation (Thm. 4.2) is clean and provides a principled pathway from the well-understood Poincaré toolkit to PV operators, giving the paper both mathematical novelty and practical utility.

- **Rigorous and complete geometric toolkit**: The derivations of closed-form exponential/logarithmic maps, parallel transport, and geodesic distance in PV space (Thm. 4.3) are technically solid. Thm. 4.4 — showing gyro operations can be expressed purely via Riemannian operations — is an elegant unification of the algebraic and geometric views.

- **Well-motivated and quantified numerical stability**: Tables 1–3 provide concrete evidence of instability in the hyperboloid model (100% violation rate at r=20; round-trip error of 1.0 in both FP32/FP64) and Poincaré ball (vanishing gradients), while PV remains stable. The comparison methodology is reproducible and fair.

- **Efficient MLR parameterization** (Thm. 5.2): The reparameterization that replaces per-class gyroaddition with inner products (matrix multiplication) is practically important. It eliminates an O(b × C × n) intermediate tensor and directly resolves memory and speed concerns that would otherwise hinder large-scale use.

- **Broad experimental validation with ablations**: Four qualitatively different tasks are evaluated, and the paper provides ablations on activations, lifting choices, normalization statistics, and Riemannian vs. tangent-space layers. On strongly hyperbolic graphs (Disease, Airport, PubMed) and genomic sequences, PVNNs consistently improve over hyperboloid and Poincaré baselines.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unresolved tension between isometry and empirical gains.** Theorem 4.2 shows PV is Riemannian isometric to the Poincaré ball, meaning any PVNN corresponds to an equivalent Poincaré ball network with identical representational capacity. Therefore the observed accuracy improvements can only arise from numerical stability (better optimization, fewer NaN/explosion events) rather than expanded expressiveness. The paper never explicitly attributes the performance gap to this mechanism, nor does it show training curves or loss landscapes demonstrating that Poincaré ball training actually degrades due to numerical issues on the test datasets. Without this link, the claim that PVNNs are *better* rather than merely more stable is not fully established.

2. **Inconsistencies between ablation tables (Tables 5, 6, 7) for Cora.** PVNN on Cora in Table 5 is 51.42 ± 1.33, while in Table 6 (the FC/BN ablation table) the corresponding PVNN row shows 52.26 ± 1.32. More strikingly, Table 7 (batch statistics ablation) reports GyroBN with Fréchet 10 iterations achieving only 46.64 ± 5.45, far below the Table 5 result. These discrepancies are not explained and cast doubt on the reliability of experimental setup control across ablations.

3. **Gradient stability test is synthetic.** The gradient experiment measures ∥∇ₓ f_r(x)∥ for f_r(x) = ∥r ⊗_H x − x∥, an artificial scalar function. While suggestive, this does not demonstrate that gradients flowing through an actual loss function during training are more stable with PV. An experiment showing training stability (e.g., gradient norms over epochs, or training success rates across seeds) in a real network would much more strongly support the core claim.

### Minor

1. **Table 3 gradient range notation is ambiguous.** For both Poincaré and PV, the listed range has its first entry larger than the second (e.g., PV: [1.1 × 10⁻⁴, 2.1 × 10⁻⁶]), which inverts the usual [min, max] convention. This appears to list [gradient at r=1, gradient at r=1000], i.e., as r grows gradients decrease. The table should clarify what the two values represent.

2. **PVNN underperforms on weakly hyperbolic Cora.** The paper attributes this to Cora's high δ-hyperbolicity (δ = 11), but offers no mechanism-level explanation for why PV geometry is specifically ill-suited here, nor any strategy to mitigate this degradation.

3. **Tangent and Euclidean GyroBN variants perform poorly on Cora** (33.10 and 32.62 in Table 7), a performance collapse that is much larger than their difference from Fréchet-based GyroBN on other datasets. This is not discussed and is surprising.

### Trivial

- The gyro operator stability test (Table 1) shows the Poincaré ball has zero failure and zero violation rates for all radii tested. The instability of the Poincaré ball is thus not from gyro operations per se but from boundary effects during gradient-based learning — this distinction would improve clarity in Sec. 6.1.

---

## Nice-to-Haves

- Training curves or convergence plots comparing PV, Poincaré, and hyperboloid would strengthen the connection between the demonstrated numerical stability and the empirical performance improvements.
- A discussion of how the curvature parameter K affects PV stability relative to existing models, since K enters the metric non-trivially via β_x.
- For the Cora/weakly-hyperbolic regime, analysis of when the isometry-induced equivalence with Poincaré ball predicts identical results vs. when numerical differences matter would be theoretically informative.

---

## Novel Insights

The central insight is that working in an unconstrained ambient space (ℝⁿ with a modified metric) resolves the boundary-proximity instabilities of the Poincaré ball and the constraint-drift failures of the hyperboloid, while the Riemannian isometry to the Poincaré ball guarantees that no representational capacity is sacrificed. Theorem 4.4 — that PV gyroaddition and scalar gyromultiplication decompose exactly into sequences of standard Riemannian operations (exponential map, parallel transport, logarithmic map) — is a structurally clean result not previously established, and it clarifies the algebraic–geometric correspondence in a way that facilitates rigorous neural layer design. The unconstrained domain also enables a simplification (direct Euclidean activation in PV space) that skips costly exp/log wrapping while retaining competitive accuracy, a practical insight that could benefit other hyperbolic architectures.

---

## Suggestions

1. Add training-time gradient norm plots (or success rate under repeated random seeds) for a real classification network to substantiate the claim that numerical stability translates to better practical training.
2. Explicitly state after Theorem 4.2 what the isometry implies for expressiveness — that PVNNs and Poincaré ball NNs are representationally equivalent — and then clearly frame the contribution as numerical/computational rather than representational. This would preempt reviewer confusion and set accurate expectations.
3. Clarify the experimental setup differences across Tables 5, 6, and 7 (e.g., whether GyroBN is used in Table 5's PVNN, which iteration count, whether Table 6 and 7 use the same random seeds).
4. Fix the notation in Table 3 to unambiguously state what the two values in the range represent (e.g., "gradient at r=1" and "gradient at r=1000").

---

## Score and Decision

The paper makes a genuine and timely contribution: PV is a natural and previously neglected model of hyperbolic geometry that resolves concrete numerical problems of existing models, backed by rigorous mathematics and broad experimental evidence. The main limitation — that the performance advantages of PVNNs stem from numerical stability rather than new representational power (which follows directly from the isometry) — is real but does not undermine the practical value of the approach, analogous to the adoption of the hyperboloid model over the Poincaré ball for its numerical properties. The inconsistencies across ablation tables are a meaningful concern that should be addressed in revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>