Now I have everything I need. Let me produce the final consolidated review.

## Summary

This paper introduces the Proper Velocity (PV) model — an unconstrained representation of hyperbolic space — to deep learning. It derives the complete Riemannian toolkit for PV (exponential/logarithmic maps, parallel transport, geodesic distance) via isometry to the Poincaré ball, builds neural layers (MLR, FC, convolution, activation, batch normalization), and validates the framework on numerical stability, image classification, graph learning, and genomic sequence learning. The key claimed advantage is that PV's unconstrained nature avoids the numerical instabilities (boundary gradients, off-manifold drift) that plague constrained models like the Poincaré ball and hyperboloid.

---

## Strengths

- **Complete Riemannian toolkit for a new hyperbolic model.** The paper provides the first systematic derivation of closed-form Exp, Log, parallel transport, and geodesic distance on PV space (Theorem 4.3), along with explicit formulas at the origin. These operators are obtained via a proven isometry to the Poincaré ball (Theorem 4.2) and are validated by clean round-trip error experiments (Table 2, PV error 2.1×10⁻⁷ in FP32 vs. 2.1×10⁻⁴ for Poincaré).

- **Efficient PV MLR formulation with practical memory benefits.** Theorem 5.2 reparameterizes the PV MLR score using only inner products ⟨x, z_k⟩, avoiding per-class gyroaddition and reducing the intermediate tensor from O(b×C×n) to O(bn + Cn). The expression also recovers Euclidean MLR as K→0⁻, confirming theoretical consistency.

- **Consistent performance gains on strongly hyperbolic data.** On Disease (δ=0), Airport (δ=1), and PubMed (δ=3.5), PVNN outperforms all baselines (Poincaré, hyperboloid, Klein ball) by margins up to 5.86% (Table 5). On all five TEB genomic datasets, PVCNN improves over HCNN-S by 3–9 MCC points (Table 10). These results are statistically supported with standard deviations.

- **Principled normalization with theoretical guarantees.** Theorem 5.4 proves homogeneity of the Fréchet mean and dispersion under PV gyro operations, ensuring that GyroBN (Eq. 25) correctly normalizes sample statistics. The ablation study (Table 7) compares Fréchet-based, tangent, and Euclidean variants, providing practical guidance on the accuracy-efficiency tradeoff.

- **Ablations separate the effect of Riemannian design from heuristics.** Table 6 shows that the full PV FC layer outperforms a tangent-space FC on the two most hyperbolic graphs (Disease: 81.24 vs. 80.86; Airport: 97.93 vs. 86.99), and GyroBN consistently beats tangent BN. Table 9 compares multiple activation strategies. These controlled comparisons strengthen the evidence for the paper's Riemannian constructions.

---

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by evidence, and no verified weakness invalidates the contributions.

### Minor

- **Numerical stability is demonstrated only in synthetic benchmarks, not during training.** Tables 1–3 convincingly show that PV avoids NaN/Inf, maintains low round-trip error, and preserves gradient magnitudes under controlled conditions (fixed curvature K=−1, random batches). However, the paper does not report training-time metrics such as gradient norms across epochs, fraction of off-manifold iterates during optimization, or convergence speed for any learning task. The claim that PV "alleviates numerical instabilities" in practical training thus rests on indirect evidence (the downstream accuracy gains could also stem from other architectural properties). A single plot of gradient norm during training on Airport or Disease would substantially strengthen this claim.

- **The gradient magnitude comparison (Table 3) does not specify the sampling distribution for x.** The paper states that gradients are measured "on a random batch" for the function f_r(x)=||r⊗x−x||, but does not describe how x is sampled (e.g., uniformly in the Poincaré ball vs. from a standard normal for PV). Because gradient magnitudes depend on the region of the space where x is drawn, the comparison is difficult to fully interpret without this detail. The reported ranges are plausible and consistent with the paper's narrative, but the experiment would benefit from transparency about the sampling procedure.

- **Curvature K is not ablated.** All numerical stability experiments fix K=−1, and the learning experiments use "a single curvature shared for all layers" (Sec. 6.4) without sensitivity analysis. Curvature is a critical hyperparameter in hyperbolic networks — it controls the effective radius of the Poincaré ball and the scaling of gyro operations. Without ablating K (e.g., on CIFAR-100 or Disease), the robustness of the reported results to this parameter is unknown. The paper would be strengthened by at least a brief sensitivity study.

- **Limited to small-scale benchmarks.** The graph datasets (Disease, Airport, Cora, PubMed) and genomic TEB datasets are standard but small. The image classification experiments replace only the final MLR head of a ResNet-18, so the contribution is confined to the classifier. While this is consistent with prior hyperbolic work, the paper does not demonstrate PVNN's advantages on large-scale or deeper architectures. The authors acknowledge this as future work.

### Trivial

- None.

---

## Nice-to-Haves

- Training dynamics comparison: a plot of gradient norms (w.r.t. all parameters) during training for PVNN vs. Poincaré/Hyperboloid on one graph task.
- A curvature sensitivity table on a representative task (e.g., CIFAR-100 or Disease with K ∈ {−0.1, −1, −10}).
- A tangent-space PV convolution baseline for the genomic experiment to isolate the effect of geometry from the architectural choice.

---

## Removed Points

These points were raised by reviewers but are excluded from the main weaknesses after verification against the paper:

1. **"PV convolution is not geometrically principled."** The paper's definition (Sec. 5.3) uses Euclidean concatenation followed by PV FC. Since PV space = ℝⁿ as a set, concatenation is a standard data-rearrangement step — the geometry is handled by the PV FC layer. The paper makes no claim that concatenation itself is a geometric operation. This criticism misinterprets the paper's design choice. Removed.

2. **"The isometry mapping may not be correct."** The critic speculates about potential issues with Theorem 4.2 without identifying a specific error. The proof is in the appendix (stripped), and the paper's derivations follow from the stated theorem. Speculative concerns without concrete grounding are not actionable weaknesses. Removed per the rule against speculative fatal claims and appendix-related criticisms.

3. **"Poincaré also has zero failure rate in Table 1, so PV isn't uniquely stable."** This is factually correct but does not undermine the paper's claims — the paper presents multiple stability tests (Tables 2 and 3 also show advantages). The critic implies this single test refutes the paper's claim, which it does not. Removed.

4. **"The comparison may not be fair because baselines may not be optimally tuned."** This is a generic, speculative concern without specific evidence that baselines were undertuned. The paper reports following standard setups from prior work and using a fair architecture template. Removed.

5. **"Without the appendix, we cannot verify the proofs."** The appendix is stripped by the parser; the paper states proofs are in App. E. Removed per hard rule.

6. **"Gradient vanishing for Poincaré may be overblown; HNNs have been trained successfully."** While true that Poincaré HNNs can be trained with careful initialization, the paper's synthetic experiment (Table 3) shows a measurable difference in gradient magnitudes. The practical significance of this difference for training is exactly the gap noted in the first Minor weakness above. This point is subsumed by that weakness. Removed as redundant/merged.

---

## Novel Insights

None beyond the paper's own contributions. The key insight — that the PV model provides a stable, unconstrained coordinate representation of hyperbolic space — is clearly articulated by the authors, and the technical derivations (isometry to Poincaré ball, closed-form operators, efficient MLR parameterization) follow from it. No reviewer surfaced a fundamentally different reading or reinterpretation of the results.

---

## Suggestions

1. **Add a training-dynamics plot.** For at least one task (e.g., Airport graph classification), show gradient norm (w.r.t. all parameters) per epoch for PVNN vs. a Poincaré baseline and a hyperboloid baseline. This would directly validate the "stability during training" claim.

2. **Specify the random-batch distribution for the gradient test (Table 3).** State explicitly how x was sampled for each model (e.g., uniform in the Poincaré ball, standard normal in PV space) so readers can assess the fairness of the comparison.

3. **Add a curvature ablation for one learning task.** Show accuracy on CIFAR-100 or Disease for K ∈ {−0.1, −1, −10, −100} to demonstrate robustness or reveal sensitivity.

4. **(Optional) Add a tangent-space PV convolution baseline for the genomic experiment.** This would isolate whether the gain comes from the PV geometry or the heuristic convolution design.

---

## Score and Decision

The paper makes a technically sound, first-of-its-kind contribution by introducing the PV model to deep learning with complete Riemannian operators and validated neural layers. The experimental evidence supports the core claims, though the stability advantage is not demonstrated during training and the curvature sensitivity is unexplored. These are addressable gaps, not fatal flaws. The writing is clear, the derivations are rigorous, and the code is released.

**Originality**: High — first systematic ML treatment of the PV model.
**Quality**: Solid — well-executed experiments with thorough ablations; synthetic stability tests are clean.
**Clarity**: Strong — well-structured, notation is precise, theorems are clearly stated.
**Significance**: Moderate-high — provides a genuinely new and practically useful representation for hyperbolic networks.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>