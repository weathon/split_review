Now I have a thorough understanding of the paper and can construct the final review by cross-verifying all claims.

---

## Summary

This paper proposes STREAM, a video evaluation metric that independently assesses spatial quality (STREAM-S: fidelity + diversity) and temporal naturalness (STREAM-T) of generated videos. By encoding each frame independently with DINO, applying FFT along the temporal axis, and using the zero-frequency amplitude for spatial evaluation while modeling non-zero frequencies via power-law fitting and skewness comparison for temporal evaluation, STREAM overcomes key limitations of FVD (spatial bias, 16-frame constraint, unbounded values). Experiments on toy data (CATER) and real datasets (UCF-101, Kinetics-600) demonstrate that STREAM behaves as expected under controlled degradations and provides insights into model strengths/weaknesses that composite scores like FVD obscure.

## Strengths

- **First metric to separately assess spatial and temporal aspects of video quality**: STREAM uniquely decomposes video evaluation into STREAM-T (temporal flow) and STREAM-S (fidelity/diversity). This is supported by controlled toy experiments (Figures 2–4) where STREAM-T is invariant to uniform visual noise while STREAM-S responds proportionally, and vice versa for temporal distortions. No prior metric (including FVD) offers such decomposition.

- **Bounded values enabling absolute interpretation**: Unlike FVD which has no upper bound (reaching 822 in Figure 4), STREAM sub-scores are bounded in [0,1], providing interpretable evaluation without requiring a reference comparison. This is explicitly listed as a contribution in §1.

- **Length-agnostic evaluation**: STREAM handles arbitrary video lengths without modification, whereas FVD is inherently limited to 16 frames by its I3D embedding network. This is demonstrated in §3.2.3 (Table 2) where STREAM evaluates 128-frame videos directly while FVD requires a sliding-window workaround (sFVD).

- **Explainability and actionable insights**: STREAM reveals specific model weaknesses beyond a single composite score. Table 1 shows TATS has high temporal naturalness (STREAM-T=0.9832) and realism (STREAM-F=0.9120) but low diversity (STREAM-D=0.0850), while Table 2 highlights a catastrophic drop in temporal coherence for long videos (TATS STREAM-T drops from ~0.98 to 0.0302). These insights are validated against human judgments (Spearman ρ=0.9 for realism, 0.6 for temporal coherence, §3.2.2).

- **Methodological novelty in temporal evaluation**: The use of FFT-based frequency decomposition on per-frame DINO features to separate spatial (DC component) and temporal (AC components) information is a clean and principled design choice, explained in §2.1–2.3.

## Weaknesses

### Fatal
None.

### Major

- **The power-law assumption underlying STREAM-T is not empirically validated.** The paper's central temporal metric (§2.3) rests on the assumption that the FFT amplitude spectrum of each DINO feature dimension follows a power law C·ζ^{−α}. The derivation of the skewness formula and the subsequent histogram-correlation comparison depend on this assumption being reasonable. However, the paper provides no goodness-of-fit metrics (e.g., R² for the least-square fits), no representative spectra from real or generated videos, and no discussion of what happens when this assumption is violated. While the toy experiments empirically demonstrate that STREAM-T behaves as expected under controlled temporal distortions (frame swaps, random translations), the lack of direct validation of the modeling assumption leaves a gap between the theoretical framing and the empirical evidence. The metric may well work—the toy experiments suggest it does—but the paper's explanation of *why* it works is incomplete. Addressing this would require showing, for several real and generated videos, that the power-law fit is adequate and reporting the distribution of α and fit quality.

### Minor

- **Unexplained patterns in long-video evaluation (Table 2).** STREAM-T for DIGAN drops from 0.9743 (16 frames) to 0.1327 (128 frames), while MeBT drops only from 0.9616 to 0.8265—an inversion across models that is not discussed. The paper focuses discussion on TATS's collapse (which is expected from prior work) but does not explain why DIGAN, a well-known architecture, exhibits near-complete temporal collapse while MeBT maintains reasonable temporal coherence. Additionally, Table 2 reports no standard deviations (unlike Table 1 which includes ± values for all metrics), despite the paper stating all results are averages of five repeated measurements (line 147). Standard deviations would help assess whether these differences are significant.

- **STREAM-D = 0.0000 for MoCoGAN-HD saturates the metric.** This value indicates that *all* generated mean features lie outside the real support under the k-NN estimate with k=5. The paper presents this result (§3.2.2, Table 1) without discussing whether this reflects genuine mode collapse or a metric artifact (e.g., sensitivity to k). Since this is the one model where the diversity metric completely saturates, a brief analysis would help the reader interpret the result correctly.

- **No limitations section.** The paper concludes (§4) with a one-paragraph restatement of contributions and no discussion of limitations. A metric paper would benefit from acknowledging known limitations, such as: dependence on the choice of image embedding network (DINO vs. CLIP could yield different results), the fact that STREAM-T discards the zero-frequency component and thus cannot detect temporally-consistent global appearance shifts, and the sensitivity of the P&R-based STREAM-S to the choice of k. These are real limitations that should be stated rather than left implicit.

- **Choice of histogram correlation versus divergence not motivated.** STREAM-T compares skewness histograms between real and generated data via correlation (Pearson's ρ on histogram bin counts). The paper does not explain why correlation is preferred over distributional divergences (e.g., Wasserstein distance, KL divergence) that are standard for comparing histograms. Correlation is sensitive to scale and location, and histogram binning discards ordering information. A brief justification would strengthen the methodological presentation.

- **Hyperparameter k=5 in STREAM-S not justified.** The paper sets k=5 for k-NN in the P&R-style support estimation (line 140) without any ablation or sensitivity analysis in the main text. P&R is known to be sensitive to k, and the video setting (using mean features to represent entire videos) may require a different choice than the default used in image P&R.

### Trivial
None.

## Nice-to-Haves

- A comparison of STREAM-T against simpler temporal coherence baselines (e.g., average frame-to-frame feature distance, CLIP temporal score) would help contextualize what the power-law + skewness approach adds.
- A brief note on computational cost (DINO encoding + FFT per dimension + power-law fitting) would help practitioners assess practicality.
- Ablation of k in STREAM-S (beyond the bin-size ablation already mentioned for the appendix) would strengthen the analysis.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Human evaluation details relegated to appendix** (Harsh Critic Point #2): The paper states Spearman ρ=0.9 for realism and 0.6 for temporal coherence, with full study details in the appendix. Per hard rules, criticisms about content that resides in the appendix (stripped by the parser) are removed. The key numbers are present in the main text.

2. **Qualitative samples referenced in appendix not verifiable** (from section-by-section notes): The paper references qualitative samples in \Aref{sec:sample_quality_of_short_gan}. Per hard rules, appendix-referenced content is assumed to exist in the original submission.

3. **Comparison against "velocity features" or frame differences** as alternatives for temporal representation: This demands a different paper rather than strengthening this one. Moved to Nice-to-Haves.

4. **Missing related works**: Per hard rules, I cannot confirm the existence or absence of related works without external sources.

5. **Formatting/style nitpicks and "typos"**: Per hard rules, all formatting/typographical concerns are parser artifacts and are removed.

6. **Criticism that "the reader cannot assess whether the study was well-designed"** regarding the human evaluation: This is a direct consequence of the appendix being stripped by the parser. Removed per hard rules.

## Novel Insights

Beyond the paper's own contributions, the most interesting pattern that emerges from the reviews is the asymmetry between the paper's two sub-metrics: STREAM-S (spatial) is methodologically straightforward (mean-DINO-feature + P&R) and easy to validate, while STREAM-T (temporal) involves a more complex pipeline (FFT → power-law fit → skewness → histogram correlation) whose components are individually plausible but collectively unvalidated as a chain. The toy experiments show the metric *works empirically*, but the paper's theoretical scaffolding around the power-law is both the most novel part and the least verified. This suggests a path for improvement: either simplify STREAM-T by validating each step empirically, or reduce reliance on the power-law assumption by using a nonparametric approach (e.g., directly comparing FFT amplitude distributions).

## Suggestions

- **Validate the power-law assumption empirically.** Show, for a few real and generated videos, representative FFT amplitude spectra across DINO feature dimensions with the fitted power-law overlaid, and report goodness-of-fit metrics (e.g., R²). This one addition would substantially strengthen the temporal metric's credibility.
- **Add a limitations paragraph** to the conclusion acknowledging the embedding-network dependence, the zero-frequency discard limitation in STREAM-T, and the k-sensitivity of STREAM-S.
- **Include standard deviations in Table 2** to match the reporting standard of Table 1, and briefly discuss why DIGAN and MeBT exhibit such different long-video temporal behaviors.
- **Comment on the STREAM-D = 0.0000 result** for MoCoGAN-HD to help readers distinguish genuine model failure from metric saturation.

## Score and Decision

The paper addresses an important and real problem (video evaluation metrics conflate spatial and temporal quality) with a well-motivated approach. The toy experiments are carefully designed and convincingly demonstrate STREAM's behavior under controlled conditions. The real-data experiments and model comparisons provide additional support. The main technical gap—unvalidated power-law assumption for STREAM-T—weakens the theoretical foundation but does not invalidate the empirical results, since the toy experiments demonstrate correct behavior regardless. Given that this is a conference paper and the core contribution (disentangled spatial/temporal evaluation) is useful and demonstrated empirically, the paper is above the acceptance threshold but would benefit from addressing the major weakness before final publication.

**Score**: 6.0 / 10 (weak accept)

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>