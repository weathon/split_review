Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes a two-stage, LM-based controllable text-to-speech system. The first stage generates discrete "style tokens" (extracted via a masked autoencoder) conditioned on text and fine-grained attribute labels (age, gender, pitch, emotion, SNR, reverberation); the second stage generates codec tokens conditioned on text and style tokens. The system supports both fully label-driven control (generating new timbres) and hybrid control (combining a speaker embedding with pitch/emotion labels). The key design rationale is that the style token generation stage can scale to large, diverse corpora (GigaSpeech, ~10,000 hours) while the acoustic generation stage can stay on high-quality but smaller data (LibriTTS, ~585 hours), alleviating data scarcity for controllable TTS.

## Strengths

- **Two-stage architecture that enables data scaling**: The paper's central design insight—splitting style generation (which can use large, noisy data) from acoustic generation (which benefits from high-quality data)—is well-motivated and empirically validated. The two-stage model maintains stable content accuracy (WER) and naturalness (UTMOS) as CFG scale increases, while a one-stage baseline trained on LibriTTS degrades sharply on out-of-domain test sets (Figure 3). This supports the claim that the two-stage design enables robust scaling.

- **Fine-grained control via discrete labels with CFG**: The use of binned attribute labels (instead of coarse natural-language prompts) coupled with classifier-free guidance demonstrably improves control accuracy. Figure 4 shows CFG scales of 3–5 improving control accuracy by 10–20 percentage points on fine-grained attributes like age and pitch std, with clear ablation across scales.

- **Flexible hybrid control mode**: The system supports both fully discrete-label control (generating new timbres) and hybrid control where a speaker embedding fixes timbre while pitch/emotion labels are varied. Table 3 validates that the two-stage model retains control advantages in this hybrid setting while achieving comparable speaker similarity, demonstrating the versatility claimed in the introduction.

- **Comprehensive evaluation across domains**: The system is evaluated on three test sets (LibriTTS, GigaSpeech, DailyTalk) spanning read speech, diverse acoustics, and conversational dialogue. Evaluation covers UTMOS, WER, speaker similarity, MCD, and control accuracy with confidence intervals, providing a broad picture of generalization.

- **Analysis of attribute correlations and proposed mitigation**: Section 4.4 identifies strong correlations between high-level attributes (gender, arousal) and low-level pitch features, which could cause conflicting control signals. The paper proposes both a statistical conditional sampling method and learned MLP predictors (achieving >80% soft accuracy for pitch mean prediction). This is a practical contribution that many existing systems overlook.

## Weaknesses

### Fatal
None.

### Major

- **One-stage vs. two-stage comparison conflates architecture with data scale**. The one-stage baseline is trained *only* on LibriTTS (~585 hours of clean speech), while the two-stage style LM is trained on the *full GigaSpeech-xl* (~10,000 hours, varied conditions). The paper itself repeatedly attributes improvements to "the first stage trained on extensive data" (lines 225, 232, 249). This means the comparison does not isolate the *architectural design* from *data scale*. A one-stage model trained on GigaSpeech (or a two-stage model with style LM trained only on LibriTTS) would be needed to determine whether the two-stage design provides benefit beyond enabling the use of larger data. Without this, the paper's core claim about the two-stage paradigm is not convincingly isolated. (Note: The two-stage architecture *enabling* data scaling is itself a valid engineering contribution, but the paper should frame it as such and ideally provide a scaling curve.)

- **Insufficient evidence for content-disentanglement of the style representation**. The paper repeatedly claims the MAE learns "content-disentangled style features" (abstract, Section 3.2, conclusion). The sole evidence is a swapping experiment: when phonemes and style tokens from different samples are swapped, the model fails to generate meaningful speech (Section 4.3.1). However, this failure would occur *even if style tokens contained substantial content leakage*—any mismatch between leaked content and the new phoneme sequence would cause garbled output. A proper quantitative test (e.g., decoding phonemes from style tokens alone and measuring accuracy) is needed to support the strong disentanglement claim. The swapping experiment shows style tokens don't carry *enough* content to override wrong phonemes, but does not measure leakage.

- **Limited comparison to prior controllable TTS systems**. The paper compares against zero-shot TTS models (YourTTS, XTTS-V2) not designed for fine-grained control, and a one-stage baseline. It does not compare—even on a single shared metric—to any prior system supporting attribute-level control (e.g., NaturalSpeech 3 with discrete attribute conditioning, PromptTTS 2, or attribute-editing approaches). The abstract claims "superior control over attributes such as pitch and emotion," but this claim is unsubstantiated against the relevant prior art. While implementing all possible baselines is expensive, even one comparison on shared attributes/metrics would significantly strengthen the paper.

### Minor

- **Control accuracy metric needs context**. The ±1 bin relaxation is reasonable and transparently stated, but the paper does not report the number of bins per attribute or chance-level accuracy. For attributes with very few bins (e.g., gender: 2 bins), the 90%+ reported accuracy is harder to interpret without knowing what random assignment would achieve.

- **Attribute correlation mitigation not validated in the TTS pipeline**. Section 4.4 proposes MLP predictors to resolve label conflicts, but the MLP is only evaluated on prediction accuracy (~40% exact, >80% soft). Whether using these predictors actually improves TTS quality or control accuracy is not shown. This remains a suggestion rather than a validated component.

- **No ablation of the MAE auxiliary losses**. The MAE uses four losses (reconstruction, contrastive, pitch, energy) with λ weights (line 67). No experiment measures the contribution of each loss to style representation quality or downstream control accuracy. An ablation would clarify design choices and help future work.

- **No scaling study for the style LM data size**. The paper repeatedly claims that scaling the style LM to large data improves control, but no experiment varies the training corpus size. A clear trend (control accuracy vs. data hours) would directly support this central claim.

### Trivial
None.

## Nice-to-Haves

- Evaluating on attribute combinations not seen in training data (extreme/novel combinations) would demonstrate generalization beyond the training distribution.
- An ablation comparing the MAE-learned style representation against simpler alternatives (e.g., speaker embedding + frame-level pitch/energy statistics) would clarify whether the learned representation adds value beyond standard signal processing.

## Removed Points

- **"CFG implementation for mixed condition is underspecified"**: The paper explicitly states "we only conduct CFG over discrete control labels" (line 117) and the CFG formula in Section 3.4 uses the empty control token ∅ for the unconditional case. This specification is sufficiently clear.
- **Criticism about missing baselines like NaturalSpeech 3 being practically infeasible for a full re-implementation**: Kept the concern but reframed—the criticism is that the paper should compare to *at least one* prior controllable TTS system on shared metrics, which is a reasonable ask. The reviewer's full list of systems is moved here as context.
- **Strength Finder's claim that "content-disentangled style representation" is a proven strength**: This conflicts with the verified weakness about insufficient evidence for disentanglement. The design *intent* is a strength, but the evidence is weak, so this strength is moved here.

## Novel Insights

None beyond the paper's own contributions. The reviews corroborate the main observations: the two-stage data-scaling strategy is the paper's strongest contribution, while the disentanglement claim and experimental isolation are the weakest points.

## Suggestions

1. **Disentangle architecture from data scale**: Train a one-stage model on a subset of GigaSpeech comparable to LibriTTS, or train the two-stage style LM on LibriTTS only. Either would show whether the two-stage architecture itself provides benefit beyond enabling the use of more data. Alternatively, provide a scaling curve (control accuracy vs. style LM data size) to explicitly demonstrate the scaling benefit.

2. **Quantify content leakage in style tokens**: Train a phoneme predictor on style tokens alone and report phoneme error rate, comparing against a predictor using content features as an upper bound. This would directly support or refute the disentanglement claim.

3. **Add at least one controllable TTS baseline**: Compare against one prior system supporting attribute-level control on shared metrics (e.g., control accuracy for pitch/emotion). Even a single comparison would substantially strengthen the paper's claims.

4. **Add a MAE loss ablation**: Remove each auxiliary loss and measure the effect on style representation quality (e.g., reconstruction MCD, control accuracy) to justify the multi-objective design.

5. **Report bin counts and chance accuracy**: Provide the number of bins per attribute and chance-level control accuracy so readers can interpret the reported percentages.

## Score and Decision

The paper presents a well-motivated system with a clean design rationale—splitting style generation (scalable to large data) from acoustic generation (high-quality data). The discrete label interface with CFG is practical and shows clear benefits. However, the experimental evaluation has significant confounds: the central comparison conflates architecture with data scale, the key claim of content-disentanglement is supported only by circumstantial evidence, and the paper lacks comparison to prior controllable TTS systems that would contextualize its claims. These issues are fixable but require non-trivial additional experiments. In its current form, the paper does not convincingly support all of its stated contributions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>