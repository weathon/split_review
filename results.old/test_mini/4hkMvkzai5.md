## Summary

DeCodec rethinks the neural audio codec as a universal disentangled representation learner. It introduces a Subspace Orthogonal Projection (SOP) module and Representation Swap Training (RST) procedure to decouple speech and background sound in the feature domain, while Semantic Guidance (SG) further decomposes speech into semantic and paralinguistic components. The core idea — moving from cascaded pipelines to a single unified representation that enables task-driven feature selection — is well motivated and the architectural design is novel.

## Strengths

- **First demonstration of speech–background sound decoupling in a codec representation domain.** The ablation (Table 4) shows that neither SOP alone nor RST alone yields effective decoupling (SDR-B < –10 dB for both), but their combination in Ablation-3 achieves SDR-B = 0.49 dB and SDR-S = 7.90 dB. This clean ablation isolates the contribution of each proposed module and verifies that the joint design, not individual components, produces the decoupling. This is a genuinely novel result among neural codecs.

- **Strong speech enhancement performance via representation recombination.** Table 2 shows DeCodec achieves the highest DNSMOS OVL among all SE models (3.39 without reverb, 3.13 on real recordings), including discriminative, diffusion, and transformer-based baselines. The BAK score of 4.13 (without reverb) demonstrates effective background suppression, and the causal variant (DeCodec-c) remains competitive with non-causal SE models. This provides concrete evidence that the decoupled representation can be practically exploited for a useful task.

- **Ablation study cleanly isolates each component's contribution.** Table 4 systematically ablates SOP, RST, and SG, showing that (a) SOP+RST together raise SDR-B from below –10 dB to +0.49 dB and SDR-S to 7.90 dB, while (b) adding SG trades modest SDR for large WER* reduction (41.9 → 25.8). This disentangles the roles of the three modules and makes the design choices interpretable.

## Weaknesses

### Major

- **Uncontrolled bitrate in the reconstruction comparison (Table 1).** DeCodec operates at 8 kbps total (4.0 + 4.0), whereas all baseline codecs use 2.0–6.0 kbps. Higher bitrate trivially improves reconstruction fidelity, so the reported SDR advantage (e.g., 7.61 vs. EnCodec's 6.86 at 6 kbps) cannot be interpreted as evidence of superior codec design. The paper's abstract claim that DeCodec "maintains advanced signal reconstruction" is not well supported because the comparison is not controlled for the primary factor driving reconstruction quality. This is not fatal to the core disentanglement contribution, but it undermines the reconstruction-related claims and the strength of the overall narrative. The authors should either match total bitrate (e.g., fewer RVQ layers in DeCodec to reach 6 kbps) or frame the reconstruction results purely as documentation with explicit caveats.

- **Background sound extraction quality is poor in the full model (Table 4).** The full DeCodec (with SG) achieves SDR-B of –0.36 dB (non-causal) and –1.11 dB (causal). Negative SDR indicates the extracted background sound is more distorted than silence. While the primary application of the decoupling is speech-focused (SE, VC), the paper's framing of "explicit decoupling of speech and background sound" implies two-way functionality. The BGS branch cannot reconstruct background sound with useful fidelity in the full model, which limits the claimed universality. The Ablation-3 (SOP+RST without SG) does achieve positive SDR-B (0.49 dB), suggesting SG is the cause of the degradation, but this trade-off is not discussed in the paper.

### Minor

- **No statistical significance or confidence intervals reported.** Given the small differences in some comparisons (e.g., WER 50.46 vs. 52.73 in the VC task; SDR of 6.79 vs. 6.86 between DeCodec-c and EnCodec on clean speech), it is unclear whether the reported advantages are reliable or within measurement noise. This is particularly important for the DNSMOS scores and WER results in the VC experiment.

- **The theoretical derivation for RST (Section 3.6) is heuristic rather than rigorous.** The proof uses the mean value theorem to argue that Zs₁ must be independent of n₁ (Equation 15-16), but the conclusion is inductive — it relies on approximations from training objectives (13)-(14) and the assumption that the decoder Jacobian captures the relevant behavior. The argument is reasonable as motivation but overstated as a formal guarantee. Similarly, the SOP derivation (Section 3.4) that minimizing L⊥ yields true orthogonal projectors requires the assumption that the covariance matrix of Y is "angular" (i.e., feature channels are mutually independent), which is neither verified nor discussed as an approximation.

- **No BGS-only reconstruction ablation.** The ablation study (Table 4) evaluates SDR-B and SDR-S jointly but does not include an ablation that specifically tests whether the BGS branch alone can reconstruct background sound from a mixture (e.g., evaluating only the BRVQ + decoder path). This would directly validate the two-way decoupling claim.

- **No subjective listening evaluation.** Despite the paper mentioning a demo page, no MUSHRA or similar listening test is reported. DNSMOS is a useful non-intrusive proxy, but for a codec claiming high reconstruction and SE quality, a subjective evaluation would substantially strengthen the evidence.

### Trivial

- In Table 4, "DeCodec-c" and "DeCodec" appear in the ablation table but the ordering of rows could be clearer (Ablations 1-3 first, then the full models).
- Minor: Table 1 caption uses "kpbs" instead of "kbps."

## Nice-to-Haves

- A controlled bitrate comparison (e.g., DeCodec with 4+0 = 4 kbps total vs. SpeechTokenizer at 4 kbps) would cleanly separate the speech-decoupling benefit from the bitrate advantage.
- A comparison of DeCodec's SE mode against using its own BGS replacement strategy combined with SpeechTokenizer (the closest ablative baseline) would clarify the advantage of the unified design.
- An analysis of the semantic guidance trade-off: the paper notes that SG reduces SDR but improves WER*, but does not quantify whether the BGS quality degradation is a necessary cost or an artifact of the current optimization.

## Novel Insights

A genuinely novel observation emerges from the calibration exercise: the gap between DeCodec and the closest accepted anchor (FlexiCodec, 5.67) is predominantly *not* about the architecture or the core idea but about *evaluation control*. FlexiCodec retrains its baselines at the same bitrate and frame rate; DeCodec compares against off-the-shelf baselines at heterogeneous bitrates. This underscores a broader pattern in speech codec papers at this venue: the community evaluates novelty generously when the idea is strong, but penalizes uncontrolled comparisons even when the idea itself is sound. DeCodec's architecture is arguably as novel as FlexiCodec's, but the uncontrolled reconstruction comparison weakens the paper's case more than any architectural limitation.

## Suggestions

1. **Add a controlled bitrate variant**: Retrain or configure DeCodec at 4–6 kbps total (e.g., by reducing SRVQ or BRVQ layers) and report its reconstruction against baselines at the same bitrates. Even if the performance drops, this would bound the efficiency cost of the decoupling and allow a fair comparison.
2. **Report confidence intervals or error bars for key metrics** (WER, SDR, DNSMOS), especially where differences are small.
3. **Add a brief limitations discussion to the main text** acknowledging the BGS quality limitations and the bitrate overhead.
4. **Include a direct BGS reconstruction evaluation** (e.g., SI-SNR on isolated BGS) to make the two-way decoupling claim more concrete.

## Removed Points

These points were raised by reviewers but removed per filtering rules (with brief justification):

- *ASR/TTS results are in the appendix* — REMOVED per hard rule: the parser strips appendix content from all papers; the results exist in the original submission.
- *Over-reliance on appendix for key claims* — REMOVED per hard rule: same as above.
- *"Limitations are deferred to Appendix H"* — REMOVED per hard rule: same as above.
- *"SE BAK advantage may come from replacing BGS with blank — overly aggressive suppression"* — REMOVED as speculative; the paper explicitly describes this mechanism and the DNSMOS results measure overall perceptual quality, not just suppression.
- *"Missing comparison with related works"* — REMOVED per hard rule: cannot assert missing related works without external verification.
- *"The paper would benefit from more discussion on XY"* (generic suggestions from Strengthening section) — REMOVED as discussion of hypothetical improvements not tied to paper flaws.
- *Strength Finder claims about "biologically motivated design" and "systematic evaluation"* — KEPT as genuine strengths with specific evidence in the paper. Generic strengths about "addressing an important problem" were dropped.

## Score and Decision

**Score calibration summary:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `kYkfCs4ZAH.md` (FlexiCodec) | 5.67 | R1, R2 | Stronger paper — controls bitrate in baselines, more thorough experiments. DeCodec is below this. |
| `lCaU7NlZ1I.md` (Self-Guidance) | 5.00 | R2 | Similar novelty level with minor evaluation gaps. DeCodec has more ambitious architecture but less controlled evaluation. Comparable. |
| `MDHVDfUrDz.md` (CodecSep) | 4.00 | R1, R2 | Weaker — mixed reviews, presentation concerns. DeCodec is above this. |
| `mrTTkF3LEM.md` (XY-Tokenizer) | 4.00 | R1 | Had concerns about limited novelty. DeCodec has clearer architectural novelty. Above this. |
| `RILri9w9IW.md` (FuseCodec) | 3.50 | R2 | Methodological fragmentation. DeCodec is clearly stronger. |
| `TgRMixfAPK.md` (H-P Disentangled) | 3.33 | R1 | Similar theme (disentangled codec) but weaker architecture. DeCodec above this. |
| `FA2R2KwyTH.md` (Speech Codecs Beyond) | 3.00 | R1 | Had critical experimental flaw (language mismatch). DeCodec is stronger. |
| `JeIDPXc9XG.md` (AudioCodecBench) | 2.40 | R1 | Benchmark paper, different category but weaker overall. |

Round 1 bracket: 4.0–5.5. Round 2 narrowing placed DeCodec between the 4.0-level papers (CodecSep, XY-Tokenizer) and FlexiCodec (5.67). The paper's genuine novelty in speech-BGS decoupling is a clear strength, but the uncontrolled bitrate comparison and weak BGS extraction quality in the full model prevent it from reaching the 5.5+ tier occupied by FlexiCodec. Comparing directly to Self-Guidance (5.00), DeCodec has more architectural ambition but also more significant evaluation gaps. The paper is comparable to Self-Guidance in overall quality — a novel idea with notable evaluation shortcomings — placing it just below 5.0.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>