Now I have all the information needed. Let me construct the final review.

## Summary

This paper proposes Conv-LoRA, a parameter-efficient finetuning method for SAM that inserts lightweight convolutional layers inside LoRA's bottleneck structure and uses Mixture-of-Experts (MoE) for dynamic scale selection. The method aims to inject local priors into SAM's plain ViT encoder and recover high-level semantic learning capacity that SAM's binary-mask pretraining suppresses. Experiments across binary and multi-class segmentation benchmarks spanning medical, natural, agricultural, and remote sensing domains show consistent but modest improvements over LoRA and other PEFT baselines.

## Strengths

- **Consistent improvement over all PEFT baselines across multiple domains with negligible parameter overhead.** Conv-LoRA (4.02M parameters) outperforms LoRA (4.00M) — and all other PEFT methods, including LST with 11.49M parameters — on every metric across all datasets in Table 1 (binary) and Table 2 (multi-class). The improvement is consistent in direction, not cherry-picked. The parameter overhead over LoRA is only 0.02M (≈0.5%), which genuinely preserves parameter efficiency.

- **Diagnostic evidence for SAM's semantic limitation and its recovery via PEFT.** The linear probing experiment (Sec. 4.2) cleanly shows that SAM's ViT-B encoder achieves only 54.2% on ImageNet-1K vs. MAE's 67.7%, confirming SAM's pretraining suppresses high-level semantics. The mIoU jump from decoder-only tuning (~50%) to PEFT methods (≥67%) on Trans10K-v2 multi-class segmentation (Table 2) directly supports the claim that finetuning the encoder recovers semantic understanding.

- **Attention distance analysis validates the design motivation.** Figure 5 shows SAM's deep layers have many short-mean-distance attention heads compared to MAE, confirming SAM acquires a local prior through segmentation pretraining — justifying why additional convolutions could further exploit this property.

- **MoE is more efficient than multi-scale fusion.** Table 3 (MoE vs. multi-scale) shows MoE achieves higher Jaccard (77.9 vs. 77.4) on ISIC 2017 while being faster (1.22 vs. 0.79 iters/s) and more memory-efficient (21.7 vs. 23.4 GB), supporting the efficiency motivation.

## Weaknesses

### Fatal
None.

### Major

- **The MoE gating mechanism — a central design contribution — is not analyzed at all.** The paper claims the gating network learns to dynamically select experts at appropriate scales for different inputs, but provides no evidence for this. There is no analysis of: (a) expert selection frequency/distribution across a dataset, (b) correlation between selected scale and object size in the input, (c) whether the gating collapses to a single expert, or (d) visualization of gating probabilities on representative images. Table 3 shows MoE outperforms multi-scale sum on one dataset, but this does not demonstrate that the gating is doing anything meaningful — it could simply be that sparsity acts as a regularizer. Without this analysis, the MoE component risks being over-engineered: a simple per-dataset grid search over scales (which the paper itself shows works reasonably well in Table 4) might match or exceed performance at lower complexity.

- **Gains over LoRA are modest and statistical significance is not established.** The improvements on most metrics range from 0.3 to 1.5 points (e.g., Road IoU: 62.6 vs. 62.2; CAMO S_α: 88.3 vs. 88.0; Leaf Dice: 84.3 vs. 83.6). Given that multiple comparisons are made across many datasets and metrics, the absence of any statistical significance testing (paired tests or confidence intervals) is a real gap. Some differences (e.g., Leaf Dice: 84.3±0.34 vs. 83.6±0.13) appear significant at ~2 SE, but others (e.g., Road Dice: 76.8±0.27 vs. 76.5±0.18) do not. The paper's claim of a "clear performance boost" (Table 1 caption) is stronger than the evidence warrants, especially for the smaller-gap datasets. This matters because the baseline (LoRA) already achieves strong performance, and the added MoE+convolution complexity raises the question of whether the practical benefit justifies the complexity.

### Minor

- **Novelty is incremental relative to Convpass.** The paper acknowledges Convpass (Jie & Deng, 2022) which also inserts convolutions into LoRA's bottleneck for ViT image classification. The main differentiators are (a) application to SAM/segmentation rather than image classification, and (b) the multi-scale MoE extension. While these are legitimate extensions, the conceptual delta from Convpass is modest. The paper would benefit from a more explicit discussion of what novel technical challenges arise in the SAM + segmentation setting that Convpass did not address.

- **The specific rank *r* used for LoRA/Conv-LoRA is not stated.** The paper defines *r* symbolically (line 137) but never gives the numerical value used in experiments, making the parameter counts (4.00M vs. 4.02M) less interpretable and harming reproducibility.

- **The "optimal scale" ablation (Table 4) is limited to only 2 datasets.** While the results do show that the best scale varies (ratio 4 for Leaf, ratio 2 for ISIC 2017), this is thin evidence for the claim that scale preference varies "across different datasets" in general. Expanding this to more datasets would strengthen the motivation for MoE.

- **The "domain-specific" baselines in Table 1 are not identified by name.** The placeholder "*Domain Specific*" is explained in the caption as referring to methods "specifically designed for the tasks," but the specific methods are not named in the main text. This makes the comparison opaque.

### Trivial
None beyond those listed as minor.

## Nice-to-Haves

- **Demonstrate MoE gating is meaningful.** A visualization of gating probabilities per expert for sample images, or a check of whether selected scale correlates with average mask area, would substantially strengthen the paper.
- **Fixed-scale per-dataset comparison.** For each dataset, compare Conv-LoRA (with MoE) to the best single-scale version found by validation sweep. If the fixed-scale version matches MoE on most datasets, the MoE complexity is harder to justify.
- **Statistical significance tests** for the core Conv-LoRA vs. LoRA comparison across datasets would clarify where the method is most impactful.

## Removed Points

These points were identified by reviewers but flagged for removal per the review guidelines:

- **"Base ViT size not stated"** — Removed because line 281 explicitly states "SAM's ViT-B encoder." Factually wrong.
- **"Structure loss not defined in main text"** — Removed because line 188 defines it as "the combination of weighted IoU loss and binary cross entropy loss." Factually wrong.
- **"Missing ablation with scale=1 (convolution at default scale)"** — Removed because Table 4 *includes* scale=1 for both Leaf and ISIC 2017 datasets. The reviewer overlooked this.
- **"Paper should show LoRA/Conv-LoRA improves ImageNet accuracy after finetuning"** — Removed as scope creep. The paper's claim is about SAM's limitation, supported by linear probing. Requiring full ImageNet finetuning is beyond the paper's scope and would require resources disproportionate to the claim.
- **"The paper should also cover Y / domain Z / additional tasks"** — Not present in these reviews, but the critic's demands for broader baselines beyond what is standard for the paper's class were filtered.

## Novel Insights

None beyond the paper's own contributions. The reviews surface well-known concerns (statistical rigor, ablation completeness) that apply broadly to PEFT papers reporting incremental gains, but do not reveal any novel perspective on the method or problem.

## Suggestions

1. **Add MoE gating analysis.** This is the single most impactful addition. Show expert selection distributions for at least 2–3 datasets, and check whether the selected scale correlates with a simple proxy for object scale (e.g., average mask area ratio). Without this, the MoE contribution is purely architectural — a gating network is proposed but never shown to gate.

2. **State the rank *r* numerically.** This is a one-line fix critical for reproducibility.

3. **Acknowledge the modest gain magnitude explicitly** and provide statistical testing (even a simple paired bootstrap or 95% CI) for the Conv-LoRA vs. LoRA comparison across all datasets. If the gains are not significant on some datasets, say so and discuss implications.

4. **Name the domain-specific baselines** (or add a footnote) so readers can assess the comparison.

5. **Expand the optimal-scale ablation** to more datasets, or alternatively remove the claim that scale preference "varies across datasets" as a general finding if it's only tested on two.

## Score and Decision

The paper addresses a real problem — adapting SAM to downstream segmentation — and the broad, consistent experimental evaluation is a genuine strength. However, the core limitations are significant: the gains over LoRA are modest across the board, and the MoE component — which is half of the claimed contribution — is completely unanalyzed. The paper would need substantially stronger evidence (gating analysis, statistical significance, clearer separation of convolution vs. multi-scale benefits) to support its central claims. In its current form, the evidence is thin enough to tilt toward rejection, though the method has potential merit.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>