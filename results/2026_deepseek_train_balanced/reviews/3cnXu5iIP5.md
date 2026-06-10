## Summary

This paper introduces the Local Euler Characteristic Transform (ℓ-ECT), an extension of the global Euler Characteristic Transform to local neighborhoods of nodes in featured graphs. The ℓ-ECT produces a fixed-size vector representation of each node's local neighborhood by computing sublevel set filtrations of the embedded feature space along sampled directions. The authors prove theoretical properties including invertibility (enabling subgraph counting in principle) and construct a rotation-invariant metric for spatial alignment. Empirically, ℓ-ECT features fed into an untuned XGBoost classifier achieve strong results on several node classification benchmarks, particularly on heterophilic graphs where standard GNNs struggle.

## Strengths

- **Genuinely novel extension of ECT to local graph neighborhoods.** The ℓ-ECT is a theoretically grounded descriptor that provably captures sufficient information to reconstruct local neighborhood feature vectors (Theorem 2), providing a clear mathematical foundation that goes beyond heuristic local feature engineering.

- **Strong empirical performance on multiple heterophilic datasets.** ℓ-ECT + XGBoost substantially outperforms GCN, GAT, GIN, and H2GCN on Cornell (83.8% vs. 64.9%), Wisconsin, Texas, Roman Empire (78.9% vs. 63.6%), and Amazon Ratings. These are large, systematic gaps, not marginal improvements.

- **Formally proven rotation-invariant metric with practical validation.** Theorem 4 establishes that d\_ECT is a metric on rotation classes of finite simplicial complexes, and the spatial alignment experiments (wedged spheres, star graphs) verify that the metric can recover ground-truth rotations with near-zero Hausdorff distances.

- **Theoretical expressivity advantage over GNNs for subgraph counting (Corollary 1).** While this claim is theoretical rather than demonstrated, it correctly identifies a formal capability that message-passing GNNs provably lack, providing a clear motivation for the ECT approach.

## Weaknesses

### Fatal

None.

### Major

1. **Experimental design conflates representation quality with classifier choice.** The paper compares ℓ-ECT + untuned XGBoost against tuned end-to-end GNNs. This confounds two variables: the ℓ-ECT representation and the XGBoost classifier. It is possible that XGBoost — a strong out-of-the-box classifier — drives the improvements, not the ℓ-ECT's superior expressivity. A controlled experiment (e.g., feeding both ℓ-ECT vectors and GNN embeddings into the same MLP or XGBoost) is needed to isolate the representation's contribution. The paper's central claim that ℓ-ECT captures information GNNs miss is not separable from the classifier choice in the current design. The paper acknowledges this confound partially (line 126: "we emphasize that the choice of the model can be controlled by the user") but does not attempt to control it.

2. **Unclear scope of applicability regarding feature geometry.** The ℓ-ECT computes sublevel set filtrations along directions in ℝⁿ, which assumes that the Euclidean geometry of the feature space carries semantically meaningful structure. Several datasets tested (Amazon Computers/Photo with bag-of-words features, Actor with categorical features) have high-dimensional sparse features where Euclidean proximity is not clearly meaningful. The paper provides no analysis of when the ℓ-ECT succeeds or fails based on feature properties, and tests no datasets with inherently geometric features (e.g., molecular 3D coordinates, point clouds). This limits the paper's ability to characterize the method's domain of applicability.

### Minor

1. **Subgraph counting claim (Corollary 1) is presented as a practical advantage but is only a theoretical entailment.** Theorem 3 (ECT equality iff isomorphism) implies that subgraph counting is *possible in principle* via exhaustive checking of all subgraphs, but this is computationally prohibitive and the paper does not attempt it. The conclusion "ECT-based methods for graph representation learning can be more powerful than message-passing-based approaches" overstates what is actually demonstrated — the theoretical capability does not translate to the practical ℓ-ECT + XGBoost pipeline used in experiments.

2. **No runtime, memory, or scaling analysis despite acknowledged computational complexity.** With m=l=64, each node receives a 4096-dimensional ℓ-ECT vector per k-hop neighborhood. The paper acknowledges computational complexity as a limitation (line 112) but reports no wall-clock time, memory usage, or scaling behavior. For graphs with n=10,000+ nodes, the practical viability at scale is unclear.

3. **Rotation-invariant metric proved under L∞ but used with L2.** Theorem 4 proves d\_ECT is a metric under the L∞ norm, but experiments use L2 "for differentiability reasons" (line 110). The paper does not discuss whether the metric properties (identity of indiscernibles, triangle inequality) are preserved under this change, or whether the L2 approximation could introduce false positives/negatives in alignment.

4. **Spatial alignment experiments are limited to synthetic data with known ground-truth rotations.** Real-world graph alignment involves noise, outliers, partial overlap, and different cardinalities. Robustness is briefly mentioned (Fig. 4) but not systematically evaluated. This limits the strength of the claimed practical utility for spatial alignment.

5. **No standard deviations or significance tests reported.** The paper reports "5 training runs" but does not provide error bars, confidence intervals, or statistical tests. Given that many comparisons are described qualitatively ("similar or even better accuracies"), variance information is essential for assessing reliability — especially when some differences are small.

### Trivial

1. The claim that "removing directions leads to lower performance" as evidence of interpretability (Section 5.1) is weak — this observation holds for essentially any feature representation and does not demonstrate meaningful spatial interpretability without further analysis (e.g., which directions correspond to which structural patterns).

2. The abstract states "Our method exhibits superior performance than standard GNNs" but the main text hedges ("often superior," "on a par with"), and results are mixed — H2GCN outperforms on Squirrel and Chameleon, GAT outperforms on Computers. The abstract should reflect the dataset-dependent nature of the results.

## Nice-to-Haves

- Running a controlled experiment where both ℓ-ECT vectors and GNN node embeddings feed into the same downstream classifier (e.g., a 2-layer MLP or XGBoost) to directly compare representation quality.
- Testing ℓ-ECT on datasets with geometrically meaningful features (molecular graphs with 3D coordinates, point clouds) to demonstrate the method's strength in its natural setting.
- Reporting wall-clock time and memory usage for ℓ-ECT computation vs. GNN training on the datasets used.
- Providing error bars (std. dev. over 5 runs) in the tables.

## Removed Points

*These points were flagged for removal; treat with caution.*

- **"No open-source code or reproducibility details"** — Removed per Hard Rules: the paper provides key hyperparameters (m=l=64, XGBoost untuned). Code availability is not required for review.
- **"Missing appendix/proofs"** — Removed per Hard Rules: the parser strips appendix sections from all papers; they exist in the original submission.
- **"The convergence result text is garbled (ECT(X) i1s. ...)"** — Removed as a parser artifact, not an author error.
- **"N_k definition is ambiguous"** — Removed: the paper clearly states two options and specifies that experiments use k-hop neighborhoods (line 67, line 130).
- **"Theorem 2 needs careful unpacking"** — Removed: the theorem statement is precise ("one can reconstruct the feature vectors of its 1-hop neighborhood") and follows directly from ECT invertibility.
- **"The tables are embedded as images"** — Removed as a parser formatting artifact; the substantive concern (missing std. dev.) is retained in Minor weakness #5 above.
- **Harsh Critic's section-by-section notes on Related Work, Introduction** — Removed as generic observations that lack specific actionable content.

## Novel Insights

The most interesting tension revealed across the reviews is between the paper's *theoretical* framing and its *empirical* evidence. The theoretical contribution is genuinely strong: the ℓ-ECT provably captures lossless local information (invertibility), provides a metric on rotation classes, and formally distinguishes graphs that GNNs cannot. However, the empirical pipeline introduces a strong classifier (XGBoost) that makes it impossible to attribute gains to the ℓ-ECT representation versus the classifier's inductive biases. This is a surprisingly common blind spot in representation-learning papers: a novel representation is validated by pairing it with a powerful off-the-shelf model, but the baseline GNNs get no such pairing. The paper would benefit from acknowledging that the empirical evaluation tests the pipeline, not the representation in isolation, and from adding a controlled experiment to bridge the gap.

## Suggestions

1. Add an experiment where both ℓ-ECT vectors and GNN-produced embeddings are fed into the same downstream model (e.g., an MLP or XGBoost). This would directly test whether ℓ-ECT captures more useful information for the classifier.
2. Include a simple synthetic example where two nodes have different 1-hop neighborhoods that GNNs cannot distinguish (WL-test indistinguishability) but ℓ-ECT can separate, making the expressivity claim concrete rather than theoretical.
3. Add error bars to all tables and a brief discussion of statistical significance for the main comparisons.
4. Discuss the feature-geometry dependency explicitly: what types of feature spaces is ℓ-ECT appropriate for, and when might it fail? Test on at least one dataset with clear geometric features (e.g., molecular graphs) to demonstrate the method's natural use case.
5. Report runtime for ℓ-ECT computation and clarify the practical scaling limits.

## Score and Decision

**MY FINAL SCORE: <score>5.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**