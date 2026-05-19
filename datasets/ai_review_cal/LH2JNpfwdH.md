- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5
Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes a unified framework for stylizing dynamic human videos that goes beyond 2D frame-by-frame stylization by leveraging Neural Radiance Fields. The method introduces a geometry-guided tri-plane representation for efficient scene encoding, uses composite NeRFs (one for the human in canonical space, one for the background) to enable novel view synthesis and human animation, and performs stylization in the rendered feature space. The paper claims to be the first approach enabling stylized novel views and animated humans from a monocular video input.

## Strengths

- **First unified framework for a genuine new task.** The paper systematically identifies a capability gap (Tables in Section 1): existing 2D video stylization methods cannot handle novel views or animation, and existing NeRF-based stylization methods cannot handle dynamic humans or novel poses. The proposed method is the first to combine all three capabilities (stylization, novel view synthesis, human animation) in a single framework.

- **Geometry-guided tri-plane shows measurable improvement.** The proposed encoding of 3D coordinates with geometric priors (via voxel discretization and U-Net encoding) outperforms direct tri-plane optimization, reducing temporal consistency warping error from 0.207 to 0.182 (Table 4). Visual results (Figure 3) confirm sharper contours and clearer background textures.

- **Superior temporal consistency against 2D baselines on original views.** On the NeuMan dataset, the method achieves the best warping error of 0.214, outperforming the nearest competitor LST at 0.226 (Table 1). This advantage is consistent across both datasets tested.

- **Ablation validates unified framework over two-stage pipeline.** The proposed joint approach (0.165 on the authors' dataset) beats the alternative of first rendering with NeRF then applying 2D stylization (best two-stage: AdaAttN at 0.179) in Table 3. This is corroborated by a user study with ~3000 votes on original views and ~5000 on novel views/animation (Figures 6–7) where users preferred the proposed method on both consistency and overall quality.

- **Practical efficiency advantage noted.** The tri-plane representation yields an approximately 70% inference speedup over MLP-based NeRFs, a meaningful practical improvement over prior NeRF stylization works.

## Weaknesses

### Fatal

None. The approach is structurally sound and the core contribution — a unified framework for a genuinely new task — is valid.

### Major

- **No quantitative metric for style transfer quality.** The paper claims a "superior balance between stylized textures and temporal coherence" but only the "temporal coherence" side is measured quantitatively (warping error / masked LPIPS). Style quality — how faithfully the textures and patterns of the style image are transferred — is assessed only through qualitative figures and a user study that asks about "overall performance" conflating both factors. A direct style metric (e.g., Gram-based style loss or CLIP score between the output and the style image) would be a straightforward addition that directly supports the paper's core claim.

- **Narrow ablation study limits validation of design choices.** Only two components are ablated: unified vs. two-stage pipeline (Table 3) and geometry-guided vs. vanilla tri-plane (Table 4). Several significant design choices receive no ablation: the error-correction network (Section 3.2), the composite NeRF strategy (separate human/scene NeRFs vs. a single one), the choice of Hadamard product over alternatives, the U-Net encoding vs. simpler alternatives, and the decoder architecture. The tri-plane ablation conflates three interventions (voxel discretization, positional encoding projection, and U-Net encoding) into one comparison, making it impossible to isolate which component drives the improvement.

### Minor

- **Evaluation of the headline capability (novel views and animation) is thin.** The paper's central claim is enabling **stylized** novel view synthesis and human animation. The evaluation of these capabilities relies on qualitative results (Figure 5), temporal consistency on the method's own rendered outputs (Table 2), and a user study (Figure 7). There is no comparison against the obvious alternative pipeline (e.g., animate with a dynamic NeRF, then stylize with a 2D method) on metrics that isolate geometry quality from stylization quality, nor any quantitative measure of how well the geometry generalizes to held-out poses or viewpoints.

- **StyleRF comparison is between mismatched settings.** StyleRF is designed for multi-view static scenes; applying it to monocular dynamic humans without describing how it was adapted puts it at a clear disadvantage. The paper acknowledges this difference in the caption ("The proposed method designed for dynamic scenes achieves much better performance compared to StyleRF") but still presents this as a main quantitative comparison. This inflates the apparent margin and should either be removed or accompanied by a fairer adaptation.

- **Geometry-guided tri-plane is underspecified for reproducibility.** The core novel component lacks several architectural details: the U-Net depth, number of channels, down/up-sampling scheme; the 3D voxel grid resolution (only voxel size 10mm is given, not the grid dimensions); and the exact projection operation from voxel coordinates to plane coordinates. The paper states that "more details can be found in supplementary material" at several points, but these details are essential for evaluating the main technical contribution.

- **No error bars or statistical significance reported.** All temporal consistency scores (Tables 1–4) are given as point estimates to three decimal places. With small differences (e.g., 0.165 vs. 0.161 on the authors' dataset in Table 1), it is unclear whether these differences are meaningful without variance estimates or significance testing.

- **User study lacks participant count and statistical details.** The paper reports "approximately 3000 votes and 5000 votes" without specifying the number of participants, how many comparisons each participant made, or conducting any significance tests on the preference ratios.

- **Runtime claim is unsupported by measurements.** The paper states "achieving a speedup of approximately 70% at inference time" without providing any actual timing numbers, GPU hardware, or measurement methodology.

### Trivial

- The method depends on human masks for background/foreground separation (Section 3.2), but the paper does not specify how these masks are obtained (manual annotation, off-the-shelf segmentation, SMPL projection?).

## Nice-to-Haves

- Ablating the error-correction network to quantify its effect on animation quality.
- Reporting per-scene training time and GPU memory usage, which are relevant for a method targeting creative tools.
- Providing video results (the paper references supplementary material that was stripped by the parser; video is essential for judging temporal consistency).

## Removed Points

*The following points from the reviews were assessed and determined to not meet the filtering criteria. They are preserved here for reference but should be treated with caution:*

- **Decoder architecture inconsistency** (Harsh Critic Section 3.4): The critic claims "3×3 kernel sizes without intermediate layers" conflicts with "comprised of convolutional and ReLU activation layers." These are consistent — the decoder can contain multiple conv+ReLU pairs each with 3×3 kernels, without intermediate pooling or upsampling layers. This is a misreading.
- **AdaAttN training not stated** (Harsh Critic Section 3.3): The paper clearly states that φ and ψ are "learned mappings" and the stylization stage uses content and style losses from AdaAttN. The training setup is adequately specified.
- **Color bias speculation** (Harsh Critic Experiments): The claim that the method "shifts the global color" is a subjective observation from figures that could be style-dependent, not an identified weakness.
- **Missing related works on dynamic NeRF methods**: Per policy, missing related works are not included as weaknesses.
- **Code/checkpoint not released**: Per policy, questioning the release status of artifacts is not included as a weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a direct style quality metric.** Compute a Gram-matrix-based style loss or CLIP-based style score between the stylized output and the target style image on the original-view frames. This directly supports the claim of "superior balance" between style quality and temporal coherence.

2. **Strengthen evaluation of novel views and animation.** Compare against the two-stage pipeline (dynamic NeRF + 2D stylization) on metrics that can isolate geometry quality (e.g., use the same stylization method on both the proposed method's and the baseline's rendered novel views). Report temporal consistency on animated sequences, not just on rendered frames.

3. **Provide a clearer, standalone description of the geometry-guided tri-plane.** Add a diagram or pseudo-code illustrating the voxelization, projection, aggregation, and U-Net processing steps. Report U-Net architecture details (depth, channels, down/up-sampling).

4. **Expand the ablation study.** At minimum, isolate: (a) the effect of the U-Net encoding alone (without geometry guidance), (b) the error-correction network, and (c) the composite NeRF vs. a single NeRF with time conditioning.

5. **Report error bars or confidence intervals** on all quantitative metrics. Clarify the number of runs. Report participant count and significance for user studies. Provide actual timing measurements to support the speedup claim.
