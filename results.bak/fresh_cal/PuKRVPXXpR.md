Now let me produce the final consolidated review.

## Summary

The paper proposes ResTran, a simple feature transformation \(X_G = X L_b^{-1/2}\) that encodes graph topology into a vector representation, allowing standard vector-based ML methods (SVM, simple NNs) to be applied to node classification instead of using GNN architectures. The authors justify the transformation through connections to effective resistance, \(k\)-means, and spectral clustering (Theorem 8), and empirically show that ResTran + a simple classifier outperforms GCN, GAT, and SGC on several heterophilous datasets by large margins.

## Strengths

1. **Clean, principled transformation with formal justification.** Theorem 8 establishes an equivalence between \(k\)-means on Laplacian coordinates \(\mathbf{v}'_i\) and ratio cut spectral clustering in the featureless setting, and the paper extends this to the graph-with-features setting through a natural generalization. This is a genuine theoretical contribution — prior work (Dhillon et al., 2004) connected kernel \(k\)-means to normalized cut for vector data, while this paper connects \(k\)-means on the Laplacian coordinates to ratio cut for graph data.

2. **Empirically large improvements on heterophilous datasets.** Table 3 shows ResTran + a plain NN achieving substantially higher accuracy than GCN, GAT, and SGC on heterophilous datasets (e.g., Wisconsin 81.2% vs. GCN 47.8%, Cornell 73.1% vs. GCN 57.1%, Texas 73.9% vs. GCN 50.9%). These margins are large enough to be practically meaningful and go beyond incremental improvements.

3. **Effective resistance interpretation provides an intuitive explanation.** Propositions 5 and 6 show that the transformed coordinates preserve within-component resistances while allowing inter-component separation to be controlled by parameter \(b\). This gives a principled mechanism explaining why ResTran handles both homophilous and heterophilous structure differently from GNN layer stacking.

4. **Practical Krylov subspace approximation.** The paper describes an \(O(r f m)\) approximation (Algorithm 1) that avoids the prohibitive \(O(n^3)\) cost of computing \(L_b^{-1/2}\) directly, making the method feasible for large graphs.

5. **Improved unsupervised representation.** Table 1 shows that spectral clustering on ResTran consistently outperforms both graph-only and feature-only approaches across six datasets, demonstrating that the transformed representation captures combined graph and feature information better than either alone.

## Weaknesses

### Fatal

None.

### Major

1. **Insufficient baselines for the central robustness claim.** The paper claims ResTran is "more robust to the homophilous bias than established GNN methods" (abstract, introduction, conclusion), but only compares against GCN, GAT, and SGC — models known to struggle on heterophily. The paper itself cites several methods designed explicitly for heterophilous graphs (Azabou et al., 2023; Pei et al., 2020; Luan et al., 2021; also H2GCN, LINKX, ACM-GCN, FAGCN from the broader literature). Without comparisons against at least one such method, the evidence does not fully support the broad robustness claim. The result as presented demonstrates that ResTran beats simple GNNs on heterophily, which is a weaker and less informative finding. Narrowing the claim or adding heterophily-robust baselines would resolve this.

### Minor

2. **Wording error in the spectral explanation of heterophily handling.** Section 4.1 states that the heterophilous space "is amplified by small \(\lambda_j^{-1/2}\) since \(\lambda_j\) is large." Since \(\lambda_j^{-1/2}\) is *small* when \(\lambda_j\) is large, multiplying by it *suppresses* rather than amplifies. The intended contrast — that ResTran applies this suppression only once, while GNN layer stacking compounds it — is still valid, but the current phrasing is technically backwards. This is a presentation error, not a methodological collapse, but it undermines the paper's own theoretical narrative.

3. **Missing experimental details that affect reproducibility.** The paper reports averages over 10 random splits but omits standard deviations from all tables (Tables 1–3). It also does not report hyperparameters for any method (e.g., number of GNN layers, hidden dimensions, learning rate, dropout, weight decay, Krylov subspace dimension \(r\), parameter \(b\), SVM kernel parameters \(\gamma\) and \(C\)). Dataset statistics (number of nodes, edges, classes, feature dimension, homophily ratio) are not reported, making it harder to interpret results, especially the contrast between homophilous and heterophilous datasets. While the parser strips appendices (which may contain some of these details), the main text should still be self-contained on key methodological choices.

4. **No ablation or sensitivity analysis for the key hyperparameters \(b\) and \(r\).** The parameter \(b\) controls inter-component separation (Proposition 6 gives a theoretical lower bound but no practical guidance), and the Krylov dimension \(r\) controls approximation quality. Without any ablation showing how these affect accuracy across datasets, practitioners have no principled way to set them. This limits the method's immediate utility.

### Trivial

5. **Unsupervised experiment design mixes graph constructions.** Section 6.1 compares "graph-only" (spectral clustering on the original adjacency matrix) with "feature-only" and "ResTran" (both using a Gaussian kernel graph). The comparison between feature-only and ResTran is fair (same construction pipeline), but the graph-only baseline uses an entirely different graph. A cleaner design would either use the same kernel construction for all three baselines, or compare spectral clustering on the original graph vs. spectral clustering on ResTran embeddings treated as a new feature space. However, this does not affect the paper's main SSL results.

## Nice-to-Haves

- Adding heterophily-robust GNN baselines (e.g., H2GCN, LINKX) to the SSL experiments would directly validate or bound the robustness claim.
- An ablation sweep over \(b\) and \(r\) on one heterophilous dataset would improve reproducibility and provide practical guidance.
- The paper could more carefully distinguish the mechanism: ResTran preserves high-frequency (heterophilous) components because \(L_b^{-1/2}\) multiplies by \(\lambda_j^{-1/2}\) once, whereas GNN stacking multiplies by powers of the graph filter, progressively shrinking those components toward zero.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"2-WL expressive power limitation is speculative"** — The paper explicitly labels this as a conjecture and future work in the conclusion. The critic calls it an afterthought, but it is correctly scoped as speculation, not a substantive weakness.
- **"The paper does not report dataset statistics"** — This is already subsumed by the broader Minor weakness about missing experimental details (point 3). Not removed entirely, just merged.
- **"Missing Krylov subspace implementation details (iterations, stopping criterion)"** — The paper states \(r < 100\) is typical. Full implementation details would be in the appendix (which exists in the original submission). This is a presentation choice, not a substantive gap.
- **"The unsupervised experiment should use the same graph construction for all baselines"** — Demoted to Trivial because the main comparison (feature-only vs. ResTran) uses the same kernel construction and is therefore internally valid; the graph-only baseline is supplementary.
- **"The 5% label split could favor SVM over GNNs"** — This is a speculation about experimental design without evidence that it actually influences the results. If true, it would weaken both methods symmetrically.

## Novel Insights

The harsh critic's observation about the spectral wording error ("amplified by small \(\lambda_j^{-1/2}\)") is genuinely useful — it identifies a specific sentence where the paper's own explanation undermines its clarity. Beyond this, the reviews do not surface any insight that is not already present in the paper's own theoretical development (particularly the novel connection between ratio cut and \(k\)-means in Theorem 8, which the paper itself highlights but may undersell relative to prior spectral connection literature).

## Suggestions

1. **Add at least 2–3 heterophily-robust GNN baselines** (e.g., H2GCN, LINKX, ACM-GCN) to the SSL experiments. This is the single most impactful improvement — it would either validate the broad robustness claim or honestly bound it.

2. **Fix the wording in Section 4.1.** Replace "amplified by small \(\lambda_j^{-1/2}\)" with a precise statement: the heterophilous components are multiplied by \(\lambda_j^{-1/2}\) (a factor < 1) only once, whereas GNN stacking multiplies them by \(\lambda_j^k\) across \(k\) layers, driving them toward zero. The distinction is that ResTran *suppresses less aggressively*, not that it amplifies.

3. **Add standard deviations to all tables.** For 10 random splits, reporting mean ± std is standard and essential for assessing significance.

4. **Report the chosen hyperparameters** (or at least the range searched) for all methods, and add an ablation study showing sensitivity to \(b\) and the Krylov dimension \(r\).

5. **Include dataset statistics** (number of nodes/edges/classes/features, homophily ratio) in a table — this is standard practice for graph learning papers and helps readers interpret the heterophily results.

**Evaluation axes:**
- **Originality:** Good — the ResTran transformation itself is simple but the theoretical justification (Theorem 8, connection between ratio cut and \(k\)-means on Laplacian coordinates) is novel.
- **Importance of research question:** High — overcoming GNN homophily bias is an active problem, and a simple preprocessing alternative to complicated GNN architectures is valuable.
- **Claims supported by evidence:** Partially — the core empirical results are strong, but the claim about "robustness to homophilous bias" is broader than the baseline set supports.
- **Soundness of experiments:** Adequate but incomplete — missing standard deviations, limited baselines, no hyperparameter sensitivity analysis.
- **Clarity of writing:** Good overall, with one notable technical wording error in Section 4.1.
- **Value to research community:** Positive — the method is simple, well-motivated, and the empirical improvements are large enough to be practically interesting.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>