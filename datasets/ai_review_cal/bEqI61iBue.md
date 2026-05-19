- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6
Now I have a thorough understanding of the paper and both reviews. Let me construct the final consolidated review.

## Summary

HiZOO proposes incorporating diagonal Hessian information as a preconditioner into zeroth-order optimization for LLM fine-tuning. By adding one extra forward pass per step (3 total vs. MeZO's 2), the method estimates the diagonal Hessian via a Taylor expansion and uses it to scale updates according to per-parameter curvature. The paper provides a convergence theorem (for the idealized case with known Σ_t) and extensive experiments across RoBERTa-large, OPT-13B/30B/66B, Phi-2, and Llama3-8B, claiming consistent accuracy improvements and convergence speedups over MeZO.

## Strengths

- **First integration of diagonal Hessian into ZOO for LLM fine-tuning**: The paper correctly identifies that heterogeneous curvatures across parameters hurt plain ZO-SGD (MeZO), and proposes a principled fix via Hessian-informed preconditioning. This is a clear, non-obvious extension that preserves ZOO's memory advantage (O(d) Hessian storage).

- **Consistent empirical gains across a wide range of model scales and tasks**: The paper reports improvements over MeZO on RoBERTa-large (3.5% average), OPT-66B (up to 5.1%), and F1 optimization (6.36% average), covering classification, multiple-choice, generation, and non-differentiable objectives. Testing spans models from 350M to 66B parameters.

- **Memory advantage preserved**: The diagonal Hessian adds only O(d) memory, and the HiZOO-L variant keeps overhead under 10% of MeZO's memory, enabling fine-tuning of models 10× larger than full fine-tuning on the same hardware.

- **Visualization on test functions**: Figure 2 provides an intuitive demonstration of how the Hessian preconditioner handles heterogeneous curvature, showing clear convergence advantages over MeZO on synthetic functions with imbalanced curvature.

- **Ablation on EMA smoothing**: Figure 5 systematically evaluates sensitivity to α_t, demonstrating robustness across a reasonable range.

## Weaknesses

### Fatal
None.

### Major

- **Algorithm pseudocode is ambiguous and inconsistent with the mathematical derivation**: Algorithm 1 mixes scalar and vector notation in ways that prevent faithful implementation from the pseudocode alone. Specifically: (i) Line 103 uses `u_i` (a scalar sampled per-parameter in the PerturbParameter loop) in a matrix formula `(Σ^{-1/2}_{t-1} u_i u_i^⊤ Σ^{-1/2}_{t-1})` that requires vector `u_i`; (ii) Line 106 computes `projected_grad ← (ℓ_+ − ℓ_−) ∗ Σ^{1/2}_t / 2μ`, where `Σ^{1/2}_t` is a d×d diagonal matrix — this produces a vector (or matrix), yet the same variable is used as a scalar multiplier inside the per-parameter loop on line 112; (iii) The inner loop on lines 110-113 samples fresh `u_i ∼ N(0, I_d)` per parameter, but `I_d` implies a d-dimensional vector being assigned to a scalar `θ_i`. The mathematical derivation in Section 3.2 (Eqs. 3-4) correctly uses vector perturbations, but the pseudocode is inconsistent with it. This makes the method harder to reproduce from the paper alone. The core idea remains clear from the math, but the pseudocode needs a precise rewrite.

### Minor

- **Convergence theorem treats Σ_t as known and fixed, not as estimated**: Theorem 1 analyzes a generic preconditioned ZO-SGD step assuming Σ_t is given per step. It does not account for the coupling between Hessian estimation and gradient estimation, the noise from the Taylor truncation error (O(μ³)), the EMA smoothing, or the fact that the Hessian estimate shares random perturbations with the gradient estimate. This is a common idealization in optimization papers, but it means the theory provides no convergence guarantee specific to HiZOO's core novelty. The paper separately proves unbiasedness of the diagonal Hessian estimator (up to O(μ)), but never combines the two analyses.

- **"8× speedup" claim is ambiguously stated**: The abstract and introduction state "8× speedup" without specifying whether this refers to training steps or total forward passes. Since HiZOO uses 3 forward passes per step vs. MeZO's 2, a step reduction of 8× corresponds to a forward-pass reduction of (3×1/8)/(2×1) = 0.1875× (roughly 5.3×, still substantial). Section 5.4 partially clarifies that "HiZOO reduces total number of forward passes required for convergence," but the headline claims in the abstract and introduction are imprecise. The convergence criterion used to measure "speedup" is also not defined.

- **Section 4 ("Convergence Analysis") is a near-verbatim duplicate of Section 3.4**: The theorem statement, equations, and surrounding text in Section 4 (lines 362-414) are essentially identical to Section 3.4 (lines 292-332). Both have an empty proof environment. The commented-out proof block (lines 416-545) is present only once. This duplication suggests hasty preparation or a formatting error.

- **Taking absolute values of the diagonal Hessian estimate is not discussed**: The EMA update (Eq. 9) uses `|diag(Σ'_t)|` to enforce non-negativity, which breaks the unbiasedness of the Hessian estimator (the raw `diag(Σ'_t)` can be negative). The paper states this choice (line 290) but does not analyze its effect on the estimator's properties or convergence.

### Trivial
None.

## Nice-to-Haves

- A comparison with Sophia (diagonal Hessian in the first-order setting) would help contextualize the trade-offs: HiZOO avoids backprop memory but adds a forward pass; Sophia needs backprop but saves memory on the Hessian side. This is outside the paper's stated scope but would strengthen positioning.
- An ablation on the perturbation scale μ for the Hessian estimate (sensitivity of the Hessian bias O(μ) to model scale) would be informative.
- Clarifying whether a hyperparameter search was conducted for MeZO on each task to ensure fair comparison.

## Removed Points

These points from the input reviews were removed after cross-checking against the paper; treat them with caution:

- **"Missing related works (AdaZOO, ZO-SPSA with adaptive steps)"** — Removed per instructions: do not mention missing related works without external confirmation.
- **"Missing experimental details (learning rate, batch size, µ values, etc.)"** — Removed as a reproducibility nitpick; these details are typically expected in supplementary material.
- **"Empty proof blocks / missing proofs"** — Removed per instructions; the parser strips supplementary content, and commented-out proofs exist in the source.
- **"The step where they drop the −Σ^{-1} term is not explained"** — Removed as factually incorrect: Eq. (8) (lines 259-266) includes the full expression `(Σ^{-1/2}_t u_i u^⊤_i Σ^{-1/2}_t − Σ^{-1})`. The critic appears to have misread the equation.
- **"MeZO's hyperparameters might be suboptimal"** — Removed as speculative; there is no evidence in the provided text that MeZO was undertuned.
- **"Fatal / structural flaws" characterization** — Removed after verification: none of the identified issues individually or collectively invalidate the paper's core contribution. The algorithm is recoverable from the mathematical derivation, the theory limitation is common, and the speedup claims are partially addressed.
- **Strength finder's generic praise** (e.g., "addressed an important problem") — Removed as superficial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Rewrite Algorithm 1 to use consistent vector notation: draw a single perturbation vector **u** per step (not per-parameter scalars), compute the gradient estimate as a vector operation matching Eq. (4), and clearly distinguish matrix vs. element-wise operations.
2. In the convergence theory, add a remark acknowledging that the analysis assumes known Σ_t, and provide a brief discussion of how the Hessian estimation error (bias O(μ), variance from n=1) would propagate into the bound.
3. Qualify all "speedup" claims by stating both the step reduction and the estimated forward-pass reduction. Define the convergence threshold used.
4. Remove the duplicate Section 4.
5. Discuss the effect of the absolute-value operation in the EMA update (Eq. 9) on estimator bias, even if only qualitatively.
