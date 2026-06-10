## Summary

This paper introduces the first formal, information-theoretic definition of instruction-data separation for LLMs (Definition 2), operationalized as the KL divergence between output distributions when a probe string appears in the instruction argument versus the data argument. It operationalizes this via an empirical proxy using "surprise witnesses" (Definition 3-4) that requires only sampled outputs, constructs the SEP dataset (9,160 tuples across 30 tasks), and evaluates 9 models across 4 conditions (vanilla, prompt engineering, prompt optimization, fine-tuning). The key empirical finding is that no existing model achieves high separation, standard mitigation strategies either fail or collapse utility, and scaling alone does not help — suggesting architectural changes may be needed.

## Strengths

- **Novel formal definition grounded in information theory (Definition 2, Eq. 1, lines 83–96):** Separation is defined as the KL divergence between output distributions when a probe appears in the instruction vs. data argument. This is the first formal definition of this property for LLMs — prior work studied the phenomenon only qualitatively or via task-specific benchmarks. The paper explicitly identifies three sources of non-computability (lines 126–138) and addresses them.

- **Practical empirical proxy using surprise witnesses (Definitions 3–4, lines 164–181):** The empirical separation score uses witness words that reliably appear when the probe is executed but not when processed, requiring only sampled outputs. This enables evaluating black-box API models alongside open-weight models without access to token probabilities or internal states. The logical chain connecting witness presence to bounded KL divergence is explicitly argued (lines 150–158).

- **Systematic evidence that post-hoc mitigation cannot jointly achieve high separation and high utility (Tables 1–2, Figure 1, lines 524–551):** Across 9 models and 3 mitigation strategies, no combination achieves both high separation and high utility. Fine-tuning boosts average separation from 37.5% to 81.8% but collapses utility from 67.8% to 19.2%. The scatter plot (Figure 1) and its negative trend line visually substantiate the tradeoff, supporting the paper's central claim that none of the tested strategies are satisfactory.

- **Well-constructed, diverse evaluation dataset with controlled experimental design (lines 237–258):** SEP contains 9,160 tuples across 30 manually authored tasks with 100 manually written probe-witness pairs. The hybrid human/GPT-4 generation process avoids repetition issues of fully automated pipelines. Probe placement is randomized to both beginning and end of instruction/data (four combinations, line 258), controlling for ordering effects.

- **Non-obvious finding that larger/better models do not separate better (lines 375–384):** GPT-4 (20.8%) underperforms GPT-3.5 (56.6%), Llama-3 8B (30.8%) underperforms Llama-2 7B (44.3%), and Gemma-7B (56.9%) underperforms Gemma-2B (73.2%). This explicitly tested within-model-family result challenges the natural assumption that scaling solves the problem.

## Weaknesses

### Fatal
None.

### Major

- **GPT-4 contamination in the evaluation dataset (lines 244–246, 466–468).** GPT-4 was used to generate the 300 subtasks and the task prompts/data prompts in SEP, and is then evaluated on this same dataset. The paper's own prompt-engineering result shows GPT-4 achieving 95.3% separation — the only clean counterexample to the separation-utility tradeoff — but also acknowledges (line 466) that "it cannot be ruled out that GPT-4 has an unfair advantage." This concern is not merely cosmetic: if GPT-4's high separation reflects recognition of its own generation patterns rather than genuine instruction-data separation, the comparison against other models is compromised. The paper discusses this caveat but does not experimentally address it (e.g., by evaluating on an independently generated held-out set). Given that GPT-4's result is the main outlier that weakens the paper's otherwise strong narrative, this gap deserves more than a single caveat sentence.

### Minor

- **Gap between the formal two-argument model and the system/user prompt proxy (lines 356–361, 404–407).** Definition 1 assumes a language model with explicit instruction and data arguments — an architecture no current LLM possesses. The experiments proxy this via the system/user prompt convention, and for Starling/Gemma the authors "artificially introduce such a distinction" by prepending `"System prompt:"` / `"User prompt:"`. The paper acknowledges this (lines 404–407), but the consequence is that the experiments primarily evaluate how well models respond to a specific *prompt formatting convention*, not the formal construct of instruction-data separation defined in Definition 2. The disconnect between the formal framing and the experimental operationalization is larger than the paper fully grapples with.

- **Prompt engineering templates not shown (line 447).** The paper reports that prompt engineering helps some models and hurts others (e.g., Gemma-2B's utility drops from 36.7% to 15.3%), but the actual templates are not provided — only a reference to Hines et al. (2024). Without the templates, readers cannot assess whether these are reasonable formulations or whether different templates would yield different outcomes. Given the high variance across models, this is a non-trivial reproducibility gap.

- **Prompt optimization missing critical details (lines 484–496).** The optimization procedure is described at a high level ("coordinate descent approach over token positions," "gradient-strength based selection") with no specified loss function, validation criterion, number of optimization steps, or hyperparameters. The sentence describing the method is truncated by the parser, indicating an incomplete section. This makes the prompt optimization results (which show the weakest effect of all mitigation strategies) difficult to interpret or reproduce.

### Trivial

- Fine-tuning hyperparameters (LoRA rank, learning rate, number of epochs) are absent from the fine-tuning section (lines 512–531), though the paper fields a complete experimental setup that could be easily documented in a final version.

## Nice-to-Haves

- A qualitative analysis of failure modes in fine-tuned models would clarify whether utility loss reflects genuine task degradation, refusal behavior, or empty outputs. This would help future research understand whether the utility-separation tradeoff is fundamental or an artifact of the optimization setup.
- Human validation of a sample of the automatically generated dataset tuples would strengthen confidence in data quality, though this is not standard practice for datasets of this size.

## Removed Points

These points were flagged by reviewers but are removed as invalid, misreadings, or outside scope:

1. **"The empirical proxy's relationship to KL divergence is unidirectional."** — The paper explicitly only claims that *low* esep implies *low* sep_p (lines 188–190: "a small empirical separation implies... a low actual separation score"). It never claims the converse. The reviewer's concern about high esep not implying high sep_p is about a claim the paper does not make. This is a misreading.

2. **"No human validation of automatic dataset generation"** — The paper states tasks were "created manually" (line 243) and the hybrid process was designed to avoid the problems of fully automated generation (line 248). The request to validate all 9,160 tuples is disproportionate for a dataset of this scale.

3. **"No discussion of whether the problem is inherent or a training artifact"** — The paper's entire experimental design tests this question (scaling experiments within model families, comparing different mitigation strategies). The core claim (that the problem is real and current mitigations fail) does not require resolving this causality question, which the paper explicitly frames as future work.

4. **"The 100 manually written probe-witness pairs should be publicly listed"** — The paper states the dataset and code will be released (line 233). Speculating about future benchmark contamination is premature.

5. **Various formatting, style, and missing-appendix nitpicks** — Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The key novelty is already in the paper: the formal separation definition and the finding that LLMs fail it and current mitigations cannot simultaneously achieve separation and utility.

## Suggestions

1. **Address the GPT-4 confound experimentally.** Regenerate the task/data prompts using a different model (e.g., Llama-3-70B) and re-evaluate GPT-4 on this held-out set. This would either confirm or refute whether GPT-4's anomalous prompt-engineering result is an artifact, and would substantially strengthen the paper's evidence base.

2. **Release prompt engineering templates and prompt optimization details.** Include the actual templates used and the full optimization specification (loss function, steps, validation criterion) in a supplement. Without these, the prompt engineering and optimization experiments cannot be reproduced or properly assessed.

3. **Recalibrate the framing around the formal definition vs. empirical proxy.** The paper currently oscillates between presenting the formal two-argument model as an aspirational definition and using system/user prompt formatting as a stand-in. A clearer discussion of which conclusions follow from the formal definition and which follow only from the proxy would improve rigor.

4. **Document fine-tuning hyperparameters** (LoRA rank, learning rate, epochs) and show representative outputs from fine-tuned models to clarify what "utility loss" looks like in practice.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>