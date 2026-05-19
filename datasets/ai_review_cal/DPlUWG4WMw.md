- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have all the information I need. Let me write the consolidated review.

## Summary

The paper introduces "operator deep smoothing," a method applying graph neural operators (GNOs) to implied volatility surface construction. The core insight — that option data arrives in irregular, dynamic spatial configurations, making conventional neural networks unsuitable — is well-founded. Using a single GNO with ~100k parameters trained on nine years of intraday S&P 500 data, the method achieves ~0.5% MAPE on a full year of test data, substantially outperforming the industry-standard SVI baseline (1–2%), and generalizes to three other US indices without retraining.

## Strengths

- **Discretization-invariance demonstrated on realistic irregular data**: The paper formally defines discretization-invariance (Section 3.1) and shows through both the problem framing and experiments that the GNO handles implied volatility inputs whose number and spatial arrangement vary over time. This directly addresses a limitation of prior neural approaches (Bergeron et al. 2021, Cont et al. 2023) that required fixed rectilinear grids or pre-interpolation.

- **Single model substantially outperforms SVI on 10 years of real data**: A single GNO with ≈100k parameters processes >60 million volatility datapoints and achieves a MAPE of ≈0.5% on the 2021 test set vs. 1–2% for SVI (Section 4.2). This is the paper's strongest empirical result — a direct, fair comparison against the industry standard on identical real data.

- **Generalization to three unseen indices without retraining**: The GNO trained only on intraday S&P 500 data is evaluated on end-of-day data for SPX, NDX, DJX, and RUT (Table 1). It achieves δ_abs < 1.1% for NDX and < 1.7% for DJX with near-zero arbitrage losses, demonstrating robustness.

- **Differentiable no-arbitrage constraints integrated into the loss**: The paper translates Theorem 1 (strike and calendar arbitrage conditions) into differentiable penalties ℒ_but and ℒ_cal (Equations 6–7), providing a principled way to enforce financial validity.

- **Robustness to input subsampling**: A footnote (Section 4.2) notes that dropping half the input datapoints per surface during backtesting still yields accurate smoothing, directly testing the discretization-invariance property in a practical setting.

- **Parameter efficiency**: The single GNO instance (≈100k parameters) replaces SVI's 61,454 per-slice instances (307k parameters) and Ackerer et al.'s per-surface networks (cumulative 200M+ parameters for the full dataset), a striking compression.

## Weaknesses

### Fatal
None.

### Major

- **Narrative tension between "single evaluation" and the finetuning procedure**: The paper claims that operator deep smoothing "replac[es] the instance-by-instance optimization with a single evaluation of a neural network" (line 47) and uses "a single model instance" (line 11, line 59). However, the evaluation procedure (lines 419–423) involves monthly finetuning: after each month of test data, the model is trained for 10 epochs on that month's data augmented with training data. The paper does **not** report results without this finetuning. This makes it impossible to assess how much of the reported 0.5% MAPE comes from the offline-trained operator versus ongoing online adaptation. If finetuning is essential, the claimed advantage over per-surface optimization (SVI, Ackerer) is substantially weakened — the method still requires periodic recalibration, just at a coarser granularity. The paper must either (a) report performance without finetuning to demonstrate that offline training alone suffices, or (b) explicitly reframe the method as a hybrid offline + online approach and characterize the costs and benefits of both components.

### Minor

- **No-arbitrage evaluation is only on average**: Line 439 states "on average, the smoothed surfaces are completely free of arbitrage (indicated by non-negativity)." This does not rule out individual surfaces with violations — a surface that is arbitrage-free on average may still have exploitable violations on specific days. The paper should report the fraction of surfaces that are violation-free (or the worst-case violation magnitude), especially since no-arbitrage constraints are central to the method's credibility (Section 1 explicitly criticizes simpler interpolation for violating them).

- **Ackerer et al. comparison is not evidence**: The paper claims to be "highly competitive" with Ackerer et al. (2020) (lines 60, 429), citing that paper's reported MAPE of ~1% on synthetically generated data. The paper is transparent about this limitation in a footnote (line 429: "reports a MAPE of around 1% for synthetically generated data" and "does not perform a similar restriction of the domain"), but the comparison still appears in the abstract and results section as evidence. Since the methods are evaluated on different data with different domain restrictions, the MAPE comparison is not meaningful. The parameter-efficiency comparison (200M vs 100k) is valid and interesting on its own and should be kept; the accuracy comparison should be removed or reframed as a qualitative observation rather than evidence.

- **Architectural modification not ablated**: The paper states that "purely non-local architecture led to substantially reduced performance" (line 333) to justify the proposed hybrid architecture (non-local first layer, local subsequent layers), but provides no ablation table or quantitative evidence. This is a key design claim that could be easily substantiated.

- **Laplacian regularizer not analyzed**: The Laplacian regularization term ℒ_reg (line 339) is mentioned but not shown in any experiment. It is unclear whether it was used in the reported results, and if so, how its weight was selected.

- **No multi-run statistical analysis**: While Figure 4 does show 25%-75% quantiles over time, the overall results lack error bars from multiple training runs with different seeds. The finetuning involves stochastic gradient steps, so the stability of results across runs is relevant.

### Trivial
None.

## Nice-to-Haves

- A computational cost comparison (total amortized cost: training + monthly finetuning) versus SVI across the full test period would make the efficiency claim concrete.
- Ablation comparing three GNO variants (full local+non-local, non-local only, and the proposed hybrid) on a validation subset would strengthen the methodological contribution.
- Reporting whether the finetuning compensates for distribution shift vs. underfitting on new data.

## Removed Points

- **Criticism about missing appendix/SVI calibration details**: The parser strips appendix sections from all papers; these details exist in the original submission. Removed per hard rules.
- **Criticism that the Ackerer comparison is "fatal" or invalidates the paper's core claims**: The paper is transparent about the differences in its footnotes, and the paper's main comparison is with SVI (not Ackerer). The accuracy comparison is weak but not fatal. Downgraded from the critic's framing to Minor.
- **Claim that the paper "cannot be independently verified" or that reproducibility is lacking**: The paper includes a code repository statement (line 118) and supplementary materials with code and trained model weights (line 383). Removed per hard rules about not questioning existence of cited resources.
- **Criticism that parameter-count comparison with Ackerer is "misleading"**: The comparison (100k vs. 200M) is correctly framed as a discussion of architectural parameter efficiency when applied at dataset scale, not per-surface. This is a valid and interesting point. Removed as factually incorrect characterization by the reviewer.
- **Strength about "efficient online calibration replacing instance-by-instance optimization"**: This strength conflicts with the verified weakness about the finetuning gap. Per calibration rule, when a strength and weakness disagree, the weakness wins. Moved here.

## Novel Insights

The key insight that emerges from the reviews — beyond what the paper itself states — is that the paper sits at an awkward junction between two narratives. The "once-trained, always-applied" neural operator framing (standard in PDE applications) clashes with the financial-domain reality that models must adapt to market regime shifts. The monthly finetuning the authors use is actually a sensible response to this tension, but by not reporting the no-finetuning baseline, they leave the reader unable to separate the operator learning contribution from the online adaptation contribution. A more honest framing — "pretrained neural operator with lightweight online adaptation" — would better reflect what the paper actually evaluates and would be a more reproducible contribution.

## Suggestions

1. **Show results without finetuning**: This is the single most impactful addition. Even a brief experiment showing the pretrained GNO applied directly to the test set (no monthly adaptation) would resolve the narrative gap. If performance degrades, characterize the degradation rate and reframe the method accordingly.
2. **Report per-surface no-arbitrage violation rates** rather than (or in addition to) averages. Report the fraction of surfaces with ℒ_but or ℒ_cal exceeding a small tolerance, and the maximum violation.
3. **Remove the accuracy comparison with Ackerer et al.** or replace it with a proper re-implementation. Keep the parameter-efficiency comparison.
4. **Add ablation results** for (a) the architectural modification (full GNO vs. non-local-only vs. proposed hybrid) and (b) the Laplacian regularizer weight sensitivity.
