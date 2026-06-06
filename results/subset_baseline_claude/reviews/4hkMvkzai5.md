## Summary

DeCodec proposes a neural audio codec that simultaneously disentangles speech from background sound, and further decomposes speech into semantic and paralinguistic components. The two core technical innovations are: (1) a Subspace Orthogonal Projection (SOP) module that projects the encoder's mixed audio embedding into two orthogonal subspaces, and (2) a Representation Swap Training (RST) procedure that cross-pairs speech representations from one sample with background sound representations from another sample, supervising reconstruction of the swapped mixture. These two components are combined with semantic guidance (HuBERT supervision on the first SRVQ layer) to yield hierarchical disentanglement. The codec is evaluated on reconstruction, speech enhancement, and one-shot voice conversion tasks, with ablation studies validating each component.

---

## Strengths

- **Novel disentanglement paradigm**: Treating the codec itself as a universal disentangled representation learner rather than prepending a dedicated separation front-end is conceptually appealing and well-motivated; the three claimed advantages (no front-end distortion, unified representation domain, single-pass feature selection) are compelling.

- **Clever self-supervised training via RST**: The representation swap training creates natural supervision for disentanglement without requiring explicit separation labels at inference time. The idea of reconstructing a cross-paired signal (speech from sample A + BGS from sample B) and minimizing the L1 error against the expected hybrid mixture is elegant and practical at scale.

- **Strong speech enhancement results**: Table 2 shows DeCodec outperforming three dedicated SE systems (Inter-SubNet, StoRM, SELM) on the DNS Challenge test set in OVL and BAK metrics, including in the causal regime—without being trained as a specialist SE model. This is a genuinely impressive result that validates the claim that representation-domain decoupling can serve as a competitive alternative to time-domain separation.

- **Thorough ablation study**: Table 4 clearly demonstrates that neither SOP alone (Ablation-1, SDR-B = –13.15 dB) nor RST alone (Ablation-2, SDR-B = –10.67 dB) is sufficient for disentanglement, while their combination (Ablation-3) substantially improves both SDR-B and SDR-S. This well isolates the contribution of each component.

- **Causal version**: Providing a causal DeCodec-c that matches EnCodec in reconstruction SDR and approaches SELM in SE quality (both non-causal baselines) is a practical contribution for streaming/real-time scenarios.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unfair bitrate comparison in Table 1**: DeCodec uses parallel SRVQ (4.0 kbps) + NRVQ (4.0 kbps) for a total of 8.0 kbps, while all baselines operate at 2.0–6.0 kbps. The highest SDR figures for DeCodec may simply reflect greater bit-budget rather than superior codec design or disentanglement. The paper should include an analysis showing the disentanglement and reconstruction gains are not solely attributable to doubled capacity—e.g., a matched-bitrate ablation or per-stream rate ablation.

2. **Train-test mismatch in semantic guidance**: Equation 7 computes the SG loss using HuBERT features of the *clean speech* **s**, not the noisy mixture. At inference time on noisy audio, the clean speech is unavailable, yet the SRVQ is supposed to produce noise-robust semantic representations. The paper does not explain how this gap is bridged or validate that the SG supervision on clean speech adequately generalizes to noisy inputs.

3. **Logical gap in the theoretical proof (Section 3.6)**: The proof argues that minimizing Equation (12) forces Zs to be independent of **n**. The key step invokes the mean value theorem and asserts "the left side depends on Zs₁ through ξ"—but ξ is defined as a point between Zn₁ and Zn₂, so it is not obviously a function of Zs₁. This makes the conclusion that Zs₁ must be independent of **n₁** logically incomplete. The empirical results in Table 4 are convincing, but the theoretical justification as written does not fully hold.

### Minor

1. **Marginal VC improvement over the cascade baseline**: In Table 3, DeCodec achieves WER 50.46 vs StoRM-SpeechTokenizer's 52.73—a difference of ~2 WER points. The paper claims this shows an "advantage," but the absolute performance level is poor and the margin is within typical evaluation noise. Additionally, DeCodec performs VC+SE (outputting no background sound), while SpeechTokenizer-based methods don't remove background; the SIM comparison is therefore measuring different outputs.

2. **Downstream ASR/TTS results are in the appendix**: The paper's central claim is that DeCodec serves as a "universal front-end" for downstream tasks, yet the ASR and TTS evaluations are deferred to Appendix F/G and cannot be assessed here. The main paper's evidence for the "universal" claim rests primarily on SE and VC alone.

### Trivial

- Equation (5) writes the orthogonality loss as ‖⟨S, N⟩ – 0‖₂, which is redundant; this simplifies to ‖⟨S, N⟩‖₂. Minor presentation issue.

---

## Nice-to-Haves

- A matched-bitrate ablation (e.g., 4.0 kbps total split between SRVQ and NRVQ) compared against DAC/SpeechTokenizer at the same bitrate would directly address the fairness concern in Table 1.
- Showing ASR downstream performance with and without the SG component on noisy test data (not just the ablation WER* metric) would be more informative than the current footnote to an appendix.
- A visualization of the learned subspaces (e.g., t-SNE of S vs N embeddings separated by source type) would strengthen the disentanglement claim.

---

## Novel Insights

The Representation Swap Training procedure is a genuinely novel training strategy: rather than requiring paired clean/noisy data or explicit signal separation, it constructs cross-paired supervision signals by swapping the background sound subspace across samples and minimizing reconstruction loss against the corresponding composite ground truth. This implicitly forces the two subspaces to be semantically aligned with their respective sources without any source-level labels at inference time. The approach generalizes ideas from cross-modal swap training (common in style transfer and voice conversion research) into the codec domain, and represents a principled way to impose source-specific semantics on otherwise unconstrained orthogonal projections.

---

## Suggestions

- Provide either a per-stream bitrate ablation or a matched-total-bitrate version of DeCodec in Table 1 to address the fairness concern.
- Clarify in the text exactly how the HuBERT semantic guidance loss is applied during training when only mixture audio is available—does the model require access to oracle clean speech **s** during training, and if so, describe the data pipeline clearly.
- Fix the theoretical proof in Section 3.6 by making explicit how ξ depends on Zs₁, or replace the informal proof with a more rigorous treatment.
- Move key ASR/TTS results (even a summary table) to the main paper to fully substantiate the universal front-end claim.

---

## Score and Decision

DeCodec presents a genuinely novel codec-level disentanglement paradigm with a creative training procedure and strong speech enhancement results that hold up against dedicated SE baselines. The bitrate comparison issue and the theoretical gap are real concerns but do not invalidate the SE findings or the ablation evidence for the disentanglement mechanism. The paper introduces ideas that are sufficiently novel and practically useful to merit community attention, conditional on the authors addressing the bitrate fairness issue and clarifying the semantic guidance training setup.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>