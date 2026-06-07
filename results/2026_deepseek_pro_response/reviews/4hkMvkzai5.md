Now let me finalize my comparison and write the review.

**Round 1 bracket**: Based on comparisons with RepCodec (5.50), Universal Semantic Disentangled (4.80), and Restructuring VQ (8.00), I bracketed DeCodec between 5.0 and 7.0.

**Round 2 narrowing**: After reading FlowDec (7.00), HALL-E (6.40), GenSE (6.00), and Separate and Diffuse (6.00):

- DeCodec is clearly below FlowDec (7.00): FlowDec has proper theoretical grounding, complete method specification, well-justified design choices, and strong competitive results. DeCodec's pseudo-proof and missing training objective are substantial gaps that FlowDec doesn't have.
- DeCodec is slightly below HALL-E (6.40): HALL-E has three well-defined contributions (MReQ, HALL-E, MinutesSpeech), well-documented training, and comprehensive experiments. DeCodec's idea is comparably novel but execution is less polished.
- DeCodec is comparable to GenSE (6.00) and Separate and Diffuse (6.00): similar level of novelty, decent experiments with some limitations, borderline accept.

**Final score: 6.0**

---

## Summary
DeCodec proposes a neural audio codec that disentangles mixed audio into speech and background sound representations via a Subspace Orthogonal Projection (SOP) module and Representation Swap Training (RST), with Semantic Guidance (SG) for further speech decomposition. The model is evaluated on reconstruction, speech enhancement, and one-shot voice conversion, positioning itself as a universal front-end for diverse audio tasks.

## Strengths
- **Compelling ablation evidence for SOP+RST synergy (Table 4):** SOP-only yields SDR-B of −13.15 dB and RST-only yields −10.67 dB; only their combination achieves 0.49 dB — a jump of over 10 dB on background-sound reconstruction. This is among the cleanest demonstrations in the neural codec literature that both components are jointly necessary for decoupling.
- **DeCodec outperforms dedicated speech enhancement models on DNS Challenge (Table 2):** On the without-reverb subset, DeCodec achieves OVL 3.39 / SIG 3.64 / BAK 4.13, exceeding the best specialized SE baseline SELM (3.26 / 3.51 / 4.10). On real recordings, DeCodec achieves OVL 3.13 / BAK 3.99, again surpassing SELM (3.12 / 3.44). A codec model beating purpose-built discriminative, diffusion, and transformer SE models on background suppression is a strong, surprising result.
- **Practical disentanglement demonstration:** Replacing BGS tokens with "blank audio" tokens for SE (Section 4.2.2) requires no additional model or fine-tuning, cleanly demonstrating the value of representation-domain decoupling.
- **Well-chosen baseline coverage:** The paper evaluates against acoustic codecs (EnCodec, DAC, HiFi-Codec), a speech tokenizer (SpeechTokenizer), three SE paradigms (Inter-SubNet, StoRM, SELM), and a cascaded pipeline (StoRM-SpeechTokenizer), with each baseline appropriate to its task.

## Weaknesses

### Fatal
None.

### Major
- **The "theoretical proof" in Section 3.6 is not mathematically valid (Eqs. 13–16).** The argument applies the mean value theorem to conclude that Zs must contain no background sound information. However, a sufficiently expressive decoder could satisfy the reconstruction equations while Zs₁ still contains BGS information — the decoder could learn to ignore or cancel redundant information across representation streams. The reasoning conflates what the loss *encourages* with what it *guarantees*, and the mean value theorem step does no real work beyond restating the assumption. The paper presents this as a "theoretical proof" when it is at best an intuition. The RST idea is interesting on its own and does not need a pseudo-proof, but presenting an invalid proof as "theoretical" damages the paper's credibility.
- **The full training objective is never specified.** The paper defines three auxiliary losses (L⊥ in Eq. 5, L_SG in Eq. 7, L_RST in Eq. 12) but does not state whether standard codec losses (multi-scale STFT, adversarial, feature matching, commitment) are included, nor their relative weights. The architecture is described as adopting DAC's encoder-decoder, so these losses are presumably present, but omitting the complete objective prevents reproducibility. This can be resolved in rebuttal but is a substantial gap for a codec paper.

### Minor
- **Reconstruction comparisons span different bitrates (Table 1).** DeCodec at 8.0 kbps (4.0 speech + 4.0 BGS) is compared against baselines at 2.0–6.0 kbps. Since reconstruction quality correlates with bitrate, the SDR advantage is partially attributable to the higher total bitrate. The paper should discuss this confound explicitly.
- **VC results do not support the claim of "effective" one-shot voice conversion (Table 3).** The WER of 50.46% means converted speech is largely unintelligible. The improvement over the cascade baseline is only 2.27 pp. The paper acknowledges this (citing voicing-time mismatches, Section 4.2.3) but the abstract's claim of "effective one-shot voice conversion on noisy speech" overstates what the numbers show.
- **DNSMOS-only evaluation for SE (Table 2).** DNSMOS is a non-intrusive metric with known biases. Reporting SDR or PESQ against clean reference would provide a more direct measure of the speech-distortion vs. noise-suppression trade-off.

### Trivial
- The notation ⟨S, N⟩ in Eq. 5 is ambiguous — it is unclear whether S and N are frame-level vectors or span the temporal dimension.
- The claim about the covariance matrix being "angular" (line 106) is stated without definition or justification.

## Nice-to-Haves
- Replace the pseudo-proof in Section 3.6 with an empirical disentanglement analysis (mutual information, probing classifiers, or CCA between speech and BGS streams) or simply present RST as a training heuristic without claiming a proof.
- Add a bitrate-matched comparison or discuss the bitrate confound explicitly.
- Report reference-based metrics (SDR, PESQ) for SE to complement DNSMOS.
- Contextualize the approach relative to the speech separation literature (Conv-TasNet, SepFormer) beyond the brief mention in the introduction.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *Missing training hyperparameters (optimizer, LR, batch size, codebook sizes, number of quantization layers)* — Removed per reproducibility nitpick rule. These are standard details addressable in rebuttal and impractical to fully enumerate in all submissions.
- *No statistical significance or variance reported for any result* — Removed per rule against demanding confidence intervals for benchmark evaluations where single-run reporting is standard practice.
- *Missing discussion of speech separation literature as a weakness* — Moved to Nice-to-Haves as a scope-strengthening suggestion rather than a flaw.
- *Speculation about appendix content (ASR, TTS experiments)* — Removed per rule against penalizing stripped appendices; the parser removes these sections and they exist in the original submission.
- *"Blank audio" representation acquisition procedure not detailed* — Removed as minor implementation detail addressable in rebuttal.

## Novel Insights
None beyond the paper's own contributions. The core idea of using representation-swap training with orthogonal projection to achieve disentanglement within a codec is genuinely novel and the ablation evidence for their synergy is compelling.

## Suggestions
- Replace Section 3.6's "proof" with an honest empirical or information-theoretic analysis of disentanglement, or present RST as a training heuristic without overclaiming theoretical guarantees.
- State the complete training objective with all loss terms and their weights, following the standard codec paper convention.
- Report VC results on cleaner mixtures (SNR ≥ 10 dB) to show where the method succeeds, and characterize the 50% WER result as a limitation rather than a success.
- Train or evaluate DeCodec at a matched lower total bitrate to isolate the architectural contribution from the bitrate advantage.

## Score and Decision

**Anchor comparison summary:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| RepCodec | 5.50 | R1 | DeCodec is stronger: more novel contribution, better ablation, harder problem |
| Universal Semantic Disentangled | 4.80 | R1 | DeCodec is stronger: more principled disentanglement, cleaner ablation, competitive SE results |
| Restructuring VQ | 8.00 | R1 | DeCodec is weaker: less rigorous theory, less complete specification, weaker claims |
| FlowDec | 7.00 | R2 | DeCodec is weaker: FlowDec has proper theory, complete method, well-justified design |
| HALL-E | 6.40 | R2 | DeCodec is slightly weaker: HALL-E has better-documented training, three solid contributions; DeCodec's ablation is cleaner but execution less polished |
| GenSE | 6.00 | R2 | Comparable: similar novelty level, decent experiments with limitations |
| Separate and Diffuse | 6.00 | R2 | Comparable: novel combination of ideas, results with some caveats |

**Round 1 bracket:** 5.0–7.0
**Round 2 narrowed to:** 6.0

DeCodec has a genuinely novel idea with strong ablation evidence, but the invalid "theoretical proof" and missing training objective are substantial issues that prevent it from scoring higher. It is comparable to borderline-accept papers at 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>