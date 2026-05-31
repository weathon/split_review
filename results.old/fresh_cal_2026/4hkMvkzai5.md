Now I have all the information needed. Let me construct the final consolidated review.

## Summary
The paper introduces DeCodec, a neural audio codec that learns to disentangle speech and background sound (BGS) representations via a subspace orthogonal projection (SOP) module and a representation swap training (RST) procedure, with further semantic–paralinguistic decomposition within the speech stream guided by HuBERT features. The key claim is that this unified codec can serve as a front-end for multiple tasks (SE, VC, ASR, TTS) without cascaded separation pipelines.

## Strengths

- **First explicit speech–BGS decoupling in a neural codec via joint SOP+RST.** Table 4 shows that using both SOP and RST yields SDR-B of 0.49 dB and SDR-S of 7.90 dB on noisy speech, while either module alone gives SDR-B below −10 dB. This cleanly validates that both components are necessary for effective disentanglement in the representation domain.

- **Speech enhancement results competitive with dedicated SE models.** Table 2 shows DeCodec achieves DNSMOS OVL 3.39 (without reverb) and 3.13 (real recordings), matching or exceeding specialized models like SELM (3.26 / 3.12) and StoRM (3.21 / 2.94), while also offering a causal variant. This is the strongest application-level result in the paper and directly demonstrates the practical value of the decoupled representation.

- **Hierarchical disentanglement is robust to noise, unlike prior speech-decomposition codecs.** In one-shot VC on noisy speech (Table 3), DeCodec achieves WER 50.46% vs. 74.18% for SpeechTokenizer and 52.73% for the cascaded StoRM–SpeechTokenizer pipeline. This shows the joint optimization of speech–BGS decoupling and semantic–paralinguistic decomposition provides robustness that prior speech-only codecs lack.

## Weaknesses

### Fatal
None.

### Major

- **Unfair bitrate comparison in the reconstruction evaluation (Table 1).** DeCodec operates at 4.0+4.0 = 8.0 kbps total, while all baselines operate at substantially lower bitrates: EnCodec (6.0), HiFi-Codec (2.0), DAC (4.5), SpeechTokenizer (4.0). The paper does not acknowledge this disparity and claims "the proposed DeCodec achieves the highest SDR" without qualifying that it uses nearly double the bitrate of several baselines. This confound is especially severe for noisy speech, where the full 8 kbps is actively used. The reconstruction results would be informative only with matched-bitrate comparisons (e.g., baselines at 8 kbps via multi-codebook configurations, or DeCodec at lower total bitrate). This does not undermine the core disentanglement contribution — which is supported by the ablation study and SE results — but it undermines the secondary claim that "DeCodec maintains advanced signal reconstruction."

- **The RST theoretical proof (Section 3.6) is not rigorous and overclaims.** The derivation applies the mean value theorem to obtain ∂Dec/∂Zn|_ξ (Zn₂−Zn₁) ≈ n₂−n₁ and concludes that Zs must be independent of n because the right side is independent of Zs. This step assumes that the Jacobian's dependence on Zs through ξ does not affect the relationship — an assumption that is neither stated nor justified for a neural network decoder. The argument also assumes exact reconstruction (Eqs. 13–14 are approximations, not equalities, so the subtraction is inexact). The paper presents this as a "theoretical proof" ("Here, we theoretically prove that the proposed L_RST can further force Zs ∈ V_S to be speech representations only"), which overstates what is at best a sketch. The empirical evidence (Table 4, SE results) independently supports the disentanglement claim, so the paper would be better served by framing this as intuition and letting the experiments carry the argument.

### Minor

- **Missing comparison with speech-decomposition codecs (FACodec, DualCodec) on clean speech.** The paper discusses FACodec and DualCodec in the related work but never compares against them experimentally. For the semantic–paralinguistic decomposition aspect, only SpeechTokenizer is used as a baseline (Table 3, and on noisy speech only). Including a clean-speech comparison (e.g., WER from RVQ-1 only, speaker similarity from residual RVQs) would strengthen the speech-decomposition claim.

- **Reconstruction quality trade-off not fully discussed.** Table 4 shows Ablation-1 (SOP only) achieves SDR-O of 8.93, which drops to 4.62 for the full causal DeCodec — nearly a 50% reduction. The paper mentions "a slight decrease in SDR" but this is a significant trade-off between decoupling fidelity and reconstruction quality that users should be aware of.

- **One-shot VC WER of 50.46% remains high for practical use.** While the paper explains this may stem from voicing mismatch between source and reference, and the result improves upon the cascaded baseline (52.73%), a 50% WER is not yet practically usable for VC applications. The evaluation also combines VC with SE (BGS removed), making it unclear how the VC component performs on its own without denoising.

- **No inference-time computational cost reported.** The paper does not report model parameters, inference speed, or real-time factor. Since DeCodec uses two parallel RVQ streams and two projection layers, the overhead relative to a standard codec like DAC should be quantified.

- **Controllable BGS preservation is asserted but not evaluated.** The abstract claims DeCodec enables "controllable background sound preservation/suppression in TTS," but the VC experiment removes all BGS (BRVQ-1:8 suppressed) and no experiment demonstrates selective BGS preservation.

### Trivial
None.

## Nice-to-Haves
- Additional SE metrics beyond DNSMOS (e.g., PESQ, STOI) would strengthen the SE evaluation, though DNSMOS is a standard metric in this domain.
- Quantitative disentanglement metrics beyond SDR-B/SDR-S (e.g., mutual information estimates) could further validate the subspace separation, but the current ablation is already informative.

## Removed Points
These points were raised by reviewers but are excluded from the main weaknesses above for the reasons noted:

- **Criticism of the A2 neuroscience framing as overstated.** The paper uses this as biological inspiration, not a claim to test. This is a presentation choice, not a weakness. — REMOVED (nitpick).
- **Missing ASR/TTS results in the main paper.** The paper explicitly states these are in Appendix F and G. The appendix was stripped by the parser; these results exist in the original submission. — REMOVED (parser artifact).
- **Criticism about baseline training distribution mismatch (noisy speech).** Several baselines (HiFi-Codec, DAC) show very low SDR on noisy speech (−0.66, −1.62), suggesting they were not trained on noisy data. This is a valid observation but is better absorbed into the bitrate-comparison weakness rather than treated separately. — MERGED.
- **"Theoretically grounded RST procedure" strength.** The harsh critic identifies that the proof is not rigorous, and this strength conflicts with the verified weakness. Per the filtering rules, when a strength and weakness disagree, the weakness wins. — REMOVED.
- **"Competitive reconstruction quality alongside decoupling" strength.** This conflicts with the verified bitrate-mismatch weakness. — REMOVED.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the critical evaluation gaps (especially the bitrate confound and the overclaimed proof) but do not add new observations about the method or results that the paper itself does not already present.

## Suggestions
1. **Fix the reconstruction comparison.** Either (a) retrain or configure baselines at matched total bitrate (e.g., EnCodec at 8 kbps, SpeechTokenizer with more RVQ layers), or (b) ablate DeCodec at lower bitrates (e.g., 4.0+2.0, 4.0+0.0 kbps) and show a rate-distortion curve. This directly addresses the most damaging criticism.
2. **Retitle Section 3.6.** Replace "theoretically prove" with "provide intuition for" or similar. The empirical evidence is sufficient without overclaiming the proof.
3. **Add clean-speech comparisons with FACodec and DualCodec** for the speech decomposition component (e.g., WER from the semantic token alone, speaker similarity from the residual).
4. **Report model size and inference speed** (parameters, RTF) to help readers assess the computational cost of the dual-stream architecture.
5. **Demonstrate controllable BGS preservation** with a simple experiment (e.g., VC with background kept vs. removed) to substantiate the claim in the abstract.

## Score and Decision

**Round 1 bracket:** The paper clearly sits above the weak anchors (scores 1.33–3.0: withdrawn/rejected papers with major flaws) and below the strong anchors (scores 8.0: Oral/Poster papers). Initial bracket: **4–6**.

**Round 2 narrowing within bracket:** Compared against papers in the 4–6 range:

| Anchor | Avg Score | Decision | Comparison |
|--------|-----------|----------|------------|
| FlexiCodec | 5.67 | Accept (Poster) | Cleaner evaluation, more modest claims. DeCodec has more novel disentanglement concept but weaker empirical validation. **DeCodec < FlexiCodec.** |
| CodecSep | 4.00 | Reject | Less novel, but evaluated more fairly. DeCodec has stronger motivation and results. **DeCodec > CodecSep.** |
| XY-Tokenizer | 4.00 | Withdrawn/Reject | Similar domain, DeCodec's speech-BGS disentanglement is more novel. Evaluation quality is comparable. **DeCodec ≈ XY-Tokenizer (slightly above).** |
| Self-Guidance | 5.00 | Reject | Simple but well-executed trick, rejected. DeCodec is more ambitious. **DeCodec ≈ Self-Guidance.** |

DeCodec's core contribution (speech-BGS disentanglement in a codec) is genuinely novel and the SE results are strong. However, the unfair bitrate comparison and overclaimed theoretical proof are significant evaluation weaknesses that prevent this from being as clean a paper as FlexiCodec (accepted at 5.67). Placing it between the rejected codec papers (~4–5) and the accepted one (~5.7), a score of **4.5** is appropriate.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>