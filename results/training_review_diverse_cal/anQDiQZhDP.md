Now I have a comprehensive understanding of the paper. Let me produce the final consolidated review.

---

## Summary

Vevo proposes a fully self-supervised framework for zero-shot voice imitation with controllable timbre and style. Its core idea is to use the vocabulary size of a VQ-VAE applied to HuBERT features as a progressive information bottleneck: at K=4096, timbre is filtered out (yielding "content-style" tokens), and at K=32, most style information is also filtered (yielding "content" tokens). These tokens feed a two-stage pipeline — an autoregressive transformer for content-to-content-style modeling (prompted by a style reference) and a flow-matching transformer for content-style-to-acoustic modeling (prompted by a timbre reference) — enabling timbre, style, and voice imitation from a single pretrained framework.

## Strengths

1. **Novel self-supervised disentanglement via VQ-VAE vocabulary size.** The idea of using codebook vocabulary size as a tunable information bottleneck to progressively discard timbre → style → content is conceptually clean and well-executed. Table 2 provides a systematic analysis showing that at K=4096, S-SIM to source drops to 0.236 (timbre filtered) while FPC stays at 0.797 (style retained), and at K=32, FPC drops to 0.706 (style also filtered), with WER rising only modestly to 6.6. This is direct evidence of progressive filtering, not merely indirect.

2. **Zero-shot style imitation surpassing supervised baselines.** Vevo-Style, trained only on 60K hours of neutral audiobook data without any style-specific annotation or fine-tuning, achieves higher accent accuracy (91.2% vs. ~80–85%) and emotion accuracy (90.3% vs. 85.1%) than supervised baselines that rely on parallel corpora or style labels (Table 4). This is the paper's most striking result and demonstrates a genuinely new capability.

3. **Unified framework covering multiple tasks from a single pretrained model.** The same pretrained modules (M_style and M_acoustic) handle timbre imitation, style imitation, voice conversion, and zero-shot TTS through different inference pipelines (Section 3.4). This versatility is a direct product of the disentangled token design.

4. **Duration reduction is both principled and practical.** Merging consecutive duplicate content tokens further strips unit-level duration cues (a style signal) and reduces input sequence length to 42% with minimal performance degradation (Table 6). This design insight cleanly serves both disentanglement and efficiency.

5. **Systematic comparison of HuBERT representations and quantization methods.** Table 2 compares HuBERT continuous features, K-means, VQ-VAE at multiple vocabulary sizes, PPG features, and ASR tokens under controlled conditions, providing a clear methodological guide for future work.

## Weaknesses

### Fatal
None.

### Major

1. **Unclear baseline evaluation methodology for Tables 3 and 5.** The paper states for Table 3 that "We selected several SOTA baselines… We used the same evaluation samples as in Section 4.1" but does not specify whether the baseline systems were re-run on those exact 700 samples using the same metric pipelines, or whether published numbers are quoted. For Table 5, the comparison with Voicebox is controlled (same training data), but comparisons with CosyVoice and MaskGCT lack similar detail. Without knowing whether metrics (WER via Whisper, S-SIM via WavLM, etc.) were computed uniformly across all systems, the reader cannot assess whether the claimed advantages are genuine or reflect differences in evaluation conditions. This is not a fatal flaw — the paper's core technical contributions (disentanglement method, unified framework) stand independently — but it weakens the SOTA claims that the paper emphasizes. The authors should clearly state the evaluation protocol for all baselines or re-run them under common conditions. *(Note: Table 4 explicitly describes using demo website samples, so this concern applies primarily to Tables 3 and 5.)*

### Minor

1. **Text-to-token mapping for Vevo-TTS is not described.** The paper introduces $\widetilde{Q_c}(\mathcal{T}_i)$ and $\widetilde{\mathcal{M}}_{style}$ for the text-input variant but never explains how text is converted to content tokens (phoneme tokenizer? grapheme? cross-attention with a language model?). This is a significant omission for the TTS application, which is one of the four tasks claimed.

2. **Training details of the global style encoder are underspecified.** The paper notes it uses "WavLM-based representation layers and TDNN-based feature extraction layers" and shows that $g(u)$ is included in the AR transformer input, but it does not explicitly state whether the style encoder is trained jointly with the AR transformer, pretrained separately, or frozen. This matters for understanding the source of style disentanglement.

3. **The WER comparison text in Section 4.4 contradicts the data.** The paper states "Vevo-TTS, while showing slightly inferior performance in WER (which is a common weakness for AR models), excels across all other metrics" when comparing to Voicebox. However, the reported numbers show Vevo-TTS achieves *better* WER than Voicebox on both ACCENT (4.3 vs. 5.3) and EMOTION (2.6 vs. 3.9). The "slightly inferior" characterization appears to refer to CosyVoice/MaskGCT, but the sentence structure ties it to the Voicebox comparison, creating a factual inconsistency.

4. **Disentanglement evidence, while direct for timbre, is less complete for style-style interactions.** Table 2 convincingly shows timbre is filtered at K=4096 and style is partly filtered at K=32, but the paper does not directly measure whether content-style tokens (K=4096) and content tokens (K=32) can be used in a simple reconstruction task to verify that swapping tokens transfers only the intended attribute. The downstream results are supportive but do not fully isolate the token representation from the modeling stages' capacity.

### Trivial

1. **No confidence intervals for subjective MOS scores.** MOS and CMOS scores are reported as single numbers without error bars, making it unclear whether differences (e.g., N-MOS 4.13 vs. 3.91 in Table 3) are significant. This is a common issue in the field but worth noting.

2. **No dedicated limitations discussion.** The paper would benefit from acknowledging that audiobook data is primarily read speech with limited prosodic diversity, or discussing potential failure cases and computational costs.

## Nice-to-Haves

- **Direct token-level classifiers:** Training accent/emotion/speaker classifiers on the discrete tokens themselves (rather than on downstream model outputs) would further strengthen the disentanglement claim by measuring attribute separation directly in the token space.
- **Full-pipeline tokenizer ablation:** While Table 2 compares tokenizers within the acoustic model, ablating the tokenizer choice (VQ-VAE at K=4096 vs. K=32 vs. K-means vs. ASR tokens) through the *full* AR+flow-matching pipeline would isolate the token contribution more cleanly from the model architecture. (Note: the paper already includes a partial ablation via Vevo-Style vs. Vevo-Style (ASR) in Table 4.)
- **Reproducibility table:** A dedicated hyperparameter table covering the style encoder, text tokenization, and data split details would improve reproducibility.

## Removed Points

Several criticisms from the harsh reviewer are removed or downgraded after cross-checking:

- **"Disentanglement claim supported only by indirect evidence"** — The paper shows *direct* evidence in Table 2: different K values produce measurable differences in S-SIM (timbre), FPC (style), and WER (content) when used in the *same* downstream model. This directly measures what information passes through the bottleneck, not merely indirectly.
- **"Missing ablation isolating tokenizer contribution"** — Partially addressed by Vevo-Style vs. Vevo-Style (ASR) comparison in Table 4 and the systematic tokenizer comparison in Table 2. The remaining gap (full-pipeline ablation) is downgraded to Nice-to-Have.
- **"Global style encoder not clearly described — could be doing all the work"** — The paper shows the style encoder output $g(u)$ is just one input among many in a sequence-to-sequence AR model that predicts content-style tokens from content tokens. The encoder is a small component, not an alternative source of disentanglement.
- **"Potential unfair comparison" framing** — The concern is about *clarity* of methodology, not about unfair bias toward the author's method.

## Novel Insights

The strongest meta-insight from this set of reviews is that the paper's most impressive result (zero-shot style imitation surpassing supervised methods) also rests on the cleanest evaluation methodology (demo website samples, explicit per-group comparisons). The weaker methodological documentation for Tables 3 and 5 creates an unfortunate asymmetry where the paper's boldest claims are backed by its least transparent comparisons. The authors would substantially strengthen the paper by bringing the evaluation rigor of Section 4.3 (style imitation) to the other sections.

## Suggestions

1. **Clarify baseline evaluation protocol**: For each baseline in Tables 3 and 5, state explicitly whether results were obtained by running the baseline code on your test set, using the baseline's demo outputs, or quoting published numbers. If quoted, note the differing evaluation contexts.
2. **Re-evaluate style encoder description**: State explicitly whether the global style encoder is trained jointly with the AR transformer, and if its parameters are updated during training or frozen.
3. **Describe text tokenization**: Even briefly — e.g., "we use a grapheme-to-phoneme converter followed by the content tokenizer's encoder" or "we finetune a text encoder jointly with M_style."
4. **Correct the WER text**: In Section 4.4, rephrase to clarify that Vevo-TTS achieves better WER than Voicebox but trails CosyVoice/MaskGCT.
5. **Add confidence intervals**: For key MOS and CMOS comparisons where differences are small.

## Score and Decision

The paper presents a genuinely novel approach to self-supervised speech disentanglement and a well-engineered unified framework. The main concerns are about evaluation methodology clarity rather than technical soundness. With clarification of baseline evaluation protocols the paper would be a strong contribution to the field.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>