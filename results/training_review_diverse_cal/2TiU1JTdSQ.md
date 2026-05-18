Now I have a thorough understanding of the paper and can verify all claims against the actual text. Let me produce the final review.

## Summary

This paper proposes Selective LoRA, a fine-tuning method for text-to-image (T2I) models that identifies which layers are most sensitive to a desired concept (e.g., viewpoint or style) via a gradient-ratio metric, then selectively applies LoRA to only those layers. The goal is to generate domain-aligned yet diverse segmentation datasets — avoiding the memorization/overfitting of full LoRA while fixing the domain misalignment of pretrained-only approaches. Experiments on Cityscapes (in-domain few-shot and fully-supervised) and four domain generalization benchmarks (ACDC, Dark Zurich, BDD100K, Mapillary Vistas) show consistent improvements over DatasetDM and other prior work, with +2.30 mIoU in few-shot and +1.53 mIoU average across DG settings.

## Strengths

1. **Novel and well-motivated approach to targeted fine-tuning.** The concept sensitivity metric (gradient norm ratio between a concept loss and the standard diffusion loss) is a clean way to automatically identify which layers are relevant to a specific concept (style or viewpoint). This automates what prior work did manually (ablating blocks one by one) and is validated by the different behavior of style-selective vs. viewpoint-selective LoRA across in-domain vs. DG tasks.

2. **Consistent and substantial performance gains across multiple benchmarks.** The method beats DatasetDM, DGInStyle, DATUM, and InstructPix2Pix in nearly all settings. Gains are meaningful: +2.30 mIoU at 0.3% few-shot, +1.34 mIoU fully-supervised, +1.53 mIoU average across four DG datasets. Results hold across three different DG backbones (ColorAug, DAFormer, HRDA), showing robustness.

3. **Clean ablations showing that concept choice matters.** Tables 5 and 6 systematically compare style-selective vs. viewpoint-selective LoRA at various proportions. The finding that style-selective LoRA (2%) is best for in-domain while viewpoint-selective LoRA (3%) is best for DG directly validates the paper's thesis — the right concept to learn depends on the problem setting. This is not a trivial result.

4. **Practical efficiency.** Fine-tuning Selective LoRA takes only one hour on a single V100 GPU, versus 20 hours for DatasetDM's label generator training. The selected proportion search (1–10%) is reasonable.

5. **Quantitative analysis of the alignment-diversity trade-off.** Using CMMD (domain alignment) and CLIP Score (text-condition faithfulness under adverse weather prompts), the paper shows that Selective LoRA balances these competing objectives better than original LoRA. Original LoRA achieves the best CMMD but catastrophically loses CLIP Score; Selective LoRA preserves both.

## Weaknesses

### Fatal
None.

### Major

1. **No "random layers" baseline in the ablation.** The ablation tables (5, 6) compare Selective LoRA against the pretrained model and original LoRA (all layers), but do not include a control where the same proportion of layers (2%, 3%) is selected at random. Without this, we cannot tell whether the sensitivity-based selection adds value beyond "fine-tuning any small subset of layers avoids overfitting." Since the selected proportions are very small (2–3%), it is plausible that almost any 2% of layers would produce similar results. This directly weakens the claim that *which* layers are selected matters. The fix is straightforward: add a random-selection baseline (averaged over multiple seeds) to the ablation.

### Minor

2. **Confounding between T2I image quality improvement and label generator adaptation.** The main comparisons against DatasetDM (Tables 1, 2) involve two simultaneous changes: (a) the T2I model is fine-tuned with Selective LoRA, and (b) the label generator is retrained on the features of the fine-tuned model (line 120: "Distinct from DatasetDM, we train the label generator based on the fine-tuned T2I model"). This means gains could come from either better images, better feature representations for the label generator, or both. The ablation studies (Tables 5, 6) partially address this because there all methods (pretrained, original LoRA, Selective LoRA) retrain the label generator on their respective models, isolating the effect of layer selection. However, the main tables — which readers will cite — do not. A clean decoupling experiment (e.g., generating images with the fine-tuned model but using a label generator trained on the pretrained model's features) would strengthen attribution.

3. **Memorization claim lacks quantitative support.** The paper repeatedly invokes "memorization" as the motivation for Selective LoRA, but the only evidence is qualitative (Figure 1). No quantitative diversity or memorization metrics are reported — e.g., nearest-neighbor retrieval in feature space, LPIPS pairwise diversity, or FID relative to the training set. Since Table 3 shows original LoRA has the *best* CMMD (domain alignment), the paper must rely on the memorization argument to explain why original LoRA underperforms in segmentation. Quantifying this gap would make the motivation substantially stronger.

4. **The number of images used for computing concept sensitivity is unspecified.** Section 3.2 (line 78) says "a few generated images" — how many? This parameter affects the variance of the sensitivity scores and should be reported. (If it is in the appendix, it was stripped; please include it in the main text.)

5. **No comparison to full fine-tuning or other PEFT methods (Adapters, Prefix Tuning).** The paper argues that full fine-tuning and original LoRA overfit, but does not actually include full fine-tuning as a baseline. Including it — even as an additional row — would directly validate the claim that Selective LoRA hits a better sweet spot. Other PEFT variants would further strengthen the evaluation.

### Trivial

6. **The stop-gradient in the concept loss (Eq. 4) is mentioned but not justified.** The design choice to use `sg[ϵ_θ(x_t, c_Aug)]` as a pseudo-target is reasonable (standard practice in distillation/sensitivity estimation), but a brief justification would help readers.

7. **The different optimal k for style (2%) vs. viewpoint (3%) is noted but not discussed.** The paper searches {1, 2, 3, 5, 10}% and picks the best, but does not offer intuition for why viewpoint requires slightly more layers.

## Nice-to-Haves

- Add a brief discussion of failure cases — e.g., what happens when the desired concept is not well-represented in the pretrained model's knowledge.
- The CLIP Score table (Table 4) could be complemented with human evaluation or additional diversity metrics for a fuller picture.
- A discussion of why the optimal k differs between style and viewpoint would improve the reader's understanding of the method.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **DG comparison fairness on dataset size** (Critic point 3): The paper explicitly states (line 146) that *all* DG methods train on "a combination of the 2975 Cityscapes image-label pairs and the 2500 generated image-label pairs." The comparison is controlled. The reviewer misread this passage.
- **Label generator training details too vague** (Critic point): The paper explicitly states "Additional implementation details, including the label generator architecture, hyper-parameters, number of generated pairs, and pseudo-code, are provided in Appendices A.1, A.2, and A.3." The appendix was stripped by the parser.
- **"First to comprehensively address" is risky** (Critic point): This is a claim about related work coverage. Per instructions, missing related works are not evaluated.
- **FIX/NEW markers suggest not-yet-cleaned draft** (Critic point): These are formatting/parser artifacts. The original submission does not have these issues.
- **Pure formatting/style nitpicks** have been removed per policy.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the review is the asymmetric finding in Tables 5 and 6: style-selective LoRA dominates in-domain (where you want the target style), but viewpoint-selective LoRA dominates DG (where you need to preserve the ability to generate varied weather). This demonstrates that different downstream tasks require different *concepts* to be memorized vs. kept flexible, and the paper's framework provides a principled way to make this choice. The CMMD vs. CLIP Score trade-off (Tables 3 and 4) further reinforces this — alignment and condition fidelity are inherently at odds, and the method can navigate the Pareto front by choosing which concept to fine-tune.

## Suggestions

1. **Add a random-layer-selection baseline** to the ablation (Tables 5, 6). Average over several random seeds for robustness. This is the single most impactful addition.
2. **Quantify memorization/diversity** with metrics such as: LPIPS distance to nearest training image, within-set LPIPS diversity, or FID/IS relative to the training set.
3. **Decouple the label generator** in one experiment: generate images with the Selective LoRA model but use a label generator trained on the pretrained model's features. If gains hold, image quality is the driver.
4. **Specify the exact number of images** used to compute concept sensitivity.
5. **Include full fine-tuning** as a baseline in the ablation to directly validate the overfitting claim.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>