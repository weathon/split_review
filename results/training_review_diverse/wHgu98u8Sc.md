Now I have thoroughly verified the reviewer claims against the paper. Let me construct the consolidated review.

---

## Summary

This paper introduces ν-ensembles, a method that improves deep ensemble calibration in the small-data regime by assigning *different random labels* from an unlabeled set to each ensemble member, then training each member on the combined labeled and randomly-labeled data. The method is refreshingly simple (no architectural changes, no auxiliary losses, no joint training), adds negligible computational overhead over standard ensembles, and is shown to produce better-calibrated predictions across LeNet, MLP, and WideResNet22 architectures on CIFAR-10 and CIFAR-100 while maintaining accuracy.

## Strengths

- **Simple and practical method with clear calibration improvements.** Table 1 shows that ν-ensembles achieve substantially better calibration (e.g., ECE drops from ~10% to ~6% on CIFAR-10 with LeNet) across all architectures and both datasets, while maintaining the same accuracy as standard ensembles. The method adds no architectural changes, no auxiliary losses, and no joint training — only a single random-labeling pass on unlabeled data. This is a genuinely useful tool for practitioners.

- **Empirical confirmation of increased ensemble diversity.** The mutual information (MI) metric in Table 1 is consistently lower for ν-ensembles (e.g., 0.112 vs. 0.150 for LeNet on CIFAR-10), directly validating that the random-labeling strategy produces more diverse ensemble members. The calibration benefits are thus linked to a measurable and theoretically grounded property.

- **Robustness to distribution shift.** Figure 3 demonstrates that ν-ensembles retain and sometimes widen their calibration advantage under common corruptions (e.g., ECE improvement grows from ~10% to ~15% for ResNet22 at high corruption intensity), showing the benefit is not limited to in-distribution settings.

- **Computational efficiency compared to prior diversity-promoting methods.** ν-ensembles have O(1) memory scaling (sequential training) and only O(m) added computation for the unlabeled set, versus O(K) for Masegosa and Agree-to-Disagree ensembles that require joint or sequential member training. Figure 4 directly quantifies this advantage.

- **Theoretical analysis of sampling without replacement.** Proposition 2 analytically shows that sampling without replacement yields higher ensemble variance, and the paper provides empirical confirmation. This gives implementable guidance for practitioners.

## Weaknesses

### Fatal

None.

### Major

- **Data quantity confound undermines the mechanistic interpretation.** Each ν-ensemble member is trained on the labeled set *plus* 5000 unlabeled examples (with random labels), while each standard-ensemble member is trained on the labeled set alone (1000–40000 samples). A ν member therefore sees 6000 to 45000 training examples versus 1000 to 40000 for the standard ensemble. The paper attributes the calibration improvement to *diversity from different random labels across members*, but it does not control for the simpler hypothesis that adding any data (even with random labels) regularizes individual members and improves calibration. The critical control — a standard ensemble where every member is trained on labeled data plus the *same fixed random labeling* (shared across members) — is absent. Without this control, the empirical evidence does not distinguish the claimed diversity mechanism from a data-quantity effect. The with/without-replacement comparison in Section 5.3 partially addresses this (both conditions use the same data quantity with different label assignments), but the core comparison against standard ensembles remains confounded.

- **Theoretical disconnect between the PAC-Bayes bound and the algorithm.** Theorem 1 presents a bound where the variance term `V(ρ̂)` is computed on the unlabeled set *using true labels* (the sum runs over `y`). The ν-ensemble, however, trains on unlabeled data with *random* labels, not true labels. The paper never argues that training on random labels tends to increase `V(ρ̂)` on the true-label distribution, nor does it provide any empirical measurement of true-label variance. The bound therefore provides motivation at the wrong level of abstraction: it says "if you maximize variance on true labels you improve test NLL," but the method maximizes variance on *random* labels. Without a bridge connecting these, the theory does not justify the algorithm — it is a generic inequality with no demonstrated connection to the specific design choice. This is a structural weakness in the paper's scientific argument, not merely a missing detail.

### Minor

- **No error bars or multiple seeds.** All reported metrics (Table 1, Figures 2–3) are single-run point estimates without confidence intervals or standard deviations. In the small-data regime (1000–4000 training samples), stochasticity from data splits and initialization is high. While the consistency of the pattern across architectures and datasets provides some reassurance, a single run per configuration cannot establish significance, especially for the claimed 30–50% relative ECE reductions. This is an evidential gap that weakens confidence in the headline claims.

- **Unclear whether baselines had access to the same unlabeled data.** The paper compares ν-ensembles against Masegosa and Agree-to-Disagree ensembles but does not state whether those baselines also used the 5000 unlabeled examples. Agree-to-Disagree (Matteo et al., 2023) is described as forcing disagreement on unlabeled data, so it presumably does use them. For Masegosa, it is unclear. If the baselines did not use unlabeled data, the comparison is unfair: ν-ensembles benefit from extra data while the baselines do not. The paper should clarify this and, ideally, evaluate all methods with and without access to the same unlabeled set.

- **Reproducibility details are insufficient.** The paper states "AdamW" and "hyperparameter search with 50 trials" but does not list the search space, learning rate schedule, number of training epochs, or early-stopping criteria. A practitioner cannot reproduce the results from the information provided. Additionally, training details for baseline methods (Masegosa, Agree-to-Disagree) are not given.

- **The without-replacement empirical result is only summarised, not shown.** Section 5.3 states: "We confirm our prediction by redoing the experiments in Table 1, but this time sampling with replacement. On average, sampling without replacement results in better calibration across our different metrics." This result is not presented in a table or figure — only a single sentence. Given that this comparison directly supports the diversity mechanism (since data quantity is held constant), it deserves full tabular presentation.

- **No analysis of why the method fails in the large-data regime.** The limitations section (Section 6) honestly notes that the method "had a detrimental effect on calibration" in the large-data regime, but offers no analysis or hypothesis for why. This limits guidance for practitioners on when the method is appropriate.

### Trivial

- The failed DICE replication attempt is noted honestly (line 103) but without analysis of why it failed. This is not a weakness of the paper's method but could be addressed with a brief comment.

## Nice-to-Haves

- Measuring mutual information on the *unlabeled set* used during training (rather than the test set) would more directly connect the diversity-enforcement mechanism to the measured diversity.
- A small synthetic or toy experiment with known ground truth could isolate the diversity mechanism without confounds.
- Reporting the true-label variance `V(ρ̂)` on a held-out labeled set for both standard and ν-ensembles would help bridge the theory-practice gap.

## Removed Points

*"The function h in the bound is never specified; the bound is therefore not checkable."* — The paper explicitly states "h: ℝ⁺ → ℝ⁺ is a strictly increasing function" (line 77). This is a standard PAC-Bayes formulation where h is a generic function that exists by the theory; it is not left undefined. Removed as factually incorrect.

*"The validation set's role is never explained."* — The paper states it uses "5000 samples as validation data Z_val" (line 95) and that hyperparameter search used 50 trials (line 99). While not exhaustively detailed, the validation set's role in tuning is clearly stated. Removed as a misreading.

*"Section 5.3: Proposition 2 assumes each model perfectly fits its random labels, which is unrealistic."* — This is a standard theoretical simplification for an analytical proposition. The paper then validates the trend empirically. Removed as a generic nitpick that misjudges the role of theory.

*"Missing appendix / missing proofs / missing references"* — Parser artifacts; removed per instructions.

*"DICE replication failure not analysed"* — The paper honestly reports the attempt and correspondence with the authors. This is a disclosure, not a weakness. Removed per instruction to avoid penalizing honest reporting.

## Novel Insights

The most valuable observation from these reviews is the concrete suggestion to control for data quantity by comparing ν-ensembles against standard ensembles trained on labeled data *plus the same unlabeled set with a single fixed random labeling shared across members*. This experiment cleanly separates the two hypotheses — "more data per member" versus "diverse labels per member" — and the paper's central claim stands or falls on it. The reviews also highlight that the with/without-replacement comparison (which the paper already runs but under-reports) is in fact a more powerful control than the paper currently treats it as, because it holds data quantity constant while varying label diversity. Recasting this experiment as the primary evidence for the diversity mechanism would strengthen the paper significantly.

## Suggestions

1. **Add the control experiment**: Standard ensemble where each member trains on labeled data plus the same 5000 unlabeled samples with a *single fixed random labeling* (shared across all members). If ν-ensembles still outperform this baseline, the diversity mechanism is isolated.
2. **Report means and standard deviations** over at least 3–5 independent runs (different data splits and random seeds) for all metrics. The patterns are consistent enough that significance likely holds, but it must be shown.
3. **Present the without-replacement vs. with-replacement comparison as a full table**, not a single sentence. This is the cleanest evidence for the diversity mechanism.
4. **Bridge the theory-practice gap**: measure `V(ρ̂)` (computed with true labels) on a held-out set for both standard and ν-ensembles to empirically verify that random-label training increases true-label variance.
5. **Clarify the baseline setup**: explicitly state whether Masegosa and Agree-to-Disagree baselines had access to the same unlabeled set, and if so, describe how they were adapted.
6. **Provide full hyperparameter search spaces** and training details (epochs, learning rate schedule, early stopping) for all methods.

## Score and Decision

This paper proposes a genuinely simple and practical method that delivers clear calibration improvements with minimal overhead. The strengths are real: the method is easy to implement, the empirical improvements are consistent across architectures and datasets, and the computational cost is negligible. However, the experimental design confounds data quantity with label diversity for the central comparison, and the theoretical framework does not connect to the algorithm in a substantive way. These are not fatal — the method empirically works — but they weaken the paper's scientific argument about *why* it works. The contributions are sufficient for acceptance at a conference that values practical empirical methods, but the paper would benefit substantially from addressing the control experiment and error bars before publication.

**Score**: 6.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>