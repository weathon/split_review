Now I have a thorough understanding of the calibration landscape. Let me produce the final consolidated review.

## Summary

DiSTAR proposes a zero-shot TTS framework that couples an autoregressive (AR) patch-level drafter with a masked diffusion model, operating entirely in the RVQ discrete code space. The AR module drafts a compact hidden sketch for the next patch, and the masked diffusion Transformer completes the patch in parallel via iterative discrete demasking. The design avoids duration predictors, supports greedy and sampling-based decoding, and enables on-the-fly bitrate control via RVQ layer pruning. Experiments on LibriSpeech and Seed-TTS show best-in-class WER, competitive speaker similarity and UTMOS, and leading subjective CMOS/SMOS.

## Strengths

- **Novel and well-motivated architecture.** Combining a causal AR drafter with a discrete masked diffusion infiller in a shared RVQ space is a genuinely new design that jointly models temporal (cross-patch) and layer-wise (intra-patch) dependencies. The paper clearly articulates why this avoids the fragilities of continuous-domain next-patch diffusion (high-dimensional optimization) and the limitations of single-codebook AR (intra-frame coupling), making the contribution conceptually clean.

- **Strong empirical results supported by multiple metrics.** Table 1 shows DiSTAR-medium achieves the lowest WER among all baselines on both LibriSpeech test-clean (1.66%) and Seed-TTS test-en (1.32%). Table 2 shows the best SMOS (3.31 ± 0.25) and the only positive CMOS (0.22 ± 0.13) in subjective evaluation, with the CMOS advantage being the most convincing demonstration of improved naturalness/robustness. The subjective results are gathered from human raters, providing independent evidence beyond automatic metrics.

- **Controllable inference without retraining.** Section 4.4 and Figure 2 demonstrate that DiSTAR can trade off bitrate, compute, and quality at test time by simply pruning upper RVQ layers, enabled by stochastic layer truncation during training. Speaker similarity rises from ~0.58 (2 layers) to ~0.64 (9 layers) while WER remains roughly stable — a practical advantage for deployment under varying bandwidth constraints.

- **Principled removal of duration predictors.** The discrete [EOS] token provides a natural termination signal for patch-level generation, eliminating the need for explicit duration predictors, stop heads, or forced alignment that many competing systems require (e.g., DiTAR, F5TTS). This simplifies the pipeline without sacrificing quality.

## Weaknesses

### Fatal
None.

### Major

- **DiSTAR achieves lower WER than both human speech and the codec reconstruction of the original audio, a result that is neither explained nor discussed.** On LibriSpeech test-clean, DiSTAR-medium reports 1.66% WER vs. human 1.80% and RVQ resynthesis 1.83%; on Seed-TTS test-en, 1.32% vs. human 1.47% and RVQ resynthesis 1.71% (Table 1). The fact that the generated speech is *more intelligible to the ASR model* than the codec's own reconstruction of the ground-truth audio is a striking pattern that should at minimum be acknowledged and contextualized. The paper's silence on this point is a significant omission. While the result does not necessarily invalidate the evaluation — plausible explanations exist (e.g., the diffusion process may smooth codec artifacts that confuse the ASR, or the ASR model may have distributional biases) — the paper should provide such reasoning or analysis. Without it, readers cannot determine whether the WER advantage reflects genuine improvements or an evaluation artifact.

- **No confidence intervals or variance estimates are reported for objective metrics in Table 1.** Given that many comparisons have narrow margins (e.g., DiSTAR-medium 1.66% vs. F5TTS 2.02% on LibriSpeech; DiSTAR-medium 1.32% vs. F5TTS 1.35% on Seed-TTS), the absence of error bars makes it impossible to assess whether the observed differences are statistically significant. This is a standard expectation for empirical papers in this field.

- **The inference-cost claim ("maintaining the inference cost close to its continuous counterpart DiTAR") is unsupported.** DiSTAR uses NFE=24 vs. DiTAR's NFE=10. Without any wall-clock time, FLOPs, throughput, or latency measurements, the claim is purely speculative and potentially misleading. If per-NFE cost is indeed lower (e.g., because discrete token operations are cheaper than continuous latent operations), the evidence must be provided.

### Minor

- **The paper overclaims SOTA across all dimensions.** The abstract states DiSTAR "surpasses state-of-the-art zero-shot TTS systems in robustness, naturalness, and speaker/style consistency." However, DiSTAR is not SOTA on SIM (E2TTS scores 0.70 vs. DiSTAR's 0.67 on LibriSpeech) or UTMOS (IndexTTS scores 4.35 vs. DiSTAR's 4.29 on LibriSpeech; DiTAR scores 4.15 vs. DiSTAR's 4.05 on Seed-TTS). The SOTA claim is supported for WER and subjective CMOS, but should be calibrated for the other metrics. The confidence intervals for CMOS (0.22 ± 0.13) also partially overlap with F5TTS (0.01 ±‱0.12), so the edge in subjective naturalness should be stated more carefully.

- **The main-paper ablations are limited to decoding strategies (Table 3).** The paper does not ablate the core architectural choice — i.e., what happens if the masked diffusion module is replaced with a standard patch-level AR LM, or if the AR draft is removed. While the appendix may contain additional ablations (stripped by the parser), the main body would benefit from at least one ablation that isolates the contribution of the masked diffusion component versus simpler alternatives.

- **Subjective evaluation is reported on only one dataset (Seed-TTS test-en).** Including a second dataset (e.g., LibriSpeech) in subjective tests would strengthen the claim of generalization.

- **The "tail-first" bias and associated decoding heuristics (Section 3.4) are described but not quantitatively supported.** Table 3 shows the combined effect of temperature shaping + hybrid sampling, but does not decompose the individual contribution of each trick (e.g., position-wise temperature shaping alone, layer-wise temperature shaping alone). The claim that these heuristics mitigate a specific bias would be stronger with such decomposition.

### Trivial
None.

## Nice-to-Haves

- A decomposition ablation for the three decoding heuristics (layer-wise temperature, position-wise temperature, hybrid sampling) to isolate their individual effects.
- A discussion of the effect of overlapping vs. non-overlapping patch design (stride relative to patch size).
- An evaluation of the repetition-aware penalty's impact on code diversity.

## Removed Points

- **"WER below human performance means the evaluation is fundamentally flawed / cannot be trusted."** The critic frames this as a fatal flaw that invalidates all quantitative results. This is too strong: the differences are small, the subjective results independently support quality claims, and plausible explanations exist. I have retained this as a **Major** weakness (the paper's silence on the anomaly) rather than a fatal one.
- **"Missing ablations of the masked diffusion module, conditioning strategy, aggregator design, stochastic layer truncation."** These are listed in the paper as deferred to Appendix C/D, which is standard. Per the rules, the parser stripping the appendix should not be penalized. Removed.
- **"The conceptual inconsistency between Eq. (1) and Eq. (2)."** The paper explicitly states that Eq. (1) is the factorization via the chain rule, and Eq. (2) is the training loss for the masked diffusion component. The relationship is clear enough. Removed.
- **"Blurry description of 'linearized across time'."** The paper clarifies that "the target RVQ streams are linearized across time into a one-dimensional token sequence" and adds that positional/type embeddings are added. This is standard for patch-based models. Removed.
- Strengths that are generic/overlapping removed: "Elimination of duration predictors" is retained as a strength; "Competitive parameter efficiency" and "Robustness under greedy and stochastic decoding" are less central and combined into other strengths or dropped.
- **"Pure formatting nitpicks"** and **"typos/grammar"** removed per rules.

## Novel Insights

The harsh critic identifies the WER anomaly (generated speech outperforming codec resynthesis) as the single most important issue, and this is a genuinely sharp observation that the original paper overlooked. The insight is that this anomaly, if left undiscussed, undermines the credibility of the primary quantitative claim even if the result is ultimately correct. This is a useful meta-point about evaluation hygiene in TTS: when a generative model outperforms its own codec's reconstruction of ground truth, the burden is on the authors to explain why. No reviewer points to a deeper structural flaw in the method itself; the architecture is sound and the contribution is real.

## Suggestions

1. **Address the WER anomaly head-on.** Add a dedicated paragraph in the results section discussing why DiSTAR's WER is lower than the codec resynthesis and human speech. Potential explanations include: Whisper's sensitivity to codec artifacts that the diffusion process smooths out, distributional mismatch between human speech and Whisper's training data, or a genuine improvement in intelligibility. If possible, verify with a second ASR model (e.g., a different Whisper variant or a wav2vec-based model) and report whether the pattern holds.

2. **Add confidence intervals or error bars to Table 1.** Even bootstrap-estimated intervals over the test utterances would substantially improve evaluation rigor.

3. **Provide concrete inference-cost measurements.** Report wall-clock time, RTF, or FLOPs for DiSTAR vs. DiTAR on the same hardware with comparable batch sizes.

4. **Calibrate the SOTA language.** Replace blanket "state-of-the-art" claims with metric-specific statements: "best WER and subjective CMOS, competitive SIM and UTMOS."

5. **Add at least one tight ablation** (e.g., replace the MDM with a patch-level AR LM) in the main paper to isolate the contribution of the masked diffusion component.

## Score and Decision

### Calibration

**Round 1 (bracketing):**
- Weak anchors (< 3.5): SaMoye (3.00, withdrawn), TinyStories (3.00, withdrawn) — these papers have fundamentally broken evaluations or trivial contributions. DiSTAR is clearly stronger.
- Middle anchors (3.5–7.5): DiTTo-TTS (6.25, accepted), S-DiT (5.75, rejected), F5-TTS (5.50, rejected), Vec-Tok (5.20, rejected), T2V2 (6.25, accepted).
- Strong anchors (> 7.5): Block Diffusion (8.00, oral), Transfusion (7.60, oral) — these are major methodological innovations at scale. DiSTAR is much weaker.

**Initial bracket**: 4.5–6.5.

**Round 2 (narrowing within bracket):**
Compared to **DiTTo-TTS (6.25, accepted)**: That paper had extensive ablations, rigorous comparisons, and no unexplained evaluation anomalies, though limited novelty. DiSTAR has stronger novelty but weaker evaluation rigor. DiSTAR is weaker than DiTTo-TTS.

Compared to **S-DiT (5.75, rejected)**: Had unsupported claims and unclear contributions but comprehensive experiments. DiSTAR has clearer contributions but a more concerning evaluation anomaly. Roughly comparable, DiSTAR slightly weaker due to the unresolved anomaly.

Compared to **F5-TTS (5.50, rejected)**: Incremental engineering with strong empirical support. DiSTAR has stronger architectural novelty. Slightly above F5-TTS.

Compared to **T2V2 (6.25, accepted)**: Unified ASR+TTS, strong experiments. DiSTAR is roughly comparable in contribution strength but has the evaluation weakness that T2V2 lacks.

**Final assessment**: DiSTAR's core architecture is a genuine contribution, and its results (especially subjective) are strong. However, the unexplained WER anomaly, missing confidence intervals, unsupported efficiency claim, and overclaiming collectively prevent the paper from meeting the acceptance bar at a top venue in its current form. The paper is closest in profile to S-DiT (5.75, rejected).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>