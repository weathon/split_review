Now I have all the information I need. Let me produce the consolidated review.

---

## Summary

The paper develops a theoretical framework for provably learning hidden concepts from multiple classes of observations, motivated by the cognitive mechanism of learning through comparison. It proves that (i) concepts unique to class pairs can be disentangled via local comparison (Theorem 1); (ii) all class-dependent concepts are identifiable up to element-wise invertible transformations under a Structural Diversity condition (Theorem 2); and (iii) the connective structure between classes and concepts can be recovered without requiring Structural Diversity (Proposition 3). The theory is nonparametric — no assumptions on concept types, functional relations, or parametric generative models are needed. Experiments on synthetic data (MCC curves) and real-world datasets (Fashion-MNIST, EMNIST, AnimalFace, Flower102) provide supporting evidence.

## Strengths

- **Nonparametric identifiability via structural diversity across classes.** Theorem 2 shows that class-dependent concepts can be identified up to element-wise invertible transformations and a permutation under only structural diversity (Assumption 1) and mild distributional variability, without requiring linearity, additivity, disjoint Jacobians, or parametric generative models. This significantly relaxes assumptions from prior work (e.g., Rajendran et al. 2024 requiring linearity; Brady et al. 2023, Wiedemer et al. 2024 requiring no occlusion or additivity).

- **Flexible partial identifiability through local comparison.** Theorem 1 and Proposition 1 show that even when global conditions fail, any pair (or subset) of classes with sufficient diversity still yields guarantees for their unique concepts. This "identify what you can" approach is more practical than prior methods that lose all guarantees if any assumption is violated, and the paper explicitly discusses this advantage (Section 3.1, "Insights" paragraph).

- **Identifiability of the hidden structure.** Proposition 3 demonstrates that the connective structure matrix M (linking classes to concepts) can be identified up to row permutation *without* requiring Structural Diversity, providing a separate guarantee that holds in even more general scenarios than concept identifiability.

- **Diverse empirical validation.** Experiments span four real-world datasets (Fashion-MNIST, EMNIST, AnimalFace, Flower102) and show that identified concepts align with semantically interpretable attributes (e.g., "sleeve length" for pullover, "heel height" for ankle boot, "Ursid" for panda). The Flower102 experiment (Figure 9) demonstrates that the same concept is consistently recovered across different environments, supporting the robustness claim.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 2's additional assumption quantifying over all measurable sets is very strong and insufficiently justified.** The condition requires that for *any* measurable set A_z (non-zero probability, not a product of class-independent and class-dependent subspaces), there exist *some* pair of classes (k,v) whose conditional probability masses on A_z differ. This is not merely "distinct conditional distributions" — it requires that every non-trivial measurable set distinguishes at least one pair of classes. The paper's defense (Section 3.2, "assumption is highly likely to be satisfied") is too hand-wavy for a condition that quantifies over uncountably many sets. A rigorous justification or a weaker sufficient condition is needed. This limits the practical applicability of the main global identifiability result.

- **Gap between asymptotic identifiability and the claim of "provably learning."** The title and abstract claim "provably learning concepts," but the theory establishes identifiability under exact distribution matching with infinite data (the standard in the nonlinear ICA / identifiability literature). No finite-sample bounds, convergence rates, or consistency results are provided. While this gap is common in identifiability papers, the framing ("provably learning") over-promises relative to what is delivered.

### Minor

- **Confusing presentation of conditions involving D̂ and τ in Theorem 1.** The condition `[T D_c g]_{:,i} ∈ ℝ^{n_A}_{D̂_{:,i}}` involves the estimated Jacobian support D̂ (a quantity depending on the estimator). Upon close reading, this condition is actually automatically satisfied: D̂ is defined as the support of D_ĉĝ, and by the chain rule D_ĉĝ = T D_c g (when the estimated model matches the marginal distribution), so the condition reduces to `[T D_c g]_{:,i} ∈ ℝ^{n_A}_{supp(T D_c g)_{:,i}}` which is true by definition. The only substantive requirement is the spanning condition on the true Jacobian. However, the paper's notation and presentation make this unclear, inviting the (incorrect) circularity objection raised by the reviewer. The definition of τ ("set of matrices with the same support of T in D_ĉĝ = T D_c g") is also ambiguous and could be stated more cleanly. This is a presentation/rigor issue that should be fixed.

- **Synthetic experiments have a weak baseline and do not systematically test assumption components.** The "Base" model simply removes structural regularization. A stronger ablation would test each condition separately: (i) removing the Structural Diversity assumption while keeping Jacobian conditions, (ii) violating the spanning condition while keeping Structural Diversity, etc. Without such controlled experiments, it is unclear whether the observed MCC improvements are due to the specific theoretical conditions or merely to sparsity regularization.

- **Real-world experiments are entirely qualitative.** Concept traversals and heat maps are interesting but do not constitute quantitative validation of identifiability. Datasets with known ground-truth generative factors (e.g., dSprites, Shapes3D, MPI3D) would enable MCC computation in a non-synthetic setting, partially bridging the theory-practice gap.

### Trivial

- **"Do not depend on" in Theorem 1 is not formally defined.** The phrase "ẑ_{π(A_i\A_j)} do not depend on z_{A_j}" presumably means functional independence: the function mapping z to ẑ has zero partial derivatives w.r.t. the specified components. This should be made explicit.

- **Minor notation issues.** The hat symbol is used inconsistently in Example 2 (line 93) with garbled superscripts (likely a PDF extraction artifact); the definition of τ could be made clearer.

## Nice-to-Haves

- Adding quantitative metrics on real-world data (e.g., using datasets with known generative factors) would significantly strengthen the experimental validation without being strictly necessary for a theory paper.
- Comparison to prior concept discovery methods (e.g., Concept Bottleneck Models) on the real-world benchmarks could contextualize the empirical results, though this is outside the paper's stated scope.
- A discussion of when the strong condition in Theorem 2 (measurable sets) can be replaced by simpler sufficient conditions (e.g., distinct conditional densities) would improve accessibility.

## Removed Points

- **"Circularity invalidates the theoretical core"** — Removed. The condition involving D̂ is automatically satisfied (D̂ = supp(T D_c g) by definition), so there is no circularity; the paper's presentation is merely confusing. The substantive condition is the standard Jacobian spanning condition. See the Minor weakness above.
- **"Missing appendix/proofs"** — Removed per meta-instructions (parser strips appendix).
- **"Shark/turtle example inconsistent with formal definition"** — Removed. The example is illustrative ("might include") and the critic's interpretation conflates "class-dependent" with "unique to a single class."
- **"Conditional independence stated without justification"** — Removed. This is a modeling assumption common in the literature, not a missing justification.
- **"Does not compare to Concept Bottleneck Models"** — Removed as scope creep; the paper is about identifiability theory, not benchmark performance.
- **"No dSprites/Shapes3D experiments"** — Moved to Nice-to-Haves; these would strengthen but are not core flaws.

## Novel Insights

The most interesting observation emerging from the reviews is that the paper's *presentation* of conditions involving D̂ and τ is the source of a serious misunderstanding that could have been avoided with simpler, cleaner notation. The critic interpreted D̂ as an unknown property of the estimator that must be checked, when in fact it is determined by the relation D_ĉĝ = T D_c g and the condition is automatically satisfied. This highlights a broader challenge in identifiability papers: when conditions involve the estimated model (even implicitly), authors must be exceptionally careful to distinguish what is assumed about the true process from what follows from distribution matching. The paper's core theoretical contribution (identifiability through structural diversity) does *not* suffer from circularity — the actual mathematical condition reduces to a spanning condition on the true Jacobian — but the paper would benefit substantially from restating the theorems without the unnecessary D̂/τ apparatus.

## Suggestions

1. **Restate Theorem 1 without D̂ and τ.** Since the condition [T D_c g]_{:,i} ∈ ℝ^{n_A}_{D̂_{:,i}} is automatically satisfied given the definitions, the theorem can be stated with only the spanning condition on the true Jacobian. This would eliminate the circularity confusion entirely.
2. **Weaken or better justify the measurable-set condition in Theorem 2.** Either prove it follows from a simpler condition (e.g., distinct everywhere-positive densities) or acknowledge its strength and discuss when it can be replaced.
3. **Add controlled synthetic ablations** that test each assumption component independently (Structural Diversity on/off, spanning condition satisfied/violated).
4. **Add at least one quantitative real-world experiment** on a dataset with known ground-truth generative factors.
5. Define "do not depend on" formally.

## Score and Decision

The paper addresses an important problem — providing identifiability guarantees for concept learning without restrictive parametric assumptions. The core ideas (structural diversity across classes, local-to-global comparison) are novel and valuable. The theoretical contribution is genuine, and the confusing notation does not invalidate the mathematics. However, the strong assumption in Theorem 2 needs better justification, the experimental validation has notable gaps, and the gap between asymptotic identifiability and "provably learning" is not bridged. With revisions, this could be a strong paper.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>