Now I have a thorough understanding of the paper and all calibration anchors. Let me compose the final consolidated review.

---

## Summary

USR 2.0 improves the Unified Speech Recognition (USR) semi-supervised framework by replacing slow autoregressive pseudo-labelling with CTC-driven teacher forcing: greedily decoded CTC outputs are fed into the decoder to generate attention pseudo-labels in a single forward pass, eliminating the AR bottleneck. Mixed sampling (alternating CTC-driven and AR modes with probability 0.5) mitigates the resulting exposure bias. The method halves training time, significantly improves out-of-distribution robustness (long utterances, noisy audio, unseen datasets), and achieves state-of-the-art results on LRS3, LRS2, and WildVSR across ASR, VSR, and AVSR with a single unified model.

## Strengths

- **Comprehensive OOD robustness gains**: The paper demonstrates consistent improvements across three distinct distribution-shift scenarios: long utterances (Figure 3a-b, USR 2.0 remains stable while USR degrades sharply beyond 150 frames), noisy audio (Table 1, AVSR at 0 dB: 14.0% vs. 14.8% for USR), and unseen datasets (Table 3, e.g., LibriSpeech ASR: 21.7% vs. 25.3% for USR under greedy decoding). These are not cherry-picked — they cover diverse real-world shifts.

- **Nearly 2× training speedup with maintained or improved accuracy**: Figure 5 convincingly shows USR 2.0 reaches lower VSR WER in roughly half the wall-clock time across three model scales and pre-training configurations. Table 2 confirms this speedup does not sacrifice final accuracy — USR 2.0 matches or outperforms USR and task-specific baselines on LRS3.

- **Well-designed ablation isolating the core mechanism**: Table 4 cleanly demonstrates that the CTC-driven mode achieves 24.2% OOD AVSR WER vs. 40.1% for standard AR mode, while maintaining competitive ID performance (3.2% vs. 2.9%). This directly validates the central claim that CTC-driven teacher forcing transfers CTC's robustness to the decoder.

- **Mixed sampling trade-off thoroughly characterized**: Figure 4 shows that the AR-mode sampling probability controls a clear, predictable trade-off between ID accuracy, OOD robustness, and training cost, with 0.5 providing a strong balanced optimum. Additional ablations (Appendix C.2, Table 10) dissect the relative weighting of CTC vs. attention pseudo-labels in the auxiliary losses.

- **Demonstrated scalability**: The Huge model (953M parameters, ~2500 hours unlabelled data) achieves 17.6%/0.9%/0.8% WER on LRS3 VSR/ASR/AVSR (Table 7 in Appendix), matching or exceeding heavily supervised systems that use external ASR models or 680k-hour Whisper encoders.

- **Qualitative analysis substantiates mechanistic claims**: Table 11 provides concrete examples of autoregressive degradation (omission, repetition) on long OOD utterances under USR, and shows USR 2.0 resolves these issues. Appendix C.4 further discusses CTC-conditioned sequence-level inconsistencies with specific examples, demonstrating honest engagement with the method's limitations.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **OOD evaluation relies on automatic Whisper transcriptions as reference**: The OOD robustness experiments on VoxCeleb2 (Section 5.1) and AVSpeech (Section 5.3) use automatically transcribed utterances from Whisper as ground truth. While the paper is transparent about this (noting samples are "automatically transcribed" and that Whisper is "treated as an oracle"), Whisper's own errors introduce noise into the reference transcriptions. The relative comparisons among methods remain valid since all are evaluated against the same references, and the qualitative examples (Table 11) corroborate the quantitative trends. Nevertheless, the paper should explicitly discuss this limitation and argue why it does not threaten the conclusions, rather than leaving it implicit.

- **Limited discussion of why adaptive AR-mode schedules do not outperform fixed sampling**: The constant probability of 0.5 is well-justified by the sweep in Figure 4. The paper mentions in a footnote that adaptive schedules were tried and performed similarly (Appendix C.2), but offers no explanation for why. A brief discussion (e.g., exposure bias is not monotonically decreasing in a simple way, or the model benefits from CTC-driven mode throughout training) would add insight.

### Trivial

None beyond parser artifacts in the extracted PDF (garbled tables/figures), which are not author errors.

## Nice-to-Haves

- A scatter plot or distribution of per-utterance WER differences between USR and USR 2.0 on an OOD set would complement the length-binned analysis and qualitative examples by showing whether the improvement concentrates on particularly challenging utterances.

- Brief discussion of whether CTC-driven teacher forcing could inspire fully non-autoregressive decoding schemes for inference-time use, given the observed robustness properties.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing appendix, missing proofs"** — The parser strips appendix sections; the original submission includes a thorough appendix (Appendix A–D) with hyperparameters, additional ablations, qualitative examples, and coherence discussion.

- **"Discuss why adaptive AR-mode schedules do not outperform fixed sampling" as a major gap** — The paper already addresses this in a footnote (line 364) and Appendix C.2. Not a missing element, just could benefit from slightly more discussion.

- **"Explore CTC-driven teacher forcing for fully non-autoregressive decoding" as a required contribution** — This is a nice direction for future work but well outside the paper's stated scope. Moved to Nice-to-Haves.

- **Strength Finder claim about "importance of problem"** — Removed as generic/superficial. All remaining strengths are concrete and evidence-backed.

## Novel Insights

Beyond the paper's own contributions, the key insight worth highlighting is the observation that global sequence coherence is unnecessary for effective knowledge transfer in the pseudo-labelling setting. The paper argues—and empirically demonstrates—that as long as teacher and student operate under the same forced CTC-derived inputs, token-wise cross-entropy training remains effective even when the teacher's output sequence contains malformed phrases or repetitions. This insight challenges the intuition that pseudo-labels must be globally coherent to be useful, and it may transfer to other sequence-to-sequence self-training domains (e.g., handwriting recognition, music transcription) where a fast, locally-conditioned alignment signal exists alongside a more expressive autoregressive decoder.

## Suggestions

- Add 1–2 sentences in Section 5 explicitly discussing the use of automatic Whisper transcriptions as reference: acknowledge the potential noise, argue why relative comparisons are unaffected, and note that the qualitative examples (Table 11) provide orthogonal validation.

- Expand the footnote about adaptive AR-mode schedules with a one-sentence hypothesis for why they don't help (e.g., "likely because exposure bias does not follow a simple temporal progression that monotonic scheduling can capture").

## Score Justification Against Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/yt40xuRBA9.md` (CTC-DRO) | 5.00 | Solid speech recognition paper with a clear method and good results. USR 2.0 has substantially broader experiments (multiple OOD scenarios, scaling, comprehensive ablations), achieves SOTA, and addresses a more general problem. Clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/HQMVRQUEaM.md` (Multilingual MT) | 5.33 | Good multimodal MT contribution with self-evolution mechanism. USR 2.0 is more thorough experimentally with larger empirical gains over baselines. |
| `/home/wg25r/review_agent/human_reviews_2026/dDHnO3Vhyj.md` (SALAD) | 6.00 | Well-motivated paper with strong analysis of text-speech gap. Notable weaknesses included missing validation of core motivation and limited experimental scope. USR 2.0 has fewer significant weaknesses and more comprehensive empirical validation. Comparable or slightly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/ghwxbTx7do.md` (SSPO) | 6.00 | Strong semi-supervised method with theoretical backing and empirics. USR 2.0 is comparably high-quality — a principled method with thorough validation and practical significance. |
| `/home/wg25r/review_agent/human_reviews_2026/wkRrpXD8Np.md` (Self-Training LLMs) | 2.67 | Fundamentally flawed — limited novelty, negative results unsurprising. USR 2.0 is far stronger across all dimensions. |
| `/home/wg25r/review_agent/human_reviews_2026/ISSxXXiu3w.md` (Chunk SSL) | 3.50 | Limited contribution, mixed reviews. USR 2.0 substantially stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/xGmWHCpVoM.md` (SS-SENet) | 3.50 | Limited scope and evaluation. USR 2.0 far more comprehensive. |

USR 2.0 exceeds the 5.0–5.33 band anchors in experimental breadth and empirical gains, and is comparable to or slightly stronger than the 6.0 anchors (SALAD, SSPO) when accounting for weakness severity. The core contribution is well-motivated, the method is elegant, the experiments are thorough, and the practical significance (halving training time, SOTA results, demonstrated scalability) is clear.

**Score: 6.5** — Strong accept. A clear, well-supported contribution that significantly improves a recognized bottleneck in semi-supervised speech recognition, with comprehensive experiments, practical gains, and insights that may transfer to other sequence-to-sequence self-training settings.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>