- Decision: Reject
- Avg Score: 5.67
- Scores: 8, 3, 6
Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

## Summary

This paper establishes a theoretical framework for the nonparametric identifiability of hidden concepts from multiple classes of observations, drawing inspiration from comparison-based cognitive learning. The key results are: (1) local comparison guarantees (Theorem 1, Proposition 1) that can identify unique concepts between any pair of classes even when global conditions fail, (2) global identifiability of all class-dependent concepts (Theorem 2) under a Structural Diversity condition, and (3) identifiability of the connective structure between classes and concepts (Proposition 3). The framework operates without assuming specific concept types, functional relations, or parametric generative models — instead relying on structural conditions on the class-concept dependency matrix and Jacobian sparsity.

## Strengths

- **Provable nonparametric identifiability with different assumptions from prior work**: Theorem 2 (Section 3.2) shows that under the Structural Diversity condition (Assumption 1) and a distributional variability condition, all class-dependent concepts are identifiable up to element-wise invertible transformation and permutation. The proof (referenced to Appendix B.3) does not require linearity (Rajendran et al., 2024), additivity/no-occlusion (Lachapelle et al., 2023; Brady et al., 2023; Wiedemer et al., 2024), or parametric generative models. This provides a genuinely different theoretical angle on concept learning identifiability.

- **Local comparison guarantees enable partial recovery when global conditions fail**: Theorem 1 and Proposition 1 (Section 3.1) provide guarantees for disentangling unique concepts between any pair (or set) of classes, independent of whether global Structural Diversity holds. As the paper discusses (Section 3.1, Implications), this allows recovery of as many concepts as possible when diversity is limited — a flexibility absent from prior work that loses all guarantees upon any assumption violation.

- **Nonparametric identifiability of the connective structure between classes and concepts**: Proposition 3 (Section 3.3) shows that the binary structure matrix M linking classes to concepts is identifiable up to row permutation without requiring Structural Diversity, relying only on pairwise comparison assumptions. This recovers latent compositional relations from observational data without parametric assumptions.

## Weaknesses

### Major

- **Unclear definition of τ and the T ∈ τ condition in Theorem 1**: In the Technical Notations (line 44), τ is defined as "a set of matrices with the same support of T in D_ĉĝ = T D_c g, where T is a matrix-valued function." Then Theorem 1 (line 79) requires "a matrix T ∈ τ." As written, this is circular: τ is defined relative to T, and T is then chosen from τ. While the intended meaning can be inferred (τ is the set of matrices sharing a support pattern, and T is a specific matrix with that pattern), the circular presentation undermines the reader's ability to assess whether the condition is substantive. This condition appears in Theorem 1, which is foundational to Propositions 1, 2, 3, and Theorem 2. The authors should provide a non-circular, standalone definition and clarify why the condition is not vacuous. *Why this matters: This is the most important presentation issue in the paper — without a clear definition, the core theoretical machinery is difficult to evaluate.*

### Minor

- **Real-world experiments lack quantitative evaluation and baselines**: The real-world results (Fashion-MNIST, EMNIST, AnimalFace, Flower102) are purely qualitative — showing concept visualizations without ground-truth comparisons. The paper states "the semantics of the identified concepts align with our understanding" (line 187), but there is no quantitative metric, no baseline comparison, and no systematic evaluation of whether the recovered concepts correspond to true latent concepts. For datasets like Fashion-MNIST where attribute-level labels exist, proxy tasks (e.g., classifier accuracy from recovered concepts to known attributes) would strengthen the empirical support. For a theory paper this is not fatal, but it limits how convincingly the practical applicability of the theory is demonstrated.

- **The distributional variability condition in Theorem 2 is stronger than the paper's discussion implies**: The condition requires that for every non-product subset A_z of the latent space, there exist two classes with different integrals of p(z|c) over A_z (lines 107-111). The paper justifies this by arguing "it is virtually impossible for the measures corresponding to all classes to be almost identical" (line 129). However, this conflates two different strengths: classes having different overall distributions (likely) vs. classes having different integrals on *every single non-product subset* (a much stronger condition). Two classes could have different distributions yet still yield equal integrals on specific subsets A_z. The paper's Gaussian example (Example 4) shows the condition can hold but does not establish that it is mild in practice.

- **The ℓ₁ regularization on M̂ and F̂ could produce a confound in synthetic experiments**: The objective function (line 161) uses ℓ₁ norm applied to M̂ and F̂, which directly encourages the sparsity patterns that the theory relies on. The synthetic experiments compare "Ours" (generated satisfying the assumptions + ℓ₁ regularization) to "Base" (no structural conditions + presumably no or different regularization). The gap between Ours and Base could partially reflect the regularization's inductive bias rather than the identifiability conditions per se. The paper does not test whether models with the right inductive bias recover concepts even when identifiability conditions are violated.

- **Proposition 3 is claimed but not experimentally validated**: The paper proves that the connective structure M can be recovered (Proposition 3), but the experiments never test structure recovery accuracy (e.g., F1 score or AUROC on the synthetic data where the ground-truth M is known). This leaves a gap between theory and empirical verification for one of the claimed contributions.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- A concrete interpretation of the Structural Diversity assumption on real datasets (e.g., of the four real-world datasets used, which satisfy it and which do not) would help readers calibrate its restrictiveness.
- Sensitivity analysis under mild violations of Structural Diversity (e.g., injecting shared concepts) would strengthen claims about practical relevance.
- Statistical variance information (error bars, significance tests) for the synthetic MCC plots would improve interpretability.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Assumptions stronger than framing suggests** (harsh critic point #2, about the Jacobian spanning condition being restrictive). The paper's claim is about not assuming concept types, functional relations, or parametric models. The Jacobian spanning and Structural Diversity conditions are structurally different from these categories, and the paper makes this distinction clear (line 127). Removed as misread.

2. **Cognitive analogy is ornamental** (harsh critic, Section 1 notes). This is a style critique. Many papers use motivating analogies without directly operationalizing them. Removed as a style nitpick.

3. **p(z|c) = p(z_A|c)p(z_B) is a strong conditional independence** (harsh critic, Section 2 notes). The paper acknowledges this and cites prior work using similar modularity. Removed as the paper already justifies this.

4. **Proposition 2 similar to Zheng et al. (2022)** (harsh critic, Section 3 notes). The paper explicitly cites Zheng et al. (2022) and says "as proposed in (Zheng et al., 2022)" (line 145). Removed as factually incorrect — the paper already acknowledges the connection.

5. **Cherry-picking risk with SD selection** (harsh critic, Section 4 notes). The paper uses a transparent criterion ("largest standard deviations"). This is a principled selection method, not cherry-picking. Removed as speculative and incorrect.

6. **Strength finder's generic/overclaimed strengths**: The strength about "empirical validation on both synthetic and real-world datasets" is overstated — the real-world validation is weak. This is better captured as a nuanced point in my weaknesses section. The strength about "provable nonparametric identifiability" is legitimate and retained.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface any genuinely novel insight about the paper that the paper itself does not already articulate.

## Suggestions

1. **Clarify the definition of τ and the T ∈ τ condition in Theorem 1.** Provide a non-circular definition. Specifically: define τ as the set of matrices with a given support pattern (e.g., the support of the Jacobian of the transformation between estimated and true latent variables, which emerges from the identifiability relationship D_ĉĝ = T D_c g), then state the condition as "there exists a matrix T with supp(T) matching that pattern such that...". Example 2 attempts to illustrate this but the main definition needs rewriting.

2. **Add quantitative evaluation for at least one real-world dataset.** For Fashion-MNIST, attribute labels (garment type, sleeve length, etc.) could serve as proxies. Measuring correlation between recovered concept dimensions and these attributes would substantially strengthen empirical support.

3. **Discuss the strength of the distributional variability assumption more accurately.** Acknowledge that requiring distinct integrals on *every* non-product subset is stronger than merely requiring classes to have different distributions, and briefly discuss when this might fail.

4. **Add structure recovery results** (Proposition 3) to the synthetic experiments — report F1 or AUROC for recovering M.

5. **Consider an ablation** that tests whether ℓ₁ regularization alone (without identifiability conditions) can produce high MCC, to rule out the confound.
