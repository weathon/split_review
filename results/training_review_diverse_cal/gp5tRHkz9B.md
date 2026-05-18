Now I have all the information I need to verify claims against the paper. Let me write the consolidated review.

## Summary

This paper proposes LLM-Boost, a simple method to initialize GBDT predictions with logits from an LLM (or TabPFN) and then fit trees to the residuals, controlled by a scaling parameter *s*. The method is evaluated on 16 classification datasets subsampled to multiple sizes (10, 25, 50, 100, 200, 500, full), comparing against standalone GBDTs, standalone LLMs, selection (best on validation), and stacking (LLM scores as additional features). The core idea—replacing the GBDT's initial constant prediction with the LLM's output—is intuitive, lightweight (LLM inference is a one-time cost), and consistently improves over both constituent models across sample sizes.

## Strengths

1. **Simple, principled fusion mechanism.** LLM-Boost replaces the GBDT's constant initial prediction with the LLM's logits and learns residuals, controlled by a single tunable scaling parameter *s*. This is conceptually clean, easy to implement, and does not require modifying the GBDT training loop beyond initialization (Section 3.2–3.3).

2. **Systematic evaluation across dataset granularities.** The paper evaluates on 16 datasets at sample sizes 10, 25, 50, 100, 200, 500, and the full dataset, providing fine-grained analysis of where LLM-Boost helps most (small-to-medium) and where the TabPFN variant takes over (medium-to-large). This granularity is a genuine strength relative to papers that evaluate only at one or two scales.

3. **Generality across model choices.** The boosting procedure is validated with Flan-T5-XXL, Llama-3-8B, XGBoost, and LightGBM, and is also applied to TabPFN, demonstrating that the approach is model-agnostic and not tied to a specific architecture (Sections 5.1–5.3).

4. **Causal ablation isolating column headers.** By shuffling column headers on the Adult dataset (Figure 5), the paper empirically demonstrates that meaningful headers drive the advantage at small sample sizes, while even degraded headers provide some benefit. This cleanly supports the motivating intuition.

5. **Practical two-stage hyperparameter tuning.** The paper proposes tuning GBDT hyperparameters first, then independently tuning the scaling parameter *s*, which guarantees improvement in validation loss and stabilizes optimization (Section 4.2). This is a practical insight useful to practitioners.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Missing simple ensemble baseline ("average of predictions").** The paper compares against selection (best on validation) and stacking (LLM scores as features) but does not include the simplest possible baseline: equal-weight (or validation-tuned weighted) averaging of GBDT and LLM predictions. This is a natural competitor for the ensemble claim, and its omission makes the "state-of-the-art" language in the abstract ("demonstrate state-of-the-art performance against numerous baselines and ensembling approaches") overstated relative to the actual comparison set. The core contribution is still well-supported—LLM-Boost beats selection and stacking—but the claim should be scoped accordingly.

2. **No statistical testing on aggregate metrics.** Per-dataset results are averaged over 5 seeds with reported standard errors (line 154), but the aggregate curves (Figures 2–4) showing average rank and average z-score across datasets lack confidence intervals or formal tests (e.g., Wilcoxon signed-rank comparing LLM-Boost to the best baseline at each sample size). While the pattern is consistent across three metrics (rank, z-score, AUC) and 16 datasets—making a major validity concern unlikely—adding statistical tests on the aggregates would strengthen the central claim and bring the paper up to current best practices.

3. **Under-specified detail about the centering constant *C* in Equation 1.** The paper states that *C* "can be added to make SCORE_LLM centered around 0 for numerical stability" but does not specify how *C* is chosen (fixed per dataset? tuned? zero?). Since the equation is the formal definition of the method, this detail should be clearly stated for reproducibility.

4. **Prompt robustness not systematically tested.** The paper uses a single prompt format (derived from Slack & Singh 2023) and acknowledges that Llama-3-8B performed poorly due to prompt design difficulty (Section 5.3). While the paper does explore model size and number of shots (Section 5.5, Figure 6)—contrary to the claim that it does not—it does not vary prompt format or serialization template beyond the one used. Demonstrating robustness to at least one alternative prompt format (or showing that results are stable) would strengthen confidence that the method leverages genuine semantic understanding rather than prompt artifacts. The shuffled-columns ablation (Figure 5) partially addresses this, but prompt-format sensitivity remains untested.

5. **TabPFN data-subsampling asymmetry.** For datasets larger than 1000 samples, TabPFN is capped at 1000 random samples (line 165, standard per the original work), while GBDT sees the full dataset. This means the TabPFN component in the LLM-Boost + TabPFN variant is operating under a data disadvantage on large datasets. The paper is transparent about this, but it should be discussed more explicitly as a limitation when interpreting the claim that "TabPFN+GBDT achieves the best performance on larger datasets."

### Trivial
None.

## Nice-to-Haves

- A simple averaging baseline (equal-weight or validation-tuned weight) would round out the ensemble comparisons.
- Per-dataset breakdown tables could be featured more prominently (the paper notes they exist in full results tables; bringing a summary into the main text would help readers assess variance).
- A brief discussion of when the GPU cost (up to 18 hours for LLM inference on 4 GPUs) is justified by the AUC improvement would help practitioners decide whether to adopt the method.
- The paper is scoped to binary/multi-class classification with ≤5 classes; noting whether the method extends to regression or many-class classification as future work is already done in the limitations, which is appropriate.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the paper does not compare against deep tabular methods (FT-Transformer, TabNet, NODE).** The paper's scope is fusing LLMs (which use column headers) with GBDTs. Deep tabular methods do not use column headers and are a different model class. Demanding this comparison evaluates the paper against the wrong expectations. **[Scope creep]**

- **Criticism that the paper "does not explore... number of shots (only 3-shot is used)."** The paper explicitly experiments with varying numbers of shots in Section 5.5 (Figure 6). This claim is factually incorrect. **[Factually wrong]**

- **Criticism about the "trough in LLM performance" undermining the "in between" claim.** The paper already explains this phenomenon in the Figure 2 caption (line 159: "due to us using only a subset of datasets which have sufficient training samples"). The claim is not invalidated; the explanation is provided. **[Already addressed in paper]**

- **Criticism that only ≤5 class datasets are used.** The paper explicitly states this filtering criterion and it is a transparent scope choice, not a weakness. **[Scope, not a weakness]**

## Novel Insights

The most interesting observation from the cross-review analysis is that the paper's core contribution is not the LLM+GBDT fusion *per se* (related feature-engineering approaches exist), but rather the specific *residual-learning formulation* with a tuned scaling parameter that smoothly interpolates between the LLM prior and the GBDT's inductive bias. The consistent pattern across sample sizes—where LLM-Boost tracks the better of the two models at the extremes and exceeds both in the middle—suggests that the scaling parameter *s* is acting as an adaptive prior-strength controller, and the data in Figure 6 (varying model size and shots) further supports that stronger LLM priors yield stronger boosting gains. This interpretation implies the method's effectiveness is tied to the *complementarity* of the two model classes rather than any specific property of the LLM or GBDT, which is why it also works with TabPFN—a non-LLM model with complementary scaling behavior. The failure case with Llama-3-8B (due to prompt design difficulty) reinforces this interpretation: if the LLM's predictions are too noisy, the residual-learning formulation has nothing useful to work with, and performance degrades.

## Suggestions

1. Add simple averaging (equal-weight and/or validation-tuned) as a baseline, and either add confidence intervals to the aggregate plots or report a non-parametric test (e.g., Wilcoxon signed-rank at each sample size).
2. Specify how the constant *C* in Equation 1 is determined, and clarify whether it is fixed or tuned.
3. Tone down the "state-of-the-art" language to match the actual comparison set (e.g., "outperforms standalone models and two common ensembling strategies").
4. Show prompt robustness for at least one dataset by varying the prompt format or serialization template.
5. Explicitly discuss the TabPFN subsampling asymmetry as a limitation when interpreting the large-dataset results.

## Score and Decision

The paper makes a clear and useful contribution: a simple, well-motivated method for combining LLMs' semantic understanding with GBDTs' scalability, evaluated at fine granularity across sample sizes. The weaknesses are addressable (missing baseline, lack of statistical testing on aggregates, one under-specified detail) but do not undermine the core claims. The evidence is consistent across 16 datasets, multiple metrics, and different model combinations.

**Score:** 6.5

**Decision:** Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>