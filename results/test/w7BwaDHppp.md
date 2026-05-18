Now I have all the evidence I need. Here is the consolidated review:

---

## Summary

This paper proposes an adaptive mapping function for unbounded neural radiance fields, using a p-norm distance metric whose exponent p is selected per-scene from a COLMAP point cloud. The core idea — that the mapping manifold's shape should adapt to scene geometry rather than being fixed — is motivated through a stereographic-projection analysis of existing mappings (inverted sphere, contract). An angular ray parameterization is introduced to maintain even sampling in the deformed embedding space. Experiments integrate the proposal into four NeRF backbones (DVGO, TensoRF, iNGP, NeRF) across three datasets, showing consistent PSNR/SSIM/LPIPS improvements over contract mapping, especially when cameras are far from the scene origin.

## Strengths

1. **Novel geometric analysis of existing mapping functions via stereographic projection (Section 4.1, Figures 1–2).** The paper provides a unified framework for viewing the inverted-sphere mapping (cylinder manifold) and contract mapping (paraboloid manifold) as special cases of a deformable manifold. This conceptual framing is genuinely novel and clarifies why fixed mappings allocate capacity independently of scene structure.

2. **Adaptive p-norm mapping function (Section 4.3, Figure 3).** The central technical contribution — a mapping that deforms the embedding manifold according to a p-norm distance, with per-scene p selection — is a clean solution to a recognized problem. The intuition (large p → convex manifold → more capacity to near content; small p → concave → more capacity to distant content) is well-motivated and physically sensible.

3. **Angular ray parameterization (Section 4.4, Figure 4).** The paper correctly identifies that a non-linear mapping requires a correspondingly adapted ray parameterization to avoid over/under-sampling. The angular formulation (θ/θ_max) is a principled fix, and the toy example (p=2) convincingly illustrates the issue.

4. **Plug-and-play integration across diverse backbones.** The method is evaluated on DVGO (voxel grid), TensoRF (tensor decomposition), iNGP (hash grid), and NeRF (MLP) — four architecturally distinct frameworks — with consistent improvements, demonstrating practical generality beyond any single architecture. Ablations (Table 2) confirm both the mapping and parameterization components contribute independently.

## Weaknesses

### Fatal
None.

### Major

1. **The p-value selection procedure is critically underspecified, harming reproducibility of the core contribution (Section 4.3).** The paper describes randomly sampling two 3D points, projecting them, computing Euclidean distance, repeating, and "select[ing] a p value with the maximum distance." This leaves essential questions unanswered: How are candidate p values generated (grid search? random sampling? some optimization?) and over what range? How many candidate p values are evaluated per scene? Does each iteration randomly pick a different p and record its max pairwise distance, or are all iterations run for each candidate p and then compared? The "maximum distance" criterion also does not directly measure the stated goal ("evenly distributed in the whole space") — two points maximally far apart says nothing about whether intermediate space is filled. Because the p-selection IS the adaptive mechanism that distinguishes the method from fixed mappings, this underspecification is a serious gap.

2. **The "state-of-the-art" claim is unsupported because the evaluation omits the strongest existing methods for unbounded scenes.** The paper compares against contract mapping and inverted-sphere mapping embedded into the same backbones, plus NeRF+ and F2-NeRF. However, mip-NeRF 360 (Barron et al., 2022) and Zip-NeRF (Barron et al., 2023) are the dominant complete pipelines for unbounded 360° scenes and are directly cited as related work. The contract mapping is one component of these methods, but mip-NeRF 360 and Zip-NeRF additionally use multisample cone integration, proposal network supervision, and distortion-based regularization. A claim of "state-of-the-art" requires comparison against these full methods on standard benchmarks, not just their spatial mapping in isolation.

### Minor

1. **The angular ray parameterization has a geometrically sloppy notation that obscures its correctness (Eq. 4, line 127).** The paper defines d as a direction vector (line 56: "d is a vector of a viewing direction") but then writes θ_max = ∠(d − Q, o − Q), subtracting a point Q from a direction vector d. The geometric intent (as t → ∞, x = o + td aligns with d, so the angle between (x−Q) and (o−Q) approaches the angle between d's direction from Q and (o−Q)) is clear, but as written the expression is not well-defined. This should be corrected.

2. **The ablation study is limited to a single scene (bicycle, one dataset).** Table 2 provides useful component-level validation, but the effect of p and the angular parameterization may vary significantly with scene structure. A more thorough ablation across multiple scenes with different geometry would strengthen confidence in the method's robustness.

3. **The method's sensitivity to point cloud quality is not discussed.** The p-selection relies on a COLMAP point cloud, which can be sparse in textureless or distant regions. The paper does not analyze how point cloud density, noise, or outliers affect the chosen p value or downstream rendering quality.

### Trivial

1. **"RANSAC" is a misnomer.** The described procedure (random sampling of pairs, distance computation, max-criterion selection) has no consensus step, no outlier rejection, and no model fitting. Calling it "RANSAC" implies a robustness mechanism that is not present.

## Nice-to-Haves

- Specify the p-selection procedure concretely: define the candidate set (e.g., grid over [1, 8] in steps of 0.5), the number of random pairs per candidate, and whether the selection uses mean or max distance.
- Compare against full mip-NeRF 360 and Zip-NeRF pipelines on standard (non-shifted) evaluation splits to substantiate the SOTA claim.
- Verify that the angular parameterization works for p values other than p=2 (the only shown example) — either analytically or with an additional figure/toy example.

## Removed Points

The following criticisms from the reviewers were removed per verification:

- **Missing derivation in Section 4.2 (Claim 4 from Harsh Critic).** The reviewer noted the derivation from stereographic projection to existing mapping functions is absent. However, Section 4.2 is a parser artifact — the PDF extraction stripped it, but it exists in the original submission. The instructions explicitly prohibit penalizing papers for parser-stripped content.
- **"×2 camera-shift scenarios are artificial."** The paper evaluates on BOTH ×1 (standard) and ×2 (stress test) settings. The ×2 condition is a deliberately constructed worst-case scenario to demonstrate the method's advantage, not a replacement for standard evaluation. The paper shows improvement at ×1 as well (line 159: "better performance overall, except in some cases of ×1").
- **"No analytical derivation linking the angular sampling to p-norm mapping."** While the paper's evidence for the angular parameterization is primarily visual (Figure 4), the toy example with p=2 is a reasonable proof-of-concept. A derivation would strengthen the paper but its absence is not a flaw that invalidates the contribution.
- **Strength Finder's "State-of-the-art quantitative results" strength.** This conflicts with verified Weakness #2 (missing SOTA baselines) and is partially unsupported. The results show improvement over contract mapping in the same backbones, which is genuine, but the SOTA framing is overstated.

## Novel Insights

The most interesting cross-panel observation is that the harsh critic and strength finder agree on the paper's core assets (stereographic analysis, adaptive mapping idea, angular parameterization) but disagree on whether the evaluation suffices. The decisive weakness is not a methodological error but a scope mismatch: the paper positions itself as a general improvement for unbounded NeRF ("state-of-the-art") but designs its experiments to isolate the mapping function's effect. The experimental design (same-backbone comparisons) actually supports a more modest claim — that the adaptive mapping beats the contract mapping within a given framework — and the paper would be stronger if it claimed this precisely rather than claiming SOTA over methods that include additional architectural innovations beyond the mapping itself.

## Suggestions

1. **Specify the p-selection algorithm completely.** Provide the exact procedure: candidate p range and step size, number of random pairs per iteration, selection criterion, and number of trials. Consider replacing the ad-hoc max-distance heuristic with a more principled measure of point cloud coverage (e.g., mean pairwise distance or entropy).
2. **Replace or qualify the "state-of-the-art" claim.** Compare against full mip-NeRF 360 and Zip-NeRF on standard splits, or alternatively reframe the contribution narrowly as "improving mapping functions within existing backbones" and drop the unsubstantiated SOTA language.
3. **Fix the notation in Eq. (4).** Replace d − Q with (direction from Q along d) or reparameterize to avoid the ill-defined expression. Clarify that as t → ∞, the angle ∠(x−Q, o−Q) converges to ∠(d, o−Q) (or the equivalent with Q-centered direction).
4. **Extend the ablation to 2–3 additional scenes** with distinct geometric profiles (e.g., one sparse outdoor scene, one dense urban scene) to demonstrate that the p-selection generalizes.
5. **Rename the "RANSAC" procedure** to something more descriptive (e.g., "randomized p-selection" or "max-distance sampling") to avoid misleading readers.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>