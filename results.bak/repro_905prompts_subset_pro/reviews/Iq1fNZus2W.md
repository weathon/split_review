Now I have all the evidence I need. Let me synthesize the final review.

---

## Summary

This paper addresses the prohibitive computational cost of multi-condition attention in Diffusion Transformers (DiTs). The authors analyze attention patterns in existing multi-condition DiTs and identify two forms of redundancy: (1) spatial-aligned conditions exhibit strongly diagonal attention, and (2) subject-driven conditions activate only sparse, keyword-correlated regions. Motivated by this analysis, they propose Patch-wise and Keyword-Aware Attention (PKA), which decomposes full attention into Position-Aligned Attention (PAA) for spatial conditions and Keyword-Scoped Attention (KSA) for subject conditions, complemented by an early-timestep sampling strategy and a condition KV-cache. The method achieves up to 10× inference speedup and 5.12× VRAM reduction in the attention module relative to full-attention baselines.

## Strengths

- **Strong analytical motivation**: The paper provides concrete, visual evidence for its design. Figure 2 clearly demonstrates diagonal localization in spatial-condition attention matrices, and Figure 3 shows sparse, keyword-correlated activations for subject-driven conditions. This directly and convincingly motivates the decomposition into PAA and KSA.

- **Substantial and well-measured efficiency gains**: Figures 7 and 8 provide quantitative, scaling evidence across condition counts (1–16) for both latency (3.90× to 10× speedup vs. UniCombine) and VRAM (2.46× to 5.12× reduction). These are the paper's strongest results and are measured against two recent, relevant baselines (OminiControl2, UniCombine).

- **Principled algorithmic contributions**: PAA reduces complexity from O(N²) to O(N) via one-to-one aligned attention (Eq. 2). KSA introduces a lightweight keyword-based relevance mask (Eq. 3) that prunes query-key interactions to salient regions only (Eq. 4). Both are clearly specified and motivated.

- **Complementary training insight**: The early-timestep sampling strategy (Section 3.3) is grounded in a perturbation analysis (Figure 5) showing visual conditions exert strongest influence at high t. The ablation (Figure 11) demonstrates faster convergence with μ>0 versus standard or late-biased sampling.

- **Practical engineering contributions**: The condition KV-cache (Figure 4a), which computes key/value projections once at the first denoising step and reuses them, is a sensible design choice that compounds the attention savings.

## Weaknesses

### Major

- **Confounded quality evaluation**: The quantitative quality comparison in Table 1 uses the full proposed method (PKA + early-timestep sampling). The baseline methods (OminiControl2, UniCombine) are compared without, as far as the paper describes, using the same early-timestep schedule. The ablation studies in Section 4.3 report latency, VRAM, and qualitative images for PAA and KSA individually (Figures 9, 10), but provide no quantitative quality metrics (FID, SSIM, CLIP-I) for PKA versus full attention under identical training. Consequently, the gains in Table 1 cannot be confidently attributed to the attention mechanism itself — they may be partially or largely driven by the improved training schedule. The claim that PKA "maintains or improves generative quality" (abstract, line 20) therefore has weaker evidential support than the efficiency claims. This matters because the paper's value proposition depends not only on speed but on demonstrating that the savings do not degrade output quality.

- **Unclear baseline training parity**: Section 4.1 states "We employ OminiControl2 and UniCombine as baselines" and describes fine-tuning FLUX.1 with LoRA for the proposed method, but never clarifies whether the baselines were re-implemented and fine-tuned with identical data splits, optimizer (Prodigy), LoRA configuration, and iteration count (20K). If the baselines use their original checkpoints or different training protocols, the Table 1 comparisons may not be a fair measure of methodological advantage. The paper should state explicitly how each baseline was obtained. This is particularly important given the large gaps reported (e.g., 8–20 FID points).

### Minor

- **Ablations limited to efficiency and qualitative results**: While the PAA and KSA ablations (Figures 9, 10) effectively demonstrate efficiency trade-offs and qualitative quality preservation, the absence of quantitative quality metrics in these ablations leaves a gap. Reporting FID/SSIM for PKA vs. full attention under identical training would substantially strengthen the quality-maintenance argument.

### Trivial

- None identified that are attributable to the original paper rather than parser artifacts.

## Nice-to-Haves

- An experiment applying the early-timestep sampling scheme to a full-attention baseline (or to OminiControl2/UniCombine) would cleanly disentangle how much of the quality improvement comes from the attention design versus the training heuristic.

- Clarifying the exact mechanism by which the KSA mask is produced at the very first denoising step (beyond the high-level description in Figure 4a) would aid reproducibility, though the paper already indicates full computation occurs at that step.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic's claim that the confound is "fatal"**: The harsh critic framed the confounded quality evaluation as a fatal flaw that "undermines the paper's headline contributions." This overstates the issue. The paper's primary contribution is efficiency, and those results (Figures 7, 8) are robust and independent of the confound. The quality-maintenance claim, while imperfectly supported quantitatively, has qualitative backing in the ablations (Figures 9, 10). The concern is real but is Major, not Fatal.

- **Harsh critic's "missing KSA initialization detail"**: The paper already states that "Full computation occurs only at the first step" (Figure 4 caption) and Eq. 3 describes the mask computation at timestep t for reuse at t+1. The critic's concern is a minor implementation detail. Moved to Nice-to-Haves.

- **Strength Finder's "reasonable experimental setup"**: This strength is too generic and is partially contradicted by the unclear baseline training parity, which is a genuine concern. Removed.

- **Strength Finder's "well-controlled ablation studies"**: While the ablations are useful, calling them "well-controlled" overstates the case given the absence of quantitative quality metrics. The ablation contributions are captured under other strengths.

## Novel Insights

The paper's decomposition of multi-condition attention into position-aligned and keyword-scoped modules is genuinely insightful. The key observation — that different condition types exhibit structurally different attention redundancy patterns (diagonal for spatial conditions, sparse-keyword for subject conditions) — is simple but non-obvious, and it enables a clean factorization of the attention computation that existing efficiency methods (token pruning, caching, linear attention) do not exploit. This condition-type-aware sparsity lens could inform future work on efficient multi-modal transformers beyond image generation.

## Suggestions

- Add a controlled experiment: train PKA and a full-attention variant under identical conditions (same LoRA config, same standard timestep distribution, same iterations) and report the full Table 1 metrics. This single experiment would directly address the major evaluation concern.

- State explicitly in Section 4.1 whether OminiControl2 and UniCombine were re-implemented and fine-tuned under identical conditions as the proposed method, and if not, acknowledge the limitation.

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| DyDiT (taHwqSrbrb) | 5.50 | R1 | PKA has stronger analytical motivation, more dramatic efficiency gains, and addresses a harder multi-condition problem |
| PT-DiT (lTrrnNdkOX) | 6.40 | R2 | Both address DiT attention redundancy; PKA has more principled condition-type-aware decomposition and better efficiency results |
| LinFusion (D2as3jDmRA) | 6.25 | R2 | PKA is more targeted and problem-specific with stronger motivation |
| LEGO Bricks (qmXedvwrT1) | 6.67 | R2 | Comparable analytical depth; PKA has more impressive core efficiency numbers but LEGO has slightly more thorough evaluation |
| UniCon (uJqKf24HGN) | 7.00 | R1 | Similar level of contribution quality; UniCon's evaluation is more rigorous; PKA's efficiency gains are more dramatic |
| SANA (N8Oj1XhtYZ) | 8.50 | R1 | SANA is a full framework with broader scope and more comprehensive evaluation; PKA is narrower but deeper in its specific problem |

**Round 1 bracket**: 5.5–7.5. **Round 2 narrowing**: The paper is clearly stronger than PT-DiT (6.40) and comparable to LEGO (6.67). The efficiency results are outstanding, the analytical motivation is excellent, and the method is well-designed. The two major weaknesses (confounded quality evaluation, unclear baseline parity) are genuine but addressable and do not invalidate the core efficiency contribution. This places the paper at **6.5**, between PT-DiT and UniCon.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>