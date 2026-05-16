Now I have all the verification I need. Let me produce the consolidated final review.

## Summary

This paper proposes ExVideo, a post-tuning method to extend the temporal capacity of video diffusion models (specifically Stable Video Diffusion) from 25 frames to 128 frames. The approach modifies three temporal modules: it extends positional embeddings with a cyclic initialization, adds an identity-initialized 3D convolution layer, and fine-tunes temporal attention parameters. Training is conducted with parameter-efficient techniques (freezing non-temporal blocks, mixed precision, gradient checkpointing, flash attention, DeepSpeed) on 40k videos using 8 A100 GPUs for one week. The paper presents qualitative results across diverse styles and resolutions, along with optical flow visualizations of the training progression.

## Strengths

- **Memory-efficient 5× frame extension with clearly documented engineering optimizations.** The paper achieves extension from 25 to 128 frames using only 1.5k GPU hours on 8 A100 GPUs with a dataset of 40k videos. The training recipe is concretely described: freezing all parameters outside the temporal blocks, mixed precision training, gradient checkpointing, flash attention, and DeepSpeed sharding. This combination makes a 5× length extension feasible with limited compute and is a genuine practical contribution.

- **Preservation of generalization across unseen styles and resolutions is qualitatively demonstrated.** The generated examples (Figures 2 and 4) show the extended model producing coherent videos in styles (flat anime, pixel art) and resolutions (1024×576, 768×768) that were absent from the training dataset. This provides initial evidence that the extension does not collapse the base model's adaptability, though it remains purely qualitative.

- **Principled identity initialization for the added 3D convolution layer.** Initializing the central kernel unit as an identity matrix with remaining parameters set to zero ensures that the added layer does not alter video representations before training, providing a clean starting point. This is a thoughtful design choice that avoids degrading the pre-trained model's behavior at initialization.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative evaluation whatsoever.** The paper's experimental section is titled "Case Studies" and contains only qualitative visual examples and optical flow visualizations. No standard video generation metrics are reported — no FVD, IS, CLIP score, frame consistency, or user preference. The paper's core claim that "the substantial increase in video length doesn't compromise the model's innate generalization capabilities" cannot be verified without numbers. The field standard for video diffusion papers (even lightweight adaptation papers) includes quantitative evaluation, and its complete absence is a structural gap. This is the single most serious weakness.

2. **No comparison against the baselines the paper itself identifies.** The introduction explicitly categorizes three existing strategies for longer videos (training on long clips, streaming/sliding window, frame interpolation) and criticizes them (e.g., streaming leads to "lower video coherence" and "error accumulation"). Yet the paper never empirically compares ExVideo against any of these alternatives. Even a simple baseline — e.g., generating overlapping 25-frame clips with the base SVD and blending, or using frame interpolation to upsample the base model's output — would contextualize the contribution. Without this, the claim that ExVideo is preferable to existing approaches is unsupported.

3. **No ablation studies isolating the three design choices.** The method introduces three modifications to temporal modules: (a) extended positional embeddings with cyclic initialization, (b) an additional identity 3D convolution layer, and (c) fine-tuning temporal attention parameters. The paper provides no ablation to determine which components drive the extension capability, whether all are necessary, or what the gain of each is. A reader cannot assess whether the identity convolution alone (without attention tuning) would suffice, or whether the cyclic initialization matters. This undermines the scientific contribution and makes the design choices appear arbitrary.

These three gaps are independent and jointly severe. Each individually weakens the paper; together they prevent verification of the method's effectiveness, superiority, or internal necessity.

### Minor

1. **"Parameter-efficient" claim is not quantified.** The paper states the method is "parameter-efficient" and "exceptionally memory-efficient" but provides no concrete numbers: no trainable parameter count, no memory consumption compared to full fine-tuning or training from scratch, no inference-time FLOPs comparison. While the training setup (8 A100s, 1 week, batch size 1 per GPU) is reported, and only temporal blocks are trained, the relative efficiency gain is not substantiated. Adding a simple table (trainable params vs. total params, peak memory vs. an unoptimized baseline) would address this.

2. **Cyclic initialization of positional embeddings is under-specified.** The paper states extended embeddings are "initialized in a cyclic pattern, drawing upon the configurations of the pre-existing embeddings" but does not define the procedure precisely. Is it simple repetition of the 25 original positions? Interpolation? A formula or pseudo-code would be needed for reproducibility.

3. **Comparison with other models (Section 4.4) is insufficiently controlled.** Only two prompts are shown. The comparison pits the authors' pipeline (text-to-image model + extended SVD) against other text-to-video models without controlling for the first frame, guidance scales, or random seed. While the qualitative difference in motion dynamics is visually apparent, the uncontrolled setup limits what can be concluded.

4. **No analysis of quality degradation over frame count.** A key question for any temporal extension method is whether quality degrades as the frame index increases (e.g., frame 100 vs. frame 5). The paper provides no plot or metric tracking quality across the 128 frames.

### Trivial
- The kernel size of the added identity 3D convolution layer is not specified (the paper says "central unit ... initialized as an identity matrix" but does not state the kernel dimensions).

## Nice-to-Haves
- A small-scale human evaluation (e.g., preference between ExVideo outputs and a stitched-baseline at matched lengths) would strengthen the qualitative claims.
- An analysis of failure cases beyond the brief mention of human portraits in the Limitations section (e.g., examples of truncation or artifact accumulation).
- Inference wall-clock time comparison: how long does generating 128 frames take vs. generating 25 frames and upsampling?

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not explain whether resolution adaptation was needed or how it was handled"** (from Harsh Critic, Section-by-Section Notes). The paper explicitly states: "Given the model's design to accommodate varying resolutions, we opt to conduct the training at this resolution." This is an explanation. The criticism is factually incorrect and is removed.

- **"The statement that 3D convolution layers are 'retained in their original form' is unclear — are they frozen or trainable?"** (from Harsh Critic). The paper states "All parameters outside the temporal block are fixed while training" (Figure 1 caption) and "All parameters except the temporal blocks are frozen" (Section 3.3). Since 3D convolution layers are part of the temporal blocks (as shown in the architecture figure), they are within the trainable subset. "Retained in their original form" refers to architectural preservation, not frozen status. The paper is sufficiently clear on this point.

- **"Superior motion dynamics compared to existing models"** (from Strength Finder). This claimed strength conflicts with a verified weakness: the comparison (Section 4.4) is uncontrolled (different pipelines, no shared first frame, no metrics, only two prompts), so the paper cannot substantiate this claim as a strength. Per rules, when a strength and verified weakness conflict, the weakness wins.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no perspective that the paper itself does not already articulate or imply.

## Suggestions

1. **Add quantitative evaluation before resubmission.** Report FVD on a standard benchmark (e.g., UCF-101, MSR-VTT, or a held-out set), CLIP score for text alignment, and a frame-consistency metric (e.g., warping error or LPIPS between consecutive frames). This is the single change that would most strengthen the paper.

2. **Add at least one concrete baseline comparison** against streaming (e.g., generating multiple 25-frame clips with the base SVD and conditioning each new clip on the last frame of the previous one) and frame interpolation (e.g., generating 25 frames and interpolating to 128 frames). This would contextualize the method's value relative to the alternatives the paper itself discusses.

3. **Run a three-way ablation** that disables each component separately: (a) no identity convolution, (b) no temporal attention fine-tuning, (c) no positional embedding extension (use original positions and pad/truncate). Report a key metric (e.g., FVD) for each variant.

4. **Quantify the "parameter-efficient" claim**: report the number of trainable parameters vs. total model parameters, peak GPU memory usage vs. an unoptimized full-fine-tuning baseline, and relative training cost.

5. **Precisely specify the cyclic initialization** with a short formula or algorithm, and state the kernel dimensions of the added convolution.

## Score and Decision

The paper presents a plausible and practically motivated method for extending video diffusion models. The engineering optimizations are concretely described and represent a real practical contribution. However, the evaluation is critically insufficient: the complete absence of quantitative metrics, the lack of any comparison against the baselines the paper itself identifies, and the absence of ablation studies make it impossible to assess whether the method works, how well it works, or why it works. These are structural gaps, not presentation issues, and they prevent acceptance in the current form.

The contribution is potentially valuable, and the method is well-described. With substantial additions to the evaluation (metrics, baselines, ablations), the paper could meet the bar for publication. In its current form, however, the evidence does not support the claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>