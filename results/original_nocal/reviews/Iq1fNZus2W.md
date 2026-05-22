Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes Patch-wise and Keyword-Aware Attention (PKA), a framework that replaces the computationally expensive full-attention mechanism in multi-condition Diffusion Transformers with two specialized lightweight modules: Position-Aligned Attention (PAA) for spatial conditions (one-to-one attention at aligned positions, reducing complexity from O(N²) to O(N)) and Keyword-Scoped Attention (KSA) for subject-driven conditions (attention confined to keyword-relevant regions via a temporally-reused mask). An early-timestep sampling strategy is also introduced to accelerate fine-tuning. Experiments on FLUX.1 demonstrate up to 10× inference speedup and 5.12× VRAM reduction for the attention module while maintaining or improving generation quality on multi-condition tasks.

## Strengths

1. **Well-motivated architectural decomposition grounded in attention analysis (Figs. 2–3):** The paper provides clear empirical evidence that attention in multi-condition DiTs is highly redundant—spatial conditions concentrate along the diagonal (Fig. 2) and subject-driven conditions activate only sparse regions (Fig. 3). This directly motivates PAA and KSA, respectively, rather than relying on generic intuition. The design is principled and the two-module decomposition follows logically from the observed sparsity patterns.

2. **Compelling and scalable efficiency results (Figs. 7–8):** PKA achieves a 3.90× to 10× inference speedup and 2.46× to 5.12× VRAM reduction compared to the full-attention baseline UniCombine. Crucially, the advantage grows with the number of conditions (from 1 to 16), demonstrating that the method addresses exactly the scaling bottleneck it identifies. The efficiency gains are architectural (not dependent on training protocol) and are the paper's strongest contribution.

3. **Competitive or superior quantitative quality across three multi-condition tasks (Table 1):** On Subject-Canny, Subject-Depth, and Canny-Depth tasks, PKA achieves the best FID (e.g., 52.99 vs. 61.03 UniCombine on Subject-Canny), SSIM, CLIP-I, and DINOv2 scores, and is competitive on controllability metrics. This provides evidence that the efficiency gains do not come at the cost of generation quality.

4. **Clear module-level efficiency ablation (Figs. 9–10):** The PAA ablation compares against full attention and sliding window attention, showing lower latency (13.63s) and VRAM (237MB) than all variants. The KSA ablation shows a graceful tunable trade-off between efficiency and detail retention as the threshold ε varies. These experiments validate the efficiency benefits of each module.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline training protocol is not clearly specified, potentially confounding the quality comparison.** The paper states "To ensure a fair comparison, we fine-tune the FLUX.1 model using LoRA" (Section 4.1), but this description appears in the authors' own Training Details and does not explicitly state whether OminiControl2 and UniCombine were also fine-tuned under *identical* conditions (same LoRA rank, training data subset, iterations, optimizer). If baselines were used with their pre-trained/off-the-shelf weights while PKA was fine-tuned on the curated Subject200K subset, the quality improvements in Table 1 could partly reflect dataset-specific fine-tuning rather than the PKA architecture. The paper claims "fair comparison" but omits the specific details needed to verify this. This concern does *not* affect the efficiency results (Figs. 7–8), which are architectural, but it weakens the claim that quality is maintained or improved.

2. **Ablation studies lack quantitative quality metrics for the core modules.** Figures 9 (PAA) and 10 (KSA) report only latency and VRAM, not FID, CLIP-I, SSIM, or controllability scores for each ablated variant. The paper's central claim is that efficiency gains come "without compromising generative performance," yet the ablations provide no quantitative evidence to support this for the individual components. The visual comparisons are suggestive but insufficient—for instance, it is unclear whether PAA introduces any spatial control degradation relative to full attention, or how different KSA threshold values quantitatively affect subject fidelity. The main experimental results (Table 1) partially compensate by evaluating the full system, but the module-level quality story remains unsubstantiated.

### Minor

1. **Early-timestep sampling is validated only visually.** The shifted logit-normal sampling (μ>0, δ>1) is motivated by the perturbation experiment in Figure 5, which is a sound conceptual motivation. However, the only evidence for its benefit is the visual progression in Figure 11. No controlled experiment compares the final model's performance (on any metric from Table 1) with vs. without the shifted sampling or against the standard Logit-N(0,1) baseline. This limits the support for the claimed "accelerated convergence and enhanced control fidelity."

2. **Evaluation set size is not reported.** The paper states "a subset from the Subject200K dataset" is curated and partitioned into training and testing sets, but the actual number of images/samples is never given. Similarly, no confidence intervals or standard deviations are reported for any metric in Table 1 or Figures 7–10, making it impossible to assess the significance of the reported differences.

3. **Condition Cache is presented as a contribution without discussing its applicability to baselines.** The KV cache for condition tokens (Fig. 4a) is enabled by the design choice that conditions only self-attend. This is a valid benefit of PKA's architecture. However, the paper does not discuss whether a similar caching strategy could be retrofitted to the full-attention baseline, which would partially narrow the efficiency gap. A brief discussion would strengthen the positioning.

4. **All main evaluation tasks use only 2 conditions.** The paper emphasizes scaling to up to 16 conditions (Figs. 7–8), but the quality evaluation (Table 1, Fig. 6) is limited to 2-condition tasks (Subject+Canny, Subject+Depth, Canny+Depth). Providing quality results for scenarios with 4–8 conditions would better justify the practical relevance of the scaling claims.

### Trivial
None.

## Nice-to-Haves
- Providing quality metrics (FID, CLIP-I, etc.) for the PAA and KSA ablation variants.
- Including a controlled quantitative comparison (on a Table 1 metric) of the full model trained with vs. without the early-timestep sampling strategy.
- Reporting the evaluation set size and adding confidence intervals or standard deviations for key metrics.
- Showing failure cases where PAA or KSA breaks (e.g., when spatial alignment is not diagonal).

## Removed Points

These points from the reviewers were verified against the paper and removed for the following reasons:

1. **"Paper does not cite relevant prior work on token pruning or local attention (Swin, MaskGit)"** — Removed. The paper's Section 2.2 explicitly cites relevant efficient DiT literature (PixelPonder, OminiControl2, caching methods, layer pruning). The critic's suggested references (Swin, MaskGit) address general-purpose efficient attention, which is a different scope from multi-condition DiT control. The paper's related work coverage is appropriate for its contribution.

2. **"FID values >50 are unusually high"** — Removed. The Subject200K dataset involves subject-driven generation with reference images, where FID values in this range are not unusual for this challenging setting. The paper consistently compares against baselines under the same metric conditions, so the relative ranking is what matters.

3. **"The paper does not detail whether all methods use the same input resolution, token counts, or hardware"** — Removed. The paper explicitly states measurements are on "a single NVIDIA RTX 6000 Ada GPU" and that "each condition is represented by 1024 tokens." This is sufficient for a fair efficiency comparison.

4. **Strength Finder claim #5: "Early-timestep sampling accelerates convergence (Fig. 11)"** — Demoted from standalone strength to a minor supporting point because it relies solely on visual evidence without quantitative validation.

5. **Strength Finder claim that "Ablation validates each module independently"** — Partially removed. The ablations do validate efficiency independently, which is noted as Strength #4, but the claim that they validate quality preservation is unsupported (consistent with Weakness #2 above).

## Novel Insights

None beyond the paper's own contributions. The core insight—that multi-condition attention in DiTs is highly redundant and can be decomposed into position-aligned (spatial) and keyword-scoped (subject) modules with dramatically lower computational cost—is the paper's main novelty and is well-supported. The reviews do not surface additional novel interpretations beyond what the paper itself articulates.

## Suggestions

- **Clarify baseline comparison protocol:** Explicitly state whether OminiControl2 and UniCombine were fine-tuned under identical conditions (same LoRA config, data, iterations, optimizer). If they were, add that detail to Section 4.1. If not, provide an ablation where PKA is evaluated without fine-tuning or where baselines are re-fine-tuned fairly, to disentangle architectural benefits from training benefits.

- **Add quantitative quality metrics to ablation studies:** Include FID/CLIP-I/DINOv2 scores for the PAA variants (w/o PAA, SWA window sizes) and at least one KSA threshold sweep, to quantitatively verify that the modules preserve quality.

- **Quantitatively validate the early-timestep sampling:** Compare final model performance (using a Table 1 metric) between the proposed Logit-N(μ,δ) and the standard Logit-N(0,1) baseline, on at least one task.

- **Report evaluation set size and confidence intervals** to improve reproducibility and enable significance assessment.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>