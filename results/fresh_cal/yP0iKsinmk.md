Now I have all the information needed. Let me synthesize the final review.

---

## Summary

AdaFlow proposes a training-free method for text-driven editing of minute-long videos (1000+ frames) on a single GPU. It introduces two innovations: (1) Adaptive Attention Slimming (AAS), which reduces the KV sequence length in extended self-attention by retaining only tokens most relevant to the query frame, and (2) Adaptive Keyframe Selection (AKS), which uses DIFT-based similarity to partition the video into content-homogeneous clips and select one representative keyframe per clip. The paper also contributes LongV-EVAL, a benchmark of 75 one-minute videos with 225 prompt-video pairs. Experimental results show AdaFlow achieves competitive or superior quality while requiring roughly half the inference time of the fastest baseline (24 min vs. 40+ min per video).

## Strengths

1. **Adaptive Attention Slimming (AAS) is a well-motivated, specific technical contribution.** Section 4.2 formalizes the observation that in extended self-attention, not all tokens are equally important for maintaining frame consistency. By selecting only the top-\(m\) tokens per query based on DIFT similarity heatmaps (Eq. 8), AAS directly tackles the quadratic memory bottleneck that has limited prior work to dozens of frames. This is a concrete, training-free mechanism whose value is evidenced by the method's ability to process 14+ keyframes jointly (Section 5.2) and to edit 1000+ frames in one pass.

2. **Adaptive Keyframe Selection (AKS) is a principled improvement over uniform sampling.** Section 4.1 and Algorithm 1 describe how AKS uses DIFT temporal heatmaps to segment the video into clips based on content changes, then selects one keyframe per clip. Figure 4 provides a clear qualitative ablation: without AKS, rapidly changing regions (a car entering the frame, a cat yawning) become blurry, whereas AKS preserves sharpness. This directly addresses a known limitation of TokenFlow's uniform keyframe sampling.

3. **The LongV-EVAL benchmark fills a genuine evaluation gap.** Section 5.1 introduces 75 one-minute videos with three editing prompts each (foreground, background, style), annotated via Video-LLaVA and GPT-4. Prior benchmarks focus on short clips (seconds), so this provides a standardized test bed for long video editing that the community can reuse. The code is anonymously released.

4. **Empirical evidence of efficiency and quality advantages is provided.** Table 1 shows AdaFlow achieves the best or second-best scores on VQ, OC, and SC while requiring only 24 minutes per video — roughly half the inference time of the closest competitor. Table 2 reports strong user preference (67.2% for video quality, 81.9% for temporal consistency). Figure 3 qualitatively demonstrates that AdaFlow maintains temporal coherence over 1000+ frames where baselines exhibit artifacts or inconsistency.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative metric measures prompt-to-edit fidelity.** The four automatic metrics in LongV-EVAL (FQ: frame aesthetic quality, VQ: DOVER video quality, OC: DINO frame-to-frame similarity, SC: CLIP similarity between *adjacent frames*) all assess video quality and temporal consistency — none measures whether the edited output actually follows the editing prompt. A method that made minimal changes to the source video could score well on OC and SC while completely failing the editing task. The user study (Table 2) asks participants about "video quality and temporal consistency," which also does not directly measure prompt alignment. The qualitative examples (Fig. 1, Fig. 3) demonstrate prompt-following, but this gap weakens the quantitative evaluation of the paper's central claim ("high-quality long video editing"). Standard metrics such as CLIP score between edited frames and the prompt, or CLIP directional similarity, would directly address this.

2. **The "order of magnitude" improvement from AAS is not quantified with a baseline comparison.** The abstract and introduction state that AAS "allows AdaFlow to increase the number of keyframes for translations by an order of magnitude." Section 5.2 states: "if the number of keyframes exceeds 14, pruning is initiated." Nowhere does the paper report how many keyframes can be jointly edited *without* AAS on the same GPU. If the baseline (TokenFlow or an AAS-ablated AdaFlow) already supports 14 keyframes, the "order of magnitude" claim is misleading. If it only supports 2–3 keyframes, that should be demonstrated. Without this ablation, the core technical claim is unverifiable from the presented data.

### Minor

3. **Segmentation protocol for baseline comparisons is underspecified.** The paper states: "Since TokenFlow, FLATTEN, and RAVE are unable to edit long videos in a single inference, we segment the long videos for editing. Based on their computational resource usage, we edit 128, 32, and 16 frames at a time" (Section 5.2). No details are given about whether segments overlap, how boundary artifacts are handled, or whether blending is applied. This omission makes it difficult to assess whether the reported quantitative advantages (Table 1) are partially artifacts of the comparison design.

4. **No variance or significance measures in quantitative results.** Table 1 reports point estimates for all metrics without standard deviations, confidence intervals, or significance tests. Given that the benchmark contains 225 editing tasks, reporting variance would help readers assess the reliability of the reported advantages.

5. **AAS's token dropping strategy could lose frame-level information from distant keyframes.** Section 4.2 selects top-\(m\) tokens based on DIFT similarity to the query frame. Tokens not in the top-\(m\) for any keyframe are dropped from *all* KV pairs. The paper does not discuss whether this could systematically discard information from keyframes that differ significantly from the query, potentially reducing the benefit of attending to multiple keyframes.

6. **Offline DIFT correspondences vs. online computation is not ablated.** Section 4.3 computes DIFT correspondences once at timestep \(t=0\) and reuses them across all denoising steps. This is an efficiency design choice. However, correspondences at \(t=0\) (clean latents) may differ from those at later, noisier timesteps. An ablation comparing offline vs. per-step correspondences would strengthen confidence in this design choice.

7. **AKS ablation is qualitative only.** Figure 4 provides a compelling qualitative comparison with/without AKS, but no quantitative ablation (e.g., temporal consistency scores with/without AKS) is provided.

### Trivial
None.

## Nice-to-Haves

- **Computational breakdown:** The paper reports 24 minutes per video. A breakdown (DDIM inversion, DIFT extraction, AKS computation, keyframe translation, latent propagation) would help readers identify bottlenecks.
- **Hyperparameter sensitivity for AKS:** The threshold (0.75) and sliding window parameters are likely content-dependent. A brief analysis varying these parameters would aid reproducibility.
- **Failure case discussion:** The paper acknowledges (Section 4.3) that motion-flow-based methods cannot handle structural modifications (e.g., adding new objects). A dedicated limitations section or failure analysis would improve credibility.

## Removed Points

**"Ten times longer" phrasing is loosely worded (Critic, Section-by-Section Notes).** The paper states AdaFlow edits "about ten times longer than the compared methods." TokenFlow edits 128 frames per inference; AdaFlow edits ~1000+. The ratio is ~7.8×, and "about ten times" is a reasonable colloquial approximation. This is a presentation nuance that does not affect the technical validity. *Reason for removal: not a substantive weakness; the claim is approximately accurate.*

## Novel Insights

The reviews surface one insight not foregrounded by the paper: the connection between the two contributions (AAS and AKS) is deeper than presented. AKS reduces the *number* of keyframes by selecting only representative frames, while AAS reduces the *token cost per keyframe* by slimming attention. Together, they attack the memory bottleneck from two orthogonal directions — cardinality and dimensionality — yet the paper treats them largely independently. A synthesis of how the two interact (e.g., does AKS make AAS more effective by reducing the number of diverse tokens competing for the top-\(m\) budget, or less effective by producing clips with homogeneous content where token-level slimming has less to gain?) would strengthen the framing.

## Suggestions

1. **Add prompt-alignment metrics to Table 1** — specifically CLIP score (edited frames vs. prompt) and CLIP directional similarity (source-to-target change). This directly addresses the most critical evaluation gap.
2. **Provide a memory-scaling ablation for AAS:** report GPU memory as a function of keyframe count *with and without* AAS. Report the maximum number of keyframes achievable at 80 GB budget in both conditions. This would substantiate the "order of magnitude" claim.
3. **Describe the baseline segmentation protocol** (overlap size, boundary blending, if any) in the main text or appendix.
4. **Include error bars or standard deviations for quantitative metrics** in Table 1.
5. **Add a quantitative ablation for AKS** (e.g., temporal consistency with/without AKS) to complement the qualitative Figure 4.

## Score and Decision

The paper makes genuine contributions — AAS and AKS are novel, well-motivated, training-free designs that together enable a clear engineering advance (1000+ frame editing on one GPU). The LongV-EVAL benchmark is a useful community resource. However, two significant evaluation gaps (no prompt-alignment metric, unquantified AAS baseline comparison) weaken the evidence for the paper's headline claims. These are addressable and do not invalidate the core contributions, but they must be fixed.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>