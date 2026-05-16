Thank you for the thorough paper and reviews. I have carefully verified each claim against the actual paper content. Let me construct the consolidated review.

---

## Summary

TreeX proposes a post-hoc explainability method for MPGNNs that extracts **global graphical subgraph concepts** (i.e., dataset-level motifs) by mining over the full *L*-hop subtrees produced during message passing — avoiding costly subgraph enumeration. The method clusters node embeddings from the last GNN layer, identifies local concepts via overlapping subtree edges, aggregates these into global concepts, and learns per-class weights. It is one of the first methods to produce explicit subgraph motifs as global explanations while also supporting instance-level explanation. Experiments on synthetic (BA-2Motifs, BAMultiShapes) and real-world (Mutagenicity, NCI1) datasets show faithful motif extraction and competitive local fidelity.

## Strengths

- **Novel problem framing and approach.** The idea of generating global-level *graphical* subgraph concepts (rather than latent prototypes or text rules) by mining over message-passing subtrees is a genuinely underexplored and practically important direction. The paper correctly identifies that existing global explainers either produce non-graphical outputs or cannot apply them to individual instances.

- **Theoretical grounding via Perfect Rooted Tree Representation.** Theorem 4.2 proves that for maximally powerful MPGNNs with injective AGG/UPDATE and countable inputs, the *l*-th layer root node embedding is a lossless representation of the full *l*-hop subtree. This provides a principled justification for the method's key design choice — using precomputed node embeddings as subtree representations — bypassing the need for expensive subgraph encoding.

- **Qualitative evidence of meaningful concept extraction.** On BA-2Motifs, TreeX correctly recovers the ground-truth five-node cycle and house motifs. On Mutagenicity, it extracts known mutagenic functional groups (-NO2, -NH2, -N2O) as class-0 patterns. These results directly demonstrate that the extracted subgraph concepts correspond to chemically and structurally meaningful motifs, which is the paper's central claim.

- **Efficiency advantage.** TreeX reduces the search space from *O*(*n*!) (subgraph enumeration) to *O*(*n*) (subtree extraction) per graph. Table 4 shows it is orders of magnitude faster than SubgraphX and competitive with EiG-Search, while additionally producing global concepts those methods cannot provide.

## Weaknesses

### Fatal
None.

### Major

- **The fidelity evaluation protocol for TreeX is under-specified, making the quantitative results difficult to interpret.** The paper does not define how the explanation subgraph *Gᵢ^𝒳* is constructed from the learned concept importances. Section 4.3 describes computing concept importance *Iₜ = K wₜ* for an instance, but never specifies how this importance vector translates to a concrete subgraph for the fidelity computation (AccFidelity/ProbFidelity). Without this specification, the numbers in Tables 1 and 2 cannot be independently verified or compared. This is not a minor omission — the reader cannot tell whether high fidelity reflects genuinely faithful explanations or simply the retention of most of the original graph.

- **No control for explanation size or sparsity in the fidelity comparison.** The paper does not report the average number of edges (or sparsity) of explanations produced by TreeX versus any baseline. If TreeX's explanations are dense (retaining most edges of the original graph), near-perfect AccFidelity is trivial. Local baselines like SubgraphX deliberately produce sparse subgraphs, making the comparison potentially misleading. Reporting explanation size is standard practice in the explainability literature and its absence is a significant methodological gap.

- **The incorrect-prediction analysis is overclaimed.** The paper states that TreeX can "discover the cause of incorrect predictions" and "uncover the reasons behind the incorrect predictions." However, Table 3 simply reports the rate at which a separately learned linear classifier (weighted concept counts) would predict the true class on misclassified instances. This shows the linear classifier disagrees with the original GNN, but it does *not* explain *why* the GNN made its error — it does not identify which concepts the GNN over-relied on or overlooked in its internal computation. The qualitative case study in Figure 4 partially alleviates this (showing a concrete example of concept analysis), but the paper's language throughout Section 4.3 and the framing of Table 3 substantially overstate what has been demonstrated. The claim should be tempered to "a method for analyzing which concepts differ between predicted and true classes" rather than "discovering causes."

### Minor

- **Key hyperparameters unreported.** The paper does not report the values of *k* (local clusters), *m* (initial global clusters), or *λ* (L2 penalty weight) for any dataset. These are critical for reproducibility and understanding the method's behavior. They may appear in the appendix (which the parser strips), but should be summarized in the main text.

- **The edge-extraction heuristic lacks analysis.** Equations (3–4) define a local concept by taking edges that appear in the maximum number of subtrees within a cluster. This heuristic may produce disconnected subgraphs, and there is no discussion of whether the extracted subgraphs are connected or interpretable. The paper also does not analyze whether the mode-based edge selection is robust or whether alternative aggregation strategies (e.g., thresholding) would change results.

- **No ablation studies.** The paper does not ablate any of its design choices (clustering algorithm, number of clusters, edge-extraction heuristic, L2 penalty strength). Given that the method has several tunable components, the lack of sensitivity analysis makes it difficult to assess robustness.

- **GNN architecture details are only implied.** The paper states it "focuses on explaining the maximally powerful MPGNNs" and gives GIN as an example, but does not explicitly state the exact architecture (number of layers, hidden dimensions, pooling method) used in experiments. This should be stated in the experimental setup.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment on synthetic BA-2Motifs quantifying whether extracted concepts are *isomorphic* to ground-truth motifs (beyond visual similarity) and whether the extraction is stable across multiple runs.
- Discussion of limitations — particularly the strong injectivity assumption for Theorem 4.2, the heuristic nature of the edge-extraction step, and how violations affect practical performance.

## Removed Points
*These points were flagged for removal per meta-review guidelines; treat them with caution.*

- **"No analysis on synthetic data with known ground-truth motifs"** — The paper *does* evaluate on BA-2Motifs (which has known 5-node cycle and house motifs) and shows that TreeX extracts them correctly (Figure 3, Section 5.2). The reviewer's valid underlying concern is about *rigor* (quantitative isomorphism verification, stability), not absence of analysis.
- **"No experiments on non-molecular datasets"** — Factually incorrect. BA-2Motifs and BAMultiShapes are synthetic non-molecular datasets (Barabási–Albert graphs with inserted motifs).
- **"No public code or checkpoints"** — Per guidelines, questioning the existence/release status of artifacts cited in the paper is not a valid criticism.
- **"Missing appendix results" / missing comparisons** — Parser-stripped content; the original submission contains these in the appendix.
- **Missing related works** — Cannot be verified without external sources.
- **Formatting/style nitpicks and typo claims** — Parser artifacts, not author errors.

## Novel Insights

The reviews surface one genuinely novel insight that the paper itself does not emphasize enough: the pipeline from subtree extraction → clustering → edge-overlap extraction creates an inherent tension between the theoretical guarantee (Theorem 4.2: node embeddings perfectly represent subtrees) and the heuristic nature of the subsequent steps (k-means on those embeddings, mode-based edge selection). The theory guarantees that similar embeddings → isomorphic subtrees, but the step of aggregating edges via a mode across a cluster has no analogous guarantee. This gap between the theoretically grounded component and the heuristic downstream processing is where future work could provide the most impact — either by designing a principled aggregation step that preserves the theoretical guarantees or by empirically characterizing when the heuristic fails.

## Suggestions

1. **Explicitly define how *Gᵢ^𝒳* is constructed** from the concept importance vector. Is it a thresholded subgraph (keep edges with importance > τ)? A union of top-weighted concepts? The fidelity results are uninterpretable without this.
2. **Report explanation size** (average edge/node count) for all methods in the fidelity comparison, and show that TreeX achieves high fidelity even when explanations are comparably sparse.
3. **Temper the claims about discovering "causes" of incorrect predictions.** Rephrase to "analyzing which concepts differ between the predicted and true classes" and provide more detailed case studies (e.g., concept importance breakdown per class for individual misclassified instances).
4. **Add a controlled experiment on BA-2Motifs** verifying that extracted global concepts are isomorphic to the ground-truth motifs, with stability metrics across runs.
5. **Report hyperparameters** *k*, *m*, *λ* in the main text and include a sensitivity ablation on at least one dataset.

## Score and Decision

The paper tackles an important and genuinely underexplored problem, proposes a novel approach with a sound theoretical kernel, and provides encouraging qualitative results. However, the fidelity evaluation is under-specified to the point of being uninterpretable, the incorrect-prediction analysis claims more than it demonstrates, and missing controls (explanation size, hyperparameters, ablations) weaken the empirical contribution. These are significant but addressable issues — they do not invalidate the core idea, but they prevent the contribution from being firmly established in the current form.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>