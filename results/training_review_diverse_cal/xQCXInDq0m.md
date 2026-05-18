Here is my consolidated final review.

---

## Summary

This paper introduces Context Steering (CoS), a training-free inference-time method that modulates the influence of contextual information on LLM outputs. CoS computes the log-likelihood difference between an LLM's predictions with and without a context, then scales this difference by a parameter λ to amplify or attenuate contextual effects. The paper applies CoS to three tasks: personalization (movie summarization), bias mitigation (BBQ, IAT), and hate speech quantification (implicit hate tweets). The core idea is conceptually clean and interpretable.

## Strengths

- **Training-free, inference-time control with an interpretable formulation.** CoS operates entirely at inference time by modifying next-token log-probabilities, requiring no fine-tuning, data collection, or model weight access. The contextual influence function defined as LLM(·|C,P) − LLM(·|∅,P) provides an interpretable mechanism distinct from activation-steering or contrastive-decoding approaches (Eq. 1, Section 3.2).

- **Unified approach across diverse applications.** The same CoS framework is applied to personalization, bias mitigation, and hate speech quantification — problems typically addressed with separate methods. The qualitative examples (Table 1, Table 2) compellingly demonstrate that varying λ produces coherently modulated outputs.

- **BBQ bias reduction results are clear and systematic.** On the BBQ benchmark, CoS with an equalizing context improves accuracy and reduces bias across all topics for both T0pp and Mistral-7b-instruct models, with effects scaling monotonically with λ (Figure 3, Section 4.2). This is the cleanest quantitative evidence in the paper.

- **Applicable to API-gated models.** The method only requires access to output log-probabilities, not internal weights, making it usable with black-box LLM APIs (Section 1).

## Weaknesses

### Fatal
None.

### Major

- **Personalization user study uses only two λ values, undermining the "trend" claim.** The human study (8 participants, 70 responses each) tests only λ ∈ {-1, 3}. With only two discrete λ levels, the data cannot demonstrate a *monotonic trend* — it can only show that λ=3 and λ=-1 differ. The reported Spearman ρ = 0.67 (p < 0.001) is not interpretable as evidence of a monotonic relationship because with a binary independent variable, Spearman's correlation merely reflects a group mean difference (and if computed on two group-level averages, ρ would be forced to ±1). The paper's central claim of "controllable" personalization that "increases with λ" needs at least 3–5 λ values (e.g., -1, 0, 1, 2, 3) with appropriate regression or trend analysis to be properly supported. The comparison between λ=-1 and λ=3 itself is valid but insufficient to establish smooth controllability.

### Minor

- **No controlled validation of the inverse inference procedure.** Equations (3) and (4) define Bayesian inversion to recover context or λ from a generation, and a qualitative example is provided (Figure 2), but there is no controlled experiment measuring how accurately CoS recovers known ground-truth λ values or known contexts. The hate speech quantification (Section 4.3) uses the inferred λ as its measure without first validating the inference. End-to-end correlation with human ratings (p = 0.0295) partially addresses this, but a controlled synthetic evaluation would substantially strengthen the quantification claim.

- **IAT bias reduction is confounded by potential task refusal.** The paper reports that for association tasks, "higher λ results in an increased rate of the model rejecting to answer the request" (Section 4.2). If the model selectively refuses harder cases under higher λ, the remaining responses will appear less biased by selection artifact rather than genuine debiasing. Refusal rates are not reported separately from bias scores, making it impossible to distinguish genuine debiasing from task avoidance.

- **No comparison against other inference-time control methods.** The paper compares CoS against its own λ=0 (standard context prepending) and λ=-1 (no context) baselines but not against any existing inference-time control technique (e.g., DExperts, activation steering, contrastive decoding, or simple logit interpolation without the subtraction term). While the paper's contribution is the CoS method itself, comparisons against alternatives would help assess whether the specific CoS formulation offers practical advantages.

- **BBQ evaluation only covers ambiguous prompts.** The paper evaluates accuracy and bias on ambiguous BBQ prompts but does not report whether CoS preserves performance on disambiguated prompts, where "unknown" is not the correct answer. This is important for practical deployment.

- **Hate speech classification accuracy is uneven and well below human performance.** CoS achieves 82% on the Black group (human: 88%) but only 47% on the Immigrant group (human: 64%), barely above random chance for 3 classes. The method underperforms the LLM baseline on the Muslim group (60.5% vs. 62%). These results are reported transparently but weaken the classification claims.

- **No discussion of the computational cost of two forward passes per token.** CoS requires one forward pass with context and one without at each generation step. This cost is not discussed, which is relevant to the claimed API-gated applicability.

- **Choice of λ values varies across experiments without rationale.** λ = -0.5 for hate classification, varying values for BBQ, λ ∈ {-1, 3} for personalization. No justification is given for these specific choices, giving the method an ad-hoc appearance.

### Trivial
- No explicit discussion of computational cost/latency of the dual forward pass.

## Nice-to-Haves

- Run the personalization study with 4–5 λ values (e.g., -1, 0, 1, 2, 3) and analyze with a linear mixed model treating λ as a continuous predictor.
- Add a controlled validation of the inverse model by fixing contexts and λ, generating responses, and measuring recovery accuracy.
- Report refusal rates separately from bias scores in the IAT experiments.
- Evaluate CoS on both ambiguous and disambiguated BBQ prompts.
- Compare CoS against at least one alternative inference-time control method.
- Provide guidance or a simple heuristic for selecting λ values for different tasks.

## Removed Points

- **"Correlation with two points is always ±1, and p-values cannot be properly calculated"** — The reviewer assumed ρ was computed on two aggregated points. With 560 individual-level ratings (8 participants × 70 responses) and λ as a binary variable, a correlation/p-value *can* be computed across individual data points; the deeper issue (only 2 λ values cannot demonstrate a monotonic trend) is retained in Major.
- **"Figure 4 appears to show more than two points"** — Speculative without seeing the figure; the paper may be plotting per-movie results, which would naturally show multiple points per λ condition. Removed.
- **Missing related works** — Per policy, I cannot confirm existence of missing citations.
- **Formatting/style nitpicks** — Removed as parser artifacts.
- **Reproducibility nitpicks about undisclosed hyperparameters** — No severe reproducibility gaps warrant citation.
- **"Framework unifies disjoint problems"** (strength from Strength Finder) — Kept as it is supported by the paper.
- **"Controllable personalization validated by human study with Spearman ρ=0.67"** (strength) — Weakened rather than dropped; the comparison λ=-1 vs λ=3 is still informative even though the trend claim is overextended. The strength is retained in spirit but the weakness is flagged.

## Novel Insights

The main novel insight from synthesizing the reviews is that CoS is caught between two evaluation paradigms. The strongest evidence (BBQ) shows monotonic λ-dependent debiasing, validating the core mechanism. Yet the paper's flagship demonstration (personalization) uses the weakest design — only two λ values — while the inverse inference (hate speech) lacks the controlled validation that would close the loop. This suggests the paper's contributions are real but unevenly supported: the forward control mechanism is convincingly demonstrated on BBQ, but the "controllable dial" claim and the Bayesian inversion pipeline both need tighter experiments. A paper restructured to lead with the BBQ results, add a controlled inverse-model validation, and relegate the personalization study to a proof-of-concept (acknowledging its limited λ range) would present a cleaner, more defensible contribution.

## Suggestions

1. Expand the personalization user study to include 4–5 λ values (-1, 0, 1, 2, 3) and use linear mixed-effects modeling with λ as a continuous predictor to properly demonstrate monotonic controllability.
2. Add a synthetic validation experiment for the inverse model: fix (C, P, λ), generate responses, then measure how accurately the inference procedure recovers the true λ or context.
3. Report refusal rates alongside bias scores for the IAT experiments, or design the experiment to distinguish genuine debiasing from selective non-response.
4. Evaluate CoS on disambiguated BBQ prompts to show the method does not harm performance when "unknown" is not the correct answer.
5. Include at least one comparison against a simple alternative (e.g., repeated context prepending, or logit interpolation without the subtraction term) to establish whether the specific CoS formulation matters.
6. Acknowledge the 2× per-token computational cost and discuss practical implications for API usage.

## Score and Decision

The core idea is sound and the BBQ results provide reasonably convincing evidence that CoS modulates contextual influence. However, the personalization user study — the paper's flagship demonstration — has a methodological flaw that substantially weakens the "controllable personalization" claim, and the inverse model validation is missing a controlled experiment. The paper would benefit from a major revision addressing these gaps. In its current form, the evidence is too uneven to recommend acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>