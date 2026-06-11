Now I have enough context. Let me finalize the review with the calibrated score.

---

## Summary
DiSTAR proposes a zero-shot TTS framework that operates entirely in the discrete RVQ code space, coupling an autoregressive Transformer (which produces patch-level contextual summaries h_k) with a discrete masked diffusion model (which performs parallel infilling of multi-codebook tokens within each patch). The paper demonstrates strong subjective results against competitive baselines (F5TTS, E2TTS, CosyVoice 2) and shows practical controllability via RVQ layer pruning at inference time without retraining.

## Strengths
- **Novel architecture coupling AR drafting with discrete masked diffusion over RVQ codes**: The patch-wise decomposition — where a causal AR model captures cross-patch dependencies via a hidden sketch h_k and a bidirectional masked diffusion Transformer resolves intra-patch multi-codebook structure in parallel — is a clean architectural contribution not present in prior discrete TTS systems. The training objective (Eq. 2) directly implements this as a conditional masked-LM loss over patch-level spans.
- **Strong subjective results against credible baselines**: Table 2 shows DiSTAR leads in both SMOS (3.31 ± 0.25) and CMOS (0.22 ± 0.13) on SeedTTS test-en, outperforming F5TTS (CMOS 0.01), E2TTS (CMOS −0.08), CosyVoice 2 (CMOS −0.04), and FireRedTTS (CMOS −0.34). This is the paper's most compelling piece of evidence.
- **Stochastic layer truncation enables retraining-free bitrate/compute control**: The training scheme in Section 3.4 randomly drops upper RVQ layers, and Figure 2 validates that retaining more layers monotonically improves speaker similarity (0.58 → 0.64 from 2 to 9 layers) while WER remains stable (1.88–2.18), confirming the hypothesis that upper layers encode acoustic detail rather than linguistic content.
- **RVQ-aware decoding heuristics address a real "tail-first" bias**: The paper identifies that tokens near the end of each patch receive inflated confidence during masked diffusion decoding and proposes three mitigations (layer-wise and position-wise temperature shaping, hybrid sampling). Table 3 validates concrete improvements (WER 2.11→1.91, SPK 0.626→0.640).
- **Clean pipeline simplification**: By operating entirely in the discrete domain, DiSTAR inherits [EOS]-based termination without auxiliary duration predictors or stop heads, and shares the RVQ code space between drafter and refiner to reduce inter-module mismatch.

## Weaknesses

### Fatal
None.

### Major
- **Ablation study in the main paper is insufficient for a methods contribution**: Section 4.3 contains only Table 3, comparing three decoding-strategy variants on two metrics. The paper references ablation of patch size in Appendix D and CFG settings in Appendix C (stripped by the parser from this version), but even including those, the main paper presents no ablation of the core architectural coupling itself — e.g., MDM-only (no AR conditioning) or AR-only (predicting tokens without diffusion) variants would directly test whether the AR+MDM decomposition matters. There is also no ablation of the number of diffusion steps (NFE), the aggregator design, or the contribution of overlapping windows (S < P). For a paper whose primary contribution is a new architectural framework, readers cannot assess whether each component is individually motivated from the main text.

### Minor
- **DiSTAR beats the codec's own reconstruction on WER without explanation**: On SeedTTS test-en, RVQ-resynthesized audio (the codec's theoretical fidelity ceiling) scores 1.71% WER while DiSTAR-medium achieves 1.32%. On LibriSpeech: 1.83% vs. 1.66%. This is a striking result — the generated speech is apparently more intelligible to the ASR model than the codec can reconstruct from ground-truth codes. The paper neither acknowledges nor explains this phenomenon, despite WER being a headline metric. It may reflect the diffusion model acting as a regularizer that cleans up coding artifacts, or an evaluation pipeline artifact; either warrants discussion.
- **"Rich output diversity" is claimed but never measured**: The abstract states DiSTAR "maintain[s] rich output diversity," and Section 3.4 discusses the diversity-determinism trade-off, but no diversity metric (e.g., variance of acoustic features across multiple samples of the same prompt) appears in the experiments. The claim is unsubstantiated.
- **"SOTA speaker similarity" claim needs qualification**: The paper claims state-of-the-art speaker similarity, but objective SIM scores (Table 1) show DiSTAR-medium trailing E2TTS on both LibriSpeech (0.67 vs. 0.70) and SeedTTS (0.66 vs. 0.71). The claim holds only for subjective SMOS (Table 2), not objective SIM. The paper should distinguish these.
- **Exposure bias mitigation is partial**: The paper claims DiSTAR "mitigat[es] classic AR exposure bias" (abstract, line 96). However, the AR module still sees ground-truth history during training but generated history during inference, so exposure bias persists across patches. The mitigation applies only *within* patches where the masked diffusion operates non-autoregressively. The claim should be qualified.
- **"Inference efficiency" is not quantified**: Section 4.4 is titled "Inference Efficiency and Controllability" but reports no wall-clock time, RTF, FLOP counts, or memory measurements. The only efficiency-related result is the RVQ layer-pruning quality trade-off (Figure 2), which demonstrates compute-vs-quality control rather than absolute efficiency relative to baselines. This title-content mismatch is misleading.

### Trivial
- **No limitations discussed**: The conclusion (Section 5) summarizes contributions without acknowledging any limitations or failure cases.
- **NFE mismatch with DiTAR**: DiSTAR uses NFE=24 while DiTAR is reported at NFE=10 (as per its own paper). The comparison conflates architectural and compute differences, though the paper does transparently mark DiTAR's reported numbers with ♦.

## Nice-to-Haves
- A diversity metric (e.g., variance of WavLM embeddings across multiple samples of the same prompt) would substantiate the diversity claim.
- Wall-clock timing or RTF measurements comparing DiSTAR to baselines would strengthen the efficiency narrative.
- An MDM-only ablation (no AR conditioning) would help demonstrate that the AR module contributes beyond providing context to the diffusion model.
- Discussion or ablation of the overlapping-window design (S < P) to show whether the overlap improves boundary smoothness.
- Explicit clarification in Section 3.4 that θ_AR is trained jointly via gradients from the MDM loss through h_k would resolve ambiguity about the training procedure.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic claimed Equation (1) is "misleading" and the AR training is a "structural issue"**: Overblown. The paper clearly describes the architectural decomposition (AR produces h_k, MDM predicts tokens conditioned on h_k), states training minimizes Eq. 2, and notes "end-to-end optimization" (line 29). The chain-rule factorization in Eq. 1 is conceptual framing, not a claim that θ_AR has a separate loss. Kept only as a minor clarity note.
- **Harsh Critic claimed overlapping-patch predictions create unresolved conflicts**: Based on a misreading. The prediction target ˙C^(k) has length S (the stride), so generated segments are contiguous and non-overlapping. The overlap exists only in input context windows C^(k). Line 112 explicitly states: "the diffusion head predicts, in one shot, a segment whose length matches the aggregator's stride on the output stream, ensuring consistency."
- **Harsh Critic claimed decoding heuristics "feel like patches" and add hyperparameters other systems don't need**: Stylistic opinion, not a factual weakness. The paper identifies a real problem (tail-first bias) and validates mitigations in Table 3.
- **Harsh Critic claimed the introduction's critique of continuous-latent systems lacks citation**: The introduction cites relevant systems and makes reasonable framing arguments. Standard academic positioning.
- **Strength Finder "pipeline simplification" as an independent strength**: This is a consequence of the core architectural choice, not a separate contribution. Folded into the architecture strength.
- **Strength Finder "embedding initialization" as a separate strength**: While sensible, this is a minor engineering detail, not a contribution-level strength.

## Novel Insights
The paper's most interesting empirical finding — that DiSTAR's generated speech achieves lower WER than the codec's own reconstruction from ground-truth codes — goes unexamined. If this is genuine (the masked diffusion model acts as a regularizer producing cleaner token sequences than the original encoder), it suggests discrete diffusion over RVQ codes may have a denoising/cleaning effect that improves intelligibility beyond the codec's fidelity ceiling. This phenomenon has implications beyond TTS for any system using RVQ codecs and deserves dedicated investigation.

## Suggestions
- Explicitly state in Section 3.4 that θ_AR is trained jointly via gradients from the MDM loss through h_k, clarifying the end-to-end training procedure.
- Add a brief paragraph discussing the WER vs. codec-upper-bound result — even a speculative explanation acknowledges the anomaly.
- Qualify the "SOTA speaker similarity" claim to specify it refers to subjective (SMOS), not objective (SIM).
- Either measure output diversity or soften the "rich output diversity" claim in the abstract.
- Rename Section 4.4 or add actual timing measurements to match the "efficiency" in the title.

## Score and Decision

**Calibration anchors referenced:**

| Paper | Avg Score | Round | Comparison to DiSTAR |
|---|---|---|---|
| MaskGCT (ExuBFYtCQU) | 5.25 | R1, R2 | DiSTAR more novel architecture, stronger subjective results |
| VALL-E 2 (0bcRCD7YUx) | 5.00 | R2 | DiSTAR more principled approach, better evaluation evidence |
| Vec-Tok Speech (C53xlgEqVh) | 5.20 | R2 | DiSTAR cleaner architecture, better subjective results |
| DiffAR (GTk0AdOYLq) | 5.75 | R1, R2 | Roughly comparable; DiSTAR has more modern baselines and stronger subjective results |
| DiTTo-TTS (hQvX9MBowC) | 6.25 | R1, R2 | DiSTAR more novel but thinner ablation; roughly comparable overall |
| CLaM-TTS (ofzeypWosV) | 6.40 | R1, R2 | CLaM-TTS stronger on evaluation thoroughness and theoretical grounding |
| HALL-E (868masI331) | 6.40 | R2 | HALL-E more comprehensive evaluation, introduces benchmark dataset |
| Interpolating AR/Discrete Diffusion (tyEyYT267x) | 8.00 | R1 | Strong-theory paper; DiSTAR is an empirical systems paper, not comparable |

**Round 1 bracket:** 5.0–6.5  
**Round 2 narrowed:** DiSTAR sits between MaskGCT (5.25) and CLaM-TTS (6.40), comparable to DiffAR (5.75) and slightly below DiTTo-TTS (6.25). DiSTAR has stronger novelty than DiTTo-TTS but thinner evaluation; it has stronger results than MaskGCT but less comprehensive ablation than CLaM-TTS.

**Final score:** DiSTAR is a solid paper with a genuinely novel architecture, strong subjective results, and practical controllability features, held back by an overly thin main-paper ablation, several unsubstantiated claims, and an unexplained WER anomaly. It lands at **6.0** — a clear accept with room for improvement.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>