Now let me write the final consolidated review.

## Summary

This paper investigates how memory granularity affects retrieval-augmented response generation in long-term conversational agents, and proposes **SeCom**, a method that (1) constructs memory units at the topical-segment level using an LLM-based conversation segmentation model (zero-shot or with reflection-based refinement on few examples), and (2) denoises memory units via prompt compression (LLMLingua-2) before retrieval. Experiments on LOCOMO and Long-MT-Bench+ show SeCom outperforming turn-level, session-level, and summarization-based baselines, while the segmentation model itself achieves strong results on dialogue segmentation benchmarks (DialSeg711, TIAGE, SuperDialSeg).

## Strengths

- **Systematic empirical analysis of memory granularity.** The paper provides clear evidence (Figures 2b, 2c) that both turn-level and session-level memory units degrade retrieval accuracy (DCG), and that response quality varies with chunk size (Figure 2a). This directly motivates the need for segment-level granularity and is a useful empirical finding independent of SeCom itself.

- **Effective compression-based denoising for retrieval.** The paper demonstrates that LLMLingua-2 improves retrieval recall at compression rates >50% across both BM25 and MPNet retrievers (Figures 3a, 3b), and increases similarity with relevant segments while decreasing similarity with irrelevant ones (Figure 3c). This is a clean retrieval-only evaluation that isolates the denoising effect at a fixed number of retrieved segments.

- **Strong conversation segmentation performance.** The proposed segmentation model (GPT-4 based, with optional reflection) outperforms all unsupervised baselines and many supervised baselines on three dialogue segmentation datasets (Table 4). The transfer learning result — learning a rubric from only 100 examples in a source dataset and generalizing to a target dataset — is particularly noteworthy.

- **Robustness across retrievers and LLMs.** SeCom shows smaller performance variance than baselines when switching between BM25 and MPNet (Table 1), and outperforms baselines with both GPT-3.5-Turbo and Mistral-7B (Tables 1, 3). This indicates the method is not tied to a specific retrieval or generation backbone.

## Weaknesses

### Fatal
None.

### Major

1. **Concentration of GPT-4 across data generation, segmentation, and evaluation, without human validation.** GPT-4 is used to (a) generate the LOCOMO test QA pairs, (b) power the segmentation model that constructs SeCom's memory units, and (c) score responses via GPT4Score and pairwise comparisons. This creates a situation where the same model family both *defines the task* and *evaluates the output*. While this does not invalidate the results, the paper's strongest claims (Table 1, Figure 4) depend almost entirely on GPT4Score, and the conventional metrics (BLEU, ROUGE, BERTScore) show smaller margins. The paper lacks any human evaluation or discussion of this limitation — a notable gap for a system claiming to improve *personalized* response quality. The concern is that systematic biases in GPT-4's preferences could inflate SeCom's apparent advantage, especially since SeCom's memory units are produced by GPT-4 itself. **Why it matters:** Without human judgments or an evaluation pipeline that breaks the GPT-4 dependency (e.g., human-written questions as in Long-MT-Bench+'s original design, or a non-GPT-4 evaluator), the convincingness of the claimed improvements is substantially weakened.

2. **Segmentation model capability is not disentangled from granularity choice.** SeCom's segmentation uses GPT-4, while the turn-level and session-level baselines use raw conversational structure with no equivalent segmentation step. The performance gap in Table 1 could therefore reflect the use of a far more capable model (GPT-4) to construct memory units, rather than the superiority of segment-level granularity *per se*. The paper ablates the compression component but never isolates the segmentation model's contribution — e.g., by replacing GPT-4 with a heuristic segmenter (sliding window, utterance embedding shift) and re-running the end-to-end QA experiment. Without this control, the reader cannot tell how much of the gain comes from the *idea* of topic-coherent segments versus the *engineering* of using a strong LLM to produce them. **Why it matters:** This directly affects the generality of the paper's central claim. If the advantage largely comes from GPT-4's segmentation capability, the contribution shifts from "segment-level memory works" to "GPT-4-powered segmentation works," which is a materially different finding.

3. **Compression ablation confounds denoising with number of retrieved units.** The ablation in Table 2 removes compression and reports a 9.46 GPT4Score drop on LOCOMO, attributed to "denoising improving retrieval quality." However, the context budget is fixed at 4k tokens. Without compression, each segment is longer, so fewer segments fit within the same token budget. The drop could simply reflect fewer retrieved memory units rather than any effect of noise removal. Figure 3 partly addresses this by showing compression improves recall at a fixed *K* (number of segments), but that is a retrieval-only evaluation on Long-MT-Bench+, not an end-to-end QA result on LOCOMO. **Why it matters:** The paper's central claim that compression-based denoising independently improves end-to-end performance is not cleanly supported by the current ablation design.

### Minor

1. **Ambiguity about compression settings for baselines.** The paper states that "denoising-enhanced turn-level and session-level" baselines are used in the main results, but does not explicitly confirm whether the same compression rate (75%) and the same LLMLingua-2 model were applied to these baselines. While this is the natural reading, an explicit statement would remove ambiguity.

2. **Summarization comparison fairness.** The paper argues that segment-level memory avoids "information loss" from summarization (citing Maharana et al., 2024), but segment-level memory also selects a subset of turns — it is a different kind of reduction. The paper does not directly compare against a summarization baseline that aims for the same token budget, so the "information loss" argument for the specific setting is plausible but not directly demonstrated.

### Trivial
None.

## Nice-to-Haves

- A small-scale human evaluation (e.g., 50–100 examples judged by 2–3 annotators for coherence, factuality, and preference) would substantially strengthen confidence in the GPT4Score trends.
- Reporting the average number of retrieved segments (or total tokens) in the "w/o denoising" condition under the fixed 4k budget would clarify the compression ablation confound.
- A sweep of compression rates (0%, 50%, 75%, 90%) on LOCOMO's end-to-end QA would be informative.
- Reporting end-to-end QA performance with the zero-shot segmenter versus the reflection-augmented one would show whether the small-annotation refinement matters in practice.

## Removed Points

These points were raised by the reviewers but removed after verification against the paper:

- **Reflection-based segmentation guidance is vague / hard to reproduce.** The reviewer noted the mechanism is described in abstract terms. However, the paper references Appendix Figures 6, 7, and 8 for the exact prompts and learned rubric. The parser strips appendices; these materials exist in the original submission. Removed per hard rules on missing appendix content.

- **The paper claims segment-level avoids information loss but doesn't prove it.** This is a matter of degree. The paper does compare against three summarization baselines (SumMem, RecurSum, ConditionMem) and shows they underperform. The argument is not unsubstantiated, though a token-budget-controlled comparison would be stronger. Moved to Minor rather than removed entirely.

- **Unfair comparison claims against baselines.** No evidence of unfair asymmetry favoring the author's method was found. If anything, the denoising-enhanced baselines are a generous design choice. Removed per hard rules.

## Novel Insights

Beyond the paper's own contributions, the most interesting cross-cutting observation from the reviews is that the paper's two main design choices — segment-level granularity and compression-based denoising — address different failure modes that interact in a non-trivial way. Segment-level units solve a *structural* problem (relevant information spans multiple turns; single turns are fragmentary, whole sessions are noisy), while compression solves a *signal-level* problem (within a retrieved unit, extraneous tokens dilute relevance signals for the retriever). The fact that the compression ablation (Table 2) produces a larger drop than the granularity ablation (Figure 5) suggests that the signal-level problem may be the more significant bottleneck in practice, at least given GPT-4's segmentation quality. This is a useful observation for future work: investing in better segmentation may have diminishing returns if the retrieved units are not also cleaned before retrieval.

## Suggestions

1. **Disentangle the compression confound.** Run the LOCOMO ablation with two controlled conditions: (a) SeCom w/o denoising but retrieving the same *number* of segments as the full SeCom (i.e., fewer tokens but same unit count), and (b) using padding or additional lower-ranked segments to match the total token budget. This would isolate whether the gain comes from noise removal or from fitting more units into the budget.

2. **Control for segmentation model capability.** Replace GPT-4 with a cheaper segmenter (e.g., utterance-embedding cosine shift with a threshold, or a simple fixed-window approach) and re-run the LOCOMO experiment. If SeCom still outperforms denoising-enhanced turn-level baselines, the granularity claim is robust. If performance drops sharply, the scope of the claim should be revised accordingly.

3. **Add at least a small human evaluation** or replace GPT-4 as the evaluator for one condition (e.g., use an LLM from a different family, or use human-written questions as the test set for LOCOMO, following the Long-MT-Bench+ protocol).

4. **Explicitly report the compression settings for baselines** and clarify whether the same LLMLingua-2 model and rate were used.

## Score and Decision

The paper addresses a genuine and practical problem (what granularity to store conversation history for retrieval), proposes a well-motivated two-component solution (segment-level memory + compression denoising), and provides fairly extensive experiments. The segmentation model's independent evaluation on dialogue segmentation benchmarks is strong, and the robustness checks across retrievers and LLMs are commendable.

However, the evaluation has three structural concerns — GPT-4 concentration without human validation, the segmentation model confound, and the compression ablation confound — that together weaken the convincingness of the claimed improvements. These are fixable but non-trivial to address. The core ideas are solid, and the paper is clearly written, but in its current form the evidence falls short of being fully convincing.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>