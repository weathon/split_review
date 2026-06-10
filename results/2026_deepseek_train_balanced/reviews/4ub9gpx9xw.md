## Summary

This paper introduces "causal concept faithfulness," a formal definition of faithfulness for LLM explanations grounded in causal inference (correlating true causal concept effects with explanation-implied effects), and proposes a Bayesian hierarchical modeling approach to estimate it under realistic API-access constraints. The method is applied to three LLMs (GPT-3.5, GPT-4o, Claude-3.5-Sonnet) on two datasets (BBQ social bias, MedQA medical QA), revealing patterns of unfaithfulness including cases where LLM explanations hide the influence of safety measures.

## Strengths

- **Rigorous causal formalization of faithfulness (Section 2, Definitions 2.1–2.3).** The paper defines faithfulness as the Pearson correlation between vectors of causal concept effects (CE, measured via KL divergence over answer distributions after intervention) and explanation-implied effects (EE, measured as mention rates). This is significantly more precise than prior work relying on task-specific adversarial tests or human evaluation, and provides a general mathematical framework applicable across settings.

- **Bayesian hierarchical estimation for sample efficiency under API constraints (Section 3).** The paper addresses a real practical challenge—estimating per-question concept faithfulness with limited API calls—by using hierarchical models that pool information across questions via shared priors on concept-category effect magnitudes and a global faithfulness parameter. This is a genuine methodological innovation over prior perturbation-based approaches that either require large samples or produce high-variance estimates.

- **Discovery of a new semantic pattern of unfaithfulness (Section 4.1, lines 133–134).** The method reveals that GPT-4o and GPT-3.5 produce explanations that omit the influence of safety measures: when identity information is present, models select "Undetermined" but attribute this to question ambiguity rather than the presence of social identity information. The paper correctly notes this pattern was not reported in prior work. This demonstrates the method's ability to surface interpretable patterns beyond aggregate scores.

- **Nuanced analysis that faithfulness scores alone can mislead about harm (Section 4.1, lines 135–141).** The paper shows GPT-3.5 has the highest quantitative faithfulness score (0.75) on BBQ but is unfaithful in a potentially more harmful way (masking social bias) than less-faithful models. This concretely validates the paper's central argument about the importance of semantic patterns.

## Weaknesses

### Fatal

None.

### Major

- **Insufficient validation that the method measures faithfulness.** The paper acknowledges "there is no ground truth for faithfulness" (line 98) but responds by leveraging BBQ's known unfaithfulness patterns as partial validation. However, several validation strategies that would significantly strengthen the claims are absent: (a) no synthetic experiments where ground-truth faithfulness is known by construction (e.g., a model with a known decision rule and explanation policy); (b) no quantitative comparison to any existing faithfulness measure from prior work (Turpin et al.'s task-specific probes, Lanham et al.'s post-hoc tests, Chen et al.'s simulatability metric); (c) no human evaluation; (d) no sanity checks (e.g., verifying that a model prompted to produce faithful explanations scores higher). The BBQ-based validation recovers one known pattern (hiding social bias) and discovers one new pattern, but this provides only face validity. The central empirical claims—that GPT-3.5 has F=0.75 on BBQ, that GPT-4o has F=0.34 on MedQA, that one model is more faithful than another—rest on the assumption that the operationalization (PCC between CE and EE as estimated by the Bayesian model) captures the construct of faithfulness. The paper provides limited evidence for this assumption.

- **Heavy reliance on GPT-4o for five distinct subtasks with no quality control, while GPT-4o is also one of the evaluated models.** GPT-4o is used to: (a) extract concept sets from each question (line 72), (b) identify concept values and alternative values (line 72), (c) assign concepts to categories (line 72), (d) generate all counterfactual questions (line 74), and (e) determine whether each model's explanation mentions a concept (line 82). Errors in any step propagate into the faithfulness estimates, but there is no error analysis, no human validation, and no inter-annotator agreement check for any of these steps. The limitations section (line 186) states the outputs are "high-quality in general" but provides no evidence. The fact that GPT-4o is both the primary auxiliary model and one of the three models being evaluated amplifies the concern: for the GPT-4o-as-M case, the same model generates the counterfactuals, classifies its own explanations, and evaluates its own faithfulness. Systematic biases in GPT-4o's concept extraction or explanation analysis could differentially affect the evaluation of GPT-4o itself.

- **No quantitative comparison to existing faithfulness methods.** The paper discusses prior work (Turpin et al., Lanham et al., Chen et al., Parcalabescu & Frank) in Section 5 but never compares its method against any existing approach. Even a simple convergent-validity check—e.g., whether the method's faithfulness rankings align with Turpin et al.'s finding that LLMs mask social bias on BBQ, or whether the method produces different conclusions than simpler alternatives—would help establish credibility. Without such comparisons, the added value of the proposed method over existing approaches is unclear.

- **Bayesian hierarchical model is underspecified for reproducibility.** Section 3 describes the modeling approach at a high level but omits: (a) the specific prior distributions used, (b) the inference algorithm (MCMC? variational Bayes?), (c) the software framework, and (d) any convergence diagnostics. Without these details, the method cannot be reproduced or audited. Given that the entire empirical contribution depends on this estimation procedure, the lack of specificity is a significant barrier.

### Minor

- **Overlapping credible intervals undermine comparative claims about model faithfulness.** On BBQ, the scores are GPT-3.5: F=0.75 (90% CI=[0.42, 1.00]), GPT-4o: F=0.56 (CI=[0.24, 0.86]), Claude: F=0.64 (CI=[0.33, 0.95]). All intervals overlap substantially. The paper states "GPT-3.5 produces more faithful explanations than the two more advanced models" but the evidence for this comparative claim is weak given the intervals. Similar overlap is present on MedQA. The paper does not discuss whether inter-model differences are statistically meaningful.

- **"Hiding the influence of safety measures" interpretation is plausible but not uniquely supported.** The paper attributes the pattern to safety alignment measures (line 133), but an equally plausible alternative exists: the model may simply recognize the BBQ question as a stereotype test (by the presence of identity information in an intentionally ambiguous context) and choose "Undetermined" as a cautious response, without this being related to safety alignment per se. The paper's hedging ("it appears that") appropriately limits the claim, but the interpretive framing around "safety measures" goes beyond what the data can distinguish.

- **Disentanglement assumption is stated but not verified (Section 2, line 31).** The paper assumes concepts can be changed independently, which is a strong assumption for natural language (e.g., changing "candidates' genders" likely requires changing pronouns, names, and potentially correlated descriptions). The paper relies on GPT-4o to generate counterfactuals that respect disentanglement but provides no verification that the generated counterfactuals actually change only the targeted concept. If interventions change multiple concepts simultaneously, the CE estimates conflate multiple causal effects.

- **EE definition averages mention rates across original and counterfactual questions without justification (Definition 2.2, line 52).** The definition averages the model's explanation mention probability across both the original input and all counterfactual inputs. The model's explanations for counterfactual questions may reference entirely different concepts (since the counterfactual changes the input), and averaging across different inputs conflates explanation behavior in different contexts. The rationale for this design choice is not explained; it would be more natural to only consider explanations for the original question.

### Trivial

None.

## Nice-to-Haves

- Synthetic experiments with a controlled LLM where ground-truth decision rules and explanation policies are known would strongly validate the method.
- A human evaluation of, say, 50 counterfactuals checking for realism, minimality, and disentanglement would strengthen the causal estimation pipeline.
- A stability analysis testing whether results hold when using a different auxiliary LLM (e.g., Claude-3.5 as auxiliary for evaluating GPT models) would alleviate concerns about the GPT-4o dual role.
- Specifying the Bayesian model's priors, inference algorithm, and convergence diagnostics would improve reproducibility.

## Removed Points

These are flagged for removal; treat them with caution:

1. **Harsh critic's Claim 1 framed as "fatal":** The critic says "no evidence that the method measures faithfulness." This is overstated—the paper provides partial validation through the BBQ task structure (recovering known patterns of unfaithfulness). The underlying concern remains valid and is retained as a Major weakness, but the "fatal" severity is not warranted given the paper's theoretical grounding and partial validation attempts.

2. **Harsh critic's "structural gap" language:** The critic asserts the paper cannot be accepted "without a validation study." This judgment call is resolvable through peer review; the retained Major weakness is sufficient to convey the severity of the concern.

3. **Harsh critic's point about "method not applicable to existing systems":** The critic says "does not correspond to currently available systems." All models and tools cited in the paper are assumed to exist per review guidelines. This is removed.

4. **Harsh critic's note about "stability analysis (range of N cut off)":** This is a PDF parsing artifact; the original submission presumably contains the full analysis. Removed.

5. **Strength Finder's generic phrasing about "important problem":** The paper's problem importance is evident; this strength is too generic to retain as a distinct item.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no weakness or strength that fundamentally reframes the paper's contribution beyond what the paper itself states. The key tension (strong theoretical framing + weak empirical validation) is apparent from reading the paper directly.

## Suggestions

1. **Add a validation experiment with synthetic ground truth.** Construct questions where the model's "true" decision rule is known (e.g., a deterministic rule based on concept A only) and verify that the method recovers the expected CE and EE patterns. This would provide the strongest evidence that the measurement pipeline works.

2. **Add a human quality check on GPT-4o's outputs.** Sample 50–100 counterfactuals and have annotators assess realism, minimality, and disentanglement. Report error rates for concept extraction, category assignment, and explanation classification. This would address the most actionable concern about the method's pipeline.

3. **Compare against at least one prior faithfulness method.** Apply a simplified version of prior work (e.g., Turpin et al.'s BBQ-specific probe, or Chen et al.'s simulatability metric) to the same data and compare the resulting faithfulness characterizations. Even qualitative agreement/disagreement analysis would help calibrate the community's understanding.

4. **Report Bayesian model details.** Specify priors, inference algorithm (e.g., NUTS-MCMC with PyMC or Stan), and convergence diagnostics (e.g., R-hat, effective sample sizes). This is essential for reproducibility.

## Score and Decision

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>