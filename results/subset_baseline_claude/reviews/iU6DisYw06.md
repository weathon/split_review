## Summary

The paper proposes an evaluation framework called **auto-consistency** to assess whether LLM-generated token-level explanations for sentiment predictions are functionally coherent with the model's actual predictive behavior. Three metrics—Sufficiency, Comprehensiveness, and Counterfactuality—adapted from the extractive rationalization literature are applied to tokens highlighted by the LLMs themselves as influential. Experiments on IMDB and Steam datasets with five models (GPT-4o-mini, Gemma3:4B, Granite8B, DeepSeek-R1:1.5B/14B) reveal that GPT-4o-mini follows the expected pattern while DeepSeek models exhibit two distinct failure modes: contradiction (1.5B) and over-sensitivity (14B).

---

## Strengths

- **Well-motivated research question.** Evaluating whether LLM self-explanations are functionally aligned—not just textually plausible—is a legitimate and underexplored problem, and using behavioral interventions rather than internals is the only feasible strategy for proprietary models.
- **Comparative diversity.** Including both closed-source and open-source models from distinct families, plus an intra-family scale comparison (DeepSeek 1.5B vs. 14B), provides richer analysis than single-model studies.
- **Interpretable findings.** The observation that DeepSeek 1.5B contradicts itself across metrics (high instability under sufficiency and comprehensiveness simultaneously) while DeepSeek 14B over-relies on highlighted tokens is qualitatively interesting and reported with reasonable consistency across both datasets.
- **Reproducibility effort.** The paper commits to sharing code and prompts, and provides hardware/software details. The methodology is described with sufficient precision to be replicated.

---

## Weaknesses

### Fatal
None.

### Major

1. **No random-token baseline.** The central empirical claim—that the highlighted tokens play a functionally coherent role—cannot be evaluated without comparing to an equivalent intervention on randomly selected tokens (matched in count and/or position). Without this control, the observed metric values could arise from any meaningful token modification, not specifically from the model-highlighted tokens being functionally important. This omission makes it impossible to distinguish "auto-consistency" from ordinary sensitivity to text perturbation.

2. **Feeding unnatural/partial text back to an LLM is methodologically problematic.** The Sufficiency metric asks the same LLM to score a fragment of typically 1–3 disconnected tokens (e.g., "Pay to win. Buggy."). LLMs do not typically receive such truncated inputs, and their score on such inputs may reflect generic prior responses to partial text rather than a meaningful inference about sentiment. No analysis or sanity check is provided to validate that the LLM's behavior on these fragmentary inputs is interpretable.

3. **The expected "progression" is asserted, not justified.** The paper treats the trajectory Sufficiency→Comprehensiveness→Counterfactuality as the normative benchmark of good explanations, but this ordering is not formally derived. A model that produces wider score swings under counterfactual intervention could simply be more sensitive to antonym substitution for reasons unrelated to whether its explanations are faithful. The paper does not establish an absolute reference for what metric values constitute "good" auto-consistency.

### Minor

- The abstract references "GPT-4o" but experiments use "GPT-4o-mini"—a meaningfully smaller model. This inconsistency appears throughout.
- The use of a scalar review score [1, 10] instead of probabilities is motivated, but different models may have intrinsically different score calibrations (e.g., one model may cluster scores around 7 while another uses the full range), confounding cross-model comparisons of Δ*R* magnitudes.
- Counterfactual construction via WordNet antonyms + "not" prefix is coarse and can produce grammatically awkward phrases. It is unclear how often "not" prefixation was used vs. true antonyms, and whether this choice systematically biases any model.
- Statistical significance tests and confidence intervals are absent. Several differences in Table 1 that drive the paper's conclusions are small enough to warrant formal testing.

### Trivial

- Bold text in Table 1 marks values "explicitly discussed in Section 6" rather than best-performing entries—an unusual convention that is somewhat distracting.

---

## Nice-to-Haves

- An ablation comparing model-highlighted tokens to random tokens of equal count would transform the paper from descriptive to evidential.
- A human evaluation confirming that highlighted tokens are actually plausible explanations would strengthen the claim that the metrics are diagnosing explanation quality rather than model robustness.
- Extending to one non-sentiment task (e.g., NLI or factuality) would substantially increase the paper's scope.

---

## Novel Insights

The two-mode failure taxonomy for DeepSeek—contradictory fragility at 1.5B (high flip rates even under sufficiency) versus over-reliance at 14B (collapse under comprehensiveness and counterfactual) — is the most novel empirical observation. It suggests that scaling within a model family does not linearly improve explanation coherence and may introduce distinct qualitative failure modes. However, the absence of a random-token baseline prevents firm conclusions about whether these failures are genuinely attributable to explanation infidelity or to general sensitivity properties of the respective models.

---

## Suggestions

- **Add random token controls**: For each sentence, sample tokens uniformly at random (matching the count of highlighted tokens) and apply identical interventions. Report all four metrics for random vs. highlighted tokens side by side. This is the single change with the highest impact.
- **Report Δ*R* distributions, not just means**: A boxplot or histogram of per-sentence metric values would clarify whether the means are driven by a few extreme cases or reflect systematic behavior.
- **Clarify the "sentence" sampling procedure**: The IMDB dataset contains full reviews, not sentences; explain how 2,000 "sentences" were extracted from it and whether sentence length is controlled across models.

---

## Score and Decision

The research question is legitimate and the paper is clearly written, but the missing random baseline is a significant methodological gap that limits the conclusions. The scope is narrow (only sentiment analysis, only two datasets), and the central normative claim—that the observed metric trajectory reflects explanatory faithfulness—is asserted rather than formally grounded. As a standalone contribution for ICLR, this reads closer to a workshop paper or short communication. The empirical findings are not incorrect but are insufficiently controlled to support the strong auto-consistency framing.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>