Now I have the full paper. Let me synthesize the meta-review based on direct verification against the paper text.

---

## Summary

DeCodec reframes neural audio codecs as universal disentangled representation learners. The core technical contributions are (1) a Subspace Orthogonal Projection (SOP) module that factorizes encoder embeddings into orthogonal speech and background-sound subspaces, and (2) a Representation Swap Training (RST) procedure that forces each subspace to correspond to its designated signal component. A semantic guidance (SG) layer additionally decomposes the speech RVQ into semantic and residual paralinguistic codes. The single codec then serves as a zero-configuration front-end for speech enhancement (by replacing the background-sound token stream with a silence token stream), one-shot voice conversion on noisy speech, ASR feature extraction, and TTS.

---

## Strengths

- **SOP+RST ablation provides direct causal evidence for disentanglement** (Table 4, Ablation-1/2/3): SOP alone yields SDR-B = –13.15 dB and SDR-S = –1.91 dB; RST alone yields SDR-B = –10.67 dB and SDR-S = 3.03 dB; their combination achieves SDR-B = 0.49 dB and SDR-S = 7.90 dB. This is a clear and clean result demonstrating necessity of both components for meaningful disentanglement.

- **SE via representation substitution achieves state-of-the-art DNSMOS across both non-causal and causal settings** (Table 2): DeCodec attains OVL 3.39 / BAK 4.13 (without-reverb) and OVL 3.13 / BAK 3.99 (real recordings), outperforming discriminative (Inter-SubNet), diffusion (StoRM), and transformer-based (SELM) SE models. Notably, causal DeCodec-c (OVL 3.31, BAK 4.09) surpasses non-causal SELM (OVL 3.26, BAK 4.10) on the without-reverb set, a meaningful result for latency-sensitive applications.

- **Semantic guidance further decomposes speech into semantic and paralinguistic codes in a noise-robust way** (Table 4): Adding SG to SOP+RST reduces downstream ASR WER* from 41.9 (Ablation-3 causal) to 25.8 (DeCodec-c) and 23.6 (DeCodec non-causal), confirming hierarchical structure within the speech subspace.

- **Both causal and non-causal variants are provided and evaluated**, which broadens applicability to real-time and offline settings alike. Causal DeCodec still achieves SDR 6.79 dB on clean speech (Table 1), close to non-causal EnCodec at 6.86 dB.

---

## Weaknesses

### Fatal
None.

### Major

- **The reconstruction comparison in Table 1 is not controlled for bitrate.** DeCodec operates at 4.0+4.0 = 8.0 kbps (parallel SRVQ + NRVQ), while EnCodec is 6.0 kbps, DAC is 4.5 kbps, HiFi-Codec is 2.0 kbps, and SpeechTokenizer is 4.0 kbps. The abstract's claim that DeCodec "maintains advanced signal reconstruction while enabling new capabilities" and the Section 4.2.1 statement that it "achieves the highest SDR for speech reconstruction" are presented without acknowledging the 33–100% bitrate advantage. Furthermore, on Mel Distance—a metric where lower is better—DAC outperforms DeCodec on both clean (0.65 vs 0.89) and noisy (0.69 vs 0.81) speech despite running at 4.5 kbps. DeCodec's SDR lead at double the bitrate is not evidence of architectural superiority; it is evidence of having more capacity. The paper should either (a) include a bitrate-matched comparison or (b) explicitly reframe the extra bitrate cost as a deliberate design trade-off for disentanglement. As written, the reconstruction headline overstates the comparison.

- **The theoretical argument in Section 3.6 has a logical gap.** The key step asserts (line 154): "The left side depends on Zs1 through ξ, while the right side is independent of Zs1. Therefore, for consistency ∀n1, n2, Zs1 must be independent of n1." However, ξ is a point on the line segment between Zn1 and Zn2 (by the MVT), not a function of Zs1. The Jacobian ∂Dec/∂Zn evaluated at ξ does not obviously depend on Zs1 unless there is an additional argument about how the decoder couples Zs and Zn. The conclusion that "Zs1 must be independent of n1" does not logically follow from the presented derivation. The intuitive argument — that the decoder must be treating Zs and Zn as independently controlling different signal components — is correct in spirit but is effectively restating the training objective. Since Table 4 provides robust empirical validation of the mechanism, the paper would be strengthened by either (a) replacing this section with an honest empirical argument or (b) making the proof rigorous.

### Minor

- **The semantic guidance loss (Equation 7) uses HuBERT features of the clean speech s, not the noisy mixture y.** This is stated in Section 3.5: "H denote...Hubert-L9 representation of the **corresponding clean speech s**." This implicitly requires paired clean/noisy training data. The paper's training setup generates synthetic mixtures from clean speech (Section 4.1: "700h of speech data...mixed with...background sound"), so clean references are available by construction. However, this training condition is not explicitly discussed as a design constraint, and it is not acknowledged in the experimental comparison for SE. Papers that discuss generalization to in-the-wild (non-simulated) noisy training data would face this constraint — worth an explicit statement.

- **SE evaluation uses only DNSMOS, a non-intrusive perceptual quality metric, with no signal-level metrics (PESQ, STOI).** Section 4.2.2 acknowledges "slightly inferior speech signal reconstruction" due to the quantization bottleneck, yet no metric captures this quantization artifact quantitatively. Intrinsic metrics would directly reveal whether the codec bottleneck degrades intelligibility, which DNSMOS cannot distinguish from perceptual quality.

- **The SOP derivation in Section 3.4 has a load-bearing conditional.** The derivation from Equation (6) to the conclusion P_S P_N^T = 0 requires that "YY^T satisfies the angular matrix, indicating that the encoder extracts sufficiently diverse embeddings with different feature channels being mutually independent." This is stated as a condition, not derived, and is not empirically validated. If the encoder's covariance structure deviates from this, the orthogonality conclusion breaks down. An empirical check (e.g., showing the distribution of off-diagonal terms of the covariance matrix in practice) would strengthen this section.

### Trivial

- The WER of 50.46% for one-shot VC (Table 3) is briefly attributed to "different speech segment voicing times" — a plausible explanation that deserves one more sentence of analysis or illustration to be convincing rather than dismissive.

---

## Nice-to-Haves

- A bitrate–quality trade-off curve (or table) showing how reconstruction metrics change as additional RVQ layers are added would reframe the 8.0 kbps design as a principled choice and directly answer whether the bitrate premium fully accounts for DeCodec's SDR gain.
- A cross-reconstruction test (substitute Zn2 from a held-out acoustic environment and measure how well the output matches s1+n2 with a known reference) would provide the cleanest possible demonstration that the RST mechanism generalizes beyond training conditions.
- Reporting PESQ/STOI alongside DNSMOS for SE experiments would complete the evaluation picture and address the quantization artifact concern directly.
- Comparing VC against a clean-speech VC baseline (even using denoised input) would better contextualize the WER 50.46% result.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic – "practical interface for VC/SE not reproducible"**: The paper does describe the SE and VC operations precisely enough (SE: replace NRVQ tokens with those from blank audio; VC: swap SRVQ-2:8 of source with those of reference), and the procedures follow directly from the codec formulation. The concern about reproducibility is too speculative to retain.

- **Harsh Critic – "bitrate unfair in the direction favoring the baseline"**: Actually this favors the *author*, so it is a valid criticism and is retained above. Reviewing the rule: "REMOVE if asymmetry favors the baseline" — this asymmetry favors DeCodec, so it stays in. (No removal here; kept in Major.)

- **Harsh Critic – training details should be in main paper not appendix**: Appendix sections are stripped from the parsed version; we cannot verify this. Per the rules, we do not criticize missing appendix content.

- **Strength Finder – "Theoretical argument backed by MVT is a strength"**: Disputed by the harsh critic (and verified as having a logical gap). Removed from strengths.

- **Strength Finder – "Disentanglement does not degrade reconstruction fidelity" (SDR lead)**: Undermined by the bitrate discrepancy. DeCodec does not clearly demonstrate architecture-superior reconstruction; the SDR lead coincides with a bitrate advantage. Removed as standalone strength; the ablation-based reconstruction evidence is kept.

---

## Novel Insights

The most genuinely novel observation synthesized across the reviews is the following: the paper's strongest argument for disentanglement is not the theoretical proof (which is incomplete) and not the reconstruction comparison (which is confounded by bitrate), but the *functional completeness demonstrated by representation substitution*: the fact that zeroing the NRVQ stream produces SE-quality output, and swapping SRVQ-2:8 tokens produces a voice-transferred output, constitutes a behavioral test that the subspaces actually carry orthogonal and semantically meaningful information. This kind of "intervention as proof" is more rigorous than the MVT argument and should be the rhetorical center of the paper. The ablation study (Table 4) is the next-strongest evidence. Future work building on this paper should investigate whether the disentanglement quality (measured by cross-reconstruction) scales with the bitrate allocated to each parallel RVQ stream, which would clarify whether the 4+4 kbps split is optimal or excessive for the SE/VC use cases.

---

## Suggestions

1. **Correct the reconstruction comparison framing**: Either run DAC/EnCodec/SpeechTokenizer at 8 kbps (by adding extra RVQ layers to their off-the-shelf checkpoints) or explicitly reframe the SDR result as "at 8 kbps, DeCodec achieves X SDR versus Y SDR for the 8 kbps variant of EnCodec." Failing that, at minimum add a sentence in Section 4.2.1 acknowledging that the comparison is not bitrate-controlled and that the extra capacity is the cost of disentanglement.

2. **Replace or qualify Section 3.6**: Rewrite the theoretical section as an "informal argument" or "motivating analysis," rather than a proof. The empirical ablation (Table 4) is far more persuasive and should be cited as the primary evidence.

3. **Add one sentence in Section 3.5 or 4.1** explicitly noting that SG requires access to the clean speech reference during training, and that this is achievable in the simulated training setup used here. Briefly note what happens if SG is provided on noisy speech (or not provided) — this is relevant for deployment on real noisy data.

4. **Supplement Table 2 with at least one intrinsic SE metric** (PESQ or STOI on the simulated test set) to quantify whether the quantization bottleneck causes intelligibility loss that DNSMOS misses.

---

## Evaluation on Key Axes

- **Originality**: High. The idea of using a codec's quantization subspace structure for unified speech/background-sound disentanglement is a genuinely new framing. Existing work on codec disentanglement (SpeechTokenizer, FACodec) is limited to clean speech; DeCodec's coupling of SOP+RST with parallel RVQs for mixed-audio disentanglement is original.

- **Importance of research question**: High. Real-world audio is almost universally mixed; a single codec that enables all of SE, VC, ASR feature extraction, and TTS with disentangled representations would be broadly useful.

- **Claims supported**: Moderate. The SE results (Table 2), VC results (Table 3), and ablation (Table 4) are well-supported. The reconstruction headline (abstract, Section 4.2.1) is overstated due to the bitrate discrepancy. The theoretical claims are insufficiently rigorous.

- **Soundness of experiments**: Moderate. The SE and VC setups are reasonable; the ablation design is good. The reconstruction comparison is structurally unfair without a bitrate-matched baseline.

- **Clarity**: Moderate. The overall paper structure is clear, but Section 3.6 presents an incomplete argument as a proof, and the bitrate issue is never acknowledged in the text.

- **Value to the research community**: High. Releasing a codec that intrinsically enables SE, VC, ASR, and TTS without front-end separation modules would be practically valuable. The ablation design offers a clean template for future disentanglement work.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>