I now have a thorough understanding of the paper and both reviews. Let me write the consolidated review.

## Summary

This paper proposes a codebook-based video compression framework that solves the cross-platform floating-point inconsistency problem faced by entropy-model-based neural video codecs. By transmitting index sequences from learned codebooks instead of using entropy models with arithmetic coding, the method inherently avoids distribution estimation mismatches across platforms. A window-based cross-attention context model replaces optical flow alignment, resulting in a simplified pipeline. The method outperforms H.265 (medium) by 33.7% in SSIM-BPP on average across three 1080p datasets, and demonstrates 0% BD-rate difference when encoding on V100 and decoding on P40.

## Strengths

- **Inherently solves cross-platform decoding failures.** By eliminating entropy models and arithmetic coding — the root cause of platform-dependent decoding errors in neural codecs — the method transmits only codebook index sequences, which are deterministic across platforms. Table 2 confirms 0% BD-rate difference between V100 encoder / V100 decoder and V100 encoder / P40 decoder on UVG, providing direct evidence that the cross-platform problem is avoided without integer-arithmetic tricks or calibration data.

- **Outperforms H.265 (medium) in SSIM by a wide margin.** On three 1080p datasets, the method achieves −43.7%, −38.2%, and −19.1% SSIM-BPP BD-rate savings against H.265, averaging −33.7% (Table 1). The RD curves in Fig. 3 visually confirm the SSIM advantage at all bitrates. This is the paper's main quantitative contribution.

- **Cross-attention context model avoids optical flow and autoregressive modeling.** Section 3.2 introduces a window-based cross-attention (WCA) that uses reference latents as key/value and current latents as query, eliminating pixel-level alignment. Table 3 shows WCA-based-4 saves 82.5% context-modeling time (13.0ms vs. 74.2ms) compared to a large-window variant (CA-based-64) while achieving nearly identical SSIM BD-rate (−40.7% vs. −40.8%), demonstrating the efficiency of the windowed design.

## Weaknesses

### Fatal

None.

### Major

- **No comparison to any neural video codec.** The paper references DCVC, MIMT, AlphaVC, and other neural codecs in its related work, and the abstract states that "advanced neural video codecs can surpass the most complex traditional codecs," yet provides zero experimental comparison against any of them. The stated justification — "existing neural video codecs cannot achieve cross-platform decoding directly" (line 188) — explains why cross-platform comparison is infeasible, but does not justify the absence of same-platform RD comparisons. A reader cannot assess whether the method's RD performance is competitive with the neural codec landscape it seeks to improve upon. The method could outperform H.265 by 33.7% SSIM while still being far behind DCVC or MIMT. Adding at least one neural codec baseline (same-platform, acknowledging it would fail cross-platform) is essential to situate the contribution. This does not invalidate the paper's core cross-platform claim, but it severely limits the paper's ability to demonstrate the significance of its approach.

- **Fixed bitrate per frame is a fundamental limitation.** The method compresses each frame to a fixed number of indices determined by spatial dimensions and the number of stages, producing constant bitstream size regardless of content complexity. The paper acknowledges this (line 280) but treats it as a future-work item. This directly explains the weak PSNR performance on MCL-JCV (+23.7% BD-rate, Table 1) and the method's overall weakness on PSNR relative to SSIM (average −1.7% PSNR-BPP). The ability to control bitrate only globally (via codebook size selection, Section 3.5) rather than per-frame means static scenes waste bits and complex scenes cannot allocate enough. For a method positioned as a practical codec, this is a significant gap that is not merely a "limitation" but a core design constraint that limits deployment scenarios.

### Minor

- **GOP size asymmetry in evaluation.** The paper uses GOP size 32 for their method but GOP size 12 for H.264/H.265 baselines (line 188). Larger GOPs mean fewer keyframes, which reduces overall bitrate. The authors cite prior work for the H.264/H.265 settings, but the asymmetry could partially confound the RD comparisons and should be controlled or explicitly discussed. A sensitivity analysis (e.g., showing H.265 results at GOP 32) would address this.

- **Missing optical flow baseline in ablation.** The paper's central architectural claim is that cross-attention replaces optical flow alignment, yet the ablation (Table 3) compares only a Resblock-based model (no context modeling) and CA-based-64 (larger window). Without an optical-flow-based context model baseline (e.g., warping + residual coding as in DCVC/DVC), it is unclear whether the cross-attention design is genuinely beneficial relative to the approach it claims to supersede, or merely comparable to it.

- **"Minimalist" claim is over-stated for the full model.** The paper repeatedly calls the framework "extremely minimalist" (abstract, Section 1, Section 3.2), yet the WCA-based-4 model has 53.4M parameters and takes 229.3ms to decode a single 1080p frame on a V100. While the framework design is simpler (no entropy model, no optical flow, no autoregressive modeling), the actual computational footprint is not "extremely minimalist" — particularly the full model. The light-decoder variant (46.2M params, 35.8ms) is more convincingly efficient. The claim should be calibrated to the variant being discussed.

- **H.265 (medium) preset is a relatively weak anchor.** The paper is transparent about using the medium preset (line 182), but slower presets (e.g., slow, veryslow) improve H.265 RD performance. The reported gains may be smaller against stronger H.265 configurations. This is not a fatal issue — the comparison is still valid and transparent — but it should be acknowledged as a limitation of the chosen anchor.

### Trivial

None.

## Nice-to-Haves

- A same-platform RD comparison against a lightweight neural codec (e.g., DCVC-Small, MIMT-Small) would greatly help readers assess the trade-off between cross-platform capability and RD performance.
- Cross-platform testing on genuinely diverse hardware (AMD GPU, Apple silicon, CPU inference) would strengthen the cross-platform claim beyond the current V100↔P40 test.
- An entropy-constrained variant (e.g., a simple factorized prior on index probabilities with integer arithmetic) would address the fixed-bitrate limitation and substantially strengthen the contribution.

## Removed Points

The following criticisms from the reviews were removed or downgraded after verification against the paper:

- **"Weak cross-platform validation (V100 vs P40 both NVIDIA)"** — The critic demands CPU, AMD, Apple tests. While more diversity would strengthen the paper, the mechanism (index transmission without entropy models) is theoretically platform-independent. The 0% BD-rate result across two different NVIDIA architectures with different CUDA compute capabilities provides solid evidence. Downgraded from Major to removed after consideration — the critic's ask for bit-exact reconstruction across all possible platforms is practically infeasible for an academic submission and overstates the risk given the mechanism. Moved to Nice-to-Haves.

- **"Center cropping to 1920×1024 discards content"** — This is a standard technical requirement (divisibility by 128 for the encoder's downsampling factor of 8). Not a weakness.

- **Suggestions that are requests for the paper to cover additional domains or tasks** — These are scope-creep demands that would turn the paper into a broader paper rather than a stronger version of itself.

- **Generic formatting/style nitpicks** — Removed per the hard rules.

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that codebook-based vector quantization can replace entropy models for cross-platform neural video compression — is the contribution itself, and the reviews do not surface a secondary synthesis that goes beyond this.

## Suggestions

1. Add same-platform RD comparisons against at least one lightweight neural video codec (e.g., DCVC-Small) to contextualize the RD performance relative to the neural codec literature.
2. Address the GOP size asymmetry by either re-running H.265 at GOP 32 or explicitly quantifying the effect.
3. Include an optical-flow-based context model in the ablation (even a simple DVC-style warping baseline) to directly substantiate the claim that cross-attention is preferable.
4. Consider adding a simple, integer-friendly entropy model on the codebook indices (e.g., a factorized prior with integer lookup tables) to enable content-adaptive bit allocation while maintaining cross-platform capability.
5. Calibrate the "minimalist" language to distinguish between framework design simplicity (valid claim) and computational footprint (53.4M params / 229ms is not minimalist).

## Score and Decision

The paper addresses a genuine deployment problem (cross-platform floating-point inconsistency in neural video codecs) with a clean, well-motivated approach (codebook-based compression to eliminate entropy models). The SSIM results against H.265 are strong, and the cross-platform validation with 0% BD-rate difference is compelling. However, the evaluation has significant gaps — most critically, the complete absence of any neural codec baseline prevents readers from situating the contribution, and the fixed-bitrate limitation is more than a minor concern for a system positioned as a practical codec. The paper is a solid contribution with clear novelty and a real contribution, but it needs stronger contextualization and at least a partial solution to content-adaptive bit allocation to be fully convincing.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>