Now let me finalize and produce the consolidated review.

**Round 1 bracket:** [5, 7]. The paper is clearly above the weak-anchor range (SAM medical papers at 2–3) and below the very-strong range (papers at 8+ on unrelated topics). Within the mid-range I found anchors at 4.0 (SmartSAM, Reject), 5.33 (RefAM, Reject), 5.0 (gen2seg, Accept Poster), 6.0 (OC-ZSS, Accept Poster), and 7.0 (SAM 3, Accept Poster).

**Round 2 narrowing:** Comparing against OC-ZSS (6.0) and gen2seg (5.0) as the closest topical anchors: SAMRefiner has more thorough cross-setting evaluation than either, stronger ablations, and a clearer practical contribution. It is better than gen2seg and at least comparable to OC-ZSS. It is not at the scale of SAM 3 (7.0) but is better validated within its scope. **Final score: 6.0.**

---

## Summary

This paper proposes SAMRefiner, a framework that adapts the Segment Anything Model (SAM) for mask refinement — improving pre-existing coarse masks without task-specific training. The core technical contribution is a multi-prompt excavation strategy that mines diverse prompts (distance-guided points, context-aware elastic boxes, Gaussian-style masks) from coarse masks and lets them collaborate to mitigate mask defects. An optional IoU adaptation step (SAMRefiner++) further refines mask selection using a LoRA adapter on SAM's IoU head, trained in a self-supervised manner. The method is evaluated across an unusually broad range of settings (unsupervised, semi-supervised, weakly-supervised, fully-supervised), multiple datasets (DAVIS, COCO, VOC), and both instance and semantic segmentation tasks, consistently showing improvements and efficiency gains over prior refinement methods.

## Strengths

- **Multi-prompt excavation is clearly effective.** Table 1 shows the multi-prompt combination achieves 58.4/64.5 IoU on DAVIS-585, far exceeding single-prompt baselines (mask alone: 10.8/23.0, point+box: 47.0/55.2). The improvements are large, consistent, and directly support the claim that diverse prompts collaborate to overcome coarse mask defects.

- **Thorough and unusually broad evaluation.** The method is tested on three supervision paradigms (unsupervised, semi-supervised, weakly-supervised), two task types (instance and semantic segmentation), multiple datasets (DAVIS-585, COCO, VOC), and with multiple downstream backbones (Mask R-CNN, Cascade, SOLOv2, YOLACT). Tables 3, 4, and 6 all show consistent gains, strongly supporting the "universal" claim.

- **Clean ablations for each component.** Tables 2a–c isolate the contribution of distance-guided points, context-aware elastic boxes (CEBox), and the split-then-merge (STM) pipeline, with each component showing measurable gains. This makes the method's design decisions transparent and justified.

- **Practical efficiency advantage.** Table 5 reports that SAMRefiner refines COCO train5K in 409 seconds — roughly 2–10× faster than CascadePSP, CRM, and SegRefiner — because SAM can batch-process multiple masks per image. This is a genuine practical advantage over prior refinement methods.

- **Novel insight about mask prompt utility.** The paper documents that the mask prompt alone fails for SAM (10.8/23.0 IoU) but, when combined with point and box, yields a ~20% IoU gain over point+box alone. This is a useful empirical finding for the community.

## Weaknesses

### Fatal

None.

### Major

- **The IoU adaptation step's robustness to systematic coarse-mask errors is not analyzed.** The ranking loss (Eq. 4) encourages the adapted IoU head to rank highest the mask that is most similar to the coarse mask. If coarse masks have systematic biases (e.g., consistently missing thin structures), the adaptation could learn to favor masks that replicate these errors. While Table 1 shows SAMRefiner++ *consistently improves* over SAMRefiner across all prompt combinations, the paper provides no analysis of *when* the adaptation degrades — e.g., by corrupting coarse masks with known noise patterns and measuring whether the adaptation still helps. Without this analysis, it is unclear whether the gains in Table 1 reflect genuine refinement or a tendency to select masks similar to the initial coarse mask. This does not invalidate the main contribution, but it weakens the evidence for the IoU adaptation component.

- **The SOTA comparison (Table 5) does not separate the contribution of SAM's backbone from the prompting scheme.** SAMRefiner uses SAM's ViT-H backbone with massive SA-1B pretraining, while prior methods (CascadePSP, CRM, SegRefiner) use far smaller models trained from scratch. The paper attributes the large gap to "better robustness to mask noise," but an equally plausible factor is SAM's richer features. Controlling for this — e.g., by reporting how much of the gap is closed when prior methods use SAM's image encoder as a feature backbone — would sharpen the claim that the prompting strategy is the driving factor. As presented, the reader cannot attribute the improvement to the method vs. the backbone.

### Minor

- **No sensitivity analysis for key hyperparameters.** The CEBox expansion threshold (λ=0.1), similarity binarization threshold (0.5), and Gaussian mask parameters (ω=15, γ=4) are set to fixed defaults across all datasets without any ablation showing that performance is stable over a range of values. Given these parameters control prompt geometry, their stability matters for the claim of robustness.

- **No error bars or measures of variance.** All numerical results (Tables 1–6) are reported as point estimates without standard deviations, confidence intervals, or multiple-run statistics. Given variance in coarse mask quality across images, this limits the reader's ability to assess the significance of the reported improvements, especially where gains are modest (e.g., <2% in some Table 3/4 entries).

- **SAM checkpoint variant is not specified.** The paper does not state which SAM variant (ViT-B, L, or H) is used. Given that efficiency claims and absolute performance numbers depend on model size, this omission makes the results harder to reproduce and interpret.

- **No failure analysis.** The paper shows only positive visual results (Figs. 1, 4). Given the method's reliance on prompting from noisy masks, cases where refinement degrades the mask (e.g., removing valid thin structures, adding spurious regions) are likely but not discussed or visualized. Acknowledging failure modes would strengthen credibility.

### Trivial

None.

## Nice-to-Haves

- An analysis of how performance changes when coarse masks are systematically corrupted with known noise patterns (erosion, dilation, random holes) to test the IoU adaptation's robustness.
- An upper-bound experiment where SAM is prompted with the tight box from the *ground-truth* mask, to show how much of the remaining gap to ground truth is due to prompt quality vs. SAM's inherent limitations.
- Sensitivity analysis for CEBox parameters (λ, iteration count) and Gaussian mask parameters (ω, γ) across one or two datasets.

## Removed Points

- *"Missing related works"* — Per policy, I do not include missing-citation criticisms as I cannot verify existence of all relevant works.
- *"Formatting/style nitpicks"* / *"Missing appendix content"* — These concern content stripped by the parser, not present in the original submission.
- *"The training-free SAMRefiner is not well-defined"* — The paper clearly differentiates SAMRefiner (training-free prompting) from SAMRefiner++ (with IoU adaptation). The distinction is explicit.
- *"Batch processing definition is unclear"* — The paper explains "SAM can batch process multiple masks in an image simultaneously" (line 205), which is sufficiently clear for the claim.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful observation about the circular dependency risk in the IoU adaptation step, but this is an analysis gap rather than a novel insight about the approach itself.

## Suggestions

1. **Add a controlled experiment for the IoU adaptation:** Systematically corrupt coarse masks (e.g., add erosion, dilation, salt-and-pepper noise) and measure whether SAMRefiner++ still improves over SAMRefiner or begins to degrade. This directly addresses the concern about error reinforcement.
2. **Disentangle backbone from method:** Report results where SAM's ViT image encoder is used as a feature backbone within CascadePSP or CRM, to separate the contribution of SAM's pretraining from the prompting strategy.
3. **Add error bars** to the main tables, especially for Tables 3 and 4 where improvements are modest. At minimum, report variance across multiple coarse mask qualities or across dataset folds.
4. **Specify the SAM checkpoint** (ViT-B/L/H) used in all experiments and discuss whether results vary across variants.
5. **Add a failure case figure** showing examples where SAMRefiner degrades the mask, with a brief discussion of common failure patterns.

## Score and Decision

The paper is a solid, well-executed contribution to mask refinement. The multi-prompt excavation strategy is effective, the evaluation is unusually thorough across tasks and settings, and the efficiency advantage is practically significant. The main concerns — incomplete analysis of the IoU adaptation's robustness and conflated SOTA comparison — are real but bounded; they reduce the clarity of *what* drives the reported gains without invalidating the core contribution. The empirical evidence for the prompting scheme itself (Tables 1–2, training-free SAMRefiner) is strong and independent of these concerns.

**Score: 6.0** — A solid paper with real contributions and thorough experiments, held back from the top tier by incomplete analysis of a key component and a SOTA comparison that does not fully isolate the method's contribution from the backbone's capacity.

### Calibration Report

| Path | Avg Score | Round | Comparison to This Paper |
|------|-----------|-------|--------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/qdtdDX18GE.md` | 2.50 | 1 | Medical SAM paper, withdrawn — much weaker |
| `/home/wg25r/review_agent/human_reviews_2026/e1iCiitcMw.md` | 2.00 | 1 | Medical SAM enhancement, withdrawn — much weaker |
| `/home/wg25r/review_agent/human_reviews_2026/voBQXpnqKS.md` | 3.00 | 1 | Unrelated topic, withdrawn — weaker |
| `/home/wg25r/review_agent/human_reviews_2026/i9c9tT5dFq.md` | 3.00 | 1 | Multi-view SAM, withdrawn — weaker |
| `/home/wg25r/review_agent/human_reviews_2026/r35clVtGzw.md` | 7.00 | 1,2 | SAM 3, Accept Poster — larger-scale contribution, comparable quality, slightly stronger |
| `/home/wg25r/review_agent/human_reviews_2026/08pxmTLKTT.md` | 4.00 | 1 | SmartSAM, Reject — weaker evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/qhglCWZsuh.md` | 4.00 | 2 | Seg-Agent, Reject — weaker; less thorough evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/gfICbAYTwn.md` | 5.33 | 1,2 | RefAM, Reject — weaker validation and novelty concerns |
| `/home/wg25r/review_agent/human_reviews_2026/fEZ6DqfwTR.md` | 5.33 | 2 | No time to train! Reject — less thorough evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/7Db6Pbrcha.md` | 5.00 | 2 | SHERPA, Reject — weaker |
| `/home/wg25r/review_agent/human_reviews_2026/oeWqDrTb38.md` | 6.00 | 2 | OC-ZSS, Accept Poster — comparable quality and thoroughness |
| `/home/wg25r/review_agent/human_reviews_2026/cSpjHOf04S.md` | 5.00 | 2 | gen2seg, Accept Poster — weaker evaluation quality |
| `/home/wg25r/review_agent/human_reviews_2026/DM0Y0oL33T.md` | 8.00 | 1 | Unrelated topic — stronger but different domain |
| `/home/wg25r/review_agent/human_reviews_2026/kI27Niy4xY.md` | 8.00 | 1 | Unrelated topic — stronger but different domain |
| `/home/wg25r/review_agent/human_reviews_2026/DTQIjngDta.md` | 8.00 | 1 | Unrelated topic |
| `/home/wg25r/review_agent/human_reviews_2026/kkBOIsrCXh.md` | 8.00 | 1 | Unrelated topic |

**Round 1 bracket:** [5, 7].  
**Round 2 narrowing:** Compared to OC-ZSS (6.0, Accept Poster) — comparable thoroughness and quality. Compared to gen2seg (5.0, Accept Poster) — clearly stronger evaluation. Compared to SAM 3 (7.0, Accept Poster) — smaller scope but better validated within scope.  
**Final score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>