I have thoroughly read the paper and verified each claim from the reviewers against the actual text. Here is my consolidated review.

---

## Summary

MVTokenFlow addresses 4D content generation from a monocular video. The pipeline first uses a pretrained multiview diffusion model (Era3D) to generate multiview images per frame independently, then reconstructs a coarse dynamic 3D Gaussian field. From this coarse field, it renders 2D optical flow maps for all viewpoints, which guide a token propagation mechanism during a second multiview diffusion pass to improve temporal consistency. Finally, the regenerated spatiotemporally consistent images are used to refine the 4D field. The core technical novelty is using rendered 2D flows from a coarse 4D field to associate pixels across time for token propagation in the diffusion process.

## Strengths

- **Novel use of rendered 2D flows to guide token propagation for temporal consistency.** The idea of rendering 2D flows from a coarse dynamic 3D Gaussian field and using them to propagate diffusion tokens across frames on all viewpoints (not just the front view) is a principled and well-motivated approach to a known bottleneck in 4D generation. The ablation in Fig. 6 and Table 3 provides clear evidence that this flow-guided token propagation reduces flickering and improves FVD.

- **Coarse-to-refine pipeline that recovers 3D motion before refining appearance.** The two-stage design (reconstruct coarse 4D field → render flows → regenerate consistent multiview images → refine) is clean and effectively decouples motion learning from appearance refinement. Fig. 5 shows the coarse field's blurry output (c) vs. the significantly sharper refined result (b), and Table 3 confirms that removing the refinement stage degrades all metrics.

- **State-of-the-art quantitative results on all reported metrics.** On the Consistent4D benchmark, MVTokenFlow outperforms three recent baselines (Consistent4D, SC4D, STAG4D) across PSNR, SSIM, LPIPS, and CLIP scores (Table 1), with a particularly notable improvement in LPIPS (0.128 vs. the next best 0.199). Table 2 further shows superior novel-view video synthesis.

- **Computationally practical design.** The method leverages off-the-shelf Era3D without retraining and runs on a single A40 GPU, making it accessible to academic researchers.

## Weaknesses

### Fatal
None.

### Major

- **The main quantitative comparison (Table 1) does not include a direct temporal consistency metric (e.g., FVD) for baselines.** The paper's central technical challenge is temporal consistency across frames and views, and the headline contribution—token flow—is designed specifically to improve it. However, the metrics described for Table 1 (PSNR, SSIM, LPIPS for reference view alignment; CLIP for multi-view consistency) do not directly measure temporal coherence across frames. FVD (a standard temporal video quality metric) appears only in the ablation study (Table 3) and is not reported for any baseline method. This makes the paper's quantitative "win" in temporal consistency rest primarily on qualitative evidence (Fig. 3). While the reported per-frame metrics against reference videos do have *some* relation to temporal quality, they are not a substitute for a direct temporal metric. The authors should report FVD (or an equivalent temporal metric) for all baselines to substantiate the paper's central claim quantitatively.

### Minor

- **Concern about rendered flow quality on unseen viewpoints.** The flow loss (Sec. 3.2) is applied only on the front view, where RAFT-estimated flows provide supervision. For other viewpoints, the coarse field's rendered 2D flows rely on the shared 3D representation generalizing. The paper states that the coarse field "already produce[s] a reasonable 3D flow field" (Sec. 3.3) but provides no direct quantitative validation of flow quality (e.g., endpoint error on held-out views). The ablation in Fig. 5 shows that the overall pipeline works, which indirectly suggests the flows are adequate, but a direct diagnostic would strengthen confidence in this critical assumption.

- **Token propagation implementation is underspecified in several details.** The paper does not state which self-attention layer(s) the propagated features are extracted from, nor how the 2D flow warping is implemented (e.g., bilinear/backward warping, handling of boundary pixels or occlusions at the warp level). The paper does address occluded/disoccluded regions by limiting propagation to early diffusion steps (t ≤ τ = 20), which is a reasonable design choice, but the lower-level warp implementation is left unclear. This makes precise reproduction harder than it should be for the paper's core technical contribution.

### Trivial
None.

## Nice-to-Haves

- **Ablate keyframe interval and number of keyframes.** The paper sets a keyframe interval of 8 but does not study how this parameter affects the trade-off between propagation coverage and error accumulation. A sensitivity analysis would strengthen understanding of the method's robustness.

- **Validate coarse-field flow quality directly.** Computing flow endpoint error (EPE) against RAFT flows on held-out viewpoints from the coarse field's rendered videos would directly address the concern about generalization to unseen views.

- **The limitation section (Sec. 5) currently focuses only on multiview diffusion model capabilities.** A brief discussion of when token propagation itself can be expected to struggle (e.g., large motion, rapid occlusion changes, low-texture regions) would improve the paper's completeness.

## Removed Points

These points were removed from the review; treat them with caution.

- **"Only three baselines, missing Efficient4D, 4DGen, DreamGaussian4D"** — Removed because the paper explicitly states it compares with "recent available open-source methods" (line 113). The authors have justified their baseline selection. Demanding comparisons with methods that may not be open-source or compatible with the Consistent4D benchmark is not a valid weakness under the paper's stated scope. (Per rule: REMOVE if the paper's choices are defensible within its class.)

- **"Circular dependency is a significant methodological concern"** — Downgraded from the reviewer's "significant" framing to a Minor weakness. The coarse field is trained on multiview images from all viewpoints, not just the front view, so the shared 3D Gaussian representation encodes motion information across views. The flow loss on the front view provides direct supervision, while the multi-view rendering losses regularize the 3D motion field. The ablation evidence (Fig. 5, Table 3) shows the full pipeline works better than alternatives, which implicitly validates the flows. The concern is a legitimate nuance but not a structural flaw.

## Novel Insights

None beyond the paper's own contributions. The reviews raise standard evaluation-gap and reproducibility-detail concerns that are common in the 4D generation literature.

## Suggestions

1. **Report FVD (or another standard temporal coherence metric) for all baselines in the main comparison table.** This is the single most important improvement—it would directly verify whether the proposed token flow delivers its claimed temporal benefit over existing methods.

2. **Add a brief diagnostic for rendered flow quality on novel viewpoints.** Even a visual comparison of rendered flows vs. flows computed from the final refined videos (or a quantitative EPE computation on a subset of views) would substantially address the coarse-field generalization concern.

3. **Specify which self-attention layers are used for token propagation and the warp implementation details** (e.g., bilinear interpolation, occlusion masking) in the paper or supplement.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>