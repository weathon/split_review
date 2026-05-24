Now I have verified all key claims against the paper. Let me write the final consolidated review.

## Summary

This paper introduces UniWav, the first unified pre-training framework for speech that jointly learns a representation encoder and a Flow Matching decoder from scratch via a single pre-training objective. The same pre-trained checkpoint can be fine-tuned for speech recognition (discriminative), in-context text-to-speech (generative), and speech tokenization (bridging both). Experiments across all three tasks show competitive performance with task-specific foundation models, with particularly strong results on low-bitrate speech tokenization.

## Strengths

- **First unified speech pre-training framework for both discriminative and generative tasks.** Prior work either focuses on representation learning (HuBERT, wav2vec 2.0) or generative modeling (SpeechFlow) separately. UniWav demonstrates that a single encoder-decoder pre-trained from scratch can serve both families of tasks, achieving comparable performance to task-specific models on ASR (within ~0.5% WER of HuBERT Base) and TTS (matching SpeechFlow on ASR-WER and speaker similarity).

- **State-of-the-art low-bitrate speech tokenization.** At 500 bps, UniWav achieves 4.9% ASR-WER, 3.93 UTMOS, and 0.409 speaker similarity — all best among methods at any bitrate tested. At 1 kbps, it substantially outperforms SpeechTokenizer (5.6% vs. 9.1% WER; 3.72 vs. 2.08 UTMOS). The margin demonstrates that generative pre-training directly benefits resynthesis quality.

- **Novel scaling analysis revealing non-obvious encoder-decoder interactions (Tables 3, 4).** The analysis shows that a large encoder benefits from the generative decoder (WER improves), while a small encoder degrades when the decoder is present. For TTS, encoder depth compensates for limited decoder depth. These trade-offs are new findings specific to unified pre-training and inform future architecture design.

- **Mutual information analysis (Figure 2) provides an interpretable explanation of the model's behavior.** UniWav's encoder retains higher mutual information with speaker labels and lower with phone labels compared to HuBERT, directly accounting for its strong generation quality and slightly lower ASR discriminability.

## Weaknesses

### Fatal
None.

### Major

- **TTS evaluation protocol is ambiguous regarding baseline comparisons.** The paper states: "we use Montreal Force Aligner... to obtain alignment for both training and evaluation (and apply the same for prior works that require alignment)" (line 167). This leaves unclear whether the VALL-E and Voicebox numbers in Table 1 are re-run under this identical alignment protocol or taken from prior publications. VALL-E was originally designed without forced alignment (using a duration predictor instead), and applying a different alignment protocol could systematically advantage or disadvantage it. Without explicit confirmation that baselines were re-run under controlled conditions, the claim of "comparable performance" on TTS rests on uncertain ground. The authors should clarify this in the text — ideally by reporting which numbers are re-run vs. cited — and, if some are cited, add a caveat about protocol differences.

### Minor

- **ASR gap is acknowledged but the "comparable" framing in the abstract is slightly optimistic.** The paper reports a ~0.5% absolute WER gap on test-other (17% relative) against the best prior work. The Limitations section is honest about this, but the abstract's "comparable performance" framing (line 4) and similar statements in the intro (line 23) soften the trade-off. Since the paper's contribution is the unification itself, a more precise characterization in the abstract (e.g., "slightly behind on ASR while matching on TTS and significantly exceeding on tokenization") would better serve readers.

- **No ablation on the decoder-only-at-masked-positions design choice.** The paper states "we only compute loss at the masked positions" for both encoder and decoder (line 124). For the decoder, this means it never learns to reconstruct unmasked frames, which is unusual. An ablation comparing this to computing decoder loss on all positions would clarify whether this design is essential or incidental.

- **No sensitivity analysis for the loss weighting hyperparameter λ.** The paper says downstream performance is "less sensitive to λ" (line 124) but does not present the supporting evidence. A sweep over λ values (e.g., 0.1, 0.5, 1.0) with ASR and TTS results would be informative.

- **Mutual information estimates do not discuss finite-sample bias.** The plug-in estimator used for MI in Figure 2 is upward-biased on finite samples. The paper does not discuss this, so the absolute MI values should be interpreted with caution (though the cross-layer trends are likely robust).

### Trivial
None.

## Nice-to-Haves

- **A controlled ablation for the tokenization experiment** that disentangles encoder vs. decoder contribution: fine-tune UniWav's decoder on fixed HuBERT-L representations (quantized), then compare to using UniWav's own encoder. This would isolate whether the dramatic tokenization gains come from the encoder's better information preservation or the decoder's generative capability.

- **Comparison to a "cascaded" baseline** (pre-train encoder, freeze it, train decoder on top) would directly test whether joint training provides a benefit over staged training, beyond what the scaling analysis in Tables 3/4 hints at.

- **Confidence intervals or standard deviations** for key WER and similarity metrics would strengthen comparisons, particularly for the small gaps (e.g., 0.1% between UniWav and SpeechFlow on TTS ASR-WER).

- **Reporting negative results on alternative training configurations** (the paper mentions some were unstable) would be useful for future work on unified pre-training.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Criticism about speaker similarity text contradiction (Harsh Critic, Section-by-Section notes #2):** The reviewer claimed UniWav at 1 kbps has higher speaker similarity than SpeechTokenizer, "contradicting" the text claim "UniWav only falls short on speaker similarity." However, reading the full passage (lines 200-201), the paper means "falls short" in absolute terms (speaker information is lost at low bitrate compared to high-bitrate or original audio), then immediately clarifies that the score is still *higher* than SpeechTokenizer (0.499 vs. 0.340). The text is consistent; the reviewer misread it. **Removed — factual misunderstanding.**

- **Criticism asking for a tokenization ablation to decompose encoder vs. decoder contribution (Harsh Critic #3):** This is a reasonable suggestion for further analysis but not a weakness of the paper as-is. The paper already demonstrates a large empirical margin and provides a plausible explanation (jointly learned encoder preserves more phoneme information). **Moved to Nice-to-Haves.**

- **Missing cascaded baseline comparison (Harsh Critic's "Missing Parts"):** Interesting suggestion but the scaling analysis (Tables 3/4) partially addresses this by showing results with zero encoder/decoder depth. A full comparison with a frozen encoder is a natural follow-up, not a required experiment for this initial paper. **Moved to Nice-to-Haves.**

- **Missing ablation on decoder masking strategy (Harsh Critic's "Missing Parts"):** Also a useful ablation but not a core weakness. **Moved to Nice-to-Haves with λ sensitivity analysis.**

- **Criticism that the paper should report confidence intervals:** Standard practice in this field is single-point comparisons on these benchmarks. Requesting CIs is not specific to this paper's methodology. **Removed as generic.**

## Novel Insights

The most interesting insight emerging across the reviews is the trade-off characterization that the scaling analysis provides: generative pre-training can either help or hurt discriminative performance depending on encoder capacity. This is a non-obvious finding — a small encoder degrades with the decoder (3.0→3.3 WER), but a large encoder improves (2.4→2.3 WER) — and it directly informs future work on unified pre-training. The mutual information analysis further grounds this in representation properties, showing that the generative objective pushes the encoder to retain speaker information at the cost of phonetic purity, which explains both the slight ASR degradation and the strong TTS/tokenization results.

## Suggestions

1. **Clarify the TTS evaluation protocol explicitly.** State in the main text whether the VALL-E and Voicebox numbers in Table 1 are re-run under the authors' alignment protocol or taken from publications. If re-run, confirm that the same training data, alignment, and evaluation pipeline were used. If cited, add a caveat about protocol differences.

2. **Tighten the abstract's framing** to precisely characterize the ASR-Generation trade-off (e.g., "slightly behind on ASR while matching TTS baselines and significantly exceeding on tokenization").

3. **Add a λ-sensitivity plot or table** to support the claim that performance is "less sensitive" to this hyperparameter.

4. **Add a brief discussion of MI estimator bias** in the analysis section (Figure 2), noting that absolute values should be interpreted cautiously while trends are robust.

## Score and Decision

**Score:** 7.5  
**Decision:** Accept  

This paper makes a genuine contribution — the first demonstration that a single encoder-decoder can be pre-trained from scratch to serve both discriminative and generative speech tasks with competitive results. The method is clearly described, the experiments cover three distinct tasks, and the scaling and MI analyses provide novel insights. The main weakness is the ambiguity in the TTS evaluation protocol, which needs clarification but does not invalidate the core contribution. The tokenization results are decisive enough to stand on their own as evidence of the value of joint pre-training.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>