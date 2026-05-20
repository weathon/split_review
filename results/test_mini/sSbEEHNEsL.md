Now I have sufficient calibration data. Let me produce the final consolidated review.

## Summary

This paper proposes USR 2.0, an improved semi-supervised framework for unified audio-visual speech recognition. The key idea is **CTC-driven teacher forcing**: instead of slow autoregressive decoding to generate attention-based pseudo-labels, the teacher's greedily-decoded CTC outputs are fed into the decoder to produce attention targets in a single forward pass. Since CTC and the resulting attention pseudo-labels are aligned in length, the student predicts both jointly, coupling the branches for robustness. A mixed-sampling schedule (50% CTC-driven, 50% autoregressive) mitigates exposure bias. The paper demonstrates that USR 2.0 yields ~2× faster training, substantially improved OOD robustness (long utterances, noise, cross-dataset), and state-of-the-art in-distribution results on LRS3 (17.6%/0.9%/0.8% VSR/ASR/AVSR with Huge model), all with a single unified model.

## Strengths

- **Novel and well-motivated method.** CTC-driven teacher forcing is a clever insight — the observation that global coherence is unnecessary in the pseudo-labelling setting (since teacher and student share the same forced input) turns a seeming weakness into a feature. The joint CTC-attention prediction via aligned targets is elegant and cleanly explained (Equations 3–6, Section 4).

- **Comprehensive OOD evaluation with large margins.** The paper evaluates robustness across three challenging dimensions — long utterances (Figure 3), additive noise at multiple SNRs (Table 1), and cross-dataset transfer to LibriSpeech, WildVSR, and AVSpeech (Table 3). The gains are substantial and consistent: e.g., LibriSpeech WER drops from 25.3% (USR) to 15.4% (USR 2.0), a 39% relative improvement. The bucketed analysis of long utterances shows USR 2.0 remains stable while USR collapses (from ~4.6% at 50 frames to ~60% at 400 frames with greedy decoding).

- **State-of-the-art in-distribution results with a single unified model.** Table 2 shows USR 2.0 matching or surpassing all prior methods — including those using separate models per modality — across VSR, ASR, and AVSR at multiple model scales. The Huge model achieves 17.6%/0.9%/0.8% on LRS3, setting a new SOTA. The pattern of larger gains when VoxCeleb2 is used as unlabelled data coherently supports the hypothesis that OOD robustness → better pseudo-labels → better in-distribution performance.

- **Well-designed ablations.** Table 4 cleanly isolates the contribution of each pseudo-label type: removing CTC targets from the decoder hurts OOD (35.1% vs. 24.2%), while removing attention targets hurts in-distribution (3.6% vs. 3.2%). Figure 4 provides a useful sensitivity analysis of the mixed-sampling probability (0.0–1.0), showing OOD stability up to 60% AR probability before sharp degradation, with explicit training-time trade-offs.

- **Training efficiency is clearly demonstrated.** Figure 5 plots VSR WER against wall-clock training time across multiple model scales, directly showing that USR 2.0 reaches a given WER in roughly half the time of USR. The paper explains the speedup as a combination of faster per-step computation (CTC-driven teacher forcing avoids AR decoding) and faster convergence (50 vs. 75 epochs).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **OOD evaluation relies on automatically transcribed references without noise analysis.** The OOD evaluations on VoxCeleb2, LibriSpeech, WildVSR, and AVSpeech use Whisper transcriptions as ground truth (acknowledged in Section 5.1: "treating Whisper… as an oracle"). While this is standard practice given the lack of human transcripts for these datasets, the paper does not discuss how reference noise could affect relative rankings — e.g., if Whisper has systematic biases on certain accents or noise conditions, apparent improvements could be partially confounded. A human-verified subset or a robustness analysis (e.g., measuring agreement between methods under varying reference quality) would strengthen the OOD claims. This does not invalidate the results but weakens their precision.

2. **Training time evidence is graphically presented but lacks precise tabular breakdown.** Figure 5 provides a convincing visual comparison, but the paper would benefit from a table reporting total training hours, number of steps, and average step time for each model scale and pre-training setup. Currently, the reader must estimate from the figure. The headline claim of "~2× faster training" deserves this level of precision for reproducibility. Additionally, an ablation controlling for training duration — training USR for the same wall-clock time as USR 2.0 — would help separate gains attributable to the method itself from gains from simply training with more efficient steps.

3. **Decoding protocol for baselines in Table 2 is underspecified.** USR 2.0's inference uses beam size 40 and CTC weight 0.1 (Section 4.3). For AV-HuBERT and other self-supervised baselines compared in Table 2, the decoding settings (beam size, CTC weight, attention-only vs. joint decoding) are not stated. While baseline numbers are taken from published papers, specifying the protocols in a footnote would improve fairness assessment and reproducibility.

4. **Interaction between masking and CTC conditioning is not explicitly stated.** In CTC-driven mode, the student receives masked inputs (modality-specific masking) but conditions its decoder on teacher CTC PLs. The paper does not clarify whether the teacher's CTC PLs are generated from unmasked audiovisual inputs regardless of the student's mask, or whether masking affects the conditioning. The design is likely sensible (teacher always sees full unmasked input), but this should be stated explicitly (Section 4).

### Trivial
None.

## Nice-to-Haves

- A controlled experiment isolating the effect of CTC-attention coupling from the effect of faster training: train USR with the same number of steps as USR 2.0 but keeping the original AR-based PL generation, then compare.
- A small human-verified subset (e.g., 100 samples) of the OOD data to confirm that Whisper transcription noise does not affect method rankings.
- A brief limitations paragraph acknowledging the dependence on Whisper-transcribed OOD references and the sensitivity of the EMA momentum schedule.

## Removed Points

- **Missing LRS2/WildVSR main-paper results.** The harsh critic flagged that SOTA claims for LRS2 and WildVSR appear only in the appendix. Per policy, the appendix was stripped by the parser (it exists in the original submission), and this criticism cannot be verified. Removed.
- **"33% epoch reduction alone does not give 2×."** The paper explicitly states two factors: (a) faster per-step computation (CTC-driven teacher forcing bypasses AR decoding) and (b) fewer epochs (50 vs. 75). Figure 5 provides direct wall-clock evidence. Removed as factually inaccurate reading of the paper.
- **Strawman about missing baselines or unfair comparison favoring the author's method.** The comparison asymmetry, if any, favors the baselines (which can use separate models per modality), not USR 2.0. Removed per policy.
- **Generic formatting/style nitpicks and missing related work.** Removed per policy.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no fundamentally new observation about the method or its implications beyond what the paper already articulates. The core insight — that global coherence is unnecessary for pseudo-labels and that CTC-driven teacher forcing enables joint prediction — is the paper's own contribution.

## Suggestions

1. Add a small table reporting total training hours, number of steps, and average step time for each model scale (Base, Base+, Large, Huge) for both USR and USR 2.0.
2. Specify the decoding protocol (beam size, CTC weight, attention-only vs. joint) for each baseline in Table 2, either in a footnote or in the caption.
3. Add a brief note in Section 4 clarifying that the teacher's CTC PLs are generated from unmasked audiovisual inputs regardless of the student's mask.
4. Add a limitations paragraph acknowledging the reliance on automatically-transcribed OOD references.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/tpkBiKShwV.md` | 2.67 | Round 1 (weak) | Semi-supervised speech disease detection. Much weaker — narrow scope, noisy labels, less rigorous evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/iYjUG2LcnE.md` | 2.50 | Round 1 (weak) | Speech-to-speech LLM. Much weaker — limited experimental validation |
| `/home/wg25r/review_agent/human_reviews_2026/yt40xuRBA9.md` | 5.00 | Round 1 (mid) | **CTC-DRO** — multilingual ASR with robust optimization. Similar area, accepted poster. USR 2.0 has more novel method, broader evaluation, clearer results |
| `/home/wg25r/review_agent/human_reviews_2026/0fk3GVbJPm.md` | 4.50 | Round 1 (mid) | Syllable-level UASR. Rejected — narrower scope, novelty concerns. USR 2.0 stronger |
| `/home/wg25r/review_agent/human_reviews_2026/DZeic3NpHy.md` | 5.00 | Round 2 (mid) | OmniVinci omni-modal LLM. Accepted poster. USR 2.0 has cleaner evaluation and clearer contributions |
| `/home/wg25r/review_agent/human_reviews_2026/MiV3WXDYJb.md` | 6.00 | Round 2 (mid) | **WAVE** — multimodal embeddings. Accepted Oral. Comparable quality; USR 2.0 has slightly weaker training-time documentation but stronger OOD analysis |
| `/home/wg25r/review_agent/human_reviews_2026/ghwxbTx7do.md` | 6.00 | Round 1 (mid) | Semi-supervised preference optimization. Strong theory-experiment balance. USR 2.0 comparable in rigor |
| `/home/wg25r/review_agent/human_reviews_2026/ghwxbTx7do.md` | 6.00 | Round 2 (mid) | Same paper as above |
| `/home/wg25r/review_agent/human_reviews_2026/qOyF214xmg.md` | 8.00 | Round 1 (strong) | Transducing Language Models. Much stronger — deep theoretical contribution. USR 2.0 not at this level |
| `/home/wg25r/review_agent/human_reviews_2026/oBXfPyi47m.md` | 8.00 | Round 1 (strong) | RL world models. Much stronger — foundational techniques |
| `/home/wg25r/review_agent/human_reviews_2026/BlbLPArfCD.md` | 4.67 | Round 2 (mid) | MoST — speech-text mixture of experts. Rejected. USR 2.0 clearly stronger |
| `/home/wg25r/review_agent/human_reviews_2026/CPtKeEcLsU.md` | 4.67 | Round 2 (mid) | Emotion dataset. Rejected. Not comparable |
| `/home/wg25r/review_agent/human_reviews_2026/nspzrcvzcB.md` | 6.00 | Round 2 (mid) | Audio-visual knowledge distillation. Accepted Poster. Comparable quality |

**Round-1 bracket:** Based on the weak anchors (~2.5–3.2) and strong anchors (8.0+), the paper clearly falls in the middle band. Initial plausible range: 5.0–7.0.

**Round-2 narrowing:** Comparison with the CTC-DRO paper (5.0, accepted poster) shows USR 2.0 is clearly stronger — more novel method, broader evaluation, larger improvements. Comparison with WAVE (6.0, accepted Oral) shows comparable quality: USR 2.0 has stronger OOD analysis but weaker training-time documentation. The paper sits above the typical ~5.0 poster acceptance threshold but below the ~7+ tier of papers with deeper theoretical contributions. I place it at **6.5**.

**Final score and decision:**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>