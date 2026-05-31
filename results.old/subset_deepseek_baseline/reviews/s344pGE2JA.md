## Summary
This paper extends influence functions to a category-wise setting, introducing an *influence vector* that quantifies each training sample’s impact on every class. Using these vectors, the authors propose a linear‑programming plus genetic‑algorithm framework (PARETO‑LP‑GA) to reweight training samples and achieve Pareto improvements—where performance on a targeted set of classes improves without severely harming others. The method is validated on synthetic binary data and on CIFAR‑10, showing positive results for two use cases: direct improvement of low‑performing classes and course correction after a detrimental epoch.

## Strengths
- **Novel perspective**: The paper shifts the focus from overall accuracy to category‑wise Pareto frontiers, a natural and important extension that is largely overlooked in the data‑centric learning literature.
- **Clear synthetic verification**: The synthetic experiments in Figure 2 convincingly show that the proposed influence vectors capture the expected tradeoffs (joint detrimental, joint beneficial, and conflicting influences), lending intuition to the approach.
- **Empirical correlation**: The strong Spearman correlations ( > 0.8) between cumulative category‑wise influence and actual accuracy changes (Figures 3–4) demonstrate that the influence vectors are predictive of performance shifts.

## Weaknesses
### Fatal
- **Missing baseline for Direct Improvement (DI)**: In Table 1 (left), the paper shows “Epoch‑10” and “Epoch‑11 (DI)” but does **not** report what the original (unweighted) Epoch‑11 accuracy would have been. Without this baseline, it is impossible to determine whether the 16% and 11% gains in classes 0/2 are actually due to the method or merely part of the normal training trajectory. This omission fundamentally undermines the claimed improvement.

### Major
- **No comparison to any baseline method**: The paper evaluates PARETO‑LP‑GA in isolation. There is no comparison with simpler alternatives (e.g., removing samples with negative overall influence, random re‑weighting, or static importance weighting). The reader has no sense of whether the complexity of LP+GA provides added value.
- **Weak theoretical foundation for the “performance ceiling”**: The condition for reaching the Pareto frontier is given informally (samples lie on the line y = –x for two classes). For the multi‑class case the paper relies on a PCA heuristic; no rigorous guarantee or characterization is provided. The phrase “performance ceiling” is used repeatedly but remains ill‑defined.
- **Limited experimental scope of the main method**: PARETO‑LP‑GA is demonstrated only on CIFAR‑10. The text datasets and STL‑10 are used only to validate the influence vectors, not the actual re‑weighting framework. The paper dismisses them because “models achieved high accuracy early”, but this raises concerns about the general applicability of the method when significant tradeoffs exist.

### Minor
- **Computational cost not discussed**: Each GA iteration requires solving a linear program, and the algorithm involves training a model for one epoch per candidate solution. The paper neither reports runtime for CIFAR‑10 nor discusses scalability to larger datasets or deeper models.
- **Fitness function implementation details**: The −∞ penalty in Algorithm 1 is ambiguous (how is it handled numerically in the GA?). GA operations (selection, crossover, mutation) are not specified, making reproducibility harder despite the provided code.

### Trivial
- Figure 1 caption repeats three times.

## Nice‑to‑Haves
- An ablation study separating the contributions of the influence vector, the linear program, and the genetic algorithm.
- Experiments on datasets with more classes or naturally imbalanced class performance to better test the tradeoff behavior.
- A discussion of sensitivity to the influence function approximation method (EKFac vs. others).

## Novel Insights
None beyond the paper’s own contributions.

## Suggestions
1. **Add the missing baseline** for the Direct Improvement experiment: report the original Epoch‑11 accuracies from standard training.
2. **Include at least one simple baseline** such as (a) removing the top x% detrimental samples by overall influence and retraining, or (b) using fixed per‑class importance weights derived from validation performance.
3. **Clarify the theoretical condition** for the Pareto frontier: either provide a derivation or clearly state the assumptions under which the influence‑vector hyperplane condition holds.
4. **Run PARETO‑LP‑GA on at least one more dataset** where tradeoffs are present (e.g., a long‑tailed dataset or an imbalanced version of CIFAR‑10).
5. **Report computational time** and discuss scalability.

## Score and Decision
MY FINAL SCORE: <score>4</score>  
MY FINAL DECISION: <decision>Reject</decision>