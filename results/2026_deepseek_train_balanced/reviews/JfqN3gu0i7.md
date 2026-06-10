## Summary

This paper studies the classification excess risk of kernel classifiers (spectral algorithms) when the Bayes classifier lies in an interpolation space [ℋ]^s of an RKHS. Its central contribution is establishing the minimax optimal rate n^{-sβ/(2sβ+1)} for Sobolev RKHS binary classification, proved via a matching lower bound (Theorem 3.1, novel for Sobolev RKHS in general dimension d>1) and an upper bound (Theorem 3.2). The paper also extends the upper bound to overparameterized neural network classifiers via NTK approximation and proposes a heuristic "Truncation Estimation" method for the smoothness parameter s with experiments on synthetic and real data.

## Strengths

- **Novel minimax lower bound for Sobolev RKHS classification in arbitrary dimension (Theorem 3.1).** Prior minimax results for Besov spaces were restricted to d=1; this paper extends the lower bound to Sobolev RKHS for d>1, filling a genuine gap in the classification theory literature.
- **Matching upper bound confirming optimality (Theorem 3.2).** The rate n^{-sβ/(2sβ+1)} matches the lower bound up to a logarithmic factor. By choosing ν ≍ n^{β/(sβ+1)}, gradient-flow kernel classifiers are shown to be minimax rate optimal for Sobolev spaces. The analysis builds cleanly on existing spectral algorithm and interpolation space machinery.
- **Connection to overparameterized neural networks (Corollary 4.1).** The extension via NTK approximation is technically valid and bridges kernel theory with deep learning, even if it relies substantially on prior results.
- **Smoothness estimates on real datasets align with difficulty ordering.** Estimated s values from the Truncation Estimation method (~0.49 for MNIST, ~0.44 for Fashion-MNIST, ~0.20 for CIFAR-10) are consistent with the known relative difficulty of these datasets, providing some empirical plausibility.

## Weaknesses

### Major

1. **Unusual δ-dependence in the lower bound (Theorem 3.1).** The bound is stated as C·δ·n^{-sβ/(2sβ+1)} with probability at least 1-δ. Standard minimax lower bounds have constants independent of δ (or at worst depending on log(1/δ)). The linear δ factor means the bound shrinks by an order of magnitude when demanding higher confidence (e.g., δ=0.01 vs δ=0.1), making it qualitatively weak at typical confidence levels. This is not a proof-in-appendix issue — the δ dependence is stated explicitly in the theorem. The authors must clarify whether this is a typographical artifact (intended to be an absolute constant) or a genuine consequence of the proof. If real, it would mean the lower bound rate only holds with a constant that degrades with confidence, which is non-standard and undermines the claimed optimality.

2. **The practical smoothness estimation method does not fulfill its stated purpose.** The paper motivates the Truncation Estimation method as making the theory "more applicable in realistic settings" (abstract). However, the upper bound requires choosing ν ≍ n^{β/(sβ+1)}, which depends on the unknown s. The paper never demonstrates that using the estimated ŝ to select ν yields near-optimal classification performance — neither theoretically nor empirically. Absent this step, the method serves a different purpose (assessing relative dataset difficulty) than the stated one. Additionally: (a) the truncation point (always 100) is chosen with no justification or sensitivity analysis, (b) the method has no theoretical guarantees (no consistency, no rates), and (c) the synthetic validation is limited to a single 1D setting (min kernel on [0,1]).

3. **Unsubstantiated claim about applicability to non-Sobolev kernels.** The paper claims (lines 46, 276) that Theorem 3.2 applies to "any general RKHS with an embedding index α₀=1/β, such as an RKHS with a shift-invariant periodic kernel and an RKHS with a dot-product kernel." No proof or citation is provided that these kernel families satisfy α₀=1/β. The verification for the Sobolev RKHS itself is confined to a commented-out TeX block (lines 234–241). If these claims cannot be substantiated, the claimed generality of the upper bound is unsupported, and the paper should be scoped to Sobolev RKHS.

### Minor

4. **Neural network section (Section 4) is thin.** The section applies existing results (Li et al., 2023; Haas et al., 2023) to derive Corollary 4.1, but contributes no new experiments, no discussion of practical feasibility (the required width grows polynomially in n, λ_min^{-1}, etc., which could be astronomically large), and no substantive analysis beyond the corollary statement. This does not diminish the core theory, but it adds little as a standalone contribution.

5. **The δ-dependence asymmetry between bounds.** The upper bound has standard log(1/δ) dependence (C·ln(4/δ)), while the lower bound has linear δ dependence. These are not symmetric, which is odd for a claimed optimality result. If the lower bound's δ issue is resolved, this mismatch should also be addressed.

6. **Synthetic validation of Truncation Estimation is restricted to 1D.** While the paper does include a synthetic experiment (Figures 1, 2, known s=0.5), it uses only the min kernel on [0,1] in one dimension. No higher-dimensional test with known ground-truth s is presented.

### Trivial

- None.

## Nice-to-Haves

- An experiment validating the predicted convergence rate n^{-sβ/(2sβ+1)} directly on synthetic data with known s and β (rather than just estimating s) would more directly support the theory.
- A brief discussion of why the Tsybakov noise condition is not used (the commented-out Assumption 4) and how its inclusion would affect the rates would help readers situate the results.
- Clarifying the relationship between squared-loss excess risk and 0-1 excess risk for classification would improve readability.

## Removed Points

These points are flagged to be removed; treat them with caution:

- "No synthetic experiment with known s is run" [Harsh Critic]: The paper DOES contain a synthetic experiment (min kernel, cos(2πx), s=0.5, Figures 1–2). The criticism is factually wrong.
- "Claim in contribution (ii) is potentially misleading — Audibert and Tsybakov (2007) gave lower bounds for Hölder classes": The paper discusses Besov spaces, not Hölder classes. Cannot verify without external sources. Removed.
- "Commented-out blocks should be removed": Formatting/presentation nitpick. Removed.
- Various style, formatting, and typo criticisms (parser artifacts). Removed.

## Novel Insights

The most noteworthy observation emerging from the reviews is the structural asymmetry between the δ-dependence in the lower bound (linear) and upper bound (logarithmic). If the lower bound's δ-dependence is genuine, this would be a significant technical weakness — it would mean the lower bound is provably loose for small δ, and the claimed optimality would only hold in a weak sense (comparing a log(1/δ) upper bound against a δ lower bound). If it is a typo, the paper would benefit from correcting it. Either way, this asymmetry is a concrete point the authors must address in any revision.

Additionally, the Truncation Estimation method, despite its limitations, highlights a genuinely under-explored direction: the estimation of the interpolation smoothness parameter s that appears in misspecified kernel regression/classification rates. Even a heuristic first step in this direction is notable, but the paper would benefit from clearly separating this speculative component from the core theoretical contribution.

## Suggestions

1. **Clarify or correct the δ-dependence in Theorem 3.1.** This is the single most important issue. If δ-independent, state it as such. If linear δ is necessary, explain why and discuss implications for the claimed optimality.
2. **Substantiate the embedding index claims for non-Sobolev kernels with proofs or references, or remove those claims.** The core contribution stands on Sobolev RKHS alone.
3. **Either remove the Truncation Estimation method or reframe it honestly as a heuristic for assessing relative dataset difficulty** (not as a tool to make the theory "more applicable"). If kept, provide at minimum a sensitivity analysis for the truncation point.
4. **Either expand the neural network section with experiments/discussion or condense it to a remark in the discussion.** In its current form, it is too thin to be a meaningful contribution.

## Score and Decision

The paper's core theoretical contribution — establishing minimax optimal rates for Sobolev RKHS classification — addresses a genuine gap in the literature. The matching upper and lower bounds, if technically sound, would be a solid contribution. However, the unusual δ-dependence in the lower bound raises a red flag that must be resolved before the results can be assessed as fully correct. Additionally, the paper overreaches in its claims about practical applicability and generality to other kernel classes. These issues do not necessarily invalidate the core theory, but they mean the paper in its current form makes stronger claims than it supports.

Given the unresolved question about the lower bound's validity and the overclaims, this is a borderline paper that would benefit from major revision focused on the theoretical core.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>