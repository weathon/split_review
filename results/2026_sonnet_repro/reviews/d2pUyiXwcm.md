Now let me perform the calibration search.**Round 1 bracket: 6–8** (paper exceeds middle anchors; stronger theory + higher dimensions than SINGER at 6.33, but clear weaknesses prevent 8+)

Now narrowing within bracket:Now I have enough to write the final review. Let me compile it.

---

## Summary

SCaSML (Simulation-Calibrated Scientific Machine Learning) proposes a physics-informed inference-time framework that improves pre-trained SciML surrogate solvers for semi-linear parabolic PDEs without any retraining. The core insight is a "Structural-preserving Law of Defect" (Fact 2.3): the error of a surrogate model satisfies a new semi-linear PDE with the same structural form as the original, enabling efficient stochastic simulation via Multilevel Picard (MLP) iteration. This yields a product-error bound (Theorem 2.5) showing that corrections scale with the product of surrogate and simulation errors, and an improved convergence rate. Experiments across 5 PDE benchmarks up to 160 dimensions show 20–80% error reduction.

---

## Strengths

- **Structural-preserving Law of Defect (Fact 2.3)**: The derivation that the defect $\tilde{u} = u - \hat{u}$ satisfies a semi-linear PDE of the same form as the original (equation 7) with modified nonlinearity $\tilde{F}$ is the key technical contribution. This preservation is non-trivial and directly enables the high-dimensional MLP simulation that makes the method tractable. To the authors' knowledge it is the first derivation preserving the semi-linear structure needed for Feynman–Kac-based solvers.

- **Product-error bound (Theorem 2.5)**: Equation (9) rigorously shows that the correction step's error is bounded by $E(M, N) \cdot (C_F \, e(\tilde{u}))$ — a product of the MLP solver error and the surrogate error. This has the non-obvious implication that better surrogates make the correction problem *easier*, and it leads directly to the improved computational complexity claim (Corollary E.9).

- **Compelling LQG results (Table 1, LOG section)**: Standalone MLP produces relative $L^2$ errors of 5.27–5.63 at 100–160 dimensions — far exceeding 1.0 and indicating catastrophic divergence — while SCaSML achieves 0.055–0.099. This is the clearest demonstration that SCaSML is doing something fundamentally different from simply spending more compute: there is no budget allocation under which standalone MLP at this dimension succeeds.

- **Empirical convergence verification (Figure 4)**: Log-log plots of error vs. training size for GP surrogates at $d \in \{20, 40, 60, 80\}$ show SCaSML's slope is consistently steeper than the base GP, directly supporting the accelerated convergence claim of Corollary 2.6.

- **Plug-and-play compatibility**: Results in Table 1 show consistent improvement over both PINN (VB-PINN) and Gaussian Process (VB-GP) surrogates for the viscous Burgers equation without any modification to the correction procedure, demonstrating true surrogate-agnosticism.

- **Inference-time scaling (Figure 3b)**: All four subplots show monotonically increasing improvement with evaluation budget, corroborating the elastic-compute claim. The improvement is consistent across all tested problems.

---

## Weaknesses

### Fatal
None.

### Major

- **Discrepancy between informal and formal convergence rate claims**: Section 2.1 (informal argument), the proof sketch in Section 2.4, and Figure 4's caption all state the improved rate as $m^{-\gamma - 1/2}$. Corollary 2.6, however, states the improved rate as $O(m^{-\gamma - 1/2 + \alpha(1)})$. The term $\alpha(1)$ appears with no definition, bound, or interpretation in the main text. If $\alpha(1) \geq 1/2$, Corollary 2.6 does not establish a rate improvement over the surrogate at all. The informal claim $m^{-\gamma - 1/2}$ appears 5+ times in Section 2 and creates a systematically misleading impression relative to the formal result. The paper should either: (a) bound $\alpha(1)$ explicitly and show it is $< 1/2$, or (b) retract the specific informal rate $m^{-\gamma - 1/2}$ and replace it with the form stated in the corollary. The empirical slopes in Figure 4 could help resolve this if the exponents are measured and compared to $\gamma + 1/2$.

### Minor

- **Fixed-budget comparison deferred to appendix (Appendix G.7)**: The main paper's Table 1 compares methods at their natural compute cost — the surrogate at 0.3–3s, SCaSML at 10–87s. For the LCD and DR problems where standalone MLP also produces a reasonable solution, it is not shown in the main body whether the same accuracy SCaSML achieves could be obtained by running MLP longer at the same total budget. The paper explicitly notes Appendix G.7 contains this analysis, but the result that substantiates the "elastic compute" claim beyond the LQG failure case belongs in the main body for complete reader understanding. (For the LQG case this concern does not apply, since standalone MLP diverges regardless of budget.)

- **Abstract's "20–80%" range excludes the DR results**: The abstract states SCaSML "reduces the error of various surrogate models by 20–80%." Section 3.4 reports DR improvements of only 6.6–10.9%, which falls materially below the 20% lower bound cited. The abstract should include the full range ("7–80%") or qualify the range with "across most benchmarks."

- **Clipping threshold asymmetry not fully isolated**: Experiments set dramatically different clipping thresholds for standalone MLP versus SCaSML's correction step (e.g., threshold 10 vs. 0.1 for LQG; 10 vs. 0.01 for DR). The paper justifies this by noting the defect's smaller magnitude (Section 3.3: "reflecting the smaller magnitude of the defect"), which is theoretically sound. However, the Table 1 comparison conflates two contributions: (a) variance reduction from the surrogate warm start, and (b) tighter numerical stability enabled by the smaller-magnitude problem. The decomposition of these contributions is not shown.

### Trivial

- Figure 3b shows four subplots with very different y-axis scales (0–10%, 26–31%, 50–65%, 55–72.5%) using visually identical layouts, making the LQG subplot's smaller range easy to miss. A note on scale differences would prevent misreading.

---

## Nice-to-Haves

- A practical guidance remark attached to Assumption 2.4 would help practitioners. The assumption requires both $L^\infty$ residual control and $W^{1,\infty}$ error control. For PINN surrogates, $W^{1,\infty}$ guarantees are non-trivial. A brief remark on what surrogate quality is "good enough" for the correction to add value — ideally with a concrete threshold or empirical check — would make the framework more actionable.

- A regime analysis: when is SCaSML *not* expected to help? The paper implicitly covers the failure mode in LQG (MLP diverges; SCaSML succeeds). A brief comment on when the surrogate is so inaccurate that the defect PDE is as hard as the original would sharpen the boundary of applicability.

- The Quadrature MLP variant is introduced in Section 2.3 but all main experiments use Full-history MLP. A brief statement explaining why, or a pointer to a comparison, would complete the picture.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — W^{1,∞} assumption on PINN**: The critic notes that $W^{1,\infty}$ convergence for PINNs is non-trivial. While true in general, this is a standard regularity assumption and the paper defers full justification to the appendix; this is not itself a flaw of the main-text exposition. **Removed** (speculative gap, not a verifiable flaw from main text).

- **Harsh Critic — LLM analogy is "loose"**: The framing analogy between inference-time scaling in LLMs and in SCaSML is acknowledged by the paper as inspirational rather than technical. This is positioning, not a scientific claim. **Removed** (pure framing nitpick).

- **Harsh Critic — Comparison to control-variate methods in MC-PDE literature not explicit in introduction**: The paper's Section 4 (Conclusion) explicitly states "our framework uses the machine learning model as a control variate in stochastic simulations to reduce the variance of Monte Carlo simulation." The connection is made; that it appears in the conclusion rather than the introduction is a presentation preference, not a missing acknowledgment. **Removed** (adequately addressed).

- **Strength Finder — "First physics-informed inference-time scaling framework"**: This is a priority claim about an important problem, not a specific technical strength grounded in paper content (beyond what is already captured under the structural-preservation insight). **Removed as generic** from strengths section.

- **Strength Finder — "Statistical significance p ≪ 0.001"**: This is a reporting detail (Appendix G.4), not a technical strength. Removed as generic. The core strength is the empirical consistency across benchmarks.

---

## Novel Insights

The key conceptual contribution goes beyond the method itself: by showing that the defect of any semi-linear surrogate satisfies a PDE with the *same structural class*, the paper reveals that structural preservation under error linearization is a property intrinsic to semi-linear operators — not just a trick for this specific formulation. This implies that *any* existing high-dimensional stochastic solver designed for the original PDE class can be repurposed as a corrector at inference time with no algorithmic modification, merely by substituting the modified nonlinearity $\tilde{F}$. This has direct implications for the broader MLP solver literature: the correction problem is always "easier" than the original because the effective Lipschitz constant of $\tilde{F}$ is controlled by the surrogate error, suggesting a systematic use of rough surrogates as variance reducers in classical stochastic PDE simulation.

---

## Suggestions

1. **Resolve the $\alpha(1)$ discrepancy**: Either bound $\alpha(1) < 1/2$ in the main text with a brief argument (or by measuring the empirical exponent in Figure 4 and comparing to $\gamma + 1/2$), or replace all informal statements of "$m^{-\gamma-1/2}$" with "$m^{-\gamma - 1/2 + \alpha(1)}$" to match the formal result.

2. **Promote the fixed-budget result to the main body**: Move the key finding from Appendix G.7 into Section 3. A single table or figure comparing SCaSML vs. standalone MLP at matched wall-clock time would definitively answer the compute-fairness question for the non-LQG benchmarks.

3. **Quantify the empirical convergence exponent**: In Figure 4, measure the actual slope for both GP and SCaSML across dimensions and report the numerical values. Comparing these to the predicted $\gamma$ and $\gamma + 1/2$ directly would either corroborate or refine the formal Corollary 2.6.

4. **Fix the abstract range**: Change "20–80%" to "7–80%" (or similar) to reflect the DR results, or add the qualifier "on most benchmarks."

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Human Score | Round | Comparison to paper under review |
|------|----------------|-------|----------------------------------|
| wVADj7yKee (SINGER) | 6.33 | R1+R2 | SCaSML clearly superior: 8× higher dimensions, stronger theory, LQG failure-mode demonstration |
| jqVj8vCQsT (Neural Solver for PINN) | 5.60 | R1 | SCaSML stronger: more novel idea, rigorous theory, higher-dimensional experiments |
| 5rfj85bHCy (HyResPINNs) | 5.00 | R1 | SCaSML stronger: true dimensionality scalability, product-error bound |
| kIPEyMSdFV (Reverse Diffusion MC) | 7.00 | R2 | Comparable: clean theory + experiments, different domain; paper similar in rigor |
| 2U8owdruSQ (DNN + stochastic process) | 6.80 | R2 | Paper under review comparable or slightly better: similar empirical breadth, more novel theoretical contribution |
| FJv8VMPxWi (Convergence for hybrid methods) | 6.60 | R2 | Paper under review comparable: both have convergence guarantees + experiments |
| 8OxL034uEr (MgNO) | 6.50 | R2 | Paper under review better: more compelling high-dimensional results |
| G3CpBCQwNh (PhysPDE) | 6.50 | R2 | Different sub-field; paper under review stronger in theoretical depth |

**Round 1 bracket**: 6–8.  
**Round 2 narrowing**: Round 2 anchors cluster at 6.33–7.00. The paper is clearly above SINGER (6.33) and the 6.5 cluster, and comparable to the 7.0 (Reverse Diffusion MC) anchor in rigor and empirical breadth. The $\alpha(1)$ discrepancy — a genuine theoretical imprecision in the paper's most prominently claimed result — prevents a score of 7.5+. The LQG results and structural preservation insight push it above 6.5.

**Final score: 7.0 — Accept**

*Originality*: High — the defect-PDE preservation insight is non-obvious and, to the reviewer's knowledge, new. The inference-time scaling framing is novel in this domain.  
*Importance of research question*: High — reliable, error-correctable solvers for high-dimensional PDEs are broadly needed.  
*Claims well-supported*: Mostly yes — the product-error bound is rigorous; the convergence rate claim has a formal gap (α(1) term) that deserves attention.  
*Soundness of experiments*: Good — 5 benchmarks up to 160d, multiple surrogate types, statistical significance testing. The LQG failure-mode case is especially compelling.  
*Clarity of writing*: Good — the derivation of the defect PDE is clear and well-motivated; the α(1) discrepancy is the main clarity issue.  
*Value to research community*: High — provides a principled, surrogate-agnostic correction procedure with provable guarantees.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>