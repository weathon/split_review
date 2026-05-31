## Summary

DeCodec rethinks audio codecs as universal disentangled representation learners. It introduces a subspace orthogonal projection (SOP) module and a representation swap training (RST) procedure to decouple speech and background sound into orthogonal subspaces, and further uses semantic guidance (SG) to decompose speech into semantic and paralinguistic components within the speech subspace. The resulting codec enables controllable feature selection for multiple downstream tasks—speech enhancement, one-shot voice conversion, ASR, and TTS—from a single front-end, avoiding cascaded separation pipelines.

## Strengths

- **Novel and well-motivated problem framing.** The paper identifies a genuine gap: existing codecs entangle speech and background sound, and cascaded pipelines suffer from error propagation. The analogy to human auditory processing (A2 cortex) provides a compelling biological motivation for disentanglement in the representation domain.
- **Technically sound and principled method.** The SOP module enforces orthogonal subspaces via a trainable projection with an orthogonality loss, and the RST procedure is derived from a clean theoretical argument (subtraction of reconstructions) to guarantee that the subspaces capture independent sources. This is more principled than heuristic disentanglement losses.
- **Comprehensive ablation study.** Table 4 clearly demonstrates that neither SOP nor RST alone achieves decoupling, but their combination yields large gains in SDR-B and SDR-S. The addition of SG then further improves semantic preservation (lower WER*). This validates each component.
- **Strong empirical performance on multiple tasks.** DeCodec achieves top DNSMOS scores for speech enhancement, outperforming strong baselines including SELM and StoRM. It also enables one-shot VC with simultaneous denoising, and its reconstruction quality on noisy speech is competitive with existing codecs despite the added decoupling overhead.

## Weaknesses

### Fatal
None.

### Major
- **One-shot voice conversion evaluation is insufficient.** The reported WER of 50.46% is very high, indicating poor intelligibility. The comparison is limited to SpeechTokenizer-based methods; no state-of-the-art one-shot VC system (e.g., FreeVC, SVC) is compared, even using the same noisy input. The claim of “effective” voice conversion is therefore overstated without evidence that DeCodec’s output is practically usable for voice conversion.
- **Speech enhancement evaluation lacks standard intrusive metrics.** Only DNSMOS (non-intrusive) is reported. Metrics like PESQ, STOI, or SI-SNR are standard for SE and would allow fair comparison with the many methods that report them. The absence is a gap that weakens the SE claims, especially since DNSMOS is known to have domain biases.
- **Downstream ASR and TTS results are not presented in the main paper.** The title, abstract, and conclusion claim improved ASR robustness and controllable TTS, but the main text contains no quantitative evidence. The reader must rely on appendices that are stripped from the provided PDF. This makes the central claim of “universal front-end for multiple audio applications” only partially supported within the main paper.

### Minor
- **Assumption about the covariance matrix in the SOP derivation is strong.** The derivation that orthogonality of outputs implies orthogonality of projection matrices relies on *Y Y^T* satisfying the “angular matrix” condition (feature channels being mutually independent). It is not shown that the encoder actually produces such a covariance structure, which leaves a theoretical gap.
- **No direct comparison to simple alternative pipelines.** For example, one could apply a strong SE model (e.g., StoRM) to noisy speech and then pass the clean signal through SpeechTokenizer. This would be the most natural baseline but is not included. The marginal gain over StoRM-SpeechTokenizer in VC (WER 50.46 vs. 52.73) is small.
- **The total bitrate of 8 kbps (4+4) is relatively high.** While the focus is on representation learning rather than compression, this may limit practical deployment in bandwidth-constrained scenarios.

### Trivial
None.

## Nice-to-Haves

- Include standard SE metrics (PESQ, STOI) to strengthen the SE evaluation.
- Compare one-shot VC with SOTA VC methods (on clean speech, and also with a denoising front-end) to better contextualize performance.
- Report downstream ASR and TTS results directly in the main body to support the claimed universality.
- Provide visualizations of the orthogonal projections (e.g., correlation matrices) to verify the theoretical assumption about covariance.

## Novel Insights

Beyond the paper’s own contributions, the key insight is that decoupling can be achieved by combining orthogonal projection with a **representation swap** training procedure. This avoids explicit separation losses (which can cause distortion) and instead uses a self-supervised consistency argument that forces each subspace to encode only one source. This principle is likely transferable to other multi-source representation learning problems beyond audio.

## Suggestions

- Add a table with PESQ/STOI/SI-SNR for the SE task on the DNS test set.
- Improve the VC section by including a stronger baseline (e.g., FreeVC applied on the output of a denoising model) and reporting intelligibility metrics such as character error rate in addition to WER.
- If space permits, move a subset of downstream ASR/TTS results (e.g., a single table) from the appendix to the main paper.

## Score and Decision

The paper proposes a well-designed, principled method for disentangled audio representation learning and demonstrates promising results across several tasks. The major weaknesses are the narrow VC evaluation and the absence of downstream task results in the main text. However, the core contribution—an orthogonal projection plus swap training framework for source separation in the representation domain—is novel and valuable. With reasonable strengthening of the experiments, this work would make a strong contribution.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>