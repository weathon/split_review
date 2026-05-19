- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 6, 6, 8, 5
Now I have all the information needed. Let me produce the consolidated final review.

## Summary
This paper proposes a novel synthetic framework based on interleaved Markov chains with varying lags to study how attention-only transformers perform in-context causal structure selection. It provides an explicit, interpretable construction of a 3-layer attention-only (disentangled) transformer that implements "selective induction heads" — circuits that aggregate past transition probabilities to identify the correct lag and copy the corresponding token. The paper empirically shows that both constructed and trained transformers match the performance of the maximum likelihood (ML) estimator asymptotically, and that trained attention maps qualitatively resemble the construction.

## Strengths

- **Explicit, interpretable construction of a 3-layer transformer.** Section 4.1 provides concrete attention matrix entries for each layer (Eq. 4–6), detailed enough to be implemented from scratch. This goes beyond prior induction-head work (Olsson et al., 2022; Nichani et al., 2024) by handling variable lags rather than fixed causal structures.

- **Novel synthetic task that isolates causal structure selection.** Section 3 defines interleaved Markov chains with fixed transition probabilities but varying lags. Unlike prior Markov-chain frameworks with fixed causal structure, this task requires the model to dynamically identify the correct lag in context — a principled abstraction of a core challenge in natural language. The Bayesian model average and ML baselines are correctly derived.

- **Empirical alignment between trained and constructed transformers.** Figure 4a shows that attention maps from trained standard and disentangled transformers closely match the construction, especially in the first and third layers. The KL divergence plots in Figure 3 demonstrate that both trained and constructed transformers match ML performance asymptotically. This evidence supports the claim that gradient descent discovers a similar algorithm to the construction.

## Weaknesses

### Major

- **The central theoretical claim (asymptotic convergence to ML) relies on an unproven claim.** Section 4.3 explicitly states: *"While specific cases (e.g., two lags, no normalization, or independent lags) are proven in App. B, we leave the complete proof of Claim 1 for future work."* Claim 1 — that the expected normalized transition probability is higher for the correct lag — is the linchpin connecting the construction to maximum likelihood. Without it, the theoretical analysis is incomplete. The abstract overstates this by claiming "a theoretical analysis proving that this mechanism asymptotically converges to the maximum likelihood solution," which contradicts the paper's own admission. This is the single most impactful weakness: the paper frames itself as advancing theoretical understanding, but its core theoretical result is deferred.

### Minor

- **The claim that "2-layer attention-only transformers cannot solve the task" is asserted without evidence in the main text.** This claim appears in the introduction (line 19) but no experiment, analysis, or even summary of a result is provided in the main body to support it. If the experiment exists in the appendix, the main text should at minimum summarize the finding. Without it, the necessity of the 3-layer construction is less well-motivated.

- **Attention map comparisons are qualitative only.** Figure 4a's visual comparison is suggestive but not conclusive — especially for the second layer where "similar diagonal structure" is noted but the trained maps appear noisier. A quantitative metric (e.g., fraction of attention weight on expected diagonals, cosine similarity between attention vectors) would substantially strengthen the claim that trained models implement the same algorithm.

- **KL divergence plots lack error bars or confidence intervals.** The paper reports KL divergence as a deterministic function of sequence length, but since sequences are randomly generated, some measure of variance (especially at shorter lengths where performance varies) is important for assessing reliability of the results. This is a standard expectation for empirical work.

### Trivial

- None of consequence beyond the above.

## Nice-to-Haves

- A discussion of why the construction's finite-sample KL sometimes appears lower than ML (which is theoretically optimal given known P*) would clarify whether this is noise, a plotting artifact, or a genuine property of the softmax construction.
- A brief analysis of how large λ and β need to be relative to the transition probabilities to avoid misclassification would strengthen the practical applicability of the construction.
- A more precise comparison distinguishing "selective induction heads" from standard induction heads (Olsson et al., 2022) would clarify the novelty.

## Removed Points

- **Criticism about the typo in A^{(1)}_{ij} definition (two identical conditions with opposite signs).** This is either a parser artifact or a minor notational issue. The surrounding text and matrix illustration make the intended pattern clear. Per Hard Rules, formatting/typographical criticisms are removed.
- **Strength Finder's claimed strength #3 ("Theoretical proof that the transformer predictor asymptotically converges to ML").** This strength is factually inaccurate — the paper explicitly says Claim 1's proof is left for future work. Removed as unsupported.
- **Criticism about the connection between normalized probabilities and MLE being insufficiently justified.** The paper's argument (Claim 1 → ergodicity → correct selection matches ML) is a coherent logical chain; the gap is the unproven Claim 1, not a missing connection between functional forms. The section's claim is about matching the *selection*, not the numerical values. This criticism conflates two separate issues.
- **Criticism about the construction outperforming ML for short sequences.** The paper says the construction "matches" ML performance; minor visual deviations in the plot could be noise. This is speculation without a clear anchor in the paper's text.
- **Criticism about missing discussion of ties/near-ties in the argmax.** This is an edge case that would be addressed by the (admittedly incomplete) theoretical analysis; it is not a core flaw.

## Novel Insights

The harsh reviewer's observation that the construction uses *averages of normalized transition probabilities* while MLE uses *sums of log-probabilities* — and that the paper's "equivalence" claim must bridge this gap — is a genuine insight not fully articulated in the paper itself. The paper's argument from Claim 1 + ergodicity implicitly glosses over the fact that the normalized denominator depends on all lags simultaneously, creating a dependency structure that a cleaner proof would need to handle. This is a worthwhile observation for the authors to address in their theoretical development.

Beyond this, the reviews surface no genuinely novel insight beyond the paper's own contributions.

## Suggestions

1. **Complete or scale back the theoretical claims.** The paper's most pressing issue is the gap between the abstract's "proving" and Section 4.3's "we leave the complete proof... for future work." Either prove Claim 1 (even under mild additional assumptions), or honestly reframe the paper as presenting an empirically successful construction with a plausible but unproven convergence argument. This single change would resolve the main tension in the paper.

2. **Add quantitative attention similarity metrics** (e.g., fraction of attention weight on the expected diagonals in each layer) to Figure 4a.

3. **Include the 2-layer failure experiment in the main text**, or at minimum summarize the result clearly.

4. **Add error bars** to the KL divergence plots (Figure 3), especially for shorter sequence lengths where variance is expected to be higher.
