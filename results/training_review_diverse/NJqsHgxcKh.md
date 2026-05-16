Now I have all the information I need. Let me synthesize the final review.

## Summary

MetaTST proposes incorporating multi-level textual metadata (dataset descriptions, task descriptions, sample statistics) into time series forecasting by formalizing metadata via language templates and using a frozen LLM to encode them into tokens that complement standard series tokens. The method is evaluated on short- and long-term forecasting under both single-dataset individual and multi-dataset joint training settings across twelve benchmarks, achieving SOTA results.

## Strengths

1. **Novel and well-motivated direction.** The paper identifies a genuinely underexplored gap — metadata describing the forecasting scenario — and proposes a structured way to incorporate it via multi-level language templates. This is a clean departure from prior work that uses only time series values.

2. **Consistent SOTA across extensive benchmarks.** MetaTST achieves the best average MSE/MAE on short-term individual (0.300 vs. next-best TimeXer 0.307), long-term individual (0.125 vs. TimeXer 0.132), short-term joint (0.281 vs. TimeXer 0.311), and long-term joint (0.136 vs. TimeXer 0.150) settings. The breadth across twelve datasets and two training paradigms is substantial.

3. **Compelling joint-training results.** MetaTST is the only method that consistently benefits from joint training: positive promotion on all datasets (+10.8% short-term, +3.54% long-term), whereas baselines like PatchTST, iTransformer, and TimeXer often degrade (negative promotion). This directly supports the claim that metadata helps disambiguate cross-domain patterns — the strongest empirical result in the paper.

4. **Frozen LLM as encoder (not backbone) is a principled design choice.** Unlike GPT4TS and TimeLLM, which fine-tune LLMs as the forecasting backbone, MetaTST uses a frozen LLM only to encode text descriptions, avoiding expensive fine-tuning. The ablation (Fig 4a) showing encoder LLMs (BERT, T5) outperform decoder LLMs (Llama, GPT-2) is informative and aligns with the role of the LLM as a representation extractor.

5. **Ablation confirms metadata contributes beyond endogenous/exogenous series.** Figure 3 shows removing metadata consistently degrades performance across both individual and joint settings, demonstrating that metadata provides non-redundant information.

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablation: is the LLM encoding necessary, or would a simple learned embedding suffice?** The paper ablates the content of metadata (Fig 3) but never tests whether the LLM encoding itself is needed vs. a cheap non-LLM alternative (e.g., a learned lookup table for dataset ID + task ID, plus a linear projection of sample statistics). The paper frames the LLM as providing "vast prior knowledge of the world" for metadata understanding, but this claim is unsubstantiated without this control. If a simple learned embedding matches MetaTST's performance, the paper's most distinctive architectural claim collapses. This is the single highest-leverage missing experiment and a significant gap in the evaluation.

### Minor

2. **Motivation–method framing mismatch.** The introduction motivates metadata with an example of two crossroads whose similar traffic patterns diverge due to different *company closing times* — a sample-specific external fact. Yet the actual metadata is primarily dataset- and task-level descriptions (domain, frequency, target variable) plus sample-level statistics (mean, std) derived from the series itself. None of these supply the kind of localized external knowledge the example invokes. The paper's claimed contribution about LLMs providing "context‑specific" world knowledge is thus overstated for the content the metadata actually contains. This is a presentation/overclaim issue, not a fatal flaw — the method still delivers genuine gains — but the framing should be adjusted.

3. **No statistical significance for small improvements.** Results are single-run with no confidence intervals, standard deviations, or multiple seeds. While this is standard in time-series forecasting, the reported margins are often small (e.g., 0.001–0.003 MSE on ETTh1, ETTh2, ETTm1, Weather in Table 2), making it difficult to assess whether the gains are reliable or noise. The ablation study (Fig 3) also lacks error bars.

4. **LLM choice for main experiments is ambiguous.** The method section mentions "LLM can be of any architecture, ranging from auto-regressive LLMs (e.g. Llama-3-8B)" but never explicitly states which LLM was used for the main results (Tables 2–5). Fig 4a compares BERT, T5, GPT-2, and Llama — and BERT works best — but without the main-text specification, the reader cannot assess computational fairness or reproducibility. Given that Fig 4a suggests BERT-base (~110M params) would be a natural choice, the asymmetry concern raised by the harsh critic (assuming Llama-3-8B was used) is largely defused, but the paper should state its choice explicitly.

5. **Efficiency analysis may undercount LLM cost.** Figure 4b compares training speed but the paper does not clarify whether the (frozen) LLM forward pass time is included in MetaTST's bar. Since sample-level metadata (mean, std) varies per sample, the LLM encoding cannot be fully cached and must be computed fresh. The efficiency claim is "favorable" but cannot be evaluated without knowing whether this cost is included.

6. **Sample-level statistics are derived from the input series.** The sample-level metadata (mean, std, start timestamp) is computed from the input series itself — it is not "external" context. The paper should discuss whether this redundancy adds value beyond what the Transformer could learn from normalized inputs.

### Trivial
- The metadata templates themselves are not shown in the main text. At least one example per level (dataset, task, sample) should be included for clarity and reproducibility.

## Nice-to-Haves
- A robustness test where metadata is randomized or corrupted would strengthen the causal claim that the model uses semantic content.
- Per-dataset breakdown in the ablation study (Fig 3) instead of dataset-averaged bars would better reveal where metadata matters most.

## Removed Points

These points are flagged for removal; treat them with caution.

- **The critic's claim that "the main tables use Llama-3-8B" causing severe computational asymmetry.** The paper only lists Llama-3-8B as an *example* architecture; it never states it was used for main experiments. Fig 4a shows BERT works best, making BERT-base (~110M params) the likely choice, which would have comparable capacity to the GPT-2 backbone used in LLM4TS baselines. The underlying concern (unclear LLM choice) is kept as Minor #4 above.
- **The critic's claim that "the dismissal of prior LLM4TS as 'statistically ineffective but computationally expensive' is not substantiated."** This dismissal appears in Related Work but is empirically supported later in the Experiments section (MetaTST outperforms GPT4TS and TimeLLM with lower cost). It is a sequencing issue, not a factual gap.
- **Criticisms about metadata templates not being shown / being in the appendix.** Parser-stripped appendix content is not a weakness of the paper.
- **The critic's claim that Fig 3 "aggregates over datasets in a way that hides variance."** The figure caption describes individual per-dataset ablation results; without seeing the figure, this criticism is speculative and possibly incorrect.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a tension the paper does not fully address: the gap between the motivating narrative ("metadata provides external world knowledge via LLMs") and the simplest explanation of the results ("adding discriminative dataset-level features to the token sequence improves forecasting"). The joint-training results — where MetaTST is uniquely able to benefit from mixing diverse datasets — are the strongest evidence that metadata helps with cross-domain disambiguation, and they arguably constitute the paper's most compelling contribution. This suggests the most direct path to strengthening the paper is not a more elaborate LLM pipeline but rather demonstrating that the metadata mechanism is *qualitatively different* from simply increasing model capacity or adding dataset embeddings.

## Suggestions
1. Add a non-LLM metadata baseline: a learned lookup table for dataset ID + task ID + linear projection of sample statistics (mean, std, start timestamp). If this matches MetaTST, the LLM is incidental; if it underperforms, the LLM's value is proven.
2. Explicitly state which LLM was used for the main experiments in the main text (e.g., "we use BERT-base as the metadata encoder throughout").
3. Run 3–5 seeds for at least the main tables and report mean ± std.
4. Clarify whether the LLM forward pass cost is included in the efficiency analysis.
5. Adjust the motivating example to match what the metadata actually provides, or add a discussion of what types of metadata would be needed for the crossroads scenario.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>