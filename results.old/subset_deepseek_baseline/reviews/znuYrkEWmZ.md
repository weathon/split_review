## Summary

This paper investigates in-context learning (ICL) under a “blended training” paradigm where each training prompt mixes examples from multiple function classes (linear, quadratic, checkerboard, residual) without any task identifiers. The authors compare vanilla-trained models (single function per prompt) against blended-trained models on several synthetic classification benchmarks. They report that blended training achieves comparable accuracy to vanilla training while improving out-of-distribution generalization and noise robustness. Through three mechanism probes (OOD testing, bias analysis, and attention head ablation), they argue that both training regimes behave inconsistently with the common “function selection” hypothesis—suggesting that models do not simply pick among pre-learned functions but adapt more flexibly.

## Strengths

- **Addresses a relevant and under-explored scenario.** Blended training, where a prompt naturally mixes different task types, mirrors real-world ambiguity more closely than single-function prompts. Studying this setting is timely and practically motivated.
- **Systematic experimental design.** The paper defines clear synthetic function classes with known decision boundaries, enabling controlled evaluation of accuracy, OOD generalization, and noise robustness. The inclusion of a noise-augmented baseline helps isolate whether blended training’s benefits are merely due to noise-based regularization.
- **Multiple probes into mechanism.** The authors go beyond reporting accuracy by conducting three targeted experiments (OOD function test, bias test, attention head ablation) that attempt to interrogate the model’s internal behavior. The attention head ablation diagnostic is a clean method for measuring head importance.
- **Clear, well-presented results.** Tables and figures are easy to read, and the paper’s structure makes the different experiments easy to follow.

## Weaknesses

### Major

1. **Overclaimed refutation of the function-selection hypothesis.** The evidence provided is not strong enough to convincingly reject the function-selection account.  
   - The OOD test (Table 4) shows both vanilla and blended models outperform a “mix baseline” (max of single-function models). This could simply reflect that multi-function training yields a richer internal representation that generalizes to new combinations—not that the model avoids function selection entirely. The baseline is not a tight test of selection.  
   - The bias test (Table 5) does not directly measure whether the model evaluates and selects the lowest-error function. It only observes a preference for LC that shifts under increasing evidence for CC. A model could still be selecting among functions while having a prior bias—this is consistent with Bayesian inference, not contradictory.  
   - The attention head ablation (Fig. 2) shows that top heads impact both tasks, but this is expected in a shared architecture and does not rule out that other heads specialize. The analysis lacks a test for functional specificity (e.g., does any head affect only one task?).

2. **Lack of a positive mechanistic account.** The paper concludes that “function selection may not adequately explain model behavior” but offers no alternative explanation for how the model adapts under blended training. The claim that “attention heads serve as general-purpose mechanisms” is vague and not supported by the ablation data (which only shows that some heads are broadly important). The reader is left without a concrete understanding of what blended training actually does to the model’s internal processing.

3. **Limited novelty beyond existing work.** Blended training was already introduced by Li et al. (2024b), and that prior work is cited but not discussed in enough detail to clarify what this paper adds beyond performance validation. The mechanism analyses, while interesting, are not deep enough to provide significant new insight into the underlying principles of ICL.

### Minor

- The evaluation description is confusing: “the 100-th point was appended 2000 times to assess prediction accuracy within that context.” It is unclear whether this means 2000 different query points are generated for the same prompt or 2000 repeated trials with the same query. Clarification would help reproducibility.
- Table 4 mixes different settings (some columns are tasks, others are model types). The column labeled “mix” is defined as the maximum of single-function models, but that choice is not justified; a simple average or a different aggregation could change the comparison.
- The heatmaps (Fig. 2) lack a clear description of the normalization. It is stated that weights \(W_{i,j}\) are computed within each layer, but the color bar ranges (0.00–0.16 vs. 0.000–0.175) are not consistent across models, making cross-model comparison difficult.

### Trivial

None.

## Nice-to-Haves

- A more granular analysis of attention head specialization (e.g., using activation correlation or probing for task-specific subspaces) would strengthen the mechanistic argument.
- The paper could test whether blended training’s benefits hold when the number of function classes is larger or when functions have different input-dimensionalities.
- Including a baseline where prompts are simply noisier (e.g., random label flips) but still single-function could further differentiate blended training from noise augmentation.

## Novel Insights

None beyond the paper’s own contributions. The paper primarily provides empirical evidence that blended training can match vanilla accuracy while improving OOD generalization and noise robustness, and that some simple forms of function selection (like lowest-error preference) do not fully explain model behavior. This is a useful but incremental addition to the ongoing discussion about ICL mechanisms.

## Suggestions

1. **Sharpen the mechanistic tests.** For the function selection hypothesis, design a more direct test: e.g., probe whether the model’s representation of the current prompt correlates with a single function class, or train a classifier to decode the function identity from hidden states. If such decoding fails under blended training, that would be stronger evidence against selection.
2. **Provide a positive explanation.** Even a speculative framework (e.g., “the model learns a mixture-of-experts style composition” or “it fits a local linear model”) would help interpret the results and guide future work.
3. **Improve clarity of evaluation.** Clearly state whether the 2000 repetitions use the same prompt with different query inputs or repeated draws of the same query. Also report variance (error bars) for the main accuracy tables.
4. **Discuss prior work more explicitly.** Clearly state what Li et al. (2024b) reported and what the current paper adds in terms of mechanism and generalization analysis.

## Score and Decision

**Score:** 5  
**Decision:** Reject  

**Reasoning:** The paper addresses a worthwhile question and provides a clean set of experiments, but the central mechanistic claims are not well supported by the evidence presented. The OOD, bias, and ablation experiments are too indirect to convincingly refute the function-selection hypothesis, and no alternative mechanistic explanation is offered. The practical benefits of blended training (OOD generalization, robustness) are demonstrated, but this alone does not provide sufficient novelty or depth for an ICLR acceptance. The contribution is incremental and the conclusions are over-reaching relative to the experimental design.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>