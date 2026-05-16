Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper derives the first rigorous generalization bounds for Kolmogorov–Arnold Networks (KANs), covering two settings: (i) activation functions expressed as linear combinations of basis functions, and (ii) activation functions lying in a low-rank Reproducing Kernel Hilbert Space (RKHS). The bounds extend spectral-norm-based MLP theory to the KAN architecture, handle unbounded Lipschitz loss functions (covering squared, Huber, pinball, and ramp losses), and include a novel low-rank analysis connected to LoRA-style fine-tuning. Numerical experiments on simulated and real data examine the correlation between a derived complexity measure and the excess loss.

## Strengths

- **First generalization bounds for KANs.** The paper explicitly notes (Section 1.1) the absence of prior work quantifying KAN complexity. Theorems 2 and 4 fill a genuine gap in the literature on this recently proposed architecture, and the mathematical derivation is sound — extending covering-number chaining arguments (Proposition 1) and Maurey's sparsification (Proposition 2) to the KAN structure in a non-trivial way.

- **Bounds that deprioritize combinatorial parameters in the basis-function case.** Theorem 1's covering-number bound depends on the $l_1$ norm of coefficient matrices and Lipschitz constants, with network widths and basis-function counts entering only through logarithmic factors. This is a meaningful extension of MLP bounds (Bartlett et al. 2017) to the more flexible KAN architecture, where activation functions themselves are parameterized.

- **Bounds without the bounded-loss assumption.** Theorem 2 (Assumption 4) removes the common bounded-loss requirement and covers a general class of Lipschitz loss functions (squared, Huber, pinball). The paper explicitly contrasts this with prior work (Section 1.2): "our results cover a wider range of loss functions... which are not required to be bounded."

- **Novel low-rank RKHS analysis with practical connections.** Theorem 3 provides generalization bounds when activation functions lie in a low-rank RKHS (Matérn kernel), with the bound scaling polynomially in ranks and Lipschitz constants. Remark 6 connects this to LoRA-style fine-tuning — a genuine bridge between theory and current practice that the paper notes is new even relative to MLP theory.

## Weaknesses

### Fatal
None.

### Major

- **Overstated claim about combinatorial-parameter independence for the low-rank bound.** On line 357, the paper states that the low-rank result "has no explicit dependence on combinatorial parameters." This is inaccurate. Theorem 3 (thm-main3) defines ξ = Σ_{i=1}^L d_i r_i ( ... )^{(d_{i-1}/ν) ∨ 1}, where d_i are layer widths appearing linearly in ξ, and d̃ = max_i d_i appears in the exponent (ν/d̃) of the sample-size term, affecting the convergence rate. The abstract and contributions section correctly limit the "no combinatorial parameters" claim to the basis-function case, but the body of the paper extends it to the low-rank case without qualification. This overstatement should be corrected.

### Minor

- **Empirical validation is weaker than claimed.** The paper asserts a "tight correlation" between the complexity measure and excess loss, but the experimental design has limitations that temper this conclusion:
  - **Normalization choice.** The complexity values are normalized so that "the maximum value of the complexity measure is equal to the last value of the excess loss." This post-hoc scaling forces the curves to coincide at one point, making the visual match partly an artifact. The paper points to an appendix section for more detail, but the basic approach raises questions about what the unnormalized relationship looks like.
  - **No measure of variability.** The experiments are reported for a single run per dataset (line 417: "We run 1000 epochs for each dataset"). No error bars, multiple random seeds, or sensitivity analysis are provided. A claim of correlation requires some statistical evidence.
  - **Limited architectural variation.** The experiments use one architecture per dataset and do not systematically vary width, depth, basis-function count, or Lipschitz constants to test whether the bound's functional form (e.g., dependence on ∏ ρ_j or Σ (B_i c_i)^{2/3}) is predictive across different network designs.

- **Cross-entropy loss Lipschitz condition not verified.** The theory (Assumption 4) requires the loss to be Lipschitz. Cross-entropy is Lipschitz only when predictions are bounded away from 0 and 1. The paper uses cross-entropy for classification tasks (iii, iv, MNIST, CIFAR-10) but does not discuss whether this condition holds in practice.

- **The complexity measure is computed from the trained instance, not the class.** The bound is a function of the function class M, but the experiments compute the complexity measure from the specific trained network (which depends on the final parameters). While this is a common simplification in empirical evaluations of generalization bounds, it weakens the advertised connection between the class-level theory and the instance-level experiments.

### Trivial

- The product of Lipschitz constants ∏ ρ_j appears in both the basis-function bound (Theorem 1) and the low-rank bound (Theorem 3). For deep networks this product can be exponentially large, potentially making the bounds vacuous. This is a known limitation shared with all composition-based bounds (including MLP bounds) and does not detract from the paper's specific contribution.

## Nice-to-Haves

- The paper references an appendix section (sec-add-discuss) comparing the KAN bound with the MLP bound from Bartlett et al. (2017). Including a concise summary of this comparison in the main text would help readers appreciate the key difference (e.g., $l_1$ norms of coefficient matrices versus spectral norms of weight matrices).
- A brief discussion of the computational cost of computing the complexity measure components (B_i, ρ_j, c_{ij}) would clarify whether it could serve as a practical regularizer during training.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"No comparison with MLP bounds"* (Harsh Critic): The paper explicitly states on line 250, "In Section \ref{sec-add-discuss}, we compare this bound with a corresponding bound for MLPs." This section exists in the original submission (stripped by the parser).
- *"Practical difficulty of tuning ε, τ, η, s, s'"* (Harsh Critic): These are standard probabilistic bound parameters (confidence levels and moment exponents), not practical tuning knobs. The paper's handling is standard for the literature.
- *"Empirical validation showing tight correlation with excess loss"* (Strength Finder): This claimed strength conflicts with the verified weaknesses about the experimental design (normalization concerns, lack of error bars, limited variation). The experiments are suggestive but do not convincingly establish the strength of the relationship as claimed.
- *"Limitations of the bound (exponential product of Lipschitz constants)"* framed as a specific weakness of this paper: This is a well-known limitation of all composition-based covering-number bounds (including MLPs) and does not uniquely weaken this paper's contribution.
- *"Computational cost not discussed"*: A nice-to-have at most.
- Various formatting/style nitpicks and demands for content in the (stripped) appendix.

## Novel Insights

The main novel insight emerging from the review process is that the theoretical derivation is sound and fills a clear gap, but the paper's messaging around the empirical validation needs recalibration. The experiments are better characterized as a proof-of-concept demonstration (showing that the complexity measure and excess loss evolve similarly during training) rather than as rigorous evidence of "tight correlation." The overstated claim about combinatorial-parameter independence for the low-rank case is the paper's most concrete weakness and should be fixed. Beyond the paper's own contributions, no external novel insight emerges from the reviews.

## Suggestions

1. **Correct the overstatement on line 357.** Acknowledge that the low-rank bound includes layer widths d_i linearly in ξ and through d̃ in the exponent. Qualify the claim: e.g., "the bound scales polynomially with the underlying ranks and Lipschitz constants, with layer widths entering only linearly and in the exponent of the sample-size term."
2. **Strengthen the empirical section.** Add at least 5–10 runs with different random seeds for a subset of datasets, report mean ± standard deviation, and show the unnormalized complexity measure (or justify the normalization more convincingly). Consider adding a scatter plot of complexity vs. excess loss at different training epochs with a reported correlation coefficient.
3. **Verify or discuss the Lipschitz condition for cross-entropy.** Add a brief comment on whether the softmax predictions remain bounded away from 0 and 1 during training, or note that this is an approximation.
4. **Move the MLP comparison to the main text** (or at least summarize the key difference) so readers can immediately see how the KAN bound's $l_1$-coefficient dependence contrasts with the spectral-norm dependence of MLP bounds.

## Score and Decision

The paper makes a solid theoretical contribution — it is the first to provide generalization bounds for KANs, the mathematical reasoning appears sound, and the handling of unbounded losses and the low-rank analysis are genuine improvements over existing MLP theory. The main weaknesses (overstated claim about the low-rank bound, limited empirical validation) are correctable and do not undermine the core theoretical results. The paper meets the bar for a theory paper with supplementary experiments.

**Score: 7.0**

**Decision: Accept**

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>