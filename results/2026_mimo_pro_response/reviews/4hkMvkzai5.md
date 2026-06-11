Now I have sufficient calibration data. Let me compile the final review with all anchors considered.

## Summary

DeCodec proposes a neural audio codec that disentangles audio into orthogonal speech and background sound subspaces via a Subspace Orthogonal Projection (SOP) module combined with a Representation Swap Training (RST) procedure, and further decomposes speech into semantic and paralinguistic components via Semantic Guidance (SG). The system enables speech enhancement through representation recombination, demonstrates one-shot voice conversion on noisy speech, and provides noise-robust ASR features, all from a single codec model.

## Strengths

- **Convincing ablation study validates the core SOP+RST mechanism (Table 4):** Ablation-1 (SOP only, SDR-B = −13.15) and Ablation-2 (RST only, SDR-B = −10.67) show catastrophic decoupling failure when either component is used alone, while Ablation-3 (SOP+RST, SDR-B = 0.49, SDR-S = 7.90) demonstrates their combination is essential. This is direct, quantitative evidence for the paper's central technical claim that both mechanisms are needed for effective speech-background disentanglement.

- **Speech enhancement via representation recombination outperforms dedicated SE models (Table 2):** DeCodec achieves the highest DNSMOS BAK score (3.99 on real recordings), surpassing purpose-built SE systems including SELM (3.44) and StoRM (3.38), by simply replacing background sound representations with those of blank audio — no SE-specific training required. This is a genuinely novel and practically impactful capability.

- **Well-formulated orthogonal subspace decomposition (Section 3.4, Equations 2–6):** The SOP module uses clean linear algebra (direct sum decomposition, orthogonal projection operators) with clear mathematical derivation. The orthogonality constraint (Eq. 5) is well-motivated and standard.

- **Causal variant achieves competitive real-time performance:** DeCodec-c achieves OVL 3.31/2.99, BAK 4.09/3.94 on DNS Challenge real recordings, comparable to non-causal SELM (3.26/3.12, 4.10/3.44), demonstrating viability for streaming/real-time applications.

- **Multi-task versatility from a single model:** The paper demonstrates SE, one-shot VC, and noise-robust ASR features from the same codec using simple representation manipulation — replacing BRVQ components for SE, swapping SRVQ layers for VC, and using clean semantic representations for ASR. This is a practical advantage over task-specific cascaded pipelines.

## Weaknesses

### Fatal
None.

### Major

- **Unacknowledged bitrate disparity confounds the primary reconstruction comparison (Table 1):** DeCodec operates at **8.0 kbps** (4.0 kbps SRVQ + 4.0 kbps BRVQ) while baselines range from 2.0–6.0 kbps — a ~2× bandwidth advantage over the strongest baseline EnCodec (6.0 kbps) and ~4× over HiFi-Codec (2.0 kbps). The paper claims DeCodec "achieves the highest SDR for speech reconstruction" and "performs comparably to existing codec models in reconstruction" (Section 4.2.1), but never acknowledges this bitrate disparity. Table 1 lists the kbps column but provides no commentary on it. Without a bitrate-matched ablation (e.g., reducing SRVQ/BRVQ codebook levels to match 6.0 kbps or 4.0 kbps), the reconstruction gains in SDR could simply reflect the larger quantization budget, making the primary reconstruction comparison uninformative about whether the disentanglement mechanism itself imposes a reconstruction cost. This is the most significant evaluation issue: the paper's central Table 1 cannot be interpreted at face value.

- **Incomplete training objective specification:** The paper describes three novel loss terms: L_⊥ (Eq. 5), L_RST (Eq. 12), and L_SG (Eq. 7). However, since DeCodec is built on the DAC encoder-decoder framework (Section 3.3), standard codec training would also include signal reconstruction losses (time-domain, multi-scale STFT, or mel), adversarial losses from multi-scale discriminators, and VQ commitment losses. None of these are described, nor are the weights between the various loss terms given. This limits reproducibility and makes it impossible to understand the relative contribution of the disentanglement losses versus reconstruction losses.

- **"Universal" framing is not experimentally supported:** The title and abstract repeatedly emphasize "universal disentangled representation learner," and the paper claims DeCodec is "an universal front-end for multiple audio applications" (Abstract). Yet every experiment is speech-centric: speech reconstruction, speech enhancement, speech voice conversion, and speech ASR. ESC-50 and DNS-Noise are used only as background noise mixed with clean speech at controlled SNRs (−5 to 40 dB for training, −5 to 20 dB for evaluation). There are no experiments on non-speech mixed audio (e.g., music over environmental sound, overlapping sound events). The word "universal" should be substantiated by broader experiments or downscoped to "speech-centric."

### Minor

- **RST theoretical proof has a logical gap for nonlinear decoders (Section 3.6, Eq. 13–16):** The proof that RST forces disentanglement uses the mean value theorem: from Eq. 15, Dec(Zs₁ + Zn₂) − Dec(Zs₁ + Zn₁) ≈ n₂ − n₁, the MVT yields ∂Dec/∂Zn|_ξ (Zn₂ − Zn₁) ≈ n₂ − n₁ (Eq. 16). The paper then claims "The left side depends on Zs₁ through ξ, while the right side is independent of Zs₁. Therefore, for consistency ∀n₁, n₂, Zs₁ must be independent of n₁." However, ξ lies between Zn₁ and Zn₂ and the Jacobian ∂Dec/∂Zn evaluated at ξ depends on the full decoder input (including Zs₁) through the decoder's nonlinearity. The equation could hold for specific Zs₁ values that encode some n₁ information as long as the decoder's nonlinearity compensates. The proof is only rigorously valid for a linear decoder. This should be reframed as intuition or restricted to the linear case.

- **Voice conversion results are weak (Table 3):** WER of 50.46% means converted speech is barely intelligible. The paper acknowledges this ("relatively high WER," Section 4.2.3). The abstract's claim of "effective one-shot voice conversion on noisy speech" is overstated given this result. The comparison is also limited — only SpeechTokenizer and its StoRM cascade serve as baselines.

- **No variance or error bars reported:** All results are single numbers. For 300-clip evaluation sets, confidence intervals or standard deviations should be reported, especially for marginal differences like SDR 7.61 vs 6.86.

- **"Angular matrix" term used without definition (Section 3.4):** The paper states that when YY^T "satisfies the angular matrix," P_S and P_N are orthogonal projection matrices. This term is not standard and is never defined, making the mathematical claim in Eq. 6 unverifiable.

- **Missing baselines discussed extensively in related work (Section 2):** FACodec, Mimicodec, and DualCodec are discussed at length but appear in no experimental comparison. Only SpeechTokenizer is included as a semantic-codec baseline.

### Trivial
- Noise evaluation range is narrow (DNS-Noise mixed at −5 to 20 dB SNR only).

## Nice-to-Haves
- A bitrate-matched ablation would significantly strengthen the paper's primary reconstruction claim.
- Loss ablation varying the weights of L_⊥, L_RST, and reconstruction losses would deepen understanding of training dynamics.
- Evaluation on non-speech mixed audio would substantiate the "universal" framing.
- Full specification of the training objective including all loss terms and their weights.

## Removed Points
These points are flagged to be removed, treat them with caution.
- None — all points were verified against the paper text.

## Novel Insights

The paper's genuinely novel insight is that representation-domain disentanglement via orthogonal subspace projection combined with a swap-training procedure can achieve speech/background-sound decoupling that outperforms dedicated SE models in background suppression (BAK 3.99 vs SELM 3.44 on real recordings) without any SE-specific training. The clean ablation showing neither SOP nor RST alone works (SDR-B below −10 dB) but their combination yields effective decoupling (SDR-B = 0.49) is a strong empirical contribution. The demonstration that simply swapping representation components enables SE and VC from a single codec model is a practical and elegant approach that offers a genuinely new paradigm for controllable audio processing.

## Suggestions
- **Critical:** Add a bitrate-matched ablation (e.g., reduce SRVQ/BRVQ levels to match 6.0 kbps and 4.0 kbps total) to fairly evaluate reconstruction quality against baselines.
- **Critical:** Specify the complete training objective with all loss terms (reconstruction, adversarial, VQ commitment) and their weights.
- Downscope the "universal" claim to "speech-centric" unless non-speech mixed audio experiments are added.
- Reframe the RST proof in Section 3.6 as intuition for nonlinear decoders, or restrict the formal proof to the linear case.
- Define "angular matrix" in Section 3.4.
- Report error bars/confidence intervals for all metrics.

## Calibration Anchors

| Anchor Paper | Avg Score | Round | Comparison to DeCodec |
|---|---|---|---|
| DM-Codec (UFwefiypla) | 3.00 | 1 | Incremental speech codec (SpeechTokenizer + LM distillation). DeCodec has a much more novel core mechanism. |
| Disentangling Textual/Acoustic Features (xJc3PazBwS) | 3.75 | 1 | Disentanglement via Information Bottleneck. DeCodec's SOP+RST is more practically validated. |
| Universal Semantic Disentangled (Id2JMVSQHZ) | 4.80 | 1,2 | Disentangled codec for privacy. DeCodec has more novel mechanism and better ablation. |
| Codec-LM Co-design (KCVv3tICvp) | 5.00 | 1,2 | Incremental codec-LM techniques. DeCodec's contribution is more fundamental. |
| Vec-Tok Speech (C53xlgEqVh) | 5.20 | 1,2 | Speech codec with semantic tokens. Similar novelty, but DeCodec has stronger ablation and worse evaluation fairness. |
| RepCodec (LfDUzzQa3g) | 5.50 | 2 | Simple but effective speech tokenizer. DeCodec is more novel but has evaluation issues. |
| GenSE (1p6xFLBU4J) | 6.00 | 1,2 | LM-based SE, accepted. Lacks novelty per reviewers but has clean evaluation. DeCodec is more novel but has the bitrate fairness issue. |
| CLaM-TTS (ofzeypWosV) | 6.40 | 2 | Strong codec-LM for TTS, accepted. Clean evaluation and well-validated. DeCodec is below this in evaluation quality. |
| FlowDec (uxDFlPGRLX) | 7.00 | 1,2 | Strong codec paper with flow matching, accepted. Fair comparisons, clean evaluation. DeCodec is well below this. |

**Round 1 bracket:** 4.5–6.0 (between the rejected disentangled codecs at 4.80–5.50 and accepted speech processing papers at 6.00).

**Round 2 narrowing:** RepCodec (5.50, rejected) and GenSE (6.00, accepted) form tight anchors. DeCodec is more novel than RepCodec but has a more significant evaluation issue (bitrate fairness). DeCodec is more novel than GenSE but GenSE has cleaner evaluation. DeCodec sits at approximately 5.5 — on the boundary between weak reject and weak accept.

**Final score: 5.5** — The paper presents a genuinely novel SOP+RST mechanism with a compelling ablation study and an impressive SE result that outperforms dedicated models. However, the primary reconstruction comparison is confounded by an unacknowledged ~2× bitrate advantage over the strongest baseline, the training objective is incompletely specified, and the "universal" framing is unsupported. These evaluation issues prevent the paper from reaching acceptance in its current form, despite a strong core contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>