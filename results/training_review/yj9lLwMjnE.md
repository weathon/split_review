Now I have all the information needed. Let me produce the final consolidated review.

## Summary

UniWav proposes an encoder-decoder framework for unified pre-training of speech representation learning and generation. The encoder uses self-distillation with online clustering (DinoSR-style), while the decoder uses Flow Matching, trained jointly from scratch on 60k hours of LibriLight. The paper evaluates on three tasks: ASR (fine-tuning the encoder with CTC), in-context TTS (fine-tuning encoder+decoder), and speech tokenization (inserting a discrete bottleneck). Results show competitive ASR within ~0.5% WER of specialized models, TTS matching generative-only pre-training (SpeechFlow), and strong low-bitrate tokenization performance.

## Strengths

- **First end-to-end unified pre-training framework for both discriminative and generative speech tasks**: The paper jointly trains a representation encoder (self-distillation + online clustering) and a Flow Matching decoder from scratch, without relying on a two-stage pipeline or pre-trained teacher. This is a genuine architectural contribution — prior work either trained these components separately or used cascaded systems (Polyak et al., 2021; Zhang et al., 2023b).

- **Demonstrates feasibility of a single model across three diverse tasks**: Table 1 shows UniWav achieves reasonable ASR (within 0.5% WER of HuBERT/WavLM) while also matching SpeechFlow on in-context TTS (ASR-WER and speaker similarity). This is meaningful: no prior single pre-trained model supports both categories, and the paper's results confirm that the conflicting objectives can be balanced.

- **State-of-the-art low-bitrate speech tokenization**: At 500 bps, UniWav outperforms all prior methods (EnCodec, DAC, unit-HiFiGAN, SpeechTokenizer) on ASR-WER, UTMOS, and ViSQOL by clear margins, and remains competitive on speaker similarity. At 1 kbps, UniWav's ASR-WER (5.6%) and UTMOS (3.72) substantially exceed SpeechTokenizer (9.1%, 2.08), approaching 4 kbps SpeechTokenizer quality. This is the paper's strongest quantitative contribution.

- **Useful ablation and analysis (Tables 3–4, Figure 2)**: The scaling study reveals that the generative objective helps the encoder only when the encoder has sufficient capacity (24 layers) — a non-obvious finding. The mutual information analysis provides interpretable evidence for why UniWav retains more speaker information than HuBERT in deeper layers, linking architecture behavior to downstream task performance.

## Weaknesses

### Fatal
None.

### Major

- **Tokenization results confound joint training with decoder pre-training**: The headline tokenization results (Table 2) are achieved by fine-tuning a decoder that has already received 600k steps of flow-matching pre-training. The baselines (unit-HiFiGAN, SpeechTokenizer, EnCodec, DAC) do not benefit from a comparable pre-trained decoder — they train their decoders from scratch or use different training paradigms. The paper attributes the tokenization advantage to "joint representation and generation learning" (Section 3.4), but this claim cannot be separated from the confound of simply having a pre-trained flow-matching decoder. An ablation that pre-trains a decoder on *fixed* HuBERT representations (or on UniWav's encoder representations from a separately pre-trained encoder) and then fine-tunes for tokenization is needed to validate the attribution. Without it, the paper's most impressive quantitative result does not support its strongest interpretive claim. This is fixable but nontrivial.

- **No confidence intervals or variance estimates for any reported metric**: All results in Tables 1–4 are reported as single numbers without standard deviations, confidence intervals, or significance tests. This makes it impossible to assess whether the 0.5% ASR gap is statistically meaningful, whether the TTS parity with SpeechFlow is within noise, or whether the tokenization margins are robust. While single-run evaluation is common practice in large-scale speech pre-training, the paper draws comparative conclusions that require some uncertainty quantification.

### Minor

- **ASR framing overstates "comparable"**: The abstract and introduction claim "comparable performance" to task-specific models on ASR. The actual gap is ~0.5% absolute WER on test-other (~15–20% relative degradation vs. HuBERT/WavLM), which is meaningful in ASR literature where 0.1–0.2% gaps are taken seriously. The paper does acknowledge this in the results section ("falls short... by around 0.5% WER") and limitations, but the main messaging uses "comparable" without this caveat, which could mislead readers.

- **Mutual information estimation methodology is underspecified**: The paper computes empirical MI between quantized representations (1024 codebook entries) and labels (~40 phones, ~251 speakers) by tabulating P(unit), P(label), and P(unit, label). With a finite sample from the dev set, most of the 1024 × ~40 = ~40,960 bins will have zero counts, which biases raw plug-in MI estimates upward in a way that depends on sample size. The paper does not discuss this known issue or use a standard correction (e.g., shuffling-based estimation, shrinkage estimators). This does not necessarily invalidate the qualitative trends but weakens confidence in the exact comparisons to HuBERT.

- **Potential claim inconsistency at 500 bps**: The paper states "At 500 bps, UniWav leads in all metrics by a margin, outperforming all other methods" (Section 3.4), but at least one reviewer identified that UniWav's speaker similarity at 500 bps (0.493) is *lower* than HuBERT-Large unit-HiFiGAN (0.510). The specific table values cannot be independently verified from the parsed text (the table is an image), but if this is accurate, the "leads in all metrics" claim is factually incorrect and should be qualified. The authors should clarify this in revision.

### Trivial

- The claim in Section 2.3 that self-distillation without clustering was "less stable" is stated without any quantitative support. While this is a minor design note, a brief comparison would strengthen confidence.

## Nice-to-Haves

- **Discussion of EnCodec dependency**: UniWav uses a pre-trained, fixed EnCodec encoder for input features and EnCodec decoder for waveform reconstruction. This means UniWav cannot generate speech independently — it is a codec-conditioned generative model. Acknowledging this as a design trade-off (rather than a hidden limitation) would improve transparency. The appendix apparently studies mel spectrogram as an alternative, which is good.
- **Evaluation on more diverse domains**: The paper focuses on English audiobook speech (LibriSpeech/LibriLight). Testing on spontaneous speech, multiple languages, or noise conditions would strengthen claims about generality. The paper acknowledges this as future work.
- **Force-aligned phones as conditioning**: The TTS evaluation uses oracle phone alignments from a force aligner, which simplifies acoustic modeling. The paper applies this consistently to all methods, so comparisons are fair, but the absolute numbers (ASR-WER ~2%) reflect this simplified setting and should not be compared to TTS systems that do not use oracle alignments.

## Removed Points

These points were flagged for removal and should be treated with caution:

- "First attempt claim is too broad" — The paper explicitly qualifies this as "first unified *pre-training* framework for both types of tasks" and distinguishes cascaded systems (Polyak et al., Zhang et al.) as separate lines of work. The criticism conflates cascaded pipelines with end-to-end joint pre-training.
- "Observation #1 is contradictory" — The critic compares UniWav vs. HuBERT (cross-model, Table 1) and claims it contradicts the internal ablation (UniWav with vs. without decoder, Table 3). These are different comparisons; the internal ablation's finding (decoder helps with 24-layer encoder) is internally consistent and not contradicted by the cross-model comparison.
- "Self-distillation without clustering comparison missing from appendix" — The paper states this as a minor design observation from experience. Per guidelines, appendix content may exist in the original submission and cannot be verified. The core point (lack of quantitative evidence) is real but trivial.
- "ViSQOL numbers are N/A" — Cannot be verified from the parsed text (table is an image).
- "Force-aligned phones not acknowledged" — The paper *does* explicitly state "we use Montreal Force Aligner to obtain alignment for both training and evaluation (and apply the same for prior works that require alignment)."

## Novel Insights

An interesting tension emerges across the reviewer inputs and the paper's own data: the framework's success on tokenization (its strongest result) may actually stem more from the decoder pre-training than from the joint encoder–decoder training that the paper emphasizes. Meanwhile, the ASR results confirm that the encoder pays a measurable price for the generative objective (~0.5% WER), and the TTS results show no gain over a generation-only pre-training baseline. This paints a nuanced picture: the unified framework is *feasible* and practically useful (especially for tokenization), but the claimed synergy between the two objectives is not yet convincingly demonstrated — the evidence is equally consistent with the decoder simply benefiting from its own pre-training while the encoder does its best despite the added objective. The scaling analysis partially addresses this (decoder helps encoder only at sufficient encoder capacity) but does not extend to the tokenization setting. A clean ablation controlling for decoder pre-training would be the single highest-impact addition the authors could make.

## Suggestions

1. **Add the critical ablation**: Pre-train a decoder (same architecture, same flow-matching objective) on *fixed, frozen* HuBERT-Large representations (or on representations from a UniWav encoder pre-trained without decoder loss) for 600k steps, then fine-tune for tokenization at 500 bps. Compare to UniWav's tokenization result. This will disentangle whether the tokenization advantage comes from joint training or from having a pre-trained decoder. This is the single most important experiment missing from the paper.

2. **Reframe the ASR claim**: Change "comparable performance" (abstract, introduction) to something like "competitive performance within 0.5% WER of specialized models" — this is more precise and aligns with what the limitations section already acknowledges.

3. **Report confidence intervals or variability**: For at least the main results (Tables 1–2), report standard deviations across multiple evaluation runs or bootstrap confidence intervals. This is especially important given the suspicious exact parity with SpeechFlow on TTS metrics.

4. **Clarify the 500 bps speaker similarity claim**: If UniWav's speaker similarity at 500 bps is indeed lower than HuBERT-Large unit-HiFiGAN, correct the "leads in all metrics" statement. If the critic's numbers are wrong, provide the correct comparison explicitly.

5. **Improve MI estimation**: Use a standard bias-corrected MI estimator (e.g., shuffling-based baseline or quadratic shrinkage) rather than raw plug-in estimates, or at minimum discuss the sparsity issue and its impact on the reported values.

6. **Add analysis of why the decoder helps at 24 encoder layers but hurts at 6 layers**: An analysis of gradient flow, representational similarity (CKA), or gradient norms between encoder and decoder during pre-training could illuminate this interesting finding.

## Score and Decision

UniWav makes a genuine contribution by demonstrating that a single end-to-end pre-trained encoder-decoder can serve both discriminative and generative speech tasks. The tokenization results are empirically strong, the scaling analysis provides actionable insights, and the MI analysis offers useful interpretability. However, the central attribution claim — that joint training is the source of the tokenization advantage — is not adequately supported due to the decoder pre-training confound. The ASR framing is also somewhat overstated. These are fixable issues, and the paper's core technical contribution (the framework itself) is solid.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>