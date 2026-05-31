Now let me run the calibration search to properly score the paper.**Round 1 Bracket:** The paper plausibly sits between **4.5 and 6.0**. It is more principled than the 4.5 anchor (which lacked any formal theory), but not as broadly impactful as the 6+ papers. Let me narrow.Now I have sufficient calibration data. Let me write the consolidated final review.

---

## Summary

The paper studies conformal prediction (CP) for surrogate models of time-dependent PDEs, where the non-stationarity of PDE solutions breaks the exchangeability assumption required by standard CP. It contributes (1) an impossibility result showing that in function spaces, even simple PDEs yield mutually singular distributions at arbitrarily close time points (Theorem 4.1), precluding any coverage guarantee; (2) a positive constructive result showing that for discretized linear PDEs with Gaussian initial conditions, the solution is Gaussian at every time step with closed-form mean and covariance (Theorem 4.2), enabling a likelihood-weighted conformal predictor with exact coverage guarantees; and (3) empirical validation on synthetic second-order PDEs and a real-world thermography dataset.

---

## Strengths

- **Theorem 4.1 — impossibility in function space.** The result that $d_{\text{TV}}(\mathcal{P}_t, \mathcal{P}_{t+\delta}) = 1$ for all $t \geq 0$, $\delta > 0$ is concretely proven for the heat equation with Gaussian initial conditions (Section 4.2). This negative result is a genuine contribution: it definitively closes off the function-space approach for coverage guarantees and provides principled grounding for moving to discretized settings. Its direct relevance to the neural operator literature (which often frames learning in function space) makes it useful to the community.

- **Closed-form Gaussian propagation enabling exact WCP.** Theorem 4.2 establishes that the method-of-lines discretization of a linear PDE with Gaussian initial conditions yields Gaussian solutions at every time step, with covariance $\boldsymbol{\Sigma}_t = \exp(t\mathbf{A})\boldsymbol{\Sigma}_0\exp(t\mathbf{A}^T)$. While the proof is short, the key insight — that this closed-form structure allows density ratios (Equation 1) to be computed exactly, enabling **exact** (non-asymptotic) coverage guarantees — is the central methodological contribution and is genuine.

- **Empirical coverage vs. baselines.** Table 1 and Figure 3 document that naïve CP and LSCI progressively undercover as the PDE becomes more unstable ($a < 0$, smaller $a$), with LSCI dropping to 0.0 at late timesteps in the most unstable cases. WCP maintains approximately 90% coverage where it produces finite bands. This is a principled demonstration of the method's advantage in the setting for which it is designed.

- **Computational efficiency.** The paper reports that WCP runs in seconds while LSCI takes approximately 40 minutes for 5000 test samples, providing a substantial practical advantage alongside its stronger guarantees.

---

## Weaknesses

### Fatal
None.

### Major

- **Motivating framing fundamentally mismatches the method's scope.** The introduction and Figure 1 invoke stock market crashes, climate time series, and weather forecasting as motivating applications—all predominantly nonlinear phenomena. The paper's formal contribution, however, applies only to *linear* PDEs with *Gaussian* initial conditions under *finite-difference discretization*. Section 6 acknowledges "extending the analysis to nonlinear PDEs is a natural next step," but this understates the gap: a practitioner following this paper to handle Navier-Stokes or a neural weather model will find nothing applicable. The claimed coverage guarantee—the central contribution—does not hold for the motivating examples. The introduction should be substantially revised to scope the framing to linear PDEs, or the method must be extended.

- **Infinite-band results conflated with meaningful coverage in the evaluation.** Table 1 reports "Coverage = 1.0" for $a = -0.0075$ at timestep 20 ($n_\infty = 100\%$) and for $a = -0.01$ at timesteps 15 and 20 ($n_\infty = 100\%$). In these cases, *all* test samples receive infinite prediction bands, and the coverage of 1.0 is computed over zero remaining samples—trivially satisfied. The paper argues in Section 5 that "reporting trivial bands is usually a more valuable result than delivering bands with undercoverage," which has principled merit. But pooling these degenerate outcomes with genuine finite-band results in a single Coverage column creates a misleading impression of the method's utility. The evaluation should clearly separate regimes where WCP produces finite, informative bands from regimes where it abstains entirely, e.g., by reporting a "useful coverage rate" (fraction of finite-band samples that are covered). The comparison to LSCI at those same timesteps is non-informative: LSCI produces finite intervals that undercover; WCP declines to predict. These are qualitatively different failure modes, not comparable outcomes.

- **Computational scalability of the method is unaddressed.** The weights in Equation (1) require computing $\boldsymbol{\Sigma}_t = \exp(t\mathbf{A})\boldsymbol{\Sigma}_0\exp(t\mathbf{A}^T)$ and evaluating multivariate Gaussian densities. Computing $\exp(t\mathbf{A})$ for a grid of size $n$ costs $O(n^3)$, and evaluating the full multivariate Gaussian density requires $O(n^3)$ for Cholesky decomposition. For a modest 2D grid of $128 \times 128 = 16{,}384$ points, this is intractable. The paper's synthetic experiments appear to use 1D spatial grids, and the real-world dataset is described as "small 2D" (Section 5). The paper makes no mention of computational complexity or how the method scales with spatial resolution, leaving the claim of practical applicability to engineering problems unsupported for realistic grid sizes.

### Minor

- **Theorem 4.2's proof is a textbook affine-Gaussian fact.** The proof is four sentences and reduces to "an affine transformation of a Gaussian is Gaussian." The genuine contribution is the *framing*—recognizing that the method-of-lines discretization yields an affine map connecting initial conditions to solutions—not the proof itself. The paper should position this as a useful structural observation rather than a theorem of independent mathematical significance.

- **Real-world experiment is almost entirely absent from the main text.** Section 5 devotes a single sentence to the thermography results: "Our method achieves target coverage over all tested time steps." No quantitative comparison with baselines, no bandwidth figures, and no ablation appear in the main body. For a paper that lists empirical validation as a stated contribution, the real-world evidence should be substantively represented in the main text.

- **Remark 4.5 asserts transfer of discrete guarantees to continuous PDE solutions without quantification.** The remark states that "bands on the discretized solution can be transferred to the original solution by leveraging numerical error guarantees." This depends critically on the PDE and the discretization scheme, and can fail for unstable PDEs (which are the main focus of the experiments). No bounds are given, no conditions are stated, and no reference provides the transfer result. The remark promises more than the paper delivers.

### Trivial

- **The assumption that an "analytical form of the PDE" is available** (Section 4.1: "we can generate our own data using numerical solvers") is stated once but not consistently flagged as a limitation. For surrogate modeling scenarios where the governing equations are partially unknown, this assumption is violated and the method cannot compute the required weights. This should be explicitly acknowledged in the limitations.

---

## Nice-to-Haves

- A theoretical characterization of when WCP produces finite versus infinite bands—expressed in terms of spectral properties of $\mathbf{A}$ and the ratio of $\boldsymbol{\Sigma}_{t+\delta}$ to $\boldsymbol{\Sigma}_t$—would let practitioners assess before commitment whether their PDE system falls in the tractable regime.
- A discussion of robustness to misspecification of the Gaussian initial condition assumption (e.g., when $\boldsymbol{\Sigma}_0$ is estimated from finite data, or when the true distribution is non-Gaussian) would strengthen the practical section; Remark 4.3 acknowledges the location-scale generalization but does not address robustness to misspecification.
- Including a "useful coverage rate" metric (coverage restricted to samples receiving finite bands) alongside $n_\infty$ would clarify the tradeoff between abstention and informative coverage.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **[REMOVED — Missing baselines (trajectory-based methods)]** The harsh critic notes that Moya et al. (2025) and Gray et al. (2025) are not included as baselines. However, those methods calibrate at *trajectory level* (not pointwise) and are designed for a different prediction task. The paper explains this distinction (Section 2). This is a nice-to-have at best, not a methodological gap.

- **[REMOVED — Theorem 4.1 described as non-novel]** The harsh critic notes this is an "application of the Feldman-Hájek theorem." The paper explicitly acknowledges this on the page ("representative of a broader phenomenon... Hairer 2023"), so the claim is not overclaimed. The contribution is the PDE-specific instantiation, which is useful. No independent misconduct.

- **[REMOVED — Speculative fatal about Remark 4.5 and unstable discretizations]** The harsh critic frames Remark 4.5 as "promising something the paper does not deliver" and calls it a structural flaw. This is legitimate as a minor concern but the claim is aspirational/directional, not a formal theorem. Demoted to Minor.

- **[REMOVED — Missing proofs in appendix]** The harsh critic notes that the thermography experiment details are deferred to Appendix A.6. This is addressed in the rule prohibiting removal of appendix content. The substantive criticism (lack of main-text results) is retained as a Minor weakness.

- **[REMOVED — Strength: "Clear concrete motivation via Figure 1"]** The harsh critic raises a valid conflict: Figure 1 uses nonlinear examples (stock market crashes, climate trends) to motivate a method that cannot handle nonlinear problems. The motivation is legitimate for illustrating non-stationarity in general but is misleading about the paper's actual scope. Retained as part of the Major framing weakness instead.

---

## Novel Insights

The key non-obvious insight of this paper is the *cascade of two complementary results*: an impossibility in the continuous function-space setting (where distributions are always mutually singular) paired with a constructive possibility in the discretized setting (where linear Gaussian structure gives exact density ratios). This framing cleanly explains why the "function-space" perspective used in the neural operator literature is fundamentally incompatible with conformal coverage guarantees, while also providing a precise, actionable exit from the impossibility via discretization. The identification of this gap—and the structured way of stepping around it—is the paper's most original contribution, even if neither result requires new mathematical machinery.

---

## Suggestions

1. **Restructure the evaluation to separate finite-band and infinite-band outcomes.** Add a "useful coverage rate" column to Table 1 and clearly label infinite-band cells as "abstained" rather than treating coverage=1.0 at n_∞=100% as comparable to genuine coverage results.
2. **Revise the introduction to scope the contribution correctly**: frame the method as a solution for linear PDEs with known Gaussian dynamics, and reframe Figure 1 to illustrate non-stationarity in *linear* PDE settings rather than stock crashes and climate trends.
3. **Add a computational complexity analysis**: state explicitly the cost of computing $\exp(t\mathbf{A})$ and the Gaussian density, and discuss when this is tractable (1D grids, small 2D) and when it is not (large 2D/3D).
4. **Move the thermography experiment into the main body** with at least a coverage-bandwidth table at multiple timesteps and a visual comparison against the baselines.

---

## Score and Decision

**Calibration anchors:**

| Paper | Path | Avg Human Score | Round | Comparison |
|---|---|---|---|---|
| Calibrated Physics-Informed UQ | cF6OoaYcRa.md | 4.50 | R1 (mid) | Clearly weaker — no formal theory, very limited experiments |
| Solving DEs with Constrained Learning | 5KqveQdXiZ.md | 5.25 | R1 (mid) | Comparable scope, broader ML contribution but different domain |
| Non-Exchangeable Conformal Risk Control | j511LaqEeP.md | 6.00 | R2 | Closely related topic, broader scope, better evaluation — stronger |
| PAC Prediction Sets Under Label Shift | 4vPVBh3fhz.md | 6.40 | R2 | Broader applicability, more robust evaluation — stronger |
| Conformal Inference for Time Series (ECI) | RD9q5vEe1Q.md | 5.50 | R2 | Similar: principled CP under distribution shift; ECI is more broadly applicable, similar theory modesty |
| Class-Conditional CP for Imbalanced Data | Dtxc7mlKRg.md | 4.60 | R2 | Narrower in scope, similar incremental contribution — slightly weaker |
| Active Learning for Neural PDE Solvers | x4ZmQaumRg.md | 7.00 | R1 (mid) | More comprehensive benchmark; stronger evaluation — substantially stronger |

**Round 1 bracket:** 4.5–6.0 based on the mid-band anchors.

**Round 2 narrowing:** Within the bracket, the paper under review sits *below* j511LaqEeP (6.00) and below the ECI paper (5.50). Both of those have broader applicability (general non-exchangeable settings vs. strictly linear/Gaussian PDE class), more diverse experiments, and do not have the infinite-bands evaluation transparency issue. The paper is clearly *above* the 4.50 anchor (much stronger theoretical grounding, more principled evaluation). It is also slightly below ECI (5.50) because: (a) WCP's scope is significantly narrower, (b) the framing/scope mismatch is a genuine issue, (c) the evaluation in the most unstable regime is misleading, and (d) computational scalability is unaddressed.

**Final score: 5.0** — A real but narrow and unevenly presented contribution. The core idea is principled and the impossibility result is genuinely useful, but the scope/framing mismatch, the evaluation transparency problem around infinite bands, and the unaddressed scalability concern limit the paper's impact in its current form.

**Decision: Reject** (borderline — the paper would benefit from revised framing, clearer evaluation, and scalability discussion before acceptance).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>