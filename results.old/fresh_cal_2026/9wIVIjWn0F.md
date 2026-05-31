Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes RTA, a regression-based test-time adaptation method for CLIP. The key insight is that using ground-truth label cross-entropy loss for view selection ("Ceiling TTA") dramatically outperforms entropy-based selection. RTA trains a lightweight LightGBM decision tree on pseudo-labeled diverse data once, learning a mapping from augmented-view logits to predicted cross-entropy loss. At test time, the tree is used to select the top-k views with the smallest predicted loss for ensemble prediction without any online updates. Experiments across 16 benchmarks (single-label, multi-label, cross-domain) show RTA outperforming existing entropy-based TTA methods.

## Strengths

1. **Compelling ceiling experiment and empirical finding.** Tables 1–2 convincingly demonstrate that using ground-truth label cross-entropy loss (LCE) for view selection achieves near-saturating performance far above entropy-based selection (e.g., ViT-B/16 on ImageNet-A: LCE 90.2% with 64 views vs. SE 64.3%). This observation is well-motivated and provides a clear upper-bound reference for the field.

2. **Strong and comprehensive empirical evaluation.** RTA is evaluated across 16 diverse benchmarks spanning single-label (Table 3, 5 ImageNet variants), multi-label (Tables 5–6, 3 datasets), and cross-domain (Table 4, 10 datasets) settings, with two backbone architectures (RN50, ViT-B/16). It consistently outperforms existing methods including Zero, BCA, TDA, and ML-TTA, often by non-trivial margins (e.g., +1.67% mAP on MSCOCO RN50 over ML-TTA, +5.73% on IN-A RN50 over DiffTPT).

3. **Practical "train-once, deploy-anywhere" paradigm.** The regression model is trained once offline on diverse pseudo-labeled data and applied at test time without any per-instance optimization, memory banks, or parameter updates. This is in contrast to methods like TPT/DiffTPT that require per-instance prompt tuning or cache-based methods like TDA that maintain evolving memory. The LightGBM model (depth=5, 16 leaves, 1000 training samples) adds negligible inference cost.

4. **Rigorous analysis of the regression relationship.** The paper provides t-SNE visualizations (Figure 2) showing structural correlation between logits and loss, and Spearman's rank correlation analysis (Figure 3) confirming monotonic relationships. The ablation on number of regression samples (Figure 5) provides practical guidance.

## Weaknesses

### Major

1. **Missing comparison against direct max-softmax-probability selection.** The regression target in Equation 4 is `-log(softmax(pseudo_label_class))` — by construction, `-log(p_max)` where `p_max` is the maximum softmax probability. This quantity can be computed in closed form at test time from the logits of each augmented view without any regression training. The paper compares only against entropy-based baselines, never against the simpler baseline of selecting views by the smallest `-log(p_max)` (equivalently, highest softmax confidence). Without this comparison, it is impossible to determine whether the learned regression model adds any value beyond the deterministic closed-form computation. This is the paper's most significant oversight.

2. **Necessity of the regression model is not demonstrated.** Related to point 1, the paper provides no evaluation of the regression model's predictive accuracy — e.g., correlation (MSE or Spearman) between the tree's predicted loss and the actual pseudo-loss on held-out test views. Such an analysis would establish whether the tree captures meaningful signal beyond what is already available via direct computation. Combined with the missing max-probability baseline, the core claim that regression adds value over closed-form computation remains unsubstantiated.

### Minor

3. **Multi-label formulation is underspecified.** The paper reports multi-label results (Tables 5–6) but never explains how the regression target is constructed for multi-label data — e.g., per-class losses averaged or summed, or whether the pseudo-label is defined per class or as a single joint prediction. This omission affects reproducibility of the multi-label results.

4. **No variance or significance reporting.** The main tables (Tables 3–6) report only point estimates. Given that many gains are modest (e.g., +0.23% on IN-R for ViT-B/16, +0.66% on OOD Average for ViT-B/16), confidence intervals or multiple-run statistics are needed to assess whether improvements are statistically significant.

### Trivial

None.

## Nice-to-Haves

- An ablation study comparing RTA against directly computing `-log(p_max)` from softmax to select views would cleanly separate the value of the regression mechanism from the value of the pseudo-label-target formulation.
- Adding a small set of variance bars (e.g., 3 runs) for key comparisons would strengthen the reliability claims.

## Removed Points

- **"Unfair comparison: RTA uses additional data that baselines do not use"** — This criticism misunderstands the paper's paradigm. RTA's "train once on diverse data, deploy anywhere" is a fundamentally different approach from per-instance optimization methods. The comparison against entropy-based TTA methods is valid as a comparison of two different TTA paradigms. What is missing (and covered in Major Weakness 1) is a controlled ablation against direct closed-form computation, not against per-instance baselines on the same data budget. REMOVED: The reviewer framed this as an unfair comparison, but the paradigms differ by design; the concern is better captured by the missing ablation against direct `-log(p_max)` computation.

- **"Regression decision tree is circular / unnecessary"** (from Strengthening section) — Partially preserved in Major Weaknesses 1–2 but the framing as "circular" is too strong. The regression tree COULD learn a different function if trained on different targets (e.g., if pseudo-labels are noisy). The core issue is the missing comparison, not circularity per se. REMOVED: tone softened into the two Major Weaknesses above.

- **Strengths about "addressing an important problem"** — Generic. REMOVED.

- **Criticism about "pseudo-label generation is underspecified"** — The paper states it uses "high-confidence samples" (Section 4.2). The process is described with sufficient clarity for the single-label case. REMOVED.

## Novel Insights

None beyond the paper's own contributions. The reviewers do not surface any cross-paper pattern or meta-observation that goes beyond what the authors already state.

## Suggestions

1. **Directly compare against max-probability view selection** — Replace the regression model at test time with `argmax over views of -log(max(softmax(logits)))`. If RTA outperforms this, the regression model provides genuine value; if not, the claimed novelty needs reframing.
2. **Report regression model accuracy** — Add a simple Spearman correlation or MSE plot between the tree's predicted loss and the actual pseudo-loss on a held-out set of views, to establish that the tree learns something beyond a trivial approximation.
3. **Clarify the multi-label formulation** — State explicitly how the regression target (Equation 4) is extended to multi-label: per-class binary CE averaged, or a multi-label loss formulation.
4. **Add variance estimates** — Report standard deviations over 3 runs for key comparisons.

## Score and Decision

My round-1 bracketing placed this paper between 4 and 6 based on calibration anchors. Round-2 anchoring against papers in the same sub-area confirmed the comparison:

- **FGA (5.00, Accept Poster)**: Novel flatness-guided TTA with theoretical backing but theory concerns. Current paper has stronger empirical breadth but weaker methodological novelty. Comparable quality overall.
- **ADTE (4.50, Accept Poster)**: Simple entropy replacement with incremental novelty. Current paper has a more ambitious claim but a more fundamental methodological gap. Slightly stronger empirically.
- **CLIP-TTA (4.67, Reject)**: Incremental dual-regularization over CLIP-OT. Current paper's missing baseline is a more serious concern than CLIP-TTA's incrementality, but the empirical evidence is broader.
- **PEA (5.50, Accept Poster)**: Clean backprop-free TTA with solid motivation and broad experiments. Current paper has comparable empirical breadth but a less clean methodological story.

The paper has strong empirical contributions and an interesting ceiling finding, but the methodological contribution is weakened by the missing comparison against the closed-form `-log(p_max)` computation. This gap is significant enough to prevent a high score but the overall empirical package supports a borderline accept.

Score: **5.0**, Decision: **Accept (Poster)** — contingent on the authors convincingly addressing the max-probability baseline concern in the rebuttal or camera-ready version.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>