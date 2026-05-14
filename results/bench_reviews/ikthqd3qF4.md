Now I have sufficient context. Let me compose the final review.

## Summary

The paper addresses the problem of detecting "cross-applicants" (individuals submitting multiple mortgage applications) in large-scale, anonymous loan-level data. The key methodological contribution is a set of observable lower bounds on precision and relative recall for unsupervised record linkage, derived by exploiting a structural constraint: an individual can originate at most one first-lien mortgage. The bounds depend only on the fraction of clusters with multiple originations and the empirical origination probability — both observable without ground-truth labels. The authors instantiate the method with agglomerative clustering, validate it on a simulation where ground-truth identifiers are known, and apply it to 65.5 million HMDA mortgage applications, reporting 92.3% estimated precision at their preferred specification.

## Strengths

- **Clever use of a structural constraint as a supervision signal.** The idea that "no individual can originate two first-lien mortgages" serves as a weak label that makes precision bounds provably computable from observable data. This is genuinely novel and connects naturally to a range of other settings (e.g., insurance, college admissions, single-offer job markets), giving the framework broad applicability.

- **Method-agnostic framework enabling label-free model selection.** Because the bounds depend only on predicted labels (clusters) and not on the clustering algorithm, they allow principled comparison of 96 combinations of distance functions and tolerance parameters ε without any ground truth. The precision-sample-size frontier (Figure 5) and the use of Corollary 2 for knee-based specification selection demonstrate a practical, label-free tuning procedure.

- **Real-world application at scale.** The HMDA application is genuinely large-scale (65.5M applications) and tackles a practically important problem. The paper demonstrates that the method is computationally feasible and yields plausible results (314k clusters at 92.3% estimated precision), with clear downstream use cases (fairness measurement, lending standard monitoring, shopping behavior analysis).

## Weaknesses

### Fatal
None.

### Major

1. **The core inequality Pr[Mult|False] ≥ p² is not adequately justified in the main text, and the intuition given is misleading.** The paper's entire bound hinges on Remark 1: since Pr[Mult|¬False] = 0, we have Pr[False] = Pr[Mult] / Pr[Mult|False]. The bound Pr[False] ≤ Pr[Mult]/p² requires Pr[Mult|False] ≥ p². The paper's intuition (Section 2.2, line 175) considers "random pairs of applications" where the probability of two originations is p². But false-positive clusters are explicitly **not** random pairs — the algorithm selects applications that are similar on the very covariates (credit score, income, LTV, date) that are correlated with origination probability. If the algorithm tends to cluster low-credit-score applicants together, both individuals in a false-positive cluster may have below-average origination probabilities, giving q₁q₂ < p², reversing the inequality and invalidating the bound. The paper states that Lemma 1 in the appendix proves Pr[Mult|False] > p² under Assumptions 1–2. This proof cannot be evaluated from the main text, and the provided intuition does not address the selection concern. **This is the single most important unresolved issue in the paper.** The claimed guarantee is only as credible as Lemma 1; without it, the 92.3% figure in HMDA is an estimate that may or may not be a lower bound.

2. **The simulation validates the bound only under ideal conditions that satisfy all assumptions perfectly.** Section 3 generates data where Assumptions 1–2 hold exactly, multiple originations per individual are impossible by construction, and the clustering occurs on simple Euclidean distance in low dimensions. The bound closely tracks true precision in this setting (Figures 3a vs. 4a), but this is a consistency check, not a robustness test. The simulation does not probe the most concerning failure mode: scenarios where covariate-origination correlation is strong (e.g., low-credit applicants are both more likely to be falsely clustered together and less likely to originate). Without experiments injecting realistic correlations between the features used for clustering and the origination outcome, it is unclear whether the bound degrades gracefully or catastrophically in practice.

### Minor

3. **Restriction to clusters of size two is a significant limitation that is not fully explored.** The paper drops all clusters with more than two applications (footnote 4), which means: (a) true cross-applicants who submit three or more applications are entirely undetected, artificially depressing recall; (b) the reported 92% recall in simulation applies only to the subset of cross-applicants captured as size-2 pairs, not the full population; (c) the bound's tightness and applicability to larger clusters (where Pr[Mult|False] may differ) is not examined. While this restriction is clearly stated, its consequences for the practical usefulness of the method are underexplored.

4. **No independent validation of the HMDA results.** The HMDA application (Section 4) relies entirely on the bound — there is no external check (e.g., manual inspection of a random sample of clusters, comparison with credit-bureau data, or validation against a labeled subset). The authors reference "additional diagnostics" in the appendix, which is not present. Without any form of validation, the application demonstrates that the method *runs* at scale, but not that it actually finds real cross-applicants with the claimed precision.

5. **The bound after dropping multiple-origination clusters (Equation 1) is introduced without derivation.** The formula Pr[False] ≥ (1 − Pr[Mult]/p²)/(1 − Pr[Mult]) is presented as a direct improvement, but the derivation is not shown even by sketch. It is not obvious that true-positive clusters (TP) and false-positive clusters with zero/one origination (FP_0) are exchangeable in the way the formula implies. A brief derivation in the main text would help.

### Trivial
None.

## Nice-to-Haves
- A robustness simulation varying the strength of correlation between covariates used for clustering and the origination probability, with a clear diagnosis of when the bound degrades.
- External validation of a small random sample of HMDA clusters (e.g., comparing names/addresses if available in the confidential data, or at minimum a distributional diagnostic).
- Extension of the bound to clusters of arbitrary size, or a clear theoretical argument for why size-2 is sufficient.

## Removed Points
- Criticisms about the proof being deferred to the appendix (parser strips appendices; they exist in the original submission).
- Criticisms about missing "additional diagnostics" referenced in the appendix (same reason).
- The claim that the bound "cannot be independently verified" due to data unavailability — the paper cites a specific confidential version of HMDA that exists.
- Pure formatting/style nitpicks and claims about "typos" that are parser artifacts.
- The criticism that the simulation is "circular" — every simulation validates under its assumptions; this is not a weakness per se, though the lack of robustness testing is a genuine concern (kept in Major #2).
- Generic strengths from the Strength Finder that lacked specific content (e.g., "the problem is important," "the writing is clear") — these are already reflected in the summary.
- The strength about "scalable implementation using state-of-the-art hierarchical clustering" — this is implementation detail, not a distinctive intellectual contribution.
- The strength about "concrete downstream applications" — these are future work, not a demonstrated contribution.

## Novel Insights
None beyond the paper's own contributions. The reviews do not reveal an unforeseen implication or connection that the authors themselves missed.

## Suggestions

1. **Address the core inequality head-on in the main text.** Provide a clear, self-contained justification for why Pr[Mult|False] ≥ p² for false-positive clusters, or state the inequality as an additional explicit assumption (rather than claiming it follows from Assumptions 1–2). If Lemma 1 is correct as claimed, present its key steps in the main paper. If not, the bound can still be useful as a heuristic, but the paper must stop claiming it is a guaranteed lower bound.

2. **Add a targeted robustness simulation.** Generate data where the clustering features (credit score, income) are correlated with origination probability, and measure the gap between the bound and true precision as the correlation strength varies. This would directly address the central concern.

3. **Validate a small subset of HMDA predictions.** Even inspecting a few hundred clusters manually (e.g., checking whether applications in the same cluster have consistent names or addresses in the confidential data) would dramatically strengthen the paper's empirical claims.

4. **Clarify the effect of the size-2 restriction on reported recall.** The 92% recall figure should be contextualized: what fraction of all cross-applicants are excluded by the size-2 filter, and what is the recall conditional on being captured?

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| LRIM Benchmark (IAZXEX1dVV) | 6.67 | Stronger paper: clear, provable contribution with thorough validation. Current paper is less polished and has an unresolved theoretical gap. |
| XQC RL (tx1ZvypKqS) | 6.50 | Stronger paper: well-motivated, strong empirical results, minor weaknesses only. Current paper has a more fundamental concern. |
| Embedding bounds (fQIE4NJOVm) | 5.20 | Comparable: both have interesting theoretical contributions with presentation/logic gaps. Current paper has a more practical application but a more central theoretical concern. |
| Robustness of Probabilistic Models (ZFZhV7Snf4) | 4.00 | Comparable: both have split reviews, interesting ideas with substantive concerns. Current paper is slightly more novel but has a more central unresolved issue. |
| DBSCAN clustering (hi6opqxk5X) | 2.80 | Weaker paper: insufficient experiments, missing baselines. Current paper has better real-world application and a more novel contribution. |
| Curvature/Bispectrum (pcqyhDvG0i) | 1.50 | Much weaker: fundamental theoretical errors, withdrawn. Current paper is substantially stronger. |

### Assessment
The paper introduces a genuinely clever idea — using the structural constraint of at-most-one origination to derive observable precision bounds for unsupervised record linkage. The HMDA application demonstrates the method's practical feasibility at scale. However, the paper's central claim (that the bound is a guaranteed lower bound) rests on an inequality (Pr[Mult|False] ≥ p²) whose justification is deferred to the appendix and whose intuitive motivation in the main text (the "random pairs" analogy) is misleading when applied to algorithmically selected clusters. The simulation validates only the ideal case. These concerns are substantive enough to prevent acceptance at the current level of development but do not invalidate the core insight, which could become a solid contribution with adequate justification and robustness analysis.

**Score: 4.5** — Borderline. The idea is interesting and the application is real, but the theoretical foundation has an unresolved gap that is central to the paper's main claim.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>