Now I have all the information I need. Let me compile the final consolidated review.

**Round 1 bracket: 3.5–7.5**

The paper is clearly above the weak anchors (USC at 4.80 was rejected with weaker novelty; RepCodec at 5.50 was rejected but had cleaner evaluation) and clearly below the strong anchors (FlowDec at 7.00 was accepted with polished evaluation; GenSE at 6.00 was accepted with public code/demo).

**Round 2 narrowing:** After comparing with all anchors, I place the paper at **5.5**. It has stronger technical novelty than USC (4.80) but weaker evaluation. It is comparable to RepCodec (5.50) in overall quality — both have novel ideas with evaluation gaps. It is weaker than GenSE (6.00, accepted) which had a cleaner, better-supported evaluation despite less novelty.

---

## Summary

DeCodec rethinks audio codecs as universal disentangled representation learners. It proposes a Subspace Orthogonal Projection (SOP) module to project audio embeddings into orthogonal speech and background sound subspaces, complemented by a Representation Swap Training (RST) procedure that forces each subspace to encode only its target component. Within the speech branch, semantic guidance (SG) further decomposes representations into semantic and paralinguistic streams. Experiments across reconstruction, speech enhancement, one-shot voice conversion, and ablation studies show that the approach enables controllable feature selection.

## Strengths

- **Novel disentanglement mechanism (SOP+RST):** The core technical contribution — decomposing the encoder embedding via learned orthogonal projections and training with cross-signal swap reconstruction — is genuinely novel and grounded in a clean theoretical argument (§3.6). The ablation study (Table 4) convincingly shows that neither SOP alone nor RST alone achieves decoupling (SDR-B < −10 dB), while their combination jumps to SDR-B=0.49 and SDR-S=7.90 dB, demonstrating that both components are necessary.

- **State-of-the-art speech enhancement without a dedicated SE model:** DeCodec achieves the highest DNSMOS scores on the DNS Challenge test set (OVL 3.39, SIG 3.64, BAK 4.13), outperforming dedicated discriminative, diffusion, and transformer SE baselines (Table 2). This provides strong evidence that representation-domain decoupling is practically useful for noise suppression.

- **First codec to simultaneously achieve reconstruction, SE, and VC:** The paper demonstrates that a single codec model can serve multiple tasks (reconstruction, speech enhancement, one-shot VC) by selective recombination of its disentangled representations, going beyond what existing codecs or speech tokenizers can do.

- **Theoretical justification for representation separation:** Section 3.6 provides a formal argument (Eqs. 13–16) grounding why the RST loss forces the quantized speech vector Zs to be independent of background sound and vice versa, beyond the empirical validation.

## Weaknesses

### Major

- **Reconstruction comparison confounded by mismatched bitrate (Table 1):** DeCodec runs at 8.0 kbps total (4.0 speech + 4.0 background), while baselines use substantially lower rates (EnCodec 6.0, HiFi-Codec 2.0, DAC 4.5, SpeechTokenizer 4.0). Higher bitrate trivially improves SDR, so the reconstruction advantage (7.61 vs. 6.86 for EnCodec, and especially 7.61 vs. 0.60 for DAC) is partly attributable to the bitrate gap rather than the method itself. The DAC SDR of 0.60 dB is notably low even for its bitrate, which raises questions about whether evaluation conditions (sampling rate compatibility with official checkpoints) were properly controlled — the paper states baselines are "inferred from official checkpoints" but does not specify how sampling rate differences were handled. A fair comparison would match total bitrate.

- **Background sound representation carries very limited information:** In the full model, SDR for the separated background sound is only −0.36 dB (non-causal) to −1.11 dB (causal) in Table 4. Even the ablation-3 variant (SOP+RST without SG) reaches only 0.49 dB SDR-B. This means the background branch is essentially a noise gate that identifies what is *not* speech, but cannot faithfully reconstruct or preserve background sound. The paper's stated goal of "controllable background sound preservation/suppression" (abstract) is only partially supported — the suppression side works (via discarding the BGS branch), but preservation is not demonstrably effective in the main paper. This asymmetry is not adequately discussed as a limitation.

- **No comparison with a cascaded pipeline (speech separation + standard codec) for reconstruction or SE:** The paper's main motivation is to avoid the error propagation and signal distortion of the traditional cascaded approach (Figure 1a). However, no experiment directly compares DeCodec against a speech separation model feeding a standard codec. For VC the paper does compare against StoRM-SpeechTokenizer (a cascaded pipeline), which partially addresses this, but a reconstruction/SE cascaded baseline is missing. Without this comparison, the claimed advantage over cascading is asserted but not tested.

### Minor

- **One-shot VC WER is very high even if better than baselines:** DeCodec's 50.46% WER on noisy speech VC (Table 3) means roughly half the words are incorrect. The paper acknowledges this and provides a plausible explanation (voicing-time mismatch), but calling this "effective one-shot voice conversion" overstates the practical utility. No clean-speech VC results are reported, making it difficult to disentangle whether the poor WER stems from the VC mechanism itself or from the noisy input. A clean-speech VC experiment (e.g., DeCodec on LibriSpeech-clean) would clarify this.

- **No statistical significance for reported metrics:** Several DNSMOS and SIM differences in Tables 2 and 3 are small (e.g., DeCodec OVL 3.39 vs. SELM 3.26 on clean; DeCodec SIM 0.83 vs. StoRM-SpeechTokenizer 0.83). Without confidence intervals or significance tests, it is unclear whether these differences are reliable or within evaluation noise.

- **No subjective listening evaluation:** The paper relies entirely on objective metrics (SDR, DNSMOS, WER, SIM). For audio quality claims — especially the SE comparison — a listening test or at least a demo page with samples would strengthen the evidence considerably.

### Trivial

None.

## Nice-to-Haves

- A bitrate-matched version of DeCodec (e.g., using fewer RVQ layers to match 4–6 kbps) would cleanly separate the effect of disentanglement from the effect of higher bitrate.
- Visualizing the learned projection matrices or embedding trajectories in the SOP subspaces would strengthen the claim that the subspaces correspond to speech vs. background sound.
- Reporting results on a wider range of mixture types (e.g., speech + music, overlapping speakers) would test the generality of the approach.

## Removed Points

These points were considered but removed with justification:
- **"ASR/TTS claims unsupported"** (Harsh Critic): The paper states these results are in Appendices F and G, which were removed from the review copy (parser artifact). Not a flaw in the paper.
- **"SOP additive decomposition assumption is a strong modeling choice"**: This is the paper's modeling assumption, openly stated and trained to enforce. Not a weakness per se.
- **"Mel distance nuance (DAC better)"**: An observation, not a weakness of the paper. The paper acknowledges this.
- **"No evaluation on music"**: Beyond the paper's stated scope (speech + background sound). Scope creep.
- **"Abstract/Introduction dangling claims"**: These are supported by results in removed appendix sections. Not evaluable but not the paper's fault.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a bitrate-controlled version of DeCodec (e.g., 4.0 or 6.0 kbps total by reducing RVQ layers) to the reconstruction comparison. Report SDR at matched bitrates.
2. Report clean-speech one-shot VC results to establish a baseline for the VC mechanism's effectiveness independent of noise.
3. Add statistical significance measures (bootstrapped confidence intervals) for the DNSMOS and WER comparisons where differences are small.
4. Include a cascaded pipeline baseline (e.g., Conv-TasNet or DPRNN as front-end + DAC/EnCodec as back-end) for reconstruction and SE.
5. Discuss the weak background sound reconstruction (SDR-B ≈ 0 dB) as a limitation of the current approach and explore what it means for applications requiring background sound preservation.
6. Provide a demo page with audio samples for subjective assessment.

## Score and Decision

The paper proposes a genuinely novel approach to disentangled audio representation learning, with a well-designed mechanism (SOP+RST) and strong evidence for SE performance. However, the reconstruction evaluation is confounded by bitrate mismatch, the background sound representation is demonstrably weak, a key cascaded baseline is missing, and several claims would benefit from stronger statistical backing and subjective validation. These issues are addressable but prevent full support of the paper's claims in its current form.

**Calibration Anchors Consulted:**
- **UFwefiypla** (3.00, Round 1, weak anchor): Unrelated topic. Lower quality.
- **mlPTNEIsgb** (3.25, Round 1, weak anchor): Unrelated topic. Lower quality.
- **Id2JMVSQHZ** (4.80, Rounds 1&2, USC): Similar topic (codec disentanglement for privacy). Weaker novelty (applied existing techniques); rejected. DeCodec has stronger technical novelty → scores higher.
- **LfDUzzQa3g** (5.50, Rounds 1&2, RepCodec): Similar topic (codec-based representation). Comparable novelty but simpler; rejected. DeCodec is comparable in overall quality.
- **KCVv3tICvp** (5.00, Rounds 1&2, Codec-LM Co-design): Different focus, fewer tasks evaluated. DeCodec has broader evaluation → scores higher.
- **1p6xFLBU4J** (6.00, Rounds 1&2, GenSE): Accepted. Cleaner evaluation with code/demo, but less novelty. DeCodec has more novelty but weaker evaluation → scores slightly lower.
- **uxDFlPGRLX** (7.00, Round 2, FlowDec): Accepted. Polished evaluation, strong baselines, theoretical depth. DeCodec is clearly weaker.
- **Round 1 bracket:** 3.5–7.5. **Narrowing:** Paper is between USC (4.80) and GenSE (6.00), comparable to RepCodec (5.50).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>