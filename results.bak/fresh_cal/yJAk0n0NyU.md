Now I'll produce the final consolidated review.

## Summary

This paper proposes BlockDance, a training-free acceleration method for Diffusion Transformers (DiTs) that identifies and reuses "Structurally Similar Spatio-Temporal (STSS) features"—the outputs of shallow/middle transformer blocks after the denoising structure has stabilized. By caching these high-similarity features at one step and skipping the first ~20 blocks in subsequent steps, BlockDance reduces per-step computation while maintaining output quality. A secondary contribution, BlockDance-Ada, learns an instance-specific reuse policy via reinforcement learning. The method is evaluated on three tasks (class-conditional image generation with DiT-XL/2, text-to-image with PixArt-α, and text-to-video with Open-Sora), showing 25–35% acceleration with minimal quality degradation relative to baselines like DeepCache and ToMe.

## Strengths

1. **Well-motivated, targeted feature reuse grounded in analysis.** The paper provides clear evidence (cosine similarity matrices in Figure 2, PCA visualizations in Figure 3) that shallow/middle block features stabilize early in denoising while deep block features continue to change, and that feature reuse should be restricted to the latter 60% of steps and to blocks ≤20. This analysis directly motivates the method's specific design choices and differentiates it from prior coarse-grained reuse strategies like DeepCache.

2. **Consistent quality advantage over baselines across diverse settings.** On PixArt-α (Table 1), BlockDance (N=2) achieves SSIM 0.852 vs DeepCache's 0.812 at comparable latency, with better FID (32.31 vs 34.35), CLIP score, IQS, and PickScore. On Open-Sora (Table 3), BlockDance (N=2) holds FVD close to the original (282.9 vs 282.1) while DeepCache degrades sharply to 371.6. This pattern holds across both image and video domains, supporting the claim that targeted reuse of structurally similar features outperforms indiscriminate reuse.

3. **Systematic ablations validating design choices.** Figures 8–10 isolate the effects of reuse frequency, reuse stage, and block depth. The ablations confirm that applying reuse before structure stabilizes (0–40% denoising) causes structural artifacts (Figure 9), and reusing blocks beyond index 20 degrades texture (Figure 10). These experiments directly support the paper's core hypothesis.

4. **Plug-and-play, training-free operation.** BlockDance requires no fine-tuning, architectural changes, or additional training, and is demonstrated across three different architectures (DiT-XL/2, PixArt-α, Open-Sora) spanning class-conditional, text-to-image, and text-to-video generation.

## Weaknesses

### Fatal
None.

### Major

1. **Unresolved discrepancy between claimed and (apparent) latency-based acceleration for DiT-XL/2.** The main text states that BlockDance accelerates DiT-XL/2 by 37.4% at N=2 and up to 57.5% at higher N. However, the Harsh Critic reports that Table 2 shows baseline latency 0.244s, BlockDance N=2 latency 0.190s (22.1% reduction), and N=3 latency 0.172s (29.5% reduction). These are far lower than the text's claims. Since Table 2 is embedded as an image in the text extraction, these numbers cannot be independently verified from the available material. The discrepancy is potentially serious because it affects one of the paper's central quantitative claims. If the table values are correct, the abstract's stated range of "25% to 50% acceleration" is also not met by this experiment (22–30% would be the accurate range), and the specific claims of 37.4% and 57.5% on lines 155 of the paper text would be wrong. The authors must clarify whether the text percentages or the table numbers are correct, and ensure consistency in the final version.

### Minor

2. **Time-conditioning mismatch is not discussed.** The method caches features \(F_t^i\) computed at time step \(t\) and feeds them into block \((i+1)\) during a reuse step at a different time step. In standard DiT architectures, each block receives the current time embedding via mechanisms like adaLN. The cached features were computed under the time embedding of the cache step, but reused under a different time embedding. The paper does not acknowledge this mismatch or explain why it does not cause degradation. The empirical results suggest it is tolerable, but a conceptual clarification would strengthen the paper and help practitioners assess transfer to other architectures with different conditioning mechanisms.

3. **BlockDance-Ada evaluation is narrow.** The adaptive variant is evaluated on only one model (PixArt-α with 10k captions) and one dataset (COCO validation). The improvement over fixed-strategy BlockDance (N=2) is marginal: acceleration of 32.0% vs 25.4% at similar FID (32.47 vs 32.31). The decision network has 0.08B parameters — described as "lightweight" but non-trivial. No evidence of generalization to other models (e.g., DiT-XL/2 or Open-Sora) is provided.

4. **No variance or statistical significance reported.** Latency and quality metrics are reported as point estimates without standard deviations or confidence intervals. For small quality differences (e.g., FID 32.31 vs 32.29 between BlockDance and PixArt baseline), it is unclear whether the difference is statistically meaningful. Latency measurements should include variance across runs.

5. **Memory overhead is ambiguously stated.** The paper reports cached feature sizes of 18MB, 4.5MB, and 72MB for the three models, but does not clarify whether this is per cache step or total accumulated memory. For video generation (72MB), this is non-negligible and should be contextualized.

6. **Ablation: asymmetry in reuse range across models not explained.** BlockDance applies reuse in the 40%–95% range for PixArt-α but 25%–95% for DiT-XL/2 and Open-Sora. The paper does not explain why structure stabilizes earlier in DiT-XL/2 and Open-Sora than in PixArt-α.

### Trivial

7. **Minor text inconsistency.** The paper states that DeepCache achieves "approximately 27% acceleration" on PixArt-α while Table 1 shows identical latency (0.355s) for DeepCache and BlockDance (25.4% acceleration). This suggests the percentages may be computed using different baselines.

## Nice-to-Haves

- For the time-conditioning concern: a simple cosine-similarity or MSE comparison between cached features (from the cache step) and the features that would have been computed if a full forward pass were run at the reuse step, for the first i blocks, would help close the conceptual gap.
- For BlockDance-Ada: applying the learned policy to a second model (e.g., DiT-XL/2) without retraining, or showing training convergence curves, would strengthen the contribution.
- A brief discussion situating BlockDance relative to step-distillation methods (when training-free moderate acceleration is preferable vs. when distillation's larger speedups with quality loss are acceptable) would help practitioners choose the right tool.

## Removed Points

- **"DeepCache numbers are identical latency" (re: Table 1)**: The Harsh Critic notes that DeepCache and BlockDance have identical latency (0.355s) but claims "27.1% acceleration" for DeepCache vs "25.4%" for BlockDance. This is a minor inconsistency in how percentages are computed, not a weakness of the method. It reflects a presentation nitpick that the reviewer themselves notes as "minor inconsistency."
- **"SD3 and Flux not empirically evaluated"**: The paper mentions these as supported models but does not evaluate them. This is a scope limitation the paper does not claim to have addressed. Demanding evaluation of every compatible model is scope creep.
- **"BlockDance-Ada training details sparse / no training curves"**: The paper provides key training details (10k samples, 100 epochs, batch size 16, learning rate 1e-5, optimizer Adam, reward model ImageReward, λ=2). Training curves are the kind of detail commonly deferred to an appendix, which may be stripped by the parser. Not a genuine weakness.
- **"Comparison with step-distillation asymmetric"**: The paper already acknowledges this asymmetry (line 145: "BlockDance, although requiring more inference time, achieves higher generation quality" vs PixArt-LCM). The reviewer's suggestion to add discussion is a nice-to-have, not a weakness.
- **"Decision network has 0.08B parameters — non-trivial"**: The Strength Finder praises this as a lightweight network. The Harsh Critic calls 80M non-trivial. Both are correct depending on perspective. Since 80M is ~13% of PixArt-α's parameters, this is more about framing than substance. The paper calls it "lightweight" relative to the base model, which is reasonable.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces that the paper's central insight—that shallow/middle DiT block features of stable structure are safe to reuse while deeper block features are not—is well-supported by the similarity analysis, but the evaluative discussion reveals two things the paper itself does not fully address: (1) the role of time conditioning in feature computation during reuse is a genuine architectural detail that the paper glosses over, and (2) the quantitative claims for the DiT-XL/2 experiment may be inflated relative to the reported table data. These are gaps the paper should close, not new insights.

## Suggestions

1. **Resolve the DiT-XL/2 latency discrepancy immediately.** Clarify whether Table 2 or the text percentages are correct, ensure all acceleration numbers are computed consistently, and adjust the abstract's claimed range if needed.
2. **Add a brief paragraph in Section 3.3** discussing why features computed under one time embedding can be reused under another (e.g., the time embedding primarily affects later blocks, or the adaLN in block (i+1) re-normalizes the cached features for the new time step).
3. **Report standard deviations or confidence intervals** for at least the primary latency and quality metrics (FID/SSIM/FVD) across multiple runs.
4. **Clarify memory footprint** — state whether the reported sizes are per cache step or total, and discuss implications for memory-constrained deployment.
5. **Give a brief justification** for why the reuse range differs between PixArt-α (40%–95%) and DiT-XL/2/Open-Sora (25%–95%).

## Score and Decision

The paper presents a clean, well-motivated idea with strong empirical evidence across multiple models and tasks. The core contribution (BlockDance training-free acceleration) is simple, effective, and clearly better than prior feature-reuse methods. However, the unresolved numerical discrepancy in the DiT-XL/2 experiment undermines confidence in the reported speedups. This must be corrected before the paper can be fully endorsed. The remaining weaknesses (time-conditioning discussion, narrow BlockDance-Ada evaluation, missing error bars) are addressable and do not invalidate the core contribution.

**MY FINAL SCORE: <score>5.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**