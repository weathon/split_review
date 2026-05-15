Here is my consolidated final review.

---

## Summary

This paper applies the representativeness heuristic framework from cognitive science (Bordalo et al., 2016; Kahneman & Tversky, 1972) to study political stereotyping in LLMs. It formalizes "kernel-of-truth" (γ), "representativeness" (ε), and "exaggerative degree" (κ) parameters to quantify how LLM responses about political party positions deviate from empirical survey data. Across six LLMs and two datasets (ANES, MFQ), the paper finds that LLMs systematically exaggerate party positions relative to both the empirical self-placement of party members and human predictions of party positions. The paper also tests three prompt-based mitigation strategies (AWARENESS, FEEDBACK, REASONING) that reduce this exaggeration to varying degrees.

## Strengths

- **Formal cognitive-science framework for quantifying exaggeration**. The paper introduces mathematically precise measures — representativeness (likelihood ratio, Eq. 1), kernel-of-truth (γ, Eq. 4), and exaggerative degree (κ, Eq. 3) — to diagnose LLM stereotyping. This moves beyond merely noting that LLMs have political leanings and enables the attribution of specific biases to representativeness heuristics. The framework is operationalized in Tables 1–3, which report estimated γ, ε, and κ across models and datasets.

- **Consistent empirical demonstration that LLMs exaggerate political positions relative to humans**. Using two independent survey datasets (ANES, MFQ) and multiple LLMs, the paper shows that Believed Means for Republicans are inflated and for Democrats deflated beyond both the Empirical Means and human-predicted means. The most direct evidence is Figure 4, where every model's (x,y) point lies above the y=x line, meaning the gap between parties in the model's beliefs is larger than the gap in the empirical data. This pattern holds across models and datasets with remarkably few exceptions.

- **Novel prompt-based mitigation strategies grounded in cognitive science that reduce exaggerative bias**. The paper tests three mitigation strategies (AWARENESS, FEEDBACK, REASONING) derived from human self-correction literature. Table 3 shows that the baseline prompt yields the highest κ (worst exaggeration) across almost all model–dataset combinations, while the best mitigation method reduces κ substantially, demonstrating that LLM stereotyping can be partially controlled with targeted prompts.

- **Multi-model and multi-dataset evaluation increases robustness**. Experiments span six LLMs (GPT‑4, GPT‑3.5, Gemini, Llama2, Llama3, Qwen2.5) and two conceptually distinct datasets (ANES: issue positions; MFQ: moral foundations), strengthening the generality of the findings over single-model or single-domain studies.

## Weaknesses

### Fatal

None.

### Major

None. The core claims are supported by the evidence, and no fundamental methodological error invalidates the analysis.

### Minor

- **Parameter estimation procedure is underspecified.** The paper reports numerical values for γ (Table 1), ε (Table 2), and κ (Table 3) with standard deviations, but never explicitly describes how these parameters are estimated from the data. Equations 4, 5, 6, and 3 each have one free parameter given the empirical and believed distributions, so the parameters are algebraically determined per topic — but the paper should state this clearly, explain that standard deviations come from aggregation across topics, and report the number of topics used for each estimate. Without this, the reader cannot fully interpret the reported values or assess whether the standard deviations capture meaningful variation.

- **No statistical testing or confidence intervals for headline comparisons.** The paper's central claim — "LLMs tend to exaggerate these positions more than human respondents do" (Figure 2, Figure 4) — is supported by visual differences in means, but no confidence intervals, significance tests, or effect sizes are reported. Given that each model produces multiple responses and human survey data has known sampling variance, bootstrapped confidence intervals or permutation tests would strengthen the evidence that the observed differences are reliable rather than noise.

- **Mitigation prompts may confound instruction-following with genuine self-correction.** The AWARENESS prompt explicitly describes the representativeness heuristic ("The representativeness heuristic involves overestimating the probability of types more prevalent in the target group…"), and the FEEDBACK prompt tells the model its prior response may be biased. These interventions may be closer to providing the model with the answer than testing whether the model self-corrects. A control condition using a neutral prompt like "Please answer accurately" without mentioning heuristics is needed to distinguish heuristics-specific debiasing from generic instruction-following.

- **The right-tail analysis uses N=2 without justification or sensitivity analysis.** The paper sets N=2 for the right-tail representativeness analysis (Eqs. 5–6) without explaining why this value was chosen or showing results for N=1, 3, 4. Since the representativeness measures ε depend on this choice, a sensitivity analysis is needed to assess robustness.

### Trivial

- The paper plots only means in Figures 2 and 3, but the representativeness framework operates on the full probability distribution (the likelihood ratio). Showing full distribution plots (e.g., stacked bar charts of Likert-scale responses) for a few example topics would make the mechanism more visible and reveal whether exaggeration is driven by tail probabilities or uniform shifts.

## Nice-to-Haves

- A goodness-of-fit analysis for the formal model (e.g., residuals, R², or scatterplots of predicted vs. observed believed means) would verify that the linear relationships in Eqs. 4–6 are empirically appropriate.
- An analysis disentangling data bias from heuristic bias — i.e., controlling for the actual distribution of party-related text in training data — would help distinguish whether models are "exhibiting a heuristic" or simply reproducing training distribution extremes.
- A table or heatmap showing which scale points are the exemplars (a*) for each topic and model would ground the analysis concretely.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Critical Issue 1 (Structural mismatch between empirical and believed quantities)** — REMOVED. This criticism is factually wrong and misinterprets the paper's framework. The kernel-of-truth hypothesis (Bordalo et al., 2016) is specifically about how beliefs about groups relate to actual group characteristics. 𝔼(a|X⁺) (self-placement of party members) is the appropriate empirical measure of a group's actual position; 𝔼^B(a|X⁺) (LLM's belief about the party's position) is the belief term. These are intentionally different quantities — the model in Eq. 4 explains how beliefs are formed from empirical reality, with γ capturing the exaggeration. The paper also includes Human Pred Mean (humans answering the belief question) as an additional reference point in Figure 2, further validating the comparison. The critic's claim that "these are not comparable quantities" fundamentally misunderstands the kernel-of-truth framework, which is predicated on the distinction between empirical reality and beliefs about that reality.

2. **Equation 3 dimensional inconsistency** — REMOVED. The claim that Eq. 3 is "dimensionally inconsistent" is incorrect. Probabilities are dimensionless numbers in [0,1]; a ratio of probabilities (left side) and a scalar times a probability (right side) are both dimensionless. There is no dimensional inconsistency.

3. **Related Work does not engage with Blodgett et al. (2021)** — REMOVED. The paper explicitly cites Blodgett et al. (2021) at line 202, acknowledging the critique about the lack of precise definitions of stereotypes, and explains how the current work addresses this gap by drawing on cognitive science theory.

4. **Limitations omit self-placement vs. party-placement mismatch** — REMOVED. As noted above, this is not a genuine mismatch; the paper's framework is correctly specified. Omitting a non-issue from limitations is not a flaw.

5. **Reference class X⁻ not justified** — REMOVED. The paper clearly states X⁺=Republicans and X⁻=Democrats throughout (Section 3). For a two-party political analysis, this is the natural contrast, and the choice is transparent.

6. **Data mapping from Likert to probability space unclear** — WEAKENED to trivial. The paper states that attributes correspond to Likert scale points A={1,...,7} and defines p_{a,X⁺} as the conditional probability of a group member selecting attribute a. This is sufficiently clear. The categorical vs. aggregated means concern is addressed by the fact that the paper uses both the full distribution (for likelihood ratios) and the mean (for the linear equations).

7. **Over-interpretation of psychological mechanism** — REMOVED. The paper is explicit (lines 14, 18, 27, Introduction) that it is applying the formal mathematical framework of representativeness heuristics to analyze LLM outputs. It does not claim LLMs have cognitive processes analogous to humans; it uses the framework as an analytical lens, which is a standard scientific practice.

## Novel Insights

The most interesting finding to emerge from the reviews is the differential effectiveness of mitigation strategies across datasets: REASONING works best for ANES (issue positions) while FEEDBACK works best for MFQ (moral foundations). This suggests that the nature of the task (factual positions vs. moral intuitions) may determine which debiasing approach is most effective, pointing toward a need for task-adaptive mitigation strategies rather than one-size-fits-all prompt engineering. Additionally, the Llama3-8b reversal (showing opposite trends) is a genuinely useful observation that complicates the narrative of universal LLM exaggeration and warrants systematic investigation as a function of model size, architecture, or training data composition.

## Suggestions

1. **Explicitly describe the estimation procedure for γ, ε, and κ.** State that each parameter is solved algebraically per topic from the corresponding equation, then averaged across topics (with standard deviations across topics). Report the number of topics used.

2. **Add bootstrapped confidence intervals or permutation tests** for the mean differences in Figures 2 and 4 to support the central claim with statistical evidence.

3. **Add a neutral control prompt** ("Please answer accurately") to the mitigation analysis to distinguish instruction-following from heuristics-specific debiasing.

4. **Report sensitivity to N** in the right-tail analysis (Eqs. 5–6) by showing results for N=1,2,3,4.

5. **Show full distribution plots** (bar charts of probability over the 7-point scale) for a representative selection of topics and models.

## Score and Decision

The paper makes a genuine contribution by introducing a principled cognitive-science framework for quantifying LLM stereotyping, with clear formalization and consistent empirical evidence across models. The core claims are well supported (Figure 4 in particular is compelling). The identified weaknesses — underspecified estimation procedure, lack of statistical testing, insufficient control in mitigation experiments, and sensitivity analysis for N — are all addressable in revision. There are no fatal flaws.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>