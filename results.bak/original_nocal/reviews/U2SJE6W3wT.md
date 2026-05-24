Now I have all the information needed. Let me construct the final review.

## Summary

This paper proposes AdcVSR, a compressed one-step Real-VSR model that distills a large 3D DiT teacher (DOVE, 10.55B parameters) into a compact 2D+1D architecture (0.57B parameters). The key innovations are: (1) augmenting a pruned SD2.1 backbone with lightweight 1D temporal convolutions to handle temporal modeling efficiently, and (2) a dual-head, dual-discriminator adversarial distillation scheme that separates detail and consistency optimization. Experiments across 6 datasets show AdcVSR achieves 95% parameter reduction and 8× speedup over DOVE while maintaining competitive perceptual quality and attaining the best temporal consistency among all compared methods.

## Strengths

1. **Large efficiency gains with competitive quality.** Table 1 shows AdcVSR reduces parameters from 10.55B (DOVE) to 0.57B (95% reduction) and inference time from 4.42s to 0.55s (8× speedup) on a 25-frame 512×512 video, while ranking among the top-3 on most perceptual and temporal consistency metrics.

2. **Best temporal consistency among all compared methods.** AdcVSR achieves the lowest flow warping error E_warp* on both UDM10 (1.67 vs. next-best 2.22 from DOVE) and VideoLQ (6.74 vs. 8.41 from DOVE), directly validating that the 2D+1D design with dual-head distillation effectively suppresses flickering.

3. **Ablations convincingly isolate each contribution.** Table 2 shows 2D+1D (0.55B, DISTS 0.2112) nearly matches a pruned 3D DiT (8.36B, DISTS 0.2098) — a gap of 0.0014 with 93% fewer parameters. Table 3 demonstrates the dual-head, dual-domain discriminator jointly optimizes both CLIPIQA (0.6861) and E_warp* (2.22), outperforming single-head (0.6745/6.32) and single-domain (0.6421/3.59) variants. Table 4 confirms DOVE is the best teacher for this distillation pipeline.

4. **Comprehensive evaluation.** The comparison covers 6 test datasets (3 synthetic, 3 real-world), 10 competing methods spanning non-generative, multi-step diffusion, and one-step diffusion approaches, and 9 metrics covering fidelity, perceptual quality, temporal consistency, and efficiency.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **No variance estimates for any metric.** Tables 1–4 report single numbers without error bars, confidence intervals, or any measure of variability. Given the modest evaluation set sizes (UDM10: 10 videos, VideoLQ: 50), the reader cannot assess whether reported differences (e.g., AdcVSR's E_warp* of 1.67 vs. DOVE's 2.22 on UDM10) are statistically reliable. While single-run evaluation is common practice in this field, the paper's headline claims about "best" performance would be materially strengthened by reporting variance or performing multiple runs.

2. **Ablation results are reported on different datasets.** Table 2 (network design) uses UDM10, Table 3 (discriminator design) uses YouHQ40, and Table 4 (distillation setup) uses MVSR4x. This prevents direct cross-table comparison of ablation magnitudes and raises the question of whether conclusions generalize across datasets. A common dataset for all ablations would increase confidence.

3. **Fidelity trade-off under-discussed.** AdcVSR's PSNR (25.36) and SSIM (0.7697) on UDM10 are notably below DOVE (26.00/0.7805) and SeedVR2 (25.92/0.7674). The paper frames this as "competitive" but could more explicitly characterize the perception–fidelity trade-off, e.g., under what conditions the fidelity loss is acceptable in exchange for the large efficiency gains.

4. **Qualitative evaluation limited to static frames.** Figure 3 shows two frames with temporal profile plots, but temporal consistency is inherently a temporal phenomenon. Side-by-side video comparisons in supplementary material would be more convincing.

### Trivial

None.

## Nice-to-Haves

- A controlled baseline that applies the *original* ADC pipeline (without 1D convs or dual-head discriminators) to a video model would more cleanly isolate the contribution of the proposed modifications.
- Testing generalization to other video diffusion teachers (e.g., SeedVR2, Stable Video Diffusion) would strengthen the claim of being a "systematic recipe."
- A Pareto frontier plot showing the perception–fidelity–efficiency trade-off across methods would help readers interpret where AdcVSR sits relative to the state of the art.

## Removed Points

*These points have been removed from the main review because they either misunderstand the paper, reflect reviewer knowledge gaps, or are speculative/nitpicky. They are preserved here for reference but should not influence the overall assessment.*

1. **"Directly applying ADC to Real-VSR fails" is only rhetorical.** The paper clearly explains (Sec 3.1, lines 93) that AdcSR has no temporal modeling and "when applied frame by frame to videos, it inevitably introduces flickers" — citing prior work (Zhou et al., 2024; Rota et al., 2024). This is a standard logical argument about an image-only method applied to video, not an unsubstantiated empirical claim. **Reason for removal:** The criticism is incorrect; the claim is supported by both reasoning and citations.

2. **Architecture under-specification (placement of 1D convolutions).** The paper specifies: "insert residual blocks after each UNet block" (line 103), with details in the Fig. 2 caption ("after each 2D spatial RB and Transformer block"), kernel size 3, and same channel count as the preceding block (line 139). **Reason for removal:** The specification is adequate for reproducibility in this field.

3. **Softplus with "0" label criticism.** The reviewer notes the use of Softplus with unlabeled (y=0) data produces a constant loss, calling it "unusual." **Reason for removal:** Trivial implementation detail; the formulation is correct and the paper already explains the labeling scheme.

4. **Missing ablation isolating 2D+1D from dual-head distillation.** Table 3's "Single-Head, Dual-Domain" variant uses the full 2D+1D architecture with a single-head discriminator, which is exactly this ablation. **Reason for removal:** Already present in the paper.

5. **"3D attention is redundant" claim not properly tested.** The paper presents this as a hypothesis (not a proven claim) and supports it with Table 2 showing a 2D+1D model at 0.55B nearly matches a 3D model at 8.36B on DISTS (0.2112 vs 0.2098). This is compelling evidence that heavy 3D attention is unnecessary for this task. **Reason for removal:** The criticism demands a same-capacity 3D baseline that is intrinsically incompatible with the paper's compression goal, and the existing evidence strongly supports the stated hypothesis.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm that the paper's strengths (efficiency gains, dual-head disentanglement, competitive temporal consistency) are genuine and well-supported, while the weaknesses (no error bars, different ablation datasets) are standard presentation issues that do not threaten the core claims.

## Suggestions

1. Add error bars or bootstrapped confidence intervals to Tables 1–4. Even running each experiment 3 times or reporting bootstrap variance over the test videos would substantially improve credibility of ranking claims.
2. Consolidate ablations onto at least one shared dataset to enable direct cross-table comparisons.
3. Add an explicit discussion of the PSNR/SSIM trade-off, including a characterization of when fidelity loss is acceptable.
4. Include side-by-side video comparisons in supplementary material.

## Score and Decision

The paper presents a well-motivated, empirically validated compression method for Real-VSR. The 2D+1D architecture insight is principled, the dual-head adversarial distillation scheme is novel and effective, and the efficiency gains (95% parameter reduction, 8× speedup) are substantial. The identified weaknesses are minor and addressable; they do not undermine the paper's core contributions. This is a strong, publication-ready paper.

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>