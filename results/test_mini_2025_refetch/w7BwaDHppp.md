Now I have sufficient calibration. Let me write the final consolidated review.

---

## Summary

This paper proposes a geometry-aware projective mapping for unbounded NeRF scenes, replacing fixed mapping functions (inverted sphere, contract) with a $p$-norm-based mapping whose $p$ value is adapted per scene via RANSAC on SfM point clouds. It also introduces an angular ray parameterization that distributes samples more evenly in the distorted embedding space. The core methodological contributions are a unified stereographic-projection analysis showing that existing mappings correspond to cylindrical/paraboloidal manifolds, and a deformable $p$-norm manifold that can allocate capacity adaptively.

## Strengths

- **Unified geometric analysis via stereographic projection (Section 4.1–4.2).** The paper decomposes inverted-sphere and contract mappings into inverse stereographic + orthogonal projections, revealing they correspond to cylindrical and paraboloidal manifolds (Eqs. 6, 8). This is the first work to provide this unified perspective, and it cleanly explains why fixed-shape manifolds cannot adapt to scene geometry — a genuinely novel conceptual contribution.

- **Large gains in challenging camera configurations (Table 1).** On mip-NeRF 360 ×2 (cameras moved away from scene origin), iNGP+contract collapses to 15.10 PSNR while iNGP+Ours achieves 26.35 PSNR — an >11 dB improvement. Similar large gaps appear for TensorRF (21.50 vs. 23.44). These results validate that the adaptive mapping can prevent catastrophic undersampling in scenarios where fixed mappings fail.

- **Generality across diverse NeRF backbones (Table 1).** The method is integrated into four distinct frameworks (DVGO, TensorRF, iNGP, NeRF) and consistently improves over the contract baseline in nearly every setting, showing the contribution is not tied to a specific architecture.

- **Ablation isolates component contributions (Table 2).** The controlled swaps — using p-norm with normalized ray param (14.87 PSNR at ×2) and contract with angular param (22.20) — show that both components contribute to the full method's 23.67 PSNR.

## Weaknesses

### Major

- **"State-of-the-art" claim is not supported by the evidence.** The abstract and conclusion claim "state-of-the-art novel view synthesis results," but the paper compares only against contract mapping embedded in the same backbones, not against the actual SOTA methods it cites (mip-NeRF 360, Zip-NeRF) running in their native frameworks. The ×1 results — which reflect standard benchmark conditions — show modest gains of 0.1–1.4 dB across backbones. The large improvements come only from the synthetic ×2 configuration. This overclaiming undermines the paper's position.

- **RANSAC-based $p$ selection is inadequately validated (Section 4.3).** The RANSAC procedure (randomly sample two 3D points, project, maximize Euclidean distance) is a heuristic with no theoretical grounding. It is evaluated on a single scene (bicycle) in the ablation (Table 2), showing only two automatically chosen $p$ values ($p=1.5$, $p=1.1$). There is no comparison against a grid search over $p$, no analysis of sensitivity to $p$ across multiple scenes, and no evidence that maximizing pairwise distance in the embedding space achieves the stated goal of "evenly distributing points."

- **Angular ray parameterization is the dominant contributor, not the $p$-norm mapping.** The paper's title and central framing emphasize the geometry-aware $p$-norm mapping, but the ablation (Table 2) tells a different story: at ×2, contract+angular achieves 22.20 PSNR, while adding the $p$-norm mapping only improves to 23.67 PSNR (a 1.47 dB gain). Meanwhile, p-norm+normalized (without angular param) collapses to 14.87 PSNR. This asymmetry persists at ×4 and ×8. The evidence suggests the angular ray parameterization is responsible for the bulk of the improvement, while the $p$-norm mapping itself provides a secondary benefit.

### Minor

- **Evaluation relies primarily on synthetic camera modifications.** The ×2/×4/×8 scenarios are artificial — cameras are moved away from the scene origin according to the paper's own design (Fig. 5). There is no evidence that such configurations arise in standard capture practices. The ×1 results (Table 1) show consistent but modest improvements, and on NeRF at ×1 the contract baseline actually has slightly better SSIM/LPIPS than Ours despite comparable PSNR (25.58 vs. 25.68).

- **No error bars or statistical significance.** All results in Tables 1 and 2 appear to be single-run evaluations. Given that many improvements (especially at ×1) are only 0.1–0.5 dB, confidence intervals or multi-run statistics would help assess significance.

- **The angular ray parameterization definition (Eq. 10) has unclear treatment of the 4D center of projection.** The equation uses $\theta = \angle(\mathbf{x} - Q, \mathbf{o} - Q)$ where $Q = (0,0,0,1)$ is a 4D point, but $\mathbf{x}$ and $\mathbf{o}$ are 3D points. The paper does not specify how the angle is computed across dimensions of different sizes. This is likely a minor oversight in presentation (using homogeneous coordinates) but should be clarified.

### Trivial

- The paper's citation to "COUCLUSION" (Section 6 header, line 251) contains a typo.

## Nice-to-Haves

- An integration of the $p$-norm mapping into the mip-NeRF 360 codebase (replacing only the contract mapping while keeping integrated positional encoding and cone tracing) would isolate the mapping function's effect in its intended context.
- A sensitivity analysis of $p$ across multiple scenes with different camera configurations, including comparison to a grid search baseline, would strengthen the RANSAC validation substantially.
- Reporting training time/memory overhead would help practitioners assess the method's practical cost.

## Removed Points

- *"Contract mapping dropped into voxel-grid methods destroys the original method's properties"* — The paper compares both mappings within the same backbone, which is the correct way to isolate the mapping function's effect. Removed.
- *"Qualitative results are cherry-picked"* — Speculative without evidence. Removed.
- *"Hyperparameters unchanged could disadvantage the contract baseline"* — Speculative; removed.
- *"Double the number of samples is unjustified asymmetry"* — The paper clearly justifies this (Section 5.1: "To balance the single evaluation, we double the number of samples on a ray"). Removed.
- *Generic concerns about missing related work / appendix content* — Removed per filtering rules.
- *Formatting, spelling, and grammar nitpicks* — Removed per filtering rules (parser artifacts).
- *Strength Finder: generic/superficial strengths* — Generic statements about importance of problem, etc., removed.
- *Harsh critic's claim about "on ×1 the paper's best result (26.65 PSNR) is far below published mip-NeRF 360 result (~28.6 PSNR)"* — This compares different backbones (iNGP vs. mip-NeRF 360's MLP architecture), not a fair comparison of mapping functions. Removed.

## Novel Insights

The harsh critic correctly identifies a structural tension in the paper: the claimed contribution (geometry-aware $p$-norm mapping) is conceptually the centerpiece, but the ablation evidence shows the angular ray parameterization — presented as supporting the mapping — is empirically the dominant component. This suggests the paper could be reframed more honestly: the angular parameterization is the primary innovation that prevents under-sampling when cameras are far from the scene origin, and the $p$-norm mapping is a secondary refinement. The stereographic projection analysis remains the paper's strongest standalone contribution, independent of the experiments.

## Suggestions

1. **Tone down the claims.** Remove "state-of-the-art" from abstract and conclusion. Reframe the contribution as "a principled geometric framework for analyzing unbounded scene mappings and a method that improves capacity allocation when cameras are far from the scene origin."

2. **Validate the RANSAC $p$ selection properly.** Add a comparison against grid-searched $p$ values on at least 3–5 scenes, and include a sensitivity plot showing performance vs. $p$ across a range.

3. **Expand the ×1 evaluation.** Show that the method at least matches (or doesn't degrade) performance on standard benchmarks without camera modification. The current Table 1 ×1 results are mixed.

4. **Clarify the relative contribution.** Acknowledge more explicitly that the angular parameterization provides the larger empirical gain, and either reframe the paper's emphasis accordingly or add evidence that the $p$-norm mapping provides unique benefits beyond what the angular parameterization alone achieves.

---

**Calibration Report**

**Round 1 — Bracketing anchors** (all three bands queried with topic "NeRF unbounded scene novel view synthesis mapping function"):
- Weak band (avg < 3.5): WKfMFtlz5D (2.50), mYo9r0CwUf (2.33), hrXt6Fdl2P (2.60), LieTse3fQB (2.50), AMVLOv30Qg (3.33) — Papers with limited or flawed contributions. Our paper is clearly above these.
- Middle band (3.5–7.5): Nu7dDaVF5a (6.00), zDJf7fvdid (6.00), QuVlUn4T2G (6.75), igfDXfMvm5 (5.50), o4CLLlIaaH (6.50) — Accepted posters with solid but not exceptional contributions.
- Strong band (>7.5): QQBPWtvtcn (7.67), P4o9akekdf (8.00), noe76eRcPC (8.00) — Strong oral/spotlight papers. Our paper is below these.

**Initial bracket:** 4.5 – 6.0

**Round 2 — Narrowing anchors** (queried on NeRF evaluation/ablation/claims at two score ranges):
- 4.5–6.0: bLKcCe7hYh (UC-NeRF, 5.80), L3DxhwXKZk (ExpanDyNeRF, 4.60), B8FA2ixkPN (GML-NeRF, 5.00), 4uaogMQgNL (UpFusion, 5.25)
- 5.5–6.5: Nu7dDaVF5a (6.00), A2mRcRyGdl (6.33), bLKcCe7hYh (5.80)

**Comparison to key anchors:**
- vs. UC-NeRF (5.80, accepted): UC-NeRF has more thorough evaluation but a less novel conceptual contribution. Our paper has higher conceptual novelty but weaker evaluation (synthetic camera modifications, poorly validated RANSAC). Comparable caliber — slightly below UC-NeRF.
- vs. ExpanDyNeRF (4.60, rejected): Both evaluate with synthetic camera modifications. Our paper has genuinely novel theoretical content (stereographic analysis) that ExpanDyNeRF lacks. Clearly above.
- vs. GML-NeRF (5.00, rejected): GML-NeRF has incremental contribution. Our paper's conceptual contribution is stronger. Above.

**Final score:** 5.5 — The paper has a genuinely novel conceptual contribution (stereographic projection analysis) and demonstrates real improvements in challenging scenarios, but the evaluation has significant gaps: overclaimed SOTA status, poorly validated RANSAC selection, and an ablation that shows the angular parameterization (not the p-norm mapping) is the dominant contributor, undermining the paper's central framing.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>