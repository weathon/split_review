- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6
I have read the paper carefully. Let me now produce the consolidated review.

---

## Summary

This paper introduces a new structural assumption on Gaussian kernel matrices—that their ℓ₁ norm grows linearly in n rather than quadratically—and presents a subquadratic-time algorithm for approximate kernel matrix–vector multiplication under this assumption. The algorithm is the first to work for unrestricted input vectors (allowing negative entries), overcoming the non‑negativity restriction of prior work (Backurs et al., 2021). The authors validate the assumption empirically on BERT attention matrices derived from SQuAD, and claim additional experiments on RoBERTa and GPT. The theoretical runtime is Õ(d n^{1.89}/ε²).

## Strengths

1. **Removal of the non‑negativity restriction on input vectors.** The paper achieves subquadratic time for kernel matrix–vector multiplication with *unrestricted* vectors, under Assumption A. Prior work (Backurs et al., 2021) required non‑negative vectors and used the error guarantee ∥Kx−y∥₂ ≤ ε∥Kx∥₂, which can be zero when x lies in the nullspace of K. The new guarantee ∥Kx−y∥₂ ≤ ε∥x∥₂ eliminates this limitation (Section 1.2). This is a genuine theoretical advance.

2. **Provable subquadratic runtime for general vectors under an empirically motivated assumption.** Theorem 1.1 states a runtime of Õ(d n^{1.89}/ε²), which is o(n²) for fixed d, ε. The algorithm combines heavy‑key recovery via LSH and light‑key estimation via KDE‑based variance control (Lemmas 3.4, 3.5). The analysis is non‑trivial and the proof structure (Section 3) is clearly laid out.

3. **Empirical validation of the ℓ₁‑based assumption (Assumption A) on real transformer attention matrices.** Figure 1 shows that for all 12 layers and 12 heads of BERT on SQuAD, the maximum ratio (∥K∥₁ − sum of top n entries) / (sum of top n entries) is bounded by 4.6, directly supporting the claim that ∥K∥₁ = O(n). Experiment (ii) further shows that a stronger uniform‑bound assumption fails (the n‑th and (n+1)‑th largest entries are nearly equal), motivating the paper's ℓ₁‑based approach over the ℓ∞‑based one in Han et al. (2023).

4. **Improved reduction from attention matrices to Gaussian kernel matrices (Lemma 4.1).** The reduction is independent of the vector x and yields better precision guarantees than that of Zandieh et al. (2023), needing to be performed only once per matrix rather than once per matrix–vector pair.

## Weaknesses

### Fatal
None.

### Major

1. **Empirical validation of the assumption is narrow in scope.** The main experiments use only BERT base (uncased) on the SQuAD dataset with context length at most 512. The paper states "We also present additional experimental evaluation on other models RoBERTa and GPT" (Section 4) but provides **no results** for these models—no figures, tables, or discussion. For a paper whose practical relevance depends on the assumption holding across diverse transformer architectures and longer contexts (modern LLMs use 2k–128k token contexts), this significantly weakens the evidence. The reader cannot assess whether the assumption generalizes beyond one model, one dataset, and 512‑token sequences.

2. **The comparison with prior work is incomplete and somewhat one‑sided.** The paper argues that its algorithm improves over Backurs et al. (2021) on a specific pathological example (one row of all ones, others zero). While this example *does* satisfy Assumption A (contrary to a reviewer claim—the matrix has ℓ₁ norm = n, which is O(n)), it is a corner case rather than a systematic comparison. Backurs et al. has a better asymptotic exponent (n^{1.173} vs. n^{1.89}) on matrices that satisfy both settings. The paper does not characterize the regimes (n, ε, matrix structure) where one algorithm dominates the other, leaving the reader unsure when the new algorithm is genuinely superior.

### Minor

1. **The algorithm is not implemented or tested.** While this is a theory‑first paper and an implementation is not required for the theoretical contribution to be valid, the title and framing ("Improved Algorithms") create an expectation of practical relevance that would be strengthened by even a small‑scale experimental evaluation (e.g., runtime vs. exact multiplication on the same BERT‑derived matrices used in Section 4). The absence of any empirical validation of the algorithm itself limits the assessment of its practical constant factors and real‑world behavior.

2. **The optimal parameter choices (γ=0.109, α=1/3) are stated without justification or sensitivity analysis.** The proof states these are chosen "to balance the exponents," but no explanation is given for how these precise values are derived or whether the runtime is sensitive to small deviations. A brief note on the optimization landscape would improve reproducibility of the theoretical claims.

3. **The runtime bound Õ(d n^{1.89}/ε²) uses Õ to suppress polylog(n) factors, but the 1.89 exponent already incorporates o(1) terms from LSH (ρ=0.173).** It is unclear whether the remaining Õ hides additional n^o(1) factors or only polylogarithmic ones. Clarification would aid comparison with prior work.

### Trivial
None.

## Nice-to-Haves
- Expanding the empirical validation to at least one other architecture (e.g., RoBERTa or GPT‑2), longer sequences (e.g., from Longformer), and reporting distributions (e.g., per‑layer/head histograms) rather than just a single maximum ratio.
- A direct runtime comparison (even simulated) between the proposed algorithm and naive multiplication on the matrices used in Section 4, to estimate hidden constant factors.
- A systematic theoretical comparison characterizing when the new algorithm's error guarantee outweighs the worse exponent relative to Backurs et al.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Criticism that the worst‑case matrix (one row of all ones) violates Assumption A.** This is factually incorrect. The matrix has ℓ₁ norm = n (one row of n ones), which is O(n). It satisfies Assumption A with c=0. The corresponding argument about rescaling ε in Backurs et al. is valid for this example, and the comparison is not invalidated on these grounds.
- **Criticism that "no experimental evaluation of the algorithm" is a fatal / fundamental omission.** For a theory‑first paper that provides provable guarantees, the lack of implementation is a limitation but not a fatal flaw. The paper's primary contribution is theoretical (removing the non‑negativity restriction under a new assumption). The criticism has been retained as a Minor weakness for its practical relevance dimension.
- **Formatting nitpicks about missing pseudocode images and garbled text.** These are parser artifacts, not author errors.
- **Criticism that the "first subquadratic" claim needs qualification.** The abstract clearly states "Under this assumption, we obtain the first subquadratic time algorithm," which already qualifies the claim.

## Novel Insights
The most interesting observation from the reviews is the tension between the paper's two contributions: the algorithm (theoretical, unverified) and the assumption (empirically validated on limited data). The reviews highlight that a stronger bridge between them—either implementing the algorithm on the same matrices used for validation, or proving a tighter connection between the assumption and the algorithmic building blocks—would substantially elevate the paper's impact. The finding that a uniform‑bound assumption fails (Section 4, Experiment ii) while an ℓ₁‑based assumption holds is a genuinely useful characterization that future work on attention approximation could build on, regardless of whether this specific algorithm is ever implemented.

## Suggestions
1. Include the claimed RoBERTa and GPT experiments, even as a brief appendix figure. This would directly address the most impactful weakness.
2. Add a sentence clarifying whether the Õ notation hides n^o(1) factors or only polylog(n), and briefly describe how γ=0.109 and α=1/3 are derived.
3. Consider adding a small‑scale implementation of the algorithm (or a simplified variant) on n=256–512 matrices from the same BERT experiments, comparing approximate Kx against exact Kx to demonstrate that the theoretical guarantees translate to practice.
4. Reframe Section 1.2's comparison with Backurs et al. to more clearly delineate the regimes (matrix structure, n, ε) where each algorithm is preferred, rather than relying primarily on a single corner case.
