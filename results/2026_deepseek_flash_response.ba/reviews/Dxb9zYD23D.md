## Summary

This paper proposes ST-Diff, a framework for unconditional multivariate time series generation that reframes time series as "videos" via the Short-Time Fourier Transform (STFT). The key idea is to convert a multivariate time series into a spectro-temporal video tensor (time × frequency × covariates), then apply a custom video diffusion model with domain-specific architectural biases (anisotropic patching, learned bias matrices for covariate and frequency attention). The approach outperforms existing time-domain and image-based diffusion baselines on standard benchmarks, with particularly striking gains on long sequences.

## Strengths

1. **Genuinely novel paradigm, well-motivated.** The "time-series-as-video" representation via STFT preserves the temporal axis explicitly while revealing spectral structure — unlike prior work that either operates in the time domain (losing spectral structure) or collapses time into a static 2D image (losing temporal dynamics). The invertibility of STFT back to the time domain makes this principled. The motivation (Section 1, lines 17–21) is clear and compelling.

2. **Thoughtful architectural inductive biases.** The anisotropic patching (Section 4.3, line 93–94) aggregates along frequency while preserving unit granularity along the covariate axis, justified because covariates are an unordered set. The learnable bias matrices B_C and B_F initialized from empirical cross-correlation and log-magnitude covariance provide domain-specific priors that generic video diffusion lacks.

3. **Strong quantitative results, especially on long sequences.** Table 2 on ETTh shows the Discriminative Score stays near-constant across lengths 64→128→256 (0.030→0.032→0.029) while Diffusion-TS degrades substantially. Context-FID at length 64 (0.031 vs. 0.631 for Diffusion-TS) is over an order of magnitude better. This strongly supports the claim that preserving the temporal axis via the video representation avoids the degradation that plagues both time-domain and image-based methods.

4. **Multi-faceted qualitative evaluation.** Beyond standard discriminative/predictive scores, the paper provides t-SNE, KDE, ACF, and PSD visualizations (Figures 3–4) that corroborate quantitative results from multiple angles — embedding space, marginal distributions, temporal autocorrelation, and spectral density.

## Weaknesses

### Major

1. **No ablation studies.** The framework has multiple interlocking components whose individual contributions are never isolated: (a) the EMA-based trend-residual decomposition, (b) the STFT-based video representation vs. raw time-domain or single-image alternatives, (c) the anisotropic patching strategy, (d) the learned bias matrices B_C and B_F, and (e) the cross-covariance loss on STFT magnitudes. Without ablations, it is impossible to attribute the reported performance to the core time-series-as-video paradigm vs. auxiliary losses or favorable hyperparameter choices. This is a substantial gap for a paper whose central claim is that its *representation* and *tailored architecture* deliver gains.

2. **Incomplete baseline comparison weakens the claimed SOTA.** For two of four evaluation metrics (Context-FID and Correlational Score), the strongest modern baselines (Diffusion-TS, ImagenTime) are marked "—" (not reported) across all six datasets in Table 1. This means ST-Diff is compared against only TimeGAN and TimeVAE — older, weaker baselines — on half the evaluation dimensions. The "21 out of 24 metric-dataset combinations" claim is mathematically correct given what is reported, but many of those wins are uncontested because competitors have no entry. The SOTA assertion as stated is stronger than what the evidence supports.

3. **Context-FID metric is not defined in the main paper.** Context-FID is used as one of four primary quantitative metrics (Table 1, line 148) but the evaluation metrics section (lines 109–110) defines only Discriminative, Predictive, and Correlational scores. Without knowing what Context-FID measures, the reader cannot interpret scores like "0.031" or assess whether improvements of various magnitudes are meaningful.

### Minor

4. **Cross-covariance loss is underspecified.** The loss appears once (line 140) with a high-level description: "quantifies the discrepancy between normalized covariance matrices." No mathematical definition, no weighting relative to the MSE noise-prediction loss, no ablation demonstrating its contribution. Since the architecture already has strong spectral inductive biases, it is unclear whether this loss drives the results or the architecture does.

5. **Two values in ST-Diff cells of Table 1 are unexplained.** Each ST-Diff cell contains two numbers (one regular, one bolded) with no caption or footnote explaining whether these represent two runs, two configurations, or a parser artifact. This makes the table difficult to interpret.

6. **Limited long-sequence evaluation scope.** The long-sequence results (Table 2) are on ETTh only. While impressive, they cover just one of six datasets. If the method's advantage is supposed to grow with sequence length, demonstrating this on more datasets would substantially strengthen the claim.

### Trivial

7. **EMA trend decomposition is presented without discussion of alternatives.** The paper uses EMA for trend-residual decomposition (line 71) but does not discuss or justify this choice over alternatives like STL or seasonal-trend decomposition. This is a minor design consideration.

## Nice-to-Haves
- Adding a computational cost comparison (parameters, training time, inference speed) would contextualize the acknowledged higher cost of spatiotemporal architectures.
- Running Diffusion-TS and ImagenTime in the same evaluation framework for Context-FID and Correlational scores would substantiate or qualify the SOTA claim.
- A systematic ablation study isolating each component (as described in Major weakness 1) would resolve the primary methodological concern.

## Removed Points

These points were flagged during review synthesis but are excluded from the main review with justification:

- *"The short-sequence setting (L=24) is unusually easy"* — REMOVED because the paper states that L=24 is the standard evaluation protocol used in prior work (Naiman et al., 2024; Yuan & Qiao, 2024), and the paper additionally evaluates long sequences on ETTh (Table 2). This criticism does not account for the stated convention.

- *"Reproducibility: anisotropic patch size, number of transformer layers, attention heads not reported"* — REMOVED per instructions: these are nitpicks about trivial implementation details that a conference paper cannot fit in the main body and would be in the (stripped) appendix.

- *"The SOTA claim is lopsided"* — MERGED into Major weakness 2 with specific evidence. The original framing as "fatal" was downgraded because the claim is not false, merely overstated.

- *"Missing related works"* — REMOVED per instructions (I cannot confirm whether cited works exist or not).

- *"Formatting, grammar, typo issues"* — REMOVED per instructions (parser artifacts, not author errors).

- *Strength: "the problem is important"* — REMOVED as generic. All papers in this area address important problems.

- *Strength: "principled handling of non-stationarity"* — RETAINED but de-emphasized as it is a straightforward EMA decomposition without comparison to alternatives.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one synthetic observation: the paper presents an elegant inversion of the standard design space. Prior work either (a) operates in the time domain with frequency-domain *losses* (Diffusion-TS uses Fourier-based loss) or (b) collapses time into a static image representation (ImagenTime). ST-Diff instead makes the time-frequency representation the *primary domain* of the generative process and uses standard MSE noise-prediction loss (plus a cross-covariance auxiliary loss). This design choice — making the representation do the heavy lifting rather than the loss function — is a philosophically different approach that the paper does not explicitly articulate as a design principle, but that emerges from reading the method and positioning together.

## Suggestions

1. **Add a systematic ablation study** isolating: (a) ST-Diff without the cross-covariance loss, (b) ST-Diff with isotropic (square) patching, (c) ST-Diff without the bias matrices B_C/B_F, (d) ST-Diff applied directly to raw time series (skipping STFT, treating the multivariate sequence as a 1D "video") to isolate the benefit of the spectro-temporal representation itself. Without these, the contribution of individual components cannot be assessed.

2. **Define Context-FID** explicitly in the main text, or add a clear reference to its definition location.

3. **Complete the baseline comparison** by either running Diffusion-TS and ImagenTime in the same evaluation framework for Context-FID and Correlational scores, or transparently explaining why this cannot be done.

4. **Clarify the two values in ST-Diff rows** of Table 1 with a caption or footnote.

5. **Extend long-sequence evaluation** to at least 2–3 additional datasets beyond ETTh to substantiate the scalability claim.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
> "time series generation diffusion model unconditional" queries across bands

- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/RDLvnUJ5JZ.md` — avg 3.00 (reject; weak paper on TS diffusion forecasting). ST-Diff is clearly stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2whSvqwemU.md` — avg 3.00 (reject; FM-TS, flow matching for TS generation). ST-Diff is notably stronger in novelty and method.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/zB6uMznFuZ.md` — avg 3.00 (reject; latent diffusion for heterogeneous TS). ST-Diff is stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2orBSi7pvi.md` — avg 3.00 (reject; spatio-temporal diffusion for TS analysis). ST-Diff is stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/4h1apFjO99.md` — avg 6.33 (accept; **Diffusion-TS**, direct baseline). ST-Diff has more novel paradigm but weaker experimental rigor (no ablations, incomplete baseline comparison). Slightly weaker overall.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/etUJR2xBYa.md` — avg 4.20 (reject; TimeDiT). ST-Diff is stronger in both novelty and execution.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/b3CzCCCILJ.md` — avg 6.00 (accept; diffusion guidance method, not TS-specific). Different domain.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lcmd2Qdrsv.md` — avg 5.60 (reject; Mixture-of-Diffusers). ST-Diff has more novel core idea and better qualitative evaluation; comparable experimental rigor issues.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/I5lcjmFmlc.md` — avg 8.00 (reject; image diffusion classifier, different domain). Not comparable.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/RuP17cJtZo.md` — avg 8.00 (accept; Generator Matching, foundational theory). Not comparable.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/uKZdlihDDn.md` — avg 7.60 (accept; fluid simulation diffusion). Different domain.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/CxXGvKRDnL.md` — avg 8.00 (accept; image compression diffusion). Different domain.

**Round 1 bracket:** The paper is clearly above the 3.00-level weak papers and below the 7.5+ outstanding papers. The plausible range is **4.0–6.5**, with the most direct comparison being Diffusion-TS (6.33) above and TimeDiT (4.20) below.

**Round 2 (Narrowing):**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/4h1apFjO99.md` — 6.33 (Diffusion-TS). ST-Diff has more novel paradigm but no ablation studies (Diffusion-TS had ablations in appendix). ST-Diff is slightly weaker.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lcmd2Qdrsv.md` — 5.60 (MoD, rejected). ST-Diff has more novel core idea and better qualitative validation; comparable on experimental gaps. ST-Diff is slightly stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/qae04YACHs.md` — 6.33 (TMDM, forecasting, different task). Not directly comparable.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/HdUkF1Qk7g.md` — 6.00 (D3U, forecasting, different task). Not directly comparable.

**Final bracket:** The paper sits between the rejected MoD (5.60, slightly weaker) and the accepted Diffusion-TS (6.33, slightly stronger). The core contribution is more novel than both, but the experimental rigor is below the accepted-paper standard for this venue.

**Round 1 bracket:** 4.0–6.5  
**Round 2 narrowing:** The paper is between MoD (5.60, rejected) and Diffusion-TS (6.33, accepted) — closer to MoD due to the absence of ablations and incomplete baseline comparison.

**Final score:** 5.5

### Decision Rationale

This paper presents a genuinely novel and well-motivated paradigm (time-series-as-video) with thoughtful architectural design and strong results, particularly on long sequences. However, the experimental evaluation has critical gaps that prevent the claims from being fully supported at a top venue: **(1) no ablation studies** to isolate which of the many intertwined components drive performance, **(2) incomplete baseline comparison** where the strongest competitors are missing entries for half the evaluation metrics, and **(3) an undefined primary metric** (Context-FID). These gaps make it impossible to conclusively attribute the reported gains to the core contribution. The core idea is valuable enough to warrant revision, but the paper in its current form does not provide sufficient evidence.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>