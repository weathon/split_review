- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 3, 5, 5, 5
Now I have all the information I need. Let me compose the final review.

## Summary

This paper proposes GESR, a geometric evolution model for symbolic regression that combines three modules: (1) semantic gradients to correct nonlinear distortions between sub-semantic and target semantic spaces during backpropagation, (2) a geometric search operator that directly approximates the target in semantic space with variance-based ranking and tree-size regularization, and (3) Levenberg-Marquardt optimization with L2 regularization for global constant adjustment and subtree pruning. The method is evaluated on SRBench (120 black-box datasets) and SRSD (120 scientific discovery datasets) against 25 baselines, with an ablation study on Friedman datasets using Wilcoxon signed-rank tests.

## Strengths

- **State-of-the-art solution rate on scientific discovery benchmarks**: GESR achieves 100.0%, 87.5%, and 58% accuracy solution rate (R² > 0.999) on easy, medium, and hard SRSD datasets, surpassing the second-ranked baseline by 23.3%, 42.5%, and 36% respectively (Table 1). These margins are large and meaningful.

- **Superior accuracy across diverse black-box problems**: On SRBench's 120 black-box datasets, GESR outperforms all 25 baseline methods in test R², with advantages in model size compared to previous semantic approaches like SBP-GP (Figure 4, box plots).

- **Ablation with statistical validation confirms component necessity**: Removing weight optimization, mutation-point selection, semantic gradients, or replacing the geometric mutation all produce statistically significant performance drops (Wilcoxon p < 1e-2 to 1e-7, Table 2), directly supporting the paper's claim that each module contributes.

- **Demonstrated noise robustness**: On Feynman and Strogatz datasets with varying Gaussian noise levels, GESR maintains the highest accuracy solution rate among all methods with stable performance (Figure 5).

- **Novel and well-motivated technical combination**: The semantic gradient formulation (Eqs. 1–3) provides a principled way to handle the nonlinear mapping distortion between sub-semantic and target semantic spaces—a problem not explicitly addressed by prior geometric semantic work. The geometric search operator (Section 3.3) explicitly incorporates diversity and overfitting safeguards (variance-based ranking, λ exploration parameter, tree-size discount factor η).

## Weaknesses

### Fatal
None.

### Major

- **No multi-run variance reporting for the headline SRSD results (Table 1).** The paper's central claim of state-of-the-art accuracy on SRSD rests on single-point solution-rate percentages with no mention of how many independent runs were performed, no standard deviations, no confidence intervals, and no statistical test attached to Table 1. This is particularly consequential because GP-based methods are known to exhibit variance across runs due to randomness in initialization, mutation selection, and termination. While Figure 4 (SRBench) uses box plots that inherently show distributional information, Table 1 has none. The ablation study demonstrates the authors know how to use statistical testing (Wilcoxon), making its absence from the main results conspicuous.

- **No reporting of GESR's computational budget.** The paper does not specify the number of generations, population size, tournament size, or function evaluations used by GESR. Without this information, it is impossible to assess whether the accuracy gains stem from the algorithmic contributions or from a larger computational budget relative to baselines. The paper acknowledges that baselines used half-grid search over parameters while GESR used fixed hyperparameters, but the raw computational cost comparison is missing entirely.

### Minor

- **Method description has several underspecified aspects.** (a) The semantic gradient computation (Eqs. 1–3) requires partial derivatives through the backpropagation path, but expression trees commonly contain nonsmooth operators (abs, sign, conditional branching) whose differentiability is not addressed. (b) The derivation of the combination coefficient k in Eq. 7 is described at a high level (least-squares minimization) but the intermediate steps are not fully laid out, requiring the reader to reverse-engineer the loss function. (c) The variance-based constraint in Eq. 9 is asserted to "ensure smoother function fitting" without any justification for why a variance ratio ≥ 1+λ achieves this effect. These ambiguities do not invalidate the method but hinder independent implementation.

- **The semantic gradient approach incurs computational overhead** that is not discussed. Computing chain-rule gradients through arbitrary expression trees at each generation, and evaluating them on all training points, is nontrivial—comparison with simpler alternatives (e.g., uniform weighting, or using the output vector directly) would clarify whether the added complexity is worthwhile.

### Trivial

- **Eq. (1) inconsistency**: The surrounding text states the goal is to "minimizes the theoretical risk" but the equation uses `argmax` instead of `argmin` over the loss ℒ. This is clearly a typo and should be corrected.

## Nice-to-Haves

- Sensitivity analysis comparing semantic gradient weighting against simpler alternatives (uniform weighting, direct output vector) on a few representative datasets.
- Wall-clock time or function-evaluation comparison between GESR and the top 3–5 baselines on a subset of datasets to decouple algorithmic advantage from compute budget.
- A hyperparameter table listing all GESR settings (population size, number of generations, λ, β, μ, η, frequency of LM optimization, number of candidate subtrees, etc.) with brief justification for the chosen fixed values.

## Removed Points

- **"The appendix may contain additional pseudocode"** — Removed per rule: criticisms about missing appendix content are not valid since the parser strips those sections.
- **"The paper does not specify training/validation splits or how R² is computed"** — Removed because Figure 4 caption explicitly says "R² test" and SRBench by convention uses held-out test sets.
- **"No error bars for Figure 4"** — Removed because Figure 4 uses box plots, which inherently display distribution (median, quartiles, outliers). The critic's framing that no variance information exists for any main result is incorrect for Figure 4.
- **"Provide pseudocode or algorithm summary in main text"** — Removed as a reproducibility nitpick about presentation rather than a substantive weakness. The method is described across three subsections with equations and a schematic (Figure 1).
- **"The related work would benefit from mentioning X, Y, Z"** — Removed per rule: missing related works should not be mentioned.
- **Strength: "Semantic gradient addresses a specific mapping distortion"** — This is kept (merged into Strengths), not removed. It is specific and evidence-grounded.

## Novel Insights

The integration of the three modules (semantic gradients, geometric search, and LM-based weight optimization) is novel, but the reviews do not surface an unexpected insight beyond the paper's own contributions. The critical observation is that the ablation confirms each module contributes independently—particularly the finding that replacing the geometric mutation with a standard linear-scaling approach (Virgolin et al.) causes one of the largest performance drops (p < 1e-6), which suggests the geometric search operator is the most important component. None beyond the paper's own contributions.

## Suggestions

1. **Report multi-run statistics for Table 1.** Run each experiment 10–30 times and report median solution rates with interquartile ranges or bootstrapped confidence intervals. Apply the same Wilcoxon signed-rank test used in the ablation to verify that GESR's advantage over the second-best baseline is statistically significant.
2. **Report GESR's computational budget explicitly.** State population size, number of generations, and any early-stopping criteria. Compare function evaluations or wall time against top baselines on a representative subset.
3. **Clarify the three underspecified aspects** (differentiability of operators for semantic gradients, derivation steps for k in Eq. 7, justification of variance-based constraint in Eq. 9) with a brief discussion or explicit derivation.
4. **Fix the argmax/argmin typo in Eq. (1).**
