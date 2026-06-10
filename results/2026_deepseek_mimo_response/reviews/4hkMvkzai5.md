Now I have enough calibration data. Let me finalize the review.

**Round 1 bracket:** 5.0–6.5. The paper is clearly more novel and better validated than USC (4.80, Reject), RepCodec (5.50, Reject), and Vec-Tok (5.20, Reject). It's comparable to GenSE (6.00, Accept) and Vevo (5.50, Accept), but has more identified issues than GenSE while also having stronger architectural novelty.

**Round 2 narrowing:** After comparing against GenSE (6.00, Accept), Vevo (5.50, Accept), HALL-E (6.40, Accept), and VQScore (7.00, Accept), DeCodec sits around 6.0. It has broader demonstrated capabilities than Vevo and comparable SE contributions to GenSE, but the bitrate fairness issue and mathematical overclaiming prevent a higher score. Score: **6.0**.

---

## Summary
DeCodec introduces a neural audio codec that hierarchically disentangles audio into orthogonal speech and background sound subspaces (via a Subspace Orthogonal Projection module and Representation Swap Training) and further decomposes speech into semantic and paralinguistic components (via Semantic Guidance). This enables speech enhancement and one-shot voice conversion through simple representation recombination at inference time, without task-specific fine-tuning.

## Strengths
- **SE results surpass dedicated models via simple representation manipulation**: Table 2 shows DeCodec achieves the highest DNSMOS scores overall (OVL 3.39/3.13, BAK 4.13/3.99 on simulation/real recordings), outperforming dedicated SE systems (SELM: 4.10/3.44 BAK; StoRM: 3.94/3.38 BAK). This is achieved purely by replacing background sound representations with those from "blank audio," demonstrating the genuine practical utility of disentangled representations.
- **Clean ablation demonstrating SOP+RST synergy**: Table 4 shows SOP alone yields SDR-B=-13.15 dB and RST alone yields SDR-B=-10.67 dB — both fail at disentanglement. Their combination jumps to SDR-B=0.49 and SDR-S=7.90, providing clear quantitative evidence that both components are jointly necessary.
- **Novel and elegant paradigm**: The core idea — that a codec with disentangled representations can perform SE and VC through simple code manipulation without dedicated architectures — is conceptually clean and substantiated by competitive empirical results across multiple tasks.
- **Causal variant is competitive**: Table 2 shows DeCodec-c achieves BAK=3.94 on real recordings, exceeding non-causal dedicated models StoRM (3.38) and SELM (3.44), confirming viability for streaming applications.

## Weaknesses

### Fatal
None.

### Major
- **Bitrate fairness confounds reconstruction claims**: Table 1 shows DeCodec operates at 8.0 kbps (4.0+4.0 for two parallel RVQs) while baselines range from 2.0 (HiFi-Codec) to 6.0 (EnCodec). The headline claim of highest SDR (7.61 vs. 6.86 for EnCodec) cannot be attributed to architectural design versus the 33% capacity advantage over the strongest baseline. The paper never discusses this or provides matched-bitrate comparisons. While the dual-RVQ architecture inherently requires more bitrate (one stream for speech, one for BGS), the absence of any analysis makes the reconstruction quality claim uninterpretable.

- **SG's negative effect on disentanglement goes unacknowledged**: Table 4 shows adding SG (Ablation-3 → DeCodec-c) causes SDR-B to drop from 0.49 to -1.11 dB — background sound disentanglement becomes negative — and SDR-O drops from 6.68 to 4.62. The paper describes this only as "a slight decrease in SDR but a significant reduction in WER*" without acknowledging that disentanglement quality degrades substantially. This tradeoff is central to understanding the system and deserves explicit analysis.

- **SOP mathematical framing overstates implementation guarantees**: Section 3.4 defines projection operators satisfying P_S + P_N = I and P_S P_N^T = 0 (Eq. 4, 6), but the implementation (Eq. 5) only enforces output orthogonality. The completeness property P_S + P_N = I — essential for the direct sum decomposition claimed in Eq. 2-4 — is never enforced. The derivation in Eq. 6-7 argues that orthogonality of outputs implies orthogonality of projection matrices under an "angular matrix" condition on YY^T, but this condition is neither defined precisely nor verified. The system works because reconstruction loss implicitly encourages completeness, but the formal framework overstates what the implementation delivers.

### Minor
- **One-shot VC WER of ~50%**: Table 3 shows DeCodec achieves WER=50.46%, meaning roughly half of words are misrecognized. While this outperforms StoRM-SpeechTokenizer (52.73%), the abstract's claim of "effective one-shot voice conversion on noisy speech" overstates practical utility. The paper acknowledges voicing misalignment as the cause but frames it as incidental.
- **"Blank audio" for SE underspecified**: Section 4.2.2 states background sound representations are replaced with those from "a blank audio" without specifying whether this is silence, a learned zero vector, or something else.
- **Total training loss not shown**: Individual loss components are described separately (reconstruction, adversarial, orthogonality, RST, SG) but their combination and weighting are not presented in the main paper.
- **RST argument presented as "proof" but is a heuristic**: Section 3.6's Eqs. 13-16 assume perfect reconstruction (Eqs. 13-14) and that the Jacobian ∂Dec/∂Zn is approximately independent of Zs. These are assumptions about the decoder's behavior, not derived properties. This should be presented as motivating intuition.

## Nice-to-Haves
- Matched-bitrate comparisons (e.g., EnCodec/DAC at 8 kbps or DeCodec at 6 kbps) to isolate architectural gains from capacity.
- Comparison with dedicated speech separation models (Conv-TasNet, SepFormer) for the disentanglement capability.
- Analysis of why SG degrades SDR-B and whether this can be mitigated.
- Mutual-information-based metrics for measuring information leakage between speech and BGS code streams.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Strength Finder's claim that the RST "proof" is rigorous: contradicted by the paper's own assumptions (Eqs. 13-14 assume perfect reconstruction, which never holds in practice). Demoted to heuristic argument.
- Strength Finder's claim that DeCodec has best reconstruction quality: partially invalidated by the bitrate fairness issue; cannot attribute the gain purely to architecture.
- Neuroscience analogy as a weakness: the A2 cortical mapping is loosely motivated but doesn't harm the core contribution; this is a presentation choice.
- Missing appendix content (ASR/TTS results): stripped by parser, not genuinely missing from the submission.

## Novel Insights
The paper's genuinely novel contribution is the SOP+RST paradigm for speech/background sound disentanglement within a codec. The ablation cleanly demonstrates that SOP and RST are jointly necessary — neither alone achieves disentanglement — which is a meaningful finding. The SE-by-recombination approach is elegant and practically validated, outperforming dedicated models. The observation (in the ablation data, if not explicitly discussed) that SG trades off disentanglement for semantic preservation is also a valuable insight for the community, even though the paper underacknowledges it.

## Suggestions
- Add matched-bitrate reconstruction comparisons to isolate architectural contributions from capacity effects.
- Explicitly discuss the SG–disentanglement tradeoff rather than minimizing it as "a slight decrease."
- Specify what "blank audio" means in the SE procedure.
- Moderate the RST section from "theoretical proof" to "motivating argument."
- Moderate the abstract's VC claim to reflect the ~50% WER limitation.

## Score and Decision

**Calibration anchors retrieved:**

Round 1:
- DM-Codec (3.00, Reject): Speech tokenizer, lacks novelty. DeCodec is clearly stronger.
- UniAudio (3.00, Reject): Audio foundation model, rejected. DeCodec >> this.
- USC (4.80, Reject): Disentangled speech codec for privacy. Less novel than DeCodec; missing related work.
- GenSE (6.00, Accept): Generative SE via language models. Comparable contribution level to DeCodec, both accepted with some weaknesses.
- RepCodec (5.50, Reject): Speech representation codec. Cleaner but narrower than DeCodec.
- Codec-LM co-design (5.00, Reject): Codec improvements for TTS. Less ambitious than DeCodec.
- VQScore (7.00, Accept): Self-supervised SE metric. Cleaner contribution, fewer identified issues, less ambitious.
- Progressive Compression (8.00, Accept): Diffusion compression, not topically relevant.

Round 2:
- USC (4.80, Reject): Already seen. DeCodec clearly better.
- RepCodec (5.50, Reject): Already seen. DeCodec more ambitious and better validated.
- Codec-LM (5.00, Reject): Already seen. DeCodec has more novelty.
- Vec-Tok Speech (5.20, Reject): Speech vectorization/tokenization. DeCodec has stronger results.
- Vevo (5.50, Accept): Controllable voice imitation with disentanglement. Comparable novelty; DeCodec has stronger SE results and cleaner ablation.
- GenSE (6.00, Accept): Already seen. DeCodec comparable in contribution.
- HALL-E (6.40, Accept): Hierarchical neural codec LM for TTS. Different scope, comparable quality.
- VQScore (7.00, Accept): Already seen. DeCodec has more identified weaknesses but broader scope.

**Bracket:** Round 1 placed the paper between 5.0 and 6.5. Round 2 confirmed DeCodec is comparable to GenSE (6.00) — both have strong, novel contributions with identifiable weaknesses — and clearly stronger than papers rejected at 5.0-5.5. The bitrate fairness issue and mathematical overclaiming prevent it from reaching the VQScore level (7.00). Final score: 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>