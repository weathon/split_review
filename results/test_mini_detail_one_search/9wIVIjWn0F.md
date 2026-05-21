Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes Regression-based Test-time Adaptation (RTA), a method that trains a LightGBM regression tree on pseudo-labeled ImageNet data to predict view-level cross-entropy loss from CLIP logits. At test time, it selects the top-k augmented views with the smallest predicted loss for ensemble classification, bypassing entropy-based selection. Experiments across single-label (ImageNet variants, 10 cross-domain datasets) and multi-label benchmarks (MSCOCO, VOC2007, NUSWIDE) show consistent improvements over prior TTA methods.

## Strengths

- **Ceiling TTA experiments validate the core premise.** Tables 1–2 show that view selection using ground-truth label cross-entropy (LCE) dramatically outperforms entropy-based selection across all ImageNet variants and both backbones (e.g., +19.0% on IN-1k, +25.9% on IN-A for ViT-B/16 with 64 views). This clearly demonstrates that a regression-based view-selection signal is promising and motivates the approach concretely.

- **Competitive or SOTA results across a broad evaluation suite.** RTA outperforms prior entropy-based methods (Zero, BCA, ML-TTA, etc.) on most datasets. On ImageNet variants (Table 3) it achieves the best average accuracy (66.90% for ViT-B/16); on multi-label datasets (Tables 5–6) it surpasses ML-TTA on all three benchmarks (e.g., 58.95% vs. 57.52% mAP on MSCOCO). The evaluation is extensive, covering single-label, cross-domain, and multi-label settings with two backbones.

- **Single training session that transfers across distributions.** The regression model is trained once on 1,000 pseudo-labeled samples from ImageVal-12k and applied directly to all downstream tasks without retraining or online updates. The cross-domain results (68.70% average on 10 diverse datasets, Table 4) provide concrete evidence that this pre-trained mapping transfers effectively.

- **Supporting analyses (t-SNE, Spearman correlation, ablations) strengthen the narrative.** Figure 2 shows clear logits-loss structural correlations, Figure 3 quantifies monotonic relationships, and Figures 4–5 demonstrate robustness to the number of views and regression samples.

## Weaknesses

### Major

- **The paper does not explain how the regression tree handles datasets with different numbers of classes — a critical omission that undermines reproducibility.** The LightGBM regression tree is trained on 1000-dimensional logit vectors (from ImageVal-12k, which uses ImageNet's 1000 classes). Algorithm 1 computes logits for *L* classes where *L* = 1000. At test time, Algorithm 2 also states "for *j* = 1, …, *L* do" but does not specify what class set *L* refers to. Downstream datasets have different numbers of classes: Pets (37), Aircraft (100), MSCOCO (80), VOC2007 (20), etc. A decision tree trained on 1000 features cannot accept inputs with a different dimensionality without modification. The paper provides no mechanism (e.g., always using ImageNet class prompts for tree features while reserving downstream class prompts for final classification) and no discussion of this issue. This omission directly affects the validity of all cross-domain (Table 4) and multi-label (Tables 5–6) results. *Evidence: Section 4.2, Algorithms 1–2; Section 5.1 Implementation Details.*

### Minor

- **The large gap between the Ceiling TTA (ground-truth LCE) and RTA's actual performance is not discussed.** For ViT-B/16 on IN-A, Ceiling TTA reaches 90.2% while RTA achieves only 65.65% — a gap of 24.6 points. On IN-R the gap is 13.4 points (94.4% vs. 81.05%). While some gap is expected when replacing ground-truth labels with a learned proxy, this magnitude is large and the paper offers no analysis of where the regression model errs, whether pseudo-label noise is the bottleneck, or how the gap might be reduced. The paper's "key finding" claim that "lower loss consistently indicates more accurate predictions across all distributions" is undercut by this gap since the regression predictions are far from the true lower-loss signal.

- **The composition and overlap of the regression set ("ImageVal-12k") with the ImageNet-1k test set is not clarified.** The paper samples 1,000 high-confidence pseudo-labeled examples from ImageVal-12k as training data for the regression tree, while ImageNet-1k (the standard validation set) is used as a test benchmark. If ImageVal-12k is a subset of the ImageNet validation set and the 1,000 training samples overlap with the 50k test images, this would constitute data leakage that inflates IN-1k results. The paper should clarify whether the regression and test samples are disjoint.

- **No ablation on the confidence threshold (0.8) used to filter pseudo-labels.** The regression model is trained only on samples with CLIP confidence ≥ 0.8, but at test time it is applied to all views — including low-confidence ones where the distribution of logits may differ substantially. The paper does not analyze sensitivity to this threshold.

- **Runtime comparison with baselines is absent despite the claim of "negligible additional cost."** Generating 64 augmented views, running CLIP on each, and predicting loss via LightGBM adds computational overhead. No wall-clock times or throughput measurements are provided to substantiate the "negligible" claim.

### Trivial

None.

## Nice-to-Haves

- The paper would benefit from an analysis of where the regression model's predictions diverge from true LCE — e.g., by categorizing failure cases by pseudo-label correctness, view quality, or class type.
- Investigating whether the confidence threshold (0.8) trades off regression accuracy vs. training data quantity could help practitioners.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The method only applies to benchmarks with the same class set as ImageNet"** — This is too strong. A plausible workaround exists (always using ImageNet class prompts for tree features), and the paper's omission is that it doesn't specify this. The criticism as framed asserts a fatal flaw that cannot be definitively confirmed from the paper alone.
- **"Potential data leakage... weakens the claim of learning a distribution-agnostic mapping"** — The leakage concern is valid but the conclusion about the "distribution-agnostic" claim is overstated. The method still applies across diverse datasets (cross-domain, multi-label) where no overlap exists.
- **Harsh critic's "Critical Issues" section framing the dimensionality mismatch as structural/fatal** — Moved to Major weakness instead. The issue is real and significant, but there are plausible resolutions (fixed 1000-dim ImageNet features for tree inference + downstream class logits for final classification) that the paper simply fails to document.
- **Strength Finder's generic/superficial characterizations** — Claims such as "This directly demonstrates a strong and useful regression relationship" that lack specific citations to concrete passages are removed.
- **"The paper does not specify how the regression tree is applied to datasets with different numbers of classes. This is the most important missing detail."** — Absorbed into the Major weakness above.
- **Missing appendix/proof references** — Removed per hard rule (parser strips appendices; they exist in the original submission).
- **Formatting/style nitpicks** — Removed per hard rule.
- **Missing related work** — Removed per hard rule (cannot verify existence of missing citations from external knowledge).

## Novel Insights

None beyond the paper's own contributions. The core observation (logits have a predictable relationship with cross-entropy loss) is the paper's main insight, and the reviews do not surface any independent novel understanding that the authors missed.

## Suggestions

1. **Clarify the dimensionality handling.** Explicitly state whether the test-time logit features fed into the regression tree are always computed using the ImageNet-1000 class prompts (with each dataset's own class names used only for the final ensemble classification). If a different approach is used, describe it fully.
2. **Disclose regression-test overlap.** Report whether the 1,000 regression samples from ImageVal-12k are disjoint from the 50k ImageNet-1k test set. If they are not, re-run without overlap or quantify the leakage.
3. **Analyze the ceiling gap.** Add a brief analysis or ablation showing why the predicted regression loss diverges from true LCE — e.g., by comparing predictions on high- vs. low-confidence pseudo-labeled views.
4. **Add runtime numbers.** Report wall-clock time or throughput for RTA vs. a baseline method (e.g., Zero) to substantiate the "negligible additional cost" claim.
5. **Ablate the confidence threshold.** Show how varying the threshold (0.7, 0.8, 0.9) affects both the quantity of usable training data and downstream accuracy.

## Score and Decision

**Calibration anchors (all from DeepReview 13k):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `kIP0duasBb.md` (RLCF) | 6.67 | Solid TTA paper with novel idea, accepted. Current paper has more extensive benchmarks but a more significant methodological omission. |
| `75PhjtbBdr.md` (ML-TTA) | 6.25 | Multi-label TTA, accepted. Similar strength of empirical results but current paper's unspecified dimensionality handling is a bigger gap. |
| `yD2JMeKumt.md` (DOTA) | 6.00 | Rejected despite 6.0 due to multiple significant issues. Current paper has fewer issues but one comparably serious omission. |
| `TPZRq4FALB.md` (READ) | 8.00 | Very strong TTA paper with clean methodology. Current paper is well below this tier. |
| `pdzHpQbGrn.md` (Active TTA) | 2.50 | Weak paper with limited novelty. Current paper is substantially stronger. |
| `Rc3RP9OoEJ.md` (InCPL) | 5.00 | Mid-range TTA paper. Comparable quality; current paper has more innovative core idea but less clarity. |

The paper makes a genuinely interesting contribution (regression-based view selection for TTA, replacing entropy) and provides extensive experiments. However, the failure to specify how the regression tree handles variable-dimensionality logits across datasets is a serious omission that affects the reproducibility of all cross-domain and multi-label results. This prevents acceptance in the current form, though the issue is addressable and the core contribution has merit.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>