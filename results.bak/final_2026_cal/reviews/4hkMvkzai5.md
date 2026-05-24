Now I have all the information needed to write the consolidated review. Let me produce it.

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

Let me write the final review now.

---

**Calibration Report:**

Round 1 bracket: 3.5–5.5

Round 2 anchors read in full:
- TgRMixfAPK (3.33): HP-CodecX — disentangled codec for bandwidth extension. Rejected. DeCodec has stronger empirical validation (cleaner ablation, SE/VC experiments).
- FA2R2KwyTH (3.00): AR-regularized codec. Withdrawn. DeCodec is clearly stronger in novelty and evaluation scope.
- MDHVDfUrDz (4.00): CodecSep — codec-based sound separation. Mixed reviews (4,2,8,2). Comparable evaluation quality; DeCodec has more novel contribution.
- mrTTkF3LEM (4.00): XY-Tokenizer — semantic-acoustic codec. Mixed (2,6,4,6,2). DeCodec has cleaner ablation and more convincing novelty.
- lCaU7NlZ1I (5.00, Reject): Self-Guidance — marginal improvements to codec fidelity. DeCodec has a more novel contribution but suffers from similar evaluation gaps.
- kYkfCs4ZAH (5.67, Accept): FlexiCodec — dynamic frame rate codec. More thorough evaluation (downstream TTS in main paper, demo, code release). DeCodec is weaker in evaluation completeness.
- JbLmIoWwDC (6.00, Accept): Gogo — granularity-ordered codec. Stronger evaluation. DeCodec doesn't match this rigor.

Final score: 4.5 — the paper has a genuinely novel technical approach (SOP+RST) and the ablation study convincingly shows the joint method enables decoupling. However, two significant evidence gaps prevent acceptance: (1) the abstract's ASR and TTS claims are unsupported in the main paper, and (2) the RST "proof" is not rigorous. The decoupling evaluation lacks separation baselines, and SDR-B values near 0 dB raise questions about practical utility.## Summary

DeCodec proposes a neural audio codec that hierarchically disentangles audio into speech vs. background sound subspaces (via Subspace Orthogonal Projection + Representation Swap Training) and within speech into semantic vs. paralinguistic components (via semantic-guided RVQ). The goal is a single codec that serves as a universal front-end for reconstruction, speech enhancement, voice conversion, ASR, and TTS. The core technical ideas (SOP, RST, SG) are well-motivated and the ablation study confirms their joint necessity.

## Strengths

1. **Novel joint design (SOP+RST) achieves explicit speech–background sound decoupling in a codec.** The ablation study (Table 4) is the strongest evidence: SOP alone gives SDR-B = –13.15 dB, RST alone gives –10.67 dB, but SOP+RST together jump to 0.49 dB (non-causal) / –1.11 dB (causal). This ~13 dB improvement demonstrates that the *combination* of orthogonal projection and swap training is what forces the subspaces to specialize, not either component individually. Prior codecs do not report any such decoupling metric.

2. **Representation-based SE achieves the best background suppression among all compared methods.** On the DNS Challenge test set (Table 2), DeCodec achieves BAK scores of 4.13 (synthetic) and 3.99 (real recordings), outperforming discriminative (Inter-SubNet: 3.82/3.57), diffusion (StoRM: 3.94/3.38), and transformer (SELM: 4.10/3.44) models. This shows that the decoupled representation allows cleaner background removal than any time- or spectrogram-domain SE model tested.

3. **Competitive reconstruction fidelity while adding decoupling modules.** Despite the extra SOP and parallel RVQ components, DeCodec achieves the highest SDR on both clean (7.61 dB) and noisy (5.21 dB) speech among all codec baselines (Table 1), demonstrating that the disentanglement does not substantially compromise signal reconstruction.

4. **Causal variant with practical performance.** DeCodec-c (causal) achieves SDR 6.79 dB (clean), DNSMOS OVL 3.31, and BAK 4.09 — competitive with non-causal models — making it applicable to low-latency scenarios.

## Weaknesses

### Major

1. **ASR and TTS results claimed in the abstract are absent from the main paper.** The abstract states "improved ASR robustness through clean semantic representations, and controllable background sound preservation/suppression in TTS." Section 4.2 explicitly delegates these to Appendix F and G, which are not available in the main text. A reader cannot verify whether the codec's semantic representations actually improve ASR on noisy speech, or whether the TTS system can selectively preserve/suppress background sound. Claims in the abstract and introduction must be supported in the main paper.

2. **The RST "proof" (Section 3.6, Equations 13–16) is not rigorous and is overclaimed.** The paper says "Here, we theoretically prove that the proposed L_RST can further force Zs... to be speech representations only." The argument uses the mean value theorem for vector functions to relate decoder output differences to noise differences, concluding that Zs must be independent of noise. This reasoning has two issues: (a) the standard mean value theorem does not hold for vector-valued functions in the simple form presented (a single interior point ξ); the integral form would apply, which complicates the argument. (b) Even setting that aside, the Jacobian ∂Dec/∂Zn evaluated at (Zs₁, ξ) depends on Zs₁, so the claimed independence does not follow from the stated equations. The method may work empirically (the ablation supports it), but presenting this as a formal proof is misleading. The authors should either provide a correct theoretical justification or clearly describe the argument as an intuitive sketch supported by empirical evidence.

3. **Missing baselines for evaluating decoupling quality.** The paper reports SDR-B and SDR-S (Table 4) but does not compare against any speech separation baseline (e.g., a simple mask-based separation, a light-weight separation model, or an oracle ideal binary mask). Without this comparison, the absolute SDR-B values (0.49 dB non-causal, –1.11 dB causal, –0.36 dB full) are difficult to interpret — they show the method *works*, but not how *well* it works relative to existing approaches. A typical speech separation system would achieve SDR-B well above 0 dB. The method used to extract decoupled signals for SDR-B/SDR-S computation (e.g., zeroing one RVQ branch?) is also not described.

### Minor

4. **SE evaluation uses only DNSMOS; no intrusive metrics.** While DNSMOS is standard for DNS Challenge blind test sets and the baselines are evaluated with it as well, the absence of PESQ, STOI, or SI-SDR leaves questions about whether the high BAK scores come at the cost of speech quality in ways DNSMOS may not fully capture. Adding these would strengthen the evaluation.

5. **The term "angular matrix" in Section 3.4 is not defined.** The paper states "When the covariance matrix YYᵀ satisfies the angular matrix, indicating that the encoder extracts sufficiently diverse embeddings with different feature channels being mutually independent..." — this condition is never defined or explained, making the derivation of P_S P_Nᵀ = 0 unclear.

6. **One-shot VC evaluation is on noisy speech only, conflating denoising and conversion quality.** The reported WER of 50.46% (Table 3) is still very high. While this improves over the cascaded baseline (52.73%), evaluating VC on clean speech (where background is not an issue) would establish baseline conversion quality and allow the noisy evaluation to isolate robustness benefits.

7. **No error bars, confidence intervals, or statistical significance reported for any metric.** Given test sets of 300 clips and the moderate differences between methods (e.g., WER 50.46 vs 52.73), variance could affect conclusions.

### Trivial

8. The "angular matrix" issue above also qualifies here — it is a missing definition that hurts clarity. The paper would benefit from a brief clarification.

## Nice-to-Haves

- Include a controlled experiment for the ablation: mix speech from speaker A with noise N1, and speech from speaker B with noise N2; swap representations and verify that the decoder reconstructs A+N2 (not A+N1). This would directly validate the RST claim.
- Add a comparison with a simple codec-based SE baseline (e.g., encode with EnCodec, drop some RVQ layers, decode) to demonstrate the advantage of explicit decoupling over generic codec artifact removal.
- Report the computational cost (parameters, MACs, RTF) of the proposed method.
- Include an evaluation of the causal vs. non-causal latency trade-off.

## Removed Points

*(These are points raised by reviewers that were evaluated against the paper and found to be distorted, factually incorrect, or already addressed. They are listed here for completeness but should not carry weight in evaluation.)*

- *"The paper does not discuss how the semantic guidance is applied at inference time — if it uses the noisy speech's own HuBERT representation, the guidance may be noisy."* **Removed.** The SG loss (Eq. 7) uses HuBERT of the *clean* speech **s**, which is the training target. During training, clean speech is available as the supervision signal. During inference, HuBERT is not needed at all — the guidance is purely a training loss that shapes the RVQ codebook. This is standard practice (same as SpeechTokenizer). The paper's description is clear enough to anyone familiar with the literature.
- *"The paper should ideally report SI-SDRi, PESQ, STOI for SE."* **Moved to Minor.** DNSMOS is the standard metric for DNS Challenge blind test sets and all baselines use it. The paper's SE comparison is fair as-is. Adding intrusive metrics would strengthen but is not a requirement.
- *"The paper does not mention training hyperparameters, optimizer settings, learning rate schedules, or computational cost."* **Moved to Nice-to-Haves.** These details are important for reproducibility but the paper is already at the submission page limit; they would typically appear in appendices or an ethics statement.
- *"DeCodec operates at 8 kbps, higher than most baselines."* **Not a weakness.** The architecture uses independent RVQs for speech (4 kbps) and background sound (4 kbps), which is by design. The paper acknowledges this. Claiming this as a weakness ignores the fact that the higher bitrate is a structural consequence of dual-stream coding — it is not an apples-to-apples comparison with single-codec bitrates.

## Novel Insights

The most interesting finding is that the **BAK score gap** between DeCodec and dedicated SE models on real recordings (3.99 vs. next-best 3.57 for Inter-SubNet) is substantially larger than on synthetic data (4.13 vs. 4.10). This suggests that representation-domain decoupling may generalize better to unseen acoustic conditions than time-domain separation — a testable hypothesis for future work. Additionally, the asymmetric impact of SG (large WER improvement, modest SDR degradation) reveals a clean trade-off surface between semantic faithfulness and signal fidelity that was not previously quantified in a single codec.

## Score and Decision

**MY FINAL SCORE:** <score>4.5</score>
**MY FINAL DECISION:** <decision>Reject</decision>