Now I have a thorough understanding of the paper and can verify each claim. Let me produce the consolidated review.

---

## Summary

This paper investigates the "first-step advantage" in multi-step math reasoning: smaller language models often fail because they cannot reliably select the correct initial reasoning step, even though they possess the knowledge to solve the task. The authors first demonstrate that providing the correct first step from a larger LLM (e.g., GPT-4) boosts small-model accuracy by up to 3× (Table 1), and that weaker first-step guidance can actually hurt performance. They then propose QuestCoT, a prompting strategy where the model asks itself a guiding sub-question before generating its chain of thought. QuestCoT yields consistent improvements over standard CoT across four math reasoning datasets and seven small models (Table 2). The core contributions are establishing the causal role of the first step in small-model reasoning and a simple, zero-training method to realize this benefit.

## Strengths

- **Direct causal evidence that getting the first step right is the critical bottleneck.** Table 1 reports dramatic gains when the first step is provided by GPT-4—e.g., OlMo-7B rises from 13.64 to 37.90 on GSM8K (nearly 3×), Gemma-2B from 7.50 to 17.84, and LLaMA2-7B from 10.53 to 23.27. The monotonic improvement with guiding-model quality (LLaMA2-70B → GPT-3.5 → GPT-4) confirms that first-step *quality* drives the effect, not just having any guidance.

- **Demonstration that smaller models possess latent knowledge they cannot consistently surface.** Figure 1 shows that with 35 samples, the accuracy gap between Mistral-7B and GPT-4 on GSM8K narrows from ~50 points to <10 points, supporting the claim that small models *can* generate correct answers but struggle to select the right chain on the first attempt.

- **QuestCoT delivers consistent, non-trivial improvements over CoT across models and datasets.** In Table 2, QuestCoT outperforms CoT on 25/28 model×dataset combinations. The gains are largest for the weakest models—OlMo-7B gains +5.8 (GSM8K), +8.6 (SVAMP), +5.0 (ASDiv), +7.2 (MultiArith)—where improving the first step has the most room to help.

- **Thorough leakage analysis.** The paper manually verifies on 1000 development samples that the first-step guidance does not leak the final answer (999/1000 cases where the first-step equation result does not match the final answer).

- **Qualitative analysis identifies concrete failure modes.** Figure 5 (in the paper) provides specific examples of unnecessary calculations, real-world knowledge errors, and context-understanding errors that CoT makes but QuestCoT avoids by starting with a well-chosen sub-question.

## Weaknesses

### Fatal
None.

### Major

- **No variance estimation or significance testing for the main QuestCoT results (Table 2).** The paper reports only point accuracies with greedy decoding (temperature=0) and a single random draw of 4-shot prompts from the test set. The gains for high-baseline models (e.g., Phi3-Mini: +2.0 on GSM8K, LLaMA3-8B: +1.0 on GSM8K) are small enough that they could be within the noise introduced by prompt selection—especially since "randomly selected from the test set" means different prompt draws could yield different results. Because the paper's central empirical claim is that QuestCoT *consistently* outperforms CoT, the absence of any variance characterization weakens the evidence. This is the most significant gap. (Note: the first-step guidance results in Table 1 involve much larger gains and are less vulnerable to this concern.)

- **The few-shot prompts for QuestCoT (Table 2) are sampled from the test set, which is non-standard.** The paper states (line 189) that "4-shot prompting with prompts randomly selected from the test set" is used. This means the few-shot examples are drawn from the same distribution as the evaluation samples, and a single random draw is used without characterizing variance across draws. While both CoT and QuestCoT use the same prompts (so the relative comparison is fair), the absolute accuracy numbers may not be directly comparable to standard benchmarks, and the results could shift with different prompt draws. The standard practice is to use training-set prompts or fix the prompts and average over multiple draws.

### Minor

- **The first-step guidance experiment lacks a clean control for *any* initial hint vs. a *correct* initial hint.** The paper partially addresses this by showing that guidance from a weaker model (LLaMA2-70B) can *hurt* Phi3-Mini's performance (Table 1: 76.95 → 75.10 on GSM8K), demonstrating that not all guidance is beneficial. However, a more direct control—e.g., providing a plausible but incorrect first step—would more cleanly separate the effect of "having guidance" from "having correct guidance." The "starting right" claim is central to the paper's framing, so this distinction matters.

- **The Subques comparison is shown only on two datasets (GSM8K, SVAMP) and in figure form without a full table reporting token costs.** Figure 4 shows that QuestCoT outperforms Subques across models, and the paper claims lower token costs, but no token counts are reported. A full table with exact accuracy numbers and token cost comparisons across all four datasets would strengthen this analysis.

- **The Venn diagram analysis (Figure 6) is based on a single model (Phi3-Mini).** The finding that QuestCoT shares more correct solutions with both CoT and Subques than those two share with each other is interesting, but replicating it on at least one more model (e.g., Mistral-7B or OlMo-7B) would make the claim more robust.

- **The error analysis in Section 5 is qualitative and based on non-random selection of success cases.** The paper examines "instances where QuestCoT was successful" and categorizes errors. This is a standard and useful qualitative approach, but a systematic categorization on a larger, defined sample (e.g., all cases where QuestCoT succeeded and CoT failed) would add rigor.

### Trivial

- The phrase "the model learns this questioning itself" (line 191) slightly overstates what is happening—the model is prompted to ask a sub-question via few-shot examples, not trained through a learning procedure. The paper immediately clarifies that "the only change from CoT is to add an extra question in the prompt as a demonstration," so this is a minor wording imprecision.

- The 1B-model null result is described as "not statistically significant improvements" but no formal test is reported. For a model achieving only 3-3.5% accuracy on GSM8K, the lack of meaningful improvement is clear, but the phrasing invites unnecessary criticism.

## Nice-to-Haves

- Reporting token-cost comparisons between CoT, QuestCoT, and Subques in a table format.
- Averaging results over multiple draws of few-shot prompts (even 3-5 runs) to provide variance estimates.
- A control condition in the first-step guidance experiment with a randomly generated or deliberately incorrect initial step.

## Removed Points

- **Criticism that Figure 1 metric "slightly overclaims" that smaller models can solve the task.** The paper is transparent about using "accuracy if an answer exists in one of the output chains" and explicitly interprets this as showing the model *can* produce correct answers, not that it reliably selects them. This is an accurate and appropriately qualified claim. The paper's own framing is coherent.
- **Criticism about the multiple-sampling metric being "accuracy if an answer exists."** This is the correct metric for testing whether the model has the knowledge to produce the correct answer—it directly tests the stated hypothesis. No overclaim.

## Novel Insights

None beyond the paper's own contributions. The review-derived insight of noting that the test-set prompt contamination and the lack of variance estimation compound each other—both increase uncertainty about whether the observed gains reflect a stable improvement or prompt-selection noise—is already implicit in the individual weaknesses.

## Suggestions

1. **Characterize variance for Table 2.** Even a small number of repeated runs with different few-shot prompt draws (3–5 draws), reporting mean and standard deviation, would substantially increase confidence in the QuestCoT gains. A bootstrap on the test set would also help.
2. **Switch to training-set prompts or development-set prompts** for the few-shot examples in the QuestCoT comparison, or explicitly justify why test-set prompts are used and report variance across prompt draws.
3. **Add a control for the first-step guidance experiment** where a plausible-but-incorrect first step is provided, to confirm that the benefit comes from correctness rather than from any hint.
4. **Expand the Subques comparison** to a full table with exact accuracies and token costs across all four datasets.
5. **Replicate the Venn-diagram analysis** on at least one additional model (e.g., Mistral-7B) to show the pattern generalizes.

## Score and Decision

The paper makes a genuinely useful observation—that starting correctly is the critical bottleneck for small-model reasoning—and proposes a simple, practical solution. The first-step guidance results (Table 1) are striking and well-controlled. The main weaknesses are in the presentation of the QuestCoT results (Table 2), where the lack of variance characterization and the non-standard test-set prompt selection reduce confidence. These are fixable issues that would strengthen a paper whose core finding is likely robust given the consistency of the pattern across 7 models × 4 datasets. The paper is a solid empirical contribution to understanding and improving small-model reasoning.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>