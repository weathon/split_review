Now I have a thorough understanding of the paper and can verify all claims against it. Let me compose the final consolidated review.

## Summary

This paper identifies an ambiguity in the standard definition of "semantic shift" for OOD detection and formalizes it by introducing precise definitions of Semantic Space (span of differences between class mean vectors) and Covariate Space (its orthogonal complement). Under a linear classifier + Gaussian assumptions framework, the authors prove (Theorem 1) that OOD distributions whose mean differs from ID means only in Covariate Space are indistinguishable from ID by any post-hoc method. They propose a "Tractable OOD" definition requiring a minimum distance δ in Semantic Space, and validate their theory with both synthetic experiments and an ImageNet-based setup where 10 post-hoc methods all fail at ~50% AUROC when breed-level features fall into the Covariate Space under coarse-grained training.

---

## Strengths

- **Precise formalization of Semantic and Covariate Spaces clarifies an ambiguous notion.** The paper provides clean, mathematically grounded definitions (Definition 1-2, Proposition 1) that replace vague descriptions of "semantic shift" with a verifiable condition. This enables rigorous analysis of which OOD settings are fundamentally intractable. (Evidence: Equations 3-5, Proposition 1.)

- **Theoretical proof that Covariate-space-only shifts are undetectable by post-hoc methods (Theorem 1).** The paper proves that if two distributions have identical Semantic Space projections, their output distributions under a trained linear classifier have zero KL divergence. This formally explains — and goes beyond merely observing — why certain OOD settings are impossible for any post-hoc method. (Evidence: Theorem 1, Corollary 1.)

- **Clean experimental demonstration of a real-world intractable case on ImageNet.** The breed-aggregated vs. breed-separated training comparison is well-designed: all 10 post-hoc methods fail (AUROC ≈ 50%) under the breed-aggregated setup for OOD-breed detection while succeeding (≈ 70–75%) under breed-separated training. The experiment cleanly isolates the training-setup-dependent nature of tractability. (Evidence: Table 2, Figure 4, Figure 5.)

- **Weight matrix decomposition (Proposition 2) provides mechanistic insight into why the classifier is blind to Covariate Space features.** The visualization in Figure 2 shows weights on Covariate Space dimensions converging to zero during training, directly confirming the proposed mechanism. (Evidence: Proposition 2, Figure 2.)

- **Multiple converging lines of evidence strengthen the empirical case.** The paper validates its theory through synthetic Gaussian data (Table 1), ImageNet experiments (Table 2), weight dynamics (Figure 2, Figure 5), confidence distribution comparisons (Figure 4), and t-SNE feature visualization (Figure 6), all converging to the same conclusion.

---

## Weaknesses

### Fatal
None.

### Major

1. **The "Tractable OOD" definition (Definition 4) is a diagnostic re-framing, not a practical solution.** The definition requires OOD distributions to differ from ID in Semantic Space by at least δ. However, the Semantic Space itself depends on the trained model's class means and cannot be determined a priori for a real dataset without already having the model and its features. The paper does not provide a method to estimate the Semantic Space from training data alone, which limits the definition's utility for benchmark construction or model evaluation. While the δ-ablation experiment (Table 2) is informative, it validates an expected monotonic relationship rather than establishing that the definition can be applied in practice.

2. **The core formal insight — that OOD detection fails when coarse-grained training collapses discriminative features — is not surprising.** The finding that a classifier cannot detect OOD samples differing only along feature dimensions it was never trained to use is intuitive and well-appreciated in the community (e.g., the practical difficulty of near-OOD vs. far-OOD, and the effect of label granularity on OOD detection). The paper provides a clean mathematical wrapper around this intuition but does not derive any non-obvious predictions or offer a method to overcome the limitation. The contribution is valuable as formalization but modest in terms of novel insight.

### Minor

1. **The ImageNet experiment does not directly verify that OOD dog breeds have identical Semantic Space projections.** The paper argues that under breed-aggregated training, breed-specific features reside in the Covariate Space because the classifier does not need them for ID classification. The evidence is circumstantial: AUROC ≈ 50% is consistent with the theory, but the paper never computes or estimates the actual Semantic Space projections of ID and OOD dog class means (e.g., using penultimate-layer features) to confirm they are indeed equal. A direct measurement would strengthen the causal link between the theoretical condition and the observed failure.

2. **The theoretical analysis makes strong simplifying assumptions (linear classifier, Gaussian class-conditional distributions, Assumptions 1-2) and the gap to deep nonlinear networks is bridged only empirically.** The paper openly acknowledges this in its Limitations section, which is commendable. However, the claim that experiments "confirm that our theoretical analysis holds within high-dimensional image-based input spaces and when nonlinear classifiers are applied" (line 326) is somewhat overstated — the experiments are consistent with the theory but do not verify that the conditions of Proposition 2 (e.g., Assumption 2) actually hold for the ResNet's learned features. The theory's predictions are corroborated, not proven, in the deep learning setting.

### Trivial
None.

---

## Nice-to-Haves

- **Direct verification of Semantic Space projections on ImageNet:** Computing the ID and OOD class means in the ResNet-18's penultimate feature space, then projecting them onto the estimated Semantic Space, would confirm whether the OOD breed means truly have equal Semantic projections.
- **Controlled synthetic experiment with a learned (nonlinear) deep feature encoder:** Passing synthetic data through a small CNN and checking whether the theory's predictions hold for learned features would strengthen the connection between the linear theory and deep learning practice.
- **Visualization of the weight matrix decomposition (Proposition 2) for the ResNet's last layer** after transforming to the empirical Semantic Space basis would provide a direct analogy to Figure 2 in the deep learning setting.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength Finder's Strength #4 ("Tractable OOD definition provides a constructive solution")** — This conflicts with the verified weakness that the definition is primarily diagnostic rather than practically actionable. The weakness is more compelling, so this strength is removed.
- **Criticism: "omits works on subclass-specific OOD detection and near-OOD/far-OOD distinction"** — Instructions prohibit citing missing related works, as the reviewer cannot confirm their existence or relevance.
- **Criticism: "does not engage with formal definitions in Yang et al. 2024 (OpenOOD)"** — Same as above; removed per instructions.
- **Criticism: "Assumption 2 is not proven or empirically checked"** — The paper explicitly states these assumptions are validated in the appendix (line 142), which was stripped by the parser.
- **Criticism: "proof of Proposition 2 (appendix not provided)"** — The appendix exists in the original submission; the parser stripped it.
- **Criticism about missing appendix, missing proofs in appendix** — All such references are to sections stripped by the parser; they exist in the original submission.
- **Criticism that the paper "does not cite or discuss prior work, overclaiming novelty"** — This is a missing-related-works criticism, removed per instructions.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already articulate or imply. The core observation — that formalizing the Semantic/Covariate Space decomposition cleanly explains when and why post-hoc OOD detection fails — is the paper's own contribution, and the reviews largely confirm that the paper executes this well while noting that the insight itself is intuitive in hindsight.

---

## Suggestions

1. **Add a direct measurement of Semantic Space projection equality in the ImageNet experiment.** Compute feature-space class means from the trained ResNet-18, estimate the Semantic Space from the ID class mean differences, and verify that OOD breed class means have near-identical projections. This would directly confirm the theory's key condition and address the most substantive evidential gap.

2. **Reframe the "Tractable OOD" definition more modestly.** Explicitly acknowledge that the definition's primary value is analytic and diagnostic (a necessary condition for tractability), not prescriptive, and discuss the practical challenge of determining the Semantic Space a priori. This would preempt the criticism that the definition is circular.

3. **Tone down the claim that experiments "confirm" the theory holds for deep networks.** Replace "This confirms that our theoretical analysis holds within high-dimensional image-based input spaces and when nonlinear classifiers are applied" (line 326) with a more measured statement like "These results are consistent with the theoretical predictions and suggest that the framework extends beyond the simplified setting, though a rigorous theoretical treatment for deep networks remains open."

---

## Score and Decision

The paper makes a modest but genuine contribution by formalizing an ambiguity in OOD definitions and providing a clean theoretical analysis under simplifying assumptions, supported by well-designed experiments. However, the core insight is unsurprising, the "Tractable OOD" definition is more diagnostic than practical, and the theoretical gap to deep networks is bridged only empirically. The paper is well-written and competently executed, but the contribution is not strong enough for acceptance at a top venue in its current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>