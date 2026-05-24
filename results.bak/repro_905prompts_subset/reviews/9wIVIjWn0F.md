Now I have everything I need. Let me compose the final consolidated review.

## Summary of Calibration

**Round 1 bracket**: The paper is between weak (scores 2-3.5) and strong (scores 7.5+) anchors, most likely in the 4-7 range.

**Round 2 narrowing**: Compared against anchors at similar quality levels:
- BaFTA (5.50, Reject) — conceptually sound backprop-free TTA, incremental but clean
- DOTA (6.00, Reject) — sound distributional estimation concept, experimental concerns
- ROSITA (4.67, Reject) — incremental, some methodological issues
- ML-TTA (6.25, Accept) — clear contribution with BEM

RTA has stronger and more consistent empirical results than BaFTA/ROSITA, but a more fundamental conceptual flaw than any of these anchors. The regression target being a deterministic function of the logits is not merely an incremental concern — it directly undermines the paper's framing. I place it below BaFTA (5.50) and DOTA (6.00), settling at **5.0**.

---

## Final Review

## Summary

This paper proposes Regression-based Test-time Adaptation (RTA) for vision-language models (CLIP). The core idea is to train a decision tree (LightGBM) to map a view's logits to the cross-entropy loss with respect to the pseudo-label (the argmax class), then use this regression model at test time to select low-loss augmented views for ensembling. Experiments across single-label, multi-label, and cross-domain benchmarks show RTA outperforming existing entropy-based TTA methods.

## Strengths

- **Consistent and broad empirical improvements.** RTA outperforms prior TTA methods (TPT, DiffTPT, TDA, Zero, BCA, ML-TTA) across many benchmarks and two CLIP backbones (RN50, ViT-B/16). On ImageNet-A with ViT-B/16, RTA reaches 65.65% vs. 64.03% for Zero; on multi-label MSCOCO, 58.95% mAP vs. 57.52% for ML-TTA. These gains hold across 10 cross-domain datasets, demonstrating robustness.

- **Lightweight and practical design.** The decision tree (max_depth=5, n_leaves=16) is trained once on 1,000 pseudo-labeled samples and applied without per-instance updates, making it computationally negligible at test time. This contrasts favorably with methods requiring online optimization or dynamic memory banks.

- **Clear ceiling analysis.** Tables 1-2 convincingly demonstrate that using true-label cross-entropy loss (LCE) for view selection yields dramatic gains over entropy-based selection (SE) — e.g., ViT-B/16 on ImageNet-A: 90.2% (LCE) vs. 64.3% (SE) with 64 views. This provides a strong motivation for approximating this criterion.

## Weaknesses

### Major

1. **The regression target is a deterministic function of the logits, making the learned model theoretically unnecessary.** The pseudo-label is the argmax class (the class with highest softmax probability, filtered by confidence ≥ 0.8). Equation (4) computes the cross-entropy loss w.r.t. this pseudo-label: −log(softmaxₗ(logits)), which is simply −log(softmax_max(logits)). This is a fixed algebraic transformation of the input logits — it has nothing to do with "diverse unlabeled data," distribution shift, or any property of the training set. A decision tree trained to approximate this function can be replaced by the exact computation at no meaningful extra cost (softmax over L classes is O(L), the same operation already required to produce the logits). The paper's framing as discovering a "structural relationship" and obtaining a "free lunch" from diverse data is misleading: the relationship is the softmax function itself, and any single labeled example would suffice to determine it.

2. **Missing critical baseline: direct max-softmax view selection.** The paper compares RTA only against entropy-based methods (TPT, Zero, etc.), never against the simplest baseline: select views with the highest softmax probability (equivalently, lowest −log(softmax_max)) computed directly from the logits without any regression model. Since the regression target approximates exactly this quantity, any gains reported over entropy-based methods could be entirely due to the scoring criterion (max-softmax vs. entropy) rather than the regression model. Without this control, the experiments cannot attribute the improvements to the proposed framework.

3. **Overclaimed cross-distribution generalization.** The paper states that RTA "only needs to be trained once on diverse unlabeled data and adapts to any test distribution without updates." However, the regression model is instance-level: it takes the current view's logits and outputs a scalar. The mapping it learns is distribution-independent (it's the softmax function, which applies equally regardless of the input distribution). The "diversity" of training data is irrelevant to the target function, and the contrast with "methods that rely solely on the probability distribution of a single test instance" is incoherent — RTA also operates on one instance's logits at a time.

### Minor

4. **The t-SNE and Spearman analyses (Figures 2-3) do not demonstrate non-trivial structure.** The t-SNE shows that logits cluster by loss value, which is expected because the loss is a continuous function of the logits. The Spearman correlations between individual logit dimensions and the loss are of limited relevance since the loss depends on the full vector. These analyses do not reveal any information beyond the known softmax computation.

5. **No analysis of the regression model's approximation error.** The paper does not report how accurately the decision tree approximates the target (e.g., MSE between tree predictions and exact −log(softmax_max) on held-out data), nor whether approximation errors correlate with downstream task performance. This makes it impossible to assess whether the tree adds noise or bias, or whether using the exact value would change results.

### Trivial

None.

## Nice-to-Haves

- Compare against direct max-softmax selection (lowest −log(max(softmax))) to isolate whether the gains come from the regression model or the different scoring criterion.
- Report the decision tree's approximation error (MSE) on held-out data as a sanity check.
- Train the regression model on non-ImageNet data or without the 0.8 confidence filter to test robustness to the training distribution.

## Removed Points

- **"The regression mapping is a deterministic function" framing as fatal.** This point is elevated to Major and addressed above in Weakness #1. It is not fatal because the empirical results are real and the approach of using max-softmax for view selection has practical value even if the regression model is theoretically unnecessary. However, the paper's framing is incorrect and would need major revision.

- **Criticism about missing related works.** Removed per protocol — I cannot verify the existence of missing references.

- **Formatting/style nitpicks, reproducibility concerns about undisclosed hyperparameters.** Removed per protocol — the paper provides sufficient implementation details for reproducibility (LightGBM with max_depth=5, n_leaves=16, lr=0.01, etc.).

## Novel Insights

The paper's genuine empirical finding — that selecting views based on max-softmax confidence (whether computed directly or approximated) consistently outperforms entropy-based selection across many benchmarks — is interesting and practically useful. However, this is not recognized by the paper's own framing, which attributes the gains to a "regression model learned from diverse data." The fundamental insight the paper should have drawn is that for CLIP-based TTA view selection, the criterion matters more than the complexity of the selection mechanism, and max-softmax is a better criterion than entropy. This reframing would significantly strengthen the paper.

## Suggestions

1. **Reframe the contribution.** Acknowledge that the regression target is −log(softmax_max(logits)), which can be computed exactly. Explain why an approximate tree might still be preferable (e.g., computational efficiency for very large L, regularization/smoothing of noisy logits, or software/hardware constraints on softmax). Compare against exact max-softmax selection empirically to substantiate any claimed advantage.

2. **Add the missing baseline.** Compare RTA against selecting views with the smallest directly-computed −log(softmax_max(logits)). If performance is similar, the paper's value shifts to demonstrating that max-softmax > entropy for view selection, not that regression helps. If RTA outperforms exact computation, analyze why (e.g., the tree provides beneficial regularization).

3. **Tone down generalization claims.** Remove or qualify statements about "training once on diverse data" and "adapting to arbitrary distributions." The mapping is distribution-independent, and the data diversity claim is irrelevant to the learned function.

4. **Add approximation error analysis.** Report the decision tree's MSE on held-out data across each test dataset to verify the approximation quality and assess whether errors correlate with performance degradation.

## Score and Decision

**Round 1 bracket**: The paper sits between weak anchors (scores 2–3.5) and strong anchors (7.5+), with initial bracket of [4, 7].

**Round 2 anchors used for narrowing**:

| Anchor | Score | Decision | Comparison |
|--------|-------|----------|------------|
| RLCF (kIP0duasBb) | 6.67 | Accept | Stronger — has a clear methodological contribution (RL-based CLIP reward) without the conceptual issue |
| DOTA (yD2JMeKumt) | 6.00 | Reject | Stronger conceptually — distribution estimation is sound even if experiments have concerns |
| ML-TTA (75PhjtbBdr) | 6.25 | Accept | Stronger — BEM is a clear contribution for multi-label TTA |
| BaFTA (KNtcoAM5Gy) | 5.50 | Reject | Comparable — both have empirical strengths and conceptual concerns, but BaFTA's approach is not fundamentally flawed |
| ROSITA (lF9QXpfNHm) | 4.67 | Reject | Weaker methodologically, but ROSITA addresses a genuinely novel problem setting |
| TTVD (5sU32OCxgZ) | 6.00 | Accept | Sound geometric contribution with solid experiments |

**Final calibration**: RTA has unusually strong and broad empirical results for a paper in this score range, which is a genuine strength. However, the conceptual issue (regression target being a deterministic function of the logits) is more fundamental than the weaknesses identified in BaFTA (5.50) or DOTA (6.00). The missing baseline (direct max-softmax selection) prevents attribution of the reported gains to the proposed framework. The paper is below the acceptance threshold (~6.0) but not a weak paper — the empirical discovery that max-softmax outperforms entropy for view selection has real value, even if the current framing is flawed.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>