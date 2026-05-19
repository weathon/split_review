- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 5, 6
Now I have a thorough understanding of the paper and can synthesize the review. Let me construct the consolidated assessment.

## Summary

The paper introduces PassUntil, an evaluation strategy based on inverse binomial sampling, to measure very small success probabilities in LLM evaluations (down to ~10⁻⁵). Using this high-resolution measurement, the authors discover that small models (0.03B–1.5B) show consistent, measurable improvement on tasks previously thought to exhibit "emergent" breakthrough behavior. They derive a task scaling law PU ∼ exp(−cN⁻ᵅ) from the loss scaling law and demonstrate accurate prediction of a 2.4B model's performance (0.05% deviation on HumanEval series 1). The paper also categorizes growth curves into sub-scaling, scaling-law, and super-scaling (accelerated emergence) types, and provides mathematical analysis relating these shapes to multi-step reasoning and multiple-circuits hypotheses.

## Strengths

- **PassUntil evaluation strategy (Section 4.1).** The paper proposes a practical sampling-based method that can measure success probabilities as low as 10⁻⁵, well below what conventional evaluation detects. The method is correctly grounded as a maximum likelihood estimate (negative binomial → r/K). This is the key enabler for all subsequent findings and is a genuine practical contribution to LLM evaluation methodology.

- **Empirical demonstration of predictable task scaling (Sections 5.3–5.4, Table 1).** The paper trains two model series (0.03B–2.4B), fits a scaling law to the four smaller models, and predicts the held-out 2.4B model's performance. The instance-level fit achieves 0.05% deviation on HumanEval (series 1) and 1.7% on Date Understanding (series 2). The prediction of a held-out model from smaller ones is a valid experimental design that directly supports the paper's core claim.

- **Conceptual framework for categorizing emergence (Section 6, Definition 1).** The paper formally defines three types of scaling curves (sub-scaling law, scaling law, super-scaling law/accelerated emergence) in terms of convexity/linearity/concavity of log(−log(PU)) vs. log N. This provides a useful vocabulary and mathematical grounding for thinking about different kinds of emergent behaviors, going beyond prior descriptive accounts.

- **Theoretical analysis linking growth shapes to model structure (Theorems in Section 6).** The paper proves that multi-step reasoning predicts convex (sub-scaling) growth, while a multiple-circuits hypothesis predicts concave (super-scaling) growth. These are mathematically sound results that offer testable connections between model architecture and scaling behavior.

## Weaknesses

### Fatal

None.

### Major

- **Prediction validation lacks uncertainty quantification and generalization testing.** The paper reports 0.05% deviation on HumanEval but provides no confidence intervals around the predicted value, no cross-validation testing (e.g., predicting an intermediate model size from smaller ones), and no evaluation on an unseen model family (e.g., Pythia or GPT-2) to verify that the task scaling law is not an artifact of the specific architecture and training recipe. With only 4 data points fitting a 2-parameter model, and a single held-out point for validation, one cannot assess whether the prediction accuracy generalizes. The 0.05% figure could be a fortuitous fit; the paper needs bootstrap confidence intervals and ideally a held-out model size or model family.

- **The accelerated emergence analysis lacks rigorous comparison against simpler alternatives.** The 2-circuit soft voting model is fit to 4–5 data points per task with 4 parameters (α₁, α₂, c₁, c₂), but the paper never tests whether the concave fit is statistically significant (e.g., does a quadratic term in log N fit significantly worse?), nor does it compare against simple baselines such as a quadratic or sigmoid in log–log space. The claim that the circuit model "aligns more accurately" is qualitative. With this few data points, a 4-parameter model is expected to fit well regardless of the true underlying process. The paper correctly acknowledges this is a "loose" test, but the presentation implies stronger confirmation than the evidence supports.

### Minor

- **Conceptual gaps in the derivation of the task scaling law from loss scaling (Section 4.2).** The derivation equates PU with the product of token probabilities of the *most probable* correct sequence, while PassUntil measures the probability that *any* generation passes. The paper assumes "its dominance compared to other sequences" (line 116) and uniform α across all tokens. For generation tasks like HumanEval, where many correct solutions exist, multiple correct sequences may contribute, making the derived form an approximation whose accuracy is untested. The paper does not verify whether the functional form holds when computed directly from token probabilities. These gaps are acknowledged but not examined, weakening the claimed theoretical foundation.

- **Limited scope of the accelerated emergence study.** Only 8 tasks from one benchmark (UICL in BigBench) are studied, and 3 of the 8 are missing data points for the smallest models. A phenomenon claimed as a general category of emergence is supported by 5 tasks from a single benchmark. The paper should either acknowledge this limitation more prominently or provide additional evidence from other benchmarks.

- **The two-stage prediction for hard instances (estimating PU from test loss) introduces unquantified uncertainty.** The paper uses a learned mapping from test loss to PU for hard instances without reporting the error in this mapping or how it contributes to the final prediction. The 0.05% figure on HumanEval (series 1) might not reflect accuracy on tasks requiring this two-stage procedure.

### Trivial

None.

## Nice-to-Haves

- **Direct comparison to Schaeffer et al.'s "increase resolution" approach.** The paper distinguishes its approach from Schaeffer et al.'s but never directly compares them. For a fixed compute budget, does PassUntil (aggressive per-instance sampling) give better predictions than the Schaeffer approach (more test instances with fewer samples each)? This comparison would strengthen the justification for PassUntil.

- **Ablation on the choice of r.** The paper uses r=1 or 2 but does not study the effect of this choice on estimate variance or prediction accuracy.

- **Analysis of how resolution improves with sampling budget.** A plot of PU estimate vs. K for a few instances would help other researchers set practical sampling budgets.

- **Generalization to an unseen model family.** Testing the task scaling law on Pythia, GPT-2, or another independently trained series would substantially strengthen the claim that the law is general rather than architecture-specific.

## Removed Points

These points were raised by reviewers but are excluded from the main weaknesses for the reasons stated:

1. **"Infinite resolution is misleading."** The paper qualifies this with "theoretically" and "as long as computational resources are not bounded" (line 32), and explicitly mentions the practical bound of K_max=10⁵ (line 100). In the limit K→∞, resolution→0, so the claim is theoretically accurate. Removed as a mischaracterization.

2. **"The derivation fails for 5/8 UICL tasks."** This is the paper's own finding that it calls "accelerated emergence." The paper uses the derivation to establish a baseline expectation, then discovers deviations — that is the contribution, not a flaw. Removed because it misreads the paper's argument structure.

3. **"The paper does not discuss the bias of r/K."** With r=1,2 and K up to 10⁵, the bias of the MLE for negative binomial is negligible in this regime. Removed as technically correct but practically irrelevant.

4. **"The comparison to beam search is unfair."** The pilot compares beam search and random sampling only to illustrate that more samples increase resolution, not to claim superiority. Removed.

5. **"The quote is pretentious."** Style opinion. Removed per formatting/style instructions.

6. **Missing related works.** Cannot be verified externally. Removed per instructions.

7. **Speculation about unverified assumptions leading to "the derivation is flawed."** While the derivation has conceptual gaps (kept as a Minor weakness), the claim that it is "flawed" or should be abandoned is too strong given the paper's explicit listing of assumptions.

## Novel Insights

The reviews surface an interesting tension not fully explored by the paper itself: PassUntil's enormous sampling budget (10⁵) per instance is what enables the discovery of smooth task scaling in small models, yet the same abundance of sampling also creates a risk of detecting statistically significant-but-spurious improvements — especially for generative tasks where the space of possible correct answers is large. The paper's 0.05% prediction on HumanEval is remarkably precise, but without confidence intervals one cannot distinguish between genuine predictive power and an overfit to the 4-point trend. A more subtle point: the accelerated emergence analysis claims the circuit model fits "better" than the scaling law, but since the scaling law is a special case of the circuit model (when the two circuits converge or one dominates), the comparison is not between independent alternatives but rather between a restricted and an unrestricted model — the unrestricted model will always fit at least as well. The interesting question is whether the improvement is statistically significant, which the paper does not address.

## Suggestions

1. **Add confidence intervals.** Report bootstrap or Bayesian confidence intervals around all predicted values (Table 1), and ideally around the fitted α parameters.
2. **Add held-out validation.** At minimum, predict an intermediate model size (e.g., 0.3B or 1.5B) from smaller models to verify that the trend generalizes within the series. Stronger: test on an independently trained model family.
3. **For the accelerated emergence analysis:** Compare the 2-circuit model against a simple quadratic in log N (which also has 3 parameters) using a nested model test or AIC/BIC. Report whether the concavity is statistically significant given the bootstrap standard errors shown in the figures.
4. **Acknowledge the derivation gap explicitly.** State that the task scaling law is empirically observed to follow the form exp(−cN⁻ᵅ), and that the derivation from loss scaling is intended as motivation with acknowledged simplifying assumptions, not a formal proof.
5. **Discuss computational cost tradeoffs.** 10⁵ samples × 20 instances × 5 models = 10⁷ forward passes. Put this cost in context for practitioners.
