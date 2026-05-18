Now I have enough information to write the consolidated review. Let me synthesize everything carefully.

---

## Summary

This paper introduces ExVideo, a post-tuning method that extends the frame generation capacity of video diffusion models. Applied to Stable Video Diffusion (SVD), ExVideo increases the output from 25 to 128 frames (5×) using only ~1.5k GPU hours on 40k videos, while freezing most parameters and extending only temporal modules. The method proposes three architecture-specific extensions: (1) retaining but not modifying 3D convolutions, (2) fine-tuning temporal attention, and (3) replacing positional embeddings with extended trainable ones initialized in a cyclic pattern, plus an identity-initialized 3D conv adapter. Qualitative results show generalization to unseen styles and resolutions.

## Strengths

- **Parameter-efficient 5× extension with low training cost.** ExVideo extends SVD from 25 to 128 frames using only 1.5k GPU hours (8×A100 for one week) on a 40k-video dataset, with all non-temporal parameters frozen, mixed precision, gradient checkpointing, Flash Attention, and DeepSpeed (Section 3.3). This cost is orders of magnitude below training a long-video model from scratch, directly supporting the paper's core efficiency claim.

- **Preservation of base model generalization.** After post-tuning, the extended model generates coherent videos in styles not seen in the training data (e.g., flat anime, pixel art in Figure 2) and at resolutions beyond the fixed training resolution (Figure 4). This demonstrates that the extension does not destroy the base model's versatility — a crucial requirement for practical adoption.

- **Systematic strategy covering three temporal module architectures.** The paper does not present a single monolithic trick but specifies tailored modifications for 3D convolutions (identity-initialized adapter), temporal attention (fine-tuning), and positional embeddings (cyclic trainable extension) (Section 3.2, Figure 1). This design is architecture-aware and provides a reusable framework for other video diffusion models.

- **Training progress visualization confirms learning of long-term motion dynamics.** Figure 3 shows optical flow at different training steps (before training, after 32k steps, after 64k steps), illustrating a clear progression from jittery output to smooth camera movement to complex layered motions. This provides direct evidence that the post-tuning learns meaningful long-range temporal structure beyond what the original 25-frame model can produce.

## Weaknesses

### Major

- **No quantitative evaluation of video quality.** The paper contains zero automated metrics — no FVD (Fréchet Video Distance), no CLIP score, no frame-consistency measure, and no user study. The entire empirical case rests on cherry-picked still frames and optical-flow visualizations (Figures 2–6). Without quantitative evaluation, the reader cannot determine whether the claimed "coherent videos of up to 128 frames" maintain acceptable quality relative to the original SVD at 25 frames, or whether quality degrades as frame count increases. This is the single most significant weakness: the core claim of "enhancing capability" is not backed by measurable evidence. For a video generation paper at a top venue, FVD is the expected standard, and its absence is a critical gap.

- **No ablation study of design choices.** The method introduces several design decisions — cyclic positional embedding initialization, an identity-initialized 3D convolution adapter, fine-tuning only temporal attention, and freezing everything else. None of these choices are empirically justified. Which component drives the improvement? Would fine-tuning alone suffice without the identity conv? How sensitive are results to the initialization scheme? Without ablations, the contribution reads as an ad-hoc collection of heuristics rather than a principled, validated extension strategy. This is not a wishlist item; it is a standard expectation for a methods paper proposing multiple interacting components.

### Minor

- **Training details are incompletely reported.** The paper does not state: (1) the total number of training steps (only intermediate checkpoints at 32k and 64k steps are referenced in the visualization section, but the final step count after one week of training is not given); (2) the frame length or temporal duration of the videos in the OpenSoraPlan training set; (3) how training videos are preprocessed/sampled to match the target 128-frame sequences; and (4) any loss curves or convergence behavior. Additionally, the "cyclic pattern" used to initialize the extended positional embeddings is described only as "drawing upon the configurations of the pre-existing embeddings" — it is unclear whether the existing 25 embeddings are simply repeated, interpolated, or otherwise arranged to fill 128 positions. These gaps make the work harder to reproduce and assess.

- **The comparison with other models (Figure 6) is uncontrolled.** ExVideo uses Hunyuan DiT to generate the first frame, whereas compared models (AnimateDiff, VideoCrafter, etc.) generate videos from text alone. This confounds the base image quality with the video extension capability. The paper also claims "superior capability" for generating motion dynamics based solely on a few qualitative examples without controlling for the number of frames generated by each competitor. A fairer comparison would hold the first frame constant across methods or compare image-to-video generation directly.

- **No comparison against straightforward baselines using the same base model.** The paper could compare ExVideo against inference-time strategies that use the original SVD without post-tuning, such as generating overlapping 25-frame clips with stitching/conditioning, or frame interpolation from 25 to 128 frames. These baselines would isolate whether the post-tuning actually adds value beyond what the base model can already do. Currently, the paper only compares against entirely different models with different architectures and training data.

### Trivial

None.

## Nice-to-Haves

- Reporting loss curves and final training loss would provide confidence in convergence.
- A larger random sample of outputs (e.g., side-by-side grids from multiple prompts) rather than hand-picked examples would strengthen the qualitative argument.

## Removed Points

- **"The paper does not state whether all videos are used at 512×512 resolution":** The paper explicitly states "The videos in this dataset maintain a resolution of 512×512" (Section 3.3). This criticism is factually incorrect.
- **"The number of training steps is not given":** The paper does reference 32,000 and 64,000 training steps as intermediate checkpoints in the training visualization (Section 4.2). The total final step count is not given, but this partial information partially addresses the concern. The essence (total steps not stated) is retained as a minor weakness above.
- **Strength Finder claims about specific resolutions (e.g., "1024×576, 576×1024 in Figure 4"):** These numerical values are not stated in the paper text and appear to be inferred from figures. The general claim about resolution generalization is retained as a strength.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the method that the authors themselves did not already articulate. The core idea — borrowing LLM context-extension principles (cyclic positional embedding + frozen base + fine-tuned temporal attention + lightweight adapter) and applying them to video diffusion — is the paper's own contribution and is correctly presented as such.

## Suggestions

1. **Add quantitative evaluation as the highest priority.** Report FVD and CLIP score on a held-out test set comparing (a) the original SVD at 25 frames, (b) ExVideo at 128 frames, and (c) ExVideo evaluated on the first 25 frames only (to isolate quality degradation from length extension). Without this, the paper cannot be evaluated as a scientific contribution.

2. **Run an ablation study** removing the identity convolution and replacing cyclic initialization with naive random initialization. This would clarify which design choices are essential and fits squarely within the method's own evaluation framework.

3. **Add a controlled comparison** where the first frame is held constant across all compared methods (e.g., generate a single first frame and feed it to all image-to-video models), so that quality differences are attributable to the video generation pipeline rather than the initial image.

4. **Report the total training steps** and describe the cyclic initialization of positional embeddings more precisely (e.g., "the 25 original embeddings are tiled/repeated 5× with stride X to cover 128 positions, then fine-tuned").

5. **State the frame length distribution** of the OpenSoraPlan training videos and how videos are sampled/cropped to 128-frame sequences for training.

## Score and Decision

The paper proposes a well-motivated, parameter-efficient method for extending video diffusion model outputs from 25 to 128 frames, with plausible qualitative results and clearly documented training cost. However, the evaluation is fundamentally incomplete for the claims being made: there are no quantitative metrics, no ablation studies, and no controlled comparisons. By current standards at top venues for video generation research, the absence of FVD alone is a critical gap that prevents proper assessment of the core contribution. The paper would require substantial revision — primarily a proper quantitative evaluation — before it could be considered for acceptance.

**Overall assessment:** The idea has merit, but the empirical validation is insufficient.

**Score:** The paper's contribution is interesting but under-validated. On a scale where 10 is a strong accept and 0 is a desk reject, this paper falls in the weak reject range for a top venue due to the absence of standard evaluation practices.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>