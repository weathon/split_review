Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes a method for hiding images in diffusion models by editing the learned score function at a single secret time step, enabling one-step extraction. A hybrid parameter-efficient fine-tuning (PEFT) approach combining sensitivity-based layer selection with LoRA variants (rsLoRA, LoRA+, LoCon) reduces the number of modified parameters to improve secrecy and efficiency. Experiments on DDPM, EDM, and consistency models show state-of-the-art extraction fidelity, comparable generation quality to the original model, and substantially lower GPU cost than prior diffusion-model steganography methods.

## Strengths

- **One-step secret time-step hiding simultaneously improves extraction fidelity, secrecy, and efficiency.** Unlike prior methods that require multi-step guided reverse processes, extraction is a single forward pass at a chosen time step. Results show PSNR 36.81 dB for 32×32 secret images (Table 1, vs. next best 30.52 dB) and GPU hours of 0.6 vs. 18.6 for the fastest competitor (Table 2), demonstrating concrete gains on all three axes.

- **Hybrid PEFT demonstrably improves secrecy by modifying fewer parameters.** Table 6 directly compares the proposed PEFT against full fine-tuning: PEFT achieves better secrecy (FID 4.13 vs. 6.53, PSNR 31.28 vs. 29.11) while maintaining fidelity, confirming that limiting parameter changes reduces detectability through output-based metrics.

- **Generalization across diffusion model families and support for multi-image hiding.** The method is validated on DDPM, EDM, and consistency models (Table 7), and Section 3.3.1 extends it to hiding multiple images for different recipients (Tables 4–5). This breadth is not demonstrated by prior diffusion-model steganography methods, which are typically restricted to latent diffusion models.

- **Distillation-based secrecy loss is computationally efficient.** Rather than co-training a full diffusion denoising process as regularization, the secrecy loss distills the pre-trained score function's output (Eq. 8), which directly contributes to the large efficiency gains (0.6–0.7 GPU hours vs. ≥18.6 for competitors in Tables 2–3).

## Weaknesses

### Fatal

None.

### Major

None. The core methodology is sound, the results are strong across multiple metrics and settings, and no flaw invalidates the central claims.

### Minor

- **Critical hyperparameters are missing, impairing reproducibility.** The paper introduces λ (fidelity–secrecy trade-off, Eq. 9), γ (parameter sparsity), δ (layer sparsity), M (sensitivity accumulation iterations), LoRA rank, optimizer, learning rate, and number of training iterations — none of these are reported with concrete values. While these are easy to add and do not challenge the core claims, they make the method irreproducible as published.

- **No cross-extraction testing is provided for the multi-image scenario.** The paper claims that "without additional secret keys, the i-th recipient is unable to extract other secret images" (Section 3.3.1), but provides no experimental verification (e.g., attempting extraction of all C images using each key). This is not a fatal flaw — the claim is plausible — but it is an unsubstantiated security claim that requires evidence.

- **No analysis of the secret key's resistance to brute-force search.** The secret key consists of a fixed noise \(z_s\) and a secret time step \(t_s\) (1…T). The paper does not estimate the candidate key space or the cost of testing each candidate. An estimate showing the effective key space (or a proposal to strengthen it) would directly support the security claims.

- **No confidence intervals or variance reporting.** Quantitative results in Tables 1–7 are reported as point estimates without error bars or standard deviations. For sample-level metrics (PSNR, SSIM, LPIPS, DISTS) and FID, variability across secret images or random seeds matters for assessing reliability.

- **The secrecy threat model is narrower than the claim.** The paper evaluates secrecy exclusively through output-level metrics (FID, PSNR, SSIM, etc. on generated images), which matches the stated inspector scenario ("commonly used metrics"). However, the paper does not discuss whether a more sophisticated inspector analyzing weight statistics or parameter distributions could detect the stego model. A brief discussion of this limitation (rather than claiming unqualified "high secrecy") would improve the paper's rigor.

### Trivial

- No limitations section is included; the paper concludes abruptly after presenting results. Adding a brief discussion of limitations (e.g., applicability limited to pixel-space diffusion models, unvalidated weight-level detectability) would be appropriate.

- The paper does not discuss potential dual-use concerns of an image-hiding method that improves secrecy, which is standard practice for security-related contributions.

## Nice-to-Haves

- An ablation comparing the distillation-based secrecy loss (Eq. 8) against using the standard DDPM denoising objective as regularization would clarify whether the distillation formulation is critical for secrecy or merely an efficiency choice.

- A simple steganalysis experiment (e.g., comparing weight statistics between original and stego models) would strengthen the secrecy claim against a broader threat model, though this is beyond the paper's stated inspector scenario.

- Per-dataset breakdown of results for the mixed secret-image dataset (COCO, DIV2K, LSUN church, Places) would improve experimental clarity.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Comparison baselines conflate different steganography paradigms"** — This criticism misunderstands Table 1, which compares *extraction fidelity* (PSNR, SSIM, etc. between extracted and ground-truth images). This metric is directly comparable across paradigms. The paper also explicitly notes (in the Secrecy subsection) why image steganography methods are not in the secrecy tables, showing careful task separation.

- **"Insufficient evidence for high secrecy (weight-level detection)"** — The reviewer demands weight-statistics steganalysis that the paper's stated threat model does not require. The paper defines the inspector as using "commonly used metrics" (i.e., generation quality metrics), and the secrecy evaluation follows this model. Requesting a different threat model is scope creep; this is at most a limitation worth mentioning (which I have noted in Minor).

- **"Missing ablation on λ"** — The reviewer mentions missing λ ablation. The paper does not report the λ value, which is a genuine reproducibility issue (covered above), but requesting a full ablation sweep of a single trade-off parameter is a wishlist item. The missing value, not the missing ablation, is the real problem.

- **"The paper should also cover ethical considerations"** — This is standard practice for security papers but is not a weakness in the technical contribution. Moved to Nice-to-Haves/Trivial.

## Novel Insights

The reviews surface one observation not fully articulated by the paper itself: the distillation-based secrecy loss (Eq. 8) can be viewed as a form of *score function regularization* that is computationally cheaper than standard diffusion training because it avoids sampling the full denoising trajectory. The reviewers do not produce a genuinely novel insight beyond the paper's own contributions, but this reframing highlights why the efficiency gains are structural rather than merely implementation-level.

## Suggestions

1. **Report all missing hyperparameters** in a reproducibility table: λ, γ, δ, M, LoRA rank, optimizer, learning rate, batch size, and number of training iterations.
2. **Add a cross-extraction experiment** for the multi-image scenario: attempt to extract each secret image using every other recipient's key, reporting success/failure metrics.
3. **Provide a key-space analysis**: estimate the number of candidate keys (time steps × noise seeds) and the computational cost of testing each candidate. If the space is small, propose a strengthening mechanism.
4. **Add confidence intervals or standard deviations** to all quantitative tables, especially for sample-level metrics.
5. **Add a limitations paragraph** acknowledging that secrecy is validated against output-based metrics and that weight-level detectability is not evaluated.
6. **Include a brief discussion of ethical considerations** and potential dual-use concerns.

## Score and Decision

This is a solid method paper with a clear contribution, strong empirical results across fidelity, secrecy, and efficiency, and generalization across diffusion model families. The weaknesses are primarily about missing experimental details and unvalidated security sub-claims rather than methodological flaws. The paper would benefit from the suggested additions but does not require them for the core contribution to be valid.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>