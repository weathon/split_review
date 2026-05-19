- Decision: Reject
- Avg Score: 6.00
- Scores: 10, 3, 5, 6
Now I have thoroughly verified the paper content against each reviewer claim. Let me construct the consolidated review.

## Summary

This paper introduces "Writing in the Margins" (WiM), an inference pattern for LLMs that leverages chunked prefill of the KV cache to generate extractive summaries ("margins") from each context segment, which are then classified for relevance and appended to the prompt before final answer generation. The method requires no fine-tuning and is evaluated on 7 models across 4 benchmarks spanning multi-hop reasoning, single-hop QA, and aggregation tasks.

## Strengths

- **Large and consistent empirical gains on aggregation and multi-hop reasoning tasks.** On the CWE benchmark (aggregation), WiM improves F1 scores by 30+ percentage points for several models (e.g., Meta-Llama-3.1-8B-Instruct: LLM F1=0.22 → WiM F1=0.93 from Table 2). On multi-hop reasoning (HotpotQA, MultiHop-RAG), the average accuracy improvement is 7.5% across all 7 models (Table 2 average row, WiM Avg=0.73 vs LLM Avg=0.66). These gains are tabulated in full detail.

- **Novel KV-cache-aware prompting pattern with clear algorithmic specification.** The paper formally describes how to interleave margin generation with chunked prefill (Algorithm 2), showing which decoding steps are added and how they can be batched with prefill steps (Table 1). This differs from prior scratchpad and RAG approaches by exploiting the existing chunked-prefill mechanism and reusing the KV cache.

- **Ablation studies justify key design decisions.** Table 3 shows that filtering irrelevant margins improves accuracy for 6/7 models (e.g., Palmyra-4-Chat-128K: 0.64 filtered vs 0.55 unfiltered). Table 4 shows that using both margins and full context (WiM's default) outperforms using only margins or only context for 5/7 models. These controlled experiments isolate and validate the contributions of the two core components.

- **Interactive retrieval design with practical benefits.** Section 6 describes how WiM enables streaming margins, a progress bar, early exit, and human-in-the-loop labeling (Figure 5). These features address real-world concerns about latency and transparency in long-context processing.

## Weaknesses

### Fatal
None.

### Major

- **Unquantified computational overhead despite repeated efficiency claims.** The paper states that WiM "increases computational overhead marginally" (abstract), "adds only minimal additional computation" (Section 1), and "can be efficiently batched with the original prefill steps" (Section 2). However, no empirical measurements are provided — no wall-clock time, FLOPs, peak memory, tokens processed per query, or latency numbers are reported. The extra decoding cost of N short extractive generations (4–16 margin notes per query, as stated in Section 3) is non-trivial, and the claim that batching makes this overhead negligible is purely qualitative. Since efficiency is part of the paper's core value proposition, this gap prevents readers from evaluating the accuracy–cost trade-off.

### Minor

- **No statistical confidence or variance reporting.** Each experimental condition uses exactly 100 examples (Section 3). No confidence intervals, bootstrap estimates, or significance tests are reported. For the smaller reported differences between methods (e.g., individual model–task differences of 0.01–0.03 accuracy points), it is unclear whether the observed differences are reliable or within noise.

- **No real long-context benchmarks.** All tasks are RULER-based synthetic or subsampled datasets. The absence of standard long-context benchmarks such as LongBench, L-Eval, or Qasper limits external validity and makes it harder to assess how WiM transfers to naturally-occurring long-document scenarios.

- **No analysis of prompt sensitivity.** The margin generation prompt was "manually identified" as promising (Section 3). No experiments vary the prompt template, the segment size (tested only at 4096 for most tasks and 8192 for CWE), or the classification threshold. The first-token-based classification rule ("YES#" vs "NO#") is tightly coupled to the exact phrasing, but robustness to prompt variation is not assessed.

- **RAG baseline comparison is transparent but framed in a way that could mislead.** The paper replaces the RAG retriever with the same LLM classifier used in WiM (Section 3), and acknowledges this. However, claims like "WiM outperforms RAG by 9%" (Section 4) appear without qualification in prominent positions. A reader scanning the abstract and headlines could infer a comparison to standard RAG, which is not what was measured.

### Trivial

- The aggregated "Average (Excl. CWE)" column in the main results table (Table 2) combines 7 data points from HotpotQA (3 lengths), MultiHop-RAG (1), and SQuAD (3 lengths), effectively weighting each length variant equally rather than each dataset equally. Reporting per-dataset averages as supplementary would improve clarity.

## Nice-to-Haves

- The paper notes that 18.5% of CWE answers involve Python code (Section 4), which degrades F1 by ~20%. A deeper analysis of when and why models resort to this behavior, and whether WiM reduces it, would strengthen the contribution.
- Per-benchmark breakdowns in the ablation study (Tables 3 and 4) would be more informative than the current aggregation across three diverse benchmarks.
- While the paper describes an interactive retrieval design (Section 6), it does not include a user study or latency simulation. An implementation-based evaluation of the early-exit or streaming benefits would complement the design description.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"keep" column ambiguity in Table 1:** The column shows which KV cache entries are retained at each step (pkv for context, M for margins). The table caption and surrounding text explain this. This is not a substantive ambiguity.

- **RAG baseline is not representative (as an unfair-comparison criticism):** The paper explicitly states (line 285): "we replaced the retriever in RAG with the classifier used in WiM" and acknowledges "real RAG systems" would yield lower results. Per the filtering rules, criticisms about asymmetric comparisons that favor the baseline (not the author's method) are removed. The comparison is an ablation of the margin generation step, and the paper is transparent about it. (The framing concern about potentially misleading headlines is kept as a Minor weakness above.)

## Novel Insights

The harsh critic's primary insight — that the paper's central efficiency claim is entirely unsupported by measurements — is a real and important observation that would have been easy to miss given the paper's confident narrative tone. The strength finder correctly identified that the paper's ablations and multi-model evaluation are its strongest empirical assets. Neither reviewer questioned the core idea's novelty, which stands as the paper's strongest attribute.

## Suggestions

1. **Add a wall-clock time / memory measurement.** Even a single setting (one model, one task, with and without WiM) with token-level latency breakdowns would convert the efficiency claim from a qualitative assertion to an evidence-backed statement. Report: total inference time, peak GPU memory, tokens generated, and tokens processed for LLM, RAG, and WiM.

2. **Report standard errors or bootstrap confidence intervals** for the main comparisons, especially the headline average numbers. This is standard practice for 100-example evaluations and costs almost nothing.

3. **Add per-dataset average results** alongside the current aggregated "Average" column so readers can assess consistency without mental arithmetic.

4. **Disclaim the RAG comparison** explicitly in the abstract or at the start of Section 4: "Our RAG baseline uses the LLM classifier as a retriever; real RAG systems with cheaper retrievers would likely underperform this strong baseline."
