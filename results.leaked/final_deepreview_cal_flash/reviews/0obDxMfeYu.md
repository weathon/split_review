Now let me compile my final analysis and write the review.

The paper's core strengths and weaknesses are now clear. Here's my calibration summary:

**Round 1 bracket**: [4.5, 6.0] — the paper is clearly above the weak anchors (~3.0) and below the SAL paper (6.5) which has cleaner theory-alignment.

**Round 2 narrowing**: Key anchors within the bracket are PALM (5.75, accept), SPADE (5.50, accept), Gradient Norm (5.50, reject). The paper is most comparable to SAL (6.5, accept) but with a significant theory-alignment gap that SAL doesn't have. Compared to PALM (5.75), Medix has a more novel approach but a more structural weakness (the theory-alignment gap). I place Medix below these accepted papers due to the unresolved disconnect between its theoretical claims and its actual algorithm.

**Final score position**: The paper sits at 5.0. It has genuine contributions (novel median-based approach, strong empirical results) but the theory–algorithm gap is a real structural issue that undermines one of its core claimed contributions (C2), and the experimental comparison lacks some rigor (no error bars for baselines).

---

## Summary

This paper proposes Medix, a framework that uses the element-wise median (EWM) of gradients to filter candidate OOD samples from unlabeled wild data, then trains a binary OOD detector on the identified outliers and labeled InD data. The median is motivated by its robustness to contamination up to 50%. The paper provides theoretical error bounds and reports strong empirical results on CIFAR-10 and CIFAR-100 across multiple OOD test sets, outperforming 20 baselines.

## Strengths

1. **Novel median-centric approach for wild-data OOD detection.** Using the element-wise median of gradients as a robust aggregation mechanism to identify outliers from unlabeled mixtures is a genuinely new idea. The optimization formulation (Eq. 4) — finding a subset whose EWM is closest to the InD mean gradient — provides a clean conceptual framing that differs fundamentally from prior work using top singular vectors (SAL) or constrained optimization (WOODS).

2. **Strong and consistent empirical gains.** On CIFAR-100 (Table 2), Medix achieves an average FPR95 of 5.42%, outperforming WOODS (6.74%) by 1.32 percentage points and InD-only methods like KNN+ (46.40%) by 40.98 percentage points. On CIFAR-10 (Table 1), Medix achieves 0.80% average FPR95 versus WOODS' 3.40%. The improvements hold across all five OOD test sets.

3. **Theoretical analysis of median robustness under contamination.** Theorems 4.1 and 4.2 bound inlier and outlier misclassification rates under a Huber contamination model, showing that the EWM-based approach remains controlled when the OOD proportion π < 0.5. Theorem C.3 (appendix) provides a relaxed version under only bounded second moments.

4. **Addresses a practical limitation of prior work.** The paper correctly notes that prior methods (Katz-Samuels et al. 2022a, Du et al. 2024a) assume **batch-level** mixing ratios, whereas Medix operates under more realistic **dataset-level** mixing, better reflecting real-world deployment.

## Weaknesses

### Major

1. **Theory–algorithm gap: the theorems are not about the proposed algorithm.** Theorems 4.1 and 4.2 bound the misclassification rates of an "EWM filtering rule" that is never formally defined. No argument is given that Algorithm 1 (the greedy iterative removal procedure) implements this rule or inherits its bounds. The bounds involve oracle quantities \(m_{\text{in}}\) and \(m_{\text{out}}\) (the true unknown counts of InD and OOD points) and do not account for the iterative nature of Algorithm 1 or its approximation error. The paper claims (Section 4) to provide "theoretical guarantees of Medix's filtering stage" and concludes (Section 7) that the bounds "demonstrate that Medix maintains robustness," but the link is not established. This directly affects contribution C2, which is presented as a core contribution. Without a clear connection, the theory supports the general median-based filtering *concept* but not the specific algorithm submitted as Medix.

2. **Hyperparameter selection on test OOD performance, risking overfitting.** The hyperparameters \(k\) (removed per iteration, searched over {4k, 7k, 10k, 20k}) and \(\epsilon\) (searched over {5e-5, 5e-4, 5e-3, 5e-2}) are selected "with the objective of maximizing OOD performance" (Section 5.2) without specifying a held-out validation set distinct from the test OOD. Combined with the wide search range for \(k\) (4k–20k on wild sets of ~25k InD + 25k OOD), this raises the risk of overfitting the hyperparameters to the specific test OOD datasets.

### Minor

3. **No error bars for baseline methods.** In Tables 1 and 2, only Medix reports standard deviations (over 5 runs). The 20 baselines (MSP, ODIN, KNN, KNN+, OE, WOODS, DRL, etc.) are listed without any variance information, making it impossible to assess whether Medix's improvements (e.g., 1.32% FPR95 over WOODS on CIFAR-100) are statistically significant.

4. **"Open-world" claims are not fully supported by the evaluation protocol.** The main experiments follow the matched-protocol standard in the sub-field (wild data constructed from the same OOD dataset used at test time; Section 5.1). For example, PLACES365 appears both in the wild mixture and as the test OOD. While the paper references an "unseen OOD" experiment in Appendix A.4 (\(P_{\text{out}}^{\text{test}} \neq P_{\text{out}}\)), the main results and the "open-world" branding in the abstract/title are not qualified to reflect this limitation.

### Trivial

5. The 2D synthetic demonstration (Figure 2) uses an OOD mean at \([20, 2\sqrt{3}]\) while the farthest InD class center is at \([0, 2\sqrt{3}]\) — a separation of 40 standard deviations given \(\sigma=0.5\). This is presented as a simple illustration, which is fine, but the separation is far larger than what would be encountered in the image experiments.

## Nice-to-Haves

- **Computational complexity:** The main text should briefly discuss the O(\(|S|^2\)) leave-one-out cost per iteration of Algorithm 1, given it is a practical concern for large wild sets.
- **Clarify the theory–algorithm connection:** Even an informal argument that Algorithm 1 approximately minimizes the objective in Eq. 4, and hence qualitatively behaves like the optimal EWM filtering rule analyzed in the theorems, would significantly strengthen the paper.
- **Error bars for baselines in the main tables** would make the empirical claims more trustworthy.

## Removed Points

These points from the input reviews are removed or downgraded per the filtering rules:

1. **"Uncontrolled comparison — InD-only baselines use the full 50k training set while Medix uses 25k."** Removed. The asymmetry favors the baselines (more labeled data), not Medix. The paper acknowledges this, and Medix outperforming despite this disadvantage strengthens, not weakens, the results.
2. **"Missing related works."** Removed per hard rule. I cannot verify the existence or absence of any citation from external knowledge.
3. **"Formatting/style/typo issues."** Removed per hard rule — these are parser artifacts, not author errors.
4. **"Reproducibility concerns about unreleased code/data."** Removed per hard rule. The paper states "We provide the necessary code to reproduce our results."
5. **"Theory symbols m_min, m_in undefined."** These quantities are defined in context (m_min is the smaller of m_in and m_out; m_in and m_out are the true counts of InD and OOD in the wild set). The concern is overstated.
6. **"2D synthetic example is trivial and doesn't prove anything."** It is explicitly presented as a simple demonstration, not as evidence for real-world performance. Kept as Trivial #5 above rather than a serious weakness.

## Novel Insights

None beyond the paper's own contributions. The core tension — that the paper's theoretical analysis supports a "median-based filtering" concept but does not analyze the actual greedy algorithm — is the most important observation to emerge from the review process.

## Suggestions

1. **Bridge the theory–algorithm gap.** Either (a) prove that the greedy Algorithm 1 achieves (or approximately achieves) the bounds in Theorems 4.1 and 4.2, (b) reinterpret the theorems as analyzing the optimal solution to Eq. 4 and explain why Algorithm 1 is a reasonable approximation with its own convergence properties, or (c) at minimum, formally define the "EWM filtering rule" and transparently discuss the gap.
2. **Report error bars** for all baseline methods in the main tables, or at least provide a statistical significance analysis of the key comparisons.
3. **Specify the validation protocol** used for hyperparameter selection and confirm whether the test OOD was ever used for tuning. If a held-out validation set was used, describe it.
4. **Qualify the "open-world" language** in the abstract and introduction, or move the cross-distribution evaluation (Appendix A.4) into the main paper to support the claim.
5. **Include a brief complexity analysis** of Algorithm 1 in the main text, noting the per-iteration cost.

## Score and Decision

**Bracket**: Round 1 bracketing placed the paper between weak OOD detection anchors (~3.0) and the SAL paper (6.5), with a plausible range of [4.5, 6.0]. Round 2 narrowing found anchors at 5.75 (PALM, accept), 5.50 (SPADE, accept), and 5.50 (Gradient Norm, reject). The paper is weaker than PALM and SAL due to the theory–algorithm gap, but stronger than the gradient norm paper in terms of novelty. The final score is positioned at the lower end of the bracket because the theory–algorithm gap is a structural issue that directly affects a claimed core contribution.

**All anchors consulted across rounds**:
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 6Z8rZlKpNT (Normalizing Flows OOD) | 3.40 | R1 | Weaker — no theory, limited results |
| l5ouuojPGe (Thresholding) | 3.00 | R1 | Weaker — different sub-problem |
| jlEjB8MVGa (SAL) | 6.50 | R1 | Stronger — cleaner theory-alignment, same problem setting |
| bcWwhF8cTZ (Gradient Norm) | 5.50 | R1,R2 | Comparable score but rejected for overlap; Medix has better novelty |
| kwCHcaeHrf (SPADE) | 5.50 | R2 | Stronger theory-practice alignment, accepted |
| uNkKaD3MCs (PALM) | 5.75 | R2 | Stronger overall — cleaner contribution, accepted |
| sZZ3R0lV9f (MixDiff) | 5.25 | R1,R2 | Different sub-problem (API-constrained) |
| zUrdd5NRLH (GROD) | 5.00 | R1,R2 | Weaker — less convincing results, rejected |
| Zww4Xqmk38 (Tree-based) | 4.75 | R2 | Weaker — less rigorous, rejected |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>