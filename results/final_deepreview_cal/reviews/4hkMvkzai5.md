Now I have all the calibration data I need. Let me synthesize the final review.

---

## Summary

DeCodec proposes reframing neural audio codecs as universal disentangled representation learners. The paper introduces three technical contributions: a Subspace Orthogonal Projection (SOP) module that factorizes mixed audio into orthogonal speech and background-sound subspaces, a Representation Swap Training (RST) procedure that aligns those subspaces with their semantic labels, and semantic guidance (SG) to further decompose speech into semantic and paralinguistic components. The resulting codec supports audio reconstruction, speech enhancement (by zeroing the background subspace), and one-shot voice conversion on noisy speech via representation recombination.

## Strengths

- **Effective speech-background decoupling (Table 4):** The ablation study cleanly demonstrates that only the combination of SOP and RST achieves meaningful separation. Ablation-3 (SOP+RST, no SG) lifts SDR-B from below −10 dB (single-component ablations) to 0.49 dB, and SDR-S from −1.91/3.03 dB to 7.90 dB. This is the paper's strongest piece of evidence for the core mechanism.

- **Competitive and in some cases superior speech enhancement (Table 2):** By simply replacing background-sound representations with silence representations, DeCodec achieves the highest DNSMOS OVL (3.39/3.13) and BAK (4.13/3.99) scores on the DNS Challenge blind test sets, outperforming specialized discriminative, diffusion, and transformer SE models. This demonstrates that the speech-background decoupling in the representation domain is functional enough to serve as an effective SE strategy.

- **Competitive reconstruction fidelity (Table 1):** The non-causal DeCodec achieves the highest SDR on both clean (7.61 dB) and noisy speech (5.21 dB) among all tested codecs, with WER (1.92%) close to the best semantic-preserving model (SpeechTokenizer, 1.82%). This shows that the added disentanglement objectives do not degrade core codec performance.

- **Clean ablation isolating component contributions (Table 4):** The ablation study systematically demonstrates that SOP alone, RST alone, and their combination each produce distinct effects. The addition of SG is shown to substantially reduce WER* (from 41.9% to 23.6%/25.8%) at a modest SDR cost, confirming that semantic guidance meaningfully improves representation quality for downstream ASR.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Flawed theoretical justification of RST (Section 3.6, Eqs. 13–16):** The mean-value theorem argument claiming to prove that Zs contains no background information is not rigorous. The derivation states that the left side of Eq. 16 depends on Zs₁ through ξ while the right side is independent of Zs₁, and concludes that Zs₁ must be independent of n₁, n₂. This does not follow logically: the Jacobian ∂Dec/∂Zn is evaluated at a point that includes Zs₁ (at Zs₁+ξ), so the left side can depend on Zs₁ through the derivative magnitude as well as through ξ. The approximation (≈) further weakens any deductive force. Since the RST procedure is empirically validated by the ablation study, this theoretical imprecision does not threaten the paper's core claims, but the "proof" should be either corrected or replaced by a purely empirical justification (e.g., mutual information estimates, ABX tests). Presenting a non-rigorous argument as a proof weakens the paper's credibility.

- **Asymmetric background-sound reconstruction quality not addressed (Table 4):** The SDR for decoupled background sound (SDR-B) is −0.36 dB for the best non-causal DeCodec and 0.49 dB for the SOP+RST ablation without SG, while decoupled speech (SDR-S) reaches 6.73–7.90 dB. This large asymmetry means the background-sound subspace does not preserve the background signal with fidelity comparable to speech. The paper never acknowledges or discusses this gap, yet the abstract and introduction frame the codec as enabling both background suppression AND preservation for tasks like immersive TTS. Since the core demonstrated strength is in speech enhancement (background suppression), this asymmetry is a limitation worth characterizing rather than a fatal flaw.

- **High WER in one-shot VC limits practical utility of hierarchical decomposition (Table 3):** The WER of 50.46% after swapping SRVQ-2:8 is a large improvement over raw SpeechTokenizer (74.18%) and slightly better than the cascaded StoRM-SpeechTokenizer (52.73%), but remains far from intelligible speech. The paper acknowledges this limitation (attributing it to voicing mismatches), but the practical value of the semantic-paralinguistic decomposition for generation tasks is not yet convincingly demonstrated. This is partially mitigated by the WER* ablation (23.6%) showing that the semantic codes themselves carry cleaner information when not subjected to cross-utterance recombination.

### Trivial

- The derivation linking the orthogonality loss to projection matrix orthogonality (Eq. 6 and surrounding text) relies on an untestable assumption that the encoder produces embeddings with a diagonal covariance matrix. This is not needed for the method to function and should be de-emphasized.

## Nice-to-Haves

- A comparison with a strong speech-separation front-end (e.g., Conv-TasNet or SepFormer) feeding a clean-speech codec on downstream ASR/TTS tasks would strengthen the claim that representation-level decoupling is preferable to cascaded pipelines.
- Reporting SE metrics as a function of input SNR would reveal the method's limitations under severe noise conditions.
- Perceptual quality evaluation of the extracted background sound (even if distorted) would help characterize what information the background subspace actually retains.
- An ablation that swaps only subsets of SRVQ layers (e.g., only the last few) in the VC experiment would help diagnose whether the high WER stems from semantic contamination or prosodic mismatch.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Downstream ASR/TTS experiments missing from main paper:** REMOVED — the paper explicitly states these results are in Appendix F and G. The parser strips appendices; they exist in the original submission. Per review protocol, this is not a valid criticism.
- **Demand for larger datasets or more models:** REMOVED — the 700-hour training set and five baseline codecs are adequate for the paper's scope.
- **Criticism about "first time" claims being overstated:** REMOVED — this is a presentation nitpick rather than a substantive flaw; the contribution framing is clear enough.
- **Demand for listening tests for background sound extraction:** MOVED to Nice-to-Haves — this would strengthen the paper but is not required given the paper's primary demonstrated strength is in suppression, not preservation.
- **Concern about only guiding the first RVQ layer with SG:** REMOVED — this is a design choice, not a demonstrated flaw; the ablation shows SG meaningfully improves WER*.
- **SIG score gap between DeCodec (3.45) and SELM (3.59) in real recordings:** REMOVED as a standalone weakness — the paper explicitly discusses this gap, attributing it to discretization quantization penalties.

## Novel Insights

None beyond the paper's own contributions. The core insight — that orthogonal subspace projection combined with representation-swap training can achieve speech-background disentanglement in a codec — is the paper's own contribution and the strongest novel element. The idea of using blank-audio representation substitution for zero-shot speech enhancement within a codec is clever and well-executed.

## Suggestions

- Replace the mean-value-theorem "proof" in Section 3.6 with empirical sanity checks: measure the mutual information between Zs and the noise signal under RST training, or run ABX tests to verify that speech/noise identity is not predictable from the "wrong" subspace.
- Add a brief discussion of the SDR-B vs. SDR-S asymmetry in Section 4.2.4. Characterize what background information is preserved and what is lost; if faithful background preservation is not a current priority, reframe the contribution accordingly rather than claiming universality across both suppression and preservation use cases.
- Report the Whisper WER baseline on the unfiltered noisy test set alongside the WER* values in Table 4, so the reader can gauge whether 23.6% represents meaningful improvement.

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison to DeCodec |
|--------|------|-----------|-------|----------------------|
| DM-Codec | UFwefiypla | 3.00 | R1-bracket | DeCodec is substantially stronger in scope and experiments |
| UniAudio | nhgTmx1TZJ | 3.00 | R1-bracket | DeCodec has clearer contributions and more focused evaluation |
| USC (privacy codec) | Id2JMVSQHZ | 4.80 | R1+R2 | DeCodec has broader scope, stronger SE results, and cleaner ablations |
| Codec-LM Co-design | KCVv3tICvp | 5.00 | R1+R2 | Different focus; DeCodec's architectural novelty is comparable |
| Vec-Tok Speech | C53xlgEqVh | 5.20 | R2 | DeCodec has more principled design and stronger SE evidence |
| RepCodec | LfDUzzQa3g | 5.50 | R1+R2 | Similar quality level; DeCodec is more ambitious but has more rough edges |
| Separate and Diffuse | UXALv0lJZS | 6.00 | R1-bracket | DeCodec is below this in theoretical rigor and evaluation thoroughness |
| HALL-E | 868masI331 | 6.40 | R2 | DeCodec is clearly below in evaluation completeness and design justification |
| CLaM-TTS | ofzeypWosV | 6.40 | R2 | DeCodec is below in overall polish and experimental depth |

**Round-1 bracket:** 4.80–6.00

**Round-2 narrowing:** The paper sits closest to RepCodec (5.50) and Vec-Tok Speech (5.20). It is more ambitious than both — tackling a genuinely harder problem (speech-background disentanglement) — and delivers strong SE results that neither anchor matches. However, it has more rough edges: a flawed theoretical argument, an undiscussed asymmetry in reconstruction quality, and VC results that are directionally correct but not practically usable. It is clearly below the 6.00+ anchors in evaluation rigor. Given that its strengths (SE results, clean ablations, genuine novelty) outweigh its weaknesses (flawed proof, some overclaimed scope), a score of **5.5** is appropriate — comparable to RepCodec in overall contribution quality.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>