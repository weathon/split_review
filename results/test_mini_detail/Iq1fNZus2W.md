Now let me compose the final review.

## Summary

This paper addresses the computational bottleneck of multi-condition control in Diffusion Transformers, where the standard "concatenate-and-attend" mechanism scales quadratically with the number of conditions. The authors propose Patch-Wise and Keyword-Aware Attention (PKA), decomposing full attention into two specialized modules: Position-Aligned Attention (PAA) for spatial conditions (one-to-one attention between aligned patches), and Keyword-Scoped Attention (KSA) for subject conditions (attention confined to keyword-activated regions). An early-timestep sampling strategy is also introduced to accelerate fine-tuning. Experiments on FLUX.1 show up to 10× inference speedup and 5.12× VRAM reduction for the attention module, with generally competitive or better generative quality metrics.

## Strengths

- **Impressive efficiency gains with clear evidence.** Figure 7 demonstrates a 10× inference speedup over UniCombine at 16 conditions, and Figure 8 shows a 5.12× attention-module VRAM reduction. These speedups are explicitly labeled (3.90× at 4 conditions, 6.46× at 8, 10× at 16) and the trend is consistent. This is the paper's strongest contribution.

- **Quantitative evidence that efficiency does not broadly degrade quality.** Table 1 shows PKA achieves the best FID (e.g., 52.99 vs. 61.03/72.03 on Subject-Canny), best SSIM (0.553 vs. 0.493/0.406), best CLIP-I (0.945 vs. 0.912/0.878), and best DINOv2 (0.926 vs. 0.901/0.867) across all tasks. Subject consistency and generative quality are consistently improved or competitive.

- **Empirical attention-pattern analysis directly motivates the architectural design.** Figures 2 and 3 provide concrete evidence: attention matrices for spatial conditions are diagonally concentrated, and subject-condition attention is localized. This grounding distinguishes the work from purely heuristic efficiency proposals and makes the design of PAA and KSA principled.

- **Thorough ablation of both modules.** Figure 9 confirms PAA (13.63s, 237MB) outperforms even the most efficient sliding-window variant (14.00s, 276MB). Figure 10 validates KSA's tunable ε threshold, showing smooth trade-offs between efficiency and subject fidelity — an informative analysis.

- **Perturbation analysis motivating early-timestep sampling.** Figure 5 demonstrates that perturbing spatial conditions early in denoising causes a larger SSIM drop than perturbing late, providing empirical grounding for the shifted-sampling strategy.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The Subject-Canny F1 drop is understated.** On the Subject-Canny task, PKA achieves F1=0.414 versus UniCombine's 0.551 — a 25% relative drop in edge controllability. The paper describes this as "a minor exception" and "a narrow margin," which minimizes a non-trivial trade-off. Critically, on the Canny-Depth task (without a subject condition), PKA achieves the best F1 (0.411 vs. 0.369), suggesting the issue is specific to the Subject+Canny interaction. The paper offers no analysis or ablation to explain why this occurs or whether a hybrid approach could mitigate it. This does not invalidate the contribution — the paper still leads on FID, SSIM, CLIP-I, and DINOv2 on the same task — but readers should have an honest account of where and why controllability is sacrificed.

- **Baseline comparison setup is underspecified.** The paper states it "fine-tunes FLUX.1 using LoRA" but does not state whether OminiControl2 and UniCombine were also fine-tuned under the same conditions or used with their released weights. If the baselines were not fine-tuned on the same data, PKA (which was) would have an inherent advantage. The paper should clarify this, or add a controlled experiment where all methods are fine-tuned under identical training budgets.

- **Early-timestep sampling lacks quantitative validation.** The only evidence for this component is the visual comparison in Figure 11. No FID, controllability metrics, or convergence curves are provided comparing training with and without the shifted sampling. Since the final model combines PKA + early-timestep sampling, the individual contribution of the latter cannot be isolated. A simple ablation with quantitative metrics would settle this.

- **Keyword token identification is underspecified.** KSA's mask generation (Eq. 3) depends on a "keyword set 𝕂." The paper says it "typically contains just 1 to 2 tokens" and that the dataset is curated so that "each image caption contains a descriptive keyword," but it does not specify whether keyword tokens are identified automatically (e.g., by TF-IDF, attention scores from the text encoder) or provided as part of the dataset. This is necessary for reproducibility and for understanding failure modes when prompts have multiple or ambiguous subjects.

- **No limitations or failure cases are discussed.** The paper claims no limitations of its own method (e.g., when a subject occupies most of the image frame, making KSA masks cover everything; or when spatial conditions are poorly aligned). Adding a limitations paragraph would strengthen credibility.

- **No confidence intervals or statistical significance reported.** Table 1 reports point estimates without variance, making it impossible to assess whether differences between methods are significant.

### Trivial

- The latency numbers in Figure 9's table show PAA (13.63s) versus "SWA, 1" (14.00s) — the one-to-one design is genuinely faster, but the "swa condition" column in the table header could be confusing. Minor table readability issue.

- The paper states "w/o KSA [is] equivalent to ε=0" (line 306). This is accurate (no masking = every position passes), but the phrasing could be clarified to avoid confusion.

## Nice-to-Haves

- Reporting total VRAM consumption (including weights and activations), not just attention-module VRAM, would give a more complete practical efficiency picture.
- A discussion of when KSA's temporal consistency assumption (reusing masks from t to t+1) might break, e.g., at very early timesteps when the mask is noisy.
- Extrapolation of the efficiency measurements to practical use cases (2–4 conditions at higher resolutions) rather than the 1024-token-per-condition setup used in Figures 7–8.

## Removed Points

These points from the inputs were removed with justification:

- *"Condition cache is a standard engineering practice, not a novelty."* — KV caching is standard in LLMs, but applying it to condition tokens in multi-condition DiTs is a reasonable engineering contribution within the paper's scope. The paper does not overclaim this as a core novelty.

- *"w/o KSA equivalent to ε=0 is inaccurate."* — The reviewer claimed this was inaccurate, but it is in fact accurate: without KSA masking, all positions pass, which is equivalent to a threshold of zero. The paper's statement is correct.

- *"Temporal consistency assumption breakage at early steps."* — This is a speculative concern about when a cited assumption might break, not a demonstrated flaw in the paper.

- *"SWA condition column mislabeled" / confusion about latency ordering.* — The paper's numbers (PAA 13.63s faster than SWA-1 14.00s) are correct; the labeling is functional. Minor table readability issue moved to Trivial.

- *Pure formatting/style nitpicks* from the harsh critic were removed per policy.

## Novel Insights

The harsh critic and strength finder largely converge on the paper's core narrative but diverge on the severity of the Subject-Canny F1 issue. The interesting synthesis is that the paper's own data reveals a meaningful condition-type interaction: PAA (one-to-one aligned attention) works well for spatial conditions in isolation but may compete for bandwidth when a subject condition is simultaneously present, causing the observed F1 degradation. This suggests that PAA's strict one-to-one alignment may be too rigid when the model must jointly satisfy edge constraints and subject appearance constraints in the same spatial region. Neither reviewer identified this specific mechanism, but it is the most natural explanation for why PKA excels on Canny-Depth (no subject) but lags on Subject-Canny. This observation could guide a future hybrid that uses a small window (not just one token) around the aligned position in multi-condition settings.

## Suggestions

1. Add an ablation comparing PKA trained with vs. without the early-timestep sampling, reporting both efficiency and quality metrics — this would cleanly isolate the sampling contribution.
2. Analyze the Subject-Canny F1 drop: provide or discuss whether PAA's rigid one-to-one alignment is the cause, and whether a small neighborhood window would recover the gap.
3. State explicitly whether OminiControl2 and UniCombine were also fine-tuned with LoRA on the same dataset, or used off-the-shelf.
4. Clarify how keyword tokens are identified for KSA (automatic method or manual specification) and discuss robustness to prompts with multiple candidate subjects.
5. Add a limitations paragraph acknowledging cases where PKA may falter (large subjects, misaligned spatial conditions).

## Score and Decision

**Calibration Anchors (all rounds):**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|-----------|
| PT-T2I/V | lTrrnNdkOX.md | 6.40 (Accept Poster) | R1/R2 | Closest comparable — also proposes efficient attention for DiTs. PKA has stronger efficiency metrics (10× vs 59% reduction) but weaker analysis of one degradation case. Slightly below this anchor. |
| Multi-Scale DiT | leBbjaUxut.md | 5.00 (Reject) | R1/R2 | Contested paper (scores 8,6,3,3). Had novelty overclaim and missing ablation issues. PKA is clearly stronger — cleaner contribution, better experimental support. |
| LinFusion | D2as3jDmRA.md | 6.25 (Reject) | R2 | Also about efficient attention for diffusion. Rejected despite good scores. PKA's contribution is more focused and clearly scoped; fewer experimental gaps. Comparable quality. |
| CatVTON | jt1h2dnmng.md | 6.25 (Accept Poster) | R2 | Efficient architecture for a specific application (virtual try-on). Different domain but similar methodology level. PKA is comparable in rigor and contribution. |
| APCtrl | yPxhj1FKhG.md | 3.67 (Reject) | R1 | Conditional control for diffusion. Had serious soundness and novelty concerns. PKA is substantially stronger. |
| Diffusion w/o Attention | qWtz3dOmML.md | 3.00 (Reject) | R1 | Replaced attention entirely. PKA is much stronger empirically and methodologically. |
| ELR-Diffusion | edx7LTufJF.md | 2.50 (Withdrawn/Reject) | R1 | Low-rank training approach. PKA is far stronger. |

**Round 1 bracket:** 4.5 – 7.0  
**Final determination:** The paper sits between PT-T2I/V (6.4, accepted) and the 5.0-level rejected papers. It has a clearer empirical motivation than PT-T2I/V but slightly weaker analysis of one critical failure mode. The efficiency results are the paper's strongest asset and are convincingly demonstrated. The quality-maintenance claim is generally supported but nuanced by the Subject-Canny trade-off.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>