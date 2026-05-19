- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 3, 6
Now I have all the information I need. Let me produce the consolidated review.

## Summary
This paper tackles 3D garment deformation from a posed body mesh. It proposes a skinning-free approach that decomposes garment deformation into vertex positions (low-frequency shape) and vertex normals (high-frequency wrinkles), renders both as 2D images, and uses image transfer networks (with pretrained DINO and cross-attention) to predict deformation. A multimodal fusion optimization combines both modalities to recover the final 3D garment. The method achieves state-of-the-art results on VTO and TailorNet benchmarks across tight and loose garments.

## Strengths
1. **Skinning-free decomposition is clearly beneficial.** The ablation in Table 3 shows that two LBS-based variants (Canonical Image + LBS, LBS + Image Refine) with the same image-transfer framework yield markedly higher RMSE and Hausdorff distances than the proposed skinning-free method (e.g., on dress RMSE 96.2 and 89.1 vs. 82.9; on t-shirt 73.3 and 72.9 vs. 66.7). This directly validates the core claim that avoiding LBS artifacts improves accuracy.

2. **Pretrained DINO encoder and cross-attention each contribute to wrinkle quality.** Table 4 quantifies the drop when replacing DINO with ResNet-50 (dress RMSE 82.9→87.1, STED 0.193→0.204) and when removing body-garment cross-attention (RMSE 82.9→89.0, STED 0.193→0.214). Figure 6 visually confirms that these variants produce visibly smoother results.

3. **State-of-the-art quantitative results on both tight and loose garments across two benchmarks.** Tables 1 and 2 report the lowest RMSE, Hausdorff distance, and STED on all four garment types (t-shirt, dress, pants, skirt) compared to five baselines including both learning-based and physics-based methods. The gains are largest on loose garments (dress, skirt), which is precisely where skinning-based methods struggle most.

4. **Multimodal fusion optimization effectively combines position and normal priors.** Table 5 and Figure 7 show a clear progression: position initialization alone gives RMSE 88.7 on dress, normal fusion reduces it to 82.9, and adding edge length/normal consistency losses removes rim artifacts while improving STED from 0.198 to 0.193.

5. **Multi-view rendering with template projection avoids manual UV mapping.** Section 3.1 explains that projecting the template mesh (constant silhouette) from front/back views avoids self-occlusions and retains canonical shape priors. Figure 6 shows that alternative UV-mapping via xatlas produces complex islands that hinder pretrained encoders, while the proposed projection yields clean images.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **The normalization scheme for position/normal images is underspecified.** Section 3.1 states that vertex positions and normals are "linearly rescale[d] ... to fit RGB colors, i.e. within the range [0, 1]" (line 35), but does not specify whether this rescaling uses per-mesh min-max bounds, dataset-wide bounds, or fixed global bounds. This directly affects both reproducibility and the interpretation of what the decoder must learn. The description of `RGB(·)` as "the linear rescaling function" (line 44) provides no further detail. This should be clarified.

2. **No quantitative evaluation on cross-garment generalization.** Section 4.6 presents joint training on 50 dress garments from CLOTH3D but only shows qualitative results (Figure 8). Adding even a single metric (e.g., RMSE on a held-out test set) would substantially strengthen the generalization claim and match the rigor of the main experiments. The paper acknowledges this is a proof-of-concept, but the gap between qualitative-only and quantitative is noticeable.

3. **No runtime or inference time reported.** The paper contrasts learning-based methods favorably with physics-based simulation in terms of efficiency, and the fusion optimization runs for 100 steps per stage, but no actual wall-clock time is reported. Adding per-frame inference time (image transfer + optimization) would allow readers to assess the practical trade-off.

4. **Hyperparameter sensitivity is not discussed.** The loss weight λ_rn is set to 0.001 on t-shirt and 0.01 on other garments "based on their scales" (line 137), but no analysis of how performance varies with these weights is provided. A brief sensitivity study would demonstrate robustness to these choices.

5. **"Equivalently achieved" phrasing overstates the claim.** The abstract states "3D garment deformation can be equivalently achieved via 2D image transfer" (line 4), and the introduction repeats this (line 19). Given the discretization in rendering, multi-view interpolation for non-visible vertices, and the subsequent optimization to recover the full 3D mesh, "approximated" or "represented through" would be more precise than "equivalently."

### Trivial
- None.

## Nice-to-Haves
1. **A direct 3D regression baseline (skinning-free, without image projection) would help attribute the gains more precisely.** The paper's ablations isolate the skinning-free aspect (Table 3) and the image design choices (Table 4), but testing a direct 3D predictor — e.g., a graph network or MLP operating on body mesh embeddings with the same position+normal decomposition — would clarify whether the image representation itself provides additional benefit beyond the skinning-free decomposition. This is a useful direction for follow-up work but does not weaken the current contribution, since the paper already demonstrates the combination works and ablates its components.

2. **Including a comparison with automatic UV mapping as a full baseline (not just in the qualitative ablation) could further strengthen the case for multi-view projection.**

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- The harsh critic's speculation that per-mesh normalization "could limit generalization or introduce artifacts" — this is speculative; the paper works well empirically, and the issue is simply that the scheme needs specification, not that there is a known problem.
- The critic's statement about "a direct 3D predictor could plausibly match or exceed its performance" — this is speculative and not grounded in any evidence presented. The paper's ablations already show the image-based components individually help.
- The critic's framing of the missing direct 3D baseline as a "critical issue" — this overstates the severity. The paper's core contribution (skinning-free + image transfer) is verified; this is a decomposition-of-attribution question for follow-up work, not a fatal gap.

## Novel Insights
None beyond the paper's own contributions. The reviews largely affirm the paper's stated findings — that skinning-free decomposition avoids artifacts, that DINO and cross-attention improve wrinkle quality, and that multimodal fusion helps recover details — without uncovering unanticipated limitations or new interpretations.

## Suggestions
1. Specify the exact RGB normalization scheme (per-mesh, per-dataset, or fixed bounds) in the final version.
2. Add inference runtime (per-frame) in the experiments section.
3. Include at least one quantitative metric on the CLOTH3D cross-garment experiment.
4. Consider a brief sensitivity analysis on the fusion loss weights.
5. Soften "equivalently" to "represented through" or "approximated via" in the abstract and introduction.
