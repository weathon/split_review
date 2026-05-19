- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 6, 3
Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper introduces RX-DPM, a method that applies Richardson-style extrapolation to ODE-based diffusion sampling. The key insight is to combine two numerical solutions computed over the same interval (one obtained in a single step, the other over multiple steps) to obtain a higher-order accurate estimate at every $k$ steps. The paper derives the extrapolation coefficients for non-uniform time grids (Section 4.1–4.2), provides a global truncation error analysis showing RX-Euler achieves $O(1/N^2)$ convergence versus $O(1/N)$ for Euler (Section 4.4), and demonstrates empirical improvements across multiple backbones (EDM, DDIM, DPM-Solver, PNDM) and datasets.

## Strengths

1. **Generalized Richardson extrapolation for non-uniform grids in DPMs.** The paper derives truncation error formulas (Equations 11–16, Section 4.1) and extrapolation coefficients (Equation 19, Section 4.2) that work for arbitrary time step scheduling, unlike standard Richardson extrapolation which requires uniform grids. This is a principled adaptation to a key characteristic of DPM sampling schedules and is shown to outperform naïve Richardson (Figure 2).

2. **Accuracy improvement without additional NFEs for Euler/DDIM.** The two required solutions (one-step and $k$-step estimates) share intermediate computations, so no extra network evaluations are needed (Section 4.2: "RX-Euler (RX-DDIM) does not require additional NFEs… the first prediction … can be stored and reused"). This makes the method essentially free in terms of computational cost for first-order solvers.

3. **Global truncation error analysis with provable convergence improvement.** Section 4.4 derives closed-form global errors for Euler ($c/N$) and RX-Euler ($c/(k^2-1)N^2$), demonstrating a one-order improvement in the leading error term under the same NFE budget. This theoretical guarantee directly supports the core claim of enhanced numerical accuracy.

4. **Consistent empirical gains across diverse backbones, datasets, and solvers.** The method improves FID/CLIP over baselines on CIFAR-10, FFHQ, AFHQv2, ImageNet, LSUN Bedroom, CelebA, and LSUN Church, with EDM, DDIM, DPM-Solver, PNDM, SN-DDIM, and NPR-DDIM backbones (Figures 2–3, Tables 1–4). Improvements are especially pronounced at low NFEs (e.g., $N \leq 10$ on CIFAR-10).

## Weaknesses

### Fatal
None.

### Major

1. **The higher-order solver extension (Section 4.3) rests on an unverified assumption and imprecise implementation description.** The extrapolation for higher-order solvers assumes a "linear error accumulations assumption" (Equation 22) — that the error of a $k$-step solution from a high-order method decomposes into a simple sum of per-step errors — without justification for why this should hold for Runge-Kutta or Adams-Bashforth methods where error propagation is nonlinear. Additionally, the RX-Runge-Kutta recipe approximates the intermediate evaluation $\mathbf{z}_{i-\delta'}$ as "$\mathbf{z}_{i-1}$ or $\mathbf{z}_{i-1-\delta}$, depending on the proximity of its time step" — this is not precise enough for reproducibility. The paper's theoretical analysis of convergence therefore does not extend rigorously beyond first-order Euler-type methods. The empirical results are mostly positive (DPM-Solver-2/3, PNDM) but the failure on F-PNDM + LSUN Church is not deeply analyzed in terms of when the linear-error assumption breaks down. Since the paper presents the method as a general framework for arbitrary ODE solvers (title: "Multiple ODE Solutions," contributions claim applicability to "general DPM solvers"), this is a meaningful gap between scope and rigor.

2. **The comparison with IIA (Zhang et al., 2024) is not reproduced under controlled conditions.** The paper states that "the values are brought from the tables of the paper" (Section 5.3) rather than reproduced with the same base solver, NFE range, and dataset preprocessing. This makes the comparison unreliable — differences in experimental setup could account for some or all of the reported gains. Controlled replication (or clearly stating the conditions under which IIA numbers were obtained) is needed to substantiate the claimed improvements over this baseline.

### Minor

3. **No error bars or measures of variability for any FID/CLIP result.** All results are reported as point estimates from a single sampling run (50K samples). While single-run evaluation is common in the diffusion model literature, several improvements are marginal (e.g., Table 2, DPM-Solver-2 on CIFAR-10: 3.13 vs 2.99 at NFE 15), and without some estimate of variance it is impossible to assess whether the reported gains are statistically meaningful.

4. **CLIP score degradation at 15 NFEs in Stable Diffusion (Table 1) is acknowledged but not investigated.** FID improves but CLIP drops. The paper speculates this "may be related to the classifier-guidance scales" but does not test this hypothesis (e.g., a small grid search over guidance scales). Since CLIP score is a primary metric for text-to-image alignment, this unresolved degradation weakens the claim of "strong generalization performance" for the conditional generation setting.

5. **The optimal covariance experiment (Section 5.6) confounds two effects.** The method reduces the number of times the optimal covariance is applied to half of the baseline (because extrapolation replaces two covariance-application steps with one). This change alone could affect quality regardless of the extrapolation's numerical benefit. An ablation controlling for covariance application frequency (e.g., applying covariance half the time without extrapolation) is needed to attribute the improvement to the extrapolation step.

### Trivial
None.

## Nice-to-Haves

- A wall-clock timing comparison would strengthen the "negligible computational overhead" claim.
- A discussion of when RX-DPM may fail (e.g., when the baseline solver does not show monotonic error reduction with step size, as in F-PNDM on LSUN Church) would improve the paper's utility for practitioners.
- The derivation in Section 4.1 assumes the leading error coefficient ($x''_{t_i}$) is approximately constant across sub-steps; explicitly acknowledging this standard approximation would improve clarity.

## Removed Points

The following criticisms from the inputs are removed with justification:

- **LA-DPM λ=0.3 "chosen post-hoc":** The paper uses the hyperparameter from the original LA-DPM paper ("the extrapolation hyperparameter presented in the paper fixed at λ=0.3"), not a value chosen to favor the proposed method. Additionally, the authors state they use the Euler base solver because "LA-DPM yields better results with Euler method than with Heun's method" — if anything, this favors LA-DPM. The criticism is factually incorrect. **Removed.**

- **Hybrid RX+EDM "undermines the core contribution":** The paper is transparent that this is a heuristic ("Although this approach is heuristic, it suggests that there is still room for improvement") and explicitly states that Heun and RX-Euler each have regimes where they perform better. The paper never claims RX-Euler is uniformly superior to all second-order methods at all NFEs. The hybrid is presented as a future direction, not a necessary patch for a broken method. **Removed.**

- **Algorithm 1 truncated / missing appendix / reproducibility concerns about missing sections:** These reflect parser artifacts that strip appendices and truncate some content. The original submission contains the full material. **Removed per review policy.**

- **Section 4.1/4.2 minor criticisms about the constant c assumption:** The assumption that the second derivative is approximately constant across sub-steps is a standard approximation in Taylor-expansion-based error analysis when step sizes are small. The paper is consistent with standard practice. **Removed as methodological nitpick that does not threaten the validity of the result.**

- **Criticism about "Naïve" Richardson comparison being poorly described:** The description in Section 5.2 is sufficient: naïve Richardson applies extrapolation once (not repeatedly), which is the standard one-shot application. The paper's method applies it every $k$ steps. The distinction is clear. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The reviews surface the scope-theory gap in the higher-order extension, which is worth highlighting but does not constitute a novel observation about the paper.

## Suggestions

1. **Narrow the theoretical claims to first-order solvers (Euler/DDIM)** and present the higher-order extensions as empirical explorations with explicit acknowledgment of the unverified linear-error assumption. This would make the paper's strongest contribution (RX-Euler with non-uniform grid derivation) the centerpiece and protect it from criticisms aimed at the weaker extension.

2. **Reproduce IIA under the same conditions** (same base solver, NFEs, preprocessing) or, if exact reproduction is infeasible, clearly document the settings used in the original paper and discuss any differences that could affect comparability.

3. **Run a small grid search over guidance scales** for Stable Diffusion to determine whether the CLIP degradation at 15 NFEs can be closed. If it cannot, discuss this as a limitation openly.

4. **Add an ablation study** for the optimal covariance experiment (Section 5.6) that controls for the number of covariance applications to isolate the effect of extrapolation from the reduced stochasticity.
