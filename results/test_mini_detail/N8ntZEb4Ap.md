Now I have strong calibration anchors. Let me compile the final review.

## Round-1 Bracket

Round 1 bracketed this paper between <3.5 (weak anchors like avg 2.33–3.00, rejected for fatal flaws) and >7.5 (strong anchors like avg 8.0, accept-oral). The paper clearly falls in the middle band (3.5–7.5). The most similar anchors in this band scored 4.0–5.75, all rejected or withdrawn.

## Round-2 Narrowing

DeepDRK (avg 5.75, Reject) is the closest topical match — a neural FS paper with real experiments but concerns about ablation and hyperparameter tuning. AutoNFS has a cleaner method and stronger benchmark results but a more concerning flaw (complexity claim). TDColER (avg 5.5) has comprehensive evaluation but a less clean story. The Gumbel band selection paper (avg 4.0) is weaker than AutoNFS in every dimension. I place AutoNFS around 5.0 — it has genuine contributions but the complexity overstatement is a significant issue.

---

# Consolidated Review

## Summary

AutoNFS proposes a fully differentiable neural feature selection method that uses a Gumbel-Sigmoid relaxation to learn a global feature mask jointly with a predictive model, with a cardinality penalty that lets the number of selected features emerge from optimization rather than being pre-specified. The method is evaluated on the Cherepanova et al. (2023) benchmark (11 datasets, 10 baselines, three corruption scenarios), where it achieves the best average rank in all three scenarios, and on 24 real-world metagenomic datasets, where it reduces dimensionality by ~92% while maintaining or slightly improving predictive performance.

## Strengths

- **Clean formulation for automatic feature count determination.** The use of a single cardinality penalty (L_select, Eq. 3) with λ=1 eliminates the need to pre-specify k, a practical pain point in most FS methods. Table 1 (right) shows that across 11 datasets spanning classification and regression with varying dimensionality, AutoNFS converges to a much smaller feature set (e.g., 65 out of 128 on aloi, 5 out of 8 on california) without user-specified budget.

- **Consistently top-ranked on a well-established FS benchmark.** Figure 2 shows AutoNFS (labeled GFS-NetWork) achieves the best average rank in all three corruption scenarios of the Cherepanova et al. (2023) benchmark — Corrupted: 2.1, Random: 3.9, Second-order: 3.6 — beating the next-best method (Deep Lasso) by 0.7–1.7 rank points. This is a rigorous comparison with 10 baselines across 11 datasets.

- **Selected features are demonstrably near-minimal for predictive power.** Figure 3b shows AutoNFS achieves the highest average decrease in performance (0.313) when any single selected feature is removed, directly supporting the claim that the selected set is minimally sufficient — removing any feature harms prediction.

- **Demonstrated effectiveness on real high-dimensional biological data.** On 24 metagenomic datasets (avg 535 features), AutoNFS reduces dimensionality to 41 features (7.7%) while improving average accuracy for both MLP (+0.8 pp) and Random Forest (+1.2 pp) over the full feature set, suggesting the selected features capture task-relevant information that transfers across classifiers.

## Weaknesses

### Fatal
None. The core method and its empirical results on the benchmark are not invalidated by any single verified issue.

### Major

- **The "nearly constant computational overhead" claim is not adequately supported and is theoretically questionable.** The paper asserts that AutoNFS scales as D^0.08 (near-constant) and claims this as a central advantage. However, the masking network f: ℝ^{D_e} → ℝ^D must have a final layer with O(D) parameters (it outputs D separate logits), and the task network g's first layer also takes D-dimensional input. The empirical plot (Figure 4a) showing ~10 seconds flat across D=100 to D=100,000 is surprising and requires explanation — it suggests the measurement may be dominated by fixed overhead (data loading, Python runtime) rather than correctly isolating the FS module's cost. The paper does not describe f's architecture, making this claim impossible to verify theoretically. Since this is presented as a key contribution (appearing in the abstract, introduction, and contributions list), the overstatement is a significant issue that the authors should correct or substantially qualify.

### Minor

- **Architecture of the masking network f is unspecified.** The paper states f: ℝ^{D_e} → ℝ^D but provides no details about its internal structure (number of layers, hidden dimensions, activation functions). This information is essential for reproducibility and for evaluating the computational complexity claim. (Section 3.2)

- **Several relevant neural FS baselines are not included in the benchmark.** While the paper follows the Cherepanova et al. (2023) benchmark and includes 10 baselines (including neural methods Deep Lasso, LassoNet, and AM), it omits directly related differentiable FS methods cited in the related work — Stochastic Gates (Yamada et al. 2020), Hard Concrete / L_0 gates (Louizos et al. 2017), and INVASE (Yoon et al. 2018). Including these would strengthen the claim of outperforming "neural FS methods."

- **Metagenomic experiments lack comparisons with other FS methods.** Table 2 compares only full-data vs. AutoNFS-reduced performance. Without at least one other FS baseline (e.g., Lasso, Random Forest importance, or a neural method), it is unclear whether the subsets AutoNFS selects are better than alternative subsets of the same size. The claim of "effectiveness in high-dimensional biological data" would be stronger with such comparisons.

- **The automatic determination of feature count is not thoroughly demonstrated in the main paper.** The paper fixes λ=1 for all datasets and references an ablation in Appendix F (removed by parser) for sensitivity analysis. The main paper should include at least a plot of the number of selected features vs. λ for one or two datasets, or the convergence behavior of selected features during training (referenced as Figure 5), to substantiate the claim that feature count emerges automatically.

### Trivial

- The method is called "AutoNFS" throughout the text but "GFS-NetWork" in Figures 2 and 4. While the caption notes "AutoNFS (GFS-NetWork)", the naming should be unified.

## Nice-to-Haves

- **Weaken or correct the computational complexity claim.** Dropping the "nearly constant" narrative and reporting the actual linear scaling (O(D) in the final layer) would make the paper more honest. The advantage over filter/wrapper methods that scale superlinearly is still meaningful even at O(D). The complexity experiment should isolate the FS module's cost from fixed overhead.
- **Ablate Gumbel-Sigmoid vs. a deterministic sigmoid during training** to isolate the benefit of stochasticity.
- **Show the evolution of the number of selected features during training** (through time or epochs) to demonstrate the "curriculum" effect of temperature annealing.
- **Include statistical significance tests** for the ranking results (e.g., as done in Cherepanova et al. 2023).

## Removed Points

These points were considered but removed from the main evaluation:

- **Harsh critic's "fatal" classification of the complexity issue**: The complexity overstatement is major but not fatal — it does not invalidate the core method or the benchmark results.
- **Criticism about missing appendix content / missing proofs**: The parser strips appendices; these exist in the original submission.
- **Criticism about without-FS-baselines in metagenomic being "unsupported"**: The experiment's primary goal is to show dimensionality reduction does not hurt performance (which it does), not to prove AutoNFS beats other methods on this data. The FS baseline comparison is a Minor limitation, not a fatal gap.
- **Strength finder's "nearly constant computational overhead" strength**: Conflicts with the verified weakness; removed per policy.
- **Formatting/style nitpicks (naming inconsistency)**: Downgraded from Minor to Trivial.
- **Request for more classifiers in metagenomic experiment**: The paper tests two fundamentally different classifiers (MLP and RF), which is reasonable scope.
- **Statistical significance criticism**: Generic concern without evidence that rankings would change with significance testing.

## Novel Insights

The reviews highlight a tension: AutoNFS's core methodological contribution — learning a mask with automatic cardinality via Gumbel-Sigmoid + penalty — is clean and empirically effective, but the paper overreaches with the complexity claim. This is a pattern where a solid algorithmic idea is weakened by overclaimed ancillary benefits. The practical takeaway is that the method works well and automatically determines feature count; the computational advantage over existing methods (even at O(D) rather than O(1)) is still meaningful for very high dimensions where filter methods already scale linearly and wrapper methods scale superlinearly. The key gap in evaluation is not the benchmark (which is strong) but the real-data metagenomic experiment, which would benefit from FS baselines to confirm that the selected subsets are genuinely good, not merely non-destructive.

## Suggestions

1. **Clarify the masking network architecture** (Section 3.2) — specify the number of layers, hidden dimensions, and activation functions of f. This is needed for both reproducibility and complexity analysis.
2. **Correct or substantially qualify the complexity claim.** State the actual scaling (at least O(D) for the final layer of f and the input layer of g) and explain why the empirical measurement in Figure 4a appears flat. If the measurement methodology has a legitimate explanation, describe it explicitly.
3. **Add at least 2–3 FS baselines to the metagenomic experiments** (e.g., Lasso, Random Forest importance, or one neural method) to demonstrate that AutoNFS selects better subsets than alternatives, not just any subset.
4. **Include a sensitivity plot of selected features vs. λ** in the main paper, and show the convergence of the feature count during training.
5. **Add 1–2 of the missing neural FS baselines** (STG or L0 regularization) to the benchmark comparison if feasible; otherwise, acknowledge the gap in a limitations paragraph.

## Score and Decision

**Round-1 bracket (3 queries):**  
- <3.5 band: anchor (lt6xKGGWov, avg 2.33, weak reject, major methodological flaws); anchor (2bF381xEke, avg 3.00, unclear contributions)  
- 3.5–7.5 band: anchor (PauyrluLud, avg 4.00, Gumbel band selection paper — weaker than AutoNFS); anchor (xtTut5lisc, avg 5.00, iterative feature selection — comparable flaws); anchor (0SOhDO7xI0/DeepDRK, avg 5.75, neural FS — comparable quality)  
- >7.5 band: anchor (f4gF6AIHRy, avg 8.00, accept-oral — far stronger submission)

**Round-2 narrowing:**  
- Anchor (0SOhDO7xI0/DeepDRK, avg 5.75): Neural FS paper with comprehensive experiments but complex method with many loss terms and hyperparameters. AutoNFS has a cleaner method and better benchmark positioning, but DeepDRK's flaws are less central to its narrative. **AutoNFS is slightly weaker** due to the complexity overstatement.  
- Anchor (Thnk4ez3wN/TDColER, avg 5.50): Tabular data paper with strong benchmark. Comparable evaluation quality but a different problem. **AutoNFS is comparable** in overall quality.  
- Anchor (PauyrluLud, avg 4.00): Gumbel-Softmax band selection — same technical toolkit but much weaker evaluation and more significant hyperparameter issues. **AutoNFS is clearly stronger** than this anchor.

**Final score:** 5.0. The paper has a clean, effective method and strong benchmark results, but the unsupported complexity overstatement and evaluation gaps (missing neural FS baselines, metagenomic comparisons) keep it below the acceptance threshold.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>