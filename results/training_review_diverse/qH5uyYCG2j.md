Now I will write the final consolidated review.

## Summary

This paper proposes a two-stage controllable text-to-speech system that uses a masked autoencoder (MAE) to learn a discrete, content-disentangled style representation. The first stage is an autoregressive transformer (style LM) that generates style tokens conditioned on phonemes and discrete control labels (pitch, emotion, age, gender, SNR, etc.), trained on large-scale data (GigaSpeech-xl, ~10k hours). The second stage (acoustic LM) generates codec tokens from phonemes and style tokens, trained on high-quality but smaller data (LibriTTS, ~500h). The system supports both fully discrete-label-based control and control with a reference speaker embedding. Classifier-free guidance (CFG) is applied to the style token generation to improve control accuracy for fine-grained attributes.

## Strengths

- **Two-stage architecture enables data scaling for style modeling.** Figure 3 shows a clear and significant advantage: the two-stage model maintains stable WER (~5–10%) and UTMOS (~3.5–4.0) across increasing CFG scales on in-domain and out-of-domain test sets, while the one-stage baseline (trained on LibriTTS only) degrades sharply. This validates the core system-level claim that separating style generation (trainable on large, diverse data) from acoustic generation (needing high-quality data) improves robustness.

- **Fine-grained control via discrete labels with CFG is effective.** Figure 4 demonstrates that CFG substantially improves control accuracy for fine-grained attributes (pitch std, age) from below 60% to over 80% on several test sets. Figure 5 shows the two-stage model outperforms the one-stage baseline on emotion attributes (arousal, dominance, valence) by 10–20 percentage points across all three test sets. These results support the paper's claim about precise attribute control.

- **Flexible control combining speaker embedding with discrete labels is demonstrated.** Table 3 shows that when using a reference speaker embedding together with pitch and emotion labels, the two-stage model achieves speaker similarity (0.82–0.86 cosine) comparable to the discrete-label-only setting while maintaining high control accuracy (e.g., 88.83% for arousal on GigaSpeech). This demonstrates a practically useful capability.

- **The MAE-based style representation captures rich style information.** Table 2 shows that reconstruction with ground-truth style tokens achieves substantially lower MCD than zero-shot TTS systems (5.59 vs. 7.94 on LibriTTS), confirming that the style tokens encode fine-grained prosodic and acoustic detail beyond speaker identity. The spectrograms in Figure 2 visually support this.

## Weaknesses

### Fatal
None.

### Major

- **The one-stage vs. two-stage comparison is confounded by training data scale.** The one-stage baseline is trained on LibriTTS (~500h), while the two-stage model's style LM is trained on GigaSpeech-xl (~10k hours) — a 20× difference. The paper attributes the two-stage model's superior content accuracy and robustness under CFG to the two-stage design, but the massive data disparity is a far more plausible explanation for much of the observed gap. A clean ablation (training both models on the same data, e.g., training the two-stage style LM on LibriTTS or training the one-stage model on GigaSpeech) is needed to isolate the architectural contribution from the data-scale contribution. This is the paper's central experimental claim, and the confound undermines its support.

- **No experimental comparison to existing controllable TTS systems.** The paper evaluates control accuracy only against its own one-stage baseline. Several published systems (PromptTTS, TextrolSpeech, InstructTTS, PromptTTS 2) also target style control, and TextrolSpeech uses an interface (discrete labels) that is directly comparable. Without any external comparison on shared metrics (UTMOS, WER, or control accuracy on a common test set), the significance of the proposed system's performance relative to prior art cannot be assessed. This is a critical omission that limits the paper's contribution claim.

- **The correlation-handling methods (Section 4.4) are not validated in the TTS pipeline.** The paper identifies the important problem of correlated labels and proposes both statistical sampling and MLP-based prediction to resolve conflicts. However, these methods are never integrated into the main TTS pipeline or evaluated for their effect on control accuracy, WER, or naturalness. As presented, they remain suggestions rather than demonstrated components of the system.

### Minor

- **The swap test reasoning is not airtight.** The paper claims that the failure of cross-sample phoneme/style-token swapping "demonstrates that our style representation does not result in significant content information leakage." However, if style tokens were fully content-disentangled, the model *should* be able to synthesize speech from any phoneme/style pair. The failure is equally consistent with content leakage OR with the style tokens encoding utterance-level prosodic structure (timing, rhythm) that is inherently tied to specific content. The paper should either provide a quantitative disentanglement metric (e.g., WER when decoding from style tokens alone) or soften the claim.

- **No human evaluation.** All reported metrics are objective (UTMOS, WER, speaker cosine similarity, MCD, label accuracy). For a controllability claim, human listening tests (e.g., AB preference on attribute control or naturalness) are standard practice in the TTS community and would significantly strengthen the paper's evidence. The demo page is a helpful supplement but does not replace formal subjective evaluation.

- **The one-bin tolerance for control accuracy should be supplemented with raw accuracy.** The paper relaxes control accuracy to include predictions within one bin of the target. While this relaxation is reasonable, the raw bin-level accuracy should also be reported to allow readers to gauge the difficulty of the control task and the model's precision.

### Trivial
None.

## Nice-to-Haves

- An analysis or discussion of the effect of phone-level merging on sub-phoneme prosodic detail (e.g., micro-variation in pitch within a phoneme). The paper acknowledges the design choice but does not discuss its possible limitations.
- A simple random or majority-class baseline to contextualize control accuracy numbers.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Zero-shot TTS comparison for reconstruction is unfair"** — The purpose of this comparison is to show that style tokens capture richer information than speaker embeddings alone (which is informative and expected given the proposed method has access to ground-truth style features). The comparison is informative for its stated goal and does not constitute a methodological error. The codec compression row is also present in Table 2, contrary to the claim that it is "not discussed."
- **"One-bin tolerance hides poor performance"** — The relaxation is standard practice for fine-grained control and is transparently stated. Requesting raw accuracy is reasonable but does not rise to a weakness.
- **"Phone-level merging discards sub-phoneme prosodic detail"** — This is a design choice, not a flaw. The reconstruction results demonstrate that this level of granularity is sufficient for the paper's goals.
- **"No random baseline for control accuracy"** — A minor wishlist item that would not change the paper's conclusions.
- **"The paper overstates the data issue as unique to natural-language interfaces"** — The paper does not claim uniqueness; it motivates the issue and proposes a specific solution. This is an opinion, not a weakness.

## Novel Insights

The harsh critic's observation about the swap test being inconclusive rather than supportive is a useful methodological caution, but the more interesting insight from the reviews is the tension between the paper's two main claims: the two-stage architecture enables data scaling (which is real), versus the claim that the architecture itself is responsible for the quality improvement (which is confounded). The most novel observation from the review process is that the paper's central strength — the data-scaling advantage — is simultaneously its core methodological weakness in terms of experimental rigor. Addressing this tension (e.g., by adding a controlled ablation) would significantly strengthen the paper.

## Suggestions

1. **Unconfound the one-stage vs. two-stage comparison** by training at least one of the following: (a) the one-stage baseline on a similarly large dataset (GigaSpeech-xl), or (b) the two-stage model's style LM on LibriTTS (same data as the one-stage baseline). This would isolate the architectural contribution from the data-scale contribution.
2. **Include at least one external baseline** (e.g., TextrolSpeech or PromptTTS 2) on a shared evaluation set using the same metrics. Even if the proposed method only equals or slightly outperforms on a subset of attributes, this would contextualize the contribution.
3. **Integrate the correlation-handling methods** (Section 4.4) into the main TTS pipeline and report results with and without conflict resolution. Demonstrate that using predicted pitch labels from the MLP improves control accuracy or WER.
4. **Quantify content-disentanglement** directly (e.g., WER of a recognizer on reconstructions from style tokens alone, or mutual information between style tokens and phoneme transcriptions).
5. **Add human evaluation** — at minimum an AB preference test for naturalness and a controllability rating task — to complement the objective metrics.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>