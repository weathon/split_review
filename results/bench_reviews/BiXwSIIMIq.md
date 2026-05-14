Now I have all the information I need. Let me produce the final review.

## Summary

This paper introduces AC-DC, a three-stage score-based denoiser (auto-correction via additive noise, directional correction via conditional Langevin dynamics, and Tweedie/ODE denoising) designed to mitigate the manifold mismatch between ADMM iterates and the Gaussian-noise-trained score functions. The authors provide the first convergence guarantees for score-based denoisers within ADMM-PnP: a weakly-nonexpansive fixed-point ball convergence under constant step size (strongly convex loss) and bounded-denoiser convergence under adaptive step size (nonconvex loss). Experiments on six inverse problems across FFHQ and ImageNet show consistent improvements over nine baselines.

## Strengths

- **First convergence theory for score-based denoisers in ADMM**: Theorems 1–3 extend prior ADMM-PnP fixed-point convergence theory (Ryu et al., 2019; Chan et al., 2016) to score-based settings, establishing weakly nonexpansive and bounded-denoiser properties for the AC-DC denoiser under mild conditions (Sections 4.1–4.3). This is a nontrivial extension because prior convergence results for score-based PnP covered only primal algorithms.

- **The AC-DC denoiser is a well-motivated and principled solution to a real obstacle**: The paper identifies that ADMM dual variables further distort the noise geometry of iterates beyond what primal PnP methods face, and designs a three-stage denoiser to address this. The DC step (conditional Langevin dynamics) is a genuine addition beyond standard noise-injection schemes. The ablation in Figure 5 qualitatively demonstrates that DC steps progressively improve reconstruction (J=0→10→20).

- **Broad and competitive experimental validation**: Evaluated on six inverse problems (super-resolution, random/box inpainting, Gaussian/motion deblurring, phase retrieval) × two datasets (FFHQ, ImageNet) × nine baselines (DPS, DAPS, DDRM, DiffPIR, RED-diff, DPIR, DCDP, PMC). Ours-tweedie achieves best or second-best PSNR on 11 of 12 task-dataset combinations in Table 1, often by substantial margins (e.g., 32.84 vs. 29.08 for DPS on random inpainting FFHQ).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theory–practice gap in the DC step (partially addressed)**: Theorems 2 and 3 state convergence results under the assumption that the DC Langevin dynamics reach the stationary distribution at each iteration, while the implementation uses J=10 steps. The paper references Appendix E.2 for non-stationary counterparts, which mitigates but does not fully remove this gap. The analysis also assumes exact solution of the x-subproblem (7a), whereas practice uses up to 1000 Adam iterations with early stopping. These divergences between the analyzed algorithm and the implemented one would benefit from empirical verification (e.g., showing primal/dual residual trajectories behave as the theory predicts).

- **Missing computational cost analysis**: The AC-DC denoiser uses J=10 Langevin steps per ADMM iteration (plus ODE steps for Ours-ode), which implies potentially many more score evaluations than baselines. The paper does not report NFE counts or wall-clock time for any method, making it difficult to assess whether the gains come from the method's design or from additional compute. A fair comparison would require cost-controlled evaluation.

- **No quantitative ablation of the DC component on a test set**: Figure 5 shows the effect of DC steps (J=0,10,20) on only a single image example. Quantitative ablation over 100 images (PSNR/SSIM/LPIPS for different J values) would substantiate the claim that DC is responsible for the quality lift, rather than just the AC stage.

- **Undefined notation in Algorithm 1**: The DC update uses `σ_{z_t}` without definition. The derivation text surrounding Equation (10) uses `σ_ac^(k)` instead, creating confusion about which noise level parameter enters the Langevin correction.

- **Adaptive step-size theory not empirically validated**: Theorem 3 provides convergence guarantees under an adaptive ρ schedule, but all experiments use constant ρ. The paper acknowledges this in the limitations section, but the theory for the nonconvex, adaptive case remains untested.

- **Dual-variable distortion claim is asserted but not isolated**: The paper motivates ADMM's difficulty by claiming dual variables "further distort the noise geometry," but provides no controlled experiment (e.g., comparing ADMM-PnP vs. proximal gradient with the same AC-DC denoiser) to isolate this effect. This weakens the stated motivation for focusing on ADMM specifically.

### Trivial
- The notation σ_{z_t} in Algorithm 1 line 5 requires explicit definition to avoid confusion with σ_ac^(k) used in the derivation.

## Nice-to-Haves
- An empirical convergence plot (primal and dual residuals over ADMM iterations) to connect the practical behavior with the fixed-point ball theory.
- A runtime/NFE table so readers can assess the computational cost of the additional DC steps relative to baselines.
- A quantitative DC ablation (PSNR vs. J) over the full 100-image test set.
- An experiment comparing ADMM-PnP to a primal-only PnP method (e.g., proximal gradient) with the same AC-DC denoiser to empirically justify the "dual-variable distortion" motivation.

## Removed Points
These points are flagged to be removed; treat them with caution:
- *"Incomplete tables, duplicated/blank entries in Table 1"* — These are parser-induced formatting artifacts from the PDF extraction, not author errors. The original submission's table is properly formatted.
- *"Equation (9) and following paragraph garbled/uninterpretable"* — Parser artifact; the original manuscript is clean.
- *"Notation switches confusingly between z and ẑ"* — The notation tracks the different processing stages (ẑ^(k) → z_ac^(k) → z_dc^(k) → z_rw^(k)) and is sufficiently clear.
- *"Unique advantage of DC over existing correction mechanisms not clearly established"* — The ablation in Fig. 5 (J=0 vs J=10 vs J=20) and the quantitative comparisons against baselines that use noise injection (DiffPIR, DPS) empirically establish DC's advantage.
- *"Multiple PMC rows in Table 1"*, *"missing hyperparameter declarations"* cited without specificity — Parser artifacts.

## Novel Insights
The most interesting observation across the reviews is the methodological tension: the paper provides convergence theory that relies on idealized assumptions (stationary Langevin dynamics, exact subproblem solves) that are not met in practice, yet the experiments demonstrate clear and consistent improvements. This raises the question of whether simpler analyses (e.g., bounded-denoiser plus diminishing noise, which Theorem 3 sketches under adaptive scheduling) could explain the practical success of the constant-step-size implementation, and whether the weakly nonexpansive analysis is necessary for explaining the observed results. The paper is transparent about this gap but does not bridge it.

## Suggestions
1. **Report NFEs and wall-clock time** for every method in Table 1 to enable cost-controlled comparisons.
2. **Add a quantitative DC ablation** over the full test set: report PSNR/SSIM/LPIPS for J ∈ {0, 5, 10, 20} on all 100 images.
3. **Define σ_{z_t} explicitly** in Algorithm 1 or in the notation appendix, and align it with σ_ac^(k) from the derivation.
4. **Include residual-convergence plots** (primal and dual residuals vs. ADMM iteration) for one or two representative tasks to visually connect with the fixed-point ball theory.
5. **Consider running at least one experiment** with the adaptive ρ schedule from Theorem 3 to validate the nonconvex convergence theory.

## Score and Decision

### Calibration Anchors
- **8pQsiFyTQi.md** (RISP, avg 6.0, Accept Poster): Convergence theory for score-based priors in RED with momentum. Weaker experimental breadth (fewer tasks/datasets) and simpler method (RED-style, not ADMM). The current paper has broader experiments and a more novel denoiser design.
- **voMeZVAkKL.md** (FAST-DIPS, avg 6.0, Accept Poster): ADMM-style splitting with analytic steps for diffusion priors. Stronger on computational efficiency analysis, but uses only FFHQ and has less novel methodological contribution. Comparable overall.
- **oJP8Geymcr.md** (PnP-CM, avg 4.0, Withdrawn/Reject): Consistency models in PnP-ADMM. Limited novelty (direct combination of existing components), missing ablations, single dataset. The current paper is substantially stronger in novelty and experimental breadth.
- **EKLhCNjzQR.md** (ZO-APMC, avg 4.5, Reject): Derivative-free posterior sampling with SGM priors. Strong theory but impractical bounds, niche setting, weaker experiments. The current paper has more practical impact and stronger experiments.
- **GK9yjjuyRT.md** (NLNP, avg 2.5, Reject): Poorly explained method, unclear contributions, insufficient experiments. The current paper is far superior in clarity, experimental rigor, and contribution.
- **qYDObsHldZ.md** (avg 4.0, Accept Poster): Simple adaptive-moment plug-in for diffusion sampling. Weak theory but strong empirical results. The current paper has both a novel method and convergence theory.
- **T6yNe9iZOj.md** (CGRS, avg 3.0, Reject): Consistency-guided reverse sampling. Limited novelty and weak experiments. The current paper is clearly stronger.

The paper under review sits above the 4–4.5 papers (PnP-CM, ZO-APMC) and is comparable to the 6.0-level accepted posters (RISP, FAST-DIPS). Its strengths—a novel three-stage denoiser targeting a real problem, the first convergence analysis for score-based denoisers in ADMM, and broad competitive experiments—outweigh the minor weaknesses (theory-practice gap partially addressed via appendix, missing NFE analysis, notation issue). The contributions are substantive and the presentation is clear.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>