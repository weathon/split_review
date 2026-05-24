Now I have a clear picture from all the anchors. Let me finalize my calibration:

- **Round 1 bracket**: This paper is clearly above the ≤3.5 band (weak reject papers) and clearly below the 8.0 band (the Rotation Trick, which is a cleaner, more principled contribution with no confounding issues). The paper sits in the middle band, somewhere around 5.5-7.0.

- **Round 2 narrowing**: The paper is comparable to ImageFolder (6.25) — a tokenizer paper with solid results but some concerns about comparisons. It's slightly below FSQ (6.50) — a simpler, cleaner contribution without confounding issues. It's clearly above BSQ-ViT (5.75) — VQ-Transplant has stronger cross-dataset results and more thorough VQ method comparisons.

My final score: **6.0**. The paper has a genuinely useful engineering contribution with extensive experiments, but the headline speedup claim is confounded and the MMD-VQ novelty is incremental. This lands between the 5.75 and 6.25 anchors.

---

## Summary

VQ-Transplant proposes a framework for swapping vector quantization (VQ) modules in pre-trained visual tokenizers without retraining the entire encoder-decoder. The method operates in two stages: (1) substitute the VQ module and train it with a frozen encoder/decoder, and (2) adapt the decoder for ~5 epochs on ImageNet-1k to resolve quantization–decoder mismatch. The authors also introduce MMD-VQ, a distribution-aligned VQ method using maximum mean discrepancy. The framework is evaluated across five VQ algorithms in both multi-scale and fixed-scale configurations on a pre-trained VAR tokenizer, with additional cross-dataset experiments on FFHQ, CelebA-HQ, and LSUN-Churches.

## Strengths

- **Clever engineering contribution with practical value**: The core idea — decoupling VQ module development from expensive full retraining — is genuinely useful for resource-constrained VQ research. The framework is simple, well-motivated, and would enable rapid iteration on quantization methods, which is a real bottleneck in the field.

- **Extensive and systematic empirical evaluation**: The paper evaluates five distinct VQ algorithms (Vanilla, EMA, Online, Wasserstein, MMD) in both multi-scale (Section 5.1) and fixed-scale (Section 5.2) configurations, consistently showing that decoder adaptation improves reconstruction across all methods. The ablation on adaptation epochs (Tables 4–5, Figure 3) and the from-scratch comparison (Table 6) provide a thorough picture of the method's behavior.

- **Strong cross-dataset generalization**: Tables 8–10 demonstrate that VQ-Transplant with Wasserstein VQ and MMD VQ achieves state-of-the-art reconstruction r-FID on FFHQ (1.21), CelebA-HQ (2.60), and LSUN-Churches (1.79), outperforming prior tokenizers including VQGAN-LC and RQVAE. This is the paper's strongest empirical contribution, showing the framework generalizes beyond the VAR tokenizer's original training distribution.

- **Lightweight decoder adaptation is genuinely efficient**: The adaptation requires only 5 epochs (22 hours on 2×A100 GPUs), which is substantially cheaper than training a tokenizer from scratch. The progression from post-substitution r-FID (~1.5) to post-adaptation r-FID (~0.81) is well-documented and visually convincing (Figure 2).

## Weaknesses

### Major

- **Headline 21.8× speedup vs. VAR confounds dataset size with method efficiency**: Table 1 compares VAR trained on OpenImages (~9M images, 16×A100, 60 hours) against VQ-Transplant trained on ImageNet-1k (~1.2M images, 2×A100, 22 hours). The speedup factor therefore mixes genuine per-example efficiency gains with a ~7.5× reduction in dataset volume. The paper does acknowledge in Section 5.3 that ImageNet-1k is a subset of OpenImages, but this does not resolve the confounding in the headline metric. The from-scratch experiments in Table 6 only train MMD-VAR, not the original VAR method, so they do not serve as a controlled data-matched comparison for the original VAR baseline. The speedup claim relative to other ImageNet-1k-trained tokenizers in Table 1 (Llama GEN: 9.1×, ImageFolder: 29.1×) is more defensible but receives less emphasis. The paper should either (a) report training cost for the original VAR on ImageNet-1k, or (b) explicitly qualify the 21.8× figure as incorporating both dataset and method differences.

### Minor

- **MMD-VQ is an incremental extension of Wasserstein-VQ**: The core idea — replacing the 2-Wasserstein distance with MMD for distribution matching — is a straightforward substitution. The empirical gains over Wasserstein-VQ are modest: at K=4096 adaptation, MMD VAR achieves r-FID 0.91 vs. Wasserstein VAR's 0.93; at K=8192, 0.81 vs. 0.83 (Table 3). While consistent, these differences are within a range that could be affected by hyperparameter tuning, which is not controlled for.

- **"Plug-and-play" framing is overstated**: The decoder adaptation stage requires a specific adversarial training setup (DINO-S discriminator, DiffAug, consistency regularization, LeCAM regularization) on a specific dataset. This is not truly dataset-agnostic or zero-shot. To be fair, the paper does describe the adaptation setup explicitly, and 5 epochs is genuinely lightweight. But the abstract and introduction language could be more precise about what "plug-and-play" means in practice.

- **No downstream generation evaluation**: The paper evaluates only reconstruction metrics (r-FID, LPIPS, PSNR, SSIM, r-IS). While reconstruction is the standard evaluation for tokenizer papers, demonstrating that the transplanted tokenizer works in a generative pipeline (e.g., training an autoregressive model on the resulting tokens and reporting generation FID) would strengthen the practical relevance claim.

## Nice-to-Haves

- Report variance across runs (standard deviations or confidence intervals) for the main results, particularly where r-FID differences between methods are small.
- An ablation training the original VAR from scratch on ImageNet-1k to provide a clean data-matched cost comparison.
- A decoder-from-scratch baseline (random initialization rather than fine-tuning from the pre-trained decoder) to isolate how much the pre-trained weights matter for adaptation efficiency.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh critic claim: "The reconstruction evaluation is incomplete; downstream generation performance is never assessed" — characterized as a "significant evidential gap."** → Moved to Minor. While downstream generation evaluation would strengthen the paper, reconstruction quality is the standard and sufficient evaluation for tokenizer papers in this subfield. Most baselines in Table 2 (DQVAE, DiVAE, RQVAE, VQGAN variants) are also evaluated only on reconstruction. This is a nice-to-have, not a critical gap.

2. **Harsh critic claim: "Decoder adaptation undermines the plug-and-play narrative" — characterized as a "methodological gap."** → Kept but downgraded to Minor. The paper explicitly describes the adaptation setup and it is genuinely lightweight (5 epochs). The cross-dataset results partially address the dataset-dependence concern.

3. **Harsh critic claim: "No discussion of the data overlap issue."** → Removed. The paper explicitly discusses this in Section 5.3: "This limitation arises because the original VAR tokenizer was trained on OpenImages—where ImageNet-1k is a subset—raising a critical question: Can the framework generalize to datasets structurally distinct from both ImageNet-1k and OpenImages?"

4. **Harsh critic claim: "The paper omits a critical baseline: a variant where the decoder is adapted from scratch (random initialization)."** → Moved to Nice-to-Haves. While informative, this is an ablation that would strengthen but not fundamentally alter the paper's conclusions.

5. **Strength Finder: "Massive training cost reduction with superior reconstruction" with full endorsement of the 21.8× figure.** → Kept the strength but qualified it given the dataset-confounding issue noted in the Major weakness.

6. **Harsh critic claim: "No standard deviations or statistical testing."** → Moved to Nice-to-Haves. Common in this subfield; the r-FID differences between VQ-Transplant and baselines are large enough that statistical significance is not in serious question.

## Novel Insights

The paper's key insight — that a frozen pre-trained encoder combined with a lightweight decoder adaptation can support VQ module swapping — is genuinely novel. Prior work treats the VQ module and encoder-decoder as monolithic; the demonstration that distribution-aligned VQ methods (Wasserstein, MMD) achieve better compatibility during substitution is a useful empirical finding that could guide future VQ design. The observation that reduced quantization error does not directly translate to better reconstruction without decoder adaptation (Section 5.1) is well-documented and actionable.

## Suggestions

- **Rerun the VAR baseline on ImageNet-1k** or explicitly qualify the 21.8× figure. Even a rough estimate (e.g., scaling the OpenImages cost by the dataset size ratio) would help readers interpret the claim.
- **Include a small-scale generative evaluation**: train a lightweight autoregressive transformer on tokens from a transplanted tokenizer and report FID. This would directly address the most common criticism of tokenizer-only evaluations.
- **Discuss MMD kernel sensitivity**: the multi-Gaussian kernel has bandwidth hyperparameters; an ablation showing robustness would strengthen the MMD-VQ contribution.

---

## Score and Decision

**Round 1 bracket**: Between 5.5 and 7.0. Above the weak-reject tier (≤3.5) and below the strong-accept tier (≥8.0, e.g., "Rotation Trick" at 8.0).

**Anchor comparisons across rounds**:

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| TDzAqTqDHV (QCR) | 3.00 | R1 | Paper under review is substantially stronger — genuine contribution, extensive experiments |
| bEvI30Hb2W (LVM-NET) | 3.00 | R1 | Paper under review is substantially stronger |
| yGnsH3gQ6U (BSQ-ViT) | 5.75 | R1/R2 | Comparable tokenizer paper; paper under review has stronger cross-dataset results and more thorough VQ comparisons, but BSQ-ViT has a cleaner headline claim without dataset confounding |
| mb2ryuZ3wz (Variable tokens) | 5.75 | R1/R2 | Paper under review is comparable or slightly stronger in empirical thoroughness |
| 3TnLGGHhNx (BPE Visual) | 6.00 | R1 | Paper under review has stronger empirical results but both have novelty concerns |
| QE1LFzXQPL (ImageFolder) | 6.25 | R2 | Very comparable — both tokenizer papers with solid results and some concerns about missing comparisons |
| 8ishA3LxN8 (FSQ) | 6.50 | R2 | FSQ is a cleaner, simpler contribution without confounding issues; paper under review is slightly below |
| GMwRl2e9Y1 (Rotation Trick) | 8.00 | R1 | Paper under review is clearly below — Rotation Trick has a mathematically principled, genuinely novel contribution without confounding issues |

**Final score determination**: The paper sits between ImageFolder (6.25) and BSQ-ViT (5.75). It has stronger cross-dataset generalization than BSQ-ViT but a more significant confounding issue in its headline claim than ImageFolder. Settling at **6.0**, which reflects a solid paper with a useful contribution and extensive experiments, but with a headline claim that needs qualification and an incremental secondary contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>