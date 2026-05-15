Now I have all the information I need. Let me produce the final consolidated review.

## Summary

Fox-TTS proposes a family of flow-matching Transformer models for expressive zero-shot TTS, with three key contributions: (1) a novel learnable speaker encoder using temporal augmentation, mean pooling, and an information bottleneck — trained without speaker labels; (2) a sentence-level duration predictor for improved prosody; and (3) Fox-eval, a multi-domain benchmark with 5,000 samples across 122 speakers and 10 expressive scenarios. Results show that Fox-TTS outperforms the open-source CosyVoice on the Fox-eval benchmark and achieves a CMOS of -0.05 vs. human recordings on DiDiSpeech.

## Strengths

- **Novel learnable speaker encoder with three explicit designs** — The temporal data augmentation (random clip to 50–75% + shuffle), temporal mean pooling, and information bottleneck module jointly provide explicit conditioning without speaker labels or pre-trained speaker ID models (Section 2.2). This contrasts with both in-context learning approaches (VALL-E, Voicebox) and systems relying on pre-trained speaker encoders (CosyVoice). The claim that the bottleneck dimension empirically trades off pronunciation stability vs. speaker similarity is a plausible and interesting design principle.

- **Sentence-level duration predictor with speaker-aware conditioning** — Unlike conventional phoneme-level duration predictors (which require fine-grained annotations and can produce suboptimal prosody), Fox-TTS uses a sentence-level predictor that takes both phoneme sequences and learnable speaker embeddings as input (Section 2.2). This is a practical design choice for scaling to large unlabeled data and for capturing speaker-specific speaking rates.

- **Fox-eval benchmark for expressive zero-shot TTS** — The collection of a 5,000-sample, 122-speaker, 10-domain benchmark (including outdoor interviews, TV shows, cartoons, etc.) addresses a genuine gap in the TTS evaluation landscape, where most benchmarks focus on read speech in clean conditions. The domain-level breakdown in Table 3 provides more granular insight than aggregate metrics alone.

- **Logit-normal timestep sampling for faster convergence** — The adoption of standard logit-normal timestep sampling (from Esser et al., 2024) over uniform sampling, with a claimed >2× convergence speedup (Section 2.3), is a practical training improvement relevant to the flow-matching community.

- **Human-level CMOS on DiDiSpeech** — Fox-TTS achieves a CMOS of -0.05 against human recordings, with better WER and speaker similarity (Table 2). This demonstrates that the model produces speech nearly indistinguishable from humans in normal scenarios.

## Weaknesses

### Fatal

None. The paper's core approach is sound and the contributions are real, but the evaluation is incomplete in ways that weaken the central claims.

### Major

- **Insufficient baseline comparison to support the state-of-the-art claim** — The paper compares only against CosyVoice and concludes "state-of-the-art performance." While the authors note that "most large-scale TTS models … are not released," there exist several open-source zero-shot TTS systems (e.g., XTTS v2, Bark, YourTTS, StyleTTS 2) that could serve as additional baselines on Fox-eval. CosyVoice is a strong baseline, but a single point of comparison is insufficient to justify a SOTA claim, especially when Fox-TTS_Flow (one of three proposed variants) actually has worse WER than CosyVoice on the expressive benchmark (Table 1). The paper's primary conclusion would be much better supported with at least 2–3 additional baselines, even if those models are not trained at the same scale.

- **No ablation of the speaker encoder's three key designs** — The temporal data augmentation, mean pooling, and information bottleneck module are presented as core contributions (Section 2.2), yet none are systematically ablated. There is no experiment comparing Fox-TTS_Flow with and without temporal augmentation, without mean pooling, or with varying bottleneck dimensions. The bottleneck dimension is said to enable an "explainable" trade-off between pronunciation stability and speaker similarity, but no data supports this claim. Without these ablations, it is impossible to attribute the observed performance to the claimed novel designs rather than to the overall flow-matching architecture or scale of training data.

- **No direct evidence that the speaker encoder prevents semantic leakage** — The paper asserts that the speaker encoder "prohibit[s] semantic leakage" (line 51) and that mean pooling makes "semantic content become irrecoverable" (line 51). Yet the paper acknowledges that "achieving complete removal is theoretically impossible" (line 53). No experiment quantifies the residual semantic information in the speaker representation (e.g., training a content classifier on the speaker embeddings and measuring its accuracy vs. chance). This makes the central design motivation — explicit conditioning that avoids the pitfalls of in-context learning — empirically unvalidated.

### Minor

- **Risk of data contamination for zero-shot evaluation not addressed** — Fox-TTS is trained on "millions of hours" of internet-crawled speech (Fox-train). The paper does not state whether the speakers in Fox-eval or DiDiSpeech were excluded from this training data. If even a fraction of the 122 Fox-eval speakers appear in Fox-train, the zero-shot results are confounded by speaker memorization rather than generalization. This is standard to check and should be reported.

- **Subjective evaluation lacks standard reporting details** — MOS scores are reported as single numbers per system (Table 1) without confidence intervals, number of raters, or inter-rater agreement. The CMOS of -0.05 (Table 2) is reported without variance or significance testing. While this level of reporting is not uncommon in the TTS literature, the strength of the claims ("human-level quality," "state-of-the-art") demands more rigor. The MOS instruction asks raters to judge similarity "in terms of prosody and expressiveness" but does not ask about naturalness or audio quality, which are core TTS evaluation dimensions.

- **>2× convergence speedup claim unsupported** — The logit-normal timestep sampling is claimed to yield ">2x convergence speed up" (Section 2.3), but no training curves, loss plots, or wall-clock time comparisons are provided. This is a strong quantitative claim made without supporting evidence.

- **DiDiSpeech language compatibility unclear** — The human comparison (Table 2) uses DiDiSpeech, a Chinese multi-speaker dataset. CosyVoice is Chinese-focused. It is unclear whether Fox-TTS was trained on Chinese data or whether the comparison is language-matched.

### Trivial

None that survive filtering — the parser-stripped formatting issues (e.g., the garbled "Model Configuration.2." heading) are artifacts, not author errors.

## Nice-to-Haves

- A sweep of bottleneck dimension \(C_{spk}\) with corresponding WER and SIM curves would validate the claimed trade-off and turn the bottleneck from a stated design into a demonstrated one.
- A comparison between the sentence-level duration predictor and a phoneme-level predictor to justify the design choice quantitatively.
- Releasing Fox-eval publicly would significantly amplify the paper's contribution to the community.

## Removed Points

These points were raised by reviewers but are flagged for removal per the meta-review guidelines. Treat with caution.

1. **"Missing model configuration details — fundamental reproducibility failure"** (Harsh Critic #2): The "Model Configuration." heading followed by garbled text (line 103) is an artifact of PDF-to-text parsing stripping the appendix content where architectural specifications (layers, heads, dimensions, parameter counts) were provided. The main text describes the architecture functionally (improved Transformer block with RoPE, cross-attention, AdaLN; phoneme encoder, speaker encoder, flow-based denoiser, duration predictor). Per guidelines, weaknesses about missing appendix content are removed.

2. **"Missing related works"** (Harsh Critic's note about VALL-E-style models): Per guidelines, missing related work criticisms are removed because the meta-reviewer cannot independently verify whether specific works are relevant or missing.

3. **"Pure formatting/style nitpicks"** / **"Typos, spelling, grammar"**: Any such criticisms are parser artifacts, not author errors, and are removed per guidelines.

4. **"Sub-point about Table 3 listing only 8 domains"**: The paper text consistently states 10 domains (lines 24, 101). The extracted table image cannot be reliably verified from the text, and this claim contradicts the paper's stated numbers.

5. **"Sub-point about missing 'Interview' and 'Cartoon'"**: The paper explicitly mentions these as examples of domains (lines 24, 101), contradicting the criticism.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unexpected interpretation or cross-connection that the authors themselves missed. The core tension is straightforward: the paper proposes a well-motivated architecture with several thoughtful design choices, but the experimental validation is too narrow for the strength of the claims made.

## Suggestions

1. **Expand the baseline comparison.** Add at least 2–3 open-source zero-shot TTS systems (e.g., XTTS v2, Bark, YourTTS, or a style-transfer baseline) to the Fox-eval evaluation. If these models cannot be run on the full benchmark, a representative subset would already strengthen the SOTA claim considerably.

2. **Ablate the speaker encoder designs.** Run Fox-TTS_Flow with the three designs removed individually (no temporal augmentation, no mean pooling, no bottleneck) and report WER/SIM. Plot the bottleneck dimension sweep to substantiate the claimed trade-off. Include a semantic leakage test: train a content classifier on speaker embeddings and report its accuracy vs. a baseline.

3. **Report data contamination analysis.** State explicitly whether any Fox-eval or DiDiSpeech speakers appear in the Fox-train training set. If overlap is impossible by construction, explain why.

4. **Provide training curves** to support the >2× convergence speedup claim for logit-normal timestep sampling, and report MOS with confidence intervals and rater counts.

5. **Clarify the DiDiSpeech comparison language setup** — specify whether Fox-TTS was trained on Chinese data and whether the comparison is language-matched.

## Score and Decision

The paper proposes a thoughtful architecture with three well-motivated design novelties (learnable speaker encoder with augmentation/pooling/bottleneck, sentence-level duration predictor, and Fox-eval benchmark). The core approach is sound and the results on the single baseline are competitive. However, the evaluation is not commensurate with the strength of the claims. The SOTA claim rests on a single baseline comparison, the central speaker encoder designs are not ablated, the claimed >2× convergence speedup is unsupported, and data contamination is not ruled out. These are major — not fatal — weaknesses, and they are addressable with additional experiments. In its current form, the paper's contributions are promising but not yet fully evidenced.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>