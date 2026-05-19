- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3
Now I have all the verification I need. Let me construct the final consolidated review.

---

## Summary

This paper introduces Freq-Synth, a synthetic data generation framework for zero-shot and few-shot time series forecasting. Through a Fourier analysis lens, the authors define "frequency confusion" and "frequency generalization" as factors affecting model learning, then propose generating task-specific sinusoidal signals using only the target domain's sampling rate. Experiments show that training on small amounts of this synthetic data (5k examples) outperforms training on large real-world corpora (~1000× larger) across 6/8 benchmarks and 6 different models, with especially dramatic gains on ETTm datasets (60% MSE reduction).

## Strengths

- **Novel conceptual framework (frequency confusion and generalization).** Definitions 4.1 and 4.2 provide a clean analytical lens for understanding why models struggle with zero-shot forecasting — namely, they degrade when multiple frequencies are present (confusion) and fail to generalize to unseen frequencies. This is validated through controlled sine-wave experiments (Fig. 1) that show the pattern across 6 models, and further supported by evaluating actual released pre-trained models (TimesFM, Timer, TTM) on sinusoidal inputs (Sec. 5.1), which reveal that models perform well only near 1/24 Hz — the dominant frequency in their pre-training distribution.

- **Consistent and substantial zero-shot gains across architectures.** Table 1 demonstrates that Freq-Synth synthetic data (5k examples) surpasses real-data training (Monash + PEMS, ~1000× larger) in 6/8 benchmark datasets for all six evaluated models (TTM, Timer, UniTime, Moment, GPT4TS, PatchTST). The average MSE drops from 0.602–0.819 (real) to 0.426–0.481 (synth). The 60% reduction on ETTm1 across all models (e.g., TTM: 1.253→0.454) is a particularly concrete and large-margin result.

- **Efficient and practically attractive data generation.** Generation time comparison (Sec. 5.2) reports 0.1 seconds for Freq-Synth to generate one million time points versus 3s (TimesFM), 14.6s (ForecastPFN), and 138.2 minutes (KernelSynth). This efficiency, combined with the method's simplicity (only the sampling rate is needed), makes it a practical tool.

- **Superiority over other synthetic data methods.** Table 2 shows Freq-Synth achieves the lowest average MSE (0.407) among methods operating with a known target sampling rate, versus TimesFM (0.466), ForecastPFN (0.739), and S-Naive (0.497), despite using only 1/14 the data volume. Even without the target sampling rate (Freq-Synth Natural), it outperforms KernelSynth (0.493 vs 0.628).

- **Few-shot benefits from synthetic pre-training.** Table 3 shows that fine-tuning from a Freq-Synth pre-trained model on 10% of target data yields lower average MSE than fine-tuning from a real-data pre-trained model for TTM (0.327 vs 0.366), Timer (0.325 vs 0.404), and PatchTST (0.335 vs 0.405), suggesting the synthetic pre-training provides a better initialization for downstream tasks.

## Weaknesses

### Fatal
None.

### Major

- **Zero-shot comparison confounds data volume and frequency coverage.** The real-data training setup uses a large, diverse corpus (~1000× larger than the 5k synthetic examples) described only as "a subset of datasets from Monash and PEMS." Which specific datasets and how they were selected is not stated. While the paper acknowledges that the 15-minute frequency of ETTm is absent from the real training set (and attributes the gains on ETTm to this gap), the comparison does not isolate whether the synthetic advantage comes from frequency alignment, smaller data volume (less overfitting), or other confounding factors. A counterexample — Weather and Exchange, where real data wins — shows the method is not universally superior, but the paper does not discuss why. This limits the strength of the paper's primary experimental claim.

- **No standard deviations or confidence intervals for main results.** Table 1 reports averages over three seeds and four horizons but provides no error bars. Without variance information, it is impossible to assess whether the reported improvements (some of which are modest, e.g., ETTh2 for TTM: 0.415→0.412) are statistically significant. This is a standard expectation for benchmark evaluations.

### Minor

- **Few-shot experiment missing a "train from scratch" baseline.** The comparison is "Real pre-train + fine-tune" vs. "Synth pre-train + fine-tune," but a simpler baseline of training from scratch on the 10% target data is absent. Without it, the reader cannot tell whether the benefit comes specifically from synthetic pre-training or from any pre-training that provides a better initialization than random.

- **The evidence for frequency confusion (Fig. 1 left) is acknowledged as "even if mild" by the paper itself.** The MSE increase when adding frequencies is modest, which somewhat weakens the claim that models "commonly suffer from poor learning from data with multiple frequencies." The right-hand experiment (presence vs. absence of target frequency) is more convincing.

- **No discussion of limitations or failure cases.** The paper does not address scenarios where Freq-Synth might fail — e.g., datasets with no clear fundamental frequency, irregularly-sampled data, multi-seasonal patterns, or non-stationary signals. Including a limitations paragraph would strengthen the paper.

- **Ablation of design choices is deferred to appendix.** Key hyperparameters (number of harmonics \(h\), pool size \(m\), amplitude distribution \(A'\), number of sines per variate \(l\)) are mentioned but their impact is not ablated in the main paper. An ablation showing which design choices matter most would strengthen the reader's understanding of the method's robustness.

### Trivial

- None that warrant mention; any presentational issues are within the range of typical workshop/conference submissions.

## Nice-to-Haves

- A controlled experiment where the real-data training set is truncated to the same size as the synthetic set and the same frequency distribution is ensured, to directly isolate the effect of synthetic data versus data volume.
- Periodogram similarity plots comparing synthetic and real data for each benchmark dataset, to visually confirm that Freq-Synth covers the dominant frequencies of the target domain.
- Additional ablation testing whether training on random frequencies (not harmonics of the target) produces the same benefits, to verify the claim that harmonics specifically are what matter.
- Direct validation of whether Freq-Synth *pre-training* mitigates the frequency overfitting observed in Sec. 5.1 (currently that section tests only existing pre-trained models).

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper:

1. **"Table 2 is uninterpretable without specifying the evaluation model."** — REMOVED as factually incorrect. The paper clearly states (line 219): *"The MSE and MAE measures are averaged on a forecasting horizon of 96 across all six models (see Sec. \ref{subsec:zs_pred})."* Six models are enumerated in Sec. 4.2 (TTM, Timer, UniTime, Moment, GPT4TS, PatchTST). The table is fully interpretable.

2. **"Foundation models overfit to certain frequencies supported only by a toy experiment."** — REMOVED as factually incorrect. Sec. 5.1 (lines 306) evaluates *actual released pre-trained models* (TimesFM, Timer, TTM from their original repositories) on sinusoidal signals and shows performance degradation at non-1/24 Hz frequencies. This is not a "toy experiment" — these are the real production models.

3. **"The method feels engineered rather than derived from the analysis."** — REMOVED as a subjective and unverifiable characterization. The method is explicitly derived from the analysis: the analysis shows that frequency alignment matters, so the method generates data aligned to the target frequency's harmonics.

4. **"The paper does not test whether Freq-Synth pre-training would mitigate this overfitting."** — REMOVED (downgraded to Nice-to-Have). This is a suggestion for extending the paper, not a weakness of what is presented. The paper's main experiments (Tables 1-3) already demonstrate Freq-Synth's effectiveness.

5. **Generic reproducibility concerns about missing appendix content.** — REMOVED per hard rules; the parser strips appendix sections from all papers.

## Novel Insights

The most interesting emergent observation from the reviews is that the harsh critic's "fatal" criticisms collapsed upon verification: the paper actually *does* specify the evaluation model for Table 2 and *does* evaluate real pre-trained models in Sec. 5.1. This suggests the paper is clearly written but dense enough that a hurried reader can miss explicit methodological statements. A more substantive novel observation is that the paper's core experimental strength — consistent gains across 6 architectures in 6/8 datasets — holds even for datasets whose frequencies are present in the real training set (e.g., ETTh1, Electricity), not just the ETTm datasets with the missing 15-minute frequency. This means the method provides benefits beyond simply filling a frequency gap in the real training distribution, which is a stronger finding than the paper itself emphasizes.

## Suggestions

- **Clarify the real-data training setup.** Specify the exact subset of Monash and PEMS datasets used, the number of training examples, and the hyperparameter selection procedure. This is essential for reproducibility.
- **Add error bars or confidence intervals to Table 1.** Since results are averaged over three seeds, reporting standard deviations would allow readers to assess the reliability of the improvements.
- **Add a "train from scratch on 10% data" baseline to the few-shot experiment (Table 3).** This would clarify whether the benefit comes from pre-training generally or from synthetic pre-training specifically.
- **Add a limitations paragraph** discussing when Freq-Synth might underperform (non-periodic data, irregular sampling, multi-seasonal patterns) and the scope conditions of the method.
- **Include the key ablation results in the main paper** (at least one figure showing sensitivity to \(h\), \(l\), and \(A'\)), rather than deferring all implementation detail to the appendix.
