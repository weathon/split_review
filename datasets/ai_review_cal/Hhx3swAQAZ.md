- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have all the information I need. Let me write the consolidated review.

## Summary

ExVideo proposes a post-tuning method to extend video diffusion models (specifically Stable Video Diffusion) from generating 25 frames to 128 frames (a 5× increase), using only 1.5k GPU hours of training on a 40k-video dataset. The approach introduces three modifications to the temporal modules: extended trainable positional embeddings with cyclic initialization, an added identity-initialized 3D convolution layer, and fine-tuning of temporal attention parameters while freezing all other weights.

## Strengths

- **5× frame extension with remarkably low training cost**: The paper achieves a genuine 5× increase in output frames (25→128) using only 1.5k GPU hours on a modest 40k-video dataset, which is a concrete and verifiable efficiency claim. All other weights besides temporal modules are frozen, making this a practical post-tuning strategy.

- **Preserved generalization across styles and resolutions**: Qualitative demonstrations (Figures 3, 5) show the extended model generating coherent videos in unseen styles (flat anime, pixel art) and at various resolutions not seen during training, indicating that the base model's versatility survives the extension process.

- **Identity-initialized 3D convolution as a no-deterioration adapter**: Initializing the 3D convolution kernel with an identity matrix (center unit) and zeros elsewhere ensures that before training, the added layer is a no-op, preventing any degradation of the base model's outputs at initialization. This is a clean design choice grounded in adapter literature.

- **Visualized learning trajectory**: The optical flow visualizations across training steps (Figure 4) provide intuitive evidence that the model progressively learns temporal dynamics — from jittery frames to smooth camera motions and finally to complex layered motions — rather than simply memorizing short-motion patterns.

## Weaknesses

### Fatal

None.

### Major

- **Complete absence of quantitative evaluation**: The paper's central claims — that ExVideo "doesn't compromise quality," "preserves generalization," and "outperforms existing models in motion dynamics" — are supported by zero numerical metrics. No FVD, IS, CLIP score, or any standard video generation metric is reported. The entire "Case Studies" section is qualitative. Without quantitative evidence, the paper reads as a demonstration rather than a validated research contribution. This is the most significant weakness and directly limits the paper's credibility. (Verifiable: no quantitative metrics appear anywhere in the paper.)

- **No ablation of the proposed components**: The method introduces three distinct modifications: (1) extended trainable positional embeddings with cyclic initialization, (2) an added identity 3D convolution layer, and (3) fine-tuning of temporal attention parameters. No experiment isolates any single component. It is impossible to determine which modification drives the observed effects, whether any are redundant, or whether the method would work with fewer changes. (Verifiable: no ablation experiments are present.)

- **Uncontrolled and insufficiently documented comparisons**: The comparison in Section 4.4 shows only two hand-picked prompts, does not specify how baselines were configured (e.g., which text-to-image model they used, what seeds, whether outputs were selected), and concludes that "the majority of existing video synthesis models usually generate videos with minimal motion dynamics" based on this narrow qualitative comparison. As documented on the page, the paper states only what first-frame generator its own pipeline uses (Hunyuan DiT) and does not describe the baselines' setups. This does not invalidate the method, but it means the claimed advantage in motion dynamics is not substantiated.

### Minor

- **Vague description of the "cyclic pattern" for positional embedding initialization**: The paper states that extended positional embeddings are "initialized in a cyclic pattern, drawing upon the configurations of the pre-existing embeddings" (Sec. 3.2, line 72). The exact initialization scheme is not specified — is it a simple repetition, zero-interleaved, Fourier-based? This ambiguity hampers reproducibility, since initialization quality directly affects the model's ability to handle unseen temporal positions.

- **Missing training details**: The paper mentions the learning rate (10⁻⁵), batch size (1 per GPU), and hardware (8×A100s, 1 week), and that exponential moving averages are used for weight updates, but does not specify the EMA decay rate, the total number of training steps, or the convergence criterion used to stop training. While Figure 4 references 32k and 64k steps, the total step count is never stated.

### Trivial

None.

## Nice-to-Haves

- **Inference cost analysis**: The paper thoroughly discusses training efficiency but provides no analysis of inference time or memory for 128-frame generation versus 25-frame generation. This would help practitioners assess practical deployability.
- **Generalization to other base models**: The paper claims ExVideo is theoretically compatible with most video synthesis models but only tests on Stable Video Diffusion. Applying the method to at least one additional model (e.g., AnimateDiff, VideoCrafter) would strengthen this claim.
- **A controlled comparison protocol**: Future extensions would benefit from using the same text-to-image model and random seeds across all pipelines, and evaluating on a diverse set of standard prompts with multiple runs per prompt.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"No discussion of computational cost during inference"* — moved to Nice-to-Haves above (reasonable suggestion, not a core flaw).
- *"No generalization test on another base model"* — moved to Nice-to-Haves above (beyond the paper's stated scope; the paper tests SVD and claims theoretical compatibility).
- *"Specific implementation of gradient checkpointing is omitted"* — this is an implementation-level detail that is neither standard to report nor essential for reproducing the method.
- *"Failure rate for human portraits not quantified"* — the Limitations section (p. 7) acknowledges this difficulty qualitatively; requesting a quantified failure rate for a known limitation of the base model is beyond reasonable scope.
- *"Different text-to-image models used in comparisons"* — the harsh critic speculates that baselines used different text-to-image generators without evidence from the paper. The broader point about uncontrolled comparisons is already retained as a Major weakness; the speculation about specific different models is removed.
- *"Harsh critic's Strengthening the Paper on Its Own Terms (a/b/c)"* — these are suggestions (user study, temporal consistency metrics, ablations). Ablations are already listed as a Major weakness; the rest are moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add quantitative evaluation using standard video generation metrics (FVD on a benchmark like UCF-101 or MSR-VTT, CLIP score for text alignment, and a human preference study) to substantiate the quality claims.
2. Perform an ablation study isolating each of the three proposed modifications (trainable positional embeddings, identity 3D convolution, temporal attention fine-tuning) to identify which components drive the observed improvements.
3. Document the baseline configurations in comparisons explicitly (same/different text-to-image model, seeds, selection criteria) and report results on a systematic evaluation set rather than two hand-picked prompts.
4. Clarify the "cyclic pattern" initialization for positional embeddings with exact pseudocode or a mathematical description.
5. Report the EMA decay rate and total training steps explicitly.
