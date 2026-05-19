- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3
Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces **graph reconstructability** — whether GNN node embeddings retain enough information to recover the input adjacency matrix — as a new lens for analyzing GNN expressiveness, moving beyond the standard WL-test-based (graph-level) perspective to a node/edge-level one. The authors derive precise theoretical conditions under which GCN and GIN can reconstruct the graph using either identity features or contextual features (Propositions 2–5). To address the quadratic scaling cost of identity features and the homophily dependence of contextual features, they propose **Nearly Orthogonal Random Features (NORF)** and a generalized **Graph Reconstructable Neural Network (GRNN)** framework. The key theoretical result (Corollary 1) is that NORF reduces the embedding dimensionality from O(|V|) to O(log|V|) while provably preserving reconstructability. Synthetic experiments confirm the predicted trends, and experiments on real graphs show GRNN with NORF achieves high AUC on both assortative and disassortative graphs.

## Strengths

- **Novel theoretical lens for GNN expressivity.** Graph reconstructability shifts the focus from graph-level isomorphism detection (the WL-test paradigm) to whether embeddings preserve local topological structure — a perspective that directly connects to node-level tasks like link prediction and community detection. This is a genuinely different and well-motivated framing.
- **Explicit, testable conditions for GCN and GIN.** Propositions 2–5 derive precise inequalities (e.g., ε > D/2 − 1 for GIN with identity features; ρ > 1/|C| for GIN with contextual features) that characterize when these models preserve reconstructability. These are fine-grained predictions grounded in concrete architectural choices, going beyond the coarse "as powerful as 1-WL" statements common in the literature.
- **NORF and dimensionality reduction (Theorems 1–2, Corollary 1).** The paper proves that NORF can replace one-hot identity features while requiring only O(log|V|) dimensions, eliminating the O(|V|²) memory cost of identity features while maintaining the orthogonality bounds needed for reconstructability. This is a clean theoretical result with practical implications.
- **GRNN as a unifying framework (Theorem 3).** The paper shows that GCN, GIN, and attention-based aggregation are all special cases of GRNN, and the dimensionality bound (O(∥w∥₁⁴ log|V|)) explains why normalized aggregation (GCN, GAT) is provably more dimension-efficient than unnormalized aggregation (GIN).
- **Synthetic experiments that directly test theoretical predictions.** Figure 1 systematically varies homophily, noise, degree, and dimensionality, and the trends match the theoretical conditions (e.g., GCN's reconstructability collapses when noise exceeds the predicted threshold σ₀ > 2σ₁; GIN's reconstructability degrades when ε < D/2).

## Weaknesses

### Fatal
None.

### Major
- **Downstream task comparisons (Tables 2, 3) conflate feature advantage with architectural advantage.** The paper reports that GRNN with contextual+NORF outperforms baselines (GCN, GIN, GAT, SGC, SEAL, CommDGI), but the baselines are evaluated with only one feature type (typically contextual features). The paper explicitly states "combining NORF and contextual features achieves the highest performance" and "surpasses the performance of previous methods that solely rely on contextual features." To attribute GRNN's superiority to its architecture or reconstructability property (rather than simply having more informative input features), the baselines should also be tested with the contextual+NORF feature combination under identical conditions. Without this controlled ablation, the downstream task evidence for GRNN's architectural advantage is weak. This is fixable but substantially weakens the claim that "retaining graph reconstructability benefits network mining tasks."

### Minor
- **Proposition 1's "if and only if" claim overstates the equivalence between reconstructability and the inner-product condition.** The paper defines reconstructability generally (Definition 1) but then Proposition 1 equates it to the specific condition that linked pairs have strictly larger inner products than unlinked pairs. The "only if" direction (that any reconstructable model must satisfy this inner-product ordering) is not argued or justified; it is one specific sufficient decoder (a logistic/linear threshold). The paper should either adopt the inner-product condition as the *definition* of reconstructability for the purpose of the analysis, or drop the "only if" claim. The theoretical results are internally consistent once this choice is made, but the framing as "if and only if" is imprecise.
- **Propositions 6 and 7 are asserted without proof or rigorous analysis.** Proposition 6 states that AUC can evaluate reconstructability — a near-trivial observation given that AUC measures the ranking of positive vs. negative pairs. Proposition 7 claims that GRNN embeddings approximate an affiliation matrix via symmetric NMF, but no derivation or empirical verification is given. These appear as substantive claims in the main text but function as informal speculation. They should either be removed or moved to the appendix with supporting justification.
- **No standard deviations or error bars reported.** All tables report single-point estimates. With 100,000 synthetic graphs, error bars are expected; for real graphs run over random splits, variance should be quantified. The paper does not mention the number of runs or any measure of variability.

### Trivial
- The GRR metric description in the synthetic experiments is cut off mid-sentence ("#reconstructable graphs"), making it unclear how the reconstructability threshold θ is determined. This should be clarified.

## Nice-to-Haves
- A sensitivity analysis for ε around the theoretically recommended value (e.g., varying ε from 0.5× to 2× the predicted optimal) would strengthen the connection between theory and practice, especially since the GIN bound ε > 2(1+ρ)D is acknowledged as potentially large.
- Including simple non-GNN baselines (e.g., node2vec, spectral clustering) in the downstream tasks would contextualize the absolute AUC/Acc scores and help assess whether reconstructability is a practically useful proxy for performance.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **"The theoretical guarantee for GRNN (Theorem 3) assumes a fixed aggregation weight w, yet GRNN is proposed as a framework that includes learned attention weights."** — REMOVED because it is factually incorrect. For attention-based models (GAT, Graph Transformer), the weights are normalized to sum to 1 via softmax, making ∥w∥₁ = 1 always. Theorem 3's conditions become ε = 0.5 and 4/13 > δ, which hold uniformly regardless of the specific learned attention values. The theoretical guarantee does extend to attention models; the critic overlooked the normalization property stated in the paper (line 172: "their weights are normalized to O(1) by softmax function").

2. **"Weakenss about missing related works"** — REMOVED as per instruction.

3. **"Weakness about missing appendix / proofs in appendix"** — REMOVED as per instruction (appendix is stripped during parsing).

4. **General concerns about "the evaluation lacks rigor" without concrete anchors** — REMOVED per discipline rule.

## Novel Insights
The harsh critic's observation that Proposition 1's "if and only if" formulation conflates a definition with a specific sufficient condition is genuinely insightful. The paper's entire theoretical architecture rests on checking whether the inner-product ordering holds, so readers need to know whether the "only if" direction is actually intended or just loose language. Conversely, the strength finder correctly identifies that the dimensionality reduction from O(|V|) to O(log|V|) via NORF is the paper's sharpest result — it cleanly solves a practical bottleneck (identity features don't scale) and is backed by a concrete bound. These two observations together suggest the paper's real value is the NORF+GRNN framework as a *constructive approach* to dimension-efficient reconstructability, while the analysis of existing GNNs (GCN/GIN with contextual features) is more of a supporting motivation. None beyond the paper's own contributions.

## Suggestions
1. **Clarify Proposition 1.** Explicitly state that the paper studies reconstructability *under inner-product decoding* (or equivalently, linear logistic classification), and argue why this is a natural choice (e.g., it mirrors link prediction practice and graph autoencoder decoders). This makes the theoretical results precise rather than over-claimed.
2. **Add controlled ablation for downstream tasks.** Run GCN and GIN with contextual+NORF (same setup as GRNN) to isolate whether GRNN's advantage is architectural or due to richer input features. If GRNN still wins, this strongly supports the reconstructability claim.
3. **Report standard deviations or confidence intervals** for all tables, especially where results are close.
4. **Either provide justification for Propositions 6 and 7 or remove them** from the main body. As currently presented, they inflate the claimed contributions without support.
5. **Clarify the GRR metric** by completing the description of how the reconstructability threshold is determined for synthetic graphs.
