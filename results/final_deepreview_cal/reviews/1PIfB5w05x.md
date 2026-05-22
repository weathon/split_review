Now I have sufficient calibration anchors. Let me synthesize the final review.

**Round 1 Bracket**: Based on the initial bracketing, the paper sits between the middle-band anchors (3.5-7.5) and is clearly above the weak band (avg 1.67-3.33). The strong band anchors (avg 8.0) are clearly above this paper. **Initial bracket: ~5.5 to ~7.5.**

**Round 2 Narrowing**: Looking at anchors specific to sparsity/LASSO theory:
- Lasso Bandit (6.33): accepted, but had presentation issues and some reviewers questioned the practical verifiability of conditions. Our paper is cleaner.
- In-Context Sparse Recovery (7.00): accepted, had strong theory+experiments but some reviewers raised concerns about fairness of comparisons and theory-practice gaps.
- Sparsistency for iOT (6.75): accepted, similar purely-theoretical contribution style, though heavier notation.

Our paper is cleaner and more focused than the Lasso Bandit paper, and its contributions are more self-contained than the iOT paper. The main limiting factor is that the agnostic Price of Quality bound comes from a sufficient condition (acknowledged but a presentation risk) and the absence of simulations. **Final score: 6.5.**

Now let me write the consolidated review.

Let me think about the weaknesses carefully and filter them:

1. **Price of Quality bound is from a sufficient condition** - This is valid. The paper is transparent about it in Remark 3.2, but the headline phrasing could be misinterpreted. This is a **Minor** weakness since the paper is honest about the limitation but the presentation could be clearer.

2. **LASSO proof sketch is brief** - Valid observation. The full proof is in the appendix. The main text gives a one-paragraph sketch mentioning QR decomposition + Haar measure but doesn't explain why this approach works. This is **Minor** to **Nice-to-Have** since the full proof exists in the appendix.

3. **No experiments/simulations** - The critic acknowledges this is not required for a theory paper. This is a **Nice-to-Have**.

4. **No necessary conditions for information-theoretic recovery** - The paper acknowledges this. This is a **Minor** limitation.

5. **Role of δ not discussed** - Very minor point. **Trivial**.

6. **Remark 3.4 about generalizations is brief/sketch** - Valid observation. **Trivial** to **Minor**.

Now let me also check the Strength Finder's claims:

1. "Explicit sufficient conditions for support recovery with heterogeneous noise" - Valid. Theorems 1 and 2 give concrete inequalities.
2. "Definition and analysis of the Price of Quality" - Valid. Introduced clearly.
3. "LASSO threshold depends only on total sample size and average noise" - Valid. Theorem 3.
4. "Transparent handling of limitations" - Valid. Remark 3.2.
5. "Non-trivial technical extension for LASSO" - Valid. Uses QR decomposition + Haar measure.
6. "Explicit condition on noise scaling (Proposition 4.1)" - Valid.
7. "Generalization to arbitrary noise structures" - Valid but brief. Should note this is more of a sketch.

Now let me check which weaknesses from the harsh critic to keep or remove:

**Keep:**
- Price of Quality bound presentation (Minor)
- LASSO proof sketch brevity (Minor)
- No necessary conditions for info-theoretic recovery (Minor, paper acknowledges this)

**Remove / Move to Nice-to-Have:**
- No experiments/simulations → Nice-to-Have (critic acknowledges not required)
- Role of δ → Trivial

**Remove (factually not a problem):**
- The critic says "One minor concern: Theorem 1 requires δ ∈ (0,1) as an error tolerance, but the condition (9) involves δ in the log terms. For fixed δ < 1, the condition scales with s log(p/s), which is the usual threshold. This is fine, but the role of δ is not discussed further." - This is acknowledged as "not a flaw, but a detail that would strengthen." Move to Trivial.

Now for the "Removed Points" section, let me think about what I'm actually removing.

Actually, per the instructions: "REMOVE means moved it to a new section called Removed Points, do not completely remove them from the review"

So I need to create a Removed Points section for things I remove.

Let me also check: "If two reviewers raise the same concern in different framings, merge them; do not let duplication inflate the weakness count." - The harsh critic and strength finder don't really have overlapping concerns.

Let me finalize my review now.Now I have all the information needed. Let me write the consolidated review.

## Summary
This paper studies sparse support recovery in a high-dimensional linear model where observations come from two sources: a small number of high-quality (low-noise) measurements and a larger number of low-quality (high-noise) measurements. It provides sufficient conditions for information-theoretic recovery in both an agnostic setting (decoder does not know per-sample noise levels) and an informed setting (decoder knows the variances), introducing the *Price of Quality* — the number of low-quality samples needed to replace one high-quality sample under those sufficient conditions. On the algorithmic side, it extends the classical LASSO phase transition (Wainwright, 2009) to the heterogeneous-noise agnostic setting, showing that the LASSO threshold depends only on the average noise level and total sample size, revealing a striking robustness of computational recovery to data heterogeneity.

## Strengths
- **First sufficient conditions for sparse support recovery with heterogeneous noise.** Theorems 1 and 2 provide concrete, interpretable inequalities (equations 9 and 16) characterizing when mixed-quality data are jointly sufficient for information-theoretic recovery. These are the first results of their kind for this problem and directly support the paper's central claimed contribution.
- **Price of Quality framework.** The paper introduces a clean conceptual tool (equation 5) that quantifies the trade-off between high- and low-quality data, and analyzes its behavior across three SNR regimes in both agnostic and informed settings. This provides a useful vocabulary for discussing data-quality trade-offs in sparse recovery.
- **LASSO phase transition extended to heterogeneous noise (Theorem 3).** The paper shows that in the agnostic setting, the LASSO's recovery threshold depends only on total sample size \(n\) and the average noise variance \(\sigma_{\text{avg}}^2\) — not on the individual noise levels. This is a non-trivial extension of Wainwright (2009) that requires overcoming the loss of isotropic structure via a QR decomposition and Haar measure argument. Proposition 4.1 further provides explicit necessary and sufficient conditions on noise scaling. This is the paper's strongest technical contribution.
- **Transparent handling of limitations.** Remark 3.2 explicitly discusses the looseness of the Chernoff-bound relaxation used in Theorem 1, the cubic equation whose exact solution would yield a tighter condition, and alternative estimators the decoder could use. The paper is honest about what it does and does not prove.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Agnostic Price of Quality bound (\(\gamma < 2\)) is a property of the sufficient condition, not a proven fundamental limit.** The paper is transparent about this in Remark 3.2, and the abstract and conclusion do include qualifiers ("for this sufficient condition to hold", "under our sufficient condition"). However, the headline claim — "one high-quality sample is never worth more than two low-quality samples" — is the paper's most attention-grabbing statement, and a casual reader could come away thinking it is a proven information-theoretic limit rather than an artifact of a specific bounding technique. A reader who reads carefully will see the qualifiers, but the phrasing in the conclusion's first mention of the bound does not include the qualifier. This does not invalidate the contribution — the sufficient condition and its trade-off are legitimate mathematical objects — but the presentation risk is real and should be addressed.
- **LASSO proof sketch is too brief to assess the key technical step.** The main text states that the classical proof's failure due to \(\Sigma\) not being a scalar multiple of the identity is overcome by a QR decomposition of \(X_S\) and analysis via Haar measure on the orthogonal group. This is described in a single sentence. While the full proof is in the appendix, the main text would benefit from a short high-level explanation of *why* the QR decomposition + Haar measure resolves the difficulty — e.g., which property of the Haar distribution is used (invariance under rotation, concentration of the max of sub-Gaussian coordinates, etc.). The sketch currently states what is done but not why it works.
- **No necessary conditions for information-theoretic recovery.** The sufficient conditions in Theorems 1 and 2 are not matched by necessity results. The paper acknowledges this (Remark 3.3 and the conclusion), but it leaves open the question of how far the sufficient conditions are from the true threshold. For the informed setting (Theorem 2), the paper notes that the Chernoff exponent is optimized exactly (unlike the agnostic case), which suggests the condition may be tight, but no proof or explicit conjecture is given.

### Trivial
- **Role of \(\delta\) undiscussed.** The error tolerance \(\delta \in (0,1)\) appears in the log terms of the sufficient conditions (9) and (16), but its asymptotic effect — e.g., how small \(\delta\) can be before the condition becomes vacuous — is not discussed. A brief comment would help.

## Nice-to-Haves
- **Simulations illustrating the phase transitions.** This is a theory paper and does not require experiments. However, even simple simulations showing the sharpness (or looseness) of the sufficient conditions, or illustrating the LASSO phase transition with heterogeneous noise, would substantially strengthen the paper. Given the paper's honest acknowledgment that the agnostic condition is not tight, simulations could be particularly illuminating.
- **A more informative discussion of Remark 3.4 (generalizations).** The extension to general invertible \(\Sigma\) is interesting but very brief — essentially just writing down equation (22). A discussion of when this generalization might be loose or tight, or an example where it applies, would be helpful.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Criticism about missing experiments.** Removed because the critic acknowledges this is not required for a theory paper. Moved to Nice-to-Haves.
- **Criticism about insufficient discussion of \(\delta\).** Removed from main weaknesses. This is a very minor presentational detail; moved to Trivial.
- **Strength Finder's claim about "generalization to arbitrary noise structures" as a core strength.** This is a brief remark (Remark 3.4) that sketches an extension without fully analyzing it. It is a supporting observation, not a core strength of the paper. Moved from core strengths to incidental observation.

## Novel Insights
None beyond the paper's own contributions. The synthesis of the two reviewers' inputs does not produce an insight about the paper that the paper itself does not already articulate.

## Suggestions
- Revise the abstract and conclusion so that every mention of the agnostic Price of Quality bound is unambiguously qualified as a property of the *sufficient condition*, not a problem-level bound. The current qualifiers ("under our sufficient condition", "for this sufficient condition to hold") are present but could be made more prominent and consistent — particularly in the conclusion's first sentence about the bound.
- Add 3–5 sentences to the LASSO proof sketch explaining *why* the QR decomposition + Haar measure approach resolves the key difficulty created by the non-scalar \(\Sigma\). Even stating which concentration property of the Haar distribution is used would substantially improve readability.
- Consider adding a brief conjecture about the tightness of the informed sufficient condition (Theorem 2), since the Chernoff exponent is optimized exactly there.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| ZDoaLbOFaP (Sparse Covariance NNs) | 3.00 | R1 (low) | Well below this paper |
| sIcPMMhl9W (Shuffled Regression) | 5.80 | R1 (mid) | Below; had non-rigorous approximations and clarity issues that this paper does not share |
| qZwtPEw2qN (Ambient Diffusion) | 6.80 | R1 (mid) | Comparable; had strong empirical validation which this paper lacks, but this paper's theory is cleaner |
| wpXGPCBOTX (Sparsistency for iOT) | 6.75 | R2 (mid) | Comparable theoretical paper; similar in scope and rigor, but this paper is better organized |
| f3jySJpEFT (Lasso Bandit) | 6.33 | R2 (mid) | Below; had presentation issues and concerns about condition verifiability |
| NHhjczmJjo (In-Context Sparse Recovery) | 7.00 | R2 (mid) | Slightly above; had experiments and broader appeal, but faced concerns about theory-practice gaps |

**Round 1 bracket:** ~5.5 to ~7.5. **Round 2 narrowing:** The paper is stronger than the Lasso Bandit paper (6.33) and the Shuffled Regression paper (5.80), and comparable to the Sparsistency for iOT paper (6.75) and Ambient Diffusion paper (6.80). It sits slightly below the In-Context Sparse Recovery paper (7.00) primarily because that paper included experiments. **Final score: 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>