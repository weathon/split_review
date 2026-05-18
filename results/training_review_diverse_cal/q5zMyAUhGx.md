Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper provides the first rigorous generalization bounds for Kolmogorov–Arnold Networks (KANs), covering two settings: activation functions as linear combinations of basis functions (Theorems 3.2/3.2') and activation functions lying in a low-rank RKHS (Theorems 3.3/3.4). The bounds are derived via covering numbers and Maurey's sparsification lemma, avoid dependence on combinatorial parameters, apply to unbounded losses, and are accompanied by numerical experiments showing correlation between a normalized complexity measure and excess loss on simulated and real data.

## Strengths

1. **First rigorous generalization bounds for KANs.** The paper establishes the first theoretical guarantees for KANs, an architecture of growing interest. Theorem 3.2 covers basis-function representations (B-splines, wavelets, Fourier series, etc.), and Theorem 3.3 covers the low-rank RKHS setting, with no comparable prior results for KANs (the paper notes this gap in the introduction).

2. **Bounds avoid dependence on combinatorial parameters and accommodate unbounded losses.** The bound in Theorem 3.2 scales with the l₁ norm of coefficient matrices and layer-wise Lipschitz constants, with node/basis counts appearing only inside a logarithmic factor. Unlike the MLP bounds of Bartlett et al. (2017), it applies to unbounded regression-type losses (e.g., squared error) via a truncation argument (Assumption 3.4). These differences from prior MLP results are explicitly stated in the main text (lines 91–92).

3. **Novel low-rank RKHS analysis with fine-tuning interpretation.** Theorem 3.3 provides generalization bounds for KANs whose activation functions lie in a low-rank RKHS (e.g., Matérn kernel), scaling polynomially with ranks and Lipschitz constants. Remark 3.1 connects this to a fine-tuning framework analogous to LoRA, which the paper notes appears to be new and without comparable MLP results.

4. **Flexible operator norms per layer.** Proposition 2.1 generalizes covering-number arguments from MLPs (Anthony & Bartlett, Bartlett et al.) to different operator norms at each layer, a useful architectural flexibility.

## Weaknesses

### Fatal
None.

### Major

1. **Empirical validation only demonstrates correlation with a rescaled proxy, not the actual bound.** The paper normalizes the complexity measure so that its maximum matches the final excess loss value (line 417). This means the experiment shows that *some linear function* of ᾶ tracks excess loss, but it does not test whether the bound's *specific numerical values, constants, and rates* (e.g., the 1/n and log terms in Theorem 3.2) are informative or tight. The actual values of the bound's components — Bᵢ, ρᵢ, cᵢ — are not tracked or reported. While the shape correlation is suggestive, the claim of "practical relevance of these bounds" (abstract, line 7) is overstated relative to what the experiments actually validate. The experiments are consistent with the theory but do not confirm the bound's numerical magnitude.

2. **Low-rank RKHS bounds (Theorem 3.3) receive no empirical support.** The abstract and contributions list both settings as main results, yet the numerical experiments exclusively use the basis-function representation. No experiment — not even a synthetic one — is provided to examine whether the low-rank structure holds in practice or whether the polynomial rates are plausible. This leaves a stated main contribution entirely unexamined empirically.

### Minor

1. **Bound constants are estimated post-hoc from trained networks, with no discussion of typical magnitudes.** The Lipschitz constants ρⱼ and coefficient norms Bᵢ are estimated from the trained network after the fact (line 401). The paper does not discuss how large these constants typically are for KANs on real data, whether they remain manageable as depth grows, or how to choose the caps a priori. This limits the practical guidance the bounds provide, even though the bounds remain valid as uniform guarantees over the defined function class.

2. **Choice of parameter v in the covering number bound (Proposition 2.2) is left unspecified.** The Proposition admits any v in (0,2] for the mixed norm ‖𝐆(X)‖_{v,s}, and the main theorem uses r=1 (so s=∞). The resulting bound depends on this choice, but no specific v is justified or discussed in the main theorem development. The constants in ᾶ implicitly assume a particular v (likely v=2), but this is not made explicit.

3. **Experiments only use B-spline-based KANs despite theoretical breadth.** The paper lists many basis families (wavelets, Fourier, RBF, Jacobi, polynomials) and claims the theory covers them, but only B-spline activations (following Liu et al. 2024) are tested. Varying the basis type would strengthen the claim of practical relevance across the settings the theory addresses.

### Trivial
None.

## Nice-to-Haves

- Validate the bound as a numerical guarantee, not just a correlation: report actual values of ᾶ, the bound RHS, and the excess loss at multiple checkpoints, without rescaling.
- Track the components of ᾶ (l₁ norms, Lipschitz constants, product terms) over training to reveal which factors drive bound growth.
- Provide a synthetic experiment for the low-rank RKHS case (e.g., activations constrained to a low-dimensional subspace of a Matérn RKHS), even if simple.
- Discuss how the rate in Theorem 3.2 compares to known minimax rates for composition models.
- Test at least one alternative basis function (e.g., Fourier or wavelets) to broaden the empirical scope.

## Removed Points

These points were raised but are excluded from the main weaknesses per the review guidelines:

- **"The bound's dependence on constants is potentially circular"** — Removed because this misunderstands how uniform bounds work. The bound is a standard worst-case guarantee over a function class defined by caps on Bᵢ, ρᵢ, etc. Computing it post-hoc from trained parameters is standard practice (e.g., Bartlett et al. 2017 does the same with spectral norms). The valid kernel of this concern (constants not discussed) is kept as a Minor weakness.

- **"The main body defers the MLP comparison to the appendix"** — Removed because (a) the paper already summarizes the key differences in the main text (lines 91–92: three enumerated points), and (b) the detailed comparison is in an appendix section (sec-add-discuss) that was stripped by the parser. Per guidelines, missing appendix content is not a valid criticism.

- **"Missing discussion of the bound's rate relative to minimax rates"** — This is a reasonable discussion point but not a weakness of what the paper does present; moved to Nice-to-Haves.

- **Requests for more basis types in experiments** — Scope creep for a theory paper whose primary contribution is not empirical. Kept as Minor (the overclaim of "practical relevance" across basis types is the real issue, already captured in Major weakness 1).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the theory's scope and the empirical validation's strength, but this is a standard observation about theory-plus-empirics papers rather than a novel insight.

## Suggestions

1. Reframe the abstract and conclusion to distinguish more carefully between "the bounds are theoretically derived and empirically plausible" versus "the bounds are validated as numerical guarantees." Acknowledge that the experiments show a correlation between the complexity measure and excess loss in shape but do not test the bound's numerical tightness.

2. Track and report the raw values of Bᵢ, ρᵢ, cᵢ, and the un-normalized ᾶ at several training checkpoints. Even a table in the appendix would give readers a sense of their scale and evolution.

3. Add a brief explanation in the main text of how the parameter v in Proposition 2.2 is chosen and how it affects the bound.

4. Either provide a synthetic experiment for the low-rank RKHS case (e.g., activations constrained to a rank-limited subspace of a Matérn RKHS) or explicitly state in the abstract/introduction that the low-rank bounds are purely theoretical contributions without empirical validation.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>