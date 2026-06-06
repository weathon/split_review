## Summary

DeCodec proposes a neural audio codec that decouples speech from background sound and decomposes speech into semantic and paralinguistic components. The technical core is a **Subspace Orthogonal Projection (SOP) module** that factorizes encoder outputs into orthogonal subspaces, combined with a **Representation Swap Training (RST) procedure** that anchors these subspaces to speech/BGS respectively. The codec enables speech enhancement, one-shot voice conversion, and noise-robust ASR/TTS without a cascaded front-end separation pipeline.

---

## Rebuttal Assessment

### Weakness 1: Bitrate comparison uncontrolled (Major)
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author makes three legitimate arguments, all verified against the paper: (1) The kbps column in Table 1 is explicitly shown; (2) DeCodec does *not* universally win across all reconstruction metrics — DAC achieves the best Mel Distance on clean speech (0.65 vs. 0.89) and SpeechTokenizer the best WER (1.82 vs. 1.92), confirmed in Table 1; (3) Section 4.2.1 line 202 *does* use conservative language: "performs comparably to existing codec models in reconstruction while possessing its own distinctive advantages." However, the in-text claim on line 188 ("achieves the highest SDR for speech reconstruction") remains unqualified, and no matched-bitrate baselines or explicit rate–quality–disentanglement trade-off discussion appears in the paper — the promised revision addition does not count.
- **Score impact:** Weakness downgraded (Major → Minor) — the multi-metric evidence and conservative in-text framing credibly reduce, but do not eliminate, the concern.

### Weakness 2: Theoretical proof in Section 3.6 has logical gap (Minor)
- **Author's response:** Acknowledge
- **Assessment:** Honest but unconvincing as a rebuttal — The authors fully concede the logical gap: "ξ is defined by the MVT solely with respect to the path between Zn₁ and Zn₂ and does not intrinsically depend on Zs₁." The empirical Table 4 evidence is cited as substantiation, which the original review already credited. No fix is present in the paper.
- **Score impact:** Weakness unchanged

### Weakness 3: Semantic guidance requires paired clean/noisy data — undisclosed (Minor)
- **Author's response:** Partially address
- **Assessment:** Partially convincing — Section 4.1 (line 164) confirms: "Around 700h of speech data were randomly selected and **mixed** with randomly selected background sound...to form the training set." The paired data is inherently available through synthetic mixing, meaning the constraint is satisfied without extra effort *in the described setup*. However, the paper still never explicitly frames this as a scope limitation. The author's acknowledgment is honest, and the actual impact is mitigated by the synthetic mixing approach.
- **Score impact:** Weakness downgraded (Minor → Trivial)

### Weakness 4: SE evaluation relies solely on DNSMOS (Minor)
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The justification (Section 4.1 line 168: "The results of these models on the DNS Challenge testset are taken from the paper (Wang et al., 2024)") is verified and reasonable. Adding PESQ/STOI for DeCodec alone without comparable baseline figures would create an asymmetric evaluation. The WER values in Table 1 serve as a partial intelligibility proxy. That said, the quantization-intelligibility trade-off the original reviewer identified is real and acknowledged by the authors themselves ("slightly inferior speech signal reconstruction," line 206). The revision promise does not fix the issue.
- **Score impact:** Weakness downgraded (Minor → Trivial) — the methodological justification is legitimate

### Weakness 5: Angular-matrix assumption load-bearing but untested (Minor)
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly notes the "when" qualifier in Section 3.4 (line 106: "When the covariance matrix YYᵀ satisfies the angular matrix..."), verified in the paper. More importantly, Eq. 5 (L_⊥) directly minimizes ⟨S, N⟩ regardless of whether YYᵀ is angular, so the practical orthogonality enforcement does not strictly depend on the angular assumption. The assumption is a theoretical simplification for the derivation, not a prerequisite for the mechanism to work.
- **Score impact:** Weakness downgraded (Minor → Trivial)

### Weakness 6: High WER (50.46%) for VC+SE with only qualitative explanation (Trivial)
- **Author's response:** Partially address
- **Assessment:** Partially convincing — Author correctly notes WER 50.46 vs. StoRM-SpeechTokenizer's 52.73, and correctly frames this as a competitive advantage over the cascade. No quantitative stratification by voiced-frame overlap is added to the paper. Weakness unchanged in scope.
- **Score impact:** Weakness unchanged

---

## Strengths

- **SOP+RST ablation directly validates the disentanglement mechanism (Table 4, lines 246–250):** SOP alone yields SDR-B = −13.15, SDR-S = −1.91; RST alone yields SDR-B = −10.67, SDR-S = 3.03; only the combination achieves SDR-B = 0.49, SDR-S = 7.90. Both components are necessary and their interaction is non-trivial.
- **State-of-the-art SE without a dedicated front-end (Table 2):** DeCodec achieves highest DNSMOS OVL (3.39/3.13), SIG (3.64/3.45), and BAK (4.13/3.99) among all compared models, including diffusion-based and transformer-based systems.
- **Multi-metric reconstruction picture is nuanced, not purely bitrate-driven:** DAC best Mel Distance (0.65 vs. 0.89 clean), SpeechTokenizer best WER (1.82 vs. 1.92), supporting the paper's conservative claim that DeCodec is competitive rather than universally superior.
- **Causal variant retains substantial performance:** DeCodec-c outperforms causal Inter-SubNet on all DNSMOS scores (Table 2), confirming practical deployment viability.
- **Semantic guidance synergy (Table 4):** SG addition reduces WER* from 41.9 to 25.8 (causal) / 23.6 (non-causal), confirming hierarchical semantic/paralinguistic factorization within the speech subspace.

---

## Weaknesses

### Fatal
None.

### Major
None (downgraded from original).

### Minor
- **Bitrate disparity still unacknowledged in the abstract and unqualified in SDR discussion (line 188):** The abstract's "maintains advanced signal reconstruction" and the in-text claim "achieves the highest SDR" remain unqualified despite the 33%–100% bitrate premium over baselines. The kbps transparency and multi-metric picture partially mitigate this, but an explicit rate–quality–disentanglement trade-off section is missing from the paper.
- **Logical gap in Section 3.6 theoretical proof (lines 150–154):** Acknowledged by the authors. The mean value theorem argument does not formally establish that Zs is independent of n; ξ depends only on the path between Zn₁ and Zn₂, not on Zs₁. Table 4 provides empirical support, but the theoretical framing remains misleadingly labeled as a "proof."

### Trivial
- **Angular-matrix assumption unverified:** The conditional framing ("when") and the empirical L_⊥ enforcement reduce the severity; flagging this assumption explicitly in the text would improve rigor.
- **Semantic guidance paired-data scope not explicitly stated as limitation:** Implicit in the synthetic mixing training setup but should be stated.
- **DNSMOS-only SE evaluation:** Methodologically justified given baseline result provenance, but PESQ/STOI appendix addition would fully address the intelligibility question.
- **High VC+SE WER with only qualitative explanation:** Competitive margin over StoRM-SpeechTokenizer is established; quantitative voicing-time analysis absent.

---

## Nice-to-Haves

- An explicit discussion of the rate–quality–disentanglement trade-off (e.g., comparison of reconstruction performance at normalized bitrate, or analysis of how many RVQ layers are consumed by disentanglement vs. pure reconstruction capacity) would turn the 8.0 kbps design from a perceived advantage into a clearly framed engineering necessity.
- PESQ/STOI supplementary evaluation to directly characterize quantization-induced intelligibility effects that DNSMOS cannot capture.
- Reframing Section 3.6 as "intuitive motivation backed by empirical evidence" rather than a formal proof.

---

## Novel Insights

The paper's conceptual novelty — treating orthogonal subspace decomposition as the representation-level analog of cortical speech/BGS regional processing, and using cross-sample reconstruction loss to anchor subspaces to signal categories — remains genuinely new within the codec literature. The rebuttal adds a useful clarification that the multi-metric reconstruction picture is more nuanced than the original review characterized: DeCodec's SDR superiority is real but co-exists with losses on Mel Distance (vs. DAC) and WER (vs. SpeechTokenizer), which shows the dual-stream design imposes a *selective* rather than universal reconstruction cost. The ablation finding that neither SOP nor RST alone is sufficient — verified from Table 4 — is the paper's most structurally important insight: geometric inductive bias (SOP via L_⊥) must be in place before the supervisory swap loss (RST) can assign signal types to subspaces.

---

## Suggestions

1. Add a sentence in the abstract and Section 4.2.1 explicitly framing the 8.0 kbps dual-stream design as the rate cost of disentanglement, pointing readers to the transparent kbps column in Table 1.
2. Replace the Section 3.6 proof framing with: "We provide an intuitive argument that the RST loss encourages speech/BGS independence; Table 4 provides empirical validation." Correct or remove the claim about ξ depending on Zs₁.
3. Add a scope limitation to Section 4.1 or Appendix H explicitly stating that the semantic guidance training requires paired clean/noisy data (satisfied here via synthetic mixing) and discussing what would be needed for purely in-the-wild training data.
4. Add PESQ/STOI for DeCodec in an appendix alongside the explanation of why DNSMOS was used as the primary comparison metric.

---

## Score and Decision

**Updated calibration:**

The rebuttal successfully reduces the major bitrate weakness by pointing to verifiable evidence already in the paper: (a) the kbps column is transparent, (b) DeCodec does not universally dominate all reconstruction metrics (DAC best Mel Distance, SpeechTokenizer best WER), and (c) Section 4.2.1 uses conservative summary language. These are not promises — they are facts verifiable in the paper that the original review underweighted. The remaining issues (unqualified "highest SDR" on line 188, absent rate-quality discussion, proof gap) are real but narrower than originally framed.

The rebuttal's honest acknowledgment of the theoretical proof gap and paired-data constraint, combined with reasonable justification for the DNSMOS-only SE evaluation (baselines taken from prior publication), suggests the paper's core claims are more robustly grounded than a score of 5.5 reflected.

**Original score:** 5.5 (Reject)  
**Score change:** +0.5 — the major weakness is legitimately downgraded by verifiable paper evidence; the remaining issues are Minor/Trivial.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>