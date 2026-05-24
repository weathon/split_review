Now I have all the information. Let me write the consolidated review.

---

## Summary

This paper develops a theoretical framework for parameterizing equivariant functions mapping tuples of tensors to tensors under the diagonal action of the orthogonal, Lorentz (indefinite orthogonal), and symplectic groups. It provides explicit, practical parameterizations (Corollaries 1–3) based on invariant theory, avoiding Clebsch–Gordan decompositions, and demonstrates the approach on three synthetic problems: stress-strain tensor prediction, path signature approximation, and sparse vector estimation. The theoretical contribution — a unified characterization across multiple classical groups with parity handling — goes beyond prior work restricted to O(d) or SO(d).

## Strengths

1. **General invariant-theoretic characterization of equivariant tensor functions (Theorems 1 and 2).** The paper shows that O(d)-equivariant polynomial (and, by Thm. 2, entire) tensor functions can be expressed as contractions of input tensors with isotropic tensors, which are themselves built from Kronecker deltas and Levi-Civita symbols (Lemma 3). This provides a principled, unified alternative to Clebsch–Gordan-based methods. The theory extends to the Lorentz and symplectic groups, which e3nn/escnn do not cover. The connection to classical invariant theory (Jeffreys, 1973; Roe Goodman, 2009) is cleanly leveraged.

2. **Practical parameterizations for the vector-input case (Corollaries 1 and 3).** The paper distills the general theory into explicit recipes suitable for machine learning: equivariant functions from vectors to tensors are expressed as linear combinations of tensor products of input vectors and Kronecker deltas (or their Lorentz/symplectic analogues), with coefficients that are learnable functions of pairwise inner products. This makes the method accessible to practitioners and avoids the complexity of the full theorem.

3. **Demonstration on three diverse scientific problems.** The experiments span materials science (stress-strain tensors), time series analysis (path signatures), and theoretical computer science (sparse vector estimation). The method consistently outperforms non-equivariant baselines, and the sparse vector results show that learned equivariant models can operate in regimes where theory-based SoS methods lack guarantees. The path signature application combining equivariance with reparameterization invariance is a novel and natural use case.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No experimental comparison with existing equivariant architectures for O(d).** The path signature experiment (Table 2) uses O(d)-equivariant functions mapping vectors to tensors. Established architectures such as e3nn (Geiger & Smidt, 2022) or escnn (Cesa et al., 2022) directly handle this setting for d=3 via Clebsch–Gordan decompositions. Without such a comparison, it is difficult to assess whether the proposed parameterization offers practical advantages (accuracy, speed, sample efficiency) over widely-used baselines. The related work section acknowledges these methods and notes they are "more memory efficient than our general formulation in Theorems 1 and 2, but comparable to our Corollaries 1 and 3," yet no empirical validation of this comparison is provided.

2. **Inconsistent behavior of full vs. reduced model in sparse vector estimation (Table 3).** The reduced variant "Ours (Diag)," which only uses squared norms as input to the coefficient MLP, outperforms the strictly more expressive full model in several settings (e.g., Accept/Reject with Diagonal covariance, Bernoulli-Gaussian with Diagonal/Identity covariance, Corrected Bernoulli-Gaussian with Diagonal covariance). This suggests possible overfitting, optimization difficulties, or sensitivity to the high-dimensional Gram matrix input. The paper does not analyze or discuss this behavior, which weakens the claim that the full parameterization is reliably beneficial.

3. **TFENN baseline numbers are quoted from the original paper, not re-implemented.** The stress-strain experiment (Table 1) compares against TFENN (Garanger et al., 2024) using values reported in that paper. The paper is transparent about this ("The TFENN errors are the results reported in Garanger et al. (2024)"), but training conditions (dataset splits, optimization details) may differ. Combined with the fact that the MLP augmented baseline uses only 4 random rotations (which is unlikely to approximate equivariance well), the empirical advantage over the strongest baselines in this experiment is less conclusively established than in the sparse vector experiment.

4. **Data augmentation baselines are weak.** Both the stress-strain and path signature experiments use MLP baselines trained on datasets augmented with only 4 random transformations. This is unlikely to provide a competitive approximation to equivariance; a stronger baseline (e.g., 20–50 transformations, or group averaging with many samples) would be needed to fairly compare against data augmentation strategies. The paper states the numbers transparently, but the weakness of this baseline inflates the apparent gap between equivariant and non-equivariant methods.

### Trivial

- In Table 2, the "Ours" entries for O(d) and Lorentz report values like 0.002 and 0.005 without standard deviations, while other entries include them. The caption states this is because std < 1e-3, which follows the stated convention, but it would be cleaner to include all standard deviations (e.g., using scientific notation).

## Nice-to-Haves

- A brief analysis of why the full model underperforms the diagonal variant in certain sparse-vector settings (e.g., does the Gram matrix input cause optimization difficulty? Could regularization or architectural changes help?).
- A discussion section acknowledging limitations: computational cost scaling with output rank and number of input vectors, reliance on synthetic data, and the absence of comparisons with other equivariant tensor architectures for O(d).

## Removed Points

These points from the input reviews were removed or demoted because they are factually incorrect, speculative, nitpicks, or scope-creep:

- *Claim that TFENN dataset sizes "may not match" original experiments* — **Removed.** The paper explicitly states it uses "the TFENN Garanger et al. (2024) dataset," making the data source clear.
- *Claim that missing standard deviation in Table 2 is an omission* — **Removed.** The paper specifies a convention (std reported when ≥ 1e-3), and follows it; this is a formatting choice, not an error.
- *Several "Strengths" from the Strength Finder that were generic or sycophantic* — **Removed.** E.g., "novel combination of path signatures with equivariant tensor learning" is kept; generic strengths about "addressing an important problem" are dropped.
- *Criticism about missing appendix content, proofs, or references* — **Removed per instructions:** the parser strips these sections; they exist in the original submission.
- *"Could the metric be measuring a proxy?"* — **Removed.** Speculative, no concrete anchor in the paper.

## Novel Insights

The only genuinely novel observation that emerges across the reviews beyond the paper's own contributions is the systematic failure-case pattern in Table 3: the full Gram-matrix-based model underperforms the simpler norm-only variant precisely in the regimes where SoS also struggles (identity or diagonal covariance). This suggests the full model's expressivity may be a liability when training data is limited or the signal structure is simple — a phenomenon worth investigating but not addressed in the paper.

## Suggestions

1. Add a comparison with e3nn (or escnn) on the O(d) path signature problem to directly test whether the proposed parameterization offers accuracy or efficiency advantages over an existing, widely-used equivariant architecture.
2. Investigate and discuss the full vs. diagonal model inconsistency in the sparse vector experiments — at minimum, report training curves and regularization sensitivity to explain when the full model is beneficial.
3. Increase the number of data augmentation transformations for the MLP augmented baselines (to at least 20–50) to provide a fairer data-augmentation comparison.
4. In Table 2, report standard deviations for all entries (using scientific notation for small values) for completeness.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>