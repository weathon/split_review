Now I have enough information to produce the final consolidated review.

---

## Summary

This paper proposes EffiDPSRecon, an efficient diffusion posterior sampling method for CT reconstruction at reduced radiation doses. The method integrates three components—(1) a conjugate gradient (CG) projection onto the data-consistency manifold, (2) a forward resampling step that re-noises the data-enhanced estimate before a DDIM reverse step, and (3) FBP-based initialization to start the reverse process at a much earlier timestep (N′=50 instead of 1000). Experiments on LDCT (three dose levels) and sparse-view CT (32, 64, 96 views) from the Mayo Clinic dataset show that the method achieves an average ~3.5 dB PSNR improvement over DPS and MCG while requiring roughly 10% of their computation time.

## Strengths

- **Significant acceleration with improved quality**: Table 2 shows DPS and MCG take ≥5 minutes per slice while EffiDPSRecon takes ~30 seconds (~10× faster), and Table 1 shows it achieves the highest PSNR/SSIM across all six test conditions. The acceleration and quality gains are demonstrated jointly rather than traded off.

- **Consistent quantitative superiority**: EffiDPSRecon outperforms all baselines (FBP, ADMM-TV, FBPConvNet, DPS, MCG) in every scenario—three LDCT dose levels and three sparse-view counts—with gains of roughly 2–4 dB over the next-best method depending on the setting.

- **Robustness to aggressive step reduction**: Figure 3 shows that when the number of reverse steps is reduced from 1000 to as few as 10–100 (with matching FBP initialization), EffiDPSRecon maintains high PSNR while DPS and MCG degrade sharply. This validates the claim that the method can operate at 50 steps without fidelity loss.

- **Ablation confirms both novel components matter**: Table 3 shows that removing either the CG projection or the forward sampling step reduces PSNR by 1–2 dB, providing evidence that both proposed mechanisms contribute to performance beyond what either alone provides.

- **Two clinically relevant scenarios**: The method is evaluated on both low-dose noisy CT (varying photon counts) and sparse-view CT (varying projection counts), demonstrating generality across different dose-reduction strategies.

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablation of the FBP initialization.** The ablation study (Table 3) tests removal of CG and forward sampling, but never tests what happens when the FBP initialization is replaced with a random Gaussian draw at the same reduced timestep (N′=50). The acceleration claim hinges on reducing steps from 1000 to 50, and the FBP initialization is presented as a key enabler. Without this ablation, it is unclear whether the performance at few steps is driven by the proposed sampling recipe (CG + forward resampling) or simply by the FBP starting point. Figure 3 shows that DPS and MCG *fail* with FBP init at few steps, suggesting that initialization alone is insufficient—but a direct (b) condition (EffiDPSRecon without FBP init) is needed to complete the argument.

2. **Narrow comparison to other diffusion-based methods.** The paper claims "over ten times faster than existing diffusion-based techniques" and "state-of-the-art" performance, yet only compares against two specific diffusion methods (DPS and MCG, both from 2022–2023) run at 1000 steps. By the current date, there are other approaches for accelerated diffusion sampling in inverse problems (e.g., reduced-step variants, better initialization strategies applied to other backbones). Without a broader comparison set or a more measured framing, the reader cannot determine whether the contribution is the specific algorithmic recipe or whether similar gains are achievable by simply applying FBP initialization and data-consistency steps to other diffusion backbones. The paper does include non-diffusion baselines (FBP, ADMM-TV, FBPConvNet), which is helpful, but the central "fastest diffusion" claim requires more support.

3. **The forward resampling step may create a distribution mismatch for the score network.** In Equation (22), the method samples \(x_t(\mathbf{y}) = \sqrt{\bar{\alpha}_t} \hat{\mathbf{x}}_0(\mathbf{y}) + \sqrt{1-\bar{\alpha}_t}\, z\), where \(\hat{\mathbf{x}}_0(\mathbf{y})\) is a CG-corrected estimate rather than a true data sample. The score network \(\epsilon_\theta\) is trained on forward-processed *true* images. Evaluating it on inputs constructed from a CG-projected estimate could produce out-of-distribution inputs, especially at low noise levels where the noise direction \(z\) may not align with the diffusion forward path. The paper asserts that this step "aligns with the forward process" (line 183–184) but does not analyze whether the resulting inputs lie in-distribution for the score network. This is a genuine concern about the method's robustness and a potential failure mode that is unexamined.

### Minor

1. **Ambiguous "3.5 dB" baseline.** The abstract and introduction state "an average PSNR improvement of 3.5 dB" without specifying the reference method. From Table 1, the gain relative to the best competitor varies by task (ranging from ~2.4 dB to ~4.3 dB depending on the condition and comparison method). The claim would be clearer if it stated the comparator explicitly (e.g., "3.5 dB over DPS on average").

2. **Lack of robustness/sensitivity analysis.** The method involves two tunable hyperparameters—the step size \(\rho_t\) and the number of CG iterations \(k\)—neither of which is studied. Showing performance under a range of these values, or a simple sensitivity plot, would strengthen the contribution and help practitioners apply the method.

3. **No discussion of failure cases or limitations.** The paper does not discuss scenarios where the method might struggle (e.g., extremely low dose or very few views where diffusion models may hallucinate). Acknowledging limitations would add credibility.

### Trivial

- **Computational cost breakdown.** The paper reports total seconds per slice but does not break down time between CG, network evaluation, and Radon transform operations. A per-component breakdown would help readers judge scalability and identify bottlenecks.

- **"Projection" via CG is not a true projection.** The paper describes CG as a projection onto \(\mathcal{M}_0\) (the normal-equation solution set), but a finite-step CG from a specific initialization does not guarantee an orthogonal projection in the strict sense. Clarifying what "projection" means here would improve precision.

## Nice-to-Haves

- Add an ablation comparing EffiDPSRecon with random initialization at N′=50 to isolate the contribution of FBP initialization from the rest of the sampling recipe.
- Add an analysis of whether the forward-resampled inputs \(x_t(\mathbf{y})\) are in-distribution for the score network (e.g., by comparing LPIPS distances to true forward-process samples at the same \(t\)).
- Sensitivity analysis for \(\rho_t\) and \(k\) (number of CG steps).

## Removed Points

- *Criticism about "+" and "−" signs used interchangeably.* This is a PDF parsing artifact, not an author error.
- *Recommendation to compare against specific named methods (DDNM, PnP diffusion, RedDIff).* Per guidelines, I cannot confirm the existence or applicability of these methods to CT reconstruction, and missing-related-works critiques are not allowed.
- *"Comparison to a learned iterative method (e.g., unrolled ADMM).* The paper already includes ADMM-TV (iterative regularized reconstruction) and FBPConvNet (supervised DL method). This request is redundant given the existing baselines.
- *Some of the "Strengthening the Paper on Its Own Terms" suggestions* that are restatements of points already covered in the weaknesses above. These are preserved in the weaknesses section in distilled form.

## Novel Insights

The notion of using *two* data-consistency steps per diffusion iteration—one in the image domain (CG projection of the posterior mean) and one at the noise level (forward resampling before DDIM)—is an interesting architectural departure from the single-correction approaches in DPS and MCG. The key insight, which the paper could develop further, is that data consistency may be more effective when applied to the denoised estimate \(\hat{x}_0\) rather than to the noisy latent \(x_t\) (as in DPS/MCG). The forward resampling step then bridges the cleaned estimate back to the correct noise level for the diffusion model's score function. This two-stage design (correct then re-noise) is pragmatically motivated, and its empirical success suggests a design principle worth formalizing.

## Suggestions

1. **Add the missing FBP-init ablation.** Test EffiDPSRecon at N′=50 with random Gaussian initialization (replacing Equation 24). If performance remains high, the sampling recipe itself is driving the acceleration; if it collapses, the contribution is primarily the initialization, and the paper should reframe its claims accordingly.

2. **Broaden the comparison or moderate the claims.** Either benchmark against additional accelerated diffusion approaches or rephrase claims from "over ten times faster than existing diffusion-based techniques" to "over ten times faster than standard 1000-step DPS/MCG."

3. **Clarify the 3.5 dB baseline** by stating the comparator (e.g., "over DPS" or "over the best competing method").

4. **Add a brief limitations paragraph** discussing potential failure modes, such as very low dose or hallucination risk.

## Score and Decision

**Originality:** The method combines existing components (CG, forward resampling, FBP init) in a novel way for diffusion-based CT reconstruction, but each component is individually known. Incremental but non-trivial.  
**Importance of research question:** High—reducing radiation dose in CT while maintaining quality is an important clinical problem.  
**Claims supported:** Partially. The core empirical results (faster, better) are supported for the compared methods, but the missing FBP-init ablation and narrow comparison set weaken the strongest claims.  
**Soundness of experiments:** Adequate but incomplete (missing ablation, no sensitivity analysis).  
**Clarity of writing:** Clear in describing the method steps, though some claims are imprecisely stated.  
**Value to community:** Practical result (10× faster with higher quality) is useful, especially for clinical deployment.

The paper presents an empirically effective method with real practical merit (10× speedup with simultaneous quality improvement). However, the evidence for what drives this improvement is incomplete, and the comparison set is too narrow to fully substantiate the strongest claims ("over ten times faster than existing diffusion-based techniques"). The weaknesses are addressable through additional experiments and more measured framing. As it stands, the paper is borderline—the contribution is real but not yet fully supported.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>