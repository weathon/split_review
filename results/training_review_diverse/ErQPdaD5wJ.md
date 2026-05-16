Now I have all the evidence I need. Let me write the consolidated review.

## Summary

This paper addresses hyper-parameter optimization and model selection for unsupervised anomaly detection (UAD), where no labeled validation data is available. It proposes three surrogate metrics — RTM, EAG (internal), and NPD (semi-internal) — that approximate expected test performance, and integrates them with Bayesian optimization. NPD, which measures the discrepancy between anomaly scores on a held-out validation set and a Gaussian-generated pseudo-anomaly set, is the paper's main contribution. Experiments on 38 datasets with four UAD methods show that NPD-guided search outperforms existing internal evaluation heuristics (EM/MV, MC, HITS) and random/default baselines.

## Strengths

- **Novel and well-motivated metric (NPD).** The idea of using an isotropic Gaussian as a proxy for unseen anomalies is clever and grounded in a simple argument: the Gaussian has higher entropy than the training data (Theorem 1), so it provides a diverse reference set without requiring real anomalies. NPD is hyper-parameter-free (unlike RTM and EAG which need a threshold), and its translation/scale invariance (Theorem 2b) makes it robust to arbitrary score scaling.

- **Strong empirical evidence across scale.** The benchmarking on 38 datasets with 4 UAD methods (one shallow, three deep) is substantial. Mean AUC and F1 results in Table 1 show NPD achieving the best or second-best performance across methods, with statistically significant gains over Random (p < .01 for OCSVM, AE, DPAD). The UOMS study (Table 2) further shows RTM and NPD outperforming consensus-based selection (MC, HITS) on a pool of up to 2,667 models.

- **Truly unsupervised operation.** Unlike meta-learning methods (Zhao et al., 2021, 2022) that require labeled historical datasets, AutoUAD works entirely with the training data alone. This is explicitly and honestly contrasted in the Related Work section.

- **Clear problem formulation.** The formalization of AutoUAD (Definition 2) with two explicit goals — (1) hyper-parameter optimization per method and (2) model selection across methods — gives the paper clean framing. The distinction between UAD (inductive, trained on normal data) and transductive outlier detection is appropriately scoped.

## Weaknesses

### Fatal

None.

### Major

- **Overstated Spearman correlation claim.** The paper states: "taking Figure 6 as an example, we see NPD consistently has a strict positive correlation with AUC and F1, where the Spearman rank coefficient is always 1" (lines 205–211). While the phrase "as an example" limits this to Figure 6, claiming perfect rank correlation (ρ = 1) within any real BO trajectory is an extraordinary assertion that the paper does not substantiate. No Spearman correlation coefficients are computed or reported across any other datasets or conditions. This single overstatement weakens the paper's credibility despite the aggregate results being positive. The authors should either retract this claim or back it with quantitative rank-correlation statistics across all 38 datasets.

### Minor

- **Unspecified validation split size M for NPD.** Definition 6 splits training data into X_trn (size N−M) and X_val (size M), but M (or the proportion) is never stated. This is a reproducibility gap: NPD's behavior (variance, sensitivity to the training/validation trade-off) depends on M. The authors should specify the value and ideally justify it or show robustness.

- **Theoretical analysis does not directly establish the surrogate claim.** The paper advertises "theoretical guarantees" (abstract, contribution list), but the theorems provide only peripheral support. Theorem 2 gives an upper bound on NPD in terms of score gaps, but an upper bound does not logically entail that maximizing NPD maximizes separation — the bound and the metric share the same denominator structure, so the direction of implication is unclear. Theorem 3 bounds KL divergence under GMM approximations but is never connected to why NPD should predict test AUC. The theoretical content is interesting background but is weaker than the "guarantee" framing suggests.

- **Statistical comparison only against Random, not among metrics.** The p-values in Table 1 compare each metric against Random. The lone p-value* column compares NPD to the second-best overall mean, but there are no per-method statistical tests among the proposed metrics themselves (e.g., NPD vs. RTM for a given UAD method). This leaves uncertainty about whether NPD's advantage over RTM/EAG is significant method-by-method.

- **Missing per-dataset win/loss summaries.** Only mean AUC/F1 across 38 datasets is reported. A critical difference diagram, Nemenyi test, or a win/tie/loss table would clarify whether NPD dominates consistently or has high variance. The current reporting could hide that NPD wins by a little on many datasets but loses badly on some.

### Trivial

None.

## Nice-to-Haves

- **Add an oracle (Max) column to the UOMS table (Table 2).** The Max baseline is present in the BO study (Table 1) but absent from the UOMS comparison. Including it would show how close RTM/NPD come to the theoretical optimum and contextualize the remaining gap.
- **Add a limitations subsection.** The conclusion briefly notes that "the highest NPD did not always correspond to the best model performance." This could be expanded into a short discussion of when NPD is likely to fail (e.g., when training data is already near-Gaussian, or when anomalies are highly localized in a small subspace).
- **Computational cost discussion.** The overhead of generating and scoring the Gaussian dataset per hyper-parameter candidate is not mentioned; a brief note would help practitioners assess the practical trade-off.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"NPD's Spearman rank correlation with both AUC and F1 is 1.0 (Figure 6)" listed as a strength by the Strength Finder* — This conflicts with the verified weakness about the overstated Spearman claim. The weakness wins; the strength is removed.
- *"Weak connection between theoretical analysis and surrogate quality" framed as a fatal/structural issue by the harsh critic* — I have moved this to Minor. The theoretical analysis is peripheral but does not invalidate the empirical results. The paper's core contribution (the metrics and their empirical validation) stands on its own.
- *Harsh critic's broader concern about "missing oracle in UOMS table" as a "methodological gap"* — Moved to Nice-to-Haves. It is a useful addition but not a flaw in the existing analysis.

## Novel Insights

The reviewer critiques surface some genuine tensions in the paper. The most interesting observation is the fundamental asymmetry in the theoretical framing: the paper claims that Theorem 2's upper bound supports the claim that maximizing NPD maximizes separation, but an upper bound actually provides a necessary condition for good separation (small NPD implies small gap), not a sufficient one for the converse. This is a subtle but real logical gap that the paper elides. However, no reviewer raises a deeper structural insight beyond this — the paper's main value remains its strong empirical demonstration rather than its theoretical apparatus.

## Suggestions

1. **Replace the "Spearman = 1" claim** with quantitative rank-correlation statistics (Spearman or Kendall τ) computed across BO iterations for all 38 datasets and all UAD methods. Report the mean correlation and the fraction of datasets where ρ > 0. This directly supports the surrogate claim and remedies the overstatement.
2. **Specify the validation split ratio M** for NPD. State the exact value (or proportion) used in experiments. A short sensitivity analysis (e.g., varying M from 10% to 50% on a subset of datasets) would further strengthen the paper.
3. **Add per-method statistical tests** comparing NPD against RTM and EAG (e.g., paired t-test or Wilcoxon signed-rank per UAD method) so readers can see where the advantage is significant.
4. **Provide dataset-level win/tie/loss counts** or a critical difference diagram comparing NPD against the second-best metric, to supplement the averaged means.
5. **Tone down the "theoretical guarantee" language** in the abstract and contributions. Replace with "theoretical motivation" or "theoretical analysis" to better match what the theorems actually deliver.

## Score and Decision

The paper makes a real contribution to a practically important problem. NPD is a novel, simple, and empirically effective surrogate metric. The main issues are an unsubstantiated strong claim about perfect rank correlation, a missing reproducibility detail (M), and a slightly inflated theoretical framing — all fixable. The empirical evidence across 38 datasets and four methods is substantial enough to support acceptance.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>