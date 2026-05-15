Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces PIE (Performance-Improving Edits), a dataset of over 77K C++ competitive programming submission pairs where a human programmer made a >10% speedup, with execution times measured deterministically using the gem5 simulator to avoid benchmarking noise. Using this dataset, the authors systematically evaluate prompting and fine-tuning strategies for adapting LLMs (CodeLlama, GPT-3.5, GPT-4) to program optimization, introducing techniques including retrieval-based few-shot prompting, performance-conditioned generation, and self-play synthetic data augmentation. The best adapted model (GPT-3.5 with synthetic self-play data) achieves a mean speedup of 6.86× with Best@8 sampling, and the paper explores whether LLMs can learn to reproduce and surpass the kinds of high-level algorithmic optimizations that human programmers perform.

## Strengths

- **Deterministic, reproducible performance measurement via gem5 is a genuine methodological contribution.** The paper convincingly demonstrates the severity of benchmarking noise (Hyperfine experiment showing mean 1.12× spurious speedup for identical programs, top 5% seeing 1.91×) and replaces noisy real-hardware measurements with the gem5 full-system simulator, providing deterministic execution times. This is a principled solution to a real problem that has plagued prior work on learned code optimization, and it underpins the reliability of the entire evaluation. (Section 2, "Performance measurement using gem5")

- **The PIE dataset is a large-scale, well-constructed resource for a practically important task.** At 77K+ pairs across 1,474 problems, with problem-level train/test splits and extensive unit tests (median 82.5–104 test cases per problem), the dataset enables meaningful research on LLM-based code optimization that was not previously possible. The use of gem5 for consistent runtime annotations adds significant value over prior datasets that relied on noisy or inconsistent timing. (Section 2)

- **Systematic exploration of many adaptation strategies with clear, well-supported conclusions.** The paper evaluates instruction prompting, few-shot, chain-of-thought, retrieval-based prompting, standard fine-tuning, high-quality subset fine-tuning, performance-conditioned generation, and synthetic self-play data — and cleanly demonstrates that data-driven methods using PIE substantially outperform prompting-only approaches. For example, performance-conditioned generation improves CodeLlama 13B from 3.43× to 5.65× speedup at Best@8 (Table: fine_tuning_experiments). The ablation of high-quality vs. full data and the synthetic data control experiment (footnote about quantity vs. type of data) lend credibility.

- **Novel techniques (performance-conditioned generation, self-play for optimization) are clearly effective.** Performance-conditioned generation tags training examples with a binned score (1–10) indicating proximity to optimal achievable performance for the problem. This yields consistent improvements across models. The self-play pipeline — generating novel competitive programming problems, then using a fine-tuned LLM to produce optimized versions — improves Best@1 performance and demonstrates a path to augmenting the dataset beyond human examples. (Section 3.2)

## Weaknesses

### Fatal
None.

### Major

- **The headline human-vs-model comparison is asymmetric in a way that inflates the claimed result.** The paper states that the model achieves a mean speedup of 6.86× "higher than average optimizations from individual programmers (3.66×)" — but the model is evaluated with Best@8 (8 generations with correctness filtering), while the human baseline is the average speedup of individual human edits (one attempt per data point). This is not an apples-to-apples comparison: giving the model multiple attempts and selecting the fastest correct output is a fundamentally different setup from measuring a single human submission. The second comparison (9.64× vs. 9.56× "upper limit") also compares 39,129 model generations against 118,841 human written-from-scratch submissions; these are different tasks (targeted optimization vs. general solution writing). The core contributions of the paper — the dataset, the evaluation framework, and the adaptation strategies — do not depend on this "outperforms humans" framing, but the abstract and introduction overstate it. The paper would be stronger if it reframed the human numbers as contextual reference points rather than a direct competition.

- **No statistical significance testing or confidence intervals for any speedup comparisons.** Given the small test set (41 problems, 978 pairs) and the large variance across problems, some of the reported differences between methods (e.g., 9.64× vs. 9.56×; the comparison between GPT-4 and GPT-3.5 CoT) may not be meaningful. This is especially relevant for the "new upper limit" claim, which rests on a 0.08× difference.

### Minor

- **The test set is inherently biased toward "optimizable" problems.** Because the dataset filters for pairs where a human achieved >10% improvement, the test set contains only problems with known optimization opportunities. This is appropriate for evaluating whether LLMs can learn from human optimization patterns, but it means the results do not speak to how the model would perform on arbitrary programs where improvements may be rarer or harder. The paper does not acknowledge this selection bias or its implications for generalizability.

- **Performance-conditioned generation requires knowing the optimal achievable performance per problem, limiting transferability.** The tags are constructed by comparing each solution to the best-in-dataset performance for that problem (using top-10% bins). This information is available only because the dataset contains all human submissions. In a realistic deployment scenario, this tag would be unknown. The method is thus tied to the benchmark structure in a way that may not transfer to new, unseen problems without some way to estimate the optimal performance.

- **Retrieval-based prompting lacks analysis of what is actually being retrieved.** The paper uses CodeBERTScore embeddings to retrieve similar programs but provides no case studies or analysis showing whether retrieved examples are semantically or algorithmically similar to the test program. A few qualitative examples would help validate the retrieval approach and build intuition.

- **The 42.8 million gem5 simulation claim is stated without any computational budget or feasibility details.** While this scale is plausible for an industry lab (Google DeepMind), the paper provides no information about parallelization strategy, simulator throughput, or total compute used. Given that gem5 is orders of magnitude slower than native execution, a brief discussion of how this was managed would increase confidence.

- **The correctness-speedup trade-off is acknowledged but under-analyzed.** The paper notes that retrieval-based prompting can increase speedup at the cost of correctness (Section 4), but does not analyze the Pareto frontier or discuss how users might navigate this trade-off in practice.

### Trivial

- The GPT-4 underperformance vs. GPT-3.5 on CoT Best@8 is attributed to "lack of output diversity" without any diversity measurement to support this claim.

## Nice-to-Haves

- **Comparison to non-LLM automated optimization tools.** The paper surveys related work on compiler transformations, autotuning, superoptimizers, etc., but does not include any as baselines. Adding even one representative (e.g., a superoptimizer or an autotuning search) would substantially strengthen the claim that LLM-based approaches add value. However, this is scope creep relative to the paper's stated focus on LLM adaptation, and its absence is not a fatal flaw.

- **Per-problem speedup distributions (histograms/CDFs) rather than just means.** This would help assess whether improvements are concentrated on a few easy problems or broadly distributed.

## Removed Points

- **Criticism about asking humans for multiple attempts (equal budget):** This is a reasonable suggestion but not a required fix — the paper is transparent about using Best@k, and comparing multiple LLM attempts to single human attempts is standard practice in the code generation literature. Moved to Nice-to-Haves.

- **Criticism about missing appendix sections:** Per instructions, the parser strips appendix content; these exist in the original submission.

- **Criticism about garbled table/figure references:** These are parser artifacts, not author errors.

- **Criticism that the paper does not compare to existing automated optimization tools as a weakness:** The paper's contribution is specifically about adapting LLMs for optimization and comparing LLM-based approaches against each other and against humans. Requiring comparison to superoptimizers, autotuners, or algorithm selectors demands the paper answer a different research question. Moved to Nice-to-Haves.

- **Criticism that the 10% threshold means the dataset only contains successful optimizations:** This is by design — the dataset is about learning from performance-improving edits that human programmers actually made.

- **Criticism about LLM-generated test cases from AlphaCode:** The paper acknowledges this (line 77) and filters problematic cases. This is a reasonable methodological choice, not a flaw.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the work that the authors themselves missed.

## Suggestions

1. **Reframe the human comparison.** Present the 3.66× and 9.56× numbers as contextual reference points rather than direct baselines that the model "outperforms." Acknowledge the asymmetry (single human edit vs. Best@8; human general-solution-writing vs. model targeted-optimization) explicitly.
2. **Add statistical significance testing** (e.g., bootstrap confidence intervals) for the key speedup comparisons, especially the 9.64× vs. 9.56× and the method-to-method comparisons.
3. **Discuss test set selection bias** explicitly and caveat generalizations to broader program optimization scenarios.
4. **Add qualitative retrieval examples** (2–3 good, 2–3 poor) to validate the retrieval approach.
5. **Provide a brief computational budget overview** for the gem5 simulation pipeline to address plausibility concerns.
6. **Include per-problem speedup distribution plots** (CDFs or histograms) to complement the mean values.

## Score and Decision

The paper's core contributions — a large, simulator-grounded dataset for code optimization, a systematic evaluation of LLM adaptation strategies, and several novel techniques (performance-conditioned generation, self-play for optimization) — are solid and well-supported. The main weakness is an overclaimed "outperforms humans" narrative based on asymmetric comparisons; this does not invalidate the paper's contributions but does require reframing and additional caveats. With reasonable revisions to the presentation of results, this paper would be a valuable addition to the literature.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>