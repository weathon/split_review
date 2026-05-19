- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5
Now I have all the evidence I need. Let me write the final consolidated review.

## Summary
The paper presents the first mini-batch algorithm for maximizing a non-negative monotone decomposable submodular function under cardinality and p-system constraints. It shows that mini-batch sampling with weighted sampling improves over the prior sparsifier approach theoretically and empirically, and makes the surprising experimental observation that uniform sampling outperforms weighted sampling. The paper's main claimed contribution is a smoothed analysis with two natural smoothing models that provides theoretical justification for why uniform sampling works better in practice.

## Strengths
- **First mini-batch algorithm for decomposable submodular maximization**: The paper introduces Algorithms 2 and 3 and proves (Theorem 1.3) that mini-batch sampling provides either a multiplicative (1−ε)-approximate or additive (ε/γ)-approximate incremental oracle w.h.p. using a batch size α that depends on curvature or a slack parameter. This is a novel algorithmic contribution that advances beyond the sparsifier approach by resampling per iteration.

- **Experimental demonstration of mini-batch and uniform sampling advantages**: Figure 1 shows that for small batch sizes β, the mini-batch approach (especially with uniform sampling) achieves higher utility than the sparsifier while using about the same number of oracle calls on CIFAR100 and FashionMNIST. The paper also conducts 20 runs per condition, lending robustness to the results.

- **Practical elimination of expensive preprocessing**: Uniform sampling requires no preprocessing (removing the O(Nn) oracle calls), yielding query complexity independent of N (Table 1). Lemma 2.1 shows the expected sampled function size is α for uniform vs. ≤ αn for weighted sampling — a concrete theoretical advantage that translates to practice.

- **Empirical validation of smoothing parameters**: The paper computes φ values for all four datasets under Model 2 (CIFAR100: 0.38, FashionMNIST: 0.35, Uber pickup: 0.61, Discogs: 0.13) and reports φ = Θ(1), confirming that the theoretical preconditions for uniform sampling's superiority hold in real data.

## Weaknesses

### Fatal
None.

### Major
- **Misapplication of the bounded-dependency Chernoff bound (Theorems 4.2 and Lemma 4.3)**: Theorem 4.1 (Pemmaraju, 2001), as stated in the paper (line 203), requires the random variables X₁,…,X_N to be **identically distributed**. In the proof of Theorem 4.2, the bound is applied to the variables fⁱ(e) for i ∈ [N]. Model 1 only guarantees that each fⁱ(e) has expectation at least φ and bounded dependency d — it does **not** state that the fⁱ(e) are identically distributed. Lemma 4.3 (Model 2) inherits the same issue, since it applies the same concentration argument to a single element e*. This is a gap in the proof of the paper's main claimed contribution (the smoothed analysis explanation for uniform sampling's superiority). The analysis would need to either (a) add an identical-distribution assumption to the smoothing models, (b) cite a more general concentration inequality that handles non-identically distributed variables with bounded dependency, or (c) use a different argument altogether. Until resolved, the theoretical foundation for why uniform sampling is superior is incomplete.

### Minor
- **Dependency parameter d is not discussed empirically**: Both smoothing models involve a dependency parameter d and require N = Ω((d/φ) log(nd)). The paper measures φ empirically but provides no discussion, estimate, or argument that d is bounded for any of the datasets. This weakens the link between theory and experiment; the claim that the assumptions "hold for our datasets" is only partially verified.

- **Dataset diversity for mini-batch vs. sparsifier comparison**: The main experimental comparison (Figure 1) is reported only for two image datasets (CIFAR100, FashionMNIST). The Uber pickup and Discogs datasets are mentioned but excluded from these plots because of small ground set size. Broader validation would strengthen the empirical case.

### Trivial
- The paper could note the practical range of constant factors in the query complexity bounds (e.g., the log n factor, implicit constants from union bounds) to help readers assess when the Θ(1/nφ) improvement becomes meaningful.

## Nice-to-Haves
- The paper mentions combining mini-batch with stochastic-greedy but does not present experimental results for that combination. This would be a natural extension to include.
- Adding a horizontal line showing the full greedy (lazy-greedy) utility in the plots would help calibrate how close the sampled methods are to the exact greedy solution.
- A direct total-query-budget comparison (utility vs. total oracle calls on a single plot) would make the mini-batch advantage more transparent, though the paper already provides separate utility and query plots.

## Removed Points
- **"Experimental comparison is not properly controlled for total query cost"**: The reviewer claimed the mini-batch uses k times more oracle calls than the sparsifier for the same β. This is incorrect. Both methods evaluate their sampled functions against n candidates per iteration for k iterations, yielding approximately k·n·βN oracle calls during execution for both. The paper's statement that both use "about the same number of queries" is accurate and the comparison is fair. Removed as factually wrong.

- **"No comparison against full greedy in terms of utility"**: The paper compares against lazy-greedy, which is the standard efficient implementation of the greedy algorithm. This is a perfectly reasonable baseline. Removed as a strawman.

- **"Preprocessing cost of computing p_i's is O(nN)"**: The paper clearly acknowledges this cost, includes it in Table 1, and frames the elimination of this cost under uniform sampling as a key advantage. Removed — the paper already addresses this.

- **"No discussion of constant factors"**: This is a generic critique that applies to nearly all theory papers presenting asymptotic bounds. It is not a meaningful weakness. Moved to Trivial.

- **Various formatting/style gripes**: Removed per hard rules (parser artifacts).

## Novel Insights
None beyond the paper's own contributions. The harsh critic's identification of the Chernoff bound misapplication is a valid technical finding, but it is a flaw in the paper's proof, not a novel insight about the problem domain. The strength finder's synthesis does not surface any insight beyond what the paper itself claims.

## Suggestions
1. **Fix the concentration argument**: Replace or extend Theorem 4.1 with a concentration inequality that holds for non-identically distributed but bounded-dependency variables (e.g., Janson's inequality or a more general bounded-difference martingale argument). Alternatively, add the condition "identically distributed" to the smoothing models and discuss whether this is reasonable for the intended applications.
2. **Provide empirical context for d**: Even a brief discussion of why d is expected to be small in the datasets (e.g., due to the structure of the data or the independence of data points in the image datasets) would significantly strengthen the empirical grounding of the smoothed analysis.
3. **Acknowledge the gap transparently**: In the current version, the paper treats the concentration step as straightforward. Adding a remark about the identical-distribution requirement and how it is (or could be) satisfied would improve rigor.
