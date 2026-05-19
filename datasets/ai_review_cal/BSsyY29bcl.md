- Decision: Reject
- Avg Score: 5.80
- Scores: 8, 5, 6, 5, 5
I have now thoroughly reviewed the paper and both reviewer inputs. Let me produce the consolidated review.

---

## Summary

The paper proposes TwinsFormer, a Transformer-based architecture for time series forecasting that decomposes the input into trend and seasonal components and employs a dual-stream interactive design. Unlike prior decomposition-based methods that process components independently, TwinsFormer feeds the seasonal stream through attention and FFN modules (with a subtraction/residual mechanism) while using the seasonal stream's intermediate signals (attention output, FFN output) to supervise the trend stream via an interactive module. The two streams are gated and summed before final projection. Experiments on 13 real-world benchmarks show TwinsFormer achieves top-1 average MSE/MAE on 18 out of 22 settings against 10 baselines.

---

## Strengths

- **State-of-the-art performance across multiple benchmarks**: Tables 1 and 2 (main results) show TwinsFormer achieves the best average MSE/MAE on 18 out of 22 settings across 13 real-world datasets, outperforming 10 diverse baselines including iTransformer (e.g., 6.2% MSE reduction on ECL, 5.1% on Traffic). The advantage holds for both long-term and short-term forecasting.

- **Systematic ablation study isolates component contributions**: Table 3 ablates 7 variants — disabling decomposition, swapping components, replacing the subtraction mechanism with addition, removing each interactive input ($E_T'$, $A_S$, $F_S$), and removing the gate mechanism — each causing clear performance degradation. This provides direct causal evidence that the interactive strategy, not just decomposition alone, drives the gains.

- **Plug-and-play compatibility is demonstrated**: Table 4 shows that applying the interactive strategy to five different Transformer backbones (Transformer, Informer, Autoformer, Flowformer, Periodformer) consistently improves performance. This supports the claim that the interactive module generalizes across attention mechanisms.

- **Efficiency analysis on Traffic**: Figure 6 compares TwinsFormer and its efficient variant (TwinsFormer-E, trained with 20% of variates) against 8 baselines, showing competitive performance with substantially reduced memory footprint. The complexity analysis clarifies that the primary cost scales with the number of variates ($O(N^2)$), not the lookback length.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Rationality analysis is simplified, and the conclusion is slightly overstated.** The derivation in Section 3.2 (Equations 8–10) argues that the sum of the two interactive streams reconstructs the original signal, showing the design "perfectly fits the requirements of the decomposition design without bringing in redundant signals." However, the paper explicitly states it is "omitting the constraints from various functions" — i.e., treating non-linear operations (attention softmax, gating, convolutions) as linear. The architectural point about additive structure is sound, but the claim of "perfectly fits" overstates what the simplified analysis supports. The paper would benefit from acknowledging this gap more candidly and from providing empirical evidence (e.g., measuring reconstruction error of $O_S + O_T$).

- **Compatibility study (Table 4) lacks baseline configuration details.** The reported improvements (28–47%) over older Transformer variants (Transformer, Informer, Autoformer, Flowformer, Periodformer) are large. While these are older methods (2021–2023) and large relative gains over weak baselines are not inherently suspicious, the paper does not specify how each baseline was configured or tuned for the comparison. Adding configuration details or, better, a controlled comparison on a modern baseline (e.g., iTransformer ± the interactive module) would strengthen the plug-and-play claim.

- **Efficiency analysis is limited to a single dataset (Traffic).** The memory comparison in Figure 6 is shown only on one dataset. Training time, FLOPs, or comparable efficiency figures for the main experimental settings are not reported. The TwinsFormer-E variant (trained with 20% of variates) is also under-described: how are the 20% of variates selected (random, by correlation, or other)?

### Trivial

- The visualization analysis (Figure 5) is qualitative. Quantitative metrics (e.g., attention entropy, representation rank) would be more informative but are not essential for the paper's core claims.

---

## Nice-to-Have

- Reporting error bars / multiple-seed runs for the main results. (Single-run reporting is the norm in this field but would strengthen the statistical grounding.)
- Justifying the design choices in the interactive module (e.g., why multiscale convolutions with kernel sizes 1,3,5; why sigmoid gating) either through ablations or literature citations.

---

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Ablation 'w/o decomposition' doubles model capacity"** — Factually incorrect. The architecture has two streams regardless of whether decomposition is used. The ablation feeds the same observed series to both streams (instead of trend to one and seasonal to the other), keeping the same number of parameters. The comparison tests input assignment, not capacity.

- **"Overclaimed novelty; prior works already consider interactions"** — The paper hedges with "to our best knowledge" and "first attempt to consider interactions between decomposed components on Transformer." The cited prior works (Autoformer, FEDformer, DLinear) do not explicitly design interactive modules between decomposed branches — they process components independently and sum them. The critic conflates implicit architectural interactions with the paper's explicit dual-stream supervision mechanism.

- **"Tables shown as images prevent verification"** — Parser artifact. The original PDF has proper tables.

- **"Figure 2 is difficult to read"** — Parser/formatting artifact from PDF extraction.

- **"Lookback sensitivity analysis is weak evidence"** — Generic criticism; the experiment shows improving trends across three datasets, which is standard practice.

- **"No discussion of hyperparameter sensitivity"** — The paper reports standard implementation details (Adam optimizer, L2 loss, early stopping). Hyperparameter details are available in the original submission (appendix was stripped by parsing).

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Qualify the rationality analysis.** Replace "perfectly fits" with more measured language, and optionally provide an empirical check (e.g., measuring the reconstruction error $||(O_S + O_T) - X||$) to show the sum property approximately holds under the non-linear operations.

2. **Add configuration details for Table 4** or replace/ supplement it with a cleaner comparison: apply the interactive module to a single strong modern baseline (e.g., iTransformer) and report the delta. This would directly answer concerns about baseline tuning.

3. **Describe the TwinsFormer-E variant** more completely: how are the 20% of variates selected? If random, what variance does the selection introduce? If correlation-based, describe the selection criterion.

4. **Consider adding an ablation** varying the multiscale kernel sizes or replacing the multiscale conv with a single linear projection in the interactive module to justify the design choice.

---
