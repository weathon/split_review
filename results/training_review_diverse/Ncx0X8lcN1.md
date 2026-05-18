Now I have all the information I need to verify the reviewer claims against the paper. Let me produce the consolidated review.

## Summary

This paper presents HiReview, a two-stage framework for automatic literature review generation that first constructs a hierarchical taxonomy from a citation network (via graph-context-aware retrieval and hierarchical graph clustering) and then uses that taxonomy to guide LLM-based content generation. The approach is evaluated on a curated dataset of 518 review papers with extracted taxonomy trees and citation networks, showing consistent improvements over AutoSurvey and other baselines on LLMScore and BERTScore metrics.

## Strengths

- **Taxonomy-then-generation paradigm demonstrably improves structure and relevance.** Table 1 shows HiReview achieves Structure 0.9484 and Relevance 0.9428, substantially ahead of AutoSurvey (0.9122, 0.9093) and all other baselines. The ablation in Table 2 confirms removing the taxonomy drops Structure to 0.8790 and Coverage to 0.8612, directly validating that the hierarchical taxonomy drives the improvement.

- **Graph context-aware retrieval is critical to overall performance.** Table 2 ablation shows that removing the retrieval module collapses Coverage from 0.9163 to 0.6705 and Relevance from 0.9428 to 0.7073 — worse than zero-shot LLMs — establishing that the graph-aware retrieval is essential for both topic coverage and content relevance.

- **Consistently low variance across runs.** Table 1 reports standard deviations of ±0.03 or smaller across all LLMScore metrics for HiReview, reliably lower than AutoSurvey (±0.04–0.07) and pure LLMs (±0.07–0.14), indicating the framework produces stable, reliable outputs — a practical advantage for automated systems.

- **Novel soft-to-hard hierarchical clustering aligned with taxonomy structure.** The clustering design (Section 4.2.1) uses soft clustering at the base level (allowing paper overlap across topics) and transitions to hard clustering at higher levels, matching how real literature taxonomies organize papers. Table 3 shows this approach outperforms both K-means and LLM-based clustering.

- **Dataset contribution.** A manually curated dataset of 518 review papers with extracted taxonomy trees and 2-hop citation networks (average 6,658 papers, 11,632 edges) is constructed and released, providing a valuable resource for training and evaluating taxonomy-driven review generation.

- **Efficient joint training via pre-training and LoRA.** The two-step training strategy (Section 4.4) pre-trains the GNN clustering module, then fine-tunes the PLM with LoRA while keeping the GNN fixed. This avoids training instability from simultaneous GNN+LLM optimization and makes the approach computationally feasible.

## Weaknesses

### Fatal
None. The core claims are supported by experimental evidence, and no fundamental methodological flaw invalidates the contribution.

### Major

1. **Factual accuracy is claimed in the abstract but not directly evaluated.** The abstract claims "superior ... factual accuracy," and the introduction motivates the work by noting LLM hallucination problems. However, the evaluation relies entirely on **LLMScore** (coverage, structure, relevance) and **BERTScore** (semantic similarity to human-written reviews). Neither metric directly measures factual correctness, grounding, or whether specific claims in the generated review are accurate. A plausible confound exists: a well-structured, fluent review containing factual errors could score well on both metrics. This is a mismatch between what is claimed and what is measured. The authors should either (a) add a direct evaluation of factual accuracy (e.g., fact-checking against the source papers, human annotation of factual errors per generated paragraph), or (b) remove the factual accuracy claim and confine the stated contributions to what the metrics actually measure (coverage, structure, relevance).

### Minor

2. **Clustering evaluation metric undefined and baselines too narrow.** Table 3 reports "Accuracy of hierarchical clustering" without defining what accuracy means (exact cluster match? pairwise agreement? adjusted Rand index?). The baselines compared are LLM clustering and K-means, which are not standard graph clustering methods. Adding comparisons to citation-network clustering methods (e.g., Louvain, Leiden) and reporting a clear metric (e.g., adjusted Rand index or normalized mutual information against the ground-truth taxonomy at each hierarchical level) would make the clustering contribution verifiable.

3. **Key hyperparameter values not reported.** The paper introduces several hyperparameters (α for neighbor weight in retrieval, p_τ for edge connection threshold, τ for temperature, λ_l for hierarchical loss weighting, number of hierarchical levels L, LoRA rank, learning rates, train/test split) but does not report their values or how they were selected. Providing these is essential for reproducibility.

4. **Taxonomy extraction process from review papers is not described.** The paper states (Section 5.1) that taxonomy trees were extracted from 518 review papers but never explains how. Was this done by parsing section headings automatically? Through human annotation? What was the inter-annotator agreement? This matters because the extracted taxonomy trees serve as ground truth for both clustering supervision and evaluation, and the quality of the dataset depends on this process.

5. **No comparison to dense retrieval methods for the retrieval module.** The graph-context-aware retrieval uses BM25 on paper titles with neighbor score aggregation. The paper claims "significant improvement in retrieval accuracy" but provides no retrieval ablation comparing BM25+neighbor against dense retrieval options (e.g., Sentence-BERT, SPECTER) that could leverage paper abstracts or full text. Since titles are short and retrieval quality bounds downstream performance, this comparison would strengthen the paper.

6. **Limited human evaluation grounding.** While the paper follows AutoSurvey's protocol (citing Wang et al. that LLMScore aligns with human preferences), the field would benefit from at least a small-scale human evaluation (e.g., 5–10 topics, rated by domain experts on coverage, structure, and factual accuracy) to validate the automated metrics for this specific method. This is noted as minor because the paper's evaluation approach is consistent with prior work in the area.

### Trivial

7. **The multi-version selection step (generating multiple reviews and selecting the best via LLM evaluation) introduces uncontrolled variance.** The paper does not analyze how this selection process affects the scores or what consistency the selection criterion achieves across runs.

8. **"Hyper-parameters" — the paper refers to α as "a pre-defined weighting factor" without specifying the value or a sensitivity analysis.**

## Nice-to-Haves

- A sensitivity analysis on α (neighbor weight) and p_τ (clustering threshold) would demonstrate robustness to hyperparameter choices.
- A discussion of failure cases (e.g., when the citation graph is sparse, when topics cut across citation clusters) would provide practical guidance on when HiReview works best.
- Reporting the number of hierarchical levels per review on average and how the stopping criterion (no further meaningful clusters) is operationalized would improve reproducibility.
- Analysis of whether the taxonomy extracted from human-written reviews matches the paper's predicted taxonomy (beyond just clustering accuracy) would validate the overall approach more directly.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Contradiction about fine-tuning the topic generator"** — REMOVED. The reviewer claims a contradiction between fine-tuning LLaMA on 518 reviews and the w/o clustering variant using GPT-4o "as the number of taxonomy trees is insufficient for effective fine-tuning." This is not a contradiction. The main experiment fine-tunes LLaMA on the **per-cluster topic generation** task, where each cluster at each hierarchical level provides a training example (many more than 518). The w/o clustering variant generates the entire taxonomy in a single step, for which only 518 examples exist. Different granularities → different data quantities → no contradiction.

2. **"First claim overstated"** — REMOVED. The paper does not explicitly claim to be "the first" to use hierarchical taxonomy generation from citation networks. It uses "novel" (standard academic language). The only explicit novelty claim ("an issue that no existing work addresses") refers specifically to the soft-to-hard clustering transition — a narrow technical point that is defensible. The paper clearly distinguishes its taxonomy-then-generation approach from AutoSurvey's outline-then-generation.

3. **"Scalability concern about small graphs"** — REMOVED. The 2-hop citation networks averaging ~6.6K nodes are the appropriate scale for evaluating LRG on individual review topics. The paper's method processes the subgraph after retrieval, and the paper does not overclaim large-scale capabilities. Scaling to larger fields is a future-work consideration, not a weakness.

4. **"Multi-version selection adds uncontrolled variance"** — Kept as Trivial (see above).

## Novel Insights

The most striking finding from the reviews is that the graph-context-aware retrieval module is by far the most critical component — its removal causes a catastrophic drop (Coverage from 0.9163 to 0.6705, Relevance from 0.9428 to 0.7073) that is much larger than the drop from removing the taxonomy itself. This suggests that for literature review generation, getting the right papers is both harder and more important than organizing them well — a finding with practical implications for future LRG system design. Conversely, it also means that the paper's main claimed novelty (hierarchical taxonomy generation) produces a comparatively modest incremental gain over the retrieval + clustering pipeline, which warrants clearer acknowledgement.

## Suggestions

- Directly address the factual accuracy gap: either add a factual accuracy evaluation (e.g., LLM-as-judge for factual consistency against source papers, or human annotation of factual errors) or remove the claim from the abstract and introduction.
- Define the clustering accuracy metric in Table 3 and include comparisons to standard graph clustering methods (e.g., Louvain, Leiden).
- Report all hyperparameter values (α, p_τ, τ, λ_l, number of levels, LoRA rank, learning rates) and the train/test split.
- Describe how taxonomy trees were extracted from review papers (annotation protocol, quality control, inter-annotator agreement if human).
- Add a retrieval ablation comparing BM25+neighbor against a dense retriever (e.g., SPECTER, all-MiniLM-L6-v2) to justify the design choice.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>