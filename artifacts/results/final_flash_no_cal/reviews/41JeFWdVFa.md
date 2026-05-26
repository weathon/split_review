Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

The paper proposes LDP, a lightweight denoising autoencoder plug-in (642k parameters) that improves the generalization of pre-trained single-image super-resolution (SISR) models to unseen degradations. LDP models the degradation process within a DAE framework: it takes an HR/SR image as input, adds patch-wise noise, conditions on the high-frequency component of the target LR image, and learns to reconstruct the corresponding LR image via a denoiser with adaptive layer normalization. LDP operates in two modes — as a training-time loss that enforces LR cycle consistency during SR model fine-tuning, and as an inference-time posterior sampling correction for diffusion-based SR models. Experiments on four SR architectures (FeMaSR, StableSR, SwinIR, MambaIR) across five synthetic degradation types and three real-world benchmarks show consistent improvements in PSNR, SSIM, LPIPS, and no-reference metrics.

## Strengths

- **Novel and well-motivated formulation.** Casting degradation modeling as a denoising autoencoder that leverages the property that noisy HR and LR features become aligned (borrowing from diffusion theory) is a creative architecture-level contribution. The patch-wise noise schedule and the use of $y_{hf}$ as a lightweight condition to distinguish different LR outputs from the same HR input are sensible design choices that are explicitly grounded in the paper's motivation.

- **Consistent empirical gains across diverse SR backbones.** Tables 3 and 4 show that fine-tuning with LDP improves PSNR, SSIM, and LPIPS for all four blind SR models (CNN-based FeMaSR, diffusion-based StableSR, Transformer-based SwinIR, Mamba-based MambaIR) on all five synthetic degradation types. Some gains are substantial (e.g., StableSR +2.16 dB PSNR on Hybrid; SwinIR +0.83 dB on Hybrid). On real-world benchmarks, the fine-tuned models improve on most no-reference metrics (MUSIQ, QAlign, CLIPIQA) for most model–dataset pairs.

- **Lightweight and practical.** LDP adds only 642k parameters, trains on a single GPU in 16 hours, and can be plugged into existing pre-trained SR models without architectural modifications. The dual-mode design (training loss + inference-time posterior sampling) increases practical utility.

- **LDP demonstrably does not collapse to trivial downsampling.** Table 2 shows that the similarity between LDP's predicted LR and a simple bicubic-downsampled SR is significantly lower than DRN's, confirming that the degradation model learns meaningful degradation patterns beyond simple interpolation.

## Weaknesses

### Major

- **Central experiment lacks a proper fine-tuning baseline without LDP.** The paper's primary evidence for LDP's effectiveness (Tables 3 and 4) compares models fine-tuned *with* the LDP loss against the *original pre-trained checkpoints* of those models. This conflates two factors: the LDP loss itself and the effect of continued training on a broader, multi-degradation dataset (DF2K with BSRGAN patterns). Without an ablation that fine-tunes each SR model on the same data for the same number of steps using only the model's original loss (without the LDP loss), the contribution specifically attributable to LDP's cycle-consistency constraint cannot be isolated. The ablation study (Table 6) compares variants of LDP's loss components against the original pre-trained SwinIR, but crucially does not include a "fine-tune with original SR loss only" condition. For models like MambaIR where the reported gain is tiny (e.g., +0.05 dB PSNR on the Down set), the uncontrolled design makes the result uninterpretable.

### Minor

- **Overclaiming in the posterior-sampling results (Table 5).** The paper states that after applying LDP, "the baselines show improvements across nearly all metrics on most datasets." Inspection of Table 5 reveals that this is overstated. For LDM on RealSR, *every* metric degrades (NIQE 6.651→6.830, MANIQA 0.2904→0.2810, CLIPIQA 0.4564→0.4319, MUSIQ 52.09→50.37, QAlign 2.685→2.610). For ResShift on RealSR, the changes are essentially zero. The claim should be qualified to acknowledge that posterior-sampling gains are concentrated in diffusion models that already have moderate baseline quality (StableSR, UPSR) and are not universal.

- **Notation inconsistency between Eq. 4 and implementation.** In Eq. 4, the high-frequency component is extracted using a downscale factor of $s^2$ (which would be 16 for the main $s=4$ setting). The implementation in Section 4.1 instead uses $s' = 2$. The paper should clarify whether $s^2$ in Eq. 4 is a notational error or a separate hyperparameter, as this directly affects what information $y_{hf}$ contains and the reproducibility of the method.

- **The conditioning shortcut risk is acknowledged but not empirically examined.** The paper correctly notes that the condition $y_{hf}$ must not allow the degradation model to bypass learning meaningful degradation parameters (Section 3.1, criterion 1). However, no ablation tests whether swapping $y_{hf}$ with random noise or a constant degrades performance. Given that the DPM is designed to extract structure from $y_{hf}$ to predict degradation weights, an experiment isolating the information flow from $y_{hf}$ versus from the SR input would strengthen the paper's claims.

- **Reporting lacks variance estimates.** No confidence intervals, standard deviations, or repeated-run statistics are provided. While single-run evaluation is standard in large-scale SR benchmarking, the absence of variance information makes it impossible to assess whether very small reported gains (e.g., MambaIR +0.05 dB on Down, SwinIR +0.0034 SSIM on Hybrid) are meaningful or within measurement noise.

- **Uneven gains across models are not discussed.** The improvements are far from uniform: StableSR and FeMaSR (models with initially poor fit to diverse degradations) show large gains, while Transformer and Mamba baselines show modest improvements. The paper would benefit from discussing this heterogeneity to clarify *when* LDP helps most — this is informative for practitioners deciding whether to adopt the method.

### Trivial

- The figure caption descriptions of the data flow between the NAM, Denoiser, and Downsample modules are somewhat inconsistent across Figure 2(a) and Figure 2(d). For instance, (a) states that NAM produces $F$, while (d) states the Denoiser produces $F$. The paper should harmonize these descriptions to avoid confusion.

## Nice-to-Haves

- A "fine-tune on DF2K+BSRGAN without LDP" baseline for all four SR models in Tables 3 and 4 would cleanly resolve the main attribution question. The ablation in Table 6 partially addresses this for SwinIR by showing that LDPV1 (frequency loss only) improves from 23.52→23.99, but this still uses a frequency loss that is not the original SR loss. Showing the effect of vanilla fine-tuning would establish the marginal contribution of the LDP symmetric loss.
- A failure-case analysis for the posterior-sampling mode (Table 5), especially for LDM where all metrics degrade, would make the conclusions more nuanced and credible.
- The conditioning shortcut could be tested by a simple ablation that replaces $y_{hf}$ with Gaussian noise during LDP inference.
- Reporting standard deviations (even from a small number of runs on a representative subset) would improve statistical credibility.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"Architectural exposition is difficult to follow (Denoiser data flow)."* — The figure captions are slightly inconsistent, but the equations (Eqs. 2–3, 7–12) and the body text provide a complete and unambiguous description of the data flow. The critic's claim that the Denoiser is described as taking $HR_t$ and $z$ in the body text while Figure 2(d) shows $C'$ and $x_t$ is a misreading: $z$ is an internal variable derived from $C'$ and $t_{emb}$, not an independent input. The description is adequate for reproducibility.
- *"Comparison against DRN/DualSR on Noise/Blur/JPEG/Hybrid is an easy win by design."* — DRN and DualSR are the established baselines in the degradation-modeling literature. DRN was designed for bicubic degradation and its limitations are well-known; DualSR is an image-specific optimization method. The comparison is fair and standard. There is no requirement that baselines be competitive on all degradation types.
- *"The paper consistently frames the problem as 'unseen degradations' yet fine-tunes on synthetic data matching the test sets."* — This is a partial misreading. The pre-trained models were trained on narrow degradation distributions; the BSRGAN-based fine-tuning data exposes them to a wider but still synthetic range. The test sets include both synthetic (DIV2K-based with specific held-out degradation configurations) and real-world datasets (RealSR, DPED, RealSRSet). The framing is standard for blind SR generalization papers and not misleading.
- *"No statistical significance / confidence intervals."* — Single-run evaluation is the norm in large-scale SR benchmarks. The absence of variance estimates is a field-standard practice, not a unique flaw of this paper. Demoting to Minor is generous; it is included as a minor weakness only because some gains are extremely small.
- *"Tables 1–2, LDP's lower similarity to downsampled SR shows it is not a trivial downsampler but does not demonstrate correct modeling of the specific degradation."* — The paper compares LDP's predicted LR against the input LR (Table 1) and shows competitive or better PSNR/SSIM/LPIPS than DRN and DualSR across all five degradation types. This directly demonstrates that LDP models the *specific* degradation, not just any random degradation.
- *"The magnitude of improvements suggests LDP primarily benefits models with poor initial fit."* — This is an informative observation but stated as a weakness, when it is actually useful context for understanding the method's scope. The paper could discuss this more, but it is not a flaw.
- *"Missing related works."* — Cannot be verified without external sources, and the instruction prohibits mentioning missing related works.

## Novel Insights

Beyond the paper's own contributions, the review highlights a structural tension: LDP's main experimental design (comparing LDP-fine-tuned models against original pre-trained checkpoints) cannot separate the effect of the cycle-consistency loss from the effect of continued training on broader degradation data. This is ironic because the method's core motivation is precisely about constraining the solution space via cycle consistency — yet the evaluation does not include the one baseline that would isolate that constraint. A second synthetic insight is that the posterior-sampling results (Table 5) reveal LDP's dual role is highly model-dependent: it helps StableSR and UPSR meaningfully but hurts or does nothing for LDM and ResShift. This suggests the inference-time gradient correction interacts non-trivially with the base diffusion model's pretraining distribution and noise schedule, a point the paper does not explore.

## Suggestions

- **Add a vanilla fine-tuning baseline** for all four SR models in Tables 3–4 (same data, same steps, original loss only). This is the single most important missing experiment.
- **Tone down the claim about Table 5** to accurately reflect that LDM and ResShift see essentially no benefit or degradation on real-world datasets.
- **Clarify the notation in Eq. 4** — if the hyperparameter is $s'$ (set to 2 in implementation) rather than $s^2$, revise the equation accordingly.
- **Add a conditioning ablation** that replaces $y_{hf}$ with a fixed signal (e.g., zeros or random noise) during LDP inference to confirm the condition is necessary and not a shortcut.
- **Discuss the heterogeneous gains** across models — this would strengthen the paper's practical guidance and scientific value.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>