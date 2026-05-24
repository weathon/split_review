Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

---

## Summary

This paper introduces Medix, a median-based framework for OOD detection using unlabeled wild data. Medix operates in two stages: (1) filtering outliers from the wild mixture via a greedy iterative algorithm that removes samples whose gradients cause the largest drop in the L2 distance between the element-wise median (EWM) of wild gradients and the mean InD gradient, and (2) training a binary OOD detector on the identified outliers plus labeled InD data. The paper provides theoretical bounds on inlier and outlier misclassification rates under sub-Gaussian assumptions and reports strong empirical results across 11 InD–OOD pairs, outperforming 20 baselines including WOODS, OE, and KNN+.

## Strengths

1. **Strong empirical performance across diverse benchmarks.** On CIFAR-100, Medix achieves an average FPR95 of 5.42%, outperforming WOODS (6.74%) and reducing KNN+'s FPR95 by 40.98%. On CIFAR-10, Medix achieves 0.80% average FPR95 versus WOODS's 3.40%. Results are reported with standard deviations over five runs (Tables 1–2).

2. **Novel use of element-wise median for wild-data outlier extraction.** The median-based filtering criterion (Eq. 4) and the greedy leave-one-out approximation (Algorithm 1) represent a distinctive approach to the wild-data OOD problem. The paper provides empirical motivation (Figure 1) showing that deviation between the EWM and the InD mean gradient increases monotonically as OOD samples are added.

3. **Two-sided theoretical error bounds with explicit structure.** Theorems 4.1 and 4.2 give separate bounds for inlier misclassification (InD→OOD) and outlier misclassification (OOD→InD), decomposing each into a contamination effect (controlled when π < 0.5), a concentration effect that decays with sample size, and (for outliers) a separation effect. The paper also notes a looser bound (Theorem C.3) that requires only bounded second moments, broadening the scope.

4. **Handles dataset-level mixing without batch-level structure.** As the paper explicitly notes (Section 6), prior methods like WOODS and Du et al. (2024a) assume batch-level mixing, which is unrealistic for large outsourced collections. Medix operates on dataset-level mixtures, making it more practically applicable.

## Weaknesses

### Major

1. **Theory does not match the actual algorithm.** Theorems 4.1 and 4.2 analyze a static "EWM filtering rule" that classifies points based on gradient deviation from a single median computed on the full wild set. However, Algorithm 1 is a *greedy iterative removal* procedure that recomputes the median after each set of removals and selects points based on the *change* in distance (δ_i), not on their individual gradient deviation from a fixed reference. The paper acknowledges the greedy approximation (line 97: "we propose a greedy approximation") but never discusses whether the theoretical bounds transfer to the iterative procedure, what the approximation error is, or whether the greedy selection criterion δ_i preserves the guarantees. Since the paper's central claimed contribution (C2) is presenting theoretical guarantees "demonstrat[ing] Medix achieves a low error rate," this gap between the analyzed object and the executed algorithm is significant.

2. **Missing the most directly comparable baseline (SAL / Du et al. 2024a) from the empirical comparison tables.** The paper cites Du et al. (2024a) as "the only work that provides such a foundation for the 'in-the-wild' setting" (line 21) and references it throughout. Yet SAL (Du et al., 2024a) does not appear in Tables 1 or 2. Given that SAL addresses the identical problem setup (unlabeled wild data, two-stage filtering+training, theoretical guarantees, same evaluation benchmarks), its absence from the main comparison is a significant omission that makes it difficult to assess Medix's relative contribution.

3. **CONJ and DRL are listed among the baselines but omitted from the main results.** Lines 178–179 state that "we included more recent baselines, including CONJ (Peng et al., 2024) and DRL (Zhang et al., 2024), to provide a more thorough evaluation." Neither appears in Tables 1 or 2. If these results exist in the appendix, they should be in the main tables; if not, the claim of comparing against "20 baselines" is misleading.

4. **Unclear whether the WOODS comparison is fair.** The paper states (Section 6) that "Katz-Samuels et al. (2022a); Du et al. (2024a) operate under the assumption of batch-level mixing" while Medix "enables dataset-level mixing without relying on batch-level structure." However, the paper also states (line 174) that it "use[s] the same experimental protocol as Katz-Samuels et al. (2022a)." It is never clarified whether WOODS was re-implemented with dataset-level mixing (for which it was not designed) or batch-level mixing (which would be a different data regime from Medix). Either choice could skew the comparison.

### Minor

1. **The theoretical bounds are loose and their practical implications are unexamined.** The contamination term π/[2(1−π)] in Theorem 4.1 gives ERR_in ≥ 0.33 at π=0.4 and 0.5 at π=0.5, far above the paper's empirical error rates (~12.5% in Figure 2). While upper bounds need not be tight, the paper should discuss this looseness and clarify what value the bounds provide beyond the trivial observation that error is ≤ 1.

2. **The synthetic 2D experiment (Figure 2) has limited evidential value.** The OOD mean is placed at [20, 2√3] while InD means are within about 3.5 units of each other — an extremely large separation (distance ~20+). This does not test the challenging near-OOD regime or demonstrate that the method scales to high-dimensional image data.

3. **Computational cost is not discussed in the main text.** Algorithm 1 requires computing the leave-one-out EWM for every sample in the current set at each iteration. Even with the top-k batching (k up to 20k), the naive complexity is O(m²·d) per iteration. The paper defers efficiency analysis to the appendix (A.6), leaving the reader to wonder whether the method is practical at scale.

4. **No explicit convergence analysis of the iterative removal process.** The stopping criterion (|δ_max| < ε) is motivated by the monotonically-increasing deviation observed in Figure 1, but that figure was generated by *adding* OOD samples, not by the greedy *removal* process. There is no empirical or theoretical analysis of whether the greedy removal converges, or to what.

### Trivial

- None.

## Nice-to-Haves

- Ablation study comparing Medix's greedy iterative procedure against a simpler single-pass filter (computing gradient deviation from a pre-computed EWM threshold), to isolate the benefit of the iterative approach.
- Experiments across different contamination ratios π (e.g., 0.2, 0.3, 0.4, 0.6) to test the theoretical boundary π < 0.5 and the robustness of empirical performance.
- Discussion of failure modes: what happens when OOD gradients are close to InD gradients (near-OOD, domain shift within InD classes).

## Removed Points

- **"Theoretical bounds are too weak/loose to be meaningful"** — The harsh critic argued that the bounds are so loose as to lack practical value. This conflates the purpose of upper bounds (which need not be tight to be informative about structural properties like the π < 0.5 threshold) with empirical error rate prediction. The paper does not claim tightness. Downgraded to Minor weakness 1.

- **"Computational cost is prohibitive"** — The paper states that efficiency analysis is presented in Appendix A.6, which is stripped by the parser. Per instructions, criticisms based on content known to exist in the stripped appendix are removed. Downgraded to Minor weakness 3 (as a main-text omission).

- **"OE is designed for clean auxiliary OOD sets, not contaminated wild data"** — The paper explicitly acknowledges this (line 31, abstract) and still includes OE as a standard baseline. This is a well-known limitation of OE; the paper is transparent about it and includes it as a reference method, not as a fair comparison on its own terms. Removed as scope creep.

- **"Sub-Gaussian i.i.d. assumption is questionable because gradients share a feature extractor"** — This is a standard (and nearly universal) simplifying assumption in theoretical ML papers. Many accepted papers make stronger assumptions. The paper also provides empirical validation of sub-Gaussianity (Figures 4a/4b) and a looser bound without the sub-Gaussian assumption (Theorem C.3). Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews identify the theory-algorithm gap and the missing baselines, but these are observations about what the paper lacks rather than novel synthèse of what it reveals. The core observation — that the median-based approach for wild-data filtering could be effective — is well-articulated by the paper itself.

## Suggestions

1. **Align the theory with the algorithm.** Either (a) prove that the greedy iterative procedure's output set has error controlled by the stated bounds (e.g., via a monotonicity argument or by bounding the approximation error of the greedy procedure relative to the optimal solution of Eq. 4), or (b) replace Algorithm 1 with a static filter (e.g., one-step EWM thresholding) that directly matches the theoretical analysis. Without this, the theoretical contribution is disconnected from the method.

2. **Add SAL (Du et al., 2024a) and the other mentioned baselines (CONJ, DRL) to the main comparison tables.** SAL is the most closely related work; its omission from the empirical comparison is a gap that must be filled.

3. **Clarify the WOODS experimental setup.** State explicitly whether WOODS was run with batch-level or dataset-level mixing, and if the latter, note how this deviates from its original design.

4. **Add a computational complexity section to the main text.** Even a brief analysis (e.g., "each iteration costs O(m²·d), but in practice we observe convergence within T iterations, and Appendix A.6 shows wall-clock times") would address the practicality question.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>