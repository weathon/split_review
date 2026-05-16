Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper introduces a mutual information shaping technique for 3D Gaussian Splatting that enforces correlations between Gaussians belonging to the same object by shaping activations of the attribute-decoding network, rather than Jacobians. The core claims are: (1) activation shaping (vs. Jacobian shaping) preserves the correlation structure across successive parameter perturbations, enabling consistent multi-step editing without re-shaping; (2) the training is lightweight (~7% of Gaussians sampled, ~1 minute fine-tuning on a single GPU); and (3) the method achieves an 11% mIoU improvement on 3D segmentation over prior state-of-the-art.

## Strengths

- **Lightweight fine-tuning with significant efficiency gains**: The method samples only ~7% of Gaussians during training and completes the fine-tuning stage in about 1 minute on a single RTX 3090 (Sec. 4.1). This is a concrete and well-supported advantage over existing scene-editing methods that require optimizing the entire Gaussian set.

- **Quantitative improvement in 3D segmentation**: On the LERF-Mask dataset, the method outperforms prior work by an average of 11% mIoU (Table 1). The comparison against JacobiGS (same pipeline with JacobiNeRF-style MI loss substitution, Sec. 4.2) provides a controlled ablation that partially isolates the effect of the proposed activation shaping from other components.

- **Empirical demonstration of multi-step editing consistency**: The object movement experiments (Fig. 6) provide compelling qualitative evidence that JacobiGS diverges after multiple perturbations while the proposed method maintains coherent motion and leaves uncorrelated objects intact, directly validating the paper's central claim.

- **Breadth of applicability**: The method is demonstrated across static scenes (Mip-NeRF 360, LERF), dynamic scenes (D-NeRF), and outdoor scenes (NERDS 360), with applications including segmentation, object removal, movement, and re-colorization, showing generality beyond a single scenario.

## Weaknesses

### Major

- **Insufficient theoretical derivation for the core claim of post-perturbation consistency**: The transition from Eq. 4–6 to Eq. 7 is too compressed. Eq. 7 states that `cos(∂Φ_i^(d), ∂Φ_j^(d)) ≈ cos(∂h_i^(0), ∂h_j^(0))` — that the similarity of Jacobians after *d* perturbations approximates the pre-perturbation activation derivative similarity. The paper says this holds "when ∂h_i^(0) and ∂h_j^(0) point in the same or opposite directions," which is exactly what the contrastive loss enforces. However, the key missing step is *why* this approximation survives successive perturbations. The paper mentions that the network undergoes a "conformal transformation in its tangent space" (Sec. 3.3, line 67) but offers no proof or even a sketch of this claim in the main text; the derivation is deferred ("A detailed derivation and the proof..."). This leaves the central theoretical advantage over JacobiNeRF incompletely supported. The empirical results are strong enough that this is not fatal, but it is a significant gap in the paper's argument.

- **Editing evaluation is entirely qualitative**: Object removal (Fig. 5) and object movement (Fig. 6) are shown only as rendered images. No quantitative metrics (LPIPS, FID, CLIP consistency, background reconstruction accuracy, or user study) are provided. For removal, there is no evaluation of background fidelity against held-out views of the empty scene. For movement, there is no measure of shape distortion or background drift after repeated perturbations. The paper claims "significant performance improvements" for editing tasks, but without quantitative evidence the strength of this claim cannot be assessed. This is the most important missing piece for a paper whose title and abstract foreground scene editing.

### Minor

- **Ablation does not cover segmentation or editing**: The ablation study (Table 2) reports PSNR on reconstruction only. While the comparison against JacobiGS (Sec. 4.2) provides some evidence for the MI shaping's effect on segmentation, a dedicated ablation on segmentation mIoU — and ideally on editing quality — would substantially strengthen the evidence. The paper cannot fully disentangle how much of the segmentation gain comes from the activation shaping vs. the mask generation pipeline (SAM+DEVA) and the contrastive learning framework itself.

- **Missing implementation details**: The paper does not specify (a) the architecture or initialization of the attribute-decoding MLP Φ_a (number of layers, hidden dimensions), (b) the strategy for sampling the ~7% of Gaussians during fine-tuning (is it random, mask-aware, contribution-based?), or (c) per-scene results with variance/confidence intervals for the segmentation numbers. These affect reproducibility and the interpretability of the efficiency claim.

- **InfoNCE/Exact MI precision gap**: The paper states it is "maximizing the mutual information" between Gaussians (Eq. 3, Sec. 3.2), but the loss in Eq. 8 is the InfoNCE loss, which is a lower bound on mutual information, not the exact quantity. The paper cites van den Oord et al. (2018) but should explicitly acknowledge that it maximizes a lower bound rather than exact MI, for precision.

### Trivial

- The notation ∂h_i^(0) is defined as "the Jacobian ∂∂Wh(l)" — this is garbled in the extracted text and would benefit from clearer typesetting (e.g., ∂h_i^(0) = ∂h_i/∂W^(l) or similar).

## Nice-to-Haves

- A simple quantitative metric for editing: e.g., LPIPS against the original scene over unedited regions after removal, or bounding-box consistency of moved objects across perturbation steps.
- Per-scene tabulation of segmentation mIoU to assess variance across scenes.
- A brief discussion of how the viewing direction input d (used in Φ_a for rendering robustness) interacts with the editing perturbation, if at all.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"No ablation isolating the effect of mutual information shaping on segmentation performance"* — The paper does compare against JacobiGS (same pipeline, different MI loss), which functions as a controlled ablation. The 11% improvement may be against Gaussian Grouping (which has multiple architectural differences), but there is a direct JacobiGS comparison. This criticism is partially incorrect and is downgraded accordingly.

2. *"Viewing direction d is mentioned but never used in the editing procedure"* — The viewing direction is an input to the attribute-decoding network for rendering quality (Eq. 2, line 103), not an editing parameter. This is a misunderstanding of the architecture.

3. *"The paper should clarify whether the editing perturbation uses the same Jacobian or an approximation based on activations"* — Sec. 3.7 explicitly states "we perturb the attribute decoding network by applying the average Jacobian ∂Φ_a of user-selected Gaussians." The paper is clear on this point.

4. *"The appendix was removed by the parser..."* — Per hard rules, weaknesses about missing appendix content are removed. The main text must stand on its own, but the parser-stripped appendix is not an author error.

5. *"The claim that network weights optimized solely by reconstruction loss fail to reveal meaningful correlations is not backed by any quantitative metric"* — Fig. 2(a) provides a visual illustration; this is a motivational claim, not a quantitative result, and the qualitative comparison with Fig. 2(b) is appropriate for its role.

6. *"The paper does not report the number of Gaussians in the scenes"* — This is standard to vary per scene in 3DGS and is a minor detail that would appear in a full version or supplement; the key point is the 7% sampling fraction relative to the total per scene.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally different interpretation of the work than what the authors present.

## Suggestions

1. **Strengthen the theoretical section**: Provide an explicit 1- or 2-layer MLP case study showing that activation alignment is preserved under weight perturbation. Either prove the "conformal transformation" claim or present a clear intuitive argument with an illustrative example. Deferring the proof to an appendix the reader cannot assess weakens the paper's core argument.

2. **Add quantitative editing metrics**: At minimum, report LPIPS on the unedited region after object removal (against the original reconstruction), and either CLIP consistency or bounding-box alignment for object movement. Even one quantitative editing benchmark would substantially raise the evidential bar.

3. **Add a segmentation ablation table**: Keep all components (mask generation, MLP architecture, training schedule) fixed and compare three conditions: (i) no MI shaping, (ii) Jacobi-style shaping (baseline), (iii) proposed activation shaping. This would cleanly attribute the 11% gain to the proposed method rather than the overall pipeline.

4. **Report per-scene results with variance** for the segmentation metric, and specify the Gaussian sampling strategy (e.g., random uniform, mask-weighted, contribution-based) for the 7% subset.

## Score and Decision

The paper addresses an important problem — efficient, coherent 3D scene editing — and the core idea (activation shaping for consistent multi-step editing) is novel. The segmentation results are quantitatively strong and the efficiency numbers are impressive. However, the theoretical justification for the paper's central claim is compressed and incomplete, and the editing evaluation — which is central to the paper's framing — rests entirely on qualitative comparisons without any quantitative metrics. These are significant limitations. The paper would be competitive at a strong venue with the suggested additions but in its current form falls short of the rigor needed for acceptance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>