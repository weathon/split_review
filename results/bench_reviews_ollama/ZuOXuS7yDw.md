Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

GRAMA introduces an adaptive neural Autoregressive Moving Average (ARMA) framework for Graph Neural Networks that transforms static graph inputs into sequences of graphs via independent MLP projections, then processes these sequences using ARMA recurrence with GNN-based residuals. The method preserves permutation equivariance (unlike prior graph SSM approaches that use heuristic node orderings or random walks) and claims to mitigate oversquashing by enabling long-range information propagation through the ARMA/SSM mechanism.

## Strengths

- **Preservation of permutation equivariance**: GRAMA correctly identifies that prior graph SSM methods (Graph-Mamba's degree-based ordering, random-walk sampling) sacrifice permutation equivariance. By creating sequences in the feature/sequence dimension rather than node-ordering dimension, GRAMA maintains this property—a genuine and important advantage over those approaches.

- **Strong empirical results on long-range tasks**: The feature transfer experiment (Figure 2) is the most compelling evaluation: GRAMA-GCN maintains near-zero error at source-target distance 50 on line, ring, and crossed-ring graphs, while all standard MPNN baselines (GCN, GAT, GraphSAGE, GIN) degrade catastrophically. On graph property prediction (Table 1), GRAMA-GPS achieves the best results across all three tasks (Diameter, SSSP, Eccentricity), outperforming A-DGN and SWAN models designed for long-range propagation.

- **Backbone-agnostic plug-in design**: GRAMA works as a drop-in mechanism compatible with any GNN backbone, demonstrated across GCN, GatedGCN, and GPS. On Peptides-func (Table 2), GRAMA boosts GCN and GatedGCN by more than 11 AP points over their baselines.

- **Clear differentiation from prior ARMA-GNN (Bianchi et al., 2019)**: The paper correctly notes that the prior ARMA(1,1) model uses nonlinearities between steps, preventing SSM conversion, while GRAMA maintains linearity within blocks. Empirically, Table 1 shows GRAMA outperforming ARMA-GNN by an average of 2.4 log10(MSE) points.

## Weaknesses

### Fatal

None.

### Major

- **The "sequence" constructed from independent MLP projections lacks genuine temporal/sequential structure, weakening the theoretical framing.** The paper's central motivation is importing SSM/ARMA machinery to graphs by creating a "sequence." However, the sequence (Eq. 2) is constructed by applying L different learned MLPs to the *same* static node features, creating L copies that differ only by a learned linear+nonlinear projection. The initial "residuals" δ^(ℓ) = f^(ℓ+1) − f^(ℓ) are just differences between these independent projections—not innovations from a genuine temporal process. This does not invalidate the method (the ARMA recurrence still operates on the sequence dimension during the R recurrence steps), but it undermines the paper's claim that it has "solved" the graph-to-sequence problem. The sequence is artificial, and the paper should be more forthright about this—framing it as a learned multi-view embedding that happens to be processable by ARMA, rather than claiming to have found a principled graph-to-sequence transformation.

- **The theoretical analysis of "long-range interactions" (Theorem 4.4) addresses long-range in the artificial sequence dimension, but the paper links it to oversquashing, which is a graph-spatial phenomenon.** The theory proves that roots of the characteristic polynomial closer to the unit circle yield slower decay of the *temporal* state matrix powers. The paper itself acknowledges the two-domain operation ("spatial graph domain via a GNN backbone, and the sequence domain via the ARMA mechanism"), but the concluding claim that Section 4 provides "the theoretical foundation for the employment of GRAMA as a method to address the oversquashing phenomenon in GNNs" overstates what the theory establishes. Information propagation in the *graph spatial* domain is governed by the number of GNN applications (R recurrence steps yield R hops of message passing). The ARMA coefficients control how information from different sequence positions is mixed—which affects what gets propagated, not how far it travels in graph distance. The paper would be significantly stronger if it formally analyzed how the temporal-sequence mixing interacts with the graph-distance propagation, rather than conflating them.

### Minor

- **No ablation comparing ARMA-weighted skip connections against standard residual connections in a same-depth GNN.** Stripped to its essentials, GRAMA's recurrence is an R-step deep GNN with ARMA-weighted skip connections. Without an ablation that replaces the ARMA structure with generic learned residuals at the same depth, we cannot determine whether the ARMA constraint specifically helps or whether depth + skip connections alone explain the gains. This would be the single most informative experiment to validate the ARMA framing.

- **The feature transfer baselines (Figure 2) are mostly 1-2 layer MPNNs, making depth an asymmetric variable.** GRAMA uses R recurrences (each applying one 1-hop GNN), effectively running R layers deep. Comparing against shallow baselines conflates the benefit of depth with the benefit of the ARMA mechanism. A multi-hop or equivalently deep GNN baseline would isolate the ARMA-specific contribution. That said, A-DGN and GPS are included and also perform well, partially addressing this.

- **The claim that computational cost "remains reasonable" (Section 3.1) is unsupported by any measurement.** Each GRAMA block requires L separate MLP projections plus R GNN applications. No wall-clock time, memory usage, or FLOPs are reported, making it difficult to assess practical trade-offs.

### Trivial

- The constraint p=q=R=L (after Eq. 7) seems driven by implementation convenience rather than design principle, and is not justified.

## Nice-to-Haves

- Visualization of the learned ARMA coefficients (φ, θ) on different graph types, to assess whether the ARMA constraint learns meaningful patterns or acts as generic weighted residual connections.
- Formal analysis of how the temporal recurrence depth R relates to effective graph-distance range of information propagation, to substantiate the oversquashing claim with graph-structural rather than temporal-sequence analysis.
- Computational cost comparison (training time, memory) with backbones and other graph SSM methods.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The SSM equivalence (Theorem 4.1) is a well-known result, not a contribution."** — The harsh critic claims this is merely a textbook result from Hamilton (1994). While the ARMA↔SSM equivalence is indeed well-known in time series, the paper's contribution is *applying* this equivalence to derive stability and long-range interaction conditions *in the context of GNNs*. The paper explicitly frames it as "formally casting common knowledge... to the realm of GNNs" rather than claiming novelty of the equivalence itself. Removed as overstated criticism.

- **"GRAMA is functionally equivalent to a multi-layer GNN with learned weighted skip connections and the ARMA framing adds no proven benefit."** — This is a reasonable concern *as an ablation request* (demoted to minor weakness above) but is overstated as a structural refutation. The ARMA structure imposes a specific parameterization on the skip connections (AR coefficients on previous states + MA coefficients on residuals) with stability constraints derived from theory. Whether this specific constraint helps vs. generic residuals is an empirical question, not a logical impossibility. Removed as a fatal/major claim; retained as minor ablation request.

- **"The introduction sets up a straw comparison with prior work."** — The paper's contrast with Graph-Mamba and random-walk methods on permutation equivariance is factually correct and well-documented. This is not a straw comparison. Removed.

- **"Mixed results on heterophilic benchmarks"** — Upon checking Table 4, the results are indeed mixed (e.g., GRAMA-GCN doesn't consistently beat GCN on all heterophilic tasks). However, this is expected—GRAMA is designed for long-range propagation, and heterophilic tasks don't primarily test this. This is at most a minor observation about scope, not a major weakness. Removed as major.

- **Strength finder's claim about "theoretical grounding via SSM equivalence directly supporting oversquashing mitigation"** — As analyzed above, the theoretical grounding supports long-range in the *sequence* dimension, not directly *graph-distance* oversquashing. This claimed strength conflicts with a verified weakness and is removed.

- **Requests for statistical significance tests and confidence intervals** — Standard deviations over random seeds are reported, which is the norm in this field. Removed as nice-to-have at best.

## Novel Insights

The paper reveals an interesting architectural design space: rather than trying to serialize graph topology (as prior graph SSM work does), one can create a sequence *orthogonal* to the graph structure—in the feature/embedding dimension—and apply sequential processing there while the GNN handles the spatial dimension. This two-domain decomposition is conceptually clean and preserves permutation equivariance by construction. However, the critical unresolved question is whether the ARMA mixing across the artificial sequence dimension provides *qualitatively different* information propagation benefits in the graph spatial domain compared to simply running a deeper GNN with standard residuals, or whether the empirical gains observed are primarily a depth + better optimization effect from the weighted skip connections.

## Suggestions

- Add an ablation replacing ARMA-structured skip connections with generic learned weighted residuals at the same recurrence depth R. This is the single most important experiment to validate the ARMA framing specifically.
- Tone down the claim that Section 4 provides "theoretical foundation for addressing the oversquashing phenomenon" to instead state that it provides "theoretical foundation for long-range information preservation in the sequence domain, which combined with the GNN backbone's spatial propagation, empirically mitigates oversquashing"—acknowledging the gap between what the theory proves and what the experiments demonstrate.

## Score and Decision

The paper makes a legitimate contribution: a permutation-equivariant, backbone-agnostic mechanism that empirically achieves strong long-range propagation on the tasks designed to test it. The feature transfer results (Figure 2) are compelling. However, the theoretical claims overreach—specifically, the paper claims Section 4 addresses oversquashing (a graph-spatial phenomenon) when the theory only analyzes sequence-dimension decay. The artificial nature of the sequence (L independent projections of the same input) undermines the claim of having "solved" the graph-to-sequence problem. The absence of the key ablation (ARMA-weighted vs. generic residuals at same depth) leaves the core framing question unanswered. These are significant but not fatal issues: the method works in practice and the permutation-equivariance advantage is real.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>