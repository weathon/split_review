## Summary

This paper proposes the Orthogonal Neural Operator (ONO), which replaces standard kernel integral operators in neural operators with an "orthogonal attention" mechanism derived from Mercer's theorem. The core idea is to parameterize orthonormal eigenfunctions via neural networks and use them to construct an attention-like operator (without softmax) with an explicit orthogonalization regularizer implemented via EMA-based covariance estimation and Cholesky decomposition. Experiments on six PDE benchmarks show competitive results, with strongest performance on Airfoil, Pipe, and NS2d.

## Strengths

- **Principled derivation from Mercer's theorem to attention without softmax (Section 3.3, Equations 7–14).** The paper provides a clean theoretical path: start from a kernel integral operator, expand via Mercer's theorem, truncate to k eigenfunctions, parameterize them with NNs, enforce orthonormality, and arrive at an attention matrix of the form $\hat{\bm{\psi}}' \mathrm{diag}(\hat{\boldsymbol{\mu}}) \hat{\bm{\psi}}^\top$. This derivation distinguishes the work from prior attention-based neural operators that introduce attention heuristically.

- **Controlled ablation isolates the orthogonalization benefit (Figure 1, Elasticity limited-data experiment).** ONO (with orthogonalization) degrades only 58% (0.0114 → 0.0181) when training data drops from 1200 to 400, while ONO$^{-}$ (same architecture, no orthogonalization) degrades 97% (0.0352 → 0.0694). This directly supports the paper's central claim that orthogonalization provides a regularization benefit under data scarcity.

- **Orthogonalization consistently outperforms BN and LN as the attention normalization (Table V).** On Airfoil (0.0056 vs 0.0808/0.0288), Pipe (0.0034 vs 0.2151/0.0056), and Elasticity (0.0118 vs 0.0149/0.0387), the orthogonalization choice dominates, showing it provides more than just scale normalization.

- **Scalability to 30 layers (10M parameters) without degradation (Table VII).** ONO-30 reduces error by 37% on Elasticity and 76% on Plasticity compared to ONO-8, demonstrating that the orthogonal attention does not saturate or destabilize with depth — a nontrivial property for attention-based neural operators.

## Weaknesses

### Major

- **Generalization experiments compare only against FNO, which inflates the headline claims.** The zero-shot super-resolution results (Table III) and temporal generalization results (Table IV) compare ONO *only* against FNO. FNO is well-known to struggle with resolution change (its own error jumps from 0.1164 to 0.3631 on Darcy), making the reported 80–89% error reduction less informative. The paper's justification (line 484: "due to its well-acknowledged mesh-invariant property") is weak — other attention-based operators (LSM, GNOT) are also mesh-invariant and would provide far more meaningful comparisons. The paper itself calls LSM and GNOT "the latest SOTA neural operators" (line 317) yet omits them from exactly the experiments that support the paper's strongest claims.

- **No variance or statistical significance reporting anywhere.** Every table reports a single number per method with no standard deviations, confidence intervals, or mention of random seeds or multiple runs. Several claimed wins are small (ONO's 0.1195 vs F-FNO's 0.1213 on NS2d is a 1.5% difference; ONO's 0.0072 vs LSM's 0.0069 on Darcy is a 4.3% *loss*). Without error bars, the reader cannot determine whether any of the fine-grained comparisons are meaningful, and the paper's "SOTA on three benchmarks" claim rests on these unassessed margins. This is a structural weakness that cuts across the entire experimental section.

### Minor

- **FNO and Geo-FNO report identical numbers on two benchmarks without explanation.** On both NS2d (0.1556) and Darcy (0.0108), FNO and Geo-FNO report identical errors. If Geo-FNO reduces to FNO on regular-grid benchmarks (because its learned mapping becomes identity), this should be stated explicitly. The identical numbers with no comment will reasonably raise reader suspicion.

- **Underperformance on Elasticity and Plasticity is inadequately analyzed.** ONO loses to GNOT on Elasticity (0.0118 vs 0.0086, a 27% gap) and to U-FNO on Plasticity (0.0048 vs 0.0028, a 41.7% gap). The paper calls Elasticity "second-lowest... with a slight margin" and Plasticity "competitive," but the Plasticity gap is nearly double the error of the best method. No analysis is given for *why* ONO underperforms on these benchmarks or what this reveals about the method's limitations.

- **Novelty framing could be clearer.** The orthogonalization procedure (EMA covariance + Cholesky decomposition) is inherited directly from the neural eigenfunction literature (deng2022neuralef, deng2022neural), which the paper cites but does not clearly delineate what is inherited versus novel. The genuinely new contributions — applying this framework as a kernel integral operator in a neural operator, and the two-flow architecture — would benefit from being explicitly separated from inherited components.

- **No limitations discussion.** The paper does not discuss when ONO might fail, what types of PDE problems it is ill-suited for, or what the failure modes of the orthogonalization might be (e.g., when mini-batches are too small for reliable covariance estimation, or when the EMA estimate lags behind the current feature distribution).

### Trivial

- The paper states ONO has "comparable computational cost to the linear Galerkin Transformer" (line 418), but ONO at 7.87s/training-step is actually *faster* than Galerkin at 9.88s (Table II). This is a minor wording issue.

## Nice-to-Haves

- Include at least one strong attention-based baseline (LSM or GNOT) in the zero-shot super-resolution and temporal generalization experiments to substantiate the headline claims.
- Include an "Ortho + LN" condition in Table V to test whether orthogonalization and layer normalization are complementary.
- Analyze the learned eigenfunctions (visualize them, show spectral decay) to connect the architectural design back to the Mercer motivation.

## Removed Points

These points from the inputs were removed after verification against the paper:

- **Harsh critic's claim that "The Mercer expansion is therefore a motivation for the architecture, not a guarantee about its behavior"** — The paper frames Section 3.3 as "Theoretical Insights," not as a formal guarantee. This is accurate as written; the criticism attributes a claim the paper does not make. **Removed (strawman).**

- **Harsh critic's "selectively favorable baseline comparisons" in the main results table** — The paper includes seven baselines across six benchmarks. The selection is standard and competitive. The critic's specific complaint about the limited-data experiment omitting LSM/GNOT is addressed above in the generalization experiments weakness; the main table is not the issue. **Reduced to a focused point on generalization experiments only.**

- **Harsh critic's claim about "Galerkin performs competitively on Darcy (0.0084 vs ONO's 0.0072) — closer than the paper suggests"** — The paper states ONO achieves "second-lowest prediction error" on Darcy, which is accurate. The critic's characterization is subjective. **Removed.**

- **Strength Finder's Strength 2 ("far beyond prior mesh-invariant operators")** — The zero-shot experiments only compare against FNO. "Far beyond prior mesh-invariant operators" is an overstatement not supported by the evaluation. **Rephrased in main strengths to reflect the FNO-only comparison.**

- **Strength Finder's Strength 5 characterization** — The critic's criticism of Table V (orthogonalization vs BN/LN serving different mathematical roles) has some merit; the comparison is not apples-to-apples but still informative. **Strength kept but tempered in phrasing.**

- **Harsh critic's "No code release or reproducibility statement"** — The absence of a code release statement is noted but the hard rules remove reproducibility nitpicks about code release. **Moved here.**

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface novel connections or implications that the paper itself does not already articulate.

## Suggestions

1. **Add variance reporting.** Run all experiments with at least 3 random seeds and report means ± standard deviations. This is essential for ICLR-level claims, especially where margins are small.
2. **Add at least one attention-based baseline (LSM or GNOT) to the zero-shot super-resolution and temporal generalization experiments.** Without this, the 80–89% error reduction claims rest on a single, weakly-performing comparator.
3. **Explain the FNO/Geo-FNO identical numbers** (or, if they are carried over from a reference, note the source explicitly).
4. **Add a limitations paragraph** that discusses when ONO underperforms (e.g., Elasticity, Plasticity) and when the EMA-based covariance estimation might struggle.
5. **Include an "Ortho + LN" ablation** to test whether the two normalizations are complementary.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>