Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes Binary Spherical Quantization (BSQ), a parameter-free quantization method that projects visual embeddings onto a hypersphere and applies binary quantization. Combined with a Vision Transformer encoder/decoder using blockwise causal masking, BSQ-ViT achieves a unified architecture for both image and video tokenization. The method delivers state-of-the-art reconstruction quality on ImageNet (rFID 0.41, 43% better than SDXL-VAE) and UCF-101 (rFVD 4.10 vs 8.62 for MAGVIT-v2) with 2.4× higher throughput, while the bounded quantization error and factorized entropy computation enable stable training and efficient codebook usage.

## Strengths

1. **State-of-the-art reconstruction quality with higher speed**: BSQ-ViT achieves rFID 0.41 on ImageNet-1k val (36-bit), a 43% reduction compared to SDXL-VAE (0.72), while being 2.4× faster (45.1 vs 18.9 images/s per GPU, Table 1). On video, it reduces rFVD on UCF-101 from 8.62 (MAGVIT-v2) to 4.10 with L=36 (Table 2).

2. **Simple, parameter-free quantizer with clear advantages over VQ/LFQ**: BSQ's implicit codebook on the hypersphere grows exponentially with L with no learned parameters. The ablation (Table 4) shows BSQ consistently improves with larger L (rFID 2.66 at L=18 vs 4.51 at L=10), while VQ saturates beyond 16K entries (rFID worsens from 4.27 to 6.61). LFQ collapses with ViT (0.6% code usage, rFID 30.7), while BSQ maintains 93.8% code usage.

3. **Efficient factorized entropy computation**: The soft quantization probability factorizes into independent Bernoulli distributions per dimension (Eq. 5), reducing entropy computation from O(2^L × L) to O(L). The ablation (Table 6b) shows the factorized approximation (0.212 ms) achieves nearly identical rFID (2.86 vs 2.76 for group size 6) while running fastest.

4. **Unified image/video architecture with practical speed advantages**: The blockwise causal masking (Section 4.2) allows joint training on mixed image/video data and variable-length video inference without padding overhead. Fine-tuning an ImageNet-pretrained tokenizer on videos yields dramatic improvements (rFVD drops from 342 to 11.62, Table 2). On 1920×1080 video, BSQ-ViT achieves 6.1 FPS (encode+entropy coding+decode), outperforming VCT (1.4 FPS) and H.264 (2.6 FPS) (Table 4).

5. **Thorough ablation studies**: The paper systematically ablates losses (commit, entropy components, LPIPS, GAN), group sizes for entropy approximation, and the role of ℓ2 normalization, providing good insight into what makes BSQ work.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The bounded quantization error (Eq. 6) is asserted without derivation or citation.** The bound $\mathbb{E}_\vu[d(\vu,\hat\vu)] < \sqrt{2 - 2/\sqrt{L}} < \sqrt{2}$ is stated as fact, and the paper claims this leads to better gradient fidelity during training. While the bound itself is plausible and the empirical results independently validate the method, a brief derivation (or at minimum a citation to a known result) would allow readers to verify the claim. This is a real gap in the theoretical argument, but it does not undermine the paper's empirical contributions.

2. **The video compression evaluation is limited.** The paper shows only a single bitrate operating point for the proposed method on each benchmark, and the comparison to standards has mixed results: competitive with H.264 and HEVC on MCL-JCV MS-SSIM, but clearly behind HEVC and VCT on UVG PSNR. The paper acknowledges the UVG gap and attributes it to training data limitations (line 868), which is reasonable but not substantiated. Additionally, no rate-distortion curve is presented for the learned method across multiple bitrates. The abstract's claim of "comparable results on video compression with state-of-the-art video compression standards" is largely supported but would benefit from more precise scoping.

3. **The image generation experiment lacks architectural and training details.** The paper reports FID 5.44 at 128×128 (Table 3) using a masked LM following MaskGIT, but does not specify the model architecture size, training recipe, masking schedule, or whether the tokenizer was frozen or jointly fine-tuned. The number of decoding steps differs (32 vs 12 for VQ/FSQ baselines), which complicates comparison. While the goal of this experiment is to demonstrate BSQ's viability for generation, the missing details make the result difficult to interpret or reproduce.

4. **The throughput comparison (Table 1) does not report hardware configuration.** The paper reports images/s per GPU for all methods but does not specify the GPU model or software environment. While the paper does re-run most baselines on its own hardware (line 418), the omitted hardware details limit the informativeness of the comparison. This is standard to disclose.

### Trivial
- None.

## Nice-to-Haves

- A brief diagnostic (e.g., plotting latent norms or gradient magnitudes during training) of **why LFQ fails with ViT** would strengthen the claim that BSQ's normalization is the crucial factor. The current comparison is convincing but not fully explained.
- An analysis of the **compression efficiency trade-off** between blockwise causal and non-causal attention masks would be directly relevant to the compression use case. The paper notes non-causal works slightly better but does not examine whether the causal variant uses fewer bits.
- Exploring **intermediate L values** (e.g., 24, 28) to show the rFID vs. L scaling trend more granularly would strengthen the scaling argument.

## Removed Points

These points were flagged by reviewers but are removed or downgraded per the review guidelines. They are included here for completeness and should be treated with caution.

- **"LFQ comparison is not apples-to-apples because entropy losses may differ"** — The paper's ablation (lines 907-909) removes ℓ2 normalization from BSQ while keeping everything else identical, producing a clean test of normalization. This is in fact a *better* comparison for isolating the effect of normalization than using the original MAGVIT-v2 LFQ (which uses a different entropy approximation). The naming "LFQ" is slightly imprecise but the ablation itself is valid.
- **"VCT is excluded from MCL-JCV, making comparison inconsistent"** — Including VCT only where it has published results (UVG) is standard practice. Not a weakness.
- **"Paper conflates compression standards with learned codecs"** — The paper consistently distinguishes between standards (H.264/HEVC) and learned codecs (VCT), e.g., lines 9, 48, 867.
- **"No analysis of computational cost for entropy approximation"** — The paper provides Table 6b showing speed (ms) for each group size, including the factorized approximation, and discusses the O(L) vs O(2^L×L) complexity.
- **"Missing ablation on L for BSQ"** — The paper already shows L ∈ {10, 14, 18} at 128×128 and L ∈ {18, 36} at 256×256, demonstrating clear scaling trends.

## Novel Insights

The most interesting observation emerging from the reviews is that BSQ's advantage over LFQ is *multiplicative* rather than additive: the bounded quantization error (due to sphere projection) and the factorized entropy computation (due to the sphere's geometry) reinforce each other during training. The bounded error makes the straight-through estimator more faithful, which in turn allows the clean factorized entropy loss to take full effect. This synergy explains why removing normalization alone causes LFQ-style collapse (code usage 0.6%), and why the simple factorized entropy (group size 1) works as well as more complex group-based approximations. An ablation that jointly ablates normalization and entropy approximation type would cleanly confirm this synergy hypothesis.

## Suggestions

- Add a short derivation of the bounded quantization error (Eq. 6) in the appendix. The bound follows from the geometry of the hypersphere's inscribed hypercube and would take 5-10 lines to derive.
- Expand the compression evaluation to include multiple bitrate operating points (e.g., by varying L or adding a rate-distortion loss). If this is impractical, qualify the claims more precisely (e.g., "competitive with H.264 on selected benchmarks").
- Specify the hardware used for all throughput measurements (GPU model, CUDA version).
- Provide architectural details of the masked LM used for generation: model size (parameters/layers/width), training recipe, masking schedule, and whether the tokenizer was frozen.

## Score and Decision

**Originality**: 7/10 — BSQ is a simple but elegant combination of spherical projection and binary quantization. The factorized entropy insight is clean.  
**Importance**: 8/10 — Visual tokenization is a critical component for generative models and compression. The unified image/video architecture is practically valuable.  
**Claims**: 7/10 — Main claims are well-supported empirically. The compression claim is slightly overbroad relative to the evidence. The theoretical bound claim lacks derivation.  
**Soundness**: 8/10 — Experiments are well-designed with thorough ablations. The comparisons are generally fair.  
**Clarity**: 7/10 — Generally well-written. The main ideas are clearly conveyed. Some experimental details are missing (generation setup, hardware).  
**Value**: 8/10 — BSQ-ViT provides a strong, practical tokenizer that unifies images and videos. The method is simple enough to be widely adopted.

The paper presents a clean and effective method with strong empirical support. The weaknesses identified are minor and addressable — none threaten the core contribution. The bounded quantization error derivation is the most substantive gap, but the empirical evidence independently validates the method's effectiveness. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>