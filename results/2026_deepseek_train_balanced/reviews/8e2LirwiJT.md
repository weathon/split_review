## Summary

This paper diagnoses a critical blind spot in temporal graph benchmarks: existing datasets are dominated by repeated edges, allowing temporal GNNs to succeed via memorization rather than learning the sequential dynamics that drive real-world applications. The authors introduce TGB-Seq, eight large-scale temporal graph datasets (1.87M–18.7M edges, six with 0% repeated edges) spanning e-commerce, movie ratings, business reviews, social networks, citations, and web links. A controlled toy experiment (Section 3.2) shows that nine temporal GNNs score at chance (50% AP) on a simple sequential pattern that a sequential-recommendation method (SGNN-HN) solves, and the paper traces this failure to specific architectural components. Comprehensive evaluation reveals that no method dominates across datasets, and training costs scale prohibitively for memory-based architectures.

## Strengths

- **Controlled toy experiment isolates an architectural failure mode (Section 3.2, Table 1).** The paper constructs a synthetic dataset where nodes have no features, timestamps are identical, and one-hop neighborhoods are isomorphic—stripping away all confounding factors. Nine temporal GNNs score ~50% AP (chance), while SGNN-HN succeeds. This is stronger evidence than merely observing poor real-data performance: it proves the failure is architectural, not data-driven. Prior benchmarks (TGB, BenchTeMP) do not include controlled diagnostic datasets of this kind.

- **Mechanism-level diagnosis explains *why* memory and aggregation modules fail (Equations 1–3, lines 76–102).** The paper traces failure through each component: the memory module (Eq. 1) produces identical memories for items i₄ and i₉ because they co-occur with their user groups at the same timestamps; the aggregation module (Eq. 2) collapses because one-hop neighborhoods mirror each other; DyGFormer's common-neighbor computation (Eq. 3) fails due to zero overlap, and CAWN's random walks also fail because neighborhoods are symmetric. This diagnostic reasoning goes beyond standard benchmarking by identifying specific architectural assumptions that break down on sequential dynamics.

- **Large-scale, diverse datasets deliberately curated to minimize repeated edges (Section 4, Table 2, Figure 4).** TGB-Seq includes eight real-world datasets (1.87M–18.7M edges) from diverse domains, with six achieving 0% repeated edges. The curation directly addresses the problem documented in Figure 2 (eightfold gap between historical and unseen edge performance on existing datasets). Power-law degree distributions (Figure 4) confirm these are genuine large-scale networks.

- **No single method dominates across TGB-Seq, validating multi-dimensional evaluation (Tables 3–4, lines 145–151).** Striking rank reversals occur: DyGFormer is best on Wikipedia but near-worst on GoogleLocal; GraphMixer best on ML-20M and Yelp but poor on Taobao where TCL leads; TGN best on GoogleLocal but far from best on Wikipedia/Reddit. This variability demonstrates that TGB-Seq assesses distinct capabilities rather than a single skill, unlike benchmarks where repeated-edge memorization dominates.

- **Training cost analysis (Section 5.2, Figure 5) and rigorous evaluation protocol (k=100 negative samples).** The paper measures per-epoch training time across dataset scales, showing that memory-based methods (JODIE, DyRep, TGN) only complete training on the smallest dataset. Using 100 negative samples (vs. k=20 in TGB) provides a more robust ranking signal.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions—the datasets, the diagnostic toy experiment, and the comprehensive evaluation—are valid and useful. The issues below concern framing and supporting evidence, not fundamental flaws.

### Minor
- **Overclaiming in the "inherently incapable" characterization (abstract, line 7).** The toy experiment shows that nine temporal GNNs fail on a *specific* degenerate setup where nodes have no features, timestamps are identical, and neighborhoods are isomorphic. The paper's repeated characterization—"inherently incapable of learning simple sequential dynamics"—is broader than what the evidence supports. The experiment does not test whether these methods could capture sequential dynamics when *any* distinguishing signal (node features, edge features, temporal offsets, differentiated neighbor identities) is available. The claim should be scoped to the specific architectural limitations revealed under these controlled degenerate conditions. Softening this language would make the paper more precise without weakening its contribution.

- **The specific link between TGB-Seq difficulty and "sequential dynamics" is asserted more strongly than demonstrated.** The paper's central thesis is that TGB-Seq tests "complex sequential dynamics." The evaluation protocol is standard future link prediction with MRR on datasets curated to minimize repeated edges. While the toy experiment directly tests sequential patterns, and the real-world datasets are drawn from domains where sequential dynamics are plausible, the paper does not provide evidence that the performance degradation on TGB-Seq is *specifically* caused by the absence of sequential-dynamics-capturing capability rather than by other factors (e.g., larger scale, higher sparsity, the general difficulty of predicting unseen edges). A direct probe—such as measuring whether shuffling interaction order degrades performance—would substantially strengthen this link. Without such analysis, the benchmark is better characterized as "a benchmark for generalization to unseen edges in diverse, large-scale temporal graphs" alongside the sequential-dynamics framing.

- **Missing explicit, quantitative comparison of repeated-edge proportions across existing datasets and TGB-Seq.** The paper's motivating premise is that existing datasets contain "excessive repeated edges" compared to TGB-Seq. While the paper states that 6 of 8 TGB-Seq datasets have 0% repeated edges (line 33) and Figure 2 shows the historical-vs-unseen performance gap on existing datasets, it never reports the actual proportion of repeated edges in Wikipedia, Reddit, Social Evo., Enron versus TGB-Seq datasets in a single comparable table. Adding this quantitative comparison would make the core motivation verifiable at a glance and strengthen the paper's framing.

### Trivial
- **No limitations or future work section.** The paper ends with a standard summary conclusion. A limitations section discussing scope (e.g., no node/edge features in most datasets, single-metric evaluation, focus on continuous-time graphs) would improve completeness and help guide future work.

## Nice-to-Haves

- **Sequence-shuffling ablation.** The single most convincing addition would be an experiment that compares models' performance on chronologically ordered vs. shuffled interaction sequences. If MRR drops substantially when sequence order is preserved, this would directly demonstrate that sequential dynamics matter for TGB-Seq.
- **Statistical significance testing beyond standard deviation**, given the variance visible across three runs.
- **Characterization of sequential patterns per dataset** (e.g., average sequence length per node, temporal autocorrelation, transition statistics) to help researchers understand what specific challenges each dataset poses.
- **Systematic analysis of when EdgeBank works vs. fails**, to more precisely isolate the effect of repeated edges.

## Removed Points

These points were identified by the reviewers but are removed after verification against the paper:

- **"Discussion of higher-order neighbors (lines 104–105) is truncated."** — This is a PDF parser artifact, not an author error. Removed per rule.
- **"SGNN-HN comparison is apples-to-oranges."** — The paper explicitly acknowledges this architectural difference in the Related Work section. Removed as the paper already addresses it.
- **Criticisms about missing appendix content or reproducibility details.** — The parser strips appendices; these exist in the original submission. Removed per rule.
- **Generic concerns about "could the metric be measuring a proxy" without specific evidence in the paper.** — Removed as speculation rather than identified problems.

## Novel Insights

None beyond the paper's own contributions. However, one observation that emerges from synthesizing the reviews is worth noting: the paper's toy experiment and real-data evaluation together reveal an interesting tension. The toy experiment proves that *some* temporal GNN architectures cannot exploit sequential patterns when node features are absent, yet GraphMixer—one of the simplest methods—achieves top performance on ML-20M and Yelp among temporal GNNs. This suggests two possibilities that the paper does not explore: either these datasets do not require deep sequential modeling, or the features and structure present in the real data compensate for architectural limitations that appear in the featureless toy setup. Resolving this tension would make the paper's diagnostic story more complete.

## Suggestions

1. **Narrow the "inherently incapable" language** to describe the specific architectural limitations revealed under the controlled degenerate conditions, rather than asserting a universal incapability.
2. **Add an explicit table** comparing repeated-edge proportions across existing datasets (Wikipedia, Reddit, Social Evo., Enron) and all TGB-Seq datasets.
3. **Either add a sequence-shuffling experiment** to directly link TGB-Seq's difficulty to sequential dynamics, *or* reframe the paper's central contribution as "a benchmark for generalization to unseen edges in diverse, large-scale temporal graphs" with the sequential-dynamics framing as a secondary narrative supported by the toy experiment.
4. **Add a limitations section** to the final manuscript.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>