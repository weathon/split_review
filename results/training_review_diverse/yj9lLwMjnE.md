Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes UniWav, an encoder-decoder framework for unified pre-training of speech representations. The encoder uses self-distillation with online clustering (DinoSR) and the decoder uses Flow Matching, trained jointly from scratch on 60k hours of LibriLight. The same pre-trained model is fine-tuned for ASR, in-context TTS, and speech tokenization — achieving competitive results on all three tasks. The scaling analysis reveals that generative pre-training benefits discriminative representations only when the encoder is sufficiently large, a non-obvious insight.

## Strengths

1. **First unified pre-training framework for speech representation learning and generation.** The paper delivers on its central claim: a single pre-trained model that can be fine-tuned for both ASR and TTS/ tokenization, where prior foundation models were task-specific. This is demonstrated concretely in Table 1 (ASR + TTS from same model) and Table 2 (tokenization).

2. **Competitive performance on both ASR and TTS from the same pre-trained model.** On LibriSpeech test-other, UniWav achieves 6.9% WER (960h fine-tuning), within ~0.5% of task-specific SOTA models like WavLM. For TTS, it matches SpeechFlow on ASR-WER (2.1) and speaker similarity (0.675), while SpeechFlow cannot do ASR. This shows unification does not catastrophically degrade either capability.

3. **State-of-the-art low-bitrate speech tokenization.** At 500 bps, UniWav leads all four baselines across ASR-WER, UTMOS, and speaker similarity. At 1 kbps, it achieves 5.6% ASR-WER and 3.72 UTMOS vs. SpeechTokenizer's 9.1% and 2.08 (Table 2). The discrete bottleneck method (Eq. 11) is a principled adaptation that leverages both semantic and residual layers.

4. **Scaling analysis reveals a non-trivial interaction between generative and discriminative objectives.** Table 3 shows that with a small encoder (depth 12), adding the decoder hurts ASR (17.4% → 18.0%), but with a large encoder (depth 48), the decoder helps (16.6% → 16.2%). This is a genuine insight for future unified modeling work, supported by controlled experiments.

5. **Mutual information analysis provides a principled explanation for UniWav's behavior.** Figure 2 shows UniWav preserves lower phone-MI in later layers than HuBERT (explaining the small ASR gap) but higher speaker-MI across most layers (explaining strong generation/resynthesis performance). This ties design choices to task outcomes and suggests directions for disentanglement research.

6. **Ablation of design alternatives validates the final configuration.** Section 2.3 reports that alternative encoder objectives (self-distillation without clustering, distilling from pre-trained HuBERT) and decoder choices (EnCodec reconstruction instead of Flow Matching) were empirically inferior. These negative results strengthen the paper by showing the chosen combination is justified.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Data-scale confound partially affects tokenization comparisons with SpeechTokenizer.** UniWav is pre-trained on LibriLight (60k hours) before tokenization fine-tuning, while SpeechTokenizer (the strongest tokenization baseline) is trained only on LibriSpeech (960h). The paper mitigates this by including unit-HiFiGAN with HuBERT-LARGE (also pre-trained on LibriLight, §3.4), which closes the gap for that baseline. However, the margin over SpeechTokenizer at 1kbps (5.6% vs. 9.1% ASR-WER; UTMOS 3.72 vs. 2.08) may partly reflect pre-training data scale rather than architectural advantage alone. The authors should either (a) pre-train a smaller UniWav on 960h for a controlled comparison, or (b) note this confound more explicitly in the tokenization section.

2. **Missing ablation for TTS: joint vs. separate pre-training.** For ASR, Table 3's decoder-depth=0 condition provides the relevant comparison (encoder-only pre-training → fine-tune). For TTS, however, the paper does not compare the current joint-training pipeline against the alternative of: (a) pre-training the encoder alone with DinoSR, (b) freezing it, and (c) training the decoder on the frozen representations with Flow Matching. This would directly test whether joint training benefits generation, or whether sequential training suffices. The scaling experiments in Table 4 hint at the answer but do not isolate this specific question.

3. **No error bars or variance reported.** The ASR gap to SOTA is ~0.5% WER, and TTS similarity differences are as small as 0.01. Without standard deviations across multiple fine-tuning runs (at least 3), the reader cannot judge whether these differences are meaningful. This is standard practice in the SSL/ASR literature and would substantially increase confidence.

4. **TTS evaluation uses forced alignment for all models, but original protocols differ among baselines.** The paper states it applies forced alignment "for prior works that require alignment." While this is transparent, VALL-E and Voicebox were originally evaluated with their own conditioning setups. The paper does not confirm that the re-implemented baselines achieve their reported numbers under this protocol. A brief verification that reproduced values match published ranges would strengthen confidence.

### Trivial

1. Only test-other WER is reported for ASR (Table 1). Including test-clean and dev results would enable more granular comparison without adding length.
2. No human evaluation (MOS) for TTS quality. ASR-WER and speaker similarity are standard proxies but UTMOS (already used for tokenization) could be applied to TTS outputs for a fuller picture.
3. The mutual information analysis (§3.5) uses quantized representations (k-means on encoder features), while HuBERT MI analysis in prior work uses raw representations. The paper should note this methodological difference explicitly in the text when comparing MI curves in Figure 2.

## Nice-to-Haves

- Reporting inference latency or FLOPs for the unified model vs. separate task-specific models would help assess the practical value of unification.
- An ablation of the input feature choice (EnCodec latent vs. mel spectrogram) on both ASR and TTS would strengthen claims about generality (Appendix A.1 is referenced but its contents were not visible in the provided text).
- Sensitivity analysis over the semantic layer index *i* in the tokenization method (Eq. 11) would show whether the mutual-information-based selection is robust to the discrete bottleneck introduced during fine-tuning.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Data scale confound in ASR: the table appears to list only the 960h versions for prior work"** — The paper's text states it "falls short of state-of-the-art by around 0.5% WER." It does not claim these are only 960h models. WavLM (trained on 94k hours, more than UniWav) appears to be the SOTA reference. The critic's specific claim about table contents is unverifiable and the available evidence contradicts it. **Removed as factually uncertain / partially incorrect.**

2. **"The ~0.5% WER gap to HuBERT-Large (which also uses LibriLight)"** — The paper does not specify HuBERT-Large as the SOTA comparator for ASR. The gap could be to WavLM (94k hours), which would be a conservative comparison favoring the baseline. **Removed as unsupported by the paper text.**

3. **"decoder depth=0 is not a separate pre-training baseline"** — Decoder depth=0 in Table 3 literally means "the corresponding training objective was ignored" (§3.5), i.e., encoder-only pre-training followed by ASR fine-tuning. This is precisely the separate pre-training baseline for ASR. **Removed as a misunderstanding.**

4. **"Using alignment may inflate UniWav's performance while degrading baselines"** — The paper applies alignment to "prior works that require alignment" (§3.3). VALL-E and Voicebox use phone-level alignments in their original formulations. The critic provides no evidence that alignment degrades their performance. **Removed as speculative.**

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel synthesis: the scaling analysis (Tables 3–4) implies that whether unification helps depends critically on encoder capacity — a small encoder cannot simultaneously serve both objectives, but a large encoder benefits from the generative signal. This pattern mirrors findings in vision (Li et al., 2023, cited by the paper) and suggests a "critical capacity threshold" hypothesis for multi-objective pre-training that future work could formalize. No other insight from the reviews goes beyond what the paper already argues.

## Suggestions

1. Add standard deviations (≥3 runs) to the main results in Tables 1 and 2, especially for the close comparisons (ASR WER, TTS similarity). This is the single highest-impact fix.
2. Add the joint-vs.-separate ablation for TTS: pre-train encoder alone (DinoSR, no decoder), freeze it, train decoder on frozen representations with Flow Matching, then compare to the joint-trained model. This cleanly tests the benefit of unification for generation.
3. For the tokenization comparison, either train a smaller UniWav on 960h (for direct comparison with SpeechTokenizer) or add an explicit caveat about pre-training data scale.
4. Include test-clean WER in Table 1 and UTMOS for TTS outputs.
5. Add a brief verification that reproduced VALL-E/Voicebox TTS numbers under the forced-alignment protocol are consistent with published ranges.

## Score and Decision

The paper tackles an important and timely problem. The core idea is novel, the method is sound, and the scaling analysis provides genuine insight. No fatal or major weaknesses threaten the core claims. The three verified weaknesses (partial data-scale confound in one tokenization comparison, missing TTS ablation, absence of error bars) are clearly fixable and do not undermine the main contribution: that a single unified pre-training framework can work well across discriminative and generative tasks. The paper honestly acknowledges its limitations and does not overclaim.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>