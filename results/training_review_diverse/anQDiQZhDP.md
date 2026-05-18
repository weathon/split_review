Now I have all the information I need. Let me construct the final review.

## Summary

Vevo proposes a unified, zero-shot voice imitation framework that decouples timbre, style, and linguistic content by using VQ-VAE vocabulary size as a controllable information bottleneck applied to HuBERT features. A two-stage pipeline — autoregressive transformer for content→content-style modeling and flow-matching transformer for content-style→acoustic — enables controllable timbre, style, and voice imitation from a single set of pre-trained models. Trained on 60K hours of audiobook data without style-specific fine-tuning, Vevo matches or exceeds existing methods on accent and emotion conversion, voice conversion, and TTS tasks.

## Strengths

- **Novel progressive disentanglement via VQ-VAE vocabulary size.** The paper introduces a clean idea: treat the codebook size K as an information bottleneck and empirically demonstrates that reducing K filters timbre first (K=4096 → content-style tokens) and then style (K=32 → content tokens), all without labels. Table 2 provides systematic evidence: S-SIM to source drops from 0.306 (K=16384) to 0.236 (K=4096), and FPC drops from 0.797 to 0.706 when reducing from 4096 to 32, while WER stays low until K<16. This is a well-executed analysis that directly supports the design.

- **Unified zero-shot framework with strong style imitation results.** Vevo matches or surpasses existing methods in zero-shot accent and emotion conversion despite never being fine-tuned on style-specific corpora. In Table 4, Vevo-Style outperforms all baselines (ASR-AC, VoiceShop, Conv-Speak, Emovox) on every reported metric — e.g., A-ACC 83.3 vs. 72.4 (best baseline), E-ACC 73.2 vs. 56.8. This demonstrates genuine zero-shot generalization from neutral audiobook data to expressive domains.

- **Controllable attribute imitation from the same pre-trained models by varying inference pipeline.** Four variants (Vevo-Timbre, Vevo-Style, Vevo-Voice, Vevo-TTS) share the same M_style and M_acoustic models, differing only in tokenizers and references during inference (Section 3.4). Table 3 shows Vevo-Timbre preserves source style (PS-MOS 4.12) while Vevo-Voice achieves both high accent and emotion similarity (AS-MOS 4.02, ES-MOS 3.98), demonstrating independent control of timbre and style.

- **Rigorous empirical analysis of the design space.** Section 4.1 provides a thorough ablation across vocabulary sizes (8 to 16384) and compares VQ-VAE tokens against HuBERT continuous features, K-means tokens, ASR tokens, and PPG features (K-means at K=1024 yields WER 6.6 vs. VQ-VAE 3.7), validating the choice of VQ-VAE over prior quantization approaches.

- **Practical efficiency contributions.** Duration reduction (merging consecutive duplicate units) improves duration conversion (DDUR 0.70 vs. 0.80) while shortening input sequences. The reference-global-guided continuation mode reduces input length to 42% with only 0.1–0.2 drop in similarity metrics (Table 6), offering a practical speed/quality trade-off.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Timbre preservation in style imitation is not directly evaluated.** The paper defines style imitation (Vevo-Style) as preserving the source's timbre while imitating the reference's style. However, Table 4 reports only accent/emotion similarity and intelligibility — it does not report S-SIM to source or any subjective speaker-preservation score for Vevo-Style generations. Table 2 shows that content-style tokens (K=4096) retain some timbre information (S-SIM to source = 0.236), and without measuring speaker similarity between the source and the Vevo-Style output, it is difficult to verify that timbre is truly preserved rather than contaminated by the style reference. While the paper's design (using the source as timbre reference in the acoustic model) provides theoretical grounding, direct empirical evidence would strengthen the controllability claim.

- **Style imitation comparison (Table 4) relies on demo website samples.** The paper transparently states it uses baseline demo samples as the evaluation set. This introduces potential selection bias (baselines showcase their best results) and limits reproducibility. While the zero-shot capability is demonstrated by the approach itself, the comparative claims of state-of-the-art performance would be more persuasive with a controlled experiment on a fixed, publicly available test set (e.g., Expresso or Audiobox subsets) where all systems are evaluated under identical conditions.

- **"Self-supervised" framing is slightly overstated for the TTS variant.** The core framework (VQ-VAE, speech-to-speech M_style, M_acoustic) is indeed self-supervised. However, the abstract states "Solely self-supervised trained on 60K hours," and the Vevo-TTS variant requires ASR-transcribed audiobooks for the text-to-content-style model. The paper acknowledges this in Section 4 (training data uses ASR transcriptions), but the abstract and conclusion language could more precisely delineate which components are self-supervised and which use transcription supervision.

- **Global style encoder training signal is underspecified.** The paper describes the global style encoder as "WavLM-based representation layers and TDNN-based feature extraction layers" and includes its output g(u) in the transformer input sequence. However, it is not explicitly stated whether the encoder is jointly trained with the AR transformer via the next-token prediction loss, or trained separately. This detail matters for reproducibility.

### Trivial

- **No confidence intervals reported for objective metrics.** Evaluation sets are modest (700 samples total, with subsets of 150–200). While single-run evaluation is common in large-scale speech benchmarks, reporting standard deviations or significance tests for key metrics (WER, S-SIM) would strengthen the results.

- **The content token trade-off is acknowledged but could be discussed more.** The paper states "such Kc and Ks may not be optimal" and speculates that residual style information in Q_c may limit style imitation (Section 4.3). This is honest but the paper could expand on whether residual style information in content tokens might reduce the model's ability to accept style from the reference.

## Nice-to-Haves

- A controlled listening test for style imitation on a fixed set (e.g., Expresso + accented data) with MOS and confidence intervals.
- S-SIM to source for Vevo-Style generations to directly verify timbre preservation.
- An ablation varying K_s (e.g., 2048, 4096, 8192) and measuring the timbre/style trade-off in style imitation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Subjective evaluation methodology is critically underspecified.** *Reason for removal:* The paper provides no details about number of listeners, confidence intervals, or test protocol for MOS evaluations. However, per the hard rule about parser-stripped content (appendices containing supplementary methodological details are stripped from all papers), these details plausibly exist in the original submission and may be restored upon publication.

- **Table 3 confusion about EMOTION-specific metrics.** *Reason for removal:* The paper's table caption already clarifies which metrics are evaluated on which subsets ("PS-MOS, E-SIM, and ES-MOS are evaluated only on EMOTION. A-SIM and AS-MOS are evaluated only on ACCENT"). The reviewer's concern is addressed by the existing text.

## Novel Insights

The key insight that emerges from this review is that the paper's contribution is strongest in its *design principle* (vocabulary size as a progressive information bottleneck) and weakest in the *evaluation of targeted attribute control*. The progressive filtering story is well-told and empirically supported for the tokenizer stage, but the downstream verification of controlled generation — particularly the claim that timbre is preserved in style imitation — relies on architectural reasoning rather than direct measurement. This gap is common in the disentanglement literature, but the paper would be significantly strengthened by closing it. Additionally, the demo-sample-based style imitation comparison, while practically motivated, means the paper's most impressive comparative claims (zero-shot style imitation beating task-specific models) rest on weaker empirical ground than the voice conversion and TTS results, which use a fixed test set.

## Suggestions

1. Add S-SIM to source for Vevo-Style generations (Table 4) to directly verify timbre preservation.
2. For a stronger version, conduct a controlled style imitation evaluation on a fixed test set (e.g., Expresso for emotion, accented Audiobox subset) with at least one open-source baseline.
3. Reframe the abstract to clarify that the core disentanglement and speech-to-speech components are self-supervised, while the TTS variant additionally uses ASR transcriptions.
4. Explicitly state whether the global style encoder is jointly trained with the AR transformer and what loss signal reaches it.
5. Add confidence intervals or significance markers for key objective and subjective metrics.

## Score and Decision

This paper presents a well-motivated and novel approach to controllable voice imitation, with clean design and extensive experiments. The core idea — using VQ-VAE vocabulary size as a progressive information bottleneck — is original and well-validated. The weaknesses are addressable and do not undermine the central contribution. I recommend acceptance.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>