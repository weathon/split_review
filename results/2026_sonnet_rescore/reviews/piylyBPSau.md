## Summary

GenCoGS introduces a unified few-shot novel view synthesis method that augments 3D Gaussian Splatting with two generative completion strategies: (1) Generative Point Cloud Completion-based Gaussian Initialization (GCGI), using a DGCNN+Transformer+FoldingNet pipeline with a kd-tree outlier filter, and (2) Generative Pseudo View Completion-based Gaussian Optimization (GCGO), using an I2V diffusion model guided by a perturbed camera trajectory and a novel generative consistency loss. Experiments on LLFF, DTU, and Shiny benchmarks consistently show improvements over prior 3DGS-based methods, with the largest single gain being +2.40 dB PSNR on DTU (3-view) over the next-best 3DGS method.

---

## Strengths

- **GCGI demonstrably improves initialization quality.** The CPG+CPF pipeline generates a visibly cleaner point cloud (Figure 3c vs. 3b), and Table 4 confirms a +0.66 dB PSNR, +0.024 SSIM, −0.016 LPIPS improvement over the baseline from GCGI alone.
- **GCGO ablation properly isolates contributions.** Table 5 systematically compares random sampling (LPIPS 0.188) vs. trajectory-based sampling (0.181) vs. trajectory + consistency loss (0.164), confirming each sub-component contributes. This is a well-designed ablation rarely seen in systems papers.
- **Strong DTU results.** GenCoGS achieves 23.11 dB PSNR on DTU (3-view), a +2.40 dB improvement over the second-best 3DGS method (BinoGS at 20.71) and +2.91 dB over the next best overall method (CAT3D at 22.02), substantiated by Table 2 and Figure 5 visual comparisons.
- **Robustness to sparse initialization demonstrated.** Table 6 shows that even with only 1/4 of the SfM points, GCGI still yields gains (+0.37 dB PSNR, −0.008 LPIPS over no-CPG baseline), indicating the pipeline is not brittle to input quality.
- **Consistent multi-benchmark coverage.** Unlike many prior methods that omit multi-view-count experiments, GenCoGS is evaluated at 3, 6, and 9 views on LLFF, providing a clearer view of how gains evolve with observation count.

---

## Weaknesses

### Fatal
None.

### Major

- **Shiny benchmark comparison excludes state-of-the-art baselines.** Table 3 contains only RegNeRF, FreeNeRF, SparseNeRF, 3DGS, and FSGS. BinoGS, CAT3D, IPSM, and ReconFusion — all present in Tables 1 and 2 — are absent without explanation. The +1.47 dB PSNR headline gain on Shiny is measured over FSGS, which is among the weakest baselines in Tables 1 and 2. Without the stronger baselines, the Shiny results cannot inform readers about GenCoGS's standing in the field on that dataset.

- **CPG training protocol unspecified in the paper body.** Section 3.1.1 describes the CPG architecture (DGCNN + Transformer encoder-decoder + FoldingNet) via Equations 1–4 but does not state: the training objective, the training data, or whether CPG is initialized from a pretrained model (e.g., ShapeNet-pretrained). While the appendix (which the parser strips) may contain these details, the Reproducibility Statement points to Section 4 for "complete implementation details," and Section 4 lists only inference hyperparameters (k=3, δ₁=1.0, etc.). Ablation gains attributed to GCGI design choices cannot be fully interpreted without knowing the training regime. This is a gap in the reviewable portion of the paper.

### Minor

- **LPIPS non-monotonicity across view counts on LLFF is unacknowledged.** Table 1 shows that GenCoGS LPIPS at 6-view (0.108) is slightly *worse* than BinoGS (0.106), and at 9-view both methods are tied at 0.090. The paper states in §4.1 that GenCoGS "consistently outperformed…nearly in all metrics," but the abstract gives a general impression of broad improvement. The AVGE metric still improves uniformly, so this does not undermine the core contribution, but it should be explicitly acknowledged rather than folded into a summary of improvements.

- **Ablation baseline (Table 4: 20.79 PSNR) is 0.48 dB higher than the FSGS row in Table 1 (20.31).** The paper does not explain this discrepancy (re-implementation, different SfM output, different hyperparameters). Since GCGI/GCGO are built on a FSGS-style baseline, gains computed from the higher in-paper baseline look smaller than they would if measured against published FSGS. Clarifying this would strengthen confidence in the reported deltas.

- **No runtime or memory comparison is provided.** GenCoGS layers an I2V diffusion model inference run and a learned point-completion network on top of FSGS. For a method positioned around practical deployment under data sparsity, the absence of any training time, per-frame inference time, or GPU memory figure (all runs done on an A6000) is a genuine omission.

- **The generative consistency loss (L_reg) explanation is internally ambiguous.** The mask M̂_r (Eq. 14–15) equals 1 where Δ_C is *high* — i.e., where the diffusion output diverged most from the rendered pseudo-view. L_reg (Eq. 16) then enforces an L1 penalty specifically in those regions, pulling the Gaussians toward the diffusion output where the model changed things most. The paper characterizes this as "suppressing hallucination," yet the mask selects regions of maximum diffusion intervention. The empirical ablation (Table 5) confirms L_GC helps, but the paper does not reconcile why applying reconstruction supervision at high-gap regions is the correct mechanism. An intuitive account (e.g., high-gap = structurally hollow regions the Gaussians fail on, and the diffusion's intervention there is meaningful completion rather than hallucination) is needed.

- **Low vanilla FSGS baseline on DTU (17.34) is not discussed.** On LLFF, FSGS (20.31) is only 1.13 dB below BinoGS (21.44); on DTU, the same gap is 3.37 dB (17.34 vs. 20.71). GenCoGS's +2.40 dB gain over BinoGS on DTU is its strongest result, but the unusually poor FSGS-DTU baseline — on which GenCoGS is built — raises the question of whether there is a configuration issue specific to DTU that GenCoGS happens to fix or whether the DTU setting is simply harder for plain 3DGS. Clarifying this would sharpen interpretation of the DTU gains.

### Trivial
None beyond what is covered above.

---

## Nice-to-Haves

- **Ablation of GCGO activation timing (m = 4,000 / 5,000 iterations).** The choice to activate the GCGO only in the final 20% of optimization is a strong structural decision. An ablation varying m would help justify it and would benefit readers seeking to adapt this design.
- **Separate analysis of completion in observed vs. unobserved frustum.** The paper's contribution is framed around completing "unobserved regions." A direct evaluation (e.g., measuring improvement on rendered views within vs. outside the training-view frustum) would provide a more precise picture of where each strategy helps.
- **Isolate diffusion model contribution from trajectory design.** Table 5 compares random vs. trajectory-based sampling and trajectory ± L_GC, but does not compare trajectory-based with diffusion vs. trajectory-based with plain interpolated (non-diffusion) pseudo views. This additional row would confirm that the I2V model specifically drives the gain, not merely the trajectory perturbation.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"CPF filtering contradicts the goal of completing unobserved regions" (Harsh Critic, framed as structural flaw).** Partially valid as a framing concern but overstated. The filter threshold is δ₁ × μ(P₀), where μ(P₀) is the mean *pairwise* distance of all points in the sparse cloud — on typical SfM outputs this is a very large number, permitting complementary points at substantial distances from P₀. Figure 3(c) visually confirms that meaningful structural detail is retained after filtering. The mechanism is better described as local geometric enrichment than as pure hallucination removal, but this is a framing/presentation issue, not a contradiction. Retained as part of the L_reg clarity Minor weakness above.

- **"Improvements over BinoGS are modest on LLFF at 3-view (+0.69 dB), not a major advance."** This is a magnitude criticism without a threshold justification. The improvements at 3-view are consistent across all four metrics (PSNR, SSIM, LPIPS, AVGE) and there is no established minimum threshold for significance. Removed as a noise criticism.

- **"DTU gains may reflect BinoGS instability rather than GenCoGS quality."** Speculative — not grounded in any specific evidence in the paper. Removed.

---

## Novel Insights

The paper surfaces a practically important insight: in the few-shot 3DGS pipeline, generative completion needs to be applied at *both* the initialization stage (point cloud) and the optimization stage (pseudo view guidance) to address distinct failure modes — initialization incompleteness causes persistent floating artifacts, while optimization-phase guidance from interpolated pseudo views systematically under-covers unobserved regions. The separate ablations in Tables 4 and 5 confirm these are orthogonal contributions (+0.66 dB from GCGI, +0.86 dB from GCGO, and a further combined gain from their interaction), suggesting that prior work targeting only one stage leaves systematic gains on the table. The "generate-and-filter" paradigm applied to point cloud completion — generating with a learned network and filtering via a geometry-aware distance criterion — is a clean strategy that other initialization-focused works could adopt.

---

## Suggestions

1. Include BinoGS, CAT3D, IPSM, and ReconFusion in Table 3 (Shiny), or explicitly state and justify their absence.
2. Add a paragraph in the main body (or clearly direct readers to the appendix section) describing the CPG training objective, training dataset, and whether weights are transferred from a pretrained model.
3. Add a runtime comparison table (training time per scene, inference time per frame) against FSGS and BinoGS.
4. In Section 4.1, acknowledge the 6-view and 9-view LPIPS behavior explicitly ("LPIPS at 9-view matches BinoGS; gains are concentrated in PSNR, SSIM, and AVGE at higher view counts").
5. Reconcile the ablation baseline (20.79) with the FSGS entry (20.31) in a footnote or implementation detail paragraph.
6. Revise the L_reg explanation to explicitly describe *why* applying supervision in high-gap regions suppresses hallucination (e.g., "these are the structurally hollow regions the Gaussians cannot reconstruct from training views alone, so diffusion guidance there is both necessary and informative").

---

## Score and Decision

**Originality:** The unified generate-and-filter paradigm applied to both stages of 3DGS (initialization and optimization), along with the novel perturbed-trajectory + consistency-loss GCGO design, represents a genuine methodological contribution. **4/5**

**Importance of research question:** Few-shot NVS from sparse views is an active, practically relevant problem. The paper directly addresses a well-identified failure mode (scene incompleteness) at two complementary stages. **4/5**

**Claims supported:** The main claims — GenCoGS outperforms prior 3DGS-based methods on three benchmarks — are well-supported by Tables 1 and 2, and the ablations properly isolate component contributions. The Shiny comparison is underpowered, and the LPIPS trend at higher view counts is not acknowledged. **3/5**

**Soundness:** The method design is technically coherent. The consistency loss mechanism has a conceptual ambiguity but is empirically validated. The CPG architecture is described but its training is not. **3/5**

**Clarity:** Generally clear; some notable ambiguities in the L_reg explanation and the baseline discrepancy between Tables 1 and 4. **3/5**

**Value to research community:** Demonstrates that point-cloud completion can meaningfully improve 3DGS initialization and that I2V diffusion models can be tamed for per-scene optimization guidance. Both ideas are transferable beyond the specific system. **4/5**

**Overall:** A solid contribution with strong empirical results (particularly on DTU), well-designed ablations, and a coherent dual-stage completion framework. The two Major weaknesses (incomplete Shiny comparison, CPG training details) are correctable and do not invalidate the core results. The paper crosses the acceptance threshold.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>