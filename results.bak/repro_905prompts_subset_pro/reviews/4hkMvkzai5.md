Now I have a comprehensive picture of the paper and its calibrating anchors. Let me synthesize the final review.

## Summary

DeCodec proposes a neural audio codec that disentangles mixed audio (speech + background sound) into orthogonal subspaces, and further decomposes speech into semantic and paralinguistic components. The key technical novelties are a Subspace Orthogonal Projection (SOP) module that enforces output orthogonality, a Representation Swap Training (RST) procedure that uses cross-utterance mixing to attribute speech vs. background to the correct subspaces, and semantic guidance from HuBERT applied to the speech RVQ. The disentangled representations enable speech enhancement (by zeroing out the background code), one-shot voice conversion on noisy speech (by swapping paralinguistic codes), and—per the appendix—improved ASR and TTS.

## Strengths

- **Compelling ablation evidence for the core disentanglement claim**: Table 4 shows that SOP alone (SDR-S = –1.91) or RST alone (SDR-S = 3.03) fail, but their combination (Ablation-3) yields SDR-S = 7.90 dB and SDR-B = 0.49 dB. This dramatic jump is the paper's strongest evidence that speech and background representations are genuinely decoupled only when both mechanisms are present.

- **Strong speech enhancement results via representation-level manipulation**: By replacing the background representation with that of silence, DeCodec achieves the highest DNSMOS scores on the DNS Challenge blind test sets (OVL 3.39, BAK 4.13 without reverb; OVL 3.13, BAK 3.99 on real recordings), outperforming dedicated SE models including SELM and StoRM (Table 2). The causal variant also surpasses the causal Inter-SubNet baseline.

- **Effective semantic-paralinguistic decomposition via semantic guidance**: Adding SG reduces the semantic-aware WER* from 41.9 (Ablation-3) to 25.8 (DeCodec-c) and 23.6 (non-causal DeCodec), directly enabling the one-shot VC experiments (Table 4).

- **Reconstruction quality is preserved despite the disentanglement overhead**: The non-causal DeCodec achieves the highest SDR on both clean (7.61 dB) and noisy speech (5.21 dB) among all codec baselines, and its WER (1.92) is close to SpeechTokenizer (1.82), indicating semantic content is well-preserved (Table 1).

- **Causal variant remains practically competitive**: DeCodec-c achieves SDR comparable to EnCodec (6.79 vs. 6.86) while adding disentanglement capabilities, and outperforms the causal Inter-SubNet SE model, supporting real-time applicability.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **SE evaluation relies solely on DNSMOS; no intrusive metrics reported**: For a method that claims accurate signal-level decoupling of speech from background, standard intrusive metrics such as PESQ, STOI, or SI-SDR on the simulated test set—where ground-truth clean speech is available—would directly verify that the enhancement recovers a clean waveform without distortion. The current DNSMOS-only evaluation leaves open the possibility that the representations are merely favorable to the DNSMOS model rather than producing genuinely higher-fidelity speech.

- **One-shot VC WER remains high (50.46%) despite improvement over baselines**: The paper acknowledges this is likely due to voicing mismatches between source and reference speech. While the improvement over the cascaded StoRM-SpeechTokenizer baseline (52.73%) is positive, the absolute WER means the converted speech is still substantially degraded. This weakens—though does not invalidate—the claim that semantic and paralinguistic information are cleanly decomposed in noisy conditions.

- **Reconstruction comparison is not bitrate-controlled**: DeCodec uses 4.0+4.0 = 8.0 kbps total (speech + background streams) while baselines operate at 2.0–6.0 kbps. The paper's claim is that DeCodec "maintains advanced signal reconstruction while decoupling representations," which is a reasonable framing given the two-stream design inherently requires more bits. However, without a bitrate-equivalent comparison or a rate-vs-quality tradeoff curve, the magnitude of the reconstruction advantage relative to architecture (vs. bitrate) is unclear.

- **SDR-B and SDR-S computation is not fully specified**: Table 4 defines these as "signal distortion ratios for reconstructing decoupled background sound and decoupled speech," but the precise procedure (e.g., which representations are combined and fed to the decoder) is not described. This makes the ablation metrics harder to interpret and reproduce.

### Trivial

- **The SOP theoretical derivation assumes the encoder output covariance matrix is "angular" (diagonal)**: The paper acknowledges this condition but does not enforce or verify it during training. The practical effect of the orthogonality loss is still a useful inductive bias, and this does not affect the empirical results, but the theoretical link between the loss and the claimed projector structure is loose.

- **The "blank audio" procedure for SE is underspecified**: The paper states that background representations are replaced with those of "a blank audio with the same length" but does not clarify whether this is a zero signal, encoded silence, or a learned null vector.

## Nice-to-Haves

- **Intrusive SE metrics (PESQ, STOI, SI-SDR)** on the simulated test set would strengthen confidence in the enhancement quality and are standard in SE research.

- **Bitrate-controlled comparison or rate-quality tradeoff curves** would sharpen the reconstruction claim and situate DeCodec more precisely among existing codecs.

- **Comparison to a codec trained on clean speech only** would isolate whether the disentanglement actually improves robustness over a codec that never sees background sound—a strong baseline for the "noise-robust" claim.

- **Statistical significance or multiple-run variance** on the main tables would help gauge the reliability of small margins (e.g., the ~2-point WER difference in VC).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"ASR and TTS results rely on appendix-only results"** (from harsh critic): Removed per hard rules—the parser strips appendix sections; these results exist in the original submission. The paper explicitly directs readers to Appendices F and G.

- **"The paper over-claims relative to what is actually shown" regarding universal front-end**: This criticism depends entirely on the stripped appendix content, which we cannot verify as absent. Removed per hard rules.

- **Strength Finder's framing of VC as "robust one-shot voice conversion"**: The improvement over baselines is real but the absolute WER (50.46%) does not support calling the conversion "robust." The strength is retained but re-characterized above.

- **"Comparison to a simple encode-only-speech codec" as a weakness**: Moved to Nice-to-Haves; this is a scope-expanding suggestion, not a flaw in the current evaluation.

## Novel Insights

The paper's key insight—that orthogonal projection combined with cross-utterance representation swapping can attribute speech and background information to separate subspaces within a codec without any explicit separation front-end—is genuinely novel and well-motivated by the auditory neuroscience analogy. The ablation study's demonstration that neither mechanism works alone but their combination produces clean decoupling (SDR-S jumping from sub-3 dB to 7.90 dB) provides a crisp, falsifiable finding that advances understanding of how disentanglement can be achieved in learned audio representations.

## Suggestions

- Clarify the SDR-B and SDR-S computation procedure in Table 4 so readers can interpret exactly what the decoupled reconstructions measure.
- Specify the blank-audio representation used for SE (zero signal, encoded silence, or learned null vector).
- Consider reporting at least one intrusive SE metric (PESQ, STOI, or SI-SDR) on the simulated test set where ground truth is available; this would substantially strengthen the SE claims at low cost.
- If the appendix ASR/TTS results are strong, a one-paragraph summary or small table in the main body would better support the universal-front-end narrative without requiring the reader to consult supplementary material for central claims.

---

**Anchors used for calibration:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| USC | Id2JMVSQHZ | 4.80 | R1 mid | DeCodec is clearly stronger: more novel mechanism, better ablations, broader tasks |
| RepCodec | LfDUzzQa3g | 5.50 | R1 mid | DeCodec has broader scope and stronger ablation; RepCodec is more narrowly evaluated |
| Vec-Tok Speech | C53xlgEqVh | 5.20 | R2 | DeCodec has clearer core contribution and more downstream validation |
| GenSE | 1p6xFLBU4J | 6.00 | R2 | Comparable: similar evaluation breadth, DeCodec has stronger novelty, GenSE has deeper per-task evaluation |
| CLaM-TTS | ofzeypWosV | 6.40 | R2 | CLaM-TTS has deeper evaluation for its single task; DeCodec broader but thinner per task |
| FlowDec | uxDFlPGRLX | 7.00 | R2 | FlowDec is stronger: more thorough evaluation (MUSHRA), stronger theoretical contribution |

**Round 1 bracket:** 4.80–7.00, narrowed to ~5.5–6.5 based on comparison with USC (weaker) and FlowDec (stronger).

**Round 2 narrowing:** Comparison against GenSE (6.00, similar evaluation breadth, stronger novelty for DeCodec) and CLaM-TTS (6.40, deeper single-task evaluation) places DeCodec near 6.0—comparable to GenSE but not reaching the depth of CLaM-TTS or FlowDec.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>