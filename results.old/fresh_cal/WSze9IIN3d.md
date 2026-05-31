Now I have verified all key passages. Let me produce the final consolidated review.

---

## Summary

This paper proposes progressive autoregressive video diffusion models, where frames in the attention window are assigned progressively increasing noise levels rather than a single uniform noise level. This allows for large overlaps between consecutive attention windows and smoother temporal transitions during autoregressive extension. The method is implemented by modifying only the noise scheduling and timestep embedding of pre-trained models (Open-Sora v1.2 and a modified variant), requiring no architectural change. Experiments at 1 minute (1440 frames) show improvements over replacement-based autoregressive baselines in dynamic degree, aesthetic quality, and imaging quality.

## Strengths

1. **Well-motivated progressive noise schedule** — The core idea (Sec 3.1, Eq. 4–5) of assigning linearly increasing noise levels across frames in the attention window is clearly described and conceptually sound. It reduces the noise-level gap between adjacent frames to T/S (compared to the large gap between clean condition frames and fully noisy frames in replacement-without-noise methods), enabling more fine-grained conditioning. The quantitative advantage over both replacement-with-noise and replacement-without-noise baselines on dynamic degree and scene-change count (Table 1) directly supports the value of this design.

2. **Sustained quality metrics over 1440 frames** — PA-InternalModel maintains dynamic degree, aesthetic quality, and imaging quality over the full 60-second duration, while baseline models (RW-InternalModel, RN-OpenSora, SVD-XT) show clear drops in these metrics as sequence length increases (Table 1, Fig. 3). The trend analysis over time strengthens the claim that the method avoids the typical degradation pattern of autoregressive video extension.

3. **Minimal architectural modification** — The method changes only the noise scheduling logic and timestep embedding (flatten/unflatten B×F dimensions, Sec 4.1); the underlying backbone (DiT) remains unmodified. This makes the approach architecturally lightweight and compatible with different video diffusion architectures, as claimed.

4. **Training-free applicability demonstrated** — PA-OpenSora-base, without any fine-tuning, outperforms RN-OpenSora-base on dynamic degree, aesthetic quality, and imaging quality while reducing scene changes (Table 1). This demonstrates practical applicability to existing pre-trained models that used masked pre-training, even if the theoretical justification for *why* it works training-free could be stronger.

5. **Ablation shows necessity of two key fixes** — The qualitative ablation (Sec 4.3, Fig. 4) demonstrates that removing chunk-by-chunk denoising causes rapid divergence and removing clean-frame retention causes frame-to-frame discontinuity. While only qualitative, this convincingly shows these modifications are essential to the method's practical success.

## Weaknesses

### Major

1. **Contradiction between "no quality degradation" claim and acknowledged degradation** — The abstract states the method generates videos "without quality degradation" (line 10), and similar claims appear at lines 32 and 120. However, the Discussion section (lines 344–347) explicitly states: *"Some slight errors remaining in the 'clean' latents... can be carried onto later frames, resulting in quality degradation"* and acknowledges the method *"could still generate videos with some degree of quality degradation over time if the base video diffusion model is not well trained."* This is an internal contradiction that undermines the paper's headline claim. The absolute "no quality degradation" framing should be conditioned or removed to match the paper's own honest assessment of its limitations.

2. **Uneven test sets across compared models, without confidence intervals** — PA-InternalModel uses 48 videos from 24 prompts, while most other models use 80 videos from 40 prompts; StreamingSVD uses 40 videos from 40 prompts (line 261). With these sample sizes, the absence of per-prompt breakdowns or confidence intervals makes it difficult to assess whether the reported differences are statistically significant. The paper acknowledges that three of six VBench metrics are "not discriminative" (line 277), meaning the quantitative case rests on a subset of metrics where the advantage is present but fragmented (e.g., SVD-XT has the best dynamic degree but worst quality; StreamingSVD has the best scene count). A more rigorous statistical treatment would strengthen the comparisons substantially.

### Minor

1. **Ablation of the two critical modifications is purely qualitative** — The chunk-by-chunk denoising and clean-frame retention (Sec 4.1) are presented as essential fixes that rescue the method from failure. Yet their ablation study (Sec 4.3) provides only qualitative comparisons with no VBench metrics. Since these engineering modifications are fundamental to making the method work, quantitative ablation results (e.g., VBench scores with/without each fix) would significantly strengthen the paper. Without them, a reader cannot distinguish how much the core progressive noise schedule contributes vs. the engineering workarounds.

2. **Training-free claim is weakly justified** — The paper asserts that Open-Sora's masked pre-training "allows \opensora to learn that the noise levels can be independent with respect to the latent frames" (line 212), thereby enabling training-free progressive autoregressive sampling. While the empirical results (Table 1) support that it does work, the paper provides no analysis of *how* the model handles per-frame timestep conditioning without fine-tuning (e.g., whether the model actually attends differently to frames with different timesteps, or whether the gains come from simply having clean frames in the window). The justification is a brief logical leap rather than a supported analysis.

3. **Missing runtime/memory comparison** — The paper claims "the additional computational cost at inference time is minimal" (line 40) but provides no runtime or memory numbers. Given that the method extends the attention window from S to S+C frames (keeping clean frames), quantifying the cost relative to simpler sliding-window approaches would substantiate this claim and help practitioners assess the method's practical overhead.

4. **Chunk-by-chunk granularity blunts the fine-grained claim** — The chunk-by-chunk fix (Sec 4.1) assigns the same noise level to all C=5 latents in a VAE chunk. This means the actual per-frame noise level granularity is coarser than the per-frame framing in the abstract and method description. While still finer than the baselines (which use a single noise level for all frames), the method should be more precisely characterized as operating at chunk-level granularity.

### Trivial

None.

## Nice-to-Haves

- Add confidence intervals or per-prompt breakdowns for the main VBench metrics, especially given the uneven test set sizes.
- Include a quantitative ablation comparing progressive vs. uniform noise levels while keeping chunk-by-chunk and clean-frame tricks fixed.
- Provide a user study or pairwise preference judgment to support the qualitative superiority claims, since the quantitative metrics are not decisive across all dimensions.
- Report whether the method continues to generate coherent video beyond 1 minute, since the paper discusses world simulator applications.
- Analyze why the chunk-by-chunk fix resolves the cumulative error (e.g., is it due to 3D VAE temporal dependencies within a chunk?).

## Removed Points

These points were raised in the reviews but are removed from the main assessment for the reasons stated:

- *"RW-InternalModel trained for 3× more steps than PA-InternalModel makes comparison unfair"* — This asymmetry actually *strengthens* the paper's case: PA achieves better results despite less training. If the baseline training protocol was suboptimal, that is a separate concern, but more training steps favoring the baseline does not undermine the comparison.

- *"The test measures video extension not text-to-video"* — The paper explicitly addresses this (lines 264–265): "Since our focus is on long video generation, we focus on the video extension capability of the models rather than the text-to-short-video generation capability." This is an appropriate scoping decision, not a weakness.

- *"The chunk-by-chunk fix contradicts the fine-grained claim"* — The method is still substantially more fine-grained than the baselines (which assign one noise level to all frames). The contradiction is overstated; this is better framed as a minor precision issue.

- *"Related Works reads like a catalog"* — Subjective stylistic assessment without concrete evidence.

- *"Trend plots not shown with proper axes or error bands"* — The referenced figures exist in the original submission (Fig. 3/fig_score_over_time). I cannot evaluate figure quality from text extraction alone.

- *"Method does not generalize beyond 1 minute"* — The paper's stated scope is 1 minute; this is a scope limitation, not a flaw.

- *"Weaknesses about missing appendix content, proofs, or references"* — These sections are stripped by the PDF extraction process and exist in the original submission.

- *Generic weaknesses about dataset/model scale* — The current scale is adequate for the paper's claims; larger-scale evaluation would strengthen but is not required.

- *Strengths about "important problem" or generic praise* — Removed as non-specific.

## Novel Insights

The reviews surface a tension that the paper does not fully resolve: the core idea (per-frame progressive noise levels) is elegant and well-motivated, but the method's practical success depends heavily on two engineering modifications (chunk-by-chunk denoising and clean-frame retention) that are not part of the core proposal. The qualitative-only ablation leaves open the question of whether a simpler approach (e.g., sliding window with large overlap) might achieve similar results. Additionally, the contradiction between the absolute "no quality degradation" claim in the abstract and the nuanced limitations discussion reveals an interesting pattern: the paper honestly identifies its own limitations but does not align its headline claims with that honesty. The training-free result on Open-Sora is empirically interesting but the theoretical understanding of why it works lags behind the empirical observation.

## Suggestions

1. **Reconcile the "no quality degradation" claim with the Discussion.** Either condition the claim explicitly (e.g., "without significant quality degradation under our experimental conditions") or remove the absolute phrasing from the abstract and introduction.

2. **Add quantitative ablation metrics.** Run the same VBench evaluation on the two ablated variants (no chunk-by-chunk, no clean frames) and report results in a table. This would resolve the central question of whether the core progressive schedule contributes beyond the engineering fixes.

3. **Provide per-prompt breakdowns or confidence intervals for the main metrics.** Since test sets are uneven across models, include per-prompt scores in supplementary material and compute standard errors or bootstrapped confidence intervals for the aggregate numbers.

4. **Include a runtime/memory comparison table.** Report inference time per frame and peak GPU memory for PA vs. RW vs. RN on the same hardware and attention window configuration.

5. **Strengthen the training-free justification** by adding a small analysis experiment, e.g., comparing prediction error when timesteps are per-frame vs. uniform in Open-Sora, or visualizing attention patterns under different noise assignments.

## Score and Decision

The paper presents a genuinely interesting and well-motivated idea with reasonable empirical support. The progressive noise scheduling is a clean conceptual contribution, and the experimental results consistently show advantages over standard autoregressive baselines. However, the paper is held back by (a) an internal contradiction in its central claim about quality degradation, (b) uneven evaluation that lacks statistical rigor, and (c) insufficient quantitative validation of the engineering modifications that are essential to the method's success. These are significant but addressable weaknesses; they do not invalidate the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>