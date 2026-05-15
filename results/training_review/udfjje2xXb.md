Good — I've verified all claims against the paper. Let me now write the consolidated review.

## Summary

This paper proposes GKAN (Graph Kolmogorov–Arnold Network), which replaces the fixed activation functions in standard message-passing GNNs with learnable spline-based activations on edges, inspired by KANs. The claim is twofold: (1) improved accuracy over established GNN architectures across node classification, link prediction, and graph classification, and (2) inherent interpretability through visualization of the learned spline weights without relying on post-hoc explainers.

## Strengths

- **Timely and motivated architecture.** Applying KANs to graph-structured data is a natural and potentially fruitful direction given the growing emphasis on interpretability in GNNs. The paper identifies a genuine gap (GNNs as black boxes) and proposes a clean architectural modification.

- **Clear and reproducible mathematical formulation.** Section II-B provides explicit layer-wise update rules for GKAN, including message passing with spline-based activations, aggregation (add/mean), and node update. The equations for the spline activation function (basis + B-spline) are given, enabling reproduction.

- **Honest computational cost disclosure.** Table 3 reports that a single GKAN epoch takes 2.052 s on an M1 processor, three orders of magnitude slower than GCN (0.0016 s). The paper openly acknowledges this accuracy/interpretability vs. speed trade-off rather than hiding it.

- **Explicit limitations section.** Section IV-A lists three concrete limitations (memory usage, lack of edge features, and nuance about interpretability depth), demonstrating a realistic assessment of the method's current scope.

## Weaknesses

### Fatal
None.

### Major

- **PubMed/CiteSeer dataset statistics are swapped in Table 1.** Standard Planetoid statistics are: CiteSeer 3,327 nodes / 9,104 edges / 3,703 features / 6 classes; PubMed 19,717 nodes / 88,648 edges / 500 features / 3 classes. The paper lists PubMed with 3,327 nodes / 9,104 edges / 3,703 features / 6 classes and CiteSeer with 19,717 nodes / 88,648 edges / 500 features / 3 classes — a complete swap. While the actual experiments may have used the correctly named datasets (since they load from PyTorch Geometric by name), this error in the table fundamentally undermines reader trust in the reported results and metadata.

- **No variance or statistical significance reported.** The paper states results are "averaging over 100 runs" (line 371) yet Table 2 reports only single numbers with no standard deviations, confidence intervals, or significance tests. Given that improvements on some datasets are modest (e.g., 69.4 vs. 68.2 on CiteSeer node classification), we cannot assess whether these differences are meaningful relative to run-to-run noise. This is especially problematic for small datasets like MUTAG (188 graphs).

- **Baseline selection weakens the "state-of-the-art" claim.** The paper compares only against GCN (2017), GAT (2018), and GraphSAGE (2017) — architectures now 7–8 years old. GIN (2019) is cited in the introduction but not included as a baseline. Additionally, reported baseline numbers are below typical published results (e.g., Cora GCN: 76.3% vs. typical ~81.5%; MUTAG GCN: 71.3% vs. typical ~80-85%), likely because the paper uses non-standard 80/10/10 train/val/test splits instead of the standard Planetoid fixed splits. While comparisons within this setup may be internally consistent, the claimed "outperforms state-of-the-art GNN models" is not supported when the baselines are neither state-of-the-art nor configured comparably to the literature.

- **Interpretability claim is unvalidated by quantitative evidence.** The abstract claims GKAN provides "clear insights into the model's decision-making process, eliminating the need for post-hoc explainability techniques," but the evidence is purely qualitative: two figures showing normalized spline weights compared against GNNExplainer edge masks. No faithfulness metrics (fidelity, sparsity, ROC-AUC), no controlled synthetic experiments, no user studies are provided. The limitations section (line 546-548) partially walks this back: "we do not claim that GKAN is interpretable, but that it is more interpretable than other models." This tension between the strong framing in the abstract/contributions and the qualified language in the limitations is a significant issue.

- **Hyperparameter tuning asymmetry.** GKAN underwent an extensive grid search over 8 hyperparameters (learning rate, hidden channels, dropout, layers, spline grid size, spline degree, aggregation, L2-regularization), while baselines simply used "guidelines and hyperparameters provided by their authors" (line 348–349) with no specific citations to the exact settings used. This creates uncertainty about whether GKAN's gains come from the architecture or from more favorable hyperparameter tuning.

### Minor

- **Pruning and symbolification are described but never used.** Section II-A describes the full KAN interpretability pipeline (sparsity regularization → pruning → symbolification), but experiments never apply these steps to GKAN. This creates a gap between the described methodology and what is actually evaluated.

- **Training time disparity is not factored into the comparison.** GKAN is ~1,000× slower per epoch than GCN (2.052s vs. 0.0016s). While the paper is transparent about this, a fairer comparison would also evaluate whether matching the compute budget (e.g., training baselines longer or with more capacity) closes the accuracy gap.

- **Link prediction on PubMed contradicts the overall claim.** GKAN scores 82.3 AUC-ROC on PubMed link prediction vs. GCN's 90.6 — a substantial deficit. The paper does acknowledge this ("with the single exception of the link prediction with PubMed"), but the exception is notable and is mentioned only in a sentence rather than analyzed.

- **No theoretical justification for why splines improve graph learning specifically.** The paper shows that spline activations work better empirically but does not offer any analysis of why this architectural choice is particularly suited to graph-structured data versus, say, increased model capacity through wider layers or deeper networks.

### Trivial
- "teset" typo in Table 1 caption (line 336).
- "messsages" typo (line 365).

## Nice-to-Haves
- An ablation that replaces GKAN's spline activations with standard MLP activations in the same architecture, to isolate whether gains come from the KAN mechanism or simply from increased parameterization.
- Inclusion of at least one more modern baseline (e.g., GIN, GCNII) on standard splits to substantiate the "state-of-the-art" claim.
- A controlled synthetic experiment (e.g., a house/cycle motif) to demonstrate that the learned spline weights faithfully recover ground-truth relevant features.

## Removed Points

- **Strength 1 from Strength Finder: "Consistent performance gains over strong baselines"** — REMOVED: Conflicts with verified weakness that baselines are old, their numbers are below typical published results, and the comparison uses non-standard splits. The gains in Table 2 are factually present in the paper's own setup, but labeling the baselines as "strong" is not supported given the evidence above.
- **Strength 2 from Strength Finder: "Inherent interpretability demonstrated without post-hoc methods"** — REMOVED: Conflicts with verified weakness that the interpretability claim lacks quantitative validation. The paper shows qualitative visualizations, but this falls short of "demonstrating" inherent interpretability, especially given the strong claim in the abstract.
- **Criticism about missing related works (SE-GNN, ProtGNN, concept-based explanations)** — REMOVED per instruction: do not mention missing related works as you cannot independently verify their existence or relevance.
- **Strength Finder strength about "Thorough hyperparameter tuning and reproducibility"** — WEAKENED: moved to Minor weaknesses section as the tuning is thorough for GKAN but asymmetric relative to baselines.
- **Harsh critic's claim that the mathematical formulation is "a restatement of standard message passing"** — KEPT as a minor observation but reframed: it's a reasonable characterization of the contribution, but the paper's contribution is the specific application of KAN splines to GNNs, which is a novel combination even if the message-passing framework is standard.

## Novel Insights

None beyond the paper's own contributions. The reviews identify a consistent pattern: the paper's core idea (spline-based activations on graph edges) is reasonable and timely, but the execution — particularly the baseline selection, lack of variance reporting, dataset table error, and unvalidated interpretability claims — prevents the paper from establishing its stated contributions convincingly.

## Suggestions

1. **Fix the PubMed/CiteSeer table and verify all dataset statistics.** This is a first-order credibility issue: the reader needs confidence that the paper's data is correctly documented.

2. **Report mean ± std for all experiments** since the paper already runs 100 trials per condition.

3. **Include GIN (and ideally one more modern baseline like GCNII) on standard Planetoid splits** to substantiate the "state-of-the-art" claim. At minimum, clarify that the comparison is against commonly used GNN backbones, not the contemporary state of the art.

4. **Either add quantitative interpretability metrics (fidelity, sparsity, ROC-AUC) or soften the interpretability claim in the abstract and contributions** to match what is actually demonstrated. The current gap between the strong framing ("eliminating the need for post-hoc explainability techniques") and the limited evidence is problematic.

5. **Run an ablation experiment** that keeps the GKAN architecture but replaces spline activations with standard activations (ReLU, SiLU) at matched parameter counts, to isolate the source of any accuracy gains.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>