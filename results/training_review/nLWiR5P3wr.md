Now I have a thorough understanding of the paper and all reviewer claims. Let me compose the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions
## Score and Decision

Let me construct this carefully.

---

Let me verify one more thing about FoRDE-Identity vs DE on clean data, because the Strength Finder mentions FoRDE-Identity "outperforms baselines on clean data."

Looking at Table 1 (CIFAR-100):
- DE NLL: 0.70, Accuracy: 81.8
- FoRDE-Identity NLL: 0.70, Accuracy: 82.1
So FoRDE-Identity ties on NLL and is slightly better on accuracy.

Table 2 (CIFAR-10):
- DE NLL: 0.117, Accuracy: 96.3
- FoRDE-Identity NLL: 0.113, Accuracy: 96.3
So FoRDE-Identity has better NLL (0.113 vs 0.117) and same accuracy.

So FoRDE-Identity does show some clean-data benefits, just not corruption robustness benefits. This is consistent with what the paper reports.

OK, let me now write the final review.Now I have a complete understanding of the paper. Let me construct the final consolidated review.

## Summary

FoRDE proposes a particle-based variational inference (ParVI) method for deep ensembles that repels ensemble members in the space of their **first-order input gradients** (rather than weights or function outputs). To make this practical, the paper introduces a data-dependent RBF kernel whose per-dimension lengthscales are set to the inverse eigenvalues of the training-data PCA decomposition, encouraging members to diversify along high-variance input dimensions. Experiments on CIFAR-10/100-C and transfer learning show that the full method (FoRDE-PCA) improves corrupted accuracy by 1–2% over plain deep ensembles and other baselines.

## Strengths

1. **Well-motivated repulsion space with clear advantages.** The paper convincingly argues that input-gradient space is more tractable than weight space (lower dimension, no symmetry issues) and avoids the underfitting problem of function-space repulsion (lines 37–44). The 1D regression toy (Figure 2) visually confirms that gradient-space repulsion produces higher predictive uncertainty outside the training data, supporting the core intuition.

2. **Consistent empirical gains under covariate shift.** On CIFAR-10-C, FoRDE-PCA achieves 80.5% corrupted accuracy vs. 78.1% for deep ensembles and 78.2% for node-BNNs (Table 2). On CIFAR-100-C, FoRDE-PCA achieves 56.1% vs. 54.3% for DEs and 54.8% for node-BNNs (Table 1). These gains are consistent across datasets, across all three corruption metrics (cA, cNLL, cECE), and in the EmpCov-prior comparison (Table 3), where FoRDE-PCA still outperforms baselines *with* the EmpCov prior.

3. **Principled data-dependent kernel design.** The PCA-based lengthscale selection (Section 3.3) is theoretically grounded — setting inverse eigenvalues as squared lengthscales ensures stronger repulsion along high-variance data dimensions — and its connection to the EmpCov prior (lines 190–198) provides a coherent explanation for why the kernel improves corruption robustness. The ablation across three kernel variants (PCA, Identity, Tuned) systematically validates the design choice.

4. **Transfer learning and functional diversity validation.** Beyond classification benchmarks, the paper shows FoRDE outperforms baselines under a natural distribution shift (CINIC-10, Figure 5) and measures higher epistemic uncertainty on OOD data, providing evidence that input-gradient repulsion genuinely produces more functionally diverse ensembles.

## Weaknesses

### Fatal
None.

### Major

1. **Missing error bars on all corruption metrics across every table.** Tables 1–3 report cA, cNLL, and cECE as single numbers without standard deviations over seeds, despite stating results are "averaged over 5 seeds." The clean-data metrics (NLL, Accuracy, ECE) do include ±std notation. Since the paper's central claim — that FoRDE significantly outperforms baselines under covariate shift — rests entirely on these corruption numbers, the absence of variance estimates makes it impossible to assess whether the observed improvements (e.g., +1.3% on CIFAR-100-C, +2.4% on CIFAR-10-C) are statistically meaningful. This is the single most consequential reporting gap in the paper.

2. **Abstract claims of "significant" improvement are unsupported by the reported evidence.** The abstract states FoRDE "significantly outperforms the gold-standard DEs" under covariate shift. Without error bars on the corruption metrics (point 1 above), the claim of *statistical* significance cannot be verified from the paper itself. Qualifiers like "significantly" should be reserved for cases where variance is reported and a meaningful comparison can be made.

### Minor

1. **FoRDE-Identity does not improve over deep ensembles on corrupted data, clarifying the role of the kernel vs. the repulsion space.** The paper honestly reports this (line 337: "FoRDE-Identity is slightly less robust than DE against corruptions"), but the framing throughout emphasizes gradient-space repulsion as the key innovation (title, abstract, lines 7–11). Since FoRDE-Identity (gradient repulsion with identity lengthscales) yields essentially identical corruption accuracy to plain DEs (CIFAR-100: 54.1 vs. 54.3; CIFAR-10: 78.0 vs. 78.1), all corruption robustness gains are attributable to the PCA kernel design, not to the choice of repulsion space alone. The paper would benefit from a more precise disentanglement of these two contributions.

2. **The paper's central claim about outperforming DEs is specific to the PCA-kernel variant, not to the FoRDE framework generically.** While the paper presents the PCA kernel as part of FoRDE, the title "Input-gradient space particle inference" foregrounds the repulsion space. A reader could reasonably expect gradient-space repulsion itself to be the driver of improvements. The paper should more clearly state that the PCA kernel is the critical component for corruption robustness and that gradient-space repulsion alone (FoRDE-Identity) is comparable to DEs under shift.

### Trivial
None.

## Nice-to-Haves

- **An ablation applying the PCA-inspired lengthscale idea to other repulsion spaces** (e.g., function-space or feature-space repulsion with similarly data-dependent lengthscales) would more cleanly separate the effect of the repulsion space from the effect of the data-dependent kernel.
- **Reporting per-corruption-type breakdowns** (beyond the aggregate cA/cNLL/cECE) would help understand whether FoRDE-PCA benefits certain corruptions disproportionately, potentially revealing failure modes.
- **A simple visualization of input-gradient similarity between ensemble members** (e.g., pairwise cosine similarity matrices before and after FoRDE training) would provide direct mechanistic evidence for the claimed diversity.

## Removed Points

These points were flagged by reviewers but removed or reclassified as follows:

1. **"Unclear hyperparameter tuning for FoRDE-Tuned and potential data leakage"** — The paper states "Details on lengthscale tuning are presented in \cref{sec:tuning_lengthscales}" (line 324) and "Additional results on lengthscale tuning are presented in \cref{sec:tuning_lengthscales}" (line 339). These sections exist in the original submission (stripped by the parser). Speculating about test-set leakage without seeing the appendix is unfounded. **Removed per rule: do not penalize missing appendix content.**

2. **"Need for evaluation on non-synthetic distribution shift"** — The paper already evaluates on CINIC-10 (a natural distribution shift) in the transfer learning experiments (Figure 5, line 345). **Removed: the paper already addresses this.**

3. **"FoRDE-Identity performs worse than DE on corruptions" factual claim** — The difference is 54.1 vs. 54.3 on CIFAR-100-C and 78.0 vs. 78.1 on CIFAR-10-C, which is 0.1–0.2% — essentially a tie given the scale and the absence of error bars. Calling this "worse" is misleading. The paper's own description as "slightly less robust" (line 337) is more accurate. Reclassified to a minor note about the source of gains.

4. **"No quantitative diversity metrics for toy experiments"** — Toy experiments are qualitative illustrations; requesting quantitative metrics for illustrative 1D/2D figures is a scope stretch. Reclassified to nice-to-have at most.

5. **"Missing baselines" style criticisms (e.g., correlation study of input gradients)** — These are suggestions for deeper analysis, not weaknesses in what was presented. Moved to nice-to-haves.

## Novel Insights

None beyond the paper's own contributions. The reviewer discussions did not surface a genuinely novel interpretation of the method or results that extends beyond what the authors already articulate.

## Suggestions

1. **Report error bars (standard deviations over seeds) for cA, cNLL, and cECE in all tables.** This is the most impactful improvement the authors can make. Even if the error bars turn out to be small (as one might expect from 5-seed averages over 19×5=95 corruption settings), reporting them removes the central concern about statistical significance.

2. **Reframe the abstract and introduction to accurately reflect the roles of gradient-space repulsion and the PCA kernel.** Specifically: (a) clarify that gradient-space repulsion (FoRDE-Identity) provides clean-data benefits and functional diversity, while the PCA kernel is the key component driving corruption robustness; (b) remove the word "significantly" or add error bars to support it.

3. **Add a dedicated ablation comparing FoRDE-PCA to versions of other repulsive methods (weight-RDE, function-RDE, feature-RDE) augmented with an analogous data-dependent kernel.** This would resolve whether the PCA lengthscale idea is complementary to the repulsion space or whether it synergizes specifically with input-gradient repulsion.

## Score and Decision

The paper makes a genuine contribution: the idea of repelling ensemble members in input-gradient space is novel, well-motivated, and supported by empirical results that are consistent across datasets and metrics. The PCA-based kernel design is principled and its connection to the EmpCov prior provides useful theoretical grounding. However, the systematic omission of error bars on the core corruption metrics is a significant reporting gap that prevents rigorous evaluation of the paper's main claim. This is fixable in revision but weakens the current submission. The claim of "significant" outperformance is not properly supported. On balance, the paper has a solid core contribution and the most critical weakness is a reporting omission rather than a methodological flaw.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>