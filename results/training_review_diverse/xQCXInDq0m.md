Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes Context Steering (CoS), a training-free inference-time method that modulates the influence of contextual information on autoregressive LLM outputs. By computing the log-likelihood difference between conditioned and unconditioned token predictions and scaling it by a parameter λ, CoS can amplify context for personalization or attenuate it for bias mitigation. The method is clean, interpretable, and demonstrated across three applications: personalized movie summarization, bias reduction on BBQ and IAT benchmarks, and implicit hate speech classification/quantification via a Bayesian inverse formulation.

## Strengths

- **Training-free, inference-time control with an interpretable mechanism.** CoS operates purely at inference time using log-probability differences (Eq. 3), requires no fine-tuning or additional data collection, and works with any autoregressive LLM that exposes log probabilities — including API-gated models. The formulation is transparent and directly tied to token-level likelihoods.

- **Demonstrated controllable personalization with statistical significance.** The user study (N=8) shows a significant Spearman correlation (ρ=0.67, p<0.001) between λ and perceived personalization ratings across 70 movie–genre–λ combinations. The qualitative examples (Tables 1–2) convincingly illustrate that CoS can tailor responses even for orthogonal movie–genre pairs (e.g., finding comedic aspects of *Blade Runner 2049* under a comedy context).

- **Unified treatment of three distinct applications under one framework.** The same λ-scaling mechanism is applied without modification to personalization, bias mitigation, and hate quantification. This breadth demonstrates generality beyond a single task.

- **Interpretable inverse Bayesian formulation.** The ability to infer which context (Eq. 7) or what λ value (Eq. 8) likely produced a given generation provides a principled tool for probing latent assumptions in LLM outputs. The hate quantification experiment validates this approach against expert human ratings with a significant correlation (p=0.0295).

## Weaknesses

### Fatal

None.

### Major

- **No baselines against existing debiasing or personalization methods for the core claims.** For bias mitigation, the paper compares CoS only against the unmodulated model (λ=0). No comparison is made to established methods such as Self-Debias, DExperts, INLP, or instruction-based debiasing (e.g., "Be unbiased"). Without knowing whether CoS adds value over or is competitive with existing approaches, its claimed advantages for bias mitigation are unsubstantiated. The BBQ and IAT experiments show a positive trend with λ, but the lack of baselines makes it impossible to assess whether CoS is merely "better than nothing" or genuinely competitive.

- **Small user study with limited controls.** N=8 participants is insufficient to support strong claims about personalization quality. The paper reports no inter-rater reliability metric (e.g., Krippendorff's alpha), and it is unclear whether responses were fully randomized per participant or whether participants were blind to the genre condition (beyond λ). The study design also lacks a non-CoS control condition. The significant result (p<.001) is encouraging as a pilot, but the paper presents this as primary evidence when it should be treated as suggestive.

- **Inverse Bayesian inference lacks rigorous evaluation.** The context-inference formulation (Eq. 7) is validated only via classification accuracy on implicit hate (Figure 5 right) and the λ-inference (Eq. 8) via correlation with human ratings. However, there is no analysis of how the candidate set size or composition affects results, no ablation, and only one qualitative example (Figure 2) for the context-probing use case. The STEM proficiency example (Figure 2/3) is presented as a key capability but is purely illustrative.

- **No error bars, confidence intervals, or statistical tests on key quantitative results.** The BBQ and IAT results are presented as figures with no visible error bars or standard deviations. The bias metric used in BBQ is not explicitly defined in the main text. The hate quantification correlation (p=0.0295) is marginal and reported without a confidence interval.

### Minor

- **No λ sensitivity or ablation analysis across tasks.** The method's only free parameter is λ, yet the paper never studies how results vary with λ systematically beyond two values for personalization (λ∈{-1,3}) and the λ ranges shown in BBQ figures. There is no discussion of whether optimal λ differs by task, model, or context type, nor any guidance for practitioners on how to select λ in practice.

- **Model choices vary across experiments without justification.** The movie study uses Llama2-7b-Chat, BBQ uses T0pp and Mistral-7b-instruct, and the hate study does not specify the model used. While the BBQ choice is partially explained (Llama2-7b and GPT-J performed at random), the overall inconsistency confounds task performance with model choice.

- **No discussion of computational cost.** CoS requires two forward passes per token (one with context, one without), effectively doubling inference time. This is not acknowledged or measured.

- **The hate quantification λ choice (λ=-0.5) is not motivated.** The paper uses λ=-0.5 for classification but does not explain why this value was chosen or whether results are robust to this choice.

- **The LLM baseline for hate classification appears poorly implemented.** On the 2-class Black group, the LLM baseline achieves exactly 50% (random chance), suggesting a zero-shot classification prompt that may be suboptimally designed. The comparison would be stronger with a properly tuned classification baseline.

### Trivial

None beyond what appears to be minor grammatical issues in the IAT description (line 179: duplicated word "tasks tasks").

## Nice-to-Haves

- A comparison of CoS to inference-time alternatives such as activation steering (e.g., ITI, representation engineering) would strengthen the positioning.
- Reporting wall-clock time overhead for CoS relative to standard decoding.
- A systematic λ sensitivity sweep across all three applications.

## Removed Points

These points from the original reviews were removed or downgraded for the reasons given:

- **"No comparison to simply prepending the context with a stronger prompt"** — Removed because the paper explicitly compares λ=0 (plain prepending "I like {genre}, tell me about {movie}") and λ=-1 (no context) as baselines. λ=0 is exactly the "strong prompt" baseline the critic requests. The paper shows CoS at higher λ outperforms these.
- **"Inverse model section is 'essentially unsubstantiated' (no quantitative evaluation)"** — Weakened to Minor. The paper does provide quantitative evaluation: classification accuracy on implicit hate (Figure 5 right) and correlation with human ratings for λ inference (p=0.0295). The criticism is overstated; there IS evaluation, though it could be stronger.
- **"No numerical results for BBQ experiment"** — Figures are presented rather than tables. While tables would be preferable, the figures do convey results. Kept as part of the "no error bars" point.
- **"Bias metric not defined"** — Weakened. The BBQ benchmark has a standard bias metric (difference in accuracy across demographics); this is conventional enough that many papers do not re-derive it in the text. Still, a brief definition would help.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface insights that the paper itself does not articulate. The key observation — that log-likelihood differences between conditioned and unconditioned LLM probabilities define a simple, controllable influence function — remains the paper's core intellectual contribution.

## Suggestions

1. **Add at least one established baseline for each application.** For bias mitigation, compare to Self-Debias or instruction-based debiasing. This is the single most important addition — without it, the paper cannot claim CoS is effective relative to existing tools.
2. **Expand the user study** to at least 20–30 participants and report inter-rater agreement. If a larger study is infeasible, explicitly frame the current results as a pilot study.
3. **Provide a λ sensitivity sweep** (e.g., BBQ accuracy for λ∈{-2, -1, 0, 1, 2, 3} in steps of 0.5) with error bars, to give practitioners actionable guidance.
4. **Add error bars or confidence intervals** to the BBQ and IAT figures. Use bootstrapping over BBQ subjects if needed.
5. **Include a computational cost analysis** — report wall-clock time per generation with and without CoS.
6. **Fully specify the hate quantification model** and motivate the choice λ=-0.5, or show robustness across multiple λ values.

## Score and Decision

This paper presents a clean, elegant idea with genuine potential. The method is simple, interpretable, and demonstrated across diverse applications. However, the experimental validation is not yet at the level required to support the paper's central claims. The user study is underpowered, bias mitigation lacks comparisons to any existing approach, key results lack error bars, and the inverse model is only superficially validated. These gaps prevent the paper from being a convincing contribution as a full methods paper.

I rate this as a borderline-reject paper that could become acceptable after substantial experimental strengthening — particularly the addition of baselines and a larger user study.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>