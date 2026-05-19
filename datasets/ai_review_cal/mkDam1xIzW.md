- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8
Now I have all the information needed. Let me construct the consolidated review.

## Summary

This paper proposes Probabilistic Geometric Principal Component Analysis (PGPCA), which generalizes PPCA to model data that is distributed around a known nonlinear manifold (rather than around the Euclidean mean). It introduces "distribution coordinates" (Euclidean EuCOV vs. geometric GeCOV) attached to the manifold, derives an EM algorithm whose M-step reduces to the closed-form PPCA solution, and shows that log-likelihood comparison can distinguish between coordinate systems. Experiments are conducted on synthetic data (loop in ℝ²/ℝ¹⁰, torus) and neural recordings from the mouse head-direction system.

## Strengths

1. **Principled generalization of PPCA to nonlinear manifolds.** The core modeling idea — decomposing data into a manifold term φ(zₜ), a coordinate-frame term K(zₜ)Cxₜ, and isotropic noise rₜ — cleanly captures data distributed *around* a manifold (not on top of it), which distinguishes PGPCA from prior extensions (PPGA, torus PPCA) that require data to lie exactly on the manifold. (Section 3.1, Equation 1)

2. **Elegant EM derivation preserving PPCA's closed-form M-step.** The key technical result (Sections 3.4–3.5) shows that all manifold and coordinate information aggregates into a single matrix Γ(q), and the optimal C and σ² reduce to the same eigenvalue-based closed-form solution as PPCA. This is non-trivial because SVD cannot be used with a nonlinear manifold, and the result means the method inherits the efficiency guarantees of PPCA's EM algorithm.

3. **Demonstrated ability to distinguish distribution coordinates via log-likelihood.** On synthetic data, the correct coordinate system (GeCOV vs. EuCOV) consistently yields higher log-likelihood across repeated trials with statistically significant differences (paired t-test p < 1.7×10⁻¹² for loop in ℝ², p < 3.1×10⁻⁴ for loop in ℝ¹⁰; Figure 2B, 2D). This shows the framework can discriminate between coordinate hypotheses in controlled settings.

4. **Joint learning of manifold-state distribution p(z).** Section 4.3 (Figure 3) shows that PGPCA can simultaneously learn the distribution *on* the manifold (p(z)) and the distribution *around* it (C, σ²), and still correctly identify the true coordinate system. This goes beyond simply fitting residuals.

5. **Real neural data application.** On mouse head-direction circuit firing rates (Section 4.4, Figures 4B/4D), PGPCA with GeCOV consistently yields higher log-likelihood than EuCOV across all reduced dimensions for the two mice shown, and Table 2 reports results across all six mice. This provides a concrete neuroscience application matching the paper's stated motivation.

## Weaknesses

### Fatal
None. The theoretical framework is internally consistent and the derivations are logically sound.

### Major

1. **Overclaimed "hypothesis testing."** The paper repeatedly states that PGPCA performs "hypothesis testing" to choose between Euclidean and geometric coordinates (abstract, Section 4 item 2, conclusion). In reality, the procedure is model selection by comparing log-likelihoods. A proper hypothesis test requires a null distribution and Type I error control; simply selecting the model with higher likelihood does not constitute a statistical test. The paired t-tests in Figure 2B/2D are applied to repeated synthetic trials (which is a valid test for a mean difference), but this methodology is not extended to the real data, where no uncertainty quantification is provided. The framing substantially oversells the statistical rigor of the coordinate selection procedure.

2. **Empirical validation is too narrow to isolate the contribution's source.** Only PPCA and FA (both linear models) are used as baselines. The paper's main experimental comparison is PGPCA(GeCOV) vs. PGPCA(EuCOV), but there is no comparison against any nonlinear probabilistic alternative — for example, fitting a Gaussian around each manifold point (a simple "tangent-space" baseline), or applying GP-LVM (discussed in Related Work but never compared experimentally). Without a nonlinear baseline, it is unclear whether the advantage of PGPCA(GeCOV) over PGPCA(EuCOV) (Figures 4B/4D) is due to the geometric coordinate construction specifically, or simply because the coordinate system better captures the residual variance in a way that a generic nonlinear method would also capture.

3. **Real data results lack error bars and uncertainty quantification.** Table 2 reports log-likelihoods for 6 mice as point estimates with no indication of variance across runs, random initializations, or data subsamples. Figures 4B and 4D show single log-likelihood curves without error bars. The log-likelihood differences between GeCOV and EuCOV are claimed to be systematic, but without uncertainty measures the reader cannot assess whether the differences are meaningful or within noise range. The paired t-tests applied in synthetic experiments are absent from the real data analysis.

### Minor

4. **Several implementation details essential for reproducibility are not specified.**
   - **Manifold fitting:** The paper repeatedly states φ is "first fitted from data" (Sections 1, 3.2, 4.4) but never describes the fitting procedure for any experiment — not for the synthetic loop/torus nor for the real neural data (where it only cites Chaudhuri et al. 2019). Without specifying this, the method cannot be independently implemented.
   - **Landmark selection:** The discretization of p(z) via M landmarks {z₁:ₘ} is described (Section 3.3) but no guidance is given for choosing M or placing landmarks. This is a free parameter that could significantly affect results.
   - **GeCOV construction for general manifolds:** GeCOV is defined only by example (tangent+normal for a loop, two tangents+normal for a torus; Figure 1). A general prescription for constructing an orthonormal coordinate frame K(z) for an arbitrary fitted manifold is not provided.

5. **The key algebraic step from (12) to (13) is asserted rather than derived.** The derivation of $\mathcal{L}^M_1$ jumps from the expansion in equation (12) to the simplified form (13) without showing the algebraic manipulations. Given that this is the core technical result enabling the reduction to PPCA's closed form, the reasoning should be more explicit.

6. **Landmark discretization approximation error is uncharacterized.** The continuous ELBO integral is replaced by a sum over Dirac spikes (Equation 9), but there is no discussion of the approximation error or whether the EM algorithm still guarantees monotonic log-likelihood increase under this discretization.

### Trivial
7. No computational complexity analysis (e.g., O(T·M·n²) per iteration) is provided, though this is not a fatal omission for a methods paper.

## Nice-to-Haves
- A proper hypothesis testing framework for coordinate selection (e.g., parametric bootstrap likelihood-ratio test) with controlled false positive rates would substantially strengthen the claimed capability.
- A simple nonlinear baseline that respects manifold structure but uses a different coordinate approach (e.g., tangent-space-only PPCA) would help isolate the contribution of the geometric coordinates.
- Bootstrapped confidence intervals on the log-likelihood differences for each mouse in Table 2 would let readers assess effect sizes.
- Sensitivity analysis for the landmark count M and for mis-specified manifolds would clarify the method's robustness.

## Removed Points
These points are flagged to be removed; treat them with caution:

1. **"Only loop results are visualized or described in detail"** (Harsh Critic) — The paper does present torus results (Section 4.3, Figure 3, Table 2 includes "uniTorus" rows) and real neural data (Figure 4). The loop experiments receive more narrative space but all three settings are covered. *Reason for removal:* Inaccurate — torus results exist, though they are less detailed.

2. **"No quantitative metric for distribution recovery beyond log-likelihood"** (Harsh Critic) — For probabilistic generative models, log-likelihood is the standard evaluation metric. Requesting additional metrics like KL divergence is reasonable but not a deficiency given the paper's framing. *Reason for removal:* Weak/misaligned with standard practice for probabilistic models.

3. **"Figure 3 reference but missing caption"** (Harsh Critic) — Parser artifact; the original submission contains the figure and caption. *Reason for removal:* Parser artifact, not an author error.

4. **Strength: "Hypothesis testing for distribution coordinates"** (Strength Finder) — Conflicts with verified Weakness #1 (overclaimed hypothesis testing). The underlying capability (coordinate comparison via likelihood) is real and is already captured in Strengths #3 and #5. *Reason for removal:* Overstated label that conflicts with a verified weakness.

## Novel Insights
None beyond the paper's own contributions. The two reviews largely align on what the paper contributes and where it falls short; no reviewer identified a capability or limitation that the paper itself does not acknowledge or imply.

## Suggestions
1. In the main text, replace "hypothesis testing" with "model comparison via log-likelihood" or similar phrasing that accurately describes what the procedure does. If hypothesis testing is desired, add a parametric bootstrap or cross-validation scheme with error control.
2. Add at least one nonlinear baseline that respects manifold structure: e.g., a simple "tangent-space PPCA" that uses only the tangent components with isotropic noise, or GP-LVM with a likelihood-based evaluation on held-out data.
3. Report bootstrapped confidence intervals for the log-likelihood differences in Table 2 and Figures 4B/4D, so the reader can assess whether the GeCOV advantage is robust.
4. Provide a clear description (even a brief one) of how φ is fitted for the synthetic and real experiments, including the choice of landmarks M and their placement. If these choices are ad-hoc, state that explicitly.
5. Expand the derivation from (12) to (13) in a supplement or appendix — even a brief outline of the trace/orthonormality simplifications would improve trust in the core result.
6. Consider reporting the variance of log-likelihood across EM restarts or across bootstrap resamples to quantify sensitivity to initialization.
