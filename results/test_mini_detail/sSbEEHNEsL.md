Now let me write the consolidated review.

## Summary

USR 2.0 proposes CTC-driven teacher forcing for fast and robust pseudo-labelling in unified speech recognition (ASR, VSR, AVSR). The core idea is to replace slow autoregressive decoding in the teacher model with greedily-decoded CTC tokens fed into the decoder, enabling parallel attention-based pseudo-label generation. A mixed sampling strategy (alternating between CTC-driven and AR modes at 50% probability) mitigates exposure bias. The method achieves ~2× training speedup, substantially improved OOD robustness (long utterances, noise, cross-dataset), and state-of-the-art in-distribution results on LRS3, LRS2, and WildVSR using a single unified model.

## Strengths

1. **Clear, well-motivated approach to a real bottleneck.** The paper identifies two concrete limitations of USR (slow AR pseudo-labelling and decoupled supervision causing OOD brittleness) and proposes a clean solution. CTC-driven teacher forcing is conceptually simple, directly addresses both problems, and the argument for why global coherence is unnecessary in the pseudo-labelling setting is sound and well-articulated (Section 4.1).

2. **Extensive and convincing OOD evaluation.** Robustness is tested across multiple dimensions: long utterances up to 600 frames (Figure 3), additive babble noise at 4 SNR levels (Table 1), and cross-dataset generalization to LibriSpeech, WildVSR, and AVSpeech (Table 3). The finding that USR 2.0 maintains ~35% WER under greedy decoding on long OOD utterances while USR's WER rises to ~100% (Figure 3a) is a particularly strong result, and the beam-size analysis (Figure 3c) convincingly shows this reflects fundamentally better decoder training, not just inference-side correction.

3. **Strong in-distribution performance with a single model.** USR 2.0 matches or surpasses all prior methods (including separate-task models) across ASR, VSR, and AVSR on LRS3 (Table 2). The Huge model achieves 17.6%/0.9%/0.8% VSR/ASR/AVSR, setting new SOTA. The gains over USR are especially pronounced for VSR and with larger pre-training corpora, supporting the hypothesis that better pseudo-labelling benefits even in-distribution performance.

4. **Well-designed ablations.** Table 4 systematically isolates the contribution of each pseudo-label type in both CTC-driven and AR modes. The result that removing CTC supervision from the decoder degrades OOD from 24.2% to 35.1% while only slightly affecting ID (3.2% to 3.3%) cleanly supports the paper's central claim about CTC-driven robustness. Figure 4 further characterizes the ID/OOD/efficiency trade-off controlled by the AR sampling probability.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Theoretical justification for why CTC-driven teacher forcing works is underspecified.** The paper argues that global coherence is unnecessary because teacher and student are conditioned on the same CTC prefix, and the student learns a stable prefix-to-next-token mapping (Section 4.1). This is plausible and empirically supported by the ablations, but a deeper analysis (e.g., showing that the student's decoder attention patterns converge to sensible alignments under CTC conditioning, or that the CTC-conditioned outputs approximate the conditional distribution of the true sequence) would strengthen confidence in the mechanism. The paper's empirical case is strong enough to carry the claim, but the lack of formal or analytical justification leaves a gap.

2. **Comparisons at comparable scale are missing.** The paper presents USR 2.0 Huge results (17.6/0.9/0.8 on LRS3) but does not provide USR Huge results at the same scale. The authors argue that training USR with AR pseudo-labelling at this scale is computationally prohibitive (which is part of the paper's motivation), but without a same-scale comparison, it is difficult to fully separate the benefit of the proposed method from the benefit of simply using a larger model with more data. The comparison between USR 2.0 Large and USR Large (Table 2) partly addresses this, but the scaling claim would be strengthened by even a partial USR Huge baseline (e.g., trained for fewer epochs or on a data subset).

3. **No statistical significance or confidence intervals.** Many comparisons in Table 2 show differences of 0.1–0.3% WER. The paper does not report variance across runs or confidence intervals. While single-run evaluation is common practice in this benchmark setting, the absence of any uncertainty quantification makes it difficult to assess whether the smaller improvements (e.g., USR 2.0 Large ASR: 1.3% vs. USR Large ASR: 1.2%) are meaningful. Reporting variability would strengthen the paper.

4. **Mixed sampling probability fixed at 0.5 without systematic justification.** Figure 4 shows the ID/OOD trade-off varies with the AR sampling probability, but the paper uses 0.5 for all main experiments without discussing whether this value is optimal across different settings (low-resource vs. high-resource, different model sizes). The adaptive schedule mentioned in Appendix C.2 reportedly performs similarly, but the choice of 0.5 could benefit from further discussion or sensitivity analysis across settings.

### Trivial
- The term "coherence" is used loosely throughout and never formally defined (Section 4.1). A brief characterization of what global structure is lost (e.g., long-range dependencies) and why it does not harm token-wise cross-entropy training would be helpful.

## Nice-to-Haves
- Provide an intermediate analysis of the student decoder's behavior under CTC conditioning (e.g., attention map visualizations, confidence calibration).
- Include a direct comparison of pseudo-label quality (oracle WER of teacher-generated CTC vs. attention pseudo-labels) on OOD data.
- Report training time for ASR and AVSR (Figure 5 currently shows only VSR).

## Removed Points
- **"Huge model dataset sizes not specified"**: The paper states "~2500 hours of unlabelled data" on line 54. This criticism is factually incorrect. Removed.
- **"Missing comparison with USR at Huge scale is a critical/fatal issue"**: Downgraded from the harsh critic's framing as a critical issue to a Minor weakness. The paper's whole premise is that USR cannot practically scale to this size due to AR bottleneck, and a same-scale comparison at Large is provided. The point is valid but not fatal.
- **"Missing related works"**: Removed per meta-reviewer rules (cannot verify existence of missing citations).
- **Formatting/style nitpicks** (e.g., Figure 5 y-axis starting at 24%, notation clarity): Removed as presentation issues not core to evaluation.

## Novel Insights
A genuinely novel observation that emerges from the reviews (beyond what the paper explicitly claims) is that the CTC-driven teacher forcing paradigm may have broader applicability beyond speech recognition. The harsh critic notes that it could generalize to any sequence-to-sequence setting where the input and output share temporal order but lack explicit frame-level alignment (handwriting recognition, music transcription, DNA/protein sequencing). This is a valuable insight that the paper mentions in its conclusion but does not fully develop. Additionally, the finding that OOD robustness degrades sharply only when AR mode exceeds ~80% probability (Figure 4), while remaining flat across most of the range, suggests a potentially general property: a relatively small proportion of CTC-driven training is sufficient to confer robustness, making the efficiency-robustness trade-off surprisingly favorable. This is a nontrivial finding that merits further investigation.

## Suggestions
- Add a brief theoretical or analytical discussion of why the CTC-conditioned decoder outputs, despite lacking global coherence, are effective training targets. Even a simple argument about the conditional distribution converging under the shared prefix would strengthen the paper.
- If feasible, provide USR Huge results at a reduced training budget (e.g., fewer epochs) to enable a direct scaling comparison.
- Report confidence intervals or variance over multiple runs for the key comparisons, especially where differences are small (<0.5% WER).
- Discuss whether the 0.5 mixed sampling probability was tuned or whether it is robust across settings, and provide guidance for practitioners on how to select this hyperparameter.

## Score and Decision

**Round 1 Bracketing (broad search):** Initial calibration placed the paper well above weak anchors (~3.0) and high-anchors (~8.0). The paper clearly sits between 6.0 and 7.5.

**Round 2 Narrowing (detailed anchor comparison):**
- **HAINAN (avg 6.75, Accept Poster)**: Similar contribution type (efficiency-improving method for speech recognition). HAINAN's main weaknesses were incremental novelty over TDT and insufficient evaluation rigor. USR 2.0 has broader and more thorough evaluation (OOD, noise, length, cross-dataset, scaling, ablations) and a clearer methodological contribution. **USR 2.0 is slightly stronger → positions above 6.75.**
- **T2V2 (avg 6.25, Accept Poster)**: Unified ASR+TTS model. Had concerns about incomplete baselines, limited competitive performance. USR 2.0's evaluation is more comprehensive and its results are stronger relative to baselines. **USR 2.0 is clearly stronger → well above 6.25.**
- **mAV-HuBERT (avg 6.2, Reject despite score)**: Found to be incremental over AV-HuBERT with limited novelty. USR 2.0 has a clearer methodological innovation and stronger evaluations. **USR 2.0 is substantially stronger → well above 6.2.**
- **SpeechTokenizer (avg 5.75, Accept Poster)**: Had concerns about training data fairness and incomplete baselines. **USR 2.0 is clearly stronger.**

**Final calibration:** The paper is comfortably above the 6.75 HAINAN anchor given its broader evaluation and cleaner narrative, but below the 8.0-level papers (which have more fundamental theoretical contributions and oral/spotlight designations). The minor weaknesses (thin theoretical justification, missing same-scale comparison, no confidence intervals) are real but do not undermine the core claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>