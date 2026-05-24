Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes LDP (Lightweight Denoising Plugin), a 642k-parameter conditional degradation model built within a denoising autoencoder framework. LDP takes a high-resolution (HR or SR) image and produces a predicted LR image, conditioned on the high-frequency components of the target LR (y\_hf). It can be used in two modes: (1) as an auxiliary cycle-consistency loss during fine-tuning of existing SR models, and (2) as a posterior-sampling correction during inference for diffusion-based models. Experiments across four SR architectures (FeMaSR, StableSR, SwinIR, MambaIR) and multiple synthetic/real-world benchmarks show consistent metric improvements.

## Strengths

1. **Consistent improvements across diverse architectures and degradation types (Table 3).** Every baseline model gains in PSNR, SSIM, and LPIPS on all five synthetic degradation settings when fine-tuned with LDP. The gains are sometimes large (StableSR +2.16 dB PSNR on Hybrid). This breadth of evaluation (4 architectures, 5 degradation types) is a genuine strength.

2. **Lightweight and dual-mode design.** LDP has only 642k parameters and can be used both as a training-time loss and as an inference-time post-processing module. Prior degradation-modeling methods (DRN, DualSR, Lway) are either limited to specific degradations, require image-specific optimization, or incur high computational cost. LDP's parameter efficiency and dual-mode flexibility are concrete differentiators.

3. **Principled design avoids collapse to trivial downsampling.** Table 2 shows that LDP-generated LR images have substantially lower similarity to the downsampled SR than DRN's LR images do (e.g., PSNR 28.41 vs. 34.02 on Down). This confirms that LDP learns actual degradation rather than degenerating into bicubic downsampling. The conditioning on y\_hf is key to this behavior.

4. **Ablation study of loss components (Table 6).** The ablation on SwinIR shows that each proposed loss component contributes positively, and the full combination achieves the best result (24.35 PSNR vs. baseline 23.52). This provides evidence that the specific LDP loss formulation matters, not just the fact of fine-tuning.

## Weaknesses

### Major

1. **Missing control experiment: fine-tuning without LDP.** The paper compares each +LDP model (fine-tuned on DF2K with BSRGAN degradation patterns) against the same model **without any fine-tuning at all** (Tables 3, 4). The observed improvements could therefore be caused entirely by the additional fine-tuning on more diverse degradations, independent of the LDP mechanism. A proper control requires fine-tuning each baseline on the same data (DF2K+BSRGAN) using only the original loss or a simple alternative cycle loss (e.g., bicubic downsampler + L1). Without this, the contribution of LDP's specific formulation over and above "more fine-tuning on diverse data" is not established. The ablation study (Table 6) partially mitigates this by showing that LDPV7 (all LDP losses) outperforms LDPV1 (frequency loss only) by 0.36 dB, but it does not control for fine-tuning with the original loss alone. This is the central evidential gap that prevents the paper's core claim from being fully supported as written.

2. **Unfair comparison in LR-prediction experiment (Tables 1–2).** In Table 1, LDP receives the high-frequency component of the target LR (y\_hf, Eq. 4) as conditioning, while DRN and DualSR receive no such target-derived information. This gives LDP a structural informational advantage — it knows details about the target before predicting it — so the comparison does not fairly evaluate which model is a better degradation model. The paper does acknowledge this implicitly by noting that DRN "fails to map an SR image to the multiple possible LR variants" because it lacks conditional signals. However, presenting Table 1 as a straightforward performance comparison without clearly flagging this asymmetry is misleading. Table 2 remains informative (it shows LDP does not collapse to trivially downsampling the SR), but the framing of Table 1 needs significant correction.

3. **Missing critical baselines for posterior-sampling mode (Table 5).** The paper compares LDP-guided sampling against the base diffusion models without any guidance. The relevant comparisons are against existing posterior-sampling or guidance methods such as DPS (Chung et al. 2023), DR2 (Wang et al. 2023b), or ILVR (Choi et al. 2021) — all cited in the paper. Without these, the reader cannot assess whether LDP's guidance adds value beyond existing techniques. Moreover, some gains in Table 5 are extremely small (e.g., ResShift on DPED: most metrics change by <0.001), which suggests LDP provides negligible benefit for some models.

### Minor

4. **Limited scope of ablation studies.** The ablation of loss terms (Table 6) and the τ weight (Table 7) are conducted only on SwinIR on the synthetic Hybrid dataset. Key design choices — patch size, timestep range [500,1000] vs. alternatives, use of y\_hf vs. other conditioning signals, number of CRBs, DWT-based weighting — are not ablated. The paper's claim that "LDP parameters can be universally configured as τ=100 and λ₁=λ₂=λ₃=1 for any super-resolution model" is too strong given the limited ablation evidence.

5. **Computational overhead not quantified.** The paper claims LDP is "lightweight" based on its 642k parameter count, but does not report wall-clock time or memory overhead during fine-tuning (gradient through LDP, DWT computation) or during inference (forward pass through LDP at every diffusion step). This makes the lightweight claim only partially verified.

6. **Some real-world metrics worsen.** In Table 4, several metrics degrade for FeMaSR+LDP (e.g., CLIPIQA drops by 0.1163 on RealSR, MANIQA drops by 0.0393 on DPED). The paper attributes this to GAN artifact suppression, which is plausible but lacks quantitative support (e.g., a dedicated artifact metric or user study). This selective reporting weakens the evidence.

### Trivial

7. The "Degradation Prompt P\_D" (Section 3.2) is mentioned but never explained — what it is, how it is initialized, what it learns. This is a dangling detail.

## Nice-to-Haves

- A proper control: fine-tune each baseline on DF2K+BSRGAN using only the original model loss, to isolate LDP's specific contribution.
- Compare posterior-sampling mode against DPS, DR2, or ILVR.
- Report standard deviations or confidence intervals for main results.

## Removed Points

*Criticism 3 (Conceptual mismatch between motivation and implementation)* — Removed. The paper's use of the DAE framework is coherent: at high noise levels, the distributions of noisy HR and noisy LR features converge (a known property from DR2), so denoising noisy HR to produce LR features is a valid application. The DAE does not need to reconstruct its original input; the target can be LR. The framing is creative, not erroneous.

*Criticism about timestep range [500,1000] limiting degradation variety* — Demoted. This is a reasonable design choice. Without an ablation showing it matters, it is speculation; moved from the main weaknesses since the authors could reasonably defend the choice.

*Criticism that ablation of architectural choices is missing* — Demoted. This is a valid point but the paper does note that additional ablation details are in Appendix F. It remains as Minor weakness #4 above in the merged form.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation not already present in the paper.

## Suggestions

1. **Run the missing control experiment** that is standard in fine-tuning papers: fine-tune each baseline on DF2K+BSRGAN using the original SR loss (no LDP), and compare against +LDP. If LDP still wins, the paper's core claim would be properly supported.
2. **Reframe the LR-prediction experiment (Tables 1–2):** explicitly acknowledge that LDP uses y\_hf conditioning (which is available in practice) and that Table 1 shows what is attainable with this design rather than a head-to-head contest. Separate the "LDP does not collapse to downsampling" message (Table 2) more clearly.
3. **Add posterior-sampling baselines** (DPS, DR2, ILVR) to Table 5, or at minimum discuss why the comparison is informative without them.
4. **Report computational overhead** in terms of wall time and memory for both training and inference modes.
5. **Expand ablations** to cover key architectural choices (timestep range, patch size, conditioning alternatives) and run them on more than one model/dataset.

## Score and Decision

**Calibration Report.**

Round 1 (bracketing): Weak anchors at 2.00–3.67 (exei8zvY13, OKOjkFrhSs, JmGEZXkCH3 — all rejected, weaker methodology/evidence). Middle anchors at 5.25–6.50 (ClearSR 5.25/reject, AddSR 5.00/reject, RealDGen 6.00/accept, EATS 6.50/reject). Strong anchors at 8.00–10.00 (beyond this paper). Initial bracket: 4.0–5.5.

Round 2 (narrowing): ClearSR (5.25, rejected) — similar missing-baseline issues but LDP has broader architecture coverage. AddSR (5.00, rejected) — perception-distortion trade-off issues not present in LDP. The 4.25 anchor (Text Prompt SR, rejected) — weaker evidence overall. After comparison: LDP is stronger than the 4.25 anchor, comparable to ClearSR/AddSR but with a cleaner story and broader evaluation, yet the missing control experiment is a comparable evidential gap. Positioned at 4.5.

Round 3: Not needed — bracket sufficiently narrowed.

Anchor paths: OKOjkFrhSs (3.00), exei8zvY13 (2.00), JmGEZXkCH3 (3.67), FWpO8u2lim (5.25), BpKbKeY0La (5.00), JkCJBoNUcU (6.00), my0RqY48xz (6.50), vTdwuKUc5Z (4.25), 1Qn1pMLYas (4.20), fx8AJDQRVB (4.25).

This paper addresses an important problem and proposes a well-motivated approach. However, the central evidential gap (missing control for the fine-tuning experiments) means the paper, as presented, does not establish that LDP's specific formulation — rather than additional fine-tuning on diverse degradations — is responsible for the observed improvements. The contribution is plausible but not yet proven to the standard expected for acceptance. A major revision with the missing control experiment and proper baselines could address this.

MY FINAL SCORE: 4.5
MY FINAL DECISION: Reject