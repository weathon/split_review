Now I have a thorough understanding of the paper and can verify each claim. Let me construct the final consolidated review.

## Summary

TreeX proposes extracting global subgraph concepts from GNNs by clustering root node embeddings that represent L-hop message-passing subtrees, then learning class-specific concept weights. The key ideas are (1) reducing the search space from enumerating all subgraphs to mining over rooted subtrees (one per node), and (2) using the GNN's own last-layer node embeddings as subtree representations, avoiding auxiliary subgraph encoders. The paper demonstrates qualitatively that TreeX recovers known motifs (house, cycle, NO2, NH2) and shows per-instance explanation capabilities that existing global methods lack.

## Strengths

- **Novel approach to graphical global concepts**: TreeX is the first method to extract explicit subgraph-level concepts at the dataset/class level from GNNs, going beyond latent prototypes (GLGExplainer) or human-defined rules (GCNeuron). The qualitative results in Figure 3 convincingly show that TreeX recovers known motifs (house, cycle, NO2, NH2) that align with domain knowledge while baselines produce less interpretable outputs.

- **Principled use of node embeddings as subtree representations**: Theorem 4.2 proves that for injective MPGNNs (e.g., GIN), the l-th layer root embedding is a bijective encoding of the full l-hop rooted subtree. This theoretically justifies using off-the-shelf node embeddings for concept representation without auxiliary subgraph encoders, which is both elegant and computationally efficient.

- **Ability to explain incorrect GNN predictions**: TreeX's class-specific global rules provide insights into why a GNN makes wrong predictions (Section 5.2, Table 3, Figure 4). This goes beyond most existing explainers that only rationalize correct predictions and offers practical debugging utility.

- **Exponential reduction in search space for concept mining**: By mining over L-hop subtrees rather than enumerating all possible subgraphs, TreeX reduces the search space per graph from exponential to O(N) (N nodes per graph, as argued in Section 4.2). This makes global-level concept extraction practical where subgraph enumeration approaches would be infeasible.

## Weaknesses

### Major

1. **Fidelity comparison against local methods is not properly specified, making the quantitative claim unsupported.** The paper reports AccFidelity and ProbFidelity comparing TreeX against GradCAM, GNNExplainer, SubgraphX, EiG-Search (Tables 1–2), but never specifies how "the explanation" (G_i^X in the fidelity formulas) is derived from TreeX for each test instance. For the local baselines, G_i^X is a masked subgraph fed through the **full original GNN** (message-passing + classifier). For TreeX, Section 4.1 describes computing the classifier prediction on weighted global concept embeddings via ŷ_i = Ψ(w_t K_i M). If this surrogate prediction is used as "prediction on the explanation" rather than feeding an extracted subgraph through the original GNN, the comparison measures different quantities. The paper's own wording — "unlike the baselines that simply identify the explanation subgraphs, our approach additionally learns the best weights of them for more optimized prediction probability" (line 183) — strongly suggests a different measurement procedure. The claim of "comparable or superior performance" (abstract) is therefore not adequately supported, and the near-100% AccFidelity values are suspicious without clarification.

2. **Data leakage from using the full dataset for concept extraction.** Section 4.1 states that local and global concept mining is performed "across the entire dataset 𝒟" (line 77). Tables 1–2 report results on "test datasets." The paper never clarifies whether 𝒟 is only the training set or includes the test data. If test instances contribute to defining the global concepts and learning the weights w_t, the reported fidelity numbers may be artificially inflated. A proper train/test split for concept extraction is essential for valid evaluation.

### Minor

1. **Unvalidated clustering assumption.** Theorem 4.2 guarantees that different subtrees map to different embeddings (injectivity). The method's clustering pipeline relies on the converse — that embeddings close in Euclidean space correspond to structurally similar subtrees (line 25). The paper provides no experimental validation of this assumption (e.g., measuring intra- vs. inter-cluster graph edit distance). While a common heuristic, this gap weakens the theoretical foundation.

2. **GNN architecture used in experiments is underspecified.** Section 5.1 (Experimental Setup) does not state which specific GNN architecture was used, how it was trained, or its hyperparameters. The paper mentions "maximally powerful MPGNNs" and gives GIN as an example (line 44), but does not confirm which model was actually employed in the reported results. This hinders reproducibility.

3. **Extracted subgraph concepts may be disconnected and ignore node features.** The edge-counting procedure (γ(e|S_i), lines 65–73) selects all edges with maximum count, potentially yielding multiple disconnected fragments as a single "concept." The paper does not discuss concept coherence. Moreover, the extraction procedure counts edges only, without incorporating node features (critical for molecular datasets where atom type defines a motif like NO2). This is acknowledged only implicitly.

4. **Theorem 4.2 assumes countable input features.** The injectivity guarantee requires countable node features (line 120), but most real-world graphs have continuous features. The paper does not discuss this limitation or test whether it holds for the datasets used.

5. **The "n! to n" search space reduction is imprecise.** The paper states that subgraph enumeration involves "up to n! possible subgraphs" (line 112), but the actual count is 2^{|E|}. While the qualitative point (subtree space is far smaller) is correct, the specific framing is mathematically sloppy.

### Trivial

- The complexity bound "less than O(e n k)" (line 204) is stated without derivation.
- Table 3's "Rate of predicting the true labels" metric could be more clearly defined.

## Nice-to-Haves

- Sensitivity analysis on k (local clusters) and m (global clusters) would strengthen the practical guidance for users.
- A direct comparison of TreeX against global methods on motif recovery (precision/recall on synthetic datasets like BA-2Motifs where ground-truth motifs are known) would more directly validate the core claim.
- An experiment that validates the clustering assumption (e.g., showing intra-cluster structural similarity via graph edit distance) would significantly strengthen the paper's foundation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength from Strength Finder: "State-of-the-art local-level fidelity while providing global subgraph concepts"** — This conflicts with the verified weakness (Major #1) about the fidelity comparison not being properly specified. When a strength and a verified weakness disagree on the same evidence, the weakness prevails. This strength is not supported by the current experimental presentation.

- **Critic's point about missing appendix content ("Visualization of Concept Scores on Instances")** — The paper references section "3" (line 195) which was stripped by the parser. These appendix sections exist in the original submission.

- **Critic's claim that "the entire fidelity evaluation is invalid"** — While the fidelity measurement is underspecified and the comparison is questionable, this does not invalidate the entire paper. The core contribution (global subgraph concept extraction) is demonstrated qualitatively through Figure 3 and the qualitative comparisons. The fidelity issue can be resolved with proper specification and re-evaluation.

- **Critic's claim about efficiency comparison being "misleading"** — The paper explicitly acknowledges the difference in output type (lines 202, 206: "Although local-level explanation approaches are not capable of producing global subgraph concepts like our TreeX, we still perform an efficiency comparison"). The comparison is clearly scoped and not misleading.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify fidelity computation.** Specify exactly how TreeX produces "the explanation" G_i^X for each instance: does it select edges belonging to top-weighted concepts, mask the rest, and feed the resulting subgraph through the original GNN? Or does it use the weighted concept sum prediction ŷ = Ψ(w_t K_i M)? If the former, describe the selection procedure (threshold or top-k). If the latter, this should be clearly distinguished from the subgraph-masking procedure used by baselines, and the comparison should be reframed or removed.

2. **Implement proper train/test separation.** Perform concept mining (local clustering, global clustering, weight learning) exclusively on the training set. Evaluate fidelity on a held-out test set. Report whether global concepts from training data generalize to test instances.

3. **Specify the GNN architecture.** State explicitly which GNN model (GIN with how many layers, what hidden dimension, how trained) was used in experiments.

4. **Validate the clustering assumption.** Add a small-scale experiment showing that clusters of node embeddings correspond to structurally similar subtrees (e.g., intra-cluster vs. inter-cluster graph edit distance).

## Score and Decision

This paper introduces a genuinely novel approach to global GNN explainability and provides compelling qualitative evidence of its effectiveness. However, the quantitative evaluation has two serious issues: (1) the fidelity comparison against local methods is underspecified to the point where it is unclear whether the same quantity is being measured, and (2) the concept extraction may use test data, invalidating the evaluation's statistical validity. These are fixable with better experimental design, but in their current form they undermine the paper's strongest quantitative claims. I recommend rejection with encouragement to resubmit after addressing these issues.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>