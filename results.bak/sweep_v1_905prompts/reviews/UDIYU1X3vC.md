Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

## Calibration Summary

**Round 1 bracket:** Between 5.0 and 7.0.

**Round 2 anchors examined:**
- "Fully Hyperbolic Convolutional Neural Networks for Computer Vision" (6.00, Accept) — Similar scope (new hyperbolic NN layers); current paper has stronger theory (novel model vs. extending Lorentz) and broader experiments.
- "Neural networks on Symmetric Spaces of Noncompact Type" (6.00, Accept) — General theoretical framework; current paper is more focused with stronger empirical results (genomics +5–9 MCC, Airport +5.86%).
- "Shadow Cones" (6.33, Accept) — Different sub-area (partial order embeddings); comparable rigor and experimental depth.
- "Matrix Manifold Neural Networks++" (5.67, Accept) — Split opinion (3,8,6); current paper has broader validation and fewer structural concerns.
- "Balanced Hyperbolic Embeddings" (5.50, Reject) — Methodology questioned by multiple reviewers; current paper's core claims are better supported.

The paper sits between the 6.0 "Fully Hyperbolic CNN" and 6.33 "Shadow Cones" anchors — comparable to the former in contribution size, slightly below the latter in presentation polish. Its theory is thorough, the empirical coverage across 4 tasks is broader than most comparable works, but some missing details (curvature reporting, runtime, limitations) prevent a higher score.

---

## Summary

This paper introduces Proper Velocity Neural Networks (PVNNs), the first systematic treatment of the Proper Velocity (PV) model of hyperbolic space for deep learning. The PV model is an unconstrained representation of hyperbolic geometry, rooted in special relativity, that avoids the numerical boundary instabilities of the popular Poincaré ball and hyperboloid models. The paper (1) derives the complete Riemannian toolkit (exponential map, logarithmic map, parallel transport, geodesic distance) for PV space via isometries with the Poincaré ball; (2) develops core neural network layers (MLR, FC, convolution, activation, batch normalization) in PV space with efficient closed forms; and (3) validates the framework across four tasks: numerical stability, image classification, graph node classification, and genomic sequence learning. Results show that PVNNs match or outperform strong hyperbolic baselines, with particularly large gains on genomic sequence learning (+5–9 MCC points) and strongly hyperbolic graphs (+5.86% on Airport).

## Strengths

- **First complete Riemannian toolkit for PV space.** Theorem 4.3 provides closed-form expressions for Exp, Log, parallel transport, and geodesic distance on the PV manifold, derived elegantly via isometries with the Poincaré ball. Prior work covered only gyrovector algebra; this paper fills the gap needed for neural network construction.

- **Efficient, principled layer formulations.** The PV MLR (Theorem 5.2) reformulates the score function using only Euclidean inner products ⟨x, z_k⟩, avoiding the O(C·n) per-class gyroaddition required by prior hyperbolic MLRs. The PV FC layer (Theorem 5.3) likewise admits a closed form. This is a concrete practical advance for scaling hyperbolic networks.

- **Strong empirical validation on genomics and graphs.** On five TEB genomic tasks (Table 10), PVCNN outperforms HCNN-S by 5–9 MCC points with all architectures controlled. On graph learning (Table 5), PVNN achieves the best accuracy on 3 of 4 datasets, with a 5.86% gain on Airport over the strongest baseline. These results use controlled architectures and convincingly demonstrate that the PV model carries real downstream benefit, not just numerical stability.

- **Numerical stability is rigorously demonstrated.** Tables 1–3 systematically show that PV space avoids NaN/Inf failures up to r=1000 in FP32, produces 4–6 orders of magnitude lower round-trip error in Riemannian operators, and maintains stable gradient magnitudes (10⁻⁶–10⁻⁴) where Poincaré gradients vanish and hyperboloid gradients explode. This directly validates the paper's core motivation.

- **Principled normalization with theoretical guarantees.** Theorem 5.4 proves that PV GyroBN satisfies homogeneity of Fréchet mean and dispersion scaling, providing a principled foundation that not all hyperbolic normalization approaches enjoy.

## Weaknesses

### Fatal
None.

### Major
None that are fatal. The paper's core contributions are valid and well-supported.

### Minor

- **Curvature values are not reported for non-stability experiments.** The numerical stability section states K=−1, but the image classification, graph learning, and genomic experiments do not report what curvature values were used. The genomics section says "We use a single curvature shared for all layers" without stating the value. Since curvature controls the geometry's "hyperbolicness," this omission hinders reproducibility and comparison.

- **Image classification gains are marginal and within error bars.** On CIFAR-10 (Table 4), the best PV variant (95.30±0.18) vs. the best baseline (95.12±0.20) shows a gap well within the combined standard deviations. The paper acknowledges this implicitly but does not analyze whether the PV MLR actually induces a meaningfully hyperbolic feature representation (e.g., by measuring δ-hyperbolicity of penultimate features). Without such analysis, it is unclear whether the PV geometry is contributing at all on this task.

- **Numerical stability experiments are synthetic and not connected to training dynamics.** The stability tests (Tables 1–3) use random tangent vectors with large norms and synthetic gradient probes. The paper would be stronger if it connected these to actual training — e.g., by monitoring embedding norms during graph/genome training and showing that Poincaré networks encounter boundary issues that PVNN avoids, correlating with the performance gap. As it stands, the stability results confirm a theoretical advantage but do not prove it explains the downstream gains.

- **No runtime or memory comparison.** The paper argues the PV MLR is efficient (avoiding O(C·n) gyro-operations) but provides no wall-clock or memory measurements against Poincaré/hyperboloid baselines. Given that PV gyro operations (Eq. 2) are more algebraically involved, it would be informative to confirm there is no hidden overhead.

- **No limitations section.** The paper does not discuss when PV might be worse than existing models. Cora (weakly hyperbolic) shows PVNN is not best, but this is not analyzed beyond a brief note. A brief limitations paragraph would strengthen the paper.

### Trivial

- Table 7 row labeling ("Fréchet ∞") is non-standard.
- The notation in Theorem 4.3 is dense; a brief intuitive explanation of what each operator computes would improve readability.

## Nice-to-Haves

- A hyperparameter search over curvature and learning rate for each graph baseline, reported in the appendix, would address the concern that the large Airport gap (97.96 vs. 88.40 for HNN++) could partly reflect suboptimal HNN++ tuning.
- An experiment on a task where hyperbolic spaces are known to be essential and constrained models fail (e.g., very deep trees) would further bolster the case for PV's stability advantage.
- Measuring δ-hyperbolicity of learned representations in the image classification setting would clarify whether the PV MLR actually exploits hyperbolic geometry or is effectively a Euclidean classifier.

## Removed Points

The following points from the inputs were removed with justification:

- **"Potential unfairness in graph baselines — no details about how baselines were tuned."** The paper states explicitly that all models "share the same architecture consisting of two FC layers with nonlinear activations followed by an MLR classifier" and "differ only in the underlying hyperbolic model." The critic's request for hyperparameter search details is valid but the framing as a major unfairness concern is overstated given the controlled architecture comparison. Moved to Nice-to-Haves.

- **"KNN adaptation not described — KNN is originally a graph-specific method."** KNN (Mao et al., 2024) is a Klein-ball neural network, not a graph-specific method. The paper properly cites it as a hyperbolic (Klein ball) model. This criticism misunderstands the baseline.

- **"Failure to discuss when PV might be worse."** The paper explicitly notes on Cora that PVNN is not the best (Table 5) and attributes this to weak hyperbolicity. This is partial discussion, though a dedicated limitations section would be an improvement. Moved to Minor.

- **"No theoretical proofs."** The paper provides full proofs in the appendix (Theorem 4.2, 4.3, 5.2, 5.3, 5.4). This criticism is factually wrong.

- **Several generic strength-finder claims** (e.g., "this paper addressed an important problem") were removed as they lacked concrete content specific to this paper.

## Novel Insights

None beyond the paper's own contributions. The key insight — that PV space, already known in relativistic physics, provides a numerically stable unconstrained model for hyperbolic neural networks — is the paper's own, and it is correctly identified and developed.

## Suggestions

- Add curvature values for all experiments (image classification, graph learning, genomics) to the main text or appendix.
- Include a wall-clock time or FLOP comparison between PV layers and Poincaré/hyperboloid counterparts.
- Add a limitations paragraph discussing when PV may not be advantageous (e.g., weakly hyperbolic data).
- For the image classification experiments, either provide evidence (δ-hyperbolicity, embedding norm distributions) that the PV head induces meaningful hyperbolic geometry, or honestly characterize the setting as one where the geometry matters little.
- Track embedding norms during training on a representative graph/genomics task to directly connect the stability advantage to performance gains.

## Score and Decision

**Bracket derivation:** Round 1 placed the paper between 5.0 and 7.0. Round 2 narrowing against "Fully Hyperbolic CNN" (6.0), "Symmetric Spaces" (6.0), and "Shadow Cones" (6.33) places it at 6.0 — comparable to the first two anchors in contribution magnitude, with stronger empirical breadth than the former and comparable rigor to the latter, but held back from 6.5 by missing reproducibility details (curvature values, runtime) and the marginal image results.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>