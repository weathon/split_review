- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 8, 3
Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

## Summary

TimeMixer proposes a fully MLP-based architecture for time series forecasting that leverages multiscale mixing. The model downsamples the input into multiple scales, then applies Past-Decomposable-Mixing (PDM) — which separately mixes seasonal components bottom-up and trend components top-down — followed by Future-Multipredictor-Mixing (FMM) which ensembles predictions from all scales. The paper reports consistent state-of-the-art performance across 18 benchmarks covering long-term and short-term forecasting.

## Strengths

- **Consistent state-of-the-art across diverse benchmarks (Tables 1–3).** TimeMixer achieves the best MSE on all 8 long-term datasets (e.g., Weather 0.240 vs. next best 0.251; Solar-Energy 0.216 vs. next best 0.283), all 4 PEMS subsets, and all M4 frequency categories. This breadth of coverage across 18 benchmarks with a single architecture is a genuine empirical contribution.

- **Well-designed ablation that validates the core architectural insight (Table 4).** The ablation systematically tests 10 configurations. Cases ④ (no seasonal mixing), ⑤ (no trend mixing), ⑥/⑦ (same-direction mixing for both components), and ⑧ (opposite-direction mixing) all underperform the proposed design. Case ⑨/⑩ (no decomposition) also underperform. This provides strong evidence that the separate directional mixing design is empirically sound, not just intuitively appealing.

- **Favorable efficiency (Figure 6).** TimeMixer uses less GPU memory and lower running time than Transformer-based competitors (Crossformer, PatchTST, FEDformer) across sequence lengths from 192 to 3072, while maintaining competitive efficiency with other MLP-based methods. This supports the practical value of the fully MLP-based design.

- **Novel architectural perspective.** The insight that seasonal and trend components benefit from opposite mixing directions (fine→coarse for seasonality, coarse→fine for trend) is clearly motivated and the visualization of learned weights (Figures 4–5) provides qualitative support that the model learns the intended behavior.

## Weaknesses

### Fatal
None.

### Major

- **Baseline comparison transparency is insufficient.** The paper states (line 178) that "experimental results reported by the above mentioned baselines cannot be compared directly" and that they "make a great effort to provide two types of experiments," but never specifies: (1) what these two types are, (2) which type is reported in Tables 1–3, or (3) whether baseline numbers were obtained by re-running under a unified protocol (with fixed input length 96) or taken from original papers. The table captions state the input length is fixed at 96 for all long-term experiments, which is a deliberate design choice — but this choice may disadvantage baselines tuned for longer inputs (e.g., PatchTST originally used 512). Without explaining how baseline numbers were obtained, the central claim of "consistent state-of-the-art" cannot be fully evaluated. The issue is not that the comparisons are wrong, but that the paper's evidence stops short of proving fairness.

### Minor

- **No uncertainty quantification.** No error bars, standard deviations, or multi-seed averages are reported. On small-margin results (e.g., M4 weighted SMAPE: TimeMixer 11.723 vs. TimesNet 11.829), a reader cannot assess whether improvements are systematic or within noise. While single-run evaluation is common practice in this benchmark suite, the paper's strong framing ("consistent state-of-the-art") would be better served by reporting variance.

- **Ablation presentation claim is imprecise.** The paper states (line 478) that ablation was conducted "on **all 18 experiment benchmarks**," but Table 4 shows results for only 3 datasets (M4, PEMS04, ETTm1). If the full 18-dataset ablation results are in the appendix (which was stripped by the parser), the main text should explicitly reference the appendix. As written, it overstates what the reader can verify from the main body.

- **M4 input length not specified.** The M4 table caption (Table 3) states prediction lengths but does not specify input lengths, unlike the other tables. This is a missing experimental detail.

- **Efficiency analysis conducted on a single dataset (ETTh1).** Generalizability to datasets with different variate counts (e.g., Traffic with 862 channels) is not shown, although the trend in Figure 6 across varying sequence lengths is informative.

- **Scale-number analysis on a single dataset (ETTm1).** The conclusion that M=3 is optimal for long-term and M=1 for short-term is plausible but would be more convincing with verification on additional datasets.

### Trivial
None.

## Nice-to-Haves

- Adding an ablation of the downsampling method (average pooling vs. alternatives) would strengthen the claim that multiscale mixing rather than pooling choice drives performance.
- A simple baseline that linearly averages predictions from independently trained single-scale models at different resolutions would help isolate the benefit of the mixing mechanism.
- A sensitivity analysis showing how TimeMixer's performance varies with input length (e.g., 96 vs. 336 vs. 512) would address fairness concerns and demonstrate robustness.

## Removed Points

These points were raised by reviewers but are removed from the main evaluation:

- **"SCINet distinction is not fully substantiated"** — The paper's characterization of SCINet as not using multiscale information simultaneously in the prediction phase is a reasonable technical distinction. Not a weakness.
- **"Directionality justification is asserted rather than demonstrated"** — The paper provides intuitive motivation from time series principles and validates the design empirically through ablation (Table 4, cases ⑥–⑧). This is standard practice in ML architecture papers.
- **"Missing simple multiscale baseline"** — Moved to Nice-to-Haves. This is a suggestion for strengthening, not a weakness of the presented work.
- **"Missing downsampling ablation"** — Moved to Nice-to-Haves.
- **Any reproducibility concern about undisclosed hyperparameters or missing appendix content** — The parser strips appendix sections; these exist in the original submission.
- **Generic criticisms about evaluation rigor without a concrete anchor** — Removed per the filtering discipline. Only specific, verifiable criticisms are retained.

## Novel Insights

None beyond the paper's own contributions. The reviewer pool did not surface any insight about the paper that goes beyond what the authors themselves articulate.

## Suggestions

1. **Clarify the baseline comparison protocol.** Explain what the "two types of experiments" are, and specify for each baseline table whether numbers were obtained by re-running under a unified protocol or taken from published results. If re-run, report hyperparameter tuning details. This is the single most impactful revision the authors could make.
2. **Add error bars or multi-seed averages to the main results.** Even 3 seeds for the headline numbers would substantially increase confidence in the reported improvements.
3. **Correct the ablation description** to either reference an appendix for full 18-dataset results or revise the claim to match what is presented in the main body.
4. **Specify the M4 input length** in the table caption or experimental setup section.
