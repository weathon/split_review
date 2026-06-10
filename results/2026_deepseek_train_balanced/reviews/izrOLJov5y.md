## Summary

Spectron introduces a spoken language model that operates directly on continuous spectrograms (avoiding discrete quantization) by connecting a pre-trained Conformer speech encoder to a pre-trained LLM decoder via a unified training objective covering ASR, text continuation, and spectrogram reconstruction. The model generates intermediate text before spectrograms, which the paper frames as a "cross-modal chain-of-thought." Experiments demonstrate competitive speaker preservation (0.42 avg. speaker similarity), N-MOS (3.68), and zero-shot spoken QA (22.9% on LLaMA-Questions with a 1B model, matching SpeechGPT's 7B instruction-tuned variant).

## Strengths

- **Strongest speaker preservation among all baselines**: Spectron achieves avg. speaker similarity of 0.42, outperforming AudioLM 3-RVQ (0.37), AudioLM 12-RVQ (0.35), TWIST 7B (0.23), and SpeechGPT (0.05) (Table 3). This is concrete, measurable evidence that the no-quantization design choice delivers a real advantage.

- **Zero-shot spoken QA matching a 7B instruction-tuned model with only 1B parameters**: Spectron (1B, zero-shot) achieves 22.9% accuracy on LLaMA-Questions, comparable to SpeechGPT-7B (21.9%, which required instruction tuning on curated data), while all other zero-shot baselines (TWIST-7B at 0.5%, AudioLM at 6.7–7%, GSLM at 4%) are far lower (Table 4). This directly supports the claim that the joint training objective retains the original LLM's knowledge.

- **Competitive semantic quality despite using a much smaller LM**: Spectron (350M LM) achieves log-perplexity 126.08, outperforming TWIST-7B (170.81) and SpeechGPT-7B (136.42) on the semantic coherence metric (Table 1). This demonstrates parameter efficiency relative to the baselines.

- **Elegant simplification eliminating text-speech alignment**: The derivation in Eqs. (12–13) showing that the ASR and LM cross-entropy losses collapse to a single CE loss — removing the need for the text-speech time alignment function φ(s) — is a genuine engineering strength over prior cascaded or multi-stage approaches.

- **Novel derivative-based spectrogram loss**: The spectrogram derivative losses (L_f + L_t) are a technically interesting contribution. The ablation demonstrates their importance (degrading perplexity from 126.08 to 787.89 when removed).

## Weaknesses

### Major

- **"Cross-modal chain-of-thought" claim is asserted without supporting evidence.** The paper states (Sec. 3.1, line 80) that the predicted text "serves as intermediate reasoning, enhancing the quality of the synthesized speech, analogous to improvements in text-based language models when using intermediate scratchpads or chain-of-thought (CoT)." This is a causal claim: the intermediate text step is said to *improve* speech quality. However, no experiment tests this. There is no ablation comparing against a variant that generates spectrograms directly from speech encoder features without generating intermediate text — the only condition tested is removing the CE loss entirely, which removes the text objective wholesale. Without such a comparison, we cannot distinguish whether the text is a genuinely useful scaffold or merely a byproduct of the training sequence ordering. The scratchpad/CoT framing should either be supported with direct evidence or appropriately softened to "the model generates text before spectrograms as part of the training objective."

### Minor

- **The log-perplexity metric conflates ASR accuracy with semantic coherence.** The metric transcribes generated speech with a Conformer ASR, then computes GPT-2 perplexity on the transcript. If Spectron generates cleaner, more ASR-friendly audio (which its higher N-MOS and speaker similarity scores suggest), the ASR makes fewer errors, producing transcripts that better reflect intended content and lowering perplexity. The 170-point gap over GSLM (296.99 → 126.08) likely reflects acoustic quality differences as much as semantic ones. This metric is field-standard (used by GSLM, AudioLM, TWIST, etc.), which softens the concern, but the paper would benefit from acknowledging this confound and supplementing with, e.g., BERTScore between the ASR transcript and ground-truth transcript.

- **No confidence intervals or significance tests for the QA results.** The headline result (Spectron 1B 22.9% vs. SpeechGPT 7B 21.9%) is a 1 percentage point difference on only 300 questions (~3 questions). Without confidence intervals or significance testing, the gap could easily be noise. This is especially important because the paper presents this comparison prominently.

- **No evaluation of ASR accuracy (WER).** The model is trained with an ASR objective (L_ASR), yet the paper never reports word error rate on a standard benchmark like LibriSpeech test-clean. Since both the ablation study and QA pipeline depend on ASR of model outputs, a WER sanity check would substantially strengthen the evaluation.

- **Ablation extreme values raise metric-interpretability questions.** Removing either L_CE (→714.43) or the derivative loss (→787.89) pushes log-perplexity far beyond any baseline (max: GSLM at 296.99). This suggests the evaluation pipeline (ASR → perplexity) may be operating in a regime where the ASR produces garbage transcripts from degraded speech, rather than the metric cleanly measuring semantic degradation. The paper's conclusion that these components "contribute to performance" remains valid, but the extreme regime should be discussed to clarify what the values mean under collapse conditions.

### Trivial

- The 3-second fixed prompt length is stated without justification; sensitivity to this choice is not explored.
- Training transcriptions from an NST model are used without any quality characterization (e.g., estimated WER on a held-out set).

## Nice-to-Haves

- A comparison table systematically listing parameter counts, training data hours, and compute for all models (these are scattered across sections).
- Qualitative analysis of QA successes/failures (what kinds of questions does Spectron answer correctly vs. incorrectly?).

## Removed Points

These points from the reviewer inputs were filtered during synthesis, with brief justification:

1. **"LLaMA-Questions dataset bias favors LLaMA-initialized baselines"** — Removed because it is unsupported by the evidence. If such a bias existed, SpeechGPT-7B (LLaMA-based) would be expected to outperform Spectron (PaLM-2-based), but Spectron achieves 22.9% vs. SpeechGPT 21.9%. The criticism contradicts the data.

2. **"Answer matching is overly permissive"** — Removed as a weakness. Substring matching is standard practice in zero-shot evaluation where models are not trained to produce concise answers. It is applied uniformly across all baselines and does not bias relative comparisons.

3. **"TTS-synthesized inputs are problematic"** — Downgraded from a stand-alone weakness. This is standard practice in spoken QA evaluation; all baselines face the same condition. It is a scope constraint, not a source of unfairness.

4. **"Internally contradictory that derivative loss ablation degrades more than CE loss ablation"** — Removed. Both values (714 vs. 788) indicate total model collapse under different failure modes; the exact ordering is not meaningful and does not contradict any known property of the model or metric.

5. **"Vocoder dependence is a confound"** — Removed. This is standard practice for all spectrogram-to-waveform generation; the paper acknowledges it.

6. **Reproducibility nitpicks (undisclosed hyperparameters, implementation details)** — Removed per hard rules.

7. **Formatting, grammar, and missing-appendix complaints** — Removed per hard rules (parser artifacts / stripped sections).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Test the CoT claim directly**: Add an ablation that removes intermediate text generation (generate spectrograms directly from speech encoder features, without text tokens). If performance degrades, the scratchpad framing is supported; if not, drop the causal claim and describe the text step descriptively.

2. **Report confidence intervals for QA results**: On a 300-question test set, even ±2–3% CIs would substantially strengthen confidence in the reported rankings.

3. **Supplement log-perplexity with a cleaner semantic metric**: e.g., BERTScore or semantic similarity between the ASR transcript of model output and the ground-truth transcript; or report the ASR WER on generated speech to quantify the acoustic confound.

4. **Report ASR WER on a standard benchmark** (e.g., LibriSpeech test-clean) as a basic sanity check for the ASR training objective.

5. **Discuss the 3-second prompt choice**: Show sensitivity to prompt length or at minimum justify the choice.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>