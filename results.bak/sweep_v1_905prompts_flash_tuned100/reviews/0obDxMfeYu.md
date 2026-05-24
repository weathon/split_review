Now I have all the information I need. Let me synthesize the final review.

## Anchor Summary

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|-----------|
| Du et al. 2024a (SAL) | jlEjB8MVGa | 6.50 | R1 | Directly comparable (wild OOD detection + theory). SAL's theory analyzes its actual algorithm; Medix's theory doesn't. SAL is clearly stronger. |
| SPADE | kwCHcaeHrf | 5.50 | R1/R2 | Cleaner theory-practice connection, weaker empirical results than Medix. Comparably positioned. |
| Gradient Norm OOD | bcWwhF8cTZ | 5.50 | R1 | OOD error estimation via gradients. Similar missing-baselines issues. Medix is roughly comparable. |
| ProMix | voVjW1PT2c | 6.00 | R2 | Mixup for OOD with theory. Medix has stronger empirical results but weaker theory-alignment. |
| Pseudo-labels OOD | jjjxp9Wgjp | 4.25 | R1 | Weaker paper overall. Medix is clearly stronger. |
| Outlier Gradient Analysis | RWZzGkFh3S | 4.50 | R3 | Different domain but similar score calibration. |

**Round 1 Bracket:** (3.5, 7.5) — paper has real contributions but falls short of strong anchors.

**Round 2/3 Narrowing:** Comparing against SAL (6.50), SPADE (5.50), Gradient Norm OOD (5.50), ProMix (6.00), and Pseudo-labels (4.25), Medix sits below SAL and ProMix due to the theory-algorithm disconnect, and roughly at or slightly below SPADE/Gradient Norm. Final score: **4.5**.

---

## Final Consolidated Review

## Summary

This paper introduces Medix, a framework that uses element-wise median (EWM) of gradients to filter OOD samples from unlabeled wild data. The filtering stage greedily removes samples causing the largest drop in L2 distance between the EWM of wild gradients and the InD mean gradient. A binary OOD detector is then trained on the filtered outliers plus labeled InD data. The paper provides theoretical bounds on inlier/outlier misclassification rates under sub-Gaussian assumptions and reports strong empirical results across CIFAR-10 and CIFAR-100 benchmarks.

## Strengths

- **Strong empirical performance across diverse setups.** On CIFAR-100, Medix achieves an average FPR95 of 5.42% across five OOD datasets, outperforming WOODS (6.74%), OE (14.26%), and KNN+ (46.40%) by clear margins (Table 2). On CIFAR-10, Medix attains 0.80% average FPR95 versus WOODS at 3.40% (Table 1). These results are backed by 5-run standard deviations for Medix.

- **Novel median-based approach to outlier filtering.** Using the element-wise median of gradients (rather than the mean) to identify OOD samples in unlabeled mixtures is a well-motivated and technically grounded idea. The empirical motivation in Figure 1 — showing monotonic increase in EWM L2 deviation as OOD samples are added — provides a clear rationale for the optimization in Equation (4).

- **Theoretical analysis of median robustness.** Theorems 4.1 and 4.2 provide explicit bounds on inlier/outlier misclassification rates in terms of contamination, concentration, and separation effects. The bounds formally characterize when median-based filtering can be expected to work (π < 0.5, sub-Gaussian gradients, sufficient separation). A looser version without sub-Gaussian assumptions is also noted (Appendix C.3).

## Weaknesses

### Major

- **Theory–algorithm disconnect undermines the claimed provable guarantees.** Theorems 4.1 and 4.2 analyze an unspecified "EWM filtering rule" that is never defined in the paper. The actual algorithm (Algorithm 1) is a greedy, iterative, leave-one-out procedure that removes the top-k samples per iteration based on the *drop* in L2 distance upon removal. The theorems contain no reference to the algorithm's hyperparameters (k, ε), its iterative structure, or its greedy approximation to the optimization problem (4). The paper presents these theorems as guarantees "for Medix" (Section 4 opening line: "theoretical guarantees of Medix's filtering stage") and claims to be "one of the few studies that provide such a theoretical foundation" (Section 1), but the reader cannot determine whether the bounds apply to the actual algorithm. Until the authors either prove that the greedy iterative procedure obeys the same bounds or provides theorems that directly analyze it, the theoretical section does not support the paper's central claims about provable low error.

- **Missing baseline comparisons for DRL and CONJ.** Section 5.1 lists DRL (Zhang et al., 2024) and CONJ (Peng et al., 2024) as recent baselines, yet neither appears in Tables 1 or 2. The conclusion (Section 7) claims Medix "outperformed state-of-the-art methods such as WOODS and DRL" — but no DRL results are presented anywhere in the visible paper. This is a verifiable omission that weakens the paper's central claim of outperforming "across the board." If these results exist in the (stripped) appendix, the main text should still include them for the comparison to be credible.

- **Unclear hyperparameter selection protocol.** Hyperparameters ε and k are selected from {5e-5, 5e-4, 5e-3, 5e-2} and {4k, 7k, 10k, 20k} "with the objective of maximizing OOD performance" (Section 5.2). The paper does not state whether a held-out validation OOD set was used, whether selection was performed on the same OOD data used for testing, or what protocol prevents test-set leakage. If the selection was done on the test OOD data, the reported FPR95/AUROC numbers are optimistically biased relative to baselines.

- **Incomplete statistical reporting for baselines.** Medix reports standard deviations (5 runs), but none of the baselines in Tables 1 and 2 have standard deviations. This makes it impossible to assess whether the observed improvements over WOODS (e.g., 1.32% FPR95 on CIFAR-100) are statistically significant.

### Minor

- **Theoretical bounds are weak at the default contamination rate.** At π = 0.5 (the default in experiments), the contamination term in Theorem 4.1 becomes π/[2(1−π)] = 0.5, allowing up to 50% inlier misclassification from this term alone. The paper calls this a "low error rate" (Section 4), but a bound that does not rule out half the inliers being misclassified is trivial at the operating point used in experiments.

- **The synthetic validation (Figure 2) uses a 2D Gaussian toy** with OOD placed far from InD (mean [20, 2√3] vs InD means within [−2,2]). This does not reflect the high-dimensional gradient space of real neural networks or near-OOD scenarios where gradients may overlap substantially.

- **The 40.98% improvement framing is potentially misleading.** The headline number compares Medix against KNN+ (a relatively weak wild-data baseline at 46.40% FPR95). Against the strongest wild-data baseline (WOODS), the improvement on CIFAR-100 is 1.32 percentage points. While the KNN+ comparison is valid, it is presented without qualifiers that would help readers calibrate expectations.

### Trivial

- None that warrant mention beyond standard presentation improvements.

## Nice-to-Haves

- An ablation or analysis showing the progression of d_t (L2 deviation) across iterations for real datasets, and the fraction of ground-truth OOD among the removed samples at each step, would strengthen confidence that Algorithm 1 behaves as intended.
- A wall-clock time or complexity comparison against WOODS and OE would help assess practical deployability.
- A failure case analysis (e.g., near-OOD where gradient overlap is high) would set realistic expectations.

## Novel Insights

The core observation — that the element-wise median of gradients can serve as a robust statistic for identifying OOD samples in unlabeled mixtures, and that its L2 deviation from the InD mean gradient increases monotonically with OOD contamination — is the paper's main novel insight. However, the reviews surface no genuinely novel insight beyond what the paper already presents.

## Suggestions

1. **Bridge theory and algorithm.** Either (a) modify Algorithm 1 to match a static EWM-based threshold rule that the theorems actually analyze, or (b) provide new theorems that bound the error of the greedy iterative procedure directly, including the effect of k and ε.
2. **Add DRL and CONJ results** to the main tables. If they cannot be included (e.g., due to unavailable implementations), remove the claim of outperforming DRL from the abstract and conclusion.
3. **Clarify the hyperparameter selection protocol** — explicitly state whether a held-out validation OOD set was used, and if so, how it was constructed. If the test OOD was used for tuning, report results with proper held-out selection.
4. **Report standard deviations for all baselines**, or justify their exclusion.
5. **Add a discussion of the gap between the theoretical analysis and Algorithm 1** as a limitation, noting that the bounds characterize the properties of the median in mixtures rather than the specific greedy algorithm.

## Score and Decision

<score>4.5</score>
<decision>Reject</decision>