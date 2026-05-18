Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper evaluates six LLMs (GPT, LLaMA, Gemma families) against eleven XAI properties across two datasets (Adult Income, California Housing) and five ML models per task, using conventional XAI methods (LIME, SHAP, DiCE, linear coefficients) as benchmarks. The core finding is that current LLMs consistently underperform traditional XAI methods on most evaluated properties, though they show moderate promise for generating accessible natural language explanations.

## Strengths

- **Systematic multi-property evaluation framework**: The paper designs and executes a quantitative, functionally-grounded evaluation across 11 XAI properties, 2 datasets, 5 ML models, and 6 LLMs from three developers. This is substantially broader in scope than prior studies (Susnjak 2023; Serafim et al. 2024; Mavrepis et al. 2024), which relied on subjective assessment or evaluated only single properties. The framework is clearly described in Section 3.1 and the results are tabulated in Tables 1–2.

- **Quantification of robustness and stability as distinct failure modes**: The paper defines and measures robustness (format error rate, instruction-following failures) and stability (variation across identical inputs) — properties specific to LLM behavior that were not systematically assessed in prior LLM-for-XAI work. These experiments (Section 4, Tables 1–2) reveal practical limitations (e.g., frequent formatting errors, high output volatility) that subjective evaluations would miss, and the gpt-4o-mini stability artifact (always returning all features) is discussed honestly in the text.

- **Representative LLM and model selection**: Six LLMs spanning three developers (OpenAI, Meta, Google) and two size tiers per family, plus five ML models of varying complexity per task. This design enables analysis of how scale and architecture affect explanation quality (Section 3.1, LLM Selection and Model Selection and Training).

- **Honest acknowledgment of key limitations**: The Discussion explicitly identifies resource constraints (1% test sets), dependence on prompt construction, and the lack of standardized XAI benchmarks as primary limitations (Section 5), which appropriately bounds the conclusions.

## Weaknesses

### Fatal
None.

### Major

- **Conflation of XAI properties with specific benchmark methods for several metrics**. The paper operationalizes selectivity as cosine similarity with DiCE counterfactuals, completeness as similarity with SHAP values, and degree of importance as similarity with LIME. These metrics measure how well LLMs replicate specific existing methods, not whether the explanations satisfy the abstract XAI property. For example, an LLM could produce perfectly selective explanations (focusing only on influential features) that look nothing like DiCE counterfactuals — and would be penalized. Conversely, an LLM could parrot SHAP values without understanding the model at all and score well on "completeness." The paper acknowledges *"there are no standard ground-truth benchmarks for XAI"* (Section 5), but the framing of results (e.g., *"LLMs lack completeness"*) presents the findings as property evaluations rather than method-comparison results. This is not fatal because: (a) several properties have cleaner metrics (accuracy uses ground-truth labels, contrastness checks actual prediction changes, stability uses identical-input variance, robustness counts errors, fidelity for linear models compares against actual coefficients — which ARE ground truth for linear model behavior), and (b) the core conclusion that LLMs are currently unreliable for XAI is supported by multiple independent measurements. However, the framing is misleading and would need to be corrected for publication.

- **No reporting of LLM temperature or sampling parameters**. The paper does not specify whether LLM queries used temperature=0 (deterministic) or higher values, nor whether any seed was set for sampling. This is a significant reproducibility gap — the output variability attributed to "instability" could partly stem from stochastic sampling rather than genuine explanation inconsistency. The paper also does not report multiple runs with different random seeds to establish variance.

### Minor

- **No confidence intervals or statistical significance tests**. All results are reported as point estimates (mean cosine similarity, mean RMSE, etc.) without confidence intervals, standard deviations, or significance tests. Given the small test sets (261/207 samples), it is impossible to assess whether differences between LLMs (e.g., 0.29 vs. 0.28 selectivity) are meaningful. This is standard practice for the field, so it is not a fatal omission, but it weakens the quantitative rigor.

- **Small test sets (1% of original data)** . Only 261 samples for Adult Income and 207 for California Housing are used. The paper acknowledges this as a resource constraint (Section 5), but the small sample size limits the statistical power of comparisons and the generalizability of conclusions.

- **Readability scores as a proxy for comprehensibility**. Flesch-Kincaid measures sentence length and syllable count, not whether an explanation is actually comprehensible in the XAI sense (i.e., whether a human can understand the model's decision from the explanation). An explanation could score well on readability while being misleading or incomplete. The paper frames this as a "proxy" (Section 4, Comprehensibility paragraph), which is appropriate, but the property label "comprehensibility" overclaims what the metric captures.

- **Single prompt per explanation type**. The paper uses only one prompt per explanation type. Given LLMs' well-known sensitivity to prompt phrasing, this means the experiments cannot distinguish between "LLMs cannot do this" and "this particular prompt did not elicit good performance." The paper acknowledges it *"does not focus on prompt engineering"* (Section 5), but this limits the generality of the conclusions about LLM *capability*.

- **gpt-4o-mini stability score artifact**. The paper notes that gpt-4o-mini's high stability score arises because it *"incorrectly marked every feature as most influential, ignoring the instructions"* (Section 4, Stability paragraph). The score is included in Table 1 without flagging, which could mislead a casual reader — though the text does provide the caveat.

- **"LLMs as translators" conclusion is not experimentally supported**. The paper concludes that *"LLMs may be better suited for roles as translators rather than explainers"* (Section 5), but the experiments did not test a translation scenario (i.e., taking conventional XAI outputs and rendering them in natural language). This is a reasonable conjecture but goes beyond the evidence presented.

### Trivial
None.

## Nice-to-Haves

- **Qualitative examples**: The paper would be substantially strengthened by showing representative LLM-generated explanations side-by-side with corresponding LIME/SHAP/DiCE outputs for a few test instances, so readers can assess the nature of the failures qualitatively rather than relying solely on opaque cosine similarity scores.
- **Prompt exploration**: A small prompt-engineering study (e.g., 2–3 prompt variants per explanation type) would help separate prompt quality from LLM capability limitations.
- **Error handling integration**: Robustness (formatting errors) could be integrated into the corresponding property scores (e.g., setting cosine similarity to 0 for malformed outputs) rather than treated as a separate property.

## Removed Points

These points were considered but removed with justification:

- *"The evaluation metrics do not measure the XAI properties they claim to"* — Retained as Major but rephrased. The original framing as "fatal/invalidates core conclusions" was an overstatement; the paper does measure several properties cleanly (accuracy, contrastness, stability, robustness, fidelity for linear models) and the core finding that LLMs are unreliable is supported by multiple independent measurements.
- *"No qualitative examples"* — Moved to Nice-to-Have. Valuable but not a weakness.
- *"Tables are dense and difficult to parse"* — Removed as a formatting/style nitpick.
- *"Novelty relative to prior work not clearly stated"* — Removed. Section 2.3 adequately establishes the gap.
- *"Missing rationale for pairing properties with methods"* — Removed. Section 3.1 provides four criteria for explanatory method selection.
- *"The paper never actually measures those properties"* — Removed as overstatement. Several properties have clean, valid metrics.

## Novel Insights

Beyond the paper's own contributions, the most notable observation from the reviews is the tension between the paper's framing (evaluating against abstract XAI properties) and its operationalization (comparing against specific methods). This tension is not unique to this paper — it reflects a deeper unresolved challenge in XAI evaluation: without ground-truth benchmarks, "evaluating" an explanation against a property often collapses into "measuring similarity to another method that is assumed to satisfy that property." The paper would benefit from explicitly framing itself as addressing the practical question "Can LLMs approximate the outputs of established XAI methods?" rather than the philosophical question "Can LLMs satisfy abstract XAI properties?" — which would make the evaluation design fully coherent.

## Suggestions

1. **Reframe the contribution**: Restate the paper's goal as assessing whether LLMs can reproduce or approximate the outputs of specific conventional XAI methods (LIME, SHAP, DiCE, linear coefficients), rather than evaluating LLMs against abstract, ungrounded XAI properties. This aligns the evaluation design with the claims and makes the contribution both precise and defensible.

2. **Report temperature/sampling parameters** for all LLM queries and conduct multiple runs (with different seeds) to establish variance estimates.

3. **Add simple statistical comparisons** — at minimum, report standard deviations alongside means and consider effect sizes for key comparisons.

4. **Flag the gpt-4o-mini stability artifact** in Table 1 with an asterisk or footnote so the high score is not misinterpreted.

5. **Tone down the "translator" conclusion** or, better, add a small experiment where LLMs are given conventional method outputs and asked to paraphrase them in natural language to test that capability directly.

## Score and Decision

This paper makes a genuine contribution — it is the first systematic, multi-property quantitative evaluation of LLMs for XAI, and its core finding (current LLMs are unreliable explainers) is supported by multiple independent measurements (accuracy, contrastness, stability, robustness, fidelity to linear coefficients). The robustness and stability analyses are genuinely novel and practically important. However, the paper has a significant framing issue: it conflates "measuring similarity to specific methods" with "measuring abstract XAI properties" for several key metrics (selectivity, completeness, degree of importance). While not fatal (the paper acknowledges the lack of ground-truth benchmarks, and several properties are measured cleanly), this conflation means the paper's headline claims overstate what the evidence supports. Combined with the absence of LLM sampling parameter reporting, small test sets, and lack of statistical testing, the paper needs substantial revision before it is ready for publication. I recommend rejection with strong encouragement to resubmit a version that either reframes its contribution transparently or directly measures properties using synthetic ground-truth models.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>