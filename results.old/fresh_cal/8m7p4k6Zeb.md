Now I have all the information I need. Here is the consolidated review:

---

## Summary

This paper proposes finetuning LLMs (GPT-3.5 Turbo and Mistral 7B) on fully numerical synthetic key-value retrieval tasks to improve their long-context information retrieval and reasoning capabilities. The authors design two synthetic tasks (simple and multi-subkey dictionary retrieval), and show that finetuning on them (1) flattens the U-shaped accuracy curve on multi-document QA, (2) improves FLenQA reasoning even without chain-of-thought, (3) causes minimal degradation on general benchmarks, and (4) outperforms several other long-context augmentation baselines on knowledge-benchmark retention.

## Strengths

- **Synthetic KV retrieval finetuning demonstrably transfers to real MDQA tasks.** Figure 2 shows that for both GPT-3.5 Turbo and Mistral 7B, finetuning on synthetic data flattens the U-shaped/primacy-biased performance curve across gold-document positions 1–20 in 20-document MDQA, with clear improvements in the middle positions where the original models struggled most.

- **Improvement on FLenQA holds even without chain-of-thought prompting.** Figure 4 shows that both models finetuned on synthetic data achieve substantially higher accuracy than the originals when forced to answer "True"/"False" directly, indicating that the internal reasoning capability (not just surface-level retrieval) is enhanced.

- **Answer templates provide a clear, well-supported benefit.** Across all evaluations (MDQA, FLenQA with and without CoT), the "w/ template" variants consistently outperform "w/o template" variants. The token-level loss visualization (Figure 3) provides mechanistic evidence that templates let the model focus on the retrieval content rather than output formatting.

- **Synthetic finetuning causes minimal degradation on general benchmarks, unlike several alternative long-context datasets.** Table 2 shows that Mistral 7B finetuned on MultidocQA, IN2, or Needle-in-a-haystack suffers drops of up to 6.33% on TriviaQA and 6.73% on NQ-Open, while the synthetic-finetuned model shows negligible change. This comparison is informative even though the attribution of the drop to "hallucination" specifically is contestable (see Weaknesses).

- **The improvement extends to longer contexts (120-document MDQA).** Figure 5 shows that Mistral-7B-Instruct-v0.2 finetuned on synthetic data with a 24K context window improves over the original model across all tested gold-document positions.

## Weaknesses

### Fatal

None.

### Major

- **The comparison against finetuning on MDQA data (Finding 2) is constructed in a way that may inflate the relative advantage of synthetic data.** The paper explicitly states that for GPT-3.5 Turbo, the MDQA finetuning baseline was created by *prompting the model to generate complete sentences from ground-truth answers* and finetuning on those model-generated completions (line 162). This introduces model-specific noise and likely produces a weaker version of the target task, making the synthetic-data advantage look larger than it would be against a properly formatted version. For Mistral 7B, the paper does not specify whether the MDQA training data was reformatted similarly. Without a controlled comparison using the same answer-template structure for the MDQA baseline, the claim that synthetic data *outperforms* target-domain data (Finding 2) is not reliably supported. This is the most significant methodological concern in the paper.

- **The claim that synthetic data "does not encourage hallucinations" (Finding 6) is not directly tested, and the evidence provided is ambiguous.** The paper asserts this based on the observation that TriviaQA and NQ-Open accuracy drops for other baselines but not for synthetic finetuning. However, a drop on knowledge benchmarks could equally be caused by catastrophic forgetting of factual knowledge rather than hallucination *per se*. The paper does not evaluate hallucination directly (e.g., using a dedicated hallucination benchmark, or measuring whether the model generates more factually incorrect statements in open-ended generation). The cited work (Gekhman et al., 2024) studies hallucination from finetuning on *new* facts, while the other baselines here are finetuned on existing QA data that overlaps with pretraining — the mechanism may differ. This claim is broader than the evidence justifies and should be weakened or substantiated with a direct measure.

### Minor

- **No variance or significance measures are reported for the main results.** The key figures (Figures 2, 4, 5) and tables do not include error bars, confidence intervals, or multiple-seed results. Given the small training set sizes (150–350 samples), it is difficult to assess whether the observed gains are stable or depend on a particular random draw.

- **General benchmark evaluation for GPT-3.5 Turbo is incomplete.** MMLU is evaluated on only 20% of the data, and HellaSwag, TriviaQA, and NQ-Open are not reported for GPT-3.5 Turbo at all (Table 1). This limits the generality of Finding 5 for the GPT-3.5 Turbo model.

- **The failure on MDQA with relevant distractors (acknowledged in limitations) is a significant practical limitation.** The paper correctly notes that finetuned models do not improve on MDQA with relevant distractors (Figure 13). In many real-world settings, distractors are relevant to some degree. While the paper acknowledges this, it does not discuss how severely this bounds the practical utility of the approach.

### Trivial

None.

## Nice-to-Haves

- **Directly test what skill is being transferred.** Run the finetuned model on a probing task that isolates retrieval from other capabilities (e.g., retrieve a sentence by content rather than position). This could help explain why relevant distractors break the transfer.
- **Include baseline comparisons in the longer-context (120-document MDQA) experiment.** Figure 5 shows only the synthetic-finetuned model vs. original; adding other baseline comparisons (MDQA-finetuned, MultidocQA, etc.) would strengthen this result.
- **An analysis of what changes internally in the model** (e.g., attention pattern analysis or probing of representations before/after finetuning) could illuminate the transfer mechanism.

## Removed Points

The following points from the inputs were removed for the reasons stated:

- **Missing training hyperparameters (learning rate, batch size)**: The paper references \ref{sec:mistral_ft} for implementation details — this appendix section was stripped by the PDF parser, so the details exist in the original submission but are unavailable in the extracted text. Per instructions, criticisms about missing appendix content are removed.

- **"Only two base models tested"**: This describes the paper's scope, not a flaw. The paper never claims comprehensiveness across many models. This is a generic criticism that does not harm the core claims.

- **"Small training datasets (150–350 samples)"**: This is a descriptive fact about the methodology, not a weakness. The paper's results effectively demonstrate positive transfer even with small data, which is arguably a strength.

- **Criticisms about lack of attention analysis or probing**: These are suggestions for improvement, not weaknesses in what the paper does present. Moved to Nice-to-Haves.

- **"The paper does not report whether the other baselines were also finetuned with answer templates"**: The baselines (MultidocQA, IN2, Needle-in-a-haystack) are existing established datasets; applying answer templates to them would change their task structure and is not an obvious design choice. This criticism demands an apples-to-oranges comparison.

## Novel Insights

None beyond the paper's own contributions. The key empirical finding — that training on purely numerical key-value retrieval tasks transfers to natural-language document QA and reasoning — is the paper's central contribution and is well-supported. The observation that answer templates help focus learning is a nice design insight.

## Suggestions

1. **Redo the MDQA baseline comparison with proper formatting control.** Either match the answer template structure for the MDQA finetuning data, or use the raw answers in a consistent format. If synthetic data still wins under this controlled comparison, Finding 2 is substantially stronger.
2. **Weaken or substantiate the hallucination claim.** Either rename Finding 6 to something like "synthetic data does not cause the same knowledge-benchmark degradation as other baselines" (which the evidence directly supports), or add a dedicated hallucination evaluation.
3. **Add variance information.** Report results over multiple finetuning seeds or at minimum include bootstrap estimates for the key numbers in Figures 2 and 4.

## Score and Decision

The paper presents a clean, well-motivated idea with several compelling results (transfer to MDQA and FLenQA, benefit of answer templates, low degradation, favorable comparison against other baselines). The core contribution — that synthetic KV retrieval finetuning improves real long-context performance — is well-supported. However, two secondary claims (Finding 2: outperforming target-domain finetuning, and Finding 6: no hallucination) are not as well-supported as the paper presents them. The MDQA baseline comparison has an asymmetry that likely weakens the baseline, and the hallucination claim rests on ambiguous evidence. These issues are addressable in revision but weaken the paper in its current form. The core contribution is real and valuable.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>