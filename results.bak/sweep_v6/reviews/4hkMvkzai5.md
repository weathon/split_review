Now I have all the information I need. Let me produce the final consolidated review.

## Summary

DeCodec proposes a neural audio codec that explicitly decouples speech and background sound (BGS) into orthogonal subspaces, and further decomposes speech into semantic and paralinguistic components via semantic guidance. The key technical innovations are a Subspace Orthogonal Projection (SOP) module and a Representation Swap Training (RST) procedure. The paper demonstrates that this disentangled codec can serve as a universal front-end for multiple downstream tasks — speech enhancement (via BGS replacement), one-shot voice conversion on noisy speech, and noise-robust ASR/TTS support — without task-specific fine-tuning. The core idea is novel and well-motivated by auditory neuroscience, and the ablation study confirms that both SOP and RST are jointly necessary for measurable decoupling.

## Strengths

- **Novel architecture for explicit speech–BGS decoupling in a codec**: The combination of SOP (orthogonal projection) and RST (swap training) to learn disentangled speech and BGS representations within a single codec framework is genuinely novel. Ablation results (Table 4) show that neither SOP alone (SDR-B –13.15) nor RST alone (SDR-B –10.67) work, but together they achieve SDR-B of 0.49 — a clear improvement that demonstrates the joint necessity of both components. This goes beyond prior disentanglement codecs (SpeechTokenizer, FACodec) that only work on clean speech.

- **Speech enhancement via representation replacement achieves competitive DNSMOS scores**: By replacing only the BGS quantized vector with that of a blank audio, DeCodec achieves DNSMOS OVL 3.39 on the DNS Challenge test set, outperforming the reported scores of specialized SE models (SELM: 3.26, StoRM: 3.21) — including in background suppression (BAK 4.13). This provides strong indirect evidence that the disentanglement is working, and demonstrates a practical advantage: controllable feature selection without dedicated SE model training.

- **Causal version with competitive latency-performance trade-off**: DeCodec-c (causal) achieves DNSMOS OVL 3.31 — outperforming the causal Inter-SubNet (3.10) and approaching the non-causal SELM (3.26) — while also providing SDR of 6.79 on clean reconstruction (Table 1). This shows the approach is practical for low-latency applications.

- **Demonstration of reduced error propagation vs. cascaded pipelines**: In one-shot VC on noisy speech (Table 3), DeCodec (WER 50.46%) outperforms StoRM-SpeechTokenizer (WER 52.73%) while matching speaker similarity (0.83). This supports the claim that representation-domain decoupling introduces less distortion than front-end time-domain separation.

## Weaknesses

### Major

- **Reconstruction comparison at unmatched bitrates (Table 1)**: DeCodec operates at 8 kbps (4.0+4.0) while the baselines span 2–6 kbps. The causal DeCodec-c (8 kbps, SDR 6.79) is comparable but slightly worse than EnCodec (6 kbps, SDR 6.86), meaning DeCodec uses more bits for marginally less reconstruction quality. The paper's claim that "the proposed DeCodec achieves the highest SDR for speech reconstruction" is not meaningful at different bitrates. However, this weakness does not invalidate the paper's core contribution (decoupling) — it only weakens the secondary argument that reconstruction is maintained. A controlled comparison at matched bitrate (e.g., reducing DeCodec's RVQ levels to match 6 kbps or 4.5 kbps) is needed.

- **Theoretical justification of RST (Eq. 13–16) is non-rigorous**: The proof attempts to use the mean value theorem for vector-valued functions to show that the RST loss forces Zs to be independent of background sound. The mean value theorem for vector functions does not guarantee a single ξ between Zn₁ and Zn₂ for the vector-valued decoder, and the step from Eq. (15) to (16) is a heuristic approximation, not a formal derivation. The existence of a single ξ for each dimension simultaneously is not generally true. The conclusion therefore does not follow rigorously. That said, the *empirical* evidence (ablation + SE results) still supports the method — the proof is better presented as a motivating sketch rather than a formal guarantee.

### Minor

- **Speech enhancement baseline numbers are taken from a prior paper without matched evaluation**: The DNSMOS scores for Inter-SubNet, StoRM, and SELM are cited from Wang et al. (2024). While the DNS Challenge test set is standard and DNSMOS is designed as a non-intrusive metric, the evaluation pipeline (pre-processing, test set filtering, DNSMOS version) may differ. Given the small margins (OVL 3.39 vs 3.26, BAK 4.13 vs 4.10), this is a reliability concern. Running baselines under identical conditions would strengthen the claim.

- **One-shot VC WER of 50.46% is very high in absolute terms**: The paper acknowledges this and attributes it to voicing mismatch (e.g., voiced input vs. unvoiced reference). However, calling this "effective one-shot VC" is misleading — 50% WER means roughly every other word is wrong. The comparison to StoRM-SpeechTokenizer (52.73%) is favorable, but both are poor in absolute terms. The paper would benefit from a failure analysis and clearer scope for what use cases this quality suffices for.

- **Decoupling quality (SDR-B) is modest in absolute terms**: SDR-B of 0.49 dB (Ablation-3) is low, though it represents a major improvement over –13.15 dB (SOP only) and –10.67 dB (RST only). The paper does not report a source separation metric (e.g., SI-SNRi) that could more directly quantify decoupling quality, nor does it compare against a dedicated separation model baseline.

- **The derivation of P_S P_N^T = 0 from orthogonality loss (Section 3.4) is hand-wavy**: The assumption that YY^T is an "angular matrix" with independent feature channels is stated without justification. The orthogonality constraint L_⟂ is still effective in practice, but the theoretical framing overclaims what is actually proven.

### Trivial

- Table 2 shows DeCodec (non-causal) achieving SIG 3.45 on real recordings, which is below SELM's 3.59, yet the paper states "the highest DNSMOS scores in both simulation and real recording test sets" — this is accurate for OVL/BAK but not for SIG on real recordings.
- Table 4 SDR-B becomes negative with SG (–1.11 for DeCodec-c, –0.36 for DeCodec), suggesting SG somewhat interferes with BGS decoupling, but this is not discussed.

## Nice-to-Haves

- Add a controlled bitrate experiment (e.g., DeCodec at 4.5 or 6 kbps by halving RVQ levels) to make the reconstruction comparison fair.
- Include direct source separation baselines (ConvTasNet, DPRNN-TasNet) with SI-SNRi metrics to quantify decoupling quality.
- Visualize the orthogonal subspace correlation (e.g., PCA of S and N representations) to verify orthogonality beyond SDR.
- Analyze information leakage by running ASR on the BRS-only decoded output and a speech activity detector on the separated outputs.
- Run the SE baselines under identical evaluation conditions or use the official DNS Challenge scoring script.

## Removed Points

- **"The reconstruction comparison is meaningless"** (Harsh Critic): Overstated. The comparison is informative even if bitrates differ — DeCodec achieves SDR 7.61 vs EnCodec's 6.86, and the key claim is that decoupling does not catastrophically degrade reconstruction. The bitrate difference is a genuine weakness but does not render the comparison "meaningless."
- **"Claim of 'first' explicit decoupling is overstated"** (Harsh Critic): The paper qualifies this carefully: "first time" in the context of a *universal codec* achieving explicit speech-BGS decoupling. Prior work on speaker-conditioned codecs and joint source separation/coding exists but does not achieve what this paper does — the novelty claim is legitimate.
- **"Strength: Theoretical justification for the RST procedure"** (Strength Finder): This conflicts with the verified weakness that the proof is non-rigorous. Removed.
- **"Reproducibility concern about undisclosed hyperparameters/implementation details"**: The paper provides sufficient architectural and training details for a conference submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run a controlled bitrate comparison.** Reduce DeCodec's SRVQ+BRVQ levels to achieve a total bitrate of ~4.5–6 kbps and compare to DAC, EnCodec, and SpeechTokenizer at those bitrates. This would cleanly separate the effect of decoupling from the effect of higher bitrate.

2. **Retract or reframe the theoretical proof.** Replace Section 3.6's formal proof with a clear intuitive motivation for why swap training encourages disentanglement, and present the empirical ablation as the primary evidence. The current "proof" is mathematically unsound and invites criticism without providing real benefit.

3. **Run SE baselines under the same evaluation pipeline.** Re-run Inter-SubNet, StoRM, and SELM on the exact same test set using the same DNSMOS version to eliminate cross-paper variability concerns.

4. **Include a source separation baseline.** Compare DeCodec's decoupling against a simple separation model (e.g., ConvTasNet) on the same data using SI-SNRi to quantify decoupling quality directly.

5. **Add a failure analysis for one-shot VC.** Since 50% WER limits practical applicability, analyze specifically which types of source–reference pairs succeed and which fail (e.g., gender mismatch, voicing mismatch, pitch range), and discuss the scope of use cases where this is acceptable.

## Score and Decision

**Calibration anchors** (all from the deepreview_13k_calibration set):
- **DM-Codec (UFwefiypla.md)** — avg 3.00: Had a fundamental technical flaw (text/audio length mismatch in training). The current paper is stronger — no equivalent fatal flaw.
- **Universal Semantic Disentangled (Id2JMVSQHZ.md)** — avg 4.80: Similar topic (codec disentanglement), missing baselines, unclear advantage over prior work. Comparable evaluation quality but our paper has a novel architecture not present there.
- **Codec-LM Co-design (KCVv3tICvp.md)** — avg 5.00: Limited novelty (engineering tricks) but clean evaluation. Our paper has stronger technical novelty but weaker evaluation rigor.
- **Vevo (anQDiQZhDP.md)** — avg 5.50: Self-supervised disentanglement for voice imitation, accepted. Strong results but some concerns. Our paper has a comparable contribution level.
- **FlowDec (uxDFlPGRLX.md)** — avg 7.00: Clean evaluation, competitive results, accepted at a strong venue. Our paper is significantly weaker on evaluation rigor.

The paper presents a genuinely novel architecture for codec-based speech-BGS disentanglement with promising empirical results across multiple tasks. However, the reconstruction comparison is weakened by unmatched bitrates, the theoretical proof is non-rigorous, and the SE evaluation relies on cross-paper baseline scores. The core contribution — decoupled representations via SOP+RST — is empirically supported, but the scientific rigor of the evaluation needs improvement. The paper is at the borderline: the idea is strong enough to warrant attention, but the current presentation has issues that prevent a clear accept.

**Score: 5.0**

**Decision: Reject** — The paper has novel ideas and promising results, but the evaluation has significant rigor issues (unmatched bitrate comparison, non-rigorous proof, cross-paper SE baselines) that prevent acceptance in current form. The core idea merits resubmission after addressing these concerns.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>