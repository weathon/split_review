Here is my final consolidated review:

---

## Summary

DeCodec proposes reframing audio codecs as universal disentangled representation learners. The key idea is to introduce a Subspace Orthogonal Projection (SOP) module that factorizes mixed audio embeddings into speech and background sound subspaces, and a Representation Swap Training (RST) procedure that forces these subspaces to correspond to speech and background sound, respectively. Within the speech subspace, Semantic Guidance (SG) further decomposes speech into semantic and paralinguistic components. This hierarchical disentanglement enables a single codec to perform reconstruction, speech enhancement (by blanking the BGS quantizer), one-shot voice conversion (by swapping residual quantizers), and to serve as a feature extractor for downstream ASR and TTS — all demonstrated empirically.

## Strengths

- **Novel and well-motivated problem framing:** Rethinking audio codecs as disentangled representation learners for mixed speech+background audio is a genuinely new direction. The idea of factorizing mixed audio into orthogonal subspaces within a single codec is creative and practically relevant. Unlike prior codecs that either entangle everything (EnCodec, DAC) or only handle clean speech (SpeechTokenizer), DeCodec explicitly targets the real-world setting of mixed speech and background sound.

- **SOP+RST combination is empirically shown to enable decoupling:** The ablation study (Table 4) is the paper's strongest evidence. Neither SOP alone (SDR-B: -13.15) nor RST alone (SDR-B: -10.67) yields meaningful decoupling, but their joint use (Ablation-3) achieves SDR-B: 0.49 and SDR-S: 7.90 — a clear jump that demonstrates the combination is necessary and suffices for coarse speech/BGS separation. The subsequent addition of SG (DeCodec-c) reduces WER* from 41.9 to 25.8, confirming that semantic decomposition builds on top of the speech/BGS disentanglement.

- **Single model outperforms cascaded pipelines on speech enhancement:** In Table 2, DeCodec achieves the highest DNSMOS OVL (3.39 simulated, 3.13 real) and BAK (4.13 simulated, 3.99 real), surpassing dedicated SE models including StoRM and SELM. This validates that representation-domain decoupling is practically competitive with time-domain separation methods. The causal variant also performs well (BAK 4.09/3.94), suggesting real-time feasibility.

- **Causal variant maintains strong performance:** The causal DeCodec-c achieves SDR 6.79/4.62 on clean/noisy speech (Table 1), DNSMOS BAK 4.09/3.94 (Table 2), and comparable decoupling to the non-causal version. This practical consideration is valuable for deployment.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical proof that RST guarantees disentanglement (Section 3.6) is mathematically unsound.** The paper claims a proof via the mean value theorem for vector functions, asserting existence of a single ξ such that ∂Dec/∂Zn|_ξ (Zn₂−Zn₁) ≈ n₂−n₁ (Equation 16). The mean value theorem for vector-valued functions does not guarantee exact equality of this form — it only yields an inequality via the mean value inequality (||f(b)−f(a)|| ≤ sup||J(ξ)||·||b−a||). The paper's argument that the left side "depends on Zs₁ through ξ" while the right side does not, therefore forcing independence, does not follow from the stated mathematics. This does not invalidate the method (RST is a reasonable empirical loss), but the paper presents it as a formal guarantee, which overstates what is justified. The authors should present RST as a heuristic training objective supported by empirical evidence, not by this proof.

2. **Unfair bitrate confound in reconstruction comparisons (Table 1).** DeCodec uses 4.0+4.0 = 8 kbps, while EnCodec uses 6 kbps, DAC uses 4.5 kbps, and SpeechTokenizer uses 4 kbps. Higher bitrate directly benefits SDR, Mel Distance, and WER. The paper does not compare against a high-bitrate variant of DAC (12 kbps exists) or EnCodec (12 kbps exists) at matched bitrate. Therefore, the headline reconstruction advantage in Table 1 (SDR 7.61 vs. 6.86 for EnCodec) cannot be attributed to the proposed disentanglement mechanism — it may simply reflect the extra bandwidth. This is the most consequential weakness because it conflates the method's core innovation with a trivial resource advantage.

3. **Decoupling quality is weak — the background sound representation, when decoded alone, has very low fidelity.** For the full non-causal DeCodec, SDR-B is −0.36 dB; for the causal variant, −1.11 dB. Even Ablation-3 (SOP+RST, no SG) only achieves SDR-B of 0.49 dB. These numbers indicate that isolated BGS reconstruction is of very poor quality — barely above noise floor. While some degradation is expected from quantization, the paper's claim of "explicit decoupling representation" implies both directions should work. The paper also does not clearly specify how SDR-B and SDR-S are computed (e.g., are they obtained by running only one quantizer through the decoder? The decoder was never trained on single-quantizer inputs). This lack of specification is a reproducibility concern.

4. **The undefined "angular matrix" term in the SOP derivation (line 112).** The paper states "When the covariance matrix Y Y^T satisfies the angular matrix" without defining what an "angular matrix" is. This step is central to the claim that orthogonality of the projections is guaranteed, but the reasoning is opaque. This should either be formalized or removed.

### Minor

1. **One-shot VC WER of 50.46% is very high** — nearly half the words are wrong. While the paper acknowledges voicing mismatch as a cause, the claim of "effective one-shot voice conversion" is not supported by this metric. The comparison to StoRM-SpeechTokenizer (52.73% WER) shows relative advantage but both numbers are too high for practical use.

2. **Ablation shows a non-trivial trade-off between decoupling and reconstruction quality** that is not analyzed. Overall SDR-O drops from 8.93 (Ablation-1, SOP only) to 6.68 (Ablation-3, SOP+RST) to 4.62 (DeCodec-c). Adding SG further degrades SDR. The paper should discuss the cost of achieving controllability and whether this trade-off is necessary or could be mitigated.

3. **The A2 cortical analogy is overstated.** The paper repeatedly claims to "simulate" left and right hemispheres, but the actual architecture (linear projection layers + RVQs) has no neuroscientific link to A2 beyond the conceptual parallel. This is fine as inspiration but the framing of "simulation" claims more than is delivered.

### Trivial

None.

## Nice-to-Haves

- An equal-bitrate ablation: train DAC or EnCodec at 8 kbps (by adding residual quantizers) and compare reconstruction metrics to isolate the effect of disentanglement from the effect of bandwidth.
- Empirical measurement of information leakage (e.g., running ASR on the BGS-only reconstruction to check how much speech leaks into the BGS quantizer).
- Visualization (t-SNE/PCA) of speech and BGS embeddings from mixed samples to qualitatively confirm orthogonality.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Missing downstream ASR/TTS results (Harsh Critic point 4).** The reviewer notes that ASR robustness and TTS controllability are deferred to Appendices F/G. Per the instructions, these sections were stripped by the parser and exist in the original submission. Removing this criticism.
2. **Strength Finder's claim about theoretical grounding.** It claims Section 3.6 provides rigorous proof for disentanglement. Since the theoretical proof is verified as unsound (Weakness M1), this strength conflicts with a verified weakness and is dropped per instructions.
3. **Criticisms about "not yet released" or reproducibility concerns rooted in entity existence.** None applicable.
4. **Generic strengths from Strength Finder.** None that were dropped beyond the theoretical proof strength above.

## Novel Insights

The most interesting observation emerging from this review is the gap between what the paper claims theoretically (that RST provably guarantees disentanglement) and what it actually achieves empirically (modest decoupling with SDR-B near 0 dB). This tension suggests that the SOP+RST combination works, but as a heuristic alignment mechanism rather than a theoretically grounded factorization. The ablation study is actually the paper's strongest contribution — it cleanly shows that neither SOP nor RST works alone, and their combination produces a qualitative jump in decoupling. This empirical result is far more convincing than the attempted proof. The paper would be significantly stronger if it leaned into this empirical story, controlled for bitrate, and acknowledged the modest fidelity of the BGS channel as a limitation to be addressed in future work (e.g., by increasing BGS quantizer capacity).

## Suggestions

1. **Control for bitrate.** Retrain DAC or EnCodec with additional residual quantizers to match 8 kbps, or train DeCodec at a lower bitrate to match baselines. Without this, the reconstruction comparisons are uninterpretable.
2. **Remove or rewrite the theoretical "proof" in Section 3.6.** Present RST as a self-supervised training objective justified by empirical results. The current attempted proof is mathematically invalid and will be rejected by any reviewer who reads it carefully.
3. **Clarify how SDR-B and SDR-S are computed** — specify the exact evaluation protocol (e.g., whether only one quantizer is passed through the decoder, and whether this is an in-distribution input for the decoder).
4. **Define "angular matrix" or remove the claim.** The SOP derivation should be mathematically complete and self-contained.
5. **Bring the downstream ASR and TTS results into the main paper** (at least a summary table) since these are central to the claimed contribution.
6. **Discuss the reconstruction-decoupling trade-off** more explicitly. The SDR-O drop from Ablation-1 to DeCodec is substantial (8.93 → 5.21/4.62), and understanding whether this is fundamental or addressable is important for the community.

---

## Score and Decision

**Calibration anchors (from retrieval batch):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/17DNmdQ9aU.md` (StableToken) | 7.50 | Stronger paper — cleaner methodology, more rigorous evaluation, SOTA claims well-supported. DeCodec has a more novel problem framing but weaker execution. |
| `/home/wg25r/review_agent/human_reviews_2026/JbLmIoWwDC.md` (Gogo) | 6.00 | Stronger paper — better controlled experiments, clearer story. DeCodec's novel idea of cross-modal (speech+BGS) disentanglement is more ambitious but less thoroughly validated. |
| `/home/wg25r/review_agent/human_reviews_2026/MDHVDfUrDz.md` (CodecSep) | 4.00 | Similar score band. CodecSep has cleaner execution but less novel framing. DeCodec's idea is more original, but CodecSep doesn't have a flawed proof or bitrate confound. |
| `/home/wg25r/review_agent/human_reviews_2026/TgRMixfAPK.md` (HP-codecX) | 3.33 | Weaker paper — insufficient methodological detail, missing baselines. DeCodec has stronger evidence for its core claim (ablation study) and a clearer contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/nfOnCngWtp.md` (Perceptual Neural Video Compression) | 4.00 | Similar tier of contribution. Different domain but comparable in terms of having a clever idea with some execution gaps. |
| `/home/wg25r/review_agent/human_reviews_2026/FA2R2KwyTH.md` (Speech Codecs Beyond Compression) | 3.00 | Weaker paper — severe data mismatch issue undermined the entire evaluation. DeCodec's evaluation is more internally consistent despite the bitrate confound. |

The paper's core idea — decoupling speech and BGS within a codec — is genuinely novel and practically motivated. The ablation study cleanly validates the SOP+RST mechanism, and the SE results are strong. However, the paper has three significant weaknesses that prevent acceptance: (1) the attempted theoretical proof is mathematically invalid and the paper overstates what is justified; (2) the reconstruction comparisons are confounded by a large bitrate disparity (8 kbps vs. 4–6 kbps), so the claimed reconstruction advantage cannot be attributed to the method; (3) the decoupling quality is modest (SDR-B near 0 dB) and the evaluation protocol for it is underspecified. These issues can be addressed in revision, but the paper in its current form does not meet the bar.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>