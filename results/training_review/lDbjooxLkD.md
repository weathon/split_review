Here is my consolidated review:

---

## Summary

This paper introduces PassUntil, an evaluation strategy that uses massive random sampling (up to 10⁵ samples) to measure very small task-success probabilities (as low as ~10⁻⁵) in LLMs, thereby "smoothing out" the apparent discontinuity of emergent abilities. Using PassUntil, the authors derive a task scaling law (PU ∼ exp(−cN⁻ᵅ)) from the loss scaling law and validate it on three benchmarks, predicting a 2.4B model's HumanEval performance with 0.05% deviation. They then identify a class of "accelerated emergence" tasks whose scaling curves are concave in log(−log(PU)) vs. log N space, and provide preliminary evidence that a multiple-circuits hypothesis might explain this shape.

## Strengths

- **PassUntil is a genuinely useful methodological contribution.** Measuring success probabilities as low as 10⁻⁵ through repeated sampling is a simple but effective idea that directly addresses the evaluation-resolution bottleneck that has obscured subtle performance improvements in small models. The MLE property (r/K) is correctly noted, and the method applies to any pass-based metric (exact match, human eval, etc.).

- **Impressive predictive result on code generation.** The 0.05% deviation on HumanEval series 1 (0.05987 predicted vs. 0.05990 actual) is a striking demonstration. This is the first open-source attempt (to the authors' knowledge) to replicate the kind of predictable scaling hinted at in GPT‑4's report, and the result is concrete and reproducible.

- **Controlled experimental setup.** The authors train two model series (0.03B–2.4B) with consistent architecture scaling rules and verify that training losses follow the standard loss scaling law, providing a solid foundation for the task-performance analysis.

- **Instance-level fitting improves prediction.** The paper identifies that test instances vary in difficulty and scaling speed, and shows that per-instance fitting reduces prediction error compared to dataset-level fits in 3 of 4 settings (Table 1). The method for bridging hard instances via test-loss mapping is a practical innovation.

- **Taxonomy of scaling curve shapes.** The categorization into sub‑, standard, and super-scaling law growth provides a useful vocabulary for discussing different types of task improvement during scaling, and the mathematical framing (Definition 1) is clean.

## Weaknesses

### Fatal
None.

### Major

- **The "task scaling law" is validated on a narrow set of tasks, and its scope is unclear.** The derivation (Eq. 3) requires strong assumptions (zero irreducible loss per token, uniform α across tokens) that are unlikely to hold universally. The paper verifies the law on three tasks (HumanEval, Emoji Movie, Date Understanding) where it fits well, but then immediately finds that 5/8 UICL tasks violate it—producing concave curves. The paper treats this as "accelerated emergence" rather than a limitation of the derived law. This is not a contradiction per se, but it means the "task scaling law" is not a general law of task performance; it is a functional form that matches some tasks and not others. The paper provides no principled way to predict which tasks will obey it before running experiments. The impressive prediction results are on tasks selected for fitting the law, which limits the generality of the claim.

- **The analysis of "accelerated emergence" in Section 6 is preliminary and does not establish the circuits hypothesis.** The paper proves that multi-step reasoning implies convex curves (sub-scaling) and that a multiple-circuits model with hard max implies concave curves (super-scaling). However, the "test" of the circuits hypothesis is a post-hoc fit of a soft two-circuit model with free parameters (c₁, c₂, α₁, α₂, softmax weights) to the same data used to conceive the hypothesis. There is no held-out prediction, no comparison to alternative concave-generating mechanisms (e.g., data sparsity, threshold effects, quantization), and no attempt to falsify the multi-step reasoning account (which the paper proves yields convex, not concave, curves—but this only rules out one narrow hypothesis). The paper's own language ("loosely test," "in harmony with") is appropriately cautious, but the contribution is not established as an explanation for accelerated emergence.

### Minor

- **Censoring at the 10⁵ sampling budget is not systematically analyzed.** The paper acknowledges that some instances reach 10⁵ samples without a pass (PU = 0) and that this causes 3/8 UICL tasks to "miss 1 or 2 valid estimation points." However, there is no analysis of how many instances per model per task are censored, how this biases the aggregate PU estimates, or how censoring affects the fitted scaling-law parameters. This is a known issue with the negative binomial MLE under truncation and deserves direct treatment.

- **No statistical test for concavity.** The central claim that 5/8 UICL tasks are concave relies on visual inspection. A simple regression with a quadratic term in log N could provide a statistical test. Relatedly, only 2 of the 8 UICL curves are shown in figures; the reader cannot independently assess the claimed categorization.

- **Comparison to baselines is missing.** The paper does not compare PassUntil's cost-accuracy trade-off against simply increasing the test set size (the approach suggested by Schaeffer et al. 2023). A comparison of how many total tokens/inferences each method requires to achieve comparable resolution would strengthen the practical case for PassUntil.

### Trivial

- The 0.05% deviation figure in the abstract and body is cited without the task name in some places; the paper should consistently specify that this applies to HumanEval series 1 (it does so in Table 1 and Figure 6, but the abstract could be clearer).
- The paper uses \cmt{} markup in several places (e.g., lines 4, 30, 39, 69, 91, 103, 224, 253, 263, 278), suggesting these were added or modified after the initial draft. This is a minor presentation issue.

## Nice-to-Haves

- A systematic censoring analysis (how many instances hit the 10⁵ bound per model/task, and the impact on parameter estimates).
- Out-of-sample prediction for UICL tasks where the task scaling law fails, using the circuit model fitted to small models to predict larger-model performance.
- A statistical test for concavity (e.g., quadratic regression or bootstrap-based curvature test).
- All 8 UICL scaling curves visualized, not just 2.

## Removed Points

These points are flagged to be removed; treat them with caution:
- **"Infinite resolution claim is misleading and unsupported"** — The paper consistently qualifies this as *theoretically* infinite ("as long as computational resources are not bounded"), which is a standard and accurate characterization of the method's property. The practical bound (10⁵) is acknowledged in Section 4.1. This is not a factual error.
- **"Task scaling law is not a law; the paper's own evidence refutes it"** — The paper does not claim the law is universal; it derives a functional form, validates it on tasks where it fits, and then studies tasks where it doesn't (calling those "accelerated emergence"). This is a categorization framework, not a contradiction. The law holds for some tasks; the paper is transparent about this scope.
- **"The multiple circuits hypothesis is not tested"** — The paper explicitly says "we loosely test" and shows a fit. The evidence is weak, but the claim that it's "not tested" is inaccurate. The weakness is already captured in Major above.
- **"The paper does not report predictions for all four task×series combinations"** — Table 1 reports all four combinations transparently.
- **"The claim of 'mere 0.05% deviation' is selective"** — The paper specifies this applies to HumanEval series 1 and also reports the Emoji Movie prediction (~19% deviation) in the same table. Standard reporting practice.
- **Criticisms about missing statistical tests for significance in pilot experiments, or about Figure 2 lacking numerical values** — These are minor visualization points that do not threaten core claims and are partly addressed by reporting practices in the field.
- **Criticism that Section 5 only shows 3 tasks** — These are the tasks selected for the prediction experiment; the paper is transparent about which tasks were tested.

## Novel Insights

None beyond the paper's own contributions. The key empirical finding—that with sufficient sampling resolution, task performance improves smoothly and can be predicted by a derived functional form—is the paper's main insight. The observation that some tasks exhibit concave log(−log(PU)) vs. log N curves (accelerated emergence) while others are linear is a useful empirical categorization, though the mechanistic explanation remains speculative.

## Suggestions

1. **Add a systematic censoring analysis.** Report the fraction of instances per model per task that reach K=10⁵ without r passes, and discuss how zero-imputation or exclusion affects the fitted scaling parameters.
2. **Add a statistical test for concavity.** Fit a quadratic term in log N to the log(−log(PU)) curves and report whether the quadratic coefficient is significantly negative for the claimed "accelerated emergence" tasks.
3. **Visualize all 8 UICL scaling curves.** Even in an appendix, showing all curves with bootstrapped error would allow readers to assess the 5/8 vs. 3/8 categorization.
4. **Add a cost comparison baseline.** Compare PassUntil's inference cost vs. the cost of increasing the test set size (Schaeffer et al.'s approach) to achieve comparable resolution.
5. **Clarify the scope of the "law".** In the abstract and introduction, temper the claim about a "task scaling law" to acknowledge that it applies to a class of tasks and that others exhibit "accelerated emergence" that the current framework does not predict.

## Score and Decision

**Recommendation: Accept**

The paper makes a genuine contribution. PassUntil is a simple but effective methodological innovation that enables measuring previously invisible performance improvements. The 0.05% prediction on HumanEval is impressive and reproducible. The task-scaling-law derivation, while making strong assumptions, provides a useful framework that fits several benchmarks well. The analysis of accelerated emergence is the weakest part—it is more of a taxonomy than an explanation—but it opens an interesting direction. The major and minor weaknesses identified above (limited scope of validation, missing censoring analysis, weak circuits evidence) are addressable in revision and do not invalidate the core contributions. The paper is well-written, the experiments are controlled, and the release of checkpoints will benefit the community.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>