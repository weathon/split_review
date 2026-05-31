Now I have a clear picture of the paper and can verify each claim. Let me write the consolidated review.

## Summary

This paper identifies a V-shaped "stability gap" phenomenon during LLM domain continual pre-training — an initial performance drop followed by recovery — and proposes three strategies to mitigate it: (1) multi-epoch training on a smaller subset, (2) high-quality data selection, and (3) matching the pre-training data mixture rate. Experiments on OpenLlama-3B (medical and legal domains) and Llama-3-8B (medical) show that the strategies improve domain task performance while using fewer training tokens. The resulting Llama-3-Physician model achieves competitive or superior results on medical benchmarks relative to existing open-source models and approaches GPT-4.

## Strengths

- **Empirical discovery of the stability gap in LLM continual pre-training, demonstrated across multiple models and domains.** Section 3.1 shows a consistent V-shaped curve in medical task performance for both OpenLlama-3B and TinyLlama (Figure 2a,b), and notes the same pattern for the legal and general domains. This identifies a previously undocumented phenomenon in LLM continual pre-training.

- **Mechanistic explanation supported by weight-level analysis.** Section 3.2 verifies that general-task (commonsense) performance follows the same V-shape (Figure 3a), and that bottom-layer weights initially change more than top-layer weights (ratio > 1.35 in Figure 3b). This goes beyond simply observing the gap to providing evidence for the plasticity/stability gradient interpretation.

- **Proposed strategies yield substantial gains under a fixed compute budget, outperforming existing continual pre-training techniques.** Table 1 shows that the combined strategies improve OpenLlama-3B's average medical accuracy by 4.5 percentage points using only 20B tokens (40% of the 50B baseline budget), surpassing baselines including learning-rate rewarming, replay, and layer-freezing.

- **The final Llama-3-Physician model achieves strong medical performance.** Table 2 shows Llama-3-Physician-8B outperforming similarly-sized models on four medical QA tasks after task-specific fine-tuning, and Table 3 shows its instruction-tuned variant approaching GPT-4's average on medical QA while exceeding it on classification, relation extraction, and summarization tasks (Figure 5).

- **Strategies extend from continual pre-training to instruction tuning.** Section 5.4 and Figure 5 demonstrate that the same three strategies reduce the initial stability gap during instruction tuning and achieve the best performance using only 25% of the original instruction data, broadening the contribution beyond pre-training.

## Weaknesses

### Fatal
None.

### Major

- **Law-domain results are asserted but absent from the main text.** Lines 57 and 100 state that the same V-shaped curves and strategy effectiveness were observed in the legal domain, but no law-domain results (tables, figures, or even summary statistics) appear anywhere in the main paper. Since the cross-domain generality of the stability gap and strategies is a claimed contribution, this omission is a significant evidential gap.

- **The "no forgetting" claim is not verified for the Llama-3-8B model.** The abstract claims the strategies "enhance the average general task performance without causing forgetting" — this is supported for the OpenLlama-3B experiments via Figure 4(c) (commonsense task performance), but the main Llama-3-8B / Llama-3-Physician evaluation (Tables 2, 3) only reports medical-domain benchmarks. No general-domain evaluations (MMLU overall, HellaSwag, WinoGrande, ARC, GSM8K, etc.) are reported for the Llama-3-8B model. A reader cannot verify that the central "no forgetting" claim holds for the paper's main result model.

- **Ablation does not isolate each strategy's individual contribution.** Figure 4 compares "5b Random" (Strategy I), "5b HQ" (Strategies I+II), and "rate-fixed-data-dynamic" (Strategies I+II+III), which is a progressive addition but never tests Strategy III alone (e.g., applying the pre-training mixture rate to the full 50B corpus without subsetting), nor Strategy II alone on a multi-epoch setup. A proper ablation table would cleanly separate the three design choices and strengthen the paper's claims about mechanisms.

### Minor

- **Baseline comparison conflates compute reduction with strategy effectiveness.** Table 1 compares the proposed method (20B tokens, multi-epoch) to the "full token baseline" (50B tokens, 1 epoch), "rewarming," and "replay" baselines at different token budgets. The rewarming and replay baselines are only shown at 50B tokens; comparing them at the same 20B budget would isolate gains from strategy design rather than from using fewer tokens overall.

- **Factor analysis results (learning rate, subset size) are described qualitatively without supporting plots.** Lines 107-108 describe findings about learning rate and subset size, but no figure or table shows the actual data. This reduces reproducibility and prevents readers from assessing the sensitivity of the reported results.

- **Theoretical explanation is plausible but not causally validated.** The plasticity/stability gradient explanation (Section 3.2) relies on correlational evidence (weight-update ratios and commonsense task curves) and the "self-replay" argument is not directly tested (e.g., by comparing with actual pre-training data replay). This does not undermine the empirical strategies, but it weakens the claimed conceptual contribution.

### Trivial

- Figure references in the text occasionally skip (e.g., line 55 references "Figure 2(b)" for PPL but Figure 2b is labeled for medical performance at the beginning; the PPL description appears to reference subfigure (c)).
- The scaling laws discussion in Section 2 (line 43) conflates pre-training scaling laws with continual pre-training; a tighter related work section would be clearer.

## Nice-to-Haves

- Reporting the rewarming and replay baselines at the same 20B token budget as the proposed method.
- Including statistical significance markers or at least acknowledging single-seed runs.
- Reporting estimated FLOPs or wall-clock time for the Llama-3-8B runs to make the efficiency claim more concrete.
- Providing finer-grained evaluation (e.g., every 1B tokens) in the initial phase of training to better characterize the stability gap onset.

## Removed Points

These points are flagged to be removed — treat them with caution:

- *"Reproducibility: paper does not specify data preprocessing steps / exact training config"* — The paper describes KenLM-based data filtering, the exact filtering threshold methodology (lowest PPL), and states that datasets and models will be open-sourced. This is sufficient for a conference paper; further details belong in the released code.

- *"'Do not see any potential risks' claim is too strong"* — The paper's sentence is about the strategies ("Our strategies are designed to address the machine learning problem of the stability gap, and we do not see any potential risks"), and the very next sentence disclaims real-world medical use. The critic misreads the scope of the safety claim.

- *"Strategy I is essentially training on a smaller dataset for more iterations — a standard technique"* — The paper cites Muennighoff et al. (2024) and Xue et al. (2024) in this context. The novelty lies in *why* this works (mitigating the stability gap) and the combination with Strategies II and III. This is not absent from the paper.

- *"The initial V-shaped drop is not surprising because similar phenomena are known"* — The paper explicitly borrows the stability gap concept from vision continual learning and acknowledges this. The contribution is finding it in a new setting (LLM continual pre-training) with new mechanistic evidence. The critic's framing is overly dismissive of the paper's own contextualization.

- *"Missing statistical significance"* — Single-run LLM training evaluations are the norm at this scale. This is a community-standard practice, not a flaw.

- *"Missing appendix details"* — The parser strips appendices; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation that the paper itself does not already make.

## Suggestions

1. **Include law-domain results** in the main text (at minimum a summary table comparable to Table 1's structure) to substantiate the claimed cross-domain generality.
2. **Evaluate the Llama-3-8B model on general-domain benchmarks** (MMLU overall, HellaSwag, ARC, GSM8K) to directly support the "no forgetting" claim for the paper's main model. This is the highest-leverage addition.
3. **Add a clean ablation table** for the OpenLlama-3B setting showing each strategy in isolation and all combinations (baseline, Strategy I only, II only, III only, I+II, I+II+III) to cleanly separate the contributions.
4. **Add a comparison of the proposed method against rewarming and replay baselines at matched compute budgets** (e.g., all methods trained with 20B tokens).
5. **Include the factor analysis data** (learning rate sweep, subset size comparison) as a figure or table rather than only qualitative prose.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>