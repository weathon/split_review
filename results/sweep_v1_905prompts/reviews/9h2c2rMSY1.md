Now I have enough calibration data. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me finalize.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

Wait, I should think carefully about the decision. Scores of 5-6 can be either accept or reject. Let me look at the anchors:
- 5.25 "Solving Differential Equations with Constrained Learning" - Accept (w/ scores 3,8,5,5)
- 5.75 "Approximating Full Conformal Prediction" - Accept (w/ scores 6,3,8,6)
- 5.50 "Efficient Certification of PINNs" - Reject (w/ scores 5,6,6,5)
- 5.80 "Conformal Prediction for Dose-Response" - Reject (w/ scores 8,5,3,8,5)

So at approximately 5.5 there's a mix. Let me think about this paper more carefully.

The paper contributions are:
1. Theorem 4.1 - novel theoretical result about function-space impossibility
2. Theorem 4.2 - derivation of closed-form Gaussian distribution for linear PDE discretizations
3. Weighted CP framework for PDEs
4. Empirical validation

The limitations:
- Method limited to linear PDEs (genuine scope limitation)
- Remark 4.5 is vague
- Real-world example lacks detail in main text
- Only tested on one PDE family + one real-world case
- Coverage reporting is non-standard (excludes infinite bands from primary metric)
- No sensitivity analysis for parameter misspecification

I think the paper is a solid contribution that would benefit from some revisions but is likely acceptable at a good venue. The theoretical contributions are genuine, and the limitation to linear PDEs is clearly stated in the Discussion. The paper could be strengthened, but the core contribution is sound.

Actually, looking at the harsh critic's points more carefully: the main structural concern is the linear-PDE scope. But the paper is open about this in the Discussion. The abstract saying "broad class" is slightly vague but not misleading — linear PDEs ARE a broad class (heat, wave, advection-diffusion, Helmholtz, etc.). And the paper explicitly states "we derived how weighted CP can be applied to linear PDEs" in the conclusion.

The second concern about Remark 4.5 is valid but minor — it's a remark about potential future extension, not a main claim.

I think this is a Accept-level paper. But with a score around 5.5. Let me check whether that's consistent.

Actually, I think I should make the decision line up with the score. A 5.5 is borderline. Let me just assign Accept to reflect that the paper has genuine contributions that outweigh the limitations, but the score reflects that it's not a strong accept.

Actually, I think Reject is too harsh. The paper makes a clear contribution. Let me go with Accept and 5.5.Now let me write the final review.

---

## Summary

This paper studies conformal prediction (CP) for time-dependent PDE surrogate models, where exchangeability between calibration and test samples is violated due to temporal drift. The authors prove (Theorem 4.1) that in function space, solution distributions at different times are mutually singular (TV distance = 1), making exact CP coverage impossible. They then show (Theorem 4.2) that for discretized *linear* PDEs with Gaussian initial conditions, the solution distribution at any time is Gaussian with closed-form mean and covariance, enabling exact likelihood-ratio weights for weighted conformal prediction (WCP). Experiments on a family of second-order linear PDEs demonstrate that WCP systematically achieves target coverage where naïve CP and LSCI fail.

## Strengths

1. **Theorem 4.1 (function-space impossibility)**: Proves that for the heat equation with Gaussian initial conditions, TV distance between solution distributions at any two distinct times is exactly 1, establishing a fundamental barrier for CP in the infinite-dimensional setting. This is a clean theoretical result that goes beyond the generic observation that "exchangeability fails."

2. **Theorem 4.2 (closed-form Gaussian dynamics)**: Derives the exact Gaussian distribution of the discretized PDE solution for any linear spatial operator with linear boundary conditions, giving explicit mean and covariance via matrix exponentials. This directly enables closed-form likelihood ratios for weighted CP, which is the paper's core methodological contribution.

3. **Empirical validation**: Table 1 and Figure 3 systematically show that WCP maintains target 90% coverage across increasing prediction horizons on a parametric family of second-order PDEs where both naïve CP and LSCI exhibit severe undercoverage (e.g., LSCI drops to 0% coverage). The paper also transparently reports the fraction of infinite-band samples $n_\infty$, providing an honest diagnostic when the distribution shift is too large.

4. **Clean conceptual framing**: The paper carefully distinguishes the function-space impossibility (Theorem 4.1) from the discretized feasible case (Theorem 4.2), avoiding conflation between the two settings and clarifying why CP can work in practice despite the theoretical obstruction.

## Weaknesses

### Major

1. **Scope limited to linear PDEs, with tension between framing and content.**  
   Theorem 4.2 requires (i) a *linear* spatial differential operator, (ii) *linear* boundary conditions, and (iii) a Gaussian (or location-scale) initial distribution. The abstract says "a broad class of PDE problems" and the introduction says "For a broad class of PDEs," which could reasonably describe linear PDEs, but the contrast with high-impact nonlinear PDE targets (Navier–Stokes, Burgers', reaction-diffusion) that dominate the scientific ML literature is stark. The Discussion does acknowledge the linear-PDE scope, but the earlier framing invites overestimation of the method's reach. This is not a fatal flaw — the paper is honest about its assumptions in the technical sections — but the abstract and introduction should more precisely signal the linearity requirement.

2. **Remark 4.5 about continuous-solution coverage is asserted, not substantiated.**  
   The remark states: "we provide asymptotic—and in some cases even non-asymptotic—guarantees for the PDE solution $u(x,t)$ in the original space." No formal statement, bound, proof sketch, or even a concrete example follows; the remark only gestures at "leveraging numerical error guarantees of the scheme." Since all experiments evaluate coverage on the discretized grid (the same grid used for calibration), the claim about continuous-solution coverage is unsupported. This is a minor overclaim — the paper's main contribution is about discretized solutions — but it should be either removed or made precise with a concrete bound (e.g., "if the numerical scheme has error $\epsilon$, then coverage on the true solution is at least $1-\alpha - \epsilon$").

### Minor

3. **Coverage is reported on finite-band samples only, with no primary overall-coverage metric.**  
   When WCP produces infinite bands, the paper "exclude[s] the sample and only predict[s] coverage of the other samples." The paper separately reports $n_\infty$ and discusses the issue, so it is not hiding the behavior. However, the headline coverage numbers exclude the infinite-band samples, which means they do not reflect the full marginal guarantee (infinite bands trivially cover). Reporting overall coverage (including infinite bands) as a primary metric, with finite-band coverage as a secondary diagnostic, would be more standard and less likely to mislead.

4. **Real-world example lacks detail in the main text.**  
   The pulsed-thermography experiment is described in four sentences, with all implementation details (parameter estimation, discretization scheme, likelihood ratio computation) relegated to Appendix A.6 (stripped by the parser). Given that this is the only out-of-lab validation, the main text should at minimum summarize the key experimental choices and results. The claim that the cooldown phase "approximately follows the heat equation" is also vague — radiative cooling (Stefan–Boltzmann) introduces nonlinearity that may or may not be negligible.

5. **No sensitivity analysis for PDE parameter misspecification.**  
   The method assumes the PDE parameters are known exactly to compute the likelihood ratio. In practice, parameters may be uncertain. A small experiment with mismatched parameters (e.g., using $a+\epsilon$ instead of $a$ when computing weights) would significantly strengthen the paper's practical relevance. The paper mentions this as future work but does not even a small synthetic test.

### Trivial

6. **Figure 2 description is slightly confusing.** The text references "calibration at time step $\delta$" and "$4\delta$" but the figure labels show specific time steps (t=16, 36, 46, etc.) without a clear mapping to multiples of $\delta$.

## Nice-to-Haves

- A brief discussion of how weighted CP might extend to nonlinear PDEs (e.g., via local linearization, ensemble estimation of density ratios, or particle-filter-style approximations) would make the contribution feel less narrow and guide future work.
- Reporting 95% confidence intervals for coverage estimates (the standard error at n=5000 and 90% coverage is ~0.4%) would improve statistical rigor.

## Removed Points

The following points from the harsh critic were removed after verification against the paper:

- **"Coverage reporting on finite-band samples is misleading"** — REMOVED. The paper transparently reports $n_\infty$ alongside coverage and explicitly discusses the issue in the text ("In practice, this can be addressed by...considering the overall coverage including the trivial bands"). No deception is present.
- **"LSCI baseline tuning is strange / suggests handicapping"** — REMOVED. The paper uses 5000 band samples, which makes LSCI *stronger* (more candidate bands → more conservative coverage). The claim "push LSCI to over-coverage" correctly describes this effect.
- **"Real-world example insufficiently described / may be cherry-picked"** — PARTIALLY REMOVED. The concern about insufficient detail in the main text is kept (Minor #4), but the speculation about "cherry-picking" and "nonlinear radiative term" without evidence from the paper is removed as speculation.
- **"Theorem 4.1 relevance is limited"** — REMOVED. This is a subjective judgment; the theorem provides genuine theoretical insight and cleanly motivates the discretized setting.
- **"Missing appendix material"** — REMOVED per hard rule: parser-stripped appendix content is not a valid weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Sharpen the abstract and introduction** to explicitly state "linear PDEs with Gaussian initial conditions" rather than "a broad class of PDEs."
2. **Either remove or substantiate Remark 4.5.** If retaining, provide at least a simple bound linking discrete coverage to continuous coverage (e.g., via numerical discretization error).
3. **Report overall coverage including infinite-band samples** as the primary metric, with finite-band coverage and $n_\infty$ as secondary.
4. **Add a small parameter-misspecification experiment** to test robustness when the PDE parameters used to compute likelihood ratios differ from the true parameters.

## Calibration Anchors

**Round 1 (bracketing):**
- Weak band anchors (avg < 3.5): "Regression Conformal Prediction under Bias" (2.50), "Physics-Informed Neural Networks with Trust-Region SQP" (3.00), "Soft Checksums" (2.33), "In-Context Neural PDE" (3.40) — all clearly weaker than the current paper.
- Middle band anchors (3.5–7.5): "Non-Exchangeable Conformal Risk Control" (6.00), "Kernel-based Optimally Weighted Conformal Time-Series" (6.00), "Wasserstein-Regularized Conformal Prediction" (6.67) — comparable in contribution quality.
- Strong band anchors (7.5+): "PhyMPGN" (8.00), "Learning Distributions of Complex Fluid Simulations" (7.60) — these papers have broader experimental scope and less restrictive assumptions.

**Round 2 (narrowing, 4.5–6.0 and 6.0–7.5):**
- "Solving Differential Equations with Constrained Learning" (5.25, Accept) — weaker empirical support than current paper.
- "Efficient Certification of PINNs" (5.50, Reject) — similar score level but less complete contribution.
- "Approximating Full Conformal Prediction" (5.75, Accept) — comparable quality; both have clear contributions with some limitations.
- "Leave-One-Out Stable CP" (6.25, Accept) — more polished but less novel in application domain.
- "Flexible Active Learning of PDE Trajectories" (6.80, Reject despite score) — more comprehensive experiments but less theoretical depth.
- "Active Learning for Neural PDE Solvers" (7.00, Accept) — stronger experimental scope.

**Final score**: The paper sits between the 5.75 and 6.00 anchors. It has clean theory and a well-executed empirical study for its scope, but the linear-PDE limitation and several minor presentation issues prevent it from reaching the 6+ range. The theoretical contributions (Theorems 4.1 and 4.2) are genuine and the empirical results convincingly show that WCP works where baselines fail within this scope.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>