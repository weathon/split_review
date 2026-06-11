## Summary

ST-Diff introduces a novel paradigm for unconditional multivariate time series generation by reframing time series as spectro-temporal video tensors via the Short-Time Fourier Transform (STFT), then modeling them with a custom video diffusion transformer that factorizes attention along temporal, frequency, and covariate axes with domain-specific biases. The core idea bridges signal processing and video diffusion in a well-motivated way — it preserves spectral content while maintaining explicit temporal structure, addressing limitations of both time-domain models (no spectral structure) and static-image models (collapsed temporal axis).

## Strengths

- **Novel "time-series-as-video" representation**: The STFT-based mapping to a video tensor \(V \in \mathbb{R}^{T \times 3 \times F \times K}\) preserves the temporal evolution of frequency content across covariates, enabling spatiotemporal architectures that prior work (Diffusion-TS time-domain, ImagenTime static-image) cannot use. This is a genuinely new perspective on the problem.

- **Strong quantitative results where comparisons exist**: Table 1 shows ST-Diff achieves the best score on 21 of 24 metric-dataset combinations, often by substantial margins (e.g., Discriminative Score on Energy: 0.009 vs. 0.040 for the next best; Context-FID on MuJoCo: 0.010 vs. 0.251 for TimeVAE). The improvements on high-dimensional real-world datasets (Energy, fMRI, MuJoCo) are particularly compelling.

- **Superior scalability to long sequences**: Table 2 demonstrates ST-Diff maintains stable performance as sequence length grows from 64 to 256 on ETTh (Discriminative Score stays at ~0.03), while competing models degrade sharply. At length 64, ST-Diff's Context-FID (0.031) is an order of magnitude better than Diffusion-TS (0.631).

- **Principled architectural inductive biases**: The anisotropic patching (aggregating along frequency but not covariates, preserving covariate independence), tri-axial factorized attention with RoPE for temporal/frequency axes and learnable embeddings for the unordered covariate axis, and bias matrices \(\mathbf{B}_C/\mathbf{B}_F\) initialized from empirical cross-correlation and spectral covariance are well-motivated by the structure of the data and go beyond generic vision backbones.

- **Qualitative validation of temporal and spectral fidelity**: ACF and PSD comparisons on ETTh (Fig. 4) show close alignment between real and generated samples, demonstrating that the model captures dynamics beyond marginal distributions.

## Weaknesses

### Fatal
None.

### Major

- **Incomplete comparisons against key diffusion baselines, combined with ambiguous table formatting.** Table 1 — the paper's primary evidence — has two significant problems. First, the two most relevant baselines (Diffusion-TS, ImagenTime) are merged into a single row, making it impossible to attribute values to individual methods. For Context-FID and Correlational scores, this row has zero entries across all six datasets. For Discriminative and Predictive scores, entries exist for only 3 of 6 datasets with no indication which method they belong to. Second, each ST-Diff cell contains two numerical values separated by a line break (one bolded), with no explanation of what they represent (different seeds? model variants? with/without cross-covariance loss?). The paper's central SOTA claim — "21 out of 24 metric-dataset combinations" — counts many cells where the only competitors are TimeGAN and TimeVAE, not the diffusion models the paper aims to surpass. Without complete, unambiguous comparisons against the most relevant methods, the headline claim cannot be fully evaluated.

- **Complete absence of ablation studies.** ST-Diff introduces multiple novel design choices (STFT video representation vs. raw time-domain or collapsed-image alternatives, EMA-based trend-residual decomposition, anisotropic patching, tri-axial factorized attention, learnable bias matrices initialized from empirical statistics, cross-covariance loss). None of these are ablated. Without ablations, the paper provides no insight into which components drive performance. The contribution reads as a black-box system comparison rather than a scientific analysis of which design decisions matter and why.

### Minor

- **Undisclosed hyperparameters affecting reproducibility.** The EMA smoothing factor for trend-residual decomposition is not stated. The cross-covariance loss is described in one sentence (line 140) without a formal equation, loss weighting relative to the standard MSE noise-prediction loss, or ablation. Network depth (number of STDiff blocks), hidden dimensions, number of attention heads, and total parameter count are not reported.

- **No computational cost quantification.** The paper acknowledges "higher computational and memory costs" but reports no runtime, parameter count, or memory usage for ST-Diff or any baseline. This makes the practical trade-off impossible to assess.

- **Long-sequence evaluation on only one dataset.** Table 2 evaluates scalability only on ETTh. While results are strong, generalizing from one dataset to claims of "superior scalability" is thin.

### Trivial
None.

## Nice-to-Haves

- Including Crabbé et al. (2024, frequency-domain diffusion) as an experimental baseline would strengthen the positioning, as it represents the most closely related line of work and is cited in the paper but never compared against.
- Reporting architecture dimensions (number of blocks, hidden size, heads) and training time would improve reproducibility.

## Removed Points

These points are flagged to be removed, treat them with caution:
- Harsh critic's specific attribution that values in the merged ImagenTime/DiffusionTs row belong to Diffusion-TS rather than ImagenTime — this is an unverifiable assumption since both methods share one row.
- Harsh critic's concern about missing appendix content ("Extended ACF and PSD results are provided in Appendix C" — the appendix is stripped by the parser) — per policy, parser-stripped sections exist in the original submission.
- Harsh critic's claim of an "inflated" 21/24 count — while missing diffusion entries weaken the SOTA claim, counting results against all listed baselines (including TimeGAN/TimeVAE) is standard practice when comparing against the full benchmark suite.
- Strength Finder's unqualified "SOTA" strength — the SOTA claim is partially undermined by missing baseline entries, but the underlying performance data where comparisons exist remains valid.
- Generic strengths from the Strength Finder about addressing an "important problem" — these lack concrete evidence.

## Novel Insights

The most interesting pattern across the reviews is the disconnect between the paper's genuine novelty and the incompleteness of its evidence. The "time-series-as-video" framing is a genuinely new perspective that bridges signal processing and video diffusion — no reviewer disputes this. The architectural design choices are thoughtful and domain-specific. However, the paper undermines itself by making strong SOTA claims while presenting an evidence table with major gaps (missing baseline entries, merged rows, unexplained dual values). This observation goes beyond standard "more experiments needed" feedback: the paper's core weakness is not its method but the gap between the ambition of its claims and the rigor of its evidence presentation. The method itself is strong enough that completing the comparisons and adding ablations would likely substantiate the claims.

## Suggestions

1. **Complete the baseline comparisons.** Re-run Diffusion-TS and ImagenTime on the same data splits and metrics. Place each method in its own row with all cells filled. This alone would substantially strengthen the paper.

2. **Clarify Table 1.** Explain what the two values per ST-Diff cell represent (or, if this is a parser artifact from the PDF, ensure the final version uses a single unambiguous value per cell). Separate ImagenTime and Diffusion-TS into distinct rows.

3. **Add ablation studies targeting at least 3–4 of:** (a) removing the cross-covariance loss, (b) using random/zero bias matrix initialization instead of empirical statistics, (c) removing the trend-residual decomposition, (d) replacing the video model with a per-frame image model (treating time as channel) to isolate the benefit of the spatiotemporal architecture.

4. **Report computational cost:** training time, inference time per sample, parameter count, and memory usage for ST-Diff and baselines.

5. **Disclose the EMA smoothing factor,** cross-covariance loss equation and weighting, and basic architectural dimensions (number of blocks, hidden size, attention heads).

---

### Calibration Anchors

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Diffusion-TS | 4h1apFjO99.md | 6.33 | R1, R2 | Slightly stronger evidence (complete baselines, some ablations) but less novel core idea. ST-Diff is weaker in evidence quality. |
| Tabular DiT (TabDiT) | bhOysNJvWm.md | 5.00 | R2 | Had ablations and clear presentation but less novel contribution. ST-Diff is slightly better overall. |
| SigDiffusions | Y8KK9kjgIK.md | 4.33 | R1 | Limited experiments, presentation issues. ST-Diff is clearly stronger. |
| Mixture-of-Diffusers | lcmd2Qdrsv.md | 5.60 | R2 | Rejected mainly on novelty concerns; ST-Diff has much stronger novelty but similar baseline-completeness issues. |
| FM-TS | 2whSvqwemU.md | 3.00 | R1 | Weaker method and evidence. ST-Diff is substantially stronger. |
| TF-score | RDLvnUJ5JZ.md | 3.00 | R1 | Weak novelty, mostly applying existing ideas. ST-Diff is substantially stronger. |
| TimeAutoDiff | zB6uMznFuZ.md | 3.00 | R1 | Limited contribution. ST-Diff is substantially stronger. |
| STDM | 2orBSi7pvi.md | 3.00 | R1 | Weak paper. ST-Diff is substantially stronger. |
| TMDM | qae04YACHs.md | 6.33 | R1 | Forecasting-focused, less directly comparable. |
| D3U | HdUkF1Qk7g.md | 6.00 | R1 | Forecasting-focused, less directly comparable. |
| Video diffusion (scattering) | DHCp41nv1M.md | 6.33 | R2 | Different task (video recovery), less comparable. |
| VDT | Un0rgm9f04.md | 6.00 | R2 | General video generation, different domain. |
| FreqPrior | 8x0SGbCpzs.md | 6.00 | R2 | Video noise prior, different domain. |
| Solving Video Inverse Problems | TRWxFUzK9K.md | 6.50 | R2 | Image-to-video, different task. |
| High-quality TS with DiT | etUJR2xBYa.md | 4.20 | R2 | Missing baselines issue, similar quality to ST-Diff but less novel. |

**Round 1 bracket:** 4.0–6.5 (between weak ~3.0 anchors and strong ~8.0 anchors).  
**Round 2 narrowing:** Using Diffusion-TS (6.33), Tabular DiT (5.00), and Mixture-of-Diffusers (5.60) as primary anchors, the paper sits between them. It is weaker than Diffusion-TS in evidence completeness but stronger than Tabular DiT in novelty and stronger than SigDiffusions (4.33) overall.  
**Final score:** 5.5 — reflecting genuine novelty and strong results where evidence exists, tempered by significant gaps in baseline completeness and ablation analysis.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>