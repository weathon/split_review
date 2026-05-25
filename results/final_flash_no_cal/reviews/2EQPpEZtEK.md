Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

DiSTAR proposes a zero-shot TTS framework that couples an autoregressive (AR) language model with a masked diffusion model entirely within an RVQ discrete code space. The AR model drafts patch-level hidden representations, and a masked diffusion transformer (inspired by LLaDA) completes the patch in parallel via iterative demasking. The system operates without forced alignment or explicit duration predictors, supports overlapping patches, and enables on-the-fly bitrate/compute control by pruning RVQ layers at inference. Experiments on LibriSpeech and SeedTTS benchmarks report competitive WER, speaker similarity, and subjective quality scores against several recent systems.

## Strengths

1. **Novel and well-motivated architecture.** Combining an AR context encoder with masked diffusion in the *discrete* RVQ space is a novel design that inherits the stability of discrete LM training while enabling patch-level parallelism. This is a clean synthesis of ideas from DiTAR (next-patch AR→diffusion) and LLaDA (masked diffusion), applied to an underexplored setting. The design is backed by clear reasoning about RVQ's time-depth structure (Section 3.1, Figure 1).

2. **On-the-fly bitrate and compute control.** The stochastic layer truncation training strategy (randomly dropping RVQ layers during training) enables inference-time bitrate/compute trade-offs by simply pruning upper RVQ layers with no retraining. Figure 2 shows a smooth SPK–WER trade-off across 2–9 RVQ layers, supporting the controllability contribution (Section 4.4). This is a practical and clearly demonstrated advantage.

3. **Competitive WER and subjective quality.** DiSTAR-medium achieves the lowest WER among reported systems on both LibriSpeech (1.66%) and SeedTTS (1.32%) (Table 1), and attains the highest SMOS (3.31) and CMOS (0.22) in subjective listening tests (Table 2). These results are obtained with a moderate parameter budget (0.3B generation model).

4. **Elimination of explicit duration predictor and forced alignment.** The discrete [EOS] token and patch-wise masked diffusion provide a natural termination mechanism, simplifying the training pipeline relative to many continuous approaches (Section 3.1.2). This is a legitimate engineering advantage.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled baseline comparisons undermine the SOTA claim.** DiTAR scores are marked with ♦, indicating they are taken from the DiTAR publication rather than re-evaluated under identical conditions. The paper adopts the F5TTS subset for LibriSpeech evaluation, but it does not confirm that DiTAR's published numbers (or those of other baselines) were obtained on the same subset with the same ASR pipeline, prompt selection, and evaluation protocol. Without controlled re-evaluation or official-model inference on the identical test set, the claim that DiSTAR "surpasses" DiTAR and other systems is not rigorously substantiated. The paper should either re-evaluate all baselines under identical conditions or clearly disclose which numbers are from external sources and discuss the potential mismatch.

2. **No quantitative evidence for the claimed computational efficiency.** The paper states DiSTAR has "inference cost close to its continuous counterpart DiTAR" and "comparable or lower computational cost" (Section 1, contributions), but provides no latency, FLOPs, or throughput measurements anywhere. This is particularly important because DiSTAR uses NFE=24 versus DiTAR's NFE=10 (Table 1). Without efficiency numbers, the computational cost claim is unverifiable and should either be substantiated or removed.

3. **Most directly comparable baseline (DiTAR) absent from subjective evaluation.** Table 2 compares DiSTAR against FireRedTTS, CosyVoice 2, E2TTS, and F5TTS in listening tests, but omits DiTAR — the closest technical relative and the most important anchor for the paper's central motivation (discrete vs. continuous space for the same AR+diffusion pipeline). Including DiTAR in the subjective evaluation would directly test the paper's core thesis.

### Minor

4. **WER below human/resynthesis not discussed.** On LibriSpeech test-clean, DiSTAR-medium achieves 1.66% WER versus human 1.80% and RVQ resynthesis 1.83%. The generated speech is more intelligible to Whisper-large-v3 than both the original human recordings and the codec reconstruction of those recordings. This is an unusual pattern that the paper does not acknowledge or attempt to explain. While the absolute differences are small (~0.14–0.17 percentage points) and could be within measurement noise, the absence of any discussion — even a note that it may reflect ASR bias or that confidence intervals are needed — is a gap.

5. **Insufficiently isolated ablation of decoding heuristics.** Table 3 compares three decoding configurations (vanilla sampling, sampling with temperature shaping, greedy with temperature shaping), but does not isolate the individual contributions of layer-wise temperature shaping, position-wise temperature shaping, and hybrid sampling. These three heuristics are introduced as parts of the method (Section 3.4), yet no ablation shows the effect of each in isolation. Controlled ablations (e.g., temperature shaping only, greedy-only, hybrid-only) would clarify which components are essential.

6. **AR training objective is ambiguous.** The paper describes the AR module as producing a "conditioning state" and "hidden sketch," but never states whether the AR is trained with a separate next-patch prediction loss or entirely end-to-end through the masked diffusion loss (Equation 2). The text "Training minimizes the cross-entropy objective in equation 2" (Section 3.1.2) suggests the latter, but this is not clearly distinguished from the factorization in Equation 1. Clarifying the AR's training signal would improve precision.

7. **"SIM on par" overstates results.** The paper states "DiSTAR yields SIM on par with the best alternatives" (Section 4.2), but Table 1 shows E2TTS achieving higher SIM on both LibriSpeech (0.70 vs. 0.67) and SeedTTS (0.71 vs. 0.66). While DiSTAR leads on subjective SMOS, the objective SIM claim is misleading and should be qualified.

8. **[EOS] termination mechanism is asserted but not explained.** The paper claims that "the fully discrete setting preserves an [EOS] token for the immediate termination of patch-level generation" (Section 1), but the method section never explains how [EOS] integrates with the patch-wise process — whether it is a token in the RVQ code space, a special patch, or something else. This is a missing technical detail.

9. **No statistical significance for objective metrics.** No confidence intervals or significance tests are reported for WER, SIM, or UTMOS in Table 1, making it impossible to assess whether differences between systems are reliable. Subjective metrics (Table 2) do include confidence intervals, which is good.

10. **Training data parity with baselines not discussed.** DiSTAR is trained on 50k hours of Emilia, but the paper does not state whether baselines were trained on comparable data volumes. Disparities in training data scale could explain performance differences independently of architectural choices.

### Trivial
None.

## Nice-to-Haves
- A pointwise ablation of the three decoding heuristics (layer-wise temperature shaping, position-wise temperature shaping, hybrid sampling) would strengthen the technical contribution.
- Reporting latency or throughput numbers would substantiate the computational efficiency claim.
- Including DiTAR in the subjective listening test would directly test the paper's central thesis.
- Brief discussion of why WER falls below the RVQ resynthesis baseline would preempt reviewer concerns.
- A reproducibility statement detailing code/data release plans would be beneficial.

## Removed Points
These points were flagged by the reviewers but are removed with justification:

- **"Introduction overstates fragility of continuous-latent systems":** The paper uses hedged language ("many rely on," "can be sensitive") and does not claim all continuous approaches share these limitations. This is a strawman reading of the text.
- **"Language model' terminology is misleading":** Calling a causal transformer that processes discrete token sequences a "language model" is consistent with standard usage in the TTS literature. A terminology nitpick, not a substantive issue.
- **"Total parameter count understated by omitting codec":** All compared systems use external codecs/encoders whose parameters are not counted in Table 1. This is standard reporting practice in the field; the paper separately discloses the codec size (≈0.3B).
- **"Major analyses deferred to (missing) appendix":** Appendix sections are stripped by the PDF extraction pipeline, not missing from the original submission. The parser artifact should not count against the paper.
- **"No code/checkpoints released":** This is standard for anonymized submissions; many papers in this field do not release artifacts at submission time.
- **"Missing related works":** Without external sources to confirm claimed omissions, this criticism cannot be validated.
- **"Formatting/style/presentation issues":** Artifacts of the PDF extraction process, not author errors.

## Novel Insights
None beyond the paper's own contributions. The review process surfaces the standard tension between architectural novelty and evaluation rigor, but does not produce a new insight about the method or the problem.

## Suggestions
1. Re-evaluate all baselines under identical conditions (same test subset, same ASR pipeline, same prompt selection) or clearly delimit which numbers were externally sourced and discuss potential mismatch.
2. Report latency, FLOPs, or throughput measurements to substantiate the computational efficiency claim.
3. Include DiTAR in subjective listening tests.
4. Provide confidence intervals or significance tests for objective metrics.
5. Add a brief discussion of the WER relative to human/resynthesis (e.g., acknowledging potential ASR bias).
6. Clarify the AR module's training objective and the [EOS] termination mechanism.
7. Isolate the decoding heuristic components in ablation.

## Score and Decision

**MY FINAL SCORE:** <score>4.5</score>
**MY FINAL DECISION:** <decision>Reject</decision>