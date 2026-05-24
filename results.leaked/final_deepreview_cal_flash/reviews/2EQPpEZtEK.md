Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces DiSTAR, a zero-shot text-to-speech framework that operates on discrete RVQ code tokens by coupling an autoregressive language model (which drafts a compact hidden sketch for the next patch) with a masked diffusion transformer (which performs parallel discrete demasking within the patch). The design enables patch-level parallelism, explicit control via RVQ-aware decoding strategies (temperature shaping, hybrid sampling), and on-the-fly bitrate/compute control through RVQ layer pruning without retraining. On LibriSpeech-PC and Seed-TTS test-en, DiSTAR achieves the lowest Word Error Rates among compared systems and the highest subjective similarity/naturalness scores (SMOS 3.31, CMOS 0.22).

## Strengths

1. **Strong empirical results across objective and subjective metrics.** DiSTAR attains the lowest WER on both LibriSpeech-PC (1.66%) and Seed-TTS test-en (1.32%) among all compared systems, while achieving the highest SMOS (3.31) and positive CMOS (0.22) in human evaluation (Tables 1 and 2). The subjective results are from a unified listening test and are not affected by cross-paper evaluation differences.

2. **Clear technical contribution: coupling AR sketching with discrete masked diffusion over RVQ codes.** The architecture — AR LM draft + discrete masked diffusion infill operating entirely on RVQ tokens — is a principled way to model the joint time-depth structure of RVQ while maintaining the stability of discrete LM training. This differs from both continuous next-patch diffusion (DiTAR) and single-codebook AR approaches, and is validated by the overall system performance.

3. **Novel and effective RVQ-aware inference strategies.** The layer-wise temperature shaping, position-wise temperature shaping, and hybrid sampling (Section 3.4) are well-motivated by the observed "tail-first" bias in masked decoding. Table 3 shows they reduce WER from 2.11% (vanilla sampling) to 1.91% (greedy with shaping) while improving SPK from 0.626 to 0.636, providing concrete empirical guidance.

4. **On-the-fly bitrate and compute control via RVQ layer pruning.** Enabled by stochastic layer truncation during training, Figure 2 demonstrates smooth trade-offs between speaker similarity (~0.58 to ~0.64) and compute by retaining different numbers of RVQ layers at inference without retraining. This is a practically useful capability absent from most prior TTS systems.

5. **Parameter efficiency and simplified pipeline.** DiSTAR-base (0.15B) achieves competitive results while being substantially smaller than IndexTTS (0.5B) and DiTAR (0.6B). The fully discrete setting provides a natural [EOS] token for termination, removing the need for duration predictors or forced alignment, simplifying training and inference.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient clarity on baseline evaluation pipeline and cross-paper comparisons.** The paper marks DiTAR scores with "♦" as "scores reported in DiTAR paper," transparently indicating they were not re-run. However, it never states which other baselines (IndexTTS, E2TTS, F5TTS) were evaluated in the same pipeline versus cited from their original papers. WER and SIM are sensitive to ASR model version, prompt selection, and decoding parameters; without knowing which baselines were run in the identical environment, the reader cannot assess how much of the reported advantage reflects a genuine improvement versus evaluation pipeline differences. This weakens the "SOTA" claim in the abstract and conclusion, even though the subjective evaluation (Table 2, conducted in a unified setting) independently supports strong performance.

2. **No ablation of core architectural components.** The paper introduces several novel design elements — the aggregator (learned mixture of layer embeddings, overlapping windows), the coupling of an AR sketch with discrete masked diffusion, stochastic layer truncation, embedding initialization from codebook transplanting — yet the sole ablation in the main paper (Table 3) tests only inference-time decoding strategies. Patch size and CFG ablations are deferred to appendices, and the central architectural choices (e.g., with vs. without the AR sketch, with vs. without overlapping windows, the embedding initialization scheme, the aggregator design) are never isolated. Without these ablations, it is impossible to attribute the reported gains to specific components rather than to training scale, data processing, or inference heuristics.

### Minor

1. **Overstated "entirely discrete" framing.** The paper repeatedly emphasizes operating "entirely in the discrete RVQ code space" (Abstract, Section 1, Section 3.1). However, the AR summarizer produces a *continuous* hidden state **h**ₖ (Section 3.1.1) that is concatenated with discrete code history to condition the diffusion module (Section 3.3: "the AR hidden is first passed through a trainable scalar gate before concatenation"). The discrete masked diffusion refinement is a genuine differentiator from continuous next-patch systems, but the "entirely discrete" claim overstates the extent to which the pipeline avoids continuous representations internally.

2. **Unsubstantiated explanation for the SIM/SMOS gap.** The paper attributes DiSTAR's higher SMOS (despite comparable SIM) to "reduced sensitivity to high-frequency artifacts in the reference prompt, which preserves cleaner timbral cues during cloning" (Section 4.2). No spectral analysis, case study, or ablation is provided to support this claim. While the observation itself is interesting, the explanation is speculative and should be either verified or stated more cautiously.

3. **Thin main ablation section.** The ablation study (Section 4.3, Table 3) consists of a single comparison of three decoding strategies. Patch size and CFG ablations are deferred to appendices that are not accessible in the main paper. For a paper introducing multiple architectural innovations, relegating the only architectural ablations to appendices makes the core paper feel incomplete.

### Trivial
- There are minor notational ambiguities in Section 3.1.1 (Equation (1) factorizes at the frame level while generation proceeds at the patch level; the expectation notation in Equation (2) could be clarified). These do not impede understanding and are common in the literature.

## Nice-to-Haves
- **Failure analysis.** The paper does not discuss or analyze failure cases (prosodic flatness, disfluencies, codec artifacts). Acknowledging failure modes strengthens credibility.
- **Diversity evaluation.** The paper claims "rich output diversity" but provides no quantitative measure (DIST-n, acoustic diversity, or speaker similarity variance).
- **Throughput quantification.** The "blockwise parallelism" advantage is mentioned qualitatively but never quantified with wall-clock time comparisons against standard AR decoding.
- **Ablation of the AR module.** Comparing DiSTAR against a variant without the AR summarizer (using only the discrete MDM with pooled code history) would directly test whether the continuous AR sketch is necessary or whether the discrete MDM alone suffices.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Invalid comparison to DiTAR is fatal to the core claim."** — The paper transparently marks DiTAR scores as from the original paper (♦). Even without DiTAR, DiSTAR achieves the best WER on both benchmarks among the remaining baselines, and the subjective evaluation (Table 2) is entirely independent. Demoted from Fatal to Major because the SOTA claim is partially supported by other comparisons and the subjective results.
- **"Notation issues in Section 3.1.1 are a formal inconsistency."** — Equation (1) provides a standard frame-level factorization that is standard practice; the patch-level generation is an approximation compatible with this decomposition. The expectation notation in Equation (2) is standard for discrete diffusion. These are minor readability issues at most.
- **"Dependence on Appendices" as a standalone weakness.** — Merged into Minor weakness #3 (thin main ablation section).
- **"Missing comparison with masked generative codec models (Wang et al. 2024)."** — The paper cites Wang et al. 2024 in Related Works and Section 3.3. The positioning could be more explicit, but this is a scope issue, not a missing citation.
- **Strengths about "thorough ablation of inference design choices" and "parameter efficiency vs DiTAR"** are retained with caveats. Generic strengths about "addressing an important problem" are dropped.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the reviews does not surface any observation about the work that is not already stated or implied by the paper.

## Suggestions

1. **Clarify the baseline evaluation pipeline.** State explicitly which baselines were re-run in the same environment and which were cited from original papers. If only DiTAR was cited, explain why (e.g., model weights unavailable) and consider re-running it if the checkpoints are now accessible.

2. **Add architectural ablations in the main paper.** At minimum, ablate (a) the AR sketch vs. conditioning on pooled code history alone, (b) overlapping vs. non-overlapping windows in the aggregator, and (c) embedding initialization from codebook transplanting vs. random initialization. This would substantiate the claimed advantages of each design choice.

3. **Provide evidence for the SIM/SMOS gap explanation.** Either add a spectral analysis comparing DiSTAR outputs against those of continuous systems, or present a case study showing high-frequency artifacts in reference prompts. If no evidence is available, remove or weaken the speculative claim.

4. **Add quantitative diversity and throughput metrics.** Reporting DIST-n or speaker similarity variance would substantiate the "rich output diversity" claim. A wall-clock comparison showing the blockwise parallelism speedup over standard AR would directly motivate the design.

5. **Tone down the "entirely discrete" rhetoric.** Acknowledge that the AR summarizer produces a continuous conditioning state, and clarify that the discreteness claim refers to the token space in which the MDM operates, not the entire intermediate representation pipeline.

## Score and Decision

### Calibration

**Round 1 (bracketing):**
- Weak band (avg < 3.5): Fox-TTS (3.00, reject), Simple-TTS (3.00, reject), DM-Codec (3.00, reject) — DiSTAR is substantially stronger than these papers, which lacked proper baselines or had fundamental flaws.
- Middle band (3.5–7.5): DiTTo-TTS (6.25, accept), CLaM-TTS (6.40, accept), DiffAR (5.75, accept), MaskGCT (5.25, accept), Discrete Diffusion LM (6.60, reject).
- Strong band (avg > 7.5): Interpolating AR/Discrete (8.00, accept), Protein Discovery (8.00, accept) — DiSTAR is clearly weaker than these.

**Initial bracket:** 4.0–6.5.

**Round 2 (narrowing within bracket):**
Pulled additional anchors in (4.5, 7.5):
- Vec-Tok Speech (5.20, reject) — similar evaluation gaps (missing ablations, comparison clarity issues); DiSTAR has a clearer contribution but comparable evaluation weaknesses.
- MaskGCT (5.25, accept) — similar approach (masked generative modeling on discrete speech codes); DiSTAR has stronger architectural novelty but weaker ablations.
- Continuous AR Modeling (6.67, accept) — stronger evaluation, clearer results.
- "Variational Approach" (5.50, reject) — experimental concerns.
- DiffAR (5.75, accept) — comparable methodology-wise.

DiSTAR sits near the lower end of this bracket, comparable to Vec-Tok Speech (5.20) and MaskGCT (5.25) but with evaluation gaps that are more significant than those papers' weaknesses in terms of ablations.

**Final score:** 5.0 — borderline. The paper presents a genuine technical contribution and strong empirical results, but the lack of architectural ablations and insufficient clarity on baseline evaluation setup prevent a clear acceptance recommendation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>