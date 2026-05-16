## Summary

This paper proposes NetInfoF, a framework for measuring and exploiting Network Usable Information (NUI) on node-attributed graphs. It includes: (1) NetInfoF_Analysis, which computes a theoretically grounded NUI score (lower-bounding accuracy via Shannon entropy) without neural network training; and (2) NetInfoF_Model, which solves link prediction and node classification using derived node embeddings and a compatibility matrix adjustment. On link prediction, NetInfoF achieves the best average rank across 12 real-world datasets and is the only method robust to all synthetic graph scenarios.

## Strengths

- **State-of-the-art link prediction performance across diverse graphs.** On 12 real-world datasets (7 homophily, 5 heterophily), NetInfoF achieves the highest Hits@K in 11 of 12 cases and the best average rank (1.1), outperforming GCN, GAT, SAGE, H²GCN, GPR-GNN, and SlimG (Table 2). This is a clean, well-documented set of results.

- **The compatibility matrix adjustment is principled and empirically validated.** The ablation study (Table 4) shows that both the compatibility matrix and its negative-edge-aware variant H* are necessary components: dropping CM hurts performance dramatically on heterophily graphs (e.g., Squirrel drops from 24.2 to 14.3; Twitch from 19.6 to 8.9), and adding H* further improves upon H on most datasets.

- **Scalability linear in input size with demonstrated practical efficiency.** The complexity analysis shows O(f²|V| + f³ + d⁴|E|), and the empirical runtime scales linearly with edge count (Fig. 5). On OGB datasets, the model uses only 1,280 parameters while outperforming models with >279K parameters, validating practical efficiency.

- **Comprehensive synthetic validation with ground-truth NUI.** The synthetic datasets span 6 scenarios (3 feature types × 2 structure types, full cross-product), and NetInfoF achieves average rank 1.0, uniquely robust across all conditions. The NUI score correctly identifies the most informative component in each scenario, serving as a rigorous sanity check.

## Weaknesses

### Fatal

None.

### Major

- **Lemma 2 contains a sign error that contradicts its stated goal.** The displayed equation is:
  \[
  \min_{\mathbf{H}^{*}} \sum_{(i,j)\in\mathcal{E}} (1 - \mathbf{z}_i\mathbf{H}^{*}\mathbf{z}_j^\intercal) - \sum_{(i,j)\in\mathcal{E}_{\text{neg}}} (\mathbf{z}_i\mathbf{H}^{*}\mathbf{z}_j^\intercal)
  \]
  The paper states that H* "minimizes the similarity of nodes connected by the sampled negative edges" (line 343). However, the second term \(-\sum_{\mathcal{E}_{\text{neg}}} (\mathbf{z}_i\mathbf{H}^{*}\mathbf{z}_j^\intercal)\) is equivalent to **maximizing** similarity for negative edges, not minimizing it. (The overall objective simplifies to \(\text{constant} - \sum_{\mathcal{E}\cup\mathcal{E}_{\text{neg}}} \mathbf{z}_i\mathbf{H}^{*}\mathbf{z}_j^\intercal\), i.e., maximizing similarity for all edges.) The correct form to suppress negative-edge similarity would be \(+\sum_{\mathcal{E}_{\text{neg}}} (\mathbf{z}_i\mathbf{H}^{*}\mathbf{z}_j^\intercal)\) in a minimization, or equivalently \(\max \sum_{\mathcal{E}} \cdot - \sum_{\mathcal{E}_{\text{neg}}} \cdot\). Given that the ablation study shows H* empirically helps, the implementation likely follows the correct formulation while the displayed equation has a typo. Nevertheless, a sign error in a core mathematical lemma is a significant presentation failure that undermines reader trust. The authors must clarify whether the equation, the implementation, or both need correction.

### Minor

- **Unedited author comments remain in the submission.** The abstract and introduction contain visible `\xiangsx{...}`, `\james{...}`, and `\christos{...}` editing notes (lines 6, 8, 13, 18, 19). This gives the impression the paper was submitted before completing a final pass, which is inappropriate for a peer-reviewed venue; however, this is fixable and does not affect technical content.

- **The "without any model training" claim is imprecise.** Computing the NUI score requires solving for H* via LSQR (multi-target linear regression) for link prediction and k-means clustering for node classification. The paper should clarify that no *neural network* training is needed, rather than claiming no model training at all, which could mislead readers about the computational requirements.

- **The central motivating question ("will a GNN outperform MLP?") is not directly validated.** The paper asks in the abstract: "can we tell whether the GNNs will perform better than MLP?" The experiments show that NetInfoF's score correlates with its *own* performance and can identify which components are most informative (e.g., whether propagation helps). However, no experiment directly compares GNN performance to an MLP on node features alone and checks whether the score predicts that comparison. The connection between the motivating question and the presented evidence is weaker than the framing suggests. The synthetic experiments partially address this (identifying when structure is more informative than features), but a direct GNN-vs-MLP experiment would substantially strengthen the claim.

- **The undirected graph assumption is not fully accounted for in Lemma 1.** The objective \(\min_{\mathbf{H}} \sum_{(i,j)\in\mathcal{E}} \|\mathbf{z}_i\mathbf{H} - \mathbf{z}_j\|^2_2\) treats each edge as directed (i→j), but the paper defines the graph as undirected (line 190). For undirected graphs, a symmetric formulation or inclusion of both (i,j) and (j,i) would be more principled. The practical impact is unclear, but the methodological gap should be addressed.

### Trivial

- None.

## Nice-to-Haves

- An ablation study varying the propagation steps \(k_{\text{PPR}}, k_{\text{row}}, k_{\text{sym}}\) beyond the fixed value of 2 would strengthen the justification for this choice.
- For the central "would a GNN work?" question, including a simple MLP-on-features baseline in the comparison tables would directly ground the motivating claim.
- On OGB datasets, the baseline set is limited to GCN, SAGE, and SlimG — adding a few more recent methods (e.g., a subgraph GNN) would strengthen the generality claim, though this is not required given the paper's focus on *general* GNNs.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing pseudo-code in appendix / underspecified for reproducibility":** Removed because the appendix was stripped by the parser; the original submission contains it.
- **"SVD of adjacency is not standard for community structure":** Removed — SVD of the adjacency matrix (spectral methods) is a standard approach for capturing community structure. The reviewer's claim that it is non-standard is factually incorrect.
- **"Missing SEAL/Neo-GNN baselines":** Removed — the paper explicitly focuses on *general* GNN methods (as stated in Section 8), not specialized subgraph link predictors. This is within-scope scoping, not an omission.
- **"Theorems 1 and 2 are standard inequalities presented as novel":** Removed — the paper presents these as theoretical grounding for the NUI score, not as novel information-theoretic discoveries. The novelty lies in their application to derived embeddings and discretization.
- **"The paper claims robustness on limited synthetic data":** Weakened and moved to Nice-to-Haves — the 6-scenario cross-product is actually reasonably comprehensive for a sanity check.
- **"k_PPR, k_row, k_sym = 2 is arbitrary":** Moved to Nice-to-Haves — this is a design choice, and the paper explains the intuition. An ablation would be nice but is not a weakness.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful tension: the paper's strongest selling point (strong empirical link prediction results across 11/12 datasets) coexists with a sign error in a key equation and an under-validated central claim. The real lesson is that the compatibility matrix framework is empirically robust even if the exposition in Lemma 2 is wrong — suggesting the method may be more resilient than the theory suggests, or that the implementation diverges from the written lemma. The reviews also highlight that the paper's framing ("can we tell if a GNN will work?") sets up a reader expectation that the experiments do not fully satisfy, creating a disconnect between motivation and evaluation that can hurt otherwise strong submissions.

## Suggestions

1. **Fix Lemma 2 immediately.** Correct the sign in the displayed equation (change the minus before the negative-edge sum to a plus). Verify that the proof in the appendix and the implementation both use the corrected form. If the implementation already uses the correct form, state this explicitly.
2. **Remove all unedited author comments** (`\xiangsx`, `\james`, `\christos`) before any resubmission.
3. **Add a direct GNN-vs-MLP experiment** on a few datasets (e.g., Cora, Squirrel, Products) where you compare GCN against an MLP on raw features and show that the NUI score correctly predicts which will perform better. This directly validates the paper's core framing.
4. **Rephrase "without any model training"** to something more precise, such as "without iterative neural network training" or "without training a learned model."
5. **Address the undirected graph formulation** in Lemma 1 by either noting that the asymmetric loss is intentional (because link prediction treats edges as ordered pairs for scoring) or adding a symmetrized variant.

## Score and Decision

The paper has genuine empirical and methodological contributions: the NUI framework, the compatibility matrix adjustment, and consistent SOTA link prediction results. However, the sign error in Lemma 2 is a significant defect in a core technical component, and the paper's presentation (unedited author comments, imprecise claims) is below the professional threshold for acceptance. The paper could become a strong contribution after the Lemma 2 issue is resolved, the editing artifacts are removed, and the central claim is better aligned with the evidence.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>