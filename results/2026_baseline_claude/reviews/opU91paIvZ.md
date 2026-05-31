## Summary

This paper formalizes CoT (chain-of-thought) *monitorability* as a constrained optimization problem and proposes a prior-guided distillation pipeline to produce faithful and concise reasoning traces. The authors first demonstrate that naive RL fine-tuning fails to improve monitorability because the monitorability signal f(z) is nearly zero under the initial policy, causing vanishing gradients. Their solution transforms the base model's raw CoT traces using a stronger instruct model (the "prior"), filters for task-correctness-preserving monitorable traces, and uses the resulting dataset for SFT. On MMLU-Pro (hint-injection faithfulness), GSM8K, and MATH500, the method claims +10 percentage points in faithfulness and up to 60% reduction in CoT length while retaining ≥90% of base accuracy.

---

## Strengths

- **Clear problem formulation with actionable mathematical grounding.** The constrained optimization formulation (Eq. 1–3) and the gradient analysis (Eq. 4–5) provide a principled explanation of why RL fails. The argument—that L1 collapses to zero when f(z)≈0 under π₀—is clean and borne out empirically in Figure 2.

- **Compelling proof-of-concept experiment.** Figure 3 is the paper's strongest evidence: conditioning π₀ on prior-transformed traces z_s yields 85% faithfulness and 96.6% conciseness while preserving accuracy, versus ~30% and ~12% for the baseline. This decisively confirms that monitorable traces are reward-compatible and that scarcity—not incompatibility—is the obstacle.

- **Empirical faithfulness improvement across six hint categories.** Table in Figure 4 shows consistent gains across all six hint types (sycophancy, consistency, visual pattern, metadata, grader hacking, unethical information), suggesting the effect is not driven by a single category.

---

## Weaknesses

### Fatal
None.

### Major

1. **The trained model achieves 25% faithfulness while the prior achieves 85%—a 60-point gap that is never explained.** This is the paper's most consequential unaddressed issue. If the prior can produce traces that, when fed to the unchanged π₀, yield 85% faithfulness, why does SFT on those same traces only give 25%? The claim that "SFT teaches the model to imitate high-quality reasoning" is undermined by this dramatic performance gap. Without understanding or resolving this failure, the practical value of the pipeline is severely limited, and the headline result (25%) is not actually convincing as a step toward monitorable AI.

2. **Experiments are restricted to a single 1.5B model.** All training and evaluation use DeepSeek R1 Qwen-1.5B as the base policy and Qwen 2.5-7B as the prior. This configuration leaves open whether the approach scales to models where reasoning already dominates accuracy, and whether a larger base model would avoid the 25% ceiling. For a paper claiming a "principled" and general approach to CoT monitorability, single-model results are insufficient.

3. **Faithfulness metric measures hint verbalization, not causal faithfulness.** The metric f(z) = 1{hint verbalized in z} rewards the model for *mentioning* the hint but does not distinguish between: (a) the model genuinely relied on the hint, or (b) the model independently derived the answer but learned to always mention hints post-hoc. A model trained to systematically verbalize hints could score high on this metric while still being unfaithful in the causal sense. The paper acknowledges faithfulness limitations only briefly and does not provide any control to distinguish these cases.

4. **Notational inconsistency in Algorithm 1 undermines reproducibility.** Line 13 filters candidates by "f(z_si) ≤ β." For the conciseness case, f(z) = 1{Length(z) < 950} is a 0/1 indicator, while β ∈ {125, 950} is a token count. The filter condition as written is dimensionally incoherent and appears to conflate the indicator function f with the raw length. For the faithfulness case, if f=1 for faithful traces, then "f ≤ β" would keep both faithful and unfaithful traces unless β = 0.5—not the desired behavior. This suggests the algorithm, as presented, does not match the implementation.

### Minor

1. **Absolute faithfulness remains low.** Even after training, faithfulness reaches only 25% on average. While the relative improvement (~67%) sounds large, the system is unfaithful in 75% of cases, which is a significant caveat for a paper about interpretability and AI safety.

2. **The accuracy constraint is not cleanly satisfied.** Section 5.2 reports "average relative accuracy of approximately 90% compared to the base model." This contradicts the abstract's claim of "keeping accuracy essentially unchanged" and the 96% figure stated in the contributions. The discrepancy between different reported numbers across the paper is notable.

3. **No comparison to training-based baselines for faithfulness.** Direct prompting and indirect prompting (Figure 4) are the only comparisons, yet these are prompt-only methods with no learning. A comparison to an RL-based approach that attempts to directly reward hint verbalization—even if expected to fail—would more concretely validate the paper's core claim that the vanishing-gradient problem is real and nontrivial.

### Trivial
None worth noting.

---

## Nice-to-Haves

- An analysis of the gap between prior performance (85% faithfulness) and trained model performance (25%) would be the single most valuable addition.
- Experiments on at least one larger model (e.g., 7B or 13B) to test generalizability.
- A counterfactual faithfulness test: compare "hint mentioned" rate when the hint is absent to validate that the trained model only verbalizes hints when they are present, not by default.

---

## Novel Insights

The paper's most genuinely novel observation is the empirical and theoretical characterization of why monitorability-targeted RL fails: the support of the monitorability signal f(z) under the initial policy is nearly zero, so policy-gradient updates receive no useful signal in the monitorability direction (L₁ ≈ 0) while the accuracy objective (L₂) continues to dominate. This precise diagnosis—that failure is due to support mismatch rather than reward incompatibility—is well-motivated and provides a principled rationale for bypassing RL in favor of prior-guided data curation. The proof-of-concept in Figure 3 that directly verifies reward-compatibility of monitorable traces is a tight and useful empirical argument.

---

## Suggestions

- Ablate the SFT training to understand why the trained model achieves only 25% vs. the prior's 85%. Is it due to insufficient training data, distributional mismatch, or capacity limitations of the 1.5B model?
- For the faithfulness evaluation, add a "no-hint" control condition to measure the rate at which the trained model mentions hints when no hint is present, distinguishing genuine verbalization from learned mention-everything behavior.
- Fix Algorithm 1 line 13 to use a consistent definition of f and β, and add a short clarification distinguishing f as an indicator from β as a raw length budget.
- Include token counts and wall-clock training time to allow readers to assess the practical cost of the prior-guided data generation step.

---

## Score and Decision

The paper tackles an important and timely topic with a clean theoretical framing and a practical pipeline. The proof-of-concept result (Figure 3) is genuinely compelling. However, the central empirical result—25% faithfulness after training versus 85% using the prior directly—is unexplained and undercuts the core contribution. The experiment is limited to a single small model, the faithfulness metric has a conceptual gap, and the algorithm as written has a notational inconsistency. The contribution as a whole is the instantiation of "curate data via a stronger prior model, then SFT," which is a reasonable but not novel approach. These issues together push the paper below the acceptance threshold.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>