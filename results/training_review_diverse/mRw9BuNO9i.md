Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes a neural video codec that replaces probabilistic entropy models with codebook-based vector quantization, thereby avoiding the cross-platform floating-point inconsistency that plagues existing neural video codecs. The method transmits index sequences of learned codebooks rather than arithmetically coded latents, and uses a window-based cross-attention context model for temporal redundancy fusion instead of optical flow. Experiments show the approach matches or exceeds H.265 (medium) in SSIM-based rate-distortion on several 1080p benchmarks while enabling cross-platform decoding between V100 and P40 GPUs, with a light-decoder variant achieving real-time throughput.

## Strengths

- **Window-based cross-attention (WCA) provides large RD gains with dramatically lower compute.** The ablation in Table 3 shows WCA-based-4 retains essentially the same SSIM BD-rate saving (~−41%) as a much larger window-64 variant, while cutting context-modeling time from 74.2 ms to 13.0 ms (82.5% reduction). Verification: Table 3 reports CA-based-64 at −40.8% SSIM BD-rate / 74.2 ms vs. WCA-based-4 at −40.7% SSIM BD-rate / 13.0 ms.

- **Light-decoder achieves real-time 1080p decoding on V100 while still surpassing H.265 in SSIM.** The same table shows a reduced model (46.2M params, 0.74T MACs) decodes in 35.8 ms per frame (~28 fps) yet delivers −23.7% SSIM BD-rate over H.265 (medium). Verification: Table 3, row "light-decoder" — 35.8ms decode time, −23.7% SSIM BD-rate.

- **Multi-stage multi-codebook design provides a simple, entropy-model-free rate-control mechanism.** The paper demonstrates three distinct bitrate operating points by changing only the codebook sizes for predicted frames ({8192,2048,512}, {64,2048,512}, {8,2048,512}) rather than tuning rate-distortion loss weights. This is a practical engineering advantage over conventional neural codecs. Verification: Section "Codebook settings," lines 159-161.

- **The padded sliding-window cross-attention strategy is a clean architectural contribution.** By pairing non-overlapping windows (size 4) for the current frame with overlapping windows (size 8) for the reference frame, the model captures motion-induced spatial shifts without optical flow or pixel-level alignment. Verification: Section 3.4, lines 135-136.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Cross-platform evidence is thinner than claimed.** Table 2 reports a BD-rate of exactly 0% when decoding a V100-encoded bitstream on both V100 and P40. The BD-rate is reported as an integer percentage, so small per-frame differences could round to 0% — but the paper does not report per-frame PSNR/SSIM differences, does not test on a CPU or a more architecturally distinct GPU (e.g., A100, RTX 3090), and does not show that no reconstruction failure of the type in Fig. 1 occurs on P40. The theoretical argument (no entropy model → no arithmetic-coding failure) is sound, but the empirical validation is too sparse to fully substantiate the "error-free" claim. The authors should provide per-frame PSNR differences between V100 and P40 decoders and test at least one more platform pair.

- **The fixed-bitrate design limits the fairness of the RD comparison with H.265.** As the authors honestly acknowledge (Conclusions), the method produces constant bitstreams regardless of video content, while H.265 adapts its bit allocation per frame. The BD-rate metric, designed for variable-rate codecs, is applied asymmetrically. On simple/low-motion content, the method wastes bits, potentially inflating its distortion scores relative to H.265; on complex content, it is starved of bits. Aggregate BD-rate tables mix these effects. The paper does partially address this by showing per-dataset results (not just the average), and the −19.1% to −43.7% SSIM BD-rate range across datasets is informative. However, a per-video breakdown would be needed to assess how much the fixed-rate limitation biases the headline numbers.

- **Several implementation details are missing, harming reproducibility.** The paper does not specify: (a) how the light-decoder is obtained (fewer channels? fewer stages? reduced resolution?); (b) training hyperparameters (optimizer, learning rate, batch size, number of training steps, codebook update mechanism); (c) the exact bitstream format (how indices are packed — fixed-length codes of ⌈log₂K⌉ bits? how indices from multiple stages and codebooks are serialized?). Without (a) and (b), the efficiency and RD results cannot be independently reproduced.

- **The metric label is inconsistent.** Section 4.1 says metrics are "PSNR and MS-SSIM," but all tables (Table 1, 2, 3) label the distortion metric as "SSIM" / "SSIM-BPP." MS-SSIM and SSIM are different metrics, and the paper should state clearly which was used for the BD-rate calculations in each table.

### Trivial
- **Dataset cropping ambiguity.** The paper states test frames are center-cropped to 1920×1024 "to ensure the input image shape is divisible by 128" (line 178). It does not state whether H.264 and H.265 baselines also operate on cropped frames or on the original 1920×1080. If the baselines use the full resolution while the method uses cropped frames, the bits-per-pixel comparison would differ by a factor of ~1.055. This likely is not the case (standard practice applies identical preprocessing), but should be clarified.

- **The "CA-based-64" label is confusing** since it is actually a WCA method with window size 64, not global cross-attention. While explained in the text (line 248), a clearer label (e.g., "WCA-64") would avoid misinterpretation.

## Nice-to-Haves

- **Compare against a representative neural codec (e.g., DCVC) under cross-platform conditions** to empirically demonstrate the decoding failure (Fig. 1) that justifies the paper's motivation. This would turn the well-known theoretical problem into a concrete baseline for the proposed solution. The current paper omits this because "existing neural video codecs cannot achieve cross-platform decoding directly" (line 188), which is a reasonable justification but leaves the motivating phenomenon unquantified against a contemporary method.

- **Per-video breakdown of RD results** would allow readers to assess which motion/content types favor or disfavor the fixed-bitrate codebook approach, and would address the fairness concern about the H.265 comparison more directly than aggregate BD-rate tables.

- GPU memory footprint of the model, especially since global cross-attention was infeasible due to out-of-memory errors (line 248), would be useful for deployment assessment.

## Removed Points

These points were flagged by reviewers but are not included in the main review. They should be treated with caution.

1. **Harsh critic's claim that BD-rate of exactly 0% across V100 and P40 is "highly improbable" and implies the evidence is unsupported.** The paper reports BD-rate as integer percentages; small floating-point differences in decoder-network outputs would round to 0% at this precision. For a codebook-based method where decoding is primarily table lookups followed by a feedforward network, near-identical RD curves across two NVIDIA GPU families are entirely plausible. The evidence could be stronger (per-frame numbers), but it is not invalid or improbable. This criticism was downgraded from an "evidential issue" to a minor weakness.

2. **Harsh critic's assertion that the fixed-bitrate RD comparison "cannot substantiate the claimed outperformance" of H.265.** This overstates the problem. The paper acknowledges the limitation (Conclusions, line 280), and the datasets span diverse content types (UVG: high motion; MCL-JCV: varied). The asymmetric comparison still shows the method outperforms H.265 in SSIM across all three datasets and in PSNR on two of three — a meaningful result even if the comparison is not perfectly apples-to-apples. The weakness was downgraded from structural/fatal to minor.

3. **Demand for comparison against neural video codecs on cross-platform.** The paper cites established work (Ballé et al. 2019) documenting the cross-platform failure of entropy-based neural codecs, and showing Fig. 1 as a qualitative example. Running a neural codec cross-platform to demonstrate its failure would be a useful addition but is not required to validate the paper's own claims. Moved to Nice-to-Haves.

4. **CA-based-64 naming issue** — a trivial presentation concern but explained in the text. Moved to Trivial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Strengthen the cross-platform validation.** Report per-frame PSNR/SSIM differences between V100 and P40 decoders, and test on at least one more architecturally distinct platform (e.g., CPU, or an A100/RTX 3090). This would turn a plausible theoretical claim into a solidly evidenced one.

2. **Provide per-video RD results** for all three operating points across all test datasets. This would allow readers to assess the effect of the fixed-bitrate limitation and make the H.265 comparison more transparent.

3. **Clarify the bitstream format.** Specify: (a) the number of bits allocated per index for each codebook size, (b) how indices from three stages and two codebooks per stage are serialized, (c) the downsampling factors used between stages in the multi-stage VQ. This would make the reported bpp values verifiable.

4. **Add training details** (optimizer, learning rate schedule, batch size, number of training steps/epochs, codebook update mechanism) and describe how the light-decoder is constructed.

5. **Resolve the MS-SSIM vs. SSIM inconsistency** between the Experiments section and the tables.

## Score and Decision

The paper proposes a genuinely novel approach to the cross-platform problem in neural video codecs by sidestepping entropy models entirely through codebook-based compression. The WCA context model is a clean, efficient architectural contribution. The experimental results demonstrate meaningful RD improvements over H.265 (especially in SSIM) and the light-decoder variant achieves real-time throughput. The weaknesses are real but incremental — the cross-platform evidence needs strengthening (not just one GPU pair, not just BD-rate), some implementation details are missing, and the fixed-rate comparison with H.265 warrants more granular reporting. None of these issues are fatal to the core contribution, and all are addressable in a revision or rebuttal.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>