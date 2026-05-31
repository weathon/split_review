## Summary

DeCodec proposes rethinking neural audio codecs as universal disentangled representation learners for mixed audio. The system jointly decouples speech from background sound (BGS) using a Subspace Orthogonal Projection (SOP) module plus a Representation Swap Training (RST) procedure, and further decomposes speech into semantic and paralinguistic components via HuBERT-based Semantic Guidance (SG). This enables a single codec to serve as a front-end for speech enhancement, one-shot voice conversion on noisy speech, noise-robust ASR features, and controllable TTS background preservation.

---

## Strengths

- **Genuinely novel problem framing.** Prior work either used cascaded time-domain separation before codec encoding, or applied codec-based disentanglement only to clean speech. Tackling speech/BGS decoupling directly in the representation domain within a codec, and combining it with semantic/paralinguistic disentanglement, is a distinct contribution not previously demonstrated.

- **Technically coherent design.** SOP enforces geometric independence between speech and BGS subspaces (Eq. 5), while RST provides the cross-sample supervisory signal that anchors which subspace corresponds to which source (Eqs. 8–16). These two modules address complementary aspects of the problem and are meaningfully different in purpose; the ablation study (Table 4) confirms that both are necessary—SOP alone yields SDR-B of −13.15 dB, RST alone yields −10.67 dB, but their conjunction reaches +0.49 dB.

- **Strong SE results vs. dedicated models.** DeCodec achieves the highest DNSMOS OVL, SIG, and BAK on the DNS Challenge without-reverb test set, outperforming dedicated models StoRM, SELM, and InterSubNet (Table 2). Achieving competitive or superior SE performance as a *side capability* of a codec is compelling; the causal variant is already competitive with non-causal SELM.

- **Demonstrated advantage of representation-domain decoupling over cascade.** The VC experiment (Table 3) shows DeCodec (WER 50.46) outperforms the StoRM→SpeechTokenizer cascade (WER 52.73), providing empirical evidence that representation-domain decoupling loses less information than time-domain separation followed by re-encoding.

- **Thorough ablation.** Table 4 cleanly isolates SOP, RST, and SG contributions with multiple metrics (SDR-O, SDR-B, SDR-S, WER*), providing strong evidence that each module contributes to the claimed capabilities.

---

## Weaknesses

### Fatal
None.

### Major

1. **Bitrate imbalance in codec reconstruction comparison.** DeCodec operates at 8.0 kbps (4.0 speech + 4.0 BGS) while all baselines use 2.0–6.0 kbps. The higher bitrate provides more representational capacity, which partially explains the SDR advantage in Table 1. The paper does not analyze SDR at matched bitrates or discuss what happens when fewer RVQ layers are used. The headline claim of "highest SDR" is potentially attributable to this extra capacity rather than architectural merit alone.

2. **SE evaluation relies solely on DNSMOS.** DNSMOS is a non-intrusive perceptual metric that may systematically favor certain signal characteristics. Standard speech enhancement benchmarks also report PESQ, ESTOI, and CSIG/CBAK/COVL. The absence of intrusive signal-level metrics weakens the SE comparison, particularly for SIG scores where the proposed model is slightly below SELM on real recordings.

3. **Theoretical argument for RST contains an unverified assumption.** Section 3.6's "proof" that Z_s is independent of n invokes the mean value theorem (Eq. 16) and then argues that consistency requires the decoder's Jacobian ∂Dec/∂Zn to be independent of Z_s₁. This holds if the decoder is linear in Zn, but a deep convolutional decoder is nonlinear and the cross-term dependence is not ruled out. The argument is intuitive but not formally rigorous, and no empirical verification (e.g., mutual information estimates between Z_s and n) is offered.

4. **Voice conversion WER of ~50% is too high for claimed utility.** The VC WER of 50.46% approaches unintelligibility, and the explanation (misaligned voiced/unvoiced segments) raises the concern that the SRVQ-1 representation conflates prosodic timing with semantic content. No clean-speech VC baseline is provided to disentangle the contribution of noise robustness from the inherent intelligibility ceiling, making it difficult to assess how much of the high WER is fundamental vs. addressable.

### Minor

1. **Orthogonality constraint scope.** The loss L_⊥ = ‖⟨S, N⟩ − 0‖₂ penalizes the inner product of the output feature vectors but does not directly constrain the projection matrices P_S and P_N to be orthogonal projectors. The derivation in Section 3.4 requires YY^T to be an "angular matrix" (i.e., the encoder produces decorrelated channels), which is stated as a conditional but not empirically verified or encouraged by any loss term.

2. **BGS component quality not independently evaluated.** Controllable BGS in TTS is presented as a key application, but evaluation of the reconstructed BGS signal quality (e.g., SDR-B for background extraction alone, or a listening test) is not provided in the main paper.

3. **No WER in SE evaluation.** Since a primary motivation for SE is improving speech intelligibility for downstream ASR, reporting WER on the enhanced DNS test utterances would directly support the claimed ASR-robustness benefit.

### Trivial

- Minor notation inconsistency: the background sound RVQ is called NRVQ in the text body and BRVQ in the figure caption.

---

## Nice-to-Haves

- A bitrate-controlled ablation comparing DeCodec at 4.0 kbps total (fewer RVQ stages) against baselines at 4.0 kbps to cleanly isolate architectural gains from bitrate gains.
- Mutual information or correlation measurements between Z_s and the BGS signal n to empirically validate the disentanglement claims.
- A listening test for the SE and VC outputs to complement the objective metrics.

---

## Novel Insights

The most interesting insight beyond the listed contributions is the empirical finding that operating in the representation domain yields *better* speech/BGS separation quality than time-domain separation with state-of-the-art diffusion models (StoRM), even when the codec includes a lossy quantization step. This suggests that the discretization bottleneck in RVQ, often treated as a fidelity cost, can actually serve as an information filter that discards cross-component information leakage—an observation with implications for designing future multi-task audio models. The orthogonal subspace framing also offers a principled geometric lens through which to view the disentanglement problem, distinguishing this from ad hoc multi-head designs.

---

## Suggestions

- Provide a bitrate-matched reconstruction comparison (e.g., DeCodec at 4 kbps total with 2+2 or a single 4 kbps codec) to address the fairness concern directly.
- Add PESQ and ESTOI to the SE evaluation table to give intrusive quality measures alongside DNSMOS.
- Include empirical validation of the orthogonality claim: plot the cosine similarity distribution between S and N embeddings across the test set to show how close to orthogonal the trained model achieves.
- Report VC results on clean speech to establish a ceiling, then show the degradation in noisy conditions, making the noise-robustness advantage quantifiable.

---

## Score and Decision

DeCodec addresses a well-motivated gap—none of the existing universal codecs handle mixed noisy speech with explicit representation-level disentanglement—and the proposed SOP+RST combination is technically sound and empirically validated. The SE results outperforming dedicated SE models are particularly strong. The main concerns (bitrate unfairness, single-metric SE evaluation, formal proof gap, high VC WER) are real but do not undermine the paper's core contribution; they are addressable through additional experiments or clarification. The work will be of genuine interest to the audio representation learning, codec design, and multi-task audio processing communities.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>