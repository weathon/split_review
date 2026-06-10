Now I have all the calibration data I need. Let me finalize the review and score.

**My calibration reasoning:**

**Round 1 bracket: 5.5 – 8.0**
- Weak OOD detection papers (2-3): clearly weaker than this paper
- Du et al. (2024a) SAL (6.50, accepted): very closely related — same two-stage framework for wild OOD detection. Medix improves upon it.
- DOS (7.33, accepted): strong OOD method paper with good results
- Deep Orthogonal Hypersphere (8.00, accepted): strong method + theory paper with fewer gaps

**Round 2: 6.5 – 7.5**
- Medix is clearly better than Du et al. (6.50): stronger empirical results (best on all 11 settings vs. SAL's more limited wins), a more principled median-based filtering mechanism, and two-sided theoretical bounds.
- Comparable to DOS (7.33): both have strong empirical results; Medix has more theoretical depth, but DOS is cleaner methodologically.
- Below 8.00 anchors: the theory-experiment gap at π=0.5 and the hyperparameter tuning ambiguity are genuine concerns not present in the strongest anchors.

**Final score: 7.0** — clearly better than Du et al. (6.50), slightly below DOS (7.33) due to unresolved methodological questions.

## Summary
This paper introduces Medix, a two-stage framework for OOD detection that leverages unlabeled "wild" data. The first stage uses an iterative greedy algorithm based on the element-wise median (EWM) of gradient vectors to filter candidate OOD samples; the second stage trains a binary OOD detector on identified outliers and labeled InD data. The paper provides two-sided theoretical bounds on misclassification rates and demonstrates consistent improvements across 11 InD-OOD pairs against 20 baselines.

## Strengths
- **Consistent state-of-the-art performance across all evaluated settings.** Tables 1 and 2 show Medix achieves the best FPR95 on every single InD-OOD pair (0.80% avg FPR95 on CIFAR-10 vs. 3.40% for WOODS; 5.42% on CIFAR-100 vs. 6.74% for WOODS). This is comprehensive and consistent, not cherry-picked.
- **Well-motivated design with empirical validation.** Figure 1 demonstrates a clear monotonic increase in L2-norm deviation between the InD mean gradient and EWM of wild gradients as OOD samples are added, directly motivating the optimization in Eq. 4 and the stopping criterion.
- **Two-sided theoretical guarantees with interpretable decomposition.** Theorems 4.1 and 4.2 provide closed-form upper bounds on both inlier and outlier misclassification rates, decomposed into concentration, contamination, and separation effects. Remark 4.3 provides empirical evidence for the sub-Gaussian assumption, and Theorem C.3 in the appendix relaxes this assumption.
- **Comprehensive benchmarking.** 11 InD-OOD pairs with 20 baselines spanning both InD-only and InD+wild methods, plus ablation studies in the appendix.

## Weaknesses

### Fatal
None.

### Major
- **Theory-experiment gap at π=0.5.** The contamination terms in Theorems 4.1 and 4.2 both equal 0.5 at π=0.5 (the default experimental setting, line 170): π/[2(1−π)] = 0.5 and (1−π)/(2π) = 0.5. The paper explicitly states "the bound remains controlled as long as π < 0.5" (line 138), yet all experiments are conducted at π=0.5 without acknowledging this gap or evaluating at lower π values where bounds are tighter. The empirical results clearly work, but the theory does not explain *why* they work at the exact operating point used. This is the same concern reviewers raised for the predecessor work (Du et al., 2024a/SAL, which tested at π=0.1); Medix inherits it at an even more unfavorable point.

- **Ambiguous hyperparameter tuning protocol.** Line 178 states hyperparameters ε and k are selected "with the objective of maximizing OOD performance." It is unclear whether the OOD test data is used for selection — if so, reported metrics are optimistically biased. This needs clarification, as it directly affects the trustworthiness of headline numbers in Tables 1 and 2.

### Minor
- **No runtime or complexity analysis in the main text.** Algorithm 1 computes leave-one-out EWM over all remaining samples each iteration, yielding O(|S|² × d) cost. The paper defers to Appendix A.6, but a brief runtime table or discussion of scalability in the main text would help readers assess practical deployability.

- **Algorithm 1 while-loop condition likely contains a bug (line 110).** The condition "while t ≤ T or |δ_max| > ε" means the loop only terminates when both t > T AND |δ_max| ≤ ε, thus always running at least T+1 iterations regardless of convergence. This likely should be "and" to permit early stopping. Either way, it should be clarified.

- **Sensitivity to π not evaluated.** Given that the theoretical analysis explicitly depends on π, experiments varying the contamination ratio (e.g., π ∈ {0.1, 0.3, 0.5, 0.7}) would directly demonstrate robustness and bridge the theory-experiment gap. This is a natural and expected experiment.

### Trivial
None.

## Nice-to-Haves
- Evaluate at multiple π values to connect empirical behavior to theoretical bounds.
- Brief discussion of failure modes (e.g., OOD data semantically close to InD, high-dimensional gradient regimes).
- More specific comparison with Du et al. (2024a) — the paper says their thresholding "differs fundamentally" (Section 6) but does not explain what SAL does or why EWM is preferable beyond theoretical guarantees.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Connection gap between Figure 1 and Algorithm 1**: The harsh critic noted that Figure 1 shows a global OOD fraction effect while Algorithm 1 removes individual samples. The paper's logic is coherent — the monotonic trend motivates the hypothesis, and Algorithm 1 operationalizes it via leave-one-out. Overly pedantic.
- **Abstract's "40.98% improvement" wording**: Technically ambiguous (relative vs. absolute) but the numbers are correct (46.40 − 5.42 = 40.98) and context makes interpretation clear. Minor nitpick.
- **Strength about sub-Gaussian validation**: The Q-Q plot and histogram evidence is standard empirical practice and acceptable, though not a formal statistical test. This was flagged as potentially weak but is fine.

## Novel Insights
The key novel insight is that the element-wise median of gradient vectors provides a principled mechanism for separating InD and OOD samples in unlabeled mixtures, with formal robustness guarantees up to 50% contamination. The decomposition of misclassification bounds into contamination, concentration, and separation effects provides a useful analytical framework for understanding when gradient-based OOD filtering succeeds or fails. This median-based approach offers a cleaner alternative to the top singular vector method of the predecessor work (Du et al., 2024a).

## Suggestions
- Evaluate at multiple π values (e.g., π ∈ {0.1, 0.3, 0.5, 0.7}) to bridge the theory-experiment gap and demonstrate practical robustness.
- Clarify the hyperparameter tuning protocol — explicitly state whether OOD test data was used for selection.
- Fix or clarify the while-loop condition in Algorithm 1 (line 110): "or" vs. "and" has material implications for convergence behavior.
- Provide a brief runtime comparison in the main text.

## Calibration Report

**Anchors retrieved across all rounds:**

| Round | Path | Avg Score | Relevance |
|-------|------|-----------|-----------|
| 1 | l5ouuojPGe.md (Thresholding Strategies) | 3.00 | Weak OOD monitoring paper, clearly weaker |
| 1 | 3ZdGSTxKuy.md (Harry Potter OOD) | 2.00 | Weak OOD paper, clearly weaker |
| 1 | rcKzU0Vns0.md (Active Learning + OOD) | 2.50 | Weak OOD paper, clearly weaker |
| 1 | KK29oh8jZs.md (Synthetic OOD probing) | 3.00 | Weak OOD paper, clearly weaker |
| 1 | bcWwhF8cTZ.md (GradNorm OOD error) | 5.50 | Rejected OOD gradient paper, weaker scope |
| 1 | **jlEjB8MVGa.md (Du et al. SAL)** | **6.50** | **Direct predecessor, accepted; Medix improves on it** |
| 1 | RWZzGkFh3S.md (Outlier Gradient Analysis) | 4.50 | Rejected gradient paper, weaker |
| 1 | Cdhxv0Oz1v.md (GradRect OOD) | 4.20 | Rejected gradient OOD paper, weaker |
| 1 | cJs4oE4m9Q.md (Hypersphere Compression) | 8.00 | Strong anomaly detection, more polished |
| 1 | KbetDM33YG.md (Online GNN Eval) | 8.00 | Strong but different domain |
| 1 | 25kAzqzTrz.md (FixMatch theory) | 8.00 | Strong theory paper, different domain |
| 1 | EUSkm2sVJ6.md (Data Usage Inference) | 7.60 | Strong ML paper, different domain |
| 2 | eN0RyRVbSm.md (Double Descent OOD) | 6.50 | Accepted, OOD theory paper with similar scope |
| 2 | 83le3arfeA.md (Hyperbolic OOD) | 5.50 | Rejected OOD method paper |
| 2 | 9qpdDiDQ2H.md (MetaOOD) | 5.25 | Accepted but weaker OOD paper |
| 2 | VTYg5ykEGS.md (ImageNet-OOD) | 6.50 | Accepted OOD analysis/dataset paper |
| 2 | xUO1HXz4an.md (NegLabel) | 7.50 | Accepted OOD method with theory, strong |
| 2 | iriEqxFB4y.md (DOS) | 7.33 | Accepted OOD method, strong empirical results |
| 2 | y5einmJ0Yx.md (GOLD) | 7.50 | Accepted OOD method for graphs |
| 2 | cJs4oE4m9Q.md (Hypersphere) | 8.00 | Retrieved again, strong method+theory |

**Round 1 bracket: 5.5 – 8.0.** Paper is clearly above weak/rejected OOD papers and comparable to accepted ones.

**Round 2 narrowing: 6.5 – 7.5.** 
- Medix is clearly better than Du et al. SAL (6.50): stronger results on all settings, cleaner median-based mechanism, two-sided bounds.
- Comparable to DOS (7.33): Medix has deeper theoretical contribution but has the unresolved π=0.5 gap and hyperparameter ambiguity.
- Below NegLabel (7.50) and the 8.00 anchors: those papers have fewer unresolved methodological questions.

**Final score: 7.0.** The paper makes a genuine and well-supported contribution — a novel median-based filtering mechanism for OOD detection with theoretical guarantees and strong empirical results. It clearly improves upon its predecessor (Du et al., 2024a, avg 6.50). The score is held below 7.5 by the theory-experiment gap at π=0.5 and the ambiguous hyperparameter tuning protocol, both of which are addressable but require attention.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>