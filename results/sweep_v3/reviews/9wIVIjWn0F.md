Here is my consolidated final review.

---

## Summary

This paper proposes Regression-based Test-Time Adaptation (RTA) for CLIP-based image classification. The core idea is to train a LightGBM regression model (offline, on pseudo-labeled ImageNet data) that maps a view's logit vector to a scalar cross-entropy loss, then at test time uses the regressor to select the lowest-loss augmented views for ensembling, replacing the entropy-based selection used in prior TTA methods. Experiments cover single-label ImageNet variants, 10 cross-domain datasets, and three multi-label benchmarks.

---

## Strengths

1. **Ceiling TTA experiments convincingly motivate the approach.** Tables 1 and 2 show that selecting views by ground-truth label cross-entropy loss (LCE) yields massive gains over entropy-based selection (e.g., 82.4% vs 61.7% on ImageNet-1k with RN50 and 32 views). This clean oracle experiment provides a strong motivation for learning a regression mapping that approximates LCE.

2. **Broad and consistent empirical evaluation.** The paper evaluates RTA across single-label (ImageNet variants), cross-domain (10 datasets), and multi-label (3 datasets) benchmarks, for two architectures (RN50 and ViT-B/16). Results consistently show RTA matching or exceeding prior methods, often by non-trivial margins (e.g., +1.62% on ImageNet-A, +1.43% on MSCOCO mAP over the previous best).

3. **Algorithmic simplicity.** RTA avoids complex test-time adaptation machinery (prompt updates, diffusion, reward models) and instead uses a lightweight LightGBM tree trained once offline. This is a practical advantage that the paper correctly identifies.

4. **Sensitivity analysis.** Figure 5 shows the effect of training data size on performance, and Figure 4 shows saturation with enough views, which helps practitioners understand the method's stability.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unspecified label-space dimensionality alignment (undermines all cross-dataset results).** This is the most serious issue and must be resolved for the paper to be evaluable. The regression model is trained on logit vectors of dimensionality equal to the number of classes in the regression set (ImageVal-12k, 1000 ImageNet classes). At test time, the algorithm (Algorithm 2, line 6, with `L` defined in Eq.(1) as "the number of labels in the test set") uses the test dataset's own class labels, producing logit vectors whose dimensionality equals the *test dataset's* class count — e.g., 100 for Aircraft, 47 for DTD, 80 for MSCOCO. A LightGBM model trained on fixed 1000-dimensional features **cannot accept inputs of different dimensionality**. The paper provides no mechanism (padding, feature selection, separate regressors per dataset, or consistent use of the 1000-class ImageNet vocabulary) to resolve this mismatch. As written, the experimental results in Tables 3–6 are not reproducible from the described procedure.  
   *This is verifiable directly from Eqs.(1), (8) and Algorithm 2.*

2. **Multi-label formulation is completely undefined.** Tables 5 and 6 report multi-label mAP results, but the paper never specifies: (a) how the single-label cross-entropy loss of Eq.(4) (trained on ImageNet's single-label data) relates to the multi-label setting, (b) what logit dimensionality is fed to the regressor when the test dataset has 80 (MSCOCO) or 20 (VOC2007) classes vs 1000 at training, (c) what loss target is used during regression training for multi-label scenarios. This makes the multi-label results unverifiable.

3. **No-adaptation control is missing.** RTA does no per-instance model adaptation — it only selects and ensembles views. Most baselines (TPT, DiffTPT, RLCF, TDA) *update model parameters or prompts* during test-time, which is strictly more expensive and introduces different failure modes (error accumulation). The paper includes Zero as a non-adaptive baseline, which partially addresses this. However, a cleaner control would compare regression-based selection vs. entropy-based selection *both without any adaptation* (apart from Zero's built-in mechanism), to isolate the benefit of the regression mapping over entropy. The reported gains could partially reflect that RTA avoids adaptation pitfalls rather than the superiority of the learned selector. The paper should include an ablation that applies the regression selector on top of an adaptive method.

### Minor

1. **Pseudo-label circularity concern.** The regression model is trained on pseudo-labels derived from CLIP's own predictions (confidence ≥ 0.8). The target it learns is the CE loss w.r.t. those pseudo-labels — a transformed version of CLIP's confidence. The paper does not directly show that the regressor's predicted loss correlates *more strongly* with true LCE than entropy does. The Spearman correlation (Figure 3) is on the raw logits vs. LCE, not on the regressor's predictions. Adding a scatter plot of predicted loss vs. true LCE on a held-out set across distributions would strengthen the motivation.

2. **Pseudo-label threshold at 0.8 filters hard examples.** The regression model is trained only on easy, high-confidence samples. Its behavior on hard test examples (where CLIP's confidence is low) is not validated. An analysis of predicted loss vs. true loss on low-confidence held-out samples would help.

3. **Gains are modest on some benchmarks.** On ImageNet-1k with ViT-B/16 (Table 3), RTA improves over Zero by only 0.24% (71.13% vs 70.89%). On several cross-domain datasets (Table 4), RTA is comparable to or slightly behind BCA. Statistical significance (confidence intervals, multiple seeds) is not reported, so it is unclear whether these small margins are reproducible.

4. **"Free lunch" claim is overstated.** Training the regression model requires computing CLIP logits for thousands of samples across all 1000 classes with prompt templates, which is a non-trivial one-time cost. The paper correctly notes this is a one-time cost, but calling it a "free lunch" is misleading.

### Trivial
- Eq.(8) has a subscript typo: it uses `x_i^{reg}` where the context and algorithm clearly intend `x_i^{test}`.
- The notation in Eq.(8)–(10) uses `reg` superscripts for test-time variables, creating confusion.

---

## Nice-to-Haves
- An analysis of how the regressor's feature importance (which logits matter most) changes across different test distributions would provide insight into what the regression mapping actually learns.
- A direct comparison of computational cost (inference time, FLOPs) between RTA and each baseline.

---

## Removed Points
These points were raised but are not retained as valid weaknesses:

- **"Regression model is trained on only 1000 samples; scaling behavior suggests data-hunger"** — The paper acknowledges this and Figure 5 shows that even 1000 samples suffice for strong performance, with diminishing returns from more data. This is not a weakness.
- **"The paper should include a neural network regressor baseline"** — The choice of LightGBM vs. a neural network is an engineering decision. The paper shows the approach works with a simple tree model; a different regressor choice would not change the method's validity.
- **"Pure nitpicks about the RTA falling into test-time augmentation rather than adaptation"** — RTA is clearly evaluated in the same framework as prior TTA methods (TPT, Zero, etc.), and the paper compares fairly against them.
- **"Missing related work"** — Not verifiable; the reviewer has no external source to confirm miss.
- **"Should compare RTA against entropy-only without any adaptation"** — Zero is already a no-adaptation entropy baseline in the comparisons. This is partially addressed.
- **"Statistical significance not reported"** — This is field-normative for large-scale CLIP TTA benchmarks; single-run evaluation is standard practice. Retained as a minor concern above but would not by itself affect the score.
- **Various formatting/typography complaints** — Parser artifacts, not author errors.

---

## Novel Insights
None beyond the paper's own contributions. The reviews surface the label-space dimensionality issue as the primary weakness — a genuinely important technical gap that was not identified in the paper's own discussion of limitations. The pseudo-label circularity concern is secondary but worth noting.

---

## Suggestions

1. **Clarify the label-space mechanism explicitly.** State whether the regressor always receives 1000-dimensional logits (using ImageNet's class prompts even for non-ImageNet datasets), or whether separate regressors are trained per dataset, or whether a dimensionality-reduction/alignment technique is used. If the first option applies (always using 1000-class ImageNet logits), explain what pseudo-label / loss target is used during training and how the predicted loss at test time relates to the actual task. This clarification is essential for the paper to be reproducible.

2. **Define the multi-label formulation.** Specify how CE loss is computed for multi-label data, how the regressor is trained (or adapted) for it, and how logit dimensionality is handled when the multi-label dataset has 80 classes vs. the regressor's 1000-class training.

3. **Add a head-to-head comparison** between regression-based selection and entropy-based selection in identical conditions (no adaptation, same number of views, same CLIP backbone). Include a version where the regression selector is plugged into an adaptive method (e.g., replace entropy selection in Zero with RTA's selector).

4. **Show direct correlation** between predicted loss and true LCE on a held-out set across multiple distributions, alongside the correlation between entropy and true LCE, to demonstrate that the regression model adds value beyond a reparameterization of entropy.

---

## Score and Decision

**Calibration anchors** (all from the deepreview_13k corpus, TTA/CLIP-related):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| TPZRq4FALB.md (Multi-modal TTA, Accept) | 8.00 | Far stronger: clear problem definition, new benchmarks, technically sound. Current paper is well below this. |
| kIP0duasBb.md (CLIP reward TTA, Accept) | 6.67 | Stronger: clean method formulation, good evaluation. Current paper has a more serious clarity gap. |
| yD2JMeKumt.md (DOTA, Reject) | 6.00 | Somewhat comparable: both have unaddressed experimental clarity issues. DOTA was rejected despite the score. |
| z7PhIgVmZU.md (BAT-CLIP, Reject) | 5.50 | Current paper is slightly below: BAT-CLIP had a clearer (though flawed) methodology; RTA has a structural ambiguity. |
| FwkYeLovHk.md (Weak-to-strong for CLIP, Reject) | 3.33 | Current paper is above: more extensive experiments, more interesting core idea. |
| pdzHpQbGrn.md (Active TPT, Reject) | 2.50 | Current paper is well above: RTA has a more novel concept and much broader evaluation. |

Relative to these anchors, the paper has a genuinely interesting core idea and extensive experiments, but the unaddressed label-space dimensionality mismatch is a significant omission that prevents the results from being verified as presented. It is stronger than bottom-quartile papers but has a clarity gap that places it below the acceptance threshold.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>