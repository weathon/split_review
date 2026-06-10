## Summary

This paper proposes applying Heavy Ball (HB) momentum to existing diffusion ODE solvers to expand their stability regions and suppress divergence artifacts at low step counts. It also introduces a new method family, Generalized Heavy Ball (GHVB), that interpolates between adjacent-order Adams-Bashforth methods, offering a tunable trade-off between accuracy and artifact suppression. Both techniques are training-free, require negligible overhead, and are evaluated on pixel-based (ADM), latent-based (DiT), and text-to-image (Stable Diffusion) models.

## Strengths

- **GHVB as a principled interpolation between orders**: The GHVB construction (Section 4.2, Eq. 15) provides a clean, algebraically derived family where a single damping coefficient β continuously interpolates between adjacent-order AB methods (e.g., between DDIM and PLMS2). This is validated empirically in the L2 error plot (Fig. "GHVB_l2_norm"), where GHVB 1.1–1.9 errors smoothly span the gap between DDIM and PLMS2 — a novel and non-trivial contribution.

- **Consistent gains across three model classes**: The methods are evaluated on pixel-based ADM (FID, Fig. 15), latent-based DiT (FID, Fig. 16), and Stable Diffusion text-to-image (magnitude score, Figs. 14–15). HB momentum applied to DPM-Solver++ and LTSP consistently improves FID on ADM, and GHVB 3.8/3.9 improve FID over PLMS4 on DiT at low step counts. This breadth rules out architecture-specific artifactual improvements.

- **Stability region expansion directly visualized**: Figures 5–8 (for HB) and 10–13 (for GHVB) provide clear boundary locus plots showing systematic enlargement of stability regions as β decreases. These plots directly support the paper's proposed mechanism and are a clean visual contribution.

- **Empirical convergence order verification**: Section 5.4 (Fig. "GHVB_order_of_convergence") numerically computes convergence orders for GHVB 0.5 → ~0.5 and GHVB 1.5 → ~1.5, providing supporting evidence for the theoretical convergence claims.

- **Negligible computational overhead**: Both techniques add only a single velocity variable v_n per step — no extra function evaluations, no retraining, no model modification — making them practical drop-in replacements for existing solvers.

## Weaknesses

### Fatal
None.

### Major

- **The stability-region explanation for artifacts is a plausible hypothesis, not a validated causal mechanism.** The paper's central narrative (Section 3.2) linearizes the ODE around the converged solution x\* (where ε̅(x\*) = 0) and applies the test equation u' = λu via stiffness analysis. For most of the diffusion trajectory the state is far from x\* — it starts as pure noise — and artifacts develop during intermediate steps, not near convergence. The Jacobian ∇ε̅(x\*) evaluated at the clean-image fixed point may have little relation to dynamics during artifact onset. The paper uses "We hypothesize" (line 129) and states its assumptions (σ-dependence of ε̅ is negligible, line 129), but the introduction asserts "we...found that the narrow stability region...can cause solutions to diverge" (line 18), overstating the confidence level. The paper does not validate that the method works *because* of the stability-region mechanism (e.g., by tracking projection onto suspected unstable eigenvectors during sampling and showing they remain bounded when stability regions are enlarged). While the methods are empirically effective, the theoretical explanation remains untested, leaving alternative explanations (e.g., OOD network behavior, stiffness) equally consistent with the data.

### Minor

- **Artifact proxy metric (magnitude score) is uncalibrated.** The paper uses a threshold-τ count of high-magnitude latent variables as a quantitative artifact metric (Section 5.1) and acknowledges "images without artifacts can also have high latent magnitudes in some regions" (line 123). However, the metric is not validated against human perception or any established artifact measure. The paper would benefit from calibration or a secondary validation showing correlation with human-rated artifact severity.

- **Parameter β requires tuning with no principled guidance.** The paper reports that "using HB 0.8 with PLMS4 can worsen FID scores" on DiT (line 317), and the optimal β depends on the model, step count, and solver. No recipe is provided for choosing β (e.g., based on step size, Lipschitz constant, or spectral radius). This limits practical utility, as practitioners must grid-search for each new setting.

- **High-order convergence for GHVB 2.5/3.5 is not reliably achieved.** The paper honestly admits (line 334) that "the estimated error may be too small...and other sources of error may hinder their convergence." This partially undermines the high-order convergence claim for larger β values.

### Trivial
None.

## Nice-to-Haves

- Provide principled guidance for choosing β, e.g., based on step size or empirical spectral properties of the Jacobian.
- Calibrate the magnitude score against human judgments or an established metric.
- Add error bars or confidence intervals for the magnitude score (a new ad-hoc metric where variability would be informative).

## Removed Points

The following points from the input reviews were removed per filtering rules:

- **Missing theorem statement, Algorithm 1, and table values in extracted text**: These are parser-stripped artifacts that exist in the original submission. Per rules, missing appendix/parser-stripped content is not a valid weakness.
- **No comparison to concurrent work (DPM-Solver-v3, UniPC, etc.)**: Per rules, I cannot assert the existence of missing related works or require comparisons to works I cannot verify.
- **GHVB derivation / truncation error concern**: The critic's speculation about truncation error interplay with β is not supported by concrete evidence in the paper and is addressed by the empirical convergence verification.
- **Error bars on FID plots**: Single-run FID evaluation without error bars is standard practice in the diffusion sampling literature. Per soft rules, moved to Nice-to-Haves rather than treated as a weakness.
- **Strength about "stability region diagnosis as principled causal explanation"**: This strength conflicts with the verified weakness that the mechanism is unvalidated. Per rules, when a strength and verified weakness disagree, the weakness wins. The analysis is presented as a hypothesis, not a validated causal explanation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide empirical evidence linking the stability-region mechanism to artifact onset — e.g., track the projection of the solution onto suspected eigenvectors during sampling and show that methods with larger stability regions keep these projections bounded while standard methods let them blow up.
2. Calibrate the magnitude score against human judgments or establish its validity as an artifact metric through controlled perceptual studies.
3. Include practical guidance for selecting β based on step count, model architecture, or empirical criteria (e.g., step size relative to the spectral radius of ∇ε̅).
4. Report error bars or confidence intervals for the magnitude score, which is a newly introduced ad-hoc metric and not yet standardized in the field.

## Score and Decision

The paper presents novel, empirically validated, and practical methods for reducing divergence artifacts in diffusion sampling. The GHVB construction is a genuine algorithmic contribution, and the experimental breadth across three model classes is commendable. However, the paper's central theoretical framing — that artifacts arise specifically from insufficient stability regions and that momentum helps *because* it expands these regions — is presented with more certainty than the evidence supports. The artifact metric is uncalibrated, and parameter selection guidance is absent. These gaps are addressable and do not invalidate the empirical contribution, but they prevent the paper from being a strong acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>