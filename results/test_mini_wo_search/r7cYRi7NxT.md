Now I have all the evidence I need. Let me produce the final review.

## Summary

Hierarchical Side-Tuning (HST) proposes a parameter-efficient transfer learning method for Vision Transformers that introduces a lightweight Hierarchical Side Network operating alongside a frozen ViT backbone. Instead of injecting small modules into the backbone, HST builds a separate multi-scale side network fed by intermediate ViT features, gated through a Meta-Register (trainable tokens per block) and a Transformation Bridge. Experiments span VTAB-1K classification, COCO detection/segmentation, and ADE20K semantic segmentation. The headline result is **76.1% average accuracy on VTAB-1K with only 0.78M trainable parameters**—a clear new SOTA among PETL methods, surpassing both prior PETL methods and full fine-tuning (65.6%) on that benchmark. On dense prediction, HST consistently outperforms other PETL methods and narrows the gap to full fine-tuning to within 1–3 points.

## Strengths

- **State-of-the-art on VTAB-1K with extreme parameter efficiency.** HST achieves 76.1% average Top-1 accuracy using only 0.78M parameters (0.9% of ViT-B's 85.98M), outperforming all prior PETL methods (SSF: 73.1%, LoRA: 72.25%, AdaptFormer: 73.10%) and full fine-tuning (65.6%) by over 10 points (Table 1). The improvement is consistent across all three VTAB-1K splits (Natural, Specialized, Structured), with particularly large gains on the structured tasks where prior PETL methods struggled.

- **Significantly narrows the PETL–full-fine-tuning gap on dense prediction.** On COCO Mask R-CNN 3×+MS, HST achieves 43.9 AP^b and 40.4 AP^m—the best among PETL methods—coming within 1.2 AP^b of full fine-tuning (45.1 AP^b), while competing PETL methods lag by 5–8 points (Table 5). On Cascade Mask R-CNN, HST surpasses full fine-tuning (+0.8 AP^b). This demonstrates that HST's hierarchical side network design is uniquely effective for dense prediction, which is a recognized limitation of prior PETL work.

- **Well-motivated component ablation study.** Table 9 progressively ablates each design element (LN tuning, weight sharing, GlobalT, Fine-Grained Injection), showing that each contributes positively and that the full system yields a 4.0% gain on VTAB-1K and 10.3 AP^b on COCO over the baseline HSN. This provides clear evidence that the architectural choices are deliberate and effective.

- **Robustness across pre-training paradigms.** Under MAE pre-training (Table 2), where other PETL methods degrade substantially, HST still achieves competitive results (e.g., 79.7% on CIFAR-100 vs. full FT's 88.9%, far above VPT-Deep's 74.2%) and ties or exceeds full fine-tuning on some FGVC datasets. This demonstrates generalization beyond a single initialization scheme.

- **Parameter-efficient Meta-Register design.** Ablation (Table 10, left) shows that a single Meta-Register token achieves 76.1% accuracy, nearly matching 32 tokens (76.2%) and outperforming 64 tokens (75.9%), while minimizing computational overhead—a concrete advantage over prompt-based methods that require task-specific prompt-length search.

## Weaknesses

### Fatal
None.

### Major

- **Abstract overstates the dense-prediction results.** The abstract states: "When applied to object detection and semantic segmentation tasks on the COCO and ADE20K testdev benchmarks, HST outperformed existing PETL methods and **even surpassed full fine-tuning**." This is misleading. Examining all seven dense-prediction configurations in Tables 5–7:
  - HST surpasses full FT on 1 setting (Cascade Mask R-CNN: +0.8 AP^b).
  - HST trails full FT on 6 settings, e.g., Mask R-CNN 3×+MS (−1.2 AP^b), ATSS (−0.7 AP^b), Semantic FPN (−1.7 to −2.2 mIoU), UperNet (−2.5 to −3.3 mIoU).
  
  The introduction (line 29) more accurately says "comparable performance," and the conclusion (line 468) says "significantly reducing the performance disparity." The abstract's stronger claim should be corrected to match the evidence. HST's true achievement—narrowing the gap to 1–3 points while using a fraction of the parameters—is a strong enough selling point without overstatement.

- **Efficiency Analysis section (Section 6.5) is empty.** The paper has a titled, labeled section heading for "Efficiency Analysis" (line 376) with no content between it and the next section. For a method that adds an entire side network with cross-attention, multi-scale convolutions, and FPN-style components, reporting FLOPs, inference throughput, peak GPU memory, and training time is essential. The parameter counts alone (reported in tables) do not capture the computational cost. Without these numbers, readers cannot assess the practical trade-off between HST's performance gains and its resource usage, especially relative to lightweight methods like LoRA or SSF that inject only small matrices into the backbone.

### Minor

- **Trainable parameter counts are higher than competing PETL methods in dense prediction.** In Tables 5–7, HST consistently uses more trainable parameters than other PETL methods (e.g., 30.6M vs. 28.4M for LoRA on Mask R-CNN 1×). The paper acknowledges that its neck dimensions differ (line 159: "[64,128,256,384] vs. 768"), which explains some of the difference, but the total parameter count is still meaningfully higher. The ablation study (Table 9) adds components without controlling for total parameter count. While the gains are substantial and unlikely to be purely parameter-driven, the paper would benefit from an ablation where a baseline method is given comparable capacity to confirm that HST's design, not just extra parameters, drives the improvement.

- **The contribution of GlobalT is relatively small on its own.** Table 10 shows "only GlobalT" achieves 75.3%, "only Meta-Register" achieves 75.7%, and the combination reaches 76.1%. The improvement from adding GlobalT to Meta-Register is +0.4%. This is not a flaw—the paper correctly reports it—but the framing could be more transparent that GlobalT provides a modest incremental gain compared to the Meta-Register and Fine-Grained Injection components.

- **VTAB-1K full fine-tuning baseline is cited from VPT rather than re-run.** The full-FT numbers used for VTAB-1K come from the VPT paper (cited as [jiax2022visual]). While this is standard practice, the paper does not discuss whether the training recipe was re-optimized for modern settings. Given that HST's 10.5% gain over this baseline is a headline claim, confirming the baseline was appropriately tuned would strengthen confidence.

### Trivial

- **Figure 6 (t-SNE) caption is vague.** The caption says "t-SNE visualization of various PETL methods applied to three tasks within different categories" but does not specify which colors correspond to which method. This makes the visualization difficult to interpret without inference.

- **Ablation of side-network depth/stage distribution is missing.** Since the side network matches ViT's 12 blocks distributed across 4 stages, testing whether fewer blocks or a different allocation harms performance would be informative. This is a minor gap given the other thorough ablations.

## Nice-to-Haves

- Report FLOPs, inference speed, and peak memory for HST vs. baselines (this is listed as a Major weakness due to the empty section, but the specific choice of metrics, the level of detail, and the format are up to the authors).
- Include a controlled experiment where a baseline PETL method is given the same total parameter budget as HST in dense prediction settings to verify that the hierarchical design, not extra capacity, is responsible for the gains.
- Add variance over multiple seeds for key results (VTAB-1K, COCO) as is increasingly standard practice.
- Visualize the multi-scale feature maps from different HSN stages or analyze cross-attention weight distributions across scales to deepen understanding of what the side network learns.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing PETL baselines for dense prediction (ConvAdapter, Bi-Adapter)"** — The paper already compares against the most established PETL baselines (LoRA, AdaptFormer, SSF, VPT). The claim that additional methods are missing is a subjective scope-expansion request, not a concrete flaw. The paper explains why ViT-Adapter (full FT) is not compared. *(Removed: scope creep / unverifiable)*

- **"Comparison of HST to full FT is not apples-to-apples in representational capacity"** — This criticism fundamentally questions the premise of PETL research: that freezing the backbone and adding a small trainable component is a valid comparison to full fine-tuning. Every PETL paper makes this comparison; it is the standard evaluation paradigm. *(Removed: misunderstands the field's standard methodology)*

- **"VTAB-1K results may be from better optimization rather than the side network design"** — The ablation study (Table 9) systematically controls for this: starting from a baseline HSN (no special components, 72.1%), each architectural addition produces measurable improvements under the same training recipe. The gains are clearly tied to specific components. *(Removed: contradicted by the paper's own controlled ablations)*

- **"Related work should compare more explicitly to ViT-Adapter in terms of parameter efficiency"** — The paper already notes that ViT-Adapter uses full fine-tuning (line 59), which makes a parameter-efficiency comparison moot. *(Removed: already addressed in the paper)*

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's evident strengths and weaknesses; no genuinely novel pattern emerges from the meta-analysis.

## Suggestions

1. Correct the abstract: replace "surpassed full fine-tuning" with a precise statement such as "narrows the gap to within 1–3 points of full fine-tuning while using a fraction of the parameters, and surpasses it on one setting (Cascade Mask R-CNN)."
2. Populate the Efficiency Analysis section with FLOPs, inference throughput, and peak GPU memory for HST vs. key baselines across both classification and dense prediction settings.
3. Add an ablation controlling for total parameter count in dense prediction (e.g., scale up a baseline adapter to match HST's parameter budget on COCO).
4. Clarify the Figure 6 t-SNE caption with a proper color legend.

## Score and Decision

**Originality:** The hierarchical side-network design that builds a separate multi-scale feature extractor alongside a frozen ViT is a clean conceptual departure from insertion-based PETL methods. The Meta-Register + T-Bridge mechanism for leveraging intermediate features is novel. **7/10**

**Importance of research question:** Extending PETL effectiveness from classification to dense prediction is a timely and practically important problem. **8/10**

**Claims supported:** The VTAB-1K claim is strongly supported. The dense prediction claim is oversold in the abstract (see Major weakness) but the actual data clearly shows HST outperforms other PETL methods and narrows the gap to full FT. **6/10** (dinged by the overclaiming)

**Soundness of experiments:** Experiments are broad (19 VTAB-1K tasks, COCO, ADE20K, two backbones, two pre-training schemes). Ablations are thorough. Missing efficiency analysis is a notable gap. **7/10**

**Clarity of writing:** Generally clear and well-structured. The architecture is well-explained with adequate figures. The empty Section 6.5 and the slightly overstrong abstract are the main issues. **7/10**

**Value to the community:** HST sets a new SOTA on VTAB-1K and provides a practical solution for PETL in dense prediction, a known hard case. This is likely to be a useful reference for future work. **8/10**

**Overall:** The paper makes a substantive contribution with convincing results on VTAB-1K and strong dense-prediction performance. The two main weaknesses—the overstated claim in the abstract and the missing efficiency analysis—are addressable and do not invalidate the core technical contribution. The method is well-designed, the experiments are comprehensive for a PETL paper, and the ablations are informative.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>