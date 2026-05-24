## Final Review: SAMRefiner: Taming Segment Anything Model for Universal Mask Refinement

## Summary

This paper proposes SAMRefiner, a method to adapt the Segment Anything Model (SAM) for the task of refining coarse segmentation masks. The core idea is a multi-prompt excavation strategy that extracts distance-guided points, context-aware elastic bounding boxes (CEBox), and Gaussian-style masks from a coarse mask, then feeds these prompts to SAM to generate refined masks. A split-then-merge (STM) pipeline extends the approach to multi-object semantic segmentation, and an optional IoU adaptation step (SAMRefiner++) further improves mask selection. The method is evaluated extensively across unsupervised, weakly-supervised, semi-supervised, and fully-supervised settings on DAVIS, COCO, VOC, and LVIS benchmarks.

## Strengths

- **Multi-prompt excavation yields large and well-demonstrated gains.** Table 1 shows that the full prompt combination (point+box+mask) achieves 86.9 IoU on DAVIS-585, far above point-only (53.7) or box-only (68.8). This is a clear empirical demonstration that the prompt strategy solves a real failure mode of SAM applied to coarse masks.

- **Consistent improvements across diverse supervision levels.** Tables 3 and 4 show substantial gains in both instance segmentation (e.g., +10.3 AP for PointWSSIS with 1% labels on COCO) and semantic segmentation (e.g., +9.5 mIoU for MaskCLIP on VOC). These are practically significant results in label-limited regimes where gains of this magnitude are rare.

- **Generality across architectures is well-supported.** Table 6 shows SAMRefiner improves mask quality on 7 different segmentation architectures (Mask R-CNN, PointRend, SOLO, CondInst, Mask2Former, etc.) with consistently positive margins (e.g., +5.5 AP on Mask R-CNN RN50, +6.7 AP on SOLO). This is the strongest evidence for the claimed generality.

- **Computational efficiency is a genuine advantage.** SAMRefiner refines COCO train5K in 0.6h compared to 3.4h for CascadePSP and 1.4h for SegRefiner (Table 5), because SAM can batch-process multiple masks per image. This is a practically important differentiator.

- **STM pipeline enables SAM to handle multi-object semantic masks.** Table 2c shows STM improves MaskCLIP mIoU from 51.1 to 57.3 (+6.2), demonstrating that a non-trivial engineering adaptation was needed to make SAM work in the semantic segmentation setting.

## Weaknesses

### Fatal
None.

### Major

- **Overclaiming "generic" superiority without analyzing failure cases.** The paper states that "SAMRefiner is more generic and can improve performance remarkably on various datasets" (Sec. 4.4). However, Table 5 shows SAMRefiner underperforms SegRefiner on 2 of 8 benchmarks: VOC MaskCLIP (57.3 vs. 58.5) and DeepLabV2 (78.8 vs. 83.1). On DeepLabV2, SAMRefiner (78.8) is also beaten by CRM (81.6) and CascadePSP (81.2) — placing it 4th out of 6 methods. The paper's sole explanation ("SegRefiner's performance is not stable across different settings") is insufficient and does not address why SAMRefiner itself struggles on high-quality input masks (DeepLabV2 baseline is 76.5). The paper would be stronger by acknowledging this pattern and analyzing when SAMRefiner is and is not the best choice (e.g., does the CEBox expansion degrade tight, high-quality masks rather than help them?).

### Minor

- **IoU adaptation (SAMRefiner++) is under-evaluated.** This component is only evaluated on DAVIS-585 (Table 1), where gains are modest (86.9→87.1 IoU, albeit with a meaningful 44.1→63.8 top-1 acc). It is not applied in the main comparisons (Tables 3–6), so its practical contribution to the framework's overall performance is unmeasured. At minimum, one additional dataset (e.g., COCO or VOC) should be tested to establish generalization.

- **Hyperparameter sensitivity is not examined.** CEBox uses fixed parameters (similarity threshold 0.5, λ=0.1, maximum expanding pixels per iteration) and the Gaussian-style mask uses ω=15, γ=4. The paper states "detailed analysis" is in the appendix (which is stripped here), but the main paper contains no ablation of these parameters across different mask qualities or dataset characteristics. A method claimed to be "universal" should demonstrate that its heuristics are robust or provide guidance for tuning.

- **The DeepLabV2 result in Table 5 is under-explained.** SAMRefiner's 78.8 on VOC DeepLabV2 is only +2.3 over the 76.5 coarse mask, while both CRM (+5.1) and SegRefiner (+6.6) do substantially better. This is the worst relative performance of SAMRefiner across all benchmarks. The paper does not discuss why — is this case (high-quality initial masks from a trained model) a regime where SAMRefiner's prompting strategy adds little value?

### Trivial

- The time comparison (Table 5) is informative but the conditions differ: CRF runs with 16 workers while others use one 3090 GPU. This should be noted explicitly.

## Nice-to-Haves

- A full factorial ablation of all three prompt types across all three major datasets (DAVIS, COCO, VOC) rather than distributing component ablations across different datasets (point on DAVIS, CEBox on COCO, STM on VOC).
- An analysis of the gap between the best of three SAM masks (selected by SAM's IoU head) and the oracle upper bound (selected by GT IoU) across different settings, to contextualize how much room for improvement remains.

## Removed Points

These points were flagged in the reviews but removed after cross-checking against the paper. Treat them with caution:

- *"The method relies on several heuristics whose robustness is unexamined"* — kept but demoted to minor (the appendix may contain the claimed analysis; the main paper should
  still include a summary).
- *"Missing limitations section"* — the paper has no such section, which is a common format choice and not a specific weakness.
- *"SegRefiner analysis: the claim that SegRefiner's performance is not stable is not supported"* — actually supported by SegRefiner scoring 80.3 vs. baseline 81.4 on DAVIS-585 (worse than doing nothing) and barely above baseline on COCO MaskRCNN. The critic's objection is partially wrong.
- *"Reproducibility: CEBox iteration details in appendix"* — standard practice; the paper gives the key parameters in the main text.
- Strength Finder's claim that SAMRefiner "outperforms all prior methods" across all benchmarks — over-simplified given the two VOC entries.
- Several formatting nitpicks from the harsh critic.
- Missing related works critique — I cannot verify which works exist.

## Novel Insights

None beyond the paper's own contributions. The reviews did surface one important observation not emphasized in the paper: SAMRefiner appears to be most valuable when coarse masks are noisy or incomplete (label-limited settings, DAVIS-585 masks with defects), but less effective when the coarse mask is already high-quality (DeepLabV2 at 76.5 mIoU). The paper frames universality as a strength, but the data suggest SAMRefiner is particularly well-suited for imperfect, low-quality inputs — a nuance the discussion should address directly.

## Suggestions

- Acknowledge the two VOC benchmarks where SAMRefiner underperforms SegRefiner and analyze the common pattern: both are cases with relatively high-quality initial masks from trained segmentation models. This would strengthen scientific honesty and help users understand when to apply SAMRefiner.
- Add at least one more dataset evaluation for the IoU adaptation (SAMRefiner++) to demonstrate it generalizes beyond DAVIS-585.
- Include a brief parameter sensitivity analysis (even 2–3 configurations) for CEBox thresholds and Gaussian mask parameters, or reference and summarize the appendix analysis in the main paper.
- The DeepLabV2 result (78.8 vs. 83.1 SegRefiner) warrants a dedicated sentence or two of discussion. Why does SAMRefiner improve by only +2.3 here while SegRefiner improves by +6.6?

---

## Calibration Anchors

**Round 1 — Bracketing (broad bands on SAM/mask refinement topics)**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/L1BXvqwsMv.md | 2.50 | R1 | Weak SAM adaptation paper — clearly below SAMRefiner |
| /home/wg25r/review_agent/human_reviews/OM1R87YLTc.md | 2.00 | R1 | Unrelated, very weak — below SAMRefiner |
| /home/wg25r/review_agent/human_reviews/EQAHilKZ8D.md | 2.20 | R1 | Weak — below SAMRefiner |
| /home/wg25r/review_agent/human_reviews/BUDLe7NIjQ.md | 4.50 | R1 | MaskSAM (medical SAM adaptation), withdrawn. Narrower evaluation, less clearly motivated — below SAMRefiner |
| /home/wg25r/review_agent/human_reviews/Pq2yEKXOl7.md | 4.50 | R1 | SlotSAM, withdrawn. Compares unfavorably on evaluation breadth — below SAMRefiner |
| /home/wg25r/review_agent/human_reviews/i1bBVKRVb5.md | 4.25 | R1 | Mask Frozen-DETR, withdrawn. Narrower scope — below SAMRefiner |
| /home/wg25r/review_agent/human_reviews/Ha6RTeWMd0.md | 9.00 | R1 | SAM 2 — clearly stronger, a foundation model paper at a different level |
| /home/wg25r/review_agent/human_reviews/IRcv4yFX6z.md | 8.00 | R1 | Hierarchical segmentation — stronger paper |

**Round 1 bracket: between ~3.5 and ~7.5** (SAMRefiner is clearly above the weak-reject papers, clearly below SAM-2-level papers).

**Round 2 — Narrowing within bracket**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/vRgMxGmEz9.md | 5.00 | R2 | SAM-guided UDA 3D, withdrawn. SAMRefiner has broader evaluation and clearer contribution |
| /home/wg25r/review_agent/human_reviews/vh1e2WJfZp.md | 6.00 | R2 | DiffDIS, accepted poster. Comparable quality — both have clear method and strong results; SAMRefiner has broader evaluation but some overclaiming |
| /home/wg25r/review_agent/human_reviews/dmzM5UdAq6.md | 5.75 | R2 | PRO-SCALE, accepted poster. Similar quality — both have clear contributions and thorough experiments |
| /home/wg25r/review_agent/human_reviews/hbN3pu5mUg.md | 5.25 | R2 | LISA, withdrawn. SAMRefiner is stronger |
| /home/wg25r/review_agent/human_reviews/IdAyXxBud7.md | 6.33 | R2 | DynAlign, accepted poster. Comparable quality |
| /home/wg25r/review_agent/human_reviews/YNbLUGDAX5.md | 6.00 | R2 | ProPETL, accepted poster. Comparable quality |
| /home/wg25r/review_agent/human_reviews/J9Vwp7TiE5.md | 6.00 | R2 | SegGen, rejected despite 6.0 average. SAMRefiner is slightly stronger |

**Final score determination**: SAMRefiner is comparable to the 6.0 accepted-poster papers (DiffDIS, PRO-SCALE) and clearly above the ~4.5 withdrawn papers. Its main weaknesses (modest overclaiming, under-evaluated IoU adaptation, missing hyperparameter sensitivity) are addressable and do not undermine the core contribution. The paper sits solidly at the acceptance threshold for a poster-level paper.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>