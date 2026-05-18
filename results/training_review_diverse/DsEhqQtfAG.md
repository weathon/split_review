Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

This paper proposes Decomposed Diffusion Sampling (DDS), which replaces the expensive manifold-constrained gradient (MCG) computation in diffusion-based inverse problem solvers with efficient conjugate gradient (CG) iterations on the denoised (Tweedie) estimate. The method achieves state-of-the-art reconstruction quality on multi-coil MRI and 3D CT while reducing the number of function evaluations by 40–80× compared to prior diffusion-based solvers. The empirical contributions are substantial and clearly demonstrated across multiple modalities, sampling parametrizations (VP/VE), and noise conditions.

## Strengths

- **Dramatic acceleration with improved quality.** On multi-coil MRI (Uniform 1D ×4), DDS with 49 NFE achieves 34.61 PSNR / 0.956 SSIM, outperforming Score-MRI (33.25 PSNR, 4000 NFE) and DPS (30.56 PSNR, 1000 NFE). On 8-view sparse-view CT, DDS VP (49 NFE) achieves 33.86 PSNR vs. DiffusionMBIR's 33.49 PSNR (4000 NFE). These results are consistently verified across tables in the paper, supporting the claim of ≥80× speedup with superior or competitive quality.

- **Clean ablation isolating the CG contribution.** Table 2 (ablation) compares Score-MRI, DDNM, and DDS under identical DDIM sampling (49 NFE, uniform 1D ×4). DDS (34.61 PSNR) substantially outperforms both DDNM (31.36) and Score-MRI (26.48), with 5 CG iterations striking an optimal balance. This directly isolates the CG-based data consistency as the source of improvement.

- **Broad applicability demonstrated.** The method is evaluated on multi-coil MRI (including non-Cartesian NUFFT), 3D CT (sparse-view and limited-angle), VP and VE parameterizations, and noisy measurements — covering a wider range of realistic settings than most prior DIS work.

- **Practical advantages.** DDS avoids backpropagation through the denoiser (required by DPS) and eliminates step-size tuning (required by gradient-based DIS methods), both of which are non-trivial practical benefits.

## Weaknesses

### Fatal

None.

### Major

- **The core theoretical claim is conditional on an unverified premise.** The paper argues that if the tangent space at a denoised sample equals a Krylov subspace of the forward operator, then CG updates remain in the tangent space and no MCG is needed. While the paper is transparent about the "if" (lines 246–253 state "Suppose, furthermore, that..."), it provides no evidence — theoretical or empirical — that this condition holds in practice. The tangent space of the data manifold is a geometric object determined by the data distribution; the Krylov subspace is defined solely by the linear operator **A** and the residual. There is no a priori reason these should coincide, and the paper's brief appeal to "piece-wise linear regions" (line 229) does not bridge this gap. This does not invalidate the method — the empirical results are strong — but the paper's framing as a "synergistic combination" with a "principled justification" (abstract, intro) overreaches relative to what is actually established. The method would be better described as an empirically motivated heuristic with a plausible but unverified geometric interpretation.

### Minor

- **The logical flow from Proposition 1 to the multi-step CG argument is not fully connected.** Proposition 1 shows that under an affine-subspace assumption, the DPS/MCG update reduces to a projected gradient. The paper then jumps to doing multi-step CG within the tangent space, introducing the Krylov subspace condition as a separate argument. The connection between these two pieces — why Proposition 1 motivates using CG specifically — is not clearly articulated, making the theoretical narrative feel disjointed.

- **Noisy reconstruction experiments are limited.** Only one noise level (σ=0.05) and two mask patterns are evaluated. While the paper correctly notes that SVD-based methods (DDNM) are inapplicable here, a broader evaluation across noise levels would strengthen the claim of robustness.

- **Hyperparameter η is tuned per NFE.** The paper reports η=0.15 for 19 NFE, η=0.5 for 49 NFE, η=0.8 for 99 NFE. While this tuning is common in practice, it somewhat reduces the method's claimed generality and introduces a free parameter that could affect reproducibility across different settings.

- **VE parametrization instabilities acknowledged but not analyzed.** The paper notes that VE suffers from numerical instability with large NFE (line 385), which limits the claimed generality of being applicable "regardless of parametrization." The source of this instability is not discussed.

### Trivial

None.

## Nice-to-Haves

- An empirical analysis showing how much CG updates actually deviate from the tangent space (e.g., using the denoiser's Jacobian to estimate the tangent space and computing the projection residual) would either validate or clarify the theoretical motivation.
- Reporting condition number estimates for the imaging operators used would help understand CG convergence behavior and guide the choice of M (number of CG steps).
- A dedicated limitations/discussion section covering failure cases (e.g., very high acceleration factors, severely ill-conditioned forward operators) would improve scientific completeness.

## Removed Points

The following criticisms from the harsh reviewer are removed because they are factually incorrect or the paper already addresses them:

- **"The paper does not analyze the computational cost of CG relative to the cost of the diffusion denoiser"** — The paper explicitly reports this (line 359): "a single CG iteration takes about 0.004 sec" and compares analytic (4.51 sec) vs. CG(5) (4.71 sec).
- **"The paper does not compare against DPS with DDIM"** — Line 348 explicitly states: "for DPS, we use the DDIM sampling strategy to show that the strength of DDS not only comes from the DDIM sampling strategy but also the use of the sampling together with the CG update steps."
- **"More comparisons with DDNM for noisy cases... the authors should explain why"** — The paper already explains (lines 421–423): "methods that try to cope with measurement noise via SVD... are not applicable and cannot be compared."
- **"Insufficient comparison" / "overstated novelty"** — The paper compares against 6+ DIS methods (Score-MRI, Jalal et al., DPS, DDNM, DiffusionMBIR, MCG, Score-Med) across two major modalities, plus supervised and CS baselines. The baseline set is comprehensive for the settings studied.
- **"The 80× faster claim should be stated more clearly"** — The paper provides wall-clock times (4.7 sec for 49 NFE on RTX 3090) and explicitly attributes the speedup to NFE reduction with minimal per-step CG overhead, which is appropriate.

## Novel Insights

The key observation that bridges the harsh critic's and strength finder's perspectives is this: the paper's real contribution is an effective computational shortcut (replacing backprop-through-denoiser with CG on the denoised estimate), but it is framed as a theoretical insight about manifold geometry and Krylov subspaces. The empirical results are strong enough that the method stands on its own as a practical contribution; the theoretical scaffolding is at best suggestive and at worst a distraction from what is actually a clever engineering insight. A reader interested in the method's practical value will find plenty of evidence; a reader interested in a principled understanding of why it works will find only a conditional argument with an unverified premise. This mismatch between framing and substance is the paper's central weakness, not any flaw in the experiments or the algorithm itself.

## Suggestions

1. Reframe the theoretical contribution: explicitly describe the Krylov subspace condition as a **sufficient condition** that motivates the method but is not verified, and position the paper's primary contribution as an empirically effective and computationally efficient heuristic. The empirical results do not need the theoretical justification to be compelling.

2. Add an empirical analysis measuring how far CG updates deviate from the estimated tangent space (e.g., via the denoiser's Jacobian). This would either validate the geometric motivation or provide a more honest characterization.

3. Expand the noisy reconstruction experiments to at least two noise levels and additional mask patterns.

4. Include a brief discussion of limitations and failure cases (e.g., very high acceleration factors where DDS underperforms).

5. For the VP/VE generality claim, add a short analysis of when and why VE becomes unstable.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>