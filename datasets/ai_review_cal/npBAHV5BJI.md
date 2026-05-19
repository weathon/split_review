- Decision: Reject
- Avg Score: 7.00
- Scores: 8, 8, 6, 6
Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper identifies that Personalized PageRank (PPR)—a non-learnable, relation-agnostic heuristic—achieves near-SOTA performance on most existing inductive KGC datasets. Through empirical analysis, the authors trace this shortcut to the standard dataset construction procedure (2-hop neighborhood sampling), which inflates the shortest-path-distance gap between positive and negative test samples. They propose a graph-partitioning-based construction method to mitigate the shortcut, create new benchmarks from WN18RR, FB15k-237, CoDEx-M, and HetioNet, and benchmark several inductive KGC methods. The new datasets substantially reduce PPR's exploitability (78% average drop vs. old datasets) and cause most neural methods to underperform their old-dataset numbers.

## Strengths

1. **Identifies a real, previously undocumented shortcut in inductive KGC benchmarks.** The paper demonstrates concretely (Figure 1) that PPR—which ignores all relational information—achieves only 25–29% below supervised SOTA on existing inductive datasets. This is quantitatively grounded and poses a genuine validity concern for prior work.

2. **Establishes the root cause via systematic analysis.** The paper shows a strong correlation (Pearson = 0.87) between ΔSPD (difference in mean shortest-path distance of positive vs. negative test samples) and PPR performance (Figure 3), and traces the elevated ΔSPD to the 2-hop neighborhood sampling procedure (Figure 4). The synthetic study (Section 3.3) further demonstrates that the problem persists across a wide parameter range, supporting the claim that it is structural, not a tuning artifact.

3. **Proposes a mitigation strategy that demonstrably reduces the shortcut.** The partition-based construction (Section 4.1) yields datasets where PPR performance drops by 78% on average compared to old inductive datasets, and ΔSPD values more closely match transductive parents (Table 1). The new WN18RR (E) splits, for instance, bring PPR from 66.0 (old) down to 45.1 (close to the transductive parent's 46.2).

4. **Shows that removing the shortcut changes method evaluations materially.** Mean performance drops by 40.6% on WN18RR (E) and 9.5% on FB15k-237 (E,R) across methods (Table 4). This confirms that the old datasets inflated method performance and that the new splits present a genuinely harder test.

## Weaknesses

### Fatal
None.

### Major

1. **Dataset construction procedure is underspecified.** Section 4.1 states that Spectral Clustering or Louvain is used "as dependent on the dataset," but provides no criterion for choosing between them, no guidance on selecting the number of partitions k, and no concrete description of how partitions "display[ing] similar properties to the original graph" are identified (the cross-reference to Section 4.2 does not provide these details). This makes the procedure non-reproducible as described and leaves the method's robustness unexplored. The paper also does not report whether the resulting inference graphs are connected (graph partitioning creates internally dense but sparsely connected partitions, so inference graphs could be disconnected—a property that would affect method behavior independently of the shortcut).

2. **The CoDEx-M (E,R) case where the shortcut persists is not discussed.** Table 1 shows that for CoDEx-M (E,R), the new inductive PPR Hits@10 is *higher* than the transductive parent (13.2 vs. 9.0) and ΔSPD is *higher* (0.42 vs. 0.20). The paper highlights these values in blue as "closer to transductive," but there is no old-inductive comparison point, and both metrics moved in the wrong direction—the shortcut was not mitigated. The paper does not acknowledge or analyze this failure, which limits confidence in the generality of the proposed method.

3. **No controlled comparison of dataset statistics between old and new splits.** The paper reports that methods drop 40.6% on WN18RR (E) and 9.5% on FB15k-237 (E,R) on new vs. old datasets (Table 4), but does not report the train/inference graph sizes, entity counts, triple counts, densities, or degree distributions for either set. The synthetic study (Section 3.3, Figure 5) shows a clear tradeoff between graph size and PPR performance, so the measured drop could partially reflect differences in dataset size or density rather than shortcut removal alone. Without controlling for these factors (e.g., by subsampling old datasets to match new dataset sizes), the claim that "removing the shortcut has a large negative effect on performance" (Section 5.2) is not fully disentangled from confounding structural changes.

### Minor

1. **"Supervised SOTA" in Figure 1 is not disaggregated.** The paper compares PPR against "supervised SOTA" across 25 datasets but does not specify which method(s) achieved the SOTA numbers for each dataset or cite the source. While likely drawn from original papers, this makes it difficult for readers to verify or contextualize the gap.

2. **ULTRA is evaluated under 0-shot but compared to supervised methods without explicit paradigm caveat.** The paper correctly notes ULTRA is a foundation model, and the results are informative, but the SOTA comparison (Figure 6) mixes supervised and 0-shot paradigms without clearly stating that these address different problem settings.

3. **PPR sensitivity to the teleport parameter α is not explored.** The paper uses α=0.15 (stated explicitly on line 113) and illustrates its effect on walk weights, but does not test whether PPR's exploitability is robust to different α values. PPR behavior can shift substantially with α, and the claim that the shortcut is "structural" would be stronger if shown across a range of α.

4. **Computational cost of graph partitioning is not discussed.** Spectral clustering can have O(n³) cost; the paper does not address scalability to larger KGs or compare construction cost against the existing neighborhood-sampling approach.

### Trivial

- Table 1's blue-highlighting claim that new datasets are "more aligned with the transductive dataset than the older inductive datasets" is vacuously true for CoDEx-M (E,R) (no old dataset exists) but the coloring implies a meaningful comparison that isn't supported; the format should be clarified.

## Nice-to-Haves

- Include an oracle baseline using raw shortest-path distance as a predictor to directly verify that residual PPR performance on new datasets corresponds to genuine topological structure rather than remaining SPD artifacts.
- A qualitative case study (e.g., specific positive/negative samples where PPR succeeds/fails on old vs. new datasets) would help readers understand what the shortcut looks like in practice.
- Reporting the percentage of positive-test entity pairs that are disconnected in the inference graph would clarify whether the new datasets inadvertently create an overly sparse evaluation regime.

## Removed Points

These points are flagged to be removed; treat them with caution.

- "The new datasets are not validated as actually measuring inductive reasoning ability" — The paper's stated goal is to mitigate the PPR shortcut, not to positively validate that the new datasets measure "genuine inductive reasoning." The paper shows that (a) the shortcut is removed, (b) ΔSPD matches transductive parents, and (c) methods drop in performance. These constitute evidence that the new datasets correct the specific flaw identified. Demanding proof that they measure a broader construct ("inductive reasoning") goes beyond the paper's scope and is not standard for dataset-contribution papers.

- "Code release statement missing" — Parser artifact; the original submission likely contains this.

- "α is not stated explicitly" — α=0.15 is explicitly stated in Section 3.2 (line 113). The critic's claim otherwise is factually wrong.

- "Neural LP...unreliable results in averages without flagging them" — The paper does flag this: "Neural LP sometimes fails to converge, resulting in a near zero performance and thus causing the model to have a high performance variance" (Section 5.2). The criticism misreads the paper.

- "No statistical testing is performed" — Standard deviations are reported for all methods, which is standard for this field. Requesting additional statistical tests (e.g., t-tests) is a format nitpick.

- "Missing related works" — Not permitted per policy; no external source confirms existence.

- Various formatting/style nitpicks (parser artifacts).

The Strength Finder's generic strengths ("addressed an important problem," "targeted an interesting question") are removed—they are not specific to this paper's evidence.

## Novel Insights

The most interesting cross-perspective insight is that the harsh critic and the strength finder largely agree on the paper's central finding (PPR shortcut is real and important) but diverge sharply on whether the proposed mitigation is validated. The strength finder sees the 78% PPR reduction and the 40.6% method-performance drop as compelling evidence that the new datasets are an improvement. The harsh critic sees the same numbers as potentially confounded by size/density shifts and the underspecified construction procedure. This tension points to a concrete path forward: the paper needs (a) controlled dataset-size ablation and (b) a fully specified construction protocol. Neither reviewer disputes the paper's core diagnostic contribution; the debate is about whether the *solution* is adequately validated.

## Suggestions

1. **Add a table comparing dataset statistics** (|V|, |R|, |E|, average degree, % disconnected positive test pairs, train/inference graph sizes) for old vs. new splits on a per-inference-graph basis. This would directly address the confounding criticism.
2. **Fully specify the partition selection procedure**: state the criterion for choosing Spectral Clustering vs. Louvain, how k is selected, and what "similar properties to the original graph" means operationally (e.g., "we select partitions whose ΔSPD falls within [range] of the transductive parent").
3. **Acknowledge and analyze the CoDEx-M (E,R) case** where PPR increased. Explain why this happened and whether the method generalizes.
4. **Run an ablation controlling for dataset size**: subsample the old WN18RR (E) inductive datasets to match the new dataset's size and re-measure PPR and method performance. This would cleanly separate the effect of shortcut removal from size effects.
5. **Clarify which specific methods/checkpoints constitute "supervised SOTA"** for each dataset in Figure 1, either in a supplementary table or in the figure caption.
