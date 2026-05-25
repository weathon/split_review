Now I have enough calibration data. Let me compile everything into the final review.

## Summary of calibration anchors

Let me list all anchors:

**Round 1 - Topic Low (< 3.5):**
1. OKOjkFrhSs (3.00) - Prompt-guided SR, thin contribution → LDP is stronger
2. hgayrNSbri (3.40) - Lightweight captioning, off-topic → not comparable
3. BefqqrgdZ1 (3.25) - Medical image segmentation → not comparable
4. exei8zvY13 (2.00) - Brain MRI SR, very weak → LDP is stronger

**Round 1 - Topic Mid (3.5-7.5):**
5. r2Ji0Bzd4g (6.20) - Meta pruning for lightweight SR → stronger paper, accepted-level quality
6. VYfYISQncf (4.50) - FedSR, frequency enhancement for diffusion SR → comparable rejection
7. Zrr6kH1cSh (4.50) - AdaSR, adaptive SR framework → comparable rejection
8. QO3yH7X8JJ (5.25) - Arbitrary-scale SR from diffusion → somewhat stronger

**Round 1 - Topic High (> 7.5):**
9. MEbNz44926 (8.00) - Binary SR → much stronger
10. j7b4mm7Ec9 (7.60) - Watermarking, off-topic
11. OlzB6LnXcS (8.00) - Shortcut Models diffusion → much stronger
12. QQBPWtvtcn (7.67) - Novel view synthesis → off-topic

**Round 1 - Weakness: degradation model cycle consistency:**
13. 46mbA3vu25 (5.75) - Diffusion vs GAN SR, controlled comparison → stronger but still rejected
14. MdBt0ttZrZ (3.50) - Laplacian detail loss → weaker
15. vTdwuKUc5Z (4.25) - Text prompt diffusion SR → similar weakness profile, rejected
16. JmGEZXkCH3 (3.67) - Augmentation for SR → weaker

**Round 1 - Weakness: posterior sampling mixed results:**
17. 46mbA3vu25 (5.75) - same as above
18. fx8AJDQRVB (4.25) - Latent diffusion SR → similar
19. BtT6o5tfHu (6.67) - Solving diffusion ODEs SR → accepted but had concerns about low PSNR
20. V2x5ZTHMae (4.00) - Enhancing DPS for inverse problems → similar

**Round 2 - (4.0-6.0) blind SR plug-in:**
21. BpKbKeY0La (5.00) - AddSR, diffusion distillation → similar weakness profile (perception-distortion imbalance)
22. vTdwuKUc5Z (4.25) - already listed
23. 1Qn1pMLYas (4.20) - Cycle consistency of image-text → off-topic
24. Zrr6kH1cSh (4.50) - already listed

**Round 2 - (4.5-6.5) SR plugin missing baselines:**
25. 46mbA3vu25 (5.75) - already listed
26. r2Ji0Bzd4g (6.20) - already listed
27. BpKbKeY0La (5.00) - already listed
28. FWpO8u2lim (5.25) - ClearSR, latent LR embeddings → similar

**Bracket after Round 1:** The paper sits between the low band (~3) and mid band (~4.5-6.2), probably around 4-5. The most comparable papers are FedSR (4.50), Text Prompt Diffusion (4.25), and AddSR (5.00) — all rejected.

**Round 2 narrowing:** Within the 4-6 range, the paper is comparable to FedSR (4.5) and Text Prompt Diffusion (4.25) — all share issues with missing baselines, mixed results, and insufficient evidence for claims. It's slightly weaker than AddSR (5.0) which had a clearer contribution (acceleration). The paper is weaker than the Does Diffusion Beat GAN paper (5.75) which had a more rigorous experimental design.

**Final score:** 4.5 — Weak reject. The paper has genuine contributions (lightweight design, consistent improvements across architectures) but the evaluation has significant gaps that prevent acceptance.

Now let me write the review.## Summary

The paper proposes LDP, a lightweight denoising autoencoder plug-in (642K parameters) for single-image super-resolution that enforces LR cycle consistency. It has two operating modes: as a training-time loss for fine-tuning SR models, and as an inference-time post-processing step for diffusion models via posterior sampling. LDP takes an HR/SR image as input, adds patch-dependent noise, passes it through a denoiser conditioned on LR high-frequency components, and produces a predicted LR image whose discrepancy with the ground-truth LR is used as a regularization signal. The method is tested on four SR architectures (FeMaSR, StableSR, SwinIR, MambaIR) across five synthetic and three real-world benchmarks.

## Strengths

1. **Consistent reconstruction improvements across architectures and degradation types (Table 3).** Adding LDP during fine-tuning raises PSNR/SSIM/LPIPS for StableSR, SwinIR, and MambaIR on all five synthetic degradation types. StableSR gains +2.16 dB PSNR on the Hybrid set. These gains are non-trivial in magnitude and hold across transformer, Mamba, and diffusion-based architectures.

2. **Lightweight plug-in with dual-mode flexibility.** LDP adds only 642K parameters (Section 4.1) and can be applied either as a training-time loss or as a post-processing gradient term at inference, distinguishing it from prior degradation-modeling approaches that require joint training, image-specific optimization, or much larger models.

3. **Avoids trivial degradation solutions (Table 2).** Unlike DRN, whose predicted LR images have very high PSNR similarity to simple bicubic-downsampled SR (≥34 dB), LDP's predicted LR images are substantially different from bicubic-downsampled SR, confirming that LDP applies non-trivial degradation rather than collapsing to bicubic.

4. **Ablation study validates the loss design (Table 6).** Each proposed loss component (frequency loss, symmetric cycle losses) contributes positively, and the full combination achieves the best result (24.35 dB PSNR on Hybrid). This provides empirical support for the loss formulation.

## Weaknesses

### Major

1. **No head-to-head comparison with existing degradation-based methods in the fine-tuning setting.** The paper motivates LDP against DRN, DualSR, SCL-SASR, and Lway in Section 2.2, claiming LDP overcomes their limitations. Yet Tables 3–5 compare only “baseline SR model vs. baseline + LDP.” There is no experiment where the same fine-tuning protocol is applied with DRN, DualSR, or even a fixed bicubic downsampler as the degradation module for the cycle loss. Without this comparison, it is impossible to determine whether LDP’s specific architecture (patch-dependent noise, learned prompt, frequency-aware loss) is responsible for the observed improvements or whether any cycle-consistency loss would yield similar gains. This is the most critical evidential gap.

2. **Ambiguous fine-tuning protocol.** Table 3 reports baseline numbers (e.g., SwinIR 25.44 dB PSNR on Down, MambaIR 26.58 dB) that closely match standard pre-trained model performance. The paper states “We fine-tune existing SR models on the DF2K dataset … with our LDP employed as an auxiliary loss” (Section 4.3) but does not clearly state whether the baseline columns also underwent the same fine-tuning (without LDP) or are simply pre-trained checkpoints. If the baselines were not fine-tuned, the comparison is fundamentally unfair and the reported gains could largely reflect the benefit of additional fine-tuning, not LDP specifically. The main text should unambiguously describe the protocol; deferring this to Appendix D is insufficient.

3. **No ablation against a simple cycle loss.** Variant LDPV1 (frequency loss only) already raises PSNR from 23.52 to 23.99 (Table 6). The paper never ablates LDP against a trivial cycle-consistency loss that uses a fixed bicubic downsampler with L1 or LPIPS — the most natural baseline for measuring whether LDP’s learned degradation model provides added value. This omission makes it difficult to attribute the improvements to LDP’s specific design.

4. **Overclaimed posterior-sampling results.** Table 5 shows that LDP *degrades* LDM on RealSR across all five metrics (NIQE +0.179, CLIPIQA −0.0245, MUSIQ −1.72, QAlign −0.075). For DPED, LDM also degrades on 3/5 metrics. The paper states “after applying LDP, the baselines show improvements across nearly all metrics on most datasets,” which is inaccurate for LDM. The claim should be qualified to reflect which models benefit and which do not.

5. **No error bars or statistical significance tests.** Many improvements are small (e.g., MambaIR +0.05 dB on Down, SwinIR +0.0032 SSIM on Down). Without multiple seeds or confidence intervals, it is impossible to distinguish genuine improvement from random variation. This is particularly important when the fine-tuning protocol itself is ambiguous (see point 2).

### Minor

1. **Misleading characterization of DRN.** The paper states that DRN “handles only bicubic downsampling” (Section 2.2) and “behaves almost identically to bicubic downsampling” (Section 4.2). Yet Table 1 shows DRN achieving competitive PSNR on Noise (27.25, best among all methods) and JPEG (29.65, best) — degradations a bicubic-only model would not handle well. While Table 2 supports the collapse claim (DRN’s outputs are similar to bicubic-downsampled SR), the framing in Section 2.2 is factually inconsistent with the paper’s own Table 1 and should be corrected or clarified.

2. **Some metrics worsen with LDP, and explanations are speculative.** FeMaSR’s LPIPS increases on Blur and Hybrid (Table 3). On real-world benchmarks (Table 4), FeMaSR’s CLIPIQA drops on RealSR (−0.1163) and DPED’s MUSIQ drops for FeMaSR (−5.07). The paper explains these as “GAN artifacts misinterpreted as texture” or “metrics favor visually striking but structurally inaccurate results.” These post-hoc explanations are not supported by any user study, alternative perceptual evaluation, or additional analysis.

3. **The diffusion-model motivation is ornamental.** The paper leverages the property that “after noise is added, HR images and LR features become aligned” to justify using a denoising autoencoder. However, LDP does not actually demonstrate that the claimed equivalence holds; the noise is simply used as a regularizer in a degradation model. The method could be described more directly as a learned degradation model with noise injection, without invoking diffusion alignment. This does not affect correctness but inflates the framing.

4. **Missing comparison with Lway (Chen et al. 2024).** Lway is the most recent work in the same line (test-time adaptation using a pre-trained degradation model) and is cited but never experimentally compared. Even if the settings differ (Lway is test-time, LDP is fine-tuning), a discussion of relative strengths or a simplified comparison would strengthen the paper.

5. **Computational overhead of DPS mode not reported.** The paper claims LDP is lightweight but does not report the per-step cost of the DPS gradient computation for inference-time use, which could be significant when applied over hundreds of diffusion steps.

6. **Limitations section omits key weaknesses.** Section 6 lists two limitations (no generative ability in posterior sampling, no unpaired degradation) but does not mention the lack of comparisons with cycle-consistency methods, the ambiguous fine-tuning protocol, or the mixed posterior-sampling results.

### Trivial

1. **Figure 2 caption inconsistency.** The caption reads “Low-Degradation Prediction (LDP)” while the paper title uses “Lightweight Denoising Plugin.” The diagram is dense and the distinction between the Denoiser Module and the downsampling path is under-labelled.

## Nice-to-Haves

- Compare LDP against a simple cycle-consistency baseline (e.g., fixed bicubic downsampler + L1 loss) during fine-tuning to isolate the benefit of LDP’s learned degradation model.
- Report results with error bars (multiple fine-tuning seeds) for the fine-tuning experiments.
- Provide a head-to-head comparison with DRN or Lway used as the degradation module in the same fine-tuning protocol.
- Report the per-iteration FLOPs/latency of LDP in posterior-sampling mode.

## Removed Points

These points were considered and removed from the main weaknesses with justification:

- **“Figure 1 equation `LR' = ((SR+n)*k)↓` is a simplification that doesn’t match the architecture”** — Removed. Figure labels are simplified illustrations; this is standard pedagogical practice, not an error.
- **“Missing Appendix D details”** — Removed per instructions: the parser strips appendix content; these exist in the original submission.
- **“Section 3.2 condition shortcut learning risk not analysed”** — Removed. This is a speculative concern without evidence; the paper validates the design empirically in Tables 1–2 and Table 6.
- **“Comparison with Lway not done even though the paper highlights it”** — Demoted to Minor (already present in minor #4). The reviewer overstated the obligation given Lway operates in a test-time setting.
- **“Pure formatting/style nitpicks”** — Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard tension between a plausible method and an incomplete evaluation, but do not reveal any fundamentally new analytical perspective on the problem.

## Suggestions

1. **Add a controlled cycle-loss baseline:** Fine-tune the same SR models using a fixed bicubic downsampler to compute the cycle loss (L1 or LPIPS) instead of LDP. This directly tests whether LDP's learned degradation model adds value over a trivial alternative.

2. **Clarify the fine-tuning protocol in the main text:** State explicitly whether baseline models were also fine-tuned under identical settings (without LDP). If they were not, the comparison must be re-done with properly fine-tuned baselines.

3. **Add error bars:** Run 3 seeds of fine-tuning for at least one model (e.g., SwinIR) and report mean ± std for the main metrics to establish statistical significance.

4. **Correct the DRN characterization:** Acknowledge that the DRN model used in experiments may handle non-bicubic degradations better than the original DRN paper suggested, and reframe the motivation accordingly.

5. **Honestly bracket the posterior-sampling results:** Report that LDP helps StableSR and UPSR but consistently degrades LDM, and qualify the claim accordingly.

6. **Add real-world inference cost analysis for DPS mode.**

## Score and Decision

**Round‑1 bracket (wide):** Topic-anchored quality ladder positioned the paper in the mid band (3.5–7.5). Weakness-anchored queries showed that papers with similar evaluation gaps (missing baselines, mixed results, insufficient comparisons) cluster between 3.5 and 5.75, with most rejected.

**Round‑2 narrowing (4.0–6.0):** Direct comparison with three rejected anchors — FedSR (4.50, frequency plug-in for diffusion SR with similar evaluation weaknesses), Text Prompt Diffusion for SR (4.25, missing baselines and limited novelty), and AddSR (5.00, perception-distortion imbalance) — confirms the paper sits in the 4.0–5.0 range. The paper is not as strong as the controlled-comparison study (5.75) or the diffusion ODE method (6.67, accepted), but is comparable to or slightly stronger than the weakest rejected anchors due to its more extensive architecture coverage and ablation study.

**Final score:** 4.5. The core idea (lightweight LDP module with dual-mode cycle consistency) has merit, and Table 3 provides genuine evidence of improvement. However, the evaluation has significant gaps — no comparison with existing cycle-consistency methods, an ambiguous fine-tuning protocol, overclaimed posterior-sampling results, and no ablation against a simple cycle loss — that collectively prevent the paper from making a convincing case for its stated contributions. The weaknesses are addressable but require substantial additional experiments.

**Decision:** Reject

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>