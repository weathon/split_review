Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

USR 2.0 addresses two limitations of the USR semi-supervised speech recognition framework: slow autoregressive pseudo-labelling and brittleness under distribution shift. The key idea is CTC-driven teacher forcing, where the teacher's greedily decoded CTC outputs are fed into the attention decoder to generate pseudo-labels in a single forward pass, combined with mixed sampling to mitigate exposure bias. The result is roughly 2× faster training, substantially improved out-of-distribution robustness (e.g., LibriSpeech WER drops from 25.3% to 15.4%), and state-of-the-art in-distribution results on LRS3, LRS2, and WildVSR with a single unified model for ASR, VSR, and AVSR.

## Strengths

- **CTC-driven teacher forcing elegantly eliminates the AR bottleneck while transferring robustness.** Feeding collapsed CTC outputs into the decoder generates attention pseudo-labels in a single forward pass (~40× faster than greedy AR decoding, Figure 1), and the matched conditioning between teacher and student (Section 4.1) ensures effective knowledge transfer despite globally incoherent outputs. This is a genuinely clever insight: coherence is unnecessary in the pseudo-labelling setting when both sides share the same conditioning.

- **Joint CTC–attention pseudo-label prediction couples the two branches for robustness.** Ablations (Table 4) demonstrate that supervising the decoder with both CTC and attention targets is critical: dropping CTC targets raises OOD WER from 24.2% to 35.1%, while dropping attention targets degrades in-distribution (3.2% → 3.6%). The decoder inherits CTC's alignment stability without sacrificing attention's expressiveness.

- **Large, consistent OOD improvements across diverse axes.** Table 3 shows major gains over USR under greedy decoding on three OOD datasets (LibriSpeech: 25.3% → 15.4%, WildVSR: 80.0% → 73.7%, AVSpeech: 34.7% → 25.0%). Robustness is further demonstrated on long utterances (Figure 3a), additive noise at multiple SNRs (Table 1), and cross-dataset shifts, building a compelling body of evidence.

- **Mixed sampling effectively balances ID accuracy, OOD robustness, and training cost.** Figure 4 shows that the 0.5 sampling probability for AR mode occupies a strong operating point: ID WER remains near-optimal, OOD WER is preserved, and training time stays near the minimum. The sweep provides clear practical guidance.

- **Comprehensive scaling and efficiency evidence.** Figure 5 convincingly demonstrates ~2× faster wall-clock convergence across model sizes and pre-training configurations. Scaling to a Huge model with ~2500h of unlabelled data yields 17.6% VSR, 0.9% ASR, and 0.8% AVSR on LRS3 (Table 2), showing the method scales gracefully.

- **Practical simplicity.** The method modifies only pseudo-label generation and loss computation (Section 4.3), reusing the identical transformer encoder–decoder architecture. This low implementation overhead makes adoption straightforward.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No variance estimates for WER results.** All reported numbers are single-run results. Some in-distribution gains over USR are small — e.g., on LRS3 Base, VSR improves from 36.0% to 36.2%, AVSR from 3.0% to 2.9%. Without confidence intervals or multiple seeds, it is unclear whether these differences are statistically meaningful. This is common practice in large-scale speech recognition, but the paper would be stronger with even a brief acknowledgment of this limitation and ideally standard deviations for the main results.

- **Reliance on automatically transcribed evaluation data for some OOD benchmarks.** VoxCeleb2 (Section 5.1) and AVSpeech (Section 5.3) use Whisper transcriptions as ground truth. The paper is transparent about this — it explicitly states Whisper is treated as an "oracle" — and it also evaluates on real OOD datasets with ground truth (LibriSpeech, WildVSR). However, the paper does not discuss the reliability of these automatic transcriptions or how Whisper's error patterns might interact with different decoders. Adding a brief discussion of this caveat would strengthen the evaluation.

- **Forward-looking claims in the conclusion lack supporting evidence.** The conclusion states that these insights "can be applied to other speech recognition tasks, including audio-only, streaming, and multilingual ASR" and even "other sequence-to-sequence settings such as handwriting recognition, music transcription, or DNA/protein sequencing." While these are reasonable directions, no evidence is provided. More modest phrasing or a small pilot experiment would be appropriate.

### Trivial
None.

## Nice-to-Haves

- A computational cost breakdown (FLOPs or GPU-hours per pseudo-labelling step) comparing USR and USR 2.0 would help quantify the source of efficiency gains beyond the wall-clock time plot.
- Varying the mixed sampling probability jointly with the confidence threshold could reveal whether an even faster or more robust configuration exists.
- Characterizing failure cases where CTC outputs are poor (e.g., very noisy audio) and studying whether the decoder's attention pseudo-labels degrade in those regimes would delineate the method's robustness boundary more clearly.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Incremental conceptual contribution" as a fatal/major weakness** — The harsh critic frames the method as a "straightforward engineering extension." While USR 2.0 does build directly on USR, the CTC-driven teacher forcing insight (that globally incoherent decoder outputs are acceptable in a pseudo-labelling setting with matched conditioning) is genuinely non-obvious. The empirical payoff is substantial. I treat this as a matter of scope and significance, not a verifiable flaw; the paper's contributions are well-motivated and well-supported. The incremental nature is already reflected in the score relative to more fundamental contributions like Zipformer.

- **"-5 dB SNR advantage fading"** — The harsh critic notes USR 2.0's advantage fading at -5 dB for ASR. The paper already discusses this (Section 5.2): "its performance is comparable to AV-HuBERT." At -5 dB ASR, USR 2.0 achieves 94.4% vs USR's 104.4% — still a 10% absolute improvement. The paper acknowledges the convergence with AV-HuBERT at this extreme. This is not a hidden weakness.

- **"50 vs 75 epochs — would USR reach similar WER with more epochs?"** — The paper references Appendix C.5 for this comparison. The appendix is stripped in the provided file. Since the paper explicitly addresses this, it is not a valid criticism.

- **"Comparison with NAT pseudo-labelling baseline" and "Computational cost breakdown"** — These are scope-expanding requests, not weaknesses in evaluating what the paper claims to do. Moved to Nice-to-Haves.

- **"Multi-lingual or streaming extension"** — The conclusion's forward-looking claims are addressed as a Minor weakness above. The demand for pilot experiments is scope creep; the concern is about overclaiming, not missing experiments.

## Novel Insights

The key novel insight from the reviews is that the matched-conditioning property of CTC-driven teacher forcing — where both teacher and student see the same (potentially globally incoherent) decoder inputs — is what makes this approach viable. This is a specific, non-obvious observation that distinguishes this work from generic "use CTC to speed things up" approaches. The paper argues this well, and the ablation in Table 4 (showing the OOD gap between CTC-driven and AR modes) provides strong empirical backing. This insight could transfer to other sequence-to-sequence self-training settings beyond speech.

## Suggestions

- Report multi-seed confidence intervals or at minimum acknowledge the single-run limitation for the headline in-distribution results, particularly where gains are small (e.g., LRS3 Base VSR: 36.0% → 36.2%).
- Add a brief paragraph in Section 5 discussing the reliability caveats of Whisper-based automatic transcriptions as evaluation ground truth, even if the relative improvements are robust.
- Temper the conclusion's forward-looking claims about applicability to streaming, multilingual, and non-speech domains unless small pilot experiments can be included.

## Score and Decision

**Calibration anchors:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| CR-CTC (CIs9x2ZRgh) | 6.75 | R1 | USR 2.0 has more comprehensive experiments, larger gains, and a more interesting methodological insight. Clearly stronger. |
| HAI-T (LrmPGtnros) | 6.75 | R2 | Both are incremental but well-executed improvements. USR 2.0 has broader evaluation (OOD axes, scaling) and more dramatic practical gains. Stronger. |
| AWP (fUGhVYPVRM) | 7.00 | R1/R2 | Comparable in contribution quality — both have clever ideas with good execution. USR 2.0's empirical gains are more substantial and consistent. Slightly stronger. |
| Zipformer (9WD9KwssyT) | 7.50 | R2 | A fundamental architectural contribution. USR 2.0's contribution is more incremental. Zipformer is stronger. |

**Round 1 bracket:** 6.0–8.0 (based on CR-CTC at 6.75 and Zipformer at 7.50, with AWP at 7.00 as a close comparator).

**Round 2 narrowing:** USR 2.0 sits between AWP (7.00) and Zipformer (7.50). It is clearly stronger than HAI-T and CR-CTC (both 6.75), comparable to or slightly better than AWP (7.00), but does not reach the fundamental contribution level of Zipformer (7.50). Score: **7.0**.

The paper is well-executed with thorough experiments, genuine practical gains (2× faster training, large OOD improvements), and a clever methodological insight. The minor weaknesses (single-run results, automatic transcription caveats, forward-looking claims) are addressable and do not undermine the core contributions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>