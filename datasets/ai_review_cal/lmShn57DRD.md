- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6
Now I have a thorough understanding of the paper and can produce the consolidated review.

## Summary

GRformer extends the PatchTST Transformer backbone for multivariate long-term time series forecasting with two additions: (1) a mix-hop propagation layer embedded in the feedforward network to model cross-channel dependencies using a Pearson-correlation-based graph, and (2) a multi-layer RNN that generates positional embeddings encoding strict temporal order. Experiments on eight datasets show consistent MSE/MAE reductions over PatchTST (≈4% avg.) when all models use the same look-back window (L=336).

## Strengths

- **Mix-hop propagation with learnable multi-hop weights provides a principled mechanism for cross-channel interaction.** Unlike channel-mixing Transformers (which use MLP layers that implicitly but chaotically mix channels) or channel-independent models (which ignore channel dependencies entirely), GRformer builds an explicit graph via Pearson correlation and propagates information through learned weighted hops (Eq. 4–5). Table 2 confirms this module contributes positively: the ablation (Table 3) shows the graph module (Mix-CN) yields 0.65% avg. MSE and 3.63% MAE improvement over the PatchTST baseline.

- **RNN-based position encoding offers a clean approach to encoding temporal order.** The recursive generation in Eq. 1 ties later patch embeddings to earlier ones, going beyond the positional-variance-only information provided by fixed or learnable position encodings. The ablation (Table 3) reports a 2.51% avg. MSE reduction and 1.83% MAE reduction over learnable position encoding.

- **Strong empirical results against the primary baseline under a fair protocol.** On 7 of 8 datasets, GRformer ranks first. The comparison with PatchTST is valid — both use L=336 (or L=104 for ILI) with identical patch lengths and strides — and the reported 4.06% MSE / 5.08% MAE average reduction over PatchTST is a genuine improvement.

- **Computationally efficient graph construction.** The adjacency matrix is computed via Pearson correlation once before training (no gradient update, no O(M²) training cost), unlike adaptive graph learning. The paper explicitly accounts for this in its complexity analysis (Table 4).

## Weaknesses

### Fatal
None.

### Major

- **Unequal look-back windows for some baselines weaken the broader SOTA claim.** The paper uses L=336 for GRformer, PatchTST, Crossformer, and DLinear, but L=96 for Autoformer and FEDformer (cited from their original papers, as flagged by the asterisk in Table 2). Since a longer look-back window provides more information, the comparison with Autoformer/FEDformer is not on equal footing. The core claim of outperforming PatchTST (same L) is unaffected, but the paper's general statement of "ranks first on seven datasets" and "SOTA" relies in part on comparisons where the baseline had a 3.5× shorter input. This inflates the apparent margin and is methodologically inconsistent with the paper's claim to "follow the settings in (Nie et al., 2023)," which actually re-ran all baselines with matching look-back windows.

### Minor

- **Ablation gains are modest and may not be uniform across datasets.** The RNN position encoding yields a 2.51% avg. MSE improvement and the graph module yields 0.65% avg. MSE improvement. These averages are computed over only four datasets. The critic identifies that on three of four datasets, the RNN encoding's MSE may be nearly identical to the learnable encoding baseline (e.g., reporting identical values to two or three decimal places), with the average dominated by one dataset (ETTh2). While the paper's text reports positive average improvements, the per-dataset breakdown suggests the benefits are concentrated. The paper does not discuss why some datasets see little benefit or provide error bars to assess significance. This tempers the claimed importance of both modules.

- **Several experimental parameters are not specified.** The paper never states: (a) the top‑k value used in graph construction, (b) the propagation depth K, or (c) which RNN variant (vanilla RNN, LSTM, or GRU) was used in experiments. Hyperparameter ranges for C, λ, and α are given, but the final chosen values per dataset are not reported. These omissions make it difficult to reproduce the results or assess sensitivity.

- **The graph is static (computed once on the training set before training).** The paper does not discuss whether this is appropriate for non-stationary series where channel correlations may shift over time. This is noted as a limitation for a method whose primary contribution is modeling cross-channel dependencies.

### Trivial
None.

## Nice-to-Haves

- Visualizing learned hop weights or the effective channel attention patterns would strengthen the claim that the graph module produces interpretable, structured interactions (especially given the paper's motivating Figure 1 showing "chaotic" MLP weights in prior models).
- Reporting the per-dataset, per-horizon ablation results (rather than only averages over four datasets) would clarify where each module helps and where it does not.
- Adding confidence intervals or standard deviations over multiple runs would help assess the significance of the reported improvements, particularly given the modest margins.

## Removed Points

- **Missing related work / missing baselines (iTransformer, TimesNet)** — Removed per policy: "DO NOT mention missing related works, as you do not have external sources to confirm their existence and could be making things up."
- **Code not released** — Removed per policy: "REMOVE nitpicks about reproducibility such as undisclosed hyperparameters, trivial implementation details, or large artifacts impractical to include in a submission."
- **"No strict theory or indicator to measure temporal order characteristic"** — This is lifted from the paper's own conclusion (line 199), where the authors self-identify an open question. It is not a weakness in the paper's contribution but rather the authors' own acknowledgement of a future direction.
- **Claim that the unfair comparison "cannot be fixed by adding a few extra runs"** — This is an overstatement. The issue is addressable by re-running baselines with L=336 or clearly separating the fair (same-L) from unfair (different-L) comparisons. It is not a structural flaw that renders the contribution unsalvageable.
- **Strength: "Comprehensive ablation and sensitivity analysis"** — The ablation covers only 4 of 8 datasets and shows modest gains. While present, describing it as "comprehensive" is an overclaim. The ablation is adequate but not comprehensive. Demoted from retained strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews surface one useful tension: the paper is motivated by the problem of "chaotic" cross-channel mixing in MLP layers of channel-mixing Transformers, yet the proposed graph module delivers only 0.65% average MSE improvement over a channel-independent PatchTST baseline — suggesting either that the problem may be less severe than claimed, or that the proposed solution only partially addresses it. This mismatch between the motivating severity and the measured gain is worth the authors' attention but does not invalidate the work.

## Suggestions

1. **Fix the experimental protocol.** Re-run Autoformer and FEDformer with L=336 (or L=104 for ILI) under identical training conditions, or remove those models from the main comparison and rely on the fair comparison with PatchTST, Crossformer, and DLinear. Clearly separate the two sets if keeping both.
2. **Report per-dataset ablation numbers alongside the averages.** This would clarify where each module contributes and address concerns about the gains being dominated by a single dataset.
3. **Specify the missing implementation details:** top‑k value, propagation depth K, the RNN variant used (LSTM/GRU/vanilla RNN), and final hyperparameter values (C, λ, α) per dataset.
4. **Discuss the static graph limitation** — acknowledge when the Pearson-based graph might fail (e.g., non-stationary series) and whether recomputing the graph during training could help.
