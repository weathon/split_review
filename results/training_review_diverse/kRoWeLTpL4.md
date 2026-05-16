Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces CP-Fuse, an inference-time method that fuses two language models trained on disjoint sets of copyrighted material. The approach adaptively weights model logits based on the generation history to reduce the likelihood of reproducing memorized training data. Experiments on overfitted models show a 25×+ reduction in exact-match substring lengths and competitive utility preservation compared to baselines like MemFree and token-wise cp-delta.

## Strengths

- **Dramatic reduction of verbatim memorization in the constructed setting**: CP-Fuse reduces exact-match substring lengths by over 25× compared to overfitted models (e.g., from 1469.80 to 69.58 for Python instructions, Table 1) and outperforms all three inference-time baselines (SystemPrompt, MemFree, cp-delta) on every dataset and split. The improvement is consistent across exact and approximate memorization metrics.

- **Preserved utility despite strong protection**: CP-Fuse achieves pass@1 scores on APPS (0.47), MBPP (0.43), and HumanEval (0.28) that match or exceed the overfitted models, and fluency on WritingPrompts (2.17) is preserved. MemFree degrades utility noticeably (0.32, 0.41, 0.24 on code tasks), whereas CP-Fuse does not suffer from the hallucination artifacts of filtering-based approaches.

- **Seamless integration with training-time methods**: Wrapping goldfish-loss models with CP-Fuse further reduces exact match (e.g., from 84.68 to 20.68), showing CP-Fuse is complementary to existing memorization-mitigation techniques.

- **Robustness to prefix-prompting extraction**: CP-Fuse maintains near-constant exact match as prefix length increases (Figure 4), demonstrating resilience against adversaries with partial knowledge of the training data.

## Weaknesses

### Fatal
None.

### Major

- **Theoretical overclaiming and weak connection to guarantees**: The paper's abstract states the balancing property "prevents the regurgitation of memorized data" (line 4), and the related work section claims it "offers a principled theoretical explanation" (line 79). However, Lemma 2 (the balancing property) does not actually guarantee copyright protection — it states that if one model dominated the history, *either* the next-token expected log-probabilities are balanced *or* the fused model collapses to the less-dominant model. In the second case, the less-dominant model could freely generate its own copyrighted content. The paper acknowledges this case in the text ("if the second case holds, then the generation of y_t is independent of log p^{(1)}") but this doesn't make it protective. The paper also does not prove that CP-Fuse satisfies *k*-NAF or any other formal guarantee — it is only described as "inspired by" the *k*-NAF framework. The theoretical framing therefore overstates what the balancing property actually provides. The method's empirical success is credible, but the theoretical narrative should be recalibrated to match the evidence.

- **Missing ablation of the adaptive mechanism**: The paper compares CP-Fuse (which performs a grid search over (α, β) at each token based on sequence history) against token-wise cp-delta (which uses fixed α = β = 1/2). The observed improvement is attributed to "adaptively setting the weights based on sequence history" (Section 5.1), but the experiment does not ablate whether the gain comes from history-dependence or simply from having any tunable parameters. A proper control would compare CP-Fuse (history-dependent grid search) to CP-Fuse with a single fixed (α, β) pair chosen per dataset. Without this ablation, the central claimed advantage of the method — that it is the *adaptive, history-dependent* weighting that drives protection — is not convincingly isolated.

### Minor

- **Evaluation limited to a constructed overfitting regime**: The paper uses models fine-tuned on disjoint 3,000-sample splits, where every training example is treated as copyrighted and models are heavily overfitted. This setting guarantees both high memorization and clean separability of copyrighted material — conditions that maximally favor a fusion approach. In realistic deployments, memorization is sparse, copyrighted content is not neatly separable across two models, and base models are not overfitted. The paper acknowledges this limitation in the conclusion ("operates under the assumption of copyright separability... it would be valuable to apply our algorithm in real-world scenarios"), but this acknowledgment does not fully mitigate the concern that the main results may not transfer. Showing results on standard pretrained models (e.g., GPT-2, Pythia) that reproduce copyrighted content at lower rates would significantly strengthen the work.

- **Utility not evaluated on the same prompts used for copyright metrics**: The utility benchmarks (APPS, MBPP, HumanEval, WritingPrompts fluency) use held-out test sets, not the copyrighted prompts from the fine-tuning splits. While this is standard for measuring general capability, it means we cannot directly assess whether CP-Fuse sacrifices correctness on the very inputs where copyright risk arises. A model that avoids copying by writing incorrect code on copyrighted prompts could look fine on standard benchmarks.

- **No discussion of computational or inference cost**: The grid search discretizes [0, 2) into 10 steps and [2, 10] into 9 steps at each token position. The paper calls this "efficient" but does not report latency, memory, or FLOPs relative to baselines. Depending on how the 2D grid is constructed (19² = 361 evaluations vs. 19 if α and β are constrained), the overhead could be substantial. This matters because CP-Fuse requires running two models at inference, which already doubles the baseline cost.

- **No standard deviations or confidence intervals**: The paper reports 95th-percentile averages without variability estimates. Given the stochasticity of text generation, this limits the reader's ability to assess the reliability of the reported improvements.

### Trivial
None.

## Nice-to-Haves

- Broader attack evaluation beyond prefix prompting (e.g., adversarial suffix attacks or "repeat the word" style extraction).
- Analysis of failure cases: when does CP-Fuse still regurgitate copyrighted content, and on what kinds of inputs?
- Evaluation on larger models and more realistic copyright scenarios (books, songs), as the authors acknowledge as future work.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"SystemPrompt is a straw-man baseline"** — removed because the paper explains its failure ("potentially due to the override of safety fine-tuning") rather than misrepresenting it. The baseline is a standard method from the literature.
- **"Lemma 1 is presented without proof"** — removed because proof deferral to appendix is standard practice in ML conferences.
- **"Goldfish loss experiment doesn't compare on the same metrics"** — removed because Table 3a actually does provide the comparison: GL Split 1→Split 1 (84.68) vs. CP-Fuse→Split 1 (20.68); GL Split 2→Split 2 (120.28) vs. CP-Fuse→Split 2 (25.50). The comparison is present.
- **"The table layout conflates two separate evaluations"** — removed as a formatting/style nitpick.
- **Various generic strengths from Strength Finder** — removed because they conflict with verified weaknesses (e.g., "theoretical explanation for copyright protection" conflicts with the verified theoretical overclaiming weakness).

## Novel Insights

The harsh critic raises a genuinely interesting observation: the balancing property's second case (p = p^(2)) means that CP-Fuse could, in principle, allow the less-dominant model to freely generate its own copyrighted content. This tension — between the intuitive appeal of "balancing" and the actual formal behavior of the algorithm — is worth exploring further. If the first model dominates the history and then the fused model switches to the second, the second model might generate content that the first model had been successfully suppressing. The paper's empirical results suggest this doesn't happen at problematic rates in practice, but understanding *why* — whether due to the specific grid discretization, the narrow range of α/β values, or the nature of the training data — would be a valuable contribution beyond what the paper currently offers.

## Suggestions

1. **Recalibrate the theoretical narrative**: Replace language implying that the balancing property "prevents" regurgitation with more measured framing (e.g., "intuitively discourages" or "empirically reduces"). Consider stating clearly that the method is heuristic with empirical validation, rather than claiming a principled theoretical guarantee.

2. **Add the missing ablation**: Compare CP-Fuse with history-dependent grid search against CP-Fuse with a fixed (α, β) chosen per dataset (e.g., via a validation set). This would isolate whether the adaptive mechanism is the source of the improvement over cp-delta, or whether any tunable parameters suffice.

3. **Report computational costs**: Provide wall-clock time and memory usage for CP-Fuse vs. baselines, acknowledging the overhead of running two models with per-token grid search.

4. **Add error bars or confidence intervals**: Even if only for a subset of experiments, variability estimates would substantially increase confidence in the results.

5. **Evaluate on a non-overfitted setting**: Test CP-Fuse on models that reproduce copyrighted content without deliberate overfitting (e.g., using the Carlini et al. extraction benchmark on a standard pretrained model). This would demonstrate the method's relevance beyond the paper's narrow constructed regime.

## Score and Decision

The paper introduces a novel, practically motivated approach to copyright protection and provides compelling empirical results within its constructed setting. However, the theoretical framing overclaims what the balancing property actually provides, and the key ablation distinguishing history-dependent weighting from mere parameter flexibility is missing. These are significant but addressable issues that do not invalidate the core empirical contribution. With revisions addressing these concerns, the paper would make a solid contribution to an important problem.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>