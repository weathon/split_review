Now I have all the context I need. Let me compose the final review.

## Summary

Medix proposes a median-centric two-stage framework for OOD detection: (1) identify outlier candidates from unlabeled wild data by iteratively removing samples whose gradients maximally shift the element-wise median (EWM) away from the InD mean gradient, and (2) train a binary OOD detector on the identified outliers plus labeled InD data. The paper provides two-sided theoretical bounds on inlier/outlier misclassification rates and evaluates across 11 InD-OOD pairs against 20 baselines.

## Strengths

- **Novel median-based filtering mechanism with strong empirical results**: The use of element-wise median of gradients for outlier extraction is a genuinely new idea in the wild-OOD setting. On CIFAR-100 (Table 2), Medix achieves avg FPR95 of 5.42% vs WOODS at 6.74% and KNN+ at 46.40%. On CIFAR-10 (Table 1), avg FPR95 of 0.80% vs WOODS at 3.40%. Improvements are consistent across all 11 InD-OOD pairs and reported with standard deviations over 5 runs, demonstrating statistical reliability.

- **Two-sided theoretical analysis with interpretable error decomposition**: Theorems 4.1 and 4.2 jointly bound both inlier and outlier misclassification rates, decomposed into contamination, concentration, and separation effects. The contamination term π/[2(1−π)] makes explicit how the bound degrades as OOD proportion approaches 50%. This is one of very few theoretical analyses for the in-the-wild OOD setting — the paper correctly notes (Section 1) that Du et al. (2024a) is the only prior work providing such a foundation. The paper also provides a looser bound under merely bounded second moments (Theorem C.3), removing the sub-Gaussian assumption.

- **Dataset-level mixing without batch structure**: The paper identifies (Section 6) that Katz-Samuels et al. (2022a) and Du et al. (2024a) assume batch-level mixing with fixed InD/OOD ratios per batch, which is unrealistic for large outsourced datasets. Medix works at dataset-level mixing, a genuinely more practical setting, and cites this as a distinguishing advantage.

## Weaknesses

### Major

1. **Theoretical bounds are too loose to explain empirical performance at the experimental setting (π = 0.5).** All main experiments use π = 0.5 (equal InD and OOD in the wild data). At this value, the contamination term in Theorem 4.1 is π/[2(1−π)] = 0.5/(2×0.5) = **0.5**, and in Theorem 4.2 it is (1−π)/(2π) = **0.5**. This means ERR_in ≤ 0.5 + vanishing concentration terms and ERR_out ≤ 0.5 + separation + concentration — guarantees no better than random guessing. The abstract claims the bounds "demonstrate Medix achieves a low error rate" and the text states the bounds "remain controlled" (line 138), which is technically true but misleading at the experimental π. The strong empirical results (FPR95 of 0.80–5.42%) operate in a regime the theory does not explain, and the paper does not reconcile this gap. This is not fatal — many ML papers have bounds that are not tight — but the paper oversells what the theory guarantees.

2. **Main evaluation uses wild OOD data drawn from the same distribution as test OOD data.** The paper constructs wild data by mixing InD CIFAR with the *same* OOD dataset used for testing (line 170: "when using PLACES365 as an OOD test set, we construct a wild mixture by combining CIFAR with PLACES365 as wild data and test on PLACES365 as the OOD set"). The abstract and conclusion describe Medix in "open-world" terms without caveat, but the primary experimental setup does not evaluate the setting where P_out^{test} ≠ P_out. The paper defers this to Appendix A.4. While this protocol follows the precedent of WOODS and Du et al. (2024a), making comparisons to those methods fair, the paper's framing as "open-world" overreaches what the main results demonstrate. A genuinely unseen-OOD evaluation should be a primary result, not an appendix.

### Minor

3. **Computational cost is uncharacterized in the main text.** The greedy algorithm (Algorithm 1) requires, at each iteration, computing gradients for all remaining samples in S, then the EWM and its distance to the InD mean gradient, then repeating this for each leave-one-out subset S\{i}. For |S_wild| = 25,000 and a Wide ResNet 40-2, this is expensive. The paper defers all efficiency analysis to Appendix A.6 without summarizing runtime, iteration count, or FLOPs in the main text, making it impossible to assess practicality from the main presentation.

4. **Hyperparameter selection may leak test information.** Hyperparameters ε and k are selected (line 178) "with the objective of maximizing OOD performance." Since the wild OOD and test OOD are from the same distribution in the main experiments, tuning to maximize OOD performance implicitly uses test-set information. A more rigorous approach would select hyperparameters without access to the test OOD distribution.

5. **Algorithm 1 stopping criterion appears logically incorrect.** The while condition is `t ≤ T or |δ_max| > ε`. With OR semantics, the loop runs at least T+1 iterations regardless of convergence (since t ≤ T is true until t > T), rendering the ε convergence check ineffective during the first T iterations. The conventional intent would use AND.

6. **Greedy approximation error is not discussed.** The algorithm removes k samples simultaneously at each iteration, but the EWM is not a linear function — removing k samples at once may produce a different effect than the sum of k individual removal effects. The paper does not discuss or validate this approximation.

7. **Synthetic 2D experiment (Figure 2) is not informative.** OOD data is placed at [20, 2√3] with variance 0.25, while InD means are within [−2, 2] and also variance 0.25 — a separation of ~18+ units. Any reasonable method would detect such outliers. This toy illustration (87.5% extraction rate) does not serve as evidence that the method works on real high-dimensional data, despite being used to claim corroboration of theory.

### Trivial

8. The "40.98% improvement" claim (FPR95 improving from 46.40% to 5.42%) is expressed as an absolute percentage-point difference but could be misread as a relative improvement. The phrasing should be clarified.

## Nice-to-Haves

- Include a runtime/iteration count summary in the main text so readers can assess practicality.
- Compare EWM against a simple mean-based baseline (not just geometric median) to validate the median-centric framing.
- Present the unseen-OOD results (Appendix A.4) as a primary table — this directly tests the open-world claim.

## Removed Points

- **"Missing related works"**: Removed per policy — I cannot confirm existence of uncited references.
- **"Weaknesses about format/style/typos/parser artifacts"**: Removed per hard rule — these are parser errors, not author errors.
- **"Unfair comparison with baselines (25k vs 50k InD samples)"**: The paper transparently acknowledges this asymmetry (line 182), and comparisons among wild-data methods are fair (all use 25k).
- **"Theory is fundamentally wrong"**: The critic's claim that bounds are "vacuous" is reframed as "too loose to explain empirical results" — the bound structure itself is informative and the analysis is sound; the issue is the paper's overclaiming, not an error in the math.
- **"Pseudo-label dependency is a major issue"**: The paper addresses this in Appendix A.5. Demoted to minor/removed — it's an acknowledged dependency with supporting analysis deferred to appendix.
- Stress finder's generic strengths ("addressed an important problem," "interesting question"): Removed per policy — lack specific evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a sentence in Section 4 honestly contextualizing the bounds at π = 0.5: explicitly state the contamination term is 0.5 and that the strong empirical performance is far better than the worst-case bound. This would close the theory-practice gap rather than papering over it.
2. Fix the Algorithm 1 stopping condition (OR → AND) and add a brief discussion of the greedy approximation error (k-simultaneous removal vs. individual removal).
3. Include wall-clock time and number of iterations for at least one representative experiment in the main text.
4. Select ε and k using a validation split that does not overlap with the test OOD distribution, or acknowledge the limitation more transparently.

## Score and Decision

**Calibration methodology:**

**Round 1 (bracketing):** Queried for papers on (a) OOD detection with unlabeled wild data and median gradient filtering (score <3.5 — returned 2.00–3.40, clearly weaker than our paper), (b) OOD detection with wild data and theoretical guarantees (score 3.5–7.5 — returned anchors at 4.00, 5.00, 5.50, 6.50), and (c) median-based OOD detection with SOTA empirical results (score >7.5 — returned 8.00 but on different topics). The most directly comparable anchor was Du et al. (2024a) "How Does Unlabeled Data Provably Help Out-of-Distribution Detection?" at **6.50** (scores 6, 8, 6, 6; Accept), which addresses the same problem setting with a two-stage framework and theoretical guarantees. Also informative: SPADE at **5.50** (Accept, OOD detection with theory but weaker empirical results), Gradient Norm at **5.50** (Reject, different problem), and GROD at **5.00** (Reject). Initial bracket: **5.0–6.5**.

**Round 2 (narrowing):** Queried for gradient-based OOD detection papers with theoretical guarantees in the 5.0–7.0 range. Retrieved SPADE (5.50), Gradient Norm (5.50), Double Descent (6.50), and Perturb-and-Compare (5.25). Reading full reviews confirmed the bracket.

**Final score determination:** Our paper compares favorably to SPADE (5.50, Accept — which had weak empirical results uniformly dominated by baselines per its reviewers, while our empirical results are consistently SOTA). Compared to Du et al. 2024a (6.50, Accept), our paper has a genuinely different and novel filtering mechanism (EWM gradients vs. top singular value) and stronger empirical margins, but also has weaker theoretical bounds at the experimental π=0.5 and a less rigorous characterization of computational cost. These offsetting factors place our paper slightly below Du et al. 2024a.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>