Now I have all the calibration data. Let me write the consolidated review.

**My calibration analysis:**

**Round 1 (Bracketing):**
- Weak anchors (<3.5): Scores 2.5-3.0 — quantization papers with weaker contributions. VQ-Transplant is clearly stronger.
- Middle anchors (3.5-7.5): Scores 4.60-7.33 — includes Transformer-VQ (7.33), ImageFolder (6.25), BSQ-ViT (5.75), LL-VQ-VAE (4.75), VQMoE (4.60). VQ-Transplant sits in this band.
- Strong anchors (>7.5): Scores 7.60-8.00 — Restructuring VQ (8.0), CBQ (7.60). These have cleaner, deeper contributions. VQ-Transplant is weaker.

**Initial bracket: 5.0–6.5**

**Round 2 (Narrowing):**
- BSQ-ViT (5.75, accepted): Similar tokenization topic, also had fair-comparison concerns. VQ-Transplant has broader scope (multi-VQ, cross-dataset) but weaker theoretical depth. Comparable quality.
- ImageFolder (6.25, accepted): Tokenizer paper, well-received. VQ-Transplant is slightly below — the efficiency overclaim and codebook confound are more significant issues.
- "From Pixels to Tokens" (6.00, accepted): Visual tokenization. Similar quality level.
- PETL study (4.75, rejected): Empirical study, less novel. VQ-Transplant is stronger.
- Gray-Box Fine-Tuning (5.50, rejected): Framework paper. VQ-Transplant has broader experiments but similar structural issues.

**Final score: 6.0** — The paper has a genuine framework contribution, solid experimental breadth, and the issues are about claim precision rather than fundamental validity. Comparable to BSQ-ViT (5.75) and "From Pixels to Tokens" (6.00), both accepted.

---

## Summary

This paper proposes VQ-Transplant, a two-stage framework for plug-and-play replacement of Vector Quantization (VQ) modules in pre-trained visual tokenizers without costly full retraining. Stage I substitutes the native VQ module while freezing the encoder-decoder, and Stage II performs a lightweight decoder adaptation (5 epochs) to resolve decoder-quantization mismatch. The paper also introduces MMD-VQ, a quantization method using maximum mean discrepancy for distributional alignment. Experiments on the VAR tokenizer with five VQ algorithms (Vanilla, EMA, Online, Wasserstein, MMD) across ImageNet-1k and three out-of-distribution datasets (FFHQ, CelebA-HQ, LSUN-Churches) demonstrate that VQ-Transplant achieves reconstruction quality competitive with industry-level fully-trained tokenizers at substantially lower training cost.

## Strengths

- **VQ-Transplant framework is well-motivated and the two-stage design is convincingly validated.** The paper formalizes a genuinely useful idea — decoupling VQ module development from end-to-end tokenizer training — and empirically validates that the two-stage process (substitution followed by decoder adaptation) resolves the distribution mismatch. Table 3 provides clean evidence: after substitution alone, r-FID is 1.49–1.52 (blurring visible in Figure 2), and after 5 epochs of decoder adaptation, r-FID drops to 0.81–0.91.

- **Broad and systematic experimental evaluation.** The framework is tested with five distinct VQ algorithms across both multi-scale and fixed-scale configurations, spanning codebook sizes from 4K to 65K. This breadth convincingly shows that VQ-Transplant is not tied to a specific quantizer — distributional-alignment methods (Wasserstein, MMD) work well, but even conventional methods (EMA, Online) benefit substantially from the pipeline.

- **Cross-dataset generalization is demonstrated across structurally diverse domains.** Tables 8–10 show that VQ-Transplant generalizes to FFHQ (r-FID 1.21), CelebA-HQ (r-FID 2.60), and LSUN-Churches (r-FID 1.79) — datasets far from the OpenImages/ImageNet training distribution of the underlying VAR encoder-decoder. These results significantly strengthen the case that the framework is practical rather than narrowly overfitted.

- **Extended adaptation yields diminishing-but-real improvement.** Table 5 shows r-FID improving from 0.81 at 5 epochs to 0.74 at 20 epochs for K=8192, confirming the framework can trade a modest amount of additional compute for further gains without requiring a full retraining pipeline.

## Weaknesses

### Fatal
None.

### Major

- **The headline efficiency numbers (21.8× speedup, 95% cost reduction) compare incomparable setups.** Table 1 computes speedup as GPU-hours of other methods divided by VQ-Transplant's GPU-hours, but the compared methods differ simultaneously in dataset (OpenImages vs. ImageNet-1k), hardware budget (16×A100 vs. 2×A100), and training protocol (full training from scratch vs. lightweight adaptation). The "21.8×" conflates all three factors. Table 6 provides a more controlled comparison on ImageNet-1k showing VQ-Transplant beats from-scratch training at similar compute budgets, but the from-scratch baselines are run for only 5–7 epochs (which the paper itself notes is far from convergence for discrete tokenizers). The core efficiency claim is directionally correct, but the specific headline numbers are not properly qualified in the abstract and introduction. The authors should reframe these as rough estimates rather than precise measurements, or provide a directly controlled comparison on the same dataset and hardware.

- **The reconstruction improvement over the original VAR tokenizer is partly attributable to a larger codebook, not solely to the VQ-Transplant framework or MMD-VQ.** MMD VAR at codebook size K=4096 achieves r-FID 0.91 — essentially tied with the original VAR's 0.92. The headline result of 0.81 r-FID uses K=8192, which is double the original codebook capacity. This confound is not acknowledged in the paper's narrative; the improvement is presented as a success of the framework without noting that the comparison is unequal on codebook size. The paper would be strengthened by either (a) clearly separating the effect of codebook size from the effect of VQ method, or (b) reframing the contribution as "VQ-Transplant enables matching or exceeding the original tokenizer's performance when given equal or larger codebooks, at a fraction of the training cost."

### Minor

- **MMD-VQ's advantage over Wasserstein VQ (Fang et al., 2025) is not empirically substantiated.** Across all comparisons (Tables 3, 7, 8–10), MMD-VQ and Wasserstein VQ perform nearly identically — differences in r-FID are typically 0.02–0.06 (e.g., 0.91 vs. 0.93 at K=4096, 0.81 vs. 0.83 at K=8192). On FFHQ, Wasserstein VQ actually achieves better r-FID (1.21 vs. 1.37). No confidence intervals or multiple-seed experiments are reported, so the reader cannot assess whether these differences are meaningful. The paper argues MMD-VQ avoids Gaussian assumptions, but never empirically demonstrates a setting where non-Gaussian features cause Wasserstein VQ to fail. MMD-VQ is presented as a secondary contribution, and the claims about its advantages should be tempered or supported with targeted experiments on non-Gaussian distributions.

- **The paper lacks a baseline that unfreezes the encoder during decoder adaptation.** The claim that freezing the encoder is beneficial (vs. merely doing a short finetune of any kind) would be strengthened by comparing against a simple alternative: unfreezing the encoder and jointly finetuning all components for the same 5 epochs. The paper mentions joint optimization in Appendix C, but the main text should include this comparison explicitly to justify the claim that the decoupling (rather than just short finetuning) drives the efficiency gain.

### Trivial
- The title of Table 1 says "Speedup" but the column actually computes GPU-hours ratio relative to VQ-Transplant across different datasets and hardware, which conflates multiple factors. A clearer label would be "GPU-Hour Ratio" or "Estimated Relative Cost."

## Nice-to-Haves

- **Comparison where the original VQ module is retained and only the decoder is finetuned for 5 epochs.** This would isolate whether the gain from decoder adaptation is specific to the new VQ module or is simply a result of additional decoder training.
- **Statistical significance or confidence intervals** for the main results, especially for the MMD vs. Wasserstein comparisons.

## Removed Points

- **Weakness about Stage II using adversarial training undermining the motivation.** The paper's stated motivation is avoiding "costly end-to-end retraining" (lines 19, 33, 53, 64), not avoiding adversarial training per se. The decoder adaptation is lightweight (5 epochs, 22 hours on 2 A100s), which is consistent with the claimed efficiency. The paper correctly positions this as a short finetune, not as an adversarial-training-free method. **Removed** because it misreads the paper's scope.

- **Weakness about from-scratch comparison using only 5-7 epochs being insufficient.** The paper explicitly acknowledges this limitation (lines 270-271: "This outcome is expected, as discrete tokenizers typically require hundreds of epochs to achieve high-quality visual reconstruction when trained from scratch"). The comparison is intentionally asymmetric to show that VQ-Transplant leverages pre-trained weights. **Merged** into the major weakness about the efficiency comparison — the core issue is qualification of claims, not the experimental design itself.

- **Strength Finder's first strength (21.8× speedup and surpasses reconstruction fidelity)** — This conflates two separate achievements. The speedup number is imprecise (see Weaknesses), and the reconstruction improvement is confounded by codebook size. **Moved here** to avoid presenting an overclaimed strength in the final review. The actual supporting evidence for VQ-Transplant's value is presented in other strengths above.

## Novel Insights

None beyond the paper's own contributions. The reviews raise valid concerns about comparison fairness and claim precision but do not surface a structural flaw that invalidates the core framework idea, nor do they identify an overlooked connection to an existing method or theory.

## Suggestions

1. **Qualify the efficiency claims precisely.** Reframe "21.8× faster" and "95% cost reduction" as rough estimates based on a comparison across different training setups, and clearly separate the effects of dataset, hardware, and training protocol. Add a controlled experiment training VAR from scratch on ImageNet-1k for the same total GPU-hour budget as VQ-Transplant and report the resulting r-FID.
2. **Disentangle codebook size from VQ method improvement.** Present the K=4096 comparison as the proper apple-to-apple benchmark, and frame the K=8192 result as an additional benefit of the framework's ability to accommodate larger codebooks without full retraining.
3. **Either strengthen or downplay MMD-VQ.** Run experiments on datasets or synthetic distributions with known non-Gaussian structure to demonstrate MMD-VQ's theoretical advantage over Wasserstein VQ, or present MMD-VQ as a straightforward alternative rather than a superior method.
4. **Add a simple ablation** unfreezing the encoder during Stage II to validate that the decoupling (rather than just short finetuning) drives the efficiency benefit.
5. **Report variability** (multiple seeds or confidence intervals) for the central comparisons, especially MMD vs. Wasserstein.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison to VQ-Transplant |
|------|-----------|-------|------------------------------|
| BSQ-ViT (yGnsH3gQ6U) | 5.75 | R2 | Similar quality — both have a solid contribution and fair-comparison concerns. Accepted. |
| ImageFolder (QE1LFzXQPL) | 6.25 | R2 | Slightly stronger — cleaner evaluation with fewer claim-precision issues. Accepted. |
| From Pixels to Tokens (3TnLGGHhNx) | 6.00 | R2 | Comparable quality — both have broad experiments and genuine contributions. Accepted. |
| LL-VQ-VAE (sfTsvy05MX) | 4.75 | R1 | Weaker — narrower evaluation, missing generative modeling validation. Rejected. |
| VQMoE (RVPZJpmyGU) | 4.60 | R1 | Weaker — unclear method and insufficient experimental scale. Rejected. |
| Transformer-VQ (oDdzXQzP2F) | 7.33 | R1 | Stronger — clean theoretical contribution with convincing experiments. Accepted. |
| Restructuring VQ (GMwRl2e9Y1) | 8.00 | R1 | Stronger — principled method with extensive 11-setting validation. Accepted. |
| Gray-Box FT (j7oTk2nEoN) | 5.50 | R2 | Similar structural issues but narrower contribution. Rejected. |
| PETL study (Fb93MfxX7T) | 4.75 | R2 | Weaker — empirical study without novel method. Rejected. |

**Round 1 bracket:** The paper sits clearly above weak anchors (2.5–3.0) and below the strongest anchors (7.6–8.0), placing it in the 4.0–7.5 range.

**Round 2 narrowing:** Compared to BSQ-ViT (5.75) and ImageFolder (6.25) — both accepted and topically similar — VQ-Transplant has a genuinely useful framework contribution and broader VQ-method coverage, but its claims are less precisely supported. It is slightly weaker than ImageFolder (6.25) due to the efficiency and codebook confounds, and comparable to BSQ-ViT (5.75) which had similar fair-comparison concerns in its own review.

**Final score:** 6.0. The core contribution is valid and well-evidenced across multiple VQ algorithms and datasets; the weaknesses are about claim precision and presentation, not fundamental validity.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>