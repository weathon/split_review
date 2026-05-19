- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 8, 5, 8
Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me synthesize the final review.

## Summary
This paper introduces PIE (Performance-Improving Edits), a dataset of 77K+ human C++ program optimization pairs from competitive programming, with deterministic performance measurements using the gem5 full-system simulator. The paper then evaluates a comprehensive suite of LLM adaptation strategies (prompting, retrieval-augmented prompting, fine-tuning, performance-conditioned generation, and self-play synthetic data augmentation) on this benchmark. The best configuration (GPT-3.5 fine-tuned with synthetic data) achieves a mean speedup of 6.86× with Best@8 vs. 3.66× average human optimization, and an aggregate upper-limit speedup of 9.64× vs. 9.56× best human.

## Strengths

- **Deterministic, reproducible performance measurement via gem5 (Section 2).** The paper demonstrates that real-hardware benchmarking of identical programs can yield spurious mean speedups of 1.12× (std. 0.36), motivating their use of gem5 full-system simulation. This is a genuine methodological advance over prior code optimization work that relied on noisy real-hardware measurements. The 42.8M gem5 simulations provide a reliable foundation for all subsequent experiments.

- **Large-scale curated dataset (Section 2).** PIE provides 77,967 training pairs from 1,474 C++ competitive programming problems, each with deterministic gem5 runtime annotations and extensive unit tests (median 82.5 test cases/problem). This is the first large-scale open benchmark for high-level C++ code optimization, significantly advancing beyond prior work (e.g., DeepPERF on C#) in scale, language, and measurement rigor.

- **Novel performance-conditioned generation strategy (Section 3.2).** Tagging each fast program with a binned performance percentile (1–10) relative to all solutions for that problem, and prompting with the maximal tag during inference, yields substantial improvements: CodeLlama 13B improves from 47.75% to 66.56% Percent Optimized and from 3.43× to 5.65× speedup (Best@8). This is a technique specifically designed for the optimization task and cleanly validated.

- **Comprehensive and controlled evaluation of multiple adaptation strategies on a unified benchmark (Tables 2, 3, 5).** The paper systematically compares instruction prompting, few-shot prompting, chain-of-thought, retrieval-based prompting, fine-tuning, performance-conditioned generation, and synthetic data augmentation across both open (CodeLlama 7B/13B/34B) and proprietary (GPT-3.5/4) models — a more thorough evaluation than prior work.

- **Synthetic data augmentation via self-play with quantity control (Section 3.2, Footnote 5).** The paper includes an ablation comparing training on 5,793 OURS-only examples vs. 5,570 pairs that include synthetic programs, confirming that the benefit comes from the type of data, not quantity. This is good experimental discipline.

## Weaknesses

### Fatal
None.

### Major

- **No confidence intervals, variance estimates, or statistical testing for any headline metric.** All tables report point estimates (mean speedup, Percent Optimized) without standard errors, confidence intervals, or standard deviations. With only 41 problems in the test set (978 pairs), means could be driven by a handful of large speedups. The paper compares many methods (e.g., 5 fine-tuning variants) and reports rankings (e.g., 6.86× > 5.65×) without any statistical assessment of whether these differences are meaningful. This significantly undermines confidence in the relative method ranking. Adding bootstrap confidence intervals for mean speedup and paired tests (e.g., Wilcoxon signed-rank on per-problem speedups) is necessary.

### Minor

- **The claim of surpassing the fastest human speedup (9.64× vs. 9.56×) is not statistically supported.** The 0.08× margin is tiny, no confidence intervals are reported, and the comparison uses asymmetric sampling budgets: the model gets 40 generations per problem (39,129 total) while the human "budget" is the set of accepted submissions that happen to exist in CodeNet (118,841 solutions). The paper acknowledges the asymmetry ("with a higher sampling budget") but does not control for it. This claim should be explicitly caveated as "within experimental uncertainty" or dropped in favor of the stronger, well-supported result that the model can match the best human speedup.

- **The headline human comparison (6.86× Best@8 vs. 3.66× average human) under-acknowledges sampling budget asymmetry.** The model uses Best@8 (8 generations, pick fastest correct one), while the human baseline is the average of single improvement pairs from individual programmers. Best@1 results are presented in tables, but the abstract and introduction emphasize the Best@8 comparison without sufficient caveat. A human given 8 attempts might also achieve higher average speedup. This is a common issue in LLM evaluation but should be more clearly addressed in framing.

- **Timeout handling in gem5 not clarified.** The paper mentions a 2-minute timeout for gem5 simulations (line 88) but does not specify how many of the 42.8M simulations hit this timeout, nor how timeouts are handled in the speedup ratio (if a slow program times out and the fast program does not, the ratio is undefined/infinite). This should be reported for reproducibility.

- **Human baseline construction details incomplete.** The test set has 978 pairs from 41 problems, but the paper does not report how many unique programmers contributed to these pairs. If one programmer contributes many pairs for a single problem, the "average individual human" could be dominated by a few outliers. Clarifying the distribution would strengthen the baseline.

### Trivial

- The motivating example (sum from 1 to N, O(N) → O(1)) in Figure 1 is pedagogically useful but sets an expectation of dramatic algorithmic leaps that most test problems do not exhibit. The framing should acknowledge that the actual task involves more incremental optimizations.

## Nice-to-Haves

- An ablation conditioning on "1/10" or the full distribution of performance tags (rather than always "10/10") would isolate whether the tag functions as a task prompt or genuinely guides the model toward higher-quality optimizations.
- A brief analysis of failure cases (problems where the model produces no improvement across 8 samples) would deepen the contribution beyond point estimates.
- Reporting Best@40 average speedup (not just the aggregate upper limit) would help contextualize the 9.64× figure.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Potential data overlap from synthetic generation may leak optimization strategies"** (Harsh Critic, Issue 1, third bullet). This is speculative. The paper explicitly filters for identical I/O behavior (line 132) and tracks semantic duplicates. No evidence is presented to suggest leakage, and the critic provides no concrete mechanism by which structural similarity without I/O identity would transfer optimization strategies.

2. **"Synthetic data ablation is confounded by data size"** (Harsh Critic, Section 3). The critic claims the ablation uses 5,793 examples vs. 1,485 synthetic examples. This misunderstands the paper: the ablation compares 5,793 OURS-only examples against 5,570 pairs *that include* synthetic programs (Footnote 5, line 197). The datasets are roughly matched in size, directly controlling for the quantity confound. The paper already addresses this concern.

3. **"Missing hyperparameters and training details"** (Harsh Critic, "Missing Parts"). The paper states "We provide training details in \Cref{subsec:addtl_training_details}" (line 152), which was stripped by the PDF parser along with the appendix. Reproducibility details are present in the original submission.

4. **"Performance-conditioned tag might not correlate with absolute speedup"** (Harsh Critic, Section 3). This is speculative and contradicted by the experimental results (Table 5), which show that performance-conditioned generation substantially outperforms standard fine-tuning. Empirical validation is the appropriate measure, not a priori correlation analysis.

5. **"Surpassing the fastest human speedup"** (Strength Finder, Core strength 6). This strength conflicts with the verified weakness about the claim lacking statistical support and using asymmetric budgets. Per the filtering rules, when a strength and weakness disagree on the same evidence, the weakness wins.

## Novel Insights

The two reviews provide complementary perspectives. The Harsh Critic correctly identifies that the paper's strongest contribution is not the narrow claim of "surpassing humans" (which is fragile) but rather the *infrastructure* — the PIE dataset combined with gem5-based deterministic evaluation — and the systematic study of adaptation strategies whose relative rankings would be more trustworthy with uncertainty quantification. The Strength Finder usefully highlights that the performance-conditioned generation technique and the synthetic data quantity-controlled ablation are methodologically solid. Neither reviewer observes that the paper's fine-grained comparison of *retrieval* vs. *fine-tuning* vs. *performance-conditioned* approaches across model sizes constitutes a kind of "optimization strategy taxonomy" that could serve as a roadmap for practitioners — that is, the paper implicitly tells you which technique to use under which resource constraints (e.g., retrieval if you can't fine-tune, perf-cond if you can fine-tune open models, synthetic data if you have API access). This taxonomy aspect is a secondary contribution worth highlighting.

## Suggestions

1. **Add bootstrap confidence intervals** for mean speedup and Percent Optimized across all reported methods, and use a paired statistical test (e.g., Wilcoxon signed-rank on per-problem speedups) when comparing methods. This is the single highest-impact improvement.

2. **Reframe the 9.64× vs. 9.56× claim.** Either explicitly state that the two values are within experimental uncertainty (and thus the model matches the best human), or report a more conservative comparison (e.g., matching the model's sampling budget by taking the best-of-40 human submissions).

3. **Report how many gem5 simulations hit the 2-minute timeout** and how timeouts are handled in the speedup computation.

4. **Provide per-problem variance statistics** (e.g., distribution of speedups) to show results are not driven by a handful of outliers.
