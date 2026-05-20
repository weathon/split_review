Now I have thoroughly verified the paper content against the reviewer claims. Let me write the final consolidated review.

## Summary

This paper proposes DeCodec, a neural audio codec that learns to decouple audio representations into orthogonal subspaces for speech and background sound, and further decomposes speech into semantic and paralinguistic components. The core technical innovations are a subspace orthogonal projection (SOP) module that factorizes the encoder embedding into two orthogonal subspaces, and a representation swap training (RST) procedure that pushes each subspace to specialize to speech or background sound. Semantic guidance (SG) via HuBERT features is additionally applied to the speech quantizer. The model is evaluated on reconstruction, speech enhancement, one-shot voice conversion, and (in appendices) downstream ASR and TTS.

## Strengths

- **Novel architectural approach to codec-based disentanglement**: The combination of subspace orthogonal projection (SOP) with representation swap training (RST) is a genuinely new idea for neural codecs. The ablation study (Table 4) provides solid empirical evidence that the two components together achieve non-trivial decoupling: Ablation-3 (SOP+RST) attains SDR-B=0.49 dB and SDR-S=7.90 dB, whereas either component alone yields SDR-B < -10 dB and SDR-S ≤ 3.03 dB. This clean ablation design convincingly shows that both components are necessary.

- **Single model serving multiple tasks without cascaded pipelines**: DeCodec can perform audio reconstruction, speech enhancement (by replacing the BGS representation with a blank), and one-shot voice conversion (by swapping paralinguistic RVQ layers) from a single trained codec. The SE results (Table 2) are competitive with dedicated SE models — DeCodec achieves the highest DNSMOS OVL (3.39) and BAK (4.13) without reverb, outperforming SE-specific models like SELM and StoRM. This demonstrates a genuine advantage of the decoupled representation approach.

- **Comprehensive ablation study isolating component contributions**: The ablation (Table 4) carefully separates the contributions of SOP, RST, and SG, and reports multiple metrics (SDR-O for overall reconstruction, SDR-B/S for decoupling quality, and WER* for semantic preservation). This allows readers to understand the specific role of each component and the trade-offs involved.

## Weaknesses

### Fatal
None.

### Major

1. **The claimed theoretical guarantee in Section 3.6 is not a valid proof.** The paper states "Here, we theoretically prove that the proposed L_RST can further force Zs ... to be speech representations only" (line 144), but the argument using the mean value theorem does not establish this. The conclusion that "Zs1 must be independent of n1" does not follow from the equations shown: the partial derivative ∂Dec/∂Zn evaluated at an intermediate point ξ can depend on Zs1 in arbitrarily complex ways, and the equality of two reconstruction differences does not force Zs1 to be independent of n1. The derivation is at best a heuristic intuition, not a proof. This matters because the paper repeatedly invokes this "theoretical guarantee" to motivate the approach (abstract, line 45, line 144). The empirical results (Ablation-3) remain valid evidence of decoupling, but the theoretical claim should be dropped or honestly characterized as intuition.

2. **Baseline comparisons for reconstruction (Table 1) are not controlled for training data.** DeCodec is trained from scratch on 700h of speech mixed with ESC-50/DNS-Noise at random SNRs, while the baselines (EnCodec, HiFi-Codec, DAC, SpeechTokenizer) are evaluated using their official pretrained checkpoints trained on different data distributions and bitrates. No baseline is retrained or fine-tuned on the same mixture data. Consequently, the SDR, Mel distance, and WER comparisons in Table 1 primarily reflect differences in training data and bitrate allocation (DeCodec uses 8.0 kbps total vs. 4.5–6.0 kbps for baselines) rather than measuring whether DeCodec maintains reconstruction quality while decoupling. The core novelty of the paper is decoupling, not reconstruction, so this weakness is not fatal, but the reconstruction claims should be tempered.

3. **One-shot voice conversion results do not support strong claims of effectiveness.** The WER on noisy speech is 50.46% (Table 3). While this is better than the cascaded StoRM-SpeechTokenizer baseline (52.73%), a WER of ~50% means roughly every other word is incorrect, indicating very limited intelligibility. The paper acknowledges "relatively high WER" and attributes it to voicing mismatches (line 243), but provides no per-utterance breakdown or analysis to support this explanation. Given that the SE results (which rely only on speech-BGS decoupling) are strong, the weak VC performance suggests that the semantic-paralinguistic decomposition within speech (via SG) may be less effective than claimed. The paper's claim of "effective one-shot voice conversion" is not supported by the evidence.

### Minor

1. **Semantic guidance (SG) degrades speech-BGS decoupling, and the implications are under-explored.** Table 4 shows that adding SG to SOP+RST reduces SDR-B from 0.49 to -1.11 (causal) and SDR-S from 7.90 to 5.70 (causal). The paper notes this as "a slight decrease in SDR" (line 258), but the degradation is substantial — SDR-B goes from positive (actual BGS reconstruction) to negative (essentially no BGS reconstruction). Since the SE and VC experiments use the full model (including SG), readers cannot determine whether these results would be stronger without SG. Ablating SG in the SE/VC settings would clarify whether SG's value for semantic decomposition outweighs its cost to speech-BGS decoupling.

2. **The SOP orthogonality derivation (Section 3.4) is mathematically vague.** The paper states that when the covariance matrix YY^T "satisfies the angular matrix" (undefined term) and feature channels are "sufficiently diverse" and "mutually independent" (line 112), then P_S P_N^T = 0 follows. No definition of "angular matrix" is provided, and the condition is not operationalized. The claim that SOP "ensures the subspaces ... to be disentangled" is therefore justified only by the empirical L_perp loss, not by the mathematical derivation presented.

3. **The supervision asymmetry is not controlled for.** DeCodec uses clean-speech HuBERT-L9 features as semantic targets during training (Section 3.5), giving it access to oracle clean speech information that baselines do not have. This is acknowledged for the SG loss, but its impact on WER comparisons (both in reconstruction and downstream ASR) is not discussed or controlled for. An experiment training a baseline codec with identical HuBERT supervision would isolate whether the decoupling mechanism itself or simply the extra supervision drives the semantic improvements.

4. **SDR-B and SDR-S metrics are not well-defined.** The ablation study (Table 4) reports SDR-B and SDR-S for "decoupled background sound" and "decoupled speech," but the paper does not specify how ground truth signals for these decoupled components are obtained from the mixed signal. SDR requires a reference signal — are the references simply the original s and n from the mixture? If so, SDR-B of 0.49 dB means the reconstructed BGS has roughly equal signal and distortion power, which is better than negative values but still relatively weak decoupling. The paper should define these metrics explicitly.

### Trivial

- The term "angular matrix" in Section 3.4 is used without definition.
- Table format (Table 1) has an extra column separator that makes it slightly hard to parse.
- Minor: the paper says "first time" for achieving decoupled representations in a codec (line 45) — this is a strong claim that would benefit from more careful qualification given related work like DualCodec and UniCodec.

## Nice-to-Haves

- Reporting SE/VC results for the Ablation-3 variant (SOP+RST without SG) to isolate whether SG's degradation of decoupling hurts downstream task performance.
- Mutual information estimates or classifier-based probing between Zs and Zn as a more direct measure of disentanglement, complementing SDR-B/S.
- Per-SNR breakdown of VC WER to validate the voicing-mismatch explanation.
- Retraining one baseline codec (e.g., a simplified RVQGAN) on the same mixture data with the same bitrate to enable fairer reconstruction comparison.

## Removed Points

- **Criticism about missing downstream results in appendices (original #6):** Per policy, appendix content exists in the original submission and was removed by the parser. The ASR result (WER*) is already presented in Table 4 in the main paper.
- **Criticism that "the trade-off [of SG] is not discussed":** The paper explicitly states "resulting in a slight decrease in SDR but a significant reduction in WER*" (line 258). The trade-off is acknowledged, though the discussion could be deeper.
- **Criticism that WER comparisons in Table 1 are unfair due to supervision asymmetry:** The WER column in Table 1 is for **clean** speech reconstruction, where all models receive clean input. No supervision asymmetry exists for clean speech evaluation.
- **Criticism about missing code release or reproducibility details:** These are standard deferred-to-acceptance items, not review-deciding weaknesses.
- **Several generic format/style nitpicks.**
- **Strength Finder's generic strengths** (e.g., "addresses an important problem") — removed as they lack specific content.

## Novel Insights

The most interesting finding from the reviews is the tension between the two levels of disentanglement the paper attempts. The SOP+RST mechanism achieves non-trivial speech-BGS decoupling (SDR-B=0.49, SDR-S=7.90), but adding semantic guidance (SG) to also decompose speech into semantic and paralinguistic components actually degrades the speech-BGS decoupling (SDR-B drops to -1.11, SDR-S drops to 5.70). This suggests that the current collaborative optimization strategy does not fully resolve the competition between the two disentanglement objectives — the model trades off cross-source decoupling for within-speech decomposition. Whether this trade-off is fundamental or addressable through better optimization (e.g., dynamic loss weighting, two-stage training) is an open question that the paper does not investigate. The finding that full DeCodec still outperforms the cascaded denoising+codec baseline in VC (WER 50.46 vs. 52.73) hints that even the degraded decoupling may still be useful, but this seems like the most productive direction for future work.

## Suggestions

1. **Remove or recharacterize the theoretical "proof" in Section 3.6** as a heuristic intuition or informal justification. The empirical ablation (Ablation-3) already provides strong evidence for SOP+RST effectiveness.
2. **Include SE and VC results for the Ablation-3 variant** (SOP+RST without SG) to show whether SG's semantic decomposition benefit outweighs its decoupling cost in downstream tasks.
3. **Retrain at least one baseline codec on the same data mixture** for reconstruction comparison, or clearly state the data/bitrate mismatch as a limitation.
4. **Define SDR-B/S metrics explicitly** — specify the reference signals used.
5. **Provide per-utterance VC analysis** (by SNR, voicing status) to support the explanation for high WER.

## Score and Decision

Calibration anchors (from one-shot batch retrieval):

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `/home/.../kYkfCs4ZAH.md` (FlexiCodec) | 5.67 | Stronger: more rigorous experiments, better-controlled baselines, cleaner contributions, accepted as poster |
| `/home/.../GVOLiaENgU.md` (Bayes-QLAE) | 6.00 | Stronger: sound theoretical derivation combined with empirical validation, accepted |
| `/home/.../MDHVDfUrDz.md` (CodecSep) | 4.00 | Comparable: both propose novel codec-based approaches with multi-task evaluations, both have evaluation gaps; this paper has stronger ablation but weaker reconstruction baselines |
| `/home/.../TgRMixfAPK.md` (HP-Codec) | 3.33 | Weaker: HP-Codec's central claim is less well-supported by ablations, missing key baselines; this paper has more convincing ablation evidence |
| `/home/.../FA2R2KwyTH.md` (Speech Codecs Beyond Compression) | 3.00 | Comparable weakness level: both have evaluation issues that undermine central claims; this paper has more architectural novelty |
| `/home/.../6P3JxS3Pfl.md` (DisCoVR) | 4.00 | Comparable: both have theoretical derivations with gaps, but reasonable empirical contributions |
| `/home/.../b36drMoKir.md` (Gradient Flow) | 0.50 | Much weaker: fundamentally incorrect proof; this paper's empirical results are valid even if the theoretical argument is not |

This paper introduces a genuinely novel approach to disentangled codec representations with a clean ablation design, and achieves competitive SE performance without dedicated SE model architecture. However, the paper overclaims in several areas: the theoretical "proof" is invalid, the reconstruction baselines are uncontrolled, the VC results are weak, and the trade-off between the two disentanglement objectives is underexplored. The paper is stronger than rejected codec papers (CodecSep, HP-Codec) but notably weaker than accepted codec papers (FlexiCodec) in experimental rigor. A borderline submission.

MY FINAL SCORE: 4.5
MY FINAL DECISION: Reject