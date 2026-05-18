Now I have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper presents SparseDFF, a framework for one-shot dexterous manipulation that constructs view-consistent 3D dense feature fields (DFFs) from only four sparse RGBD views. The method back-projects DINO features onto a point cloud, then applies (i) a lightweight MLP trained via contrastive learning on a single source scene to improve feature consistency, and (ii) a Hough-voting-style point pruning mechanism to remove outlier points. Hand poses are optimized by minimizing feature discrepancy between source demonstration and target scene via an energy function with penetration constraints. Real-world experiments with a 24-DoF Shadow Dexterous Hand demonstrate the approach on rigid objects (boxes, drill, bowls, mugs) and deformable objects (plush toys), achieving markedly higher success rates than a naive DFF baseline and UniDexGrasp++.

## Strengths

1. **Sparse-view 3D feature distillation for dexterous manipulation.** Unlike prior DFF methods (e.g., Shen et al., Rashid et al.) that require dense camera views via NeRF-like reconstruction, SparseDFF constructs a feature field from only four RGBD cameras (abstract, Section 3). This addresses a genuine practical limitation for fixed-camera setups.

2. **Real-world validation with a high-DoF dexterous hand across diverse objects.** The method is validated on a physical 24-DoF Shadow Dexterous Hand with both rigid objects (boxes, drill, bowls, mugs) and deformable objects (plush toys), including cross-category transfers (Bowl1→Mugs, Monkey↔SmallBear) and cluttered scenes (Tables 1 and 2).

3. **Consistent and substantial improvement over baselines.** In Table 1, SparseDFF achieves 100% success on Box1/Box2/Drill/Bowl1 and 80% on cross-category Bowl→Mug transfers, while naive DFF achieves 0% on several of these and UniDexGrasp++ scores below 40% on most settings. The improvements are large and consistent across diverse transfer scenarios.

4. **Practical efficiency.** Training the refinement network on the source scene takes ~300 seconds (20,000 iterations), and hand pose optimization in a target scene takes ~20 seconds (300 iterations) on a single RTX 3090 (Section 4). This makes the approach viable for near-real-time deployment.

5. **Beyond grasping demonstrations.** The paper shows that the same framework can handle non-grasping interactions (head caressing, butt patting) transferred across objects (Figure 3), illustrating the broader applicability of the feature field approach.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative ablation isolating the contributions of the two proposed components.** The paper proposes two technical innovations — a feature refinement network and a point pruning mechanism — yet neither is ablated quantitatively. The ablations in Section 4.3 (Figures 5 and 6) are entirely qualitative (energy field visualizations and hand pose images). Because the baseline "DFF" includes neither refinement nor pruning, the reported improvements over DFF could come from either component or their combination. Without a decomposition (e.g., success rates for: DFF baseline, DFF + pruning only, DFF + refinement only, full method), it is impossible to determine which innovation drives the gains, or whether both are necessary. This is the most significant weakness in the paper.

2. **Limited statistical reporting.** All success rates are based on 10 trials per configuration with no confidence intervals, standard deviations, or per-trial breakdowns. With only 10 trials, differences such as 80% vs. 100% or 60% vs. 40% may not be statistically meaningful. The consistent pattern of improvement across diverse settings partially mitigates this concern, but the individual comparisons would be strengthened by confidence intervals or at least a statement of variance.

### Minor

3. **Missing numerical values for critical parameters.** The point pruning mechanism (Section 3.2) depends on a radius $r$ and a feature-difference threshold $\delta$ (lines 93-97), but their numerical values are never reported. These are essential for reproducibility.

4. **Per-pixel DINO feature extraction is underspecified.** The paper states DINO is applied to RGB images and features are back-projected using "pixel-point correspondences" (line 78). However, DINO is a ViT operating on image patches, so obtaining per-pixel features requires interpolation or patch-assignment logic. The paper does not describe this step, which affects feature quality and reproducibility.

5. **Limited real-world baseline comparison.** The only real-world baseline is a naive DFF (which is essentially the paper's method without refinement and pruning). UniDexGrasp++ is evaluated only in simulation due to vision instability. While this is understandable — the one-shot dexterous manipulation setting is nascent, and methods like DexPoint/GenDexGrasp rely on large training datasets incompatible with the one-shot setting — the paper could more explicitly discuss why these methods are not comparable, beyond the brief related-work note that they "depend on large demonstration datasets for training" (line 51).

6. **No failure analysis.** The method achieves 40% on Bowl1→FloatingMug and 50-60% on some cross-object transfers (Monkey→SmallBear), yet the paper offers no analysis or visualization of failure cases. Understanding why these transfers fail (e.g., feature ambiguity, penetration constraints, sampling issues) would help assess the method's limitations.

### Trivial

7. **Beyond-grasping experiments are qualitative only.** The head-caressing and butt-patting demonstrations (Figure 3) are presented without quantitative success rates. This is acceptable as a proof-of-concept but should be acknowledged as preliminary, which the paper largely does.

## Nice-to-Haves

- **Parameter sensitivity analysis.** The paper could report sensitivity experiments for the pruning parameters ($r$, $\delta$), the pruning ratio (currently fixed at 20%), and the energy-function weights ($\lambda_{\text{pen}}, \lambda_{\text{spen}}, \lambda_{\text{pose}}$).
- **Mechanistic analysis of the refinement network's cross-scene generalization.** While the paper provides a reasonable intuition (contrastive learning enforces view-consistent features, which transfers to new scenes because the network learns general feature alignment rather than object-specific mappings), a deeper analysis (e.g., feature similarity matrices across different object pairs, or a study of whether the learned transformation preserves relative feature distances across scenes) would strengthen the claim.
- **Comparison with alternative one-shot approaches** where feasible, such as applying Wei et al.'s geometric grasp synthesis or a classical feature-matching baseline in the same experimental setup.

## Removed Points

These points were raised by reviewers but are either factually incorrect, misread the paper, or reflect reviewer knowledge gaps:

1. **"Figure 5 does not show what happens when the refinement network is trained on one scene and applied to a different scene."** — This is factually inaccurate. Figure 5 explicitly shows the energy field *between source and target scenes*, comparing with and without refinement. The refinement network was trained on the source scene and applied to the target scene; this is precisely a cross-scene comparison. The valid criticism is that the evidence is qualitative only (kept as Major #1 above).

2. **"The one-shot claim is ambiguous and training cost is understated."** — The paper clearly states the training cost: "20000 iterations for adaptation, roughly 300 seconds using a single NVIDIA GeForce RTX 3090" (line 152). 300 seconds for a single source-scene demonstration is reasonable in the context of one-shot manipulation systems. The paper could state this overhead earlier (e.g., in the abstract), but the information is present and not understated.

3. **"The mechanistic explanation for cross-scene generalization is missing"** treated as a fatal gap. — The paper provides a clear intuition: contrastive learning on multi-view correspondences from the source scene teaches the network to align DINO features across viewpoints, and this transformation generalizes because it addresses a property of DINO features (view inconsistency) that is present across scenes, not scene-specific geometry. While deeper analysis would be welcome (moved to Nice-to-Haves), this is not a structural flaw — the empirical results across 9 rigid-object transfers and multiple deformable-object transfers already demonstrate the generalization works.

4. **"The paper should compare with DexPoint, GenDexGrasp, Wei et al."** — These methods require large training datasets (DexPoint, GenDexGrasp) or assume different capabilities (Wei et al.'s geometric synthesis). The paper's related work notes this distinction (line 51). Comparing methods with fundamentally different data requirements is not a baseline omission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a quantitative ablation table with success rates (20+ trials each) for: (i) raw DFF, (ii) DFF + refinement only, (iii) DFF + pruning only, and (iv) full method. Report means and bootstrapped confidence intervals. This is the single most important improvement the authors could make.

2. Report the numerical values of $r$ and $\delta$ for the pruning mechanism, and clarify how per-pixel DINO features are obtained from the ViT.

3. Include a brief failure analysis for the lowest-success-rate settings (e.g., Bowl1→FloatingMug at 40%), discussing whether failures stem from feature ambiguity, optimization local minima, or penetration constraints.

4. Consider moving the training overhead (300 seconds) to the abstract to align expectations, and clarify whether a network trained on one demonstration can be reused for another demonstration on the same source object.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>