Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper proposes a Generalized Exact Path Kernel (gEPK) that decomposes a neural network's predictions into contributions from each training point and training step via inner products of parameter gradients (Theorem 3.1). Building on this representation, the paper shows (Theorem 4.1) that the set of per-training-point parameter gradients spans the subspace of test gradients that contribute to learned adjustments, and qualitatively connects several gradient-based OOD detection methods (GradNorm, ReAct/DICE/ASH/VRA, GradOrth) to this spanning set. The paper further proposes using the matrix of training-point input gradients to measure signal manifold dimension around test points.

## Strengths

1. **Extended EPK representation without restrictive assumptions**: Theorem 3.1 generalizes the Exact Path Kernel (Bell et al., 2023) by dropping the symmetry requirement that made the original a true kernel, thereby avoiding a discontinuity in input space while still decomposing predictions per training point and step. The representation is exact (not asymptotic) and applies to any differentiable parametric model trained with gradient descent.

2. **Conceptual unification of gradient-based OOD methods under a common spanning set**: Theorem 4.1 establishes that the set \(B = \{\varphi_{s,0}(x_i)\}\) spans the subspace of test parameter gradients relevant to learned predictions. Section 4.1 then reinterprets GradNorm, ASH/ReAct/DICE/VRA, and GradOrth as projections onto subsets of this basis. While qualitative, this provides the first theoretical bridge between these methods and helps explain the otherwise puzzling observation (raised by Igoe et al., 2022) that parameter gradients work well for OOD detection.

3. **Novel approach to measuring signal manifold dimension via training input gradients**: The paper proposes computing the SVD of the matrix \(G\) of training-point input gradients \(\nabla_{x_{\text{train}}} f(x_{\text{test}}; \theta_{\text{trained}})\) and using its explained-variance profile to estimate the intrinsic dimension of the signal manifold. The experiments (Figure 1) show that on MNIST only 94/784 dimensions explain 95% of variation, on CIFAR 1064/3096, and on a toy problem 2–3 — consistent with known properties of these datasets.

4. **Empirical evidence that training concentrates the gradient subspace**: Figures 5 and 3 show that the parameter gradient and input gradient subspaces become lower-dimensional after training compared to initialization, and that different random initializations converge to similar input gradient subspaces (Figure 4). These observations connect the theoretical framework to practical phenomena like adversarial transferability.

## Weaknesses

### Fatal
None. While the paper has significant issues, none invalidate its entire contribution.

### Major

1. **Flawed derivation in Section 5 connecting the gEPK to the input-gradient matrix**: The derivation in Equations 24–25 attempts to differentiate the gEPK expansion w.r.t. test input coordinate \(x_j\) and then claims "these gradients will be zero except when \(i=j\)" (line 187). This statement is mathematically confused: \(i\) indexes training points and \(j\) indexes input coordinates — they are different index sets, so "\(i=j\)" is not a meaningful condition. Moreover, the derivative \(\frac{d}{dx_j}\) of the gEPK sum should involve \(\frac{d\varphi_{s,t}(x)}{dx_j}\) for *all* training points \(i\), since \(\varphi_{s,t}(x)\) depends on the test input regardless of which training point is being summed. The paper's attempt to reduce the expression to a sparse matrix indexed by a single input dimension is not justified. **However** — crucially — the actual quantity the experiments measure (the matrix of training input gradients \(\nabla_{x_{\text{train}}} f(x_{\text{test}}; \theta_{\text{trained}})\)) is well-defined and computed directly from the trained model, not through the gEPK derivation. The experiments in Figures 1, 4, and 5 are therefore not invalidated by this derivation error. *But the theoretical justification that the rank of \(G\) corresponds to signal manifold dimension via the gEPK is unsupported as written.* This derivation needs to be corrected or removed; as it stands, it undermines confidence in the dimension estimation contribution.

2. **OOD methods unification is qualitative, not formally proven**: Section 4.1 describes how each method relates to the gEPK basis, but the connections are suggestive rather than rigorous. For instance, the claim that ASH truncation corresponds to "projection onto the parameter tangent space of the training data with the highest variation" is intuitive but never made precise. The paper states it "explains" these methods, but does not prove formal equivalence or derive the methods' score functions as special cases of the gEPK under specific assumptions. For a paper whose stated contribution includes providing "theoretical justifications" for OOD methods, this gap is significant.

3. **Experimental validation is insufficient for the paper's applied claims**: The OOD detection experiment (Figure 2) reports only a histogram without standard quantitative metrics (AUROC, FPR@95), uses only one dataset pair (MNIST vs. Fashion-MNIST), and includes no comparison to existing OOD methods. The paper explicitly states "the purpose of this paper is not to develop state of the art OOD detection methods" (Figure 2 caption), which is fair, but the claim of *explaining* why gradient methods work would be much stronger with even a simple quantitative demonstration that the gEPK-based score matches or correlates with an existing method's performance across multiple benchmarks. Similarly, the dimension estimation results (Figure 1) are not compared against standard intrinsic dimension estimators (MLE-based, graph-based), making it difficult to assess what the proposed measure adds.

### Minor

1. **Sign inconsistency between Theorem 3.1 and its proof**: The theorem statement (line 46) gives \(f(x;\theta_S) = f(x;\theta_0) + \sum \sum \varepsilon (\int \varphi) L' \varphi\) with a *positive* sign, while the proof (line 76) derives \(y_N = f(x;\theta_0) - \sum \sum \varepsilon (\int \varphi) \cdot L' \varphi\) with a *negative* sign (arising from gradient descent going against the gradient). This inconsistency can be fixed trivially (e.g., including the negative sign or redefining \(L'\) to absorb it), but its presence suggests carelessness in the theoretical core.

2. **Notation inconsistency and limited scope of the training assumption**: The proof uses \(N\) to denote both the number of training steps (line 76: \(\sum_{s=1}^N\)) and the number of training data points (line 76: \(\sum_{i=1}^N\)), while the theorem statement distinguishes \(S\) (steps) and \(N\) (data). The theorem assumes full-batch gradient descent with constant learning rate and scalar loss — the paper does not discuss how the representation extends to minibatch SGD, adaptive optimizers (Adam), or vector-valued outputs in multi-class settings (beyond a brief mention). These limitations are not unusual for a theoretical paper but should be acknowledged more explicitly.

3. **Computational feasibility is acknowledged but not analyzed**: The full gEPK requires storing gradients for every training step and point (\(O(S N M)\)). The paper mentions sketching and truncation in passing (line 159) but provides no analysis of approximation error. Given that the paper proposes a practical tool for OOD and dimension estimation, this gap limits the work's applicability.

### Trivial

- The equation in the GradOrth section (line 133–146) contains garbled/corrupted text (e.g., "spanaocf ttihvae"), which appears to be a PDF extraction artifact rather than an author error, but should be cleaned in the camera-ready version.
- The notation in Equation 25 uses \(G_j\) on the LHS while the RHS still depends on \(i\), which is confusing.

## Nice-to-Haves

- A concrete theorem showing that at least one existing OOD method (e.g., GradOrth, since it most explicitly constructs a reference basis) is exactly a special case of the gEPK projection under specific simplifying assumptions would substantially strengthen the unification claim.
- Standard quantitative OOD evaluation (AUROC) on CIFAR-10 vs. SVHN or TinyImageNet, comparing to at least GradNorm or GradOrth.
- An analysis of how well the gEPK-based dimension estimate correlates with standard intrinsic dimension estimators (e.g., MLE-based, TWO-NN) on controlled synthetic data where the true dimension is known.
- A discussion of how the gEPK extends (or fails to extend) to minibatch SGD — even a brief remark about continuous-time limits would improve the paper.

## Removed Points

These points were flagged but are removed or downgraded for the reasons given:

- **"The derivation error invalidates the experiments in Figures 1, 4, and 5"** (from harsh critic): Overstated. The experiments compute training input gradients directly from the trained model, which is a standard and valid operation. The gEPK derivation was an attempt at theoretical grounding but is not required for the experiments to be meaningful. The experiments stand independently.
- **"The matrix G as defined is not a valid measure of per-training-point input sensitivity"** (from harsh critic): Incorrect. The matrix \(G\) (training point input gradients) is a well-defined and standard sensitivity measure. The SVD of this matrix gives meaningful information about which input directions matter for the model's predictions.
- **"The paper does not cite relevant related work"** (implicit in critic's discussion): The rule states not to mention missing related works, as we cannot independently verify their existence.
- **Generic strengths from Strength Finder** (e.g., generic praise of the approach without specific evidence): Not present — all strengths listed by the Strength Finder are grounded in specific theorems/figures.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the reviews is that the paper's *qualitative* unification of OOD methods (Strengths) and its *flawed* derivation in Section 5 (Weakness) coexist in a revealing way: the gEPK framework genuinely provides a common language for describing what methods like GradNorm and GradOrth do, but the paper overreaches when trying to derive new quantities (like the input-gradient matrix \(G\)) from the path decomposition. The correct approach would be to simply define \(G\) as the matrix of training input gradients directly — a quantity that is independently useful for dimension estimation — and then note that the gEPK offers a *conceptual* lens for understanding why this matrix captures information about the training data's influence, rather than attempting a formal derivation that mixes indices. This suggests the paper's strongest contribution is the *interpretive framework* (unifying OOD methods via gradient subspaces), while the dimension estimation contribution is best presented as an independent empirical technique inspired by, but not reliant on, the gEPK formalism.

## Suggestions

1. **Fix or remove the flawed derivation in Section 5**: Either (a) re-derive correctly by differentiating \(\varphi_{s,t}(x)\) directly (which depends on all training points) and acknowledging that \(G\) is simply the matrix of training input gradients, defined without recourse to the path decomposition, or (b) present the dimension estimation results in a separate section that does not depend on the gEPK, simply noting the conceptual connection.

2. **Fix the sign inconsistency in Theorem 3.1**: Ensure the theorem statement matches the proof's negative sign, or explicitly state a convention (e.g., absorb the sign into \(L'\)).

3. **Make the OOD unification more precise for at least one method**: Even one concrete derivation showing that GradOrth (with specific simplifying assumptions) becomes a special case of the gEPK projection would significantly strengthen the paper's central thesis.

4. **Add standard quantitative metrics to the OOD experiment**: Report AUROC and FPR@95 on at least 2–3 OOD benchmark pairs (e.g., CIFAR-10 vs. SVHN, CIFAR-10 vs. TinyImageNet) with a simple baseline comparison.

5. **Acknowledge the full-batch GD limitation explicitly** and add a brief discussion (even speculative) of whether the representation extends to SGD via continuous-time approximations.

## Score and Decision

This paper introduces an interesting theoretical framework (gEPK) and provides a novel conceptual unification of gradient-based OOD detection methods. The core theoretical results (Theorems 3.1 and 4.1) are sound modulo a sign fix. However, the paper has three significant problems that prevent acceptance in its current form: (1) a mathematically flawed derivation in Section 5 that attempts to connect the gEPK to the input-gradient matrix, (2) a unification of OOD methods that is qualitative rather than formally established, and (3) experimental validation that is too weak to support the paper's applied claims. The paper needs at least one substantial revision cycle to correct the derivation error, make the OOD unification precise for at least one method, and provide more rigorous experiments.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>