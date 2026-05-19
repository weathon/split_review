- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have all the information needed. Let me produce the consolidated final review.

## Summary

This paper proposes HSDGNN, a hierarchical spatiotemporal graph neural network for multivariate time-series forecasting. The key idea is to organize variables as nodes where each node contains a sub-graph of the variable's attributes, then perform two-level graph convolutions: an intra-attribute sub-graph convolution to capture dependencies among attributes of the same variable, and a spatial diffusion convolution on the dynamic inter-variable graph. A second GRU module processes the temporal evolution of these spatially-aggregated signals. Experiments on four traffic datasets and one electricity dataset show consistent improvements over GNN-based baselines, with up to ~15% relative improvement in MAPE over the strongest baseline DDGCRN.

## Strengths

- **Hierarchical graph modeling with explicit intra-attribute dependency learning**: The paper introduces a sub-graph convolution (Section 3.2, Eq. 3–5) that operates on the attributes of each variable. The ablation study (Table 3) confirms that removing this module (HSDGNN w/o IDLM) degrades performance, and that simply including all attributes without structured intra-dependency modeling (HSDGNN w/o MF) also underperforms the full model. This directly supports the paper's central claim.

- **Temporal modeling of dynamic graph topologies via a second GRU**: The spatial-dependency learning module incorporates GRU₂ (Eq. 11) to process the sequence of diffusion outputs. The ablation (Table 3) shows that removing GRU₂ causes the largest performance drop among all variants, providing strong evidence that capturing temporal dynamics of spatially-aggregated signals (conditioned on the dynamic graph) is beneficial.

- **Consistent state-of-the-art results across five datasets**: Table 1 reports that HSDGNN outperforms all baselines on PEMSD4, PEMSD8, PEMSD5, PEMSD11, and PSML across MAE, RMSE, and MAPE. The improvement over the strongest baseline DDGCRN reaches 15.3% in MAPE on the PSML electricity dataset, with small standard deviations over 10 runs.

- **Favorable model scalability**: Table 2 shows that HSDGNN's parameter count stays nearly constant across datasets of different sizes, unlike ST-AE and SDGL whose parameters grow with the number of variables. This is explicitly noted in Section 4.2 as a practical advantage.

- **Hyperparameter robustness**: Figure 4 demonstrates stable performance across varied embedding dimensions, hidden state dimensions, number of blocks, and diffusion steps, with most configurations outperforming DDGCRN.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Ambiguous description of whether the dynamic graph G is per-time-step or per-window**: In Section 3.2 (Dynamic topology generation), the paper computes G from the temporal fusion T (a sequence of GRU₁ hidden states) and then applies it in diffusion convolution (Eq. 9) with T, followed by GRU₂ processing the temporal sequence. The text does not explicitly state whether G is recomputed at each individual time step within the window or computed once for the entire window. From context, G appears to be computed once per input window (varying across windows, which is what makes it "dynamic"), but this should be stated explicitly for reproducibility. If G is per-window, the claim about modeling "changes in graph topologies" captures topology variation across windows rather than within-window evolution. This is a clarity issue, not a methodological flaw.

- **Limited domain diversity in evaluation**: Four of the five benchmark datasets are traffic measurements from the same Caltrans PeMS system (PEMSD4, PEMSD8, PEMSD5, PEMSD11). While the electricity dataset (PSML) provides a second domain, the paper's claim of testing on "datasets from different domains" is overstated. Adding one more non-traffic domain (e.g., air quality, energy, or human activity) would substantially strengthen evidence of generality.

- **No comparison with strong non-graph forecasting models**: The baseline set is dominated by GNN-based methods plus LSTNet. Transformer-based time-series models (Informer, Autoformer, FEDformer, PatchTST) mentioned in the related work (Section 2.1) are not included. Since the paper claims "state-of-the-art performance" in a general MTSF context, the absence of these competitive non-graph baselines limits the ability to assess whether gains come from the hierarchical graph design specifically or from any strong learned representation. The authors acknowledge transformer models' computational cost, but even one representative comparison would contextualize the results.

- **Overselling of what GRU₂ captures**: The paper claims GRU₂ captures "temporal correlations regarding the changing spatial dependencies" (Section 1) and "the change of graph topology" (Section 3.2). In practice, GRU₂ processes Z (the diffusion output), which is the spatially-aggregated signal conditioned on G — not the graph topology G itself. The temporal dynamics GRU₂ captures are of the aggregated spatial signals, not directly of the topology. The ablation supports GRU₂'s importance, but the framing is slightly overstated.

- **Sparse description of the PSML electricity dataset**: The paper describes PSML only as "minute-level load and renewable energy over 3 years across the US" (Section 4.1). The number of variables, number of attributes, temporal granularity, and train/val/test splits are not reported. This makes it harder to assess how the hierarchical formulation applies to this dataset.

### Trivial

- The notation in several equations could be more precise (e.g., T without subscript in Eq. 6, 𝚿 used without definition). A notation table would improve clarity.

## Nice-to-Haves

- **Visualization of learned intra-attribute graphs**: Showing the learned R matrix for different variables or time points would provide intuitive insight into what the intra-dependency module learns.
- **Simpler baseline for attribute fusion**: Adding a variant that simply concatenates all attributes as input features (without sub-graph convolution) would directly quantify the benefit of the intra-graph structure over a naive approach.
- **Statistical significance tests**: Paired tests or confidence intervals alongside the 10-run means and standard deviations would add rigor to the claim of consistent improvement.

## Removed Points

- **Criticism about "why other attributes are not predicted jointly"**: The paper clearly scopes its problem to predicting the main attribute (Section 3.1, line 65). This is a stated design choice, not an omission.
- **Criticism about R = ReLU(E·E^T) needing more justification**: This is a method design choice. The paper explains it is used as an approximation to avoid computing the Laplacian (Section 3.2, last sentence before Section 3.2's Temporal-dependency learning subsection). Further theoretical analysis would be nice but is not required.
- **Criticism about missing appendix content, proofs, or references**: The parser strips appendices; these exist in the original submission.
- **Reproducibility nitpicks about undisclosed hyperparameters**: The paper provides code in a repository and describes key hyperparameters. The level of detail is appropriate for a conference paper.
- **Criticism about limited hyperparameter range tested (embedding dimensions 4–16)**: The range tested is appropriate for the model dimensions and is sufficient to demonstrate trend.

## Novel Insights

The most notable observation that emerges from synthesizing the reviews and the paper is the interplay between the two GRU modules: the ablation shows that removing GRU₂ (the spatial-module GRU) hurts more than removing GRU₁ (the temporal-module GRU), reversing the natural expectation that the primary temporal component would be more critical. This suggests that the spatial-dependency learning module's second GRU does more than simple temporal smoothing — it integrates information across time steps after spatial diffusion, effectively learning spatiotemporal patterns that neither module alone captures. This insight is implicit in the paper's ablation results and could be explored further.

## Suggestions

1. Clarify in the Dynamic topology generation section whether G is computed per time step or per input window, and if per-window, state explicitly that "dynamic" refers to variation across different input windows.
2. Add at least one non-traffic, non-electricity benchmark (e.g., weather, air quality) to broaden the domain coverage.
3. Include one representative transformer-based time-series baseline (e.g., PatchTST or FEDformer) to position the method within the broader MTSF literature.
4. Provide dataset statistics (number of variables, attributes, time steps, splits) for PSML in the main paper.
5. Tone down the claim that GRU₂ captures "the change of graph topology" — it captures temporal dynamics of signals aggregated via the dynamic graph, which is a closely related but distinct claim.
