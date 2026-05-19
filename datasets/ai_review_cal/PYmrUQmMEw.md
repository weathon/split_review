- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8
Now I have all the information I need. Let me produce the consolidated review.

---

## Summary

This paper proposes LLaMA-Omni, an architecture for low-latency speech interaction with LLMs. The model consists of a pretrained speech encoder, a speech adaptor, an LLM (Llama-3.1-8B-Instruct), and a streaming speech decoder (a CTC-based non-autoregressive Transformer). Unlike cascaded ASR+TTS systems, it processes speech instructions directly and generates both text and speech responses simultaneously. The paper also contributes InstructS2S-200K, a 200K-example speech instruction dataset constructed by rewriting text instructions (Alpaca + UltraChat) via Llama-3-70B-Instruct and synthesizing speech via TTS. Claims include response latency as low as 226ms, superior content and style over prior speech-language models, and training in under 3 days on 4 GPUs.

**Important note on the parsed text:** All experimental subsections (Section 4) and several model-subsections (encoder details, adaptor, training, inference) are represented only as `\input{Sections/...}` placeholders that were not expanded by the parser. These sections exist in the original submission. Where relevant I distinguish between parser artifacts and issues verifiable from the present content.

## Strengths

- **Principled architectural design for low-latency speech interaction.** The choice of a CTC-based non-autoregressive streaming Transformer as the speech decoder is well-grounded in prior work on streaming generation (lines 95–106; citing ma2023non, zhang2024streamspeech). By having the decoder produce discrete speech units in parallel with the LLM's autoregressive text decoding, the architecture directly addresses the sequential bottleneck of cascaded pipelines. This is a genuine architectural contribution, not merely an engineering choice.

- **Thoughtful dataset construction pipeline.** Section 3 describes a three-step process (instruction rewriting with filler words and spoken-form conversion, response generation for conciseness, speech synthesis) that tailors existing text instruction data to speech interaction scenarios. The rules for rewriting (adding filler words, converting non-text symbols, enforcing brevity) are specific, motivated, and address a real gap — existing instruction datasets are designed for text, not speech.

- **Clear positioning against prior work.** The Related Work section (lines 88–106) provides a well-organized taxonomy of speech/audio language models (native multimodal vs. encoder-based) and streaming generation methods (monotonic-attention, CTC, Transducer), clearly differentiating LLaMA-Omni from both SpeechGPT-style models (which require large-scale pretraining) and encoder-only models (which lack generation capability).

- **Efficiency-motivated design.** The paper explicitly targets training on modest hardware (4 GPUs, <3 days), which is a practically valuable goal distinct from resource-intensive approaches like SpeechGPT.

## Weaknesses

### Fatal
None.

### Major

- **The TTS model used for dataset construction is not specified.** In Step 3 (line 58), the paper states "we need to further convert them into speech using TTS models" but provides no details: not the model architecture (e.g., FastSpeech, VITS, Tacotron), not whether it is single-speaker or multi-speaker, not the voice characteristics, not the sampling rate, not the codec used for discrete unit extraction. This is critical because: (a) the quality of the discrete units the speech decoder learns to predict depends heavily on the quality and voice characteristics of the training speech, and (b) without this information, readers cannot assess whether the model would generalize to natural human speech or is overfitted to a specific synthetic voice. This is not a parser artifact — Section 3 is fully visible and this detail is simply absent.

- **The latency claim ("as low as 226ms") is not scoped or defined.** The paper repeats this number in the abstract (line 4), introduction (line 16), and conclusion (line 112), but never states what this latency measures. Does it include: end of speech input to start of speech output? End of speech input to end of speech output? Average over utterances? Minimum? Under what input-length conditions? On what hardware? The `\input{Sections/450_trade_off_latency}` section that presumably contains this analysis is not accessible, but the definition — a basic methodological requirement — should appear in the abstract or main text regardless. Without scoping, the number cannot be interpreted.

- **No evaluation of whether the dataset construction choices are beneficial.** The dataset pipeline makes several non-trivial design decisions: adding filler words, enforcing conciseness, using Llama-3-70B for rewriting. The paper provides no ablation or analysis to show these steps improve performance. For example: does adding filler words to training instructions help the model handle natural disfluencies, or does it cause the model to expect fillers during inference on clean speech? An ablation comparing models trained with vs. without these rewriting steps would be necessary to validate the pipeline. (This is a gap in the paper's methodology, not a parser artifact — the data section is available and no such analysis is mentioned.)

- **The paper's central empirical claims cannot be verified from the available text.** All experimental subsections (setup, evaluation, baselines, main results, trade-off analysis, decoding time, case study) are `\input` placeholders (lines 66–84). This means the comparisons against baselines, the metrics used (content/style evaluation), the evidence for "better responses in both content and style," and the latency measurement itself are entirely unobservable. While this is a parser artifact and the sections exist in the original submission, it is a practical limitation that prevents this review from assessing the core evidentiary basis of the paper.

### Minor

- **Single-turn only, despite multi-turn being the natural use case.** The dataset uses only the first turn of UltraChat (line 59), limiting the model to single-turn interactions. Multi-turn speech interaction is mentioned only as future work (line 112). This scope limitation should be stated explicitly and earlier in the paper.

- **No evaluation on real human speech.** The entire dataset is synthetic speech from TTS. Even a small-scale evaluation with recorded human speech instructions would significantly strengthen confidence in the model's robustness to natural speech variation (accents, disfluencies, background noise).

### Trivial

None.

## Nice-to-Haves

- A decomposition of the 226ms latency into acoustic processing, LLM generation, and speech synthesis components would strengthen the latency claim and provide diagnostic value.
- The speech encoder and adaptor architectures should be named explicitly in the main text for reproducibility (though they may be specified in the inaccessible `\input` sections).
- A human evaluation protocol for content and style quality (beyond automatic metrics) would strengthen the claim of "better responses in both content and style."

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The experimental section is effectively absent from the provided text" (as a fatal paper flaw).** The harsh critic treats this as a structural flaw that should lead to rejection. However, all experimental sections are `\input{Sections/...}` commands — a standard LaTeX mechanism that the PDF parser did not expand. The sections exist in the original submission. Per the review instructions, parser-induced content stripping should not be penalized as a paper flaw. This is retained as a major weakness in the "practical limitation" sense above, but not as a fatal error.

2. **"Llama-3-70B is a closed model accessible via API" as a weakness.** The paper cites a HuggingFace URL for the model. Llama-3-70B-Instruct is an open-weight model available on HuggingFace. The harsh critic's framing that this is a "closed model" is inaccurate for the stated source. Removed as factually incorrect.

3. **"Dataset size is relatively small (200K) for fine-tuning an 8B-parameter model"** — This is a generic concern. The paper claims the method is data-efficient (training <3 days on 4 GPUs). Without seeing the actual results, this remains speculation rather than a specific identified problem. Demoted from inclusion.

4. **"The paper overstates eliminating the need for speech transcription"** — The paper states "eliminates the need for speech transcription" accurately in context: it means no separate ASR stage, which is true of the fused architecture. The paper explicitly notes that text tokens are still generated internally (lines 14–16). The critic's reading over-narrows the claim. Removed as a misunderstanding.

5. **"Related work coverage misses X"** — Not included, per the rule against citing missing related works without external verification.

6. **"The model architecture specifics are not named (Whisper, linear projection)"** — These may be specified in the `\input{Sections/210_encoder}` and `\input{Sections/220_adaptor}` sections that the parser did not expand. Speculative.

7. **Strength Finder's claimed strengths about low latency and efficient training** — These are simply restating the paper's unverifiable claims, not evaluating evidence. Removed as superficial/generic.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the TTS model used for dataset construction** (model architecture, voice characteristics, sampling rate, codec configuration). This is essential for reproducibility and for readers to assess the domain gap between training and real-world speech.

2. **Define latency measurement precisely.** State whether the reported 226ms is the minimum, mean, or median; what start/end events bound it; what hardware it was measured on; and under what input-length conditions.

3. **Add ablation experiments for dataset construction choices.** At minimum, compare: (a) with vs. without filler words in instructions, (b) with vs. without the conciseness rewriting step. This would validate the pipeline's necessity.

4. **Include a small-scale evaluation on real human speech** to demonstrate robustness beyond the synthetic training distribution.

5. **Explicitly state the scope limitations** (single-turn, synthetic speech only) in the main text, not just as future work.

6. **If the `\input` sections are substantial, consider whether they belong in the main paper** rather than separate files, to ensure they are captured by standard PDF extraction tools.
