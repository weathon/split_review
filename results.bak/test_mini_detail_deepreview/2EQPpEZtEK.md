Now I have enough information to produce the final review. Let me synthesize everything.

**Round-1 bracket:** Based on the calibration search, the paper sits between weak TTS papers at ~3.0 (Simple-TTS, DM-Codec, Fox-TTS) and strong papers at 8.0 (not TTS). The relevant middle band (3.5-7.5) includes accepted TTS papers at 5.25 (MaskGCT), 6.25 (DiTTo-TTS), 6.40 (CLaM-TTS), and 6.40 (HALL-E).

**Narrowing within bracket:** DiSTAR compares favorably to MaskGCT (5.25) — more novel architecture, stronger WER results. It's comparable to DiTTo-TTS (6.25) and CLaM-TTS (6.40) in novelty/empirical strength, though slightly weaker on evaluation completeness.

**Final score rationale:** The paper has genuine but contained weaknesses (NFE mismatch, incomplete ablations, unaddressed super-human metrics). It's a solid conference contribution. Placing it slightly below the strongest anchors (~6.4) but above MaskGCT (5.25) yields **6.0**.

---

## Summary

DiSTAR proposes a zero-shot text-to-speech framework that operates entirely in the discrete RVQ code space, coupling a causal autoregressive language model (which produces a contextual hidden state) with a masked diffusion transformer to perform patch-wise parallel generation. The key architectural contribution is extending next-patch diffusion (previously done over continuous latents, e.g., DiTAR) into the discrete RVQ domain, thereby avoiding continuous-latent optimization challenges while retaining patch-level parallelism and adding RVQ-specific decoding control. The method dispenses with forced alignment and duration predictors.

## Strengths

- **State-of-the-art objective results across benchmarks.** DiSTAR-medium (0.3B) achieves 1.66% WER on LibriSpeech test-clean and 1.32% on Seed-TTS test-en, outperforming all compared baselines including DiTAR (2.39%/1.78%), F5TTS (2.02%/1.35%), and IndexTTS (2.57%/1.92%) (Table 1). This directly supports the claim of strong robustness.

- **Best subjective naturalness and speaker similarity among compared systems.** In blind listening tests (Table 2), DiSTAR attains SMOS of 3.31 (highest) and a positive CMOS of 0.22 relative to human speech, surpassing E2TTS (SMOS 3.29, CMOS -0.08) and F5TTS (SMOS 3.08, CMOS 0.01).

- **Parameter-efficient scaling.** DiSTAR-medium (0.3B) achieves lower WER and comparable UTMOS to DiTAR (0.6B parameters), showing the discrete AR+masked diffusion design uses parameters more efficiently than the continuous counterpart.

- **Controllable bitrate/compute via RVQ layer pruning.** Figure 2 demonstrates that pruning upper RVQ layers at inference trades speaker similarity (0.58→0.64) while WER stays near its minimum from 6 layers onward, enabled by the stochastic layer truncation training technique.

## Weaknesses

### Major

- **Mismatched NFE comparison with DiTAR.** The main comparison (Table 1) pits DiSTAR at NFE=24 against DiTAR at NFE=10. Since DiTAR's performance likely improves with more function evaluations, the claimed superiority of DiSTAR may partly reflect compute budget rather than representational advantage. The abstract states "inference cost close to its continuous counterpart DiTAR," but 2.4× the NFE (24 vs. 10) makes this claim unsupported. The paper should either match NFE between the two methods or report DiTAR at NFE=24. Without this, the reader cannot assess whether the discrete formulation provides genuine quality advantages over continuous next-patch diffusion or simply benefits from more decoding steps.

### Minor

- **Super-human WER not discussed.** DiSTAR-medium achieves 1.66% WER on LibriSpeech test-clean, below the human reference of 1.80%. Similarly on Seed-TTS test-en (1.32% vs. 1.47% human). This is a known phenomenon in the TTS literature (e.g., VALL-E 2 reported similar findings), but the paper does not acknowledge or contextualize it. A brief discussion of why ASR-based WER can favor synthesized speech (e.g., cleaner acoustics, ASR model biases) would improve the paper's credibility.

- **Positive CMOS vs. human speech unaddressed.** DiSTAR obtains a statistically significant positive CMOS of 0.22 ± 0.13 relative to human speech (Table 2), meaning listeners preferred DiSTAR over ground-truth recordings. The paper does not discuss this, which risks undermining the CMOS metric's face validity.

- **Incomplete ablation of decoding heuristics.** The three decoding tricks (layer-wise temperature shaping, position-wise temperature shaping, hybrid sampling) are introduced to counter a "tail-first bias," but Table 3 only compares the combined set against a baseline — the individual contribution of each trick is never isolated. The reader cannot tell whether all three are necessary or whether simpler alternatives would suffice.

- **No confidence intervals for objective metrics.** Only subjective metrics (CMOS, SMOS) have confidence intervals. WER, SIM, and UTMOS in Table 1 are reported as point estimates without variance or statistical significance. For a paper making SOTA claims, this limits the reader's ability to assess whether differences are meaningful.

- **Missing comparison with VoiceCraft.** VoiceCraft (Peng et al., 2024) is a discrete AR LM for TTS that the paper's approach explicitly aims to improve upon. It is cited in the related work (line 49) but not included in the objective or subjective comparisons. While no paper can compare with every system, VoiceCraft's relevance to the discrete-space thesis makes its omission notable.

- **No FLOPs or real-time factor reported.** The paper provides parameter counts but not total decoding cost. Since DiSTAR runs the AR LM once and the diffusion head for N=24 steps, the total cost is 1 + 24 forward passes through the diffusion transformer. Reporting FLOPs or RTF would substantiate the "inference cost close to DiTAR" claim.

### Trivial

- The stride parameter $S$ is introduced with the possibility of overlapping windows ($S < P$), but all experiments use $S = P = 8$ (no overlap). The paper should note whether overlapping patches were tested.

## Nice-to-Haves

- **Domain shift evaluation.** The introduction motivates DiSTAR partly by claiming continuous latents are "sensitive to domain shift," but this is never tested. An experiment measuring WER under domain shift (e.g., noise, accents, spontaneous speech) would substantiate this motivation.
- **Ablation of embedding initialization** (transplanting codebook channels, Section 3.4) and whether it helps relative to random initialization.
- **Demonstration that stochastic layer truncation does not hurt full-depth performance** by comparing models trained with and without the technique at 9 layers.

## Removed Points

These points were flagged by reviewers but are removed after cross-checking against the paper:

1. **"The 'drafting' claim is misleading: the AR LM does not produce discrete tokens."** The paper's Section 3.1.1 and 3.1.2 clearly describe the AR module as producing a "compact hidden sketch" / conditioning state $\mathbf{h}_k$, and the term "draft" is used figuratively throughout the TTS literature (DiTAR uses the same language). The method section is transparent about the AR producing a hidden state, not discrete tokens. This is a terminology preference, not a factual error.

2. **"Non-monotonic WER under RVQ layer pruning."** The variation (WER: 1.88 → 2.04 → 1.98 across 6→8→9 layers) is within typical measurement noise for WER (±0.1–0.2% absolute). The paper's description ("WER changes little") is accurate.

3. **"Missing related works"** (Mega-TTS 2, NaturalSpeech 3, etc.): Every paper must make choices about which baselines to include. The paper already compares with 6+ strong baselines on both objective and subjective metrics, which is standard.

4. **"Equation (2) weighting not justified."** The paper explicitly states it "recovers an upper bound on the sequence negative log-likelihood," which is consistent with the LLaDA-style masked diffusion formulation it cites.

5. **"Criticism about code/model not released."** Removed per the hard rule: reproducibility concerns rooted in doubting release status are not valid criticisms.

6. **Generic formatting/style criticisms** removed as parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The harsh critic identified one genuinely useful cross-check (the NFE mismatch) and several diligence issues, but no synthesis-level observation that the paper itself does not already surface.

## Suggestions

1. **Compare DiSTAR to DiTAR at matched NFE** (both at NFE=10 or both at NFE=24). This is essential for the paper's core claim about discrete-space advantages. If DiSTAR wins at NFE=10, the discrete-space thesis is strongly supported; if not, the advantage should be framed as a compute-quality trade-off rather than a representational one.

2. **Acknowledge and contextualize the super-human WER and positive CMOS.** A brief paragraph discussing ASR model bias, the "cleaner synthetic speech" hypothesis, and how the listening test was conducted (was the human reference from the same recording conditions?) would substantially strengthen credibility.

3. **Add individual ablations of the three decoding heuristics** (layer-wise shaping, position-wise shaping, hybrid sampling) to validate each component.

4. **Report confidence intervals or standard deviations for objective metrics** (WER, SIM) across multiple runs or bootstrap samples.

## Score and Decision

**Round-1 bracket:** The paper sits between weak TTS papers at ~3.0 (Simple-TTS, DM-Codec, Fox-TTS) and the 8.0 band. The relevant middle band (3.5–7.5) includes accepted TTS papers at 5.25 (MaskGCT), 6.25 (DiTTo-TTS), 6.40 (CLaM-TTS), and 6.40 (HALL-E).

**Round-2 narrowing (4.5–7.5):** DiSTAR is clearly stronger than MaskGCT (5.25) — more novel architecture, better WER results, more thorough evaluation. It is comparable to DiTTo-TTS (6.25): both combine existing ideas in novel ways and have strong empirical support, but DiSTAR's evaluation has slightly more unaddressed issues. Compared to CLaM-TTS (6.40) and HALL-E (6.40), DiSTAR has cleaner architecture and better WER, but its evaluation shortfalls (NFE mismatch, missing ablations) prevent it from reaching the same quality tier.

**Final score:** 6.0 — A solid conference contribution with good empirical results and a well-motivated architecture, held back by a few addressable but consequential evaluation gaps.

**Anchors used:** 
- MaskGCT (5.25, round 1) — DiSTAR has stronger results and more novel architecture
- DiTTo-TTS (6.25, round 1) — Comparable novelty; DiSTAR evaluates more thoroughly on some axes but less on others  
- CLaM-TTS (6.40, round 1) — Comparable paper quality; DiSTAR has better WER but less complete ablations
- HALL-E (6.40, round 1) — HALL-E had a stronger dataset contribution; DiSTAR has better core TTS results
- RADD (6.20, round 2) — Different topic; comparable theoretical depth but DiSTAR stronger empirically

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>