Now I have a thorough understanding of the paper and the reviews. Let me construct the consolidated review.

---

## Summary

This paper proposes STBP, a framework for continual spatio-temporal forecasting that combines a general-purpose backbone (with a frequency-domain network FreNet and dual-stream linear graph attention DLGA) with an expandable contextual pattern bank. At each incremental period the backbone is frozen while the pattern bank is expanded and fine-tuned, enabling the model to adapt to new nodes and distributions while retaining prior knowledge. Experiments on three streaming benchmarks show SOTA results, with MAE reductions of 21.4%, 21.9%, and 2.4% over the best baseline on PEMS-Stream, CA-Stream, and AIR-Stream respectively.

## Strengths

1. **Consistent SOTA forecasting accuracy.** Table 1 shows STBP achieving the lowest MAE, RMSE, and MAPE across all three datasets and all forecasting horizons. The margins are substantial on the traffic datasets (e.g., PEMS-Stream avg. MAE 12.31 vs. second-best STRAP at 15.67) and meaningful on the meteorological dataset (AIR-Stream avg. MAE 23.64 vs. second-best STRAP 24.21). These results are the paper's primary empirical contribution and directly support the claim of superior forecasting.

2. **Few-shot robustness directly supports the forgetting-mitigation claim.** Table 2 shows that with only 10% training data per incremental period, STBP outperforms all baselines by large margins (PEMS-Stream MAE 13.58 vs. 16.13 for EAC). Since few-shot performance under parameter expansion strongly correlates with knowledge retention from prior stages, this experiment provides the most direct quantitative evidence that the pattern bank enables effective knowledge reuse.

3. **Scalability is demonstrated both analytically and empirically.** The paper derives O(N) complexity for DLGA via linear attention (Eq. 9) and validates it in the efficiency study (Figure 8, third subplot), where the linear-attention variant uses substantially less GPU memory than the quadratic variant as node count grows. The scatter plots on real datasets also show STBP maintains competitive training time per period despite its more expressive backbone.

4. **Novel dual-stream attention design.** The use of the pattern bank component **P**<sub>τ</sub><sup>(2)</sup> as an additional key in the linear attention mechanism (Eq. 9) is an original architectural contribution. This design is clean, interpretable, and provides a principled way for the stored pattern bank to influence spatial correlation modeling without quadratic complexity.

5. **Qualitative evidence of learned pattern structure.** The t-SNE visualization (Figure 6) shows that the pattern bank evolves from a chaotic initial state into well-separated clusters whose temporal dynamics are interpretable. New nodes from later periods are assigned to existing clusters, suggesting that the bank captures reusable pattern archetypes.

## Weaknesses

### Fatal
None.

### Major

1. **No explicit forgetting metric is reported.** The paper claims the pattern bank "alleviates catastrophic forgetting" as a core contribution (Section 4.2, Section 6), but never directly measures forgetting. While the overall SOTA results and few-shot improvements are consistent with forgetting mitigation, they do not isolate it from other factors (e.g., better architecture, better optimization). A standard forgetting measure — e.g., the performance on the first period's test set after training on later periods, or a per-period breakdown of old-node vs. new-node performance — is needed to substantiate this specific claim. Without it, the paper's claim about forgetting is inferred rather than demonstrated.

### Minor

2. **The ablation study would benefit from a cleaner isolation of the pattern bank's effect.** The "Retrain" (train-from-scratch) and "Online" (full fine-tuning) variants remove the pattern bank but also change the training regime. The "w/o Backbone" variant retains the pattern bank but replaces the entire backbone. Neither directly answers: *does the pattern bank provide a benefit beyond simply freezing the backbone?* The comparison with EAC (a prompt-tuning baseline with frozen backbone) partially addresses this gap since STBP outperforms EAC, but a direct ablation — frozen backbone without pattern bank vs. frozen backbone with pattern bank — would cleanly isolate the contribution. The paper's central claim about the pattern bank would be on firmer ground with this variant.

3. **FreNet is claimed to be important but is not separately ablated.** The paper states that FreNet "makes a notable contribution" (Section 5.3), but the only backbone-level ablation replaces the entire backbone (w/o Backbone), conflating FreNet with DLGA and other components. A controlled ablation that replaces FreNet with a simple temporal convolution or linear layer while keeping DLGA intact would isolate whether the frequency-domain design specifically helps with distribution drift. This is a relatively easy experiment that should be added.

4. **Per-period performance is not reported.** Only period-averaged metrics are shown (Table 1). In continual learning, it is important to see whether performance degrades over periods (forgetting), stabilizes, or improves. Reporting per-period results (or at least performance on the first period across later stages) would address weakness #1 and strengthen the empirical evaluation.

### Trivial

- Equation (5) uses "·" without clarifying whether it denotes element-wise multiplication or matrix multiplication. Given the dimensions (N<sub>τ</sub> × d), it is likely element-wise, but the gating mechanism's exact operation should be explicitly stated.
- The toy dataset in Figure 8 (third subplot) is mentioned but its construction (number of nodes, graph structure) is not described in the main paper. This information likely exists in the appendix (stripped), but a brief description would improve readability.
- The circle sizes in Figure 8 indicate GPU memory but exact values are not provided on the plots, making quantitative comparison difficult.

## Nice-to-Haves

- A per-period forgetting curve (old-node performance as new periods are added) would cleanly validate the central forgetting-mitigation claim.
- A quantitative evaluation of the t-SNE clusters against ground-truth node types (e.g., sensor functional classes) would strengthen the interpretability analysis beyond visual inspection.
- A FreNet ablation (replacing with a simple temporal module) to isolate its contribution to distribution-drift handling.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The continual learning evaluation protocol is undefined"** — The paper defines the streaming graph formalism in Section 3 and cites established streaming benchmarks (TrafficStream/Chen et al. 2021, EAC/Chen & Liang 2025) which define the standard protocol. Dataset statistics and period details are referenced to the appendix (stripped by the parser). The protocol is adequately specified for reproducibility in this field.
- **"PEMS-Stream (Chen et al., 2001) cites a 2001 paper on the PEMS system, not a dataset"** — The citation year is almost certainly a parser artifact (the paper likely cites Chen et al. 2021, i.e., TrafficStream, which introduced the streaming PEMS dataset). The paper references a well-known benchmark; the dataset exists.
- **"The paper's framing that only CSTF methods address continual learning is not entirely accurate"** — This is a framing observation without a concrete impact on the paper's claims or results.
- **"The EAC column shows multiple numbers per cell"** — This is a PDF parsing artifact from table alignment, not an error in the submission.
- **"Small standard deviations suggesting low variance"** — This is a speculative observation without evidence of an error; small std devs are consistent with deterministic components in the pipeline.
- **"Criticisms about missing appendix content"** — Per instructions, these are removed because the parser strips appendix sections from all papers; they exist in the original submission.
- **"Cross-domain continual learning would strengthen the claim"** — The paper explicitly scopes this to future work, and it extends beyond the paper's stated contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add an explicit forgetting metric — e.g., report the MAE on the first period's test set after each subsequent period for STBP and key baselines. This directly validates the forgetting-mitigation claim.
2. Add an ablation: frozen backbone without pattern bank (e.g., freeze the backbone and only train a lightweight linear adapter per node, or compare against EAC's prompt pool removed) versus full STBP. This isolates the pattern bank's standalone contribution.
3. Add a FreNet ablation: replace FreNet with a simple temporal convolution while keeping DLGA and the pattern bank intact.
4. Clarify the operation in Equation (5) — specify whether "·" is element-wise multiplication, matrix multiplication, or a gating operation.
5. Provide exact GPU memory values (as annotations or a table) alongside the efficiency scatter plots.

## Score and Decision

**Overall assessment:** The paper makes a solid contribution to continual spatio-temporal forecasting with a novel architecture that combines frequency-domain processing, linear graph attention, and an expandable pattern bank. The empirical results are strong and consistent across multiple benchmarks. The main weaknesses are about experimental completeness rather than fundamental flaws: the forgetting-mitigation claim needs a direct metric, the ablation could be cleaner, and FreNet's contribution is not separately tested. These are addressable in a revision and do not undermine the core SOTA result. I recommend acceptance.

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>