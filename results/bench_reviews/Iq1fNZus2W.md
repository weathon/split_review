Now I have strong calibration context. Let me synthesize the final review.

## Summary

This paper proposes Patch-wise and Keyword-Aware Attention (PKA), a framework to reduce the quadratic attention overhead in multi-condition Diffusion Transformers. It introduces two specialized modules: Position-Aligned Attention (PAA) for spatial conditions (one-to-one attention between aligned patches), and Keyword-Scoped Attention (KSA) for subject conditions (attention only in keyword-relevant regions), complemented by a Condition KV Cache and an early-timestep training sampling strategy. The approach is conceptually clean, and the reported efficiency gains are substantial (up to 10× speedup, 5.12× VRAM reduction).

## Strengths

- **Principled attention decomposition grounded in empirical analysis.** The paper identifies and characterizes two distinct types of attention redundancy in multi-condition DiTs — spatially localized diagonal patterns for layout conditions (Figure 2) and sparse keyword-activated regions for subject conditions (Figure 3) — then designs modules (PAA, KSA) that directly exploit each pattern. This is a principled departure from generic pruning or caching approaches.

- **Substantial efficiency gains with a plausible mechanism.** The claimed speedups (up to 10×) and VRAM reductions (up to 5.12×) are well-motivated by the complexity analysis: PAA reduces QK computation from O(N²) to O(N) per spatial condition, and KSA prunes query-key interactions via a cheap keyword-driven mask. The Condition KV Cache compounds savings across the full denoising trajectory.

- **Early-timestep sampling is an insightful training contribution.** The perturbation analysis (Appendix A.2/Figure 5) convincingly shows that visual conditions exert their strongest influence in early denoising steps. The shifted logit-normal distribution that skews training toward these steps is a practical, transferable idea beyond this specific architecture.

## Weaknesses

### Fatal

None.

### Major

1. **Uncontrolled baseline comparison.** The paper compares against OminiControl2 and UniCombine but never specifies whether these baselines were fine-tuned under conditions identical to the authors' method (same LoRA rank, same data subset, same training iterations, same optimizer). Lines 380–382 describe the authors' fine-tuning setup for "our method," but lines 385–387 simply name the baselines without stating how they were configured. If baselines were used off-the-shelf while the method received task-specific LoRA fine-tuning, the comparison is invalid for both quality and efficiency claims. This is the primary barrier to accepting the paper's central assertion that the method "maintains or even improves generative quality."

2. **Ablation studies lack quality metrics.** 
   - The PAA ablation (Figure 9) reports only latency and VRAM for full attention, SWA variants, and PAA — no FID, DINOv2, CLIP-I, or controllability metrics (F1, MSE) are provided for any variant. Without these, the claim that PAA "delivers high-quality spatial control" is unsupported.
   - The KSA ablation (Figure 10) shows a single qualitative example with varying thresholds ε. There are no aggregate metrics across a test set showing how quality degrades as ε increases.
   - The early-timestep sampling ablation (Figure 11) shows qualitative results at different iterations and one SSIM curve (Appendix Figure 13), but no final FID/DINOv2 numbers on the full metric suite.
   
   Since the paper's core claim is that efficiency is achieved "without compromising generative quality," the lack of quality metrics in ablations is a significant gap.

3. **Keyword extraction is unspecified for general use.** The method requires 1–2 keyword tokens per subject condition to generate the KSA mask (Eq. 3). The paper describes curating the training set to ensure captions contain descriptive keywords (line 378–380), but provides no protocol for automatically extracting keywords from arbitrary prompts at inference time. This limits reproducibility and applicability beyond the curated dataset. A rule-based or LLM-based keyword extractor should be specified.

### Minor

1. **Attention visualization methodology is underspecified.** Figures 2 and 3 are central to motivating the paper, but no details are given about which model, which layer, or which timestep produced these attention matrices. The claim of "intensely localized" attention along the diagonal would be strengthened by reporting these details and showing that the pattern holds across layers/timesteps.

2. **KSA mask reuse is not ablated.** The mask is computed once at timestep t and reused thereafter (line 300–301), justified by "temporal consistency." No experiment compares this single-computation strategy against recomputing the mask periodically (every k steps), leaving the reader unable to assess whether accuracy is sacrificed.

3. **Early-timestep sampling parameters lack sensitivity analysis.** The chosen parameters (μ=0.5, δ=1.5) are justified by one training curve (Appendix A.3). No multi-seed analysis or evaluation across the full metric suite is provided to establish statistical significance or robustness.

4. **PAA resolution alignment is not discussed.** Equation (2) assumes aligned patches between image and condition tokens at the same spatial coordinates, but no comment is made on resizing or alignment when condition map resolutions differ from the latent resolution.

5. **Evaluation is predominantly reconstruction-based.** The three tasks (Subject-Canny-to-Image, Subject-Depth-to-Image, Canny-Depth-to-Image) all generate images matching ground-truth conditions. Multi-condition control in practice often involves novel compositions (e.g., "a cat on a beach given a depth map," where no ground-truth exists). A compositional benchmark would better test generalization.

### Trivial

None.

## Nice-to-Haves

- Compare against PixelPonder (Pan et al., 2025), which addresses a similar problem in multi-condition DiTs.
- Provide an automatic keyword extraction pipeline (e.g., rule-based or LLM-based) for arbitrary prompts.
- Report end-to-end wall-clock timing (including VAE encode/decode) in addition to attention-only timing to contextualize the 10× speedup claim.
- Show attention mask visualizations for KSA overlaying the binary mask on generated images to demonstrate correct subject localization.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Missing Table 1 quantitative data (Critic's Point 2).** The parsed text does not contain the numerical data from Table 1. This is a parser artifact — the table exists in the original submission. The critic's concern about missing statistical significance (variance, etc.) is a separate valid point, but the claim that "no numerical data appears" is a formatting artifact and should be disregarded.
  
- **Missing OminiControl2's "efficient variant" comparison.** OminiControl2 (Tan et al., 2025) *is* the efficient variant of OminiControl. The paper already compares against it. The critic appears to have conflated OminiControl with OminiControl2.
  
- **Missing specification of subject encoding.** The paper builds on FLUX, where conditions are encoded via the standard VAE encoder and projected into the token space — standard practice in DiT-based multi-condition frameworks. The method is clear enough for reproducibility.
  
- **Dynamic conditions not discussed (Condition Cache).** The paper is about static conditions; criticizing the absence of dynamic-condition analysis is scope creep.
  
- **Perturbation experiment details (Section 3.3).** Appendix A.2 clearly states: "the condition is removed at different timesteps." The experiment is on OminiControl (not the authors' model), which is honestly reported. The critic's concerns about transferability are noted but the experiment is described.
  
- **10× speedup vs. Figure 9 discrepancy.** Figure 9 is a single-condition ablation of PAA; Figure 7 reports speedup across multiple conditions. These measure different regimes — the 10× figure applies when many conditions create a large quadratic baseline, not to the single-condition ablation. The critic conflated the two.
  
- **Section 3.1 Eq. 1 — QKV computation.** In standard multi-modal attention, Q, K, V are computed from the full concatenated sequence. The notation is standard and unambiguous in the DiT literature.

## Novel Insights

The reviews surface an important tension not fully discussed in the paper: the method's reliance on curated keyword-bearing captions and reconstruction-based evaluation tasks means its applicability to open-ended, compositional multi-condition generation remains unvalidated. The paper's strongest conceptual insight — that different condition types exhibit qualitatively different sparsity patterns (diagonal alignment vs. keyword-triggered activation) — is genuinely useful and could inform future efficient attention designs beyond the specific PAA/KSA instantiation. However, the reviews collectively highlight that the experimental framework is not yet robust enough to support the contribution claims.

## Suggestions

1. **Run controlled baseline comparisons.** Fine-tune OminiControl2 and UniCombine under the same LoRA configuration, data, iteration count, and optimizer as the proposed method. Report FID, DINOv2, CLIP-I, F1, and MSE for all methods with variance. This is the single most important improvement needed.

2. **Add quality metrics to ablations.** Report FID and controllability metrics (F1, MSE) for the PAA ablation comparing full attention, SWA variants, and PAA. Report CLIP-I and DINOv2 across the test set for each KSA threshold ε. Show that quality is not degraded.

3. **Specify a keyword extraction pipeline.** Even a simple LLM-based keyword extractor with a few examples would significantly improve reproducibility.

4. **Recompute KSA mask periodically** and ablate against single-computation reuse to verify that temporal consistency justifies the current design.

5. **Test on compositional (non-reconstruction) tasks** to demonstrate generalizability beyond the current setup.

## Score and Decision

**Calibration anchors** (all from the human-review corpus):

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/eD8IPvNoZB.md` (SLA) | 5.00 | SLA has similar efficient-attention motivation but provides GPU kernel implementation, quality metrics in ablations, and thorough experimental validation. Current paper is weaker on experimental rigor. |
| `/home/wg25r/review_agent/human_reviews_2026/uXmbrTlko7.md` (ScalingCache) | 5.00 | Training-free caching with experiments across 3 major model families and comprehensive fidelity metrics. Current paper experiments on only one base model (FLUX) with less thorough metrics. |
| `/home/wg25r/review_agent/human_reviews_2026/V3eUas3VCL.md` (DiffSparse) | 4.50 | Token sparsity with learnable allocation, tested on 4 model families. Current paper's conceptual framework is cleaner but experimental scope is narrower. |
| `/home/wg25r/review_agent/human_reviews_2026/3Z3Is6hnOT.md` (Fast-dLLM) | 7.00 | Thorough theoretical grounding, comprehensive ablations, multiple benchmarks. Current paper lacks comparable experimental depth. |
| `/home/wg25r/review_agent/human_reviews_2026/kI27Niy4xY.md` (VIST3A) | 8.00 | Novel framework with thorough experiments across model pairs and ablations. Current paper is far from this level of validation. |
| `/home/wg25r/review_agent/human_reviews_2026/OPFE1zPYbU.md` (Rethinking Diffusion...) | 1.00 | Fundamentally flawed with no real contribution. Current paper is substantially better — does have genuine contributions and plausible methodology. |
| `/home/wg25r/review_agent/human_reviews_2026/DDcrkBwzec.md` (ECM) | 4.50 | Similar topic (efficient conditional generation), similar issues with incomplete experimental validation. Comparable quality level. |

The paper's core idea is clean, well-motivated, and addresses a real bottleneck. However, the experimental validation has two major gaps — uncontrolled baseline comparisons and ablation studies that lack quality metrics — that prevent verification of the central claim. Stronger papers in the same area (SLA, ScalingCache, DiffSparse) provide more thorough experimental frameworks and were accepted at poster level. In its current form, this paper falls short of the bar set by those works.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>