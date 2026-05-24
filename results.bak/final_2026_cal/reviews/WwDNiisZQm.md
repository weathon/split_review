Now I have all the information I need. Let me write the final consolidated review.

## Calibration Summary

**Round 1 — Bracketing (boundary anchors):**
- Low band (<3.5): MambaMatch (2.50), TVMamba (3.00), MoMamba (3.00) — Mamba vision papers with fundamental flaws, CMIC clearly stronger.
- Middle band (3.5–7.5): MambaSIC (4.00), SF-Mamba (4.50), R-D Limits Theory (4.00), Taming Hierarchical (5.50), Turbo-DDCM (4.80) — LIC papers in various states.
- High band (>7.5): Text-to-3D (8.00), VIST3A (8.00), Permutation-Equivariant (8.00) — Not compression papers; breakthrough-level contributions.

**Round 1 bracket:** 5.5–7.5

**Round 2 — Narrowing (middle band):**
- Taming Hierarchical Coding (5.50, poster): Spectral regularization for hierarchical LIC. CMIC has stronger method novelty and equally strong results → CMIC > 5.50.
- SP-MoMamba (6.00, rejected): Superpixel+SSM for SR. Criticized as over-engineered with limited novelty (essentially combining existing techniques). CMIC has clearer novelty and more principled motivation → CMIC > SP-MoMamba.
- Turbo-DDCM (4.80, poster): Diffusion compression with weak quantitative results → CMIC clearly stronger.

**Final assessment:** CMIC introduces genuinely novel mechanisms (content-adaptive token permutation via VQ-style clustering, global-prior prompting) that are well-motivated and clearly demonstrated. The empirical results are strong (best on 2/3 datasets, competitive on the 3rd), and the qualitative evidence (ERF, clustering visualizations) is among the best in the LIC literature. Weaknesses are minor: the SOTA claim overreaches slightly (MLICv2 marginally better on Kodak), and confidence intervals would strengthen the evaluation. These are fixable issues that do not undermine the core contribution. Compared against the calibration anchors, CMIC is clearly above the 4–5.5 range of typical LIC papers and sits approximately at the boundary of accept-level work.

**Score: 6.0** → **Decision: Accept**

---

## Summary
This paper introduces Content-Aware Mamba (CAM) for learned image compression, addressing two fundamental limitations of Mamba-style SSMs when applied to images: (1) the fixed, content-agnostic raster scan that ignores feature-space similarity, and (2) strict causality that prevents access to future context. CAM proposes Content-Adaptive Token Permutation (CTP), which clusters tokens by feature similarity via a shared codebook and reorders the sequence to group semantically similar tokens, and Global-Prior Prompting (GPP), which injects sample-specific global priors into the SSM output projection to relax causality. The resulting model CMIC achieves strong BD-rate savings of –15.91%, –21.34%, and –17.58% over VTM-21.0 on Kodak, Tecnick, and CLIC, outperforming prior Mamba-based LIC models (MambaVC, MambaIC) while using 56% fewer parameters and 57% fewer FLOPs.

## Strengths

- **Novel and well-motivated method.** The paper identifies two genuine problems with Mamba for compression—its predefined scan order is agnostic to content similarity, and its causal structure limits global awareness—and proposes clean, principled solutions. CTP uses a VQ-VAE-inspired codebook with EMA updates for stable, differentiable clustering and sequence reordering. GPP leverages the clustering centroids to generate sample-specific prompts that condition the SSM output. Both components are clearly described, well-grounded in the problem analysis, and isolated through clean ablation studies.

- **Strong empirical performance with thorough evaluation.** CMIC achieves the best reported BD-rate on Tecnick (–21.34%) and CLIC (–17.58%) among all compared methods, and is competitive on Kodak (–15.91%, within 0.25pp of the best method MLICv2). The evaluation spans three datasets, two distortion metrics (PSNR, MS-SSIM), comprehensive complexity metrics (params, FLOPs, latency, peak memory), and seven ablation experiments covering component contributions, network structure choices, cluster size, and throughput. The RD curves (Figs. 4–6) consistently show CMIC at or near the top across all bitrates.

- **Exceptional qualitative evidence.** The effective receptive field (ERF) visualizations (Figs. 7–9) are a highlight: they convincingly demonstrate that CMIC produces larger, content-adaptive receptive fields compared to CNN-, Transformer-, and prior Mamba-based models. The layer-wise ERF analysis (Fig. 9) cleanly isolates the effects of CTP (semantic, non-Euclidean activation patterns) and GPP (breaking causal boundaries). The clustering visualizations (Fig. 10) confirm semantically meaningful grouping (e.g., red doors, clouds, feathers). This qualitative support for the claimed mechanisms is among the strongest in the recent LIC literature.

- **Significant efficiency gains over Mamba competitors.** CMIC achieves better RD performance than MambaIC while using 56% fewer parameters (69.11M vs. 157.09M), 57% fewer FLOPs (2.39T vs. 5.56T), 39% lower latency (0.405s vs. 0.669s), and 78% less peak memory (4.44GB vs. 20.32GB). This practical advantage comes from the single-scan design versus MambaIC's multi-directional scans, and is clearly attributed.

## Weaknesses

### Minor

1. **Overstated SOTA claim.** The abstract and Section 4.3 claim "state-of-the-art" performance without qualification. However, on Kodak, MLICv2 achieves –16.16% BD-rate vs. CMIC's –15.91%. While CMIC is best on Tecnick and CLIC, the blanket SOTA claim should be qualified (e.g., "best overall across datasets" or "state-of-the-art on Tecnick and CLIC, competitive on Kodak"). This 0.25pp gap is small and within typical variance, but the claim as written is imprecise.

2. **No confidence intervals or uncertainty measures.** BD-rate and PSNR comparisons are reported to two decimal places without standard deviations, confidence intervals, or statistical tests. The test sets are small (Kodak: 24 images, Tecnick: 100, CLIC validation: ~30). The reader cannot assess whether the reported margins—including the 2.36pp gap over MambaIC on Kodak—are systematic or within noise. This is a common weakness in LIC papers but should be acknowledged, especially when small numerical differences are used to support the SOTA claim.

3. **Ablation baseline interpretation.** In Table 2, the baseline ("CTP off, GPP off") replaces CAM with vanilla Mamba, but the full CMIC architecture already includes window-attention blocks in every stage (Section 3.2). The measured 2.7–3.6% BD-rate gain from CTP+GPP is the improvement on top of a hybrid (window-attention + vanilla Mamba) baseline, not the gain over a pure Mamba architecture. The paper should explicitly note this when interpreting the ablation and when comparing to pure Mamba models like MambaVC/MambaIC. The current framing could overstate the benefit of CAM relative to a pure-Mamba alternative.

### Trivial

4. **Minor imprecision about causality.** The paper states GPP "mitigates the strict causality." This is accurate for the output (the prompt depends on all tokens and conditions the output projection), but the hidden state update \(h_i = \bar{A}h_{i-1} + \bar{B}x_i\) remains causal. The phrasing is slightly imprecise but not incorrect, and the ERF evidence (Fig. 9) convincingly shows non-causal effects in practice.

5. **DCAE also outperforms on Kodak but isn't discussed.** DCAE achieves –15.40% on Kodak vs. CMIC's –15.91% (better BD-rate), but the narrative text compares only to FTIC, TCM-L, MambaVC, and MambaIC. Including DCAE (which uses a different architecture) in the discussion would be informative.

## Nice-to-Haves
- Bootstrapped confidence intervals for BD-rate/PSNR comparisons would strengthen the evaluation.
- A brief limitations discussion (e.g., when clustering might fail on highly uniform images) would make the paper more complete.
- The adaptive cluster analysis (Table 5, showing 23–26 out of 64 centroids active per image) is interesting and could be discussed more explicitly as evidence of dynamic content-awareness.

## Removed Points
- **"MLICv2 omitted from narrative text" (Harsh Critic):** Removed. The paper explicitly lists "MLICv2 (Jiang et al., 2025)" in the compared methods (Section 4.3, line 231). The critic's claim of selective omission is incorrect.
- **"Latency hardware not specified" (Harsh Critic):** Removed. Section 4.1 states "All experiments are carried out on NVIDIA A100 GPUs," which covers latency measurements. Appendix A.14 additionally provides encoding latency on RTX3090.
- **"Missing entropy model architecture details" (Harsh Critic):** Removed. Section 3.2 and Fig. 3 describe the entropy model: "built upon the SCTX model," "depthwise convolution for context modeling," "gated MLPs for parameter aggregation." This is sufficient for a methods paper.
- **Strength Finder strengths about "addressing important problem" and "clear writing":** Removed as generic and insufficiently specific. The concrete strengths (SOTA performance, ablation evidence, ERF/clustering visualizations, efficiency gains) are retained.
- **"Missing related works" (Harsh Critic impulse):** Not raised explicitly, but the paper's related work coverage is adequate for the scope.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Qualify the SOTA claim.** Rephrase to "state-of-the-art on Tecnick and CLIC, and competitive with the best methods on Kodak" or "best overall across three datasets."
2. **Add confidence intervals.** Bootstrapped 95% CIs for BD-rate on each dataset would address the uncertainty concern and clarify whether gaps over MambaIC and MLICv2 are meaningful.
3. **Clarify ablation baseline composition.** In the ablation discussion, note that the baseline (vanilla Mamba) operates alongside window-attention blocks, so reported gains are on top of a hybrid architecture, not a pure-Mamba baseline. This would prevent over-interpretation.
4. **Include DCAE in the narrative comparison** alongside MLICv2 for completeness.

## Score and Decision

**Calibration anchors used:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| MambaSIC (0dHrYUd17W) | 4.00 | 1 | Straightforward Mamba application, limited novelty → CMIC clearly stronger |
| SF-Mamba (X4KsowemNB) | 4.50 | 1 | Visual Mamba with engineering focus, marginal results → CMIC stronger |
| Taming Hierarchical (lO6I66lweK) | 5.50 | 2 | Spectral regularization for LIC, accepted poster. CMIC has stronger method novelty |
| SP-MoMamba (ZeIsHH8Xx2) | 6.00 | 2 | Superpixel+SSM for SR, rejected for over-engineering. CMIC has cleaner novelty |
| Turbo-DDCM (eIF1QvC94Z) | 4.80 | 2 | Diffusion compression, weak quantitative results → CMIC clearly stronger |

Round-1 bracket: 5.5–7.5. Round-2 narrowed to ~6.0 based on comparison to SP-MoMamba (6.0, more complex but less novel) and Taming Hierarchical (5.5, less novel method).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>