Now let me run calibration searches to bracket the score.Round 1 bracket: **4.5 – 6.5**. Let me narrow with round 2.Now I have sufficient data to write the final review. Let me compile it.

---

## Summary

DeCodec proposes a neural audio codec that simultaneously decouples speech from background sound and decomposes speech into semantic and paralinguistic components. The key technical contributions are a **Subspace Orthogonal Projection (SOP) module** that factorizes the encoder output into orthogonal subspaces, and a **Representation Swap Training (RST) procedure** that forces these subspaces to correspond to speech and background sound respectively. The resulting codec enables downstream tasks — speech enhancement via representation substitution, one-shot voice conversion, and noise-robust ASR/TTS — without a cascaded front-end separation pipeline.

---

## Strengths

- **SOP+RST ablation directly validates the disentanglement mechanism (Table 4):** SOP alone (Ablation-1) yields SDR-B = −13.15 and SDR-S = −1.91; RST alone (Ablation-2) gives SDR-B = −10.67 and SDR-S = 3.03; only the combination (Ablation-3) achieves SDR-B = 0.49 and SDR-S = 7.90. This is the strongest evidence in the paper — both components are necessary and their interaction is non-trivial.

- **State-of-the-art speech enhancement without a dedicated front-end (Table 2):** DeCodec achieves the highest DNSMOS overall quality (OVL 3.39 without reverb, 3.13 real recordings) and background suppression (BAK 4.13 / 3.99) among all compared models including diffusion-based (StoRM) and transformer-based (SELM) systems. This directly validates that representation-domain decoupling can substitute for time-domain separation.

- **Causal variant retains substantial performance:** DeCodec-c (causal) achieves SDR 6.79 dB on clean speech (Table 1) and OVL 2.99 / BAK 3.94 on real recordings (Table 2), outperforming causal Inter-SubNet, demonstrating practical applicability without non-causal look-ahead.

- **Semantic guidance (SG) achieves a hierarchical decomposition on top of BGS decoupling:** Adding SG to Ablation-3 reduces WER* from 41.9 to 25.8 (causal) / 23.6 (non-causal) (Table 4), confirming that within-speech semantic/paralinguistic factorization works synergistically with the speech-BGS split.

---

## Weaknesses

### Fatal
None.

### Major

- **Bitrate comparison in Table 1 is not controlled, yet the abstract states "maintains advanced signal reconstruction."** DeCodec operates at 4.0+4.0 = **8.0 kbps** while EnCodec runs at 6.0 kbps, DAC at 4.5 kbps, and SpeechTokenizer at 4.0 kbps. DeCodec uses 33%–100% more bandwidth than the baselines it surpasses in SDR. The paper correctly shows the kbps column in Table 1, but never discusses this disparity or acknowledges that higher bitrate almost universally yields better SDR. The 8 kbps design is a consequence of needing two parallel RVQ streams for disentanglement — a genuine engineering trade-off that should be framed as such rather than omitted. As written, "achieves the highest SDR" implies architectural superiority when it at least partially reflects bitrate advantage. The claim would be defensible if the paper included either (a) baselines at matched 8 kbps, or (b) an explicit discussion of the rate–quality–disentanglement trade-off.

### Minor

- **The theoretical proof in Section 3.6 does not logically establish what it claims.** The key step (lines 150–154) applies the mean value theorem to obtain Eq. (16), then states: "The left side depends on Zs1 through ξ, while the right side is independent of Zs1. Therefore, for consistency ∀n1, n2, Zs1 must be independent of n1." However, ξ lies on the path between Zn1 and Zn2 — it does not depend on Zs1 in the sense the argument requires, and the Jacobian ∂Dec/∂Zn|ξ depends on shared decoder parameters rather than on Zs1 specifically. The conclusion essentially restates the training objective (the decoder must map Zs+Zn to s+n regardless of which n is used) rather than proving it follows from the loss. The empirical result in Table 4 does support the claim — the argument should be reframed honestly as an intuitive motivation backed by empirical evidence rather than a formal proof.

- **The semantic guidance loss (Eq. 7) requires paired clean/noisy training data, an undisclosed constraint.** The loss aligns the first-layer SRVQ output with "HuBERT-L9 representation of the **corresponding clean speech s**." This means training requires ground-truth clean speech for every sample. The training setup (Section 4.1) accomplishes this by synthetically mixing clean speech with noise — which is reasonable — but the paper never explicitly states that this paired-data requirement is a necessary training condition, nor discusses what happens when clean references are unavailable (e.g., purely in-the-wild data). This should be stated as a scope limitation.

- **SE evaluation relies exclusively on DNSMOS, concealing quantization-induced intelligibility loss.** Table 2 reports only p.835 DNSMOS (OVL, SIG, BAK), which is a non-intrusive perceptual quality estimator. The paper itself acknowledges (Section 4.2.2): "includes discretization quantizers, resulting in slightly inferior speech signal reconstruction." Intrinsic metrics (PESQ, STOI) would reveal whether the quantization bottleneck creates intelligibility degradation not captured by DNSMOS.

- **The angular-matrix assumption in Section 3.4 is load-bearing but untested.** The derivation that P_S P_N^T = 0 (which the paper calls demonstrating that the projectors are "indeed orthogonal") depends on the assumption that "YY^T satisfies the angular matrix, indicating that the encoder extracts sufficiently diverse embeddings with different feature channels being mutually independent" (line 106). This is stated as a conditional premise, not verified empirically or theoretically. If the encoder embeddings are correlated, the derivation collapses. At minimum, this assumption should be clearly flagged as unverified.

### Trivial

- The WER of 50.46% for the VC+SE output is very high; the paper attributes it to voicing-time mismatch and this explanation is plausible, but a brief quantitative analysis (e.g., how much WER improves on paired-duration segments) would strengthen the interpretation.

---

## Nice-to-Haves

- An explicit bitrate–disentanglement trade-off analysis (how many RVQ layers does disentanglement consume over reconstruction-only capacity?) would reframe the 8 kbps design as principled rather than appearing advantageous by accident.
- A cross-reconstruction experiment (substitute N from a completely different acoustic environment, compare decoded output to the known s1+n2 target) would directly validate the RST mechanism beyond the SDR-B/SDR-S proxy in Table 4.
- Intrinsic SE metrics (PESQ, STOI) alongside DNSMOS to honestly characterize the quantization-intelligibility trade-off.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Harsh critic: VC baseline set is "thin" and only 2 WER points better than StoRM-SpeechTokenizer.** → Partially valid observation but framed as a weakness of the core claim. The paper never claims VC is its headline contribution; it is demonstrating disentanglement functionality. The narrow margin is noted in the Minor tier implicitly. Removed as a standalone weakness because the comparison set (SpeechTokenizer + its cascade variant) is appropriate given the paper's framing.

- **Harsh critic: Section 3.2 inference interface for SE/VC is "not specified precisely enough to be reproducible."** → This is a reproducibility concern about appendix-level implementation details. Per hard rules, removed.

- **Strength finder: "The representation swap training procedure is backed by a clear theoretical argument."** → This directly conflicts with the verified Minor weakness about the logical gap in Section 3.6. Removed per filtering rule (weakness wins).

- **Strength finder: "Disentanglement does not degrade reconstruction fidelity."** → This is a generic claim that conflicts with the Major bitrate-comparison weakness. The SDR superiority is at least partly attributable to the bitrate advantage, not solely to the disentanglement architecture. Removed; the nuanced version is retained in the bitrate weakness discussion.

---

## Novel Insights

The paper's core conceptual move — treating orthogonal subspace decomposition as the representation-level analog of cortical speech/BGS regional processing, and using cross-sample reconstruction loss to anchor subspaces to semantic categories — is genuinely novel within the codec literature. The crucial finding from the ablation (Table 4) is that neither SOP nor RST alone is sufficient: SOP without RST produces excellent overall reconstruction (SDR-O = 8.93) but near-zero decoupling (SDR-B = −13.15, SDR-S = −1.91), while RST without SOP shows partial improvement (SDR-S = 3.03) but still fails at BGS isolation (SDR-B = −10.67). Only their combination produces genuine decoupling. This suggests that the orthogonal projection must be in place before the swap loss can "assign" signal types to subspaces — a structural insight about how geometric and supervisory inductive biases interact in multi-stream VQ systems.

---

## Suggestions

1. Add a reconstruction comparison at matched or normalized bitrate (e.g., run baselines at 8 kbps or discuss how DeCodec performs at 4 kbps single-stream) and explicitly frame the dual-stream design as a rate cost of disentanglement.
2. Replace the Section 3.6 "proof" framing with an honest statement: "We provide an intuitive argument that the RST loss encourages speech/BGS independence; Table 4 provides empirical validation." Correct or remove the logical claim about ξ depending on Zs1.
3. In Section 4.1 and/or limitations (Appendix H), explicitly state that training requires paired clean/noisy data and discuss sensitivity to this constraint.
4. Add PESQ and STOI to Table 2 (even in an appendix) to characterize the quantization-intelligibility trade-off that DNSMOS alone cannot reveal.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| UFwefiypla.md (DM-Codec) | 3.00 | R1 low | Much narrower scope, weaker evaluation |
| mlPTNEIsgb.md (Blind forward/inverse audio) | 3.25 | R1 low | Different topic, less relevant |
| Id2JMVSQHZ.md (USC privacy-preserving codec) | 4.80 | R1 mid / R2 | Similar disentangled-codec framing; DeCodec is more comprehensive and better ablated |
| LfDUzzQa3g.md (RepCodec) | 5.50 | R1 mid / R2 | Simpler single-task codec contribution; DeCodec has broader scope but similar quality concerns |
| KCVv3tICvp.md (Codec-LM co-design) | 5.00 | R1 mid / R2 | Adjacent topic, narrower scope than DeCodec |
| C53xlgEqVh.md (Vec-Tok Speech) | 5.20 | R2 | Similar multi-task speech codec; comparable quality |
| 1p6xFLBU4J.md (GenSE) | 6.00 | R1 mid | Accepted; comprehensive SE framework with complete evaluation; DeCodec is comparably ambitious but has the unaddressed bitrate issue |
| qqExiDNsa7.md (pre-trained models for speech sep.) | 5.00 | R2 | Less relevant |

**Round-1 bracket:** 4.5 – 6.5

**Round-2 narrowing:** The most comparable anchors in the bracket are USC (4.80), RepCodec (5.50), Vec-Tok (5.20), and GenSE (6.00). DeCodec is clearly more ambitious and better empirically supported than USC (which lacked ablation, ignored key related work, and had narrower scope). It is comparably scoped to RepCodec but more novel — SOP+RST for BGS-speech decoupling is a genuine new mechanism absent from RepCodec. However, GenSE (6.00, accepted) has a cleaner, more complete evaluation without the bitrate comparison ambiguity. DeCodec's Major weakness (the unacknowledged bitrate advantage in the headline reconstruction claim) is analogous to USC's overclaiming and prevents reaching GenSE's level. Final position: **between RepCodec (5.50) and GenSE (6.00), closer to 5.5** given the bitrate framing issue remains unresolved and the theoretical proof is non-rigorous.

**Originality:** High — SOP+RST combination for codec-level BGS-speech decoupling is novel.  
**Research question importance:** High — enabling downstream tasks without cascaded pipelines is practically impactful.  
**Claim support:** Moderate — core disentanglement claim is well-supported by ablation; reconstruction claim is overstated due to bitrate disparity.  
**Experimental soundness:** Moderate — SE evaluation metric choice (DNSMOS only) is limiting; VC evaluation is thin.  
**Writing clarity:** Good overall, with the theoretical proof section being the main problematic area.  
**Value to community:** Good — the multiple downstream task demonstrations and the ablation analysis provide useful insights for the codec research community.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>