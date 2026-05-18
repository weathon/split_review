Now I have a thorough understanding of both the paper and the reviews. Let me produce the final consolidated review.

---

## Summary

This paper proposes GoLLIE, a Code-LLaMA model fine-tuned to follow detailed annotation guidelines (label definitions and representative annotation examples) for zero-shot information extraction across NER, event extraction, and event argument extraction. The key idea is to represent tasks as Python class definitions with guidelines in docstrings/comments, and use training regularization (class shuffling, dropout, paraphrasing, class name masking) to force the model to attend to guidelines rather than memorizing label patterns. The results show large zero-shot gains: GoLLIE 7B raises average zero-shot F1 from 42.3 (baseline without guidelines) to 55.3, with the 34B version reaching 60.0, substantially outperforming prior zero-shot methods.

## Strengths

- **Large and robust zero-shot improvements across diverse benchmarks**: GoLLIE 7B improves average zero-shot F1 from 42.3 (baseline without guidelines) to 55.3, a 13-point absolute gain, with further scaling to 60.0 F1 for the 34B model (Table 2). These gains are consistent across most datasets and domains. The baseline and GoLLIE share the same backbone (Code-LLaMA), training data, and input format — differing only in whether guidelines are provided — making the comparison clean within the paper.

- **Ablation study cleanly isolates the role of different guideline components**: The ablation (Table 3) shows that removing representative candidates causes the largest drop (55.3→49.9, p=2.2e-10), while removing paraphrases/definitions yields smaller effects (54.8, not significant). Removing all regularization drops to 42.3. This provides causal evidence that the specific content of guidelines (especially the examples) drives the improvement, not merely format changes.

- **Error analysis demonstrates that GoLLIE genuinely follows guidelines, not just label names**: For polysemous labels like Media, Vulnerability Patch, Trailer, and Task, GoLLIE achieves 60–76 F1 while the baseline is at 0–28 (Table 4). The MultiNERD Time case is particularly revealing: GoLLIE labels years as Time (following the guideline definition) even though the dataset annotations do not — showing the model follows the guidelines rather than memorizing dataset patterns.

- **Scalable improvement with model size in zero-shot**: GoLLIE 34B achieves the highest average zero-shot F1 (60.0) and shows a smaller performance gap between seen and unseen labels as parameters increase (Figure 1). This demonstrates that guideline-following capability benefits from LLM scaling laws.

- **Supervised performance is not substantially degraded**: Comparing GoLLIE to the within-paper baseline, the average supervised F1 is nearly identical (73.0 vs 73.3, Table 1), confirming that zero-shot-oriented regularization does not harm in-domain capability.

## Weaknesses

### Fatal
None.

### Major

- **"Zero-shot" framing is weakened by guideline/candidate construction from target datasets**: For evaluation datasets without publicly available official guidelines (the paper names no specific list, but the affected set plausibly includes CrossNER, FabNER, HarveyNER, MIT Movie, MIT Restaurants, MultiNERD, WikiEvents), human experts created guidelines "based on the annotations from the development split" and sampled candidates from the train split (Section 4.1, line 137). This means the guidelines and examples provided at test time are informed by the *same dataset* being evaluated — specifically its annotation patterns. This is not true zero-shot, because the test input contains information derived from the target dataset's own annotations. The paper does not acknowledge this limitation or discuss its implications. However, this does **not** invalidate the core claim that guidelines improve results: (a) the within-paper baseline comparison is still controlled (same setup, just without guidelines), (b) the MultiNERD Time example shows GoLLIE following the guideline *in opposition to* the dataset's annotation patterns, suggesting the guidelines are not simply mirroring the data, and (c) the model is still evaluated on test splits it has never seen during training. The method is effective, but the "zero-shot" framing needs qualification.

### Minor

- **Ablation shows candidates drive the majority of the improvement, not abstract definitions, but the paper's framing over-emphasizes "guidelines"**: Removing candidates drops F1 from 55.3 to 49.9 (the largest single-component effect), while removing paraphrases (the closest proxy for "definitions" alone) drops only to 54.8 (not significant). Candidates account for roughly 7.6 of the 13-point gain versus baseline (42.3). The paper acknowledges this in the ablation discussion but the title, abstract, and broader framing emphasize "annotation guidelines" generically. The contribution is more precisely about providing *representative annotation examples* formatted as part of guidelines, with definitions playing a supporting role. The paper would benefit from reframing this honestly.

- **Comparison with prior work confounds backbone, training data, and the guideline factor**: GoLLIE (Code-LLaMA) is compared against Instruct-UIE (Flan-T5) and PromptNER (GPT-3.5/T5). The within-paper baseline (Code-LLaMA without guidelines) provides a controlled comparison, but the claim of "surpassing by a large margin the current zero-shot SoTA methods" conflates backbone choice, training data size/quality, and the use of guidelines. A controlled experiment using the same backbone with/without guidelines (beyond the paper's own baseline) would strengthen the attribution.

- **Code-specific representation raises transferability questions**: Using Code-LLaMA with Python docstrings for guidelines is a pragmatic choice, but the method's reliance on a code-pretrained backbone and code-formatted input means it is unclear whether the same benefits would transfer to non-code-based LLMs or natural-language-only guideline formats. The paper does not probe this boundary.

### Trivial

- The paper mentions "no significant contribution" from class name masking (line 299), which is consistent with the ablation. The critic's claim that this "tension is not discussed" is incorrect — the paper explicitly acknowledges it. No issue here.

- On WNUT and NCBIDisease, GoLLIE underperforms the baseline by 1–2 F1 points in the supervised setting (Table 1). The paper's "no degradation" claim is about *average* performance, which holds (73.0 vs 73.3), but this is not a significant concern for a zero-shot-oriented paper.

## Nice-to-Haves

- A clear table listing each evaluation dataset, whether official guidelines exist, and exactly how guidelines and candidates were constructed (which splits used, whether human experts or pre-existing). This would resolve ambiguity and strengthen reproducibility.

- An explicit acknowledgment and discussion of the experimental design limitation regarding guideline construction from target dev splits, and a justification for why this does or does not violate the zero-shot framing.

- An analysis that separates the contribution of definitions alone vs. candidates alone vs. both, beyond the current ablation's "w/o Paraphrases" and "w/o Candidates" conditions.

- A discussion of the human effort required to create guidelines for new tasks, since the method requires this for each new domain.

## Removed Points

- **MultiNERD "Time" example as evidence of data leakage**: The critic claimed this example "further illustrates the leakage problem" because GoLLIE is "rewarded for matching the derived guidelines." In fact, the paper shows the opposite: GoLLIE labels years as Time (following the guideline definition) while the dataset *does not* annotate years, causing GoLLIE to score only 3.5 F1. If the guidelines were leakily derived from the dataset's annotations, they would have matched the dataset's convention. This example actually *counters* the leakage argument and supports the paper's claim that GoLLIE genuinely follows abstract guidelines. **Removed** (factually wrong interpretation).

- **"w/o masking" tension is undiscussed**: The critic claimed the paper does not discuss the non-significance of class name masking. The paper explicitly states (line 299): "class name masking seem to have no significant contribution to the final result." **Removed** (factually incorrect — the paper does discuss it).

- **Criticism about missing appendix/proofs/references**: These are parser artifacts. **Removed** per instructions.

- **Various formatting/style nitpicks**: Not present in the original submission. **Removed** per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's core findings, with the main tension being whether the data leakage concern is fatal (it is not — it is a significant framing issue but the method's effectiveness is still supported by controlled comparisons and the MultiNERD Time counterexample). The ablation's revelation that candidates dominate the effect is the most important secondary finding from both the paper's own analysis and the reviews.

## Suggestions

1. **Acknowledge and qualify the guideline construction limitation**: Add a paragraph discussing which zero-shot evaluation datasets lack official guidelines and how this affects the "zero-shot" claim. Either exclude datasets without independent guidelines from the primary zero-shot results and relegate them to an appendix, or re-run with guidelines written without access to the target data.

2. **Reframe the contribution more precisely**: The title and abstract should reflect that the main empirical driver is *representative annotation examples* rather than abstract guideline definitions, with definitions playing a complementary role. Something like "Annotation Guidelines (especially representative examples) improve Zero-Shot IE."

3. **Add a controlled backbone comparison**: Even a single ablation re-evaluating Instruct-UIE's approach on Code-LLaMA (with/without guidelines) would cleanly separate the backbone effect from the guideline effect.

4. **Report per-dataset guideline construction sources**: Add a supplementary table showing for each evaluation dataset whether official guidelines exist, whether candidates were from official guidelines or sampled from train split, etc.

5. **Add definitions-only vs. candidates-only vs. both analysis**: This would directly address whether the contribution is primarily about examples or about abstract definitions.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>