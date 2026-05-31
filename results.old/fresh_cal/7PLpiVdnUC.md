Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes LieLAC (Lie Algebra Canonicalization), a framework for making pre-trained neural networks equivariant under arbitrary Lie groups—including non-compact ones—using only the Lie algebra's infinitesimal generators. The authors extend the theory of canonicalization and frame averaging to non-compact groups via weighted closed canonicalizations, prove connections between these concepts, and demonstrate the method on invariant image classification (affine/homography groups) and Lie-point-symmetric PDE evolution (heat, Burgers, Allen-Cahn equations with a Poseidon foundation model).

## Strengths

1. **Theoretical extension to non-compact Lie groups.** The paper introduces weighted closed canonicalizations (Definition 4) and proves that the sequential closure of weighted orbit canonicalizations equals weighted closed canonicalizations (Theorem 1). This addresses a known limitation of prior work (Dym 2024, Ma 2024) that was restricted to finite or compact groups—a non-trivial result because non-compact orbits are not closed.

2. **Demonstration of PDE symmetry groups with non-compact structure.** The paper works out how energy-based canonicalization applies to SL(2,R) (heat and Burgers equations) and SE(2) (Allen-Cahn equation) using only generators of the Lie algebra via a global exponential parameterization for solvable algebras. No previous equivariant architecture handled these continuous non-compact groups.

3. **Strong image classification results.** On affNIST and homNIST, LieLAC applied to a standard pre-trained CNN achieves accuracies of 0.972 and 0.960, clearly outperforming the dedicated equivariant baselines affConv (0.943) and homConv (0.927) from Macdonald et al. (2022). The t-SNE visualizations further corroborate that canonicalization maps transformed data back to the original MNIST distribution.

4. **Fine-tuning efficiency for foundation models.** On the Allen-Cahn equation, LieLAC applied to the Poseidon foundation model reduces average test error from 4.132E-03 to 2.254E-03 without fine-tuning, and to 1.055E-03 with fine-tuning on only 100 trajectories. The OOD error drops from 7.619E-03 to 1.143E-03 (a ~6.7× reduction), demonstrating practical utility for large pre-trained models.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between theoretical construction and practical algorithm.** The theoretical development (Section 3) defines weighted canonicalizations as probability measures—specifically, the normalized Hausdorff measure—on the full set of minimizers M_E(x). The practical algorithm (Section 4) uses multi-initialization gradient descent to find *a* minimizer (or at best a distribution over initializations), without explicitly stating whether the output is a single element or an average over multiple found minimizers. The paper does not analyze how the practical algorithm relates to the theoretical guarantees (continuity, invariance under the Reynolds operator) or under what conditions the approximation is faithful. This gap is acknowledged implicitly (Section 4: "how these can be used in practice remains unaddressed") but is never closed: the reader cannot tell which theoretical properties, if any, the deployed algorithm inherits. Given that the core contribution claims theoretical grounding, this disconnect is a significant weakness.

2. **PDE experiments lack quantitative results in the main paper for two of three claimed examples.** The paper's central claim (abstract, conclusion) is demonstrating "Lie point symmetry equivariant neural PDE solvers using pre-trained models." However, the main paper sections for the heat and Burgers equations (Section 5.3) provide only visualizations of canonicalized solution snapshots and group-theoretic exposition, with no quantitative error numbers, no comparison to baselines, and no evaluation on transformed test sets. Quantitative results appear only for the Allen-Cahn equation (Table 1). This makes it impossible to evaluate the method's effectiveness for the heat and Burgers equations from the main paper alone. The paper references appendix sections for further details, but the main text should provide self-contained evidence for its core claims.

### Minor

1. **No explicit invariance/equivariance metrics for image classification.** The paper reports classification accuracy on affNIST and homNIST, which is an indirect measure of invariance. Direct metrics (e.g., variance of predictions under random transformations, or consistency across orbit elements) would more directly validate that the canonicalization achieves the claimed equivariance.

2. **No ablation on the optimization procedure.** The paper uses multi-initialization gradient descent but does not report how many initializations are used, how the number of initializations affects canonicalization quality, or how frequently the optimization fails to find a global minimizer. These details affect the computational cost assessment and the reproducibility of results.

3. **Ambiguity in the Allen-Cahn table row labeling.** The row "Poseidon + ft (can)" in Table 1 is not clearly explained—specifically, whether this is Poseidon fine-tuned on canonicalized data and then tested with or without canonicalization. This makes the comparison across rows harder to interpret.

### Trivial

None.

## Nice-to-Haves

- An ablation comparing the learned VAE-based energy to simpler alternatives (e.g., distance to dataset mean) would clarify whether the learned component is essential or whether a simpler energy suffices.
- A comparison to data augmentation baselines (Brandstetter 2022) for the PDE experiments would contextualize the improvements, though the paper's main claim is about canonicalization as an alternative to architectural equivariance, not to data augmentation.
- Quantitative invariance metrics (variance under random transformations) for the MNIST experiments would strengthen the validation.

## Removed Points

These points from the reviewers are flagged for removal—treat them with caution:

1. **"Hausdorff measure assumption is unexamined"** — The paper explicitly states this assumption (line 204: "We therefore must assume that $E$ is such that for all $x$, the Hausdorff measure of $\mc{M}_E(x)$ is non-zero") and references a discussion in the appendix ("Refer to \Cref{sec:measuretheory} for more discussion on the Hausdorff measure and on why this assumption is reasonable"). The assumption is acknowledged, not unexamined. Whether it holds in practice is a legitimate concern, but the paper does not ignore it.

2. **"Allen-Cahn restricted to C4 is a far cry from handling non-compact groups"** — The paper clearly explains this restriction arises because the domain $\Omega=[0,1]^2$ with periodic boundary conditions must be preserved by transformations. Only rotations by multiples of 90 degrees map the square to itself. The full SE(2) group is used for translations; only the rotation subgroup is discretized due to the domain constraint. This is an experimental design choice, not a limitation of the method.

3. **"The practical algorithm picks a single minimizer"** — The paper says it uses "a multi-initialization strategy for fixed step gradient descent, which turns out to be sufficient for convergence." It does not explicitly state that only a single minimizer is used, nor does it rule out averaging over multiple minimizers found from different initializations. The exact protocol is underspecified, but the critic's strong claim is not directly supported by the paper text.

4. **Speculative fatal claims** — Assertions that the theory-practice gap "invalidates the direct transfer of any theoretical guarantees" are phrased as fatal but depend on assuming the worst-case implementation scenario. The paper separates theory and practice into distinct sections and acknowledges practical challenges with optimization.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the strengths and weaknesses already articulated in the paper.

## Suggestions

1. **Clarify the practical algorithm's relationship to theory.** State explicitly: does the deployed method use a single minimizer, an average over multiple minimizers from different initializations, or a different aggregation? Then characterize the resulting approximation quality directly rather than appealing to the measure-based framework. Show—even on a toy problem—how the practical approximation degrades as optimization becomes harder.

2. **Include quantitative results for all PDE examples in the main paper.** For heat and Burgers equations, report at minimum the error on transformed test sets with and without canonicalization, ideally alongside baseline comparisons (even a simple data augmentation baseline would contextualize the results).

3. **Add explicit invariance metrics for the image classification experiments.** Report the variance of predictions or logit vectors under random transformations to directly measure the degree of invariance achieved.

## Score and Decision

The paper makes a genuine theoretical contribution (extending canonicalization theory to non-compact Lie groups) and provides a compelling practical demonstration on image classification. The Allen-Cahn/Poseidon experiment is a notable proof-of-concept for pre-trained neural operators. However, the paper's central claim about PDE applications is weakened by the absence of quantitative results for two of three examples in the main paper, and the gap between the measure-theoretic ideal and the deployed optimization algorithm is underexplored. These are addressable weaknesses, not fatal flaws, and the theoretical framework plus the successful image classification experiments provide sufficient value.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>