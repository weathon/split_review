Now I have all the information needed to write the final review. Let me carefully synthesize.

---

## Summary

The paper identifies a genuine problem: existing temporal graph benchmarks are dominated by repeated edges, inflating apparent performance of temporal GNNs and masking their inability to generalize to unseen edges with sequential dynamics. The authors propose TGB-Seq, a collection of eight large-scale datasets spanning recommendation, social networks, citations, and web links, curated to minimize repeated edges and force models to learn sequential patterns. A controlled toy experiment (Table 1) shows that all nine tested temporal GNNs perform at chance level (~50% AP) on simple sequential dynamics while a sequential recommender gets 100%, cleanly motivating the benchmark. The main experimental results show that existing temporal GNNs suffer substantial performance degradation on TGB-Seq compared to established benchmarks, and training cost analysis reveals scalability bottlenecks.

## Strengths

1. **Controlled toy experiment cleanly isolates the sequential-dynamics deficit.** Section 3.2 (Table 1) constructs a synthetic dataset where the only signal is a sequential pattern. All nine temporal GNNs achieve only ~50% AP (random guessing), while SGNN-HN gets 100%. This is the single strongest piece of evidence supporting the paper's motivation.

2. **Mechanistic explanation of why memory and aggregation components fail.** Section 3.2 formally analyzes both the memory module (Equation 1) and the aggregation module (Equation 2), showing that when items have identical interaction patterns and timestamps, both modules produce identical embeddings. This goes beyond performance numbers to explain the architectural limitation.

3. **Large-scale, diverse, real-world datasets with verified power-law structure.** TGB-Seq includes eight datasets (1.8M–18.7M edges) spanning e-commerce, movie ratings, business reviews, social networks, citations, and web links. Figure 4 confirms power-law degree distributions (a hallmark of real networks). The diversity is valuable — performance rankings shift across datasets (e.g., GraphMixer best on ML-20M/Yelp but not Taobao), indicating the benchmark probes different capabilities.

4. **Training-cost analysis reveals practical scalability bottlenecks.** Figure 5 reports per-epoch training time across three dataset scales, showing memory-based methods (JODIE, DyRep, TGN) go OOT on larger datasets, and even efficient methods like DyGFormer take 3.5 hours/epoch on Yelp. This quantification is useful for practitioners.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Missing quantitative repeated-edge statistics.** The paper's central motivation is that existing benchmarks have "excessive repeated edges" while TGB-Seq is "carefully curated to minimize repeated edges." Yet the paper only provides the qualitative statement that "Only Yelp and Taobao contain a small number of repeated edges" (line 33). For the non-bipartite datasets (Flickr, YouTube, Patent, WikiLink), repeated edges are definitionally impossible by the nature of the interactions (you cannot follow, cite, or link to the same node twice from the same source). For ML-20M, MovieLens does not allow re-ratings, so repeats are essentially impossible. The gap is primarily for Yelp and Taobao, where exact percentages would be useful to verify the "small number" claim. Still, the absence of precise numbers for these two datasets leaves the central curation claim less quantitatively supported than it should be. **The authors should report for each dataset: (a) % of test edges that appeared at least once in training, and (b) % of test edges that are exact duplicates (same source, destination, timestamp).**

2. **Underspecified preprocessing pipeline for handling repeated edges.** The "Dataset preprocessing" paragraph (line 115) describes only chronological splitting and degree filtering. There is no description of *how* repeated edges were minimized — whether duplicates were merged, whether users with repeated interactions were filtered, or whether the raw data inherently lacked repeats. This affects reproducibility and should be clarified for each dataset.

3. **The "inherently incapable" claim is stronger than the evidence supports.** The abstract (line 7) states that existing methods "are inherently incapable of learning simple sequential dynamics." The supporting evidence (Table 1) comes from a toy dataset where nodes and edges lack features and all interactions share identical timestamps. The paper should acknowledge that in real-world settings with node features and variable timing, these methods might fare differently, and soften the claim to "struggle in the absence of distinguishing features" or similar.

4. **No sequential-dynamics baseline on non-bipartite datasets.** SGNN-HN (a sequential recommendation method) is only evaluated on the four bipartite recommendation datasets. On the four non-bipartite datasets, the paper shows only temporal GNN results. Without any baseline that *can* capture sequential structure on these datasets, it is unclear whether the low MRR scores (e.g., <20% on Patent) reflect genuinely hard problems or simply poor architectural fit of temporal GNNs. A simple baseline — e.g., a transformer over the chronological neighbor sequence of the source node — would help calibrate what performance is achievable.

### Trivial
None.

## Nice-to-Haves

- An ablation on the toy experiment where distinguishing features (e.g., position encodings) are added to break symmetry, to test whether temporal GNNs *can* learn the sequential pattern when symmetry is broken. This would strengthen the analysis of *why* they fail.
- A total-time-to-convergence analysis (best MRR within 48h) rather than per-epoch time, to give practitioners a clearer efficiency-effectiveness trade-off.
- A brief discussion of whether random negative samples could accidentally include positives that appear later in the test set (and how this is handled). This is a standard evaluation concern.

## Removed Points

- **SGNN-HN comparison is "asymmetric" / fatal.** The harsh critic framed this as a critical issue. However, SGNN-HN is a recommendation method designed for bipartite graphs; it is inapplicable to non-bipartite datasets by design. The paper's core evidence for temporal GNN failure comes from the toy experiment (Table 1), not solely from the SGNN-HN comparison. This concern is downgraded to Minor (point 4 above) — a useful suggestion but not a structural flaw.

- **Hyperparameter details missing from appendix.** The rule disallows penalizing missing appendix content (parser strips these). Removed.

- **Table 2 "nearly unreadable" due to parsing artifacts.** This is a parser issue with the PDF extraction, not a paper flaw. Removed.

- **Missing repeated-edge statistics for existing benchmarks (Wikipedia, Reddit, etc.).** Figure 2 already demonstrates the performance gap between repeated and unseen edges on these datasets. Adding exact percentages would be nice but is not required to support the paper's claims.

- **Negative sampling overlap concern.** Random sampling from all nodes is standard and the paper's approach is clearly described. This is a nitpick; removed.

- **Strength Finder's "robust evaluation protocol with 100 negative samples"** — kept as a supporting strength.

## Novel Insights

None beyond the paper's own contributions. The main novel insight is that the paper's toy experiment (Section 3.2) cleanly decouples sequential dynamics from repeated-edge memorization, revealing a blind spot in current temporal GNN architectures that the benchmark then systematically measures across diverse domains.

## Suggestions

1. Add a table reporting repeated-edge statistics (% of test edges that are repeats from training) for all eight TGB-Seq datasets, plus a comparison to existing benchmarks.
2. Provide a step-by-step preprocessing description for each dataset detailing how repeated edges were handled (merge, filter, keep-first, etc.).
3. Soften the "inherently incapable" language in the abstract and introduction to acknowledge the synthetic (no-feature, same-timestamp) setting of the toy experiment.
4. Include at least one simple sequential baseline (e.g., a transformer over neighbor sequences) on the non-bipartite datasets to calibrate difficulty.

## Score and Decision

This paper addresses a real and important gap in temporal graph benchmarking. The toy experiment is clean and convincing, the datasets are large-scale and diverse, and the evaluation is thorough. The weaknesses are fixable in a revision and do not undermine the core contribution: TGB-Seq is a valuable new benchmark that tests a capability (generalization to unseen edges with sequential dynamics) that existing benchmarks largely ignore. I recommend acceptance.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>