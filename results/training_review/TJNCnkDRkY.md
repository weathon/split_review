Now I have all the information needed. Let me write the consolidated review.

---

## Summary

GPST introduces a hierarchical transformer for generative speech language modeling that integrates semantic and acoustic tokens in a single stage. The architecture consists of a global transformer (capturing long-range semantic and acoustic dependencies) paired with a smaller local transformer (modeling residual quantizer codes within each time step), yielding an efficiency gain of roughly \(D\times\) over naive unfolding. Experiments on speaker identity transfer, acoustic continuations, multilingual generation, and Hi-Res (16-quantizer) speech demonstrate competitive results, particularly against VALL-E.

## Strengths

- **Well-motivated architectural design.** The hierarchical split (global over time, local over RVQ codes) is a clean and principled way to handle the long acoustic sequences produced by neural codecs. The complexity analysis (Section 3.6) is analytically sound, showing a reduction from \(O(N T_2^2 D^2)\) to \(O(N_g T_2^2 + N_l T_2 D^2)\), and the FLOPS argument (roughly \(D\times\) savings) is compelling.

- **Valid improvement over VALL-E under comparable conditions.** In speaker identity transfer (Table 1), GPST (190M params) achieves WER 4.2 vs. VALL-E 5.9 and SPK 0.605 vs. 0.580, using the same codec (EnCodec) and the same ASR model (HuBERT-Large). The acoustic continuations setting shows a similar margin (WER 2.8 vs. 3.8). The parameter efficiency is notable—GPST uses fewer total parameters than VALL-E's two-stage model (165M+172M).

- **Demonstration of Hi-Res (16-quantizer) capability.** GPST is the first speech LM to operate with 16 RVQ quantizers, achieving DNSMOS 4.02 (Table 2) and showing richer high-frequency content in mel-spectrograms (Figure 2). The local-drop technique provides a practical path to training with many quantizers.

- **Cross-lingual transfer result is informative.** Table 3 shows that an English-only GPST can generate Chinese acoustic continuations (CER 33.3 vs. ground-truth 26.4), demonstrating that EnCodec generalizes across languages and that the semantic token space (XLSR) provides a language-agnostic conditioning signal.

## Weaknesses

### Fatal

None.

### Major

- **WER and SPK comparisons against AudioLM / SPEAR-TTS are not controlled.** Table 1's footnote acknowledges that AudioLM's WER (6.0) was obtained with a *different ASR system* (Conformer Transducer) than the HuBERT-Large model used for GPST and VALL-E. Different ASR systems yield systematically different WERs, so the claim "GPST outperforms AudioLM on WER" is not supported by the evidence presented. Similarly, SPK scores for AudioLM (0.460) and SPEAR-TTS (0.560) are almost certainly reproduced from their original papers (which used different speaker verification pipelines, e.g., d-vectors), not computed with the WavLM-TDNN model the authors used for GPST. The paper does *not* state that all baselines were re-evaluated under identical conditions. Since these incomparable numbers appear in the same table alongside GPST's results, readers are led to conclusions the data cannot support. The VALL-E comparison is fair (same ASR, same codec), but the AudioLM/SPEAR-TTS comparisons are unreliable.

- **DNSMOS comparison is uncontrolled.** The paper states it "compare[s] DNSMOS with the examples provided on VALL-E's demo page for fairness." Demo-page samples are typically cherry-picked and may not be representative. The SPEAR-TTS DNSMOS score (3.68) is reported without any provenance—it is unclear whether it was computed by the authors or reproduced from another source under different conditions. The small DNSMOS margin between GPST (3.89) and VALL-E (3.87) is likely within the metric's noise floor anyway.

### Minor

- **Unconditional generation is described but never evaluated.** Section 3.4 describes unconditional generation, and the introduction claims GPST can "generate syntactically consistent speech with diverse speaker identities," yet no quantitative metric (WER, SPK, or any diversity metric) is reported for this mode. This leaves a claimed capability unsubstantiated.

- **Local-drop is proposed but not ablated.** The technique is described in Section 3.3 as a contribution for training efficiency, yet no experiment measures its effect on training speed, convergence, or quality. The manuscript would benefit from even a simple trade-off curve showing quality vs. token-drop rate.

- **The "exact factorization" language is slightly misleading.** Section 3.2 calls the objective in Equation (4) *exactly* factorized. The probabilistic decomposition itself is indeed exact (it is the chain rule). However, the implementation sums acoustic embeddings \(E(a_t) = \sum_{q=1}^D E_a(a^q_t)\) before passing them to the global transformer, which means the global module cannot distinguish individual code positions within a time step. The conditioning on individual codes \(a^{<q}_t\) occurs only in the local transformer. The overall model is an approximation to the full conditional (as all parametric models are), so calling the *architectural instantiation* "exact" overstates the case. The more relevant question is whether the sum is a sufficiently rich representation—this is not examined.

- **Ablation study is limited.** Table 4 only varies the global/local layer split. Missing ablations include: removing the local transformer entirely (flat prediction), varying the local-drop rate, comparing sum vs. concatenation of acoustic embeddings, and evaluating the silence-insertion trick for speaker identity transfer.

- **Cross-lingual results lack baselines.** The multilingual experiment (Table 3) reports GPST's CER/SPK but does not compare with any existing cross-lingual system (e.g., the text-based VALL-E X, or PolyVoice). While these systems differ in their task formulation, some comparison would help calibrate the reader's expectations of the cross-lingual quality bar.

- **"First work" claim should be softened.** GPST claims to be "the first work that supports spoken multilingual speech generation and Hi-Res speech synthesis." The Hi-Res claim (16 quantizers) is novel and plausible. The spoken multilingual claim is defensible (speech-to-speech, unlike VALL-E X's text-based cross-lingual TTS), but concurrent work (UniAudio, cited by the paper) explores related directions, so the phrasing invites unnecessary pushback.

### Trivial

- None.

## Nice-to-Haves

- **Subjective listening test.** The paper uses DNSMOS, a no-reference estimator, as a proxy for speech quality. A small-scale subjective MOS evaluation (e.g., comparing GPST against ground-truth resynthesis or VALL-E samples) would substantially strengthen the quality claims.
- **Statistical significance.** The paper reports averages over three runs but no standard deviations or confidence intervals for WER/SPK.

## Removed Points

- The harsh critic's claim that the "exact factorization" issue "affects the paper's theoretical framing and the claimed advantage over multi-stage models" is overstated. The chain-rule factorization is mathematically exact; the *architecture* approximates each factor, as every neural model does. The summing-embeddings concern is a valid architectural limitation (retained above, weakened to Minor), but the reviewer's framing of it as a misrepresentation conflates probability theory with model capacity. Removed because it misinterprets the nature of the claim.

- The harsh critic's criticism of missing comparison with "existing cross-lingual system (e.g., VALL-E X, SpeechGPT, PolyVoice)" as a major omission is weakened to Minor. These systems use different input modalities (text) or different task formulations, so direct comparison is not straightforward. The reviewer's demand for re-implementing SoundStorm is scope-creep (the authors give a reasonable justification for its exclusion: duplicate semantic tokens make it an apples-to-oranges comparison). Removed as scope creep.

- The demand for subjective MOS as "the gold standard" is moved to Nice-to-Haves. DNSMOS is widely accepted as a standard proxy in the speech community and is used in many papers at top venues.

- The strength finder's strength about "dramatically reducing computational cost while improving performance" is partially kept but caveated: the performance improvement against AudioLM is unreliable due to evaluation issues; against VALL-E it is valid. The framing is adjusted accordingly.

- Generic strengths from the strength finder about "LLM integration in mind" are retained as supporting strength but noted as speculative.

## Novel Insights

The most noteworthy aspect of the paper is the specific design choice of *summing* all D quantizer embeddings at each time step for the global transformer. This is surprisingly aggressive—it discards inter-quantizer structure within a frame entirely, pushing all the burden of modeling residual-code dependencies onto the small local transformer. One might expect this to hurt performance, yet the VALL-E comparison suggests it works well. This creates an interesting asymmetry: the global module operates on information-equivalent of a single "average" acoustic vector per frame, while the local module resolves the internal structure. Whether this is optimal or just a good Pareto point is an open question the paper does not explore, but the design is provocative and could inspire further work on information bottlenecks in hierarchical speech LMs.

## Suggestions

1. **Re-evaluate AudioLM and SPEAR-TTS under the same pipeline** (same ASR HuBERT-Large, same WavLM-TDNN, same test set, same EnCodec if possible) to make the comparisons in Table 1 interpretable. If model weights are unavailable, mark those results explicitly as "reported in [original paper]" with a clear caveat that conditions differ, and avoid claiming superiority over them.

2. **Report the unconditional generation results quantitatively.** At minimum, show WER and a diversity metric (e.g., self-BLEU or token entropy) for unconditionally generated samples.

3. **Add an ablation of local-drop** (e.g., WER/SPK vs. drop rate, or training throughput vs. drop rate) to substantiate the claimed efficiency benefit.

4. **Clarify the SPK evaluation protocol** in the main text: were all baseline SPK scores computed using the authors' WavLM-TDNN pipeline, or are some numbers taken from prior papers?

5. **Soften the "first work" claim** to "to the best of our knowledge, the first speech LM to demonstrate spoken multilingual generation with 16-quantizer Hi-Res capability in a single stage."

6. **Compare sum vs. concatenation** of acoustic embeddings in the global transformer as an additional ablation—this directly addresses the information-loss concern.

## Score and Decision

This paper makes a genuine architectural contribution (hierarchical transformer for single-stage speech LM) supported by a sound efficiency analysis. The VALL-E comparison is valid and shows clear improvement with fewer parameters. The Hi-Res and cross-lingual demonstrations are useful additions. However, the central empirical claims against AudioLM and SPEAR-TTS are not properly controlled, and several described capabilities (unconditional generation, local-drop) lack experimental support. The evaluation issues are fixable but the paper in its current form overstates its empirical findings.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>