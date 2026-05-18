Now I have all the information needed. Let me compile the final review.

---

## Summary

This paper identifies that existing temporal graph benchmarks are dominated by repeated edges, which allows temporal GNNs to achieve inflated performance through memorization rather than learning sequential dynamics. To address this, the authors introduce TGB-Seq, a collection of eight large-scale datasets (four bipartite recommendation datasets and four non-bipartite social/citation/web link networks) carefully curated to minimize repeated edges. Through a controlled toy experiment, they demonstrate that nine existing temporal GNNs achieve only ~50% AP on simple sequential patterns, and on the real-world TGB-Seq benchmarks, methods that excel on Wikipedia/Reddit (e.g., DyGFormer at ≥95% MRR) drop below 50% MRR. The paper provides a valuable diagnostic tool for the community.

## Strengths

- **Controlled toy experiment proves the core thesis directly.** The synthetic dataset (Figure 3, Table 1) isolates the failure: all nine temporal GNNs achieve AP ≈ 50% (random guessing) on a simple two-group sequential pattern. This is the strongest form of evidence for the paper's central claim — it is not correlational but causal, and it cleanly separates the model deficiency from dataset noise.

- **Empirical evidence that existing benchmarks inflate performance via repeated edges.** Figure 2 decomposes MRR into repeated vs. unseen edges across four established datasets, showing up to an 8× gap. This quantifies the problem and justifies the need for a benchmark that minimizes repetitions.

- **Large-scale, multi-domain benchmark covering realistic applications.** The eight datasets span e-commerce, business reviews, social networks ("Who-To-Follow"), movie ratings, patent citations, and web link networks, ranging from 1.87M to 68.8M edges. The datasets exhibit power-law degree distributions and low density — realistic properties that prior benchmarks often lack.

- **Consistent and dramatic performance degradation across all temporal GNNs.** Tables 3 and 4 show that every tested method suffers a large drop on TGB-Seq compared to Wikipedia/Reddit. The pattern is robust across 9 methods, 8 datasets, and 3 random seeds, supporting the claim that TGB-Seq exposes a real blind spot.

- **Comprehensive evaluation protocol.** Using MRR with 100 negative samples (more challenging than TGB's 20) and reporting standard deviations over 3 runs provides reliable comparisons. The negative sampling strategy (random from all nodes) is correctly justified by the no-repetition design goal.

- **Training cost analysis revealing practical barriers.** Figure 5 shows that memory-based methods (JODIE, DyRep, TGN) cannot complete one epoch on larger TGB-Seq datasets within 24 hours, highlighting that the benchmark imposes realistic efficiency constraints alongside accuracy demands.

## Weaknesses

### Fatal
None.

### Major

- **Missing edge repetition statistics for TGB-Seq datasets.** The paper's core design rationale is that TGB-Seq datasets are "carefully curated to minimize repeated edges" (line 33), with the claim that only Yelp and Taobao "contain a small number of repeated edges." Yet no quantitative statistics — percentages or counts of repeated (source, destination) pairs — are reported for any TGB-Seq dataset, nor for the existing benchmarks (Wikipedia, Reddit) used in the comparison. Since the entire benchmark is motivated by the need to escape repetition-dominated evaluation, the absence of this basic diagnostic undermines the reader's ability to verify the benchmark's central property. *This is fixable and does not invalidate the results, but a benchmark paper must report this statistic to be credible.* The paper does provide the key evidence indirectly — the dramatic performance gap between repeated and unseen edges on existing datasets (Figure 2), and the uniformly low performance on TGB-Seq — but direct repetition rates are needed.

### Minor

- **"Complex sequential dynamics" is not explicitly validated for the non-bipartite datasets.** For the four recommendation (bipartite) datasets, the notion of sequential dynamics is intuitive (a user's click/rating sequence predicts the next item). For Patent (citation network) and WikiLink (web link network), the paper asserts they "inherently exhibit complex sequential dynamics" (line 33) but offers no concrete analysis — e.g., transition probability analysis, sequence predictability baselines, or even one illustrative example of what a "sequential dynamic" looks like in a citation or web link context. The Flickr and YouTube "Who-To-Follow" datasets fall in a middle ground where some intuition exists (users follow accounts in sequence), but even there the paper provides no characterization. This does not undermine the benchmark's value — the datasets are still useful for temporal link prediction and the results speak for themselves — but it makes the paper's framing less precise and the choice of these datasets less motivated than it could be.

- **The negative sampling protocol could be clearer for the Wikipedia/Reddit comparisons.** The paper correctly states that it uses random negatives from all nodes for TGB-Seq datasets (Section 3.1, line 56). It also notes in the Observations section that the same 100-random-negative protocol was used for Figure 1 and Figure 2. However, Table 3 includes results on Wikipedia and Reddit alongside TGB-Seq datasets, and it is not explicitly stated in the table caption or surrounding text whether those results use the same random-negative protocol. Given that TGB uses historical negatives with k=20, a clarification would prevent confusion about comparability.

- **SGNN-HN baseline positioning.** SGNN-HN (a sequential recommendation method, not a temporal GNN) is included in Table 3 (bipartite datasets) to show that better performance on these datasets is achievable. This is useful and the paper correctly restricts it to bipartite datasets. However, the paper could more explicitly acknowledge that SGNN-HN operates under different assumptions (sequence-only, no graph structure, no timestamps as features) and is not applicable to non-bipartite datasets, to avoid giving the impression of an unfair comparison.

### Trivial

- The paper mentions a grid search on the validation set (line 131) but does not report search ranges or selected hyperparameters per method/dataset. While this is common in benchmark papers, providing the final hyperparameters would aid reproducibility.

## Nice-to-Haves

- Report edge repetition percentages (proportion of test edges whose source–destination pair appeared in training) for all TGB-Seq datasets and for the existing benchmarks used in comparison. Also report what fraction of test edges involve unseen source/destination nodes entirely, to clarify the generalization challenge.

- Include at least one simple sequence-only baseline (e.g., SASRec, BERT4Rec) on the bipartite datasets to further anchor how much performance a model with no graph structure or timestamps can achieve, strengthening the diagnosis that temporal GNNs are deficient in sequential modeling.

- Provide a brief analysis of sequential patterns in the non-bipartite datasets — e.g., train a simple next-item-prediction model on source histories and report its MRR. If it performs well, this confirms learnable sequential dynamics exist.

## Removed Points

- **Harsh critic's Point 2 (toy analysis ignores source node / analysis is incomplete):** The paper explicitly states (line 102) that the aggregation module "generate[s] the same embeddings for i₄ and i₉, as well as for {u_k} and {v_k}, respectively" — i.e., it *does* address source node embeddings and concludes they are also identical. The reviewer's specific claim that the analysis "ignores the source node" is factually incorrect. The broader concern about the phrase "inherently incapable" is a matter of rhetorical strength; the empirical evidence (9 models, 50% AP) firmly supports the claim, and the paper uses "might relate to" (line 76) to qualify its architectural explanation. This point is removed as a misreading.

- **Complaint about missing hyperparameter ranges (full removal):** The paper states a grid search was performed. While final hyperparameters would be welcome detail, the rules instruct removing nitpicks about undisclosed hyperparameters as a reproducibility concern of trivial weight. Moved here rather than left in Minor.

- **Various formatting, scope-creep, and taste-based suggestions** (e.g., asking the paper to add more models, expand to more domains, or change baselines to reviewer-preferred methods) are removed as not substantive.

## Novel Insights

The reviews converge on the paper's core contribution convincingly, but one meta-observation stands out: the combination of the controlled toy experiment (Table 1) and the large-scale real-world degradation (Tables 3–4) forms a *necessary and sufficient* diagnosis that is rare in benchmarking papers. The toy experiment proves *sufficiency* (sequential dynamics alone, in isolation, defeat current models), while the real-world results prove *necessity* (the effect persists and even amplifies when confounds like feature-richness and scale are added). This two-pronged evidential structure is stronger than what most benchmark papers provide and should be emphasized by the authors.

## Suggestions

1. **Report edge repetition statistics** as a column in Table 2 (or a supplementary table) to substantiate the core design claim. Include both the percentage of edges that are exact repeats of a prior (source, destination) pair and the percentage of test edges that are "new pairs" vs. "new nodes."

2. **Add a brief empirical characterization of sequential dynamics** for the non-bipartite datasets — even a simple analysis showing that a model using only the source node's interaction history can predict future edges above chance would suffice to validate the "sequential dynamics" framing for these datasets.

3. **Clarify in the caption of Table 3** that Wikipedia/Reddit results use the same 100-random-negative protocol, to avoid confusion with the TGB protocol.

4. **Soften or remove the phrase "inherently incapable"** from the abstract. The empirical evidence is strong, but the word "inherently" implies an impossibility proof the paper does not (and need not) provide. "Consistently fail to learn" or "are unable to capture" would be equally forceful and more precise.

5. **Report final hyperparameters per (method, dataset) pair** in a supplementary table to enhance reproducibility.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>