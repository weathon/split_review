- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information I need to produce the final consolidated review.

---

## Summary

This paper introduces Conv-LoRA, a parameter-efficient fine-tuning method for the Segment Anything Model (SAM). Conv-LoRA inserts lightweight convolutional layers inside LoRA's low-rank bottleneck and uses a Mixture-of-Experts (MoE) mechanism to dynamically select the feature scale at which to apply the convolution. This injects image-relevant local inductive biases into SAM's plain ViT encoder. The paper also adapts SAM for end-to-end multi-class segmentation with minimal architectural changes. Across seven binary segmentation datasets (medical, natural, agriculture, remote sensing) and two multi-class benchmarks, Conv-LoRA with only 0.63% trainable parameters consistently outperforms LoRA, VPT, Adapter, and other PEFT baselines, often by small but consistent margins.

---

## Strengths

- **Comprehensive and consistent empirical coverage.** Conv-LoRA achieves the best or second-best score on all 14 metrics across 7 binary datasets (Table 1) and best Accuracy/mIoU on both multi-class benchmarks (Table 2), using a parameter budget (0.63%) essentially tied with LoRA (0.62%) and VPT (0.62%). The evaluation spans medical, natural, agricultural, and remote sensing domains — a broad and reproducible experimental protocol.

- **Well-motivated architectural design backed by analysis.** The paper provides attention-distance analysis (Figure 3) showing SAM's encoder develops a strong local prior through its segmentation pretraining, distinct from the global-attention patterns of an MAE-pretrained ViT. This data-driven observation directly motivates adding convolutional inductive biases to reinforce that local prior.

- **Clean demonstration that SAM's pretraining suppresses high-level semantics and that encoder finetuning recovers it.** The linear probing experiment (SAM ViT-B: 54.2% vs MAE ViT-B: 67.7% on ImageNet-1K) and the multi-class results (where decoder-only finetuning yields high Accuracy but poor mIoU, while LoRA/Conv-LoRA boost mIoU by 7–8 points) together provide concrete evidence for an important claim about SAM's limitation.

- **MoE-based dynamic scale selection is shown to outperform multi-scale fusion in both accuracy and efficiency.** Table 3 reports that MoE beats multi-scale addition on ISIC 2017 while being 1.54× faster and using 1.7 GB less memory — a genuine algorithmic improvement, not a trade-off.

- **The paper verifies that optimal feature scale varies across datasets.** Table 4 shows Leaf favors ratio 4 while ISIC favors ratio 2 for single-scale convolution injection, validating the need for dynamic (per-input) scale selection rather than a fixed scale.

---

## Weaknesses

### Fatal

None.

### Major

- **Missing ablation that isolates the effect of adding convolution from the effect of MoE-based dynamic scale selection.** The paper compares MoE vs. multi-scale fusion (both include convolution) and varies the scale with single experts (also includes convolution), but never compares plain LoRA to LoRA + fixed-scale convolution (no MoE). The central claim — that the *convolutional inductive bias* improves LoRA — is not tested in a controlled, single-variable ablation within a single table. The data to partially answer this exists across Tables 1 and 4 (e.g., LoRA on Leaf: IoU 73.7; LoRA + single conv scale-4: 74.0), but the paper never frames or discusses this comparison, leaving the attribution of gains to convolution vs. parameter increase vs. multi-scale processing ambiguous. This is an evidential gap that weakens a core contribution claim.

### Minor

- **Multi-class results (Table 2) lack standard errors or confidence intervals.** The binary experiments report mean ± standard error over three runs, but the multi-class results — where improvements over LoRA are small (e.g., +1.08 mIoU on Trans10K-v2) — report only point estimates. Without error bars it is impossible to assess whether these differences are statistically significant. The paper states "All the experiments for PEFT methods are run for three times" in the context of binary experiments, and it is unclear whether this applies to the multi-class results.

- **Hyperparameter tuning procedure for baselines is ambiguous.** The Settings section states "A larger learning rate of 3×10^{-4} is found useful for the datasets we use in agriculture and remote sensing." The paper does not clarify whether this learning rate was tuned separately for each baseline on those datasets, or applied uniformly across all methods. Since gains on the Road dataset are small (Conv-LoRA IoU 62.6 vs LoRA 62.2, +0.4), uneven tuning could account for the difference. A clear statement that each baseline's LR was independently tuned (or that the same LR was used uniformly) would resolve this.

- **The distinction between Conv-LoRA and Convpass in the related work section is too superficial.** The paper says Convpass targets image classification while Conv-LoRA targets SAM for segmentation, but the truly differentiating design choice — that Conv-LoRA uses MoE for multi-scale dynamic injection while Convpass uses a single-scale convolutional bottleneck — is only stated in the method section, not in the related work comparison where it would help orient the reader.

- **Training time and memory reported only for the MoE vs. multi-scale ablation, not for the main comparisons.** The paper reports speed/memory for MoE vs. multi-scale (Table 3) but does not provide training time or memory for Conv-LoRA vs. LoRA vs. VPT in the main experiments. Reporting per-epoch training time for one representative dataset would help users assess the practical overhead of the convolutional experts.

- **Load balancing of MoE experts is not analyzed.** The paper mentions an auxiliary loss for expert balancing (weights 1.0/2.0) but provides no analysis (e.g., expert selection histograms) showing whether the gating network avoids degenerate behavior where one expert dominates.

### Trivial

None. (The rank r value and other hyperparameters that might be missing from the main text are assumed to be in the appendix, which is stripped by the parser.)

---

## Nice-to-Haves

- **Show Conv-LoRA's effect on attention distances.** The attention-distance analysis (Figure 3) compares SAM to MAE as background motivation. A direct comparison of SAM vs. Conv-LoRA-finetuned SAM's attention distances would provide direct evidence that Conv-LoRA further restructures or shortens attention, directly supporting the "injecting local prior" claim.
- **Report expert utilization histograms per dataset.** The paper argues for per-input dynamic expert selection, but only shows that the *optimal fixed scale* varies per dataset. Showing that the gating network selects *different experts for different inputs* within a dataset would strengthen the MoE motivation.

---

## Removed Points

These points were identified by reviewers but are removed for the stated reasons:

- **Linear probing "does not directly measure whether Conv-LoRA recovers semantic information"** — Removed. The paper uses the linear probing experiment to show SAM's encoder (vs. MAE) has suppressed semantic capability, not as evidence for Conv-LoRA's effect. The actual evidence for semantic recovery is the multi-class mIoU gains in Table 2. This criticism misinterprets the purpose of the experiment.

- **Interpolation smoothing may undo convolution effect (Eq. 4)** — Removed. This is a speculative concern with no supporting evidence from the paper. The empirical results across 9 datasets demonstrate the method works effectively; the critic offers no evidence that interpolation artifacts are harming performance.

- **Rank r not stated** — Removed. This hyperparameter is likely specified in the appendix (stripped by the parser); the rule states to remove criticisms about content that may exist only in stripped supplementary sections.

- **"Not a direct comparison" criticism of attention distance analysis** — Weakened to Nice-to-Have. The paper uses attention distance to motivate the method (SAM has local attention → convolution reinforcement is sensible), not as evidence for Conv-LoRA's effect. The criticism is valid as a suggestion for strengthening but not as a weakness of the current paper.

- **Related-work distinction with Convpass should be in method section** — Downgraded from "Section-by-Section note" to minor weakness. The distinction is present in the related work section ("specifically enforcing multi-scale local priors beyond the default scale, distinguishing our approach from Convpass"), just not elaborated as fully as it could be.

- **"SAM-Adapter is not cited correctly" type concerns** — Not present in the inputs.

---

## Novel Insights

None beyond the paper's own contributions. Both reviewers accurately reflected the paper's claims and evidence without introducing genuinely novel observations that the authors missed.

---

## Suggestions

1. **Add the missing ablation:** Compare (a) plain LoRA vs. (b) LoRA + single fixed-scale convolution (without MoE) vs. (c) Conv-LoRA (full MoE) on 2–3 representative datasets. This would cleanly separate the effect of adding convolution from the effect of dynamic scale selection and directly support the central claim.
2. **Report multi-class results with error bars** (or state that variance was negligible and provide representative standard deviations in a footnote).
3. **Clarify the hyperparameter tuning procedure** — confirm whether baselines received per-dataset hyperparameter tuning or used the same LR schedule as Conv-LoRA.
4. **Add a "practical cost" row** to the main comparison table (e.g., training time per epoch or total GPU-hours) for Conv-LoRA vs. LoRA vs. VPT on one representative dataset.
5. **Include an expert-selection histogram** (e.g., for Trans10K-v2 or ISIC 2017) to demonstrate that the gating network indeed selects different experts for different inputs, not just different fixed scales per dataset.

---
