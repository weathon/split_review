I've now gathered enough calibration data. Let me finalize the review.

---

## Summary

This paper proposes Patch-wise and Keyword-Aware Attention (PKA), a framework for efficient multi-condition control in Diffusion Transformers (DiTs). PKA decomposes the standard "concatenate-and-attend" full attention into two specialized modules: Position-Aligned Attention (PAA), which computes one-to-one attention between aligned spatial-condition and image patches (O(N) instead of O(N²)), and Keyword-Scoped Attention (KSA), which prunes subject-condition attention to keyword-activated regions using a temporal-consistency-based mask. The framework also includes a Condition Cache (KV caching for condition tokens across denoising steps) and an early-timestep sampling scheme for training. Experiments on FLUX.1 with LoRA fine-tuning show up to 10× inference speedup and 5.12× VRAM reduction over full-attention baselines at high condition counts while maintaining or improving generation quality.

## Strengths

1. **Well-motivated attention decomposition with clean design.** The observation that spatial-condition attention is diagonally concentrated (Figure 2) and subject-driven attention is localized to keyword-relevant regions (Figure 3) provides a clear structural prior. PAA's one-to-one alignment (O(N) complexity) and KSA's temporal-consistency-based mask reuse are clean, intuitive solutions that follow directly from the observed sparsity patterns.

2. **PAA outperforms sliding-window attention on both efficiency and quality.** The ablation in Figure 9 compares PAA against SWA with multiple window sizes. PAA achieves 13.63s/237MB versus the best SWA variant's 14.00s/276MB, while producing qualitatively similar images. This demonstrates PAA is structurally better suited for spatial-condition alignment than standard local attention.

3. **The KSA threshold ablation demonstrates a graceful efficiency-quality trade-off.** Figure 10 shows that increasing ε from 0.2 to 0.8 smoothly reduces latency and VRAM while maintaining subject fidelity, without abrupt quality degradation. This is a stronger property than the sharp quality cliffs seen with aggressive token pruning methods.

4. **Efficiency gains scale with condition count.** Figures 7 and 8 show that PKA's relative advantage increases with the number of conditions (3.90× at 4 conditions → 10× at 16 conditions, and 2.46× → 5.12× for VRAM). This scalability is practically relevant as multi-condition generation grows in complexity.

## Weaknesses

### Major

1. **The headline efficiency numbers conflate the novel attention redesign with standard condition KV caching, and the individual attention modules deliver only modest standalone gains.** The paper frames "up to 10× speedup and 5.12× VRAM reduction" as the headline result. The ablation study tells a more measured story: PAA alone gives 15.38s → 13.63s (1.13×) speedup and 308MB → 237MB (1.30×) VRAM reduction (Figure 9). KSA alone (at ε=0.2) gives 16.99s → 15.33s (1.11×) and 368MB → 280MB (1.31×) (Figure 10). The dramatic 10× figure only emerges when (a) the Condition Cache is active and (b) many conditions are used (16 conditions). The Condition Cache — computing K and V projections for condition tokens once and reusing them — is a reasonable engineering choice, but it is largely standard KV caching applied to a specific setting. The paper does not clearly separate the caching contribution from the attention-sparsity contribution. A comparison against baselines augmented with the same caching strategy would be needed to isolate what PAA/KSA uniquely contribute. The paper also does not state whether OminiControl2 or UniCombine use condition KV caching, which is necessary to interpret the comparisons in Figures 7–8.

2. **The attention redundancy analysis that motivates the entire method is purely qualitative.** Figures 2 and 3 show attention heatmaps that visually suggest diagonal concentration (spatial) and localized activation (subject). However, the paper provides no quantitative measurement: what fraction of attention mass falls within the diagonal band? What percentage of query-key pairs have attention scores below some threshold? What coverage does the KSA ε=0.2 threshold provide? Without numbers, the motivational claim that "a significant portion of the attention computation is indeed redundant" (line 21) is suggestive but not evidential. This also means the design choices for KSA's masking threshold are not quantitatively grounded.

### Minor

3. **No measure of variance or statistical significance for quantitative results.** Table 1 reports FID, SSIM, CLIP-I, DINOv2, and CLIP-T scores as single point estimates. FID differences of 8–14 points are claimed as improvements, but no standard deviations, confidence intervals, or multiple-run statistics are provided. FID has non-trivial variance depending on sample size and random seed. The paper should at minimum note whether these are single-run or multiple-run results.

4. **The early-timestep sampling contribution is validated only qualitatively on a single example.** Figure 11 shows generated images at different training iterations for different (μ, δ) settings, but only one example (an alarm clock) is shown. The claim that this "accelerates convergence and enhances control fidelity" (line 41) should be supported by quantitative metrics (FID, controllability scores, or training loss curves comparing the proposed distribution against the standard logit-normal).

5. **The perturbation experiment in Figure 5 is under-specified.** The paper does not define what "perturbation" means here — are condition tokens replaced with noise? Zeroed out? Replaced with random conditions? This is necessary to interpret why "High-to-Low" perturbation causes a sharper initial SSIM drop. Additionally, the SSIM values (0.34–0.50) are low, and the paper does not clarify whether these compare perturbed-vs-unperturbed generations or perturbed-vs-ground-truth images.

6. **Minor overclaiming.** On Subject-Canny (Table 1), UniCombine achieves higher F1 controllability (0.551 vs. 0.414) and higher CLIP-T text fidelity (0.352 vs. 0.349). The paper states "our method significantly outperforms competing baselines" (line 249) — this characterization is too strong given these exceptions. The paper acknowledges these as "narrow margins" in the text, but the contribution statements in the abstract and introduction do not reflect this nuance.

### Trivial

None.

## Nice-to-Haves
- Clarify whether baselines (OminiControl2, UniCombine) were retrained with LoRA on the same data subset used for PKA, or whether pre-trained weights were used as-is. If not, this is a confound.
- The paper would benefit from a limitations section discussing: (1) PAA assumes exact spatial alignment between condition and image tokens; (2) KSA's mask reuse across timesteps assumes temporal stability that could break under significant subject motion; (3) the Condition Cache assumes condition token representations are static across the denoising trajectory.
- The high FID values (52–80 across all methods in Table 1) warrant discussion relative to typical FID on standard benchmarks, as these likely reflect the difficulty of the multi-condition task or evaluation set size.

## Removed Points
- **"Equation formatting issue"** (garbled Equation 4 at line 136): Parser artifact, not an author error. Removed.
- **"Condition cache is not novel"**: KV caching in autoregressive models is standard, but adapting it to the specific structure of multi-condition DiTs where condition tokens only self-attend is a non-trivial application. The core issue — that the paper should separately attribute the caching contribution — is retained as Major Weakness 1.
- **"FID values very high"**: The critic's observation is partially valid but not a weakness of the method. Moved to Nice-to-Haves.
- **"Missing related works"**: Cannot be independently verified; removed.
- **Strength Finder strength 3** ("quantitative efficiency results significantly surpass strong baselines"): This is kept in spirit but tempered by the attribution issue raised in Major Weakness 1.
- **Strength Finder strength 1** ("attention pattern analysis provides empirical grounding"): The qualitative nature is acknowledged in Major Weakness 2; the grounding is real but incomplete.

## Novel Insights
None beyond the paper's own contributions. The reviews surface no observation about the paper that the paper itself does not already present or imply.

## Suggestions
1. Restructure the efficiency reporting to clearly decompose gains: report inference time and VRAM for (i) full attention without cache, (ii) full attention with condition cache, (iii) PAA/KSA without cache, (iv) PAA/KSA with cache. This would isolate the novelty contribution and make clear how much of the 10× is from the attention redesign versus the caching strategy.
2. Add quantitative analysis of attention sparsity: report the fraction of attention mass captured by PAA's diagonal alignment and the fraction of positions pruned by KSA's mask at ε=0.2 (and what coverage of the true attention mass this provides).
3. Validate the early-timestep sampling quantitatively (FID or controllability curves vs. training iterations) across multiple examples, not just one.

### Calibration Summary

**Round 1 — Bracketing:**
- Low-scoring anchors (< 3.5): `Jt1gGIumJo` (3.00), `rnTb9dm9zx` (3.00), `QKqWnNkwPL` (3.00) — all reject-level papers on diffusion model acceleration.
- Mid-scoring anchors (3.5–7.5): `taHwqSrbrb` — DyDiT (5.50), `lTrrnNdkOX` — Qihoo-T2X (6.40), `leBbjaUxut` — MDiT (5.00).
- High-scoring anchors (> 7.5): `gU58d5QeGv` — Würstchen (8.00), `fV0t65OBUu` — OCM (8.00), `OvoCm1gGhN` — Diff Transformer (8.00).

**Round 1 Bracket:** 4.0–6.5.

**Round 2 — Narrowing:**
- `taHwqSrbrb` — DyDiT (5.50): Most directly comparable paper (efficient DiT via dynamic computation). Our paper has similarly clear motivation but a more serious attribution issue (caching conflated with attention redesign). Our individual module gains (~10–30%) are comparable to DyDiT's 1.73× speedup. **Similar quality.**
- `lTrrnNdkOX` — Qihoo-T2X (6.40): Proxy-tokenized attention for DiT. More comprehensive scope (T2I, T2V, T2MV) but some reviewers found it incremental. Our paper is narrower but has cleaner ablation. **Slightly weaker.**
- `uJqKf24HGN` — UniCon (7.00): Unidirectional flow for DiT control. Cleaner contribution, more thorough experiments. Our paper's framing issues prevent reaching this quality level. **Notably weaker.**
- `D2as3jDmRA` — LinFusion (6.25): Linear attention for diffusion. Similar efficiency-focus, more comprehensive evaluation. **Slightly weaker.**
- `3BhZCfJ73Y` — APTP (6.25): Prompt-based pruning. Different focus but similar tier. **Slightly weaker.**

**Final Score Determination:** The paper is comparable to DyDiT (5.50) — it has well-motivated modules and good ablation studies, but the conflated efficiency attribution and qualitative-only motivation analysis are real weaknesses that prevent it from reaching the 6+ range. The paper is clearly above reject-level papers (3.0–3.25).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>