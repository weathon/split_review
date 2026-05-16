Here is my final consolidated review.

---

## Summary

This paper proposes BSQ-ViT, a transformer-based image and video tokenizer combining Binary Spherical Quantization (BSQ) with a ViT encoder-decoder. BSQ projects latent embeddings to a lower-dimensional hypersphere and applies binary quantization, yielding a parameter-free implicit codebook with bounded quantization error and factorized entropy computation. The transformer architecture uses block-wise causal masking to unify image and video tokenization. On ImageNet-1k 256×256, BSQ-ViT achieves rFID 0.41 (beating SDXL-VAE's 0.72 by 43%) at 2.4× higher throughput. On UCF-101 video reconstruction, it achieves rFVD 4.10 (halving MAGVIT-v2's 8.62). The paper also demonstrates competitive video compression and masked LM-based image generation.

## Strengths

1. **State-of-the-art image reconstruction with higher throughput.** Table 1 shows BSQ-ViT (36 bits) achieves rFID 0.41 on ImageNet-1k, a 43% reduction over SDXL-VAE (0.72), while running 2.4× faster (45.1 vs 18.9 images/s). This directly supports the core claim of superior reconstruction efficiency.

2. **State-of-the-art video reconstruction.** Table 2 shows BSQ-ViT (36 bits) achieves rFVD 4.10 on UCF-101 train and 6.21 on val, more than halving the previous best (MAGVIT-v2, 8.62). LPIPS is also nearly halved (0.0159 vs 0.0537).

3. **Efficient entropy computation via dimension-wise factorization.** Section 4.1 (Eq. 5–7) derives a factorized approximation for soft BSQ entropy, reducing complexity from O(2^L × L) to O(L). Table 5b shows this approximation achieves nearly identical rFID and code usage to group-based approaches while being the fastest (0.212 ms).

4. **Bounded quantization error with theoretical guarantee.** Eq. 8 bounds BSQ's quantization error below √2. Table 4 shows BSQ (L=18) achieves 93.8% code usage and rFID 2.66, while the LFQ-equivalent baseline collapses to 0.6% usage and rFID 30.7. This provides clear evidence for BSQ's training stability advantage.

5. **Clean theoretical formulation with practical payoff.** BSQ's projection to the hypersphere enables both the bounded error guarantee and the factorized entropy computation — two properties that are theoretically well-motivated and empirically validated.

6. **Unified image/video architecture.** The block-wise causal masking (Section 4.2) allows a single architecture to handle both images and variable-length videos, a practical benefit over prior 2D→3D CNN inflation approaches.

## Weaknesses

### Major

1. **Compression evaluation uses only a single quality level.** Figure 1 shows the proposed method at exactly one distortion level (33.7 dB PSNR on MCL-JCV, 37.34 dB on UVG) at two bitrates (with and without arithmetic coding). The comparison baselines (H.264, HEVC, VCT) are shown as full rate-distortion curves with multiple operating points. A single point cannot demonstrate that the method "achieves comparable results with state-of-the-art video compression standards" across the operating range, and the "better tradeoff than H.264 and HEVC" claim (line 550) rests on just this one point. On UVG, the method's single point falls below the HEVC curve anyway. The paper needs multi-quality ablation (e.g., via different L or different quantization levels) to substantiate the compression claims.

2. **Bit-rate comparison between discrete and continuous models is not apples-to-apples.** In Table 1, the "# bits" for KL-regularized models (SD-VAE, SDXL-VAE) is computed as latent_dim × 16 (FP16 storage). This is not a meaningful measure of compression efficiency: continuous latents are typically further quantized or entropy-coded in practice, and using raw FP16 precision overcounts their effective bit cost. The comparison of "bits per token" between discrete tokenizers (VQ, BSQ) and continuous VAEs on a single axis is misleading. A proper rate-distortion comparison (bpp vs. distortion, or variable-bitrate evaluation) would be more appropriate if the paper wants to claim superior compression of the discrete bottleneck.

### Minor

3. **The LFQ comparison is a controlled ablation for ℓ2 normalization, but the paper's framing overclaims.** The paper shows that removing ℓ2 normalization from BSQ (which it calls "equivalent to LFQ") collapses to 0.6% code usage (Table 4). This is a valid controlled experiment showing ℓ2 normalization is critical in their ViT framework. However, the original LFQ paper (MAGVIT-v2) achieves strong results with 3D CNNs, so the general claim "BSQ is better than LFQ" conflates the quantizer with the architecture. The finding should be stated more precisely: "BSQ substantially outperforms the LFQ quantization strategy in a ViT-based tokenizer."

4. **The throughput advantage (2.4× vs SDXL-VAE) is not fully disentangled from architecture.** The comparison in Table 1 is BSQ-ViT (ViT-B, 174M params, 45.1 img/s) vs SDXL-VAE (ConvNet, 84M params, 18.9 img/s). The ViT backbone is likely responsible for much of the speedup due to parallelization, not BSQ specifically. The paper presents BSQ-ViT as a complete system, so the throughput claim is valid at that level, but it conflates quantization and architecture.

5. **Video reconstruction comparison does not control for training data differences.** In Table 2, MAGVIT-v2 is trained on Kinetics-600 (~400K clips) while the paper's model initializes from ImageNet and fine-tunes on UCF-101 (~9K clips). The paper acknowledges this for compression (line 868) but not for reconstruction, where the comparison is presented as apples-to-apples. The reported gains are large enough to likely survive controlling for data, but the lack of acknowledgment weakens the presentation.

6. **Image generation comparison is limited.** Table 3 compares BSQ-based masked LM to VQ and FSQ results from a single reference, plus BigGAN and ADM. The paper does not compare to MaskGIT's own 128×128 results or more recent masked models (e.g., MUSE). The FID 5.44 is competitive but the comparison set is narrow.

### Trivial

7. **"Up to 100× compression" claim in the abstract is vague.** The paper never computes or justifies this number. For video compression at 0.14 bpp (with AC), this is roughly consistent with raw 8-bit video (24 bpp → ~171×), but for image reconstruction the ratio is closer to ~43×. The claim is not false but is unsupported by any explicit calculation in the paper.

8. **Minor presentation issues.** Throughput in Table 1 is reported without specifying hardware/batch size details (though the paper does say "per GPU"). Some STDs in tables are labeled as computed "across samples instead of multiple runs" (line 376), which is proper but the single-run caveat for small metric differences (e.g., rFID 0.41 vs 0.45 between BSQ variants) is worth noting.

## Nice-to-Haves

- A multi-point rate-distortion evaluation for compression (varying L or using rate control) would substantially strengthen the compression claim.
- A controlled video experiment comparing VQ vs BSQ after fine-tuning on the same backbone, controlling for bit budget (matching #bits), would isolate BSQ's contribution in the video setting.
- Releasing the model and code would increase impact and reproducibility.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Unfair / non-robust comparison to LFQ"**: The harsh critic characterized this as a structural flaw, arguing the LFQ baseline is "stripped-down" and "untuned." This is overblown. The paper's ablation (Table 4) is a valid controlled experiment: removing ℓ2 normalization from BSQ yields LFQ-equivalent behavior, showing the specific contribution of normalization. While it's true the paper doesn't reproduce the full MAGVIT-v2 training recipe on ViT, that is a different experiment. The ablation as run is informative and methodologically sound. The issue is more about how the finding is framed (see Minor weakness #3 above), not about the validity of the evidence.

- **"Missing ablation of video fine-tuning protocol"**: The critic claims the paper doesn't ablate whether gains come from fine-tuning vs. BSQ. Table 2 actually does show this: image tokenizer results (top rows) vs. fine-tuned results (bottom rows), and VQ vs BSQ within each. The gains from fine-tuning are clear across both quantizers. The critic's request for a finer-grained ablation (VQ fine-tuned on the same backbone with same #bits) is a nice-to-have, not a missing critical experiment.

- **"Statistical significance"**: The critic complains about single training runs. Single-run evaluation is standard for large-scale tokenizer training. Not a real weakness.

- **"The paper should also cover..." suggestions** about additional baselines or methods: these are scope-creep demands for breadth beyond the paper's stated direction.

- **Formatting/style nitpicks** from the original critic are removed per instructions.

## Novel Insights

The reviews surface a useful tension: the paper's strongest evidence for BSQ (the controlled Table 4 ablation showing ℓ2 normalization prevents codebook collapse) is also its most easily contested framing (the LFQ baseline is not the original MAGVIT-v2 implementation). The real insight is that the hypersphere projection does two things simultaneously — it bounds the STE gradient error and it enables factorized entropy computation — and both properties appear to matter for ViT-based tokenizers. Whether these benefits would persist with 3D CNN backbones or with the exact MAGVIT-v2 training recipe is an open question the paper does not (and need not) answer, but it cleanly establishes the advantage for the ViT setting.

## Suggestions

1. **Replace the single-point compression figure with a multi-point rate-distortion curve.** Train the model at different bottleneck sizes (e.g., L=10, 14, 18, 36) and show the full RD tradeoff. This single addition would substantially strengthen the compression claim.

2. **Re-frame the LFQ comparison more precisely.** Change "BSQ outperforms LFQ" to "BSQ's ℓ2 normalization is critical for stable training with ViT-based tokenizers; LFQ-equivalent quantization collapses without it."

3. **Acknowledge the training data difference in the video reconstruction section** (Table 2), as the paper already does for compression (line 868).

4. **Clarify the "100× compression" claim** either by removing it or by adding a brief computation showing how it is derived.

## Score and Decision

**Originality**: Good. BSQ's combination of hypersphere projection + binary quantization with bounded error and factorized entropy is a clean, non-obvious contribution.

**Importance**: High. Visual tokenization is a bottleneck for generative modeling and compression; simpler, more scalable quantizers are of broad interest.

**Claims support**: Mostly well-supported for reconstruction. The compression claims are under-supported due to thin RD evaluation.

**Soundness**: The core experiments are sound. The LFQ ablation is properly controlled.

**Clarity**: Well-written and organized. The theoretical derivations are clear.

**Value**: The method is likely to be practically useful given its simplicity, strong results, and efficiency.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>