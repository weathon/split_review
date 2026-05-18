Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces a generative framework that independently manipulates feature predictivity (how reliably a feature predicts the label) and availability (how easily a feature can be extracted from inputs) to study shortcut learning. Through controlled synthetic experiments, the authors show that nonlinear models exhibit bias toward more-available features even when those features are less predictive, while linear models do not. The paper also presents an NTK-based theoretical analysis of a two-layer ReLU network and extends the findings to naturalistic datasets (Waterbirds, CelebA) with explicit background manipulations.

## Strengths

- **Systematic disentanglement of predictivity and availability**: The generative framework (Section 3) independently controls α_i (amplification) and η_i (nesting) for each feature, enabling clean isolation of availability effects from predictivity. This is a genuine advance over prior work (e.g., Pezeshki et al. 2021) that confounded the two.

- **Crisp empirical demonstration that nonlinear activations are necessary for shortcut bias**: Controlled experiments show linear models are unbiased while introducing a single hidden layer with ReLU/Tanh induces bias, and depth amplifies it (Figures 2, 3). The parametric heatmaps across availability ratios and predictivity levels provide a comprehensive picture.

- **Theoretical analysis of the ReLU kernel's availability bias**: Theorems 4 and 5 derive explicit expressions showing that linear networks have zero availability sensitivity while ReLU networks are biased toward more-available features, with the sign given by (a₁²μ₁² − a₂²μ₂²)(a₁ − a₂). This provides a formal account of how predictivity and availability trade off.

- **Extension to naturalistic datasets with practical manipulations**: ResNet18 experiments on Waterbirds and CelebA show that background spatial extent, color, and patch removal shift feature reliance (Figure 5C), bridging the synthetic framework to real-world shortcut learning.

- **Reproducible, well-specified procedure**: The synthetic data generation (Section 3) is fully parameterized (d=100, ρ_c=0.9, σ_sc=0.6, etc.), enabling direct replication and extension.

## Weaknesses

### Major

- **Missing nesting experimental results**. Section 4 states "We also conducted experiments manipulating a second factor we expected would affect availability … the relative nesting of representations" but no data, figure, or analysis is presented. Nesting η_i is defined in the generative framework (Section 3) as a core dimension of availability, yet the paper provides no empirical test of its effect. This is a significant gap in the paper's empirical support for the full availability framework. (If these results exist in the supplementary materials that were stripped by the parser, the main text needs to reference them explicitly.)

- **Bayes-optimal classifier for naturalistic data is unspecified**. Figures 5A and 5B claim models are "more sensitive to the non-core feature than expected by a Bayes-optimal classifier." For the synthetic experiments, the optimal classifier is LDA (line 84). However, for Waterbirds and CelebA, the paper never specifies what the optimal classifier is, how it is estimated, or whether it uses the empirical training-set statistics or known generative parameters. Without this specification, the central claim that "predictivity alone does not explain the model's behavior" on naturalistic data rests on an underspecified baseline. The availability-manipulation experiments in Figure 5C do not rely on this comparison and are cleaner evidence.

- **Theory-experiment gap limits the support the theoretical account provides for the paper's broader claims**. The NTK analysis (Section 5) requires: (a) a two-layer architecture, (b) the NTK approximation (infinite width, gradient flow), (c) a small-covariance asymptotic expansion, and (d) a quadratic approximation to the ReLU kernel's angular function h. The eigenfunctions and sensitivity results are derived for the *approximate* kernel, not the true ReLU kernel. The paper uses "inevitability" language in the introduction ("shortcut bias is an inevitable consequence of nonlinear architectures," line 42) but the analysis applies only to a highly specific, approximate kernel under restrictive assumptions, and is never quantitatively compared to the empirical measurements. The paper would benefit from either (i) a quantitative consistency check (e.g., does the theory predict the sign of bias for specific α_s/α_c and ρ_s values used in Figure 1?) or (ii) explicitly scoping the theoretical claims to the approximate setting.

### Minor

- **Range claim for the reliance metric is inconsistent with the formula**. The paper states (line 96) that both reliance and shortcut bias are in [−1, +1]. However, for the Cartesian probe grid with independent z_s and z_c, a model that perfectly predicts sign(z_s) gives |Σ ŷ_i sign(z_s_i)| = n and |Σ ŷ_i sign(z_c_i)| = 0, yielding reliance = 2. The metric could thus range outside [−1, 1] depending on the probe grid and model behavior. This does not invalidate the qualitative results (comparisons across conditions remain valid) but the range claim needs correction or clarification.

- **The "inevitability" claim in the introduction overstates what the theoretical analysis establishes**. The conclusion (line 353) more carefully scopes the claim to "a single-hidden-layer nonlinear (ReLU) MLP," but the introduction (line 42) says "shortcut bias is an inevitable consequence of nonlinear architectures" without qualification. Given the approximations required, the analysis is better described as a *demonstration of a mechanism* than a proof of inevitability across all nonlinear architectures.

- **Depth trend is not addressed by the theory**. The abstract groups the depth finding ("model depth amplifies bias") with the theoretical account ("Our empirical findings are consistent with a theoretical account based on Neural Tangent Kernels"), but the theory only analyzes a two-layer network. The depth result is an interesting empirical finding but the NTK analysis provides no mechanism for it, nor does it predict the depth trend. The claim of "consistency" should be scoped to the nonlinear-vs-linear finding only.

- **Probe distribution differs from training distribution**. The evaluation probes uniformly cover the latent space on a grid in [−3μ_i, +3μ_i], while training data concentrates near ±μ_i. The probe-based reliance measure is internally consistent across conditions, but models are evaluated on points far from the training data where behavior may be driven by extrapolation properties. A brief acknowledgment of this would strengthen the paper.

### Trivial

- The paper has no limitations section; explicitly acknowledging the approximations in the theory, the restricted architecture class, and the probe distribution mismatch would improve the presentation.

## Nice-to-Haves

- A quantitative consistency check connecting the theoretical predictions to the empirical heatmaps (e.g., does the theory predict the sign of bias for the specific parameters used in Figure 1?). Even overlaying the predicted sign boundary from Theorem 5 onto the empirical data would substantially tighten the narrative.
- The naturalistic experiments (Figures 5A, 5B) could be more explicitly framed as testing predictions derived from the synthetic framework (e.g., "the synthetic framework predicts that reducing spatial footprint reduces bias; we confirm this in Waterbirds").
- A more substantive comparison with Pezeshki et al.'s "strength" notion — do the gradient-based mechanisms predict the same patterns, and are they compatible or competing?

## Removed Points

- **Availability circularity (Harsh Critic Point 3)**: The critic argues that availability in naturalistic data is inferred circularly. However, the paper's approach is standard scientific practice: define a construct operationally in a controlled setting (synthetic data), formulate hypotheses about its naturalistic manifestations, then test those hypotheses through explicit manipulations (Figure 5C). There is no circularity — the reasoning structure is transparent. Removed as factually incorrect.

- **Criticism about "availability" being a catch-all concept**: The paper explicitly defines availability as *a family of factors* (amplification, nesting, and their naturalistic analogues) and tests specific instances. This is a feature, not a bug — it invites operationalization of new factors. Removed as a misunderstanding of the paper's framework.

- **Suggestion that the paper "should also cover Y / domain Z"**: Not a substantive weakness of the existing contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the theory-experiment gap and the missing nesting results as the two main issues, but do not identify patterns or connections the paper itself missed.

## Suggestions

1. **Add the missing nesting results or remove the claim.** If the nesting experiments exist (even preliminary), include them. If they were not conducted, remove the sentence claiming they were.
2. **Specify the Bayes-optimal classifier for Waterbirds and CelebA.** Describe what the optimal classifier is, how it is estimated, and whether it uses empirical training statistics or known generative parameters.
3. **Temper the "inevitability" language in the introduction** to match the actual scope of the theoretical analysis (two-layer ReLU networks under an approximate kernel), consistent with the more careful phrasing in the conclusion.
4. **Clarify the reliance metric range** — either correct the claimed [−1, +1] range or explain the normalization that keeps it within this bound.
5. **Add a limitations section** discussing the theoretical approximations, the restricted architecture class, and the probe distribution mismatch.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>