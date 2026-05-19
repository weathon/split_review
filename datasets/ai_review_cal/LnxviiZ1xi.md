- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper introduces MPXGAT, an attention-based deep learning model for multiplex graph embedding that separates intra-layer (horizontal) and inter-layer (vertical) processing through two sub-models (MPXGAT-H and MPXGAT-V). The model uses GAT-based attention mechanisms and a custom function that combines horizontal and vertical embeddings via a learned weighting parameter β. Experiments on three benchmark datasets (arXiv, Drosophila, ff-tw-yt) evaluate AUC for link prediction, comparing against GraphSAGE, GATNE, and MultiplexSAGE.

## Strengths

- **Superior inter-layer link prediction across all datasets (evidenced by Table 1):** MPXGAT achieves the highest inter-layer AUC on ff-tw-yt (0.83 vs. next best 0.62), Drosophila (0.86 vs. 0.77), and arXiv (0.84 vs. 0.83), outperforming all three baselines including the dedicated multiplex method MultiplexSAGE. This is the primary task the model was designed for.

- **Best overall (weighted) performance on all benchmarks (evidenced by Table 2):** The cumulative weighted AUC shows MPXGAT scoring highest on ff-tw-yt (0.78), Drosophila (0.80), and arXiv (0.82). This supports the claim that when considering both link types jointly, MPXGAT is the most effective method.

- **Ablation experiments validate the dual-embedding architecture (evidenced by Tables 3 & 4):** Replacing MPXGAT-V with a standard GAT (removing horizontal embeddings from vertical processing) significantly degrades inter-layer AUC across all datasets (e.g., ff-tw-yt: 0.83→0.72) with p-values < 1e-6. A second ablation replacing meaningful horizontal embeddings with random ones degrades performance on two of three datasets. These experiments demonstrate that the separation of horizontal and vertical processing is beneficial.

- **Addresses a clear gap in prior work (evidenced by Section 1):** The paper identifies that many existing multiplex embedding methods assume all nodes appear in every layer or all inter-layer links are known — assumptions that fail in real-world incomplete networks. MPXGAT explicitly relaxes these assumptions, targeting inter-layer link prediction in heterogeneous, incomplete multiplex networks.

## Weaknesses

### Fatal
None.

### Major

- **Abstract overstates performance relative to intra-layer results.** The abstract claims MPXGAT "consistently outperforms state-of-the-art competing algorithms." However, Table 1 shows GATNE achieves higher intra-layer AUC on all three datasets (e.g., 0.91 vs. 0.80 on arXiv; 0.83 vs. 0.76 on ff-tw-yt). MPXGAT dominates on inter-layer and overall performance, but the blanket "consistently outperforms" claim is misleading without qualification. The paper's own body text acknowledges this more honestly ("MPXGAT has comparable performances with GATNE on the ff-ww-tt and the Drosophila dataset, while the latter performs better on the arXiv dataset") — the abstract and highlights should be revised to match.

- **Test set composition is not reported, making the weighted AUC unverifiable.** The overall AUC (Table 2) is computed as "a weighted sum based on the number of edges used to evaluate the models." However, the paper never reports the actual counts or proportions of intra-layer vs. inter-layer edges in the test sets. Given that the test set includes "all inter-layer links among the marked nodes" but only 20% of intra-layer links, an imbalance favoring inter-layer edges would tilt the weighted metric toward MPXGAT's strength. Without these counts, the reader cannot assess whether the overall advantage reflects genuine superiority or test set composition.

- **Limited baseline set for a "state-of-the-art" claim.** Only three baselines are compared. GraphSAGE is a single-layer method applied without distinguishing layers, making it a weak baseline. GATNE is adapted from heterogeneous graph embedding. Only MultiplexSAGE is a directly comparable multiplex-specific method. While the paper justifies excluding several methods (they assume full inter-layer knowledge), there exist other multiplex embedding approaches that relax similar assumptions (e.g., DMGI). The claim of outperforming "state-of-the-art" would be strengthened by a broader set of relevant comparisons.

### Minor

- **Horizontal embeddings contribute nothing on one dataset.** The random-embedding ablation (Table 4) shows that on Drosophila, replacing true horizontal embeddings with random vectors yields identical inter-layer AUC (0.86 ± 0.01, p=0.75). This means the horizontal embeddings provide no signal on this dataset. The paper acknowledges this but offers only a speculation ("conjecture that this outcome is due to the structure of the multiplex network") without supporting analysis. While the core architecture (having any horizontal stream) still helps on Drosophila (Table 3 shows MPXGAT-V beats plain GAT), the specific horizontal embedding values are irrelevant there, which limits the generality of the design's benefit.

- **Learned β parameter is not analyzed.** The model includes a learned scalar β that balances horizontal and vertical information (Eq. 11). Its learned values across datasets are never reported or discussed, which would provide insight into how the model adapts to different network structures.

- **Inter-layer clique assumption not discussed.** The paper assumes transitivity of inter-layer connections (if A↔B and B↔C, then A↔C, forming cliques in the vertical network). This is clearly stated (lines 86-87) but its implications for real-world networks where this assumption may fail are not discussed.

### Trivial
None.

## Nice-to-Haves

- Report hyperparameter ranges and optimal values from the grid search (number of attention heads, hidden dimensions, learning rate, epochs).
- Report the learned β values for each dataset to show how the model trades off horizontal vs. vertical information.
- Add runtime or complexity analysis comparing MPXGAT against baselines.
- Ablate the design choices that deviate from standard GAT (separate source/target weight matrices, summation vs. concatenation, bias terms) to isolate which choices drive performance gains.

## Removed Points

- *"Hyperparameter details are entirely absent — ranges, optimal values... This makes reproduction impossible."* — Removed per the hard rule on reproducibility nitpicks about undisclosed hyperparameters.
- *"No code or data availability statement."* — The datasets are cited from prior work; code release is a standard expectation but not a structural weakness of the paper's scientific content.
- *"The paper claims 'none of these methods can solve the problem of predicting links between different layers' which is contradicted by the paper's own discussion of MultiplexSAGE."* — Factually wrong. The paper's "none of these methods" (line 48) refers to the set of methods listed immediately prior (line 47), not including MultiplexSAGE, which is separately introduced as a very recent exception (line 52).
- *"The ablation comparing MPXGAT-V vs. standard GAT conflates the effect of the vertical network design with the effect of horizontal embeddings... standard GAT does not have access to the same information — it lacks the horizontal embeddings AND the inter-layer connectivity structure."* — Factually wrong. The standard GAT is applied to the vertical network and therefore does have access to the same inter-layer connectivity structure; only the horizontal embeddings differ.
- *"On arXiv, GATNE's intra-layer AUC (0.91) substantially exceeds MPXGAT's (0.80), and even MultiplexSAGE (0.71) and GraphSAGE (0.72) are not far behind."* — The comparison of MultiplexSAGE/GraphSAGE to MPXGAT is misrepresented; MPXGAT (0.80) is substantially ahead of both (0.71, 0.72), so claiming they "are not far behind" is misleading relative to the actual numbers.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Revise the abstract and highlights** to accurately reflect where MPXGAT excels (inter-layer prediction) and where it is competitive but not best (intra-layer). A framing such as "achieves superior inter-layer link prediction and best overall performance" would be accurate and honest.
2. **Report test set edge counts** (intra-layer and inter-layer counts) for each dataset so readers can interpret the weighted overall AUC in Table 2. Show both the raw counts and the proportions that determine the weighting.
3. **Add at least one more multiplex-specific baseline**, such as DMGI, to strengthen the "state-of-the-art" claim.
4. **Investigate and discuss why horizontal embeddings fail to help on Drosophila**, even briefly — e.g., whether this is due to extreme sparsity, layer structure, or the inter-layer graph already capturing the relevant signal.
5. **Report learned β values** across datasets to give insight into how the model balances information sources.

---
