## Summary
DeCodec is a neural audio codec designed as a universal front-end for hierarchical audio representation. Unlike existing codecs that either treat sounds as a monolith (DAC, EnCodec) or focus strictly on clean speech components (FACodec), DeCodec decomposes audio into **speech** and **background sound (BGS)** subspaces using a **Subspace Orthogonal Projection (SOP)** module. Within the speech stream, it further separates **semantic** and **paralinguistic** information via semantic guidance and a **Representation Swap Training (RST)** procedure. This framework allows downstream tasks like speech enhancement and voice conversion to be performed purely through feature selection and recombination in the representation domain.

## Strengths
- **Hierarchical Disentanglement in a Unified Framework:** The model achieves three levels of granularity—Speech vs. Background and Semantic vs. Paralinguistic—within a single parallel RVQ architecture. This is validated by Table 3, where the model performs one-shot voice conversion on noisy speech while simultaneously performing speech enhancement, outperforming cascaded pipelines (StoRM-SpeechTokenizer).
- **Novel Representation Swap Training (RST):** The paper proposes a specific training protocol (Section 3.6) that swaps speech and noise components between different audio mixtures to enforce the physical meaning of the orthogonal subspaces. Experimental evidence in Table 4 shows that RST combined with the SOP module is necessary to achieve effective decoupling, significantly improving SDR for decoupled components compared to SOP alone.
- **Standout Speech Enhancement (SE) Performance:** The "zero-cost" SE achieved by zeroing out the noise subspace quantizers yields higher DNSMOS scores (3.39 OVL) than specialized SE models like StoRM (3.21) and SELM (3.26). This suggests that explicit representation-level orthogonality is highly effective for noise suppression.
- **Infrastructure for Diverse Use Cases:** The authors provide both causal and non-causal versions of the architecture. Table 2 shows that the causal DeCodec-c maintains high performance, outperforming existing non-causal diffusion-based baselines in background suppression (BAK 3.94 vs 3.38 for StoRM).

## Weaknesses

### Fatal
None.

### Major
- **Skewed Baseline Bitrate Comparisons:** In Table 1, DeCodec (operating at 4.0 + 4.0 = 8.0 kbps) is compared against baselines like DAC (4.5 kbps) and HiFi-Codec (2.0 kbps). Since bitrate significantly impacts reconstruction quality (SDR), it is unclear if DeCodec's performance advantage stems from its architectural innovations or simply its higher bit budget. A direct comparison with DAC or EnCodec constrained to a comparable 8.0 kbps is required to validate the claim that DeCodec maintains "advanced signal reconstruction" (Section 1).
- **High Word Error Rate in Voice Conversion:** The One-Shot VC results in Table 3 show a WER of **50.46**. While this is an improvement over the baseline (52.73), a WER exceeding 50% indicates that the synthesized speech is largely unintelligible. This undermines the primary claim that the semantic representation (Zc) is "clean" and robust enough for high-quality audio generation or task-aware feature selection (Section 1).

### Minor
- **Theoretical Circularity in Disentanglement Proof:** The theoretical proof in Section 3.6 (Equation 16) relies on the assumption that the system successfully minimizes the swap loss in a consistent way. Neural networks are prone to finding "shortcut" solutions where paralinguistic or noise cues are surreptitiously encoded in the "semantic" stream to assist reconstruction. The absence of a quantitative leakage metric (e.g., mutual information or cross-stream probing) makes the assertion of "complete decoupling" (Section 3.4) primarily speculative.
- **Limited Analysis of Non-Additive Distortions:** The SOP module assumes an additive noise model ($\mathbf{y} = \mathbf{s} + \mathbf{n}$ in Eq. 1). However, real-world audio often involves non-linear or convolutional distortions like reverb or clipping. While Table 2 includes real recordings, there is no explicit evaluation of whether the orthogonal projection naturally handles non-additive components, which limits the scope of the "universal" claim.

### Trivial
- **Metric Discrepancy in Noisy Scenarios:** In Table 1, the "Noisy Mel Distance" for DeCodec (0.81) is worse than DAC (0.69). While the paper acknowledges this, it qualifies the performance as "second only to DAC," but does not investigate why the model specifically underperforms on his metric while leading in SDR.

## Nice-to-Haves
- **Quantifying Information Leakage:** An explicit experiment measuring how much background information can be recovered from the speech quantizers (and vice versa) would provide stronger evidence for disentanglement.
- **Bitrate-Efficiency Curve:** Training a lower-bitrate version of DeCodec (e.g., 2+2 kbps) would allow for a fairer comparison with existing lightweight codecs.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Missing Appendix Results:** The reviewer mentioned back-end eval (ASR/TTS) was in the appendix; these were excluded as they are cited and assumed present in the full submission.
- **Ambiguity in "Back-end" evaluations:** Reclassified as Major due to high WER in VC, but the reviewer's specific point about the appendix being "not fully provided" is removed as per parser rules.

## Novel Insights
DeCodec's most significant contribution is the formalization of **Representation Swap Training (RST)** to anchor orthogonal subspaces to specific physical components (speech vs. noise). While subspace project is a common linear technique, applying it within a non-linear neural codec such that selective quantization acts as an "on-off switch" for specific audio streams is a valuable step toward making codecs useful as feature extractors. The synergy between SOP and RST provides a concrete mechanism to enforce physical meaning onto latent spaces that would otherwise remain entangled.

## Suggestions
- Conduct a bitrate-matched comparison at 8 kbps (e.g., DAC-8k) to isolate the benefits of the disentangled architecture from the increased capacity.
- Perform a visualization or probing study on the "residual paralinguistic" (Zr) component to define what acoustic features (e.g., emotion, prosody) are excluded from the semantic stream (Zc).

## Score and Decision

DeCodec is a well-motivated paper that addresses the limitation of current audio codecs in handling mixed speech/noise environments. The proposed SOP and RST methods are technically sound and show clear benefits for speech enhancement. However, the experimental evaluation is weakened by an unfair bitrate comparison in the core reconstruction table and a very high WER (50.46%) in the voice conversion task, which suggests that the "semantic purity" is still lacking.

**Calibration:**
- **Round-1 Bracket:** Between 4.5 and 6.5. 
  - *Anchor [1p6xFLBU4J] (Score 6.0):* GenSE similarly targets hierarchical SE via tokens. It has clearer semantic results but less novelty in the codec architecture itself compared to DeCodec's SOP/RST. DeCodec's multi-task nature (VC + SE + Codec) is ambitious, placing it in a similar range.
  - *Anchor [Id2JMVSQHZ] (Score 4.8):* USC disentangles speaker and semantic; it shares the high-level goal but is more specialized. DeCodec's focus on speech vs. background noise is more pragmatically useful for general audio codecs.
  - *Anchor [ale56Ya59q] (Score 7.0):* High-quality self-supervised SE; significantly more mature evaluation than DeCodec.

- **Round 2 Narrowing:** The paper's contribution to codec-based disentanglement is more original than [1p6xFLBU4J], but its failure to match bitrates in Table 1 is a significant methodological oversight that prevents it from reaching a 7.0. The WER in Table 3 also suggests the "universal" utility is partially overclaimed.

Compare to:
/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/1p6xFLBU4J.md (Score 6.0) - Similar hierarchical domain.
/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Id2JMVSQHZ.md (Score 4.8) - Similar disentanglement goal but DeCodec is more comprehensive.

The paper is stronger than the 4.8-5.0 anchors due to the novelty of RST and the strong SE results, but weaker than the 7.0 anchors due to evaluation gaps.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>