Now let me run the calibration search to determine the appropriate score.Let me read the most topically relevant anchors from round 1.**Round 1 bracket: 7.0 – 8.5**

USR 2.0 is clearly stronger than the 6.75 anchors (CR-CTC and CAV2vec), which are simpler contributions with narrower evaluation. Now narrowing within [7, 8.5]:Let me read the Zipformer paper (closest topical match at 7.5) in full to calibrate.I now have enough information to write the final review. Let me compile the analysis.

---

## Summary

USR 2.0 proposes CTC-driven teacher forcing, replacing the costly autoregressive attention pseudo-labelling in the Unified Speech Recognition (USR) framework with a single parallel forward pass: the teacher's greedily-decoded CTC outputs are fed as forced inputs to the decoder to produce attention pseudo-labels. A mixed sampling strategy (50% AR / 50% CTC-driven) mitigates the resulting train–test mismatch. Together these yield ~2× training speedup, dramatically improved out-of-distribution robustness (long utterances, noise, cross-dataset), and state-of-the-art results on LRS3 across ASR, VSR, and AVSR with a single unified model.

---

## Strengths

- **~2× training efficiency demonstrated across all model scales.** Figure 5 shows USR 2.0 reaches a given VSR WER in roughly half the wall-clock time of USR for Base (LRS3), Base (LRS3+Vox2), and Large (LRS3+Vox2) configurations. This is further driven by fewer required epochs (50 vs. 75 per Appendix C.5). The speedup is concrete and consistently validated.

- **Large and consistent OOD robustness gains across diverse conditions.** Figure 3a shows USR 2.0 maintaining near-flat WER up to 600 frames while USR degrades to ~100% WER; Figure 3b confirms USR 2.0 retains an edge even with beam search (size 30). Table 1 shows USR 2.0 dominating at moderate noise SNRs (10, 5, 0 dB). Table 3 shows large cross-dataset gains: LibriSpeech WER drops from 25.3% (USR) to 15.4%, WildVSR from 80.0% to 73.7%, AVSpeech from 34.7% to 25.0%—all under greedy decoding without seeing these datasets during training.

- **Competitive or superior in-distribution performance, with new SOTA at scale.** Table 2 shows USR 2.0 matching or surpassing USR across all settings, including larger gains with VoxCeleb2 pretraining (VSR: 26.5% → 24.8% for Base+, 26.9% → 23.7% for Large). The scaled Huge model (LRS2+LRS3 labelled, VoxCeleb2+AVSpeech unlabelled) achieves 17.6%/0.9%/0.8% WER on LRS3 across VSR/ASR/AVSR—a single unified model.

- **Tight ablations confirm the specific design choices.** Table 4 isolates the value of each PL type per branch: removing CTC supervision from the decoder degrades OOD AVSR WER from 24.2% to 35.1% (CTC-driven mode); removing attention-based targets raises ID WER from 3.2% to 3.6%. Figure 4 cleanly characterizes the ID/OOD/efficiency trade-off as a function of AR sampling probability, showing sharp OOD degradation only above ~0.6 AR probability, justifying the 0.5 default.

- **Honest evaluation of beam-size trade-offs.** Figure 3c shows explicitly that large beam sizes can compensate for USR's weaker decoder—but at significant memory cost—adding credibility to the paper's efficiency and robustness claims.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theoretical argument for CTC-driven teacher forcing is stronger for incoherence than for CTC incorrectness under OOD.** Section 4.1 argues that "global incoherence does not hinder learning" because teacher and student share the same CTC-derived prefix, making the knowledge transfer stable. This is compelling when the CTC prefix is accurate. However, the OOD scenario motivating the method is precisely where CTC itself may produce systematic recognition errors. A misconditioned prefix propagates position-wise errors into attention PLs in ways that the "matched conditioning" argument does not fully address. The paper partially mitigates this via mixed sampling (Section 4.2, 50% AR mode) and the empirical evidence supports the method overall (Table 4, Figure 4), but the theoretical account in Section 4.1 does not distinguish between incoherence (benign CTC artifacts from collapse/blanks) and incorrectness (CTC recognition errors under domain shift). Strengthening this argument—e.g., by showing that the token-wise cross-entropy gradient is insensitive to prefix-level errors so long as the conditioning is matched—would make the paper's core claim more airtight.

- **Evaluation protocol inconsistency across OOD conditions.** Table 2 (ID, LRS3) uses beam size 40 with joint CTC-attention decoding; Table 3 (cross-dataset OOD) uses greedy decoding; Table 1 (noise) uses beam size 30. The paper's rationale—greedy better reflects PL generation conditions—is reasonable for Table 3, and Figure 3 already shows both greedy and beam-search results for long utterances. However, Tables 1 and 3 each show only one decoding mode, making it unclear whether the robustness gains persist fully under beam search for noise and cross-dataset conditions. Reporting both modes for Table 3 (and optionally Table 1) would complete the story that Figure 3 begins.

- **Whisper oracle limitation not acknowledged.** Section 5.1 and Table 3 evaluate on ~2,000 VoxCeleb2 samples and 1,000 AVSpeech samples using Whisper transcriptions as references. Whisper has a known length-dependent error profile; its WER increases for longer or noisier inputs, introducing length-correlated noise into the WER axis of Figure 3. Since both USR and USR 2.0 are compared against the same references, systematic bias partially cancels and the qualitative findings are likely sound. However, for Figure 3—the paper's centerpiece robustness demonstration—a brief acknowledgment of Whisper's own error variance across length buckets would strengthen confidence in the absolute magnitudes reported.

### Trivial

- The gray highlighting in Table 4 marking "default" settings is applied inconsistently across rows, creating minor confusion about which rows correspond to the actual USR 2.0 defaults.

---

## Nice-to-Haves

- Extend Figure 3's dual greedy/beam reporting to Tables 1 and 3, to show whether the robustness gains persist under beam search for noise and cross-dataset conditions. The infrastructure is already in place (Section 5.1 does this for long utterances).

- A qualitative analysis of CTC-driven vs. AR pseudo-labels: concrete examples of where the two PLs agree or diverge, and what the student predicts in each case, would make Section 4.1's "matched conditioning" argument far more persuasive than the current algebraic presentation alone.

- Consider adding a brief argument (1–2 sentences) in Section 4.1 specifically addressing the OOD case where CTC itself makes errors, distinguishing it from the incoherence case. This would close the gap between the theoretical account and the empirical scope of the paper.

---

## Removed Points

*These points are flagged to be removed. Treat them with caution.*

- **Missing standard deviations for WER results (Tables 1–3):** Removed as a reproducibility nitpick. Single-run evaluation is standard in speech recognition at this scale. The consistent direction of gains across multiple conditions sufficiently supports reliability.

- **Conclusion's speculation about handwriting/music/DNA sequencing:** The harsh reviewer flagged this as "harmless puffery." This is a style nitpick; the paper's speculation is clearly scoped as a future direction and does not affect the core contribution.

- **CTC-driven mode lacks global coherence is a concern:** The strength finder raised "global coherence" as a concern, but the paper directly addresses it in Section 4.1. The "Global coherence" paragraph in Section 4.1 explicitly explains why coherence is unnecessary in the pseudo-labelling setting: "teacher and student are conditioned on the same CTC-derived sequence… The student is trained to predict the teacher decoder's most likely next token under this shared input." This is a genuine insight, not a weakness.

- **Missing appendix discussion:** The harsh critic noted that the global incoherence discussion is deferred to Appendix C.4. Per policy, missing appendix content is not a valid criticism; the appendix exists in the original submission.

---

## Novel Insights

The core novel insight of USR 2.0—that CTC outputs can serve as a structured proxy for ground truth in teacher forcing during pseudo-labelling, enabling parallel attention PL generation without sacrificing effectiveness—is genuinely elegant. The key observation is that in self-training, coherence of the teacher's generated sequence is unnecessary; what matters is matched conditioning between teacher and student at each position. This recasts teacher forcing not as an approximation to ground truth (its standard interpretation) but as a coordination mechanism between branches, enabling CTC's robustness properties to propagate into the attention decoder through joint supervision. The result that this coupling—formalized in Equation (5) where the decoder predicts both CTC and attention targets simultaneously—primarily improves OOD performance rather than ID performance (Figure 4, Table 4) is a practically important finding: the trade-off curve is remarkably flat across a wide range of AR sampling probabilities, breaking only sharply near AR-only training.

---

## Suggestions

1. **Unify evaluation protocols for OOD.** Extend Figure 3's greedy+beam dual-reporting to Table 3 (cross-dataset) and Table 1 (noise). This would close the evaluation gap and complete the story.

2. **Tighten the theoretical argument for CTC incorrectness.** Add 1–2 sentences in Section 4.1 distinguishing the incoherence case (CTC artifacts from collapse/blanks) from the incorrectness case (CTC errors under OOD), and explain why the matched-conditioning argument still holds even when CTC makes errors.

3. **Acknowledge Whisper oracle limitations briefly.** One sentence noting that Whisper's own WER varies with input length, and that the relative (not absolute) comparison is therefore the more reliable finding, would strengthen Figure 3's credibility.

4. **Expand mixed-sampling ablation to noise conditions.** Currently Figure 4 shows the AR-probability sweep only on AVSpeech. Repeating on noise-corrupted inputs (from Table 1's setup) would show whether the optimal mixing ratio is robust across OOD types.

---

## Score Calibration

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| CIs9x2ZRgh (CR-CTC) | 6.75 | R1 | USR 2.0 is clearly stronger: more comprehensive evaluation, dual efficiency+robustness contribution, SOTA across 3 tasks |
| WEQL5ksDnB (CAV2vec) | 6.75 | R1 | USR 2.0 is stronger: narrower scope in CAV2vec, weaker ablations, single-task focus |
| M8J0b9gNfG (Multilingual VSR) | 6.20 | R1 | USR 2.0 is clearly stronger: more original contribution, better validation |
| 4lOWCkhr4g (Cross-lingual PL) | 5.25 | R1 | USR 2.0 is clearly stronger |
| 9WD9KwssyT (Zipformer) | 7.50 | R2 | USR 2.0 is comparable: both are strong efficiency+performance contributions to speech recognition. Zipformer introduces many ideas with thin ablations; USR 2.0 has a cleaner insight, broader evaluation (3 OOD axes), and unified model. Roughly comparable quality. |
| Bo6GpQ3B9a (OOD semi-supervised) | 7.00 | R2 | USR 2.0 is stronger: more empirically comprehensive |
| pdf6MbXnAS (Self-Training ICL) | 7.00 | R2 | USR 2.0 is stronger: clearer contribution, better ablations |
| uZ5K4HeNwd (Beyond Auto-Regression) | 7.00 | R2 | USR 2.0 is comparable or slightly better: similar efficiency theme, USR 2.0 has stronger empirical validation in a well-defined domain |
| PdaPky8MUn (Never Train from Scratch) | 8.00 | R2 | USR 2.0 is slightly weaker: "Never Train from Scratch" has a very clean, impactful finding with unanimous reviewer agreement; USR 2.0 has minor bounded weaknesses |

**Round 1 bracket:** 7.0 – 8.5

**Round 2 narrowing:** USR 2.0 is clearly above the 6.75–7.00 anchors. Comparable to Zipformer (7.50), which has similar strengths (strong empirical contribution, ASR domain) but also thinner ablations and more scattered novelty. USR 2.0's minor weaknesses (evaluation protocol inconsistency, theoretical gap in Section 4.1, Whisper oracle) are bounded and do not threaten the core claims. The paper sits solidly at or slightly above 7.5, but not at 8.0 given the modest theoretical and evaluation gaps. 

**Final score: 7.5**

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>