Now I have verified all claims. Let me produce the final consolidated review.

## Summary

This paper introduces FIPS, a method that compresses vision transformer MLP modules by combining **parameter sharing** (a shared basis **U** across layers, initialized via SVD) with **sparse projection factors** **V** (optimized via gradual magnitude pruning). The key insight is that sparsity in the projection matrix is necessary for this parameter-sharing approach to be effective. Experiments on DeiT-B and Swin-L show FIPS reduces MLP parameters to 25–40% while keeping accuracy competitive with the original, and outperforming prior block-level reconstruction (AAFM) and distillation-based (GFM) compression methods — often using only a fast calibration stage (<1 hour on a single GPU).

## Strengths

1. **Superior compression accuracy over strong baselines.** At 40% parameter budget on DeiT-B, FIPS achieves 81.69% top-1 accuracy, outperforming AAFM (80.33%) and GFM (81.28%) as shown in Table 1. These baselines are themselves well-established, and FIPS beats them despite GFM requiring more expensive end-to-end fine-tuning. The advantage holds across multiple budgets and for Swin-L.

2. **Ablation confirms SVD initialization is critical.** Figure 4a shows that replacing SVD-based initialization with random initialization causes a ~1 percentage point accuracy drop at 25% budget. This cleanly isolates the value of the SVD initialization, which goes beyond standard low-rank approximations by combining it with subsequent sparse optimization.

3. **Principled grouping strategy derived from empirical analysis.** Figure 2d shows that sharing parameters across 4 consecutive blocks yields the highest post-compression accuracy, and this aligns with the rank plateau observed in Figure 2c. This provides a data-driven guideline for grouping layers — a practical design insight that prior parameter-sharing work (e.g., ALBERT, which shares entire blocks) does not offer.

4. **Computationally efficient calibration stage.** The method requires only 3840 samples and 20 epochs of local error minimization, taking less than 1 hour on a single A6000 GPU. This efficiency means the method is practical for practitioners who lack large-scale fine-tuning budgets.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Abstract overclaim for Swin-L at 25% budget.** The abstract states that FIPS compresses to 25–40% parameter count "while maintaining accuracy within 1 percentage point of the original models." For Swin-L at 25% budget, the best result (FIPS+FT) drops from 86.24% to 85.16% — a loss of **1.08 percentage points**. The claim also does not hold for FIPS (without end-to-end fine-tuning) at 25% on DeiT-B (81.85→80.64, a drop of 1.21pp) or on Swin-L (86.24→84.78, a drop of 1.46pp). The claim should be qualified to specify which configurations satisfy the 1pp threshold (e.g., "within 1pp for most configurations, with slightly larger drops at the most aggressive 25% budget").

2. **No hardware runtime or memory measurements.** The paper discusses deployment on "resource-constrained devices" and provides theoretical storage-savings formulas, but presents zero actual measurements of inference speed, peak memory, or energy usage. The memory/latency analysis (Section 3) describes two computation strategies (low-rank and full-rank materialization) without committing to which FIPS uses, and the sparse V factors produced by GMP may have irregular sparsity patterns that are not GPU-friendly without custom kernels. For a compression paper that motivates itself through deployment, the absence of any hardware benchmark weakens the practical claims. The authors should either provide at least a simple speed/memory measurement or explicitly scope the contribution to parameter-count reduction rather than deployment speed.

3. **Transfer learning over-performance not discussed.** In Table 2, several compressed models outperform the original model (e.g., FIPS at 40% achieves 91.24% vs. original 90.99% on CIFAR-100; FIPS at 40% achieves 98.14% vs. original 97.77% on Flowers102). The paper does not discuss whether this reflects genuine regularization from compression, differences in finetuning setups (the original results are cited from the DeiT paper, not rerun under identical conditions), or another factor. Since these results could be misinterpreted as "compression improves accuracy," a brief discussion of the likely cause is warranted.

4. **Absence of statistical significance reporting.** No error bars or repeated runs are reported. For small accuracy differences (e.g., 0.2–0.5pp between methods), single-run results leave open the question of whether the gaps are meaningful. This is standard practice in much of the transformer compression literature, but acknowledgment would strengthen the paper.

### Trivial

- The memory/latency analysis discusses two computation strategies (low-rank path vs. full-rank materialization) without stating which one FIPS actually uses or which is recommended for which deployment scenario.

## Nice-to-Haves

- **A more controlled ablation isolating the sharing component.** The paper compares FIPS (with sharing) against AAFM/GFM (without sharing) and beats them. This is a valid comparison. However, a cleaner surgical ablation — applying FIPS's exact SVD+sparsity recipe to each layer independently (no shared **U**, separate **U** per layer) under the same total parameter budget — would directly measure the marginal benefit of parameter sharing versus the sparsity and reconstruction fine-tuning. The existing global-vs-local pruning ablation (Fig. 4a) still shares **U**; a truly independent baseline would not. This would strengthen the paper's central narrative.

- **A discussion of whether the irregular sparsity pattern from GMP is hardware-friendly**, or whether structured sparsity patterns might be preferable for actual speedup on GPUs/edge devices.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

- **"The benefit of parameter sharing is not isolated (structural gap)"** — The harsh critic claimed the paper "never directly evaluates whether parameter sharing itself provides a benefit" and that "every ablation and baseline within the paper (AAFM, GFM, Dense, Static, RigL, GMP) also shares parameters across layers." This is factually incorrect regarding AAFM and GFM: AAFM performs per-block compression without sharing, and GFM adds distillation but still does not share parameters across layers. FIPS demonstrably outperforms both. The critic's desire for a more controlled ablation (same method with/without sharing) is a reasonable suggestion, but framing the existing comparisons as absent is inaccurate. This point has been downgraded to a Nice-to-Have.

- **"Section 2.1 — reconstruction error on individual layers does not directly transfer to the multi-layer sharing setting"** — The critic acknowledges that later results confirm the 75% sparsity choice is consistent. This is a non-issue.

- **"Section 5 — calibration size analysis uses 50% budget, trend might differ at other budgets"** — Speculative and standard practice; no evidence of a problem.

- **All generic formatting/style nitpicks and parser artifacts** — Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The two reviewers agreed on the core strengths (strong empirical results, thorough ablations, fast calibration) and on the main areas for improvement (hardware benchmarks, tighter claim precision). No genuinely novel synthesis emerged that goes beyond what the paper itself states.

## Suggestions

1. **Qualify the abstract claim** to reflect that the 1pp threshold holds for most but not all configurations (specifically, Swin-L at 25% budget and FIPS without FT at 25% on some models exceed 1pp).
2. **Add at least one hardware benchmark** — a simple measurement of inference latency or peak memory on a representative GPU for the compressed vs. original model at a few key budgets (e.g., 25%, 40%). If the sparse V factors cause slowdown despite parameter reduction, acknowledge this and frame the contribution in terms of parameter count / memory footprint reduction rather than speed.
3. **Acknowledge the transfer learning over-performance** and briefly discuss likely causes (regularization, different finetuning setups).
4. **Add an ablation without sharing** (independent SVD+sparsity per layer, same total budget) as a Nice-to-Have to directly validate the sharing component.

## Score and Decision
MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>