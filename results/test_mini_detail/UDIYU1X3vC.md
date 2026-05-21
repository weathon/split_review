Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces Proper Velocity (PV) Neural Networks, leveraging the unconstrained PV model (ℝⁿ) of hyperbolic geometry — rooted in Einstein's special relativity — as an alternative to the bounded Poincaré ball and constrained hyperboloid models. The authors derive the complete Riemannian toolkit (exponential/logarithmic maps, parallel transport, geodesic distance) for the PV space via an isometry with the Poincaré ball, then build core neural network layers (MLR, fully-connected, convolutional, activation, and batch normalization) on this foundation. Experiments across four tasks — numerical stability, image classification, graph node classification, and genomic sequence learning — demonstrate that PVNNs are competitive with or outperform existing hyperbolic baselines, with particularly strong results on genomic sequence prediction.

## Strengths

1. **New geometric foundation with complete theoretical toolkit.** The paper is the first to fully develop the Riemannian geometry of the PV model (Theorems 4.2–4.3), including closed-form exponential map, logarithmic map, parallel transport, and geodesic distance. The proof that the PV space is isometric to the Poincaré ball (Theorem 4.2) provides a rigorous bridge to existing hyperbolic methods and ensures the geometric tools transfer correctly.

2. **Efficient MLR parameterization avoids expensive gyro-operations.** Theorem 5.2 (Eq. 19) rewrites the PV MLR score in terms of a single inner product ⟨x, zₖ⟩ and a scalar, reducing computation from a b×C×n gyroaddition tensor to a matrix multiplication. This is a concrete practical improvement over the naive formulation and directly addresses a scalability bottleneck.

3. **Normalization with provable sample-statistic control.** Theorem 5.4 proves that PV GyroBN shifts the Fréchet mean to the bias parameter and scales the Fréchet variance by s², guaranteeing that the layer actually normalizes batch statistics — a property not guaranteed by earlier tangent-space normalization approaches. The ablation in Table 7 provides a practical comparison of the Fréchet-based GyroBN against cheaper tangent/Euclidean variants, giving practitioners clear guidance on the accuracy-speed tradeoff.

4. **Consistent and often substantial empirical gains on strongly hyperbolic tasks.** On graph node classification (Table 5), PVNN outperforms all prior hyperbolic models (HNN, HNN++, LNN) on Disease, Airport, and PubMed (the three most hyperbolic datasets), with a 5.86% improvement on Airport. On genomic sequence learning (Table 10), PVCNN beats both the Euclidean CNN and the hyperboloid-based HCNN-S on all five TEB tasks, with gains of up to ~9 MCC points on SINEs. These results are obtained with a controlled architecture (same backbone, same CNN structure).

5. **Numerical stability advantage is clearly demonstrated in synthetic experiments.** Tables 1–3 show that PV simultaneously avoids the gradient vanishing of the Poincaré ball and the gradient explosion/NaN failures of the hyperboloid, with round-trip errors three orders of magnitude smaller than the Poincaré ball in FP32.

## Weaknesses

### Fatal

None.

### Major

1. **"Same architecture" claim is imprecise and the comparison confounds geometry with layer design.** The paper states (lines 310–311) that "all models share the same architecture consisting of two FC layers with nonlinear activations followed by an MLR classifier; they differ only in the underlying hyperbolic model." However, the PV FC layer (Theorem 5.3: yₖ = sinh(√(-K) vₖ(x))/√(-K)) is architecturally different from the Möbius gyromatrix layer used in Poincaré HNNs or the ambient-space linear layer used in Lorentz networks. The large performance gap on Airport (PVNN 97.96 vs. HNN++ 88.40) likely reflects this architectural difference alongside the geometric one. The PVNN+TFC ablation partially controls for this within PV (trading 11 points on Airport), but the baselines do not include their own tangent-space variants. To cleanly attribute gains to the PV manifold rather than the specific layer formulation, the paper would need a cross-geometry controlled comparison where all models use the same type of linear layer (e.g., tangent-space Exp₀(A Log₀(x)+b) for each geometry).

2. **Hyperboloid baseline implementation raises concerns that are not addressed.** Table 1 reports a 32.5% constraint violation rate for the hyperboloid model at r=1 — a value that is suspiciously high for a standard Lorentz gyrovector scalar multiplication at a small multiplier. The paper does not provide implementation details for the hyperboloid scalar multiplication, so the reader cannot verify whether this matches the standard formulation used in prior work (e.g., Bdeir et al. 2024). If the implementation is non-standard, the stability advantage of PV over the hyperboloid is exaggerated. The authors should clarify the exact formulation used and confirm it reproduces the standard Lorentz gyrovector behavior.

### Minor

3. **The practical significance of the stability advantage over the Poincaré ball is not directly demonstrated in downstream tasks.** Table 1 shows the Poincaré ball has zero failure and violation rates up to r=1000 — the same as PV. The round-trip error advantage (2.1e-7 vs. 2.1e-4) and gradient magnitude advantage (10⁻⁶ vs. 10⁻¹²) are clear in synthetic experiments, but the paper does not show that this translates into tangible training benefits (e.g., faster convergence, better final loss, robustness to initialization) on the downstream tasks. The downstream results could be dominated by the layer design differences (Issue 1) rather than numerical stability.

4. **Direct PV-space activation degrades severely on Cora without explanation.** Table 9 shows that "Euc. Act." (applying Euclidean activation directly in PV space) achieves only 38.10 on Cora versus 52.26 for tangent-space activation. The paper notes this but does not investigate or explain why — whether this is due to weakly hyperbolic data structure, numerical issues, or some other cause. This is a notable failure case for a design choice enabled by the unconstrained nature of PV space.

5. **The gradient magnitude range for the hyperboloid (Table 3: [0, NaN]) is reported in a misleading form.** A range that includes NaN is not meaningful; the paper should report statistics excluding NaN entries or use a metric that does not collapse under numerical breakdown.

6. **Computational overhead of PV operators is not analyzed.** The PV exponential/logarithmic maps involve sinh, cosh, and tanh⁻¹, which are more expensive than the algebraic operations in Möbius or Lorentz formulations. For the fully PV CNN on genomic tasks, a runtime comparison against the Euclidean and hyperboloid baselines would help practitioners assess the trade-off.

### Trivial

None.

## Nice-to-Haves

- Report training curves or convergence behavior for at least one graph dataset (e.g., Airport) to connect the numerical stability claims to training dynamics.
- Include macro F1 scores for Cora (which has imbalanced classes) alongside accuracy.
- Add curvature learning as a natural extension — all experiments appear to use a fixed curvature.
- Describe the initialization scheme used for the PV MLR parameters zₖ and rₖ.

## Removed Points

These were flagged in reviewer inputs but are removed from the main review for the following reasons:

- **Criticism that the paper's claims about numerical stability are "overstated" because Poincaré has zero failure rates** — Retained in weakened form as Minor Issue 3. The paper correctly reports Poincaré's zero failure rate; the stability advantage lies in round-trip error and gradient behavior, which are supported by the synthetic evidence. The practical significance gap is a valid concern but does not invalidate the core claim.

- **Complaint that the PV FC layer "does not perform a linear transformation in the usual sense"** — This is by design for a Riemannian geometry adaptation; the same is true of Poincaré Möbius layers. Not a weakness of the paper.

- **Request for controlled comparison where all models use tangent-space linear layers** — This is merged into Major Issue 1 as the specific experimental design needed.

- **Section-by-section notes about "cumbersome expressions" in the Riemannian operators** — A subjective presentation opinion, not a substantive weakness.

- **Strength Finder claims about "unconstrained representation eliminates boundary instabilities"** — Retained in strengths section as evidence-based. Claims that conflate properties with downstream performance were edited for accuracy.

- **Requests for missing appendix or proof details** — The parser strips appendices; these exist in the original submission.

- **Any criticism about missing related works** — Cannot be independently verified.

## Novel Insights

The reviews surface a subtle tension in the paper: the PV model's primary claimed advantage is its unconstrained nature (mitigating boundary-related numerical issues), yet the strongest empirical results come from the genomic sequence learning task, where the comparison is against a same-architecture hyperboloid baseline (HCNN-S) that also operates in a constrained space. This suggests that the PV model's benefits may arise as much from its different geometric parameterization of distances and inner products as from its numerical stability per se. An interesting follow-up would be to disentangle whether the PV formulation provides a fundamentally different inductive bias for hierarchical data (through its sinh-scaled distances) that benefits certain tasks independently of numerical concerns.

## Suggestions

1. Clarify the hyperboloid scalar multiplication implementation used in Table 1 and confirm it matches the standard Lorentz gyrovector formulation.
2. Add a cross-geometry controlled experiment using tangent-space linear layers (Exp₀(A Log₀(x)+b)) for all geometries to isolate the contribution of the PV manifold from the layer design.
3. Investigate and explain the severe degradation of direct PV-space activation on Cora.
4. Report training curves or convergence speed for at least one graph dataset to ground the stability claims.
5. Provide a runtime comparison of the PV CNN against the Euclidean and hyperboloid baselines on the genomic tasks.

## Score and Decision

**Score bracketing (Round 1):** The paper is clearly above the weak-anchor band (2.5–3.4, PDE/PINN papers with little relevance) and the mid-anchor band (4.5–5.5, sparse hyperbolic learning, balanced hyperbolic embeddings, Solv geometry). It sits around the upper-mid range.

**Round 2 narrowing:** Compared to **Gyrogroup Batch Normalization** (avg 7.00, ICLR Poster) — both papers contribute Riemannian/gyro toolkit components. The PV paper is broader (full network construction vs. BN only) and has more extensive experiments (4 tasks). However, GyroBN is cleaner in execution, with no confounded comparisons. The PV paper's issues (hyperboloid baseline ambiguity, imprecise comparison claims) bring it slightly below this anchor. Compared to **Spectro-Riemannian GNNs** (avg 5.75, ICLR Poster) — the PV paper is clearly more foundational and better executed. Compared to **Neural Snowflakes** (avg 6.75, ICLR Poster) — comparable scope (theory + experiments across several tasks), but Neural Snowflakes has cleaner empirical presentation. The PV paper is in the same tier but with more rough edges.

**Final score: 6.5.** This reflects a solid paper with genuine theoretical and empirical contributions, held back from a higher score by the need to resolve the hyperboloid baseline concern and provide a cleaner attribution of gains to geometry versus layer design.

**Decision: Accept.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>