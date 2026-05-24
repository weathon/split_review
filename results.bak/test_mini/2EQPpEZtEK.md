Now I have all the information needed. Let me write the final consolidated review.

## Summary

DiSTAR introduces a zero-shot TTS framework that operates entirely in the discrete RVQ code space, coupling an autoregressive language model (AR drafter) for cross-patch context with a masked diffusion model (MDM) for parallel intra-patch infilling. The design avoids forced alignment, duration predictors, and continuous-latent optimization issues. The paper reports state-of-the-art WER on both LibriSpeech-PC and SeedTTS test-en, competitive speaker similarity, and positive CMOS in human evaluation.

## Strengths

- **Novel architecture combining AR drafting with discrete masked diffusion in RVQ space.** The paper is the first to tightly couple a causal AR Transformer (for cross-patch dependencies) with a LLaDA-style masked diffusion model (for parallel intra-patch demasking) directly on discrete RVQ tokens. This is a principled advance over prior work that either uses continuous-space next-patch diffusion (DiTAR) or single-codebook AR. The design is clearly motivated and the factorization is formally stated in Section 3.1.

- **Strong empirical results across objective and subjective metrics.** Table 1 shows DiSTAR-medium achieves the lowest WER on both LibriSpeech-PC (1.66%) and SeedTTS test-en (1.32%), outperforming strong baselines including F5TTS (2.02%/1.35%) and DiTAR (2.39%/1.78%). Table 2 shows DiSTAR attains the highest SMOS (3.31) and a positive CMOS (+0.22) over F5TTS. These results are consistently strong across both metrics and datasets.

- **Practical design choices with demonstrated benefits.** (a) Stochastic layer truncation during training enables variable bitrate at inference via RVQ layer pruning without retraining (Figure 2), providing a smooth WER/SPK trade-off. (b) The fully discrete setting preserves an [EOS] token for clean termination, eliminating the need for duration predictors or forced alignment common in continuous-space systems. (c) Embedding initialization by transplanting codec channels is a simple but effective cold-start mitigation.

- **Human evaluation confirms subjective quality gains.** Unlike many recent TTS papers that rely solely on objective metrics, DiSTAR provides CMOS and SMOS scores with confidence intervals, showing a statistically significant positive CMOS of 0.22 ± 0.13 over F5TTS and SMOS on par with or exceeding strong baselines.

## Weaknesses

### Fatal
None.

### Major
None. The issues identified below are addressable and do not invalidate the core contribution.

### Minor

1. **WER below human / oracle resynthesis is not discussed.** On LibriSpeech-PC, DiSTAR-medium achieves 1.66% WER vs. human 1.80% and RVQ resynthesis 1.83%. On SeedTTS test-en, it achieves 1.32% vs. human 1.47% and RVQ resynthesis 1.71%. A synthetic system outperforming both natural human speech and the codec's own reconstruction on an ASR metric is unusual and warrants discussion. The most likely explanation — that Whisper-large-v3 is easier on the cleaner, more uniform distribution of generated speech — should be acknowledged, as it is a known phenomenon in TTS evaluation. The paper's silence on this makes the primary quantitative claim harder to interpret. The issue is not fatal (the relative ordering across systems remains meaningful) but the paper would be strengthened by a brief discussion.

2. **DiTAR comparison confounds NFE and codec representation.** Table 1 compares DiSTAR-medium (0.3B, NFE=24) against DiTAR (0.6B, NFE=10), differing on two variables simultaneously: inference compute (2.4× more NFE) and codec representation (RVQ vs. continuous). The abstract's claim of "comparable or lower computational cost" holds for parameter count but not for diffusion steps, which dominate inference cost. A controlled comparison — e.g., evaluating DiTAR at NFE=24 or DiSTAR at NFE=10 — would strengthen the paper's argument. The existing comparison is informative but not conclusive as a head-to-head win.

3. **Ablation of the three decoding tricks is too coarse.** Table 3 compares only three configurations (sample with no shaping, sample with shaping, greedy with shaping) but does not ablate the three individual tricks (layer-wise temperature, position-wise temperature, hybrid sampling). It is therefore impossible to tell which component drives the improvement from WER 2.11% to 1.99%. A simple ablation with 5-6 rows showing incremental additions would significantly improve scientific depth.

4. **No variance or confidence intervals reported for objective metrics.** Table 1 reports single numbers for WER, SIM, and UTMOS without standard deviations, confidence intervals, or indication of whether these are single-seed or multi-run averages. Given that some of the reported differences are small (e.g., SIM values of 0.67 vs. 0.68), it is unclear which gaps are meaningful. This is common in TTS benchmarks but would benefit from explicit reporting.

5. **Default config uses no overlap despite motivating overlap in Section 3.2.** Section 3.2 motivates overlapping patches (stride < patch size) to "smooth boundaries," yet the default configuration for all main experiments uses stride = patch size = 8 (no overlap). The paper never evaluates whether overlapping helps or hurts. This disconnect between motivation and experiment is a minor internal inconsistency.

### Trivial

- The WER non-monotonicity at 8 RVQ layers (Figure 2: WER increases from 1.88% at 6 layers to 2.04% at 8 layers) is not discussed.
- The paper could clarify whether the 0.3B codec parameters are counted in the "#Params" column of Table 1.

## Nice-to-Haves

- A controlled ablation replacing the masked diffusion module with an additional AR layer on the same RVQ representation would directly isolate the benefit of the diffusion component.
- A Pareto-style plot of WER vs. NFE comparing DiSTAR and DiTAR at multiple compute budgets would resolve the NFE confounding issue.
- An analysis of the "tail-first bias" (a figure showing per-position confidence over decoding steps) would make the motivation for temperature shaping more concrete.

## Removed Points

These points were raised by reviewers but are removed after cross-checking against the paper:

- **"Missing baselines VALL-E 2, VoiceBox"** — The paper's baseline set (F5TTS, E2TTS, DiTAR, IndexTTS, CosyVoice 2, FireRedTTS) is adequate and covers the most relevant recent systems. Including every system is not necessary.
- **"WER comparison invalid because human reference may use different protocol"** — The paper explicitly states it "adopts the subset from F5TTS," and the human WER is part of that established evaluation protocol. This is a standard practice.
- **"Missing ablations for core novelty (pure AR baseline)"** — While such an ablation would be informative, the paper does compare against DiTAR and other systems that represent different design points, providing indirect evidence. This is a nice-to-have, not a missing requirement.
- **"Unfair comparison because codec differs"** — The paper uses a specific codec (MAGICODEC-based RVQ) for all its experiments; the comparison to DiTAR is apples-to-oranges by design (different representations), which is standard practice when claiming a new approach surpasses an existing one. A controlled ablation would strengthen the claim but the comparison as-is is not unfair.
- **"Missing related work"** — Removed per policy (external knowledge cannot verify this).
- **Formatting, typos, and parser artifacts** — These are parser errors, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs do not surface a perspective that meaningfully reframes or extends the paper's contributions.

## Suggestions

1. Add a paragraph discussing the WER-below-human phenomenon and why the relative comparisons remain valid.
2. Include an ablation table with individual contributions of the three decoding tricks (layer-wise temp, position-wise temp, hybrid sampling).
3. Report variance (standard deviations or confidence intervals) for objective metrics in Table 1.
4. If the DiTAR comparison is central to the "comparable computational cost" claim, provide a controlled NFE comparison or a Pareto curve.
5. Clarify whether the codec parameters (0.3B) are counted in model parameter counts.

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| DiFlow-TTS | FaGDopTTTC.md | 2.50 | R1-bracket | Much weaker — fewer baselines, no human eval, lower quality |
| StyleStream | 35ykr3JpbL.md | 3.20 | R1-bracket | Weaker — different task, limited evaluation |
| From Text to Talk | e3XLWHFrnr.md | 4.40 | R1-bracket | Slightly weaker — no human evaluation, narrower baseline set |
| Hierarchical Semantic-Acoustic | h5KLpGoqzC.md | 5.20 | R1/R2 | Comparable — similar-level TTS paper with strong results and ablations |
| Gogo | JbLmIoWwDC.md | 6.00 | R2 | Slightly stronger — cleaner evaluation, but some similar weaknesses |
| Self-Speculative Masked Diffusions | ogMTEtHO6M.md | 6.00 | R2 | Stronger on method rigor but different domain (text/protein, not TTS) |
| SpeechOp | eLsEjjFODE.md | 6.00 | R2 | Stronger — broader scope, cleaner evaluation, clearer contribution |

Round 1 bracket: 4.5–6.5. Round 2 positioned the paper near the lower half of this bracket, comparable to Hierarchical Semantic-Acoustic (5.20) but weaker than Gogo (6.00). The paper has genuine architectural novelty and strong results, but the evaluation has several addressable gaps (undiscussed WER issue, coarse ablation, missing variance) that prevent it from reaching the 5.5–6.0 tier.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>