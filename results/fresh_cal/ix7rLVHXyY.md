## Summary

This paper introduces PIE (Performance-Improving Edits), a dataset of 77,967 C++ competitive programming submission pairs with deterministic execution time annotations from the gem5 full-system simulator. Using this benchmark, the authors systematically evaluate a range of LLM adaptation strategies for program optimization, including prompting variants (instruction, few-shot, chain-of-thought, retrieval-based) and fine-tuning methods (standard, performance-conditioned, self-play data augmentation). The best fine-tuned model (GPT-3.5 with synthetic self-play data) achieves a mean speedup of 6.86× under Best@8, outperforming the average human improvement of 3.66×, and the fastest model generation (9.64×) slightly surpasses the fastest human submissions (9.56×).

## Strengths

1. **Deterministic performance measurement via gem5 eliminates benchmarking noise.** Section 2 demonstrates that even a state-of-the-art benchmarking tool (Hyperfine) produces spurious speedups up to 1.91× on identical programs. Replacing this with gem5's deterministic simulation (line 88: "Executing deterministic programs in gem5 provides deterministic performance results") is a clear methodological advance over prior work relying on noisy hardware measurements. This was validated by 42.8 million simulations.

2. **Performance-conditioned generation yields large, well-documented gains over standard fine-tuning.** Section 4.2 reports that CodeLlama 13B improves from 47.75% optimized (3.43× speedup) to 66.56% optimized (5.65× speedup) under Best@8 with performance-conditioned generation—a substantial 65% relative improvement in speedup. The performance tags (ranked 1–10 per problem) are a clean adaptation of ideas from offline RL and prompt conditioning.

3. **Retrieval-based prompting far surpasses all other prompting baselines.** CodeLlama 34B jumps from 19.63% optimized (1.30× speedup) to 34.25% optimized (2.28× speedup) under Best@8 with dynamic retrieval, and GPT-3.5 improves from 26.23% (1.60×) to 51.64% (2.19×). These gains are far larger than those from instruction-prompting, few-shot, or chain-of-thought, convincingly demonstrating that the PIE dataset enables effective data-driven prompting.

4. **Large-scale, simulator-annotated dataset with careful construction.** The training set contains 77,967 pairs from 1,474 problems with a >10% improvement filter, 42.8M gem5 simulations for annotation, and problem-separated train/validation/test splits. The use of AlphaCode-generated test cases (median 104 per test problem) for broader coverage is a thoughtful addition, and the deterministic annotations are critical for both training and evaluation.

5. **Comprehensive evaluation across model families and budgets.** The paper evaluates CodeLlama (7B/13B/34B), GPT-3.5, and GPT-4 under multiple prompting and fine-tuning strategies, with results for Best@1 and Best@8. It also demonstrates that open models (CodeLlama 13B perf-cond, 5.65×) can be competitive with GPT-3.5 (6.86×) when appropriately adapted.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical uncertainty reported for stochastic LLM results.** All LLM evaluations use temperature 0.7 sampling with Best@k, yet no confidence intervals, repeated runs, or seed variability are reported for any condition. The paper itself demonstrates (Section 2, Hyperfine experiment) how easily measurement noise can produce spurious speedups. While the deterministic gem5 environment eliminates *measurement* noise, the *generation* process is inherently stochastic. Small differences between methods (e.g., 66.56% vs. 66.65% optimized, or the tight 9.64× vs. 9.56× upper-limit comparison) could shift with different random seeds. The broad qualitative trends (retrieval ≫ static prompting, fine-tuning ≫ prompting, perf-cond > standard fine-tuning) are large enough to be robust, but the lack of variance estimates weakens the precision of quantitative claims. *Verification:* The paper reports all results as point estimates with no error bars (see Section 4). The only variance reported anywhere is in the Hyperfine motivation experiment (lines 84–86).

2. **Human baseline computation is underspecified.** The paper repeatedly states that "the average individual human sampled in our test set achieved an average speedup of 3.66×" (abstract, line 11; introduction, line 38), but never precisely defines how this number is computed. Given that the test set contains 978 pairs from 41 problems (line 72), the 3.66× presumably averages speedups across all human-improvement pairs in the test set. However, the phrasing "average individual human" could also be interpreted as per-programmer best improvement averaged across programmers. This ambiguity matters because one of the paper's headline claims ("beats the average human") depends on this definition. The paper also does not clarify whether this baseline includes pairs near the 10% minimum threshold or whether failures (slower/incorrect submissions) are counted as 1.0× as they are for LLMs. *Verification:* No explicit definition of the 3.66× computation appears in the paper despite its use as a central comparison point (lines 11, 36, 38).

3. **Upper-limit comparison (9.64× vs. 9.56×) is under-described.** The method of aggregation for these critical numbers is unclear. Lines 167 and 199 describe comparing "the fastest human submissions in CodeNet" against "our model's fastest generation per problem," but it is not clear whether 9.56× and 9.64× represent (a) per-problem maximums then averaged across problems, (b) global maximum speedups across all problems, or (c) some other aggregation. The different search budgets (40 model generations vs. up to 118,841 human submissions) are acknowledged but not controlled for, making the comparison informative but not rigorous as a claim about "setting a new upper limit." Per-problem breakdowns would resolve this ambiguity. *Verification:* Lines 167 and 199 state the comparison but do not specify the aggregation function.

### Minor

1. **No ablation verifying that the model actually conditions on performance tags.** The paper introduces performance tags (1/10 to 10/10) and always decodes with the maximal tag "10/10" during inference. There is no experiment decoding with different tags (e.g., "5/10" or "1/10") to verify that the model truly conditions on the tag rather than ignoring it. The tags are assigned by rank within each problem (line 127), so the same absolute speedup could receive different tags on different problems—this is reasonable by design, but the lack of an ablation leaves uncertainty about whether the tag mechanism works as intended.

2. **Only mean speedups are reported; no distributional statistics.** The paper reports only the mean speedup across the test set (with 1.0× for failures). Reporting median, quartiles, and the proportion of cases where the model made the program slower or incorrect would provide a more complete picture of robustness. This is particularly relevant given that Best@k evaluation can produce high averages driven by a few very large speedups.

3. **Quality of AlphaCode-generated test cases is not validated.** The paper augments CodeNet's ~4 test cases per problem with AlphaCode-generated tests to reach a median of 104 per problem (line 77). While this increases coverage, there is no analysis of whether these generated tests exercise meaningful program paths or could introduce spurious failures/timeouts. The paper mentions excluding tests causing ~2-minute timeouts but does not further validate test quality.

### Trivial
None.

## Nice-to-Haves

- **Per-problem breakdown for the upper-limit comparison.** A table or histogram showing, for each test problem, the fastest human speedup, fastest model speedup, and number of attempts, would resolve the aggregation ambiguity and reveal whether the model's advantage is concentrated on a few problems.
- **Ablation decoding with different performance tags** (e.g., decode with "5/10") to verify the conditioning mechanism works as intended.
- **Quantification of CodeNet's timing inconsistency** beyond the Hyperfine experiment (which tests variance of identical runs, not accuracy of CodeNet's original CPU times).
- **Qualitative case studies** of model-generated optimizations (e.g., algorithmic changes vs. micro-optimizations) to characterize what the model has learned.

## Removed Points

These points were raised by reviewers but are not included as weaknesses in the main review for the reasons stated:

- *"Why not use the original CodeNet CPU times?"* — The paper already addresses this (line 70: "we found the information to be inconsistent"). The appendix (stripped) was cited for details. This is not a weakness; the authors chose a better method and justified it.
- *"Performance tags: same absolute speedup could get different tags on different problems"* — This is by design (relative rank within each problem). Different problems have different optimization headroom; ranking within problem is the correct signal. Not a weakness.
- *"Synthetic data may introduce bias toward patterns already captured by fine-tuned model"* — Purely speculative. The paper demonstrates positive results from synthetic augmentation (lines 195–197). Without evidence of harm, this is not a valid criticism.
- *"Few-shot examples can bias the model"* — The paper already discusses this (line 176, citing Zhao et al.). Not a weakness; the paper acknowledges and addresses this concern.
- *"CoT is an emergent capability only for large models"* — This is presented as an observation by the paper, not a flaw.
- Various formatting/style nitpicks — Removed as parser artifacts.

## Novel Insights

The two reviewers' perspectives are largely complementary rather than generating novel cross-insights. The harsh critic correctly identifies imprecision in the human baseline and upper-limit comparisons, while the strength finder correctly identifies the dataset and the large-margin adaptation gains as genuine contributions. The main synthesis is that the paper's qualitative trends (data-driven methods ≫ prompting, perf-cond ≫ standard fine-tuning, open models competitive with closed) are robust and well-supported, but several of the headline quantitative claims would be strengthened by more rigorous reporting practices (variance estimates, explicit aggregation formulas, per-problem breakdowns).

## Suggestions

1. **Add a "Statistical Considerations" subsection** reporting variance for key numbers: run each evaluation with 3–5 different random seeds and report mean ± std for speedup, percent optimized, and percent correct. This is the single most impactful fix.
2. **Explicitly define the human baseline computation.** State: "The 3.66× average is the arithmetic mean of speedups across all 978 test-set human-improvement pairs, where speedup = old_time / new_time and failures are excluded since all test pairs are accepted solutions." If a different computation was used, specify it.
3. **Clarify the upper-limit aggregation.** State explicitly whether 9.56× and 9.64× are arithmetic means of per-problem bests, geometric means, or global maximums. Consider adding a supplementary table with per-problem results.
4. **Add an ablation with different performance tags** (e.g., "5/10" vs "10/10") to demonstrate that the model genuinely conditions on the tag.
5. **Report distributional statistics** (median, Q1/Q3, failure rate) alongside means to give a fuller picture of model performance.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>