## Summary

The paper proposes AC-DC, a three-stage score-based denoiser (Auto-Correction via additive Gaussian noise, Directional Correction via Langevin dynamics, and Tweedie/ODE denoising) designed for integration into ADMM plug-and-play for solving inverse problems. It addresses the manifold mismatch problem where ADMM iterates deviate from the noisy manifolds on which score functions are trained. The paper provides convergence theory (weakly nonexpansive residuals → fixed-point ball convergence under constant step size; bounded denoiser → adaptive step-size convergence) and evaluates on seven inverse problems on FFHQ and ImageNet.

## Strengths

1. **Novel AC-DC denoiser design targeting ADMM-specific manifold mismatch.** The paper identifies a genuine gap: score functions are trained on Gaussian-noised manifolds, but ADMM iterates — especially with dual variables — have unknown noise geometry. The three-stage AC→DC→denoising design is well-motivated and directly addresses this challenge. The ablation in Figure 5 (phase retrieval) qualitatively shows that increasing DC steps from 0 to 20 progressively removes artifacts, providing concrete evidence that the DC stage contributes beyond simple noise injection.

2. **Convergence theory extending ADMM-PnP to score-based denoisers.** Theorem 1 shows that under weak nonexpansiveness of the denoiser residual (relaxing the strict contractiveness required by prior work), ADMM-PnP converges to a fixed-point ball under constant step size and strongly convex losses. Theorem 2 establishes that the AC-DC denoiser satisfies this property with high probability. Theorem 3 removes convexity via an adaptive step-size schedule. These extend prior ADMM-PnP convergence theory (Ryu et al., 2019; Chan et al., 2016) to the score-based setting — a nontrivial extension.

3. **Honest limitations discussion.** Section 7 candidly acknowledges the key gaps: constant step-size convergence for nonconvex objectives remains unproven, noise schedules are heuristic, and NFE cost is high. This transparency strengthens confidence in the claims that are supported.

## Weaknesses

### Major

1. **Incomplete and inconsistent baseline reporting in Table 1 undermines the empirical claims.** Several distinct problems:
   - **Naming ambiguity.** The baseline list (line 295) includes both DPIR (classical denoising PnP) and DiffPIR (diffusion-based PnP) as separate methods. Table 1 uses "DiPIR" consistently, but neither "DPIR" nor "DiffPIR" appears by name. Since these are distinct methods with different operating principles, the reader cannot determine which is being compared.
   - **Unannounced method.** "DDPM" appears in the Gaussian blur block (line 352) without being listed among the eight baselines or explained anywhere in the paper.
   - **Duplicate/empty PMC entries.** Super-resolution has two PMC rows with *different* numerical values (lines 324–325). Motion deblur, Gaussian blur, and box inpainting have empty duplicate PMC rows, suggesting a data-handling error that makes the PMC comparison unreliable.
   - **Selective baseline coverage.** Motion deblur reports only Ours, DAPS, DPS, and PMC — missing DDRM, DiffPIR/DiPIR, RED-diff, and DCDP. Phase retrieval reports a similarly sparse set. The paper claims "Our method significantly outperforms other PnP baseline methods considered, namely, DDRM, DiffPIR and RED-diff" (line 303), but for motion deblur and phase retrieval, these baselines are absent entirely.
   
   These gaps do not invalidate the results that *are* presented, but they prevent a fair assessment of whether the method outperforms competitors consistently. A reader cannot determine from Table 1 whether the playing field is level.

2. **No compute-adjusted comparison despite likely large NFE disparity.** The AC-DC denoiser uses J=10 Langevin steps (each a score NFE) per ADMM iteration plus a denoising step, and the x-subproblem (7a) is solved with up to 1000 Adam iterations per ADMM pass. Baselines like DPS and DDRM run a single diffusion trajectory; DiffPIR does one denoising call per iteration. The paper reports no wall-clock times, NFEs, or compute-normalized comparisons. The Limitations section acknowledges this as a concern, but the evaluation provides no context for interpreting whether gains are due to algorithmic design or higher compute budget. This is a structural gap in the empirical evidence.

### Minor

3. **Convergence theory does not cover the actual experimental setup.** Theorem 1 (constant step size) requires strong convexity of ℓ, which the paper acknowledges does not hold for phase retrieval, inpainting, or super-resolution — yet the method is applied to these tasks with constant step sizes. Theorem 3 removes convexity but requires adaptive step sizes, while experiments use constant step sizes. Additionally, Theorems 2–3 assume the DC Langevin dynamics reaches stationarity, while only J=10 steps are used for 256×256×3 images — far from mixing. Footnote 1 promises a relaxation in the appendix, but this is not accessible in the main text. The paper is transparent about these gaps in Section 7, but the disconnect between theory and practice remains significant.

4. **Limited quantitative ablation.** The DC ablation (Figure 5) is qualitative and only on phase retrieval. No quantitative PSNR/SSIM/LPIPS ablations for varying J, no ablation of the AC stage alone vs. AC+DC, and no ablation on other tasks. This makes it difficult to assess whether the DC contribution is consistent or task-dependent.

5. **Inner optimization underspecified.** Subproblem (7a) is solved with "Adam optimizer for maximum of 1000 iterations" with convergence detected by loss increase over a 3-iteration window, but the learning rate, Adam betas, and other optimizer details are not reported.

### Trivial

6. Table formatting: duplicate rows, ambiguous method names, unannounced entries should be cleaned up.

## Nice-to-Haves

- A compute-normalized analysis (NFE counts or wall-clock time) for at least one representative task.
- Quantitative ablations of DC steps (J) on multiple tasks.
- Standard deviations over the 100 test images to assess variability.
- Learning rate and optimizer settings for the inner subproblem solver.

## Removed Points

Points from inputs that were filtered after verification against the paper:
- "No code link" — REMOVED (per guidelines, citations are assumed to correspond to existing resources; code release is not required).
- "Justification for Langevin approximation is thin" — MOVED to Nice-to-Haves (the paper provides a theoretical approximation argument; empirical validation would strengthen but the argument is reasonable).
- "No statistical significance / confidence intervals" — MOVED to Nice-to-Haves (single-run reporting on 100 images is standard for large-scale benchmarks in this field).
- "The δ-ball notion is a very weak form of convergence" — WEAKENED (the paper is transparent about this being fixed-point ball convergence and acknowledges stronger results exist for other denoiser classes).
- "Strength: addresses an important problem" (generic) — REMOVED; only strengths with concrete evidence were retained.
- "Strength: clear positioning" — kept with specific citation to Section 5.

## Novel Insights

Beyond the paper's own contributions, the key synthesis from the reviews is that the AC-DC design's separation of correction into a noise-injection step (AC) followed by conditional Langevin refinement (DC) provides a principled response to a problem (manifold mismatch in primal-dual optimization) that prior score-based PnP methods largely sidestepped by using simpler noise injection alone. The convergence analysis, while not covering the exact experimental protocol, is a nontrivial structural extension of ADMM-PnP theory. The candid limitations section is a genuine strength. The main weakness is that the empirical evaluation — which should be the paper's centerpiece — has enough gaps and inconsistencies (incomplete baselines, ambiguous naming, likely data-entry errors) to prevent full confidence in the claimed improvements.

## Suggestions

1. **Clean up Table 1 decisively.** Clarify the "DiPIR" naming (use "DPIR" or "DiffPIR" as appropriate), explain or remove "DDPM," fix the duplicate PMC entries, and either fill in missing baselines for all tasks or explicitly explain their absence. This is the single most impactful fix and would substantially improve the paper.

2. **Add compute context.** Report NFE counts and/or wall-clock time for each method on at least one representative task to show whether gains reflect algorithmic design or higher compute budget.

3. **Quantify the ablation.** Report PSNR/SSIM/LPIPS for varying J on at least two tasks, and ablate the AC stage separately.

4. **Report optimizer settings.** Provide the learning rate and Adam parameters for the inner subproblem solver.

---

## Score Calibration

**Calibration Anchors (all rounds):**

| Round | Path | Avg Score | Decision | Comparison |
|-------|------|-----------|----------|------------|
| R1 | dAavOuxZvo (VIPaint) | 3.00 | Reject | Much weaker; simple diffusion inpainting without theory |
| R1 | LwAG269lIq (PDE Discovery) | 3.00 | Reject | Unrelated topic |
| R1 | R5FzCFR5yU (Hybrid PINNs) | 3.33 | Reject | Unrelated topic |
| R1 | IfPfUHRowT (Sinogram Inpainting) | 3.25 | Reject | Unrelated topic |
| R1 | **HXjXPQU3yJ (Prior Mismatch PnP-ADMM)** | **6.25** | **Reject** | **Very similar topic; cleaner experiments but less novel method. Current paper is below this anchor.** |
| R1 | **x7d1qXEn1e (Restoration Network)** | **6.25** | **Accept** | **Similar PnP+theory scope; stronger convergence result (stationary point). Current paper is below this anchor.** |
| R1 | GKAQ92ua3A (ADMM Nonconvex) | 6.00 | Accept | Pure optimization theory; less comparable |
| R1 | **kNPcOaqC5r (Learned Proximal Networks)** | **5.75** | **Accept** | **Comparable: both have notable issues but solid core contributions** |
| R1 | 6O3Q6AFUTu (NoiseDiffusion) | 8.00 | Accept | Clearly stronger; image interpolation, different scope |
| R1 | 6EUtjXAvmj (Variational DPS) | 8.00 | Accept | Clearly stronger; diffusion posterior sampling |
| R2 | **Z9Odi09Rv9 (Frequentist Diffusion)** | **4.75** | **Reject** | **Below current paper; had technical errors in Tweedie's formula** |
| R2 | **66arKkGiFy (PnP-ULA Mismatched)** | **5.75** | **Accept** | **Similar PnP+theory; cleaner experiments but more incremental contribution** |
| R2 | DsEhqQtfAG (Decomposed Diff Sampler) | 6.50 | Accept | Stronger; Krylov+diffusion for large-scale problems |
| R2 | **kRBQwlkFSP (DiffStateGrad)** | **6.75** | **Accept** | **Stronger empirical work on similar manifold mismatch problem** |

**Round 1 bracket:** [4.0, 6.5] — below the 7.5+ strong papers, above the ~3.0 weak papers.

**Round 2 narrowing:** The most comparable anchors sit at 5.75–6.75. The current paper is below Prior Mismatch PnP-ADMM (6.25) and DiffStateGrad (6.75) due to more severe empirical flaws, and comparable to or slightly below Learned Proximal Networks (5.75) and PnP-ULA Mismatched (5.75). The genuine methodological novelty is a strength, but the Table 1 issues are substantial enough to pull the score down. **Final score: 5.0.**

---

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>