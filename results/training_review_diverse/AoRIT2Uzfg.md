Now I have all the information needed to verify the reviewer claims against the actual paper text. Let me compose the final consolidated review.

---

## Summary

This paper proposes DRMGuard, the first backdoor defense framework for deep regression models (DRMs) in the image domain. It identifies a unique feature-space property of backdoored DRMs — that the angles between feature vectors and weight vectors are highly concentrated (low RAV) — and exploits it to reverse-engineer potential trigger functions without enumerating target vectors in the continuous output space. Experiments on gaze estimation and head pose estimation tasks across four datasets and four backdoor attacks show strong identification accuracy and mitigation performance.

## Strengths

- **Novel identification and exploitation of a feature-space characteristic unique to backdoored DRMs.** The paper theoretically derives (via Equation 3 and the inner-product structure of regression outputs) and empirically validates that backdoor inputs induce highly concentrated angles between feature vectors and weight vectors (RAV < 0.1 across all 8 attack–dataset combinations in Table 1). This property is absent in classification models and is used as a regularization term (Equation 4) that enables reverse engineering in continuous output spaces.

- **Principled formulation of reverse engineering for continuous output spaces.** Unlike classification defenses that enumerate over discrete classes, DRMGuard directly minimizes the variance of output components across poisoned inputs (first term of Equation 4). This avoids the intractable enumeration problem posed by regression's infinite target space. The approach achieves AUC=1.000 on all four attacks (Table 3), significantly outperforming adapted NC (0.379) and FeatureRE (0.599).

- **Strong and comprehensive empirical results.** Across four datasets and four attack types, DRMGuard achieves 95% identification accuracy on MPIIFaceGaze (Table 1) and 87.5% average accuracy across datasets (Table 2). For mitigation, it substantially reduces DAE (from ~15 to ~3) while raising AE, outperforming four adapted classification defenses (Tables 4–5).

- **Ablation studies confirm that every component is necessary.** Removing either the feature-space regularization term (FSRT) or the momentum reverse trigger (MTR) collapses accuracy to 50% (Table 8). This validates the design choices and confirms the claimed differences from classification-model defenses.

- **Adaptive attack analysis strengthens the core claim.** An attacker that explicitly targets the RAV property (Equation 8) still cannot bypass detection (95% accuracy; Table 9), because breaking the angle concentration weakens the backdoor itself (AE jumps from 1.51 to 5.71). This demonstrates a fundamental coupling between the observed feature-space property and effective backdoor attacks.

## Weaknesses

### Major

- **The momentum reverse trigger (MTR) — a critical component — is insufficiently specified.** The ablation study shows MTR is essential (without it, all benign models are misclassified as backdoored), yet the paper provides only an intuitive sketch: "assign different weights to different regions to balance the attention of the DRM on the image." The actual computation of the attention map, how momentum is incorporated, and how it modifies the generator's optimization are absent from the compiled paper. (The brief mention of gradient-based attention maps appears to be in a LaTeX comment that would not appear in the compiled PDF.) This prevents reproduction of the method.

- **The adaptation of classification-based baselines (Neural Cleanse, FeatureRE) to regression is described too briefly to assess fairness.** The paper states they are generalized "by taking the potential target vector $y_t$ as the optimization variable" (Section 4). Neural Cleanse's detection statistic (outlier detection on per-class trigger norms) and FeatureRE's feature-space constraint are designed around discrete label structure. Treating $y_t$ as a continuous optimization variable changes the behavior of these methods substantially. Without specifying the exact loss functions, optimization objectives, and detection procedures used for these adapted baselines, the reported AUC scores (e.g., NC: 0.270 for BadNets, FeatureRE: 0.730) cannot be fully attributed to the original methods' capabilities or limitations. This is important because the paper's claim of outperformance depends on this comparison.

### Minor

- **The identification threshold $\epsilon=0.03$ is set without justification or sensitivity analysis.** The binary decision rule (Equation 6) depends on this threshold, yet no analysis is provided on how $\epsilon$ was chosen, whether it was tuned, or how it generalizes across datasets with different resolutions or trigger sizes. While the ROC-AUC metric is threshold-independent and softens this concern, the TP/FP/FN/TN counts in the tables all depend on $\epsilon$.

- **Small sample sizes without confidence intervals.** Experiments use 10 benign + 10 backdoored models per setting. While this is common in the literature, reporting confidence intervals or running more seeds would improve reliability, especially for the perfect AUC=1.000 scores where 20 data points make the metric less informative than it appears.

- **Multiple backdoor results are claimed but not shown with data.** The paper mentions that DRMGuard is effective on models with multiple trigger functions (Section 4.2), but only provides a single sentence without any quantitative results. If detailed results appeared in a truncated appendix, this is understandable, but the main paper would benefit from at least a summary table.

### Trivial

- The paper frames the RAV observation as an empirical finding rather than a proven necessary condition for all backdoor attacks. This is appropriate for an empirical paper; the adaptive attack analysis already partially addresses the concern by showing that breaking RAV weakens the backdoor.

## Nice-to-Haves

- A runtime/computational cost comparison with adapted baselines would be useful, since reverse engineering involves iterative optimization.
- A discussion of whether low RAV is a necessary condition for *all* effective backdoor attacks on DRMs (beyond the four tested) would strengthen the theoretical framing, though the adaptive attack already provides evidence.

## Removed Points

- **Criticism about "no formal proof that *any* successful backdoor attack must produce low RAV":** The paper presents this as an empirical observation (Section 3.3: "Observations"), not a theorem. Asking for a formal proof misaligns with the paper's empirical scope. The adaptive attack already provides supporting evidence. Moved from weaknesses.

- **Criticism about missing appendix content or multiple backdoor details:** The reviewer acknowledges the appendix may have been truncated. The paper's single-sentence mention in the main text is thin, but this is noted in Minor weaknesses above. The stronger "no details are available" framing is removed per the rule about appendix stripping.

- **Criticism about "the paper should also cover additional tasks/datasets":** The paper already covers two regression tasks and four datasets — a reasonable scope for a single paper. Demands for broader coverage would constitute scope creep.

- **Criticism about the paper not discussing computational cost:** A nice-to-have, not a weakness that affects the core claims.

## Novel Insights

The key insight that synthesizes the reviews is that the paper's core contribution — identifying the angle-concentration (low RAV) property of backdoored DRMs — is its strongest asset and also creates its main vulnerability. The RAV property is what enables the defense, but it is also what makes the baseline adaptation and MTR specification essential: without knowing exactly how the baselines were adapted, the reader cannot tell whether their poor performance reflects a genuine limitation of those methods or a flawed re-implementation; without knowing exactly how MTR works, the reader cannot tell whether it is a genuinely novel mechanism or a re-packaged existing technique. Both specification gaps must be closed before the contribution is fully verifiable.

## Suggestions

1. **Specify the momentum reverse trigger completely.** Provide the exact formula for the attention map (e.g., based on input gradients of $f$), the momentum update rule, and how the weighted perturbation is combined with the generator's output. Include a figure or pseudocode.

2. **Fully specify the baseline adaptations.** Write out the exact optimization objectives and detection procedures used for NC and FeatureRE when applied to regression. Show that these are faithful adaptations (or acknowledge where approximations were necessary and justify them).

3. **Add a sensitivity analysis for $\epsilon$.** Report identification accuracy (or precision-recall curves) over a range of $\epsilon$ values on a held-out validation set, or justify the chosen value theoretically.

4. **Report confidence intervals** on the main identification and mitigation results, or increase the number of seed runs per setting.

## Score and Decision

The paper addresses a genuine and important gap — backdoor defense for deep regression models — and provides a clever, empirically grounded solution. The core idea (exploiting feature-space angle concentration) is novel and well-supported by theoretical derivation and experiments. However, two specification gaps prevent the contribution from being fully verifiable: the momentum reverse trigger (the paper's own method component) and the baseline adaptations (the comparison) are both described at a level too vague for reproduction or fair assessment. These are addressable in revision but are significant as-is.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>