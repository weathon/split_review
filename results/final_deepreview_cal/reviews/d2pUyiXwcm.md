Now I have a good calibration picture. Let me construct the bracket.

**Round 1 bracket:** The paper is clearly above the weak anchors in the 2.5-3.33 range (simple PINN methods with poor experiments and no theory). It sits somewhere in the middle band. Comparing to the middle-band anchors:
- HyPER (avg 5.0) - similar hybrid correction approach but weaker theory, fewer problems, unfair comparisons criticized by reviewers → our paper is stronger
- GP-PDE (avg 5.75) - good GP solver but limited geometry, originality concerns flagged → our paper is comparable or slightly stronger (more surrogate types, higher dimensions, theory)
- PIG (avg 6.50) - good experiments but limited to low-dimensional problems, no convergence theory → comparable

**Narrowed bracket:** 5.5–6.5

Let me write the final review.

## Summary
2-3 sentence summary.

The paper introduces SCaSML, a framework that corrects pre-trained surrogate PDE solvers (PINNs, GPs) at inference time by deriving a structure-preserving defect PDE and solving it with Multilevel Picard (MLP) Monte Carlo simulation. The authors prove a product-form error bound showing the final error scales as the product of surrogate and simulation errors, implying a faster convergence rate. Experiments on five high-dimensional PDEs (up to 160 dimensions) show consistent 20–80% error reduction over base surrogates.

## Strengths
1. The structure-preserving defect PDE (Fact 2.3) is a clean and useful observation: the error of a surrogate satisfies a semi-linear PDE of the same form as the original, making it amenable to stochastic solvers. This framing is novel in the context of neural-network PDE surrogates.
2. Theorem 2.5 and Corollary 2.6 provide a theoretical error bound where the final L² error is a product of surrogate error and simulation error — a genuinely new result for hybrid surrogate-Monte Carlo methods. The empirical verification in Figure 4 (steeper slopes for SCaSML than the base GP across d=20–80) corroborates the predicted scaling.
3. Comprehensive empirical evaluation across five diverse PDE families (linear convection-diffusion, viscous Burgers with two surrogate types, HJB/LQG, diffusion-reaction) in dimensions up to 160, with consistent improvements across L², L∞, and L¹ metrics.

## Weaknesses

### Major
1. **Assumption 2.4 is strong and unverified.** The theoretical product bound (Theorem 2.5) depends critically on sup-norm bounds on the PDE residual and W^{1,∞} bounds on the surrogate error. For neural network surrogates trained with PINN losses (which minimize an empirical L² residual), there is no general guarantee that the residual is bounded in sup-norm, let alone that it scales like the L² training error. The paper does not compute or report sup-norm residuals for any experimental surrogate. While Figure 4 empirically validates the predicted scaling law for a GP surrogate, the theory for PINN surrogates remains disconnected from verification. This is a gap that should be addressed by either (a) relaxing the assumption, (b) empirically verifying it on the experimental surrogates, or (c) clearly acknowledging the gap.

### Minor
2. **Unfair clipping thresholds in MLP vs SCaSML comparisons.** In the LQG experiment, the naive MLP uses a clipping threshold of 10 while SCaSML uses 0.1; similar disparities exist for VB (1.0 vs 0.01) and DR (10 vs 0.01). The paper explains this by noting the defect has smaller magnitude, but this makes the MLP comparison not apples-to-apples as a reference baseline. The primary comparison (surrogate vs SCaSML) is unaffected, which is the paper's main claim, but the MLP comparison should be interpreted cautiously. The paper does reference fixed-budget comparisons in Appendix G.7 but these are not visible from the main text.

3. **Novelty framing is somewhat overstated.** The "Structural-preserving Law of Defect" is derived by subtracting one PDE from another — a mathematically elementary operation that any linear transformation of a semi-linear PDE yields another semi-linear PDE. The genuine contribution is recognizing that this structure preservation enables MLP-based correction. Relatedly, the LLM inference-time scaling analogy (introduction) is largely decorative and does not add technical content. The paper's own description (Section 2.1, "the surrogate handles the low-frequency part...") provides a more precise framing.

4. **The cost of evaluating the surrogate's residual ε at arbitrary path points is not analyzed separately.** Computing ε(t, X_t) requires evaluating the surrogate's time derivative, gradient, and Hessian at each Monte Carlo step — a significant cost for neural network surrogates. Table 1 reports total runtime (SCaSML is 2–7× slower than naive MLP), but does not break down how much time is spent on surrogate evaluation vs. Monte Carlo simulation vs. residual computation. This makes it hard to assess where the computational bottleneck lies.

5. **No ablation on clipping threshold sensitivity.** The clipping thresholds differ between methods and problems (from 0.01 to 10), and their impact on results is not analyzed. Since clipping directly affects both accuracy and stability, sensitivity analysis would strengthen reproducibility and practical deployment guidance.

### Trivial
6. Minor presentation artifacts: Table 1 uses a notation "SCA²SM¹" that is inconsistent with the text's "SCaSML"; the variable notation ũ is used both for the defect (u - û) and the surrogate (û) in different places.

## Nice-to-Haves
- The scaling law (Corollary 2.6) is verified empirically only for the GP surrogate (Figure 4). Verifying it with a PINN surrogate would strengthen the claim's generality.
- The paper could discuss the case where the surrogate is already very accurate (as in the DR experiment, where only 6–11% improvement is seen). The current framing emphasizes the 20–80% range but could more explicitly discuss diminishing returns.
- Reporting error bars on the numerical results (especially for MLP and SCaSML which involve stochastic simulation) would improve reproducibility assessment.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Provide empirical sup-norm residuals for the surrogates used in experiments to verify the theoretical assumption, or relax Assumption 2.4 to a more realistic condition.
2. Add a compute-budget-controlled comparison in the main text (not just the appendix) where MLP and SCaSML are compared at equal runtime, or at least add a runtime-normalized error plot.
3. Include a breakdown of SCaSML runtime: time spent on surrogate residual evaluation vs. Monte Carlo path simulation vs. other overhead.
4. Tone down the "first inference-time scaling framework" language and replace the LLM analogy with the paper's own more precise framing (surrogate as control variate for variance reduction).

## Score and Decision
Score: 6.0

Now let me run calibration.

Actually wait, I've already done my calibration analysis above. Let me proceed with writing the final review, including the anchor list.

Let me trace through my calibration:

**Round 1 bracket:**
- Query 1 (weak, score < 3.5): IDs: 5sPgOyyjG5 (avg 3.0), HDmmwwTIlf (avg 2.5), LwAG269lIq (avg 3.0), R5FzCFR5yU (avg 3.33) — all simple PINN/ML methods without strong theory or high-dimensional experiments
- Query 2 (middle, 3.5–7.5): IDs: LgfaMR6Sst (avg 6.80), 3ep9ZYMZS3 (avg 5.00), x4ZmQaumRg (avg 7.00), Q9OGPWt0Rp (avg 5.25)
- Query 3 (strong, >7.5): IDs: fU8H4lzkIm (avg 8.0), AoraWUmpLU (avg 8.0), uKZdlihDDn (avg 7.6), Xo0Q1N7CGk (avg 8.0) — these are top-tier papers, mostly not directly about PDE solving methods

Bracket: Between low (~3) and strong (~8), clearly in the middle band. Initial bracket: 5–7.

**Round 2 narrowing:**
- Query 1 (4.5–7.5): 3ep9ZYMZS3 (avg 5.0), LgfaMR6Sst (avg 6.80), q4AEBLHuA6 (avg 5.75), 5rfj85bHCy (avg 5.0)
- Query 2 (4.5–7.5): 5rfj85bHCy (avg 5.0), y5B0ca4mjt (avg 6.50), XaqaitclOA (avg 5.0), ApjY32f3Xr (avg 5.25)

Read in full: 3ep9ZYMZS3 (avg 5.0), q4AEBLHuA6 (avg 5.75), y5B0ca4mjt (avg 6.50)

Comparison:
- vs HyPER (5.0): Our paper has stronger theory, more problems, higher dimensions. Clearly better.
- vs GP-PDE (5.75): Our paper has broader scope. Better.
- vs PIG (6.50): PIG has good experiments but limited to low dimensions and no convergence theory. Our paper tackles much higher dimensions and has theory (though with strong assumptions). Comparable overall.

I'd place the paper at 6.0 — clearly above 5.75 papers but slightly below 6.50 papers due to the issues with theoretical assumptions and overclaiming.

Now let me construct the full review.Now I have all the calibration data I need. Let me write the final consolidated review.

## Summary

This paper introduces SCaSML, a framework that corrects pre-trained surrogate PDE solvers (PINNs, GPs) at inference time by deriving a structure-preserving defect PDE and solving it with Multilevel Picard (MLP) Monte Carlo simulation. The authors prove a product-form error bound showing the final error scales as the product of surrogate error and simulation error, implying a faster convergence rate. Experiments on five high-dimensional PDEs (up to 160 dimensions) show consistent 20–80% error reduction over base surrogates.

## Strengths

1. **Structure-preserving defect PDE (Fact 2.3).** The derivation showing that the error PDE inherits the semi-linear form of the original problem is a clean and useful observation. Unlike classical defect-correction methods that rely on asymptotic expansions unavailable for neural networks, this structural preservation is what enables the use of efficient Monte Carlo solvers (MLP) for the correction step. The contrast with iterative methods (which produce nested simulation hierarchies with degrading convergence rates) is well-articulated in Section 2.2.

2. **Provably accelerated convergence (Theorem 2.5 and Corollary 2.6).** The product-form error bound — final L² error bounded by the product of surrogate error and simulation error — is a genuinely new theoretical result for hybrid surrogate-Monte Carlo methods. The empirical verification in Figure 4 (steeper slopes for SCaSML vs. base GP across d=20,40,60,80) corroborates the predicted scaling, lending credibility to the claim.

3. **Comprehensive empirical validation across diverse high-dimensional PDEs (Table 1).** The method is evaluated on five PDE families (linear convection-diffusion, viscous Burgers with PINN and GP surrogates, HJB/LQG, diffusion-reaction) with dimensions up to 160, using two different surrogate types. SCaSML consistently reduces relative L² error across all problem-surrogate combinations, and the breadth of validation demonstrates generalizability beyond a single surrogate class or PDE type.

4. **Demonstration of inference-time scaling (Figure 3b).** The paper shows that error steadily decreases as the number of inference-time Monte Carlo samples increases, validating the "elastic compute" concept and empirically distinguishing SCaSML from approaches where additional compute at inference yields no accuracy gain.

## Weaknesses

### Major

1. **Assumption 2.4 is strong and unverified for neural network surrogates.** The product bound (Theorem 2.5) depends on sup-norm bounds on the PDE residual and W^{1,∞} bounds on the surrogate error. For neural networks trained with PINN losses (minimizing an empirical L² residual), there is no general guarantee that the residual is bounded in sup-norm, let alone that it scales like the L² training error m^{-γ}. The residual involves second spatial derivatives of the network through the Hessian in ℒ; controlling these in sup-norm from L² training data is not justified. The paper does not compute or report sup-norm residuals for any experimental surrogate. While Figure 4 empirically validates the scaling law for a GP surrogate, the theoretical assumptions for PINN surrogates remain unverified. This disconnect between the theory and the primary experimental setting is the paper's most significant weakness.

### Minor

2. **Unfair clipping thresholds in the MLP comparison.** In the LQG experiment, the naive MLP uses a clipping threshold of 10 while SCaSML uses 0.1; similar disparities exist for VB (1.0 vs 0.01) and DR (10 vs 0.01). The paper explains that clipping reflects the smaller magnitude of the defect, but this makes the MLP-vs-SCaSML comparison not apples-to-apples. The primary comparison (surrogate vs. SCaSML) is unaffected, but the reader cannot fully attribute SCaSML's advantage over MLP to algorithmic superiority rather than hyperparameter choice. The paper references fixed-budget comparisons in Appendix G.7, but these are not visible from the main text.

3. **Novelty framing is somewhat overstated.** The "Structural-preserving Law of Defect" is derived by subtracting one PDE from another — a mathematically elementary operation that any linear transformation of a semi-linear PDE yields another semi-linear PDE. The genuine contribution is recognizing that this structure preservation enables MLP-based correction, not the derivation itself. Relatedly, the LLM inference-time scaling analogy (introduction) is decorative rather than substantive; the paper's own description in Section 4 ("our framework uses the machine learning model as a control variate") provides a more accurate and less grandiose framing.

4. **Cost of surrogate residual evaluation is not analyzed.** Computing ε(t, X_t) at arbitrary Monte Carlo path points requires evaluating the surrogate's time derivative, gradient, and Hessian at each step — a potentially significant cost for neural network surrogates. Table 1 reports total runtime (SCaSML is 2–7× slower than naive MLP across problems) but provides no breakdown of how much time is spent on surrogate evaluation vs. Monte Carlo simulation vs. residual computation. This makes it difficult to assess the computational bottleneck or optimize the approach.

5. **No ablation on clipping threshold sensitivity.** Clipping thresholds range from 0.01 to 10 across methods and problems, directly affecting both accuracy and stability. An ablation study would strengthen reproducibility and help practitioners deploy the method.

6. **Scaling law only verified for GP surrogates.** Figure 4 validates the predicted convergence rate only for the GP surrogate. Verifying it with a PINN surrogate (the primary surrogate type used in the paper) would significantly strengthen the empirical case.

### Trivial

7. Notation inconsistency: Table 1 and some figures use "SCA²SM¹" while the text uses "SCaSML". The variable ũ is used to denote both the defect (u − û) and the surrogate (û) in different contexts.

## Nice-to-Haves

- The DR experiment (where SCaSML achieves only 6–11% improvement over an already-accurate surrogate) is consistent with the theory (product bound would make the total error very small but the Monte Carlo noise floor may dominate). This case could be discussed more explicitly.
- Including error bars or confidence intervals on the numerical results (especially for methods involving stochastic simulation) would improve the reader's ability to assess statistical significance.

## Removed Points

- **"The method is not novel because control variate methods exist"**: The paper itself acknowledges this in Section 4: "our framework uses the machine learning model as a control variate." The novelty is the specific combination with structure-preserving defect PDE and MLP, not the control variate concept itself. The paper frames this appropriately.
- **"GP surrogate trained with only 20 Newton iterations is weak"**: The critic acknowledges this is "not a weakness per se." The range of surrogate quality demonstrates the method's robustness, not a flaw.
- **"The derivation is mathematically elementary"**: While true, this is a criticism of framing (kept in Minor #3) rather than a substantive weakness. The paper's contribution is the insight, not the algebraic difficulty.
- **"Training and inference separation claim is standard"**: The paper's Remark 2.2 explicitly describes this as "natural and parallels standard practices," so the paper does not overclaim here.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide empirical sup-norm residuals for the surrogates used in experiments to verify Assumption 2.4, or relax the assumption to a more realistic condition (e.g., L² control with higher-order Sobolev norm assumptions).
2. Add a compute-budget-controlled comparison in the main text — an error-vs-runtime curve where both SCaSML and the naive MLP are given varying amounts of compute — so readers can directly assess algorithmic vs. budget-driven gains.
3. Include a runtime breakdown table showing time spent on: surrogate residual evaluation (ε), Monte Carlo path simulation, and overhead.
4. Replace the LLM inference-time scaling analogy with the paper's own precise framing (surrogate as a control variate). The paper's technical content is stronger than this framing suggests.

## Score and Decision

**Calibration trace.**

**Round 1 (bracketing):**
- Low band (avg < 3.5): 5sPgOyyjG5 (avg 3.0, PINN+Monte Carlo estimation), HDmmwwTIlf (avg 2.5, hyperbolic conservation laws), LwAG269lIq (avg 3.0, adjoint PDE discovery), R5FzCFR5yU (avg 3.33, hybrid numerical PINNs) — all simple methods without theory or high-dimensional experiments. Our paper is clearly stronger.
- Middle band (3.5 < avg < 7.5): LgfaMR6Sst (avg 6.80, active learning for PDEs), 3ep9ZYMZS3 (avg 5.0, HyPER — hybrid correction for surrogate rollout), x4ZmQaumRg (avg 7.0, AL benchmark), Q9OGPWt0Rp (avg 5.25, connecting solutions to BCs). Our paper sits in this band.
- Strong band (avg > 7.5): fU8H4lzkIm (avg 8.0, PhyMPGN), AoraWUmpLU (avg 8.0, Neural ODEs), uKZdlihDDn (avg 7.6, diffusion graph networks), Xo0Q1N7CGk (avg 8.0, grid cells). Our paper is clearly below this tier.

**Initial bracket: 5.0–7.0.**

**Round 2 (narrowing):**
Read in full: 3ep9ZYMZS3 (avg 5.0, HyPER) — similar hybrid correction approach but weaker theory (no convergence guarantees), fewer problems (2D Navier-Stokes only), and was criticized by reviewers for unfair comparisons; our paper is stronger. q4AEBLHuA6 (avg 5.75, GP PDE solver) — good method but limited to simple geometries and low dimensions, overclaiming concerns flagged; our paper is comparable or slightly stronger. y5B0ca4mjt (avg 6.50, PIG) — clean experiments, good presentation, but limited to low-dimensional PDEs and no convergence theory; our paper has higher dimensions and theory but weaker presentation.

**Final score: 6.0.** The paper is clearly above the 5.0–5.75 anchors (stronger theory, more comprehensive evaluation, higher dimensions) but does not reach the 6.5 level of PIG due to the unverified theoretical assumption and some overclaiming in framing.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>