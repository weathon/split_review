Now I have all the calibration information I need. Let me produce the final consolidated review.

## Summary

USR 2.0 proposes **CTC-driven teacher forcing** for pseudo-labelling in a unified ASR/VSR/AVSR student–teacher framework. The core idea is to replace slow autoregressive decoding of the teacher with greedily-decoded CTC outputs fed directly into the attention decoder, generating attention pseudo-labels in a single parallel pass. A mixed sampling strategy (50/50 CTC-driven vs. AR mode) mitigates exposure bias. The method nearly doubles training speed, substantially improves out-of-distribution robustness (long utterances, noise, cross-dataset), and achieves state-of-the-art in-distribution results across all three tasks with a single unified model.

## Strengths

1. **Novel conceptual insight that global sequence coherence is unnecessary during pseudo-labelling.** Section 4.1 argues that CTC-driven teacher forcing can produce globally incoherent sequences, yet in a pseudo-labelling setting where teacher and student share the same CTC-derived prefix, token-wise cross-entropy remains effective. This insight justifies replacing costly autoregression with a parallel alternative and cleanly distinguishes the proposed method from standard teacher-forcing approaches.

2. **~2× training speedup, convincingly demonstrated.** Figure 5 shows USR 2.0 reaching lower VSR WER in roughly half the wall-clock training time across multiple model scales and pre-training settings. The paper transparently attributes this to both faster per-step decoding (CTC-driven mode avoids autoregression) and faster convergence (50 epochs vs. 75).

3. **Large and consistent out-of-distribution robustness gains.** Table 3 reports greedy-decoding WER drops from 25.3%→15.4% (LibriSpeech), 80.0%→73.7% (WildVSR), and 34.7%→25.0% (AVSpeech) over USR. Figure 3a shows USR 2.0 maintaining stable ~35% WER on long VoxCeleb2 utterances (400+ frames) where USR degrades past 70%. These are large-margin improvements unlikely to be erased by run-to-run variance.

4. **State-of-the-art in-distribution performance with a single unified model.** Table 2 shows USR 2.0 achieves 17.6% (VSR), 0.9% (ASR), 0.8% (AVSR) on LRS3 at Huge scale, surpassing modality-specific self-supervised baselines. Consistent improvements over USR are shown across low- and high-resource settings (e.g., Base+ VSR: 26.4% vs. 28.4%).

5. **Well-designed ablations that isolate the contribution of each design choice.** Table 4 cleanly shows that both CTC and attention targets are essential in CTC-driven mode: removing CTC targets from the decoder raises OOD WER from 24.2% to 35.1%. Figure 4 characterizes the ID/OOD/efficiency tradeoff controlled by the mixed sampling probability.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims (faster training, improved OOD robustness, SOTA results) are well-supported by the evidence presented.

### Minor

1. **No statistical significance or variance reporting.** All WER numbers are single point estimates. While the large-margin OOD gains (~10–40% relative) and 2× speedup are unlikely to be noise, several in-distribution comparisons involve small differences (e.g., 0.1–0.3% WER on LRS3). The one regression (Base, LRS3 VSR: USR 2.0 at 36.2% vs. USR at 36.0%) also falls in this small-delta regime. Reporting results over multiple seeds (≥3) for the main ID comparisons would resolve whether these small differences are meaningful.

2. **OOD AVSpeech evaluation is undersized and uses a noisy oracle.** The 1,000-sample AVSpeech test set (Table 3) transcribed by Whisper is pragmatic given the lack of clean AVSR test sets for AVSpeech, but manual filtering introduces selection bias and Whisper-based "ground truth" is itself noisy. This weakens one leg of the OOD evidence slightly, though the long-utterance (Figures 3a–b) and noise (Table 1) experiments provide strong complementary evidence that does not depend on these labels.

### Trivial
- The paper does not decompose the training speedup into per-step acceleration versus reduced epochs via a controlled ablation that holds gradient steps constant. While both factors are acknowledged, a controlled experiment isolating the mechanism would strengthen the claim about better training dynamics.

## Nice-to-Haves
- An analysis of pseudo-label quality (e.g., comparing WER of PLs from USR vs. USR 2.0 on unlabelled data) would directly test whether CTC-driven PLs are genuinely more robust.
- Error analysis on the OOD AVSpeech data to verify Whisper label reliability (e.g., agreement with human transcription on a subset).
- Ablation fixing the number of gradient steps to separate per-step speed from faster convergence.
- Reporting inference-time WER for student vs. teacher (EMA) to clarify whether improvements come from both or are driven by one.

## Removed Points
- **"Figure 1 shows Attention (Teacher Forcing) speed as 0.050s, ~3.8× slower than CTC, not mentioned in text"** — The text claims "CTC is ~40× faster than *autoregressive* decoding" (comparing CTC 0.013s to AR 0.471s), not teacher forcing. This is factually correct; the teacher forcing number is additional context, not a claim. *Removed as factually incorrect criticism.*
- **Missing related work** — Removed per policy: I cannot verify which related works exist and were missed.
- **Reproducibility concerns (undisclosed hyperparameters, missing appendix content)** — Removed per policy: the parser strips appendix content; hyperparameters are detailed in Appendix A reference.
- **Formatting/style nitpicks** — Removed per policy.
- **Strength Finder strengths about problem importance or generic praise** — Removed; only concrete, evidence-backed strengths retained.

## Novel Insights
Beyond the paper's own contributions, the most interesting novel insight that emerges from the reviews is the observation that the **primary benefit of CTC-driven mode is OOD robustness**, with ID performance largely determined by the AR mode. Figure 4 reveals that ID WER is nearly flat (varying only 0.4%) across the entire range of AR sampling probability, while OOD WER degrades sharply above 0.6 AR probability. This suggests that decoupling the two sources of performance — ID quality from AR mode, OOD robustness from CTC-driven mode — is a design principle that could generalize beyond this specific paper: for pseudo-labelling under distribution shift, a hybrid approach that mixes a robust (but less expressive) PL generator with an expressive (but brittle) one can get the best of both worlds, as long as the robust mode dominates for OOD coverage.

## Suggestions
- Add multiple-seed experiments (≥3) for the main in-distribution comparisons against USR to establish statistical reliability of small-margin gains.
- Expand the OOD AVSpeech evaluation (≥ 5,000 samples) or supplement with additional OOD benchmarks (e.g., MuAViC, held-out VoxCeleb2 with human transcription).
- Include a controlled ablation that matches gradient steps between USR and USR 2.0 to separate per-step speed from faster convergence in attributing the 2× speedup.

## Score and Decision

Now I need to determine the final score via calibration.

**Round 1 bracket**: Based on the three queries, the paper sits between the weak band (avg ≤ 3.5, not relevant here) and the strong band (avg ≥ 7.5, scores from topics not directly comparable). The most comparable anchors are from the middle band: CR-CTC (6.75), T2V2 (6.25), CAV2vec (6.75). My round-1 bracket is **[6.5, 8.5]**.

**Round 2 narrowing**: I queried for 6.5–8.5 in speech recognition with CTC/attention/student-teacher frameworks, finding AWP (7.00), CR-CTC (6.75), CAV2vec (6.75), Three-in-One (6.75). Reading AWP (7.00) closely:

- **vs. AWP (7.00)**: AWP is a clever plug-and-play CTC alignment re-weighting framework, but its primary WER improvements are modest (0.1–0.2% WER). USR 2.0 has a broader impact: it covers three tasks (ASR, VSR, AVSR), achieves SOTA at scale, demonstrates large-margin OOD gains (10–40% relative), and delivers a practical 2× training speedup. The core idea (CTC-driven teacher forcing) is also more novel than the alignment-reweighting approach. USR 2.0 is **stronger** than AWP.
- **vs. CAV2vec (6.75)**: CAV2vec focuses on AVSR robustness via corruption-aware SSL. USR 2.0 has a more novel core idea and broader evaluation scope. **Stronger**.
- **vs. CR-CTC (6.75)**: CR-CTC applies consistency regularization to CTC. USR 2.0's contribution is both more novel and more thoroughly validated. **Stronger**.

The three anchors closest to this paper in quality all sit near 6.75–7.00, and this paper is clearly stronger than all of them. It is not, however, at the level of the 8.0+ anchors (which are about different topics — talking body generation, portrait avatars) so I cannot benchmark against those directly.

**Final score: 7.5**. This reflects a paper with a genuinely novel idea, thorough empirical validation across multiple tasks and settings, practical efficiency gains, and SOTA results — held back from a higher score only by minor evidential gaps (no error bars, small OOD test set). It sits comfortably above the 6.75–7.00 band of comparable papers in the same subfield.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>