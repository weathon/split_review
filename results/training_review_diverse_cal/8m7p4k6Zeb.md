Now I have thoroughly read and verified all claims against the paper. Let me produce the final consolidated review.

## Final Consolidated Review

## Summary

This paper proposes finetuning LLMs on a synthetic dataset of numerical key-value dictionary retrieval tasks to improve their long-context information retrieval and reasoning capabilities. Experiments on GPT-3.5 Turbo and Mistral 7B show that this approach mitigates the "lost-in-the-middle" phenomenon on multi-document QA (MDQA), improves performance on FLenQA, and preserves general capabilities on standard benchmarks. The paper additionally compares against finetuning on factual long-context datasets (MultidocQA, IN2, Needle-in-a-haystack) and finds that synthetic-data finetuning causes substantially less degradation on knowledge-based benchmarks like TriviaQA and NQ-Open.

## Strengths

- **Transfer from synthetic retrieval to real tasks is empirically demonstrated.** Finetuning on key-value retrieval flattens the U-shaped "lost-in-the-middle" curve for GPT-3.5 Turbo on MDQA (Figure 2a) and mitigates primacy bias for Mistral 7B (Figure 2b), showing that a numerical dictionary task can generalize to natural-language multi-document QA. This is the paper's core empirical contribution and is well-supported.

- **General capabilities remain largely intact.** Table 1 shows that finetuning on the synthetic data causes minimal changes across MMLU, HellaSwag, GSM8K, TriviaQA, and NQ-Open (largest change: −0.68% on GSM8K for GPT-3.5 Turbo w/template, +2.73% for GPT-3.5 Turbo w/o template). This contrasts favorably with factual-data baselines, making it a practically meaningful property.

- **Answer templates provide a clear advantage.** The paper demonstrates (Figure 3, Finding 4) that providing an answer template during synthetic finetuning consistently improves downstream MDQA and FLenQA performance over the no-template variant. The token-level loss visualization in the paper supports the mechanism that templates let the model focus on retrieval rather than answer formatting. This is a clean ablation.

- **Synthetic data preserves knowledge benchmarks better than factual-data baselines.** Table 2 shows that while MultidocQA, IN2, and Needle-in-a-haystack finetuning cause 2–7% drops on TriviaQA and NQ-Open, the synthetic data causes essentially no drop. This differential is a genuine empirical finding, regardless of the causal interpretation attached to it.

- **Honest limitation section.** The paper notes that the proposed approach does not improve MDQA performance when distractors are relevant (i.e., retrieved by a retriever rather than random), which is a meaningful and honest boundary condition.

## Weaknesses

### Major

1. **Finding 2 ("synthetic > MDQA data") rests on a weakened comparison.** The paper finetunes on MDQA data by first prompting GPT-3.5 Turbo to rewrite short ground-truth answers into full sentences, then uses those sentences as training targets. This introduces confounds — the rewrites may contain artifacts, irrelevant phrasing, or subtle semantic shifts. Additionally, the MDQA-finetuned Mistral 7B actually performs *worse* at position 1 than the original model (Figure 2b), which strongly suggests the MDQA finetuning setup was suboptimal (e.g., insufficient hyperparameter search, format mismatch, or too few training steps). The paper reports "roughly the same number of training tokens" but provides no exact token counts, no learning rates, and no indication of whether hyperparameters were tuned for the MDQA baseline. Without a fairer comparison (original short-answer format, hyperparameter search, matched training conditions), the claim that synthetic data surpasses target-domain finetuning is not adequately supported. This does not invalidate the paper's core finding (transfer works), but it does mean Finding 2 should be weakened or the baseline should be fixed.

2. **Finding 6 overclaims a causal link to hallucination.** The paper shows that factual-data baselines cause accuracy drops on TriviaQA and NQ-Open while synthetic data does not, then attributes this to the synthetic data "not encouraging hallucinations" (citing Gekhman et al. 2024). However, accuracy degradation on knowledge-intensive benchmarks is not a direct measure of hallucination — it could equally reflect catastrophic forgetting, format interference, or reduced calibration. The paper provides no analysis of model outputs (e.g., checking whether errors are fabricated answers vs. refusals vs. plausible wrong answers), no measurement using a hallucination-specific benchmark, and no evidence that the observed drops are caused by the factual *content* per se rather than by distributional shift or training dynamics. The causal framing ("does not encourage hallucinations") is stronger than the evidence supports. The underlying observation (accuracy preservation) is valuable; the causal attribution to hallucination is not.

### Minor

3. **Reproducibility details are incomplete for baseline comparisons.** The paper says baselines use "roughly the same number of training tokens" but does not report exact token counts, number of training steps, learning rates, batch sizes, or whether any hyperparameter search was conducted for any of the baselines (MDQA, MultidocQA, IN2, Needle-in-a-haystack). For open-source models, these details are necessary to assess the fairness of comparisons. The appendix reference (`\ref{sec:mistral_ft}`) may contain some of these details, but they are not present in the main paper.

4. **Stage 5 (longer-context) experiment is reported too briefly.** The evaluation on Mistral-7B-Instruct-v0.2 with 120 documents (~24K tokens) is described in two sentences plus one figure. No hyperparameters, training details, or comparisons to baselines at this scale are provided. While the result appears positive, its robustness cannot be assessed.

5. **No error bars or confidence intervals.** For the main MDQA results (200 samples per position) and FLenQA (2000 total samples), no measure of variance is reported. This makes it difficult to assess whether observed differences between conditions are reliable, especially for fine-grained comparisons (e.g., template vs. no-template gaps in Figure 3).

### Trivial

6. **Small negative changes exist on general benchmarks.** The paper claims finetuning "does not hurt" general capabilities (Finding 5), but Table 1 shows GSM8K drops of 0.31% (Mistral w/template) and 0.68% (GPT-3.5 Turbo w/template). These are very small and the paper still characterizes them reasonably as "no significant degradation," but the absolute framing ("does not hurt") could be slightly more precise.

## Nice-to-Haves

- **Vary the synthetic task format** to probe the mechanism: e.g., use prose paragraphs instead of dictionaries while keeping the retrieval demand identical. This would help determine whether the transfer is specific to "numbered-list-item retrieval" or reflects a more general learned skill.
- **Directly measure hallucination rates** (e.g., FACTOR, TruthfulQA, or manual annotation of model outputs) if the authors wish to maintain the hallucination claim.
- **Include comparisons to non-finetuning baselines** such as prompt reordering (Tang et al. 2023) or RAG to contextualize the practical value of the finetuning approach.

## Removed Points

These points were flagged but removed from the main review with justification:

- *Missing comparison to RAG/prompt reordering* — Scope creep. The paper is about finetuning; comparing to non-finetuning approaches is a nice-to-have, not a weakness.
- *"Synthetic task is structurally simpler" as an alternative explanation for general benchmark preservation* — This is a reasonable observation but does not invalidate the paper; if anything, a simpler task with less capacity consumption makes the transfer finding MORE interesting, not less. The paper also uses a harder multi-subkey variant precisely to address the ceiling effect concern.
- *"The paper should also cover Y/domain Z"* — No specific such demand was made; flagged for completeness.
- *Strength Finder's claim that "synthetic data inherently avoids hallucination from factual content"* — This restates the overclaimed Finding 6 as a strength. The underlying empirical observation (accuracy preservation) is strong; the causal conclusion is not. This strength was rephrased and moved to the Strengths section as the appropriate empirical claim.

## Novel Insights

The most interesting observation in the reviews is the structural simplicity hypothesis: the synthetic key-value task may succeed because it isolates a single cognitive primitive (find X in a labeled list) that is a component of more complex long-context QA tasks, while factual-data baselines may simultaneously teach both retrieval AND new factual associations, causing interference. This framing suggests the paper's contribution is not just "synthetic > real data" but "isolating the retrieval skill from factual content yields more targeted transfer." The reviews do not reveal any genuinely novel insight beyond what the paper's own results and limitations already suggest.

## Suggestions

1. **Fix the MDQA baseline.** Train on original short-answer format, perform hyperparameter search, report exact token counts and training steps. This will either substantiate or qualify Finding 2.
2. **Reframe Finding 6** from a hallucination claim to an observation about accuracy preservation: "Synthetic data avoids accuracy degradation on knowledge-intensive benchmarks that occurs with factual-data baselines." Drop the causal language about hallucination unless direct evidence is provided.
3. **Report error bars** (e.g., bootstrap confidence intervals) for the main MDQA and FLenQA results.
4. **Expand Stage 5** with training details and at least one baseline comparison.
5. **Add one format ablation** (e.g., dictionaries → prose paragraphs) to probe whether the transfer is format-specific.

## Score and Decision

The paper's core contribution — that finetuning on synthetic key-value retrieval tasks improves real long-context QA while preserving general capabilities — is interesting, plausible, and reasonably supported. However, two of the six stated findings (Finding 2 and Finding 6) overclaim beyond what the evidence supports due to a weakened MDQA baseline and conflated hallucination framing. These issues are fixable with revision and do not invalidate the paper's central empirical results, but they do reduce confidence in the paper as currently written. With the baseline fixed and the claims appropriately scoped, this would be solid work.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>