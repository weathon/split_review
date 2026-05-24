Now I have sufficient calibration data. Let me synthesize the final review.

**Round 1 bracket:** Based on the anchors, DeCodec sits clearly above the weak band (2.50–3.25) and below the strong band (7.60–8.50). The most relevant comparison anchors are in the 4.80–5.50 range. Initial bracket: **4.5–6.0**.

**Round 2 narrowing:** Comparing DeCodec against USC (4.80), Codec-LM co-design (5.00), Vec-Tok Speech (5.20), RepCodec (5.50), and Separate-and-Diffuse (6.00), DeCodec has a more novel technical contribution than most of these but its evaluation has notable gaps. It lands around 5.0: above USC (narrower, less novel) and roughly comparable to Codec-LM co-design (5.00), but below RepCodec (5.50, cleaner execution) and well below Separate-and-Diffuse (6.00, accepted).

---

## Summary

DeCodec proposes a neural audio codec that decouples mixed audio into orthogonal subspaces for speech and background sound via a Subspace Orthogonal Projection (SOP) module and Representation Swap Training (RST) procedure. Within the speech subspace, semantic guidance further decomposes representations into semantic and paralinguistic components. The decoupled representations enable controllable feature selection for multiple downstream tasks including speech enhancement, voice conversion, ASR, and TTS. The core technical contribution — representation-domain decoupling through SOP+RST — is novel and reasonably well-supported by the ablation study.

## Strengths

- **Convincing ablation evidence for SOP+RST decoupling (Table 4).** When both SOP and RST are used, speech SDR jumps from <3 dB to 7.90 dB and background SDR from <−10 dB to 0.49 dB. Neither module alone achieves meaningful decoupling, providing clear evidence that the joint mechanism works as claimed.

- **Competitive speech enhancement via simple representation manipulation (Table 2).** By replacing background-sound embeddings with those of a blank clip, DeCodec achieves the best DNSMOS scores (OVL 3.39 simulated, 3.13 real) among all compared SE models, including specialized systems like SELM and StoRM. The causal variant (DeCodec-c) also outperforms the causal baseline Inter-SubNet (OVL 2.99 vs. 2.81).

- **Maintains codec reconstruction quality (Table 1).** Despite adding orthogonal subspaces and parallel quantizers, DeCodec achieves the highest SDR (7.61 dB) on clean speech among all compared codecs and a WER (1.92%) close to the best semantic-tokenizer baseline SpeechTokenizer (1.82%).

- **Representation-domain decoupling introduces less error than cascaded time-domain separation (Table 3).** On noisy-speech one-shot VC, DeCodec (50.46% WER) outperforms the StoRM-SpeechTokenizer cascade (52.73% WER), validating the claimed advantage of avoiding front-end separation distortion.

## Weaknesses

### Major

- **"Universal" claims are unsupported by the evaluation.** The paper frames DeCodec as a "universal disentangled representation learner" and "universal front-end for multiple audio applications," but training and evaluation use only speech mixed with two noise datasets (ESC-50, DNS-Noise). No evidence is provided that the method handles music, overlapping speech, or general audio types. The term should be replaced with a precise description of what is actually demonstrated (speech/background decoupling on those noise types).

- **Background sound extraction quality is poor.** The full non-causal DeCodec achieves SDR-B of −0.36 dB (Table 4), meaning the extracted background signal is more distorted than a silence baseline would be. The causal variant is even worse at −1.11 dB. This directly undermines the paper's claim that DeCodec can "extract" background sound and should be explicitly acknowledged and discussed rather than glossed over.

### Minor

- **One-shot VC quality is too low to support the "effective" claim in the abstract.** The reported WER of 50.46% means the converted speech is largely unintelligible, even if it marginally beats the StoRM-SpeechTokenizer baseline. The abstract's claim of "effective one-shot voice conversion" is misleading. The paper does acknowledge this limitation (attributing it to voicing mismatch), but the abstract should be tempered accordingly.

- **The total training loss is never specified as a unified equation.** L⊥, L_SG, and L_RST are defined separately, but the paper does not state how they are weighted and combined, whether standard codec reconstruction/adversarial losses are included, or what training hyperparameters (optimizer, learning rate, batch size, RST sampling proportion) are used. This impairs reproducibility.

- **Bitrate comparison is not equalized (Table 1).** DeCodec operates at 8 kbps (4+4) while baselines range from 2–6 kbps. The SDR advantage may partly reflect higher capacity rather than architectural superiority. An equal-bitrate baseline or a discussion of this confound is needed for a fair comparison.

- **The theoretical "proof" in Section 3.6 is not rigorous.** The argument invokes the mean value theorem on a high-dimensional decoder without stating necessary assumptions, and the conclusion does not formally follow. This paragraph should be recast as intuitive motivation rather than presented as a proof.

### Trivial

- The operational definitions of SDR-B and SDR-S in Table 4 are brief; specifying exactly how decoupled components are decoded and compared to references would aid clarity.
- The paper defers ASR and TTS results to appendices F and G; the abstract's claims about these should be caveated until those results are presented in the main text or a supplement available to reviewers.

## Nice-to-Haves

- A clean-speech VC experiment would isolate the quality of the semantic/paralinguistic decomposition from noise robustness and strengthen the SG contribution claim.
- Intrusive SE metrics (SDR, PESQ, STOI) on the simulated DNS set would complement the non-intrusive DNSMOS scores and provide a fuller picture of speech distortion.
- Analysis of what each quantizer captures (e.g., pitch, speaker identity, noise type) would strengthen the evidence for disentanglement.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"ASR and TTS results relegated to appendix and not verifiable."** The parser strips appendices from all papers; the original submission likely contains these results. This is a review-process artifact, not an author error.
- **"No clean-speech VC baseline provided."** The VC experiment is specifically designed to test noise robustness of the decomposition, not clean-speech VC quality. A clean-speech baseline would strengthen but its absence does not invalidate the noisy-speech comparison.
- **"The derivation relies on the implicit assumption that encoder output covariance is diagonal — the paper neither discusses nor enforces this condition."** The paper does explicitly state this condition at Eq. 6: "When the covariance matrix YY^T satisfies the angular matrix, indicating that the encoder extracts sufficiently diverse embeddings with different feature channels being mutually independent." The assumption is acknowledged; the lack of explicit enforcement is a minor concern, not a hidden flaw.
- **"The human auditory cortex analogy provides a loose motivation but is not technically embedded."** This is a stylistic preference. The analogy is brief and does not mislead; shortening it is optional.
- **"What proportion of samples are swapped during RST?" / "How is RST integrated with the rest of training?"** These are detail questions folded into the minor weakness about the missing unified loss specification.
- **"No analysis of quantizer counts K_s, K_n."** This is a nice-to-have ablation, not a substantive weakness.

## Novel Insights

The paper's core insight — that speech/background decoupling can be achieved in the representation domain of a neural codec through the combination of orthogonal projection and representation swapping, without requiring a separate time-domain separation front-end — is genuinely novel. The ablation study (Table 4) provides compelling evidence that neither orthogonal projection nor representation swapping alone is sufficient, but their combination enables meaningful decoupling. This insight has practical implications for designing unified audio processing systems that avoid the error-propagation problems of cascaded pipelines.

## Suggestions

- Replace "universal" throughout with precise language (e.g., "speech/background disentangled representation learner") and remove or heavily caveat unsupported downstream claims from the abstract.
- Add an explicit equation for the total training loss with all weights, and report key hyperparameters (optimizer, learning rate, batch size).
- Discuss the negative SDR-B values openly: acknowledge that background reconstruction quality is a current limitation, and either adjust the claim about background extraction or provide an analysis of why SDR-B is poor despite the qualitative decoupling effect shown in the SE results.
- Provide an equal-bitrate DAC baseline (or another codec at ~8 kbps) to isolate architectural effects from capacity effects in the reconstruction comparison.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| JOBokGDcX0 (Sequence Segmentation) | 2.50 | R1 | DeCodec is substantially stronger |
| UFwefiypla (DM-Codec) | 3.00 | R1 | DeCodec is substantially stronger |
| nhgTmx1TZJ (UniAudio) | 3.00 | R1 | DeCodec is substantially stronger |
| mlPTNEIsgb (Blind Audio) | 3.25 | R1 | DeCodec is substantially stronger |
| xJc3PazBwS (Disentangling Textual/Acoustic) | 3.75 | R1 | DeCodec has more novel architecture |
| Id2JMVSQHZ (USC Privacy Codec) | 4.80 | R1,R2 | DeCodec has more substantial technical contribution and broader evaluation |
| KCVv3tICvp (Codec-LM Co-design) | 5.00 | R1,R2 | Comparable; DeCodec more novel architecture but less clean evaluation |
| C53xlgEqVh (Vec-Tok Speech) | 5.20 | R2 | DeCodec has more novel core contribution |
| LfDUzzQa3g (RepCodec) | 5.50 | R1,R2 | RepCodec is cleaner but narrower; DeCodec is more ambitious with rougher edges |
| pyuCmLLluu (LLM-TSE) | 5.50 | R2 | Different problem domain; comparable quality |
| UXALv0lJZS (Separate and Diffuse) | 6.00 | R2 | Separate-and-Diffuse has a cleaner, more convincing contribution |
| vaEPihQsAA (CyberHost) | 7.60 | R1 | DeCodec is clearly below |
| tyEyYT267x / CxXGvKRDnL | 8.00 | R1 | DeCodec is clearly below |
| LbEWwJOufy (TANGO) | 8.50 | R1 | DeCodec is clearly below |

**Bracket:** Round 1 placed DeCodec in the 4.5–6.0 range. Round 2 comparisons against USC (4.80), Codec-LM (5.00), Vec-Tok (5.20), RepCodec (5.50), and Separate-and-Diffuse (6.00) narrow this to approximately **5.0**: DeCodec has a genuinely novel technical contribution with solid core ablation evidence, but suffers from overclaiming, a weak downstream result (VC), poor background extraction quality (negative SDR-B), and incomplete methodological reporting. These issues collectively prevent the contribution from being reliably assessed for acceptance in its current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>