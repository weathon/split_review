Now I have sufficient calibration. Let me write the final consolidated review.

## Summary

TSPulse introduces a family of ultra-light (1M parameter) pre-trained models for time-series diagnostic tasks — anomaly detection, classification, imputation, and similarity search. The key idea is to learn three specialized embedding views (temporal, spectral, semantic) through a masked reconstruction framework that applies different reconstruction objectives to different segments of a unified TSMixer backbone's output. The paper also contributes a hybrid masking strategy for pre-training, lightweight post-hoc fusers (TSLens, multi-head triangulation), and identity-initialized channel mixers for stable fine-tuning. Despite its tiny size, TSPulse achieves strong results across 75+ datasets, outperforming models 10–100× larger, including 20%+ VUS-PR gains on the TSB-AD leaderboard, 50%+ imputation improvements, and 5–16% classification gains on UEA — all while supporting CPU-only inference at sub-millisecond latency.

## Strengths

- **Comprehensive and convincing empirical evaluation across four diagnostic tasks.** TSPulse is evaluated on over 75 total datasets spanning the TSB-AD anomaly detection benchmark (40 datasets, both uni- and multivariate), 29 UEA classification datasets, 6 LTSF imputation datasets, and custom similarity search benchmarks. The zero-shot results are particularly strong: TSPulse (ZS, 0.48 VUS-PR) outperforms all prior methods on TSB-AD-U including fine-tuned ones, and improves over MOMENT by 73% in relative terms (Fig. 4). These gains are achieved with a model 40× smaller than MOMENT and 46× smaller than Chronos (Fig. 7 table).

- **Well-designed architectural components, each cleanly ablated.** The paper isolates the contribution of each design choice: removing TSLens causes 11–16% accuracy drop on classification (Table 1b); removing hybrid pre-training causes a 79% imputation MSE increase (Table 1c); removing either short or long embedding reduces classification accuracy by 8–10% (Table 1b); random (vs. identity) channel mixer initialization causes 9% drop. This level of decomposition makes it clear which pieces matter and by how much — a strength often missing in systems papers.

- **Practical impact: CPU-friendly, GPU-free deployment with public code/models.** The full 1M-parameter model runs inference on CPU in 0.387ms (Fig. 7), 14× faster than MOMENT and 120× faster than Chronos, while producing better retrieval accuracy. Models and source code are publicly released on Hugging Face, and the 1B-sample pre-training completes in one day on 8×A100 GPUs — a realistic resource footprint.

- **Sensitivity analysis demonstrating complementary embedding behaviors.** Table 2 shows that time embeddings are highly sensitive to phase shifts (130% distortion), FFT embeddings are moderately sensitive (21%), and semantic embeddings are robust (12%). Under missing data, semantic embeddings show 4.6% distortion vs. 8.3% (time) and 27.4% (FFT). These differences are measurable and translate to downstream task benefits — e.g., semantic embeddings excel at retrieval while time embeddings are critical for reconstruction.

## Weaknesses

### Major

- **"Disentanglement" framing overstates the architectural reality.** The paper claims "explicit disentanglement across spaces and abstractions" (abstract, contributions list), but the mechanism is loss-level separation, not architectural separation. All three token types (time, FFT, register) are concatenated and processed together by the same TSMixer backbone; the disentanglement is enforced only by assigning different reconstruction objectives to each segment of the decoder output. The paper acknowledges this in the architecture description ("is disentangled by optimizing each segment with a distinct head objective") but the title, abstract, and section headers use the stronger term. The sensitivity analysis (Table 2) confirms the embeddings have different properties — this is genuine *specialization* driven by different loss functions, which is a real contribution — but the community- standard meaning of "disentanglement" (e.g., β-VAE, FactorVAE) implies information-theoretic independence, which is neither enforced nor measured here. This mismatch risks misleading readers and is the main framing issue. The solution is straightforward: replace "disentangled" with "specialized" or "complementary" in the title and headline claims.

- **Imputation gains are predominantly attributable to hybrid masking, not the broader framework.** The ablation in Table 1(c) is unambiguous: removing hybrid pre-training (i.e., using standard block masking) causes a 79% MSE increase under hybrid-mask evaluation. The paper's abstract advertises "+50% on imputation" as a headline result of TSPulse, but nearly all of this advantage comes from the hybrid masking strategy itself, not from the disentangled representation learning, the lightweight backbone, or the reconstruction heads. The paper is transparent about this in the ablation section ("underscoring the importance of hybrid masking in pre-training"), but the high-level narrative conflates the masking contribution with other architectural innovations. A clearer decomposition — e.g., showing TSPulse's performance under block-mask evaluation separately from hybrid-mask evaluation — would remedy this.

### Minor

- **"Zero-shot" anomaly detection uses labeled tuning data for head selection.** The paper's setup for anomaly detection (Section 4.1) uses a small labeled tuning set — standard in TSB-AD — to select the best-performing reconstruction head via multi-head triangulation. While the paper is transparent about this ("when a small labeled validation set is available, it can be used to select the most effective head"), the abstract and introduction describe TSPulse as achieving "state-of-the-art zero-shot performance," and Figure 1 advertises "GPU-Free Zero-shot." This is a common practice (all leaderboard methods use the same tuning set), but it stretches the usual meaning of "zero-shot," which typically implies no labeled task data of any kind. The Head_time and Head_ensemble variants shown in Table 1(a), which require no tuning data, also outperform baselines (e.g., Head_ensemble at 0.44 VUS-PR vs. SubPCA at 0.42), so the claim holds qualitatively even without tuning; clarifying this in the high-level messaging would be more precise.

- **Similarity search evaluation uses custom benchmarks rather than standard retrieval tasks.** While the paper constructs reasonable testbeds from UCR data and synthetic augmentations, there is no evaluation on standard time-series retrieval benchmarks (e.g., UCR-based retrieval tasks or TS-Bench). The results are positive but the protocol is not directly reproducible or comparable against future work without the appendix details (which are stripped by the parser). This does not invalidate the results, but the evidence is weaker than for the other three tasks.

### Trivial

- Table 1(d) (similarity search ablation) is referenced in the text but the actual table content is not shown in the provided paper — only the surrounding description appears. This appears to be a formatting artifact.

## Nice-to-Haves

- Reporting per-dataset accuracy with standard deviation for UEA classification and variance across the 40 TSB-AD datasets would strengthen the benchmarking.
- Including a standard similarity search benchmark (e.g., UCR retrieval tasks) would improve reproducibility and comparability.
- Clarifying which task-specific pre-training variant is used for each experiment (since Section 3.1 says pre-training is specialized per task through loss reweighting).
- A mutual information analysis between embedding types would more directly validate the "disentanglement" claim if the authors choose to keep that framing.

## Removed Points

These points were raised by reviewers but are removed as invalid:

- **Criticism that disentanglement has "no mechanism preventing information mixing"** → REMOVED (overstated). The decoder outputs are explicitly split into segments (Time_E, FFT_E, Reg_E) and each segment receives a different reconstruction objective. While the backbone processes all tokens together, the loss-level separation + sensitivity analysis (Table 2) does show that the embeddings specialize differently. The paper's architectural description is clear about how separation works; the issue is only about whether "disentanglement" is the right label. The concrete concern about missing mutual information analysis is real but belongs in nice-to-haves, not as a claimed fatal flaw.

- **Criticism that the paper does not cite Darcet et al. (2024) for register tokens in-text** → REMOVED. The paper explicitly states "Motivated by recent advances in vision transformers (Darcet et al., 2024)" in Section 2 (Encoding block).

- **Criticism about "multiple pre-training variants" not being specified for each experiment** → MOVED to Nice-to-Haves. The paper says pre-training is specialized per task through loss reweighting (Section 3.1), and this is a reasonable approach, though more detail would help.

- **Strength claimed as "disentangled multi-space representation learning... confirming genuine disentanglement"** → WEAKENED. The evidence shows specialization, not information-theoretic disentanglement. The strength is real (different embeddings have different properties) but the label is too strong.

- **Strength about "state-of-the-art zero-shot performance with 10-100× smaller model size"** → KEPT with caveat about zero-shot labeling.

## Novel Insights

None beyond the paper's own contributions. The key insight — that different embedding segments optimized for different reconstruction objectives naturally specialize to different signal properties — is well articulated in the paper itself. The observation that this specialization enables lightweight post-hoc fusion (triangulation, TSLens) that outperforms single-embedding methods is the paper's own main finding.

## Suggestions

1. **Reframe "disentanglement" throughout** — replace with "specialized," "complementary," or "multi-view" in the title, abstract, and headline claims. The technical content and results do not depend on this word, and changing it would eliminate the main source of overclaiming.

2. **Separate imputation results by evaluation masking type** — show TSPulse's performance under block-mask evaluation and hybrid-mask evaluation separately, so readers can clearly see the contribution of hybrid masking vs. the rest of the framework.

3. **Clarify the "zero-shot" language for anomaly detection** — note that Head_time, Head_fft, and Head_ensemble variants (which need no tuning data) also achieve strong results, or explicitly define "zero-shot" as "no training on target data" (which is accurate) rather than implying no labeled data of any kind.

## Score and Decision

**Round-1 bracket:** Between 5.5 and 7.5 (clearly stronger than papers scoring 3.8–5.25 like "Large Pre-trained time series models" and "NuwaTS"; not as clean and principled as 8.0 papers like FITS).

**Round-2 anchors read in full:** DADA (6.0, Accept) — general anomaly detector but only one task, some innovation concerns about AdaBN. ROSE (5.75, Reject) — register-assisted forecasting, limited to one task, complex. TSPulse is stronger than both: broader evaluation (4 tasks vs. 1), cleaner ablations, better empirical results, and practical CPU deployment. The framing issues prevent it from reaching the 7.5+ tier, placing it solidly in the 6–7 range.

**Final score:** 6.5 — a well-executed paper with genuine contributions (lightweight multi-view pretraining, hybrid masking, post-hoc fusers, strong empirical results) and public code/models. The main weaknesses are framing overclaims (disentanglement, zero-shot labeling, imputation attribution) that are fixable with language changes and do not undermine the core empirical contributions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>