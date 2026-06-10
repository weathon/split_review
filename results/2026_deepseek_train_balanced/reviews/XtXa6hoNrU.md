## Summary
This paper identifies why randomized Hadamard (RH) transforms outperform randomized orthogonal (RO) transforms for W4A4 LLM quantization: both equally reduce quantization error for ordinary tokens, but RO increases quantization error on rare "massive activation" tokens while RH slightly reduces it. Based on this diagnostic, DFRot uses a weighted loss (emphasizing massive-activation tokens) and alternating optimization (quantization parameters ↔ rotation matrix via orthogonal Procrustes / SVD) to refine the R1 rotation matrix. Results show modest but consistent perplexity improvements (0.05–0.25) over QuaRot across LLaMA2-7B/13B, LLaMA3-8B, and Mistral-7B with minimal overhead (8–20 minutes).

## Strengths
- **Clean causal diagnosis of the RH > RO gap (Table 1, Section 3.2).** The controlled FP16-retention experiment directly proves that the entire performance gap between RO and RH at W4A4 is attributable to massive-activation tokens: when those tokens are kept in FP16, RO and RH yield essentially identical PPL (e.g., LLaMA3-8B W4A4KV4: 7.83 vs. 7.82). This is a genuinely novel finding that goes beyond prior work.
- **Sound and efficient method design.** The weighted loss (Eq. 4) directly operationalizes the diagnostic insight, and the alternating optimization (quantization fitting → Procrustes rotation refinement via SVD) avoids backpropagation through the full network, keeping overhead low (8–20 min). The closed-form Procrustes solution is principled, and the EM/k-means analogy provides a clean conceptual framing.
- **Systematic hyperparameter analysis.** Figures 3–6 (γ ablation across all four models, two quantization settings, both RH and RO initializations) are thorough and honest: γ=50–200 works consistently, while γ=1 or γ→∞ both degrade performance. The observation that Mistral-7B behaves differently is noted and explained.
- **Consistent gains across RTN and GPTQ.** The method improves both RTN and GPTQ settings (e.g., LLaMA3-8B W4A4KV4: QuaRot-RTN 11.06 → DFRot-RTN 9.67; QuaRot-GPTQ 8.20 → DFRot-GPTQ 7.95), demonstrating robustness to the weight-quantization algorithm.

## Weaknesses

### Fatal
None.

### Major
- **Missing comparison against the most directly comparable prior work (SpinQuant).** The paper repeatedly cites SpinQuant (lines 91, 167, 237, 345) — which also learns rotation matrices via Cayley optimization — and positions DFRot as a more efficient alternative ("substantial computational resources and adds complexity," line 43; "necessitates fine-tuning the entire network," line 237). Yet no experimental comparison to SpinQuant is provided. The evaluation is anchored entirely against QuaRot (fixed Hadamard), which is not the relevant baseline for a learned-rotation method. Without this comparison, the reader cannot assess whether DFRot's Procrustes-based optimization matches, exceeds, or falls short of SpinQuant's accuracy at comparable or lower cost. This is the single most significant gap in the experimental evaluation.

### Minor
- **"Single sample" claim is underspecified (abstract, line 15; Section 4, line 490).** The paper states that DFRot optimizes the rotation matrix with "just a single sample" / "an additional sample." The experimental setup (line 430) specifies 128 samples from WikiText-2 for GPTQ quantization, but never states how large the calibration set X^{cal} is for DFRot's rotation optimization (Section 3.3–3.4), nor whether it uses 1 sample, a subset of the 128, or all 128. This ambiguity harms reproducibility. The claim should be clarified and validated with sensitivity analysis over different single-sample choices.
- **"Outlier-Free and Massive Activation-Free" framing is overstated (title, abstract, line 630).** The method does not eliminate massive activations — they remain present in the activations. It reduces their *quantization error* via a weighted loss. The paper's own Table 1 shows that even with the RH baseline, retaining massive-activation tokens in FP16 provides further gains (QuaRot.FP16 > QuaRot), confirming these activations persist. The phrasing implies a stronger property than what is demonstrated.
- **No error bars or multiple-run statistics.** The PPL improvements over QuaRot are small (0.05–0.25) and, for some settings (e.g., Mistral-7B GPTQ: 5.81 vs 5.81 for W4A4KV4), essentially zero. Without error bars or multiple trials with different calibration subsets, it is unclear whether the smaller reported gains are statistically meaningful or within noise.
- **Massive-activation threshold is not explicitly defined.** The paper identifies X^m (tokens with massive activations) by referencing sun2024massive but does not state the operational criterion (e.g., top-k% by magnitude, a fixed norm threshold) used in its own experiments. This is needed for full reproducibility.

### Trivial
None.

## Nice-to-Haves
- Adding a limitations paragraph would strengthen the paper, given the modest gains on some models and the limited model scale (≤13B parameters).
- The diagnostic Table 1 includes W4A8KV16 results for RO/RH; the main results could report W4A8KV16 for DFRot as well, though the gap is already known to be negligible at that setting.
- A brief discussion comparing rotation-based vs. scale-based (SmoothQuant, OmniQuant) approaches in the W4A4 setting would help situate the contribution.

## Removed Points
These points are flagged to be removed; treat them with caution:
- Criticisms about commented-out blocks (lines 118–145, 304–416) being duplicative — these are PDF extraction artifacts (comment environments are invisible in the actual submission). Removed per hard rules (formatting artifacts).
- Criticisms about "limited evaluation scale" (only 4 models) — the evaluation covers two model families across 7B–13B with both RTN and GPTQ, two activation settings, and six zero-shot tasks, which is adequate for this type of contribution. The real scope concern is the missing baseline, not model count.
- Criticisms about missing related work or references — removed per hard rules (reviewer cannot authoritatively identify missing references).
- Generic strengths about "addressing an important problem" — removed as non-concrete, lacking specific evidence from the paper.

## Novel Insights
None beyond the paper's own contributions. The key finding — that the RH vs. RO performance gap at W4A4 is entirely attributable to differential handling of massive-activation tokens — is the paper's most novel contribution and is well-supported by the controlled FP16-retention experiment.

## Suggestions
1. **Add SpinQuant as a baseline.** This is the single most important addition. If DFRot matches or exceeds SpinQuant's accuracy with less compute, this directly substantiates the paper's efficiency claim.
2. **Clarify and validate the "single sample" claim.** State explicitly the size of X^{cal} for DFRot's rotation optimization, and report sensitivity to the choice of sample.
3. **Provide error bars or multiple-run statistics** for the main PPL results, especially given the small magnitude of some improvements.
4. **Define the massive-activation threshold** used to separate X^m from X \ X^m.
5. **Tone down the "Outlier-Free / Massive Activation-Free" framing** to accurately describe what is achieved: reduced quantization error on tokens with massive activations.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>