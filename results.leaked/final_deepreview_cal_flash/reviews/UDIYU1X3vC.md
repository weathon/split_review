Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces Proper Velocity Neural Networks (PVNNs), providing the first systematic treatment of the Proper Velocity (PV) model—an unconstrained representation of hyperbolic geometry—for deep learning. The authors derive the complete Riemannian toolkit (exponential/logarithmic maps, parallel transport, geodesic distance) for PV space via the isometry with the Poincaré ball, then build fundamental neural network layers (MLR, FC, convolution, activation, batch normalization) on this foundation. Experiments across four tasks (numerical stability, image classification, graph node classification, genomic sequence learning) show that PVNNs achieve competitive or superior performance compared with Poincaré-ball and hyperboloid baselines, with particular advantages in numerical stability relative to the Poincaré ball and strong gains on genomic sequence tasks.

## Strengths

1. **First complete Riemannian toolkit for the PV model.** The paper derives closed-form expressions for Exp, Log, parallel transport, and geodesic distance on PV space (Theorem 4.3), along with simplified identity-centered versions. This is a genuine theoretical contribution that enables future work on this previously unexplored representation.

2. **Principled neural building blocks with clean Euclidean limits.** Theorems 5.2–5.4 provide closed-form PV MLR, FC, and GyroBN layers that provably converge to their Euclidean counterparts as curvature \(K \to 0^-\). The MLR simplification (Eq. 19) avoiding per-class gyroaddition is practically useful, and the ablated comparisons (Tables 6–9) validate that the Riemannian PV layers outperform tangent-space approximations on strongly hyperbolic data.

3. **Convincing numerical stability advantage over the Poincaré ball.** Tables 1–3 show that PV gyromultiplication has zero failure rate up to \(r=1000\) in FP32, round-trip error of \(2.1\times10^{-7}\) (vs. \(2.1\times10^{-4}\) for Poincaré), and stable gradient norms that neither vanish nor explode. This evidence directly supports the claim that the unconstrained PV representation alleviates the boundary-saturation problem of the Poincaré ball.

4. **Strong downstream performance, especially on genomic sequences.** PVCNN outperforms both Euclidean CNN and hyperboloid HCNN-S on all five TEB genomic tasks (Table 10), with particularly large gains (e.g., SINEs MCC from 85.45 to 93.78). The controlled experimental setup (same backbone, same curvature) makes these comparisons credible.

5. **Thorough ablation studies.** Tables 6–9 systematically compare Riemannian vs. tangent-space FC and BN layers, different activation schemes, and the effect of the exponential-map lifting, providing insight into which components drive performance.

## Weaknesses

### Major

1. **Hyperboloid stability comparison appears compromised (Tables 1, 2).** The hyperboloid model shows a violation rate of 32.5% at \(r=1\) (scalar multiplication by identity) and a round-trip error of \(1.0\) in *both* FP32 and FP64 for \(\|v\|=10\). These values are implausible for a correctly implemented hyperboloid model: at \(r=1\) the output should equal the input up to machine precision, and the round-trip error should drop from FP32 to FP64. The fact that the Poincaré ball (which shares the same hyperbolic geometry through isometry) achieves 0% violation at all radii further suggests an implementation issue specific to the hyperboloid. This weakens the paper's central claim that PV "alleviates numerical instabilities" relative to the hyperboloid model specifically. **Why it matters:** The numerical stability comparison is a primary selling point of the paper, and a comparison against a buggy baseline is unreliable evidence. The PV-vs-Poincaré comparison remains valid, but the hyperboloid numbers should not be cited as-is.

2. **No curvature tuning or sensitivity analysis.** All experiments use a fixed curvature (\(K=-1\) for stability experiments, "a single curvature shared for all layers" for genomics). Hyperbolic neural networks are known to be sensitive to curvature choice, and different models may have different optimal curvatures. Without varying or learning the curvature, it is unclear whether the reported gains reflect an inherent advantage of the PV representation or a suboptimal baseline setup. Since curvature tuning/learning is standard practice in the hyperbolic NN literature (e.g., HGCN, LNN, Lorentz MLR), this omission limits the conclusiveness of the comparisons.

### Minor

3. **Missing Euclidean baseline in graph learning experiments (Table 5).** The graph experiments compare only hyperbolic models (Poincaré, hyperboloid, Klein) without a simple Euclidean MLP/FC baseline. Without this reference point, it is difficult to assess whether the hyperbolic models are genuinely beneficial for these datasets, or whether the differences among hyperbolic models are meaningful in absolute terms. (The genomic task does include a Euclidean baseline, which strengthens that section.)

4. **No limitations discussion.** The paper lacks an explicit limitations paragraph. Given that PV and the Poincaré ball are isometric (Theorem 4.2), the contribution is a numerically favorable *parameterization* of the same hyperbolic geometry, not a geometrically distinct space. The paper acknowledges the isometry but does not discuss the implications for the scope of the contribution. Similarly, the general PV operators (Exp\(_x\), PT\(_{x\to y}\)) are substantially more complex than their identity-centered simplifications—and it is unclear when the general forms are needed in practice.

5. **Computational cost not discussed.** The PV FC layer uses the closed-form MLR score \(v_k(x)\) which avoids per-class gyroaddition, but the general operators and Fréchet-mean-based GyroBN involve iterative or complex computations. A brief runtime comparison with equivalent Poincaré/hyperboloid layers would help readers assess practical trade-offs.

### Trivial

6. The general parallel transport formula (Eq. 12) references the Möbius gyration \(\mathrm{gyr}_M\), which is not defined in the main text (deferred to Appendix B.4). A brief definition or citation would improve readability.

## Nice-to-Haves

- **Fix the hyperboloid stability experiments** by using a known-correct implementation (e.g., standard Lorentz Exp\(_0\)/Log\(_0\) via \(\sinh\)/\(\cosh\)), then report corrected violation rates and round-trip errors. If the corrected hyperboloid matches PV stability, the paper should acknowledge that PV's advantage is primarily over the Poincaré ball; if PV remains more stable, the claim is strengthened.
- **Add a curvature sensitivity experiment** (e.g., vary \(K\) over \(\{-10, -1, -0.1\}\) on one task like Airport graph classification) to show whether PVNN is robust to curvature choice.
- **Include a Euclidean MLP baseline** in the graph experiments (Table 5) to contextualize the hyperbolic models' absolute performance.
- **Analyze learned embedding norms** for the genomic and graph tasks, to test whether the PV model learns large-norm embeddings that would cause saturation in the Poincaré ball.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Hyperboloid implementation is "certainly incorrect" (Harsh Critic #1).** While the hyperboloid numbers are suspicious, this claim goes beyond what can be verified from the paper alone—it is a strong assertion about implementation correctness that the authors can address. I downgraded the framing from "certainly incorrect" to "appears compromised" and kept it as Major.
- **"PV offers a geometrically distinct space" impression (Harsh Critic #2).** The paper clearly states Theorem 4.2 (isometry) and uses it as the foundation for deriving operators. The critic's concern about reader misimpression is speculative and not verified by the paper's text, which appropriately frames PV as an alternative *representation*. Removed as a weakness.
- **Relativistic connection not exploited.** This is a note, not a weakness. The paper uses the PV model as a mathematical representation; the physical motivation is background context. Removed.
- **Metric derivation in appendix.** Acceptable practice; not a weakness. Removed.
- **General PV operators are overly complex.** This is a property of the derivation, not a flaw—the identity-centered simplifications cover the main use cases. Reduced to a trivial note.
- **ReLU activation discussion.** The paper already notes this is efficient; further discussion would be a nice-to-have, not a weakness. Removed from weaknesses.
- **Notation clarity on gyroaddition.** Minor presentation point; the paper cites Ungar (2022) for details. Removed.
- **Hyperparameter details in appendix.** Standard practice; not a weakness. Removed.
- **Strength Finder strength #1 (numerical stability).** The Strength Finder overstated this as clean evidence without noting the hyperboloid issue. I kept the Poincaré comparison as a valid strength but qualified it.
- **Strength Finder strength about "important problem" framing.** Removed generic/superficial language. The concrete strengths listed above remain.

## Novel Insights

The reviews surface an interesting meta-point: the very feature that makes PV attractive—its unconstrained nature—comes from the same isometry that shows PV and Poincaré represent *identical* geometry. This creates a tension in the paper's framing. The genuine contribution is not geometric novelty (the space is the same) but rather numerical: PV is \(\mathbb{R}^n\) with a hyperbolic metric, and operating directly in this coordinate chart avoids the boundary singularities of the Poincaré ball and the constrained optimization of the hyperboloid. The paper would benefit from embracing this framing more explicitly: PVNNs are a *stable numerical parameterization* of hyperbolic geometry, not a new geometric model. This is analogous to how different coordinate charts on a manifold can have different numerical properties even though they describe the same underlying geometry.

## Suggestions

1. Re-implement the hyperboloid stability comparison using a standard, known-correct Lorentz implementation (e.g., from geoopt or the formulas in Bdeir et al. 2024). Report corrected numbers and adjust the claims accordingly.
2. Add a brief curvature sensitivity experiment (vary \(K\) over at least three orders of magnitude) on one dataset to demonstrate robustness.
3. Include a Euclidean MLP baseline in the graph experiments (Table 5) to anchor the absolute performance of hyperbolic models.
4. Add a limitations paragraph explicitly noting the isometric relationship with the Poincaré ball, the scope of the numerical advantages, and the computational cost of general vs. simplified operators.

## Score and Decision

**Calibration:** I performed two rounds of retrieval. Round 1 (bracketing) identified anchors across weak (<3.5), middle (3.5–7.5), and strong (>7.5) bands. Round 2 narrowed within (4.5, 7.5) and (5.5, 7.5). The most directly comparable anchors were:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| *Fully Hyperbolic CNNs for CV* (ekz1hN5QNh) | 6.0 | 1,2 | Similar scope (novel hyperbolic layers, thorough experiments); the PVNN paper has a hyperboloid implementation issue this anchor lacks |
| *Neural nets on Symmetric Spaces* (bwOndfohRK) | 6.0 | 1,2 | Comparable theoretical contribution; PVNN has stronger experimental validation but the hyperboloid issue weakens its central claim |
| *Matrix Manifold NNs++* (30aSE3FB3L) | 5.67 | 2 | Comparable rigor; PVNN has more extensive experiments |
| *Optimizing for Robust Hyperbolic DL* (WOopKWDWtS) | 4.4 | 1 | Rejected; PVNN is clearly stronger in contributions and evidence |
| *Hyperbolic Graph Contrastive Learning* (Iy0WQ0c75x) | 4.75 | 2 | Rejected; PVNN has more substantial contributions |

The paper is stronger than the 4.4–4.75 rejected anchors due to its complete theoretical development and broader experimental validation. It is somewhat weaker than the 6.0 accepted anchors due to the flawed hyperboloid stability comparison, which undermines a core empirical claim. The paper's remaining contributions (PV toolkit, PVNN layers, Poincaré stability comparison, downstream results) are solid, but the hyperboloid issue is a significant limitation that requires correction.

**Final score: 5.5** — a paper with genuine contributions and solid evidence overall, but with a verifiable flaw in a key experiment that needs to be addressed before the claims about numerical stability relative to the hyperboloid can be trusted.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>