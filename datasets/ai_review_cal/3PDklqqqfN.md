- Decision: Accept
- Avg Score: 7.17
- Scores: 5, 8, 8, 8, 8, 6
Now I have a thorough understanding of the paper and the reviews. Let me write the consolidated review.

## Summary

This paper introduces Multi-Field Adaptive Retrieval (mFAR), a framework for retrieval over structured documents with explicit fields (e.g., title, author, abstract). It decomposes each document into fields, scores each field independently using both lexical (BM25) and dense (Contriever) scorers, and learns a query-conditioned weighting mechanism to adaptively emphasize the most relevant fields. On the STaRK benchmark (Amazon, MAG, Prime), mFAR achieves substantial gains over baselines including BM25, finetuned Contriever, and prior state-of-the-art methods, with the best variant (mFAR₁₊ₙ, combining single-field lexical with multi-field dense) reaching 0.478 H@1 average — a 27% relative improvement over AvaTaR (0.376).

## Strengths

- **Query-conditioned adaptive weighting is demonstrably necessary.** The ablation in Table 2 shows that removing query conditioning causes large drops across all metrics (e.g., −22.6% H@1, −16.3% MRR on average). This directly validates the paper's key design choice and is not merely a marginal improvement: on Prime with 22 fields, the drop is 41.1% H@1. This is a clean, convincing ablation.

- **Hybrid (dense + lexical) multi-field scoring achieves clear improvements over both single-field and single-scorer alternatives.** Table 1 shows mFAR₁₊ₙ obtains 0.478 H@1 (average) vs. AvaTaR's 0.376, BM25's 0.374, and Contriever-FT's 0.360. The pattern is consistent: hybrid variants outperform pure-dense or pure-lexical variants on nearly every dataset and metric, supporting the claim that mixing scorers is beneficial for structured documents.

- **Multi-field dense retrieval consistently outperforms single-field dense retrieval.** mFAR_Dense beats the finetuned Contriever (single-field) on all three datasets (e.g., Prime: 0.375 vs. 0.325 H@1). As the paper notes, this is "the first positive evidence in favor of multi-field methods in dense retrieval" — a specific, verifiable result.

- **The masking ablation study (Tables 3–4) provides fine-grained interpretability.** By zeroing out individual scorers or fields at test time, the paper reveals asymmetric scorer reliance across datasets (Amazon → dense, MAG → lexical) and field-level contributions (e.g., MAG's authors field being critical). This level of analysis is not possible with black-box retrievers and demonstrates practical controllability.

- **The framework works with off-the-shelf encoders without special pretraining.** Unlike prior structure-aware methods that modify pretraining objectives, mFAR uses standard Contriever and BM25. The gains are achieved purely through field decomposition and adaptive weighting, making the approach broadly accessible.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The inference approximation (top-k shortlist) is not analyzed.** The paper mentions using a top-*k* shortlist per field-scorer to avoid computing |ℱ||ℳ||𝒞| scores (line 124), but never reports the chosen *k* nor measures how often relevant documents fall outside the union of shortlists. Without this analysis, readers cannot assess the computational-accuracy trade-off. However, this concern cuts both ways: if the shortlist is lossy, it could only *underestimate* mFAR's true performance, making the reported gains conservative — so this does not threaten the paper's core conclusions. It is a missing ablation, not a methodological flaw.

- **The "state-of-the-art" claim is slightly conflated by including AvaTaR.** The paper states AvaTaR is "not comparable with our work" (line 173) yet lists it as the top prior method and claims to surpass it. The paper's strongest comparisons are against BM25 and Contriever-FT (fair, same encoder); the inclusion of agent-based AvaTaR as a SOTA benchmark alongside an explicit incomparability disclaimer is slightly inconsistent. This is a minor presentation issue — the core contribution stands without the AvaTaR comparison, and the paper is transparent about the limitation.

- **No variance or statistical significance is reported.** Results appear to be from a single training run (no mention of multiple seeds). While single-run evaluation is standard in large-scale retrieval benchmarks, and the margins over baselines are large, a statement of variance (e.g., over 2–3 seeds) would increase confidence, especially for smaller gaps (e.g., Amazon: mFAR_Single 0.574 H@1 vs. BM25 0.483 — large gap; but within mFAR variants, gaps are smaller).

### Trivial
None.

## Nice-to-Haves

- **Runtime/compute comparison.** The method uses multiple indices and scorers. A single sentence quantifying the inference cost (e.g., number of scores computed vs. a single-index dense retriever) would help readers assess practical overhead.
- **Deeper quantitative analysis of learned weights.** The qualitative examples (Figure 3) are compelling; a quantitative breakdown of average weights per field-scorer pair across queries would further validate that the model learns meaningful field selection.
- **Explicit discussion of the 512-token field-level advantage.** Each field is encoded separately, effectively expanding the total token budget beyond a single 512-token window. This is an inherent advantage of multi-field decomposition that could be controlled for.

## Removed Points

The following points from the inputs were assessed and removed:
- **"The adaptive mechanism is straightforward" suggestion** (from Harsh Critic's "Missing Parts") — Not a weakness. Simplicity is a strength of the approach, as the results are competitive despite using a simple dot-product + softmax weighting function.
- **Generic scope-creep suggestions** (e.g., "explore MLP or cross-attention for weighting") — These ask the paper to do something different rather than evaluate what it does. They address a design choice the paper explicitly makes and are not flaws.
- Some phrasing from the Harsh Critic's AvaTaR criticism was stronger than warranted — the paper does acknowledge the incomparability, and this is a framing issue, not a substantive weakness.
- The "Strengthening the Paper on Its Own Terms" section items that are already addressed as minor weaknesses or nice-to-haves above.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation about the paper that the authors themselves do not make.

## Suggestions

1. **Report the shortlist size *k* and an ablation on a subset** (e.g., dev set) comparing full scoring vs. shortlist scoring to quantify the recall loss. This directly addresses the main methodological concern without changing the paper's substance.
2. **Reframe the AvaTaR comparison.** Either state clearly that mFAR achieves the best reported results on STaRK *among methods using comparable retrieval architectures* (excluding agent-based approaches), or keep AvaTaR in the table but with a clear note that the settings differ.
3. **Add a brief note on training variance** — even a single additional run or a statement that single-run evaluation is standard for this scale would address the concern transparently.
