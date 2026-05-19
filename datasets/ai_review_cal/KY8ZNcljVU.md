- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes NetInfoF, a framework for measuring and exploiting network usable information (NUI) in node-attributed graphs. The framework has two modules: NetInfoA, which computes a score (2^{-H(Y|X)}) that lower-bounds prediction accuracy without training a GNN, and NetInfoM, which solves link prediction and node classification using the same derived embeddings. The method derives five components capturing structure, neighborhood, features, and propagated features, and introduces a compatibility matrix with closed-form optimization to handle heterophily in link prediction.

## Strengths

1. **Principled theoretical framework for NUI measurement.** Theorems 1 and 2 (Section 3) prove that 2^{-H(Y|X)} lower-bounds accuracy, providing a formal, model-agnostic grounding for measuring usable information in graph data. This is a cleaner approach than V-information methods that require expensive model training.

2. **Strong link prediction performance against general GNNs.** Table 7 shows NetInfoM wins in 11 out of 12 real-world datasets (covering both homophily and heterophily graphs) against six GNN baselines (GCN, SAGE, GAT, H²GCN, GPR-GNN, SlimG), achieving an average rank of 1.1. The results are consistent across diverse datasets.

3. **Robustness across all synthetic graph scenarios.** Table 1 demonstrates that NetInfoF achieves average rank 1.0 across six synthetic scenarios (cross-product of Random/Global/Local features × Diagonal/Off-diagonal structure), while every baseline fails in at least one scenario. This provides strong evidence that the method correctly handles diverse graph conditions.

4. **Linear scalability with empirical validation.** Lemma 3 provides complexity analysis, and Figure 5 demonstrates empirical linear scaling on graphs up to millions of edges (Products, Twitch, Pokec). The coefficient selection technique (T2) reduces the effective number of parameters from O(d²) to a much smaller practical number.

5. **Parameter efficiency.** On OGB datasets (Table 6), NetInfoF uses only 1,280 learnable parameters versus 279K+ for GCN/SAGE, yet achieves the best results among general GNN baselines on ogbl-ddi, ogbl-collab, and ogbl-ppa.

## Weaknesses

### Fatal
None.

### Major

- **Generality claim partially unsubstantiated in the main text.** The paper lists "General, handling both link prediction and node classification" as its first advantage. While Section 5 fully describes the method for node classification, and synthetic node classification results appear in Figure 3, all real-world experimental results in the main text are for link prediction only. The paper states (line 592) that node classification real-world experiments are in the appendix "because of space limit," which is common practice, but the prominence of this claim relative to the presented evidence creates a gap. A compact summary table of real-world node classification results in the main paper would substantiate this central claim.

- **No ablation on the five embedding components.** The ablation study (Table 8) only examines the compatibility matrix variants (w/o CM, w/ only H, full H*). It does not ablate the five embedding components (C1–C5) to determine which are essential. Given that the framework's design is built around these five components, understanding each component's marginal contribution would significantly strengthen the paper.

### Minor

- **Complexity bound includes a potentially dominant d⁴|E| term.** Lemma 3 states O(f²|V| + f³ + d⁴|E|). With d=128, the d⁴ factor is ~268 million. The paper mitigates this via coefficient selection (T2, reducing effective coefficients from O(d²) to a smaller number) and provides empirical evidence of linear scaling (Figure 5). However, the stated complexity without qualification could be misleading, and the empirical linearity has only been shown on a limited set of datasets and dimensions.

- **Baseline comparisons are scoped narrowly.** The paper explicitly states it compares against "general GNN baselines" (line 599), and the abstract qualifies its claim accordingly ("compared to general GNN baselines"). However, the absence of even simple structure-based link prediction heuristics (e.g., Common Neighbors, Adamic-Adar) or classical matrix factorization makes it harder for readers to calibrate the results against well-understood reference points. This is a missed opportunity to contextualize performance, not a flaw in the claims as stated.

### Trivial
None.

## Nice-to-Have

- **Ablation on the five embedding components** (C1–C5) to quantify the contribution of each component, similar to the existing ablation on compatibility matrices.
- **Statistical significance tests** (e.g., Wilcoxon signed-rank across datasets) to strengthen the claim that NetInfoF significantly outperforms baselines.
- **A compact summary of real-world node classification results** in the main paper — even a single table row — to directly substantiate the generality claim.
- **Sensitivity analysis** for the free parameters (k_PPR, T, k_row, k_sym) to strengthen claims of robustness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Node classification results absent is a structural evidential gap / fatal."** The paper explicitly notes (line 592) this is due to space limits, devotes Section 5 to the node classification method, and shows synthetic node classification results in Figure 3. Real-world results are in the appendix. This is a standard trade-off, not fatal.
- **"Missing specialized LP baselines (SEAL, Neo-GNN, BUDDY)" and "OGB results far below SOTA."** The paper explicitly scopes its comparison to "general GNN baselines" (line 599, abstract). Specialized LP methods are outside this scope.
- **"No description of baseline adaptation for LP" and "no hyperparameter tuning."** These details are in Appx. \ref{app:rep} per line 591. Standard practice to defer such details.
- **"Theoretical guarantee has practical caveats not discussed."** The bound holds exactly on the discretized data (the variables are made discrete before computing entropy). The paper describes the discretization procedure (lines 375–380).
- **"Without any model training is misleading"** regarding NetInfoA. The closed-form estimation of H* (multi-target linear regression) and discretizer fitting are standard linear algebra operations, not "model training" as the term is used in the GNN context. The contrast with expensive GNN training is clear.
- **"Formatting issues (placeholder comments, rotated text in Table 1)."** Parser artifacts; the original submission does not have these.
- **"Synthetic datasets are too small"** — the paper does not report sizes, but this is speculation; the key point is the diversity of scenarios, not size.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the paper itself does not already make or imply.

## Suggestions

1. Include a compact table (or at minimum a summary paragraph) of real-world node classification results in the main text to directly substantiate the generality claim.
2. Add an ablation study removing each of the five embedding components (C1–C5) to demonstrate which are necessary.
3. Qualify the d⁴|E| complexity term by noting the coefficient selection reduction, or provide the amortized complexity after applying T2.
4. Add simple structure-based LP baselines (Common Neighbors, Adamic-Adar, matrix factorization) to help readers calibrate against well-understood methods.
