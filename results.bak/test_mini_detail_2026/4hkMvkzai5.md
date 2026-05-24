Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the consolidated review.

## Summary

DeCodec proposes a neural audio codec that explicitly decouples speech and background sound (BGS) into orthogonal subspaces via a Subspace Orthogonal Projection (SOP) module and a Representation Swap Training (RST) procedure, while further decomposing speech into semantic and residual paralinguistic components via semantic guidance (SG). The paper demonstrates that this hierarchical disentanglement enables a single codec to perform reconstruction, speech enhancement, one-shot voice conversion on noisy speech, and provide controllable features for downstream ASR and TTS — all without task-specific training.

## Strengths

- **Joint SOP+RST achieves explicit speech–BGS decoupling in the feature domain (Table 4).** Ablation-3 (SOP+RST) raises SDR-B from below −10 dB (Ablation-1, Ablation-2) to 0.49 dB and SDR-S from negative values to 7.90 dB. This is the paper's strongest empirical result and convincingly shows that the two modules are jointly necessary and sufficient for decoupling.

- **Semantic guidance (SG) substantially reduces semantic distortion (Table 4).** Adding SG on top of SOP+RST drops ASR WER* from 41.9% (Ablation-3) to 25.8% (DeCodec-c), validating that the hierarchical decomposition into semantic and paralinguistic components preserves intelligibility under noise.

- **Single codec model outperforms dedicated speech enhancement baselines on DNSMOS (Table 2).** DeCodec achieves the highest OVL score (3.39 simulated, 3.13 real) among all SE methods, including discriminative (Inter-SubNet), diffusion (StoRM), and transformer (SELM) models. This is a genuine surprise: a codec trained for reconstruction beats task-specific SE models.

- **Causal variant maintains competitive performance (Table 2).** DeCodec-c achieves DNSMOS OVL 3.31 on simulated data, outperforming the causal discriminative model Inter-SubNet (3.10) and approaching non-causal SELM (3.26), demonstrating practical value for real-time applications.

## Weaknesses

### Major

1. **Flawed theoretical proof for the Representation Swap Training (Section 3.6).** The paper claims to "theoretically prove" that the RST loss forces the quantized speech vector to be independent of background sound. The argument uses the mean value theorem for vector functions (Eq. 13–16) to derive: ∂Dec/∂Zn|_ξ (Zn₂−Zn₁) ≈ n₂−n₁. The paper then states: "The left side depends on Zs₁ through ξ, while the right side is independent of Zs₁. Therefore, for consistency ∀ n₁, n₂, Zs₁ must be independent of n₁." This reasoning does not hold. The Jacobian ∂Dec/∂Zn evaluated at ξ (which lies on the line segment between Zn₁ and Zn₂) depends on Zs₁+ξ, so the left side of Eq. (16) depends on Zs₁ through the Jacobian itself. The conclusion that Zs₁ "must be independent of n₁" does not follow from the equations presented. The empirical ablation (Table 4) already provides strong evidence that SOP+RST work in practice; the paper should either remove the "theoretically prove" language or present a sound argument. Claiming a guarantee that is not established undermines methodological rigor.

2. **Unmatched bitrate in reconstruction comparison (Table 1).** DeCodec uses two parallel RVQs at 4.0 kbps each, totaling 8.0 kbps. The baselines operate at substantially lower bitrates: EnCodec (6.0 kbps), HiFi-Codec (2.0 kbps), DAC (4.5 kbps), SpeechTokenizer (4.0 kbps). DeCodec's SDR advantage — especially on clean speech (7.61 vs. 6.86 for EnCodec) — is partly attributable to its higher bitrate. The paper does not acknowledge this mismatch or contextualize it. While DeCodec necessarily encodes two streams (speech + BGS) so a higher total bitrate is expected, the headline claim of "the highest SDR for speech reconstruction" is not fairly supported without a controlled comparison (e.g., matching total bitrate, or comparing against a baseline at 8.0 kbps). This is fixable with additional experiments or more careful framing.

### Minor

3. **Ambiguous SE inference procedure (Section 4.2.2).** The paper states that SE is performed by "replacing the background sound representations of the input noisy speech with the background sound representations of a blank audio with the same length." It does not specify how the blank audio's BGS representation is obtained — whether by passing a silent signal through the full encoder+SOP+NRVQ pipeline, by zeroing out the BGS branch, or some other mechanism. The decoder has been trained on summed speech+BGS inputs; if the blank BGS representation is non-zero (encoding silence characteristics), the inference distribution differs from training; if zero, it is out-of-distribution. The paper should provide a clear step-by-step description and ideally analyze whether this mismatch introduces artifacts.

4. **Undefined "angular matrix" in SOP derivation (Section 3.4).** The paper claims that when the covariance matrix YY^T "satisfies the angular matrix, indicating that the encoder extracts sufficiently diverse embeddings with different feature channels being mutually independent, we can obtain P_S P_N^T = 0." The term "angular matrix" is never defined, and the logical step from S N^T = 0 (enforced by L_⟂) to P_S P_N^T = 0 requires assumptions about YY^T that are not stated or verified. This weakens the theoretical grounding of the orthogonality constraint.

5. **Reconstruction quality trade-off not discussed (Table 4).** Ablation-1 (SOP only) achieves SDR-O of 8.93, while the full DeCodec drops to 5.21 — a 42% relative reduction. The paper mentions "a slight decrease in SDR" but this is a substantial drop. The added RST and SG components clearly harm raw reconstruction fidelity. While this trade-off is acceptable if the goal is decoupling, the paper should explicitly discuss why the full model sacrifices reconstruction quality and whether this degradation is avoidable.

6. **"Angular matrix" undefined (see point 4).** This is listed separately for completeness but is the same issue as point 4.

### Trivial

None.

## Nice-to-Haves

- **Codebook usage analysis.** Entropy or perplexity metrics for SRVQ and NRVQ would help verify that each branch is not storing cross-component information (information leakage), which would undermine the decoupling claim.
- **Intrusive perceptual metrics for SE.** Validation with ViSQOL or PESQ in addition to DNSMOS would strengthen the speech enhancement results, since DNSMOS is a non-intrusive proxy.
- **Statistical significance.** Reporting variance or confidence intervals for the main results (especially Table 1 and Table 2) would improve reliability.
- **Failure case analysis for SE and VC.** The one-shot VC WER of 50% (Table 3) is quite high; a discussion of when and why the method fails would be valuable.

## Removed Points

- **Theoretical derivation as a strength (Strength Finder point 4).** Removed because the derivation is flawed (see Weakness 1). The empirical evidence is what supports the method, not the proof.
- **Absence of statistical significance (Harsh Critic).** Removed because this is a generic criticism that applies to the vast majority of papers in this area; it is not a specific weakness of this paper.
- **Missing related works (Harsh Critic).** Cannot verify without external sources; removed per instructions.
- **Formatting/presentation/style nitpicks.** Removed per instructions.
- **Reproducibility concerns about undisclosed hyperparameters.** Not a specific weakness of this paper; most papers in this space report similar levels of detail.

## Novel Insights

The reviews surface a productive tension: the paper's claimed theoretical proof (Section 3.6) is unsound, yet the empirical ablation (Table 4) provides credible evidence that SOP+RST jointly achieve decoupling. This suggests the authors should lean on the empirical story and drop the theoretical guarantee framing. A second insight is that the paper's strongest result — beating dedicated SE models with a codec — is partly obscured by the bitrate fairness issue in the reconstruction comparison. If the authors were to run a matched-bitrate reconstruction experiment, the SE results would stand on their own as the paper's most surprising and valuable finding.

## Suggestions

1. **Remove or correct the "theoretical proof" in Section 3.6.** Replace the MVT argument with an intuitive explanation (e.g., the swap training forces the decoder to rely on each branch only for its own signal component) and cite the ablation as the primary evidence.
2. **Acknowledge the bitrate difference in Table 1 explicitly.** Add a sentence noting that DeCodec uses 8.0 kbps to encode two streams, and either add a matched-bitrate experiment or temper the claim of "highest SDR."
3. **Clarify the SE inference procedure.** Provide a step-by-step description of how the blank audio's BGS representation is obtained.
4. **Define "angular matrix" or remove the claim.** Either provide a clear definition with justification, or drop the derivation that P_S P_N^T = 0 follows from the orthogonality constraint.
5. **Discuss the SDR-O trade-off in the ablation.** Explicitly note that the full model's reconstruction quality is lower than SOP-only, and explain why this is acceptable given the decoupling gains.

## Score and Decision

**Bracketing pass (Round 1):** Three queries on "neural audio codec disentangled representation speech enhancement" with score bands (−1, 3.5), (3.5, 7.5), (7.5, 11). Weak anchors: TgRMixfAPK (3.33, HP-codec for BWE), FA2R2KwyTH (3.00, Speech Codecs Beyond Compression). Middle anchors: MDHVDfUrDz (4.00, CodecSep), kYkfCs4ZAH (5.67, FlexiCodec). Strong anchors: qOyF214xmg (8.00, Transducing LMs), kI27Niy4xY (8.00, Text-to-3D). The paper is clearly above the weak anchors (3–3.33) and well below the strong ones (8.0). Initial bracket: 3.5–6.0.

**Narrowing pass (Round 2):** Two queries covering (3.5, 5.5) and (5.5, 7.0). In the lower band: mrTTkF3LEM (4.00, XY-Tokenizer), dNUcKJEPTh (3.67, Kanade), lCaU7NlZ1I (5.00, Self-Guidance). In the upper band: kYkfCs4ZAH (5.67, FlexiCodec), JbLmIoWwDC (6.00, Gogo), RKzBRfV6J8 (5.60, Speech Separation Early Exits). DeCodec is stronger than XY-Tokenizer (4.00) and Kanade (3.67) — those papers have more limited experiments or incremental novelty — and comparable to Self-Guidance (5.00) in terms of contribution quality. However, DeCodec is weaker than FlexiCodec (5.67) and Gogo (6.00), which have more thorough evaluations, cleaner methodological contributions, and fewer rigor issues. The flawed theoretical proof and unmatched bitrate comparison are the main factors preventing DeCodec from reaching the upper band.

**Final score: 4.5.** This is a marginal reject. The paper has a genuinely novel idea (explicit speech–BGS decoupling in a codec, with strong empirical evidence from the ablation and SE experiments), but the two major weaknesses — an unsupported theoretical claim of a proof and an unfair reconstruction comparison — prevent acceptance in the current form. The paper could become a strong contribution with targeted revisions.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>