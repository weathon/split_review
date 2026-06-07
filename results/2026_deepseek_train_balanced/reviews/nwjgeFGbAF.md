## Summary

BCG is a dataset of ~10K function call graphs (FCGs) from Android APKs dated 2017–2023, intended to address two problems in existing FCG malware benchmarks: obsolete samples and duplicate APKs from repackaging. The paper provides concrete measurements of duplicate inflation in prior datasets (40–51%) and shows that removing duplicates drops classification performance by up to 16%. It then demonstrates that state-of-the-art GNNs perform near-chance (macro-F1 < 3% for family classification) on BCG, arguing the dataset is a harder, more realistic benchmark.

## Strengths

- **Quantifies duplicate extent in existing datasets with specific, measured percentages.** Section 4.3 reports that MalNet-Tiny contains ~40% duplicates (~2,000 APKs), CICMalDroid contains 41%, and a 100K-sample subset of MalNet shows ~51% duplication. These are concrete measurements on named datasets, providing direct evidence for a known but previously unquantified problem.

- **Demonstrates the inflationary effect of duplicates through controlled removal experiments.** Section 4.3 and Figure 3 show that removing duplicates from MalNet-Tiny and CICMalDroid causes a consistent drop in macro-F1 across all classifiers tested, with the largest decrease being 16.38% on CICMalDroid using GIN. This is direct experimental evidence — not just theoretical argument — that duplicate APKs inflate reported classification performance.

- **Shows that SOTA methods achieve near-trivial performance on BCG, establishing it as a genuinely harder benchmark.** Tables 4–5 report that on BCG, GraphSAGE achieves macro-F1 < 1% for family classification and GIN achieves 2.83%, while the same methods perform substantially better on existing datasets. This empirically validates the claim that malware classification on recent, deduplicated FCGs is more complex than prior benchmarks suggest.

- **Includes non-graph APK features absent from prior FCG datasets.** Table 3 enumerates extracted features (APK size, DEX size, permissions, activities, services, broadcast receivers). Prior datasets like MalNet, Drebin, and CICMalDroid lack these features, adding practical value for researchers wanting to combine graph and non-graph signals.

## Weaknesses

### Major

- **Temporal-split experiments central to justifying the dataset's recency focus are described without any quantitative results.** Section 5.2 describes two temporal experiments — one using a temporal train/test split, another splitting BCG into two temporal halves (2017–June 2021 vs. July 2021–2023) evaluated independently — but provides **no numbers, tables, figures, or confidence intervals**. The paper states "These findings collectively suggest that malware classification becomes increasingly challenging for more recent APKs" without showing any supporting data. This is a core evidential claim for why BCG's recency matters, and it is entirely unsupported in the text. The reader cannot evaluate whether the effect is real, large, or statistically significant.

- **The duplicate-detection methodology is too coarse to fully support the "unique APKs" claim.** Section 3, Step 6 identifies duplicates by exact matching on six aggregate graph statistics (number of nodes, number of edges, average degree, in-degree centrality, size of largest connected component, size of largest weakly connected component). Two genuinely different FCGs can share these summary statistics, and repackaged malware with minor structural changes (renamed methods, dead code insertion, instruction reordering) would produce FCGs that differ by a few nodes/edges and evade this filter. The paper acknowledges this ("no false positives but there may well remain false negatives") but proceeds to claim the dataset contains "unique APKs" and treats the filtered set as de-duplicated. The actual uniqueness of BCG is therefore unknown, and the reported 40–51% duplication rates in existing datasets are likely *underestimates*. This weakens one of the paper's two primary selling points. (The acknowledgment is honest but does not resolve the gap for the current claim.)

### Minor

- **The non-graph APK features use t-SNE for dimensionality reduction in a methodologically questionable way.** Section 4.4 encodes textual features with a 100-dimensional TensorFlow sentence encoder, then reduces to **2 dimensions** using t-SNE. t-SNE is stochastic, preserves neither distances nor global structure, and is designed for visualization rather than producing feature vectors for downstream classification. Reducing from 100-d to 2-d discards nearly all signal. The paper cites prior malware studies using t-SNE (Yumlembam et al., 2022; Zhu et al., 2018) but this is not standard practice for generating classification features. The utility of the provided APK features is uncertain.

- **No benign/malware split is reported for BCG.** The paper does not state how many of the 9,938 graphs are benign vs. malware — a basic descriptive statistic for any malware dataset. Table 2 (an image) likely provides per-type breakdowns, but the overall class balance is absent from the text, making it harder to assess whether the low macro-F1 scores are due to genuine difficulty or extreme imbalance.

- **No exact VirusTotal agreement threshold is specified.** Section 3, Step 3 says "we only consider the APKs flagged by multiple antivirus engines" but does not state the precise threshold (e.g., at least 5 out of 70+ engines, or 10, or a simple majority). This is a missing detail for reproducibility of the label construction pipeline.

- **No analysis of what makes BCG hard.** The paper reports that SOTA methods perform near-chance on BCG but offers no follow-up — no visualization of the graph embedding space, no confusion matrices, no examination of which families are confused, no investigation of label noise or class imbalance. The near-chance performance could indicate genuine difficulty or data quality issues, and the paper does not distinguish these.

### Trivial

None that survive filtering (parser artifacts excluded per guidelines).

## Nice-to-Haves

- A two-stage duplicate detection approach (coarse filter with aggregate statistics, then graph hashing or Weisfeiler-Lehman kernel on candidate matches) would strengthen the uniqueness claim substantially.
- Comparison of BCG against de-duplicated versions of existing datasets (MT*, CMD*) on a like-for-like basis to isolate whether BCG's difficulty comes from recency or simply from having fewer duplicates.
- An analysis of class balance (per-family sample counts) and its relationship to the low macro-F1 scores.
- Providing the full 100-dimensional sentence embeddings alongside (or instead of) the 2-d t-SNE features to give users flexibility.

## Removed Points

The following points from the inputs were removed per review guidelines:

- **Dataset URL concern (Harsh Critic Point 4):** Removed per Hard Rules — criticisms questioning the existence, release status, or availability of a cited resource must be removed. The paper cites `https://iclr.me/` and the hard rules treat all cited resources as existing.
- **Dataset size comparison (Harsh Critic Point 5 — "too small"):** Removed as a weakness. The criticism that BCG is "an order of magnitude smaller" than MalNet ignores the paper's explicit rationale: the claim is about *quality* (unique, recent, large FCGs), not raw count. BCG's average graph size (25K nodes, 54K edges) is substantially larger than typical FCGs in other datasets. The filtering rationale is clearly stated and defensible.
- **Missing comparison with de-duplicated existing datasets (Harsh Critic):** Removed as factually incorrect. Table 4 explicitly includes MT* and CMD* (de-duplicated versions of MalNet-Tiny and CICMalDroid) and compares them with BCG directly.
- **Strength Finder's temporal-split claim:** Removed as a strength because the temporal experiments are described but no quantitative results are provided. Describing an experiment without reporting results does not constitute evidence.
- **Generic "important problem" framing in Strength Finder:** Removed per filtering rules — generic statements about the importance of the problem without specific evidence are not retained as strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews identify useful critiques but do not surface a novel perspective that the paper itself misses.

## Suggestions

1. **Provide quantitative results for the temporal experiments.** This is the most critical fix — the paper's claim about recency as a source of difficulty directly depends on these experiments, and the absence of numbers is a glaring evidential gap.
2. **Strengthen duplicate detection or be more precise about what "unique" means.** If exact graph hashing is infeasible, at minimum clarify in the abstract and introduction that BCG removes exact FCG duplicates based on graph statistics — not that all APKs are guaranteed unique.
3. **Provide the full 100-d sentence embeddings alongside or instead of the 2-d t-SNE features.** If t-SNE is retained, add a clear caveat about its stochastic nature and suitability for downstream classification.
4. **Report the benign/malware split and per-family sample counts** in the main text.
5. **Specify the exact VirusTotal multi-engine threshold** used for label construction.
6. **Add an error analysis section** examining what drives BCG's difficulty — e.g., t-SNE/UMAP of graph embeddings, confusion matrices, or class imbalance statistics.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>