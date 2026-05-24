## Summary

The paper proposes Patch-wise and Keyword-Aware Attention (PKA), a framework that decomposes the full-attention computation in multi-condition Diffusion Transformers (DiTs) into two specialized modules: Position-Aligned Attention (PAA) for spatial conditions and Keyword-Scoped Attention (KSA) for subject-driven conditions. The key insight — supported by attention-pattern analysis — is that full attention in multi-condition DiTs is largely redundant: spatial conditions activate almost exclusively along the diagonal, and subject conditions activate only in localized regions. PAA replaces full attention with one-to-one aligned attention, while KSA uses text-derived keyword masks to confine subject-condition attention to salient regions. Combined with a condition KV-cache and an early-timestep sampling strategy, the system reports up to 10× inference speedup and 5.12× VRAM reduction over the full-attention baseline while maintaining or improving generative quality.

## Strengths

1. **Diagnostic attention analysis is clean and well-motivated.** Figures 2 and 3 convincingly demonstrate that for spatial-aligned conditions, the attention matrix is nearly diagonal, and for subject-driven conditions, the cross-attention maps are highly localized. This provides a principled, data-driven foundation for both PAA and KSA, and is the paper's strongest intellectual contribution.

2. **PAA is a simple, well-grounded module with clear computational benefits.** The one-to-one aligned attention (Eq. 2) directly matches the observed diagonal sparsity pattern and reduces complexity from O(N²) to O(N). The ablation in Figure 9 shows PAA outperforms sliding-window attention at multiple window sizes in both latency (13.63s vs. 14.00s–14.32s) and VRAM (237MB vs. 276MB–316MB).

3. **Strong quantitative efficiency results across condition counts.** Figures 7 and 8 show consistent scaling advantages over UniCombine and OminiControl2 across 1–16 conditions, with speedups from 3.90× (4 conditions) to 10× (16 conditions) and VRAM reductions from 2.46× to 5.12×.

4. **Generative quality is maintained or improved alongside efficiency gains.** Table 1 shows PKA achieves the best FID, SSIM, CLIP-I, and DINOv2 across all three evaluated tasks (Subject-Canny, Subject-Depth, Canny-Depth). For instance, on Subject-Canny: FID 52.99 vs. 61.03 (UniCombine), DINOv2 0.926 vs. 0.901 (UniCombine). This directly supports the claim that efficiency does not come at the cost of quality.

5. **Condition cache is a practical engineering design** that is clearly explained (Figure 4a) and enabled by the architectural choice of making condition tokens self-attend only. The ablation implicitly relies on this, and the efficiency gains scale with the number of denoising steps.

## Weaknesses

### Fatal
None.

### Major

1. **KSA's keyword-identification process is underspecified, limiting applicability.** The method assumes that the text prompt contains explicit keywords that can be used to localize the subject in the image (Eq. 3). The paper states that a curated subset of Subject200K is used where "each image caption contains a descriptive keyword" (line 206), but does not describe how keywords are identified or extracted from arbitrary prompts in a general setting. In practical subject-driven generation, a user may provide a reference image and a prompt like "a garden scene" that does not contain a direct keyword for the subject. Without a specified mechanism to identify or extract the relevant keyword tokens from general prompts, the claimed generality of KSA is unsubstantiated.

2. **The efficiency comparison conflates multiple optimizations, and the individual contribution of the condition cache is not isolated.** The headline speedups (10×, 5.12× VRAM) compare the full PKA system (PAA + KSA + condition cache + condition self-attention-only design) against baselines that lack these optimizations. The condition cache alone — enabled by making condition tokens self-attend — could be applied to any multi-condition DiT. Figures 9 shows that PAA alone (with caching already in place) saves ~11% latency (15.38s → 13.63s) and ~23% VRAM relative to the cached-but-full-attention baseline, meaning a substantial portion of the 10× gain may come from the caching mechanism. The paper does not ablate the cache independently, nor does it report whether the baselines could benefit from the same caching trick, making the headline figures difficult to attribute cleanly to the proposed attention modules.

### Minor

1. **Early-timestep sampling lacks quantitative validation.** The only evidence for this component is the perturbation analysis in Figure 5 (conducted on base FLUX, not the fine-tuned model) and a single qualitative example in Figure 11 (alarm clock). No convergence curves, no final task metrics (FID/SSIM/CLIP-I) for different (μ, δ) settings are provided. A single-image qualitative comparison is insufficient to support a claimed contribution to the method.

2. **Ablation studies for PAA and KSA report only efficiency metrics, not quality metrics.** Figures 9 and 10 show latency and VRAM for different configurations but do not report controllability or quality metrics (e.g., F1, MSE, CLIP-I, DINOv2) across thresholds or conditions. The "graceful trade-off" claim for KSA (Figure 10) would be substantially stronger if accompanied by quantitative fidelity measures as a function of ε.

3. **Training details are incomplete.** The paper does not specify the size of the Subject200K subset, the LoRA rank or target modules used, nor which condition types were seen during training (the evaluation tests canny and depth, but whether training includes both is unclear). These details are needed for reproducibility.

4. **The temporal-consistency assumption in KSA's mask reuse is unvalidated.** KSA computes a relevance mask at timestep t and reuses it at timestep t+1 (Eq. 3–4), citing temporal consistency from prior work, but no analysis of mask drift across timesteps is provided to justify this assumption in the specific setting.

### Trivial
None.

## Nice-to-Haves
- Report quantitative quality metrics (CLIP-I, DINOv2, F1) in ablation studies for PAA and KSA as a function of thresholds.
- Add an ablation isolating the condition cache contribution to disentangle cache gains from attention redesign gains.
- Include a controlled experiment where baselines are re-implemented with the same condition-caching strategy to provide a cleaner comparison.

## Removed Points

- **"SSIM differences ~0.04 at most"** (Harsh Critic point 2): This is factually incorrect. The data in Figure 5 shows differences up to ~0.11 between High-to-Low and Low-to-High curves (e.g., at step 10: 0.37 vs 0.48). The perturbation experiment's effect is larger than claimed, which actually *strengthens* the paper's motivation. The underlying concern about missing quantitative validation of the sampling strategy remains valid and is retained as a Minor weakness.

- **"FID values are extremely high (52–80)" implying poor image quality** (Section-by-Section Notes): The paper compares all methods on the same test set, so relative comparisons are fair. High absolute FID values are expected for small, specialized test sets in multi-condition generation and do not indicate a methodological flaw. Removed as a non-issue.

- **"The strong scaling at high condition counts is not practically relevant"** (Section-by-Section Notes): The paper additionally demonstrates speedups at practical counts (e.g., 3.90× at 4 conditions, shown in Figure 7). Practical relevance at 2–4 conditions is established. Removed.

- **Strength Finder's generic strengths** ("addressed an important problem," "targeted an interesting question"): These are superficial and lack specific content tied to the paper. Dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated claims without revealing unexpected cross-perspective observations.

## Suggestions

1. **Clarify KSA's keyword extraction pipeline.** Specify whether keywords are manually annotated, extracted via a simple heuristic (e.g., noun-phrase identification), or require a learned module. If the method assumes a fixed known keyword per sample in the curated dataset, state this explicitly and discuss limitations for open-ended prompts.
2. **Isolate condition cache contribution.** Add an ablation that compares (a) full attention without cache, (b) full attention with cache, (c) PAA/KSA without cache, and (d) full PKA system. This would cleanly attribute the headline speedups.
3. **Add quantitative validation for early-timestep sampling.** Report final FID/CLIP-I/DINOv2 for at least 3–4 (μ, δ) settings on a standard task.
4. **Add quality metrics to ablation tables (Figures 9 and 10).** Report CLIP-I or DINOv2 alongside latency/VRAM to substantiate the claim of graceful trade-off.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| Qihoo-T2X (lTrrnNdkOX) — proxy-tokenized efficient DiT for T2I/T2V | 6.40 | Similar scope (DiT efficiency via attention sparsity). This paper has cleaner diagnostic motivation but similar-level experimental completeness. Both propose attention-level modifications to reduce redundancy. |
| DyDiT (taHwqSrbrb) — dynamic width/token DiT | 5.50 | Similar approach of exploiting temporal/spatial redundancy in DiTs. This paper's claimed speedups (10×) are larger than DyDiT's (1.73×), but DyDiT provides cleaner attribution of gains and more thorough ablations. |
| SparseDM (3kADTLbKmm) — sparse masks for diffusion efficiency | 4.00 | Weaker paper on all dimensions. This paper is clearly stronger in motivation, results, and contribution. |
| REPA (DJSZGGZYVi) — representation alignment for DiT training | 9.00 | Far stronger. Clean, well-motivated idea with thorough experiments across multiple settings. This paper does not reach that standard. |
| TCIG (RFJGFrMvYj) — two-stage controlled generation | 1.50 | Far weaker. This paper is methodologically sound, well-motivated, and has clear experimental support — not remotely comparable to TCIG. |
| LinFusion (D2as3jDmRA) — linear attention for high-res DiT | 6.25 | Similar score neighborhood. Both papers address attention efficiency in diffusion models with similar rigor. This paper's multi-condition focus is narrower but the analysis is more targeted. |

The paper has a well-motivated core insight (attention redundancy in multi-condition DiTs), a clean module design (PAA), and convincing efficiency numbers. However, the contribution is weakened by two major issues: KSA's unspecified keyword-extraction dependency that limits its claimed generality, and the conflation of cache gains with attention-design gains in the efficiency comparison. The early-timestep sampling contribution is under-evidenced. These issues are real and non-trivial, but they do not invalidate the core contribution — the diagnostic analysis, PAA, and the overall efficient system remain valuable. Compared to the anchors, the paper sits between the 5.5 and 6.4 level: weaker than REPA (9.0) but stronger than SparseDM (4.0), comparable to Qihoo-T2X (6.4) and DyDiT (5.5), with a cleaner motivation than either but less thorough attribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>