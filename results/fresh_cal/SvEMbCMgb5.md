Now I have a comprehensive understanding of the paper and the reviews. Let me construct the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper introduces Range Regularization (R²), a family of training-time regularizers—L∞, margin, and soft-min-max—that penalize weight outliers to produce models more amenable to downstream quantization and compression. Experiments across PTQ, QAT (EWGS, LSQ), and DKM-based compression on MobileNet-V1/V2, ResNet-18, and MobileBERT show consistent improvements, particularly at very low bit-widths (1–2 bits).

## Strengths
- **Large and practically meaningful gains at extreme compression levels.** Table 5 shows that at 1-bit DKM scalar palettization (32× compression), R² raises MobileNet-V1 top-1 accuracy from 21.72% (no R²) to 51.92% (R_Linf), a 30 percentage-point absolute gain. This is a striking demonstration that outlier removal during training dramatically improves the usability of extreme compression.
- **Consistent 2-bit QAT improvements when all layers are quantized.** Table 3 reports that with EWGS 2-bit quantization including first and last layers, MobileNet-V1 rises from 55.96% (no R²) to 60.30% (R_Linf), and MobileNet-V2 from 59.44% to 62.25%. Table 1 shows that quantizing all layers without R² drops accuracy by ~3% relative to excluding first/last layers, while R² nearly closes this gap—directly supporting the paper's motivation about first/last layer outliers.
- **The paper tests three R² variants and analyzes their trade-offs.** L∞ and margin regularizers handle symmetric quantization well; soft-min-max is explicitly designed for asymmetric compression (vector DKM, Table 6). The paper acknowledges that soft-min-max is weaker for symmetric quantization, showing intellectual honesty.
- **R² extends beyond image classification to NLP.** Table 7 shows MobileBERT on QNLI with DKM compression: 1-bit accuracy improves from 79.90% to 82.53% (R_Linf), and 2-bit from 83.53% to 84.78%, demonstrating cross-domain applicability.
- **Figure 2 provides visual evidence linking the mechanism to the effect.** The weight distribution plots show that L2 and heavy L2 retain outliers (red dots), while L∞ and margin regularizers remove them, directly supporting the paper's core claim.

## Weaknesses

### Fatal
None.

### Major
- **Confounded ResNet-18 baseline (Tables 4, 5, 6).** The paper uses a torchvision pre-trained ResNet-18 as the "w/o R²" baseline (line 111, Table 4 caption), while R² models are trained from scratch with the authors' own hyperparameters. The FP accuracy difference (69.76% vs. 71.29% for R_Linf) alone accounts for ~1.5 percentage points of the gap. This means the reported QAT and DKM improvements for ResNet-18 partially reflect different training setups, not just the regularizer. For MobileNet-V1 the baseline is properly controlled (trained from scratch by authors), so this issue is limited to ResNet-18 experiments but affects multiple tables.

- **PTQ "None" baseline is underspecified and potentially unreliable for MobileNet-V1.** The paper defines "None" only as "quantizing without any advanced PTQ techniques" (Table 2 caption) without specifying the quantization scheme (symmetric/asymmetric, per-tensor/per-channel, scale/zero-point determination, calibration data). The dramatic drop to what appears to be near-random accuracy for L2-trained MobileNet-V1 (0.13% per the critic's reading) is not explained or sanity-checked. While the paper's narrative (L2 doesn't remove outliers → naive quantization fails) makes this directionally plausible, the extreme magnitude warrants a per-layer range analysis or SQNR measurement to confirm the mechanism rather than a potential implementation bug. Note that even if this one column value is questionable, the R² models' strong PTQ performance (including with AdaRound/DFQ and across MobileNet-V2) still supports the overall thesis; this does not invalidate the paper's core claims.

- **Missing ablation on the regularization strength λ.** All experiments use a fixed λ=0.01 for R² (line 110). A sweep showing sensitivity to λ would strengthen the practical guidance and demonstrate robustness.

### Minor
- **The claim of "invariance" to the quantization/compression algorithm is overstated.** The paper tests R² with several methods (EWGS, LSQ, DKM, DFQ, AdaRound) but not diverse quantizers (e.g., different rounding schemes, integer-only hardware backends, mixed-precision search). A softer claim like "effective across multiple SOTA methods" would be more precise.

- **Variance is not reported for any experiment.** For small-margin results (e.g., Table 5 where some R² gains are within 0.5%), it is unclear whether improvements are statistically significant. This is particularly relevant for 2-bit QAT experiments where run-to-run variance is known to be high.

- **The soft-min-max regularization is motivated for asymmetric compression but only weakly validated.** Table 6 shows soft-min-max achieves 54.49% vs. 55.06% for R_Linf on vector DKM—it underperforms the symmetric R² variant even on the task it was designed for. The paper acknowledges this but provides no direct ablation isolating the benefit of the asymmetric formulation.

### Trivial
None.

## Nice-to-Haves
- Provide per-layer weight range statistics (max|W|, 99.9th percentile) before and after R² to quantify the "outlier removal" mechanism numerically, complementing Figure 2.
- Specify the PTQ "None" scheme in detail (symmetric vs. asymmetric, per-tensor vs. per-channel, calibration procedure) for reproducibility.
- Add error bars or confidence intervals for the key low-bit results and DKM compression results.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *Compression ratio attribution (critic's note about 16×/32× being from DKM, not R²).* The paper's phrasing ("coupled with...compression techniques, models trained with R² perform better...at lower bit weights with 16x compression ratio") clearly attributes the compression ratio to the downstream method. This is not an error.
- *Missing related works.* Per policy, the reviewer cannot verify gaps in related work without external sourcing.
- *Criticism about "not yet released" or unverifiable models/datasets.* All cited references are assumed to exist.
- *Formatting nitpicks and typos.* These are parser artifacts, not author errors.
- *The critic's characterization that BOTH L2 and KURE baselines have ~0.13% in Table 2.* The paper's text (line 137) explicitly states "KURE...is more effective than L2 norm" for PTQ, which contradicts the claim that both perform equally poorly. Without access to the image, this specific claim cannot be verified and conflicts with the paper's own description.
- *Speculative fatal framing about the MobileNet-V1 PTQ baseline.* The critic argues this could "invalidate all MobileNet-V1 PTQ comparisons," but (a) the R² models perform well across multiple downstream methods beyond PTQ (EWGS, DKM, AdaRound), and (b) MobileNet-V2 PTQ results are not suspect. The evidence does not support a fatal judgment.

## Novel Insights
None beyond the paper's own contributions. The reviews raised useful experimental-concern points but did not introduce a novel scientific insight that the paper itself was missing.

## Suggestions
1. **Re-run the ResNet-18 baselines** by training a no-R² ResNet-18 from scratch with identical hyperparameters (same as was done for MobileNet-V1) to eliminate the torchvision training confound.
2. **Add a PTQ sanity-check appendix** showing per-layer weight ranges, quantization parameters, and activation SQNR for the "None" PTQ baseline on MobileNet-V1, explaining why the L2 baseline drops so sharply.
3. **Run a λ sweep** (e.g., λ ∈ {0.001, 0.005, 0.01, 0.05}) for at least one experimental setting to show robustness and provide practical guidance.
4. **Report standard deviations** for the key low-bit QAT (Table 3, 2-bit) and DKM (Table 5, 1-bit) results, especially where margins are narrow.

## Score and Decision
The paper proposes a simple, well-motivated idea and validates it across multiple model families, quantization methods, and even a language task. The core results at 1–2 bit quantization are compelling, and the manuscript is clearly written. The main weaknesses—the confounded ResNet-18 baseline and underspecified PTQ "None" method—are addressable and do not fatally undermine the contribution, since the strongest results (MobileNet-V1/V2 EWGS QAT, DKM compression) rely on properly controlled baselines. The paper would be strengthened substantially by addressing these concerns, but in its current form it already makes a solid empirical contribution.

**Score:** 6.0

**Decision:** Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>