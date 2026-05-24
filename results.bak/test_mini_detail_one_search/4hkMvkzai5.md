Now I have all the information I need. Let me compose the final review.

## Summary

This paper proposes DeCodec, a neural audio codec that disentangles mixed audio (speech + background sound) into orthogonal subspaces via a subspace orthogonal projection (SOP) module and a representation swap training (RST) procedure. The speech representations are further decomposed into semantic and paralinguistic components via semantic guidance (SG). The method is demonstrated on reconstruction, speech enhancement (by substituting background representations with silence), one-shot voice conversion on noisy speech, and as a feature extractor for downstream ASR and TTS.

## Strengths

- **Novel formulation of speech-background sound disentanglement within a codec framework.** Prior disentangled codecs (SpeechTokenizer, FACodec, UniCodec) operate only on clean speech or classify the entire noisy mixture as a single audio type. DeCodec is the first to explicitly factorize noisy audio into separate speech and background sound representations in the feature domain, enabling selective access to each component. The approach is well-motivated by a concrete gap in existing codec designs.

- **Ablation study provides clear empirical evidence that SOP and RST are synergistic.** Table 4 shows that neither SOP alone (SDR-B = -13.15 dB, SDR-S = -1.91 dB) nor RST alone (SDR-B = -10.67 dB, SDR-S = 3.03 dB) achieves meaningful decoupling, while their combination (Ablation-3) yields SDR-B = 0.49 dB and SDR-S = 7.90 dB. This directly supports the paper's core claim that the joint mechanism is necessary and sufficient for decoupling.

- **Competitive speech enhancement as a zero-shot byproduct.** By replacing the background sound representation with that of a blank audio segment, DeCodec achieves DNSMOS scores (OVL 3.39, SIG 3.64, BAK 4.13) competitive with or exceeding dedicated SE models (SELM: OVL 3.26, SIG 3.51, BAK 4.10). This demonstrates that representation-domain decoupling can serve as a new approach to SE without task-specific training.

- **Collaborative decoupling of speech-BGS and semantic-paralinguistic information.** The combination of SOP+RST (speech-BGS) with SG (semantic-paralinguistic) improves downstream ASR WER from 41.9% to 25.8% (DeCodec-c), showing that the two levels of disentanglement interact productively rather than conflicting.

## Weaknesses

### Fatal
None.

### Major

- **The "theoretical proof" for RST (Section 3.6, Equations 13–16) is mathematically invalid and overclaimed.** The paper states "Here, we theoretically prove that the proposed L_RST can further force Zs to be speech representations only…" but the derivation uses the mean value theorem for vector-valued functions as an equality (f(b)−f(a) = Df(ξ)(b−a)), which does not hold for vector-valued functions — only the mean value *inequality* (‖f(b)−f(a)‖ ≤ M‖b−a‖) is guaranteed. The step from Equation (15) to Equation (16) is therefore not justified by the cited theorem. Moreover, the conclusion that Zs₁ must be independent of n₁ is a non-sequitur even if the linear expansion held, because the left side's dependence on Zs₁ through ξ does not logically force independence — the argument conflates "depends on" with "containing information about." This does not invalidate the empirical method (the ablation study provides real evidence), but the paper frames this as a theoretical contribution and should remove or substantially revise the claim. Readers familiar with vector calculus will immediately identify the error, which undermines trust in the paper's rigor.

- **Reconstruction comparisons (Table 1) are confounded by total bitrate.** DeCodec operates at 8.0 kbps (4.0 speech + 4.0 BGS), while baselines use 2.0–6.0 kbps. A method at higher total bitrate naturally achieves higher SDR and lower Mel distance. Even though the BGS allocation is not directly useful for speech reconstruction, the total bitrate confound means the comparison does not support the claim that DeCodec's disentanglement is cost-free in terms of reconstruction quality. The paper needs a controlled comparison (e.g., DeCodec at comparable total bitrate, or baselines at 8 kbps) to substantiate this claim.

### Minor

- **Voice conversion results are overclaimed relative to the evidence.** The paper's abstract and introduction claim "effective one-shot voice conversion on noisy speech," but Table 3 reports WER of 50.46% — roughly half the words are incorrect. While this improves over StoRM-SpeechTokenizer (52.73%) and SpeechTokenizer without denoising (74.18%), a 50% WER does not constitute "effective" voice conversion in any practical sense. The paper should temper its language (e.g., "enables one-shot VC on noisy speech, though intelligibility remains limited") and add analysis of what drives the high WER.

- **The "angular matrix" condition in Section 3.4 is undefined.** The derivation from L_⊥ to P_S P_N^T = 0 relies on the claim that "when the covariance matrix YY^T satisfies the angular matrix" — but "angular matrix" is never defined or cited. This makes the argument incomplete and hard to verify. The paper should clarify what property of YY^T is required, or remove the claim and rely on the empirical evidence instead.

- **The SE evaluation lacks a critical control.** By replacing BGS with blank audio's representation, DeCodec is doing aggressive attenuation of everything not identified as speech. The paper should report DeCodec's reconstruction output *without any modification* on noisy speech as a lower bound — this would isolate how much of the SE improvement comes from the codec's own reconstruction behavior vs. the blank-replacement strategy. The slight SIG deficit vs. SELM on real recordings (3.45 vs. 3.59) suggests speech distortion that merits analysis.

- **No direct measurement of subspace orthogonality.** The paper trains with L_⊥ to enforce orthogonality between S and N, but never measures whether this constraint actually holds at test time. Reporting the empirical correlation between S and N (and their quantized versions Zs, Zn) would strengthen the claim that the subspaces are truly disentangled.

### Trivial

- The notation P_S P_N^T = 0 in Section 3.4 is used loosely — these are linear operators, and the product P_S P_N^T as written is not well-defined without specifying how the operators are represented as matrices.
- The log-sigmoid formulation in Equation (7) for SG loss is unusual and unexplained; a brief justification would help.

## Nice-to-Haves

- Bitrate-controlled comparison: run EnCodec, DAC, or HiFi-Codec at ~8 kbps to verify that reconstruction quality does not degrade from decoupling.
- Sensitivity analysis across SNR ranges (-5 to 20 dB) for SE and VC.
- Mutual information estimates between Zs and the background signal (and Zn and speech signal) as a more rigorous test of disentanglement than SDR of reconstructed components.
- Spectrogram visualizations of the decoupled speech-only and BGS-only reconstructions.

## Removed Points

- **"Cascaded pipeline comparison is unfair because DeCodec's architecture is fundamentally different" (original Issue 3, part 2):** The paper compares to standard codec baselines as they exist; the comparison is appropriate for establishing where DeCodec stands relative to prior codecs. Removed because the point about fundamental architectural difference is not a weakness — it's the paper's contribution.
- **"Whisper is robust to noise so it may mask deficiencies" (from Section-by-section notes):** The paper uses standard evaluation practices; this is speculative without evidence that a different ASR would produce different relative rankings.
- **"DNS-Noise in training and test may overfit" (from Section-by-section notes):** The test set mixes DNS-Noise with LibriSpeech at different SNRs; this is standard practice and the paper also evaluates on the public DNS Challenge blind test set, mitigating overfitting concerns.
- **"Baseline SE scores taken from SELM paper, not reproduced" (from Section-by-section notes):** This is standard practice when those baselines are not easily runnable in the same environment.
- **"Missing related work on β-VAE, FactorVAE" (from Section-by-section notes):** Not relevant — DeCodec operates within a neural codec framework, not as a standalone disentanglement method in representation learning.
- Several strengths from the Strength Finder were removed as generic or conflicting with verified weaknesses: (a) the claim about "theoretical analysis provides formal grounding" is contradicted by the MVT error documented above; (b) the "principled motivation from auditory neuroscience" is engaging but does not by itself constitute a research contribution; (c) the claim about "noise-robust VC with lower WER than cascaded pipeline" is true but overstated — the WER is still 50%.

## Novel Insights

The sharpest insight that emerges across both reviews is that the *combination* of orthogonal subspace projection (structural disentanglement) and representation swap training (contrastive/swap supervision) is what makes the decoupling work — neither alone suffices (Table 4). This is a non-obvious design principle: the SOP provides a substrate for separation, and the RST provides the signal that *aligns* each subspace with the correct source. Prior disentanglement work in audio codecs (FACodec, SpeechTokenizer) uses only one type of constraint (gradient reversal or semantic distillation). DeCodec's joint approach to ensuring both structural separability and content alignment is the methodological contribution that goes beyond incremental addition of one more loss term.

## Suggestions

1. **Remove or heavily caveat the "theoretical proof" in Section 3.6.** Replace the claim of proof with a clear empirical/intuitive justification: the RST loss encourages the decoder to treat Zs and Zn as interchangeable in additive combinations, which in conjunction with the orthogonal subspaces from SOP, drives information separation. This is more honest and avoids the mathematical error.
2. **Add a bitrate-controlled experiment** (e.g., compare DeCodec's speech-only sub-stream at 4 kbps to DAC and EnCodec at 4–6 kbps, or run DeCodec's speech RVQ at a higher number of codebooks).
3. **Report test-time orthogonality correlation** between S and N, and ideally mutual information estimates, to support the disentanglement claim beyond reconstructed SDR.
4. **Temper the VC claim** — the paper should acknowledge that WER > 50% makes the current VC capability proof-of-concept rather than practically effective.
5. **Add an "unmodified reconstruction" control** to the SE experiments to separate codec distortion from decoupling effects.

## Score and Decision

Comparative calibration:

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| SDXL (di52zR8xgf) | 8.00 | Far stronger — major impact paper with rigorous evaluation. DeCodec has a novel idea but lacks comparable executional polish. |
| CyberHost (vaEPihQsAA) | 7.60 | Strong audio-driven generation paper with compelling demos. DeCodec addresses a different problem but falls short in evaluation completeness. |
| RepCodec (LfDUzzQa3g) | 5.50 | Similar tier — both propose novel codec designs with solid empirical support, but RepCodec is cleaner in execution while DeCodec has more ambition but overclaims. |
| USC (Id2JMVSQHZ) | 4.80 | Both address disentanglement in codecs and share issues with overstated claims. DeCodec has stronger empirical decoupling evidence (ablation), but the theoretical flaw is more serious. |
| Disentangling Textual (xJc3PazBwS) | 3.75 | Both tackle disentanglement, but the textual/acoustic paper is more narrowly scoped and lacks clear practical applications. DeCodec has clearer motivation and more extensive experiments. |
| DM-Codec (UFwefiypla) | 3.00 | Much weaker — incremental distillation with minimal novelty. DeCodec's speech-BGS decoupling is genuinely novel. |
| Balancing Token Efficiency (IqGVIU4rvM) | 2.50 | Fundamentally flawed execution. DeCodec is substantially stronger on all dimensions. |
| TextEconomizer (DsMxVELk3K) | 3.00 | Weak paper with limited relevance. DeCodec is clearly stronger. |

The paper proposes a genuinely novel approach to codec-based disentanglement with solid empirical support from the ablation study. However, the mathematically invalid "theoretical proof" and overclaimed results (VC, reconstruction comparisons) are significant issues that prevent acceptance at a top venue in the current form. The core empirical contribution is worth preserving, but the paper overreaches.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>