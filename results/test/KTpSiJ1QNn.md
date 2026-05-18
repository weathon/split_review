Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes G-SPARC, a framework for handling cold-start nodes (nodes with no known connections) in graph learning. The core idea is to train a parametric neural network (via a Rayleigh-quotient loss using the graph Laplacian) to map node features to approximate spectral embeddings (eigenvectors of the Laplacian). During inference, cold-start nodes' features are projected into this spectral embedding space, enabling nearest-neighbor-based predictions without requiring adjacency information. The authors instantiate this in two architectures: SPARC-GCN (a modified spectral GCN) and SPARCphormer (a graph transformer using spectral-neighbor token lists), and evaluate on node classification, clustering, and link prediction across four datasets.

## Strengths

1. **Approach to a genuine and under-addressed problem.** Cold-start nodes are a real limitation of most graph learning methods, and the paper's strategy — learning a feature-to-spectral-embedding mapping during training that generalizes to unseen nodes — is a sensible and principled direction.

2. **Consistent empirical gains over existing cold-start baselines.** On cold-start node classification (Table 1), both SPARC-GCN and SPARCphormer outperform GraphSAGE and Cold-BREW across Cora, Citeseer, Pubmed, and Reddit. SPARC-GCN achieves +7.86 points over GraphSAGE on Cora and +5.83 points on Reddit, with Cold-BREW running out of memory on Reddit. These are non-trivial margins on standard benchmarks.

3. **Versatility across multiple downstream tasks.** The same spectral embedding is applied (with minimal modification) to node classification, node clustering, and link prediction, achieving competitive MRR on link prediction (e.g., 31.25 on Cora vs. LLP's 27.87) without task-specific architectural changes. This demonstrates practical generality.

4. **Effective spectral mini-batching as an additional contribution.** Spectral partitioning using the learned embeddings yields substantial gains over random mini-batching for GCN training (+14.77% on Cora, +15.08% on Citeseer) and faster convergence than both random and METIS-based partitioning on Reddit (Table 3, Figure 4). While tangential to the cold-start claim, this is a useful practical finding in its own right.

5. **Ablation analysis exploring the feature-structure interplay.** The two-moons toy example (Figure 5) cleanly illustrates that features alone (or structure alone) can be insufficient, motivating the need for joint modeling. The α-ablation (Figure 4) further shows that a balanced combination of feature affinity and adjacency produces the best spectral embeddings.

## Weaknesses

### Fatal

None.

### Major

1. **Under-specified evaluation protocol for cold-start nodes.** The paper states: "A subset of nodes from the graph is isolated by masking their adjacency connections. Test nodes are defined as nodes that were not included in the training phase but still retain full adjacency information" (lines 183–184). These two sentences conflate two different node sets without clarifying how they relate. It is never specified: what fraction of nodes are made cold-start, whether they are drawn from the training or test split, how the isolation is performed (randomly? by degree?), whether the same splits are used across all methods, or what exact adjacency information (if any) is provided to each method at inference. This lack of specificity means the reader cannot fully assess whether the comparison to GraphSAGE and Cold-BREW is on equal footing. The paper needs a precise, reproducible protocol.

2. **Missing a critical baseline: a feature-only model (MLP).** Since cold-start nodes have no adjacency, a standard MLP trained on node features alone is the simplest baseline to determine whether gains come from the spectral embedding or simply from better feature encoding. The paper compares only to GraphSAGE and Cold-BREW, both of which have their own inductive/generalization mechanisms. Without an MLP baseline, the reader cannot isolate the contribution of the spectral mapping. This is particularly important given that the method uses graph structure during training, raising the question of whether the training signal from the Laplacian is the primary source of improvement.

3. **Clustering results presented without numerical values.** Figure 3 (clustering) is a bar chart with no numerical accuracy values, error bars, or standard deviations reported in the text or figure. Given that clustering accuracy varies with initialization, and the paper claims superiority over several methods on cold-start nodes, this lack of verifiable numbers makes the clustering claims substantially weaker than they could be. A table with mean ± std would allow proper comparison.

### Minor

4. **Limited theoretical justification for the modified spectral convolution.** Replacing the fixed, orthogonal eigenvector matrix \(U\) with a learned, feature-dependent, non-orthogonal approximation \(U_\theta(X)\) in the convolution \(X_{l+1} = U_\theta(X) g_\phi U_\theta(X)^T X_l\) breaks the standard spectral convolution interpretation: \(U_\theta(X)^T X_l\) is no longer the graph Fourier transform, and the filter \(g_\phi\) is not applied in the spectral domain of the fixed Laplacian. The paper provides no reasoning or proof that this operation corresponds to a meaningful convolution. While the dimensions are consistent (verified: \(n \times k \cdot k \times k \cdot k \times n \cdot n \times d = n \times d\)), the mathematical grounding is heuristic rather than rigorous. The authors should either provide a theoretical justification or explicitly characterize this as a heuristic approximation, which would be acceptable for an empirical paper but should be stated plainly.

5. **No ablation on the number of eigenvectors \(k\).** The method relies on approximating the first \(k\) eigenvectors, but there is no experiment showing how performance varies with \(k\). This is important because \(k\) controls the trade-off between approximation quality and computational cost.

6. **Computational cost of nearest-neighbor search is not discussed.** The SPARCphormer token list construction (and link prediction) requires nearest-neighbor search in the spectral embedding space over all nodes. For Reddit (232k nodes), this is \(O(n^2)\) in the worst case. The paper does not mention whether approximation methods (e.g., FAISS, HNSW) are used, nor does it report wall-clock times or memory usage.

7. **Ambiguity in the spectral-banding experiment (Tables 3, 4, Figure 4).** The paper should clarify whether the partition used for mini-batching is computed from the true Laplacian eigenvectors or from the learned parametric mapping \(\mathcal{F}_\theta\). The description in Section 3.4 ("spectral clustering" using \(\mathcal{F}_\theta\)) suggests the latter, but this is not explicitly stated.

### Trivial

8. Stray duplicate label `\label{fig}` on line 242 alongside the proper `\label{fig:clustering}` on line 244.
9. Minor typo: "classifaction" → "classification" on line 264.

## Nice-to-Haves

- An MLP baseline for all tasks (as noted in Major 2).
- A table with numerical clustering accuracy values and standard deviations (as noted in Major 3).
- A sensitivity analysis on the number of eigenvectors \(k\).
- Discussion of approximate nearest-neighbor methods used (if any) and computational cost for large graphs.
- Clarification on how the cold-start split is constructed (random selection, degree-based, etc.) and the number of cold-start nodes per dataset.

## Removed Points

These points from the reviews were removed or downgraded; they are listed here for completeness but should be treated with caution:

- **"Dimensional inconsistency in the cold-start convolution equation"** (Harsh Critic, Critical Issue 2): Verified as incorrect. The equation \(x_{l+1} = U_\theta(x) g_\phi U_\theta(\hat{X})^T \hat{X}_l\) is dimensionally consistent: \( (1\times k)(k\times k)(k\times (n+1))((n+1)\times d) = 1\times d\). No inconsistency exists. [Removed as factually wrong.]

- **"Figure referenced as 'Figure 1' in the text, and the caption does not match the text description"** (Harsh Critic, Critical Issue 4): The paper correctly uses `\ref{fig:clustering}` throughout. No reference to "Figure 1" for the clustering figure was found. [Removed as factually wrong.]

- **"Mini-batching experiments are tangential to the cold-start problem"** (Harsh Critic, Other Observations): These are presented as an "additional application" (Section 3.4). The paper claims this as a secondary contribution, not as evidence for the cold-start claim. This is scope-appropriate and not a weakness. [Removed — evaluates against wrong expectations.]

- **"Feature Weighting Factor should have been adopted as the default method"** (Harsh Critic, Other Observations): The α-ablation is presented as an analysis exploring feature-structure alignment, not as a proposed extension. The paper explicitly discusses this as future work for heterophilous graphs. This is a reading of the ablation's purpose, not a weakness. [Removed — the paper's treatment is appropriate for an ablation/limitation discussion.]

## Novel Insights

The most interesting observation bridging the reviews is that the paper's core strength (a parametric, generalizable spectral embedding) is also the source of its main theoretical tension: the method works empirically, but the modification to spectral-GCN replaces the fixed orthogonal Fourier basis with a learned non-orthogonal approximation without characterizing what spectral properties are preserved or lost. This mirrors a broader tension in the graph learning literature between methods that are theoretically clean (exact spectral decomposition) and those that are practically effective (learned approximations). The paper would benefit from explicitly confronting this gap — perhaps by analyzing how close the learned \(U_\theta(X)\) is to the true \(U\), or by characterizing the approximation error's effect on downstream performance.

## Suggestions

1. Add a precise, bullet-point description of the cold-start evaluation protocol: how many nodes, how they are selected, what each method receives at inference.
2. Include an MLP baseline on node features alone for all tasks.
3. Replace the clustering bar chart with a table showing mean accuracy ± std for all methods on both connected and cold-start nodes.
4. Add an ablation on the number of eigenvectors \(k\).
5. Discuss the computational cost of nearest-neighbor search and whether approximation is used.
6. Provide a brief justification or explicit caveat about replacing \(U\) with \(U_\theta(X)\) in the spectral convolution, acknowledging the departure from standard spectral GCN theory.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>