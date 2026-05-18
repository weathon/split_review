Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper presents BSQ-ViT, a transformer-based image and video tokenizer that replaces traditional codebook lookup with Binary Spherical Quantization (BSQ) on a hypersphere. BSQ projects visual embeddings onto a lower-dimensional unit sphere, applies binary quantization per dimension, and yields a parameter-free implicit codebook with bounded quantization error and factorized entropy computation. The transformer architecture uses blockwise causal masking to unify image and video tokenization. The method achieves strong image reconstruction results (rFID 0.41 on ImageNet-1k val, beating SDXL-VAE by 43% with 2.4× throughput), competitive video reconstruction (rFVD 4.10 on UCF-101), and reasonable compression and generation performance.

## Strengths

- **Principled quantization with bounded error and factorized entropy.** BSQ derives an explicit bound on quantization error (Eq. 5) and shows soft quantization factorizes into independent Bernoulli distributions per dimension, reducing entropy computation from O(2^L × L) to O(L) (Eqs. 4, 6, 7). This theoretical advantage translates into empirical gains: on ImageNet-1k val, BSQ with 36 bits achieves rFID 0.41, a 43% reduction over SDXL-VAE (0.72), while the controlled ablation (Table 4a) shows BSQ consistently beats VQ and LFQ under the same architecture and training data.

- **Transformer architecture with blockwise causal masking unifies image and video tokenization.** The blockwise causal attention (Fig. 2) allows a single ViT model to process images (T=1, full mask) and videos (T>1, causal mask) with factorized spatial-temporal embeddings. This design is validated internally: the non-causal variant slightly beats the causal one (analogous to B-frames in video compression), and BSQ-ViT with L=36 achieves rFVD 4.10 on UCF-101, significantly improving over the same model's VQ variant (rFVD 10.76 with 14 bits).

- **Parameter-free implicit codebook that scales without overfitting.** The codebook C_BSQ = {-1/√L, 1/√L}^L has no trainable entries. The ablation (Table 4a) shows increasing L from 10 to 18 steadily improves all reconstruction metrics, while VQ with comparable vocabulary (65536) suffers performance degradation (rFID 6.61 vs 4.27 for 16384). The bounded error also renders the commitment loss unnecessary (Table 4b: removing it improves code usage from 45.6% to 93.8% with similar rFID).

- **Factorized entropy approximation is both accurate and efficient.** The proposed approximation (Eq. 7, effectively group size g=1) achieves nearly identical rFID (2.86 vs 2.76–3.32) and code usage (95.1% vs 93.8–96.0%) compared to MAGVIT-v2's grouping strategies while running the fastest (0.212 ms per step, Table 4c).

## Weaknesses

### Fatal
None.

### Major

1. **Video reconstruction comparisons are uncontrolled for training data.** The paper reports video reconstruction on UCF-101 (Table 2) and compares with published numbers from MAGVIT-v2, TATS, and MaskGIT without controlling for training data. The authors fine-tune their model only on UCF-101 (~9K clips), while MAGVIT-v2 was trained on substantially larger and more diverse video datasets (e.g., Kinetics-600/700). The paper acknowledges this data limitation for compression experiments (line 868) but not for video reconstruction, where it claims "state-of-the-art" improvement (e.g., rFVD 4.10 vs MAGVIT-v2's 8.62 in the abstract). The internal comparisons (BSQ vs VQ with the same ViT backbone in Table 2) are clean and show clear BSQ advantages, but the headline SOTA claim against MAGVIT-v2 is confounded by training data differences. **The paper must either provide a controlled video ablation (BSQ vs VQ vs LFQ with the same backbone on the same video data) or prominently qualify the video SOTA claims with the data discrepancy.** This is the most significant weakness because the abstract and introduction present the video result as a core achievement without the necessary caveats.

### Minor

2. **Image generation comparison uses unequal inference budgets.** The BSQ generation results (Table 3) use 32 decoding steps, while the compared VQ and FSQ methods use 12 steps. The paper acknowledges this (line 518: "We increase the number of decoding steps accordingly") but does not report BSQ results at 12 steps, making the comparison less clean. The generation quality could be partially driven by more decoding steps rather than the tokenizer alone.

3. **Compression claims in the abstract/intro are slightly overstated.** The paper's detailed text (line 867) correctly notes that "on UVG 1080P, our model is comparable to H.264 while being worse than HEVC and VCT." However, the abstract claims "comparable results on video compression with state-of-the-art video compression standards" without this nuance. On UVG PSNR (Fig. 4c), the method is clearly behind HEVC; the claim is accurate for MS-SSIM on MCL-JCV where the method ties or beats codecs, but the broad phrasing in the abstract masks the unevenness across benchmarks.

4. **Missing architecture details for the generative model and compression prior.** The paper states "we follow MaskGIT" (line 513) for image generation but provides no architecture size, training recipe, or hyperparameters for the masked language model. Similarly, the autoregressive prior used for arithmetic coding in compression is described only as a "lightweight and thus computationally efficient sequence model (~300M)" (line 74) without details on architecture, training data, or sequence length. These omissions hinder reproducibility and make it difficult to assess whether generation/compression results are driven by the tokenizer or the downstream model.

5. **Throughput/latency benchmarks lack hardware specifications.** The speed comparison (Table 5) reports encoding/decoding timing and FPS but does not specify GPU model, batch size, or numerical precision. These details are needed for reproducibility and proper comparison.

### Trivial
None.

## Nice-to-Haves

- A controlled video ablation (BSQ vs VQ vs LFQ with the same ViT backbone, trained on the same video data) would cleanly isolate the benefit of BSQ for videos, independent of training-data confounds. The current video table mixes architectures and training protocols.
- Reporting image generation results at 12 decoding steps for BSQ would enable a direct apples-to-apples comparison with VQ/FSQ baselines.
- More details on the masked LM and autoregressive prior architectures would improve reproducibility, though these are secondary to the paper's core tokenization contribution.

## Removed Points

The following criticisms from the harsh reviewer were removed after cross-checking against the paper:

1. **"The throughput comparison (Table 1) only benchmarks one competitor (SDXL-VAE)"** — Factually incorrect. Table 1 reports throughput (TP column) for ALL methods listed, including MaskGIT (37.6 img/s), DALL-E dVAE (34.0), SD-VAE 1.x (22.4), SD-VAE 2.x (18.9), etc. The "2.4×" claim specifically refers to SDXL-VAE, the best-quality prior method, and the paper clearly states this (line 429: "2.4× higher throughput than SDXL-VAE"). The criticism fails to acknowledge the TP column's coverage.

2. **"The image reconstruction comparison (Table 1) is weaker than it appears — mixing methods from different training sets"** — The paper transparently reports training data for each method via the "data" column and acknowledges cross-dataset differences (lines 416-418, 419-420). The controlled comparison (BSQ vs VQ vs LFQ under identical conditions) is provided separately in the ablation study (Table 4a). Mixing training sets in a SOTA comparison table is standard practice; the key is that the paper is transparent about it and provides controlled ablations.

3. **Claim that the paper does not acknowledge data limitations for video reconstruction** — Partially inaccurate. While the paper does not explicitly call out the MAGVIT-v2 training data discrepancy in the reconstruction section, it does state "Since most methods do not release checkpoints, we take their reported numbers directly" (line 477), which implicitly acknowledges the comparison uses published numbers rather than controlled re-implementations. The weakness is retained (Major #1) but for the overclaim in the abstract/intro rather than for complete omission.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: BSQ's cleanest, most convincing evidence comes from controlled ablations on images (where training data, architecture, and evaluation protocol are matched), while the more ambitious claims about video and compression rely on comparisons where confounding factors (training data scale, inference budget) weaken the attribution. This suggests that for future work combining quantization methods with new backbone architectures, isolating the quantization contribution requires careful experimental design — a point the paper itself partially acknowledges but does not fully address for video.

## Suggestions

1. **For the camera-ready revision**: Qualify all video reconstruction SOTA claims with the training-data caveat (model fine-tuned on UCF-101 only; baselines trained on larger datasets). Add a controlled video ablation (BSQ vs VQ vs LFQ with same ViT backbone, trained on UCF-101) to Table 2 or the appendix.
2. Report image generation results at 12 decoding steps for BSQ to match the VQ/FSQ baseline setup, or at minimum add a note acknowledging the asymmetry.
3. Add architecture details for the masked LM and the autoregressive compression prior (number of layers, hidden dimension, training data, sequence length) to the appendix.
4. Add hardware specifications (GPU model, batch size, precision) to the throughput/latency tables.
5. Tone down the compression claim in the abstract to match the more nuanced finding reported in the detailed text (line 867).

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>