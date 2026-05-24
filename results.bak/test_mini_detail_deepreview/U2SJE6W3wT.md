Now I have enough calibration data. Let me write the final review.

## Summary

This paper proposes AdcVSR, a method for compressing large 3D DiT-based video super-resolution models via an improved Adversarial Diffusion Compression (ADC) approach. The key ideas are: (1) a "2D+1D" architecture that augments a pruned 2D Stable Diffusion backbone with lightweight 1D temporal convolutions, replacing heavy 3D spatio-temporal attention; and (2) a dual-head, dual-discriminator adversarial distillation scheme that disentangles detail richness and temporal consistency into separate objective heads. Experiments show a 95% parameter reduction and 8× speedup over the DOVE teacher while maintaining competitive video quality, with particularly strong temporal consistency measured by warping error.

---

## Strengths

- **Validated "2D+1D" architectural hypothesis** (Table 2, Figure 5): The paper directly compares a pruned 3D DiT, a pure 2D backbone (AdcSR), and the proposed 2D+1D design. The 2D+1D model achieves the lowest warping error (1.67) and nearly matches the 3D teacher's DISTS (0.2112 vs. 0.2098) while using only 0.55B parameters — 7% of the 3D model's 8.36B. This concretely demonstrates that a 2D backbone with lightweight 1D convolutions can learn spatio-temporal mappings from a heavy 3D teacher.

- **Evidence that dual-head, dual-discriminator scheme resolves the detail-consistency conflict** (Table 3): On YouHQ40, single-head dual-domain gives CLIPIQA 0.6745 / warping error 6.32; dual-head single-domain gives 0.6421 / 3.59. The proposed dual-head dual-domain achieves 0.6861 / 2.22 — the best on both axes. This quantitative ablation is clean evidence that disentangling the two objectives into separate heads with dual-domain supervision is effective.

- **Massive compression with competitive quality** (Table 1, Figure 4): AdcVSR reduces parameters by 95% (10.55B → 0.57B) and achieves 8× speedup (4.42s → 0.55s for 25-frame 512×512 video) over its teacher DOVE, while ranking top-three in most quality metrics and achieving the best warping error on the real-world VideoLQ dataset (6.74). The efficiency gain is substantial and practically meaningful.

- **Systematic adversarial data curation** (Eqs. 4–5, Section 3.3): The five-type data curriculum with head-specific labels (shuffled videos → "fake" for consistency, static images → "real" for both heads) is a principled design that goes beyond standard adversarial training. The ablation in Table 4 confirms that both the teacher and the adversarial distillation are necessary for perceptual quality.

- **Comprehensive evaluation**: Six test datasets (three synthetic, three real-world), eight metrics covering fidelity, perceptual quality, and temporal consistency, plus qualitative temporal profiles in Figure 3. The ablations in Tables 2–4 systematically isolate each design choice.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Warping error improvement over the teacher is under-explained**: AdcVSR achieves lower warping error (1.67) than its teacher DOVE (2.22) on UDM10, and also beats DOVE on VideoLQ (6.74 vs. 8.41). The paper attributes this to the dual-head adversarial scheme, but the L₁ distillation losses still push the student toward the teacher's outputs, which could partially counteract the adversarial signal. A more detailed discussion of how the adversarial and distillation losses interact to enable improvement beyond the teacher — rather than just mimicking it — would strengthen the claims. The temporal profiles in Figure 3 provide visual support, but the mechanism deserves explicit analysis.

- **Missing analysis of discriminator disentanglement**: The paper introduces a sophisticated dual-head discriminator with five data types and head-specific labels, but does not verify whether the two heads actually learn the intended disentanglement. For instance, does the "detail" head correctly ignore temporal information? Do the two heads' feature representations separate along detail vs. consistency axes? Training curves, per-head accuracy on each data type, or feature visualizations would increase confidence that the scheme works as designed rather than being a conceptual artifact.

- **No limitations section**: The paper ends without discussing limitations. Important aspects to mention include: dependence on a specific teacher (DOVE) and backbone (AdcSR), the complexity of the discriminator training pipeline (five data types, two heads, two domains), and potential failure cases (e.g., large motion or fast camera panning where the lightweight 1D convolutions may be insufficient).

- **No error bars or statistical significance**: Quantitative results in Table 1 are reported as single values without standard deviations or confidence intervals. For some metrics where differences between top methods are small, error bars over multiple seeds or test splits would increase confidence.

- **Fixed number of 1D temporal convolutions not ablated**: The paper inserts one 1D temporal residual block after each UNet block but does not ablate this choice. A sweep over the number/placement of 1D convolutions would quantify how much temporal capacity is needed and support the "lightweight" claim more precisely.

### Trivial

- None.

---

## Nice-to-Haves

- An inference time breakdown (UNet vs. VAE decoder vs. other components) would improve reproducibility.
- Evaluating on a high-motion benchmark (e.g., REDS or DAVIS clips) would stress-test the temporal consistency mechanism.
- The paper could quantify the detail-consistency trade-off trajectory during training by plotting warping error vs. perceptual quality at multiple checkpoints, showing that the dual-head scheme navigates the trade-off surface better than alternatives.

---

## Removed Points

**Kept for reference (not part of the assessment):**
- "Comparison with DOVE's own compression via simple pruning without distillation" — The paper's Table 4 already covers "No Teacher" and "No Adversarial Loss" baselines that serve a similar purpose. This is a reasonable suggestion but does not constitute a weakness of the paper as written.
- "The detail head receives no gradient from real videos (y_d=0 → Softplus(0) = log 2)" — This is an accurate mathematical observation about the design, but the paper explicitly describes this as intentional ("leave real video details unlabeled, and rely on real images as positive supervision"). It is a design trade-off, not an oversight.
- "E_warp* may be susceptible to static/blurry outputs" — The paper already addresses this concern by reporting multiple complementary metrics (PSNR, SSIM, LPIPS, DISTS, MANIQA, CLIPIQA, MUSIQ, DOVER) and providing temporal profile visualizations in Figure 3. The concern is reasonable but the paper's mitigation is adequate.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not reveal a perspective on the work that the authors' own analysis misses.

---

## Suggestions

1. Add a brief analysis (possibly in an appendix) of the dual-head discriminators' behavior: per-head prediction distributions on the five data types, or a t-SNE visualization of the two heads' features. This would directly address the most significant analytical gap.
2. Discuss the interaction between the L₁ distillation loss and the adversarial loss in Section 3.3, clarifying how the student can outperform the teacher on warping error despite being pushed to mimic it.
3. Add a limitations paragraph to the conclusion covering teacher/backbone dependence and potential failure modes under large motion.
4. Include standard deviations in Table 1 for key metrics where differences are small.

---

## Score and Decision

**Calibration Summary:**

**Round 1 — Bracketing**: Queried for papers on "video super-resolution diffusion model compression adversarial distillation" in three bands:
- Low band (&lt;3.5): Papers at 2.50–3.20 (e.g., VideoDiT, self-distillation for diffusion). The paper under review is clearly much stronger — it has a concrete method, thorough experiments, and well-supported claims.
- Middle band (3.5–7.5): AddSR (5.00), Dissecting Arbitrary-scale SR (5.25), DFOSD (4.75), Solving Video Inverse Problems (6.50). 
- High band (&gt;7.5): Binarization for SR (8.00), Universal Quantized Diffusion (8.00), NoiseDiffusion (8.00), Learning to Discretize (8.00) — mostly on different topics with strong theory.

**Initial bracket:** 5.5–7.5.

**Round 2 — Narrowing**: Focused on 4.5–8.0 with more targeted queries. Key anchors read in full:
- **AddSR (5.00)**: Adversarial diffusion distillation for image SR. Had significant weaknesses: fidelity drop, missing baselines, unclear novelty. The current paper has stronger experiments, a more novel architecture, and more thorough ablations. **This paper is clearly stronger.**
- **DFOSD (4.75)**: Distillation-free one-step diffusion for image SR. Concerns about limited novelty (marginal optimization). The current paper has a genuinely novel contribution (2D+1D architecture, dual-head dual-discriminator scheme). **This paper is clearly stronger.**
- **Does Diffusion Beat GAN in ISR (5.75)**: Empirical comparison study. Had concerns about actionable insights and proprietary data. The current paper has a concrete method with clear practical value. **This paper is stronger.**
- **Solving Video Inverse Problems (6.50, accepted)**: Video inverse problems using image diffusion models. Had concerns about missing real-world degradations and limited dataset diversity. The current paper tests on 6 datasets with both synthetic and real-world degradations and has more thorough ablations. **This paper is slightly stronger.**
- **Infinite-Resolution Integral Noise Warping (6.25, accepted)**: Theory-heavy noise warping method. Mixed reviews — one reviewer rated it 3 due to low practical quality. The current paper has stronger experimental validation. **Comparable quality of contribution.**

The paper sits above the 5.0–5.75 image SR papers and is comparable to slightly stronger than the 6.25–6.50 video-related papers. It does not reach the 7.5+ level of the top anchors (theoretical rigor or breakthrough novelty).

**Final score: 6.5** — a solid paper with a clear, well-validated contribution and only minor analytical gaps.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>