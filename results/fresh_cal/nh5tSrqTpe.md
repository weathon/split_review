I now have a thorough understanding of the paper and verified the reviewer claims against the actual paper content. Here is the consolidated review.

---

## Summary

This paper proposes DPT (Don't Pre-train, Teach), a paradigm for training small models without pre-training them on a large foundation dataset. The method combines three components: (1) using an off-the-shelf pre-trained teacher model that is linearly probed on the downstream task, (2) a contrastive distillation loss based on the alignment/uniformity (A/U) framework of Wang & Isola (2020), and (3) augmenting the task dataset with synthetic images from Stable Diffusion. Experiments on 6 image recognition datasets with ResNet and ViT teachers (ResNet18/MobileNetV2 students) show that DPT achieves competitive accuracy with a pre-trained-and-linearly-probed student while claiming up to 94% reduction in student training time.

## Strengths

- **Empirical training-time savings are substantial and well-demonstrated**: Section 4.5 and Figure 5 show that DPT cuts student training time by up to 94% compared to pre-training + linear probing. The cost comparison is clearly presented, including the (acknowledged) additional cost of synthetic image generation. This is a concrete practical benefit.

- **Performance is competitive with the LP baseline across 6 datasets**: Table 3 shows DPT matches or exceeds a pre-trained-and-linearly-probed student on 4 of 6 datasets (MIT-67, CUB-2011, DTD, CIFAR-10) and comes within 1–2% on the remaining two (Caltech101, CIFAR-100). This provides real evidence that pre-training the student can be replaced under the right conditions.

- **The A/U loss is a clean adaptation with computational benefits**: Table 2 shows the A/U loss often outperforms CRD++ and KD across teacher–student pairings, while Section 4.3 correctly notes that it is cheaper than CRD++ because it requires no negative sample bank. The paper transparently credits Wang & Isola (2020) for the underlying theory.

- **Robustness to suboptimal teacher is a non-trivial finding**: Figure 4 demonstrates that even when a linearly-probed teacher performs worse on the downstream task than a from-scratch teacher, distilling from it still yields competitive student results. This increases the practical utility of the method.

## Weaknesses

### Fatal
None.

### Major

- **Headline claim is mismatched with the experimental baseline.** The abstract and introduction assert that DPT achieves "pretrain-then-finetune performance" (lines 4, 23) and "can hold its weight against, and often surpass, the pre-training regime" (line 4). However, Section 3.1 (line 85) redefines "finetuning" to mean *linear probing*, stating: *"To reflect modern practices, when we refer to finetuning, we imply the method of linear probing (LP) which freezes the backbone weights and only updates the task-specific head."* This is not standard usage — in practice, pre-trained models are almost always fine-tuned **end-to-end** on downstream tasks, which almost uniformly yields higher accuracy than linear probing. The paper's experimental comparison (Table 3) is only against LP, making the headline claim misleading. Adding a full end-to-end fine-tuning baseline is necessary to support the advertised conclusion. The core method may still be valuable (e.g., as a cheaper alternative to training from scratch or as a strong distillation approach), but the claims need recalibration. **This is the paper's most significant weakness and should be addressed before acceptance.**

### Minor

- **Cross-architecture results are deferred to the appendix.** The paper mentions "2 for other architecture pairings" (line 217) but only shows ResNet50→MobileNetV2 results in the main text (Tables 2 and 3). For a paper claiming cross-architecture generality (ViT→CNN, etc.), at least one cross-architecture result should appear in the main paper so readers can evaluate the claim without accessing supplementary material.

- **Limited analysis of when synthetic data helps vs. hurts.** Table 3 reports that synthetic data helps on some datasets (MIT-67, DTD) but the paper does not analyze why or provide a selection mechanism. The paper acknowledges that "on CUB-2011... synthetic data might hurt" (implied by the needing-to-augment vs. not-needing pattern) but offers no discussion of data quality, class-wise effects, or distribution similarity. An analysis of synthetic data quality (e.g., FID scores, visual inspection, amount sweeps) would strengthen the contribution.

- **No isolation of KD's contribution from synthetic data's contribution.** The paper uses synthetic images within the KD pipeline but does not compare against a simple supervised baseline trained on the same synthetic images without KD. This makes it hard to attribute gains to the distillation loss vs. the synthetic data itself. A clean ablation (e.g., supervised training on real + synthetic data vs. DPT on the same data) would clarify this.

- **The cost analysis in Figure 5 omits synthetic generation time from the visual comparison.** The text acknowledges that generation is expensive (line 241), but the headline 94% figure visually contrasts DPT's cost against "Pre-train + LP" without including the generation time in the plotted bars. The caption states *"The cost of DPT (n×) includes the times to finetune the teacher and generate the images"* but the figure itself does not make this visible. A breakdown bar showing generation cost would improve transparency for practitioners.

### Trivial
None.

## Nice-to-Haves

- An ablation of the two A/U loss components (alignment vs. uniformity, with varying weights) would help clarify their individual contributions in the KD setting.
- Comparison against a fully fine-tuned (end-to-end) pre-trained student, while essential for the main claim, would also strengthen the paper's practical recommendations even if DPT does not always surpass it — showing competitive performance at lower student cost is still a useful result.

## Removed Points

*These points were flagged for removal. Treat with caution if they arise in discussion.*

- **"Section 4.1 is missing; no training details/hyperparameters/repeats."** — The paper's Section 4 does contain content on Datasets and Models (lines 192–194) that likely corresponds to a Section 4.1 whose header was garbled during PDF extraction. The parser strips some formatting; the original submission likely has this section. Additionally, reproducibility nitpicks about undisclosed hyperparameters/runs are subject to removal per the review guidelines.
- **"The A/U loss is not novel; it's a direct application of Wang & Isola (2020)."** — The paper explicitly credits Wang & Isola (2020) (line 114) and describes the loss as an *adaptation* to the KD setting (line 112: *"We choose one that is inexpensive and interpretable as an illustration"*). The contribution is described as a reformulation of KD in contrastive terms, not as a fundamentally new algorithmic discovery. The framing is appropriate.
- **"DPT externalizes pre-training to the teacher/diffusion model."** — The paper acknowledges this: it states that the teacher and generative model are assumed "off-the-shelf" (lines 85, 175). The claim is about the *student* not needing pre-training, which is accurately scoped.
- **"The cost comparison is unfair because it compares against LP rather than full fine-tuning."** — This is subsumed by the Major weakness above. The concern about *cost* specifically is less severe because full fine-tuning would be more expensive than LP, so the cost savings would still hold (and might be even larger if compared against full fine-tuning). The issue is primarily about accuracy comparison, not cost comparison.
- **"Only one architecture pairing shown."** — Kept as a Minor weakness above. The removed version here refers to a more strongly-worded version that suggested it fundamentally invalidates the claim.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface a perspective that the paper itself does not already articulate or implicitly address.

## Suggestions

1. **Add a full end-to-end fine-tuning baseline** across all 6 datasets (e.g., ImageNet-pretrained student fine-tuned end-to-end). Even if DPT does not always beat it, showing competitive accuracy at a fraction of the student training cost would still be a strong result — and would allow the paper's central claim to be accurately calibrated.
2. **Recalibrate the headline claims** to match the actual evaluation. Either compare against full fine-tuning (preferred) or clearly state that the paper compares against pre-training + *linear probing* and drop language suggesting comparison against standard fine-tuning.
3. **Include at least one cross-architecture result (e.g., ViT teacher → ResNet18 student) in the main paper** so readers can verify the generality claim from the main text.
4. **Add an ablation comparing DPT against supervised training on the same synthetic+real data without KD** to isolate the distillation loss's contribution.
5. **Provide a visual breakdown of synthetic generation cost in the cost figure** so practitioners can assess the trade-off.

## Score and Decision

This paper proposes a well-motivated method with a clear pipeline and demonstrates meaningful training-time savings. However, the central weakness — a mismatch between the headline claim ("surpassing pretrain-then-finetune") and the actual baseline (pre-training + linear probing, which the paper redefines as "finetuning") — is a significant framing issue that undermines the paper's main conclusion. The core method has value, and the evaluation is otherwise reasonably thorough, but the paper cannot be accepted without addressing this gap. The recommended path is major revision: add full fine-tuning baselines and recalibrate claims.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>