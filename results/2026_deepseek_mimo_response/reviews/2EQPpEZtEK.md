Now I have enough calibration data. Let me finalize the review.

Based on my calibration comparisons:

**Round 1 bracket:** 5.5–7.0

**Round 2 anchors read in full:**
- MaskGCT (5.25): Fully NAR masked codec transformer. Related design but DiSTAR has more novel AR+diffusion coupling and stronger WER. DiSTAR should score above.
- DiTTo-TTS (6.25): DiT-based TTS without domain-specific factors. Similar level of contribution but DiSTAR has stronger WER and a more novel design. Comparable.
- CLaM-TTS (6.40): Probabilistic RVQ codec LM. Similar novelty level, similar types of weaknesses (missing ablations). Comparable.
- SAR diffusion (8.0): Foundational contribution to discrete diffusion theory. Much broader impact. DiSTAR is below.

DiSTAR sits between CLaM-TTS/DiTTo-TTS (~6.25-6.40) and Scaling Speech-Text Pre-training (7.00). Given its strong WER, novel architecture, but two significant evidential gaps (no architectural ablation, ambiguous baseline data), I score it **6.5**.

---

## Summary
DiSTAR is a zero-shot TTS framework that couples an autoregressive Transformer drafter with a LLaDA-style masked diffusion model, operating entirely in discrete RVQ code space. The AR model produces a coarse sketch of each patch, and the masked diffusion model infills the patch's RVQ tokens in parallel. The paper reports SOTA robustness (WER), competitive speaker similarity, and best subjective naturalness on standard benchmarks, with practical features like variable bitrate via RVQ layer pruning.

## Strengths
- **SOTA WER on both benchmarks (Table 1):** DiSTAR-medium achieves the lowest WER on LibriSpeech-PC (1.66%) and SeedTTS (1.32%), outperforming E2TTS (2.74%/2.20%), F5TTS (2.02%/1.35%), and DiTAR (2.39%/1.78%) while using 0.3B parameters — half of DiTAR's 0.6B.
- **Best subjective naturalness and similarity (Table 2):** On Seed-TTS test-en, DiSTAR achieves the highest SMOS (3.31±0.25) and CMOS (0.22±0.13), outperforming E2TTS (3.29±0.19 / -0.08±0.22) and F5TTS (3.08±0.20 / 0.01±0.12). The positive CMOS indicates human preference for DiSTAR's output.
- **Test-time bitrate/compute control via RVQ layer pruning (Figure 2, Section 3.4):** Stochastic layer truncation during training enables inference-time quality-compute trade-offs without retraining, with speaker similarity scaling smoothly from 0.58 (2 layers) to 0.64 (9 layers).
- **Parameter efficiency:** At 0.15B, DiSTAR-base achieves competitive WER (1.90% on LibriSpeech-PC) comparable to F5TTS at 0.3B (2.02%), and DiSTAR-medium at 0.3B beats DiTAR at 0.6B on WER.
- **Principled identification and mitigation of the "tail-first" decoding bias (Section 3.4, Table 3):** The paper diagnoses a specific failure mode in masked diffusion decoding — later positions in a patch receive overconfident predictions due to bidirectional context — and proposes layer-wise/position-wise temperature shaping and hybrid sampling. Table 3 shows improvement from 0.626 to 0.640 SIM while maintaining WER.
- **No duration predictor or forced alignment (Section 3.1.1):** The discrete RVQ formulation with [EOS] token eliminates auxiliary duration predictors, simplifying the pipeline compared to systems like DiTAR.

## Weaknesses

### Fatal
None.

### Major
- **No architectural ablation isolating AR vs. diffusion contributions.** The paper's central novelty is the coupling of an AR drafter with a masked diffusion refiner in RVQ space. However, the only ablation (Table 3) varies decoding hyperparameters (temperature shaping, greedy vs. sample), not the architecture itself. There is no AR-only baseline (pure next-patch causal model for patch contents), no diffusion-only baseline (non-autoregressive masked diffusion conditioned on text only), and no experiment that verifies the claimed synergy between the two components. Without such ablation, it is impossible to attribute the improvements to the AR+diffusion coupling versus other factors (the RVQ codec quality, the decoding heuristics, etc.). This is the most significant gap: the core architectural contribution lacks direct experimental validation.

- **Ambiguous baseline training data setup.** Section 4.1 states "All models are trained on Emilia," but the surrounding context is confusing. The same section says "We train DiSTAR of two sizes," and Table 1 marks only DiTAR with ♦ (reported from its paper), implying inconsistent treatment of baselines. If baselines were retrained on Emilia, this should be stated unambiguously (and the DiTAR ♦ inconsistency explained). If baselines used off-the-shelf checkpoints with different training data, the comparison conflates architecture with data differences — a critical confound in TTS where data is a dominant quality factor. This ambiguity undermines the reliability of the headline SOTA claims.

### Minor
- **Speaker similarity claim is overstated.** The paper states "DiSTAR yields SIM on par with the best alternatives" (Section 4.2), but E2TTS consistently leads on objective SIM: 0.70 vs. 0.67 on LibriSpeech-PC and 0.71 vs. 0.66 on Seed-TTS (Table 1). These 3–5 point gaps in cosine similarity are meaningful. The subjective SMOS (3.31 vs. 3.29) has overlapping confidence intervals (±0.25 vs. ±0.19). The claim should be corrected to accurately reflect that DiSTAR leads on WER and SMOS/CMOS but not on objective SIM.

- **No quantitative efficiency metrics despite efficiency claims.** Section 1 claims "inference cost close to its continuous counterpart DiTAR" and the abstract highlights "controllable computation via RVQ layer pruning." However, no real-time factor, latency, throughput, or FLOP counts are provided. The RVQ layer pruning analysis (Figure 2) shows quality trade-offs but not compute savings. One of the three stated contributions (controllable computation) is asserted but not substantiated by numbers.

- **Decoding heuristic ablation is bundled.** Table 3 compares three configurations, but the "temperature shaping" condition bundles three distinct tricks (layer-wise temperature, position-wise temperature, hybrid sampling). The individual contribution of each is unknown, and with four inference-time heuristics each with tunable hyperparameters, there is a risk of overfitting the decoding pipeline to evaluation benchmarks.

### Trivial
None.

## Nice-to-Haves
- An NFE ablation curve for DiSTAR would be informative, since competing systems use different NFE values (DiTAR=10, E2TTS/F5TTS=32, DiSTAR=24) and computational cost per NFE differs across architectures.
- The subjective evaluation (Table 2) compares against a different set of systems than the objective evaluation (Table 1), making it harder to form a unified picture.
- The overlapping vs. non-overlapping patch comparison is noted as being in Appendix D; including a brief summary in the main text would strengthen the aggregator design justification.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Reviewer concerns about baseline existence/availability are removed per policy.
- Pure formatting/style nitpicks are removed per policy.

## Novel Insights
The paper makes a genuinely novel architectural observation: coupling AR drafting with masked diffusion in fully discrete RVQ space avoids the optimization fragility of continuous-latent diffusion while retaining patch-level parallelism. The identification and principled mitigation of the "tail-first" decoding bias (later positions receiving overconfident predictions due to bidirectional context access) is a concrete insight applicable to the broader discrete diffusion community. The stochastic layer truncation for variable-bitrate inference without retraining is a practically valuable feature that goes beyond a single-metric comparison.

## Suggestions
- **Add an architectural ablation** comparing DiSTAR against (a) a pure AR next-patch model (replace the diffusion head with a standard causal decoder for patch contents) and (b) a non-autoregressive masked diffusion model conditioned on text only, both trained on the same Emilia data with the same RVQ codec. This single experiment would directly validate the paper's core thesis.
- **Explicitly clarify** whether baselines in Table 1 were retrained on Emilia or evaluated off-the-shelf, and explain the DiTAR ♦ inconsistency.
- **Report RTF or FLOP comparisons** for DiSTAR vs. DiTAR vs. F5TTS to substantiate the efficiency/controllability claims.
- **Correct the speaker similarity characterization** to accurately reflect that DiSTAR leads on WER/SMOS/CMOS but trails E2TTS on objective SIM.

## Calibration Report

**All retrieved anchors:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Simple-TTS | m4mwbPjOwb | 3.00 | 1 | Weaker: simple U-ViT adaptation, no RVQ depth modeling |
| Fox-TTS | pWdkM9NNCA | 3.00 | 1 | Weaker: flow-matching TTS, less novel architecture |
| DM-Codec | UFwefiypla | 3.00 | 1 | Weaker: speech tokenization focus, no generation |
| Audio Inverse Problem | mlPTNEIsgb | 3.25 | 1 | Different domain, weaker contribution |
| DiTTo-TTS | hQvX9MBowC | 6.25 | 1,2 | Similar: TTS paper, comparable novelty, DiSTAR has better WER |
| DiffAR | GTk0AdOYLq | 5.75 | 1,2 | Similar: AR+diffusion for speech, but raw waveform and less novel |
| SEDD | 71mqtQdKB9 | 6.60 | 1 | Stronger: foundational discrete diffusion contribution |
| Reparameterized Diffusion | 1pTlvxIfuV | 5.50 | 1 | Different: text generation focus |
| SAR Diffusion | tyEyYT267x | 8.00 | 1 | Much stronger: foundational theory bridging AR and diffusion |
| SymmetricDiffusers | EO8xpnW7aX | 8.00 | 1 | Different domain (combinatorics) |
| Discrete Walk-Jump | zMPHKOmQNb | 8.00 | 1 | Different domain (proteins) |
| Progressive Compression | CxXGvKRDnL | 8.00 | 1 | Different domain (compression) |
| ControlSpeech | zAogQOIphH | 5.20 | 2 | Weaker: style control TTS, more incremental |
| MaskGCT | ExuBFYtCQU | 5.25 | 2 | Similar: masked codec TTS, but DiSTAR has more novel coupling |
| DiffAR (retrieved again) | GTk0AdOYLq | 5.75 | 2 | See above |
| CLaM-TTS | ofzeypWosV | 6.40 | 2 | Similar: codec LM TTS, comparable novelty and results |
| DiTTo-TTS (retrieved again) | hQvX9MBowC | 6.25 | 2 | See above |
| HALL-E | 868masI331 | 6.40 | 2 | Similar: hierarchical codec LM, comparable contribution |
| Scaling Speech-Text | 3tukjsVyrE | 7.00 | 2 | Stronger: broader scaling contribution |

**Bracket:** Round 1 placed the paper between 5.5 and 7.0. Round 2 narrowed to 6.0–6.5: DiSTAR is clearly above MaskGCT (5.25) due to its more novel AR+diffusion coupling and stronger WER results, comparable to CLaM-TTS (6.40) and DiTTo-TTS (6.25) which share similar novelty levels and similar types of weaknesses (missing ablations, missing comparisons), but below Scaling Speech-Text Pre-training (7.00) which has broader impact.

**Final score:** 6.5 — slightly above the closest TTS anchors (DiTTo-TTS 6.25, CLaM-TTS 6.40) because DiSTAR presents a more novel architectural coupling (AR+masked diffusion in discrete RVQ space) with the strongest WER results, practical features (variable bitrate, no duration predictor), and principled decoding analysis. The two major weaknesses (no architectural ablation, ambiguous baseline data) are significant but addressable, and similar gaps exist in the anchor papers at comparable scores.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>