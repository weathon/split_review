## Summary

DiSTAR proposes coupling an autoregressive language model (AR drafter) with a masked diffusion refiner, operating entirely within a discrete residual vector quantization (RVQ) code space for zero-shot text-to-speech synthesis. The AR model drafts a compact next-patch sketch, and the masked diffusion model completes the patch in parallel, achieving blockwise parallelism without forced alignment or duration predictors. DiSTAR-medium (0.3B) achieves the lowest WER on both LibriSpeech-PC (1.66%) and SeedTTS test-en (1.32%) among compared systems.

## Strengths

1. **State-of-the-art robustness (WER) across two benchmarks.** Table 1 shows DiSTAR-medium achieves the lowest WER on both LibriSpeech-PC test-clean (1.66%) and SeedTTS test-en (1.32%), outperforming all baselines including F5TTS-v1 (2.02%/1.35%), DiTAR (2.39%/1.78%), IndexTTS (2.57%/1.92%), and E2TTS (2.74%/2.20%). DiSTAR-base (0.15B) also outperforms most systems, demonstrating parameter efficiency. The improvement even over the codec's own resynthesis WER (1.83%/1.71%) is notable.

2. **Novel architectural contribution with clear motivation.** Coupling an AR drafter with masked diffusion entirely in discrete RVQ space is a well-motivated design that addresses the joint time-depth dependency challenge of multi-codebook representations while retaining the stability and interpretability of discrete LM training. The design eliminates duration predictors and forced alignment, and the shared discrete code space enables end-to-end optimization without inter-module mismatch.

3. **Practical variable bit-rate control via RVQ pruning.** Figure 2 demonstrates that pruning higher RVQ layers at inference (enabled by stochastic layer truncation during training) smoothly trades off speaker similarity and WER without retraining. This is a concrete practical advantage of the discrete formulation.

4. **Strong subjective results with a clear CMOS lead.** Table 2 shows DiSTAR achieves CMOS of 0.22±0.13, well above all competitors (next best: F5TTS at 0.01±0.12), with non-overlapping confidence intervals. SMOS (3.31±0.25) is competitive with E2TTS (3.29±0.19).

5. **Better performance with half the parameters of the continuous counterpart.** DiSTAR-medium (0.3B) substantially outperforms DiTAR (0.6B) across all metrics, supporting the claim that the discrete design avoids optimization issues of continuous latents.

## Weaknesses

### Fatal
None.

### Major

1. **Speaker similarity SOTA claim is contradicted by the paper's own objective data.** The contributions list (line 37) claims "state-of-the-art robustness, speaker similarity, and naturalness." However, Table 1 shows DiSTAR-medium achieves SIM of 0.67 (LibriSpeech) vs. E2TTS at 0.70 and F5TTS at 0.68; on SeedTTS it achieves 0.66 vs. E2TTS at 0.71 and F5TTS at 0.68 — placing DiSTAR behind two baselines on both benchmarks for objective speaker similarity. The paper's own text (line 209) more accurately describes SIM as "on par with the best alternatives," but the abstract and contribution list go beyond this. This framing disconnect should be corrected.

2. **The core architectural contribution (AR + diffusion coupling) is not ablated.** The key novelty is coupling an AR drafter with a masked diffusion refiner. Yet no experiment isolates either component — e.g., training a variant that replaces the diffusion infiller with an AR decoder that predicts all RVQ layers autoregressively, or a variant that uses AR to produce full patches without diffusion refinement. The decoding strategy ablation (Table 3) only varies sampling temperature/mode; it does not test whether the diffusion component itself is responsible for the gains. Without this, the reader cannot attribute the reported performance to the claimed architectural insight.

3. **Inference-cost parity claim is unsupported by any measurement.** The abstract (line 31) claims DiSTAR maintains "inference cost close to its continuous counterpart DiTAR." However, no wall-clock latency, real-time factor, throughput, or FLOPs measurements are provided anywhere in the paper. DiSTAR uses NFE=24 versus DiTAR's NFE=10 (2.4× more diffusion steps) while having half the parameters (0.3B vs 0.6B). Whether these factors cancel is unclear, and no evidence is offered.

### Minor

1. **DiTAR comparison uses cited rather than re-evaluated scores.** DiTAR scores are marked with ♦ indicating they are taken from the original DiTAR paper. Since the evaluation pipeline (ASR model, prompt set, preprocessing, data splits) may differ, the most directly comparable baseline comparison is weaker than if DiTAR had been re-evaluated in the same pipeline. Other baselines (IndexTTS) may face the same issue. That said, DiSTAR outperforms DiTAR by a large margin (WER 1.66 vs 2.39 on LibriSpeech), so the main conclusion is unlikely to be overturned.

2. **No confidence intervals on objective metrics (Table 1).** For WER and SIM differences as small as 0.01–0.03 between systems, the absence of variance information makes it impossible to assess whether reported improvements are systematic or within measurement noise.

3. **Decoding heuristics introduce multiple tunable hyperparameters without sensitivity analysis.** The decoding strategy (Section 3.4) introduces at least five tunable choices (layer-wise temperature factor, position-wise temperature factor, top-k, top-p, temperature annealing range, hybrid sampling ratio) with no sensitivity analysis for any of them. A reader implementing DiSTAR would need to tune these from scratch.

### Trivial
- The non-monotonic WER trend in Figure 2 (increase from 1.88→2.04 when going from 6 to 8 RVQ layers) suggests minor measurement noise, though values are within a small range.

## Nice-to-Haves
- Re-evaluating DiTAR under the same evaluation pipeline would strengthen the most directly comparable baseline comparison.
- Adding confidence intervals or error bars to Table 1 would improve rigor.
- A brief discussion of why DiSTAR-medium's WER (1.32 on SeedTTS) is lower than the codec's own reconstruction WER (1.71) would be illuminating — this is a remarkable result worth highlighting.
- An ablation of the aggregator design (overlapping vs. non-overlapping patching) would strengthen the architectural understanding.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "IndexTTS (Deng et al., 2025) is cited as an arXiv preprint... cannot be independently verified" — REMOVED per hard rule: cannot question existence of cited works.
- "Missing appendix content / proofs deferred to appendix" — REMOVED per hard rule: parser strips appendix from all papers.
- Any typo/formatting criticisms — REMOVED per hard rule: formatting artifacts are parser issues, not author errors.
- "Missing related works" — REMOVED per hard rule.
- Strength Finder's claim of "SOTA speaker similarity" — REMOVED because it conflicts with the verified weakness: objective SIM in Table 1 shows DiSTAR is behind E2TTS and F5TTS on both benchmarks.
- Strongest framing of "DiTAR comparison undermines central competitive claim" — REMOVED because even accounting for pipeline differences, DiSTAR outperforms DiTAR by a large margin (WER 1.66 vs 2.39 on LibriSpeech), making the main conclusion robust.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Correct the speaker similarity framing throughout (abstract, contributions, conclusion) to match the evidence: DiSTAR achieves competitive SIM (not SOTA), with SOTA WER and strong subjective results.
2. Add an ablation experiment that removes or replaces either the AR or diffusion component to isolate the contribution of the coupling.
3. Provide wall-clock latency or real-time factor measurements for DiSTAR and at least DiTAR to support the inference-cost claim.
4. Add confidence intervals or error bars to Table 1.
5. Briefly discuss why DiSTAR's WER can be lower than the codec's own reconstruction WER.

## Score and Decision

**Calibration Anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| CLaM-TTS (ofzeypWosV) | 6.40 | R2 | Similar RVQ+LM TTS paper; DiSTAR has stronger WER results but weaker ablations. Comparable. |
| HALL-E (868masI331) | 6.40 | R2 | Long-form TTS with RVQ; DiSTAR has broader baseline comparison and more novel architecture. Slightly stronger. |
| DiTTo-TTS (hQvX9MBowC) | 6.25 | R1, R2 | Diffusion TTS paper; DiSTAR has stronger architectural novelty and results but weaker ablations. Comparable. |
| MaskGCT (ExuBFYtCQU) | 5.25 | R2 | Masked generative codec TTS; DiSTAR is clearly stronger in results and architectural novelty. |
| DiffAR (GTk0AdOYLq) | 5.75 | R1 | Diffusion AR speech model; DiSTAR has much stronger evaluation breadth and practical contributions. Clearly stronger. |
| Codec-LM Co-design (KCVv3tICvp) | 5.00 | R2 | RWQ codec-LM design; DiSTAR has much stronger contributions. |
| Fox-TTS (pWdkM9NNCA) | 3.00 | R1 | Weak paper; DiSTAR is far stronger. |
| Simple-TTS (m4mwbPjOwb) | 3.00 | R1 | Weak paper; DiSTAR is far stronger. |

**Round 1 bracket:** 5.0–6.5 (initial estimate based on weak anchors ~3.0 and strong middle anchors ~6.25)

**Round 2 narrowing:** Compared against CLaM-TTS (6.40), HALL-E (6.40), DiTTo-TTS (6.25), and MaskGCT (5.25). DiSTAR is comparable to CLaM-TTS and DiTTo-TTS but slightly weaker than CLaM-TTS in terms of evaluation completeness (missing core ablation, unsupported inference claim, overclaiming). It is stronger than MaskGCT. This places it at approximately 6.0.

**Final Score:** 6.0 — The paper presents a solid architectural contribution with compelling WER results and practical advantages. However, the missing ablation of the core AR+diffusion coupling, the unsupported inference-cost claim, and the overstated speaker similarity framing prevent it from reaching the higher end of the range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>