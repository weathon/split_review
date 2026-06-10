## Summary

This paper formalizes four types of explanation disagreement (stakeholder, model, method, ground truth) under a ranking-based framework and proposes EXAGREE, a two-stage pipeline that (1) samples a Rashomon set of masked model variants and trains a surrogate (DMAN) to map masks to attributions, then (2) optimizes a multi-head mask network with differentiable sorting to find Stakeholder-Aligned Explanation Models (SAEMs) whose ranking-based explanations match target preferences. Experiments on the OpenXAI benchmark show improvements in explanation faithfulness metrics and subgroup fairness relative to the original black-box model.

## Strengths

- **Formal, unified taxonomy of explanation disagreement types.** Section 2.1 (lines 63–73) provides crisp ranking-based definitions for stakeholder, model, explanation method, and ground truth disagreement under a common formalism. Prior work treated these in isolation; the paper's unification into a structured framework is a genuine conceptual contribution.

- **End-to-end differentiable pipeline for Rashomon-set search under ranking supervision.** The two-stage framework (Section 3) integrating mask-based model characterization, DMAN surrogate, and DiffSortNet for ranking-based optimization is technically novel. No prior work has combined differentiable sorting with Rashomon-set search for explanation-targeted model selection.

- **Quantitative evidence of improved subgroup fairness.** Fig. 4 (line 447) compares faithfulness metrics across male/female subgroups for the original model vs. SAEMs on Adult Income, COMPAS, and German Credit. The SAEMs visibly reduce inter-subgroup disparities in faithfulness, which is a practically meaningful result beyond aggregate agreement.

- **Consistent improvements in faithfulness metrics across multiple datasets and explanation methods.** Tables 1 and 2 show that FIS\_SAEM rows achieve the highest or tied-highest number of best-in-class metrics (e.g., 7/8 for ANN on Adult Income), improving over FIS baselines and the original black-box model on RA, SRA, and other metrics.

## Weaknesses

### Major

- **The experimental evaluation does not test the multi-stakeholder scenario the paper's framing revolves around.** The paper's headline motivation is reconciling *diverse* stakeholder preferences. Yet line 255 states: "To establish a consistent benchmark for stakeholder needs, we adopted the ground truth explanations derived from the pre-trained LR as our constant target ranking." Every experiment uses a **single** target ranking (LR coefficients). The paper attempts to proxy different stakeholders via different explanation methods (line 395), but all these "stakeholders" share the same target. Reconciling explanation method disagreement against a fixed ground truth is a weaker claim than reconciling genuinely diverse stakeholder preferences (where Stakeholder A wants features [1,2,3] and Stakeholder B wants [4,5,6]). The multi-head architecture and Proposition 1 (which is about *multiple* stakeholders disagreeing) are motivated by the multi-stakeholder case, but this scenario is never instantiated. **This gap directly reduces the scope of what the paper demonstrates relative to what it claims.**

- **The Rashomon set is restricted to masked variants of a single model architecture, not a diverse set of model classes.** Line 155 states: "all models in the sampled set can be characterized by masks." The GRS algorithm produces feature-masked versions of a single reference model (LR or ANN). The Rashomon set in the broader literature (Fisher et al. 2019, Rudin et al. 2024) encompasses functionally diverse models across architectures (trees, linear models, neural nets). The paper uses a much narrower search space. This is especially limiting when the reference model and the ground-truth model share the same architecture (LR): the SAEM is essentially a feature-masked LR whose attribution ranking is compared to unmasked LR coefficients — the improvements may partly reflect trivial sparsity effects.

- **The DMAN surrogate's approximation quality is entirely uncharacterized.** The DMAN predicts attributions from masks during optimization, but evaluation uses actual attributions (line 163). The paper acknowledges that "its accuracy is crucial" yet provides **no analysis** of the surrogate: no correlation between predicted and actual attributions, no ablation of surrogate quality, no error analysis. If the surrogate is inaccurate, the optimization may chase phantom improvements or miss genuine ones. This is a methodological gap affecting the reliability of all reported results.

- **Results are reported as point estimates without variance, confidence intervals, or statistical significance.** All tables present single values with no standard deviations across independent runs of the stochastic Rashomon sampling or SAEM optimization. Combined with undefined key parameters ($k$ is never defined despite appearing in all table/figure captions; $\epsilon$, $\lambda_1$, $\lambda_2$ values are not reported; the number of heads $h$ is not given), the experimental evaluation lacks the detail needed for reproducibility or for assessing robustness.

### Minor

- **The lemma (lines 183–185) is empty** — it has a \begin{lemma} and \end{lemma} with no content between them. This appears to be a template artifact left unfilled.

- **Proposition 1 (lines 188–194) is stated without proof and uses notation confusingly.** $M^*$ on the left-hand side denotes a "better" model, but $M^*$ was previously used (Eq. 1) to denote the optimal predictive model. The claimed proportionality relation is intuitively plausible but is presented as a Proposition with no supporting argument or proof.

- **The "User-friendly Interface" (line 450–451) is mentioned in a single sentence with no evaluation or demonstration.** Including it as part of the contribution without even a qualitative description weakens the paper's rigor.

- **Global averaging of local attributions (line 105) is a methodological choice that conflates local and global faithfulness.** The paper adapts local-level metrics to global by averaging attributions across instances, without justification or analysis of how this affects the metrics' meaning.

### Trivial

- None beyond those already captured above.

## Nice-to-Haves

- Vary $\epsilon$, $\lambda_1$, $\lambda_2$, and $h$ systematically and test robustness
- Compare EXAGREE against simple baselines for the same problem, e.g., directly selecting models with desired attribution sparsity patterns or training a model with explanation regularization
- Add a synthetic experiment where two stakeholders have *different* target rankings, to directly test the multi-stakeholder claim

## Removed Points

*These points were flagged by reviewers but are removed or demoted from the main weaknesses for the reasons stated below:*

- *Missing results for COMPAS, GMSC, HELOC, German Credit datasets* — These tables are referenced in the text (lines 400, 404) but are absent from the extracted PDF body. Per the review guidelines, parser-stripped sections are assumed to exist in the original submission. Not penalized.
- *Missing ablation study content* — Fig. \ref{fig:ablation} is referenced (line 400) but its content is not visible. Same parser-artifact reasoning.
- *Missing comparison to alternative approaches (ensembling explanations, etc.)* — The paper already compares against LIME, SHAP, Integrated Gradients, Vanilla Gradient, SmoothGrad, Gradient x Input, Random, and FIS baselines in the main tables. The set of baselines is standard for the benchmark.
- *Grammatical issues (broken sentence about Gemini API)* — Parser artifact, not present in the original submission.
- *Demand for user studies or human-subject experiments* — This is beyond the scope of a methodological/technical paper.
- *"First framework" overclaim without exhaustive literature positioning* — Minor scope of novelty, but the paper does cite relevant Rashomon-set and XAI disagreement work. Missing-related-work criticisms are filtered per guidelines.

## Novel Insights

The merger reveals a structural mismatch between the paper's framing and evaluation that neither individual review fully crystallized. The paper sells itself as solving *stakeholder* disagreement (people wanting different feature rankings), but the experiments only test *explanation method* disagreement against a fixed ground-truth. The harsh critic identified the proxy but framed it as absolute failure; the strength finder accepted the proxy at face value. The actual contribution is narrower than claimed but not vacuous — the differentiable Rashomon-set search pipeline and the fairness analysis are real contributions that would benefit from an honest reframing. The empty lemma and unanalyzed surrogate suggest the paper was rushed, but the core idea (searching over model variants for better explanation alignment) is worth pursuing.

## Suggestions

1. **Reframe the paper around what is actually evaluated.** Drop or substantially tone down the "stakeholder disagreement resolution" framing unless multi-stakeholder experiments (different target rankings) are added. The paper's actual contribution — a differentiable method to find masked model variants whose explanations better match a reference attribution — is still publishable if honestly scoped.

2. **Analyze DMAN surrogate accuracy.** Report at minimum the correlation between DMAN-predicted and actual attributions on a held-out set of masks, and show that optimizing with the surrogate leads to SAEMs that genuinely improve actual (not predicted) metrics.

3. **Report variance and define all parameters.** Run the full pipeline multiple times with different random seeds and report means ± std. Define $k$, report the value of $\epsilon$, list $\lambda_1$ and $\lambda_2$, and state the number of heads $h$.

4. **Fill the empty lemma or remove it. Provide a proof sketch for the proposition** — or demote it to a remark if it cannot be proven.

5. **Test the multi-stakeholder setting directly.** Create a synthetic scenario with two stakeholders who prefer different feature rankings, and demonstrate that EXAGREE can find SAEMs satisfying each.

## Score and Decision

**MY FINAL SCORE: <score>4.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**