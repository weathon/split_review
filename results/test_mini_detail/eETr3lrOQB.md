Now I'll write the final consolidated review.

## Summary

This paper proposes VQ-Transplant, a framework that enables swapping the VQ module in a pre-trained visual tokenizer (such as VAR) without costly end-to-end retraining, by (1) substituting the VQ module while freezing the encoder and decoder, and (2) performing lightweight decoder adaptation (5 epochs) to resolve the quantizer-decoder mismatch. The paper also introduces MMD-VQ, a distribution-aligned quantization method using maximum mean discrepancy. The framework is evaluated across multi-scale and fixed-scale VQ algorithms on ImageNet-1k and three cross-domain datasets (FFHQ, CelebA-HQ, LSUN-Churches), demonstrating both efficiency gains and competitive reconstruction fidelity.

## Strengths

1. **Practical and well-motivated framework.** The core idea of decoupling VQ module development from full tokenizer retraining is genuinely useful. The two-stage design (substitution + lightweight decoder adaptation) is simple and clearly explained. This could enable faster iteration in VQ research for groups with limited compute.

2. **Strong cross-dataset generalization evidence.** Tables 8–10 show that Wasserstein VQ and MMD VQ implemented via VQ-Transplant achieve state-of-the-art r-FID on FFHQ (1.21 vs. best baseline VQGAN-LC's 3.81), CelebA-HQ (2.60), and LSUN-Churches (1.79). Critically, these comparisons are with baselines trained from scratch on the *same* datasets, so they are not subject to the dataset confound that affects the ImageNet-1k comparison. This is the strongest evidence that the framework can produce high-quality tokenizers for new domains with minimal data.

3. **Comprehensive ablation of VQ methods.** Tables 3 and 7 systematically evaluate five different VQ algorithms (Vanilla, EMA, Online, Wasserstein, MMD) in both multi-scale and fixed-scale settings across two stages (substitution and adaptation). The consistent pattern that distribution-aligned methods (Wasserstein, MMD) outperform conventional ones, and that decoder adaptation reliably improves reconstruction, convincingly validates the framework's design choices.

4. **Decoder adaptation analysis over epochs.** Tables 4 and 5 track r-FID progression from 5 to 20 adaptation epochs, showing consistent improvement (MMD VAR K=8192: 0.81 → 0.74). This provides useful insight into the adaptation dynamics and suggests the 5-epoch default is a practical minimum rather than a hard limit.

## Weaknesses

### Major

1. **Confounded headline comparison with the original VAR tokenizer.** The central claim that MMD VAR achieves "superior reconstruction fidelity (0.81 rFID) while being 21.8× faster than training vanilla VAR (0.92 rFID)" is undermined by a training-distribution confound. The original VAR tokenizer was trained on **OpenImages** (~9M images), while VQ-Transplant's decoder adaptation is performed on **ImageNet-1k** (~1.2M images), which the paper itself notes "is a subset" of OpenImages (Section 5.3). Two concerns follow:

   - The adaptation amounts to fine-tuning on data the encoder and decoder have already seen during pre-training, which could explain part of the r-FID improvement without reflecting a fundamentally better VQ method.
   - The 21.8× speedup (960 GPU-hours vs. 44 GPU-hours) partly reflects the smaller dataset, not just the framework's algorithmic efficiency.

   The paper lacks a critical control experiment: **fine-tuning the original VAR decoder (with its native VQ module) on ImageNet-1k for the same 5-epoch budget**. Without this, the contribution of the VQ swap itself cannot be separated from the contribution of domain-specific decoder adaptation. This control would directly test whether replacing the VQ module adds value beyond simply adapting the existing decoder to ImageNet-1k.

2. **MMD-VQ is an incremental contribution over Wasserstein VQ.** The motivation for MMD-VQ is that Wasserstein VQ (Fang et al., 2025, from the same group) "critically relies on Gaussian distribution assumptions" (Section 2), but the paper provides **no empirical evidence** that the feature distributions deviate from Gaussianity or that MMD handles them better. The practical difference between MMD VAR and Wasserstein VAR is small in most results (e.g., r-FID 0.81 vs. 0.83 on ImageNet-1k K=8192 after adaptation), and Wasserstein VQ actually outperforms MMD VQ on some cross-dataset metrics (e.g., FFHQ adaptation r-FID: 1.21 vs. 1.37). The claimed advantage of MMD's non-parametric nature is asserted without supporting analysis of feature distributions or a case where Wasserstein VQ demonstrably fails due to non-Gaussianity.

### Minor

1. **Speedup claim conflates multiple factors.** While the practical speedup is real (using less compute is meaningful regardless of dataset size), Table 1 compares across different datasets (OpenImages vs. ImageNet-1k), different GPU counts (16 vs. 2), and different training paradigms (full end-to-end vs. decoder-only adaptation). A more informative metric would be GPU-hours normalized per image seen, or a direct comparison of VQ-Transplant against training from scratch on the **same dataset**.

2. **From-scratch comparison in Table 6 is not informative.** Showing that 5–7 epochs of from-scratch training (r-FID ~1.3) is worse than VQ-Transplant (r-FID 0.81) merely confirms that training from scratch needs many more epochs, which is already known. A meaningful comparison would either (a) train from scratch to convergence on ImageNet-1k and compare total compute, or (b) compare VQ-Transplant against decoder-only fine-tuning of the original VQ for the same budget, as noted above.

3. **Token count mismatch in Table 2 comparisons.** MMD VQ (fixed-scale) uses 512 tokens while VAR uses 680 tokens, and the baselines (VQGAN variants, RQVAE) use various token counts (256, 512, 1024). While the paper does not hide this information, the r-FID comparison across different token counts makes the superiority claims less straightforward than presented.

### Trivial

None.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Reproducibility concerns about missing hyperparameters (λ_P, λ_G, learning rates, etc.).** The paper states "We follow Tian et al. (2024)" for the discriminator setup and references the appendix for implementation details. Per the parser-stripping rule, appendix content is not available but exists in the original submission. The hyperparameters are standard in the VQGAN/VAR literature and can be inferred from the cited works.

- **Criticism that the comparison with from-scratch baselines in Table 2 is unfair because VQ-Transplant starts from a pre-trained model.** This critique misunderstands the paper's premise: the entire point of VQ-Transplant is that it *leverages* a pre-trained model to avoid costly retraining. Comparing against from-scratch training demonstrates the practical advantage of the approach. The valid concern (addressed above in Major weakness 1) is specifically about isolating the VQ-swap benefit from decoder adaptation on a different dataset.

- **Criticism that the motivation for MMD over Wasserstein VQ is "not empirically supported."** Tables 3 and 7 do provide empirical comparisons showing MMD VAR slightly outperforming Wasserstein VAR on ImageNet-1k. The gap is small but the paper does provide evidence. The issue is that the *theoretical* motivation (non-Gaussianity claim) is unsupported, which I retained as a Major weakness through a different framing.

- **Various formatting/style nitpicks and speculative claims about what "the appendix may contain."** Per the rules, these are removed.

- **Strength about "dramatic training cost reduction with performance improvement"** — this is the core claim that is weakened by the confound. I keep the factual observation but note it under the confounded comparison.

- **The harsh critic's suggestion that the LDM tokenizer results (Table 16) were "relegated to an appendix that is not available"** — the paper does mention it in the main text (Section 5.1) and references the appendix. The parser strips appendices, so this is an unavoidable artifact.

## Novel Insights

None beyond the paper's own contributions. The review surface is largely convergent: both the harsh critic and strength finder identify the same core evidence (Tables 1, 2, 3, cross-dataset results) and the same tension (the confounded VAR comparison). The most insightful observation not made fully explicit in the paper is that the cross-dataset results (FFHQ, CelebA-HQ, LSUN-Churches) are *structurally cleaner* evidence for the framework than the ImageNet-1k results, because there the VQ-Transplant models are compared against from-scratch baselines on the *same* target dataset, avoiding the confound. This inversion — where peripheral experiments are more rigorous than the primary one — points to a straightforward path to strengthen the paper.

## Suggestions

1. **Add the critical control experiment**: Fine-tune the original VAR decoder (with its native VQ module) on ImageNet-1k for 5 epochs, and report the resulting r-FID. This directly quantifies the benefit attributable to the VQ swap versus the benefit of simple domain-specific decoder adaptation. If the result is, say, 0.88 r-FID (worse than MMD VAR's 0.81), the claim is well-supported. If it's 0.82, then most of the gain comes from decoder adaptation, not the VQ swap.

2. **Normalize the speedup claim**: Report compute cost per training image (GPU-hours / number of training images) alongside the raw numbers, to disentangle dataset-size effects from algorithmic efficiency.

3. **Provide feature distribution analysis for MMD-VQ**: Show a t-SNE or PCA visualization comparing feature and codebook distributions, or a simple Gaussianity test (e.g., Mardia test), to substantiate the claim that features deviate from Gaussianity and that MMD handles this better than Wasserstein VQ.

4. **Clarify the token count in Table 2**: Add a note explaining that MMD VQ (fixed-scale) uses 512 tokens while VAR uses 680, and how this affects comparisons. This is already visible in the table but an explicit remark would improve transparency.

## Score and Decision

**Round 1 bracket (broad):** Between ~4 and ~7. The paper is clearly above weak papers scoring 2–3 (PQ-VAE, ELR-Diffusion, VideoDiT) but below breakthrough-level papers scoring 8+ (Rotation Trick VQ, REPA).

**Round 1 anchors used:**
- Weak band (<3.5): PQ-VAE (2.33), VideoDiT (2.50) — fundamentally flawed or incomplete
- Middle band (3.5–7.5): BSQ (6.0), Adaptive Length Tokenization (5.75), ImageFolder (6.25)
- Strong band (>7.5): Rotation Trick VQ (8.0), REPA (9.0)

**Round 2 narrow bracket:** Placed at ~4.5 to ~6.5 based on comparison with tokenization papers.

**Round 2 anchors used:**
- BSQ (6.0, Poster): Clean end-to-end tokenizer evaluation on same benchmarks. Stronger experimental rigor than VQ-Transplant.
- Adaptive Length Tokenization (5.75, Poster): Had evaluation concerns but solid contribution. Comparable significance, but VQ-Transplant has a more significant confound.
- ImageFolder (6.25, Poster): Mixed reviews (8,6,6,5). Cleaner evaluation than VQ-Transplant.
- Unified Lang-Vision Pretraining (6.25, avg): Also had evaluation concerns about fair comparison.

**Final positioning:** VQ-Transplant sits below cleanly-evaluated tokenization papers due to the confound in its headline comparison. The core idea is practically valuable and the cross-dataset results are strong, but the main claim requires a control experiment to be fully convincing. The paper would benefit from one additional experiment and a more careful framing of its efficiency claims. Current form is marginally below a clean acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>