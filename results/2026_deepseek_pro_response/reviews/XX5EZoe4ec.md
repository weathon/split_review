Now I have a clear picture from the calibration. Let me synthesize.

**Round 1 bracket**: Our paper is clearly above the weak-band papers (2.0-3.0 range), and below the strong-band papers (7.5-8.0). It sits in the 5.0-7.0 range.

**Round 2 narrowing**: 

- **Semi-Parametric Retrieval (7.00, Accept)**: Cleaner core idea (binary bag-of-tokens index), more elegant contribution. Our paper has broader scope but a less crisp central idea. RetrievalFormer is weaker than this anchor.
- **BTR (6.50, Accept)**: Binary token representations for retrieval efficiency. Similar pattern of practical efficiency tradeoffs, some presentation issues. Comparable to our paper — BTR has a cleaner idea, our paper has broader evaluation and bigger claimed speedups.
- **Conservative Evidential Learning (6.25, Accept)**: RL-based recommendation, mixed reviews (8, 3, 6, 8). Our paper is clearly stronger — better motivated, cleaner experiments.
- **EHI (6.00, Reject)**: Joint embedding-index learning, missing baselines. Our paper has more comprehensive evaluation and clearer motivation. RetrievalFormer is slightly stronger.

**Final score**: Our paper is better than EHI (6.00) and Conservative Evidential (6.25), comparable to BTR (6.50), but clearly weaker than Semi-Parametric Retrieval (7.00). I place it at **6.0**.

The paper has genuine contributions (LOOC protocol, comprehensive dual-encoder evaluation, practical latency benchmarks) weighed down by a missing critical baseline class (dual-encoder baselines), ambiguous speedup reporting, and incomplete ablation accounting. These are substantial but addressable gaps.

---

## Summary

This paper proposes RetrievalFormer, a dual-encoder transformer architecture for sequential recommendation that replaces the ID-softmax output layer with dot-product retrieval, enabling ANN-based serving and zero-shot cold-item recommendation from item features. The user tower is a transformer over enriched interaction sequences; the item tower is a feature-based encoder using an AttentionFusion module (self-attention over heterogeneous feature embeddings). The paper evaluates on Amazon Beauty, Amazon Toys, and MovieLens-1M, reporting competitive accuracy against ID-softmax transformer baselines while achieving large inference speedups via ANN, and introduces a Leave-One-Out Cold (LOOC) protocol for rigorous cold-start evaluation.

## Strengths

- **Well-motivated problem with concrete, quantified evidence**: The paper clearly identifies and quantifies the O(Nd) softmax inference bottleneck in transformer sequential recommenders, grounding the motivation in concrete latency benchmarks (e.g., SASRec exceeding 50ms p90 at just 10K items). The two linked problems — inference cost and cold-start incapability — are correctly attributed to the ID-softmax formulation.

- **Rigorous cold-start evaluation protocol (LOOC)**: The Leave-One-Out Cold protocol (Section 4.4.1) ensures zero item-ID leakage by constructing a test set from items whose IDs never appear in training, then expanding to all users whose final interaction is with such items. This is a genuine methodological advance over standard LOO evaluation. The paper honestly reports 25–35% performance drops under LOOC and correctly notes ID-softmax baselines cannot function under this protocol — a crisp demonstration of RetrievalFormer's unique capability.

- **Comprehensive benchmarking against ID-softmax baselines**: Table 1 reports results against 11 prior models across three datasets and four metrics, using the identical protocol from Liu et al. (2025) for direct comparability. The paper is transparent about its accuracy position, openly acknowledging it achieves 86–91% of the strongest baselines' Recall@20 rather than inflating results.

- **Concrete latency-scaling experiment**: RQ4 (Section 4.5, Figure 2) benchmarks latency across four orders of catalog size (10K to 10M) with full ANN index configuration specified (FAISS IVF-PQ, n_list=4096, 64-dimensional PQ codes, n_probe=32, NVIDIA V100). The sub-linear vs. linear scaling behavior is clearly demonstrated.

- **Directional ablation evidence**: The ablation study (Section 4.3) quantifies attention fusion (+10.1% over mean pooling), shared embeddings (~3% on MovieLens), and InfoNCE uniformity (+4.1%), tying each design choice to a measured performance delta.

- **Real-world validation**: The email campaign result (AUC 0.7770 vs. 0.6854 for Content-based KNN, a 13.4% relative improvement) demonstrates transfer beyond curated academic benchmarks to a setting where every item is cold-start by nature.

## Weaknesses

### Major

- **Missing comparison against other dual-encoder or retrieval-based sequential models**: Every baseline in Table 1 is an ID-softmax model. The paper never compares against a simpler dual-encoder, two-tower, or contrastive-learning sequential recommender. The paper's contribution is a specific dual-encoder architecture, but without a simple dual-encoder baseline (e.g., item ID embeddings + transformer user tower + InfoNCE loss), we cannot fully assess how much the specific design choices — AttentionFusion, shared embeddings, two-stage interaction encoding — matter beyond the dual-encoder paradigm itself. The ablation study partially mitigates this (e.g., attention fusion over mean pooling shows +10.1%), but a cumulative component-ablation culminating in the full model is needed for proper attribution.

- **Ambiguous and inconsistent speedup reporting**: The 288× speedup is featured prominently in the abstract, introduction, and conclusion. However, the paper's own latency numbers are inconsistent: line 203 reports exhaustive scoring at 3.4ms (100K) and 29.5ms (1M), while Figure 2 / line 273 reports exhaustive scoring at 0.76ms (10K) scaling to 292ms (10M). The Figure 2 exhaustive numbers appear to match the SASRec CPU ETUDE benchmark data, yet the text claims the comparison is for "the same dual-encoder scoring function." It is unclear whether the 288× compares (a) dual-encoder exhaustive dot-product vs. dual-encoder ANN, or (b) SASRec full softmax vs. dual-encoder ANN. These are different comparisons with different implications for what drives the speedup (search method alone vs. architecture change + search method). The underlying data to disentangle this appears present but is reported confusingly, undermining the central efficiency claim's precision.

### Minor

- **Ablation numbers do not sum to final model performance**: On Amazon Toys, the full RetrievalFormer achieves Recall@20 of 0.1169 (Table 1), but the highest ablation variant reported reaches only 0.1064. The ~0.01 gap is unexplained, suggesting ablations were run under different hyperparameters or training configurations. This weakens the attribution of total performance to specific components.

- **Item features per dataset are not specified**: The paper emphasizes encoding from "heterogeneous features" but never lists which features are available or used per dataset (Amazon Beauty, Toys, MovieLens-1M), only stating it follows Liu et al. (2025). A concrete feature table would improve reproducibility and interpretability of the cold-start results, which depend entirely on feature quality.

- **AttrFormer handling is somewhat inconsistent**: The paper uses AttrFormer's results throughout Table 1 (where it is the best model on all datasets) while simultaneously bracketing it as a "notable outlier" on MovieLens-1M to compare against the "established baseline cluster." If AttrFormer's results are valid (the paper does not dispute them), RetrievalFormer achieves only 81.6% of SOTA on MovieLens, not the 96.7% claimed relative to SASRec. Both comparisons should be acknowledged consistently.

- **LOOC evaluation lacks feature-based baselines on public datasets**: The paper frames LOOC as a "capability diagnostic," which is reasonable. However, only Content-based KNN on the proprietary email dataset serves as an external baseline; no feature-based or hybrid baseline is evaluated under LOOC on the public benchmarks, limiting the conclusions that can be drawn from Table 2.

### Trivial

- The claimed "3× parameter reduction" from shared embeddings is an implementation detail rather than a methodological contribution; the paper overstates its significance slightly.

## Nice-to-Haves

- A cumulative component-ablation table starting from a stripped-down base model and adding components one at a time, all under identical hyperparameters.
- Disentangled latency reporting that clearly separates dual-encoder exhaustive dot-product, dual-encoder ANN, and SASRec full softmax, all on the same hardware.
- A simple dual-encoder baseline (item ID embeddings, same user tower, same InfoNCE training) to isolate the contribution of feature-based encoding.
- A feature-based sequential baseline for LOOC on public datasets to contextualize cold-start performance.

## Removed Points

These points from the input reviews were considered and removed:

- **"No comparison against other dual-encoder models is fatal"** — Downgraded from fatal to major. The paper's primary comparison against ID-softmax models is appropriate for the accuracy-efficiency trade-off claim, and the ablation study provides partial evidence for component contributions.
- **"288× speedup is entirely conflated and deliberately misleading"** — Softened. The paper provides some disaggregated data (e.g., dual-encoder exhaustive at 3.4ms/29.5ms alongside ANN numbers, and Figure 2 attempts to show multiple comparisons). The problem is ambiguous/inconsistent reporting, not deliberate conflation.
- **"Missing appendix / deferred proofs / stripped content"** — Removed per policy. The parser strips appendices; they exist in the original submission.
- **"Formatting, typo, and style issues"** — Removed per policy as parser artifacts.
- **"Missing related work on dual-encoder sequential recommenders"** — Removed. I cannot verify specific missing citations without external sources, per policy.
- **"Item tower capacity asymmetry (no transformer layers in item tower)"** — Removed. This is an architectural design choice, not a weakness. The paper's design is reasonable given the item tower's role.
- **"The paper does not discuss existing dual-encoder or contrastive sequential recommenders in related work"** — Removed. The related work section covers two-stage retrieval models and cold-start methods. While a discussion of dual-encoder sequential recommenders would strengthen it, I cannot confirm specific missing citations.

## Novel Insights

The LOOC protocol is a genuinely novel contribution that could become a standard. Standard cold-start evaluation typically holds out user-item pairs while allowing item IDs to appear in training. LOOC's key insight — selecting items whose IDs are completely absent from training, then expanding to all users whose final interaction is with such an item — creates a stricter and more realistic cold-start benchmark. This protocol cleanly separates ID-memorization from feature-based generalization, making it useful beyond this paper for evaluating any feature-based recommender.

## Suggestions

- **Add a simple dual-encoder baseline** (item ID embedding + transformer user tower + InfoNCE): this is the single most important experiment to add, as it would isolate the contribution of feature-based encoding and AttentionFusion from the dual-encoder paradigm itself.
- **Clarify Figure 2 latency reporting**: explicitly label which measurements correspond to dual-encoder exhaustive dot-product vs. SASRec softmax, ensure consistency with the line 203 numbers, and explain the discrepancy.
- **Provide a cumulative ablation table** where components are added in sequence under identical hyperparameters, so total performance can be decomposed.
- **List item features per dataset** in a short table to improve reproducibility.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EHI (ESq3U7z6FD) | 6.00 | R1 | RetrievalFormer is slightly stronger — more comprehensive evaluation, clearer motivation |
| Relevance-based embeddings (mssRRt6OPE) | 5.75 | R1 | RetrievalFormer is stronger — broader benchmarks, more practical contribution |
| Long-Sequence Recommendation (jkpGIxSsUD) | 5.50 | R1 | RetrievalFormer is stronger — broader scope (efficiency + cold-start vs. embedding decoupling alone) |
| Conservative Evidential Learning (o99Yn1wN9J) | 6.25 | R2 | RetrievalFormer is comparable — better motivated and clearer experiments |
| BTR (3TO3TtnOFl) | 6.50 | R2 | RetrievalFormer is comparable — BTR has a cleaner core idea, RetrievalFormer has broader evaluation |
| Semi-Parametric Retrieval (l0fn10vSyM) | 7.00 | R2 | RetrievalFormer is weaker — less elegant core contribution, messier presentation |
| Conditional Information Bottleneck (h9dnHqrkfa) | 5.25 | R2 | RetrievalFormer is clearly stronger |
| Qinco2 (2zMHHZ569S) | 6.40 | R2 | RetrievalFormer is comparable — different domains |

**Round 1 bracket**: 5.0–7.0. **Round 2 narrowed**: 5.75–6.75 based on anchor comparisons, with Semi-Parametric Retrieval (7.00) as the upper bound and Relevance-based embeddings (5.75) as the lower bound.

RetrievalFormer sits between EHI (6.00) and BTR (6.50). Its strengths (LOOC protocol, comprehensive baselines, practical latency benchmarks, real-world validation) outweigh EHI's, but its weaknesses (missing dual-encoder baseline, ambiguous speedup reporting, incomplete ablation accounting) keep it below BTR's cleaner contribution. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>