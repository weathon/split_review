Here is my final consolidated review.

---

## Summary

The paper identifies a critical blind spot in temporal graph benchmarking: existing datasets contain excessive repeated edges, which rewards memorization over generalization. It provides a clean existence proof (toy dataset) that nine temporal GNNs perform at chance on a simple sequential prediction task, then introduces TGB-Seq — eight large-scale datasets (ML-20M, Taobao, Yelp, GoogleLocal, Flickr, YouTube, Patent, WikiLink) curated to minimize repeated edges. Benchmarking shows that temporal GNNs suffer large performance drops and ranking inversions on TGB-Seq compared to prior benchmarks, while incurring substantial training costs.

## Strengths

1. **Clean existence proof of the failure mode.** The synthetic toy dataset (Section 3.2, Figure 3) is well-designed: it strips away features, timestamps, and structural asymmetry, leaving sequential order as the only predictive signal. All nine temporal GNNs score ~50% AP (chance) on this task (Table 1), while SGNN-HN succeeds. This cleanly isolates the architectural limitation the paper diagnoses.

2. **Empirical demonstration of repeated-edge bias.** Figure 2 shows an up-to-eightfold gap between MRR on repeated historical edges vs. unseen edges on four established datasets (Wikipedia, Reddit, Social Evo., Enron). This provides concrete evidence for the paper's critique that prior benchmarks overestimate temporal GNN capability by letting models rely on memorization.

3. **Diverse, large-scale, low-repeated-edge datasets.** TGB-Seq spans e-commerce, movie ratings, business reviews, social networks, citations, and web links, with millions to tens of millions of edges and power-law degree distributions (Table 2, Figure 4). Only Yelp and Taobao contain natural repeated edges. This directly addresses the paper's goal of creating a benchmark where memorization is not sufficient.

4. **Substantial performance degradation and ranking inversion.** Tables 3 and 4 show methods that excel on existing benchmarks (e.g., DyGFormer at 0.869 MRR on Wikipedia) collapsing on TGB-Seq datasets (0.035 on GoogleLocal). The relative ordering of methods changes dramatically across datasets (TCL best on Taobao, weak on Yelp; GraphMixer the reverse), showing that TGB-Seq surfaces capabilities that prior benchmarks do not distinguish. The training cost analysis (Figure 5) adds practical insight: memory-based methods cannot complete one epoch within 24 hours on the larger datasets.

## Weaknesses

### Fatal
None.

### Major

1. **The paper does not validate that TGB-Seq datasets test *sequential dynamics* specifically.** The benchmark is motivated as evaluating "capturing sequential dynamics," but the primary construction criterion is minimizing repeated edges. The paper provides domain-level intuition (recommendations, who-to-follow are argued to involve sequential order) but offers no control experiment showing that a model that exploits sequential order (e.g., a Transformer on interaction sequences) significantly outperforms one that ignores order (e.g., a bag-of-interactions baseline) on these datasets. Without this, the claim that temporal GNN failures on TGB-Seq are due to inability to capture sequential dynamics — as opposed to edge novelty, dataset sparsity, scale, or degree distribution — remains an untested assertion. The toy example proves temporal GNNs *can* fail on sequential dynamics, but does not prove that their failure on TGB-Seq is for that reason. This weakens the paper's central framing.

### Minor

2. **Feature usage in experiments is not reported.** The paper specifies that the toy dataset has no features, but for the real TGB-Seq datasets it never states whether node/edge features (e.g., rating scores for ML-20M, review content for Yelp, patent classifications for Patent) are used, how they are encoded, or whether they are omitted. Since several temporal GNNs can consume features, this reporting gap makes experimental results harder to interpret and reproduce. An ablation showing performance with and without features on at least one dataset would clarify whether the observed difficulties are architectural or stem from missing feature information.

3. **No repeated-edge statistics for TGB-Seq datasets.** The paper states that "Only Yelp and Taobao contain a small number of repeated edges" but provides no quantitative statistics (e.g., fraction of edges that are repeated). These statistics are directly relevant to the paper's motivation and would help readers interpret how much of the performance gap is attributable to reduced memorization opportunities.

4. **Limited analysis of cross-dataset performance variation.** The paper reports large performance swings (e.g., GraphMixer at 72.56% MRR on Yelp vs. 17.12% on Patent) and different method rankings across TGB-Seq datasets, but attributes this broadly to "inability to capture sequential dynamics." Deeper analysis — correlating performance with measurable dataset properties (size, density, degree distribution, temporal burstiness) — would provide more actionable insights for the community.

### Trivial
None.

## Nice-to-Haves

- Add a simple sequence-based baseline (e.g., a Transformer on each node's sorted interaction history, ignoring timestamps) and a bag-of-interactions baseline to calibrate how much performance comes from order information vs. other factors. This would directly address the validation gap in the major weakness.
- Ablate specific architectural components (memory vs. pure aggregation, higher-order neighborhoods) on at least one real TGB-Seq dataset, extending the toy-example analysis to realistic settings.
- Report repeated-edge statistics (fraction of edges that are repeated) for each TGB-Seq dataset.
- Report MRR with k=20 (following TGB) alongside k=100 to facilitate comparison with prior work.

## Removed Points

- **Criticism that the SGNN-HN comparison is inappropriate and undermines the benchmark's framing** (Harsh Critic, Critical Issue 1). The paper acknowledges (Section 2, "Repeat and Exploration Behaviors") that recommendation methods "are tailored for bipartite graphs without features or interaction timestamps, whereas temporal GNNs often focus on general graphs." SGNN-HN is included as a reference to show what a sequential-order-aware method can achieve — an asymmetry that favors the baseline, not the authors' contribution. Per the hard rule that removes complaints about asymmetric comparisons when the asymmetry favors the baseline, this criticism is removed.

- **Criticism about the negative sampling strategy not being justified.** The paper explicitly justifies its choice (Section 3.1, paragraph on Negative Sampling Strategies): "historical edges are not likely to reoccur again in the future time" in TGB-Seq, making random negative sampling appropriate.

- **Criticism that the toy example is limited because it assumes identical timestamps, no features, and mirrored neighborhoods.** These are intentional design choices to isolate the sequential dynamics variable. The paper also acknowledges that higher-order neighborhoods (CAWN with walk length 3) can resolve the issue (end of Section 3.2), which the critic omits.

- **Criticism about performance variation lacking any explanation** (kept in weakened form as Minor weakness #4 — the paper does provide some discussion of ranking inversion but lacks deeper analysis).

## Novel Insights

None beyond the paper's own contributions. The reviews raise reasonable concerns about validation and reporting completeness but do not surface a fundamentally new perspective on temporal GNN failure modes beyond what the paper itself articulates.

## Suggestions

1. **Validate the sequential-dynamics claim directly.** On 2–3 TGB-Seq datasets, compare a temporal GNN to (a) a sequence-aware model (e.g., Transformer on interaction sequences, ignoring timestamps and graph structure) and (b) a bag-of-interactions model (ignoring order). If (a) significantly outperforms both (b) and the temporal GNNs, the claim is supported. If not, reframe the benchmark as testing "generalization to unseen edges in low-repeated-edge settings" rather than specifically sequential dynamics.

2. **Report feature usage explicitly.** For each dataset, state whether features exist and are used, and describe how they are encoded. Consider an ablation showing performance with and without features on one dataset.

3. **Add repeated-edge statistics.** Provide the fraction of repeated edges (identical source-destination pairs at different timestamps) for each TGB-Seq dataset.

4. **Deepen performance-variation analysis.** Investigate whether performance differences across datasets correlate with measurable properties (graph density, degree distribution, temporal burstiness) to give the community more actionable guidance.

## Score and Decision

This paper makes a genuine contribution: it identifies a real and overlooked weakness in temporal GNN evaluation (repeated-edge memorization bias), provides a clean existence proof, and constructs diverse large-scale datasets that fill a gap in the benchmarking ecosystem. The major weakness — lack of validation that the datasets test *sequential dynamics* specifically rather than other forms of difficulty — is significant but does not invalidate the benchmark's utility. TGB-Seq is a valuable resource regardless; the paper merely overstates the precision of what it tests. With stronger validation (control experiments showing order matters on real data) and more thorough reporting (features, repeated-edge statistics), this would be a strong contribution. As presented, it is a solid paper with a useful contribution and a clear path for improvement.

**Score**: 6.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>