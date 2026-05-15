Now I have sufficient calibration data. Let me compose the final review by cross-referencing every claim against the paper.

---

## Summary

DeCodec proposes reframing neural audio codecs as universal disentangled representation learners. It introduces three technical components: a Subspace Orthogonal Projection (SOP) module that factorizes audio embeddings into orthogonal speech and background-sound subspaces; a Representation Swap Training (RST) procedure that ensures those subspaces correspond to the correct modalities; and Semantic Guidance (SG) that hierarchically decomposes speech into semantic and paralinguistic codes within the speech quantizer. The resulting model supports audio reconstruction, speech enhancement (by discarding the background branch), and one-shot voice conversion (by swapping paralinguistic codes) within a single codec. Speech enhancement results on the DNS Challenge are competitive with specialized models, and ablations confirm that SOP+RST jointly enable the disentanglement.

## Strengths

- **Genuinely novel architecture for representation-level disentanglement**: The combination of the SOP module (enforcing orthogonal subspaces) with the RST procedure (swapping representations across different mixed inputs during training) is a creative attempt to achieve speech-background factorization within a codec. Ablation results (Table 4) clearly show that neither SOP nor RST alone works — only SOP+RST (Ablation-3) yields usable SDR-B (0.49 dB) and SDR-S (7.90 dB), while each alone collapses to SDR-B < –10 dB. This is a clean, well-controlled demonstration of the joint mechanism.

- **Competitive speech enhancement without a dedicated SE front-end**: Table 2 shows DeCodec achieving the highest DNSMOS scores across both simulated (OVL 3.39, BAK 4.13) and real recordings (OVL 3.13, BAK 3.99), outperforming specialized models including SELM, StoRM, and Inter-SubNet. This is a strong result that demonstrates practical utility from the representation-swap mechanism — replacing the background branch with a blank-audio encoding effectively suppresses background sound.

- **Clean ablation of semantic guidance**: Table 4 shows that adding SG to the SOP+RST setup reduces downstream ASR WER* from 41.9% to 25.8% (causal) while maintaining competitive overall SDR. This isolates the value of hierarchical semantic-paralinguistic decomposition within the speech branch.

- **Unified multi-task capability**: The model supports reconstruction, enhancement, and voice conversion within a single architecture, which is an ambitious and practically appealing goal.

## Weaknesses

### Major

- **Reconstruction comparison is confounded by unequal bitrate**: Table 1 compares DeCodec at 8 kbps total (4.0 speech + 4.0 background) against baselines operating at substantially lower total bitrates — DAC at 4.5 kbps, HiFi-Codec at 2.0 kbps, SpeechTokenizer at 4.0 kbps, EnCodec at 6.0 kbps. The paper's headline claim that DeCodec "maintains advanced signal reconstruction" while adding disentanglement is undermined because the SDR advantage (7.61 vs. baselines' 0.60–6.86 on clean speech) could be explained entirely by the higher bandwidth allocation. The paper provides no matched-bitrate comparison. This does not invalidate the disentanglement contribution, but it means the reconstruction-quality framing is not properly supported. The paper would need to evaluate DeCodec at a total bitrate comparable to baselines (e.g., 4.0–6.0 kbps) to fairly assess the reconstruction-disentanglement trade-off.

### Minor

- **Voice conversion WER is too high for practical use**: Table 3 reports WER of 50.46% for one-shot VC on noisy speech — half of all words are unrecognizable after conversion. While the paper acknowledges this limitation (attributing it to mismatched voicing times) and the result does beat the StoRM-SpeechTokenizer baseline (52.73%), this level of intelligibility collapse makes it difficult to describe the VC capability as "effective." The paper would benefit from a more candid discussion of this limitation and analysis of failure modes.

- **Disentanglement evaluation relies on reconstruction metrics without independent information-leakage probes**: The paper measures decoupling quality through SDR-B and SDR-S — metrics computed by reconstructing the expected sources from quantized representations. While standard for source separation, these metrics do not directly verify that the speech subspace is free of background information or that the background subspace carries no phonetic content. Independent probes (e.g., running ASR on the background branch output, or a sound-event classifier on the speech branch output) would provide stronger evidence for the core claim of orthogonal, non-overlapping subspaces. The current evaluation is partly circular.

- **The "theoretical proof" in Section 3.6 is informal**: The argument applying the mean value theorem to vector functions (Eq. 15–16) does not constitute a rigorous proof that RST forces clean separation. It is an intuitive consistency argument showing why the loss should work under idealized conditions. The paper should not present this as a formal guarantee, and the claim of theoretical rigor is overstated.

- **The biological motivation is decorative**: The analogy to A2 cortical organization (Section 3.4) and "neural developmental feedback mechanisms" (Section 3.6) adds no technical substance. The method works or fails on its engineering merits, not on neuroscientific metaphor. This does not harm the contribution but inflates the framing unnecessarily.

### Trivial

- SDR-B and SDR-S computation details are not described (e.g., whether decoupled background is compared against the original clean background signal or against a version extracted through the same pipeline). This is a minor reproducibility concern.

## Nice-to-Haves

- Bitrate-matched reconstruction comparison against baselines.
- Information-leakage probing of both subspaces using external classifiers.
- Analysis of VC failure modes beyond the voicing-time hypothesis (e.g., whether swapping only a subset of SRVQ layers improves WER).
- Spectrogram visualizations of separately decoded speech and background components to qualitatively assess artifacts.

## Removed Points

These points were flagged by reviewers but are removed from the main review with justification:

- **"Core downstream results are relegated to appendices and missing from the main paper"**: Per the review instructions, the parser strips appendix sections from all papers. The original submission includes Appendix F (ASR robustness) and Appendix G (controllable TTS), and the paper body explicitly states where these results can be found (Section 4.2). This is not an author error.

- **"Missing Parts and Places to Improve — Missing Experiments" section about including ASR/TTS results in the main paper**: Same justification as above — the appendices exist in the original submission and were stripped by the parser.

- **"Unfair bitrate comparison invalidates reconstruction claims" — softened from fatal to major**: The bitrate mismatch is a real issue, but the harsh critic's framing that it "invalidates" reconstruction claims entirely overstates the case. The paper's core contribution is disentanglement, not compression efficiency, and the SE/VC results do not depend on this comparison. The concern is retained as a major weakness but not as fatal.

## Novel Insights

None beyond the paper's own contributions. The idea of performing disentanglement within a codec's representation space (rather than as a preprocessing step) is the paper's own insight. The reviews did not surface a fundamentally new perspective on this work.

## Suggestions

- Report results at a matched total bitrate by reducing RVQ layers in the speech or background branch. Even if reconstruction quality drops, this would honestly characterize the trade-off between compression and disentanglement that DeCodec makes, and would let readers fairly compare against baseline codecs.
- Add a simple information-leakage experiment: pass the background-branch output through a Whisper ASR model and report WER; pass the speech-branch output through a sound-event classifier. This would directly test the central claim of orthogonal subspaces.
- Tone down the theoretical claims in Section 3.6 — present the argument as an intuitive motivation for the RST loss rather than as a proof.

## Anchor Comparison

All anchors retrieved from calibration search:

- **MelCap** (`2nr6FVNOtu.md`, avg 1.50, Withdrawn): Fundamentally incomplete — no bitrate reported, missing experiments, very limited novelty. DeCodec is substantially stronger in both contribution and execution.
- **CodecSep** (`MDHVDfUrDz.md`, avg 4.00, Reject): Similar domain (codec-based audio processing). CodecSep had presentation issues, limited novelty, and missing comparisons. DeCodec has more architectural novelty and broader task coverage.
- **FuseCodec** (`RILri9w9IW.md`, avg 3.50, Withdrawn): Semantic-contextual fusion for codecs. Similar ambition level but withdrawn. DeCodec has stronger experimental validation.
- **Self-Guidance** (`lCaU7NlZ1I.md`, avg 5.00, Reject): A simple training trick with marginal improvements, evaluated on one codec. DeCodec has substantially more novelty (SOP+RST+SG architecture vs. an auxiliary loss) and broader evaluation.
- **FlexiCodec** (`kYkfCs4ZAH.md`, avg 5.67, Accept Poster): Novel dynamic frame-rate codec with thorough experiments. Cleaner evaluation than DeCodec, but narrower scope (no SE, no VC). DeCodec has comparable novelty but weaker evaluation rigor.
- **Gogo** (`JbLmIoWwDC.md`, avg 6.00, Accept Poster): Novel granularity-ordered codec with strong results. Better evaluation than DeCodec, though both share some baseline fairness concerns. DeCodec's evaluation weaknesses pull it below Gogo.

DeCodec sits between Self-Guidance (5.00) and FlexiCodec (5.67). Its architectural novelty and multi-task scope exceed Self-Guidance, but its evaluation rigor (bitrate mismatch, informal proof, circular disentanglement metrics) falls short of FlexiCodec's standard. A score of 5.0 reflects genuine contributions that are not yet sufficiently validated.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>