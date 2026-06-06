Now I have enough data for calibration. Let me synthesize my findings.

**Comparison with anchors:**

- **Highlight Diffusion (3.00)**: Only 1.52× speedup, limited experiments, weak writing. PKA is significantly stronger — much larger speedups, better experiments, clearer writing.
- **DyDiT (5.50)**: 1.73× speedup, 51% FLOPs reduction, competitive FID, thorough ablations. PKA has more dramatic efficiency gains (10×) and better quality metrics, but weaker ablation rigor (qualitative only). Similar overall level.
- **PT-DiT (6.40)**: 49% FLOPs reduction, competitive across multiple tasks. Broader scope (T2I/T2V/T2MV). PKA has stronger efficiency numbers but narrower scope and comparable evaluation concerns.
- **LEGO (6.67)**: Competitive FID, good ablations, broader exploration. Better evaluation rigor than PKA.
- **LinFusion (6.25)**: Linear attention replacement, strong generalization across models. More thorough evaluation.

**Round 1 bracket**: 5.0–7.0
**Round 2 bracket**: 5.0–6.5

PKA sits around DyDiT (5.50) — it has stronger efficiency numbers and good quality metrics, but the qualitative-only ablations, mischaracterized F1 regression, no error bars, and ambiguous baseline treatment pull it down from higher anchors like PT-DiT (6.40) and LEGO (6.67). I'll score it at **5.5**.

---

## Summary
This paper proposes Patch-wise and Keyword-Aware Attention (PKA), an efficient attention framework for multi-condition control in Diffusion Transformers that decomposes the expensive "concatenate-and-attend" paradigm into Position-Aligned Attention (PAA) for spatial conditions, Keyword-Scoped Attention (KSA) for subject-driven conditions, a condition KV cache, and an early-timestep sampling strategy. Built on FLUX.1, PKA demonstrates up to 10× inference speedup and 5.12× VRAM reduction at high condition counts while maintaining competitive generation quality on most metrics.

## Strengths
- **Substantial, scaling efficiency gains with quantitative evidence**: Figures 7 and 8 demonstrate speedups from 3.90× to 10× and VRAM reductions from 2.46× to 5.12× that scale favorably with condition count, measured against OminiControl2 and UniCombine on a single NVIDIA RTX 6000 Ada GPU. These are among the strongest efficiency numbers in the retrieval corpus for DiT efficiency papers.
- **Strong generation quality on most metrics**: Table 1 shows the method achieves the best FID (52.99 vs. 61.03 on Subject-Canny), SSIM (0.553 vs. 0.493), and best CLIP-I/DINOv2 across all subject consistency tasks, demonstrating the efficiency gains do not broadly sacrifice output quality.
- **Clean architectural insight via condition cache**: Having condition tokens (SP, SJ) only self-attend enables their K/V projections to be computed once and cached across denoising steps (Section 3.2, Figure 4a), providing a complementary efficiency gain orthogonal to the per-step attention reductions.
- **Perturbation analysis motivating early-timestep sampling**: Figure 5 provides clear empirical evidence that visual conditions exert strongest influence during early denoising stages, with SSIM dropping sharply from 0.50 to 0.42 within 3 steps when perturbing high-to-low, while remaining at 0.50 for low-to-high perturbation.

## Weaknesses

### Fatal
None.

### Major
- **Subject-Canny F1 controllability regression is substantial and mischaracterized**: In Table 1, the Subject-Canny F1 score is 0.414 for PKA vs. 0.551 for UniCombine — a 25% relative decrease and the single largest gap in any controllability metric across all tasks. The paper describes this as "the minor exception of a narrow margin" (Section 4.2.3). Since spatial controllability via edge maps is a core claim, this regression warrants honest analysis rather than dismissal.

- **All ablations are purely qualitative — no quantitative metrics for any ablation configuration**: Figures 9, 10, and 11 compare PAA vs. SWA vs. full attention, KSA at different ε values, and early-timestep sampling at different μ/δ — but all comparisons are visual-only with only latency and VRAM numbers. For an efficiency paper claiming to maintain quality, quantitative ablation metrics (FID, F1, MSE) are essential. This is especially important for PAA vs. SWA, where the efficiency difference is marginal (13.63s/237MB vs. 14.00s/276MB for SWA window 1) and quality differences cannot be verified from images alone.

- **Ambiguous baseline training procedure**: Section 4.1 states "To ensure a fair comparison, we fine-tune the FLUX.1 model using LoRA" but does not clarify whether the baselines (OminiControl2, UniCombine) were re-implemented with the same LoRA fine-tuning protocol or use their original published models. This ambiguity undermines the fairness of the comparison — either the baselines may be under-optimized or the comparison is not controlled for training.

### Minor
- **Motivating attention analysis relies on single visualizations**: Figures 2 and 3 each present one example to establish that spatial attention is diagonal and subject attention is keyword-correlated. While visually compelling, attention patterns vary across layers, timesteps, and inputs. A systematic analysis (e.g., fraction of attention mass on diagonal across many images) would strengthen the motivation.

- **Headline 10× speedup comes from a synthetic stress test**: The 10× speedup and 5.12× VRAM reduction are measured at 16 conditions with 1024 tokens each (Section 4.2.1), while the quality evaluation in Table 1 uses 2 conditions. Reporting speedup at the 2-condition setting would give readers a more practical picture.

- **No error bars, evaluation set size, or significance testing**: Every number in Table 1 is a single point estimate with no specification of test set size or variance. For a paper whose core claim is "maintaining or improving quality," knowing whether metric differences are statistically meaningful is important.

- **PAA design is stricter than the paper's own observation**: Section 1 states "only spatially aligned *or adjacent* patches interact meaningfully," yet PAA (Eq. 2) enforces strictly one-to-one attention, discarding adjacent-patch interaction entirely. The ablation shows marginal efficiency differences between PAA and SWA with window 1, raising the question of whether this stronger restriction is justified.

### Trivial
None.

## Nice-to-Haves
- Report speedup and VRAM reduction at 2 conditions to match the quality evaluation setup.
- Add a limitations discussion acknowledging the F1 regression, restriction to FLUX.1, and keyword extraction dependency.
- Quantitative sensitivity analysis of the KSA mask threshold ε.
- Systematic attention analysis across multiple images and layers.

## Removed Points
These points are flagged to be removed, treat them with caution.
- "Missing related works" — cannot verify external references exist.
- Formatting/style nitpicks — parser artifacts, not author errors.

## Novel Insights
The paper's most novel contribution is the observation that multi-condition attention in DiTs has condition-type-specific structure (diagonal for spatial, sparse keyword-correlated for subject) that can be exploited with purpose-built modules rather than generic sparsification. The condition cache — enabled by making condition tokens self-attend-only — is an elegant design providing free efficiency gains. The perturbation analysis revealing that visual conditions matter disproportionately at early denoising stages (Figure 5) is a useful finding for the broader DiT fine-tuning community.

## Suggestions
1. Add quantitative metrics (FID, F1, MSE, CLIP scores) for each ablation configuration to verify quality is maintained.
2. Provide systematic analysis of attention patterns (statistics across many images/layers) to justify the architectural simplifications.
3. Report efficiency metrics at 2 conditions to match the quality evaluation setup.
4. Honestly discuss the Subject-Canny F1 regression and its likely cause.
5. Clarify whether baselines were re-trained under the same protocol or used original published results.

## Calibration Report

**All anchors retrieved:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 2o58Mbqkd2.md | 3.25 | 1 | Combining pre-trained diffusion models — different scope, weaker results |
| Jt1gGIumJo.md | 3.00 | 1 | Training-free attention acceleration, 1.52× speedup — much weaker than PKA |
| AjunxrcKa2.md | 3.40 | 1 | Conditional LoRA parameter generation — different topic |
| rnTb9dm9zx.md | 3.00 | 1 | Patch parallelism for diffusion — limited experiments, similar weakness profile |
| w6YS9A78fq.md | 5.00 | 1 | Unified video/3D/game generation — different scope |
| wiYV0KDAE6.md | 5.75 | 1 | Diffusion for tabular data — different domain |
| qmXedvwrT1.md | 6.67 | 1 | LEGO bricks for efficient diffusion — better ablations, similar quality trade-offs |
| lTrrnNdkOX.md | 6.40 | 1 | PT-DiT proxy-tokenized DiT — similar efficiency focus, broader scope |
| gU58d5QeGv.md | 8.00 | 1 | Würstchen efficient T2I — much stronger, different approach |
| fV0t65OBUu.md | 8.00 | 1 | Optimal covariance matching — different topic, theoretical |
| SI2hI0frk6.md | 7.60 | 1 | Transfusion multi-modal model — different scope, stronger |
| OvoCm1gGhN.md | 8.00 | 1 | Differential Transformer — foundational work, much stronger |
| taHwqSrbrb.md | 5.50 | 2 | DyDiT dynamic DiT — 1.73× speedup, thorough ablations, similar tier |
| leBbjaUxut.md | 5.00 | 2 | Multi-scale DiT — training speedup, mixed reviews |
| T1MTmAlF7x.md | 5.00 | 2 | EDM2+ efficient architecture — design exploration |
| wGVOxplEbf.md | 6.20 | 2 | SaRA sparse low-rank adaptation — good ablations |
| D2as3jDmRA.md | 6.25 | 2 | LinFusion linear attention — thorough evaluation across models |
| UmMa3UNDAz.md | 6.50 | 2 | EfficientDM quantization — comprehensive experiments |

**Round 1 bracket**: 5.0–7.0
**Round 2 bracket**: 5.0–6.5

**Final positioning**: PKA sits at the level of DyDiT (5.50) — it has more dramatic efficiency gains (10× vs. 1.73×) and strong quality metrics, but the qualitative-only ablations, mischaracterized F1 regression, no error bars, and ambiguous baseline treatment pull it below PT-DiT (6.40), LinFusion (6.25), and LEGO (6.67), which have more rigorous evaluation. The paper is clearly above the 3.0–3.5 anchors which had limited experiments and modest speedups.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>