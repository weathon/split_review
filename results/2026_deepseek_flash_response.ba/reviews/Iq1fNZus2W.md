## Summary

This paper proposes Patch-wise and Keyword-Aware Attention (PKA) for efficient multi-condition control in Diffusion Transformers (DiTs). PKA decomposes standard multi-modal attention into two specialized modules: Position-Aligned Attention (PAA) for spatial conditions (one-to-one attention between aligned patches, O(N) complexity) and Keyword-Scoped Attention (KSA) for subject-driven conditions (attention confined to keyword-activated regions). A condition KV cache reuses condition projections after the first denoising step, and an early-timestep sampling strategy is proposed to accelerate training. Experiments on a fine-tuned FLUX.1 model show up to 10× inference speedup and 5.12× VRAM reduction at 16 conditions while maintaining competitive generation quality at 2-3 condition tasks.

## Strengths

1. **Attention sparsity analysis directly motivates architectural design**: The paper diagnoses computational redundancy by showing spatial-condition attention is diagonal-dominant (Figure 2) and subject-driven attention is localized to keyword-relevant regions (Figure 3). These observations directly inform PAA and KSA design rather than relying on generic sparsity heuristics — a principled approach.

2. **Efficiency gains scale with condition count across multiple axes**: Figures 7-8 show speedup relative to UniCombine growing from 3.90× (4 conditions) to 10× (16 conditions) and VRAM reduction from 2.46× to 5.12×. PKA maintains near-constant latency (~20s) and VRAM (~400MB) while baselines grow quadratically — the strongest evidence the method addresses the quadratic bottleneck.

3. **Quality improvements across most metrics**: Table 1 shows best FID, SSIM, CLIP-I, and DINOv2 across all three tasks (Subject-Canny, Subject-Depth, Canny-Depth) while remaining competitive on F1/MSE controllability and CLIP-T text fidelity, demonstrating efficiency does not come at a quality cost in the tested regimes.

4. **Ablation studies decompose contributions**: PAA is ablated against full attention and sliding window attention (Figure 9). KSA is ablated across thresholds ε = 0.2–0.8 (Figure 10), showing systematic trade-offs between efficiency and subject fidelity.

## Weaknesses

### Major

1. **Headline claim fuses efficiency and quality evidence from different regimes**: The paper claims "up to 10× inference speedup... all while maintaining or improving generative quality" (abstract, conclusion). However, the 10× speedup and 5.12× VRAM reduction are measured at 16 conditions (Figures 7-8), while generation quality is evaluated on tasks with 2-3 conditions (Table 1). Quality is never evaluated at the high condition counts where the dramatic efficiency gains occur. Attention sparsity dynamics may differ when 16 conditions compete — interactions could degrade controllability in ways not visible at 2-3 conditions. To support the compound claim, the paper needs either quality evaluation at 8+ conditions or a reframing that decouples efficiency results from quality results.

### Minor

2. **Early-timestep sampling lacks quantitative validation**: Section 3.3 proposes a shifted logit-normal distribution (μ > 0, δ > 1) to concentrate training on early denoising steps. The evidence consists of a perturbation analysis (Figure 5) showing perturbing early steps affects SSIM more than late steps, plus a qualitative comparison (Figure 11) of three hyperparameter settings on a single alarm clock example. No quantitative metrics (FID, controllability scores, loss curves, iterations-to-convergence) are reported. The claim that this "accelerates convergence and enhances control fidelity" rests entirely on visual inspection of one example. Given this is presented as a distinct contribution, the lack of quantitative support is a gap.

3. **Subject-Canny F1 drop is understated**: On the Subject-Canny task (Table 1), F1 edge controllability drops from 0.551 (UniCombine) to 0.414 (Ours) — a **24.9% relative decrease**. The paper describes this as a "minor exception of a narrow margin." While the method wins on FID (52.99 vs. 61.03), SSIM (0.553 vs. 0.493), CLIP-I (0.945 vs. 0.912), and DINOv2 (0.926 vs. 0.901) for this task, the degradation on the one task with direct spatial controllability measurement is non-trivial and deserves candid discussion rather than minimization.

4. **"swa condition" column in PAA ablation is unexplained**: In Figure 9, a column labeled "swa condition" reports latency 13.58s and VRAM 198MB — both better than PAA (13.63s, 237MB) and better than any explicitly-discussed SWA variant. The paper's text only compares PAA against "the most efficient SWA (14.00s and 276MB)" from the SWA-1/2/3 columns, entirely ignoring this column. Without explanation of what "swa condition" represents, this confuses the comparison and undermines the claim that PAA outperforms all SWA variants.

5. **KSA mask temporal consistency assumption is not validated**: KSA computes a mask M^t at step t and reuses it at step t+1, relying on "temporal consistency" (Zhou et al., 2025). The paper does not analyze mask quality, measure mask overlap between consecutive steps, or discuss failure cases when the mask at step t misses a region that becomes relevant at step t+1. Since mask propagation is a core efficiency assumption, it should be supported.

6. **Token count per condition in quality evaluation unspecified**: The efficiency evaluation uses 1024 tokens per condition (Section 4.2.1). The quality evaluation (Table 1) does not specify the token count per condition, making it difficult to reconcile efficiency and quality results.

### Trivial

7. **Dataset curation details incomplete**: The paper curates a subset from Subject200K but does not report its size, train/test split ratio, or whether baselines (OminiControl2, UniCombine) were also fine-tuned with LoRA under identical conditions or used off-the-shelf.

## Removed Points

These points were considered but removed as they do not constitute valid weaknesses:
- "Figures 2 and 3 attribution — should be more explicit about whether reproduced or newly computed" — The paper states "we first investigated the attention patterns within existing multi-condition DiTs (Tan et al., 2024)." This is adequately clear.
- "Condition Cache is a straightforward application of KV caching, not novel" — The paper presents the cache as a structural consequence of the condition-only-self-attention design, not as a novel caching algorithm. The value is in the design choice that enables it.
- "No wall-clock time including first step overhead" — The efficiency graphs measure total inference time, which includes the first step. The overhead is visible in the data.
- Various formatting/style nitpicks reflecting parser artifacts, not author errors.
- Generic "missing related works" criticisms.

## Nice-to-Haves

- A quality-efficiency trade-off plot (e.g., FID vs. inference time) at matched condition counts would directly address the regime mismatch.
- Quantitative evaluation of early-timestep sampling (FID, controllability metrics, or loss curves for μ=0 vs. μ>0).
- IoU between KSA masks at consecutive timesteps to validate temporal consistency.
- A plot of CLIP-I vs. ε for KSA to better illustrate the quality-efficiency trade-off.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Either evaluate generation quality (FID, F1, CLIP-I) at 8+ conditions or explicitly decouple the efficiency claims from the quality claims in the abstract and conclusion.
2. Add quantitative evaluation of the early-timestep sampling strategy (at minimum, FID or controllability metrics for μ=0 vs. μ>0 at matched training iterations).
3. Explain or remove the "swa condition" column from Figure 9.
4. Provide the token count per condition used in the quality evaluation (Table 1).
5. Discuss the Subject-Canny F1 trade-off candidly rather than minimizing it.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>