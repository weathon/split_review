Now I have sufficient calibration data. Let me compile the review.

**Round 1 Bracketing:** The paper is clearly stronger than the low-band (< 3.5) anchors (rejected papers with basic self-supervised approaches or narrow scope). It is substantially weaker than the high-band (> 7.5) anchors (FITS, TimeMixer++, ModernTCN — papers with extremely clean evaluations and broad acceptance). So the plausible bracket is **4.5–7.0**.

**Round 2 Narrowing:** After reading DADA (6.0, accepted — covers only AD, but clean eval), ROSE (5.75, rejected — covers only forecasting), and the zero-shot imputation paper (6.25, accepted — covers only imputation), I place TSPulse at approximately 6.0. It has broader task scope and more architectural novelty than these anchors, but the imputation overclaim brings it down from the upper part of the bracket.

Let me now write the full review.

## Summary

TSPulse proposes a family of 1M-parameter pre-trained time-series models with disentangled representations across temporal, spectral, and semantic spaces. The model achieves competitive or state-of-the-art results on anomaly detection (TSB-AD leaderboard top ranking), multivariate classification (UEA), similarity search, and imputation, while being orders of magnitude smaller than competitors and supporting CPU deployment. The architectural innovations include multi-space masked reconstruction with hybrid masking, post-hoc fusers (TSLens, MHT), and identity-initialized channel mixing.

## Strengths

1. **Ultra-lightweight model with strong results across multiple tasks**: TSPulse uses only 1M parameters yet outperforms models 10–340× larger on anomaly detection (+20–30% VUS-PR over pre-trained baselines, Figure 4), classification (+5–16% over VQShape/MOMENT/UniTS, Figure 5), and similarity search (+25–40% over MOMENT, Figure 7). The efficiency results (14× faster CPU inference than MOMENT, 120× faster than Chronos) are compelling and well-documented.

2. **Genuinely novel disentanglement approach**: The pre-training framework explicitly learns three complementary embedding views (temporal, spectral, semantic) via multi-output heads on separate decoder segments. Sensitivity analysis (Table 2) confirms disentanglement — e.g., temporal embeddings show 130% distortion under phase shift vs. semantic embeddings' 12%. Ablation (Table 1b) shows removing either short or long embedding reduces classification accuracy by 8–10%, validating the architectural contribution.

3. **Well-designed post-hoc fusers**: TSLens for classification (+11–16% over pooling, Table 1b) and Multi-Head Triangulation for anomaly detection (+9–16% over single heads, Table 1a) demonstrate that the disentangled views can be selectively fused for task specialization.

4. **Hybrid masking and identity initialization are practical contributions**: The hybrid masking strategy (Table 1c: 79% drop under block-only pre-training) and identity-initialized channel mixers (Table 1b: 9% improvement over random init) show clear practical value.

5. **Strong efficiency and reproducibility**: The paper provides public model weights and code, and documents deployment-friendly characteristics (CPU inference, small footprint).

## Weaknesses

### Fatal
None.

### Major

1. **Imputation results are significantly overstated.** The abstract claims "+50% on imputation" and Section 4.3 states "Compared to statistical interpolation methods, TSPulse shows 50%+ gains." However, Figure 6 shows that a simple interpolation baseline ("Interpol") achieves MSE 0.039, while TSPulse (ZS) achieves 0.074 — nearly double the error. The IMP% column for Interpol is left blank, and the text avoids comparing TSPulse (ZS) to this baseline, instead only citing Naive and Linear. While TSPulse (FT) matches Interpol at 0.039 and TSPulse (ZS) does outperform all other pre-trained models (MOMENT -73%, UniTS -56%), the headline claims are misleading. This does not invalidate the paper's broader contributions, but it requires correction: the imputation narrative must acknowledge Interpol's performance and the claims must be qualified to specify which baselines are being compared against.

2. **Zero-shot anomaly detection uses labeled data for head selection.** TSPulse (ZS) for AD employs a small labeled validation set to select the best-performing head among four (Section 4.1: "We adopt this tuning set for multi-head triangulation to select the best-performing head"). The paper discloses this, but the term "zero-shot" is stretched — other leaderboard methods also use this tuning set, so the comparison is fair on those terms, but a reader expecting fully unsupervised zero-shot performance would be misled. The ablation (Table 1a) shows `Head_ensemble` (0.44) vs. `Head_triang` (0.48), so the gap from labeled selection is quantifiable. This should be more prominently discussed.

### Minor

1. **No error bars or statistical significance.** All results (VUS-PR, accuracy, MSE, MRR) are single numbers without confidence intervals, standard deviations, or significance tests. This is common in the field but limits the reader's ability to assess whether reported improvements (especially the 5% classification gain over VQShape) are systematic.

2. **The imputation figure and text selectively exclude the strongest interpolation baseline.** The Interpol baseline outperforms TSPulse (ZS) but is mentioned only in the table with a blank IMP% column and no discussion in the text. Even if the appendix provides details (which is stripped here), the main text should transparently address this comparison.

3. **No systematic study of whether combined embeddings outperform single embeddings for each task.** The AD ablation (Table 1a) partially addresses this, but the paper would benefit from a more comprehensive analysis (e.g., using only time vs. only semantic embeddings for classification).

### Trivial
None beyond formatting artifacts (parser issues, not author errors).

## Nice-to-Haves
- Include confidence intervals or per-dataset variance across benchmarks.
- Clarify what "Interpol" is (e.g., cubic spline, linear interpolation) in the main text.
- Report `Head_ensemble` alongside `Head_triang` in Figure 4 for complete transparency about the zero-shot setting.

## Removed Points
- *"Classification comparison to data-specific models is unfair"* — The paper compares against both pre-trained and data-specific models, which is standard practice. This is not a weakness.
- *"Similarity search comparison against Chronos is not meaningful"* — Chronos embeddings can be used for retrieval; the paper also compares against MOMENT. This comparison is valid.
- *"Disentanglement is a strong term for different sensitivities"* — The sensitivity analysis (Table 2) shows clearly different robustness profiles across embedding types. The claim is supported.
- *"Missing related works"* — Per instructions, I cannot confirm the existence of missing works.
- *"Reproducibility concerns about undisclosed implementation details"* — The paper states models and code are publicly available; hyperparameters are in appendices.

## Novel Insights

The key insight that emerges from synthesizing the reviews is that TSPulse's core strength — its ultra-compact size combined with explicit disentanglement — is genuinely novel and well-supported for three of its four claimed tasks. The sensitivity analysis (Table 2) provides a clean demonstration that temporal, spectral, and semantic embeddings respond differently to perturbations, which is rare in the time-series pre-training literature. However, the imputation overclaim undermines trust in the paper's overall framing; the authors need to reset that narrative transparently. If corrected, the remaining contributions (AD leaderboard top ranking, classification gains with 1M parameters, efficient CPU inference) represent a solid advance for lightweight time-series models.

## Suggestions
1. **Correct the imputation narrative in both abstract and Section 4.3.** Acknowledge that simple interpolation (Interpol) achieves lower MSE than TSPulse (ZS). Reframe the "+50%" to specify it applies to comparisons against other pre-trained models (MOMENT, UniTS), not against all interpolation baselines. Alternatively, add a discussion of when interpolation fails (e.g., block-missing patterns) and show TSPulse's advantage in those regimes.
2. **Separate the two zero-shot variants in anomaly detection reporting.** Label `Head_triang` (with labeled tuning set) and `Head_ensemble` (fully unsupervised) distinctly in Figure 4, or at least reference the ablation clearly in the main results.
3. **Add uncertainty quantification** — at minimum, report standard deviations across datasets for the headline metrics.
4. **Include Interpol transparently** in the imputation ablation and discussion.

## Score and Decision

**Calibration Anchors Used:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| xJ5CF1aOOX (Self-supervised pre-training) | 2.50 | R1 | Much weaker: narrow scope, unclear methodology |
| qZz7PKt4bE (AutoTune TS Transformers) | 3.00 | R1 | Much weaker: only fine-tuning, no pre-training |
| aKcd7ImG5e (DADA: general AD) | 6.00 | R1/R2 | Similar: both pre-trained, but DADA covers 1 task, TSPulse covers 4. TSPulse has imputation overclaim. |
| KJ1w6MzVZw (Large PT time series) | 3.80 | R1 | Weaker: limited novelty, missing baselines |
| bWcnvZ3qMb (FITS: 10k params) | 8.00 | R1 | Stronger: cleaner evaluation, no overclaims |
| iI7hZSczxE (Disentangling TS) | 5.67 | R2 | Comparable scope on disentanglement, but less task coverage |
| tdttNKCtyB (ROSE: forecasting) | 5.75 | R2 | Weaker in scope (1 task vs 4), similar score band |
| NPSZ7V1CCY (Zero-shot imputation) | 6.25 | R2 | Comparable strength but only 1 task, cleaner claims |

**Round 1 bracket:** 4.5–7.0.
**Round 2 narrowing:** The paper sits near the DADA (6.0) anchor — similar empirical strength but broader task coverage. The imputation overclaim prevents it from reaching the 6.25 level of the zero-shot imputation paper. Score = 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>