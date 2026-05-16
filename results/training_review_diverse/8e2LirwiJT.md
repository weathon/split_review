Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the consolidated review.

## Summary

This paper identifies that existing temporal graph benchmarks are dominated by repeated edges, which allows temporal GNNs to succeed through memorization rather than learning genuine sequential dynamics. To address this, the authors introduce TGB-Seq, a collection of eight datasets (four bipartite recommendation networks and four non-bipartite social/citation/web networks) curated to minimize repeated edges and challenge models to generalize to unseen edges. The paper evaluates nine temporal GNNs plus one sequential recommendation method, showing that existing methods underperform on TGB-Seq relative to their results on standard benchmarks, and provides training cost analysis.

## Strengths

- **Controlled demonstration of failure on a simple sequential pattern**: Table 1 shows that six temporal GNNs (JODIE, DyRep, TGAT, TGN, CAWN, GraphMixer, plus others) all achieve approximately 50% AP on a carefully constructed synthetic dataset where the correct next item is deterministic given the interaction history. This clean experiment provides a striking motivation for the paper's central concern.

- **Quantification of the repeated-edge bias in existing benchmarks**: Figure 2 compares MRR on repeated vs. unseen edges across four established datasets (Wikipedia, Reddit, Social Evo., Enron), revealing gaps up to eightfold. This concrete evidence directly supports the claim that existing benchmarks reward memorization over generalization.

- **Construction of a benchmark targeting an underevaluated capability**: The TGB-Seq datasets are curated to minimize repeated edges, with the paper stating that six of eight datasets have ~0% repeated edges. This design directly addresses the identified limitation and provides a testbed focused on sequential-dynamics learning. The inclusion of both bipartite recommendation networks and non-bipartite social/citation/web networks offers domain diversity.

- **Comprehensive evaluation revealing systematic performance degradation**: Tables 3 and 4 show that all evaluated temporal GNNs suffer large MRR drops on TGB-Seq compared to their performance on existing benchmarks, and are consistently outperformed by the sequential recommendation method SGNN-HN on the recommendation datasets. The evaluation uses a unified framework (DyGLib), consistent hyperparameter tuning, and three random seeds.

- **Training cost analysis on varying dataset scales**: Figure 5 reports per-epoch training times across datasets from 1.87M to 18.7M edges, identifying that memory-based methods (JODIE, DyRep, TGN) cannot complete one epoch within 24 hours on the larger datasets, revealing a practical efficiency bottleneck.

## Weaknesses

### Fatal

None.

### Major

- **The paper does not quantify repeated-edge rates for any dataset.** The paper's entire motivation rests on the claim that existing benchmarks contain "excessive repeated edges" while TGB-Seq "minimizes repeated edges." Yet no statistics are reported — not for existing benchmarks and not for TGB-Seq. The paper states that "only Yelp and Taobao contain a small number of repeated edges" but never says what that number is. Without this quantification, readers cannot assess (a) how "excessive" existing benchmarks actually are, (b) how well TGB-Seq achieves its central design goal, or (c) whether performance differences across datasets correlate with repeat rates. For a benchmark paper, this is a significant omission that weakens the connection between the paper's motivation and its main contribution.

- **The claim of "complex sequential dynamics" is asserted, not demonstrated, for the non-bipartite datasets.** The paper states that the TGB-Seq datasets "exhibit complex sequential dynamics" as a defining feature. However, there is no measurement or analysis of sequential structure — no next-item prediction accuracy for simple sequential baselines, no sequential correlation metrics (e.g., conditional entropy, Markov order), and no justification that datasets like Patent (citation network) and WikiLink (web link network) involve sequential dynamics in the sense meant for recommendation (a user's consumption journey). Patent citations have temporal order but may reflect topical or author-based patterns rather than a "user-level" sequential exploration. While the recommendation datasets (ML-20M, Taobao, Yelp, GoogleLocal) plausibly involve sequential user behavior, the non-bipartite datasets' claim to "complex sequential dynamics" is unsubstantiated. The paper groups these datasets together based on domain intuition rather than empirical verification, which weakens the coherence of the benchmark's stated purpose.

### Minor

- **The toy example lacks a positive control.** The paper claims that temporal GNNs "cannot learn simple sequential dynamics" based on a synthetic dataset where all evaluated temporal GNNs achieve ~50% AP (Table 1). However, the paper does not report whether SGNN-HN (which was evaluated on this toy per the text) or any simple non-GNN baseline (e.g., a Markov model on the user's history) can solve this task. If no baseline succeeds, the toy may be ill-posed (identical timestamps across groups, no distinguishing features) rather than revealing a specific failure of temporal GNN architecture. A positive control would significantly strengthen the paper's central narrative.

- **No limitations section.** The paper does not discuss its own scope constraints: (a) the cold-start filtering (degree ≥ 3) removes a realistic challenge, (b) several datasets lack node features, which affects model comparisons, and (c) the concept of "sequential dynamics" may not be uniformly meaningful across all eight datasets (particularly Patent and WikiLink).

- **Evaluation protocol for Wikipedia/Reddit comparison datasets not contextualized.** The paper uses k=100 random negatives for all datasets, including Wikipedia and Reddit. Prior work on these datasets often used different k and negative sampling strategies (e.g., historical negatives). The paper should explicitly note that the reported Wikipedia/Reddit MRR values in Tables 3 and 4 use the paper's own protocol and are not directly comparable to numbers reported under different settings in the literature.

### Trivial

- **Hyperparameter search ranges not reported.** The paper states that "a grid search is performed to tune the hyper-parameters" but does not provide the ranges searched or the best configuration per method. While code availability partially addresses this, a summary table would aid reproducibility.

- **Variance reporting could be stronger for a benchmark.** Standard deviations across three runs are reported, which is standard practice, but pairwise significance tests (e.g., Wilcoxon) across datasets would help determine whether performance differences between methods are reliable.

## Nice-to-Haves

- Include a simple sequential baseline (e.g., first-order Markov model using the last item in a user's history) to quantify how much sequential signal exists in each TGB-Seq dataset and establish a lower bound for what a weak sequential model can achieve.
- Include additional sequential recommendation methods (e.g., SASRec, GRU4Rec) adapted to link prediction on the non-bipartite datasets to strengthen the evidence that sequential methods outperform temporal GNNs more broadly.
- Provide a justification for the choice of k=100 random negatives, including discussion of whether historical negatives would change the conclusions.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that "SGNN-HN is not reported on the toy"**: The paper explicitly states "We use the AP metric to evaluate nine temporal GNNs and SGNN-HN" on the toy (line 70). SGNN-HN is listed as evaluated, and the critic's assertion that it "does not report its performance on the toy" is incorrect. However, the broader point that the paper does not comment on SGNN-HN's toy result and lacks a positive control is retained as a Minor weakness.
- **Harsh critic's claim that "the paper does not discuss statistical significance or variance across runs beyond reporting standard deviations" framed as a major gap**: Standard deviation across 3 runs is standard practice for this type of work. Demanding confidence intervals or significance tests goes beyond what is typical for benchmark evaluations. This is downgraded to a Trivial point.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective that the paper itself does not already articulate.

## Suggestions

1. **Add a dedicated table quantifying repeated-edge rates** for every dataset discussed — both existing benchmarks (Wikipedia, Reddit, Social Evo., Enron) and all TGB-Seq datasets. Report the proportion of repeated edges in training, validation, and test sets. This is the single most impactful improvement the paper could make, as it directly substantiates the paper's core motivation and design goal.

2. **Add a positive control to the toy experiment** — show that at least one simple baseline (e.g., a 1-layer LSTM on the user's history, or SGNN-HN) can solve the sequential prediction task, or if none can, redesign the toy (e.g., add slight timestamp jitter or node ID embeddings) to demonstrate the pattern is learnable.

3. **Provide a sequential structure analysis** — for each TGB-Seq dataset, compute a simple first-order Markov baseline (predict the next item based on the last item in the user's history) and report its MRR. This would ground the claim that the datasets contain meaningful sequential dynamics.

4. **Add a limitations section** acknowledging the scope constraints (cold-start filtering, missing node features, domain-dependent nature of sequential dynamics) and clarifying the evaluation protocol choices.

5. **Clarify in Tables 3 and 4** that the Wikipedia/Reddit results use k=100 random negatives under the same protocol as TGB-Seq, and explicitly note these are not directly comparable to numbers from prior work using different settings.

## Score and Decision

The paper identifies a genuine and important problem in temporal graph benchmarking: existing datasets are dominated by repeated edges, leading to inflated performance estimates and obscuring models' failure to generalize. The TGB-Seq benchmark, with eight real-world datasets and comprehensive evaluation of nine temporal GNNs, is a potentially valuable contribution that addresses a real community need. However, the paper's two most central claims — that existing benchmarks suffer from "excessive repeated edges" and that TGB-Seq datasets exhibit "complex sequential dynamics" — are asserted without the necessary quantitative evidence. The missing repeated-edge statistics and lack of sequential structure analysis are not minor oversights; they are the very data that would validate the benchmark's design rationale. The paper is on the right track and the fixes are well-scoped, but in its current form the evidence does not fully match the strength of the claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>