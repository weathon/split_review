## Summary
The paper proposes **Regression-based Test-Time Adaptation (RTA)** for CLIP-based image classification. The central observation ("Ceiling TTA") is that selecting augmented views by their ground-truth cross-entropy loss (LCE) yields massive accuracy gains over entropy-based selection. Building on this, the authors train a LightGBM regression tree offline on 1,000 pseudo-labeled samples from a diverse dataset (ImageVal-12k) to predict the pseudo cross-entropy loss from CLIP logits. At test time, views with the smallest predicted loss are selected and ensembled. Experiments cover single-label, cross-domain, and multi-label benchmarks with RN50 and ViT-B/16 backbones, consistently outperforming entropy-based TTA baselines.

---

## Strengths

- **Compelling motivating analysis:** The Ceiling TTA experiment (Tables 1–2) is clearly presented and revealing. With 64 augmented views and ViT-B/16, LCE-based selection reaches 90.2% on ImageNet-A vs. 64.3% with entropy—a 25.9-point gap. This decisively motivates the regression approach and is a genuine empirical insight.

- **Elegance and practicality:** Training once offline on a small, domain-agnostic dataset and applying to any downstream distribution is architecturally clean. The contrast with memory/cache-based methods (which must continuously adapt and can fail under large distribution shifts) is well-articulated.

- **Broad empirical coverage:** Results span 5 ImageNet-variant benchmarks, 10 cross-domain datasets, and 3 multi-label datasets across two architectures—far broader than most TTA papers. RTA leads or ties on almost all metrics.

- **Good structural evidence for the regression relationship:** t-SNE visualization (Figure 2) and Spearman correlation analysis (Figure 3) provide tangible evidence that CLIP logits carry structural information about correctness, justifying a regression approach over a purely entropy-based one.

---

## Weaknesses

### Fatal
None.

### Major

1. **Dimensionality mismatch in cross-domain evaluation is unexplained.** The regression model is trained with logit vectors of dimension *L* = 1,000 (ImageNet classes). On cross-domain datasets such as Cars (*L* = 196), Aircraft (*L* = 100), or Flowers (*L* = 102), the logit dimensionality differs. LightGBM is index-based; a model trained on 1,000 features cannot straightforwardly process 196-feature vectors. The paper never addresses this—it claims the method is "independent of any downstream classification task" but provides no mechanism for handling variable-length inputs. If the logit dimension is always fixed at 1,000 (using ImageNet classes throughout), this would invalidate the cross-domain results as a genuine domain-agnostic evaluation. This is the single most critical gap.

2. **Absence of a critical simple baseline: max softmax probability.** Shannon entropy and log-max-probability are monotone transforms of each other for the peaked region of the simplex, but are distinct in general. The paper should compare against selecting views by maximum softmax confidence (argmax probability), which is the obvious proxy for LCE without true labels. Without this baseline, it is unclear whether the LightGBM regression adds value over the simplest possible confidence score. If max-probability already closes a large fraction of the LCE–entropy gap, the regression component is not well-justified.

### Minor

1. **Potential distribution overlap between regression training data and test sets.** ImageVal-12k is derived from ImageNet, and testing is also performed on ImageNet-1k. Even with pseudo-labels, the regression model observes CLIP's logit patterns on ImageNet samples, which may provide an unfair advantage over methods that use no ImageNet data for adaptation. A sensitivity analysis using a non-ImageNet regression set (e.g., LAION samples) would be informative.

2. **Scalability to very large class sets is unclear.** The regression model's feature dimension scales with L. For fine-grained or retrieval tasks with thousands of classes, training cost and inference cost of computing all L text embeddings would be substantial. A brief discussion of this limit is missing.

### Trivial

- The notation inconsistency in Equations 8–10, which refers to test logits as `s^{x_i^{reg}}` instead of `s^{x_i^{test}}`, is confusing.

---

## Nice-to-Haves
- Comparison using RTA as a plug-in to strengthen existing cache-based methods (TDA, BCA) rather than replacing them, to demonstrate composability.
- Error bar / variance report across multiple runs (random augmentation view selection may have non-trivial variance).
- Analysis of regression tree feature importances to reveal which logit dimensions (classes) drive the prediction, potentially offering interpretability insights about CLIP's internal structure.

---

## Novel Insights
The core novel insight is that CLIP's logit vector, even without access to the true label, encodes reliable structural information about whether the current augmented view will be correctly classified—and that this information is stable enough across diverse distributions to be captured by a single, small, offline-trained regression model. This reframes confident view selection from a per-instance, entropy-based problem into a distributional learning problem solved once and reused everywhere. The Ceiling TTA analysis quantifying the entropy-vs-LCE gap at different view counts is independently useful as a diagnostic for future TTA research.

---

## Suggestions
- Explicitly explain how the regression model handles different class counts across datasets; if needed, describe how LightGBM's missing-value routing is used, or provide a rank-based feature preprocessing step.
- Add the max-softmax-probability selection baseline in Table 3 to isolate the benefit of the learned regression vs. direct confidence thresholding.
- Provide at least one ablation where the regression training set comes from a non-ImageNet source to demonstrate true distribution independence.

---

## Score and Decision

The paper identifies a genuine and underexplored phenomenon (logit-to-loss regression as a view selection criterion), supports it with comprehensive experiments, and delivers a practically simple system. However, the unexplained dimensionality mismatch in the core cross-domain experiment is a significant methodological gap that could undermine confidence in those results. The missing max-probability baseline also leaves the regression contribution insufficiently isolated. These are correctable issues but important enough to warrant revision before acceptance.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>