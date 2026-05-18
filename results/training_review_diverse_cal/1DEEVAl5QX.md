Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces the first mini-batch algorithm for maximizing non-negative monotone decomposable submodular functions. It considers both weighted and uniform sampling for constructing the mini-batches at each greedy step, and provides theoretical guarantees under cardinality and p-system constraints. The key empirical finding is that uniform mini-batch sampling outperforms weighted sampling in practice, which the paper explains via a novel smoothed analysis framework with two smoothing models.

## Strengths

1. **First mini-batch algorithm for decomposable submodular maximization.** The paper introduces a genuinely new algorithmic approach — replacing the standard single-sparsifier strategy with fresh mini-batches sampled at each greedy iteration. The theoretical analysis (Theorems 1.3 and 1.4) provides formal guarantees, and the approach is cleanly distinguished from prior sparsifier-based work (Rafiey & Yoshida, 2022; Kenneth & Krauthgamer, 2023).

2. **Novel smoothed analysis providing a theoretical explanation for uniform sampling's empirical success.** The paper identifies that uniform mini-batch outperforms weighted mini-batch experimentally — a fact that worst-case analysis cannot explain (since a single non-zero function could be missed by uniform sampling). To bridge this gap, the paper introduces two smoothing models (Models 1 and 2) and proves that under these models uniform sampling retains the same approximation guarantees while reducing query complexity by a Θ(1/nφ) factor (Theorem 4.2 and Lemma 4.3). Model 2 is particularly elegant: it only requires a single element to satisfy the expectation and bounded-dependency conditions, and the empirical φ values for all four datasets are Θ(1) (CIFAR100: 0.38, FashionMNIST: 0.35, Uber: 0.61, Discogs: 0.13).

3. **Consistent empirical results across multiple real-world datasets.** Experiments on CIFAR100, FashionMNIST, Uber pickups, and Discogs demonstrate that for small batch sizes (small β), uniform mini-batch achieves higher utility than both weighted mini-batch and the weighted sparsifier, while using a comparable number of oracle evaluations (Figure 1). The finding that uniform > weighted is surprising and practically useful, as uniform sampling requires no preprocessing and has complexity independent of N.

4. **Coverage of both cardinality and p-system constraints.** The paper provides rigorous guarantees for two widely studied constraint types, demonstrating generality beyond a single setting. The analysis covers both multiplicative and additive approximate oracles (Theorems 1.1, 1.2, 1.3).

## Weaknesses

### Major

1. **Overclaim of theoretical superiority for weighted mini-batch over the sparsifier.** The abstract and introduction state that "mini-batch with weighted sampling improves over the state of the art sparsifier based approach both in theory and in practice" without qualification. However, for the default unbounded-curvature setting — which covers most applications and is not verified to be bounded for the experimental datasets — the mini-batch algorithm's query complexity (Theorem 1.4, item 2: O(k²(n/ε)² log n)) is worse than the sparsifier's (O(k n² log n / ε²) per the cited works) by a factor of k. The paper does partially qualify this later ("We can get improved performance if the curvature of F is bounded," line 51), but the main claims in the abstract and introduction remain misleadingly broad. The paper should clearly delineate the regimes (bounded vs unbounded curvature) in its central claims.

2. **Smoothed analysis validation is indirect and does not verify the distributional assumptions.** The empirical "validation" of the smoothing models computes φ = (1/N) Σ_i f^i(e) from the observed data. But φ is formally defined as a lower bound on *expectations* of random variables, not on sample averages. The paper does not test whether the data plausibly arises from a distribution with the required properties (expectation ≥ φ, bounded dependency d), nor does it provide any statistical test or sensitivity analysis. While computing empirical averages as proxies for expectations is common in smoothed analysis papers, the leap from "here are the empirical averages" to "the data satisfies the model assumptions" is unsubstantiated. The paper should at minimum discuss this gap explicitly or provide supplementary evidence (e.g., adding synthetic noise to test robustness).

### Minor

3. **Experimental results lack error bars or measures of variability.** Every point in Figure 1 is reported as the average of 20 runs, but no error bars, confidence intervals, or standard deviations are shown. Given the stochastic nature of sampling (especially at small β), it is impossible to judge whether observed differences between methods are statistically significant or simply noise. This is particularly important for the paper's central empirical finding (uniform > weighted), whose reliability is unclear without some measure of variance.

4. **The ε notation across theorems is not cleanly distinguished.** Theorem 1.3 uses ε for the oracle accuracy parameter (controlling the additive error ε/γ), while Theorem 1.4 uses ε for the final approximation error. These are related by a factor that depends on k or kp. While the derivation in the text explains the relationship (line 84–85), the theorem statements themselves reuse the same symbol for different quantities. Distinguishing them (e.g., δ for oracle error, ε for final error) would improve clarity.

### Trivial

5. The meta greedy algorithm (Algorithm 1) defines Aⱼ ⊆ E\Sⱼ as "some constraint that limits the choice of potential elements" without explicit instantiation in the main text for the p-system case. While this level of abstraction is standard for a meta-algorithm, a concrete example in the text would aid reproducibility.

## Nice-to-Haves

- Including results for the Rafiey & Yoshida (2022) sparsifier baseline (in addition to Kenneth & Krauthgamer, 2023) would strengthen the empirical comparison.
- The combination of mini-batch with stochastic-greedy is mentioned in the text but not experimentally demonstrated. Showing results for this variant would further demonstrate the generality of the mini-batch approach.
- A discussion of the cost of computing marginal gains (hat{F}^j) for uniform mini-batch relative to the sparsifier would be helpful for practitioners.

## Removed Points
These points are flagged to be removed, treat them with caution

- **"The combination of mini-batch with stochastic-greedy is mentioned but no results are shown"** — The paper states (line 187) that both lazy-greedy and stochastic-greedy variants were compared; results are in Figure 1 (which is an image and cannot be fully verified from the text alone, but the paper claims the comparison was made).
- **"The paper does not address the cost of computing the marginal gains"** — This is a minor implementation detail that does not affect the paper's core claims.
- **"The meta greedy algorithm's definition of A_j is left vague"** — This level of abstraction is standard for a meta-algorithm and is adequately described.
- **Weaknesses about missing appendix, proofs, or references** — These sections are stripped by the PDF parser and exist in the original submission.
- **Pure formatting/style nitpicks** — These are parser artifacts, not author errors.

## Novel Insights

The reviewers converge on an important observation that the paper itself does not fully articulate: the paper contains *two* distinct contributions that should be evaluated separately — (a) the weighted mini-batch vs. sparsifier comparison (where the theoretical story is mixed and the claims are overblown) and (b) the uniform mini-batch + smoothed analysis story (which is genuinely novel and well-supported by the experiments modulo the validation caveats). The surprising empirical success of uniform sampling is the paper's real contribution, and the smoothed analysis provides a principled framework for why this can happen. The weighted mini-batch claims serve more as motivation/setup than as the core contribution, and the paper would benefit from restructuring its narrative to reflect this priority.

## Suggestions

1. **Qualify the weighted mini-batch claims** in the abstract and introduction to explicitly state that the theoretical improvement holds for bounded curvature, and clarify the tradeoffs for the unbounded case.

2. **Add error bars** to all experimental plots (shaded standard deviations or standard errors over the 20 runs) so readers can assess the reliability of the observed differences.

3. **Strengthen the smoothed analysis validation** by either (a) adding synthetic noise to the data to demonstrate robustness, (b) measuring and reporting dependency among the f^i values, or (c) at minimum adding a clear discussion of the gap between "empirical average" and "expectation" and why the observed values are nonetheless informative.

4. **Distinguish notation** in the theorem statements (e.g., use δ for oracle accuracy and ε for final approximation error) to avoid confusion.

## Score and Decision

This paper presents a novel mini-batch algorithm for decomposable submodular maximization, with the surprising empirical finding that uniform sampling outperforms weighted sampling. The smoothed analysis framework is a genuine conceptual contribution that goes beyond worst-case analysis. However, the paper's central theoretical claim about weighted mini-batch is overstated in the abstract and introduction without the necessary qualifications about curvature, and the smoothed analysis validation relies on an indirect empirical check that does not verify the distributional assumptions. The absence of error bars further weakens confidence in the experimental findings. These issues are addressable but nontrivial.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Borderline Accept</orange>