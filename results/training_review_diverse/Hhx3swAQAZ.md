Now I have thoroughly verified the paper content and the reviewer's claims against the source text.

Let me produce the final consolidated review.

## Summary

This paper proposes ExVideo, a post-tuning method for extending video diffusion models to generate longer videos. Applied to Stable Video Diffusion, the method increases output from 25 to 128 frames (5×) using 1,500 GPU-hours on a 40K-video dataset. The approach modifies three temporal components—fine-tuning temporal attention, extending positional embeddings with cyclic initialization, and adding an identity-initialized 3D convolution—while freezing all other parameters. The paper presents qualitative case studies across diverse styles, resolutions, and a comparison against other models.

## Strengths

- **Significant frame extension with concretely stated training cost**: The method achieves 5× frame extension (25→128 frames) with 1,500 GPU-hours on 8×A100 GPUs and a 40K-video dataset. These numbers are explicitly reported in the abstract and Section 3.3, providing a concrete baseline for the method's resource requirements.

- **Architecture-aware extension design**: The paper identifies three common temporal module types (3D convolution, temporal attention, positional embedding) and designs separate strategies for each (Section 3.2, Figure 1). The identity-initialized 3D convolution is a clean design choice that ensures the added component does not alter representations before training, and the approach is described in sufficient detail to be applicable to other video diffusion architectures beyond SVD.

- **Qualitative evidence of generalization preservation**: Figures 2 and 3 demonstrate that the extended model handles diverse styles (flat anime, pixel art) and resolutions (1024×576, 896×1152) not seen during training. This supports the claim that the base model's generalization capabilities are retained after extension.

- **Concrete engineering optimizations for memory efficiency**: Section 3.3 lists five specific techniques used to enable 128-frame training on 8 GPUs (parameter freezing, mixed precision, gradient checkpointing, Flash Attention, DeepSpeed sharding). These are actionable details that strengthen the reproducibility and practical utility of the work.

- **Principled motivation from LLM context extension**: The paper explicitly draws inspiration from LLM techniques (RoPE, ALiBi, LongLoRA; Section 2.3) to justify the post-tuning framing, connecting the video extension problem to an established literature.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative evaluation of video quality.** The entire evaluation section is titled "Case Studies" and consists entirely of qualitative still frames and optical-flow visualizations. No standard video generation metrics are reported—no FVD, no CLIP score, no user study, no frame-wise similarity scores, no temporal consistency metrics. The paper's central claims are that ExVideo generates "coherent videos" and "does not compromise the model's innate generalization capabilities." These are empirical claims that require quantitative backing. Without any metrics, the reader cannot distinguish representative results from cherry-picked examples, and the paper's core contribution remains unsubstantiated by rigorous evidence. This is the most significant weakness.

2. **No ablation study isolating the method's components.** The method modifies three architectural elements (extending positional embeddings, fine-tuning temporal attention, adding an identity 3D convolution). The paper provides no experiment isolating which components drive any observed improvement. Minimal ablations such as (a) full ExVideo, (b) ExVideo without the identity 3D convolution, and (c) ExVideo with only fine-tuned temporal attention (no extended positional embeddings) would directly test the method's design. Without this, the paper's claims about the necessity or benefit of its specific design choices are unsupported.

3. **Invalid comparison with other video synthesis models.** Section 4.4 compares ExVideo against "several existing video synthesis models" using a pipeline where Hunyuan DiT generates the first frame, which is then fed to the extended SVD (an image-to-video model). This is not a controlled comparison: ExVideo receives a high-quality text-to-image first frame as an anchor, whereas the other models are presumably generating from text alone. The asymmetry favors ExVideo, making any conclusion about "superior capability to generate videos with significant movements" uninterpretable. The comparison should either be controlled (same first frame given to all image-to-video models) or described as a demonstration rather than an evaluation.

### Minor

1. **Limited efficiency and scalability analysis.** The paper reports a single training cost (1,500 GPU-hours) and claims "memory-efficient" and "parameter-efficient" performance, but provides no systematic data. Missing elements include: comparison of inference memory/time for 128 vs. 25 frames, study of how quality scales with training data size or steps, and measurement of the method's memory footprint relative to the original model. These are useful but not fatal omissions—the reported training cost and the listed engineering optimizations do provide partial support.

2. **Unsupported claim about other models' motion dynamics.** Section 4.4 states that "most existing video synthesis models usually generate videos with minimal motion dynamics" without citing evidence or providing a controlled comparison to support this claim.

### Trivial

- The Pexels URL in the footnote is truncated in the parsed version, though the primary dataset URL (OpenSoraPlan) is fully present and functional. (Parser artifact.)

## Nice-to-Haves

- A comparison against a simple frame-interpolation baseline (generate 25 frames with SVD, then interpolate to 128) would ground the claim that such approaches are inadequate (Section 1). The paper argues this in prose but never tests it.
- An inference cost analysis (memory, generation time for 25 vs. 128 frames) would strengthen the "memory-efficient" claim.
- Evaluation on a subset of a standard benchmark (e.g., UCF-101) with FVD would substantially strengthen the paper.
- Reporting the number of trainable parameters and the exact kernel size/padding of the identity 3D convolution would improve reproducibility.

## Removed Points

- **Strength Finder's "Empirical demonstration of improved motion dynamics" (comparing with other models)**: This strength is based on the same comparison (Section 4.4) that is identified as invalid above. Since the verified weakness (invalid comparison setup) wins, this claimed strength is removed.
- **Harsh Critic's complaint about "dataset URL is broken"**: This is a PDF parsing artifact; the primary OpenSoraPlan URL is complete and functional. Per rules, parser artifacts are not author errors.
- **Harsh Critic's mention of "training hyperparameters are minimal"**: The paper provides learning rate, batch size, GPU count, training duration, loss function/scheduler consistency, and EMA usage. This is a reasonable level of detail for this paper type.

## Novel Insights

The harsh critic correctly identifies the paper's central evaluation gap. However, there is a subtle tension not noted by either reviewer: the paper positions ExVideo as a *general* post-tuning method compatible with "the majority of existing video synthesis models," yet it validates it only on Stable Video Diffusion. The claim of generality rests on the architectural commonalities described in Section 3.1, but no demonstration is provided on a second architecture (e.g., AnimateDiff's temporal attention or a DiT-based model). This limits the evidence for the claimed generality, though it does not invalidate the contribution on SVD itself.

## Suggestions

1. **Add quantitative evaluation as the highest priority.** Report FVD on a standard benchmark (UCF-101 or a subset of MSR-VTT for long videos). Even a small user study (20–50 participants rating coherence/quality) would be far better than the current qualitative-only evaluation.
2. **Add an ablation study** with at least three conditions: full ExVideo, ExVideo without the identity 3D convolution, and ExVideo without extended positional embeddings (using naive extrapolation instead).
3. **Replace the current model comparison** with a controlled setup: provide the same first frame to ExVideo and to the original SVD (generating up to 25 frames), or compare against other *image-to-video* models given the same input.
4. **Report inference costs** (GPU memory, time per video) for both the original 25-frame and extended 128-frame models.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>