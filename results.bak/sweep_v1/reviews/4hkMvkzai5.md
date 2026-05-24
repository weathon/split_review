Now I have all the information needed to write a well-calibrated review. Let me produce the consolidated review.

## Summary

This paper presents DeCodec, a neural audio codec that learns to decouple speech and background sound (BGS) into orthogonal subspaces via a subspace orthogonal projection (SOP) module and a representation swap training (RST) procedure, with further decomposition of speech into semantic and paralinguistic components via semantic guidance (SG). The system is evaluated on reconstruction quality, speech enhancement, one-shot voice conversion, and downstream ASR/TTS tasks. The core claim is that DeCodec is the first universal disentangled codec enabling controllable feature selection across diverse audio applications from a single model.

## Strengths

1. **Novel problem formulation and technical design** — The paper is the first to tackle explicit decoupling of speech and background sound inside a neural codec's representation space (as opposed to cascaded time-domain separation). The combination of orthogonality-constrained subspaces (SOP) + swap training (RST) + parallel RVQs is a creative and well-motivated approach. The ablation study (Table 4) confirms that neither SOP alone (SDR-B = −13.15 dB) nor RST alone (SDR-B = −10.67 dB) achieves decoupling, while their combination (SDR-B = 0.49 dB, SDR-S = 7.90 dB) does, validating the joint design.

2. **Strong downstream task validation** — Speech enhancement results (Table 2) show DeCodec achieving the highest DNSMOS OVL (3.39) and BAK (4.13) scores without reverb, competitive with or exceeding dedicated SE models like StoRM and SELM. Voice conversion on noisy speech (Table 3) achieves WER 50.46% vs. 52.73% for the cascaded StoRM-SpeechTokenizer pipeline, demonstrating reduced error propagation from unified representation learning rather than front-end separation.

3. **Multi-task capability from a single model** — The same trained DeCodec model enables reconstruction, SE, background sound extraction, one-shot VC, and provides noise-robust features for ASR and TTS, whereas prior codecs require separate front-ends or are limited to clean speech. This is a genuine engineering achievement.

4. **Causal version demonstrates practical applicability** — The causal DeCodec-c achieves DNSMOS OVL 3.31 and BAK 4.09, comparable to or better than the non-causal SELM and significantly better than the causal Inter-SubNet, suggesting low-latency deployment potential.

## Weaknesses

### Major

1. **Invalid theoretical proof for RST disentanglement guarantee** — Section 3.6 (Equations 13–16) attempts to prove that the swap training forces independence between speech and BGS representations using the mean value theorem for vector-valued functions. The mean value theorem in equality form (i.e., there exists ξ such that f(b)−f(a) = f′(ξ)(b−a)) does **not** hold for vector-valued functions in general — only the mean value *inequality* (bound via the norm of the derivative) is guaranteed. The decoder Dec(·) is a nonlinear neural network mapping from latent space to waveform; asserting the existence of a single ξ that yields the exact equality in (16) is not mathematically justified. The argument that "the left side depends on Zs₁ through ξ while the right side is independent of Zs₁" is also problematic because ξ lies between Zn₁ and Zn₂, so its dependence on Zs₁ is indirect and unclear. **This does not make the method invalid** — the empirical results (ablation, downstream tasks) can stand on their own — but the paper explicitly claims a "theoretical proof" of disentanglement, and that claim is not supported. The paper should either remove the proof entirely or replace it with a sound argument (e.g., relating RST to a cycle-consistency or information-theoretic lower bound).

### Minor

2. **Unfair reconstruction bitrate comparison** — Table 1 compares DeCodec at 8.0 kbps (4.0+4.0) against EnCodec at 6.0, HiFi-Codec at 2.0, DAC at 4.5, and SpeechTokenizer at 4.0 kbps. The higher bitrate is a confound: DeCodec's SDR advantage (7.61 vs. 6.86 for EnCodec on clean speech) could be partly or largely due to extra capacity rather than the disentangled design. The paper's framing that DeCodec "maintains advanced signal reconstruction while enabling new capabilities" would be strengthened by a controlled comparison at a matched bitrate (e.g., using only the speech stream at 4.0 kbps against SpeechTokenizer). This issue is non-fatal because the paper's **core** contribution is decoupling, not reconstruction supremacy.

3. **SDR-B/S evaluation protocol is not fully specified** — The paper defines SDR-B and SDR-S as "signal distortion ratios for decoupled background sound and decoupled speech, respectively" (Table 4 caption) but never states exactly how these signals are obtained from DeCodec. The decoder is trained on the sum Zs+Zn; it is not obvious whether SDR-B is computed by passing only Zn through the decoder, or by some other procedure. The SE section describes replacing BRVQ with a blank (a reasonable inference), but the ablation study's exact protocol should be stated explicitly. This gap makes the decoupling numbers harder to interpret than they should be.

4. **SDR-B values are low** — Even in the best ablation (Ablation-3: SOP+RST), SDR-B is only 0.49 dB, meaning the reconstructed BGS signal power barely exceeds the distortion power. For the full model, SDR-B is −1.11 dB (causal) and −0.36 dB (non-causal). While the improvement over SOP-only (−13.15 dB) and RST-only (−10.67 dB) is dramatic and statistically non-trivial, the absolute SDR-B values suggest BGS decoupling is far from clean. The downstream SE results (high BAK scores) partially compensate — the representation-level decoupling is clearly sufficient for practical BGS suppression — but the paper should be more measured about "effective decoupling" of BGS in terms of reconstruction fidelity.

5. **VC WER remains very high** — The best one-shot VC WER is 50.46% (Table 3), indicating poor intelligibility. The paper acknowledges this (voicing mismatch) and the improvement over StoRM-SpeechTokenizer (52.73%) is modest (~2 percentage points). A discussion of whether this is a fundamental limitation of the representation-swap approach or something addressable with better alignment/warping would strengthen the paper.

### Trivial

6. The paper says "angular matrix" is required for P_S P_N^T = 0 (top of line 112), but does not define what an "angular matrix" is mathematically. This phrase should be clarified or removed.

## Nice-to-Haves

- A controlled bitrate comparison (speech-only stream at 4.0 kbps vs. SpeechTokenizer and DAC) would cleanly isolate whether the disentangled design incurs any reconstruction penalty.
- Visual evidence of decoupling (spectrograms of original mixture, reconstruction, speech-only decode, BGS-only decode) would immediately reveal whether leakage occurs and would greatly strengthen the paper.
- Reporting per-SNR results on the noisy test set would show at what SNR levels decoupling degrades.
- UniCodec would be a relevant baseline for comparison given the paper's positioning; its absence is noted but not critical.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Missing UniCodec in experiments** — The paper critiques UniCodec for classifying noisy speech as "sound" but does not include it in any experiment. Removed because comparing against all cited models is not required — the paper uses the most common baselines (EnCodec, DAC, HiFi-Codec, SpeechTokenizer) which are the standard references.
- **Overclaim about "first integration" ignoring prior work (VoiceFilter, TF-CapsNet)** — Removed because those are speech separation methods, not codecs; the claim is about codec integration. This is standard scoping for a novelty claim within a specific framework.
- **SNR range too wide, should report per-SNR results** — Removed as an overly demanding suggestion. Training/test SNR ranges of −5 to 40 dB and reporting aggregate results is standard practice.
- **No statistical significance reported** — Removed as a generic criticism applicable to most papers in this area. Single-run evaluations with clear numerical gaps between methods are the norm for audio codec papers.
- **Missing related work citations** — Removed per instructions; you cannot confirm the existence or non-existence of external references.
- **The orthogonality loss L⊥ derivation lacking rigor** — The paper's derivation at line 108–112 is somewhat informal but the core idea (enforcing S⊥N via L⊥ regularization) is standard in representation learning and has been used successfully in many prior works. The derivation's informality is a presentation issue, not a methodological flaw.
- **Splitting nitpicks about whether L⊥ uses per-frame dot product or batch average** — This is an implementation detail that can be clarified; it does not affect the validity of the approach.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Remove or rewrite the theoretical proof (Section 3.6).** The MVT argument for vector-valued functions is mathematically incorrect as stated. Either drop the "theoretical proof" framing and present RST as an empirically-motivated training procedure (the empirical evidence is sufficient), or replace it with a sound argument (e.g., connecting RST to a mutual-information lower bound or cycle-consistency rationale).
2. **Explicitly state the SDR-B/S evaluation protocol.** Clarify how decoupled speech and BGS signals are obtained from the model (e.g., feed only the relevant RVQ output through the decoder, or use a masking procedure).
3. **Add a controlled bitrate comparison.** Evaluate the speech-only stream (SRVQ at 4.0 kbps) against SpeechTokenizer (4.0) on clean speech to demonstrate that the disentangled design does not incur a fidelity penalty.
4. **Include spectrogram visualizations** of (a) original mixture, (b) full reconstruction, (c) speech-only stream decoded alone, (d) BGS-only stream decoded alone — this would make the decoupling claim much more transparent.

## Score and Decision

### Calibration Anchors (from batch retrieval)

| Path | Avg Score | Comparison to DeCodec |
|------|-----------|----------------------|
| DM-Codec (UFwefiypla.md) | 3.00 | Weaker — had a fundamental technical flaw (text-audio alignment) and incremental novelty. DeCodec has a more novel problem and more convincing downstream evaluation. |
| Disentangling Textual & Acoustic (xJc3PazBwS.md) | 3.75 | Weaker — narrower scope (information bottleneck for speech features). DeCodec is more ambitious in scope and application breadth. |
| USC (Id2JMVSQHZ.md) | 4.80 | Comparable — both address disentanglement in codecs. USC is cleaner but DeCodec tackles a harder problem (speech+BGS in mixed audio vs. speaker anonymization). DeCodec is stronger on novelty but has more evaluation gaps. |
| Towards Codec-LM (KCVv3tICvp.md) | 5.00 | Comparable — both have solid empirical contributions with some weaknesses. DeCodec is more novel in problem formulation; Codec-LM is cleaner in execution. |
| RepCodec (LfDUzzQa3g.md) | 5.50 | Slightly stronger — simpler idea, cleaner experiments, fewer weaknesses. RepCodec is more polished but less ambitious. |
| GenSE (1p6xFLBU4J.md) | 6.00 | Stronger — accepted paper with well-designed experiments and clear contribution. GenSE is more complete in its evaluation. |

**Positioning**: DeCodec's core idea (explicit speech+BGS decoupling inside a codec) is novel and well-motivated, and the downstream results demonstrate practical utility. However, the paper is held back by an invalid theoretical proof that it presents as a key justification, an unfair reconstruction comparison, and insufficiently specified decoupling evaluation metrics. This places it above DM-Codec (3.00) and USC (4.80) in novelty and scope, but below RepCodec (5.50) and GenSE (6.00) in executional rigor. The paper would benefit significantly from addressing the proof issue and adding the suggested clarifications.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>