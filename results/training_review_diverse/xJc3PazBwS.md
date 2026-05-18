Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes a two-stage Variational Information Bottleneck (VIB) framework to disentangle neural speech model representations into separate textual and acoustic components. Stage 1 compresses representations to decode transcription (textual latents), while Stage 2 learns complementary representations conditioned on the frozen Stage-1 latents to predict a downstream task (emotion recognition or speaker identification). The framework is evaluated on Wav2Vec2 and HuBERT (Base and Large), with probing experiments showing near-perfect separation: textual latents score at random chance on acoustic features while matching original hidden states on transcription, and acoustic latents show the opposite pattern. The paper also includes a layerwise analysis of how textual/acoustic contributions vary across model layers and a preliminary feature attribution analysis using attention weights.

## Strengths

1. **Strong probing validation of disentanglement.** The sanity-check probing experiments (Section 5, Figure 3) provide the most compelling evidence: textual latents perform at random baseline on all acoustic features (pitch, intensity, gender, speaker ID), while acoustic latents achieve random-baseline WER on transcription. This bilateral failure pattern is exactly what a successful disentanglement should produce, and it is demonstrated across multiple model architectures and sizes.

2. **Task performance preserved under compression.** Table 1 shows that VIB-trained representations (d=128) are competitive with or exceed probing classifiers trained on full hidden states. For several settings the improvement is substantial (e.g., HuBERT-Large emotion: 66.1% VIB vs. 57.3% probing; speaker ID: 98.4% VIB vs. 92.3% probing). This demonstrates that the information bottleneck retains task-relevant information while discarding irrelevant features.

3. **Layerwise analysis yields interpretable insights about model behavior.** Section 6 uses the disentangled representations to separately quantify textual and acoustic contributions per layer. The finding that fine-tuned Wav2Vec2 loses acoustic emotion-relevant information in later layers while gaining textual contribution quantitatively confirms a known phenomenon and shows the framework's value as an analysis tool beyond compression.

4. **Framework generality demonstrated across architectures and tasks.** The method is evaluated on two architectures (Wav2Vec2, HuBERT), two sizes (Base, Large), both pre-trained and fine-tuned variants, and two downstream tasks (emotion recognition, speaker identification). The consistent disentanglement results across all settings support the claim that the framework is not tied to a specific model or task.

## Weaknesses

### Fatal
None.

### Major
None. The core claims (disentanglement is achievable via two-stage VIB; the representations are separable by probing; task performance is maintained) are well-supported by the evidence. The issues below are addressable without invalidating the paper's contributions.

### Minor

1. **No comparison against alternative disentanglement approaches.** The paper compares VIB-trained classifiers against probing classifiers on original hidden states, which shows that VIB compresses without losing task performance. However, it does not test whether the *disentanglement* achieved by the two-stage VIB is better or worse than what other methods (e.g., adversarial training to minimize text-predictability, β-VAE with factorized latents, or a single-stage VIB with explicit disentanglement loss) could produce. Without at least one such comparison, it is difficult to assess whether the two-stage architecture is essential or whether its main contribution is the principled IB framing. This gap is notable given that the paper positions the framework as the central contribution.

2. **Framing of stage-2 representations as "acoustic" overstates what is verified.** The paper consistently labels stage-2 latents as "acoustic" features, but the training objective (learn representations complementary to an ASR-based text representation) could in principle capture any non-textual signal — including disfluencies, discourse structure, timing patterns, or residual ASR errors — not only acoustic properties. The probing suite verifies that pitch, intensity, gender, and speaker identity are present, but these are a subset of what the representation might encode. The paper would be more defensible by explicitly stating this as a bounded claim (e.g., "features complementary to the textual representation, which we verify include standard acoustic correlates") rather than equating "not textual" with "acoustic." The title and abstract's framing should reflect this precision.

3. **Attribution analysis (Section 7) is preliminary and would benefit from stronger validation.** The paper is transparent that this is a preliminary investigation (line 260: "While a comprehensive evaluation of disentangled attribution is beyond the scope of this work"), but the abstract and introduction still present it as a contribution. The current analysis relies on a single dot-product measure averaged over the test set, without per-utterance qualitative examples, perturbation tests (e.g., zeroing out high-attention frames), or comparisons against meaningful baselines beyond Integrated Gradients. The finding that textual attention also correlates with acoustic features (line 267) is hand-waved rather than rigorously analyzed. Either deepening this section or more strongly disclaiming it in the abstract would be appropriate.

4. **Critical ablation — removing the information loss — is mentioned in a footnote without quantified results.** The footnote on line 86 states that training without the information loss yielded "a slight improvement in performance" but "failed to disentangle" the representations, and refers to Section 5 for details. However, Section 5 does not actually present these results quantitatively. Since the information loss is central to the disentanglement claim, showing these ablation numbers (e.g., probing accuracy on target vs. non-target features with and without the loss) would directly support the paper's main methodological point.

5. **β sensitivity is not investigated.** The β coefficient is scheduled linearly from 0.1 to 1.0 (line 110) without any analysis of how performance or disentanglement quality varies with β or the annealing schedule. For a VIB-based method, this is a standard sensitivity check, and its absence makes it difficult to assess robustness.

6. **Bottleneck dimension results reported for only one setting.** The paper states that d ∈ {16, 32, 64, 128, 256} was explored (line 107), but all results are shown only for d=128. Readers cannot assess how compression level affects the trade-off between task performance and disentanglement quality.

7. **Layerwise analysis limited to Base models.** Figure 4 is captioned as showing results for "Base models," but the surrounding text presents the findings without consistently qualifying this restriction. Since Large models showed different patterns in Table 1 (e.g., larger gaps between pre-trained and fine-tuned Wav2Vec2), extending the layerwise analysis to Large models would be informative.

8. **No confidence intervals or variance estimates.** Results are averaged over three runs (Table 1), but no standard deviations or confidence intervals are reported. Given the modest dataset sizes (e.g., ~4,000 IEMOCAP utterances), some comparisons may fall within run-to-run noise (e.g., Wav2Vec2 Base emotion: 61.4 probing vs. 58.9 VIB).

### Trivial
- The random baseline for WER is reported as 100 (percentage) in Table 1's caption but as 1 (fractional) in the body text for Figure 3 (line 194). This is not a substantive error — both convey the same information — but it can cause momentary confusion.

## Nice-to-Haves
- Report standard training details (optimizer, learning rate, number of epochs, batch size) currently absent from the paper.
- Include a limitations section explicitly discussing (a) the dependency of stage 2 quality on ASR performance in stage 1, and (b) the task-specific nature of the acoustic latents (i.e., they are not a general-purpose acoustic disentanglement).
- Add per-utterance qualitative examples to the attribution analysis to make the results more interpretable.
- Extend the layerwise analysis to include speaker identification as the target task, not just emotion recognition.

## Removed Points

These points were raised by reviewers but are not included as weaknesses in the main review:

- **WER=1 criticism**: The reviewer claimed that "random baseline (WER=1)" seems implausible, suggesting the figure normalizes WER by 100. This is a misunderstanding: WER of 1.0 (fractional) is equivalent to 100% error rate, which is the correct random baseline. The table uses percentage (WER=100) while the figure text uses fractional (WER=1) — a trivial unit inconsistency, not a substantive error.
- **Missing related works**: Removed per policy — external confirmation of missing citations is not available.
- **Formatting/style nitpicks**: Removed per policy — these are parser artifacts, not author errors.
- **Missing appendix/proof references**: Removed per policy — these sections exist in the original submission and are stripped by the parser.
- **Reproducibility nitpicks about trivial details**: The request for complete training logs and all hyperparameters goes beyond what is standard for a conference submission; however, the absence of optimizer/learning rate/epochs is noted in Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a comparison baseline** — a simple alternative disentanglement approach (e.g., training a single VIB encoder with an adversarial loss to discourage text-predictability in the acoustic stream) would directly demonstrate the advantage of the two-stage conditional design.
2. **Quantify the information loss ablation** — report probing accuracy on target and non-target features for encoders trained with and without the information loss term, to directly substantiate the claim made in the footnote.
3. **Add a β-sensitivity experiment** — show how WER, task accuracy, and probing-based disentanglement metrics vary across at least 3-4 β values or schedules.
4. **Tighten the framing** — replace the blanket "acoustic" label for stage-2 representations with a more precise description (e.g., "features complementary to the textual representation, verified to include acoustic correlates") to avoid overclaiming.

## Score and Decision

The paper presents a well-motivated framework with clean empirical validation. The core contribution — a two-stage VIB approach that demonstrably disentangles textual from complementary features in neural speech representations — is convincingly supported by the probing experiments and layerwise analysis. The weaknesses are addressable: they relate to framing precision, missing ablations/baselines, and the preliminary nature of one section. The paper would be strengthened by addressing these, but none invalidate the central claims.

**Score**: 7.0 / 10

**Decision**: Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>