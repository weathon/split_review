Now I have a clear picture. Let me write the final review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes PI-RGSM and PI-RGSM-K, PINN-based models for groundwater seepage in river-canal systems. The key ideas are: (1) using hard constraints for boundary/initial conditions to avoid BC/IC loss terms, and (2) incorporating hydrogeological parameters (hydraulic conductivity \(K\), recharge \(W\), boundary water levels \(H_a, H_b\)) as network inputs so a single trained model can generalize across scenarios without retraining. PI-RGSM-K extends this by treating \(K\) as a spatially-varying function \(K(x,y)\) for heterogeneous aquifers. Experiments against MODFLOW reference data on synthetic 2D problems show \(R^2 > 0.97\).

## Strengths

- **Hard-constraint formulation demonstrably improves training stability without observations.** The paper constructs an explicit constraint function \(C(x,y,t) = (x-x_{\min})(x_{\max}-x)t / N_s\) that forces the network output to exactly satisfy Dirichlet boundary and initial conditions. The empirical evidence in Table 2 is concrete: PI-RGSM achieves \(R^2 > 0.98\) using zero observational data, whereas baseline PINNs (using soft-constraint BC/IC losses) produce negative \(R^2\) values under the same observation-free setting. This directly supports the claim that hard constraints eliminate the need for tedious weight tuning among competing loss terms.

- **Input feature fusion enables zero-shot generalization across hydrogeological scenarios without retraining.** By feeding hydrogeological parameters (\(K, W, H_a, H_b\)) as network inputs alongside spatiotemporal coordinates (Section 2.4), the model learns a family of PDE solutions rather than a single one. The experiments in Tables 3–5 support this: PI-RGSM maintains mean \(R^2 > 0.977\) across varying \(W\) and \(K\) (Table 3), mean \(R^2 > 0.99\) across varying boundary conditions (Table 4), and the PI-RGSM-K variant achieves mean \(R^2 > 0.98\) under a heterogeneous \(K(x,y)\) field (Table 5) — all with a single training session. This is a practically useful advance over standard PINNs that require retraining for each new parameter setting.

## Weaknesses

### Fatal
None.

### Major
- **The heterogeneous capability (PI-RGSM-K) is tested on a trivial linear gradient that does not support the claimed generality for "complex" heterogeneity.** The paper claims PI-RGSM-K can simulate "complex dynamic groundwater seepage situations" and "complex seepage environments" (abstract, line 4), yet the only heterogeneous field tested is \(K(x,y) = -0.01x + 0.5\) (line 154) — a simple 1D linear gradient that is practically indistinguishable from a homogeneous case with a trend. The paper mentions that "\(K\) can also be parameterized using other functions... or even as a randomly generated hydraulic conductivity field" (line 154), but provides no experiments with genuinely complex heterogeneity (e.g., random log-normal fields with spatial correlation, layered media, discontinuous property distributions). The central claim of PI-RGSM-K's capability for "complex" environments is therefore unsupported by the evidence presented. This is a significant gap between the claims and the evaluation.

- **No ablation study isolates the individual contributions of the two main design choices.** PI-RGSM differs from baseline PINNs in two ways: (a) replacing soft BC/IC constraints with hard constraints, and (b) training on 10,000 randomly sampled parameter configurations versus the baselines' single fixed configuration. The Table 2 comparison conflates both differences — we cannot tell whether PI-RGSM's better performance comes from the hard constraints, from the broader training distribution, or from their interaction. An ablation comparing (i) a standard PINN trained on 10k diverse scenarios vs (ii) PI-RGSM without hard constraints vs (iii) PI-RGSM with hard constraints would be needed to properly attribute the improvement. This lack of isolation weakens the paper's claims about what each component contributes.

### Minor
- **The "self-supervised" framing is overstated.** The paper repeatedly characterizes PI-RGSM as "self-supervised" and claims it "eliminates dependence on observations" (lines 4, 14, 168), implicitly suggesting that baseline PINNs require labeled data. However, standard PINNs already train without labeled observational data — they use the PDE residual as the primary loss, which is the defining feature of physics-informed learning. The paper's own experiments run baselines "without observations" (line 166). The actual novelty of PI-RGSM is more specific: hard constraints eliminate the need for BC/IC loss terms and the associated weight tuning, not the need for observations per se. The framing inflates what is new.

- **Boundary conditions at \(y=0\) and \(y=10\) are never specified.** The domain is 2D (x: 0–40m, y: 0–10m). The paper specifies Dirichlet boundary conditions at the left and right canals (the x-boundaries), and the hard constraint function \(C(x,y,t) = (x-x_{\min})(x_{\max}-x)t/N_s\) enforces conditions only on those x-boundaries and at \(t=0\). The paper never states what boundary conditions apply at \(y=0\) and \(y=10\). Since the PDE residual (Eq. 13) includes \(\partial/\partial y\) terms, the y-boundary conditions are necessary for the well-posedness of the forward problem and for the correctness of the MODFLOW reference data. This omission affects both method reproducibility and evaluation validity.

- **Evaluation relies exclusively on \(R^2\).** Reporting only \(R^2\) without spatial error maps, maximum absolute error, or error distributions makes it difficult to assess where the model performs poorly (e.g., near boundaries, at parameter range edges, or under extreme conditions). The figures show visual agreement, but quantitative spatial error analysis would strengthen the evaluation.

- **No computational cost or training time is reported.** The paper emphasizes that the model can "adapt to and accurately predict diverse seepage situations with just one training session" but never reports training time, inference speed, or how these compare to retraining a standard PINN per scenario or running MODFLOW directly.

### Trivial
- Line 264 contains a garbled sentence fragment ("with \(R^2\) exceeding 0.99.500m to 3.500m") that appears to be a formatting corruption.
- Table 5 caption reads "Performance of PI-RGSM" but the surrounding section is about PI-RGSM-K.

## Nice-to-Haves
- The engineering control loss term (\(LOSS_{EC}\), Eq. 7) that penalizes hydraulic head dropping below a user-specified threshold is a practical design choice connecting the model to water resource management, though it is not the paper's main focus.
- A comparison against alternative surrogate modeling approaches (e.g., a neural network trained purely on MODFLOW data, or POD with interpolation) would strengthen the case that the physics-informed approach offers advantages beyond other fast-approximation methods.

## Removed Points
These points were raised by reviewers but are not included as weaknesses in the main review, with justification:
- **"Baseline comparison is structurally unfair"** — Removed. The baselines are trained on exactly the same fixed scenario they are tested on (specialized to it), while PI-RGSM is trained on 10k diverse scenarios. The comparison is not unfair to the baselines; the real issue (addressed above) is the lack of ablation to isolate contributions.
- **"Missing prior work citation on hard constraints in PINNs"** — Removed per policy (do not mention missing related works).
- **"10,000 training samples and 1,000 iterations are too few"** — Removed. This is speculative; the model achieves \(R^2 > 0.98\) with these settings, suggesting convergence is adequate for the problem.
- **"Dupuit approximation not justified"** — Removed. The paper states "assuming negligible variation in hydrogeological conditions in the vertical direction" (line 28), which is the Dupuit assumption.
- **"Specific storage vs specific yield terminology"** — Removed. This is a domain-specific terminology point that does not affect the paper's method or results.
- **Strength Finder's claim about "transparent comparison against multiple baselines"** — Removed. The comparison is on a single fixed condition and does not constitute a comprehensive baseline study.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add an ablation study: compare (a) standard PINN trained on 10k diverse scenarios, (b) PI-RGSM without hard constraints (soft-constraint version with diverse parameter inputs), and (c) PI-RGSM with hard constraints. This would isolate whether the performance gain comes from the diverse training data, the hard constraints, or their combination.
- Test PI-RGSM-K on a genuinely heterogeneous K-field — at minimum a random log-normal field with spatial correlation — to support the claim that the model handles "complex" heterogeneity.
- Specify the y-boundary conditions in the problem setup and explain how they are enforced (or why they are unnecessary).
- Report additional error metrics (MAE, max error, spatial error maps) and computational cost (training time, inference time vs MODFLOW runtime).

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>