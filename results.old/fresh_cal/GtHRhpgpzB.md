Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces a new task called Gain Map-based Inverse Tone Mapping (GM-ITM), motivated by the emerging double-layer HDR image format (SDR + auxiliary Gain Map). Instead of directly estimating HDR from SDR, the method learns the Gain Map — an intermediary representation with more balanced statistics. The authors propose GMNet, a dual-branch network with a Local Contrast Restoration (LCR) branch for pixel-level normalized GM prediction and a Global Luminance Estimation (GLE) branch for image-level peak-value estimation and global guidance via spatial-aware and channel-wise modulation. They also contribute both synthetic (derived from HDRTV videos) and real-world (captured with a Xiaomi 14 Ultra) SDR-GM datasets. Extensive experiments show GMNet outperforms existing SI-HDR and SDR-to-HDRTV methods across linear, PQ, and HDR-specific metrics on both datasets.

## Strengths

1. **Well-motivated new task with formal definition and datasets.** The paper clearly articulates why GM-ITM is distinct from SI-HDR and SDR-to-HDRTV (Section 1, Table 1), provides a clean mathematical pipeline (Section 3), and constructs the first dedicated datasets for this task — synthetic pairs from 4K HDRTV videos and real-world pairs from a mobile device supporting the ISO standard format (Section 5.2). This creates a reproducible foundation for a timely research direction.

2. **Dual-branch architecture with ablation-validated components.** The decomposition into a local contrast branch (predicting normalized GM) and a global luminance branch (estimating Q_max and providing modulation) is principled and well-matched to the GM's characteristics. Ablations (Table 4, Figure 6) confirm that each component — indirect Q_max supervision, spatial-aware modulation, and channel-wise modulation — contributes positively, with the full model significantly outperforming all ablated variants.

3. **Consistent state-of-the-art results across domains and datasets.** On both the synthetic dataset (Table 2) and the real-world dataset (Table 3), GMNet achieves best or second-best results across PSNR, SSIM, SRSIM, ΔE_ITP, and HDR-VDP3 in both linear and PQ domains. Notably, SI-HDR methods excel in the linear domain and SDR-to-HDRTV methods in the PQ domain due to their training targets, but GMNet leads in *both* — a strong indicator that learning the GM is a more effective formulation. Qualitative results (Figures 4, 5) confirm visually superior highlight detail reconstruction.

4. **Demonstrated robustness to model size and GM resolution.** Ablations on hidden-layer count (Table 5) show graceful degradation when reducing parameters, indicating practical deployability. The method maintains its advantage across varying GM downsampling scales (Table 6) where competing methods suffer larger drops — supporting the claim that GM-ITM is robust to resolution trade-offs.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Resolution alignment between prediction and ground truth during training is not explicitly specified.** The LCR branch outputs the normalized GM at full (or patch) resolution via pixel-shuffle upsampling. For the real-world dataset, the stored GM is at 2048×1536 (half the SDR resolution). The paper does not state whether the ground-truth normalized GM is upsampled to match the prediction or the prediction is downsampled to match the GT for loss computation ($\mathcal{L}_{NGM}$ and $\mathcal{L}_{GM}$). For the synthetic dataset the GM is at full 3840×2160 resolution, so this is not an issue there, but the real-world training protocol is underspecified. This does not invalidate any results — the numbers are clearly reported and internally consistent — but the authors should clarify the exact resolution alignment used during training in the rebuttal.

2. **The spatial-aware modulation kernel is global, applied uniformly across all spatial locations.** The GLE branch generates a single $3\times3\times C$ kernel that is applied via depthwise convolution at every spatial position. While this design choice is sensible and the ablation confirms it helps, the paper's framing as "spatial-aware" could be interpreted as implying spatially-varying guidance. The method works well as-is, but future work could explore spatially-adaptive kernels conditioned on local image content. This is more of an observation than a flaw.

### Trivial

- The paper mentions that $Q_{min}$ is set to zero in practice (Section 3), yet Eq. 1 still subtracts it — a minor redundancy that could be simplified for clarity.

## Nice-to-Haves

- **"Apples-to-apples" comparison isolating the target representation:** The paper's central thesis is that learning the GM is more effective than learning HDR directly. This would be strengthened by a controlled experiment where the same backbone architecture (e.g., the LCR branch alone) is trained to predict either the GM or the HDR (linear or PQ) directly, holding capacity and optimization constant. The current comparisons against unrelated architectures (HDRUNet, FMNet, etc.) introduce confounding differences.
- **Inference speed or FLOPs comparison:** Since GM-ITM targets display-end deployment, reporting inference time or FLOPs per 4K image relative to baselines would be practically informative. The model-size ablation (Table 5) partially addresses efficiency but does not directly compare runtime.
- **Failure cases or limitations discussion:** The paper does not discuss scenarios where the method might struggle (e.g., completely saturated regions with no SDR texture, or scenes where the peak GM value cannot be reliably inferred from the SDR due to clipping). Adding a brief limitations paragraph would strengthen the paper's honesty and guide future work.
- **Ablation isolating the GLE branch's global features from the scalar Q_max:** Table 4 ablates "not learning Q_max" (removing both scalar and modulation) versus indirect learning (both scalar and modulation). A configuration with Q_max predicted but without spatial/channel modulation would isolate the value of the global features beyond just the scalar value.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Number of ResBlock groups is not stated"** (Harsh Critic, Section-by-Section Notes). **REMOVED — factually incorrect.** The paper explicitly states "three cascaded ResBlock groups" (line 95) and "Each ResBlock group contains 5 blocks" (line 153). Both numbers are clearly specified.
- **"Resolution mismatch could cause the loss surface to differ from what the network is actually optimizing"** (Harsh Critic, Critical Issues point 1). **REMOVED — speculative inference about an unconfirmed scenario.** The concern about resolution alignment is valid as a missing detail (kept as Minor weakness #1 above), but the specific claim that the loss surface may not match what is optimized is speculation. The paper's results are internally consistent, and the full-resolution GT GM is available during dataset generation as an intermediate product even when the stored format is downsampled.
- **General area-of-concern sweeps** (e.g., "could the metric be measuring a proxy?", broad speculation about confounders) — not present in this review; none removed.
- **Generic/unsupported strengths from Strength Finder** — none found; all four strengths are specific, evidence-backed, and verified against the paper.
- **Formatting/style/presentation nitpicks** — the "Q_min=0" simplification note (from Harsh Critic) is retained as Trivial since it is a concrete observation about Eq. 1, not a stylistic complaint.

## Novel Insights

The Harsh Critic and Strength Finder together surface a useful tension: the paper claims that GM is an easier target because of its balanced distribution, but the evidence for this claim comes from cross-architecture comparisons (GMNet vs. HDRUNet, FMNet, etc.). Neither reviewer disputes that GMNet obtains the best results — they do — but the strongest argument for the GM *representation itself* would require an architecture-controlled experiment. This is a genuinely insightful observation that the paper could address concisely (a single table) to make its central claim bulletproof. Beyond this, the reviews do not produce novel insights beyond the paper's own contributions.

## Suggestions

1. Clarify the resolution alignment used during loss computation for the real-world dataset — specify whether the ground-truth normalized GM is upsampled, the prediction is downsampled, or the LCR branch directly operates at the GM resolution.
2. Add an architecture-controlled experiment: train the same backbone to predict GM vs. linear HDR vs. PQ HDR, to isolate the benefit of the target representation from the benefit of the network design.
3. Include a brief limitations paragraph discussing failure cases (e.g., extreme saturation, clipped highlights where GM peak is ambiguous).
4. Report inference speed or FLOPs for GMNet and baselines to contextualize efficiency for display-end deployment.

## Score and Decision

MY FINAL SCORE: <score>8.5</score>
MY FINAL DECISION: <decision>Accept</decision>