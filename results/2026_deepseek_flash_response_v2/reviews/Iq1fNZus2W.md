## Summary

The paper addresses the computational bottleneck of "concatenate-and-attend" in multi-condition Diffusion Transformers (DiTs). It proposes PKA, which decomposes full attention into Position-Aligned Attention (PAA) for spatial conditions and Keyword-Scoped Attention (KSA) for subject-driven conditions, plus a condition KV cache and an early-timestep training sampler. On FLUX.1, the method achieves up to 10× speedup and 5.12× VRAM reduction relative to the UniCombine baseline at 16 conditions.

## Strengths

1. **Empirical diagnosis of attention redundancy grounds the architectural design.** Figures 2–3 directly visualize that spatial-condition attention is concentrated along the diagonal and subject-condition attention activates only keyword-relevant regions. This evidence justifies PAA and KSA as principled sparsity exploitation rather than ad-hoc pruning.

2. **Efficiency scaling is validated quantitatively across a range of condition counts.** Figures 7–8 show measured latency and VRAM from 1 to 16 conditions, with speedups of 3.90×–10× and VRAM reductions of 2.46×–5.12× against UniCombine. The full efficiency curve is presented, not just the endpoint.

3. **KSA threshold ablation (Figure 10) demonstrates a tunable efficiency-quality trade-off.** Sweeping ε from 0.2 to 0.8 shows a graceful degradation in subject fidelity with corresponding VRAM savings (368MB → 230MB), allowing users to choose their operating point.

4. **PAA is compared against sliding-window attention at multiple window sizes (Figure 9).** PAA (13.63s, 237MB) outperforms the best SWA variant (14.00s, 276MB) on both latency and VRAM while matching generative quality, validating the one-to-one alignment strategy over even localized window-based alternatives.

## Weaknesses

### Fatal
None.

### Major

1. **F1 controllability degradation on Subject-Canny is downplayed as a "narrow margin."** In Table 1, UniCombine achieves F1 = 0.551 while PKA achieves F1 = 0.414 on the Subject-Canny task — a ~25% relative drop. The paper describes this as "the minor exception of a narrow margin on the Subject-Canny task" (Section 4.2.3). This characterization is inaccurate. A drop from 0.551 to 0.414 means the method captures substantially fewer edge pixels correctly. This directly undercuts the claim (in the abstract and conclusion) that quality is "maintained or improved" relative to baselines. The paper should acknowledge this trade-off honestly and discuss the conditions under which it is acceptable.

2. **The Condition Cache mechanism is never ablated separately from PAA and KSA.** The KV cache for condition tokens (Section 3.2) is described as a key design principle — condition tokens only self-attend within their own type, so their K/V projections are computed once at step 1 and cached for all subsequent steps. This likely contributes substantially to both speedup and VRAM savings. Yet none of the ablations (Figures 9–10) separate the cache's contribution from PAA's or KSA's. The reader cannot tell how much of the reported gain comes from the novel attention patterns versus the caching — an engineering optimization that could, in principle, be applied to other multi-condition methods. A clean ablation (full attention without cache, full attention with cache, PAA without cache, PAA with cache) is needed to attribute gains.

### Minor

3. **Headline efficiency numbers (10×, 5.12×) are achieved at 16 conditions — an extreme setting.** The abstract, introduction, and conclusion state "up to a 10× inference speedup" and "5.12× VRAM reduction" without specifying the condition count. While "up to" is a standard qualifier and the full efficiency curve is shown in Figure 7, practical multi-condition scenarios (2–4 conditions) yield more modest gains (~1.2×–3.9× speedup). The paper would benefit from explicitly contextualizing the condition count alongside headline claims.

4. **Early-timestep sampling lacks quantitative validation.** Section 4.3.3 presents only qualitative image comparisons (Figure 11) for different (μ, δ) settings. The claim that this strategy "accelerates convergence and enhances the final model's control fidelity" is unsupported — no FID, CLIP, or controllability metrics are reported. This component reads as an interesting observation that was not experimentally validated.

5. **No statistical uncertainty is reported for any quantitative result.** All results (Table 1, latency/VRAM in Figures 9–10) are point estimates without standard deviations, confidence intervals, or error bars. Given that CLIP-T scores are tightly clustered (0.325–0.354 across all methods and tasks), it is unclear which differences are meaningful.

6. **Some ablation comparisons are opaque.** In Figure 9, "swa condition" (13.58s, 198MB) achieves lower latency and VRAM than PAA (13.63s, 237MB), but the paper does not explain what "swa condition" is or why PAA is preferred despite being less efficient on both metrics. This needs clarification.

7. **High FID values (52.99–80.20) are not discussed.** These are very high by standard FID conventions. The paper should explain whether this stems from the Subject200K subset characteristics, the evaluation protocol, or other factors.

8. **PAA's one-to-one assumption and failure cases are not examined.** The paper does not discuss when spatially localized attention might miss long-range dependencies (e.g., pose skeletons, layout conditions with non-local object relationships).

### Trivial
None.

## Nice-to-Haves

- Ablate the condition cache separately from PAA and KSA.
- Add quantitative evaluation (FID/CLIP/controllability metrics) for the early-timestep sampling strategy.
- Report standard deviations or error bars for main results.
- Include a limitations section discussing when PAA's one-to-one assumption might fail or when the condition cache could degrade quality.

## Removed Points

These points were raised by the harsh critic but are removed per filtering rules:

- *"FID ambiguity about paired vs. standard"* — Speculative; the paper describes "FID between the generated and ground-truth image sets" which is standard FID.
- *"Qualitative Figure 6 claims are subjective/marketing"* — This is a standard qualitative comparison; the textual description is the authors' interpretation, which is normal practice in the field.
- *"The 'w/o subject' row in Figure 10 is a degenerate baseline"* — Technically correct but trivial: removing a condition entirely and measuring lower cost is expected and not presented as evidence for anything other than the baseline comparison.
- *"Condition tokens' frozen representations could degrade quality"* — Valid as a question but speculative without evidence; the paper's reported results do not show such degradation.
- *"Missing appendix / appendix proofs"* — Parser artifact; these exist in the original submission.
- *"Formatting/style nitpicks"* — Parser artifacts, not author errors.
- *"PAA has window size effectively 0 — no neighbors"* — Inaccurate; the paper's empirical analysis (Figure 2) demonstrates attention IS concentrated on the diagonal, justifying one-to-one alignment.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's strengths (empirical attention analysis, modular design, efficiency scaling) and weaknesses (F1 downplaying, missing cache ablation, presentation gaps). No cross-review synthesis reveals a novel angle not present in the paper itself.

## Suggestions

1. **Honestly acknowledge the F1 trade-off.** Add a sentence in the abstract, results, and conclusion noting that on Subject-Canny, edge-control fidelity (F1) is lower than UniCombine, while other metrics (FID, SSIM, CLIP-I) improve. Remove the "narrow margin" characterization.
2. **Add a Condition Cache ablation.** Evaluate: full attention without cache, full attention with cache, PAA without cache, PAA with cache — to attribute efficiency gains to each component.
3. **Quantify the early-timestep sampling benefit.** Report FID, CLIP, and controllability metrics at convergence for standard vs. proposed sampling.
4. **Contextualize efficiency at practical condition counts.** Show speedup factors at 2–4 conditions alongside the 16-condition extremes.
5. **Add error bars / standard deviations** for main quantitative results, or justify why they are not needed for the specific metrics.

---

### Calibration Anchors

**Round 1 (Bracketing):**
| Path | Avg Score | Comparison |
|------|-----------|------------|
| Highlight Diffusion (`Jt1gGIumJo`) | 3.00 | Much weaker — 1.52× speedup only, tested on SD1.4, very limited experiments |
| LinFusion (`D2as3jDmRA`) | 6.25 | Stronger experiments overall; our paper's multi-condition focus is more specific |
| UniCon (`uJqKf24HGN`) | 7.00 | Stronger — cleaner evaluation, fewer presentation gaps |
| LEGO bricks (`qmXedvwrT1`) | 6.67 | Stronger — more thorough evaluation and ablation |

**Round 2 (Narrowing):**
| Path | Avg Score | Comparison |
|------|-----------|------------|
| Sparse-to-Sparse Training (`vNZIePda08`) | 4.75 | Weaker — limited novelty; our paper has clearer contributions |
| DyDiT (`taHwqSrbrb`) | 5.50 | Slightly stronger — cleaner ablation studies despite similar scope; our paper has stronger efficiency claims but more presentation gaps |
| PT-DiT / Qihoo-T2X (`lTrrnNdkOX`) | 6.40 | Stronger — similar insight (attention redundancy in DiTs) but cleaner execution across more tasks |
| On Inductive Biases (`lWGXftRS5h`) | 5.00 | Comparable score; topically less similar (generalization analysis rather than efficiency method) |
| Ctrl-Adapter (`ny8T8OuNHe`) | 7.00 | Stronger — cleaner evaluation, more thorough |

**Round 1 bracket**: 4.0 – 6.5  
**Round 2 narrowing**: The paper is weaker than DyDiT (5.50, Accept) due to the F1 downplaying and missing cache ablation, but stronger than Sparse-to-Sparse (4.75, Reject) due to clear novelty. Positioned between these anchors.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>