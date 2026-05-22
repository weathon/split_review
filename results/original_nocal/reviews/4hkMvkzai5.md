Now I have all the evidence I need. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

Here is my consolidated review:

## Summary

DeCodec proposes a neural audio codec that learns hierarchically disentangled representations, decomposing mixed audio into orthogonal speech and background-sound subspaces via a subspace orthogonal projection (SOP) module and a representation swap training (RST) procedure, and further decomposing speech into semantic and paralinguistic components via semantic guidance (SG). The key idea is to replace the traditional cascaded speech separation + downstream processing pipeline with a single codec whose representations can be selectively combined for tasks including reconstruction, speech enhancement, voice conversion, ASR, and TTS.

## Strengths

1. **Novel architecture for hierarchical disentanglement in a single codec.** DeCodec is the first codec to jointly disentangle (a) speech vs. background sound and (b) within-speech semantic vs. paralinguistic information in a unified framework (Section 3.2, Figure 2). Prior codecs either ignore the speech/BGS distinction entirely (EnCodec, DAC) or only handle clean speech (SpeechTokenizer). The ablation study (Table 4) confirms that the full combination (SOP+RST+SG) achieves SDR-S of 6.73 dB and WER\* of 23.6, demonstrating both decoupling and semantic preservation.

2. **Speech enhancement via representation recombination achieves the highest DNSMOS BAK scores among all baselines, including dedicated SE models.** By replacing the BGS quantized vector with a silent representation, DeCodec achieves BAK scores of 4.13 (simulated) and 3.99 (real recordings) in Table 2 — the highest among all baselines including InterSubNet, StoRM, and SELM. This provides concrete evidence that the speech subspace is effectively clean of background sound, which is the practically important direction for SE.

3. **Convincing ablation study showing both SOP and RST are necessary.** Table 4 demonstrates that SOP alone (Ablation-1: SDR-B = -13.15) or RST alone (Ablation-2: SDR-B = -10.67) fail at decoupling, but their combination (Ablation-3: SDR-B = 0.49, SDR-S = 7.90) yields meaningful improvements. This provides strong empirical support for the method's design.

4. **Competitive codec reconstruction quality despite decoupling modules.** DeCodec achieves SDR of 7.61 dB (clean) and 5.21 dB (noisy) in Table 1, outperforming or matching baselines like EnCodec (6.86/4.88) and DAC (0.60/-1.62). The causal variant also achieves 6.79/4.62, demonstrating practical viability.

5. **One-shot VC on noisy speech outperforms the cascaded denoising+VC pipeline.** DeCodec achieves WER 50.46% vs. StoRM+SpeechTokenizer's 52.73% (Table 3), suggesting that representation-domain recombination introduces less distortion than time-domain separation cascades. The SG module also demonstrably reduces WER\* from 41.9 (Ablation-3, no SG) to 23.6 (DeCodec, non-causal) in Table 4.

## Weaknesses

### Major

- **The "theoretical proof" of decoupling in Section 3.6 is heuristic, not rigorous, and should not be presented as a proof.** The argument uses the mean value theorem on a neural decoder (which is not everywhere differentiable with ReLU activations) and treats approximate equations (≈) as exact equalities. The core logical step — "the left side depends on Zs₁ through ξ, while the right side is independent of Zs₁, therefore Zs₁ must be independent of n₁" — does not follow from the MVT alone. The "proof" essentially asserts that if the RST loss is minimized (Eq. 12), then the swap must have worked, which is circular. This does not invalidate the empirical approach, but the paper should not claim a formal guarantee. The empirical evidence (SE results, ablation) is what actually supports the method.

- **SDR-B values are negative or near-zero, indicating that the background-sound reconstruction from the BGS subspace is essentially failing.** For the full model, SDR-B = -0.36 dB (non-causal) and -1.11 dB (causal). Even the best case (Ablation-3: 0.49 dB) is barely positive. A negative SDR means the reconstruction error exceeds the signal energy. This directly undermines the claim of "explicit decoupling of speech and background sound" as a bidirectional property: while the speech subspace is demonstrably clean of BGS (evidenced by strong SE results), the BGS subspace does not capture background sound well. The paper glosses over this asymmetry and should explicitly discuss it as a limitation.

### Minor

- **The decoupling metrics (SDR-B, SDR-S) are underspecified.** The paper states these are "signal distortion ratios for reconstructing... decoupled background sound, and decoupled speech" (around Table 4) but does not explain the exact procedure. Is it computed by passing only the BGS (or speech) quantized vectors through the decoder and comparing to ground-truth components? Without this detail, the numbers in Table 4 are not fully interpretable or reproducible.

- **One-shot VC WER of 50.46% is very high, indicating the method is far from practical for this task.** While DeCodec outperforms StoRM+SpeechTokenizer (52.73%), the absolute performance is poor — half the words are incorrect. The paper's explanation ("different speech segment voicing times") is acknowledged as speculative. This does not invalidate the paper but weakens the VC application claim.

- **The term "angular matrix" in Section 3.4 is used but never defined.** The paper states: "When the covariance matrix YY^T satisfies the angular matrix, indicating that the encoder extracts sufficiently diverse embeddings with different feature channels being mutually independent..." This is an undefined technical term; the reader cannot assess whether this condition plausibly holds.

- **The figure caption for Figure 2 says "The input y is split into two encoders" while the text describes a single encoder.** From Equation (8) (Enc(y₁₁), Enc(y₂₂)), it's clear this is the same encoder applied to two inputs during RST training. The figure caption is misleading but the architecture is discernible from the text.

### Trivial

- The paper uses "donates" instead of "denotes" (Section 3.5).
- Section 4.2.4 typo: "SOP vlock" should be "SOP module."

## Nice-to-Haves

- Add baselines for SDR-B/SDR-S from a speech separation model (e.g., Conv-TasNet) evaluated on the same reconstruction task. This would contextualize whether 0.49 dB is typical for comparable settings.
- Include an oracle experiment: reconstruct ground-truth clean speech and BGS through the encoder-decoder separately to establish the reconstruction ceiling for each component.
- Provide t-SNE or PCA visualizations of the S and N subspaces to qualitatively show the decoupling.
- Analyze failure cases for VC to support or refute the "voicing time" hypothesis.

## Removed Points

- **"SE comparison is structurally unfair because DeCodec also does compression"** — Removed because this asymmetry disfavors DeCodec (it does compression + SE simultaneously), not the baselines. DeCodec winning despite the extra compression burden is a strength, not a weakness. The criticism cuts the wrong direction.
- **"Architecture ambiguity suggests the method is partially unreproducible"** — Demoted to Minor. The figure caption saying "two encoders" is misleading, but the text (Section 3.3) and equations (Eq. 8: Enc(y₁₁), Enc(y₂₂)) clarify this is a single encoder applied to two inputs during RST training.
- **"Table 4 SDR-B being barely positive indicates decoupling is extremely weak"** — The critic's framing was overly absolute. The asymmetry (good speech direction, poor BGS direction) is the real issue, already captured above.
- **"Missing decoupling baselines"** — Moved to Nice-to-Haves. While would strengthen the paper, the lack of baselines doesn't invalidate the internal comparison (ablation).
- **"The brain analogy adds no technical substance"** — Removed. Many papers use loose biological analogies; this is a style choice, not a technical weakness.
- **General section-by-section editing notes** (e.g., "Section 1: the motivation...") — Removed as they are minor style/scope preferences rather than verifiable weaknesses.

## Novel Insights

The most interesting observation emerging from the cross-review is the **asymmetric nature of the decoupling**: the speech subspace is convincingly free of background sound (evidenced by BAK=4.13 in SE), yet the BGS subspace reconstructs poorly (SDR-B ≈ -0.36 dB). This suggests the SOP+RST mechanism may be preferentially allocating capacity to the speech subspace, possibly because the L₁ reconstruction loss and the RST loss together privilege the higher-energy speech component. The paper does not explore this asymmetry but it is a practically important phenomenon: for SE (the paper's strongest application), only the clean speech direction matters, while for applications needing BGS extraction (e.g., soundscape reconstruction), the current approach is inadequate.

## Suggestions

1. Either remove or substantially rewrite Section 3.6's "theoretical proof." Frame it as a **heuristic justification** for why minimizing the RST loss encourages disentanglement, not as a formal guarantee. This would be more honest and prevent alienation of mathematically rigorous reviewers.
2. Explicitly acknowledge and analyze the asymmetry in decoupling quality: the speech subspace is clean, but the BGS subspace reconstruction is poor. Discuss whether this is a fundamental limitation or addressable (e.g., with higher bitrate allocation to BRVQ).
3. Clarify the exact computation of SDR-B and SDR-S — specify which decoder inputs are used and which ground-truth references.
4. Define "angular matrix" or remove the term and replace with a clearer condition.
5. For the VC results, provide failure-case analysis and report the WER of unprocessed noisy speech to establish context for the 50.46% figure.

## Score and Decision

The paper introduces a genuinely novel architecture with practical value (especially for SE), but overstates its central claim. The "theoretical guarantee" of decoupling is heuristic, and the SDR-B values indicate that bidirectional decoupling is not achieved — only the speech direction is well-supported by evidence. The contributions are real but the claims need substantial tempering.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>