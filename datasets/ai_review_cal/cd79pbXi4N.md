- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6
Now I have a thorough understanding of the paper. Let me synthesize my final review.

## Summary

This paper introduces LipsLev, the first method for deterministic certified robustness under Levenshtein distance constraints in text classification. The core idea is to use the ERP distance as a continuous relaxation of Levenshtein distance, estimate layer-wise Lipschitz constants of convolutional classifiers with respect to this metric, and employ 1-Lipschitz training to enable single-forward-pass certification. The method achieves 38.80% verified accuracy at k=1 on AG-News and is 4–7 orders of magnitude faster than existing approaches, while also being the only method that can certify at k>1.

## Strengths

- **First deterministic Levenshtein distance certification.** Table 1 and the related-work survey clearly show that prior deterministic methods (IBP-based) cannot handle insertions/deletions, and randomized smoothing methods are only probabilistic. LipsLev is the first to provide deterministic certificates under the full Levenshtein distance. This is a genuine step forward.

- **Massive speedup from single-forward-pass certification.** Table 2 reports LipsLev at 5.08e-02 seconds vs. 1.21e+03 seconds for brute-force and IBP on AG-News (k=1) — a speedup of roughly 4 orders of magnitude, consistent with the paper's claims.

- **Handles Levenshtein distances >1**, while all prior deterministic methods cannot. LipsLev provides verified accuracy at k=2 (e.g., 13.93% on AG-News, 1.83% on SST-2, 75.33% on Fake-News), whereas brute-force and IBP are marked OOT (out of time) or unsupported.

- **Novel theoretical connection between Levenshtein and ERP distances.** The paper establishes that on one-hot vectors with p=∞, ERP distance recovers Levenshtein distance (Lemma S4), and provides an upper bound on the Lipschitz constant of convolutional margin functions via Eq. (Theorem 4.3). This framework opens a new direction for Lipschitz-based text verification.

- **Effective 1-Lipschitz training procedure.** Eq. (7) enforces 1-Lipschitzness by dividing each layer's output by its Lipschitz estimate. Table 3 shows this substantially outperforms regularizing the Lipschitz constant, which either collapses to a constant classifier or yields near-zero verified accuracy.

- **Evaluation on four datasets** (AG-News, SST-2, Fake-News, IMDB) with consistent experimental setup, and honest discussion of limitations (single-layer conv, challenges with transformers/tokenizers) in the conclusion.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims (first deterministic Levenshtein certification, substantial speedup, ability to handle k>1) are well-supported by evidence. No verified weakness undermines them.

### Minor

1. **Sum-pooling Lipschitz constant is not derived.** The classifier in Eq. (6) applies global sum-pooling over the time dimension: `f(S) = (∑_i f_i^{(l)}(S)) W`. The bound in Theorem 4.3 chains through the embedding, convolutional, and linear layers but never accounts for the Lipschitz constant of the sum-pooling operation with respect to the ERP distance. While the bound `||sum(A) - sum(B)||_p ≤ d_ERP^p(A, B)` plausibly holds (and can be shown by triangle inequality over any alignment), this is not argued or proved in the paper. The gap is small and fixable — the bound is correct — but the omission means the certification guarantee in Corollary 4.4 is technically incomplete as presented.

2. **The IBP comparison, while explained, could be framed more clearly.** The paper trains one set of models (using Eq. 7) and applies three verification methods (brute-force, IBP, LipsLev) to those same models. It then states LipsLev "improves over IBP in AG-News and match IBP in Fake-News at k=1." The paper does acknowledge why IBP-specific training is impractical ("maximum perturbation sizes are 33,742 and 85,686. This makes it impractical to perform IBP verified training"), and this reasoning is sound. However, a reader could misread the claim as "LipsLev is a better verification method than IBP" rather than "on models trained with our procedure, LipsLev gives better certified accuracy than an IBP verification applied post-hoc." The paper would benefit from sharper framing that distinguishes between verification-method comparison and training-method comparison.

3. **Variance across random seeds is not reported.** The paper states results are averaged over three seeds, but Table 2 reports only point estimates without standard deviations or error bars. This is standard practice in the certified robustness literature and would increase confidence in the results.

4. **The dual norm `r` is used but never defined.** Theorem 4.3 states "Let p ≥ 1" and then uses `||w_hat - w_y||_r` without specifying that r satisfies 1/p + 1/r = 1. This is a standard definition but should be explicit.

5. **The computation of `M(K)` for convolutional layers is not specified.** The Lipschitz constant `M(K)` for the convolutional layer (represented as a block-Toeplitz matrix in Definition 4.2) requires computing an operator norm. The paper does not describe how this is computed in practice (e.g., power iteration, SVD, closed form). This is needed for reproducibility.

### Trivial

- Missing explicit definition of the dual norm r (1/p + 1/r = 1) in Theorem 4.3.
- The proof of Theorem 4.3 is deferred; a brief sketch in the main text would help readability.

## Nice-to-Haves

- An ablation measuring how much the product Lipschitz bound overestimates the true Lipschitz constant (e.g., via brute-force on very short sequences or comparison with adversarial attack success rates).
- Brief quantitative comparison or positioning against randomized smoothing approaches (Huang et al., 2023) beyond the scope table.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **IBP comparison claimed "fundamentally unfair" (Harsh Critic, Critical Issue 1).** Removed because the paper transparently explains why IBP-specific training is impractical in this setting (perturbation sizes of 33K–85K) and never claims LipsLev is a universally better verification method. The comparison is clearly scoped — the same models, different verifiers — and the paper's explanation is reasonable. This is at most a minor framing concern (retained above), not a fatal flaw.
- **Criticism that the evaluation is limited to single-layer architecture (Harsh Critic, Critical Issue 3).** Removed because the paper's methods (Eq. 6, Theorem 4.3) are formulated for l convolutional layers generally; the single-layer experiment follows a standard architecture from Huang et al. (2019). The conclusion honestly acknowledges that scaling is future work. This is a scope statement, not a weakness.
- **Missing discussion on why sum-pooling was chosen (Harsh Critic, Section 2 notes).** Removed — this is a speculative concern without evidence that a different pooling choice would change results.
- **"Reproducibility concerns about M(K) computation" raised as a major issue.** Removed — this is a minor presentational detail affecting reproducibility, downgraded to minor weakness #5 above.
- **Strength Finder's generic strengths (e.g., "this paper addresses an important problem").** Removed — these are superficial and lack specific content tied to the paper's contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that the paper itself does not articulate.

## Suggestions

1. **Add a brief lemma or remark** establishing that global sum-pooling is 1-Lipschitz with respect to ERP distance and the ℓ_p norm. This closes the technical gap in Corollary 4.4.
2. **Reframe the IBP comparison** more precisely: "On models trained with our 1-Lipschitz procedure, LipsLev achieves higher verified accuracy than IBP applied post-hoc and is the only method that can handle k>1. IBP-specific training is infeasible in this setting due to the large perturbation sets." This prevents any potential misinterpretation.
3. **Report standard deviations** in Table 2 for the three seeds.
4. **Define the dual norm r** explicitly in Theorem 4.3 (1/p + 1/r = 1).
5. **Briefly describe** how `M(K)` is computed (e.g., spectral norm of the block-Toeplitz matrix via power iteration) in Section 4.2.
