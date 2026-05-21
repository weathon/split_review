Now let me write the final review.

## Summary

DeCodec rethinks neural audio codecs as universal disentangled representation learners. It introduces a Subspace Orthogonal Projection (SOP) module to project audio embeddings into orthogonal subspaces and a Representation Swap Training (RST) procedure to associate these subspaces with speech and background sound, respectively. Parallel RVQs with semantic guidance further decompose speech into semantic and paralinguistic components. The method is evaluated on reconstruction quality, speech enhancement, one-shot voice conversion, and downstream ASR/TTS tasks.

## Strengths

- **Novel and well-validated decoupling mechanism (SOP + RST).** The ablation study (Table 4) convincingly shows that neither SOP alone (SDR-B = −13.15 dB) nor RST alone (SDR-B = −10.67 dB) achieves decoupling, but their combination (Ablation-3) yields SDR-B = 0.49 dB and SDR-S = 7.90 dB. This is a clean experimental demonstration that both components are necessary and jointly sufficient for the claimed decoupling.

- **Competitive speech enhancement without a dedicated SE model.** DeCodec achieves the highest DNSMOS scores on both simulated (OVL 3.39, SIG 3.64, BAK 4.13) and real-recording (OVL 3.13, BAK 3.99) test sets (Table 2), outperforming dedicated SE baselines (InterSubNet, StoRM, SELM). This is the paper's strongest empirical result and directly demonstrates the practical utility of representation-level decoupling.

- **Broad downstream applicability demonstrated.** Unlike most codec papers that stop at reconstruction metrics, DeCodec evaluates on speech enhancement, one-shot voice conversion, ASR robustness (Appendix F), and zero-shot TTS (Appendix G). This breadth supports the claim that the decoupled representations enable controllable feature selection for diverse tasks.

- **Both causal and non-causal versions are provided and compared.** The causal variant (DeCodec-c) achieves DNSMOS scores comparable to the non-causal SELM model and significantly outperforms the causal InterSubNet, which is practically relevant for real-time applications.

## Weaknesses

### Fatal
None.

### Major

- **The mathematical "proof" of the RST procedure (Section 3.6) is not rigorous.** The argument uses the mean value theorem for vector-valued functions on Dec(Ζs₁ + Zn₂) − Dec(Ζs₁ + Zn₁) to claim that the left-side dependence on Ζs₁ forces Ζs₁ to be independent of n₁. However, the Jacobian ∂Dec/∂Zn evaluated at ξ still depends on Ζs₁ through ξ, and the decoder is a nonlinear neural network — there is no formal contradiction in a matrix-vector product that depends on both sides through a shared point ξ. The conclusion does not follow from the equations as written. This does not undermine the empirical results (the ablation study stands on its own), but presenting this as a theoretical guarantee is misleading. The authors should remove the proof or replace it with a heuristic justification.

- **The voice conversion results do not support the claim of "effective one-shot voice conversion."** The WER on the noisy test set is 50.46%, meaning roughly half the words are incorrect. The improvement over StoRM-SpeechTokenizer (52.73%) is only 2.3% absolute. While the paper acknowledges possible voicing mismatch, the claim of "effective" conversion is inconsistent with these numbers. This task should be framed more modestly (e.g., "proof-of-concept VC").

- **Reconstruction comparison is confounded by mismatched bitrate.** DeCodec operates at 8.0 kbps total (4.0+4.0), while baselines use 2.0–6.0 kbps. Higher bitrate naturally yields better SDR. The paper's claim that DeCodec "performs comparably to existing codec models in reconstruction" is technically true but understates the advantage. Moreover, Ablation-1 (SOP only, no decoupling) achieves SDR-O = 8.93 dB at the same bitrate, suggesting that the decoupling mechanism itself incurs a reconstruction penalty that goes unquantified relative to a matched-bitrate single-codebook baseline.

### Minor

- **Missing intrusive speech enhancement metrics.** The SE evaluation relies solely on DNSMOS (non-intrusive). Adding PESQ, STOI, or SI-SNR would strengthen the claim that the enhanced speech is not just well-suppressed but also high-quality. This is standard practice in the SE literature.

- **The "universal" framing is over-extended.** The method is evaluated only on speech+noise mixtures; there is no evidence it generalizes to music, sound effects, or mixtures with more than two sources. "Universal" in the paper refers to task universality (SE, VC, ASR, TTS), not audio-type universality, which is reasonable, but the title risks misleading readers.

- **SDR-B remains negative for the full model** (−1.11 dB causal, −0.36 dB non-causal), indicating that the reconstructed background sound is still measurably distorted. This is not discussed in the paper and contrasts with the otherwise positive decoupling narrative.

- **Semantic guidance requires paired clean/noisy data** (HuBERT on clean speech s, Eq. 7), which is a practical limitation not discussed in the main text. This constrains training to datasets where clean references are available.

### Trivial
None.

## Nice-to-Haves

- Include a matched-bitrate baseline (DeCodec without SOP/RST using a single 8-layer RVQ) to directly quantify the reconstruction cost of decoupling.
- Add a simple linear decoder variant or an analysis with a frozen decoder to provide cleaner theoretical support for the RST loss.
- Report model size, FLOPs, and latency for the two-encoder design, especially for the causal variant claimed to be relevant for real-time use.

## Removed Points

- **Criticism about missing appendix (Appendix H for limitations, F/G for ASR/TTS).** The parser strips appendices from all papers; they exist in the original submission. Per instructions, this is not a valid criticism.

- **"Universal" claim critiqued as unsupported because method only handles speech+noise.** The paper uses "universal" consistently to mean task universality (SE, VC, ASR, TTS) — the abstract says "enable controllable feature selection across different audio tasks." While the title could be more precise, this is a semantic overreach, not a factual error, and the critique overstates the issue.

- **Criticism about the RST "not being a major innovation" because it's "a simple reconstruction loss on swapped mixtures."** This undersells the design: combining swap-based training with orthogonal subspace projection in a codec framework is genuinely novel. The ablation study confirms both components are essential.

- **Strength about "rigorous theoretical justification for RST."** This conflicts with the verified weakness (the proof is not rigorous). When a strength and a verified weakness disagree, the weakness wins. Moved from Strengths.

- **Strength about "robust one-shot voice conversion."** A WER of 50.46% does not qualify as "robust." The strength overstates the evidence. Moved; the VC experiment is a proof-of-concept at best.

## Novel Insights

None beyond the paper's own contributions. The central insight — that orthogonal subspace projection plus a swap-reconstruction objective can steer a codec's latent space into speech and background subspaces — is the paper's own contribution and is well-validated by the ablation study.

## Suggestions

1. Remove or substantially rewrite the flawed theoretical proof in Section 3.6. A simpler empirical justification (e.g., RST as mutual information minimization under linear decoder approximation, verified by the ablation) would be more honest and sufficient.

2. Scale back the voice conversion claims from "effective one-shot VC" to "proof-of-concept" and explicitly discuss the 50% WER limitation in the main text.

3. Add at least one matched-bitrate reconstruction comparison (e.g., DeCodec configured to 4.5 or 6.0 kbps) to support the claim that decoupling does not severely degrade reconstruction.

4. Add PESQ or STOI metrics for the speech enhancement evaluation.

5. Report SDR-B negativity in the discussion section as an honest limitation of the current decoupling quality.

## Score and Decision

### Calibration Summary

**Round 1 (Bracketing):** Searched for papers on audio codecs and disentangled representations. Weak anchors (avg < 3.5): papers scoring 2.50–3.00 on related audio processing topics. Middle anchors (3.5–7.5): Universal Semantic Disentangled Privacy-preserving Speech Representation (4.80, rejected), VChangeCodec (5.75, rejected), Towards Codec-LM Co-design (5.00, withdrawn), GenSE (6.00, accepted poster). Strong anchors (>7.5): Multi-Source Diffusion Models (8.00, oral), Multi-resolution HuBERT (8.00, spotlight). **Round 1 bracket: 4.5 – 6.5.**

**Round 2 (Narrowing):** Searched within the bracket. Additional anchors: WavTokenizer (6.50, accepted poster), Vec-Tok Speech (5.20, rejected), Unsupervised Disentanglement V3 (6.40, accepted poster). DeCodec is stronger than Universal Semantic Disentangled (4.80) and Vec-Tok Speech (5.20) because its core contribution (SOP+RST) is better validated and the experiments are more comprehensive. It is comparable to VChangeCodec (5.75) — both have genuine architectural novelty but suffer from overclaimed results and evaluation gaps. DeCodec is clearly weaker than WavTokenizer (6.50) and GenSE (6.00), both of which have cleaner SOTA-level results on focused tasks. **Final judgment: 5.5.**

**Anchors consulted (all rounds):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| JOBokGDcX0.md | 2.50 | R1 | Unrelated topic (sequence segmentation) |
| kbSU5bwoRv.md | 3.00 | R1 | SVC with disentanglement; weaker evaluation than DeCodec |
| DsMxVELk3K.md | 3.00 | R1 | Unrelated (text compression) |
| W4yLHZGqdp.md | 2.75 | R1 | Unrelated (speaker ID) |
| Id2JMVSQHZ.md | 4.80 | R1/R2 | Disentangled speech codec for privacy; missing baselines, weaker experiments |
| qDSfOQBrOD.md | 5.75 | R1/R2 | Codec+VC integration; comparable evaluation rigor, similar novelty level |
| KCVv3tICvp.md | 5.00 | R1/R2 | Codec-LM co-design; limited novelty ("engineering tricks") |
| 1p6xFLBU4J.md | 6.00 | R1 | Generative SE; cleaner SOTA results on focused task |
| h922Qhkmx1.md | 8.00 | R1 | Unrelated (music generation+separation) |
| kUuKFW7DIF.md | 8.00 | R1 | Unrelated (multi-res HuBERT) |
| vaEPihQsAA.md | 7.60 | R1 | Unrelated (talking body generation) |
| j7b4mm7Ec9.md | 7.60 | R1 | Unrelated (watermarking) |
| C53xlgEqVh.md | 5.20 | R2 | Speech vectorization+tokenization; weaker novelty than DeCodec |
| yBlVlS2Fd9.md | 6.50 | R2 | Strong codec paper with cleaner SOTA results; DeCodec weaker |
| b57IG6N20B.md | 6.60 | R2 | Unrelated (biosignals) |
| Tv36j85SqR.md | 7.20 | R2 | Unrelated (neural compression theory) |
| Lut5t3qElA.md | 6.40 | R2 | Unsupervised disentanglement; cleaner theoretical framing |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>