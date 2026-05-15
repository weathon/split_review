Now I have a thorough understanding of the paper and the reviewer inputs. Let me synthesize my final review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper introduces LieLAC (Lie Algebra Canonicalization), a framework for making pre-trained neural networks equivariant under arbitrary Lie groups (including non-compact ones) using energy-based canonicalization that only requires knowledge of the Lie algebra's infinitesimal generators. The authors extend prior canonicalization theory to non-compact groups via weighted closed canonicalizations (Section 3), provide practical guidance for energy design and Lie-group optimization (Section 4), and demonstrate the approach on invariant image classification (MNIST under affine/homography groups) and PDE equivariance (heat, Burgers, and Allen-Cahn equations with a pre-trained Poseidon foundation model).

## Strengths
- **Extends canonicalization theory to non-compact Lie groups via weighted closed canonicalizations.** The paper identifies that prior frame/canonicalization frameworks (Dym 2024, Ma 2024) require compact stabilizers or finite groups, and bridges this gap by introducing weighted closed canonicalizations (Definition 9), proving their sequential closure properties (Theorem 1), and characterizing which ones arise from energy minimization (Theorem 2). The commutative diagram (Figure 2) cleanly unifies these concepts.

- **Provides a constructive method using only infinitesimal generators, enabling equivariance for groups where only the Lie algebra is known.** For solvable Lie algebras (common in PDE symmetry groups), the method reduces group optimization to Euclidean optimization over Lie algebra coefficients via exponential decomposition (Section 4). For non-solvable cases, coordinate descent on basis vector fields is provided. This is a genuine practical advance over methods requiring full group parameterization.

- **Demonstrates improved OOD generalization for a pre-trained foundation model (Poseidon) on the Allen-Cahn PDE.** LieLAC with fine-tuning on only 100 trajectories reduces the OOD test error from 7.619e-3 to 1.143e-3 (~7× improvement) and average error from 4.132e-3 to 1.055e-3 (Table 1). This validates that the method can impose meaningful equivariance under a non-compact group (SE(2)) on a large pre-trained neural operator without costly retraining.

- **The t-SNE visualization (Figure 4) and image examples (Figure 3) provide compelling intuitive evidence that canonicalization restores distorted MNIST digits to their canonical form, cleanly separating classes.** This directly illustrates the equivariance property in a visually interpretable way.

## Weaknesses

### Fatal
None. The paper's core theoretical contribution is sound, and there is quantitative evidence for some of the claimed applications.

### Major
- **Quantitative evaluation is missing for two of three PDE test cases (heat and Burgers equations).** The paper's central motivation (Sections 1, 1.2) is making neural PDE solvers equivariant under Lie point symmetries, yet the heat equation and Burgers' equation are supported only by visual examples (Figures 2, A.3, A.4) with no numerical error metrics, no baseline comparisons, and no quantitative demonstration that canonicalization improves prediction quality. For a paper that claims to "showcase LieLAC's efficacy on ... Lie point symmetry equivariant neural PDE solvers," the absence of any quantitative PDE result for two of the three studied PDEs is a significant gap. At minimum, a table comparable to Table 1 for the heat or Burgers equation would be needed to support the core claim.

- **The MNIST comparison to equivariant architectures (affConv/homConv) is confounded.** LieLAC's canonicalizer uses a VAE energy with adversarial regularization trained on "real and partially transformed data" (Section 4), meaning the canonicalizer has access to information about the transformation distribution that the baseline equivariant architectures do not. The baselines (Macdonald 2022) are trained only on MNIST without augmentation. The claim of "improved equivariance" conflates the effect of the canonicalization mechanism with the effect of additional data used to train the canonicalizer. An ablation of LieLAC without adversarial regularization would be needed to determine how much of the performance gap is attributable to canonicalization versus extra data.

- **The Allen-Cahn experiment table uses ambiguous naming that obscures the experimental design.** The row "Poseidon + ft (can)" is not clearly explained in the main text — it is unclear whether this refers to Poseidon fine-tuned on canonicalized data, Poseidon with a canonicalized fine-tuning procedure, or some other variant. The relationship between "LieLAC [Poseidon + ft.]" and "Poseidon + ft (can)" is not self-evident. This makes it difficult for readers to interpret the comparison.

### Minor
- **The Hausdorff measure regularity assumption (Section 3.2) is mathematically non-trivial and receives limited justification.** The construction of weighted closed canonicalizations via normalized Hausdorff measure on energy minimizer sets assumes non-zero Hausdorff measure for all x. The paper acknowledges this assumption but provides no concrete examples of energies or groups for which it holds, beyond a reference to the (stripped) appendix. While the practical method (using finite sampling) likely side-steps this issue, the theoretical gap weakens the claimed theoretical contribution.

- **No ablation or analysis of the adversarial regularization component.** The paper introduces adversarial regularization to address flat energy regions (Section 4), but provides no experiments isolating its effect on canonicalization quality, convergence, or downstream task performance. Without this, readers cannot assess whether this component is essential or incidental.

- **No convergence statistics or sensitivity analysis for the Lie-group optimization.** The paper states that multi-initialization gradient descent is "sufficient for convergence" but provides no quantitative evidence — number of initializations, success rates, runtime, or sensitivity to hyperparameters — for any of the PDE or image experiments. While the solvable algebra structure (used for the PDEs shown) makes Euclidean optimization plausible, the lack of validation is a gap.

### Trivial
- **No confidence intervals or run-to-run variance reported for accuracy numbers** (Table 1 for MNIST, Table for Allen-Cahn). This is common in single-run evaluations but would strengthen the paper.
- **The 2D toy example (Section 5.1) is illustrative only** with no quantitative metric of improvement in classification accuracy.

## Nice-to-Haves
- A comparison to data augmentation baselines for the PDE cases (as in Brandstetter 2022) would help contextualize whether LieLAC's complexity and fine-tuning requirements are worthwhile relative to simpler alternatives.
- Quantifying the computational overhead of energy-based canonicalization (runtime per sample) would help practitioners assess practical applicability.
- Failure case analysis for the canonicalization optimization would give insight into the method's robustness.

## Removed Points
- **"The paper overstates the problem — many PDE symmetry groups are actually matrix groups."** The paper's claim is that existing equivariant architectures focus on "simple" (typically compact) groups, which is accurate. SL(2,R) is a matrix group but is non-compact and incompatible with most off-the-shelf equivariant architectures. This is a misunderstanding of the paper's claim.
- **"The physics-informed loss must be invariant... this is not addressed."** The paper explicitly scopes to cases where the group action separates x,t from u (line 322) and defines operator equivariance (Equation 6). The physics-informed loss is mentioned in preliminaries but the method operates at inference time, making loss invariance a secondary concern.
- **"The coordinate descent algorithm (Han et al.) is not explained."** Referencing prior work for standard optimization algorithms is standard practice; the paper does not need to reproduce the algorithm.
- **"Figure 2c is not discussed in the main text."** The figure is referenced in the main text (line 326: "examples of canonicalized solutions are shown in \Cref{fig:can_illustration}").
- **"No confidence intervals" and other formatting/reproducibility nitpicks** are moved here as trivial concerns that do not affect the paper's substance.

## Novel Insights
None beyond the paper's own contributions. The reviews identify genuine gaps (missing quantitative PDE results, confounded MNIST comparison) but do not surface novel scientific observations about the method itself beyond what the authors already present.

## Suggestions
1. **Provide quantitative PDE results for at least the heat equation** (the simplest case) with error metrics on held-out transformed initial conditions, comparing canonicalized vs. uncanonicalized model predictions. This is the single most important addition needed to support the paper's core claim.
2. **Ablate the adversarial regularization** in the MNIST experiments by reporting LieLAC's performance using only the VAE-based energy without adversarial training, to clarify whether the comparison to affConv/homConv is fair.
3. **Rename the Allen-Cahn table rows** to be self-explanatory (e.g., "Poseidon fine-tuned on canonicalized data" instead of "Poseidon + ft (can)"), and explain each row in the main text.
4. **Report convergence statistics** (success rate, median iterations) for the Lie-group optimization on at least one PDE example to substantiate the claim that multi-initialization gradient descent is "sufficient for convergence."

## Score and Decision

**Originality:** Good. Extending canonicalization theory to non-compact groups via weighted closed canonicalizations is a genuine theoretical contribution, and the application to pre-trained neural operators is novel.

**Importance of research question:** High. Making pre-trained models equivariant under non-compact symmetry groups is a relevant problem for physics-informed ML and scientific foundation models.

**Claims supported:** Partially. The PDE equivariance claim is under-supported quantitatively (2 of 3 PDEs lack metrics). The MNIST comparison is confounded. The theoretical framework is well-supported.

**Soundness of experiments:** Moderate. The Allen-Cahn experiment is the strongest, but the missing quantitative results for simpler PDEs and the confounded MNIST comparison weaken the empirical case.

**Clarity of writing:** Good overall. The theoretical sections are clearly presented. Some experimental details (table naming, OOD definition) could be clearer.

**Value to the research community:** Moderate. The theoretical framework and practical guidance are useful, but the experimental limitations mean readers must invest additional effort to validate the claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>