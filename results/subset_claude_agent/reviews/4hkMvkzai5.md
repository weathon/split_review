Now I have sufficient calibration to write the final review.

**Round 1 Bracket**: 4.5 – 6.5  
- Papers at 3.0–3.25 are clearly weaker (limited novelty, no clear contribution)
- USC (4.8), Codec-LM co-design (5.0), RepCodec (5.5) are the closest middle anchors
- GenSE (6.0, accepted) has comparable scope but was criticized for novelty

**Round 2 Narrowing**: DeCodec is more novel than RepCodec (5.5) and USC (4.8) in addressing a genuinely first-of-kind problem, but the bitrate confound and cross-paper SE comparison are substantial evaluation flaws that GenSE (6.0, accepted) does not have. This places DeCodec around **5.0–5.5**, closer to RepCodec/Codec-LM than to GenSE given the evaluation issues.

---

## Summary
DeCodec rethinks neural audio codecs as universal disentangled representation learners, introducing a Subspace Orthogonal Projection (SOP) module and a Representation Swap Training (RST) procedure to explicitly decouple speech and background sound into orthogonal parallel RVQ streams. Semantic Guidance (SG) further decomposes the speech stream into semantic and paralinguistic components. The single model enables speech enhancement, one-shot voice conversion on noisy speech, ASR feature extraction, and controllable TTS without cascaded front-end processing.

---

## Strengths

- **Novel and well-motivated problem formulation**: No prior neural codec explicitly decouples speech from background sound in the representation domain. DeCodec addresses a genuine gap: existing universal codecs (EnCodec, DAC, UniCodec) treat noisy speech as a single signal, preventing downstream selective processing. The motivation is concrete, the gap is real, and the proposed solution (parallel RVQ streams operating in orthogonal subspaces) is architecturally coherent.

- **Ablation study cleanly establishes joint necessity of SOP and RST** (Table 4): SOP alone yields SDR-B = −13.15 dB and SDR-S = −1.91 dB; RST alone yields SDR-B = −10.67 dB and SDR-S = 3.03 dB. Their combination achieves SDR-B = 0.49 dB and SDR-S = 7.90 dB. This is the paper's strongest and most credible evidence — two components that individually fail but jointly succeed.

- **Semantic Guidance contribution clearly isolated** (Table 4, Ablation-3 vs. DeCodec): Adding SG to the SOP+RST base reduces downstream ASR WER\* from 41.9 to 23.6 with only minor SDR change, confirming that hierarchical decomposition of speech is effective and separable from the speech–background decoupling task.

- **Multi-task coverage from a single unified codec**: The paper demonstrates SE, one-shot VC, ASR feature extraction, and TTS controllability from one model — a practically significant demonstration that representation-domain disentanglement replaces cascaded front-ends.

- **Noise-robust VC versus strongly degraded baseline**: DeCodec achieves WER = 50.46, SIM = 0.83 on noisy VC, while SpeechTokenizer alone produces near-unintelligible output (WER = 74.18), showing the core value of the approach even if the final numbers are not impressive in absolute terms.

---

## Weaknesses

### Fatal
None.

### Major

- **Bitrate confound invalidates the reconstruction comparison headline** (Table 1): DeCodec operates at 4.0 + 4.0 = **8.0 kbps total**, while all baselines use 2.0–6.0 kbps (EnCodec: 6.0, DAC: 4.5, SpeechTokenizer: 4.0, HiFi-Codec: 2.0). At higher bitrate, any codec achieves higher reconstruction fidelity. The SDR advantage of DeCodec over EnCodec (7.61 vs. 6.86, Δ = 0.75 dB) cannot be attributed to the disentanglement design; it may simply reflect 2 kbps of additional capacity. No ablation at reduced total bitrate (e.g., 2+2 streams) and no 8 kbps EnCodec/DAC baseline are provided. The paper's claim that "DeCodec achieves the highest SDR for speech reconstruction... demonstrating the proposed system can ensure the performance of complete signal reconstruction while decoupling representations" is unsupported on a like-for-like basis. This confound affects the paper's primary reconstruction table.

- **SE comparison mixes evaluation conditions and relies solely on a non-intrusive metric** (Table 2): Section 4.1 explicitly states: "The results of these models on the DNS Challenge testset are taken from the paper (Wang et al., 2024)." DNSMOS scores are sensitive to resampling, normalization, and audio duration handling conventions. The paper reports no intrusive reference-based metrics (SI-SNR, PESQ, STOI) for any comparison point. The claim that DeCodec "outperforms various existing SE models" cannot be verified without a controlled re-evaluation. Note that on real recordings, SIG actually favors SELM (3.59 vs. 3.45 for DeCodec) — a result the paper mentions but does not emphasize. The SE capability itself is real and interesting, but the specific claim of superiority over dedicated SE models is not properly established.

### Minor

- **"Theoretical proof" of RST disentanglement (Section 3.6) is overstated**: The proof applies the mean-value theorem and concludes from Eq. (16) that because the right-hand side (n₂ − n₁) does not depend on Zs₁, Zs must be independent of background sound. However, the Jacobian ∂Dec/∂Zn|_ξ still passes through ξ, which is evaluated at a point that depends on both Zn₁, Zn₂ and the decoder's operating point set by Zs₁. For a nonlinear decoder, the Jacobian at ξ generally does depend on Zs₁. The argument is valid only for a linear decoder, which is not the case. The result is better described as "intuitive motivation" rather than a proof, and its current framing as a theoretical guarantee is misleading (Section 3.6: "we theoretically prove that the proposed L_RST can further force Zs ∈ V_S to be speech representations only"). The empirical ablation is unaffected, but the theoretical framing is overstated.

- **Voice conversion WER margin is narrow and statistically untested** (Table 3): DeCodec achieves WER = 50.46 vs. StoRM-SpeechTokenizer's 52.73 — a 2.27-point gap with identical SIM (0.83) and no statistical significance testing. Absolute WER of ~50% is also very high. The paper attributes this to voicing time mismatch but does not quantify the failure rate or condition on match/mismatch. The claim that DeCodec "introduces less error than the front-end time-domain separation method" is not well-supported by this narrow margin.

### Trivial

- No confidence intervals or standard deviations are reported for any table, particularly relevant for the 2.27-point VC WER margin on 300-clip test sets.

---

## Nice-to-Haves

- **Bitrate-matched reconstruction comparison**: ablate DeCodec at 4 kbps total (2+2 streams), or add EnCodec/DAC baselines at 8 kbps. If the SDR advantage survives, the reconstruction claim is properly grounded. If not, the paper can still argue that DeCodec achieves competitive reconstruction *while* achieving disentanglement, which is still a meaningful claim.
- **Controlled SE re-evaluation**: run Inter-SubNet, StoRM, and SELM on the DNS Challenge test set under identical pipeline, and add at least one intrusive metric (SI-SNR or PESQ) alongside DNSMOS.
- **VC conditional analysis**: report WER separately for voicing-time-matched vs. mismatched pairs to diagnose how much of the absolute 50% WER is attributable to the fundamental conversion task vs. the identified failure mode.
- Reframe Section 3.6 from "theoretically prove" to "provide intuition under decoder linearity assumptions" or derive the result under an explicitly stated linearity condition.

---

## Removed Points

*These points are flagged as removed; treat them with caution — they may contain useful signal despite not meeting the bar for the final review.*

1. **Harsh Critic — SOP covariance assumption (Section 3.4)**: The "angular matrix" condition (that encoder channels are mutually independent) is a theoretical analysis convenience, not a runtime requirement the method depends on. The L_⊥ loss enforces soft orthogonality empirically regardless of whether the exact condition holds. Removed as speculative.

2. **Harsh Critic — SE causal comparison margin (0.05 OVL)**: The paper's own language is "achieves performance comparable to" — appropriately hedged. Removed as not rising to a criticism.

3. **Strength Finder — "State-of-the-art SE via representation recombination"**: This strength is undermined by the cross-paper evaluation confound and is demoted accordingly.

4. **Strength Finder — "Competitive signal reconstruction despite disentanglement modules"**: This strength cannot be cleanly held given the bitrate confound. The reconstruction numbers prove DeCodec works at 8 kbps, but not that it is efficient relative to baselines at lower bitrate.

5. **Harsh Critic — RST training requires paired clean/noisy sources**: The paper's Section 4.1 training setup uses synthetically mixed audio (speech + ESC-50/DNS-Noise) where clean components are known. This is clearly described, and the method's scope (training on labeled mixes) is adequately stated. Removed as addressed.

---

## Novel Insights

The most structurally interesting observation is about the bitrate interpretation: DeCodec's dual 4.0 kbps streams are not allocating extra capacity for better reconstruction — they are allocating separate codebooks for distinct perceptual components. In this light, a fair comparison is not DeCodec at 8 kbps vs. EnCodec at 8 kbps, but rather: *at what minimum per-stream bitrate does DeCodec's disentanglement hold?* If speech can be adequately represented at 2 kbps SRVQ and background at 2 kbps NRVQ (4 kbps total), then the method would be efficiency-neutral with existing baselines while gaining the disentanglement capability — a much stronger result. This framing would transform what is currently a confounded comparison into a clear architectural contribution.

---

## Suggestions

1. Add a 4 kbps total DeCodec ablation (2+2 streams) in Table 1 to establish bitrate-neutral reconstruction performance.
2. Re-run SE baselines under controlled conditions; add SI-SNR or PESQ alongside DNSMOS.
3. Report bootstrap confidence intervals for WER-based comparisons (Table 3), particularly the 2.27-point VC gap.
4. Revise Section 3.6 to reframe the "proof" as a "theoretical motivation" or explicitly state the linearity assumption required.
5. Report VC WER conditioned on voicing-time match/mismatch to contextualize the 50% absolute WER.

---

## Score and Decision

**Calibration Anchors:**

| Path | Avg Human Score | Round | Comparison to DeCodec |
|---|---|---|---|
| `UFwefiypla.md` (DM-Codec) | 3.00 | R1 | Weaker – more incremental, less novelty |
| `nhgTmx1TZJ.md` (UniAudio) | 3.00 | R1 | Weaker – broader LLM application, less focused |
| `Id2JMVSQHZ.md` (USC Privacy) | 4.80 | R1/R2 | Weaker – narrower problem, ignores related work, worse evaluation |
| `LfDUzzQa3g.md` (RepCodec) | 5.50 | R1/R2 | Similar quality – clean evaluation, less novel problem |
| `KCVv3tICvp.md` (Codec-LM co-design) | 5.00 | R1/R2 | Similar quality – incremental engineering, no fundamental new capability |
| `C53xlgEqVh.md` (Vec-Tok Speech) | 5.20 | R2 | Similar – multi-task codec but less novel disentanglement |
| `1p6xFLBU4J.md` (GenSE) | 6.00 | R2 | Slightly stronger – accepted, better evaluation rigor despite novelty concerns |

**Round 1 Bracket**: 4.5 – 6.5  
**Round 2 Narrowing**: DeCodec is more novel than RepCodec (5.5) and USC (4.8) in tackling a genuinely first-of-kind problem with two new technical modules. However, the two Major weaknesses (bitrate confound, cross-paper SE evaluation) are more significant than anything in RepCodec's review, and GenSE (6.0, accepted) has better evaluation discipline despite similar scope. This places DeCodec at approximately **5.0** — meaningfully above USC (4.8) for higher novelty, below RepCodec (5.5) for larger evaluation gaps, and notably below GenSE (6.0) for evaluation quality issues.

The paper makes a genuinely interesting contribution that deserves to be published, but the current form overstates its reconstruction and SE advantages through unfair comparisons. These are fixable problems; the core contribution (disentanglement capability, ablation, multi-task coverage) is real and would survive a revision that narrows the claims to what the evidence actually shows.

**Originality**: High — first speech+background disentanglement codec  
**Research question importance**: High — enables controllable audio processing without front-end cascading  
**Claims well-supported**: Moderate — disentanglement claims are well-supported; reconstruction/SE superiority claims are not  
**Soundness of experiments**: Moderate — ablation is sound; main comparisons have confounds  
**Clarity of writing**: Good — architecture and motivation are clearly described  
**Value to community**: High if evaluation issues are resolved; moderate in current form

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>