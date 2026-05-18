Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes a two-stage controllable TTS system built around a masked-autoencoded style representation. A style MAE learns content-disentangled prosodic/timbre features, which are discretized into style tokens via RVQ. The first-stage LM generates style tokens from phonemes and discrete control labels (binned style attributes like pitch, emotion, age, gender, SNR, C50); the second-stage LM generates codec tokens from phonemes and the style tokens. Classifier-free guidance is applied to the discrete labels to improve fine-grained control. Experiments show the two-stage system outperforms a one-stage baseline in robustness and control accuracy, and the style tokens carry rich speaker and prosodic information with low content leakage.

## Strengths

- **Two-stage design that decouples style generation from acoustic generation, enabling scalable training.** The style LM is trained on 10k hours of data while the acoustic LM only needs ~585 hours of high-quality data. Figure 3 shows the two-stage model maintains stable WER and UTMOS across CFG scales where the one-stage model degrades sharply on out-of-domain test sets. This empirically validates the practical benefit of the architecture.

- **Fine-grained control via discrete attribute labels is demonstrated quantitatively.** Figures 4 and 5 show soft control accuracy in the 70–90% range for attributes including pitch mean, pitch std, age, gender, emotion dimensions, SNR, and C50. Spectral examples (Figures 6 and 7) confirm audible acoustic changes when manipulating pitch and emotion labels.

- **The style MAE produces content-disentangled representations with rich style information.** Table 2 shows reconstruction from ground-truth style tokens matches zero-shot TTS in speaker similarity (0.86–0.91 cosine similarity) while achieving much lower MCD (4.03–4.07 vs. 6.25+), indicating precise prosody reconstruction. The qualitative swapping experiment further supports content disentanglement.

- **Classifier-free guidance applied specifically to discrete labels improves control for ambiguous fine-grained attributes.** Figure 4 shows CFG raises control accuracy for attributes like pitch std and age from ~65% to ~80% on Gigaspeech, while the paper correctly observes that applying CFG to speaker embeddings degrades quality.

- **Flexible control interface combining speaker embeddings with discrete labels.** Table 3 demonstrates the ability to control emotion and pitch variation for a specified reference speaker, achieving speaker cosine similarity above 0.78 with control accuracy comparable to the fully-discrete-label setting.

- **Systematic analysis of attribute correlations with practical mitigation methods.** Table 4 quantifies correlations among attributes (e.g., gender and pitch mean, emotion dimensions and pitch variation), and Section 4.4 proposes both statistical and learned approaches for consistent label sampling, with learned predictors achieving >80% soft accuracy.

## Weaknesses

### Major

- **The data-scarcity claim confounds architecture with training-data scale.** The paper argues that the two-stage design addresses data scarcity because the style LM can be trained on abundant data while the acoustic LM needs less high-quality data. However, the key comparison (Figure 3, Figure 5) contrasts the two-stage model (style LM trained on ~10k hours of Gigaspeech) against a one-stage baseline trained only on ~585 hours of LibriTTS. This conflates the benefit of the two-stage architecture with the benefit of having 17× more training data for the style LM. Without an ablation where the style LM is trained on the same small high-quality corpus (LibriTTS) to isolate the architectural contribution, the reader cannot tell how much of the robustness improvement comes from the two-stage design itself versus simply having more training data. The paper's narrative frames this as a data-scarcity solution, but the evidence is not tight enough to support that specific framing.

- **No comparison to natural-language-conditioned TTS systems, despite motivating against them.** The paper opens by arguing that natural language prompts are "broad and coarse-grained" and that this limits fine-grained control, then proposes discrete labels as an alternative. However, all experiments compare against a one-stage model that also uses discrete labels — validating the two-stage architecture but not the claimed advantage of discrete labels over natural language. A comparison to a natural-language-controlled system (e.g., PromptTTS 2, TextrolSpeech, Audiobox) on the same control tasks would either confirm the advantage or reveal that current language-conditioned models are already competitive for fine-grained control. Without this, the paper's motivation for replacing natural language with discrete labels remains an assertion rather than an empirically supported advantage. This is a gap in the experimental framing, not a technical flaw in the proposed system, but it weakens the narrative.

### Minor

- **Only relaxed control accuracy is reported; strict accuracy is not shown.** The paper counts labels off by one bin as correct (Section 4.2). While this is reasonable for ordinal attributes, reporting strict accuracy would let readers judge how often the model hits the exact intended bin. The relaxed accuracy figures (70–90%) could mask substantially lower strict accuracy, especially for fine-grained attributes with many bins.

- **Content-leakage evaluation is only qualitative.** The paper shows that swapping phonemes and style tokens produces meaningless speech, which is a reasonable qualitative check. However, no quantitative measure (e.g., WER from style-token-only reconstruction, or mutual information estimation) is reported. A simple quantitative experiment would make the disentanglement claim more solid, especially since style tokens are used as conditioning in the full pipeline where any content leakage could cause problems.

- **Correlation-aware label selection (Section 4.4) is discussed but not evaluated in the main controllable TTS pipeline.** The paper proposes methods to infer low-level labels from high-level labels to avoid conflicting conditions, but does not test whether this improves control accuracy or naturalness in the TTS output. The MLP accuracy figures (~40% strict, >80% soft for pitch prediction) are reported, but how this translates to downstream TTS control is not shown. This limits the completeness of that contribution.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- An ablation training the style LM on the same small dataset as the acoustic LM (LibriTTS) to isolate the contribution of the two-stage architecture from the contribution of larger training data.
- A comparison to natural-language-based TTS on the same control tasks, e.g., by converting discrete label combinations to natural-language descriptions for the baseline.
- Strict (exact bin) control accuracy alongside the relaxed metric.
- A quantitative content-leakage metric (e.g., WER from style-token-only decoding).

## Removed Points

- The harsh critic's framing that the missing natural-language baseline is "fatal" and that the paper "cannot be assessed relative to the existing literature" — this overstates the issue. The paper's core technical contributions (style MAE, two-stage architecture, CFG for discrete labels) are validated by appropriate baselines; the natural-language comparison would tighten the motivation but is not required to validate the proposed system's capabilities.
- The critic's suggestion that the data-scarcity comparison "completely undermines the paper's central motivation" — the comparison does show the practical benefit of the approach, just doesn't fully isolate the source of improvement. This is a gap in the ablation design, not a fatal flaw.
- The critic's suggestion about the relaxed metric "may overestimate performance" — the paper provides an explicit, standard justification for this relaxation ("Considering the challenges of achieving precise control with fine-grained labels") and it is a common practice in this line of work.

## Novel Insights

None beyond the paper's own contributions. The reviews identify gaps in experimental framing but do not introduce conceptual novelty beyond what the paper itself presents.

## Suggestions

1. **Add an ablation isolating data scale from architecture.** Train the style LM on the same small high-quality corpus (LibriTTS) as the acoustic LM, and compare the resulting two-stage variant against the full two-stage system. This would directly quantify the benefit of scaling up style LM training data and tighten the data-scarcity argument.

2. **Add a natural-language-conditioned baseline.** Even a single comparison on one test set (e.g., LibriTTS) between the proposed discrete-label system and a representative natural-language-controlled TTS system (e.g., TextrolSpeech, PromptTTS 2) on the same control tasks would substantially strengthen the paper's motivation.

3. **Report strict control accuracy alongside the relaxed metric** in the main figures or a supplementary table, so readers can gauge exact-bin hit rates.

4. **Add a quantitative content-leakage experiment** — e.g., decode speech from style tokens alone (without phonemes) and compute WER, or compute mutual information between style tokens and phoneme sequences.

5. **Evaluate the correlation-aware label selection** (Section 4.4) in the controllable TTS pipeline, showing whether it improves control accuracy or naturalness compared to ignoring attribute correlations.

## Score and Decision

The paper presents a technically solid and well-motivated system with genuine contributions: a content-disentangled style MAE, an effective two-stage LM pipeline, and a practical CFG-based approach for discrete-label control. The experiments are generally thorough, covering reconstruction quality, control accuracy on multiple attributes, speaker similarity, and robustness to CFG scale across three test sets. The audio quality and control accuracy results are competitive.

However, two significant gaps weaken the paper's narrative: (1) the data-scarcity claim is not properly isolated from data-scale effects, and (2) the central motivation (discrete labels over natural language) is not empirically validated against any natural-language baseline. These are framing and ablation-design issues rather than technical flaws — the system does what it claims to do, but the experiments don't fully support the narrative framing. The paper would be strengthened considerably by addressing these gaps.

Given the genuine technical contributions and the presence of addressable (rather than fatal) weaknesses, the paper merits a borderline acceptance.

**MY FINAL SCORE:** <pineapple>6.0</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>