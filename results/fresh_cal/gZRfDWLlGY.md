Now I have all the information I need. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper introduces a Generalized Exact Path Kernel (gEPK), extending the EPK from Bell et al. (2023) by removing the symmetry requirement and avoiding discontinuities. Using this decomposition, the paper attempts to connect model predictions to training input gradients and parameter gradients, offering a theoretical framing for gradient-based OOD detection methods. It also derives a method for estimating the signal manifold dimension around test points using training input gradient matrices.

## Strengths

- **Generalization of the Exact Path Kernel without symmetry requirement (Section 3).** The paper relaxes the symmetry condition of the original EPK, removing the discontinuity that EPK introduced. The trade-off is explicitly stated ("the EPK maintained symmetry at the cost of continuity, on the other hand the gEPK does not introduce a discontinuity"), and the resulting representation enables exact decomposition into both input gradients and parameter gradients. Theorem 3.1 and its proof are a genuine theoretical contribution.

- **Novel method for estimating signal manifold dimension around test points (Section 5).** The paper derives an expression for the gradient of the prediction with respect to each training input (Equations 27–29) and shows that the rank of the resulting matrix G can be used to measure the effective input dimension perceived by the model. The experimental results (Figures 1, 4, 5) quantify this for toy problems (~2–3), MNIST (~94), and CIFAR (~1064), demonstrating a practical measurement approach.

- **Cross-model comparison of feature reliance.** Figure 4 and the surrounding discussion show that two independently initialized models trained on the same data share many components of the signal manifold. This provides a novel measurement of how much models rely on the same features, with a potential connection to adversarial transferability.

- **OOD detection without test-point labels.** The paper notes (Section 4.2) that its gEPK-based approach compares test gradients against a pre-computed basis from training data, avoiding the need for ground-truth labels on test points — a practical advantage over methods like GradOrth that require labels.

## Weaknesses

### Fatal
None. The core theoretical framework (gEPK decomposition, Theorem 3.1) is not fundamentally invalidated by the issues below; however, they substantially undermine the paper's claimed contributions.

### Major

- **Logical error in the proof of Theorem 4.1 (Prediction Spanning Vectors).** The proof states: "Suppose for every s and t, φ_{s,t}(x) ∉ B. Then for every i, s, and t, ⟨φ_{s,t}(x), φ_{s,0}(x_i)⟩ = 0." This is a non-sequitur: a vector not belonging to a set B does not imply it is orthogonal to every element of B. The proof confuses "not in the set" with "orthogonal to the span." Since Theorem 4.1 is central to the paper's explanation of why gradient-based OOD methods work, this error undermines one of the paper's core theoretical claims. The theorem may be correct, but the provided proof is invalid as written. This is a basic linear algebra mistake in a paper whose primary contribution is theoretical.

- **The claimed unification of prior OOD methods is asserted, not derived (Section 4.1).** The paper promises to "establish that most gradient based methods for OOD... can be written as projections onto subsets of this span," but the actual text delivers only brief qualitative analogies. For GradNorm: "This looks like the left side of the inner product from the gEPK, however the scaling factor... does not match." For ASH/ReAct/DICE: "This is effectively a projection onto the parameter tangent space of the training data with the highest variation" — with no derivation of what "effectively" means formally. Only GradOrth receives a somewhat more detailed treatment, but even that stops short of showing its score is exactly a special case. Given that "expressing prior OOD methods with the gEPK" is billed as a central contribution, the absence of explicit algebraic correspondences is a significant gap. The paper's claim of providing "theoretical justifications which explain the surprising effectiveness of parameter gradients for OOD detection" is therefore not adequately supported.

### Minor

- **Experimental OOD evidence is insufficient to substantiate the claims.** The OOD detection experiment (Figure 2, left) is a single histogram of projection norms for MNIST vs. FMNIST with no quantitative metrics (AUROC, AUPR, FPR95), no comparison to any baseline, and no rejection thresholds. The paper acknowledges this ("As the purpose of this paper is not to develop state of the art OOD detection methods, a comparison with recent benchmarks is not provided"), but the paper also claims gEPK "can perform OOD detection" and that it "explains the success" of gradient methods. Without any standard evaluation, these claims rest entirely on the theoretical framing — yet the theory itself has gaps (Theorem 4.1 proof error, insufficiently rigorous unification). At minimum, a small quantitative evaluation (e.g., AUROC on CIFAR-10 vs. SVHN) using a practical approximation of the integral would demonstrate that the framework has empirical teeth.

- **Notational sloppiness in Theorem 3.1 and its proof.** The variable N is used for both the number of training data points and the number of training steps (Equation 16 uses Σ_{s=1}^{N} but the theorem statement defines S as the number of steps and N as the number of data points). Additionally, the derivation in Equation 15 (line 70–71) contains an extraneous "dt" at the end of the second line. While individually minor, these issues suggest a lack of careful proofreading that is problematic for a primarily theoretical paper.

- **The "signal manifold dimension" is not formally defined or connected to established notions.** Section 5 claims that "the rank of G represents the dimension of the subspace on which the model perceives a test point," but this is asserted without proof. There is no linking argument connecting the rank of G to any established definition of intrinsic dimension (e.g., local correlation dimension, MLE dimension). Without this, the dimension estimates (94 for MNIST, 1064 for CIFAR) are anecdotal rather than rigorous.

### Trivial

- The scaling argument in the gEPK representation for OOD (Section 4.2) mentions that truncating to only the final training step is "supported by the convergence of this scaling over training," but provides no formal statement or analysis of this convergence — just a single toy example (Figure 2, right).

## Nice-to-Haves

- Provide a corrected proof of Theorem 4.1 (or clarify the intended meaning). The correct statement is that the learned adjustment is a linear combination of inner products ⟨φ_{s,t}(x), φ_{s,0}(x_i)⟩, so if φ_{s,t}(x) is orthogonal to span(B), the contribution is zero.
- Include explicit algebraic derivations showing how at least one concrete OOD method (e.g., GradOrth) is a special case of the gEPK under well-specified approximations.
- Discuss practical approximations to the continuous integral over training paths (e.g., using only the final few steps, or noting when φ_{s,t}(x) is approximately constant).
- Add a limitations section acknowledging that the gEPK is currently intractable for large-scale models.
- Provide confidence intervals or error bars for the dimension estimation experiments.

## Removed Points

These points were removed from the main review for the reasons indicated:

- **"The paper claims to be first but ignores prior attempts (Igoe et al. 2022)"** — Removed because the paper describes Igoe et al. as raising *questions* about why gradients work, not providing theoretical justifications. The paper's claim is about being the first to *explain* the effectiveness, which is not contradicted by its own description of Igoe et al.'s work.
- **"Theorem 3.1 is too general / proof relies on standard assumptions"** — Removed. The conditions (full-batch GD, linear interpolation between steps) are clearly stated. The proof is a valid application of the fundamental theorem of calculus and chain rule for the stated setting.
- **"Missing related works"** — Removed per instructions (cannot verify external sources).
- **"Reproducibility concerns about undisclosed hyperparameters"** — Removed per instructions; the paper is primarily theoretical and the experiments are preliminary/proof-of-concept.
- **"Strength: Unified theoretical explanation for diverse gradient-based OOD methods"** — Removed because it conflicts with an verified weakness (the unification is asserted, not rigorously derived). The strength appears overstated relative to what Section 4.1 actually delivers.
- **"Strength: Proof that learned adjustments lie in the span of training parameter gradients"** — Weakened to a discussion rather than kept as a strength, because the proof of Theorem 4.1 is flawed (see Major weakness #1). The theorem's intent may be correct but it has not been properly established.
- **"DT at end of equation is a parser artifact"** — While this appears in the parsing, it is treated as part of the minor notational sloppiness rather than elevated as a separate issue.

## Novel Insights

The harsh critic's analysis correctly identifies a genuine logical error in the proof of Theorem 4.1 — the conflation of "not in a set" with "orthogonal to the set" — which is a basic linear algebra mistake. However, this error does not necessarily invalidate the theorem's intended claim; it means the proof needs to be rewritten. More interestingly, the tension between the critic and the strength finder on Section 4.1 reveals that the paper sits in an uncomfortable middle ground: it gestures toward a unifying theoretical framework that could genuinely explain why gradient-based OOD methods work, but it never commits to the formal derivations needed to make that claim stick. The dimension estimation part is the paper's strongest concrete contribution, yet it is treated almost as an afterthought. The paper would be stronger if it either (a) dropped or drastically toned down the OOD unification claims and focused on the gEPK as a tool for dimension estimation and cross-model comparison, or (b) provided rigorous derivations connecting at least two OOD methods to the gEPK basis.

## Suggestions

1. **Fix the proof of Theorem 4.1.** The correct reasoning is: if the learned adjustment is non-zero, then at least one inner product ⟨φ_{s,t}(x), φ_{s,0}(x_i)⟩ ≠ 0, meaning φ_{s,t}(x) has a non-zero projection onto span(B). Clarify whether the theorem claims the test gradient is *in* span(B) or merely has a *non-zero projection onto* span(B) — these are different claims and only the latter follows from Equation 16.

2. **Provide at least one worked derivation for an OOD method.** Choose GradOrth (already closest) and show, with explicit algebraic steps, how its score is a special case of the gEPK projection under the assumption of MSE loss and last-layer-only gradients. This single concrete derivation would dramatically strengthen the unification claim.

3. **Include a quantitative OOD detection experiment.** Compute the gEPK-based score on a standard benchmark (e.g., CIFAR-10 vs. SVHN) using a practical approximation (final training step only, or a few checkpoints), and report AUROC with standard deviations. Even moderate performance would demonstrate that the framework has practical relevance.

4. **Define signal manifold dimension rigorously.** Either connect the rank of G to an established notion of intrinsic dimension, or explicitly state that the paper is proposing a *new* definition (model-relative signal dimension) and justify why it is meaningful.

5. **Add a limitations section.** Acknowledge that the integral over training paths is computationally prohibitive for large models, and discuss potential approximations (e.g., discretizing the integral to a few checkpoints, or noting when φ_{s,t}(x) is approximately constant over t).

6. **Fix notational inconsistencies.** Use S (not N) for the number of training steps in Theorem 3.1 and throughout, to match the theorem statement's own notation.

## Score and Decision

The paper introduces an interesting theoretical framework (gEPK) and a novel method for dimension estimation. However, a central proof (Theorem 4.1) contains a genuine logical error, the claimed unification of OOD methods is asserted rather than derived, and the experimental support is too thin to validate the paper's broader claims. The theoretical contribution in Theorem 3.1 is sound and the dimension estimation approach is novel, but the paper's headline claims about explaining gradient-based OOD methods are not adequately substantiated. Substantial revision — including a corrected proof, at least one rigorous algebraic derivation connecting an OOD method to the gEPK, and a quantitative OOD experiment — would be needed to make this paper acceptable. In its current form, the paper reads as a promising work-in-progress rather than a complete, rigorous contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>