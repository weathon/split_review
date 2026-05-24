Now I have sufficient calibration context. Let me write the final review.

## Summary
This paper proposes DeCodec, a neural audio codec that learns to hierarchically disentangle audio representations: (1) speech vs. background sound via a Subspace Orthogonal Projection (SOP) module + Representation Swap Training (RST), and (2) within speech, semantic vs. paralinguistic via semantic guidance (SG). The model is built on the DAC encoder-decoder with parallel residual vector quantizers for the two audio components. Experiments demonstrate that the decoupling is effective (ablation shows SOP+RST together give SDR-B=0.49, SDR-S=7.90), and that the model can serve as a unified front-end for speech enhancement (DNSMOS scores competitive with or exceeding dedicated SE models), one-shot voice conversion on noisy speech, and downstream ASR/TTS tasks.

## Strengths
- **Novel and well-motivated disentanglement objective.** The paper is the first to explicitly decouple speech and background sound in the codec representation domain. The SOP+RST combination is a principled approach (orthogonality constraint + cross-sample reconstruction swapping), and the ablation study (Table 4) cleanly shows that neither SOP nor RST alone achieves decoupling, while together they yield positive SDR-B (0.49) and high SDR-S (7.90). This is the strongest evidence in the paper.

- **Multiple downstream demonstrations from a single model.** DeCodec is evaluated on reconstruction, speech enhancement, one-shot VC, and (in the appendix) ASR and TTS — all from the same trained model without task-specific fine-tuning. The SE results (Table 2) are particularly impressive: DeCodec achieves the highest DNSMOS OVL (3.39) and BAK (4.13) scores on synthetic data, surpassing dedicated models like SELM and StoRM.

- **Semantic guidance enables noise-robust semantic/paralinguistic decomposition.** The co-optimization of speech-background decoupling with semantic guidance yields representations that are robust to noise. In one-shot VC with noisy speech (Table 3), DeCodec achieves WER 50.46% and SIM 0.83 without any separate denoising front-end, substantially outperforming SpeechTokenizer (74.18% WER) and comparably to the cascaded StoRM-SpeechTokenizer (52.73% WER).

## Weaknesses

### Major
- **Bitrate mismatch undermines the reconstruction comparison.** DeCodec operates at 4.0+4.0 = 8 kbps total, while the baselines in Table 1 use lower bitrates (EnCodec 6 kbps, DAC 4.5 kbps, SpeechTokenizer 4 kbps). Higher bitrate directly provides more capacity, which can trivially explain the SDR advantage. The paper does not acknowledge this disparity or attempt a matched-bitrate comparison (e.g., reducing DeCodec to 6 kbps or adding RVQ layers to baselines). The ablation itself shows that adding disentanglement mechanisms drops SDR-O from 8.93 dB (Ablation-1, SOP only) to 5.21 dB (full DeCodec) — a ~3.7 dB loss — which further suggests the headline SDR in Table 1 significantly benefits from the higher bitrate budget rather than the disentanglement design. The reconstruction claim would be much stronger with a controlled experiment at a matched bitrate.

### Minor
- **The speech enhancement procedure is under-specified.** The paper states that SE is performed by replacing the BGS representation of the noisy input with "the background sound representations of a blank audio with the same length." It is not explained what "blank audio" is (silence?), how its BGS representation is obtained (is it simply zero?, does feeding silence through the encoder+NRVQ produce a well-defined code?), or whether this representation is precomputed once. The operation is reasonable (zero out or replace with the silence code), but the lack of clarity invites unnecessary speculation about oracle behavior. A one‑sentence clarification would resolve this.

- **Theoretical justification of RST is heuristic, not rigorous.** The mean-value theorem argument in Section 3.6 assumes the decoder is approximately linear and conflates functional non-dependence with statistical independence. The step from "the left side depends on Zs₁" to "Zs₁ must be independent of n₁" is not formally justified. This does not detract from the empirical evidence (the ablation is convincing), but the paper should frame this as an intuitive justification rather than a proof.

- **One-shot VC WER remains high.** The reported WER of 50.46% means nearly every other word is incorrect, which limits the practical utility of the VC capability. The paper acknowledges this limitation (voicing mismatch), but the framing as "effective" one-shot VC should be tempered given the high absolute WER.

### Trivial
- **Figure 2 caption vs. text discrepancy on the encoder.** The figure caption says "the input y is split into two encoders (Enc) to produce Yl and Yr," while Sections 3.2–3.3 describe a single encoder. The figure likely illustrates the RST training path (two separate samples through the same encoder), but the caption is ambiguous. This should be harmonized.

## Nice-to-Haves
- A controlled reconstruction experiment at a matched bitrate (e.g., DeCodec at 6 kbps vs. EnCodec at 6 kbps) would significantly strengthen the claim that decoupling does not hurt reconstruction.
- The ASR and TTS results currently in the appendix would add value to the main paper, since the abstract and conclusion highlight downstream task support.
- The exact number of RVQ layers and codebook sizes for SRVQ and NRVQ should be explicitly stated.

## Removed Points
- **Harsh critic's point about "DeCodec classifies noisy speech as 'sound' type" being a mischaracterization of UniCodec.** This is not a weakness of the current paper — it is a characterization of prior work and does not affect the validity of DeCodec's claims. *Removed because it is not a weakness of the paper under review.*
- **Criticism about missing downstream ASR/TTS results not being in the main paper.** The paper clearly states these are in Appendices F and G, which were stripped by the PDF parser. These exist in the original submission. *Removed per hard rules about missing appendix content.*
- **"Fairness of SE baselines" about training data.** The baselines (InterSubNet, StoRM, SELM) are cited with results taken from published papers (Wang et al., 2024), which is standard practice. The paper uses a standard DNS Challenge test set. *Removed because this is not a concrete weakness — it speculates about a potential confound without evidence.*
- **Reproducibility nitpick about exact RVQ configuration.** This is a minor detail that can be clarified, but demanding exact layer counts and codebook sizes for every component exceeds what is standard for a conference paper. *Demoted to Nice-to-Have rather than a weakness.*
- **"SE with blank audio is oracle-like" interpretation.** As clarified above, the operation does not require an oracle — encoding silence once and reusing the BGS code is straightforward. The paper just needs to explain it better. *Demoted from potential fatal flaw to Minor clarity issue.*

## Novel Insights
None beyond the paper's own contributions. The reviews surface the standard tension between ambitious claims and controlled experimental design, but do not reveal an unrecognized connection or contradiction that the paper itself misses.

## Suggestions
1. **Run a controlled reconstruction experiment at a matched bitrate** — even a single ablation reducing DeCodec to ~6 kbps (by removing some RVQ layers) and comparing against EnCodec at 6 kbps. This single change would transform the reconstruction claim from ambiguous to compelling.
2. **Clarify the SE procedure**: state explicitly that "blank audio" means silence, and that its BGS code is obtained by passing a silent waveform through the encoder + SOP + NRVQ (which can be precomputed once). Or alternatively, simply set the BGS code to zero and report that result.
3. **Reframe the theoretical RST argument** as an intuitive justification rather than a formal proof, or provide a more rigorous argument.
4. **Move one downstream task table** (ASR or TTS) from the appendix to the main paper to support the claims made in the abstract and conclusion.

## Score and Decision

**Bracket Determination (Round 1):** Three queries across weak (avg < 3.5), middle (3.5–7.5), and strong (> 7.5) bands retrieved anchors on audio codecs, speech disentanglement, and representation learning. Weak anchors (scores 2.50–3.25) were papers with nonsensical or incomplete contributions, clearly below the current paper. Middle anchors (3.75–5.50) included USC (4.80) and RepCodec (5.50), which share topical overlap but have weaker evidence or less novelty. Strong anchors (7.60–8.50) were on unrelated topics (diffusion models, gesture generation) and not directly comparable. **Initial bracket: 4.5–7.0.**

**Narrowing (Round 2):** Two queries within (4.5, 6.5) and (5.5, 7.5) retrieved GenSE (6.00, accepted) and FlowDec (7.00, accepted) as the most relevant anchors. GenSE is a strong anchor: it also tackles speech processing with a codec-based approach, and reviewers accepted it (6.00) despite noting limited novelty, because the empirical results were impressive. The current paper has *greater novelty* but *somewhat weaker experimental controls* (the bitrate issue). FlowDec (7.00) is a polished paper with thorough evaluation and cleaner comparisons; the current paper does not reach that level of experimental rigor.

**Final score:** **6.0**. The paper is comparable to GenSE (6.00): both have a clear contribution and strong empirical results, but both have notable limitations. The current paper's bitrate mismatch prevents a cleaner score. It is clearly above the 4.80–5.50 range (USC, RepCodec) where novelty or evidence was significantly weaker. A 6.0 reflects a solid, novel contribution that would benefit from addressing the bitrate control and clarity issues before publication.

**Anchor references:** USC (Id2JMVSQHZ, 4.80, R1 middle) — less novel disentanglement, missing baselines; RepCodec (LfDUzzQa3g, 5.50, R1 middle) — simpler idea, limited evaluation; GenSE (1p6xFLBU4J, 6.00, R2) — comparable quality but lower novelty; FlowDec (uxDFlPGRLX, 7.00, R2) — stronger experimental rigor.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>