Now I have sufficient calibration data. Let me compile the final review.

## Summary

This paper introduces Proper Velocity Neural Networks (PVNNs), developing the complete Riemannian toolkit (exponential/log maps, parallel transport, geodesic distance) for the Proper Velocity model of hyperbolic space — an unconstrained representation that avoids boundary issues of the Poincaré ball and hyperboloid models. It then builds fundamental neural network layers (MLR, FC, convolution, activation, batch normalization) on this geometry and evaluates them across four tasks: numerical stability, image classification, graph node classification, and genomic sequence learning. PV consistently matches or outperforms strong baselines, with particularly strong gains in genomic sequence learning (5–9 MCC points over hyperboloid HCNNs) and on strongly hyperbolic graphs.

## Strengths

1. **First complete Riemannian toolkit for the PV model (Theorem 4.3, Section 4.2).** The paper derives closed-form expressions for exponential map, logarithmic map, parallel transport, and geodesic distance on PV space, establishing a geometric foundation that was previously absent despite the PV model's known gyrovector algebra. This is a prerequisite for building neural networks in this model and is a genuine contribution to the geometric deep learning toolbox.

2. **Demonstrated numerical stability advantage (Tables 1–3, Section 6.1).** PV shows zero failure rate for gyromultiplication up to \(r=1000\) in FP32, while the hyperboloid model fails at \(r=20\). The round-trip error \(\|\mathrm{Log}_0(\mathrm{Exp}_0(v))-v\|\) for large tangent vectors is \(2.1\times10^{-7}\) (FP32) versus \(2.1\times10^{-4}\) (Poincaré) and \(1.0\times10^0\) (hyperboloid). This directly supports the practical claim that PV's unconstrained representation alleviates numerical instabilities.

3. **Efficient MLR formulation avoiding per-class gyroaddition (Theorem 5.2).** The PV MLR score is expressed using inner products \(\langle x, z_k\rangle\) computable via matrix multiplication, avoiding the \(b \times C \times n\) intermediate tensor that explicit gyroaddition would require. This is a concrete computational advantage specific to the PV derivation.

4. **Strong results on genomic sequence learning (Table 10, Section 6.4).** PVCNN outperforms hyperboloid HCNN-S on all five TEB datasets by substantial margins (e.g., SINEs: 93.78 vs 85.45 MCC; LINEs: 81.83 vs 76.12). These gains are far larger than typical hyperbolic-vs-Euclidean improvements in vision, providing compelling evidence of practical utility for this real-world application.

5. **Comprehensive ablation study separating design choices (Tables 6–9).** The paper systematically compares PV FC vs tangent-space FC, GyroBN vs tangent BN, Fréchet vs efficient batch statistics, different activation strategies, and with/without exponential map lifting — across four graph datasets. For example, on Airport, PV FC (97.93) substantially outperforms tangent FC (86.99), isolating the benefit of the Riemannian PV design.

6. **Theoretical guarantees for batch normalization (Theorem 5.4).** The paper proves that under gyroaddition the Fréchet mean satisfies \(\mathrm{FM}(\{\beta \oplus_U x_i\}) = \beta \oplus_U \mathrm{FM}(\{x_i\})\) and that scaling by \(t\) scales dispersion from zero by \(t^2\), providing principled justification for PV GyroBN.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Gradient comparison is coordinate-dependent, not an intrinsic geometric comparison (Table 3, Section 6.1).** The function \(f_r(x) = \|r \otimes_{\mathcal{H}} x - x\|\) uses different gyromultiplication operations for PV, Poincaré, and hyperboloid, and gradient magnitudes are measured in ambient Euclidean coordinates. These are not invariant under the isometry relating the models. The practical claim that PV avoids vanishing/exploding gradients in its coordinate parameterization is valid and useful for implementations, but the paper would benefit from making the framing more precise — this demonstrates a numerical advantage of the PV *parameterization*, not a fundamental geometric advantage of PV over the Poincaré ball (which is isometric to it).

2. **Several accuracy improvements lack statistical significance assessment (Tables 4, 5).** In image classification (Table 4), improvements over baselines are small (e.g., +0.2% on CIFAR-100) and often within one standard deviation. On the graph tasks (Table 5), PVNN's gain on PubMed (+0.65% over HNN++) is also modest. The paper reports standard deviations but does not indicate which differences are statistically significant. Given the overlapping error bars on multiple entries, some of the claimed improvements may not be robust. A note on statistical testing or confidence intervals would strengthen the empirical claims.

3. **PVNN underperforms on the weakly hyperbolic Cora dataset (Table 5, Section 6.3).** While the paper notes that Cora is less hyperbolic (\(\delta=11\)), it does not offer analysis or speculation about *why* PV is worse than the hyperboloid-based LNN (51.42 vs 53.34) on this dataset, or whether the unconstrained space may overfit nearly Euclidean data. A brief discussion would help readers understand the practical regimes where PV should (and should not) be preferred.

4. **The "Fréchet ∞" label in Table 7 is ambiguous.** This row likely means full convergence of the iterative Fréchet mean solver, but the notation is not defined in the caption. A brief clarification would aid reproducibility.

5. **No discussion of curvature sensitivity.** All experiments fix \(K=-1\). While this is standard practice in hyperbolic deep learning, a brief note or small ablation on curvature sensitivity would strengthen the robustness argument, especially since curvature is a key parameter in hyperbolic models.

### Trivial

- None beyond the minor issues above.

## Nice-to-Haves

- **Complexity/runtime analysis.** The PV MLR avoids per-class gyroaddition, and the paper mentions this computational advantage qualitatively. A brief FLOPs comparison or wall-clock time comparison against Poincaré and hyperboloid baselines (especially for the MLR layer) would strengthen the computational argument.
- **Memory discussion.** The paper notes that naïve gyroaddition "could cause out-of-memory errors" (Section 5.1) but does not quantify the savings. A brief note on memory usage for typical batch sizes and dimensions would be helpful.
- **Convert-Poincaré-to-PV baseline.** Since PV and Poincaré are isometric, one could convert a trained Poincaré network to PV (by mapping data, parameters, and operations) and verify identical performance. Showing this would clarify that PV's advantage is numerical stability during training rather than fundamentally different model capacity. This is an interesting conceptual experiment, not a requirement.

## Removed Points

- **Criticism about Poincaré ball showing zero failure rate (Harsh Critic's "numerical stability" framing point).** The paper explicitly reports in Table 1 and Section 6.1 that the Poincaré ball has zero failure and violation rates. The intro's claim that constrained spaces "can lead to numerical instabilities" is appropriately qualified ("potentially," "can lead to"). The paper is transparent about what the evidence shows.
- **Criticism about missing related works.** Excluded per policy (no external sources to verify).
- **Criticism about format and presentation artifacts.** These are parser issues, not author errors.
- **Strength about "isometric mapping between PV and Poincaré ball" being a core strength.** This is a tool used to derive operators rather than a standalone contribution. The paper's own Theorem 4.2 is correctly presented as a means to an end. Removed to avoid inflating the strength count with derivative claims.

## Novel Insights

The human reviews collectively surface an important tension: PV's practical advantages come *despite* being isometric to the Poincaré ball. The isometry means PV and the Poincaré ball describe exactly the same geometric space — the difference is purely in coordinate representation. Yet this representational difference yields substantial numerical benefits: PV avoids the vanishing gradients that plague Poincaré models near the boundary, and its unconstrained nature eliminates the off-manifold violations of the hyperboloid model. The genomic sequence learning results (Table 10) are particularly striking because the gains over hyperboloid HCNN-S are large (5–9 MCC points) and consistent across five datasets, suggesting that numerical stability during training translates into meaningfully different learning outcomes even though the geometry is nominally equivalent. This positions PV not as a theoretically different geometry, but as a *practically better parameterization* of hyperbolic space — a perspective that future work on hyperbolic deep learning should take seriously.

## Suggestions

1. Add statistical significance indicators (confidence intervals or p-values) to the main results tables (Tables 4, 5).
2. Explicitly reframe the gradient comparison (Table 3) as a coordinate/parameterization advantage rather than an intrinsic geometric advantage.
3. Add a brief discussion of why PV underperforms on Cora relative to the hyperboloid model.
4. Clarify the "Fréchet ∞" notation in Table 7's caption.
5. Add a short note on computational complexity of the efficient MLR formulation (Section 5.1) — a simple FLOPs comparison with the naïve gyroaddition approach would suffice.

## Score and Decision

**Bracket (Round 1):** The paper sits between the weak anchors at ~3 (rejected papers with fundamental issues) and the strong anchors at 8 (clearly excellent papers). The closest topical anchor is "Fully Hyperbolic Convolutional Neural Networks for Computer Vision" (6.00), which is a similar contribution — developing full hyperbolic neural network layers for the Lorentz model. The PVNN paper is stronger in experimental breadth (4 tasks vs primarily vision), ablation depth, and the magnitude of gains on the genomic task.

**Narrowing (Round 2):** Comparing against the HCNN anchor (6.00), the "Fast Hyperboloid Decision Tree" anchor (6.60), and the "Shadow Cones" anchor (6.33), the PVNN paper is:
- Stronger than the 6.00 HCNN paper (more comprehensive evaluation, stronger gains on real tasks, better ablations, clearer numerical stability story)
- Comparable to the 6.60 HyperDT paper (both make solid practical contributions with thorough evaluation, though HyperDT has the advantage of faster execution while PVNN has broader task coverage)
- Stronger than the Shadow Cones paper at 6.33 (more tasks, more convincing evidence)

The paper's core limitation — that PV is isometric to the Poincaré ball, meaning the main advantage is numerical/representational rather than geometric — prevents it from scoring at the 7.5+ level. However, the systematic development of the Riemannian toolkit, the efficient MLR formulation, the strong genomic results, and the thorough ablations place it clearly above the 6.00 anchor. 

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>