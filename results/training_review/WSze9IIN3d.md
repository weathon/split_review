Now I have a thorough understanding of the paper. Let me produce the consolidated final review.

## Summary

This paper proposes progressive autoregressive video diffusion models (PA-VDM), which assign progressively increasing noise levels across frames during denoising rather than a single noise level. This allows existing short-video diffusion models (DiT-based) to generate long videos up to 1440 frames (1 minute at 24 FPS) without changing their architectures. The method works training-free on models that support per-frame independent noise levels (e.g., Open-Sora v1.2 via its masked pre-training) and can be further improved by fine-tuning. Results are demonstrated on two backbones and compared against replacement-based autoregressive baselines (RN, RW) as well as StreamingT2V and SVD-XT.

## Strengths

- **Novel and well-motivated core idea**: The progressive per-frame noise schedule is a conceptually clean departure from the uniform-noise-level approach used in prior autoregressive video diffusion methods. The intuition — that later (higher-uncertainty) latents should attend to earlier (more certain) latents — is clearly explained and grounded in the diffusion framework. The insight that this enables near-total attention-window overlap (F−1 latents) with no extra computation is a genuinely useful property (Sections 3.1–3.2, Algorithm 1).

- **Architecture-agnostic and partially training-free**: The method requires no architectural changes — only modifications to the noise scheduling and training/inference procedures. The paper demonstrates this on two backbones (Open-Sora and a modified variant). Notably, PA-\opensora-base works training-free on the publicly available Open-Sora v1.2 model (leveraging its masked pre-training) and shows consistent improvements over RN-\opensora-base (Section 4.2, Table 1). This provides a verifiable proof-of-concept.

- **Effectiveness on the internal model**: PA-\internalmodel achieves the best overall quality on VBench metrics among all compared methods, with the best aesthetic and imaging quality, substantially better dynamic degree than most baselines, and the ability to maintain these metrics over 1 minute (Table 1, Figure 3). The qualitative results on the project website support these claims.

- **Clear exposition**: The paper is well-structured, with pseudocode, equations, and figures that make the method easy to follow. The ablation study (Section 4.3), though only qualitative, clearly illustrates the necessity of the two key practical components (chunking and clean-frame keeping).

## Weaknesses

### Fatal
None.

### Major

1. **Incomplete baselines relative to SOTA claims**: The paper claims "state-of-the-art results on long video generation" (abstract, introduction, discussion) but does not compare against several directly relevant methods cited in the Related Work — FreeNoise, FreeLong, Gen-L-Video, Vid-GPT, and SEINE. These methods address the same problem (extending video diffusion models to generate longer videos) and are acknowledged as related work. The only competing long-video method used as a baseline is StreamingT2V. Without comparisons to these established baselines under a shared evaluation protocol, the SOTA claim is not adequately supported. This does not invalidate the method's value, but the paper's headline assertion overreaches the experimental evidence.

2. **Quantitative evaluation is thin for the strength of the claims**: 
   - Only 80 videos are generated (40 prompts, 2 videos each), with even fewer for PA-\internalmodel (48 videos) and StreamingSVD (40 videos). No statistical significance tests (confidence intervals, bootstrapping, paired tests) are reported, making it unclear whether differences between methods are meaningful.
   - Three of six VBench metrics (subject consistency, background consistency, motion smoothness) are acknowledged as "not discriminative" — the paper honestly notes this, but it means the evaluation effectively rests on only three metrics (dynamic degree, aesthetic quality, imaging quality), plus the scene-change count which can be trivially near-perfect for static videos (as RW-\internalmodel demonstrates).
   - The ablation study (Section 4.3) is purely qualitative — only visual comparisons are shown for the two critical components (chunk-by-chunk denoising and clean-frame keeping). Quantitative VBench metrics for these ablations would substantially strengthen the paper.

### Minor

1. **Best results rely on a non-public model**: The strongest quantitative results (PA-\internalmodel) come from a "modified variant of Open-Sora" trained on a proprietary dataset (1M videos + 2.3B images) that is not released. This limits reproducibility of the headline numbers. However, this is partially mitigated by the training-free PA-\opensora-base results on the public Open-Sora model, which show consistent (if more modest) improvements — the core claim does not rest exclusively on the internal model.

2. **The practical method diverges from the elegant formulation**: Sections 3.1–3.2 present a clean progressive-noise formulation (each latent at a different noise level), but Section 4.1 reveals that this fails in practice — it requires chunking latents together (treating groups of latents as one noise level) and keeping clean frames in the attention window. These are presented transparently, but the paper does not provide a theoretical explanation for *why* the ideal progressive schedule causes cumulative divergence. The gap between the idealized formulation and the working implementation is larger than the paper's structure suggests.

3. **Evaluation focuses on video extension, not unconditional text-to-long-video**: All experiments condition on real initial frames (16–17 frames for internal model / Open-Sora, 1 frame for SVD-XT and StreamingSVD). The variable-length initialization for text-to-long-video is described (Section 3.2) but not experimentally evaluated. The paper acknowledges this, but the practical scope of the validated results is narrower than the title and abstract imply.

4. **No standard deviations or confidence intervals**: Mean metrics in Table 1 are reported without variance information despite uneven sample sizes across models (40–80 videos). This makes it impossible to assess the reliability of the reported differences.

### Trivial
None.

## Nice-to-Haves

- A quantitative ablation (VBench metrics) for the chunking and clean-frame components, alongside the qualitative comparisons.
- Reporting variance (std/CI) on the main metrics.
- A larger evaluation set with more prompts and statistical significance testing.
- Comparing against FreeNoise/FreeLong as training-free baselines, which would be feasible without retraining.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Section 2 does not discuss or compare to other autoregressive approaches like FreeNoise's sliding-window temporal attention or Gen-L-Video's parallel-decoding"* — Removed because Section 2 (Background) is specifically scoped to describe the two replacement methods (RW and RN) that the paper uses as baselines. Other methods are discussed in the Related Work section (Section 5), not the Background. This is a misreading of the paper's structure.

- *"The claim that PA-\internalmodel 'maintains' metrics over time is based on visual inspection of trends; no test for degradation is provided"* — Partially weakened: visual inspection of metric-over-time plots (Figure 3) is a standard way to assess degradation in this literature. While statistical tests would be stronger, the visual evidence is not invalid. Moved here for overstating the concern.

- *"The paper's scientific contribution rests on a black-box model"* — Removed as overstated: the paper provides training-free results on the public Open-Sora model (PA-\opensora-base) which supports the core contribution independently. The non-public model is an additional demonstration.

- *"The method requires two critical engineering fixes that are not predicted by the stated principle"* — Weakened to Minor weakness #2 above. The paper does explain the fixes and why they are needed (3D VAE chunk constraints), so this is not a fatal gap, but the lack of theoretical justification for why the ideal schedule fails is a valid concern.

- *"3 of 6 VBench metrics not discriminative... scene changes is confounded: static videos trivially achieve near-perfect scores"* — The paper acknowledges this and analyzes the trade-off: RW-\internalmodel has near-perfect scene changes but poor dynamics. Moved from a standalone criticism to incorporated into Major weakness #2.

## Novel Insights

The reviews collectively surface an interesting tension in the paper: the method's *conceptual novelty* (progressive per-frame noise levels) is clear and well-motivated, yet the *working system* relies on two engineering components (chunking, clean-frame keeping) that are not derivable from the progressive-noise principle alone. A deeper analysis of *why* the ideal schedule fails — e.g., visualizing how 3D VAE chunk boundaries interact with per-frame noise levels to cause divergence — would strengthen both the intellectual contribution and the practical guidance for future work. The training-free Open-Sora results are arguably the cleanest evidence for the core idea, since they require no fine-tuning and thus isolate the effect of the noise schedule itself, yet the paper's strongest claims
