## Summary

This paper proposes *category-wise influence functions*, which extend classical influence functions (Koh & Liang, 2017) to produce a per-sample influence *vector* of length K (one score per class), enabling class-level analysis of training sample effects. Using these vectors, the authors characterize whether a classifier has reached its "performance ceiling" via a Pareto frontier analysis, and introduce PARETO-LP-GA — a linear programming–based sample reweighting framework, with a genetic algorithm to search class-wise performance thresholds, for achieving Pareto improvements across classes.

---

## Strengths

- **Intuitive and practical extension:** The decomposition of influence into class-specific scores is a natural and practically useful generalization. The geometric visualization in Figure 1 (influence space with joint positive/negative and tradeoff regions) is elegant and illustrative.
- **Strong empirical validation of the influence estimation itself:** Spearman correlation coefficients ≥ 0.82 between predicted class-wise influence scores and actual per-class accuracy changes (after leave-out retraining) across CIFAR-10 and Emotion datasets are compelling. This validates the core category-wise influence estimation clearly.
- **Insightful observation about combinations:** The paper makes a genuinely useful point that even when all individual training samples lie in "tradeoff regions," reweighted combinations can achieve joint improvements — motivating the LP-based framework.
- **Two practical usage modes:** The distinction between *Direct Improvement* (proactive targeting of weak classes) and *Course Correction* (reactive fix for a detrimental epoch) is a sensible decomposition of real developer workflows.

---

## Weaknesses

### Fatal
None.

### Major

1. **The "performance ceiling" claim is significantly oversold.** The paper's title and introduction promise to answer "what is the performance ceiling of my classifier?" but the actual method only provides a binary indicator of whether improvement *room exists* (via a PCA-based heuristic on influence vectors) and a one-step reweighting to improve performance. The paper never estimates the actual ceiling — no upper bound on per-class accuracy is derived or approximated. The framing conflates "is the model on the Pareto frontier?" with "what is the Pareto frontier?" These are fundamentally different questions.

2. **The Pareto frontier condition is theoretically underspecified.** The paper claims the Pareto frontier is achieved when all influence vectors lie on a hyperplane. The geometric argument in Section 3.3 is only developed for the 2-class case, and even there the condition is stated informally. For K > 2 classes, the condition (all vectors on the hyperplane $\sum_k P^k(z) = 0$) is stated but not formally justified. The PCA-based operational check (first principal component explains > 20% variance ⟹ room for improvement) is ad hoc — it is neither derived from the theory nor calibrated against any ground truth.

3. **PARETO-LP-GA is evaluated on a single dataset with no baselines.** Table 1 covers only CIFAR-10. The paper explicitly excludes text/STL-10 because "NLP models achieved >90% accuracy" and "STL-10 images are cleaner" — i.e., the method is demonstrated only where a large performance gap already exists. More critically, there is no comparison against simple alternatives: class-weighted loss (inverse-frequency weighting), focal loss, or even uniform over-/undersampling of weak classes. Without such baselines, it is impossible to judge whether the LP+GA machinery provides value beyond these trivial approaches.

4. **In DI, class 8 drops by 2.90%** (from 0.948 → 0.920), which is a non-trivial degradation. The paper characterizes this as "very minimal" without justification, yet 2.90% could be significant in practice. Additionally, the improvements in DI are confounded with the effect of simply training one more epoch (the baseline is epoch-10 vs. epoch-11 with reweighting, but there is no "epoch-11 without reweighting" shown).

### Minor

1. **Notation ambiguity in Section 3.3.** Equation (1) uses validation set $V$, but in Section 3.3 the category-wise influence is defined as $P^k(z) = \mathcal{I}^{\hat{\theta}}(z, S^k)$. It is not explicitly stated that $S^k$ here refers to the class-$k$ subset of the *validation* set — readers may confuse it with the training set subset.

2. **Fitness function in Algorithm 1 (Line 7) is potentially problematic.** Using $-\infty$ for any target-class degradation can cause hard population collapse in the GA if many or all individuals in a generation fail the target constraint. A smooth penalty or soft constraint would be more robust.

3. **The threshold for the PCA-based improvement criterion (> 0.2 explained variance) is unexplained.** Why 0.2? There is no ablation or justification for this value.

### Trivial

- Minor grammatical error: "ensuring their is room for potential improvement" (Section 5.2).

---

## Nice-to-Haves

- A comparison against simple class-reweighting baselines in Table 1 would substantially strengthen the case for the LP+GA framework.
- Extending the PARETO-LP-GA evaluation to at least one text benchmark (even if accuracy is already high, demonstrating that the method doesn't *harm* performance would be informative).
- A more careful discussion of how the "performance ceiling" detection threshold (PCA variance > 0.2) was chosen, perhaps with a sensitivity analysis.

---

## Novel Insights

The most genuine contribution is the observation (Section 3.3) that sample-level influence vectors can be summed with weights, and therefore the reachable influence "directions" form a cone — meaning that even when no single sample has jointly positive influence for all classes, a weighted combination might. This recasts the data curation problem from binary (include/exclude) to continuous (reweight), which is a meaningful conceptual step. The geometric framing of the Pareto frontier in influence space (Figure 1) is the paper's strongest insight and provides a useful mental model for practitioners doing class-specific model improvement.

---

## Suggestions

- Add an "epoch-11 without reweighting" baseline in Table 1 to decouple the benefit of additional training from the benefit of the reweighting scheme.
- Formally extend the Pareto frontier hyperplane condition to K > 2 classes with a proof or at least a clear statement of assumptions.
- Provide ablations: (a) LP-only without GA (fixed thresholds), (b) GA-only without LP (uniform per-class weights), (c) simple inverse-frequency class reweighting — to isolate where the gain in PARETO-LP-GA actually comes from.

---

## Score and Decision

The paper targets an interesting and practically relevant problem, and the validation of category-wise influence estimation (the core technical contribution) is convincing. However, the headline claim — estimating the "performance ceiling" of a classifier — is substantially oversold: the method detects room for improvement and takes a step toward it, but does not characterize or approximate an actual ceiling. The PARETO-LP-GA evaluation is restricted to a single dataset with no baselines, leaving the practical value of the combined LP+GA mechanism unsubstantiated relative to simpler alternatives. These are not fatal flaws, but they significantly limit confidence in the method's broader value.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>