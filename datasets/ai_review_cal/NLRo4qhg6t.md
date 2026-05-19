- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 3, 1, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper proposes HIWE, a novel grid-based positional encoding for neural radiance fields that allocates model parameters (via a bounding-box hierarchy of adjustable sizes/densities) in proportion to a scene importance distribution. The key idea is to concentrate representation capacity on semantically important regions (e.g., objects of interest) while using coarser resolution elsewhere, enabling fast training (<15 min) with a small model (<100 MB) on large outdoor scenes. The encoding leverages hardware-accelerated ray-box intersection (OptiX) for efficient feature indexing.

## Strengths

- **Novel importance-weighted grid encoding that departs from uniform-resolution approaches.**  
  The bounding-box hierarchy (Sec. 3.3) lets important regions be represented by many small, high-resolution local grids while unimportant regions use fewer, larger boxes. This is a principled improvement over hash-grid methods (Instant-NGP, TensoRF) that treat all scene regions equally.

- **Hardware-accelerated indexing enabling practical use of 10 k–100 k bounding boxes.**  
  Casting bounding-box lookup as a batched ray-box intersection problem and using NVIDIA OptiX (Sec. 3.5) is a non-trivial engineering contribution that makes the hierarchical encoding tractable at scale.

- **Qualitative evidence of improved reconstruction in designated important regions.**  
  Figure 5 clearly shows sharper detail in the graffiti region under HIWE vs. nerfacto-big, while the paper honestly acknowledges degradation in the grass. This visual demonstration supports the paper's core trade-off claim.

- **Competitive or better full-image metrics with a much smaller model footprint.**  
  Table 1 reports HIWE achieving favorable PSNR/SSIM/LPIPS across multiple drone-captured scenes with a model under 100 MB and 15 min of training — substantially smaller and faster than the large Instant-NGP models (>750 MB, hours) required for comparable quality on these scenes.

## Weaknesses

### Fatal
None.

### Major

- **Full-image metrics do not directly measure the paper's core claim.**  
  The paper's central thesis is that HIWE delivers "higher quality representation for the important parts of the scene" (Abstract, line 21). Yet the entire quantitative evaluation (Table 1) reports only **global** PSNR/SSIM/LPIPS. A method that deliberately trades quality in unimportant regions for quality in important ones will not be properly assessed by metrics that average over the entire image. The qualitative example (Fig. 5) illustrates exactly this trade-off — better graffiti but worse grass — but no region-specific metric (e.g., PSNR inside the importance mask) isolates the benefit. This is not a fatal flaw (the qualitative evidence is real and the global numbers are not worse), but it leaves the headline claim empirically under-supported. The paper needs to report quality within the important regions to directly validate its core contribution.

### Minor

- **Incomplete efficiency comparison with Table 1 baselines.**  
  The paper claims "on-par or faster training times and small model sizes" relative to state-of-the-art, and provides model size (<100 MB) and training time (15 min) for HIWE. A coarse comparison to Instant-NGP (>750 MB, 4–5 hours) is given (line 33), but model sizes and training times are not reported for the actual baselines in Table 1 (nerfacto, nerfacto-h22, nerfacto-big, TensoRF). Without this information, the efficiency advantage over the specific methods being compared is unverifiable.

- **Several hyperparameter values needed for exact reproducibility are omitted.**  
  The paper reports L=8 and β=1.1, but does **not** specify numerical values for: N_bbox (total number of bounding boxes), N_{p0} (points per bounding box for sizing), or the feature dimension per grid corner. These are needed for an independent implementation (anchored: lines 106, 112).

- **No ablation of the importance-weighted pixel sampler.**  
  Section 3.4 describes a separate pixel-sampling component that prioritizes important regions during training. Its individual effect on convergence or final quality is never isolated from the encoding itself. Without an ablation, readers cannot attribute observed improvements to the encoding versus the sampling strategy.

- **Tension between the SfM importance function and the paper's stated motivation.**  
  Section 3.1 motivates deprioritizing high-frequency textures (grass, sand) as "less important" (line 35). However, the SfM-density importance function (Sec. 3.2) marks regions near object surfaces — which includes highly textured grass that produces dense SfM points. The paper does not discuss whether the SfM importance function actually deprioritizes the regions the motivation identifies as wasteful, nor does it visualize the SfM point cloud for the evaluated scenes.

- **No sensitivity analysis for key design choices.**  
  The number of hierarchy levels (L=8), the grid-size constant (β=1.1), and the total number of bounding boxes are used without ablation. A reader cannot assess how robust the method is to these choices.

### Trivial

- The comparison to 3D Gaussian Splatting (Sec. 4.4, Table 2) is acknowledged by the authors as tangential ("a fair and direct comparison... is challenging"). It adds little and could be condensed or removed.

## Nice-to-Haves

- Report region-specific metrics (PSNR/SSIM/LPIPS computed only on pixels that project into high-importance volumes or user-drawn masks). This would directly test the paper's headline claim.
- Characterize the trade-off quantitatively: plot gain in important regions versus loss in unimportant regions as a function of the importance distribution or bounding-box allocation.
- Ablate the pixel sampler by training HIWE with and without it.
- Add a sensitivity study for L, β, and N_bbox.

## Removed Points

These points from the reviewers are flagged to be removed — treat them with caution:

1. **"TensoRF results absent from Table 1"** (Harsh Critic, point 2). The paper states (line 148) that TensoRF results are included. Table 1 is an embedded image in the parsed PDF; I cannot verify its content. This criticism is unverifiable and removed.
2. **"2.3 dB PSNR claim not present in the table"** (Harsh Critic, point 3). The paper states "increase in PSNR of up to 2.3 dB" — "up to" indicates a maximum over scenes/baselines. Since Table 1 is an image, the specific numbers cannot be checked. Removed as unverifiable.
3. **"cube_enclosing_points is underspecified"** (Harsh Critic, point 4). The paper defines it as "returns minimum volume of a cube centered at c_bbox that encloses N_{p0} points" (line 112). The algorithmic idea (find k-th nearest neighbor distance) is clear enough for the paper's scope. Removed as too nitpicky.
4. **"Differentiability of the indexing operation is not explained"** (Harsh Critic, point 4). This reflects a misunderstanding: the indexing (finding which bounding boxes contain a point) is a forward-pass lookup and does not need to be differentiable. Gradients flow through the interpolation of corner features (Eqs. 2–3), which is standard. Removed.
5. **"No variance/confidence intervals"** (Harsh Critic, "Missing Parts"). Single-run evaluation is the norm for large-scale NeRF benchmarks in NeRFstudio; requesting CIs is a field-standard concern, not a paper-specific gap. Removed.
6. **"Baselines may not have been given fair iteration budget"** (Harsh Critic, point 2). The paper states (line 148) "We evaluate all our trained models... for 30k training iterations." All methods used the same budget. The claim that this might favor HIWE is speculation. Removed.

Strengths removed from the Strength Finder (generic / unsupported):
- "Favorable comparison to 3D Gaussian Splatting in storage efficiency" — while factually reported (86 MB vs. >1 GB), the comparison is acknowledged by the authors as tangential and not central to the paper's contribution. The strength itself is weak because the methods differ fundamentally; the storage advantage is expected. Demoted to the Trivial/Nice-to-have category.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear evaluation gap (region-specific metrics absent) but do not generate a fundamentally new observation about the problem or method.

## Suggestions

- Add a per-region quantitative evaluation: compute PSNR/SSIM on pixels whose rays intersect high-importance volumes, and separately on the complement. This directly validates the core claim.
- Include a systematic efficiency table with model sizes and training times for every baseline in Table 1.
- Disclose N_bbox, N_{p0}, and the feature dimension. These are small additions that substantially improve reproducibility.
- Add an ablation of the pixel sampler (Sec. 3.4) to disentangle its effect from the encoding.
- Discuss or visualize the SfM point cloud for the test scenes to clarify whether the SfM importance function is consistent with the paper's stated goal of deprioritizing grass-like textures.
