Now I have enough information to write the consolidated review. Let me produce it.

---

## Summary

DiSTAR proposes a zero-shot TTS framework that operates entirely in the discrete RVQ code space by coupling an autoregressive language model (for patch-level drafting) with a masked diffusion Transformer (for intra-patch refinement). The design eliminates explicit duration predictors and forced alignment, supports test-time layer pruning for variable bitrate/compute, and introduces RVQ-aware decoding heuristics. On standard benchmarks, DiSTAR-medium (0.3B) achieves the lowest WER among all compared systems, though speaker similarity (SIM) lags behind some continuous baselines.

## Strengths

- **Genuinely novel architecture coupling AR drafting with discrete masked diffusion in RVQ space.** Unlike prior work that operates in continuous latent space (DiTAR) or uses cascaded AR+refinement pipelines, DiSTAR keeps the entire generation process in discrete RVQ tokens. The AR module produces a conditioning hidden state, and the masked diffusion module performs parallel iterative demasking — this is a clean, well-motivated design that differs from both purely AR discrete TTS (VALL-E, IndexTTS) and continuous next-patch diffusion (DiTAR).

- **Strongest WER on both benchmarks.** Table 1 shows DiSTAR-medium achieving 1.66% WER on LibriSpeech-PC and 1.32% on SeedTTS test-en, surpassing all baselines including F5TTS (2.02/1.35), DiTAR (2.39/1.78), and IndexTTS (2.57/1.92). This is the paper's most robust finding and directly supports the claim that discrete RVQ space reduces the fragility observed in continuous-latent systems.

- **Test-time layer pruning for controllable bitrate/compute.** Figure 2 systematically shows the trade-off between retained RVQ layers and performance (WER, SPK) without retraining. This is enabled by stochastic layer truncation during training and provides practical controllability that no prior TTS system demonstrates at this granularity.

- **RVQ-aware decoding heuristics with quantified benefits.** Section 3.4 introduces layer-wise and position-wise temperature shaping plus hybrid sampling. Table 3 shows these heuristics reduce WER from 2.11 → 1.99 (sampling) and 1.99 → 1.91 (greedy), demonstrating that simple inference-side modifications can substantially improve discrete-space generation quality.

- **Clean ablation on decoding strategies.** Table 3 provides a direct comparison of greedy vs. sampled decoding with controlled temperature settings, giving practitioners actionable guidance.

## Weaknesses

### Major

1. **Anomalous subjective evaluation results with no protocol description.** Table 2 reports Human SMOS = 3.07 (unusually low — typical TTS human references score 3.5–4.5) and DiSTAR CMOS = +0.22 against the human anchor, meaning listeners preferred synthetic outputs over natural speech. The paper provides zero details about the subjective test: number of listeners, evaluation protocol (MUSHRA, A/B, etc.), whether reference clips were resynthesized, confidence intervals for the Human row, or randomization procedures. Without this information, the subjective claims of "surpassing in naturalness and speaker similarity" cannot be evaluated. This is the most serious weakness because it directly affects the paper's headline claims.

2. **Inference cost claim is unsupported by data.** The introduction states that DiSTAR has "inference cost close to its continuous counterpart DiTAR," but DiSTAR uses NFE = 24 while DiTAR uses NFE = 10. No wall-clock time, real-time factor, or FLOPs comparison is provided. Parameter count (0.3B vs. 0.6B) alone does not determine cost when NFE differs by 2.4×. This claim is vacuous without latency measurements.

3. **Speaker similarity claim is overclaimed relative to objective evidence.** The introduction and conclusion claim "state-of-the-art ... speaker similarity," but DiSTAR-medium's SIM on LibriSpeech (0.67) trails E2TTS (0.70) and matches DiTAR (0.67). On SeedTTS, DiSTAR (0.66) trails E2TTS (0.71) and F5TTS (0.68). The experimental section more accurately describes SIM as "on par with the best alternatives" — the abstract and conclusion should be revised to match this measured language.

### Minor

4. **One baseline (DiTAR) uses published scores rather than re-evaluation.** Table 1 marks DiTAR with ♦ for scores reported in the original DiTAR paper. Since evaluation conditions (Whisper model version, prompt selection, segmentation) may differ, this is not a controlled comparison. That said, only one baseline is affected; the other baselines (E2TTS, F5TTS, IndexTTS) appear to have been re-evaluated.

5. **Missing ablation: contribution of the AR component.** The paper never ablates the AR module by comparing against a variant that conditions the diffusion directly on past codes without the AR hidden state. Such an ablation would clarify whether the two-stage design is essential or whether a simpler conditioning scheme suffices.

6. **No comparison against a pure AR decoder of equivalent capacity.** A natural baseline is a fully autoregressive model over flattened RVQ codes (temporal + depth) with similar parameter count. This would disentangle the benefits of masked diffusion from the overall architecture.

### Trivial

7. The "AR drafted sketch" terminology (Section 1 and 3) is somewhat imprecise — the sketch is the AR module's hidden state h_k, not a separate discrete draft sequence. The method description is clear enough, but the term could mislead readers familiar with speculative decoding or two-stage draft-verify pipelines.

## Nice-to-Haves

- Report statistical significance (confidence intervals or p-values) for the WER and SIM differences, especially given small gaps between DiSTAR and F5TTS (1.66 vs 2.02 on LibriSpeech).
- Report real-time factor (RTF) or GPU-seconds for DiSTAR and DiTAR at their respective NFE settings.
- Describe the subjective evaluation protocol in full (number of listeners, procedure, whether human speech was resynthesized through the codec).
- Validate the "tail-first bias" hypothesis (Section 3.4) with distributional data on confidence scores across positions/layers.

## Removed Points

*The harsh critic's claim that the "AR drafted sketch" is never defined concretely is not accurate — the paper defines it as the hidden state h_k from the AR module in Section 3.1.1 and 3.3. Moved here as it reflects a misreading.*

*The harsh critic's claim that "comparisons against published scores instead of re-evaluated baselines" applies broadly is overstated — only DiTAR (one baseline) uses cross-paper scores. Other baselines are not marked with ♦. Downgraded to minor.*

*The strength finder's claim that "strong subjective results with positive CMOS against human references" is a strength is contradicted by the paper's own lack of evaluation protocol details. This is not a valid strength without proper documentation. Moved here.*

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide full details of the subjective listening test (protocol, number of listeners, confidence intervals for all conditions including Human) in the main paper or appendix. If the current results are genuine, they should be contextualized (e.g., explain why human SMOS is only 3.07).
2. Report actual inference speed (RTF or GPU-seconds) for DiSTAR and DiTAR to substantiate the cost claim.
3. Add an ablation removing the AR module to show its necessity.
4. Tone down the "state-of-the-art speaker similarity" claim in the abstract and conclusion to match the objective SIM results.

## Score and Decision

Round-1 bracket: Based on calibration search, similar TTS papers (CLaM-TTS 6.40, DiTTo-TTS 6.25, MaskGCT 5.25, HALL-E 6.40) place plausible scores between 4.5 and 7.0. The weak band (<3.5) anchors were irrelevant to the paper's topic and quality level. The strong band (>7.5) anchors were all non-TTS papers with different standards.

Round-2 narrowing: Comparing against MaskGCT (5.25, avg scores 6/3/6/6) — DiSTAR has stronger methodological novelty and better WER results but similar evaluation gaps. Comparing against DiTTo-TTS (6.25, avg scores 6/8/5/6) — DiSTAR has comparable novelty but weaker evaluation documentation. The paper sits between these anchors.

Final score: **5.5**. This reflects a solid paper with genuine architectural novelty and strong objective WER results, but with notable evaluation gaps (subjective test opacity, unsubstantiated inference cost claim, overclaimed SIM) that prevent it from reaching the 6+ level. The paper's core contribution is worthwhile, but the evidence for the headline claims is weaker than the presentation suggests.

Anchors consulted across all rounds and comparisons:
- **m4mwbPjOwb** (3.00, round 1): Weak TTS paper; DiSTAR is clearly stronger.
- **pWdkM9NNCA** (3.00, round 1): Weak TTS; DiSTAR stronger.
- **mlPTNEIsgb** (3.25, round 1): Non-TTS; not comparable.
- **a8dQutiF9E** (3.40, round 1): Non-TTS; not comparable.
- **ofzeypWosV** — CLaM-TTS (6.40, round 1): Mixed reception; DiSTAR has stronger WER and comparable novelty but weaker evaluation reporting.
- **hQvX9MBowC** — DiTTo-TTS (6.25, round 1/2): Strong ablations; DiSTAR has better architectural novelty but less thorough evaluation.
- **ExuBFYtCQU** — MaskGCT (5.25, round 1/2): Similar discrete-domain TTS; DiSTAR has clearer novelty and better WER.
- **868masI331** — HALL-E (6.40, round 1): Similar domain; DiSTAR has more novel architecture.
- **Qn4HEhezKW** (5.00, round 2): Non-TTS diffusion LM; not directly comparable.
- **1pTlvxIfuV** (5.50, round 2): Non-TTS; not comparable.
- **zAogQOIphH** (5.20, round 2): TTS controllability paper; DiSTAR has stronger core results.
- **sMyXP8Tanm** (6.20, round 2): Non-TTS diffusion theory; not comparable.
- **WNvvwK0tut** (6.50, round 2): Text MDM scaling; DiSTAR is more application-focused.
- **71mqtQdKB9** (6.60, round 2): Non-TTS discrete diffusion; not comparable.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>