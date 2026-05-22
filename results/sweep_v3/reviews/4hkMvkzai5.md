Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

DeCodec proposes a neural audio codec that, for the first time, explicitly disentangles speech from background sound in the representation domain, while also decomposing speech into semantic and paralinguistic components. The core technical innovations are a Subspace Orthogonal Projection (SOP) module that factorizes embeddings into orthogonal subspaces, a Representation Swap Training (RST) procedure that forces each subspace to encode only its designated source, and semantic guidance (SG) via HuBERT distillation on the first RVQ layer. The results show that DeCodec achieves competitive reconstruction, surpasses dedicated speech enhancement models on DNSMOS, and enables one-shot voice conversion and downstream ASR/TTS feature extraction — all within a single codec.

## Strengths

1. **Explicit speech–background decoupling verified through strong ablations.** The ablation study (Table 4) cleanly demonstrates that neither SOP alone (SDR-B = −13.15) nor RST alone (SDR-B = −10.67) achieves decoupling, but their combination yields positive SDR for both background (0.49) and speech (7.90). This is the paper's strongest empirical contribution and is directly tied to specific architecture choices.

2. **Speech enhancement performance surpassing dedicated SE models.** DeCodec achieves the highest DNSMOS scores across all three dimensions (OVL = 3.39, SIG = 3.64, BAK = 4.13) on the without-reverb DNS test set, outperforming dedicated SE models like SELM (3.26, 3.51, 4.10) and StoRM (3.21, 3.51, 3.94). The causal variant also exceeds the causal Inter-SubNet, demonstrating practical viability.

3. **Unified codec enabling reconstruction, SE, VC, ASR, and TTS from a single model.** Unlike prior codecs that are limited to reconstruction or require cascaded separation, DeCodec performs all these tasks via representation recombination. This architectural unification is a genuine contribution — it avoids error propagation from a separate separation front-end and enables feature-level control across tasks.

4. **Hierarchical semantic–paralinguistic disentanglement within speech.** The SG module, guided by HuBERT on SRVQ-1, demonstrably improves downstream WER* from 41.9 to 25.8 (Table 4) and enables one-shot VC (WER = 50.46 vs. SpeechTokenizer's 74.18 on noisy speech) by allowing selective replacement of SRVQ layers. This shows the semantic representation is robust to background sound interference.

5. **Systematic ablation isolating each component.** Table 4 separately tracks overall SDR, decoupling SDR for background and speech, and downstream WER* across six configurations, providing direct evidence for the necessity of each proposed module.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical proof in Section 3.6 (RST loss forcing independence) is not rigorous and should not be presented as a guarantee.** The mean value theorem for vector functions states that there exists ξ on the line segment between **Z**n₁ and **Z**n₂ such that Dec(**Z**s₁ + **Z**n₂) − Dec(**Z**s₁ + **Z**n₁) = ∂Dec/∂**Z**n|_ξ (**Z**n₂ − **Z**n₁). Critically, ξ **does** depend on **Z**s₁ because the decoder's argument is **Z**s₁ + **Z**n. The paper's leap from "the left side depends on **Z**s₁ through ξ" to "**Z**s₁ must be independent of **n**₁" is a non sequitur in the formal sense. Fortunately, the ablation study provides convincing empirical evidence for decoupling, so the paper does not *rely* on this proof. The authors should either correct the reasoning or remove it and rely on the empirical validation.

2. **Reconstruction comparison has uncontrolled confounds.** Table 1 compares DeCodec against baselines run from official checkpoints. The baselines were trained on different data distributions (mostly clean/generic audio at varying sample rates), while DeCodec is trained on a 700-hour curated noisy-speech dataset. DAC (reported at 0.60 dB SDR on clean speech) was designed for 44.1 kHz audio, while DeCodec operates at 16 kHz — a sampling-rate mismatch that likely penalizes DAC. While DeCodec's clean-speech SDR advantage (7.61 vs. EnCodec 6.86) suggests the results are not purely a data-mismatch artifact, the absence of a controlled baseline (e.g., DAC retrained on the same data) makes it difficult to attribute the reconstruction gains to the disentanglement architecture rather than to training data, bitrate differences (8 kbps vs. 4.5–6 kbps), or sampling rate. The paper should explicitly acknowledge these confounds or provide a controlled baseline.

### Minor

1. **The orthogonality derivation in Section 3.4 assumes** **Y****Y**^T **is an "angular matrix" without justification.** The paper claims that when the covariance matrix satisfies this property, **P**_S**P**_N^T = **0** follows. This assumption (that feature channels of the encoder output are mutually independent) is strong and unverified. The method works empirically, but the theoretical framing is loose.

2. **"Universal" overstates demonstrated scope.** The method is designed and evaluated on speech + background-sound mixtures. It is not demonstrated on music+speech, multi-source overlapping audio, or general audio with more than two sources. The title's "Universal Disentangled Representation Learners" and several claims of universality should be narrowed.

3. **One-shot VC WER of 50.46% is high; calling it "effective" needs qualification.** While the WER is better than baselines (SpeechTokenizer 74.18%, StoRM-SpeechTokenizer 52.73%), 50.46% means roughly half the words are incorrect. The paper acknowledges voicing-mismatch issues but should more clearly caveat that the VC capability works best when source and reference have similar prosodic characteristics.

4. **Background extraction quality is modest for the causal variant.** DeCodec-c has SDR-B = −1.11 (Table 4), meaning the extracted background sound is not well-separated. The paper achieves strong SE (suppression) via blank-audio substitution, but direct background extraction remains weak for causal settings. This asymmetry deserves explicit discussion.

5. **SOP constraint formulation (Eq. 5) using ⟨**S**, **N**⟩ is underspecified.** It is unclear whether this is the inner product summed over all dimensions (batch, time, channel) or per-frame. The distinction matters for whether the constraint enforces global or local orthogonality.

6. **Missing model size and efficiency comparison.** For a codec — where efficiency is a primary concern — the paper does not report model parameters, FLOPs, or inference throughput relative to baselines.

### Trivial
None.

## Nice-to-Haves
- Include PESQ/STOI metrics for speech reconstruction quality in addition to Mel distance.
- Clarify how the "blank audio" background representation is obtained for SE (processed through encoder? what are its characteristics?).
- Provide a failure-case analysis for VC beyond the voicing-mismatch mention.

## Removed Points
- **"Downstream ASR/TTS results absent from main text."** The paper explicitly states these are in Appendix F and G. The appendix was stripped by the PDF parser; it exists in the original submission. Per protocol, parser-stripped content is not a valid weakness.
- **"Missing baselines for reconstruction (data mismatch is fatal)."** DeCodec also achieves higher SDR than baselines on *clean* speech (7.61 vs. 6.86 for EnCodec), where data mismatch is far less relevant. This was downgraded from a critical issue to a major weakness (confound acknowledged but not fatal).
- **"Style/formatting nitpicks"** and **"Missing related works."** Removed per filtering rules.
- **Strength about "theoretical justification for representation independence."** The proof is actually flawed (see Weakness #1), so this claimed strength conflicts with a verified weakness and is dropped.

## Novel Insights

The connection between the two reviewers' comments reveals something the paper itself does not fully articulate: the combination of SOP (orthogonal projection) and RST (swap training) mirrors a form of **contrastive learning in representation space**. The RST loss essentially tells the decoder "reconstruct s₁+n₂ from Zs₁+Zn₂," which forces the speech path to be invariant to which background vector is supplied. This is functionally similar to an independence maximization objective, and the paper's empirical evidence (SOP alone fails, RST alone fails, together they work) strongly suggests the two components play complementary roles: SOP provides the *capacity* for orthogonal subspaces, while RST provides the *supervisory signal* assigning which subspace corresponds to which source. Recognizing this as an instance of (weak) independence enforcement through data augmentation could connect DeCodec to a broader literature on contrastive and invariant representation learning.

## Suggestions

1. **Remove or rewrite the proof in Section 3.6.** Replace the flawed MVT argument with an intuitive explanation: the RST loss requires the decoder to produce correct reconstructions after swapping background representations, which can only be satisfied if Zs encodes no background-specific information. If a formal argument is desired, connect to mutual information or use a simpler contradiction argument rather than the MVT.

2. **Add a controlled reconstruction baseline.** Either fine-tune DAC (the architecture DeCodec is built on) on the same training set, or at minimum add a column to Table 1 showing DeCodec's reconstruction when SOP/RST/SG are all disabled (i.e., the DAC backbone trained on the same data). This would cleanly separate the effect of disentanglement from data/compute advantages.

3. **Summarize the downstream ASR and TTS results in a main-table row or short paragraph** (even if full details stay in the appendix). Currently Table 4 shows WER* for ASR, but the TTS results are entirely gated. A single sentence with key numbers would substantiate the universality claims in the main text.

4. **Narrow scope language.** Replace "universal" with "speech-and-background disentangled" in the title and abstract. Qualify the VC claim: "one-shot voice conversion on noisy speech with improved intelligibility over cascaded baselines."

## Score and Decision

### Calibration Anchors

| Paper | Avg Score | Comparison |
|-------|-----------|------------|
| **DM-Codec** (UFwefiypla) | 3.00 | Had a fundamental flaw (unresolvable text-audio length mismatch in distillation). DeCodec has no analogous fatal flaw. |
| **ivrit.ai** (aOPTDchLBz) | 2.50 | Pure dataset paper with no method or hypothesis testing. Not comparable to DeCodec. |
| **Privacy-preserving USC** (Id2JMVSQHZ) | 4.80 | Similar level of architectural contribution (codec + disentanglement) but weaker quantitative results and missing baselines. DeCodec has stronger empirical validation. |
| **Codec-LM Co-design** (KCVv3tICvp) | 5.00 | Engineering tricks with limited novelty; modest improvements. DeCodec has greater architectural novelty. |
| **RepCodec** (LfDUzzQa3g) | 5.50 | Simple, effective idea (VQ on SSL features) but limited to semantic tokens only. DeCodec is more ambitious and comprehensive. |
| **Loopy** (weM4YBicIP) | 8.00 | Very strong results with compelling demos across all 4 reviewers. DeCodec has weaker presentation/polish and no demo evaluation. |
| **Progressive Compression** (CxXGvKRDnL) | 8.00 | Strong theoretical contribution (uniform-noise diffusion + compression) with clean evaluation. DeCodec weaker on the theory side. |

DeCodec sits above the mid-range papers (4.80–5.50) due to its more novel architectural contributions, strong ablation evidence, and demonstrated unification of multiple tasks. It sits below the 8.0 anchors, whose evaluations are more thorough and whose contributions are more general. The fixable nature of the major weaknesses (a flawed proof and comparison confounds) supports acceptance contingent on revision.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>