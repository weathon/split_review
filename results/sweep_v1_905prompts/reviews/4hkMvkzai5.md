Here is the final consolidated review.

---

## Summary

DeCodec proposes a neural audio codec that learns hierarchically disentangled representations: speech vs. background sound via a Subspace Orthogonal Projection (SOP) module and Representation Swap Training (RST), then semantic vs. paralinguistic within speech via Semantic Guidance (SG). Built on a DAC encoder-decoder with parallel RVQs, the model enables speech enhancement (by replacing the BGS quantized stream with a blank's), one-shot voice conversion (by swapping paralinguistic tokens), and supports downstream ASR/TTS. The core technical idea—using orthogonal linear projections plus cross-sample swap reconstruction to enforce subspace-level decoupling—is novel and cleanly ablated.

## Strengths

- **Novel and well-validated core technique (SOP + RST).** The Subspace Orthogonal Projection module with explicit orthogonality loss (Eq. 5–6) provides a principled mechanism for factorizing the encoder embedding into two orthogonal subspaces. The RST procedure (Eq. 8–12) enforces that these subspaces correspond to speech and background sound by training the decoder to reconstruct swapped mixtures. The ablation study (Table 4) cleanly demonstrates that neither module alone achieves meaningful decoupling (SDR-B ≈ –13 dB, SDR-S < 3 dB), but their combination jumps to SDR-B ≈ 0.49 dB and SDR-S ≈ 7.90 dB—concrete evidence that both components are jointly necessary.

- **Competitive speech enhancement without a dedicated SE model.** Table 2 shows DeCodec (non-causal) achieves the highest DNSMOS OVL (3.39), SIG (3.64), and BAK (4.13) on the DNS Challenge blind test set without reverb, outperforming dedicated discriminative (Inter-SubNet), diffusion (StoRM), and transformer (SELM) models. The causal variant (DeCodec-c) also achieves competitive results, which is noteworthy since causality is a hard constraint for many real-time applications.

- **Hierarchical disentanglement validated through multiple tasks.** The paper demonstrates three capabilities from a single codec: (a) SE by replacing the BGS stream, (b) one-shot VC on noisy speech by swapping paralinguistic tokens (Table 3), and (c) reconstruction that is competitive with dedicated codecs (Table 1). The systematic ablation isolating SOP, RST, and SG (Table 4) allows attributing each capability to specific modules.

## Weaknesses

### Major

- **None.** The paper's core claims are supported by evidence; no single issue invalidates the main contribution.

### Minor

1. **Asymmetric decoupling quality is under-discussed.** Table 4 shows SDR-B is near zero for Ablation-3 (0.49 dB) and negative for the full model (–0.36 dB), while SDR-S reaches 6.73–7.90 dB. The BGS subspace carries far less information than the speech subspace, meaning the decoupling is asymmetric: the model discards most BGS detail while preserving speech well. The SE results (Table 2) show this asymmetry is actually *useful* for suppression, but the paper frames the contribution as general "disentangled representation" without acknowledging this trade-off or reporting whether different capacity allocations (e.g., more bits for BRVQ) could improve SDR-B. The claims would be more accurate if softened to acknowledge a speech-priority asymmetry.

2. **"Effective" one-shot VC overstates the results.** Table 3 reports a WER of 50.46% for DeCodec on noisy VC. While this beats the cascaded baseline (StoRM-SpeechTokenizer at 52.73%), a 50% WER means roughly half the words are incorrect—hard to describe as "effective" voice conversion. The paper discusses voicing mismatch as a cause, but the abstract and introduction present this as a headline achievement without proper qualification. Reporting VC on cleaner conditions or adding a post-processing step would better support the claim.

3. **RST "proof" (Section 3.6) is heuristic, not rigorous.** Equations (13)–(16) attempt a theoretical justification via the mean value theorem for vector-valued functions. The multivariate MVT does not generally apply to vector-valued functions in the way invoked here (it holds component-wise and does not guarantee a single ξ for all components). The empirical evidence from the ablation is already convincing; this sketchy proof adds nothing and risks misleading readers. The paper would be stronger by either providing a proper mathematical argument or simply replacing this section with an intuitive explanation grounded in the ablations.

4. **Unmatched total bitrate between DeCodec and baselines.** DeCodec uses 4.0+4.0 = 8.0 kbps total, while SpeechTokenizer uses 4.0 kbps (Table 1). The higher total bitrate partly confounds the benefit of decoupling with extra model capacity. An ablation with matched total bitrate (e.g., 2.0+2.0 or 3.0+1.0 kbps) would cleanly separate the disentanglement advantage from the bandwidth advantage.

### Trivial

- Table 4 labels the ablation as "Decodec" (lowercase) while the paper consistently uses "DeCodec."

## Nice-to-Haves

- Reporting variance/confidence intervals for key metrics would help assess whether improvements (e.g., the 2.3-point WER gap in Table 3) are reliable.
- A discussion of the "blank audio" concept in SE (what the encoder produces for silence vs. actual silence) would improve interpretability.
- The angular-matrix condition for the SOP derivation (Eq. 6) is stated but not analyzed; a comment on when this assumption holds (or breaks) would strengthen the theory.

## Novel Insights

None beyond the paper's own contributions. The observation that orthogonal subspace projection combined with swap training produces asymmetric but practically useful decoupling is the paper's core insight, which the reviews affirm rather than extend.

## Suggestions

1. **Temper the disentanglement claim.** Acknowledge the asymmetry explicitly: the model prioritizes speech fidelity over BGS reconstruction, which is desirable for SE but limits symmetric representation quality. This is a feature, not a bug—but it should be stated clearly.
2. **Remove or replace the RST proof.** The empirical ablation (Ablation-3 in Table 4) is stronger evidence than the sketchy MVT argument. A concise intuitive explanation would be more honest and more effective.
3. **Add a matched-bitrate ablation.** Even as a small table or sentence clarifying that the bitrate imbalance does not drive the main results, this would preempt a natural reviewer concern.
4. **Qualify the VC claim.** Replace "effective one-shot voice conversion" with something like "proof-of-concept one-shot VC with lower WER than cascaded pipelines, though absolute WER remains high."
5. **Include a short limitations paragraph** in the conclusion (the paper defers this to Appendix H, but a brief mention in the main text is standard practice).

## Removed Points

These points from the inputs were removed per the filtering rules described above. They should be treated with caution and are not endorsed as valid criticisms:

- **Downstream results (ASR, TTS) only in appendix**: Removed per hard rule — the parser strips appendices. The original submission contains these results.
- **Missing hyperparameters, codebook sizes, training details**: Removed per hard rule — nitpicks about undisclosed training details that are not essential for reproducibility of the core claim.
- **SG loss described as "unusual"**: Removed — the loss is directly adopted from SpeechTokenizer (cited), so it is not a weakness specific to this paper.
- **"What is blank audio" question**: Removed — an implementation detail.
- **No music interference in training data**: Removed — scope creep; the paper targets speech-BGS decoupling.
- **Paper lacks limitations paragraph**: Moved to Nice-to-Haves.
- **General concerns about evaluation rigor without specific anchor in the paper**: Removed per filtering discipline.

## Score and Decision

### Calibration

**Round 1 — Bracketing:** Queried for "neural audio codec disentangled representation speech enhancement" across three bands:
- Low band (score < 3.5): returned anchors with scores 2.50–3.25 (unrelated papers — sequence segmentation, blind inverse problems, audio foundation models)
- Mid band (3.5–7.5): returned Id2JMVSQHZ (4.80, disentangled speech codec for privacy), 1p6xFLBU4J (6.00, GenSE — LM-based speech enhancement, accepted), KCVv3tICvp (5.00, codec-LM co-design), LfDUzzQa3g (5.50, RepCodec — semantic speech tokenization), qqExiDNsa7 (5.00, speech separation pre-training)
- High band (> 7.5): returned CxXGvKRDnL (8.00, diffusion compression), j7b4mm7Ec9 (7.60, watermarking), tyEyYT267x (8.00, diffusion language models) — not topically similar

Initial bracket: **4.5–6.5**.

**Round 2 — Narrowing:** Queried within (4.0, 6.0) and (5.0, 7.0) for more relevant anchors. Retained Id2JMVSQHZ (4.80), LfDUzzQa3g (5.50), KCVv3tICvp (5.00), 1p6xFLBU4J (6.00). Read these in full.

- **vs Id2JMVSQHZ (4.80, "Universal Semantic Disentangled Privacy-preserving Speech Representation"):** Rejected due to missing baselines, lack of quantitative superiority over existing work. DeCodec has clearer empirical validation (stronger SE results, cleaner ablation). DeCodec is stronger → above 4.80.
- **vs RepCodec/LfDUzzQa3g (5.50, "RepCodec: A Speech Representation Codec"):** RepCodec is a narrower contribution (replacing k-means with VQ for semantic tokens). DeCodec's SOP+RST is more novel, but DeCodec also has more overclaiming issues. Roughly comparable overall → around 5.5.
- **vs GenSE/1p6xFLBU4J (6.00, "GenSE: Generative Speech Enhancement via Language Models"):** Accepted. GenSE is cleaner (no overclaiming issues) but its technical novelty was questioned by its own reviewers. DeCodec has greater technical novelty but more framing problems. Slightly below GenSE → below 6.0.
- **vs KCVv3tICvp (5.00, "Towards Codec-LM Co-design"):** Rejected, seen as engineering tricks. DeCodec's contribution is more fundamental. DeCodec is stronger → above 5.0.

**Final anchor comparisons:** The paper is clearly stronger than the 4.80 and 5.00 anchors, comparable to 5.50 (RepCodec), and slightly below the clean 6.00 (GenSE). This places it at **5.5**.

### Score and Decision

**Score: 5.5** — A solid paper with a genuinely novel technique (SOP+RST), strong SE results, and clean ablations. The main weaknesses are in framing (overstating symmetric decoupling, calling 50% WER "effective" VC) and the sketchy theoretical proof. These are addressable in revision and do not undermine the core contribution. The paper would benefit from tempering its claims and adding a matched-bitrate ablation.

**Decision: Reject** — The overclaiming issues and asymmetric decoupling treatment are substantive enough that the paper in its current form does not meet the bar for acceptance at a top venue. However, with revisions that align the claims with the evidence, it would be a solid candidate for a future venue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>