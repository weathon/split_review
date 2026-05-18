Now I have all the information needed to construct the final review. Let me synthesize everything.

---

## Summary

This paper proposes SAMRefiner, a framework that adapts the Segment Anything Model (SAM) for refining coarse segmentation masks. The core innovation is a multi-prompt excavation strategy that mines three types of noise-tolerant prompts from coarse masks — distance-guided points, context-aware elastic bounding boxes (CEBox), and Gaussian-style masks — which collaborate to mitigate defects in the coarse input. An optional self-boosted IoU adaptation step (SAMRefiner++) further improves mask selection via a LoRA adapter on SAM's IoU head, trained without extra annotations. Extensive experiments across instance and semantic segmentation benchmarks under unsupervised, semi-supervised, and weakly-supervised settings demonstrate consistent improvements in mask quality and downstream model performance, often with higher efficiency than prior refinement methods.

## Strengths

1. **Novel multi-prompt excavation that jointly exploits points, boxes, and Gaussian-style masks to handle noise in coarse masks.** Table 1 demonstrates that combining all three prompt types yields substantially higher IoU than any single prompt, with the mask prompt adding meaningful gains when combined with point/box. This directly supports the core claim of a noise-tolerant prompting scheme.

2. **Self-boosted IoU adaptation (SAMRefiner++) that improves mask selection without extra annotations.** The LoRA-style adapter on SAM's IoU head, trained with a ranking loss supervised by coarse-mask IoU, consistently improves top-1 mask selection across all prompt combinations in Table 1. Fig. 5c provides supporting analysis showing coarse-IoU-based selection for single prompts approaches the ground-truth upper bound.

3. **Consistent and large-margin improvements across diverse supervision settings.** On COCO instance segmentation (Table 3), SAMRefiner improves pseudo-mask AP by over 10% for PointWSSIS with 1% annotations. For semantic segmentation on PASCAL VOC (Table 4), it boosts pseudo-mask mIoU by up to 9.8% (MaskCLIP). This breadth of positive results validates the paper's claim of universality.

4. **State-of-the-art accuracy coupled with higher efficiency.** In Table 5, SAMRefiner surpasses CascadePSP, CRM, SegRefiner, and Dense CRF on DAVIS-585, COCO, and VOC while being at least 5× faster than CascadePSP and supporting batched refinement of multiple masks per image.

5. **Split-then-merge (STM) pipeline for multi-object semantic segmentation.** The paper identifies that SAM struggles with disconnected objects in a semantic mask, and STM brings a +6.2 mIoU improvement for extremely coarse masks (MaskCLIP, Table 2c) — a well-motivated technical addition addressing a specific SAM failure mode.

6. **Systematic ablation of design choices for each prompt type.** Tables 2a–2c dissect the contribution of each component (distance-guided points vs. random/center, tight box vs. CEBox, with/without STM), providing clear evidence that each design choice is necessary for the final performance.

7. **Evaluation on COCO val set using LVIS annotations (higher-quality ground truth).** Table 6 demonstrates consistent improvements across multiple fully-supervised models (Mask R-CNN, PointRend, Mask2Former, etc.), strengthening the claim of being a generic post-processing toolkit.

## Weaknesses

### Fatal
None.

### Major
None. The weaknesses identified below concern insufficient analysis depth for specific design choices, not fundamental flaws in the approach. The paper's core contribution — that multi-prompt excavation from coarse masks enables effective SAM-based refinement — is well-supported by the experiments.

### Minor

1. **Insufficient analysis of the Gaussian-style mask prompt design.** The paper motivates the Gaussian form with a distance transform but does not ablate the hyperparameters ω and γ (set to 15 and 4, line 167) or compare against alternative mask formulations (e.g., a softened binary mask, a signed distance field, a blurred coarse mask). Given that the mask prompt adds measurable value (point+box+mask vs. point+box in Table 1), the reader cannot tell whether the specific Gaussian form matters or a simpler design would suffice. This is a common gap in prompt-design papers but worth addressing.

2. **CEBox parameters are unablated and robustness to noise is unexamined.** The similarity map threshold (0.5) and expansion threshold λ (0.1) are set without ablation. The improvement from CEBox is modest (Table 2b: AP_box 42.2→44.0 for CutLER), and the paper does not analyze failure cases where false positives in the coarse mask corrupt the query embedding and cause inappropriate expansion. The approach is sensible but the design space is underexplored.

3. **STM merging criteria are heuristic with no failure mode analysis.** The split-then-merge pipeline for semantic segmentation relies on hand-designed criteria (box area variation, mask area occupancy). While STM clearly helps empirically (Table 2c: +6.2 mIoU for MaskCLIP), the paper does not discuss when it might hurt — e.g., when two distinct objects of the same category are spuriously merged via noise, or when a single object is incorrectly split. The algorithm parameters are not ablated. This component deserves more rigorous treatment given that semantic segmentation is a primary application.

4. **IoU adaptation design choice is plausible but the alternative (multi-prompt training) is untested.** The paper trains the LoRA adapter on single-prompt examples (where coarse IoU is reliable) and applies it to multi-prompt inference (where coarse IoU is unreliable). This is well-motivated (Fig. 5c) and shows consistent improvement (Table 1), but the alternative of training on multi-prompt examples with a robust ranking loss is never compared. The improvement from SAMRefiner to SAMRefiner++ is modest (e.g., 80.2→81.0 for full prompts), so validating the design choice would strengthen the paper. Additionally, it is unclear whether this improvement generalizes beyond DAVIS-585 to COCO or VOC.

5. **No limitations paragraph.** The paper does not discuss types of coarse masks or scenarios where SAMRefiner might fail (e.g., extremely thin objects, highly cluttered scenes, or masks with severe topological errors). A brief discussion of failure modes would improve completeness and help users set appropriate expectations.

6. **The claim of being the "first solution" for SAM-based mask refinement (line 34) should be verified against concurrent work.** Given the rapid pace of the field through mid-2026, this priority claim could be contested. This does not affect the paper's technical contribution but is a factual claim worth checking.

### Trivial
None.

## Nice-to-Haves

- **Statistical significance / variability:** Reporting standard deviations or multi-run variability would help assess reliability, especially for modest improvements. However, single-run evaluation on established benchmarks is standard practice in this field.
- **Per-mask efficiency breakdown:** The paper reports total time for COCO train5K but not time per mask; since SAM encodes images once and decodes per prompt, clarifying the per-mask cost would be informative.
- **Ablation of STM parameters** (merging thresholds) and **CEBox parameters** (λ, similarity threshold) to validate robustness.
- **Test SAMRefiner++ on additional datasets** (COCO, VOC) to confirm the IoU improvement is not DAVIS-specific.

## Removed Points

- *Criticism about STM algorithm not being in main paper (referenced as Algorithm 1):* The parser strips appendix content from all papers; the algorithm exists in the original submission. Removed per instructions.
- *Criticism about the mask prompt improvement being "nearly 20%":* This is from the Strength Finder, not the harsh critic. The harsh critic correctly states the point+box+mask vs. point+box improvement as ~3 IoU points, which is accurate. No issue here.
- *Criticism that the IoU adaptation has a "logical gap":* The paper provides clear reasoning and empirical validation (Fig. 5c, Table 1). The framing as a "logical gap" overstates the issue; it is more accurately an unvalidated design choice against an alternative. Moved to Minor weakness #4 with appropriate framing.
- *Criticism about comparison with HQ-SAM adding limited insight:* This is an opinion about experimental design, not a weakness. The comparison is informative and standard practice. Removed.

## Novel Insights

The key insight that emerges across the reviews is that the paper's contribution is best understood as a **prompt engineering strategy for SAM** rather than a fundamentally new architectural contribution. The observation that SAM's mask prompt mechanism (designed for cascade refinement during pretraining) fails when used independently with coarse masks, but can be rescued by a Gaussian-smoothed form, is a non-obvious finding. Similarly, the empirical discovery that coarse-IoU-based selection is more reliable than SAM's own IoU predictions for single-prompt cases (but not multi-prompt) and that this ranking ability can transfer across prompt complexities via a lightweight adapter is a practical insight. That said, none of the novel insights extend substantially beyond what the paper itself already articulates.

## Suggestions

1. **Add ablations for the Gaussian mask prompt:** Compare against at least two alternatives (softened binary mask, signed distance field) on DAVIS-585, and test sensitivity to ω and γ. This would validate — or potentially simplify — the current design.

2. **Analyze CEBox failure cases:** Show examples where the similarity map leads to incorrect expansion and quantify how often this occurs relative to the tight box baseline. This would help readers understand when CEBox is most beneficial.

3. **Test the IoU adaptation on COCO or VOC** to confirm the SAMRefiner++ improvement generalizes beyond DAVIS-585.

4. **Add a limitations paragraph** discussing failure modes — e.g., objects with extreme aspect ratios, highly cluttered scenes, masks with severe topological errors.

5. **Verify the "first solution" claim** or rephrase it to "to our knowledge, the first."

## Score and Decision

The paper presents a well-motivated, practical method for refining coarse segmentation masks using SAM. The core idea is sound, the experiments are extensive, and the results are consistently positive across diverse settings and baselines. The weaknesses concern gaps in analysis depth for specific design choices rather than fundamental flaws. These are addressable in a revision.

**Score: 7.0** — A solid paper with clear contributions and thorough evaluation. The missing ablations and analysis gaps are worth addressing but do not undermine the core claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>