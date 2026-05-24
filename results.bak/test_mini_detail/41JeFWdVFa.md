Here is the final consolidated review.

---

## Summary

This paper proposes LDP, a lightweight denoising autoencoder (DAE) plug-in designed to improve the generalization of existing SR models to unseen degradations. LDP models the SISR degradation process within a DAE framework, using patch-dependent noise injection, a degradation prediction module conditioned on LR high-frequency components, and a lightweight denoiser. It operates in two modes: (1) as an auxiliary loss during fine-tuning of SR models, enforcing LR cycle consistency, and (2) as an inference-time posterior sampling correction for diffusion-based SR models. Experiments across four SR architectures (FeMaSR, StableSR, SwinIR, MambaIR) and multiple degradation types show improvements in PSNR/SSIM/LPIPS on synthetic benchmarks and mixed gains on real-world benchmarks.

## Strengths

1. **Novel and lightweight design with clear motivation.** LDP (642K parameters) reinterprets degradation modeling as a denoising process, with patch-dependent noise injection enabling spatially-varying degradation modeling. The use of LR high-frequency components as a condition (rather than the LR itself) to avoid shortcut learning is well-motivated and supported by Table 2, which shows LDP's predictions are substantially less similar to bicubic downsampling than DRN's (e.g., PSNR 28.41 vs. 34.02 on the Down setting), confirming LDP learns genuine degradation factors.

2. **Extensive multi-architecture evaluation.** The paper evaluates LDP across four blind SR architectures (GAN-based FeMaSR, diffusion-based StableSR, transformer-based SwinIR, state-space MambaIR) for fine-tuning, and four diffusion models (LDM, StableSR, ResShift, UPSR) for posterior sampling. This breadth demonstrates the method's general applicability.

3. **Two complementary operational modes.** LDP works both as a training-time loss (fine-tuning) and an inference-time correction (posterior sampling for diffusion models). The posterior sampling mode (Table 5) shows some real-world improvements without requiring retraining (e.g., StableSR on RealSR: CLIPIQA +0.0191, MANIQA +0.0092), establishing utility beyond the fine-tuning setup.

4. **Ablation study provides practical guidance.** Tables 6–7 show that all combinations of the proposed loss terms outperform the baseline, with τ=100 and λ₁=λ₂=λ₃=1 emerging as robust defaults. This is useful for practitioners adopting the method.

## Weaknesses

### Major

1. **Missing control experiment: fine-tuning without LDP.** This is the most significant weakness. Table 3 compares pre-trained, off-the-shelf baseline models against the same models fine-tuned *with* LDP on DF2K+BSRGAN. The paper (Section 4.1) explicitly states that fine-tuning is done "with our LDP employed as an auxiliary loss," but provides no "fine-tuned without LDP" column. The observed gains (e.g., StableSR +2.16 dB PSNR on Hybrid, SwinIR +0.83 dB on Hybrid) could therefore come from additional training on a more diverse dataset (DF2K+BSRGAN) rather than from the LDP loss itself. Without this control, the central claim that LDP improves generalization is not properly supported. The ablation study (Tables 6–7) uses the same confounded setup — the "baseline" is the pre-trained SwinIR, not a SwinIR fine-tuned on DF2K+BSRGAN without LDP.

2. **Overclaimed generalization on "unseen" degradations.** The paper's title and abstract emphasize generalization to unseen real-world degradations. However, the synthetic test sets are generated using bsrGAN.plus (BSRGAN + Real-ESRGAN), which shares the same degradation pipeline as the fine-tuning data (BSRGAN patterns applied to DF2K). These are not truly unseen degradations — they are in-distribution with respect to the fine-tuning data. The real-world benchmarks (RealSR, DPED, RealSRSet) are more appropriate tests, but Table 4 shows multiple regressions: FeMaSR CLIPIQA drops by 0.1163 on RealSR, FeMaSR MANIQA drops by 0.0393 on DPED, StableSR CLIPIQA drops by 0.0605 on DPED. The paper's claim that LDP "consistently improves" performance does not hold across all metrics and datasets, and the paper partially acknowledges this for FeMaSR ("such metrics may favor visually striking but structurally inaccurate results") but this explanation is speculative.

3. **Marginal posterior sampling results with incomplete reporting.** Table 5 reports only no-reference metrics (NIQE, MANIQA, CLIPIQA, MUSIQ, QAlign) and omits reference metrics (PSNR, SSIM, LPIPS). Many improvements are extremely small (ResShift on DPED: +0.0001 CLIPIQA, +0.001 QAlign, -0.0003 MANIQA) and some are negative (LDM on RealSR: CLIPIQA -0.0245, QAlign -0.075). Without PSNR/SSIM/LPIPS it is unclear whether the corrections improve fidelity or merely shift perceptual metrics. For several model-dataset combinations, the changes are within the noise floor of the metrics.

### Minor

4. **No comparison to the most related method (Lway) on the SR improvement task.** Lway (Chen et al., 2024) — discussed in the related work — is conceptually similar: it uses a pre-trained degradation model to synthesize LR images from SR outputs and fine-tunes the SR model. Despite this overlap, the paper does not compare LDP against Lway on the main SR improvement task. DRN and DualSR are compared only on LR prediction (Table 1), not on whether they improve SR outputs when used as a loss. This makes it difficult to assess where LDP stands relative to the closest prior work.

5. **Missing ablations for core architectural choices.** The paper does not ablate: (a) patch-dependent vs. global noise schedule, (b) removal of the degradation prediction condition, (c) the choice of timestep range [500, 1000] (described as critical for "aligning noisy HR and LR features"), (d) the number of CRB blocks \(L\). These design choices are described as important but their individual contributions are not quantified.

6. **No error bars or statistical significance.** The paper reports single-point estimates throughout. Given that several reported gains are very small (e.g., MambaIR +0.05 PSNR on Down, +0.001 SSIM on Down), it is unclear whether these are meaningful improvements or within evaluation noise.

### Trivial

7. The term "plug-in" slightly overstates the ease of use — the fine-tuning mode requires retraining the SR model, which is more invasive than a true zero-cost plug-in.

## Nice-to-Haves

- A comparison to Lway on the SR improvement task would strengthen positioning versus the closest prior work.
- Reporting PSNR/SSIM/LPIPS for the posterior sampling experiments (Table 5) would help clarify whether fidelity is preserved.
- Evaluating LDP on a synthetically degraded test set using a degradation pipeline *different* from BSRGAN (e.g., non-Gaussian blur kernels) would directly test the generalization claim.
- An analysis of the additional inference cost when using LDP for posterior sampling (gradient computation through the DAE).

## Removed Points

These points were raised by the reviewers but are removed or demoted for the following reasons:

- **DR2 property overclaim (Section 3.1 Motivation):** The harsh critic states LDP "overclaims connection to diffusion models." The paper explicitly says it "leverages a property" — this is conceptual motivation, not an architectural claim. The paper states LDP is a DAE, not a diffusion model. Removed as unreasonable.
- **Degradation prompt initialization underspecified (Section 3.2):** The paper states \(P_D\) is "jointly learned" — this is standard practice for learnable embeddings. No further specification is expected for a prompt of this type. Removed as nitpick.
- **Timestep range [500, 1000] not analyzed:** Merged into Minor weakness #5 (missing ablations); no need for a separate entry.
- **"Section 4.2 not directly relevant":** The LR prediction experiments (Tables 1–2) are directly relevant — they establish that LDP works as a degradation model, which is a prerequisite for the cycle-consistency loss. Removed.
- **Missing related works:** Removed per hard rules — I cannot verify missing citations without external sources.
- **"Plug-in" terminology concern:** The paper acknowledges LDP requires fine-tuning in Section 4.3. This is clear from context. Demoted to Trivial #7.
- **Formatting/typography concerns:** Removed per hard rules — parser artifacts, not author errors.
- **Reproducibility concerns about missing hyperparameters/implementation details:** The paper already provides training details (Section 4.1), optimizer settings, batch size, learning rate, and loss weights. Removed.
- **Strength Finder's generic strengths:** "Addressed an important problem" and "well-motivated" without specific evidence — removed as generic/superficial.

## Novel Insights

The harsh critic's observation about the missing control experiment (fine-tuning without LDP) is the most insightful point, as it identifies a confound in the main experimental evidence that is not discussed in the paper itself. The strength finder's emphasis on Table 2 (distinguishing LDP from trivial downsampling) is useful — this is a genuinely informative experiment that the harsh critic underweights. No further novel insight emerges beyond the paper's own contributions.

## Suggestions

1. **Add the control experiment.** Fine-tune each baseline model on DF2K+BSRGAN *without* LDP for the same number of iterations. Report results in Table 3. If the gains hold, the central claim becomes credible.

2. **Test on truly out-of-distribution degradations.** Evaluate on degradations not covered by the BSRGAN pipeline (e.g., structured noise, non-Gaussian blur, arbitrary kernel shapes). This would directly support the generalization claim.

3. **Compare against Lway on the SR improvement task.** Report SR performance (PSNR/SSIM/LPIPS) after fine-tuning with Lway and with LDP under identical conditions.

4. **Report PSNR/SSIM/LPIPS for posterior sampling experiments** to clarify whether the corrections improve fidelity or just shift perceptual metrics.

5. **Provide error bars or confidence intervals** for the key comparisons, especially where gains are small.

## Score and Decision

**Round 1 bracket:** Based on the initial calibration search, the paper was bracketed between weak anchors (~3.0–3.2 for generic/weak SR papers) and strong anchors (~7.6–10.0 for exceptional papers), with the most relevant middle anchors at 5.25–5.80.

**Round 2 narrowing:** After reading full reviews of "Denoising as Adaptation" (5.80, Accept Poster), "Does Diffusion Beat GAN in ISR" (5.75, Reject), "Dissecting Arbitrary-scale SR" (5.25, Reject), and "Beyond Transformations" (3.67, Withdrawn), I compared the LDP paper to each:

- **"Denoising as Adaptation" (5.80):** Both address generalization in image restoration. That paper has no comparable experimental design flaw — its weaknesses are about scope and missing baselines. The LDP paper has a more fundamental issue (missing control experiment). LDP is weaker.

- **"Does Diffusion Beat GAN" (5.75):** An empirical comparison paper with limited novelty but solid execution. LDP has stronger novelty (a new method) but a more significant evidential gap. Comparable overall, slightly weaker due to the control issue.

- **"Dissecting Arbitrary-scale SR" (5.25):** A diffusion-based SR idea with interesting analysis but limited evaluation scope. LDP has more extensive experiments and two operational modes, but the missing control shifts quality downward. Comparable.

- **"Beyond Transformations" (3.67):** A diffusion-based data augmentation paper with limited novelty and unconventional evaluation. LDP is clearly stronger.

**Final calibration:** The paper sits between 3.67 and 5.80, closer to the lower end of this range due to the structural experimental flaw. Compared to the 5.25–5.75 anchors, the LDP paper's core claims are less well-supported by its experiments.

**Score: 4.5** — The paper presents a genuinely novel approach with extensive experiments, but the central experimental evidence (Table 3) is fundamentally confounded by the missing control condition, and the generalization claim is both overstated and partially contradicted by the real-world results. These issues are fixable but as presented, the evidence does not convincingly support the claims.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>