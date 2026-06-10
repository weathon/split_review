## Summary
This paper proposes USR 2.0, an improved Unified Speech Recognition framework for semi-supervised training of a single model across ASR, VSR, and AVSR. The core contribution is CTC-driven teacher forcing—greedily decoded CTC outputs replace slow autoregressive decoding to generate attention pseudo-labels in a single forward pass—combined with mixed sampling to mitigate exposure bias. The method achieves ~2× training speedup, substantially improved OOD robustness, and state-of-the-art or matching in-distribution results.

## Strengths
- **Well-articulated technical insight**: Section 4.1 (lines 108–110) argues compellingly that globally incoherent CTC-driven pseudo-labels are effective because teacher and student share the same CTC-derived conditioning, so "the student decoder learns a stable mapping from a coherent CTC prefix to the teacher's conditionally valid next-token prediction." This cleanly separates pseudo-labelling requirements (local validity) from inference requirements (global coherence).
- **Substantial computational efficiency gains**: Figure 1 (right) shows CTC decoding at 0.013s vs. AR at 0.471s (~36× faster); Figure 5 demonstrates ~2× faster wall-clock training convergence across multiple model scales; convergence requires fewer epochs (50 vs. 75).
- **Comprehensive OOD robustness evaluation across three distinct distribution shifts**: Long sequences (Figure 3 — USR 2.0 stable at 600 frames where USR WER reaches ~100%), additive noise at multiple SNR levels (Table 1), and unseen datasets (Table 3 — USR 2.0 outperforms USR by 9.9pp on LibriSpeech, 6.3pp on WildVSR, 9.7pp on AVSpeech under greedy decoding).
- **Systematic ablation isolating component contributions**: Table 4 ablates PL types for each branch under both modes, showing CTC supervision in the decoder is critical for OOD performance (35.1% vs 24.2%) and attention-based targets matter for ID performance. Figure 4 quantifies the effect of mixed sampling probability. The observation that ID and OOD trends are "largely uncorrelated" is interesting and well-supported.
- **Robustness to beam size**: Figure 3c shows USR 2.0 maintains strong performance under greedy decoding while USR degrades significantly, only approaching USR 2.0's performance with very large beams at high computational cost—doubly useful for pseudo-labelling and low-latency inference.

## Weaknesses

### Fatal
None

### Major
- **In-distribution gains over USR are marginal for ASR and AVSR, with no variance estimates**: In Table 2, Base/LRS3 low-resource setting: VSR 36.2 vs 36.0 (+0.2), ASR 3.0 vs 3.2 (−0.2), AVSR 2.9 vs 3.0 (−0.1). These differences are within typical experimental variance, and no error bars or significance tests are reported anywhere. The gains become more pronounced for VSR at scale (e.g., Large/LRS3+Vox2: 23.7 vs 26.9), but the abstract frames results as achieving "state-of-the-art results" broadly when the in-distribution ASR/AVSR improvements are marginal and possibly within noise. The authors should either temper in-distribution claims for ASR/AVSR or provide variance estimates to support them.

### Minor
- **Whisper-generated references for some OOD evaluations**: The long-utterance evaluation (Section 5.1) uses Whisper as an oracle for VoxCeleb2, and the AVSpeech OOD evaluation (Section 5.3) uses Whisper transcriptions as ground truth. While transparently stated and common practice, absolute WER numbers on these sets are relative to Whisper's quality. Since all compared methods share the same reference, relative rankings hold. LibriSpeech and WildVSR should have human ground truth, providing cross-validation.

### Trivial
None

## Nice-to-Haves
- Provide pseudo-label quality analysis comparing CTC-driven vs AR pseudo-labels on OOD data to directly validate the training-time robustness claim (not just inference-time).
- Analyze how the confidence threshold of 0.8 interacts with CTC-driven vs AR modes, since their confidence profiles differ.
- Add variance estimates for key in-distribution results (even a single additional run for Base/LRS3 would help).
- Provide qualitative analysis of failure modes—e.g., acoustic conditions where CTC's conditional independence assumption produces poor prefixes.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"No comparison with other efficient pseudo-labelling approaches"** — scope creep; the paper improves the USR framework specifically, not all possible pseudo-labelling methods.
- **Criticism of the 0.5 probability choice** — the paper explicitly addresses this in a footnote (Appendix C.2 reference) and Figure 4 shows the choice is robust across 0.2–0.8.

## Novel Insights
The paper's core insight—that pseudo-label global coherence is unnecessary in self-training because teacher and student share CTC-derived conditioning—is genuinely novel and well-argued. The observation from Table 4 that ID and OOD trends are largely uncorrelated, with CTC supervision critical for OOD and attention targets important for ID, provides a useful decomposition of what each component contributes. The finding that robustness improvements translate to in-distribution gains because unlabelled data often comes from OOD sources is a practical insight that strengthens the motivation beyond just deployment robustness.

## Suggestions
- Add variance estimates or significance tests for the in-distribution Base/LRS3 results to support the modest ASR/AVSR gains.
- Consider adding a pseudo-label quality comparison on OOD data as direct validation of the training-time mechanism.
- Moderate the "state-of-the-art" framing for in-distribution ASR/AVSR to focus claims on VSR, OOD robustness, and efficiency where gains are clear and substantial.

## Calibration Report

**All retrieved anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| gW4bdLwypB (Objective Soups) | 3.40 | 1 | Weaker: multilingual ASR with MOO conflicts, less clear contribution |
| xRi8sKo4XI (Unsupervised Prompt Learning) | 3.00 | 1 | Weaker: different domain (LLM), limited novelty |
| UFwefiypla (DM-Codec) | 3.00 | 1 | Weaker: speech tokenization, rejected |
| aXSxSu3fvg (Semi-Supervised Early Stopping) | 3.00 | 1 | Weaker: heuristic framework, limited contribution |
| 4lOWCkhr4g (Unsupervised ASR Cross-Lingual PL) | 5.25 | 1+2 | Weaker: limited novelty, narrower scope, rejected |
| CIs9x2ZRgh (CR-CTC) | 6.75 | 1+2 | Weaker: simpler contribution (consistency regularization on CTC only), narrower evaluation |
| fUGhVYPVRM (Align With Purpose) | 7.00 | 1+2 | Comparable: CTC framework with broader applicability but weaker empirical validation and more reviewer concerns |
| 7NlGsjrEd8 (Alignment Modeling for ASR) | 4.50 | 1 | Weaker: limited scope, rejected |
| 9Cu8MRmhq2 (Multi-granularity Correspondence) | 8.00 | 1 | Stronger: but different domain (video-language) |
| weM4YBicIP (Loopy) | 8.00 | 1 | Stronger: different domain (avatar generation) |
| TPZRq4FALB (Test-time Adaptation) | 8.00 | 1 | Stronger: different domain (multimodal TTA) |
| HnhNRrLPwm (MMIE) | 8.00 | 1 | Stronger: different domain (LVLM benchmark) |
| dnqPvUjyRI (SemiReward) | 6.00 | 2 | Weaker: general SSL framework, less speech-specific impact |
| CY9f6G89Rv (TSBO) | 5.33 | 2 | Weaker: Bayesian optimization, different domain |
| 4N97bz1sP6 (Bi-modal Audio Separation) | 6.67 | 2 | Weaker: audio separation, different scope |
| LrmPGtnros (HAI-T) | 6.75 | 2 | Weaker: hybrid transducer, narrower evaluation |
| TtKN1TpvUu (T2V2) | 6.25 | 2 | Weaker: unified ASR+TTS but less comprehensive |
| M8J0b9gNfG (Multilingual VSR) | 6.20 | 2 | Weaker: rejected, narrower scope |
| wD8L86iCvD (FAVOR) | 5.25 | 2 | Weaker: audio-visual LLM representation, rejected |
| WEQL5ksDnB (CAV2vec) | 6.75 | 2 | Weaker: AVSR corruption robustness, narrower scope |

**Round-1 bracket**: 6.0 – 7.5. Weak anchors (<3.5) are unrelated domains; strong anchors (>7.5) are also unrelated domains (video-language, avatar generation). Topically relevant papers cluster in the 5.25–7.0 range.

**Round-2 narrowing**: Anchors at 6.75 (CR-CTC, HAI-T, CAV2vec) are clearly weaker—simpler contributions, narrower evaluations, less practical impact. Align With Purpose (7.0) is the closest comparable but has weaker empirical validation and more unresolved reviewer concerns. USR 2.0 has broader scope (three unified tasks), more comprehensive OOD evaluation, and cleaner practical impact.

**Final score**: 7.0 — positioned above the 6.75 anchors due to broader scope, stronger evaluation, and clearer practical impact; comparable to Align With Purpose (7.0) but with better empirical support; held back from 7.5+ by marginal in-distribution ASR/AVSR gains without variance estimates.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>