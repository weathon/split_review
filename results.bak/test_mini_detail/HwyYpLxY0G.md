Now I have all the information needed. Let me compile the final review.

## Summary

The paper proposes Aligned Scoring Rules (ASR), which optimizes proper scoring rules for textual elicitation to align with human preferences while maintaining provable truthfulness. The key idea is to minimize the MSE between a proper scoring rule (constrained to the space of "separate" scoring rules for know-it-or-not reports) and a non-proper reference score (e.g., instructor score or LLM-Judge score). The optimization over separate scoring rules is convex (Corollary 3.4), enabling efficient gradient-based methods, and the resulting rule preserves properness guarantees from the Elicitation^GPT framework. Experiments on peer grading data report that ASR improves alignment over non-aligned truthful baselines across MSE, Pearson, and Spearman metrics.

## Strengths

- **Novel and principled formulation.** The idea of optimizing a proper scoring rule to match a reference score while preserving truthfulness is genuinely novel. The convexity of the optimization over separate scoring rules (Corollary 3.4) is a clean and theoretically sound result, enabling efficient optimization with provable convergence.

- **Properness guarantee preserved during alignment.** The paper correctly builds on the Elicitation^GPT reduction (Theorem 3.2) and constrains the scoring rule to the space of proper scoring rules for know-it-or-not reports (Definition 2.5, Program 2). This ensures the aligned rule remains truthful, unlike the non-proper reference scores it targets.

- **Interpretability through convexity.** The separate scoring rule formulation (weighted average of single-dimensional rules) allows ASR to identify which rubric dimensions are important, as each single-dimensional rule's convexity reveals its contribution. The paper references a case demonstration showing this interpretability.

- **Real-world evaluation on genuine peer grading data.** The experiments use 22 assignments from two undergraduate algorithm classes with actual instructor reviews and peer reviews, providing a realistic testbed rather than synthetic data.

- **Comparison against two distinct reference scores.** ASR is aligned to both instructor scores and LLM-Judge scores with qualitatively similar improvements over baselines (Table 1, both panels), suggesting the method's robustness to the choice of reference.

## Weaknesses

### Major

1. **No train/test split — reported metrics likely in-sample.** The paper never specifies whether the MSE, Pearson, and Spearman values in Table 1 and the regression in Figure 4 are computed on held-out data. The only mention of "training data" appears in the definition of the Constant baseline (line 417: "the mean of the reference scores *s* in the training data *D*"). If ASR is optimized and evaluated on the same data, the near-identity fit in Figure 4 is an expected consequence of minimizing MSE on that dataset and conveys nothing about generalization. The core empirical claim — that ASR "outperforms previous methods" — would not be supported by in-sample numbers. This is the most significant methodological gap and requires either cross-validation or a clear train/test separation to interpret the results.

2. **Scale mismatch inflates MSE comparisons against baselines.** The V-shaped scoring rule used by EGPT(AV) and EGPT(MV) outputs values in [0, ½] (Definition 2.4). The reference scores are normalized to [0, 1] (line 286: "s normalized to [0, 1]"), and ASR is optimized to match this range. Comparing raw MSE between ASR (range [0,1]) and EGPT(AV) (range [0,½]) against a [0,1] reference systematically penalizes the baselines because their scores are on a different scale. The paper acknowledges the scale issue only in a footnote about Spearman correlation (footnote 3) but does not correct for MSE and Pearson. The Constant baseline (3.741 vs. 1.730) does not suffer from this issue and thus provides a fairer, though still in-sample, comparison.

### Minor

3. **Know-it-or-not assumption stated but not empirically verified.** Assumption 2.2 — that posterior beliefs are either 0, 1, or the prior — is the foundation of the ternary report space. The paper asserts "we observe that textual reports either express a state being 0 or 1, or have no information" (Section 2.2) but provides no quantitative evidence (e.g., what fraction of reports fall into each category, whether intermediate expressions ever occur). Without this verification, the scope of the properness guarantee for the actual dataset is unclear.

4. **No statistical significance or confidence intervals.** The dataset contains ~500 reviews across 22 assignments. The paper reports point estimates for MSE and correlation but never reports standard errors, confidence intervals, or significance tests. Given the potential for cluster-level variability (assignments may differ substantially), the reader cannot assess whether the reported differences between methods are robust.

5. **Oracle quality not reported.** The properness guarantee (Theorem 3.2) requires the question-answering oracle to be non-inverting (error rate < ½). The paper does not report any accuracy or error-rate measurement for the oracle on a labeled sample, leaving this as an untested assumption for the empirical instantiation.

### Trivial

6. The optimization objective (Program 1) normalizes the reference score *s* to [0, 1], but the normalization procedure itself is not described (min-max scaling? z-score?).

## Nice-to-Haves

- Include a hold-out evaluation (e.g., leave-one-assignment-out cross-validation) with means and standard deviations across folds to support generalization claims.
- Scale baseline scoring rules (EGPT AV/MV) to the reference score's range using a simple linear mapping before computing MSE and Pearson, isolating the effect of alignment from scale.
- Report error bars or standard errors for all main metrics, especially given the clustered data structure.
- Provide a histogram showing the distribution of reports over {0, 1, ⟂} per dimension to verify the know-it-or-not assumption.

## Removed Points

These points were flagged by the reviewers but are removed for the reasons given:

- **"Missing appendix materials" / "missing case demonstrations" / "missing proofs in appendix"** — Removed because the parser strips appendix content from all papers; these exist in the original submission.
- **"Computational cost not discussed"** — Removed as a nice-to-have that does not affect the core contribution.
- **"Optimization over separate scoring rules only — why not other aggregation forms?"** — Removed. The paper acknowledges that max-over-separate is non-convex (Section 3.2), which is a sufficient justification for scoping to separate scoring rules. This is a reasonable design choice, not a flaw.
- **"Missing related works"** — Removed per instructions (cannot confirm existence of gaps without external knowledge).
- **"The example interpretability case is referenced but not present"** — Removed (appendix stripped by parser).
- **"Missing train/test split description is the most significant missing piece" (as a separate point)** — Merged into Weakness #1, not a separate weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same core tension: the theoretical framework is clean and novel, but the empirical evaluation is insufficiently rigorous to support the claimed performance improvements. No reviewer identified a flaw in the theory or an application the authors missed.

## Suggestions

1. **Add cross-validation or an explicit train/test split.** This is the single most important change. Report MSE, Pearson, and Spearman on held-out assignments, with mean and standard deviation across folds. Without this, the empirical results are uninterpretable as evidence of generalization.

2. **Address the scale mismatch with baselines.** Either rescale baseline scores to [0, 1] via a linear mapping before computing MSE, or note clearly that the comparison is asymmetric and provide the fair re-scaled numbers.

3. **Verify the know-it-or-not assumption empirically.** A simple histogram showing the proportion of {0, 1, ⟂} reports across all summary points would significantly strengthen confidence in the framework's applicability.

4. **Report oracle accuracy on a small hand-labeled sample.** Even 50-100 examples would suffice to check whether the error rate is below ½, connecting Theorem 3.2 to practice.

5. **Add error bars or standard errors** to all main metrics, ideally accounting for the clustered assignment structure of the data.

## Score and Decision

### Calibration Details

**Round 1 (Bracketing):** Three queries on "scoring rules proper scoring rule peer grading mechanism design information elicitation" split by score band.

- Low band (<3.5): Retrieved papers at ~3.0 (all Reject). Examples: data valuation, risk quadrangle, time series evaluation — topically distant from this paper but showing that papers at this score have fundamental flaws.
- Middle band (3.5–7.5): Retrieved oQKKlzxV1o (6.75, Accept Poster) — mechanism design with scoring rules; X0epAjg0hd (5.67, Accept Poster) — calibration theory+empirics; XM7INBbvwT (4.67, Reject) — calibration HCI study; and others.
- High band (>7.5): Retrieved papers at 8.00 (all Accept Oral) — these have strong theory, thorough evaluation, and clear contributions.

**Round 2 (Narrowing, 4.5–6.5):** Queries on "mechanism design information elicitation peer grading" and "scoring rules text elicitation language models truthful alignment convex optimization."

- 488A64eOf6 (6.25, Accept Poster) — LLM decoding as metrics optimization. Strong theory + comprehensive empirical evaluation across multiple tasks, metrics, ablations, and human eval. ASR is clearly weaker on empirical evaluation.
- ULGbw2URE3 (5.50, Accept Poster) — L3Ms for constrained LLM alignment. Similar structure (novel formulation + limited experiments), but L3M's evaluation, while limited, includes proper train/test separation that ASR lacks.
- mDEYl0Ucgr (5.25, Reject) — Influencing humans for RLHF. Well-executed human studies with practical applicability concerns. ASR has stronger theory but weaker evaluation methodology.
- rTM95kwzXM (5.25, Reject), DTjmv5QJBx (5.50, Reject), CrGfGLC2Ad (5.33, Reject) — All in the 5.0–5.5 range, rejected primarily due to evaluation limitations or limited scope.

**Initial bracket:** 4.0–6.0. **After narrowing:** The paper is comparable to the ~5.0–5.5 rejected papers: it has a genuinely novel idea and clean theory, but the empirical methodology gaps (no train/test split, scale mismatch) are more consequential than typical minor weaknesses. Unlike the Accept-level anchors at 5.5–6.5, the ASR evaluation lacks basic safeguards against overfitting. Hence the score sits at 5.0 — marginally below acceptance threshold, with a clear path to improvement.

### Final Assessment

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>