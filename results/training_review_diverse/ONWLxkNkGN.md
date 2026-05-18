Now I have thoroughly verified all claims against the paper. Let me compose the final consolidated review.

---

## Summary

This paper introduces InstantIR, a diffusion-based blind image restoration method that dynamically generates "instant references" during the reverse diffusion process. The key idea is a Previewer module (a consistency-distilled diffusion model) that decodes the compact LQ representation at each denoising step into a restoration preview, which is then fused with the original LQ encoding via an Aggregator module using SFT-based fusion. This iterative alignment with the generative prior is designed to handle unknown degradations. The paper also proposes an adaptive sampling algorithm (AdaRes) that modulates Aggregator influence based on an estimated input quality indicator, and demonstrates controllable restoration via text prompts.

## Strengths

- **Novel previewing mechanism for dynamic condition alignment (well-supported)**: The idea of decoding the compact LQ representation into a restoration preview at each diffusion step, then fusing it back with the LQ encoding via the Aggregator, is genuinely novel. The design choices — consistency distillation of the Previewer for one-step generation, SFT-based fusion in the Aggregator — are clearly motivated and ablated. The ablation study (Table 5b, rows 1 vs 2) confirms that adding generative references dramatically improves non-reference metrics (CLIPIQA from 0.2721 → 0.5445, MUSIQ from 42.64 → 64.86), demonstrating that the core previewing mechanism is essential.

- **Consistent SOTA on non-reference perceptual metrics across all settings**: InstantIR achieves the highest MUSIQ and MANIQA scores on all four evaluation configurations (synthetic and real-world at both 512² and 1024² resolutions), outperforming the second-best method by up to 22% in MANIQA and 8% in MUSIQ (Table 1). This result is consistent and well-documented.

- **Thorough ablation of core design choices**: The paper ablates key components including consistency distillation of the Previewer (Table 5a), the use of generative references vs. no references vs. noisy previews (Table 5b), and the text-conditioned DCP training (Fig. 6). These experiments confirm the necessity of the previewing mechanism and validate the design decisions.

- **Controllable restoration via text prompts**: By retaining text cross-attention and disabling the Aggregator at later stages, InstantIR can perform semantic editing during restoration (Fig. 5). While not the core contribution, this extends the method's applicability beyond standard BIR.

- **Two-stage training strategy**: Training the DCP and Previewer before the Aggregator prevents error accumulation, a practical contribution that ensures stable training.

## Weaknesses

### Fatal
None.

### Major

- **Large PSNR/SSIM deficit is inadequately addressed given the paper's "SOTA" framing**: InstantIR trails baselines by 4–6 dB on PSNR on real-world datasets (e.g., 21.75 vs. Real-ESRGAN's 27.29 on RealSR in scenario 1). The paper acknowledges this only briefly, dismissing it as "misalignment of PSNR and SSIM scores with visual quality" (line 225) and a side effect of "excessive generative prior" (line 323). However, a 5+ dB gap is extreme, and the paper continues to claim "SOTA performance in quantitative metrics" (abstract, conclusion) without qualifying that this applies only to non-reference perceptual metrics. The central claim needs reframing: the contribution should be positioned as a **perceptually-driven** restoration method with an explicit fidelity–perception trade-off, not as a general-purpose BIR method achieving overall SOTA. Without this reframing or evidence that the lost PSNR comes from removing degradations rather than altering content, the reader cannot assess whether the method is genuinely restoring or merely generating attractive but unfaithful images.

- **Adaptive sampling (AdaRes) — listed as a main contribution — shows negligible empirical benefit**: Table 5b (rows 2 vs 3) shows that adding AdaRes to the pipeline that already uses generative references changes CLIPIQA from 0.5445 to 0.5456, MANIQA from 0.3747 to 0.3766, and MUSIQ from 64.86 to 64.94. These differences are within the noise of a single run without reported confidence intervals. The paper claims AdaRes "further improves the non-reference metrics" (line 264), but the numbers do not support a meaningful improvement. Since adaptive sampling is highlighted as contribution item 3 and motivated with a dedicated algorithm (Alg. 1) and theoretical analysis (Eq. 4, Fig. 3), the disconnect between the framing and the empirical evidence is significant. Either stronger evidence (e.g., controlled experiments across varied degradation levels showing systematic behavioral changes) or de-emphasis of this claim is needed.

### Minor

- **No confidence intervals or error bars**: None of the quantitative results report standard deviations or confidence intervals. Given that several metric differences between methods are modest (e.g., CoSeR vs. InstantIR on CLIPIQA in Table 1, or the AdaRes ablation), the reader cannot assess statistical significance. This is a standard expectation for empirical papers.

- **No inference cost comparison**: The paper does not report runtime, GPU memory, or parameter count relative to baselines. Since the method requires running a Previewer (LoRA) and Aggregator forward pass at each of 30 DDIM steps, the computational overhead is likely substantial and should be quantified.

- **Synthetic evaluation uses the same degradation pipeline as training**: The synthetic test set is generated using the Real-ESRGAN pipeline (line 217), which is the same pipeline used to create training LQ-HQ pairs (line 213). While real-world tests on RealSR/DRealSR partially mitigate this concern, the paper's core motivation (handling *unknown* degradation) would be better supported by evaluation on a held-out degradation type.

### Trivial
- Minor phrasing issues (e.g., "flexibility in to different conditions" on line 264).

## Nice-to-Haves
- **User study**: A pairwise preference judgment study between InstantIR and baselines (presented alongside the LQ input) would directly validate that the perceptual metric improvements translate to genuine human preference, addressing the fidelity concern.
- **Fidelity–perception trade-off analysis**: An experiment varying the Aggregator influence (e.g., via the w^l parameter in Eq. 2) and plotting the resulting PSNR vs. perceptual metric curve would demonstrate that InstantIR can be tuned across the operating spectrum, rather than accepting the large PSNR gap as a fixed cost.
- **Failure cases**: Showing examples where InstantIR produces unfaithful outputs or artifacts would improve the paper's credibility.

## Removed Points
- The harsh critic's concern about the paper not "explicitly stat[ing]" that training used only training splits — the paper states "DIV2K and LSDIR validation sets" for evaluation, and the training datasets (DIV2K, LSDIR, Flickr2K, FFHQ) are standard benchmarks where training/validation splits are conventional; this concern is not substantive.
- The strength "Adaptive restoration algorithm based on input quality" from the Strength Finder is removed because the empirical evidence (Table 5b) shows negligible benefit, creating a verified conflict per the meta-review rules.
- The claim that "the paper's practical value depends partly on [inference cost]" being framed as a weakness rather than a nice-to-have — this is a reasonable suggestion but not a weakness of the contribution.

## Novel Insights
The most interesting observation from the reviews is the tension between the paper's genuinely novel previewing mechanism (which demonstrably improves perceptual quality) and the framing of the contributions. The previewer+aggregator architecture is a creative solution to the BIR distribution-shift problem, and the empirical results on perceptual metrics are consistent and meaningful. However, the paper's effectiveness is partly obscured by two framing choices: (1) claiming broad "SOTA" while downplaying the large PSNR gap, and (2) elevating the AdaRes mechanism to a main contribution when its empirical impact is negligible. The core idea — iterative decoding of compact representations into on-the-fly references during diffusion — is strong enough to stand on its own without these overclaims.

## Suggestions
1. Reframe the contribution transparently: "InstantIR achieves SOTA perceptual quality (MUSIQ/MANIQA) on blind image restoration, with an explicit trade-off in pixel fidelity quantified in Table 1." Remove or qualify broad "SOTA performance" claims.
2. Either provide convincing evidence for AdaRes (controlled experiments varying degradation levels, sensitivity analysis, results on the full test set with confidence intervals) or demote it from the main contribution list to a secondary exploration.
3. Add confidence intervals to all quantitative results.
4. Report inference speed and GPU memory vs. baselines.

## Score and Decision

**Originality**: 7/10 — The previewing mechanism is genuinely novel and well-conceived.  
**Importance**: 7/10 — Addressing unknown degradation in BIR is an important and active problem.  
**Claims support**: 5/10 — The perceptual metric results are well-supported, but the broad "SOTA" claim is overreaching, and the AdaRes contribution is not supported.  
**Soundness**: 6/10 — The experimental design is reasonable but lacks confidence intervals and has an in-distribution synthetic evaluation concern.  
**Clarity**: 6/10 — The architecture and method are clearly described, but the framing of claims needs adjustment.  
**Value to community**: 6/10 — The previewing mechanism is a useful conceptual contribution, but the practical utility depends on the unquantified fidelity–perception trade-off.

The paper introduces a genuinely novel and well-motivated architecture with consistent non-reference metric improvements. However, the framing overreaches (unqualified "SOTA" claims despite a 4–6 dB PSNR deficit), one of the three listed contributions (AdaRes) is empirically unsupported, and the evaluation lacks standard error estimates. These are major but addressable issues — the core previewing contribution is solid. A revised version that reframes claims honestly and either validates or drops AdaRes would be strong.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>