Now let me write the consolidated review.

## Summary

DiSTAR is a zero-shot text-to-speech framework that operates entirely in the discrete RVQ code space, coupling an autoregressive language model (which drafts the next patch of codes) with a masked diffusion transformer (which fills in the patch in parallel). The method adopts the patch-wise factorization from DiTAR but replaces continuous next-patch diffusion with discrete masked diffusion (inspired by LLaDA), thereby modeling the intra-frame multi-codebook dependencies typical of RVQ representations. Experiments on LibriSpeech-PC and SeedTTS test-en show strong WER (1.66 on LibriSpeech, lowest among compared systems), competitive speaker similarity, and state-of-the-art subjective scores (SMOS 3.31, CMOS 0.22 on SeedTTS).

## Strengths

1. **Clean, well-motivated design that bridges AR and masked diffusion in the discrete RVQ domain.** The patch-level factorization (Eq. 1–2, Section 3.1.1) formalizes how an AR summarizer drafts a coarse sketch while a masked diffusion infiller resolves intra-patch dependencies in parallel. This is a sensible adaptation of the DiTAR paradigm to discrete space, and the empirical results in Table 1 show that this coupling works well: DiSTAR-medium (0.3B) achieves a WER of **1.66** on LibriSpeech test-clean, well below the 2.39 of DiTAR (0.6B, continuous next-patch diffusion), despite using half the parameters.

2. **Strong subjective evaluation results.** On Seed-TTS test‑en (Table 2), DiSTAR achieves the highest SMOS (3.31 ± 0.25) and the only positive CMOS (0.22 ± 0.13) against human (0.00) among five compared systems (FireRedTTS, CosyVoice 2, E2TTS, F5TTS). This is a notable result that directly supports the claim of superior naturalness and speaker consistency.

3. **Variable bitrate and compute control without retraining.** Section 3.4 (stochastic layer truncation) and Figure 2 demonstrate that pruning higher RVQ layers at inference provides a smooth quality–compute trade-off (SPK rising from ≈0.58 to ≈0.64 as layers increase, WER staying near 2.0). This is a practical engineering contribution for deployment scenarios with bandwidth or latency constraints.

4. **No duration predictor or forced alignment.** As noted in Section 3.1.2, DiSTAR's fully discrete setting with an [EOS] token eliminates the need for explicit duration predictors or alignment modules that many prior TTS systems require, simplifying the training pipeline.

5. **Embedding initialization bootstrapping from codec codebooks** (Section 3.4). Transplanting the first 16 embedding channels from the RVQ codebook and sampling the remaining dimensions from a matched Gaussian is a non-obvious detail that likely stabilizes early training.

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained metric anomalies that would benefit from discussion.** On LibriSpeech (Table 1), DiSTAR-medium achieves a WER of 1.66, which is lower than both the human reference (1.80) and the RVQ resynthesis (1.83). On SeedTTS, F5TTS also beats human WER (1.35 vs. 1.47), so the phenomenon is not unique to DiSTAR, but the effect is present and the paper offers no discussion of why synthetic speech might be more accurately transcribed by Whisper-large-v3 than natural speech. Similarly, the positive CMOS of 0.22 ± 0.13 against the human reference on SeedTTS (Table 2) is unusual — listeners are reported to prefer the synthetic output over natural speech. While this could reflect a real advantage of cleaner synthesized speech, the paper does not provide any analysis or caveat. The absence of subjective test details (number of listeners, protocol, confidence intervals) in the available text — though some may reside in the stripped appendix — combined with the lack of explanation for the WER anomaly, weakens the credibility of the headline results. A brief discussion acknowledging and contextualizing these numbers would substantially strengthen the paper.

2. **Incomplete baseline set for a "state-of-the-art" claim.** The paper does not compare against **VALL‑E 2** (Chen et al., 2024), a prominent zero-shot TTS system that also operates on RVQ codes with an autoregressive LM. Since DiSTAR's core contribution is about modeling the RVQ discrete space, the absence of this directly relevant discrete-space baseline is a notable omission. The baselines Voicebox and NaturalSpeech 3 are in the continuous domain and are less critical given that the paper already compares against continuous systems (E2TTS, F5TTS, DiTAR), but the VALL‑E 2 gap weakens the SOTA claim.

3. **Uncontrolled comparison against the most closely related prior work (DiTAR).** DiTAR results in Table 1 are taken from its original paper (marked with ♦) rather than from a controlled re-implementation on the same data, with matched NFE (DiTAR 10 vs. DiSTAR 24), and matched parameter count. This makes it difficult to attribute DiSTAR's improvements specifically to the discrete-space design rather than to differences in training data scale, inference compute, or model capacity.

### Minor

1. **Limited ablation study.** Only one ablation is reported (decoding strategies in Table 3), covering different temperature settings and greedy vs. sample decoding. Missing are ablations that would isolate the contribution of key components: the effect of the AR drafter (e.g., replacing it with a fixed random sketch), the effect of patch size and stride, the impact of the masked diffusion vs. a simpler feedforward infiller, and the influence of the number of diffusion steps (NFE). The paper states "detailed analysis of various components" but the evidence is thin.

2. **No reported inference speed or real-time factor.** The paper claims "inference cost close to DiTAR" but DiSTAR uses 24 NFE versus DiTAR's 10, and no wall-clock time or RTF comparison is provided. Without this, the efficiency claim is unsubstantiated.

3. **The "tail-first bias" mitigation heuristics are ad hoc and the improvement is modest.** The decoding heuristics (layer-wise temperature shaping, position-wise temperature shaping, hybrid sampling) are engineering fixes for a decoding instability rather than principled components of the method. The ablation (Table 3) shows that the best greedy result (WER 1.91) already outperforms the best sampled result with heuristics (WER 1.99), and the heuristics bring only a modest gain over vanilla sampling (WER 2.11 → 1.99). This does not invalidate the method but tempers the claimed significance of the inference strategy contribution.

### Trivial

None.

## Nice-to-Haves

- An ablation varying patch size and stride, mentioned as deferred to Appendix D, would be useful in the main text since patch design is a core architectural choice.
- A discussion of limitations (e.g., potential information loss from RVQ quantization, whether the discrete space has any fidelity ceiling) would improve the paper's completeness.
- Statistical significance or confidence intervals on objective metrics (WER, SIM) would help assess the reliability of the reported improvements.

## Removed Points

These points were raised by reviewers and removed with brief justification:

- **"Implausible results that undermine evaluation validity" (critic's framing):** The harsh critic characterized the WER and CMOS anomalies as "fatal" and "internally inconsistent with expected performance upper bounds." This framing is disproportionate. The WER anomaly (synthetic speech beating human) is also observed for F5TTS on SeedTTS (1.35 vs. 1.47 human), making it a known phenomenon in TTS evaluation — synthetic speech's lower acoustic noise can benefit ASR — not an implausible fabrication. The paper should discuss it (already listed as Major weakness 1), but the critic's "fatal" characterization is removed as overblown.
- **"Decoding heuristics are ad hoc post-hoc fixes" framing:** Removed the strong pejorative framing. The heuristics are one valid approach to a real decoding problem; they show modest but measurable improvements. Retained as Minor weakness 3.
- **Claim that discrete advantages are "asserted but not demonstrated":** Removed as this asks the paper to run experiments (training stability, loss curves, sensitivity analyses) outside its stated scope. The paper does provide indirect evidence by comparing against several continuous systems and showing competitive or better results.
- **Criticism about missing Voicebox, NaturalSpeech 3, SoundStorm as baselines:** Removed as these are either continuous-domain systems already represented by the continuous baselines included (E2TTS, F5TTS, DiTAR) or not directly relevant zero-shot TTS systems (SoundStorm). VALL‑E 2 is the one valid omission, retained in Major weakness 2.
- **Strengths that were generic (e.g., "this paper addressed an important problem"):** Removed as uninformative.
- **Formatting/style nitpicks and comments about missing appendix content:** Removed per hard rules.

## Novel Insights

The most interesting observation that emerges from the reviews is how the discrete masked diffusion formulation naturally handles a structural challenge that continuous next-patch diffusion (DiTAR) has to engineer around: modeling the joint time-depth dependencies of RVQ codes. The stochastic layer truncation (Section 3.4) leverages the layered structure of RVQ to provide a zero-cost variable-bitrate mechanism that is more principled than training separate models for different bitrates. The "tail-first bias" during decoding (Section 3.4) is a concrete practical finding for anyone working with non-autoregressive discrete speech generation — the observation that later positions within a patch become overconfident early is a side effect of the causal structure of speech that would need to be addressed in any similar architecture. These insights go beyond the paper's headline numbers and point to design considerations for future discrete speech generation systems.

## Suggestions

1. Add a brief discussion in Section 4.2 acknowledging that WER slightly below human/RVQ-resynthesis on LibriSpeech is consistent with synthetic speech being cleaner than natural recordings, and that the CMOS of 0.22 against human may partly reflect a preference for reduced acoustic variability. This would preempt the most serious evaluation concern.
2. Provide a controlled comparison: train DiTAR on the same Emilia data with matched NFE and comparable parameter count, or at minimum include a table that normalizes for these factors and discusses the caveat explicitly.
3. Add a comparison against VALL‑E 2 on at least one benchmark (LibriSpeech or SeedTTS) to substantiate the SOTA claim in the discrete RVQ space.
4. Include a real-time factor (RTF) measurement for DiSTAR at 24 NFE and for DiTAR at 10 NFE on the same hardware to support the claimed efficiency parity.
5. Expand the ablation study to cover at minimum the effect of patch size, the contribution of the AR drafter (vs. a fixed sketch), and the effect of varying the number of diffusion steps.

## Score and Decision

Let me calibrate using anchors.

**Round 1 — Bracketing:** Queried anchors in three bands:

| Band | Anchor ID | Avg Score | Topic |
|---|---|---|---|
| Weak (≤3.5) | FaGDopTTTC | 2.50 | Zero-shot discrete flow matching TTS |
| Weak (≤3.5) | im2a2MHoke | 2.50 | Non-autoregressive TTS |
| Weak (≤3.5) | v394xbZFlu | 2.50 | Discrete diffusion language generation |
| Weak (≤3.5) | HHsD970kdE | 3.00 | Diffusion for RNN states |
| Mid (3.5–7.5) | h5KLpGoqzC | 5.20 | Hierarchical semi-discrete residual TTS |
| Mid (3.5–7.5) | e3XLWHFrnr | 4.40 | AR+NAR audio-text model |
| Mid (3.5–7.5) | yh7MV2V0ba | 5.50 | Variational autoencoding discrete diffusion |
| Mid (3.5–7.5) | llMfmDtWka | 4.80 | Speech diffusion tokenizer |
| Strong (≥7.5) | kI27Niy4xY | 8.00 | Text-to-3D (different domain) |
| Strong (≥7.5) | qOyF214xmg | 8.00 | Language model transduction (different domain) |
| Strong (≥7.5) | RDerF20JYT | 8.00 | Protein generation (different domain) |

**Round-1 bracket:** 4.0–6.0. The weak anchors (2.5–3.0) are clearly below DiSTAR's quality; the strong anchors (8.0) are from different domains and not directly comparable. The most relevant anchors sit in the 4.4–5.5 range.

**Round 2 — Narrowing:** Queried inside the bracket and read full reviews for key anchors.

| Anchor ID | Avg Score | Compared to DiSTAR |
|---|---|---|
| h5KLpGoqzC | 5.20 | Comparable — both have similar trade-offs (mixed metric results, limited novelty concerns, some evaluation gaps). DiSTAR has stronger subjective evaluation. |
| e3XLWHFrnr | 4.40 | DiSTAR is clearly stronger — this paper had no subjective eval and limited SOTA comparison. |
| llMfmDtWka | 4.80 | Different domain (tokenizer, not TTS). Less directly comparable. |
| JbLmIoWwDC | 6.00 | Slightly stronger — Gogo had a more novel codec contribution. DiSTAR's method is more incremental. |
| zjaV5zmlkl | 5.50 | Comparable quality — both are solid papers with clear contributions and some evaluation limitations. |

DiSTAR sits above the 4.40 and 4.80 anchors (better evaluation, more complete results) and is comparable to the 5.20 and 5.50 anchors. It is slightly below the 6.00 Gogo paper, which had stronger methodological novelty in its codec design. The evaluation gaps (unexplained metric anomalies, missing VALL‑E 2 comparison, uncontrolled DiTAR comparison) are real but not fatal — they are addressable in revision.

**Final score: 5.5.** DiSTAR is a well-executed paper with a clearly described method, strong results across both objective and subjective metrics, and several practical engineering contributions. The evaluation anomalies and baseline omissions prevent it from scoring higher but do not undermine the core contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>