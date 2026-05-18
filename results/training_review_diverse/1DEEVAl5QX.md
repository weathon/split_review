Now I have a thorough understanding of the paper and the reviews. Let me compose the final consolidated review.

---

## Summary

This paper introduces the first mini-batch algorithm for maximizing a non-negative monotone decomposable submodular function under constraints. Instead of constructing a single sparsifier upfront (the prior state of the art), the algorithm samples a fresh mini-batch of constituent functions at each greedy iteration. The paper provides theoretical guarantees for weighted mini-batch sampling, introduces additive approximate incremental oracles as a relaxation, and attempts to use smoothed analysis to explain the surprising empirical finding that uniform mini-batch sampling outperforms weighted sampling. Experiments on four datasets (Uber pickups, Discogs, CIFAR100, FashionMNIST) demonstrate that uniform mini-batch performs well in practice.

## Strengths

- **First mini-batch algorithm for decomposable submodular maximization.** The paper replaces the sparsifier paradigm (sample once, then optimize) with per-iteration mini-batch sampling. Algorithms 2 and 3 are clearly presented, and the analysis shows that sampling a new batch each iteration enables tighter concentration.

- **Additive approximate incremental oracle.** Theorem 1.2 extends the standard multiplicative-approximate oracle framework to additive approximations, enabling the analysis to handle unbounded curvature. This is a genuine technical contribution that goes beyond existing multiplicative-only guarantees and is reused in the smoothed analysis (Lemma 4.3).

- **Clear theoretical comparison with prior work.** Table 1 gives a structured comparison of query complexities for naive, sparsifier, weighted mini-batch, and uniform mini-batch under both bounded and unbounded curvature, for cardinality and p-system constraints. This makes the improvement over Rafiey & Yoshida (2022) and Kenneth & Krauthgamer (2023) immediately visible.

- **Empirical validation across diverse datasets.** Experiments cover four datasets representing different types of decomposable submodular functions (facility location, maximum coverage, exemplar clustering). The consistent finding that uniform mini-batch performs well across datasets is practically valuable and genuinely surprising.

## Weaknesses

### Major

1. **The empirical validation of the smoothing models checks the wrong quantity.** Model 2 requires that there exists an element e ∈ E such that *every* fⁱ(e) has expectation at least φ (i.e., E[fⁱ(e)] ≥ φ for all i). However, the empirical validation (Section 4) computes min_e (1/N) Σ_i fⁱ(e) — the *average* over i, not the minimum over i. An average of 0.35 across 50,000 functions is entirely consistent with many functions having near-zero expectations. Similarly for Model 1, the paper computes max_e (1/N) Σ_i fⁱ(e) but the model requires that *every* fⁱ(e) for *every* e has E[fⁱ(e)] ≥ φ. The paper provides no argument — theoretical or empirical — that the per-function lower bound holds for any dataset. The central claim that "Model 2 is able to explain the empirical success of the uniform mini-batch algorithm on all datasets" (line 235) is therefore not supported by the evidence presented.

2. **The concentration bound used in the smoothed analysis is not justified for the setting.** Theorem 4.1 (Pemmaraju, 2001) is cited as requiring "identically distributed random variables." The fⁱ(e) in Models 1 and 2 need not be identically distributed — they can have different expectations and potentially different variances. The paper does not address this gap or cite a version of the bound that holds for non-identical distributions with bounded dependency. This affects the validity of both Theorem 4.2 and Lemma 4.3.

These two issues together undermine the paper's central claimed contribution: using smoothed analysis to provide a theoretical foundation for the uniform mini-batch algorithm's empirical success. The weighted mini-batch results (Section 2) are unaffected, but the paper's headline theoretical contribution rests on a foundation that has not been properly validated or justified.

### Minor

3. **The bounded dependency parameter d is never estimated or bounded for any dataset.** The theoretical guarantees in Section 4 depend on N = Ω((d/φ) log(nd)). Without any empirical handle on d, the applicability of the smoothed analysis to the experimental datasets is unclear.

4. **The specific k values used in the experiments are not reported.** The paper states experiments were run "for different values of k" (line 188) but never specifies which values. This makes it impossible to connect the experimental results to the theoretical claims about curvature (since curvature could depend on k) and limits reproducibility.

5. **The experimental comparison of oracle evaluations is not fully explained.** Mini-batch samples βN functions per iteration for k iterations (kβN total sampled functions), while the sparsifier samples βN functions once. Despite this, the paper shows mini-batch using *fewer* oracle evaluations for small β (Figure 1(b)). The interaction between lazy-greedy and the sampling procedures that would explain this is not discussed. This reduces transparency of the experimental comparison.

6. **No discussion of limitations.** The paper does not discuss what happens when φ is small or when dependencies are high, even though the theoretical guarantees degrade polynomially in 1/φ and d. A limitations paragraph would strengthen the paper.

### Trivial

- The paper uses the notation "Model 2" in the proof of Theorem 4.2 (line 205) where it should say "Model 1" — a copy-paste error.

## Nice-to-Haves

- A direct experimental comparison with stochastic-greedy (Buchbinder et al., 2015) as a standalone baseline (not combined with sparsifier/mini-batch) would help situate the method within the broader literature on sampling-based submodular optimization.
- Estimating d empirically for at least one dataset (e.g., via pairwise correlation of fⁱ(e) values) would significantly strengthen the smoothed analysis claims.
- Absolute (not just relative) oracle evaluation counts for at least one configuration would help assess practical significance.

## Removed Points

- **Weakness about curvature claim being "undersold."** The paper states "We can get improved performance if the curvature of F is bounded" (line 51) in the same section as the superiority claims, and Table 1 clearly separates bounded vs. unbounded curvature cases. The qualification is adequate.

- **Weakness about missing p-system implementation details (setting A_j).** This is standard for a p-system constraint and the algorithm description is appropriately abstract for a theory paper.

- **Weakness about missing comparison with stochastic-greedy as a standalone baseline.** The paper's scope is comparing mini-batch vs. sparsifier approaches; adding more baselines is a nice-to-have, not a weakness.

- **Strength about smoothed analysis providing "direct theoretical explanation."** This conflicts with verified Weakness #1 (empirical validation mismatch). Per the rules, when a strength and verified weakness disagree, the weakness wins. The theoretical framework exists but its empirical support is insufficient to claim it "explains" the results.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself misses.

## Suggestions

1. **Restructure the paper's theoretical claims.** The weighted mini-batch analysis and additive approximate oracle are solid contributions that do not depend on smoothed analysis. Consider either: (a) revising the smoothing models so the assumptions match the quantities actually measured (e.g., a lower bound on the *average* of fⁱ(e) rather than per-function), and re-deriving the guarantees accordingly, or (b) honestly acknowledging that the theoretical explanation for uniform sampling's success is open, and presenting the uniform mini-batch algorithm as an empirically motivated heuristic whose strength is its simplicity and lack of preprocessing cost.

2. **Fix the empirical validation in Section 4.** If Model 2 is retained as-is, compute the per-function minimum (min_i fⁱ(e)) rather than the average over i, and report whether this quantity is bounded away from zero. Alternatively, adjust the model definition to match what is empirically computed.

3. **Address the concentration bound gap.** Either cite a version of the bounded-dependency Chernoff bound that does not require identical distributions, or provide an argument that the bound still applies to non-identical distributions (e.g., by a standard reduction using a Doob martingale argument).

4. **Report experimental parameters clearly.** Include the specific k values used, add error bars or variance information to the plots, and explain the mechanism by which mini-batch achieves lower oracle evaluation counts than the sparsifier.

5. **Add a limitations paragraph** discussing when the method might fail (small φ, high dependencies, small N relative to n).

## Score and Decision

The paper introduces a novel algorithmic approach (mini-batch sampling for decomposable submodular maximization) with a solid weighted-sampling analysis and a useful technical contribution (additive approximate oracles). The empirical finding that uniform mini-batch works well is practically valuable. However, the paper's central claimed contribution — using smoothed analysis to theoretically explain this empirical success — is undermined by two significant issues: the empirical validation checks the wrong quantities relative to the model assumptions, and the concentration bound used is not properly justified for non-identically distributed variables. These are fixable in revision, but in the current state the paper overclaims what the smoothed analysis establishes. The weighted mini-batch results alone, while solid, represent an incremental improvement over existing sparsifier methods.

On originality and importance: the mini-batch perspective is novel and the problem is well-motivated. On soundness: the weighted analysis is sound, but the smoothed analysis has verification gaps. On clarity: generally well-written but could be more transparent about experimental methodology and limitations.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>