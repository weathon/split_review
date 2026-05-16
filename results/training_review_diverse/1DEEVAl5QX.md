Now I have all the information needed. Let me compose the final review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper introduces the first mini-batch algorithm for maximizing non-negative monotone decomposable submodular functions, with weighted and uniform sampling variants. It provides theoretical guarantees showing that the mini-batch approach achieves near-optimal approximation ratios while reducing oracle complexity, and develops a smoothed analysis framework (Models 1 and 2) that explains—both theoretically and empirically—why simple uniform sampling outperforms weighted sampling in practice.

## Strengths

- **First mini-batch algorithm for decomposable submodular maximization with formal guarantees.** The paper introduces Algorithm 3 and proves (Theorem 1.3) that with appropriate batch sizes it provides approximate incremental oracles at each greedy step, yielding near-optimal approximation guarantees (Theorem 1.4) under both cardinality and p-system constraints. This is a genuinely novel algorithmic contribution.

- **Smoothed-analysis framework that explains the practical superiority of uniform sampling.** Models 1 and 2 are natural and well-motivated. Theorem 4.2 shows that under Model 1, both the sparsifier and mini-batch achieve the same guarantees with uniform sampling (at a Θ(1/nφ) factor). Lemma 4.3 shows that even under the weaker Model 2 (requiring conditions only for a single element), the mini-batch guarantees survive. The empirical φ values are Θ(1) for all datasets (CIFAR-100: 0.38, FashionMNIST: 0.35, Uber: 0.61, Discogs: 0.13), directly validating the model.

- **Experimental demonstration that uniform mini-batch outperforms both weighted and sparsifier baselines.** Experiments on four real-world datasets show that uniform mini-batch achieves higher utility than both weighted mini-batch and the sparsifier approach, especially at small batch sizes β, while using comparable or fewer oracle evaluations (Section 3, Figure 1). The finding is consistent across datasets and is the key empirical observation that motivates the smoothed analysis.

- **General theoretical framework for additive approximate oracles.** Theorem 1.2 extends existing approximate-oracle results to an additive error model, providing guarantees for both cardinality and p-system constraints. This is used in the unbounded-curvature case and is a useful standalone contribution.

- **Practical simplicity and elimination of preprocessing cost.** Uniform sampling requires no preprocessing (zero O(Nn) cost), making the algorithm's complexity independent of N. The paper explicitly contrasts this with the weighted approach's O(Nn) preprocessing overhead.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No variance reporting in experiments.** Figure 1 reports only averages over 20 runs with no error bars, confidence intervals, or measures of spread. The main empirical finding—that uniform sampling outperforms weighted sampling—is a key driver of the paper's narrative, yet the reader cannot assess the statistical significance or variability of the observed differences. While the consistency of results across four datasets partially mitigates this concern, adding error bars would substantially strengthen the empirical claims.

- **The dependency parameter d in the smoothing models is not empirically validated.** The smoothed analysis (Theorem 4.2, Lemma 4.3) relies on both the expectation condition (φ) and the bounded-dependency condition (d). The paper carefully validates φ empirically for both models, but never verifies—or even argues for the plausibility of—the bounded-dependency assumption. The bounded-dependency Chernoff bound (Theorem 4.1) explicitly depends on d, and the proof of Theorem 4.2 uses N = Ω((d/φ) log(nd)). Without any evidence about d, the link between the theory and the experiments is partially incomplete. The paper should at minimum acknowledge this limitation or discuss why bounded dependency is a reasonable modeling assumption for these datasets.

### Trivial

- **The claim that the smoothing model is "even more general" (line 42) is stated without justification.** The paper asserts that a density-bounded distribution implies the expectation condition, which is true, but does not discuss whether the converse fails or whether bounded dependency is strictly weaker. This is a minor overstatement in a single sentence and does not affect the paper's main contributions.

- **The comparison between mini-batch and sparsifier in the theoretical results relies on Table 1 (an image), and the text only provides a high-level discussion** without restating the sparsifier's exact query complexity bounds in the same notation as Theorem 1.4. While the table and theorems collectively support the claims, a more self-contained textual comparison would help the reader.

## Nice-to-Haves

- A brief discussion of memory/I/O trade-offs between sampling once (sparsifier) vs. sampling every iteration (mini-batch) would help practitioners.
- The bounded-dependency definition from Pemmaraju (2001) could be restated more explicitly in the text to improve self-containedness.
- It would be interesting to see whether the stochastic-greedy variant (sampling elements rather than functions) can be combined with the mini-batch approach in further ways beyond what is noted.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Unsubstantiated claim that weighted mini-batch improves over the sparsifier in theory"** — REMOVED. The paper explicitly provides this comparison in Table 1 (an embedded image) and through the stated theorems (Theorem 1.3, 1.4). The reviewer's inability to parse the table is a PDF extraction artifact, not an author omission. The paper's claims are backed by explicit query complexity bounds.

- **"Parameter d is never defined formally"** — REMOVED. The paper defines d at line 40: "Elements in A_e have dependency at most d (every f^i(e) depends on at most d other elements in A_e)." This is a clear definition. The reviewer's concern about citing Pemmaraju (2001) is addressed by Theorem 4.1.

- **"Missing error bars or confidence intervals"** — Already captured as a Minor weakness above. The redundant mentions are consolidated.

- **"A direct, side-by-side table of query complexity"** — REMOVED. The paper already has this table (Table 1). The reviewer could not read it due to extraction artifacts.

- **"Memory requirements discussion"** — MOVED to Nice-to-Haves. This is a useful suggestion, not a weakness.

- **"Unfair comparison"** — REMOVED. The experiments compare methods under the same expected batch size and β, which is a fair and standard setup.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no insights about the paper that go beyond what the authors already present.

## Suggestions

1. **Add error bars or confidence bands to Figure 1.** With 20 runs per point, reporting standard deviations or using shaded regions would significantly strengthen the empirical credibility without requiring additional experiments.
2. **Discuss the bounded-dependency assumption (parameter d) explicitly.** Either provide an empirical argument (e.g., measuring pairwise correlations among the f^i(e) values), cite domain-specific reasons why it should hold, or at minimum acknowledge it as an unverified modeling assumption and discuss whether the results are robust to violations.
3. **Restate the sparsifier's query complexity in the same notation as Theorem 1.4** in the text (not just in the table image) to make the theoretical comparison fully self-contained.

## Score and Decision

The paper makes a solid contribution: a novel mini-batch algorithm for decomposable submodular maximization, a clean theoretical analysis, a well-motivated smoothed analysis framework, and convincing experimental results. The weaknesses are minor and addressable. The theoretical results are sound, the experiments are well-designed (apart from the variance reporting gap), and the smoothed analysis provides genuine insight into why a simple heuristic works well.

**Score:** 7.5

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>