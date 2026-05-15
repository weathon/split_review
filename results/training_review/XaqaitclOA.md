Now I have a thorough understanding of the paper and all the reviewer claims. Let me construct the final consolidated review.

---

## Summary

This paper studies Physics-Informed Neural Networks (PINNs) solving inviscid Burgers' equation under conditions that admit finite-time blow-up. It derives two theoretical bounds on the L² error between a neural surrogate and the true solution: Theorem 1 (arbitrary dimensions) and Theorem 2 (1+1 dimensions, with explicit boundary tracking). It then empirically evaluates these bounds on 1D and 2D Burgers' blow-up solutions, reporting correlation between the bound value and the true error across a sequence of PDE domains approaching the singularity.

## Strengths

- **Addresses an important and underexplored problem.** Understanding how PINNs behave near PDE singularities is relevant to both the PINN community and numerical analysis. The paper's focus on finite-time blow-up—a genuine phenomenon in fluids and combustion models—is well-motivated.

- **Derives mathematically valid inequalities for a zero-viscosity blow-up setting.** Prior theoretical PINN bounds (e.g., de&ndash;2022 error, Siddhartha et al.&ndash;2022) assumed viscosity, periodicity, or divergencelessness. The paper relaxes these restrictions, making the bounds applicable to known analytic blow-up solutions. This is a nontrivial extension.

- **Novel experimental design: fixing the network and varying the PDE domain.** Instead of varying network width or data size while holding the problem fixed (the standard practice in generalization-bound experiments, as the paper notes on lines 182&ndash;184), the authors fix the architecture and progressively shrink the time domain toward the blow-up. This directly tests the bounds' behavior at the difficult edge of singularity.

- **Clear visual evidence that PINNs can approximate blow-up solutions qualitatively.** Figure 1 shows that 6-layer, width-300 PINNs produce solutions that visually resemble the true solution even at δ = 0.998 (extremely close to blow-up at δ = 1). This empirical observation is the paper's most concrete and least contested contribution.

- **Transparency about limitations of the bounds.** The paper explicitly notes (lines 123&ndash;125) that Theorem 1's bound is "not like usual generalization bounds" because it depends on norms of the true solution, and it acknowledges (line 61, footnote) that the bounds are vacuous. This candor is commendable even if the abstract's framing is more ambitious.

## Weaknesses

### Major

1. **The bounds require knowledge of the true solution, which limits their practical value as generalization bounds.** Theorem 1's constants C₁ and C₂ depend on ‖∇u‖_{L^∞} and ∫‖u‖²; Theorem 2's constants depend on ‖u_x‖_{L^∞} = 1/(1−δ) and boundary norms of u. These quantities are not computable from training data alone when the true solution is unknown—which is the typical scenario. The paper acknowledges this (lines 123&ndash;125), but the abstract and introduction present "generalization bounds" without this caveat, creating a mismatch between framing and substance. A bound that requires the true solution to evaluate cannot serve its advertised purpose of predicting generalization error.

2. **The experimental correlation is confounded with the proximity parameter δ.** The experiments vary δ (closeness to blow-up) and report correlation between the bound and the true risk across δ values. Both quantities grow monotonically as δ → 1 because the true solution becomes more singular. A simpler predictor—such as 1/(1−δ) itself—would likely also correlate with the risk. The paper provides no control experiment (e.g., fixing δ and varying network architecture, initialization, or collocation points) to demonstrate that the bound captures anything beyond this trivial monotonic growth. Without such controls, the claimed "nontrivial insights" from the correlation are not substantiated.

3. **The 2D bound shows poor correlation for narrow networks, undercutting the generality of the claims.** For width-30 networks in 2D, the paper reports that "the correlation stays around 0.50 and only until δ = 0.307, and beyond that it decreases rapidly" (line 314). No explanation is offered for this failure. The paper's main claim is that the bounds "retain non-trivial insights" near blow-up, but this result suggests the bound is unreliable for narrower architectures—yet narrower architectures are computationally cheaper and more relevant in practice.

### Minor

1. **No confidence intervals or standard errors reported for correlation coefficients.** The 1D correlation is described as "∼1" and the 2D width-100 correlation as "∼0.80", but no numerical correlation statistic, confidence interval, or significance test is given. Given only six random seeds per configuration, the uncertainty is non-negligible.

2. **The "stability" claim for Theorem 2 is stated without qualification about constant blow-up.** For any fixed δ, the bound shows that small residuals imply small error—this is correct. However, the stability constant C = 1 + 2/(1−δ) diverges as δ → 1. The paper does not discuss this degradation or clarify that stability is not uniform across the family of PDE domains. This nuance matters for the claimed relationship to Wang et al.&ndash;2022.

3. **The computation of ‖∇u‖_{L^∞} in the 2D bound (lines 288&ndash;290) evaluates the temporal supremum at only two time points without justification.** While the spatial derivatives of the true solution depend only on t, the maximum of a continuous function on a closed interval can occur at interior critical points. The simplification is likely correct for the specific solution but is not justified.

### Trivial

- The 2D constants in lines 289&ndash;295 are given with messy expressions that are hard to parse. A cleaner presentation would help readers verify the derivation.
- The paper refers to figures by LaTeX labels (e.g., `\twofigref`) in the plain-text version, making the extracted text difficult to follow.

## Nice-to-Haves

- **Control experiments with fixed δ.** Varying network width or training-set size at a fixed δ would demonstrate that the bound tracks generalization error meaningfully beyond trivial co-growth.
- **Component-wise ablation.** Showing which terms in the bound (residual norms vs. solution norms) drive the correlation would clarify whether the bound provides insight beyond the growth of ‖u_θ‖.
- **Comparison against a trivial baseline predictor** (e.g., 1/(1−δ) or the norm of the true solution itself) to establish that the bound adds value.
- **Discussion of why the 2D width-30 bound fails beyond δ = 0.307.** Analyzing this failure could yield insights about the bound's structure or about PINN training near blow-up.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"The bound in Theorem 2 is also 'stable' in the sense of Wang et al. (2022) - this is false because the constant C diverges as δ→1."* — **Removed (misunderstanding).** The stability definition reproduced in the paper (footnote, line 170) concerns a fixed PDE problem (fixed δ). For any fixed δ, C is finite, so small residuals imply small error. The constant's blow-up across different δ values is a separate issue that the paper does not claim to avoid. The stability claim per se is technically correct.

2. *"The 2D bound's constants are 'suspiciously' reduced to two time points."* — **Weakened to minor.** The simplification is plausible for the specific solution (spatial derivatives depend only on t) but lacks explicit justification. It is not a fabrication.

3. *"Theorem 1 does not include boundary-condition residuals."* — **Already addressed by the paper.** The paper states (line 127) that Theorem 1 "only sees the errors at the initial time and in the space-time bulk" and explicitly motivates Theorem 2 as adding boundary tracking in 1D. This is a design choice, not an oversight.

4. *"Bounds blow up as δ→1, making them uninformative exactly where they are needed."* — **Partially addressed.** The bounds' divergence as δ→1 mirrors the divergence of the true solution and is a natural consequence of the problem, not an artifact. The paper's experiments show correlation even very close to blow-up (δ = 0.998), so the blow-up of the bound value does not prevent correlation. This is noted but not fully discussed.

5. Various generic criticisms about missing statistical rigor that are standard for single-trial PDE experiments (confidence intervals on every quantity). These are moved to Minor/Nice-to-Have as appropriate.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: that the *form* of the bounds (inequalities that mix residual norms with solution norms) makes them structurally different from standard PAC-style generalization bounds. The paper's candid admission that its bounds require knowledge of the true solution (lines 123&ndash;125) implicitly raises an interesting question for the PINN theory community: what is the right notion of a "generalization bound" for PDE solvers when the PDE and boundary data provide more information than a typical supervised learning problem? The paper does not articulate this question explicitly, but the tension between its framing ("generalization bounds") and its technical content ("bounds that exploit the known PDE structure") points toward an underexplored design space. The reviews do not yield novel insights beyond this observation.

## Suggestions

1. **Reframe the contribution.** The strongest and least contested result is the empirical demonstration that PINNs can approximate blow-up solutions. The paper's title, abstract, and introduction should lead with this finding and present the bounds as a supporting theoretical framework—not the reverse. Acknowledge upfront that the bounds are not standard generalization bounds but rather PDE-specific inequalities that require knowledge of the true solution's regularity.

2. **Add control experiments to decouple δ from the correlation.** Fix δ at, say, 0.5 or 0.9, and vary network width (30, 100, 300) or the number of collocation points. Show that the bound tracks the risk even when δ is fixed. This would directly address the confounding concern.

3. **Report numerical correlation coefficients with confidence intervals** (e.g., bootstrapped or based on the six seeds) for all experimental conditions, including the failure case (width 30, 2D).

4. **Analyze the width-30 2D failure.** This could be the most instructive part of the paper: why does the bound lose correlation for narrower networks? Is it because ‖∇u_θ‖_{L^∞} becomes a poor proxy, or because the network cannot capture the singularity well enough for the bound structure to be meaningful?

5. **Add a short discussion of why the bound constants blow up and whether this is necessary or an artifact of the proof.** Clarify the distinction between stability for a fixed problem and non-uniformity across a family of problems.

## Score and Decision

**Originality:** The problem selection is novel—studying PINNs near blow-up is genuinely underexplored. The theoretical extension to zero-viscosity Burgers' with non-trivial boundary conditions is a meaningful step beyond prior work.

**Importance of research question:** High. Understanding PINN behavior near singularities has practical implications for fluid dynamics, combustion, and any PDE application where solutions can blow up.

**Claims vs. support:** The paper's central claims—that it derives generalization bounds applicable to blow-up and that these bounds correlate with true error—are only partially supported. The bounds are mathematically valid but depend on the true solution, and the experimental correlation is confounded with δ.

**Soundness of experiments:** Weak. The single-axis variation (δ only), lack of controls, and missing statistical reporting make the experimental conclusions uncertain.

**Clarity of writing:** Generally clear at the conceptual level, though the extracted text suffers from formatting issues and the bound expressions are dense.

**Value to the community:** Moderate. The empirical observation that PINNs can approximate blow-up solutions is genuinely interesting and may inspire further work. The theoretical inequalities are a first step, but in their current form they are unlikely to be used by practitioners.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>