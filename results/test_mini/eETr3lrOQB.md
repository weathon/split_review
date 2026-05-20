Now I have sufficient calibration anchors. Let me write the final consolidated review.

## Summary

The paper proposes VQ-Transplant, a framework for replacing the Vector Quantization (VQ) module in a pretrained visual tokenizer (specifically VAR) without retraining the encoder or decoder. The key idea is two-stage: (1) substitute the VQ module with a new one while freezing the encoder/decoder, then (2) perform lightweight decoder adaptation (5 epochs on ImageNet-1k) to realign the decoder's priors with the new quantized latent space. A secondary contribution is MMD-VQ, a quantization method using Maximum Mean Discrepancy for distribution alignment. Results show that VQ-Transplant with MMD-VAR achieves 0.81 r-FID (surpassing the original VAR's 0.92) at a fraction of the full training cost (44 GPU-hours vs 960).

## Strengths

- **Practical and well-motivated framework**: The core idea of decoupling VQ module development from full tokenizer retraining is simple, useful, and clearly articulated. The two-stage pipeline (substitution → adaptation) is clean and principled. The paper convincingly demonstrates the key insight that reduced quantization error does not automatically translate to better reconstruction—decoder adaptation is essential, and the paper empirically validates this across Tables 3 and 7.

- **Comprehensive empirical validation across multiple VQ methods and datasets**: Tables 3 and 7 demonstrate integration of five distinct VQ algorithms (Vanilla, EMA, Online, Wasserstein, MMD) under the VQ-Transplant framework, showing consistent improvements after decoder adaptation. Cross-dataset experiments (FFHQ, CelebA-HQ, LSUN-Churches) in Tables 8-10 further demonstrate generalization, with Wasserstein VQ achieving r-FID 1.21 on FFHQ, significantly outperforming from-scratch baselines like VQGAN-LC (3.81) and RQVAE (7.04).

- **Clear ablation and analysis**: Table 5 and Figure 3 show r-FID progression over 20 adaptation epochs (0.92 → 0.74 for K=8192), quantifying how continued adversarial training converts quantization error reductions into better reconstruction. Table 6 compares VQ-Transplant against from-scratch training of the same method for equivalent compute budgets (22-35 hours), showing that VQ-Transplant substantially outperforms (0.81 vs ~1.26-1.40 r-FID).

- **Transparent computational cost reporting**: Table 1 directly lists GPU configurations and training hours for all compared methods, allowing readers to compute total GPU-hours. The 21.8× speedup (44 vs 960 GPU-hours) is clearly derived from the table.

## Weaknesses

### Fatal
None.

### Major

- **MMD-VQ is empirically indistinguishable from Wasserstein VQ, weakening the secondary contribution**: The paper claims MMD-VQ as a novel contribution motivated by Wasserstein VQ's Gaussian assumptions, but across every experiment the two methods produce nearly identical results, often with overlapping metrics. In Table 3 (Adaptation, K=4096): MMD VAR 0.91 r-FID vs Wasserstein VAR 0.93 r-FID. In Table 7 (Adaptation, K=16384): MMD VQ 1.05 vs Wasserstein VQ 1.04. On FFHQ (Table 8), Wasserstein VQ outperforms MMD VQ (1.21 vs 1.37). No evidence is provided that feature distributions are non-Gaussian or that MMD provides a practical advantage over Wasserstein. The paper would be stronger by presenting VQ-Transplant as the sole contribution and treating MMD-VQ as a minor variant.

### Minor

- **Speedup framing assumes the pretrained backbone as a free asset without sufficient caveat**: The headline "reducing training cost by 95%" compares VQ-Transplant's incremental cost (22 hrs × 2 A100s = 44 GPU-hours) to VAR's full training cost (60 hrs × 16 A100s = 960 GPU-hours). This is valid given the paper's stated scope (working from a pretrained backbone), but the abstract and introduction do not explicitly state that the 960 GPU-hour cost of the backbone is excluded. The paper would benefit from a one-sentence clarification: "Assuming a pretrained VAR tokenizer is already available, VQ-Transplant requires only 44 additional GPU-hours."

- **Missing baseline: decoder fine-tuning without VQ replacement**: The paper does not include a control experiment where the original VAR's VQ module is kept but its decoder is fine-tuned (alone) for the same 5 epochs on ImageNet-1k. Such a baseline would isolate whether the improvement from 0.92 to 0.81 r-FID comes from the better VQ module or simply from additional decoder training on the target dataset. This is a missing isolation experiment.

- **No variance or statistical significance reporting**: All tables report single numbers without standard deviations or confidence intervals. Given that some comparisons are tight (e.g., 0.91 vs 0.93 r-FID, or MMD vs Wasserstein across tables), it is impossible to assess whether observed differences are meaningful or within measurement noise. This is especially important for the cross-dataset results where only selected configurations are reported.

- **Cross-dataset generalization comparisons are asymmetrical**: Tables 8-10 compare VQ-Transplant results (which leverage the OpenImages-pretrained VAR backbone + ImageNet adaptation) against baselines trained from scratch on each target dataset (FFHQ, etc.). The large margin (e.g., 1.21 vs 3.81 r-FID on FFHQ) is partly attributable to the broader pretraining data of the backbone. The paper acknowledges this implicitly ("the original VAR tokenizer was trained on OpenImages") but does not discuss how this asymmetry inflates the apparent margin.

### Trivial
None.

## Nice-to-Haves

- **Stage I without reconstruction loss**: The VQ module in Stage I is trained only on quantization error and uniqueness loss without any reconstruction signal. Including an approximate reconstruction loss (e.g., through the frozen decoder's output) could potentially reduce the adaptation burden. The paper could discuss this design choice.

- **Comparison of vanilla VAR from scratch at equivalent compute**: Table 6 compares MMD VAR from scratch vs VQ-Transplant; adding vanilla VAR (standard VQGAN training) from scratch for the same 22-35 hour budget would strengthen the "same-budget" comparison and control for method-specific effects.

## Removed Points

- **"Obviating the need for costly end-to-end retraining is overstated because decoder adaptation uses GAN loss"** — The paper explicitly states that adaptation follows the same training recipe as Tian et al. (2024). The cost savings come from 5 epochs vs hundreds of epochs of full training. The framing is accurate given these orders-of-magnitude differences. REMOVED: not a genuine weakness.

- **"No reconstruction loss in Stage I might cause hard-to-fix deviations"** — The paper's own experiments (Tables 3, 5) show that even with this gap, decoder adaptation reliably closes it. This is a design choice, not a demonstrated problem. DEMOTED to nice-to-have.

- **"Missing hyperparameters for decoder adaptation"** — The paper references Tian et al. (2024) and Appendix A. The appendix is stripped by the parser. REMOVED: parser artifact.

- **"r-IS comparison is partial"** — Standard practice in the field; most baselines simply do not report this metric. REMOVED: not a weakness.

- **Strength Finder claim about MMD-VQ's lower quantization error** — While factually correct, this strength is in tension with the verified weakness (MMD-VQ indistinguishable from Wasserstein VQ). Both Wasserstein and MMD achieve similar quantization errors. The strength is retained but downgraded to reflect this nuance.

## Novel Insights

The reviews surface one insight not emphasized in the paper: the framework implicitly tests whether different VQ modules produce latents that are "compatible" with a fixed pretrained decoder. The observation that distributional-alignment methods (Wasserstein/MMD) succeed while codebook-collapse-prone methods (Vanilla VQ with <1% utilization) fail catastrophically even after adaptation (r-FID 5.02) suggests that the VQ-Transplant's adaptation phase has a boundary of recoverability. Characterizing this boundary—what signal-to-noise ratio in the quantized representation is necessary for decoder adaptation to succeed—would be a valuable extension.

## Suggestions

1. Add a control baseline: fine-tune the original VAR decoder without replacing the VQ module, for the same 5 epochs on ImageNet-1k. This directly isolates the benefit of the new VQ module.
2. Report standard deviations (or at minimum, show that key numbers are averaged over multiple runs) for close comparisons.
3. Add a sentence in the abstract/introduction clarifying: "Assuming a pretrained tokenizer is available, VQ-Transplant requires only 44 additional GPU-hours."
4. Reframe MMD-VQ as a minor variant rather than a co-equal contribution, or provide direct evidence (e.g., MMD between feature and codebook distributions during training) that MMD achieves better distribution alignment than Wasserstein VQ in practice.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/VK3p5dXYL6.md` | 3.00 | R1 (low) | Very different topic (continuous-discrete dualistic tokenization); paper under review is stronger |
| `/home/wg25r/review_agent/human_reviews_2026/609DXrfkoA.md` | 2.50 | R1 (low) | Different topic (latent binarization); less experimental grounding |
| `/home/wg25r/review_agent/human_reviews_2026/ajnBafpqmE.md` (AlignTok) | 4.50 | R1 (mid), R2 | Most similar in spirit (leveraging pretrained models); VQ-Transplant has stronger reconstruction (r-FID improves over baseline vs degrades) and more extensive experiments |
| `/home/wg25r/review_agent/human_reviews_2026/RYHzkIqHI4.md` (RobusTok) | 4.00 | R1 (mid) | Also about post-training tokenizers; VQ-Transplant is clearly stronger (cleaner framework, better results) |
| `/home/wg25r/review_agent/human_reviews_2026/juM14y0caI.md` (FVQ/VQBridge) | 6.00 | R1 (mid), R2 | Cleaner core contribution (VQBridge projector); stronger empirical results (rFID 0.88, 100% utilization at 262k); VQ-Transplant is slightly weaker due to marginal MMD-VQ |
| `/home/wg25r/review_agent/human_reviews_2026/QteJJF57yG.md` (WeTok) | 5.00 | R2 | Stronger absolute numbers (rFID 0.12) but more novelty concerns; VQ-Transplant has a more conceptual contribution; comparable overall |
| `/home/wg25r/review_agent/human_reviews_2026/1jBsi98fVe.md` (l-DeTok) | 6.50 | R2 | Cleaner principled idea, more comprehensive; VQ-Transplant is weaker |
| `/home/wg25r/review_agent/human_reviews_2026/BpgCOFefcE.md` (DualToken) | 5.00 | R2 | Different focus (understanding+generation unification); comparable quality of contribution |

**Round 1 bracket**: 4.0–7.0 (between the weakest mid-band anchor at 4.0 and the strongest at 6.5)

**Round 2 narrowing**: The paper sits between WeTok (5.0) and FVQ (6.0). It has a genuine practical contribution (VQ-Transplant) that is well-executed, but the secondary MMD-VQ contribution is weak and some evaluation choices (no variance, asymmetric cross-dataset comparisons, missing control baseline) hold it back from the 6+ range. It is clearly above AlignTok (4.5) and RobusTok (4.0).

**Final score**: 5.5 — The core VQ-Transplant idea is practical, timely, and well-supported. The paper would benefit from a sharper contribution claim (dropping or significantly toning down MMD-VQ) and a few missing baselines, but the main thesis is sound and the experiments are extensive enough to support it.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>