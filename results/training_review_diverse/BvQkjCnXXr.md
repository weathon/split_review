Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes FastLSH, a simple modification to E2LSH that first randomly samples $m$ of the $n$ dimensions before applying the standard random projection, reducing per-vector hashing cost from $O(n)$ to $O(m)$. The paper claims FastLSH retains the provable LSH property (via asymptotic equivalence to E2LSH) and validates the method across three machine learning tasks: outlier detection, neural network training, and nearest neighbor search.

## Strengths

- **Substantial and verified speedups**: FastLSH achieves up to 80× speedup in hash computation (Figure 3c) and up to 20× speedup in end-to-end index construction (Figure 3d,h) across multiple real-world datasets. These gains translate to 6.1× end-to-end speedup in anomaly detection (Table 1) and 1.7× in neural network training (Figure 2), while maintaining accuracy comparable to E2LSH.

- **Broad and consistent experimental validation**: The method is tested on three distinct tasks (outlier detection, neural network training, ANN search) using multiple real-world datasets per task (Statlog Shuttle, a9a, Musk; Delicious-200K, Amazon-670K; ImageNet, Trevi, Deep, Glove, Ukbench, etc.). Results are consistent: FastLSH preserves accuracy while significantly reducing execution time.

- **Simplicity and ease of integration**: The method requires only random sampling plus standard random projection — no Hadamard transforms or other machinery. This makes it straightforward to drop into any existing LSH-based application (ACE, SLIDE, etc.), as demonstrated in the experiments.

## Weaknesses

### Major

- **The claimed "provable LSH property" is not actually proven.** The paper asserts (lines 4, 22, 99, 276) that FastLSH "has provable LSH property" and "maintains the same theoretical guarantee as the classic E2LSH." However, the analysis never proves that the collision probability $p(s,\sigma)$ is monotonically decreasing in the Euclidean distance $s$, which is required by Definition 2.1. Instead, the argument proceeds as: (i) derive collision probability expression (Theorem 4.2), (ii) show asymptotic equivalence to E2LSH in the limit $m \to \infty$ via characteristic functions (Section 4.2), and (iii) compare first-four moments of distributions (Section 4.3) for finite $m$. Step (ii) only addresses the infinite-$m$ limit — not the finite-$m$ regime used in all experiments. Step (iii) shows distributional similarity between $\tilde{s}X$ and a normal — it does **not** establish that the LSH inequalities ($p_1 > p_2$) hold for thresholds $R$ and $cR$. Moment matching is not a proof of the LSH property. The paper conflates "asymptotically similar distribution" with "satisfies the LSH definition," which is a non sequitur. Because the paper's core differentiating claim (vs. non-LSH sketches like ACHash) rests on this theoretical guarantee, this gap is significant.

- **The collision probability depends on $\sigma$ (per-dimension squared-distance variance) in an unanalyzed way.** The paper acknowledges (line 175) that $p(s,\sigma)$ depends on both $s$ and $\sigma$, whereas E2LSH's $p(s)$ depends only on $s$. Two pairs with the same Euclidean distance $s$ can have different $\sigma$ values and thus different collision probabilities. The LSH definition (Definition 2.1) requires that *all* pairs with distance $\le R$ have collision probability at least $p_1$, and *all* pairs with distance $\ge cR$ have probability at most $p_2$. The paper offers no analysis of whether such uniform thresholds exist when $\sigma$ varies arbitrarily. This is a genuine conceptual gap in the claimed theoretical guarantee.

### Minor

- **Sampling with replacement vs. without replacement is not discussed.** The paper draws $m$ i.i.d. samples with replacement (forming a multiset, line 82). This means the same dimension can be sampled multiple times, inflating the effective dimension without adding new information. The variance of $\tilde{s}^2$ under sampling with replacement differs from sampling without replacement, but the paper does not discuss this choice or its implications.

### Trivial

None.

## Nice-to-Haves

- Show recall-vs.-query-time curves across multiple target recalls in the main paper (currently only the 0.9 operating point is in the main text; the appendix contains more). This would strengthen the empirical case.
- Report explicit $m$ values and the bucket-width scaling relationship $\tilde{w} = \frac{m}{n} w$ for each experiment in the main text, so readers can directly see the trade-off between sampling ratio and accuracy.
- Add an empirical verification that the collision probability is indeed monotonically decreasing in $s$ (e.g., by sampling random pairs and measuring empirical collision rates), which would compensate for the incomplete theory.

## Removed Points

- **Characteristic function derivation correctness (Lemma 4.4)**: The reviewer questioned whether the characteristic function expression is correct, noting the proof is deferred to the appendix. This is removed because proof details exist in the original submission's appendix (stripped by the parser). The rule states: "REMOVE weaknesses about missing appendix, missing proofs in appendix."

- **Missing $m$, $k$, $L$ values in experiments**: The reviewer noted these parameters are not reported in the main text. Removed because parameter settings are referenced to appendix sections (C.1–C.4) which were stripped by the parser. The original submission contains these details.

- **Only one recall operating point shown**: The paper shows the 0.9 recall case in the main text and references the appendix for full curves. This is a presentation choice, not a flaw — moved to Nice-to-Haves.

- **ACHash comparison is unfair**: The reviewer claimed the comparison with ACHash is expected/stated. The paper also compares against E2LSH and MPLSH alongside ACHash, so this is not a weakness — ACHash is a natural baseline as the only other fast sketch.

- **Hashing vs. end-to-end cost**: The reviewer noted that other steps (hash table initialization, linked list maintenance) can dominate. The paper already acknowledges this explicitly (line 267: "Besides hashing, the procedure of index construction consists of other operations such as hash table initialization and linked list maintenance, which cannot be accelerated"). Removed as already addressed.

## Novel Insights

None beyond the paper's own contributions. The key insight — randomly sample dimensions before the random projection to reduce hashing cost — is clean and practical. The theoretical gap (no proof of monotonicity) and the unanalyzed $\sigma$ dependence are the most important weaknesses to emerge from the review.

## Suggestions

1. **Reframe the theoretical claim honestly.** Either provide a genuine proof that the collision probability is monotonically decreasing in $s$ (or that $p_1 > p_2$ thresholds exist), or downgrade the claim from "provable LSH property" to "asymptotic equivalence to E2LSH" and present FastLSH as an empirically validated efficient heuristic with strong theoretical intuition. The current blend of incomplete theory and strong language ("provable LSH property") is misleading.

2. **Address the $\sigma$ dependence.** At minimum, provide empirical evidence (e.g., simulations) that for pairs with the same $s$ but different $\sigma$, collision probabilities stay within well-separated bounds for $R$ and $cR$. Or prove that the expected collision probability over the random sampling is still monotonic.

3. **Discuss the sampling-with-replacement choice** and its effect on the variance of $\tilde{s}^2$ relative to sampling without replacement.

4. **Add recall-vs.-time curves** and explicit $m$ values to the main paper to strengthen the empirical case and make trade-offs transparent.

## Score and Decision

The paper presents a simple, practical idea with solid empirical validation across multiple tasks. The computational gains are real and well-demonstrated. However, the paper's central differentiating claim — "provable LSH property" with theoretical guarantee — is not substantiated. The theoretical analysis proves asymptotic equivalence (in the $m\to\infty$ limit) but never establishes that FastLSH satisfies Definition 2.1 for finite $m$, which is the regime used throughout the experiments. The unanalyzed $\sigma$ dependence introduces a further gap between claim and support. These are not minor presentation issues — they cut to the core of what the paper claims as its primary contribution over non-LSH alternatives. The paper could be acceptable after major revision (either by providing a proper proof or by reframing the contribution as an empirically effective heuristic with asymptotic intuition), but in its current form the overclaiming is too significant.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>