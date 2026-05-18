Now I have all the information I need. Let me compile the final consolidated review.

---

## Summary

This paper introduces ν-ensembles, a method that improves deep ensemble calibration in the small-data regime by assigning random labels (sampled without replacement across ensemble members) to unlabeled data. The method is extremely simple: each ensemble member fits the labeled training set plus an unlabeled set with a distinct randomly chosen label per point. The paper provides a PAC-Bayes bound (Theorem 1) connecting test NLL to average member NLL and ensemble diversity on unlabeled data, and empirically evaluates calibration improvements on CIFAR-10/100 with training sets of 1K–40K samples.

## Strengths

- **Extremely simple and computationally efficient**: The method requires no hyperparameter tuning, no complex training loops, and no joint training of ensemble members. It maintains the same per-member training cost as standard deep ensembles. This is a genuine differentiator from prior diversity-promoting methods (Masegosa 2020 requires two gradient evaluations per step; Agree to Disagree requires greedy sequential training).

- **PAC-Bayes bound provides useful theoretical framing**: Theorem 1 formally connects test NLL to average training NLL minus a diversity term (empirical variance on unlabeled data) plus a complexity penalty. While the bound is generic (not specific to the random labeling procedure), it motivates why increasing diversity on unlabeled data without hurting labeled-set performance can improve test calibration.

- **Consistent calibration improvements claimed across architectures and datasets**: The paper reports that ν-ensembles match standard ensemble accuracy while improving calibration (ECE, TACE, Brier reliability, NLL) for training set sizes up to 10K on CIFAR-10/100, across LeNet, MLP, and WideResNet22 architectures. The text provides specific numbers for OOD experiments (ECE improvement from 10% to 15% for ResNet22 under high-intensity corruptions).

- **OOD robustness**: The method maintains its calibration advantage under common image corruptions across all severity levels, while retaining the same accuracy as standard ensembles.

- **Theoretical and empirical comparison of sampling with/without replacement**: Proposition 2 derives expected diversity under with-replacement sampling, and the paper confirms experimentally that without-replacement (the recommended variant) yields better calibration.

## Weaknesses

### Major

- **Experimental confound between extra data and diversity mechanism**: In the experimental setup, ν-ensembles train on Z_train ∪ U (where U is 5000 unlabeled points with random labels), while standard ensembles train on Z_train alone. This means ν-ensembles effectively train on substantially more data (up to 6× in the smallest Z_train case). The paper does not disentangle whether the calibration improvement comes from the *diversity* of different random labels per member or simply from having more training data (even with noisy labels). A controlled baseline — e.g., standard ensemble members each trained on Z_train ∪ U with the *same* random label per unlabeled point for all members — is needed to isolate the diversity effect. Without this, the central empirical claim that the specific random-labeling-per-member mechanism drives the improvement is not fully supported.

### Minor

- **Theoretical claim is overstated relative to what is proven**: The abstract states the PAC-Bayes bound "guarantees that for such a labeling we obtain low negative log-likelihood and high ensemble diversity." However, Theorem 1 is a generic PAC-Bayes bound that holds for *any* ensemble, regardless of how it was trained. It does not specifically reference the random labeling procedure. The bound provides motivation — showing that increasing diversity can lower an upper bound on test NLL — but it does not constitute a guarantee about the specific method. The paper would benefit from reframing this claim more accurately.

- **No uncertainty quantification in experimental results**: The paper does not report standard deviations, confidence intervals, or the number of random seeds used for any experiment. Given that the method's primary claimed benefit is numerical (improvements in calibration metrics like ECE, NLL, etc.), the absence of any measure of variability makes it impossible to assess whether the reported improvements are statistically significant or consistent across runs.

- **Unexplored dependency between ensemble size and number of classes**: For CIFAR-10 with K=10 ensemble members and c=10 classes, sampling without replacement assigns each class exactly once per unlabeled point across the ensemble. For CIFAR-100 with c=100 but K=10, the behavior is very different. The paper does not discuss how the relationship between K and c affects the diversity mechanism, nor does it explore varying K.

### Trivial

- **Proposition 2 assumes perfect fitting of random labels**: The analysis of expected diversity under with-replacement sampling assumes each ensemble member perfectly fits its assigned random labels. This is an unrealistic assumption, especially in the small-data regime with rich architectures. The paper partially compensates with empirical validation, but the theoretical analysis would benefit from acknowledging this gap.

## Nice-to-Haves

- A small controlled experiment varying the size of U relative to Z_train to show the transition where the method stops helping and starts hurting.
- A self-training or consistency-regularization baseline using the same unlabeled set U, to benchmark against a more standard semi-supervised approach.
- Discussion of what happens when U comes from a genuinely different distribution (true OOD unlabeled data).

## Removed Points

- **"Results cannot be verified because Table 1/Figures are not rendered"**: The images are present in the original PDF submission but not renderable by the text parser. This is a format artifact, not a paper flaw.
- **"Proposition 1 is not stated"**: Proposition 1 (the without-replacement case) was likely in the appendix, which is stripped by the parser. It is referenced in the text ("Comparing numerically propositions 1 and 2").
- **Criticisms about missing proofs in appendix**: The parser strips appendices; these exist in the original submission.
- **Various formatting/style nitpicks and complaints about parser-level text garbling**: These do not reflect author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine experimental confound that the paper itself does not discuss, but the core idea (using different random labels per ensemble member on unlabeled data) is clearly presented and the simplicity argument is well-made.

## Suggestions

1. **Resolve the confound**: Add a baseline where a standard ensemble is trained on Z_train ∪ U, with all members receiving the *same* randomly sampled label per unlabeled point (or a fixed label). If ν-ensembles still outperform this baseline, the diversity mechanism is doing real work beyond the extra data.

2. **Reframe theoretical claims**: Replace "guarantees" with language like "motivates" or "provides an upper bound showing that...". Explicitly acknowledge that the bound applies to any ensemble and that the connection to the specific labeling procedure requires showing the trade-off works in practice.

3. **Add error bars**: Report results over at least 3–5 random seeds with standard deviations, at least for the main result (Table 1).

4. **Discuss the K vs. c relationship**: Explain what happens when K < c, K = c, and K > c, and justify the choice K=10.

## Score and Decision

The paper presents a genuinely simple and interesting idea that could be practically useful. However, the central empirical comparison contains a significant confound (ν-ensembles use more training data than standard ensembles), and the theoretical claims are stronger than what the analysis supports. The absence of any uncertainty quantification further weakens the evidence. These issues are addressable in a revision, but as presented, the paper does not convincingly demonstrate that the proposed mechanism — diverse random labeling per member — is responsible for the observed improvements.

**MY FINAL SCORE:** <pineapple>4.5</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>