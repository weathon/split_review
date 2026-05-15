I now have all the information needed. Here is the final consolidated review.

---

## Summary

This paper proposes **NetInfoF**, a framework with two components: (1) **NetInfoF_A** which measures "network usable information" (NUI) via a score (2^{-H(Y|X)}) computed on five hand-crafted node embeddings (SVD, PPR, raw features, two propagation schemes) without any model training, and (2) **NetInfoF_M** which exploits NUI for link prediction and node classification. The key technical innovation is a compatibility matrix approach (H and H*) that adapts linear-GNN-style static embeddings to link prediction by handling heterophily and negative edges in closed form. Experiments show strong link prediction results — winning or tying on 11 of 12 real-world datasets against general GNN baselines — and linear scalability.

## Strengths

1. **Novel compatibility matrix for linear-GNN link prediction (Lemma 2, H*).** The closed-form formulation that jointly maximizes similarity of positive-edge node pairs while minimizing similarity of negative-edge pairs is technically well-motivated. The ablation (Table 4) shows that H* consistently improves over using no compatibility matrix and over the simpler H (without negative-edge optimization) across all 12 datasets. This addresses a genuine limitation of linear GNNs on link prediction.

2. **Strong empirical performance on link prediction.** NetInfoF achieves average rank 1.0 across all six synthetic scenarios (Table 1, synthetic) and 1.1 across 12 real-world datasets (Table 2), outperforming GCN, SAGE, GAT, H²GCN, GPR-GNN, and SlimG. On OGB benchmarks (Table 3), it outperforms GCN, SAGE, and SlimG with 218× fewer parameters. The results are consistent across both homophily and heterophily graphs.

3. **Provably linear scalability with practical speed-ups.** Lemma 3 states O(f²|V|+f³+d⁴|E|) complexity, and Fig. 3 empirically confirms linear scaling with edge count. Three speed-up techniques (warm start from H, coefficient selection retaining 95% energy, edge reduction via 2-core sampling) make the d⁴ constant manageable in practice.

4. **Carefully designed synthetic benchmarks.** The synthetic datasets cover the full 3×2 cross-product of feature scenarios (random/global/local) × structure scenarios (diagonal/off-diagonal), each with known ground-truth information structure. This is a thorough sanity check, and NetInfoF is the only method robust across all six scenarios (Table 1).

5. **Measurement without model training.** NetInfoF_A computes its score using only derived embeddings, binning, and closed-form solutions — no trained GNN is needed. This avoids the cost and variability of training, which is valuable as a diagnostic tool.

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical gap between the score and the "would a GNN work?" question.** The paper asserts (Sec. 3, line 188): "We identify that a GNN is able to perform well on the task when its propagated representation is more informative than graph structure or node features." The "propagated representation" here refers specifically to the five hand-crafted derived embeddings (C1–C5: SVD, PPR, PCA-reduced features, two propagation schemes). **No argument is given that these particular embeddings capture all information a GNN could exploit.** A GNN with multi-layer nonlinear transformations, attention, or adaptive propagation could in principle extract information that the paper's fixed two-step SVD/PPR/propagation embeddings cannot. Correlation between the score gap and performance in synthetic data (Fig. 4) is suggestive but does not establish causation. This gap weakens the paper's primary motivation: the claim that the score tells you "whether a GNN will work" overstates what is actually demonstrated — namely, that the score correlates with performance *under a fixed linear embedding family*.

2. **Several baseline results are anomalously low, raising questions about fair comparison.** In the main link prediction table (Table 2): SAGE on ArXiv (0.7±0.1), GCN on Products (2.2±0.1), SAGE on Products (0.3±0.2), and GAT on ArXiv (5.0±0.8) are strikingly low. While the paper states that experimental settings are in the appendix (which was stripped by the parser), values in the single digits or below 1% on Hits@100/1000 for established methods like SAGE and GCN suggest either suboptimal tuning for the link prediction setting or a mismatch between the evaluation protocol and how these baselines are typically configured. The paper also does not report statistical significance tests for its "11 out of 12 wins" claim. Without confidence that baselines were tuned competitively, the headline claim is less conclusive than presented.

### Minor

3. **H* optimization (Lemma 2) lacks explicit regularization in its objective.** The objective is: min ∑_{(i,j)∈ℰ} (1 - z_i H* z_j^T) - ∑_{(i,j)∈ℰ_neg} (z_i H* z_j^T). The negative-edge term drives z_i H* z_j^T toward negative infinity, which in principle can produce unbounded H* solutions. The paper uses an iterative LSQR solver with warm start and coefficient selection, which provides practical stability, but the absence of an explicit regularization term (e.g., Frobenius norm on H*) is a theoretical concern.

4. **The abstract's promised "success story" is not elaborated in the main body.** The abstract (line 22) states: "Our success story further demonstrate the correctness of \analysis in a real-world scenario, where there is no usable information in graphs constructed with some specific types of edges." No dedicated experiment or case study corresponding to this claim appears in the main text — the paper's experiments focus on RQ1 (effectiveness), RQ2 (scalability), and RQ3 (ablation). If this story exists, it is exclusively in the appendix; as delivered, the main text makes a prominent claim it does not support.

5. **Node classification results are absent from the main experimental section.** While the paper explicitly notes (line 592) "Since we focus on improving linear GNNs in link prediction, the experiments for node classification are in Appx... because of space limit," this undermines the paper's claim of being *general* (handling both tasks). A claim of generality is naturally evaluated on evidence in the main body. The node classification section (Sec. 5) is also notably brief — one paragraph each for measurement and exploitation — with no analysis of the k-means clustering approximation used for pseudo-labels.

6. **Several baselines exhibit large standard deviations** (e.g., CiteSeer GCN: 60.4±10.0, PubMed GCN: 47.6±13.0, GPR-GNN CiteSeer: 53.5±8.1), while the proposed method's standard deviations are uniformly smaller. This is partly an artifact of the method using fixed (untrained) embeddings with only a linear classifier, which naturally has lower variance. However, this asymmetry makes the comparison of point estimates less reliable.

### Trivial

None.

## Nice-to-Haves

- Directly compare the *score* gap (propagated vs. non-propagated) against the performance gap (GNN vs. MLP) on real datasets, to more directly validate whether the score predicts GNN utility.
- Add a concrete case study where the score correctly identifies uninformative structure in a real graph (the "success story" from the abstract).
- Compare against a standard mutual information estimator (e.g., Kraskov) on synthetic data to contextualize the score.
- Test sensitivity to hyperparameters like number of propagation steps, PCA dimensions, and number of bins for discretization.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Theorem 2 accuracy definition is non-standard"** (Harsh Critic, Sec. 3): The definition ∑_x max_y p_{x,y} is the standard expected accuracy weighted by P(X=x), not non-standard. **Factually incorrect — removed.**
- **"OGB baselines are not state-of-the-art"** (Harsh Critic, RQ1): The paper explicitly scopes its comparison as "general GNNs" (line 599) and excludes specialized subgraph GNNs (e.g., SEAL) by design. **Scope creep — removed.**
- **"Ablation shows H performs worse than w/o CM on some datasets, undermining necessity"** (Harsh Critic, RQ3): The paper explicitly explains this (lines 795–796): H alone can hurt in homophily graphs because it lacks negative-edge suppression. This is exactly what the ablation is designed to demonstrate. **Misunderstands purpose of ablation — removed.**
- **"Baseline training details not described in main text"** (Harsh Critic, RQ1): The paper states details are in Appx.~\ref{app:rep} (line 591), stripped by parser. Not absent — just deferred. **Removed per hard rule on appendix content.**
- **"Complexity O(d⁴|E|) is practically misleading"** (Harsh Critic, RQ2): The paper provides three speed-up techniques that substantially reduce this constant, and Fig. 3 empirically demonstrates linear scaling. **Overstated — removed.**
- **"Author inline comments (xiangsx, james, christos) not cleaned"** (Harsh Critic, Abstract/Intro): Presentation artifact. **Removed per formatting rule.**
- **Strength Finder: generic strengths** (e.g., "addressed an important problem"): These were filtered as lacking specific citation or concrete content.

## Novel Insights

The harsh critic and strength finder together surface an interesting tension: the paper's two claimed contributions (measuring NUI to predict "would a GNN work?" and exploiting it for link prediction) operate at different levels of rigor. The link prediction contribution is well-supported — the H* compatibility matrix is a genuinely clever solution to a known limitation of linear GNNs, and the empirical results are strong. The measurement contribution, however, rests on an unverified assumption that the five fixed embeddings capture all GNN-relevant information. The paper would be stronger if it disentangled these: the link prediction results stand on their own as a contribution to linear-GNN methodology, while the NUI measurement is better framed as a *heuristic diagnostic* for practitioners (analogous to probing classifiers) rather than a theoretically grounded predictor of GNN performance.

## Suggestions

1. **Add a limitations section** acknowledging that the derived embeddings are a fixed design choice and may not capture all information exploitable by expressive GNNs.
2. **Add explicit regularization** (e.g., Frobenius norm on H*) to the Lemma 2 objective and discuss its impact.
3. **Run a significance test** (e.g., Wilcoxon signed-rank) across datasets for the "11/12 wins" claim.
4. **Include the "success story" case study in the main text** — if it exists only in the appendix, remove the abstract claim or bring it forward.
5. **Move node classification results** (even in condensed form) to the main experimental section, particularly Tables 2–3, since generality is a claimed advantage.

## Score and Decision

The paper makes a genuine contribution — the compatibility matrix approach for linear-GNN link prediction is novel, well-motivated, and empirically effective. The synthetic benchmarks are thorough, and the scalability analysis is credible. However, the paper's core framing (the score as a predictor of "would a GNN work?") rests on an unverified assumption, and the baseline comparison has uncertainties that reduce confidence in the headline results. The paper is solid but not as strong as its abstract suggests.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>