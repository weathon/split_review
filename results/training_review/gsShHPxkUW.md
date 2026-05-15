Now I have all the evidence needed to verify the reviewer claims against the paper. Let me produce the final consolidated review.

## Summary

The paper proposes a causal mediation framework to quantify LLMs' deep structure comprehension (ADCE) and surface structure comprehension (AICE). It evaluates 12 LLMs across 5 tasks, finding that most models exhibit positive ADCE (indicating genuine deep structure understanding), that closed-source models rely more on deep structure than open-source models, and that ADCE provides a more reliable assessment than accuracy under spurious correlations.

## Strengths

- **Novel causal formalization of an important question.** The paper moves beyond prior work that merely measures surface-sensitivity by framing deep structure comprehension as a direct causal effect (DCE) and proposing estimable surrogates (ADCE/AICE). This provides a principled framework for addressing whether LLMs understand core semantics or merely exploit surface patterns (Sections 2–3).

- **Broad empirical scope.** The evaluation covers 12 models from 4 families (Llama, Mistral, GPT, Claude) across 5 diverse tasks (math, logic, commonsense), demonstrating that ADCE is consistently positive and grows with accuracy (R² > 0.7, Figure 3). This is the most comprehensive cross-model, cross-task analysis of deep structure comprehension I am aware of.

- **Theoretical connection to necessity and sufficiency.** Theorem 1 proves that ADCE is a weighted combination of the probability of sufficiency (PS) and probability of necessity (PN) of deep structure changes on output variations (Section 3.4). This grounds the metric in well-established causal notions and justifies ADCE as a bidirectional evaluation beyond mere accuracy.

- **Compelling spurious correlation experiment.** The CivilComments demonstration (Section 4.5) provides empirical validation that ADCE behaves as expected: as spurious correlations increase, accuracy remains misleadingly high while ADCE correctly declines, whereas in non-spurious minority groups both metrics align. This validates the theoretical argument that ADCE captures genuine deep-structure reliance better than accuracy.

## Weaknesses

### Fatal
None.

### Major

1. **Unvalidated core approximation (ICE→AICE).** The entire method rests on replacing the unobservable ICE (which requires simultaneously T=0 and s(T=1)) with the observable AICE (T=0, s(T=0)). The paper acknowledges (Section 3.2) that "the efficacy of this approximation hinges on the similarity between the original ICE and AICE" and describes intervention strategies designed to minimize the discrepancy. However, no formal bound, sensitivity analysis, or empirical validation of this approximation is provided. The intervention strategies (masking k non-core words, rephrasing via Claude) are heuristics whose approximation quality is unquantified and likely task-dependent. If the gap between ICE and AICE is large, ADCE is not a faithful surrogate for DCE, and all downstream conclusions about deep structure comprehension are undermined. This is the paper's most significant methodological vulnerability.

2. **Problematic independence assumption.** The paper states (Section 2) that deep structure d_i and surface structure s_i are independent given the input x_i (d_i ⟂⟂ s_i | x_i), citing Stolfo et al. (2022). However, since x_i := (d_i, s_i), conditioning on x_i makes the independence claim mathematically vacuous. Beyond the notation issue, the substantive assumption that deep and surface structures are separable independent components is at odds with the linguistic theory the paper invokes (Chomsky, 1971), where surface structure is a realization of deep structure. The causal graph in Figure 2 treats d and s as independent mediators from x, but in natural language they are causally and structurally entangled. The paper does not justify this assumption or discuss how violations would affect the validity of ADCE/AICE.

### Minor

1. **Confounding concerns in the ADCE–accuracy regression.** The paper reports a linear regression of ADCE on accuracy with R² > 0.7 (Section 4.2) but pools models from different families and scales. The observed correlation could be confounded by model architecture, training data size, or the fact that both metrics depend on overall model capability. No confidence intervals, statistical tests, or per-family analyses are reported, weakening the causal interpretation that "models with higher accuracy exhibit greater dependence on deep structure."

2. **Limited SFT experiment.** The prerequisite experiment (Section 4.3) uses a single model (Llama-3-8b) on a single task (Analytic Entailment) with no control for random seed, multiple runs, or comparison to other post-training methods. While the result (ADCE increases after SFT) is suggestive, the paper's claim that ADCE activation reflects "task-relevant knowledge in training data" is too broad for the evidence provided.

3. **Scale mismatch in ADCE vs. AICE comparison.** ADCE (a difference of two probabilities ranging from -1 to 1) and AICE (a single probability ranging from 0 to 1) are compared as raw magnitudes in Figure 5. While the relative ranking (ADCE > AICE vs. AICE > ADCE) is meaningful for determining which causal pathway dominates, the paper does not discuss the interpretational difference between a probability and a difference of probabilities, which could mislead readers about the absolute magnitudes.

### Trivial

- The ≠ operator for output comparison could in principle conflate trivial formatting changes (e.g., capitalization, trailing periods) with genuine semantic changes, though this is standard practice in LLM evaluation and unlikely to materially affect results given the aggregation across many samples.
- The task-level variability behind the aggregated ADCE/AICE values in Figure 5 is not shown, making it hard to assess whether the closed-source vs. open-source distinction holds uniformly or is driven by specific tasks.

## Nice-to-Haves

- A controlled validation experiment (e.g., on synthetic data with known ground truth about deep/surface structure) that quantifies the bias of AICE relative to the unobservable ICE would substantially strengthen the method.
- An ablation comparing different ways of defining AICE (different k values for masking, different rephrasing models) to assess robustness to the choice of surface intervention.
- Task-level breakdowns for the ADCE vs. AICE comparison to verify that the closed-source vs. open-source distinction is not driven by a few outlier tasks.

## Removed Points

- **Motivating experiment scope (Harsh Critic):** The criticism that Figure 1 uses only one model/task is removed because it is a motivating illustration, not a main experimental result. The main paper evaluates 12 models × 5 tasks.
- **Equation (1) being idealized:** The criticism that the formal definition in Eq. (1) is "idealized" is removed because it is explicitly a definition of an ideal condition, not a claim that LLMs satisfy it.
- **Related work inadequacy:** Criticisms about missing related work differentiation are removed per the guidelines (cannot verify completeness without external sources).
- **Missing appendix details (CivilComments ADCE computation):** The criticism that the ADCE computation for CivilComments is not specified in the main text is removed because the parser strips appendix content; the details exist in the original submission.
- **Theorem 1 practical relevance:** This subjective judgment is removed as not constituting a concrete weakness.
- **General claim of missing confidence intervals for the regression:** Kept as minor but the harsh critic's stronger framing is softened.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Validate the ICE→AICE approximation.** The single most impactful addition would be to design a controlled experiment (e.g., on synthetic data where the true ICE is computable, or on a small human-annotated set where the "correct" surface intervention is known) to measure the bias of AICE. Even a theoretical bound under specific assumptions would help.

2. **Clarify the independence assumption.** Revise Section 2 to either (a) drop the conditioning on x_i (which makes the statement vacuous) and instead state that d_i and s_i are assumed separable components of the input, or (b) explicitly discuss the limitations of this assumption and how violations might affect results. Reference to the linguistic literature (Chomsky) and prior causal work (Stolfo et al.) should be reconciled.

3. **Report task-level breakdowns for Figure 5.** Show per-task ADCE and AICE to reveal whether the closed-source vs. open-source distinction is consistent across tasks or task-dependent.

4. **Add confidence intervals or per-family regressions for the ADCE–accuracy correlation.** The strong R² claim would be more convincing with family-specific slopes, confidence bands, or at least a discussion of potential confounders.

## Score and Decision

The paper tackles an important question with a principled causal framework, broad empirical scope, and a compelling theoretical connection to necessity/sufficiency. The two major methodological concerns — the unvalidated ICE→AICE approximation and the questionable independence assumption — are significant but not fatal: the paper acknowledges the approximation challenge, describes design choices to address it, and provides empirical evidence (the spurious correlation experiment, the accuracy correlation trend) that ADCE behaves sensibly. The weaknesses are addressable in a revision or noted as limitations. On balance, the contribution is positive and the paper offers genuine methodological and empirical value to the community.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>