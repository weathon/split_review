## Summary

LDP is a lightweight (642K parameter) denoising autoencoder plug-in that improves the generalization of existing single-image super-resolution (SISR) models to unseen degradations. By leveraging the HR–LR feature alignment property of diffusion models at high noise levels, LDP performs degradation modeling on HR/SR outputs conditioned on LR high-frequency components (LR_hf), and enforces cyclic LR consistency through a symmetric loss. It can operate as (1) a fine-tuning loss that improves reconstruction quality across architectures, or (2) an inference-time DPS guidance term that corrects diffusion model artifacts.

---

## Strengths

- **Consistent improvement across four diverse SR architectures on synthetic benchmarks**: Table 3 shows LDP improves all four base models (FeMaSR, StableSR, SwinIR, MambaIR) across all five degradation types. Gains are substantial for weaker baselines (e.g., StableSR+LDP: +2.16 dB PSNR on Hybrid, +1.52 dB on Blur) and consistently positive even for strong baselines (MambaIR+LDP: +0.36 dB on Hybrid). These results are architecture-agnostic and demonstrate practical plug-in value.

- **LR prediction accuracy and non-degeneracy**: Table 1 shows LDP outperforms DRN and DualSR on Blur and Hybrid degradations. More importantly, Table 2 demonstrates that LDP-generated LR images have substantially lower similarity to downsampled SR outputs than DRN's outputs (e.g., Hybrid LPIPS: LDP 0.3586 vs DRN 0.0296), proving that LDP does not collapse into trivial bicubic downsampling—a critical design property the paper explicitly tests.

- **Lightweight and practical design**: At 642K parameters, trained in 16 hours on a single A6000, LDP is genuinely practical to integrate into existing pipelines. Its design is interpretable: patch-dependent noise enables spatially varying degradation modeling, and LR_hf as a conditioning signal is well-motivated (Section 3.1).

- **Ablation validates complementary loss components**: Table 6 shows that all combinations of the symmetric and frequency losses outperform the baseline (23.52 PSNR), and LDPV7 (full combination, 24.35 PSNR) outperforms all partial configurations, confirming that the loss terms are complementary rather than redundant.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing quantitative comparison with Lway (Chen et al., 2024)**: Section 2.2 explicitly describes Lway as a test-time adaptation method that uses pre-trained degradation models to fine-tune SR models for improved generalization—functionally the same goal as LDP. The paper characterizes Lway as an expensive alternative ("introduces significant computational overhead due to its large model size") but never benchmarks LDP against Lway in Tables 3, 4, or 5. This is the closest functional competitor, and LDP's core claim of efficient generalization improvement is asserted rather than demonstrated comparatively. A direct head-to-head—even on one architecture and dataset—is needed to substantiate the efficiency-versus-quality trade-off argument.

- **DPS mode results are overstated in Section 4.4**: The paper claims "the baselines show improvements across nearly all metrics on most datasets." However, reading Table 5 cell by cell shows that for LDM on RealSR, four of five metrics regress (NIQE: 6.651 → 6.830; CLIPIQA: 0.4564 → 0.4319; MUSIQ: 52.09 → 50.37; QAlign: 2.685 → 2.610). For ResShift on RealSR, improvements are at the fourth decimal place (CLIPIQA: 0.5353 → 0.5354; MUSIQ: 56.85 → 56.85). For UPSR on RealSRSet, QAlign regresses (3.705 → 3.656). The DPS mode is framed as a co-equal second contribution in the abstract and Section 3 (Eq. 17), but Table 5 provides only equivocal support. The paper should either scope this contribution more honestly or report variance estimates.

### Minor

- **Non-novel frequency loss accounts for substantial portion of gains**: Table 6 shows LDPV1 (frequency loss only, taken from Xie et al., 2023) achieves 23.99 PSNR vs 23.52 baseline, recovering roughly 57% of the total 0.83 dB gain attributable to LDPV7. The paper does not discuss this proportion explicitly. The LDP-specific symmetric loss (LDPV2: 24.08) contributes incrementally beyond the borrowed frequency loss, but the paper would benefit from clearly distinguishing LDP's novel contribution from the frequency baseline.

- **No ablation of LR_hf conditioning**: Section 3.1 devotes substantial argumentation to why LR_hf is the right condition (not LR itself, must be discriminative, easy to obtain). However, Table 6 ablates only loss terms—it does not include a variant where LR_hf is removed or replaced with a null condition. Without this, the performance benefit attributed to the conditioning mechanism cannot be isolated from the benefit of any cyclic regularization signal.

- **Mixed real-world results for FeMaSR on DPED**: Table 4 shows FeMaSR+LDP on DPED degrades on MUSIQ (49.14 → 44.07, −5.07), MANIQA (0.3102 → 0.2710), and NIQE (5.045 → 5.704). The paper explains this as perceptual metrics favoring "visually striking but structurally inaccurate" GAN outputs, which is a reasonable argument—but FeMaSR's NIQE regression (lower is better; degradation is 0.659) is harder to explain with the same reasoning, and the same logic is applied selectively across models. The claim in Section 4.3 that LDP "consistently improves performance" should be qualified.

### Trivial

- The synthetic test benchmarks (bsrGAN.plus) share degradation priors with LDP's training distribution (BSRGAN on LSDIR), though they differ in image content (DIV2K val vs. LSDIR train). The paper frames Table 3 improvements as generalization to "unknown complex degradations"—technically the degradation pipelines overlap, though the test images are unseen. The wording should be more precise.

---

## Nice-to-Haves

- Report sampling variance in Table 5 (e.g., across seeds for diffusion model inference); many DPS deltas are sub-0.01 in perceptual metrics and may be within typical sampling noise.
- Report parameter count and fine-tuning wall-clock time for Lway alongside LDP's 642K params / 16 hours, since the efficiency argument is central to the paper's positioning.
- The paper mentions that LDP is applied in the DPS setting via posterior sampling and treats SR outputs as clean images at each timestep. A brief discussion of how LDP's LR_hf conditioning is provided at inference time (from the LR input, not from a paired HR) would clarify the practical workflow.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **DR2 motivation "borrowed without verification"** (Harsh Critic §1): The paper cites Wang et al. (2023b) for the HR–LR alignment property and builds on it as a design choice with t ∈ [500, 1000]. Relying on prior theoretical results as architectural motivation is standard ML practice. This is not a meaningful flaw.

- **Synthetic benchmarks "partially in-distribution"** (Harsh Critic §4): While bsrGAN.plus shares degradation types with LDP's training pipeline, the test images are from DIV2K validation (different from LSDIR training set) and the full bsrGAN.plus degradation chain adds Real-ESRGAN patterns. This does not meaningfully undermine the generalization claim beyond the minor note already retained.

- **Table 6 column headers rendering identically**: This is a known parser artifact per the review policy. The ablation table is interpretable from the checkmarks/crosses and the LDPV labels.

- **DRN and DualSR as "uninformative baselines"** (Harsh Critic): The paper explicitly notes in Section 2.2 that "DRN handles only bicubic downsampling" and "DualSR requires image-specific optimization." Including them as baselines while acknowledging their limitations is not misleading—they represent prior-art degradation modeling approaches that happen to be limited in scope. The comparison is informative as an existence check against degenerate solutions (Table 2).

- **Strength Finder's claim that Table 4 shows improvements "for all tested models across almost all datasets"**: Partially removed due to genuine regressions for FeMaSR on DPED (MUSIQ, MANIQA, NIQE all worsen). Replaced by the more accurate characterization in the Strengths section.

- **Generic strength: "addresses an important problem"**: Removed per filtering rules.

---

## Novel Insights

LDP's most interesting design insight is the use of patch-dependent (rather than image-global) timestep sampling to capture spatially varying degradation, enabling the model to learn fine-grained local blur kernels rather than assuming homogeneous degradation. The conditioning on LR_hf—high-frequency components obtained by subtracting a double-downsampled-then-upsampled LR from the original LR—is a pragmatic solution to the ill-posedness of mapping a single HR image to multiple possible LR outputs under different degradations. These two design choices together allow a 642K-parameter model to serve as an effective proxy for degradation-aware cyclic consistency without the computational overhead of GAN-based or large generative degradation models. However, the ablation gap on LR_hf conditioning means the empirical contribution of this specific mechanism relative to generic cyclic regularization remains undemonstrated.

---

## Suggestions

1. **Run a head-to-head with Lway on at least one base model (e.g., SwinIR) and one benchmark (e.g., DIV2K-Hybrid)**: Report PSNR/SSIM/LPIPS and wall-clock fine-tuning time. Even qualitative parity with a speed advantage would substantially strengthen the paper's central positioning claim.

2. **Add an LR_hf ablation to Table 6**: Include a variant where the DPM is replaced by a constant condition or no condition. This directly validates Section 3.1's core design argument.

3. **Revise the DPS claims in abstract and Section 4.4**: Restrict "LDP enables test-time artifact correction" to models/datasets where gains are consistent (StableSR across all three benchmarks shows clear improvement). Present LDM's regressions transparently rather than describing the overall DPS results as improvements "across nearly all metrics on most datasets."

4. **Clarify the frequency loss attribution**: One sentence in Section 3.3 or the ablation discussion noting that LDPV1 (Xie et al., 2023's frequency loss) accounts for ~57% of the PSNR gain would fairly delineate LDP's novel contribution from the borrowed baseline.

---

## Evaluation on Key Axes

- **Originality**: Moderate. The combination of DAE degradation modeling with LR_hf conditioning and patch-wise noise is novel; individual components (frequency loss, DPS guidance, cyclic consistency) are borrowed from prior work.
- **Importance of research question**: High. Generalizing SR to unseen degradations is a core open problem with direct real-world relevance.
- **Claims well supported**: Moderate. Fine-tuning claims are well-supported; DPS claims are overstated; Lway comparison is absent.
- **Soundness of experiments**: Moderate-good. Diverse architectures and degradation types tested; DPS variance not reported; LR_hf not ablated.
- **Clarity of writing**: Good. Paper is well-organized; the selective framing of mixed results (Section 4.3, 4.4) is the main clarity concern.
- **Value to research community**: Moderate-high. A 642K plug-in with consistent improvements across 4 architectures is practically useful; gaps noted above limit full trust in all claimed modes.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>