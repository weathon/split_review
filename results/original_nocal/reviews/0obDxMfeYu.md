Now I have all the information I need. Let me synthesize the final review.

## Summary

The paper proposes Medix, a framework for OOD detection that uses the element-wise median (EWM) of gradient vectors to filter outliers from unlabeled in-the-wild data, then trains a binary OOD detector on the identified outliers and labeled InD data. The key novelty is the median-centric outlier filtering stage, supported by theoretical bounds on inlier/outlier misclassification rates (Theorems 4.1 and 4.2) that decompose error into contamination, concentration, and separation effects. Empirically, Medix is evaluated against 20 baselines across 11 InD-OOD pairs on CIFAR-10/100, reporting the best average FPR95 and AUROC in all settings.

## Strengths

1. **Novel and principled use of gradient median for outlier filtering**: Applying the element-wise median of gradient vectors to identify OOD samples in unlabeled wild mixtures is a creative and well-motivated idea. The median's known robustness to contamination (up to π < 0.5) is leveraged in a new domain, and the paper provides both theoretical bounds and empirical validation of this connection.

2. **Consistent state-of-the-art performance across 20 baselines**: On CIFAR-10 (Table 1), Medix achieves an average FPR95 of 0.80% and AUROC of 99.74%, versus the next best (WOODS) at 3.40% and 98.92% — a ~76% relative reduction in FPR95. On CIFAR-100 (Table 2), Medix's average FPR95 is 5.42% vs. WOODS's 6.74%. Results are reported with standard deviations over five runs, showing reproducibility. Critically, the paper explicitly acknowledges that Medix is trained on only 25k InD samples while InD-only baselines use the full 50k (line 186), making the comparison conservative.

3. **Two-sided theoretical misclassification bounds**: Theorems 4.1 and 4.2 jointly bound both inlier and outlier misclassification rates for median-based filtering, decomposing error into interpretable contamination, concentration, and separation terms. The bounds are not vacuous — they show the error remains controlled as long as π < 0.5. Remark 4.3 provides empirical evidence for the sub-Gaussian assumption, and the paper states that a looser bound (Theorem C.3) holds under only bounded second moments, showing robustness to the distributional assumption.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between theoretical analysis and the actual algorithm**: Theorems 4.1 and 4.2 analyze a static "EWM filtering rule" — a one-shot decision about whether a point deviates from the median. In contrast, Algorithm 1 is an iterative greedy procedure that: (a) computes the median of the *current* set S, (b) evaluates leave-one-out drops for every remaining sample, (c) removes the top-k, and (d) repeats. The iterative nature, the leave-one-out selection, batch removal (k > 1), and the termination condition based on δ_max are absent from the theoretical model. The bounds involve m_in and m_out (unknown subset sizes) and the median of the *whole* wild set, but the algorithm's median changes each iteration. The paper claims contribution C2 as "theoretical guarantees for the robustness of median-based filtering" — this is strictly true for median-based filtering conceptually, but the claim that the guarantees apply to Medix *as implemented* is overstated. This does not invalidate the paper (the core insight — median robustness in mixtures — directly motivates and explains why the algorithm works), but the theory is clearly analyzing a simplified version of the method.

2. **No ablation that isolates the filtering mechanism's contribution**: The paper's central novelty is the median-based outlier filtering stage. Yet no experiment compares Medix against a variant that either (a) treats *all* wild samples as OOD negatives (removing the filtering step entirely) or (b) uses a random subset of wild data as OOD negatives. Without these, it is difficult to attribute performance gains specifically to the median-based selection mechanism versus the mere availability of additional wild training data for the binary detector. The comparisons with WOODS and OE provide *some* control (they also use wild data without Medix's filtering), making this less than a fatal omission, but a direct within-Medix ablation would be far cleaner.

### Minor

1. **Convergence criterion is empirically motivated but not theoretically justified**: The algorithm stops when |δ_max| < ε, inspired by Figure 1's observation that deviation grows monotonically as OOD samples are *added* to a fixed InD base. The algorithm works in the opposite direction (removing points), and the paper provides no proof that the monotonic trend observed during addition implies the same during removal, nor any analysis connecting the stopping condition to the correctness of the outlier set. The criterion is intuitive but heuristic.

2. **No experiments varying the contamination proportion π**: All experiments fix π = 0.5. The theoretical bound degrades as π approaches 0.5 (the contamination term π/[2(1-π)] diverges), so testing π values both above and below 0.5 (e.g., 0.2, 0.4, 0.6) would strengthen the empirical validation of the theoretical claims and demonstrate robustness across contamination levels.

3. **Synthetic 2D experiment uses an unrealistically easy setup**: The OOD cluster mean [20, 2√3] is far from all three InD cluster means (within 2 units of the origin). The resulting 87.5% outlier extraction rate is illustrative but provides weak evidence for real-world performance given the large separation.

### Trivial
- None of note.

## Nice-to-Haves

- A "no filtering" ablation within Medix (use all wild data as negatives) would cleanly isolate the median filtering contribution.
- Wall-clock runtime or iteration counts for Algorithm 1 would help assess practical feasibility, though the paper states Appendix A.6 addresses this.
- Varying the contamination proportion π and showing that Medix's performance degrades gracefully would empirically corroborate the theoretical bounds.

## Removed Points

These points were flagged by reviewers but are removed with justification:

1. **"Uncontrolled baseline comparison / data split unfairness"** — REMOVED. The paper explicitly states (line 186) that InD-only baselines train on the *full* 50k CIFAR-100 set while Medix uses only 25k. Far from being unfair to Medix, this gives the baselines an advantage. The paper's acknowledgment makes this clear.

2. **"Computational impracticality of Algorithm 1"** — REMOVED. The paper states that Appendix A.6 evaluates computation and memory efficiency. The appendix is stripped by the PDF parser; penalizing its absence would be incorrect.

3. **"Missing related works"** — REMOVED per policy: external knowledge cannot confirm whether cited works exist.

4. **"Lack of variance on baseline entries"** — REMOVED. The paper provides ± values for Medix's results, which is standard. Many benchmark papers do not report error bars for all baselines when following established protocols.

5. **"Theory assumes known OOD gradient mean"** — REMOVED. This is a standard separation-assumption type of bound. The condition ‖μ_out − ∇̄_in‖₂ ≥ Δ√d is a structural assumption about the data, not a requirement that the mean be known to the algorithm.

6. **"Generic criticism about optimization not being solved exactly"** — REMOVED. The paper acknowledges Eq. (4) is computationally prohibitive and proposes a greedy approximation (Algorithm 1), which is standard practice.

7. **"i.i.d. assumption too strong"** — Partially addressed by Remark 4.3 providing empirical support and by the looser bound (Theorem C.3) that removes sub-Gaussianity. Kept as a general concern but downgraded from the original framing.

8. **Strength: "Provable two-sided robustness bounds"** — Kept as valid. The bounds exist and are a strength, though tempered by the theory-algorithm gap noted in Weaknesses.

9. **Strength: "Empirical validation of sub-Gaussian assumption"** — Kept as valid supporting evidence.

10. **Strength: "Low outlier extraction error on synthetic data (12.5%)"** — Kept but noted as a simple illustration rather than strong evidence.

## Novel Insights

None beyond the paper's own contributions. The core observation that the element-wise median of gradient vectors provides a robust signal for filtering outliers from wild mixtures is the paper's own contribution; the reviews do not add independent insight beyond noting the theory-algorithm gap.

## Suggestions

1. **Bring the theory in line with the algorithm**: Either (a) analyze the iterative greedy procedure itself (bound the number of iterations, the effect of batch removal, and the convergence criterion), or (b) reframe Algorithm 1 as a heuristic approximation and characterize the theory as analyzing a simplified but conceptually related decision rule. A clear statement of what the theory covers and what it does not would resolve the gap.

2. **Add a "no filtering" ablation**: Train Medix's binary detector using the entire wild set as OOD negatives (skipping the filtering stage) and compare performance. This directly measures whether median-based filtering adds value over simply training on all wild data.

3. **Vary the contamination proportion π**: Report Medix's FPR95 and AUROC for at least one InD-OOD pair at π ∈ {0.2, 0.4, 0.6} to empirically validate the theoretical claim that the bound degrades as π → 0.5.

4. **Clarify the training data for all baselines**: While the paper acknowledges the 25k/50k split difference for InD-only methods, explicitly state whether wild-data baselines (WOODS, OE) also use the reduced 25k InD set or the full 50k for a completely transparent comparison.

## Score and Decision

**Originality**: Good. The median-centric perspective for filtering wild data is novel and creatively transfers a known robust statistic to a new problem domain.

**Importance of research question**: High. OOD detection with unlabeled wild data is a practically relevant and active area.

**Claims well-supported**: Partially. Empirical claims are well-supported by comprehensive experiments. Theoretical claims are somewhat overstated relative to what is proven (theory analyzes a simplified rule, not the implemented algorithm).

**Soundness of experiments**: Good overall. The benchmark is comprehensive (20 baselines, 11 pairs), and the comparison is conservative (Medix uses less InD data). Missing the filtering ablation weakens the attribution of gains.

**Clarity of writing**: Clear. The paper is well-structured and the methodology is explained understandably.

**Value to the research community**: Positive. The median-gradient approach is a useful addition to the wild-data OOD toolkit, and the theoretical decomposition into contamination/concentration/separation effects provides conceptual clarity.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>