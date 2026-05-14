Now I have all the information I need. Let me write the consolidated review.

---

## Summary

DiSTAR proposes a zero-shot TTS framework that couples an autoregressive language model (serving as a patch-level "sketcher") with a masked-diffusion model (serving as a parallel "infiller"), operating entirely in a discrete RVQ code space. The design eliminates the need for duration predictors or forced alignment and introduces practical inference-time controllability via RVQ layer pruning and decoding heuristics. Experiments on LibriSpeech-PC and SeedTTS benchmarks show strong WER, speaker similarity, and subjective quality, with a relatively compact model (0.15B–0.3B parameters).

## Strengths

- **Clean architectural unification.** Pairing an AR sketcher with a masked-diffusion infiller in a shared discrete RVQ code space is conceptually elegant. The design naturally handles both long-range coherence (via autoregressive patches) and intra-patch parallelism (via discrete masked diffusion), without forced alignment or a duration predictor. This genuinely simplifies the TTS pipeline compared to cascaded or multi-stage alternatives.

- **Strong WER and speaker similarity across benchmarks.** On LibriSpeech-PC test-clean, DiSTAR-medium achieves 1.66% WER and 0.67 SIM; on SeedTTS test-en, 1.32% WER and 0.66 SIM (Table 1). These are the best WER numbers among all compared systems. Subjective evaluation (Table 2) shows CMOS of 0.22 and SMOS of 3.31, also leading all competitors.

- **Practical inference-time controllability without retraining.** Stochastic layer truncation during training (randomly dropping upper RVQ layers) enables test-time bitrate/compute control by simply pruning RVQ layers. Figure 2 shows a smooth speaker-similarity vs. compute trade-off, with WER remaining stable. This is a well-executed practical feature.

- **Healthy scaling behavior with modest model size.** DiSTAR-base (0.15B) already outperforms larger baselines like IndexTTS (0.5B) and DiTAR (0.6B) on WER, and scaling to 0.3B improves all metrics (Table 1).

- **Reasonable ablation breadth.** The paper ablates decoding strategies (Table 3), CFG configurations (Table 5), and patch size (Table 6), providing evidence that design choices matter.

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled baseline comparisons weaken the SOTA claim.** The main Table 1 draws DiTAR results from the original paper (marked ♦) without re-running under the same codec, training data, or evaluation pipeline. DiTAR uses a different codec (continuous) and different training data; IndexTTS, E2TTS, and F5TTS each have their own codec/data/eval setups. While cross-paper comparison is common in TTS, the paper's central claim of surpassing these systems cannot be rigorously attributed to the proposed method versus differences in codec quality, dataset scale, or evaluation software. The subjective evaluation (Table 2) additionally omits DiTAR and IndexTTS while including FireRedTTS and CosyVoice 2, creating an incomplete picture.

- **Inference-efficiency claims are unsupported by measurements.** The paper claims DiSTAR "maintains inference cost close to its continuous counterpart DiTAR" and offers "comparable or lower computational cost." No wall-clock time, RTF, FLOP counts, or throughput measurements are reported for any system. Figure 2 shows the relative trade-off from RVQ pruning, which demonstrates controllability but does not substitute for absolute efficiency comparison. This is a statement about a claimed contribution that lacks evidence.

### Minor

- **Anomalous quantitative results deserve discussion.** DiSTAR-medium achieves WER of 1.66%, below the RVQ-resynthesized baseline of 1.83% (Table 1, LibriSpeech). Subjective results show CMOS 0.22 (above the human anchor at 0.00) and SMOS 3.31 (above human at 3.07). While these are not "physically impossible" as one reviewer claimed — generative models can produce cleaner speech than codec reconstruction, and human reference recordings can contain artifacts that clean synthesis avoids — the paper should acknowledge and discuss these anomalies rather than passing over them in silence. The brief attribution to "reduced sensitivity to high-frequency artifacts" (Section 4.2) is a start but insufficient.

- **Decoding heuristics are motivated but not deeply analyzed.** The paper describes a "tail-first" overconfidence bias and proposes three heuristics (layer-wise temperature, position-wise temperature, hybrid sampling). Table 3 shows these improve WER from 2.11 to 1.99 and SIM from 0.626 to 0.640. While this is empirical evidence of effectiveness (contrary to claims that none exists), the specific temperature values (0.8, 0.95) and the 50-50 sampling/greedy split are not justified through sweeps or held-out validation. A confidence distribution plot demonstrating the claimed tail-first bias would strengthen the motivation.

- **Some evaluation details are underspecified.** The UTMOS checkpoint version is not reported (this predictor is known to be domain-sensitive). For baselines cited from prior work, it is unclear whether the same Whisper-large-v3 ASR version was used for WER computation. These details matter for reproducibility.

### Trivial

- Overlapping patches in the aggregator are motivated by a brief analogy to CNNs but not ablated — this is a small design choice that does not affect the core contribution.
- The patch-size ablation (Table 6) shows severe degradation at P=2 (WER 4.50%) with only a brief explanation. A slightly deeper analysis would strengthen this section but is not essential.

## Nice-to-Haves

- Re-running the most direct baseline (DiTAR) with the same RVQ codec and training data would substantially strengthen the SOTA comparison.
- Reporting end-to-end RTF or GFLOPS for DiSTAR versus DiTAR and at least one other system would substantiate the efficiency claims.
- A confidence-histogram or mask-ratio plot demonstrating the tail-first bias would better justify the decoding heuristics.
- Side-by-side spectrograms comparing DiSTAR, DiTAR, and codec reconstruction would make quality claims more tangible.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Physically impossible" WER claim (DiSTAR WER < RVQ resynth).** Removed. The RVQ-resynthesized baseline is NOT a theoretical lower bound for WER — ASR models can find clean synthetic speech easier to transcribe than codec-reconstructed speech that contains quantization artifacts. The generative model can implicitly act as a denoiser. This is a known phenomenon in TTS, not a physical impossibility.

- **"Not fully discrete" framing complaint.** Removed. The paper's claim that it "operates entirely in a discrete RVQ code space" clearly refers to the token space (inputs and outputs are discrete RVQ tokens), not to internal continuous embeddings. All discrete-token Transformer models use continuous embeddings internally — this is standard and not misleading.

- **"No empirical evidence" for decoding heuristics.** Removed as stated. Table 3 directly compares sampling without heuristics (WER 2.11, SIM 0.626) against sampling with the proposed heuristics (WER 1.99, SIM 0.640), providing direct empirical evidence of their effect. The criticism is reframed above as a call for deeper analysis rather than absence of evidence.

- **Demand for "equitable baseline re-evaluation."** Moved to Nice-to-Haves. While cross-paper comparison is standard practice in TTS benchmarking, re-running under matched conditions would strengthen claims.

- **Demand for spectrogram visualizations.** Moved to Nice-to-Haves. Numerical scores are the primary evaluation modality in this literature.

- **Complaint about missing appendix sections.** Removed. The parser strips appendix sections; they exist in the original submission.

- **Criticism of evaluation data/checkpoint existence.** Removed. All cited baselines (DiTAR, IndexTTS, E2TTS, F5TTS, etc.) are publicly available models.

- **"Half-sampling/half-greedy appears hand-tuned on evaluation set."** Removed as speculation. The paper explicitly states "we adopt a simple half–half scheme to avoid over-tuning" (Section 3.4).

## Novel Insights

None beyond the paper's own contributions. The core insight — that an AR drafter + masked-diffusion infiller can be unified within a shared discrete RVQ code space, eliminating alignment modules while enabling controllable inference — is the paper's original contribution, and the reviews do not surface a deeper insight beyond this.

## Suggestions

1. Add a brief discussion in Section 4.2 acknowledging that DiSTAR's WER can fall below the RVQ-resynth baseline and that subjective scores can exceed the human reference, and explain why this can legitimately occur (cleaner synthesis vs. reference artifacts, Whisper sensitivity to codec noise).

2. Either report RTF/GFLOPS for DiSTAR vs. DiTAR on matched hardware, or soften the efficiency claims in the introduction and conclusion to reflect only the demonstrated RVQ-pruning controllability.

3. Clarify in the experimental settings which UTMOS checkpoint and Whisper version were used, and whether the same ASR was used for baseline WER numbers cited from prior work.

4. Consider a brief ablation of the temperature shaping parameters or note that they were selected on a small held-out validation set to preempt concerns about test-set overfitting.

## Score and Decision

### Calibration anchors used:

| Path | Avg Human Score | Comparison to DiSTAR |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/FaGDopTTTC.md` (DiFlow-TTS) | 2.50 | Similar domain (discrete TTS). DiSTAR is substantially stronger: better WER, more extensive evaluation, cleaner architecture, and includes subjective results. |
| `/home/wg25r/review_agent/human_reviews_2026/YsrswIqSZ9.md` (UniTTS) | 3.20 | LLM-based TTS with codec. DiSTAR has stronger objective results, better-substantiated claims, and a more clearly novel architecture. |
| `/home/wg25r/review_agent/human_reviews_2026/im2a2MHoke.md` (Soft Alignment TTS) | 2.50 | Non-autoregressive TTS. DiSTAR is clearly more novel and better evaluated. |
| `/home/wg25r/review_agent/human_reviews_2026/ADRwyhQWzY.md` (BELLE) | 3.00 | Codec TTS. DiSTAR has more competitive results and more extensive evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/h5KLpGoqzC.md` (VoxCPM) | 5.20 | Hierarchical semi-discrete TTS, end-to-end, 0.5B params, accepted as poster. DiSTAR is comparably strong: cleaner architecture (no multi-stage complexity), better WER, smaller model, similar evaluation gaps (no latency data). |
| `/home/wg25r/review_agent/human_reviews_2026/yh7MV2V0ba.md` (VADD) | 5.50 | Discrete diffusion with latent variables, accepted as poster. DiSTAR is more applied with stronger empirical validation, but VADD has stronger theoretical novelty. Comparable in overall contribution quality. |
| `/home/wg25r/review_agent/human_reviews_2026/uGai5lYHlV.md` (TTSDS2) | 5.33 | Evaluation benchmark, accepted as oral. Different type of contribution; not directly comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/43LvSiz6af.md` (TTS-Hub) | 4.40 | Controllable TTS with LoRAs. DiSTAR has stronger core results and a more principled architecture. |
| `/home/wg25r/review_agent/human_reviews_2026/pz1tpHPiM3.md` (MOS-RMBench) | 3.33 | Evaluation benchmark, different contribution type. |

DiSTAR is clearly stronger than the 2.5–3.3 range papers (DiFlow-TTS, UniTTS, BELLE). It is comparable to VoxCPM (5.20, accepted poster) and VADD (5.50, accepted poster). Compared to VoxCPM, DiSTAR has a cleaner design and stronger WER but similar weaknesses (no latency data, some evaluation gaps). Compared to VADD, DiSTAR has much more extensive empirical validation but less theoretical depth.

The core contribution — a clean, well-motivated architectural unification of AR and masked diffusion in discrete RVQ space — is genuinely novel and well-executed. The empirical results are strong across multiple benchmarks. The main weaknesses are evaluation rigor (uncontrolled baselines, missing efficiency data) that weaken the SOTA claim but do not undermine the architectural contribution. These are addressable in a rebuttal or camera-ready.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>