Now I have the full paper. Let me carefully synthesize the review based on what I verified directly.

---

## Summary

This paper addresses the breakdown of conformal prediction (CP) for time-dependent PDE surrogate models, where the exchangeability assumption is violated as the solution distribution drifts over time. The authors prove that in the function-space setting, the total variation distance between solution distributions at any two time points is maximal (Theorem 4.1), making coverage guarantees impossible without further assumptions. As a constructive solution, they exploit that under a discretized linear PDE with Gaussian initial conditions, the solution is Gaussian at every time step (Theorem 4.2), yielding closed-form likelihood ratios that enable weighted conformal prediction (WCP) with formal coverage guarantees. Experiments on synthetic PDEs and a real-world pulsed-thermography dataset show WCP maintains target coverage where naïve CP and LSCI fail.

---

## Strengths

- **Meaningful negative result (Theorem 4.1):** The paper proves that for even a simple PDE (heat equation with Gaussian initial distribution), $d_\text{TV}(\mathcal{P}_t, \mathcal{P}_{t+\delta}) = 1$ for all $t \geq 0, \delta > 0$, shown in Section 4.2. This is a genuinely useful impossibility result that motivates moving to the discretized setting and clearly flags why function-space CP approaches in the neural operator literature cannot provide coverage guarantees.

- **Constructive closed-form characterization (Theorem 4.2):** The paper derives exact Gaussian distributions for the discretized solution — with mean $\boldsymbol{\mu}_t = \exp(t\mathbf{A})\boldsymbol{\mu}_0 + \int_0^t \exp((t-s)\mathbf{A})\mathbf{r}(s)ds$ and covariance $\boldsymbol{\Sigma}_t = \exp(t\mathbf{A})\boldsymbol{\Sigma}_0\exp(t\mathbf{A}^T)$ — making the density ratio in Equation (1) computable in closed form. This is the key technical enabler of WCP.

- **Formal coverage guarantees that baselines cannot provide:** Table 1 and Figure 3 demonstrate that naïve CP and LSCI (which have *no formal guarantees* in the non-exchangeable setting, as the paper correctly notes) fail severely — with LSCI dropping to 0.0 coverage for $a = -0.0075$ at timestep 20 — while WCP consistently maintains coverage where it produces finite intervals.

- **Computational speed:** WCP runs in seconds versus ~40 minutes for LSCI on 5000 test samples, which is a concrete practical advantage.

- **Appropriate generalization:** Remark 4.3 correctly notes the result extends beyond Gaussian initial conditions to the entire location-scale family (Gaussian, Cauchy, Laplace, logistic), with additional experiments in appendix A.8.

---

## Weaknesses

### Fatal
None.

### Major

- **Scope mismatch between motivation and method:** The introduction situates the work in weather prediction, aerodynamics, and financial modeling (Section 1, Figure 1), and Figure 2 uses the backward heat equation to show failures. However, the formal coverage guarantee (Theorem 4.2 and Section 4.4) applies only to *linear* PDEs with *Gaussian initial conditions* under *finite-difference discretization*. Weather prediction (Navier-Stokes), aerodynamic optimization (nonlinear fluid dynamics), and financial models are almost universally nonlinear. Section 6 acknowledges "extending the analysis to nonlinear PDEs is a natural next step," but this framing understates the gap: the central formal contribution does not apply to any of the primary motivating examples. The introduction should be reframed around the actual scope (e.g., heat transfer, diffusion, wave propagation, linear structural mechanics), which are genuinely important application domains.

- **Transparent treatment of the infinite-band regime in Table 1:** For $a = -0.01$ at timesteps 15 and 20, WCP reports coverage 1.0 with $n_\infty = 100\%$; i.e., all samples receive infinite bands and coverage is computed over zero remaining samples. The paper partially addresses this: Figure 3 caption explicitly says "We omit coverages when infinite conformal bands were reported (coverage of 1 would hold trivially)," and Section 5 states "reporting trivial bands is usually a more valuable result than delivering bands with undercoverage." However, Table 1 still lists "1.0" as the coverage in those cells alongside the LSCI comparison of "0.0," which can mislead the reader into treating these as comparable outcomes. A "useful coverage rate" — coverage computed only over samples receiving finite bands — reported consistently across both figures and tables, would present the practical tradeoff more honestly.

### Minor

- **No discussion of computational scalability:** Evaluating the WCP weights requires computing $\boldsymbol{\Sigma}_t = \exp(t\mathbf{A})\boldsymbol{\Sigma}_0\exp(t\mathbf{A}^T)$, where $\mathbf{A} \in \mathbb{R}^{n \times n}$ and $n$ is the number of spatial grid points. Matrix exponentiation costs $O(n^3)$. The synthetic experiments use 1D spatial discretizations and the thermography dataset is noted to be "small 2D" (Section 5), but the paper provides no analysis of how this scales. For even modest 2D spatial grids (e.g., $128 \times 128 = 16{,}384$ nodes), the matrix exponential becomes computationally demanding. Practitioners considering applying WCP to larger-scale problems need this information.

- **Remark 4.5 asserts continuous-space guarantees without quantification:** Remark 4.5 states "we provide asymptotic—and in some cases even non-asymptotic—guarantees for the PDE solution $u(x, t)$ in the original space," with the stated key idea being that "bands on the discretized solution can be transferred to the original solution by leveraging numerical error guarantees of the scheme." However, the remark does not identify which PDEs and discretizations admit which type of guarantee, nor quantify the approximation error. For unstable PDEs (where $a < 0$ in the experiments), discretization errors can grow rapidly. This remark makes a claim the paper does not actually deliver on within the main text.

- **Real-world experiment entirely deferred to appendix:** The thermography experiment on the Wei et al. (2023) dataset is the paper's only real-world validation, but the main body gives it a single sentence: "Our method achieves target coverage over all tested time steps" (Section 5). No quantitative results, bandwidths, or baseline comparisons appear in the main body. Given that this experiment is essential for demonstrating practical relevance in a non-synthetic setting, it warrants at least a small table in the main text.

### Trivial
None identified.

---

## Nice-to-Haves

- A theoretical characterization of when WCP transitions from finite to infinite bands (as a function of spectral properties of $\mathbf{A}$ and the ratio $\boldsymbol{\Sigma}_{t+\delta}/\boldsymbol{\Sigma}_t$) would give practitioners a way to assess in advance whether their system is in the tractable regime.
- Discussion of robustness to misspecification of the Gaussian initial condition (e.g., when the covariance $\boldsymbol{\Sigma}_0$ must be estimated from data) would strengthen applicability claims. Remark 4.3 mentions location-scale extensions but does not address approximate specification.
- A brief discussion of low-rank approximations or other computational strategies for scaling the matrix exponential to larger 2D/3D grids would greatly increase practical impact.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Trajectory-based baselines missing" (Moya et al. 2025; Gray et al. 2025):** The paper explicitly discusses these methods in Section 2 and explains why they address a different subproblem (trajectory-level exchangeability, not distribution shift beyond the calibration horizon). Including them as baselines would require a fundamentally different experimental design. Removed as scope creep.

- **Harsh Critic: "Theorem 4.1 is just Feldman-Hájek / Theorem 4.2 is just an affine-Gaussian fact":** Both theorems are indeed applications of known mathematical facts. However, evaluating a paper's contribution solely by mathematical novelty of its theorems, independent of the value of the framing and connection to the CP community, is an inappropriate standard for an applied ML paper. The contribution is identifying *that* these structures apply here and *how* to connect them to WCP. Removed as an unfair standard.

- **Harsh Critic: "The assumption that we can evaluate the exact solution operator removes the motivation for using a surrogate":** Section 4.1 states the assumption is needed to *generate training/calibration data*, not to run the surrogate at test time. The surrogate is still used for fast inference at test time; the PDE solver is only used during training and weight computation. This is a misreading of the paper.

- **Strength Finder: "Clear, concrete motivation via Figure 1 and Figure 2":** While Figure 2 is genuinely informative (failure of naïve CP on the backward heat equation), Figure 1 illustrates motivation with stock market crashes and climate trends — which are nonlinear phenomena outside the method's scope. This strength conflicts with the verified framing mismatch weakness. Partially removed; Figure 2 remains a genuine supporting strength already reflected in the main review.

---

## Novel Insights

The reviewer synthesis surfaces one insight not emphasized prominently in the paper itself: the two-tiered structure of WCP's failure mode is actually *preferable* to the single-tier failure of LSCI or naïve CP. LSCI produces dangerously overconfident finite intervals (coverage 0.0); WCP, by contrast, degrades gracefully by widening to infinity before any coverage violation, effectively signaling when the system has evolved too far from the calibration distribution. This "abstention as a first-class outcome" perspective — which the paper touches on but does not fully develop — could be a distinctive and marketable feature of the WCP framework: it converts coverage failure into detectable uncertainty rather than silent failure.

---

## Suggestions

1. **Reframe the introduction** around linear PDE applications (heat transfer, diffusion equations, linear wave propagation, structural dynamics) rather than weather and financial modeling. These are genuine and important application domains that match the method's scope.
2. **Restructure Table 1** to distinguish three regimes: (a) finite-band coverage, (b) partial abstention ($0 < n_\infty < 100\%$), (c) full abstention ($n_\infty = 100\%$), and report "useful coverage" only over (a). Move Figure 3 to explicitly show the $n_\infty$ curve alongside coverage to communicate the tradeoff.
3. **Promote the thermography results** (appendix A.6) to the main body with a compact table showing coverage and bandwidth at multiple timesteps, compared against naïve CP.
4. **Add a scalability section** discussing the $O(n^3)$ cost of matrix exponentiation and practical approximations (e.g., low-rank structure of $\boldsymbol{\Sigma}_0$, Krylov methods) for 2D/3D grids.

---

## Score and Decision

**Originality:** The problem identification (TV = 1 in function spaces, Gaussian propagation enabling closed-form weights) is novel in the CP-for-PDEs literature, though the mathematical tools are classical. *Moderate.*

**Importance:** Non-exchangeability in PDE CP is a real and under-addressed problem. The scope is narrow (linear PDEs), but the contribution is solid within that scope. *Moderate.*

**Claims supported:** The formal coverage guarantee is mathematically sound and the experiments support it where WCP produces finite bands. The framing with nonlinear motivating examples is misleading relative to actual scope. *Partially supported.*

**Soundness:** Theorems are correct. The infinite-band evaluation in Table 1 is slightly misleading in presentation but acknowledged by the authors in Figure 3. *Mostly sound.*

**Clarity:** Generally well-written, but the scope mismatch and the mixed treatment of the abstention regime reduce clarity. *Good.*

**Community value:** Provides a principled, fast alternative to LSCI with formal guarantees for an important sub-class of PDE problems. The negative result on function spaces is independently useful. *Moderate-to-good.*

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>