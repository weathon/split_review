- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5
Good. I now have a thorough understanding. Let me write the consolidated review.

## Summary

This paper proposes CurGL, a curriculum learning framework for aligning GNNs and LLMs on text-attributed graphs (TAGs). It identifies the "text-structure imbalance" problem — nodes exhibit varying difficulty levels in learning textual vs. structural information. CurGL addresses this via: (1) a text-structure difficulty measurer combining global center-boundary detection with prediction confidence, (2) a class-based node selection strategy to maintain subgraph balance while scheduling nodes by difficulty, and (3) a curriculum co-play alignment that iteratively exchanges pseudo-labels between GNN and LLM. Experiments on five TAG datasets (Cora, Citeseer, Pubmed, Ogbn-arxiv, WikiCS) show gains over baselines.

## Strengths

- **Clear problem formulation and motivation.** The paper identifies a genuine and under-explored issue — the text-structure imbalance across nodes in TAGs — and provides concrete illustrative examples (Figure 1) showing how text difficulty varies descriptively and structure difficulty varies by boundary-vs-center position. This framing convincingly motivates the need for a curriculum approach.

- **Novel integration of global structure difficulty with text difficulty for curriculum node selection.** The structure difficulty measurer (extending Class-Conditional Betweenness Centrality from Wu et al., 2024) provides a principled, global view of topological learning difficulty per node, going beyond the local neighbor-diversity measures used in prior curriculum graph learning methods like CLNode and TSS. Combining this with text difficulty derived from model confidence is a meaningful architectural contribution.

- **Ablation study confirms all three components contribute.** Figure 3 shows that removing the pseudo-label strategy, the class-based node selection, and the text-structure difficulty measurer each degrades performance, providing direct evidence that each proposed module plays a role. The training dynamics (Figure 5c,d) further show progressive improvement of both GNN and LLM.

- **Competitive empirical results across five datasets.** The method reports improvements over baseline categories on five real-world TAG datasets, including a large-scale benchmark (Ogbn-arxiv) and a more challenging web graph (WikiCS), suggesting the approach transfers beyond small citation networks.

## Weaknesses

### Fatal
None.

### Major

- **Baseline methods are not explicitly enumerated in the text.** The Experiment section (Sec 4.1) describes baselines only as broad categories ("GNNs, Curriculum Graph Learning, Pretrained Language Models, and GraphLLM methods") and references two benchmark papers (Jin et al., 2023a; Li et al., 2023c) but does not list the specific algorithms compared against. The main results table (Table 1) is an image in the parsed version, so the information may be present there, but the paper body itself never states which existing methods were included or which contemporaneous approaches (e.g., GLEM, PATTON, CLNode, TSS, which are all discussed in Related Work) are among the baselines. This under-specification makes the claimed "state-of-the-art" performance difficult to verify from the text alone, and creates a disconnect between the methods discussed in Related Work and those actually compared.

- **Computational cost of the structure difficulty measurer is unaddressed.** The global center-boundary detection (Equation 1) requires computing all-pairs shortest-path betweenness contributions — for each node, summing over pairs of nodes from different classes (boundary term) and pairs from the same class (center term). For Ogbn-arxiv (~170K nodes), exact computation is prohibitive. The paper reports no runtime, memory usage, approximation strategy, or complexity analysis. While the results were evidently obtained, the lack of any discussion about how this component scales is a significant practical gap for a method that aspires to be generally applicable.

### Minor

- **Only one backbone LLM (Sentence-BERT) and one GNN (GraphSAGE) are tested.** The paper claims CurGL is a general alignment framework, but provides no experiments with alternative text encoders (e.g., a larger BERT variant, LLaMA) or GNN architectures (e.g., GCN, GAT). While using the standard setup from the GraphLLM benchmark is defensible, the claim of generality remains unevidenced.

- **No statistical variance is reported for any result.** All tables and figures present single numbers without standard deviations, confidence intervals, or even a statement about number of runs. Given randomness in graph splits, initialization, and pseudo-labeling, this makes it impossible to assess whether the reported improvements over baselines are statistically meaningful.

- **The ablation study does not specify which dataset(s) it was conducted on.** Figure 3 and the surrounding text in Section 4.2 describe performance drops when each module is removed, but never state whether these results are on Cora, Citeseer, or another dataset. The hyperparameter and selection strategy analyses (Figures 4, 5) are explicitly on Cora and Citeseer; it is unclear whether the ablation covers the larger datasets as well.

- **The definition of text difficulty $D_t(v) = 1 - \hat{\mathbf{y}}_v$ is notationally inconsistent.** In the problem formulation (Section 2), $\hat{\mathbf{y}}_v = \text{Softmax}(\text{MLP}(\mathbf{h}_v))$, making $\hat{\mathbf{y}}_v$ a probability vector (bounded [0,1]). In the method section (line 101), $\hat{\mathbf{y}}_v$ is called "output logits" (unbounded). If $\hat{\mathbf{y}}_v$ is a vector, $1 - \hat{\mathbf{y}}_v$ is elementwise and ambiguous without specifying which component (e.g., $1 - \hat{y}_{v,c}$ for the ground-truth class $c$). The intention (uncertainty or error probability) is clear, but the notation needs correction.

### Trivial
None.

## Nice-to-Haves

- Running the ablation study on at least one larger dataset (e.g., Ogbn-arxiv) would strengthen confidence that the benefits of the curriculum design hold beyond small citation networks.
- Reporting the fraction of nodes selected at each curriculum stage and the overall pseudo-label accuracy would help assess confirmation-bias risk.
- Adding a comparison with at least one backbone variation (e.g., GCN instead of GraphSAGE) on the smaller datasets would provide useful evidence of generality.

## Removed Points

- *Structure difficulty equation incompletely described*: The harsh critic claimed the summations over pairs (u,v) are "only vaguely specified." In fact, the paper text clearly explains: the first term sums over node pairs from different classes (boundary detection), and the second term sums over pairs from the same class (center detection). The description, while lacking explicit index set notation in the parsed text (the equation itself is an image), is adequate for reproducibility. **Removed because the concern is factually unsupported by the paper's exposition.**

- *Missing related works*: The harsh critic suggested the paper should soften its novelty claim given CLNode and TSS. The paper already acknowledges these methods in the Related Work section and correctly differentiates its contribution (joint text-structure difficulty for alignment). **Removed per instructions: I cannot verify missing related works without external sources.**

- *Missing appendix/proofs*: Various references to missing content. **Removed per instructions: the parser strips these sections; they exist in the original submission.**

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on CurGL that the paper itself does not already articulate.

## Suggestions

1. **Name every baseline method explicitly** in the experiment section (either in the body or in a dedicated table header). If the table already does this, state so in the text (e.g., "See Table 1 for the complete baseline list").
2. **Add a complexity analysis or approximation scheme** for the structure difficulty measurer. Even a brief statement (e.g., "we compute shortest paths via Brandes' algorithm with landmark sampling") would substantially address the practical concern.
3. **Report standard deviations** over at least 3–5 runs for all main results.
4. **Fix the $D_t(v)$ notation**: specify that $\hat{y}_v$ refers to the softmax probability of the ground-truth (or pseudo-label) class, not raw logits, and state $D_t(v) = 1 - \hat{y}_{v, c_{\text{true}}}$.
5. **State the dataset(s)** used in the ablation study explicitly in Section 4.2.
