## Summary

VQ-Transplant proposes a two-stage framework for integrating new Vector Quantization (VQ) modules into frozen, pre-trained visual tokenizers (specifically VAR) without end-to-end retraining. Stage I replaces the native VQ module with a new one while keeping the encoder and decoder frozen; Stage II applies a lightweight decoder adaptation (5 epochs on ImageNet-1k) using reconstruction, perceptual, and GAN losses to resolve the distribution mismatch. The paper also contributes MMD-VQ, a novel quantization method based on Maximum Mean Discrepancy for kernel-based, assumption-free distribution alignment between feature and codebook vectors. The claimed result is a 95% reduction in training cost (44 vs. 960 A100-hours) while achieving r-FID of 0.81—surpassing the original VAR tokenizer's r-FID of 0.92.

---

## Strengths

- **Practically significant efficiency gains.** The cost comparison in Table 1 is concrete and fair for the intended use-case: leveraging publicly available VAR weights and only paying the cost of Stage I + II (2×A100, 22 h total). The 95% savings claim (960 → 44 A100-hours vs. VAR from scratch) is well-documented and reproduced.

- **The from-scratch ablation (Table 6) is the strongest evidence.** Training MMD VAR from scratch for 25–35 h yields r-FID 1.26–1.40, whereas VQ-Transplant for the same MMD VAR achieves 0.81–0.91 in 22 h. This controlled comparison cleanly demonstrates that the pre-trained encoder/decoder parameters are the key source of quality, not just training time.

- **MMD-VQ is technically well-motivated.** The use of a multi-kernel MMD for codebook distribution alignment removes the Gaussian parametric assumption of Wasserstein VQ, enabling better coverage of non-Gaussian, multi-modal encoder feature distributions. 100% codebook utilization across all tested codebook sizes (Tables 3 and 7) supports the claim of improved codebook usage.

- **Cross-dataset experiments (Tables 8–10) demonstrate generalization.** Transplanting into FFHQ, CelebA-HQ, and LSUN-Churches without any dataset-specific retraining shows the decoder adaptation on ImageNet-1k is not overfit to that domain. r-FID of 1.21 on FFHQ is notably better than VQGAN-LC (3.81) and RQVAE (7.04).

- **Staged ablations support each design choice.** Tables 3–5 isolate the effect of Stage I alone (quantization error drops, but r-FID remains worse than baseline) vs. both stages (r-FID surpasses baseline), clearly establishing that decoder adaptation is essential and not mere fine-tuning theater.

---

## Weaknesses

### Fatal
None.

### Major

1. **Framework is validated on a single base architecture (VAR) only.** Despite being presented as a general "plug-and-play" framework for any pre-trained visual tokenizer, all main experiments use only the VAR tokenizer backbone. There is no evidence that the two-stage transplant procedure transfers to VQGAN, LlamaGEN, ImageFolder, UniTok, or any other architecture. The strength of the generalizability claim is therefore unsupported.

2. **No downstream generation evaluation.** Reconstruction metrics (r-FID, PSNR, SSIM, LPIPS) measure tokenizer quality in isolation, but the ultimate utility of a visual tokenizer is to enable strong generative models. No experiment tests whether substituting the transplanted VQ module into a downstream VAR-based or LLM-based image generator preserves or improves generation quality (FID, IS on generated images). Without this, it is unclear whether the reconstruction improvement translates to better generation—a critical gap for an ICLR audience focused on visual generation.

3. **The "lightweight" decoder adaptation claim is complicated by the extended-epoch analysis.** The abstract and headline claim "5 epochs," but Tables 4–5 show r-FID continuing to decline through 20 epochs (0.91→0.79 for K=4096; 0.81→0.74 for K=8192). The 5-epoch result is not a natural convergence point; it is a deliberately chosen early stopping. This undercuts the efficiency narrative and raises the question of what happens with further adaptation.

### Minor

1. **MMD kernel bandwidth hyperparameters (σ values) are not reported or ablated.** The choice of σ in the multi-Gaussian kernel directly determines what distributional differences MMD is sensitive to. Without ablation or sensitivity analysis, it is unclear whether the results would be robust to different feature spaces or architectures.

2. **Mixed outcomes of MMD-VQ vs. Wasserstein VQ across datasets (Tables 8–10) are not explained.** Wasserstein VQ wins on FFHQ (1.21 vs. MMD VQ not shown as best) and LSUN-Churches (1.79), while MMD VQ wins on CelebA-HQ. No analysis of why one method is preferred over the other in specific settings is provided.

3. **The 22-hour training budget is not broken down between Stage I and Stage II.** This makes it difficult to understand the relative cost of each stage and whether Stage I could be further accelerated.

### Trivial
- The abstract states "5 epochs" as the total training duration, but the paper body also reports 20-epoch experiments; these are not reconciled in the abstract.

---

## Nice-to-Haves

- Applying VQ-Transplant to at least one non-VAR base model (e.g., VQGAN or LlamaGEN) would substantially strengthen the generality claim.
- A downstream image generation experiment (e.g., VAR + transplanted tokenizer → image generation FID) would close the loop on practical utility.
- An analysis of computational overhead of the MMD loss during Stage I relative to vanilla VQ or Wasserstein VQ.

---

## Novel Insights

The most genuinely novel insight is that the encoder and decoder of a high-quality, adversarially trained visual tokenizer encode sufficient inductive bias that replacing only the VQ bottleneck—while keeping the full encoder-decoder frozen—is nearly impossible to recover from using only a few adaptation epochs due to distributional shift, yet just 5 epochs of decoder fine-tuning with an extremely lightweight discriminator (frozen DINO-S) is sufficient to bridge that gap and even surpass the original model. This suggests that the adversarial training in state-of-the-art tokenizers primarily shapes the encoder and decoder, not the codebook, and that the codebook is a relatively interchangeable component—a finding with meaningful implications for modular design in representation learning. The 100% codebook utilization of distribution-alignment methods across all codebook sizes further suggests that the prevalent "codebook collapse" problem in VQ may be fundamentally a distributional mismatch issue amenable to kernel-based solutions.

---

## Suggestions

- Report Stage I and Stage II training times separately and report r-FID vs. wall-clock time rather than vs. epoch count.
- Test VQ-Transplant on at least one other pre-trained tokenizer backbone to validate generality.
- Add an image generation FID experiment using a downstream model with the transplanted tokenizer.
- Report σ bandwidth values and add a brief ablation or sensitivity analysis for the MMD kernel.
- Discuss when Wasserstein VQ is preferred over MMD-VQ and vice versa across datasets.

---

## Score and Decision

The paper addresses a real and practical bottleneck in VQ research (cost of end-to-end retraining), proposes a clean two-stage solution, and demonstrates clear empirical gains over competitive baselines with honest ablations. The 95% cost reduction with improved r-FID is a meaningful contribution. The primary weaknesses—limited architectural diversity in experiments and absence of downstream generation evaluation—are significant but do not invalidate the core claims. The MMD-VQ contribution is technically sound and adds novelty beyond the framework alone.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>