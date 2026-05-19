- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 6, 8, 6, 6, 6
Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper introduces Intermediate Layer Classifiers (ILCs) — linear probes trained on intermediate layer representations of frozen DNNs — and shows that they consistently outperform the common practice of using penultimate-layer features for out-of-distribution (OOD) generalization. The study covers 9 datasets spanning subpopulation, corruption, and style shifts, uses both ResNet and ViT architectures, and considers few-shot (some OOD data for probe training) and zero-shot (only ID data for probe training, OOD data only for selection) settings. The authors also propose a sensitivity metric and provide evidence that intermediate layers are less sensitive to distribution shifts than the penultimate layer.

---

## Strengths

- **Large, consistent gains on subpopulation shifts, especially in the zero-shot setting.** Figure 5 shows that using only ID data for probe training, the best ILC improves worst-group accuracy over last-layer retraining by +7.7 pp (Waterbirds: 79.4%→87.1%), +26.0 pp (CelebA: 56.0%→82.0%), and +25.2 pp (MultiCelebA: 20.8%→46.0%). These are large margins on practically important benchmarks, and the zero-shot setting was not considered in prior last-layer retraining work.

- **Data-efficiency advantage when OOD samples are scarce.** Figure 4 shows that with a very small fraction of OOD data (π ≤ 0.03), ILCs outperform last-layer retraining by +5.7 pp (Waterbirds), +3.4 pp (CelebA), and +27.0 pp (MultiCelebA). The advantage is largest precisely when OOD data is hardest to obtain, which is a practically relevant finding.

- **Systematic evaluation across diverse shift types and architectures.** The paper tests 9 datasets (subpopulation, noise perturbation, style shifts) with both ResNets and ViTs. The few-shot results on CMNIST (+16.8 pp), CIFAR-10 (+6.3 pp) and MultiCelebA (+6.3 pp) with ResNets (Figure 3), and the zero-shot results on CIFAR-10C (+2–5 pp across models, Figure 6) demonstrate generality across conditions.

- **Introduction of a sensitivity metric that provides mechanistic evidence for subpopulation shifts.** Section 5.2 defines a normalized distance-ratio metric and shows that for minority groups on CelebA and MultiCelebA, intermediate layers have substantially lower sensitivity scores than the penultimate layer (Figure 9). This connects the empirical gains to a plausible explanation.

---

## Weaknesses

### Fatal
None. The paper's core empirical claims are supported by gains large enough (many >5 pp, several >20 pp) that they would not be plausibly explained by random variation alone.

### Major

1. **No uncertainty quantification across the entire empirical study.** All figures (3–8) report point estimates with no error bars, confidence intervals, or indication of variance. While many gains are large enough to be convincing (e.g., +26 pp on CelebA zero-shot), several reported improvements are small — ViT on CIFAR-100C (−0.2 pp in Fig. 3), ImageNet-A (+0.91 pp, Fig. 7), Waterbirds pen-penultimate vs. penultimate (0.1 pp, Fig. 8) — and without variance estimates the reader cannot assess whether these differences are meaningful. This weakens confidence in the more marginal results and makes it harder to evaluate the robustness of the overall trend.

2. **The sensitivity analysis (Section 5.2) is limited to subpopulation shifts only.** The paper claims that "intermediate layers are less sensitive to distribution shifts" as a general explanation for ILCs' success (stated in the abstract, contributions, and conclusion), but the analysis in Figure 9 only covers CelebA and MultiCelebA — both subpopulation shifts. The hypothesis is not validated for corruption shifts (CIFAR-10C/100C) or style shifts (ImageNet variants, cue-conflict, silhouette), where the paper also reports ILC improvements. This gap means the proposed mechanism remains plausible but untested for most of the paper's own experimental settings.

### Minor

1. **Training details for linear probes are completely absent.** The paper does not specify the optimizer, learning rate, number of epochs, weight decay, feature normalization, or any hyperparameter used to train the ILCs or the last-layer retraining baselines. While the central findings are unlikely to hinge on these choices, the omission prevents reproducibility and makes it impossible to assess whether results are sensitive to probe-training hyperparameters.

2. **The paper overstates the uniform superiority of intermediate layers.** Certain edge cases show flat or negative results: ViT on CIFAR-100C (−0.2 pp, Fig. 3), and ImageNet variants with gains under +1 pp (Fig. 7). The paper acknowledges these briefly but does not explore why intermediate layers fail in these cases (e.g., if the effect is architecture- or scale-dependent). These exceptions don't undermine the main findings but should be discussed more transparently.

3. **The method's hyperparameter sensitivity is not explored.** The layer selection procedure (choosing the best layer up to L-2 via OOD validation) introduces at least two free parameters — the fraction of OOD validation data used for selection, and the maximum layer index considered. The paper does not test whether the results are robust to these choices.

### Trivial
None.

---

## Nice-to-Haves

- Comparison with full-training robust methods (e.g., IRM, GDRO, deep feature reweighting) would contextualize the ILC approach against more expensive alternatives, though this is outside the paper's stated scope.
- Extending the sensitivity analysis to at least one corruption-style shift (e.g., CIFAR-10C) and one style shift (e.g., ImageNet-R) would substantially strengthen the paper's mechanistic claims.
- Code release would aid reproducibility.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"No code or data release commitment"** — Removed per hard rules: the paper cites publicly available models and datasets; questioning release status is not a valid criticism of the submission.
2. **"Sensitivity metric conflates variance and shift"** — Removed: the metric is a ratio dist(probe,test)/dist(probe,probe); scaling all distances in a layer by a constant factor leaves the ratio unchanged. The criticism does not hold.
3. **"Formatting artifact in sensitivity equation"** — Removed: this is a PDF-parser artifact, not an author error.
4. **"Base model comparison raises a question about whether original classifier weights are suboptimal"** — Removed: the paper explicitly states this is out of scope, and no evidence is available to assess the speculation.
5. **"The zero-shot setting is not fully unsupervised"** — Removed: the paper acknowledges this honestly and notes it is standard practice in the field (Gulrajani & Lopez-Paz, 2020; Sagawa et al., 2020a). Not a weakness of this paper.
6. **"Lack of comparison to alternative robust training methods (e.g., IRM, GDRO)"** — Demoted to Nice-to-Have: the paper studies probing frozen representations; requesting full training comparisons is scope creep.
7. **"Missing related works"** — Removed per hard rules: cannot independently verify existence of missing citations.

---

## Novel Insights

The harsh critic and strength finder together surface a tension that the paper itself does not address: the sensitivity analysis (Section 5.2) is positioned as an explanatory mechanism, but it is only tested on the two datasets where ILC gains are largest (CelebA, MultiCelebA). This creates a confounding loop — the mechanism is validated precisely where the effect is strongest, leaving open the question of whether the same mechanism explains the smaller gains on corruption and style shifts, or whether a different explanation is needed. A genuinely informative follow-up would show whether the sensitivity metric predicts ILC improvement across *all* shift types, or whether it only tracks improvements on subpopulation shifts where spurious correlations dominate. This could reveal whether intermediate-layer robustness is a general property or one specific to certain failure modes of deep learning.

---

## Suggestions

1. **Add uncertainty quantification.** Run each experiment at least 3 times with different random seeds for probe training and report mean ± std. This is the single highest-leverage fix.
2. **Extend the sensitivity analysis.** Apply the metric from Section 5.2 to at least one corruption-shift dataset (CIFAR-10C) and one style-shift dataset (e.g., ImageNet-R) to validate the proposed mechanism for the full range of settings where ILCs are claimed to work.
3. **Disclose training hyperparameters.** Report the optimizer, learning rate, number of epochs, regularization, and any normalization used for all linear probes.

---
