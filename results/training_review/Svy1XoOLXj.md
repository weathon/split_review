Now I have all the information needed to write the final consolidated review. Let me synthesize everything.

## Summary

This paper proposes BiLoRA, a bi-level optimization framework for low-rank adapters (LoRA/AdaLoRA). It parameterizes incremental matrices in pseudo-SVD form and trains the singular vectors (in the lower level) and singular values (in the upper level) on disjoint data subsets, aiming to reduce overfitting to a single training set. Experiments on GLUE (RoBERTa, DeBERTa) and E2E NLG (GPT-2) show consistent improvements over LoRA and AdaLoRA across ten datasets and three model families.

## Strengths

- **Novel and clean synthesis of bilevel optimization with SVD-parameterized LoRA.** The idea of training singular vectors and singular values on different data subsets via a nested optimization is a new and well-motivated contribution to the PEFT literature. The paper clearly articulates why this separation could reduce overfitting relative to joint training on a single dataset.

- **Consistent empirical gains across diverse settings.** BiLoRA outperforms LoRA and AdaLoRA across ten GLUE and E2E NLG benchmarks, using RoBERTa-base/large, DeBERTa-v3-base, and GPT-2 medium/large. On RoBERTa-base GLUE, the average improvement over LoRA is +0.7 points; on GPT-2 medium E2E, BLEU improves from 68.2 to 69.8. The largest gains appear on small datasets (CoLA, RTE, MRPC), consistent with the overfitting-reduction hypothesis.

- **Robustness to hyperparameter choices demonstrated.** Ablations over three pseudo-singular-value parameterizations (Real-Value, Softmax, Approximately Binary) and over different values of the orthogonality regularizer γ₁ show that BiLoRA outperforms LoRA across all settings with limited sensitivity, reducing the concern that gains come from careful tuning.

- **Scales to billion-parameter models.** Results on DeBERTa-XXL (1.5B parameters) with three GLUE tasks show BiLoRA matches or exceeds full fine-tuning and LoRA, indicating the method does not degrade at scale.

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablation that isolates the bilevel mechanism from simpler data-splitting alternatives.** The paper's core claim is that the **bilevel nesting** (where V*(E) depends on E and the two levels are solved jointly) is what alleviates overfitting. However, the experiments never compare against simpler baselines that control for the data-splitting itself: (a) train all parameters (V and E) jointly on pooled D₁∪D₂, (b) two-stage training (train V on D₁, freeze, then train E on D₂), or (c) train all parameters on pooled data with a regularization penalty matching the reduced-data effect. Without these controls, the improvement cannot be attributed to the bilevel structure specifically — it could simply be the regularization effect of training different parameter groups on different subsets. The existing ablations (Tables 5–6) test singular-value parameterizations and orthogonality regularization, not the core algorithmic mechanism.

2. **Headline comparisons rely partly on published numbers rather than re-run baselines.** The tables clearly mark "* indicates numbers published in prior works," and Section 4.1 states "we used the reported results in previous work" for baselines. While this is common practice in the PEFT literature, the paper's central quantitative claims (e.g., "+0.7 average on GLUE") must be interpreted with caution because factors like learning rate schedules, random seeds, codebase variations, and early stopping are not controlled across papers. The paper does re-run BiLoRA using the same settings as LoRA (line 144), but does not re-run LoRA itself under those identical conditions. Direct reproduction of all baselines would substantially strengthen the evidence.

### Minor

3. **Inconsistent data-splitting strategy across task types without justification.** For NLU (GLUE), the training set is split 8:2 into D₁ (lower) and D₂ (upper). For NLG (E2E), the training set serves as the lower level and the **validation set** as the upper level (line 157). These are fundamentally different setups: the latter uses true held-out data for the upper level while the former uses an internal split of the training data. The paper offers no discussion of why different strategies were chosen or how this affects comparability of the NLU and NLG results. This inconsistency muddies the definition of the method.

4. **Training time comparison lacks sufficient controls.** Table 7 reports lower total training time for BiLoRA than LoRA, attributed to faster convergence with a larger learning rate. However, the paper does not report the learning rates used, the number of epochs for each method, or the per-step computational overhead (which should be higher for bilevel methods due to inner-loop updates). It is unclear whether LoRA could match the speed with the same larger learning rate, and whether the comparison is apples-to-apples.

5. **No direct overfitting diagnostic.** The paper motivates BiLoRA by claiming that LoRA/AdaLoRA overfit to the training data, but it never presents train-vs-validation loss curves or any direct measure of the generalization gap for any method. The evidence for overfitting reduction is indirect (larger gains on small datasets). Showing loss curves for at least one small dataset (e.g., RTE or MRPC) would make the narrative more compelling.

6. **Algorithmic details needed for reproducibility.** The paper cites the Betty library for bilevel optimization but does not specify key implementation details such as how many inner-loop steps are taken per outer-loop step, whether the lower-level problem is solved approximately or to convergence, or how the hypergradient is computed (implicit differentiation vs. unrolling). These details directly affect training cost and stability.

### Trivial
- The paper states at line 11 that "the large number of parameters in pre-trained models may make the fine-tuning process more prone to overfitting," citing Karimi Mahabadi et al. (2021). This citation is about PEFT, not about overfitting from large parameter counts, but this does not affect the paper's core argument.

## Nice-to-Haves
- A study varying the 8:2 data-split ratio (e.g., 9:1, 7:3) to report sensitivity.
- Visualization of the evolution of pseudo singular values during training to illustrate the difference between bilevel and joint training.
- Application to more recent LLMs (e.g., LLaMA, GPT-3 scale) on diverse tasks.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Strength Finder's claim about "fair experimental setup"** (point 6 under Supporting Strengths): This conflicts with verified weaknesses about unreproduced baselines and inconsistent data splitting. Removed per the rule that when a strength and weakness disagree, the weakness wins.
- **Harsh critic's claim that "no references show that LoRA overfits" and that "LoRA is commonly observed to generalize well":** The paper does cite Karimi Mahabadi et al. (2021) about overfitting with large parameter counts and provides indirect evidence through larger gains on small datasets. The claim is not a strawman but is softened — the paper lacks direct evidence but the motivation is still reasonable.
- **Request for theoretical analysis (from Missing Parts section):** This is scope-creep for an empirical paper.
- **"Apply to larger LLMs (LLaMA, GPT-3 scale)"**: Not part of the stated scope and would be a nice-to-have, not a weakness.

## Novel Insights
The reviewers' interaction surfaces an important subtlety that the paper itself does not discuss: the bilevel formulation with SVD-parameterized adapters can be viewed as a form of implicit data-dependent regularization where the upper-level data subset acts as a validation set for learning the importance weights (singular values) of each rank-1 component. This perspective connects BiLoRA to cross-validation and meta-learning — the singular values are effectively hyperparameters being optimized on a held-out subset — which suggests that the benefit may come as much from the data-splitting itself as from the bilevel nesting. The paper's failure to run the obvious control (training all parameters on pooled data) leaves this ambiguity unresolved.

## Suggestions
1. **Add the critical ablation**: Compare BiLoRA against (a) joint training on pooled D₁∪D₂, (b) two-stage training (train V on D₁, freeze, train E on D₂), and (c) joint training on pooled data with a parameter-norm penalty matching the reduced-data effect. This is the single most important experiment to validate the claim that bilevel nesting matters.
2. **Reproduce LoRA under identical conditions** for at least the RoBERTa-base GLUE experiments, reporting means and standard deviations over 3–5 seeds, to make the headline numbers directly comparable.
3. **Justify or harmonize the data-splitting strategy** across NLU and NLG, or at minimum discuss the trade-offs.
4. **Report training details** (learning rates, number of epochs, inner-loop steps) for the timing comparison and ideally isolate per-step overhead from convergence speed.
5. **Include train/validation loss curves** for at least one small dataset (e.g., RTE) to directly support the overfitting-reduction narrative.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>