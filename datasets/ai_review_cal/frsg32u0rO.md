- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes Block Verification, a modified draft-verification algorithm for speculative decoding that jointly considers the entire block of draft tokens rather than verifying token-by-token. The authors prove that block verification (1) preserves the output distribution of the target model (Theorem 1), (2) achieves optimal expected number of decoded tokens over a fixed number of iterations among all valid verification algorithms (Theorem 2), and (3) strictly dominates the standard token verification algorithm. Empirically, it yields consistent 5–8% wall-clock speedups across 8 datasets using PALM-2 models, with essentially zero additional code complexity.

## Strengths

- **Theoretical optimality proof (Theorem 2).** The paper proves that block verification maximizes the expected number of decoded tokens in a fixed number of iterations among all valid draft verification algorithms — a stronger guarantee than any prior work, all of which use the standard token verification shown here to be suboptimal.

- **Clear, fully-worked motivating example (Lemma 1).** The 2-token example in Section 2 concretely contrasts token verification (10/9 expected accepted tokens), block verification (11/9), and the ideal full-information algorithm (12/9), cleanly illustrating the non-optimality of token verification and the intuition behind joint verification.

- **Consistent empirical improvement across 8 datasets.** Table 1 shows that with δ=8 and PALM-2-XXS drafter, block verification improves block efficiency by 7.00–10.06% (avg 8.30%) and wall-clock speedup by 5.36–8.14% (avg 6.49%) over token verification, with improvements holding on every dataset and the standard deviations reported across 3 runs.

- **Plug-and-play simplicity.** As shown in Algorithms 1–2, block verification modifies only a few lines from the standard token verification algorithm (the `\diff`-highlighted changes). The outer speculative decoding loop (Algorithm 3) is unchanged. This makes adoption trivial for existing speculative decoding implementations.

- **Distribution preservation guarantee (Theorem 1).** Block verification provably maintains the identical output distribution to the target model — a non-negotiable requirement that is formally proved, not assumed.

- **Improvement scales with draft length and drafter quality.** Figure 1 and Table 2 show that the relative improvement increases with block length δ and is larger when using the stronger drafter (XXS vs. XXXS), confirming that block verification compounds with existing gains.

## Weaknesses

### Fatal
None.

### Major

- **Optimality claim vs. greedy block verification needs clearer exposition.** The paper states optimality (Theorem 2) among all valid verification algorithms, then notes in Section 4 that greedy block verification exists and can produce *more* accepted tokens per iteration, yet is empirically worse overall. The paper does offer an explanation (lines 287–288: greedy changes the decoding logic in a way that "affects the decoding speed in subsequent iterations"), and a key distinction is that optimality is measured over *a fixed number of iterations*, not per-iteration. However, the explanation is packed into two sentences, relies on an appendix section that is not visible here, and a reader could easily conclude the paper is contradicting itself. This is the paper's headline theoretical claim; it deserves a self-contained paragraph or a brief toy illustration in the main text explaining how a per-iteration gain can produce a net loss across iterations. The issue is one of clarity rather than correctness, but it is central enough to warrant being a major concern.

### Minor

- **Experimental evaluation uses only a single model family (PALM-2).** All experiments use PALM-2-S as target with PALM-2-XXS/XXXS as drafters. While the theory is model-agnostic and the results within this family are consistent, the paper's claim that block verification "can be used as a good default in speculative decoding implementations" would be significantly strengthened by demonstrating the same improvement on at least one additional model family (e.g., LLaMA + TinyLLaMA). Without this, the generality of the quantitative speedup figures is unconfirmed.

- **Computational overhead is asserted but not measured.** Line 284 states the overhead is "negligibly small" without providing measurements. The acceptance probability $h_i$ in Eq. 5 involves sums over the vocabulary of max expressions; while these operate on already-computed log-probabilities and should indeed be cheap relative to model forward passes, quantifying this overhead (e.g., microseconds added per iteration) would make the claim rigorous.

- **Raw wall-clock times / token-generation rates are not reported.** The paper reports only relative speedup percentages. Reporting absolute tokens/second would be more useful for practitioners evaluating the method in their own setups.

- **Only 3 random seeds for each experiment.** The reported standard deviations are small, but with only 3 seeds they may underestimate true variability. Increasing to 5+ seeds would improve reliability.

### Trivial

- The `\diff` macro used to highlight changes in Algorithm 2 (vs. Algorithm 1) makes the pseudocode harder to read in isolation; a self-contained presentation would be cleaner. The formulas for $h_i$ and the residual distribution are in Figure 1 rather than inline, which fragments the algorithmic exposition.

## Nice-to-Haves

- A brief limitations paragraph acknowledging settings where improvements may diminish (e.g., near-perfect drafter alignment with target, very large vocabularies) would improve the paper's completeness.
- Reporting the effect of block verification on the distribution of accepted block lengths (not just the expectation) could provide additional insight into why it outperforms token verification.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Proofs deferred to appendix" is a weakness.** — Removed: Deferring proofs to the appendix is standard practice at NeurIPS and similar venues. The paper provides intuition for parameter choices in the main text (Section 3), which is the expected level of detail.
- **"Missing related works"** — Removed: All cited works in the review are properly referenced; the review does not have external knowledge to verify missing citations.
- **"Algorithm exposition is dense and notation-heavy"** — Removed (downgraded to Trivial): The algorithms are presented in standard pseudocode with a clear running example; some density is expected for a technical contribution.
- **"Only 1000 prompts per dataset"** — Removed: This is a standard evaluation size for LLM inference experiments.
- **"The paper does not report the computational overhead of the summation over vocabulary"** — Removed the strong framing; kept as Minor point about measurement.

## Novel Insights

None beyond the paper's own contributions. The reviewers' insights generally reiterate or react to points already in the paper. The most useful observation from the review process is that the greedy block verification case deserves a more prominent and self-contained explanation — this is something the authors can address directly rather than a novel insight from outside.

## Suggestions

1. In Section 4, add a short paragraph or toy illustration clarifying why greedy block verification can yield more tokens per iteration yet fewer tokens over a fixed number of iterations, making the relationship between Theorem 2's optimality claim and the greedy variant fully self-contained.
2. Add experiments on at least one open-source model family (e.g., LLaMA-2-7B target, TinyLLaMA drafter) to establish generality beyond PALM-2.
3. Report absolute generation throughput (tokens/second) alongside relative improvements.
4. Measure and report the computational overhead of block verification's acceptance probability computation to justify the "negligible overhead" claim.
5. Increase the number of random seeds from 3 to at least 5 for more reliable variance estimates.
