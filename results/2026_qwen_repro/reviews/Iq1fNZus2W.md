Now let me synthesize the final review based on my thorough reading and verification against the paper.

## Summary

This paper proposes PKA (Patch-wise and Keyword-Aware Attention), a framework for efficient multi-condition control in Diffusion Transformers (DiTs). PKA decomposes full attention into two specialized modules: Position-Aligned Attention (PAA), which enforces one-to-one correspondence between image and spatial condition tokens to reduce spatial attention complexity from O(N²) to O(N), and Keyword-Scoped Attention (KSA), which prunes subject-driven cross-attention using a relevance mask derived from text keyword embeddings. The architecture further leverages a Condition KV cache (enabled by restricting conditions to self-attention only) and an early-timestep sampling strategy that biases training toward denoising stages where visual conditions exert strongest influence. The method achieves up to 10× inference speedup and 5.12× VRAM reduction compared to full-attention baselines.

## Strengths

- **Well-motivated architectural decomposition grounded in empirical analysis of attention redundancy.** Figures 2 and 3 convincingly demonstrate that spatial-aligned attention concentrates along the diagonal and subject-driven attention activates only in keyword-relevant regions, providing strong visual evidence that full attention is largely wasted on multi-condition DiTs.

- **Structural insight that attention decomposition enables Condition KV caching.** By restricting condition tokens (spatial and subject) to self-attention only (Sec 3.2, Fig. 4b), the design enables Key and Value projections for all conditions to be computed once and cached across all denoising steps — a practical inference optimization enabled directly by the architectural choice.

- **Comprehensive empirical evaluation across multiple multi-condition tasks.** The paper evaluates on three distinct task categories (Subject-Canny, Subject-Depth, Canny-Depth) with extensive quality metrics (FID, SSIM, F1, MSE, CLIP-I, DINOv2, CLIP-T) and efficiency metrics (latency, VRAM) across varying numbers of conditions. The quality results in Table 1 show strong FID/SSIM improvements over baselines.

- **Useful ablation isolating PAA and KSA contributions.** Section 4.3 provides controlled ablation: PAA is compared against full attention and Sliding Window Attention (Fig. 9), confirming the superiority of condition-aware locality priors over generic windows. KSA threshold ablation (Fig. 10) demonstrates graceful trade-off between efficiency and quality as ε varies.

## Weaknesses

### Fatal
None.

### Major

- **Confounding of efficiency gains by KV caching vs. attention decomposition.** The claimed 10× speedup and 5.12× VRAM reduction (Sec 4.2.1, Figs 7-8) aggregate the savings from both the attention sparsity (PAA/KSA) *and* the Condition KV caching. The caching arises from the structural choice that conditions only self-attend (Sec 3.2), not from PAA/KSA themselves. The paper does not ablate the caching effect: there is no experiment showing efficiency gains when caching is disabled, nor a comparison isolating PAA/KSA savings. In the F1=0 ablation (Fig 9: "w/o PAA" row), the baseline still presumably benefits from caching, but the gap between "w/o PAA" (15.38s, 308MB) and "PAA" (13.63s, 237MB) shows that PAA alone accounts for roughly 11% latency and 23% VRAM reduction — substantially lower in relative terms than the headline 10×. The same concern applies to KSA (16.99s vs 15.33s at ε=0.2, an ~11% effect). Without isolating these components, the efficiency story is overstated.

- **Overstated quality superiority: the paper trails UniCombine on F1 controllability in at least one task.** Table 1 shows that on the Subject-Canny task, Ours achieves F1=0.414 vs UniCombine's 0.551 — a 25% gap in edge alignment, which is precisely where spatial controllability should matter most. The paper calls this a "minor exception" (Sec 4.2.3), but a quarter-point F1 gap in spatial controllability is not minor. The paper does not explain this degradation, and the PAA's strict one-to-one design may be the cause (edges benefit from cross-patch context that PAA explicitly prunes). Claiming "state-of-the-art" generative quality while underperforming baselines on key controllability metrics is inconsistent.

### Minor

- **PAA's rigid spatial alignment requirement limits practical applicability.** PAA (Eq. 2) computes attention strictly between an image token at index *i* and a spatial condition token at index *i*. The paper does not describe how mismatched resolutions, aspect ratios, or cropping are handled in preprocessing. In real multi-condition workflows where conditions arrive at different scales or with different crops, this 1-to-1 mapping may not be directly applicable. The evaluation appears to use conditionally constrained (perfectly aligned) conditions without acknowledging this constraint.

- **KSA mask reuse may cause boundary drift.** The KSA binary mask Mᵗ is computed at timestep t and reused at t+1 and beyond (Sec 3.2.2). As the denoising process refines subject appearance, newly visible regions or shifting boundaries may not be captured by the static mask. The paper does not discuss this potential drift or analyze its impact on generation quality for subjects that evolve significantly during the denoising trajectory.

- **Ablation studies report only latency/VRAM, not quality metrics.** The PAA (Fig 9) and KSA (Fig 10) ablations show qualitative images and efficiency numbers but no standard quality metrics (FID, SSIM, CLIP-I). While the qualitative outputs appear reasonable, it is impossible to confirm whether the aggressive pruning does not silently degrade quality on these controlled comparisons.

### Trivial
None.

## Nice-to-Haves

- Report the ablation studies (Figs 9 and 10) with standard quality metrics (FID, SSIM, F1/MSE) in tabular form to quantify the quality-efficiency tradeoff.
- Provide a brief discussion of preprocessing required for PAA: how conditions of different resolutions/aspect ratios are handled (center-crop, padding, interpolation), and acknowledge this as a constraint of the current design.
- Report variance across multiple generation seeds for efficiency numbers, which can fluctuate with GPU utilization and prompt complexity.
- Discuss how the early-timestep sampling strategy would transfer to architectures or tasks beyond the FLUX fine-tuning setup used in this paper.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Baseline optimization parity concern** (Harsh Critic): The claim that OminiControl2 and UniCombine may have their own native optimizations (dynamic token pruning, adaptive downsampling) not applied to the comparison is not verifiable from the paper alone. The paper states "To ensure a fair comparison, we fine-tune the FLUX.1 model using LoRA" (Sec 4.1), suggesting they reimplemented baselines under the same LoRA fine-tuning setup. Without evidence that baselines were intentionally weakened, this is speculative. Remove.

- **Attention redundancy analysis needs quantitative measures** (Harsh Critic): The request for attention entropy/mass concentration metrics is a quality-of-analysis enhancement, not a core flaw. The figures (2 and 3) already provide strong qualitative evidence, and the ablation studies serve as quantitative validation. Demote to nice-to-have.

- **Early-timestep sampling framing** (Harsh Critic): The claim that early-timestep sampling is "a practical training schedule tweak rather than a core architectural contribution" overstates the criticism. The perturbation analysis (Fig 5) provides genuine empirical insight into temporal dynamics of condition influence. It is a supplementary contribution, not the main one, and the paper positions it correctly as complementary.

- **Generic "add quantitative metrics" criticism**: Some suggestions about reporting variance or confidence intervals are standard but not harmful to the core claims; they are folded into Nice-to-Haves rather than kept as weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Run an ablation where all methods are evaluated both with and without KV caching, and report the *residual* speedup attributable solely to PAA/KSA. This would strengthen the credibility of the efficiency claims even if the resulting numbers are smaller (likely 2–3× rather than 10×).
- Analyze the F1 score gap on Subject-Canny specifically: is it caused by PAA's strict locality pruning cross-patch context that edges need? If so, consider adding a small cross-patch window (e.g., ±1 or ±2 neighbors) to PAA and testing whether F1 recovers while maintaining most of the efficiency gain.

## Score and Decision

**Round 1 — Bracketing:** 
From the calibration search, I identified anchors in three bands:
- Low band (avg < 3.5): "Sample what you can't compress" (3.20), "Conditional LoRA Parameter Generation" (3.40) — both rejected papers with significant methodological gaps.
- Middle band (3.5–7.5): UniCon (7.00) — strong DiT efficiency paper with solid ablations and clear architectural advance; FasterCache (5.50) — useful training-free acceleration but with limited novelty; MDiT (5.00) — moderate contribution with limited validation; "Unified Video/3D/Game" (5.00) — limited novelty with mixed results.
- High band (avg > 7.5): Würstchen (8.00) — major architecture with substantially lower training costs; "Differential Transformer" (8.00) — strong theoretical and empirical advance; OCM (8.00); CADS (8.00) — all strong theoretical or architectural contributions.

**Initial bracket**: This paper sits between UniCon (7.0) and FasterCache (5.5), likely in the **5.5–7.0** range. It has more thorough evaluation than FasterCache but a confounding issue that UniCon does not have.

**Round 2 — Narrowing:**
I pulled anchors in the 5–7 range:
- FasterCache (5.50): Training-free acceleration with solid empirical results but modest novelty. PKA provides deeper architectural analysis and comprehensive quality evaluation. PKA is stronger.
- EfficientMod (6.00): Strong empirical results on efficient vision networks but limited technical novelty (primarily engineering refinements). PKA's structural insight about condition-aware attention decomposition is more principled. PKA is comparable or slightly stronger.
- "Efficiency Pentathlon" (5.25): Weaker contribution. Not comparable.

PKA's main advantages over the ~5.5–6.0 anchors: (1) the attention redundancy analysis is more directly tied to the proposed method; (2) ablation studies are cleaner; (3) evaluation across multiple multi-condition tasks is more comprehensive. 

PKA's weaknesses compared to the ~6.0–7.0 anchors: (1) the KV caching confound makes the headline efficiency claim less clean; (2) the F1 gap on controllability is unexplained; (3) less theoretically grounded than stronger papers.

Compared to UniCon (7.0), which has comparable structural insight without the confounding issue and clean ablation, PKA falls short due to the unisolated caching effect and the F1 controllability gap. I place PKA solidly below UniCon but above FasterCache and EfficientMod.

**Final score: 6.5** — the paper makes a genuine and useful contribution (clear architectural insight, clean decomposition, strong empirical support), but the efficiency claims are confounded and the quality results have unexplained gaps that prevent a higher score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>