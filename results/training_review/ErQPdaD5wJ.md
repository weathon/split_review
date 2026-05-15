Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper tackles the challenging problem of hyperparameter optimization and model selection for unsupervised anomaly detection (UAD). The authors propose three surrogate metrics — RTM, EAG, and NPD — that estimate expected test performance without any labeled anomalies. The main contribution is NPD, a semi-internal metric that compares anomaly scores on a held-out validation set against scores on an isotropic Gaussian sample matched to the training moments. The metrics are integrated with Bayesian optimization and evaluated across 38 datasets with four UAD methods. NPD consistently outperforms existing model selection heuristics (Random, MV/EM, consensus-based methods) with statistically significant gains.

## Strengths

- **Novel NPD metric with clear intuition.** The idea of comparing anomaly scores on real held-out data vs. Gaussian-generated data is genuinely novel and well-motivated. It avoids needing ground-truth anomalies, can compare across different UAD methods, and the geometric interpretation (the Gaussian-generated data probes the space outside the normal data manifold) is intuitively appealing and supported by visualizations (Figures 3, 4, 7).

- **Large-scale empirical evaluation.** The experiments span 38 benchmark datasets, four UAD methods (OCSVM, AE, DeepSVDD, DPAD), and include both BO-based hyperparameter tuning (Table 1) and direct model selection from a large grid pool (Table 2, up to 2667 models). The use of 5 random splits, statistical significance testing, and multiple performance metrics (AUC, F1) makes this one of the more thorough evaluations in the area.

- **Clear articulation of the inductive UAD setting.** Section 2 draws an important and often-overlooked distinction between transductive outlier detection (outliers present in the training set) and inductive UAD (training on normal-only data to detect future anomalies). This reframing justifies why methods designed for the former setting (e.g., early stopping with inlier priority assumptions, consensus-based approaches) may not transfer, strengthening the case for the proposed approach.

- **NPD demonstrates both cross-method and within-method selection capability.** The UOMS results (Table 2) show that NPD can select the best model from a large heterogeneous pool encompassing multiple methods and hyperparameter configurations, supporting Goal 2 of AutoUAD. The Spearman rank correlation of 1.0 in Figure 6 provides strong evidence of monotonic relationship with test performance for NPD.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical analysis does not directly establish that maximizing NPD leads to higher test AUC.** Theorem 2 provides an upper bound on NPD in terms of the normal–anomaly score gap (NPD ≤ gap/denominator). The paper then reasons "As NPD is maximized, the gap between normal and anomalous data also becomes larger." This is logically incomplete — an upper bound guarantees that when NPD is *large*, the gap must be *at least as large*, but it says nothing about monotonicity, and it does not connect to the optimization objective (test AUC on unseen data). Theorem 3 bounds KL divergence between training data and the Gaussian surrogate, which is at best a sanity check. A direct analysis (or stronger empirical evidence like full-grid correlation plots) linking NPD rankings to test AUC rankings is needed to substantiate that maximizing NPD is a sound optimization strategy. The paper relies on BO-trajectory correlation (Figure 5), but this is a partial view.

- **NPD is claimed to be "hyper-parameter-free" but has an undiscussed design parameter.** The abstract and Section 3.3 state NPD is "simple and hyper-parameter-free." However, Definition 6 introduces a validation set of size M (the training data is split into sizes N−M and M) without specifying its value or analyzing sensitivity to it. The split ratio M/N is a free parameter that could affect NPD's behavior, especially for small datasets. This is a clear discrepancy between the paper's claims and its implementation. The authors should either provide the default value used, report a sensitivity analysis, or qualify the claim.

### Minor

- **Empirical gains over Random are modest, and one method shows no gain.** For AE, NPD improves AUC by +0.023 over Random; for DPAD, +0.026 AUC. While statistically significant, the practical magnitude is limited. More notably, for DeepSVDD, the Default hyperparameters achieve higher F1 (0.712) than NPD (0.662) — a case the paper honestly reports ("NPD significantly outperforms other methods when applied to OCSVM, AE, and DPAD") but does not analyze or explain. Understanding why NPD underperforms on DeepSVDD would strengthen confidence in the method.

- **RTM and EAG are presented as contributions despite acknowledged flaws.** The paper lists RTM and EAG as contributions (Section 1) but later states they "may overfit the training set" and "introduce an additional hyper-parameter" (Section 3.3). Since these metrics are explicitly superseded by NPD and have known limitations, presenting them as equal contributions alongside NPD is overstated. A more honest framing would treat them as preliminary attempts that motivate NPD.

- **UOMS Table 2 omits MV/EM baselines.** The baselines section (Section 4) lists MV/EM as a comparison baseline, but Table 2 only reports MC, HITS, and IForest-default. The paper does not explain why MV/EM are excluded from the UOMS experiment. While MV/EM may be unsuitable for cross-method comparison, this needs clarification.

- **Theorem 1's entropy argument is presented without formal justification.** The claim "the uncertainty of χ_gen is always higher than that of χ_trn" relies on the Gaussian maximum-entropy property, but the paper does not formally prove that the conditions for this property (matching first two moments) are sufficient to guarantee the inequality almost surely. The theorem is likely correct for the stated reasons, but the "almost surely" clause is asserted without proof.

### Trivial
- The geometry interpretation ("outline of χ_gen is a hypersphere") is informal; the density contours of an isotropic Gaussian are hyperspheres, but the "outline" phrasing could mislead readers about the nature of the typical set.
- The discrete formula for EAG at line 131 appears garbled in the parsed text (parser artifact).

## Nice-to-Haves
- **Ablation study on the split ratio M/N.** Showing NPD's sensitivity (or lack thereof) to the validation split would strengthen the paper and address the claim of being hyper-parameter-free.
- **Full-grid scatter plots of NPD vs. test AUC** across all hyperparameter configurations (not just the BO trajectory). This would directly validate the surrogate assumption.
- **Computational overhead analysis.** Reporting the additional cost of training on N−M points + scoring M validation + M generated points, especially for deep methods, would help practitioners assess practical trade-offs.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The histograms in Figure 2 are cherry-picked examples"* — This is a subjective judgment with no evidence that the examples are unrepresentative. The paper shows them as illustrative (not as proof), and the claim is unverifiable.
- *"Theorem 1's entropy argument is misapplied because covariances are different"* — The reviewer is factually wrong. The Gaussian χ_gen uses diag(σ²_trn). For distributions with given marginal variances, the Gaussian with diagonal covariance has the maximum entropy. Since χ_trn has those same marginal variances (by construction), its entropy is ≤ that of χ_gen. Theorem 1 is correct.
- *"The outline ... is a hypersphere is incorrect — an isotropic Gaussian's typical set is a shell, not a hypersphere"* — A pedantic distinction. The density contours of an isotropic Gaussian are hyperspheres. The paper is providing an informal geometric intuition, not a rigorous probability statement.
- *"The paper does not compare NPD against early stopping (Huang et al., 2024) and meta-learning baselines (Zhao et al., 2021, 2022)"* — The paper gives principled reasons for excluding these comparisons: early stopping's inlier priority assumption does not hold for the inductive UAD setting (Section 2, line 36), and meta-learning requires supervision and historical labeled datasets, contradicting the unsupervised framing (Section 2, lines 21, 35). These are scope-exclusion decisions, not omissions.
- *"DeepSVDD F1 is worse than default, which weakens the narrative"* — The paper honestly reports this ("NPD significantly outperforms other methods when applied to OCSVM, AE, and DPAD") without claiming uniform superiority. This does not undermine the stated claims.
- *"The discretized formula (0.21/N…) appears typographically garbled"* — Parser artifact; not present in the original submission.
- *Various formatting/style nitpicks and generic statements* — Removed per meta-reviewer instructions.

## Novel Insights

Beyond this paper's contributions, an interesting observation emerges from the comparison of RTM, EAG, and NPD: the failure modes of internal metrics (RTM/EAG) occur precisely when the training data's score distribution does not mirror the test-time anomaly distribution — specifically when the model overfits the training data's idiosyncratic structure. NPD's advantage comes from using a synthetic Gaussian set that is *guaranteed* to lie partially outside the training data manifold, effectively simulating the out-of-distribution nature of true anomalies without needing any real anomaly examples. This suggests a general design principle for unsupervised surrogate metrics: the most robust proxies are those that introduce an independent reference distribution whose relationship to the training distribution is controlled and analyzable, rather than relying solely on properties of the training score distribution itself. The finding that NPD's Spearman rank correlation with test AUC can reach 1.0 (perfect monotonicity) while RTM/EAG sometimes show *negative* correlation is striking and warrants deeper investigation into when and why internal metrics break down.

## Suggestions

1. **Acknowledge M as a design choice** and either report the value used, show it is insensitive across reasonable ranges, or remove the "hyper-parameter-free" claim.
2. **Strengthen the theoretical connection** by adding a direct analysis (or at least full-grid empirical evidence) linking NPD rankings to test AUC rankings, beyond the BO trajectory view.
3. **Include an analysis of the DeepSVDD failure case** to understand when NPD underperforms and characterize its limitations honestly.
4. **Clarify the Table 2 omission of MV/EM** — explain why they are unsuitable for cross-method UOMS.
5. **Relegate RTM and EAG to preliminary heuristics** rather than listing them as equal contributions, to better reflect the paper's actual contribution.

## Score and Decision

The paper addresses a genuinely important and underexplored problem with a novel metric (NPD) and extensive empirical evaluation. However, the theoretical justification has a significant logical gap (upper bound ≠ monotonicity with test AUC), the "hyper-parameter-free" claim is contradicted by the undefined split ratio M, and the empirical gains are modest with one notable counterexample (DeepSVDD). These issues are addressable but weaken the paper in its current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>