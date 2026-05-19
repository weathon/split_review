- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Here is my consolidated final review.

---

## Summary

TIMBA replaces the time-oriented transformer layers in the CSDI/PriSTI diffusion-based imputation framework with bidirectional Mamba (S6) blocks. The architecture integrates SSM-based temporal processing with GNN-based spatial processing while maintaining a similar parameter count to PriSTI. The paper evaluates on three real-world datasets (AQI-36, METR-LA, PEMS-BAY) and reports that TIMBA achieves the best or tied-best result in 8 of 10 metric–dataset combinations.

## Strengths

- **Consistently best or tied-best performance on the main benchmark (Table 1).** TIMBA achieves the lowest MAE/MSE in 6 of 10 metric–dataset pairs and ties for best in 2 more, using full training (200/300 epochs). The improvements are small but consistent across multiple datasets and missingness scenarios (AQI-36, METR-LA point and block, PEMS-BAY block MAE). This provides reasonable evidence that the Mamba-based replacement offers a genuine — if modest — improvement over transformer-based temporal encoding.

- **Transparent parameter reporting.** The paper honestly reports TIMBA's parameter count (876,765) relative to PriSTI (797,533) and CSDI (416,305), acknowledging the 9.93% increase. The stated goal of matching PriSTI's parameter count as closely as possible while respecting Mamba's architectural constraints (2× expansion factor) is clearly explained.

- **Sensitivity analysis across missing rates shows a clean monotonic advantage.** Tables 3–4 (even at 50 epochs) show TIMBA achieving strictly better MAE and MSE at every missing rate from 10% to 90% on METR-LA, compared to both CSDI and PriSTI. The pattern is consistent and visually compelling.

- **Architectural description is clear and reproducible.** The bidirectional Mamba block design (Figure 2) is well-specified, the CFEM and NEM modules are explained, and the paper states that code will be provided.

## Weaknesses

### Major

- **Ablation study and missing-rate sensitivity analysis use undertrained models (50 epochs vs. 200–300).** The paper explicitly states (Section 5.3) that these experiments use 50-epoch models "due to time constraints." This is the only direct evidence supporting the central design choice of bidirectional over unidirectional Mamba blocks (Table 2) and the claim that TIMBA scales better to high missing rates (Tables 3–4). Without confirmation that the relative ordering holds at convergence, these conclusions are provisional. Since the ablation directly supports a core architectural claim, this gap is significant.

- **Unsupported scalability claim in the conclusion.** The paper states that TIMBA "can scale effectively with longer temporal sequences, generally achieving better results as the number of time steps per sample increases." There is no experiment in the paper that varies sequence length. This claim should either be supported with evidence or removed.

- **Downstream task is weakly motivated and the improvements are not statistically meaningful.** The task (predicting one node's value from other nodes at the same time step) tests spatial correlation, not temporal imputation quality. All improvements over PriSTI and CSDI are within one standard deviation (Table 5, e.g., Sensor 14 MSE: 91.90±20.33 vs. 92.70±20.27 vs. 96.99±21.25). The claim that TIMBA's imputation quality is "advantageous" for downstream tasks is not supported by these results.

- **Primary claim of "superior performance in almost all benchmark scenarios" overstates the results.** TIMBA is strictly best in 6/10 metric–dataset pairs, tied in 2/10, and worse on 2/10 (both MSE on PEMS-BAY, where CSDI performs notably better). The paper's abstract and conclusion frame this as near-universal superiority, which misrepresents the mixed evidence — particularly on PEMS-BAY, the largest dataset.

### Minor

- **Parameter count is not fully controlled, so attributing improvements to architectural bias rather than capacity is uncertain.** TIMBA is 9.93% larger than PriSTI. The paper acknowledges this but does not run a controlled experiment (e.g., scaling down the Mamba block or scaling up PriSTI's transformer). While a 10% difference is small, the reported improvements on several metrics are also small (e.g., METR-LA Point MAE: 1.69 vs. 1.70), making the attribution to architectural inductive bias rather than capacity inconclusive.

- **The bidirectional vs. unidirectional ablation does not control for parameter count.** The bidirectional block effectively doubles the temporal S6 parameters (two S6 paths) compared to the unidirectional version. The paper does not discuss or account for this confound, so part of the improvement attributed to bidirectionality could simply be due to increased capacity.

- **No statistical significance testing.** The reported confidence intervals for the key comparisons (CSDI, PriSTI, TIMBA) overlap in several cases (e.g., AQI-36 MAE: TIMBA 9.56±0.4 vs. PriSTI 9.84±0.11; METR-LA Block MSE: TIMBA 10.36±0.34 vs. PriSTI 10.64±0.13). Without proper significance testing (e.g., paired bootstrap across repeats), it is unclear whether TIMBA's margins over PriSTI reflect a reliable improvement or random variation.

- **No analysis of computational cost.** For a paper proposing an architectural alternative to transformers, the absence of training time, inference time, or memory comparisons is a notable omission. The future work section mentions reducing training/inference time, but the current paper provides no data on these costs.

### Trivial

- Minor formatting: Several entries in Table 1 use only two significant digits for confidence intervals while TIMBA's AQI-36 MAE uses one digit (9.56±0.4), creating slight inconsistency. Not a substantive issue.

## Nice-to-Haves

- Conducting the ablation and sensitivity experiments at full training (200/300 epochs) would substantially strengthen the evidence for the core claims. The authors acknowledge "time constraints," but these are the experiments most directly supporting the paper's architectural innovations.
- Adding a controlled experiment that matches bidirectional and unidirectional Mamba blocks on parameter count would cleanly isolate the effect of bidirectionality.
- A simple sequence-length scaling experiment (or removal of the unsupported claim from the conclusion) would improve accuracy.

## Removed Points

The following points from the input reviews were removed with justification:

- **"The downstream task (Table 5) uses 50-epoch models"** (Harsh Critic): Factually incorrect. The paper states (line 345) it uses "the best weights obtained from the results in Table 1," which are the fully trained 200/300-epoch models. The downstream results are not affected by the 50-epoch limitation.
- **"Parameter-controlled comparison shows improvement is not due to added capacity"** (Strength Finder): Overstated. The parameter counts differ by 9.93%, and no controlled experiment was run. The paper's honest reporting of the difference does not constitute a controlled comparison.
- **"Reproducibility commitment"** (Strength Finder): Generic. Stating that code is provided is standard practice; it does not constitute a specific strength of the scientific contribution.
- **"The paper does not explain why S6 would be better suited for time series"** (Harsh Critic, Section-by-Section): This is a conceptual argumentation gap, not a concrete weakness in the experimental evidence. The paper does state the rationale (SSMs provide temporal inductive bias while incorporating attention), but the argument is not deeply developed. Moved here because it is a matter of expositional depth rather than an experimental flaw.
- **"The limitation section is narrow"** (Harsh Critic): This is a scope preference; the paper acknowledges MAR assumption, which is the primary known limitation for this class of models.

## Novel Insights

None beyond the paper's own contributions. The reviews highlight a consistent tension: the paper's central claims require evidence from undertrained experiments and depend on parameter count differences that are not fully controlled. The main benchmark, while properly executed, shows improvements that are small and partially overlapping in confidence intervals. This is a familiar pattern for incremental architectural contributions that replace one component in an established pipeline.

## Suggestions

1. **Retrain all supporting experiments (ablation, sensitivity) to convergence.** This is the single most impactful improvement. Without it, the paper's core architectural claims rest on unverified assumptions about 50-epoch results persisting at 200+ epochs.
2. **Either add a sequence-length scaling experiment or remove the unsupported claim** from the conclusion about scaling with longer sequences.
3. **Run a controlled parameter-count comparison** — scale either the Mamba block down or PriSTI's transformer up to match parameter counts exactly — to strengthen the attribution of improvements to architectural bias.
4. **Tone down the "almost all" superiority claim** in the abstract and conclusion to accurately reflect the mixed results on PEMS-BAY.
5. **Replace or redesign the downstream task** to test temporal forecasting (e.g., predict future timesteps from history) rather than a spatially-informed same-timestep prediction.
