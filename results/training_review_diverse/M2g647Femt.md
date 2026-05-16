## Summary

This paper proposes representing inequality constraints on deep learning models as Signed Distance Functions (SDFs), enabling efficient projection into solution regions and composition via boolean operations (union, intersection, negation) for inverse design tasks. Two algorithms are provided: a linear-time SDF algorithm for Shepard Interpolation Neural Networks (SINNs) motivated by Theorem 1, and a local-search (BFS-based) SDF algorithm for piecewise-linear (e.g., ReLU) networks. Experiments on MNIST, CelebA, and ZINC-250k with classifi-ers and regressors show that the framework outperforms guided gradient descent (GGD) in most settings, particularly with SINN models.

---

## Strengths

1. **Novel framework with an appealing conceptual formulation.** The idea of representing inequality constraints on model outputs as SDFs and composing them via CSG boolean operations is well-motivated and clearly explained. This provides a principled alternative to ad-hoc loss-function engineering for inverse design tasks.

2. **Two concrete algorithmic instantiations covering complementary model families.** The paper identifies two broad model classes — smooth asymptotic functions (SINNs) and piecewise-linear networks (ReLU) — and proposes distinct algorithmic strategies for each, rather than offering a single fragile approach. The SINN algorithm is claimed to be linear-time, and the ReLU algorithm uses a domain-decomposition local search.

3. **Consistent outperformance of guided gradient descent on MNIST and CelebA.** In both single-constraint and multi-constraint (intersection) settings, composable constraints achieve substantially higher oracle agreement rates than GGD, which frequently produces adversarial samples. On CelebA multi-constraint tasks, SINN-based composable constraints reach near-perfect agreement while GGD hovers below 50%.

4. **Empirical validation across three diverse domains.** The method is demonstrated on image generation (MNIST, CelebA) and molecular design (ZINC-250k), showing the framework is not domain-specific. The confidence-based threshold adjustment (Eq. 13) for regression tasks is a nice practical addition.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1 is not properly justified, and its claimed implication is not convincingly established.** The theorem states that "a search algorithm need only search among the critical points and local extrema of M to compute the Signed Distance Function." The paper's argument is that each solution region contains at least one extremum, therefore enumerating extrema enumerates solution regions, therefore one can compute the SDF. The gap is that knowing which regions exist does not directly give the distance from an arbitrary point x₀ to the boundary of the nearest region; finding the closest boundary point requires solving a constrained optimization problem for which being near an extremum is neither necessary nor sufficient. The optimality condition for a boundary point x* closest to x₀ is (x* − x₀) ∥ ∇M(x*), not ∇M(x*) = 0. The paper provides no formal proof (the "proof" is an image/diagram) and does not bridge this gap. Since the SINN algorithm is presented as an application of Theorem 1, this undermines the theoretical foundation of the paper's first algorithmic contribution.

2. **Union and negation constraints are never tested experimentally, leaving the paper's central claim of composability unvalidated for all but one boolean operation.** The paper repeatedly emphasizes that SDF boolean operations (union, intersection, negation) enable arbitrary constraint composition. Yet every experiment uses only intersection (CelebA multi-constraint: Black Hair ∩ Male; ZINC multi-constraint: QED ∩ SAS). Union (e.g., "digit is 3 or 5") and negation (e.g., "not male") — the operations that make composition distinct from simply concatenating constraints — receive zero experimental validation. This is not a missing ablation; it is a hole in the core claim. The paper claims composability as its headline advantage over GGD, but the experiments never demonstrate it.

3. **The ReLU SDF algorithm is presented with no analysis of correctness, failure modes, or approximation guarantees.** The algorithm performs a BFS over linear domains, solving a quadratic program in each. The paper acknowledges that enumerating all domains is intractable but does not analyze when the local search will succeed or fail. The BFS may miss the optimal solution entirely if it lies in a domain not reachable via a chain of domains each intersecting the level set — a plausible scenario for non-convex piecewise-linear functions in high dimensions. The experimental evidence confirms the concern: on MNIST data-space ReLU, the method achieves only 32.4% agreement (per the reviewer, and the paper notes "the ReLU model is liable to generate adversarial samples"). Without any characterization of when the algorithm works, it remains a heuristic of unvalidated reliability, which weakens the paper's second algorithmic contribution.

4. **The ZINC experiments expose a large gap between latent-space and analytical agreement that is not adequately interrogated.** The paper reports that composable constraints achieve 95–100% latent oracle agreement but only 20–49% analytical oracle agreement (Tables 3, 4 — values from the reviewer, as table images are unavailable). The paper acknowledges the gap but does not analyze whether it stems from predictive model error, decoder error, or a fundamental limitation of the SDF approach when the predictive model is inaccurate. Since the confidence-based threshold adjustment (Eq. 13) is used but its effect is not reported separately, it is unclear whether the method is finding genuine solutions or merely exploiting inaccuracies in the learned emulator.

### Minor

1. **The role of the VAE in CelebA success is not isolated.** The CelebA experiments use a two-level VAE (TinyVAE + autoencoder) whose smooth latent space likely makes the SDF projection easier. The paper does not ablate the VAE's contribution, so it is unclear how much of the high agreement rate is due to the SDF algorithm vs. the favorable geometry induced by the VAE.

2. **The Log-Exp-Sum smoothing parameter β and its impact on solution quality are not analyzed.** The paper replaces hard min/max with a smooth approximation (Eq. 12) for gradient-based projection but does not discuss how β affects the quality of the pseudo-SDF composition or whether the approximation error matters in practice.

3. **The ReLU BFS adjacency details are underspecified for reproducibility.** The paper states that two operations are needed (identify the starting domain, find adjacent domains) but does not explain how adjacent domains are identified or how the domain graph is constructed efficiently. These details are essential for reproducing the algorithm.

4. **Only one baseline (GGD) is compared.** While GGD is the most relevant baseline for post-hoc inverse design, the absence of comparison to any other approach (e.g., augmented Lagrangian methods mentioned in the background, projected gradient descent, or simple penalty methods) makes it difficult to assess the method's practical advantages beyond the (undemonstrated) composability claim.

### Trivial
None.

---

## Nice-to-Haves

- A simple union experiment (e.g., "digit is 3 or 5" on MNIST) to validate the most novel part of the framework.
- An ablation study isolating the VAE's contribution from the SDF algorithm's contribution on CelebA.
- An analysis of how the Log-Exp-Sum parameter β affects convergence and solution quality.
- Runtime/complexity analysis for both algorithms in the main text.

---

## Removed Points

- **Algorithm 1 not detailed in text**: Removed per hard rule — the algorithm likely appeared in a figure or appendix stripped by the parser.
- **The "introduction is not directly supported by Figure 3" type sentence-level pedantry**: Removed as trivial nitpicking that does not affect the contribution.
- **"Discussion of generative models is thin; diffusion guidance should be mentioned"**: The paper already discusses diffusion models and explains why they are not easily combined with composable constraints. This is a scope-creep request.
- **"Missing comparison to augmented Lagrangian, penalty methods, projected gradient descent as baselines"**: The paper mentions augmented Lagrangians as part of its own SINN algorithm construction, not as a competing baseline. GGD is the standard baseline for post-hoc inverse design; requesting additional generic optimization baselines amounts to scope creep.
- **Strength Finder's claim about "theoretical foundation for the SINN SDF algorithm"**: This strength conflicts with the verified weakness about Theorem 1's insufficient justification. Per the rule that when a strength and weakness disagree, the weakness wins, this claimed strength is removed.
- **Generic strengths from Strength Finder** (e.g., "this paper addressed an important problem"): Removed as lacking specific content.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Provide a correct and rigorous justification for Theorem 1, or remove it.** If the SINN algorithm does not actually depend on the theorem, state that clearly. If it does, either provide a proof or substantially revise the claim to match what can actually be shown (e.g., "each solution region contains an extremum, which can serve as an initialization point for a local projection").

2. **Test at least one union constraint and one negation constraint.** Without this, the paper's headline contribution is unsubstantiated. A simple MNIST union experiment ("class 3 or class 5") would directly validate the core composability claim.

3. **Characterize when the ReLU BFS algorithm can be expected to succeed or fail.** At minimum, provide diagnostic criteria for failure, or replace the heuristic with a provably correct (if more expensive) approach for small networks.

4. **Analyze the ZINC latent-analytical gap more carefully.** Separate the effects of predictive model error, decoder error, and SDF projection error. Report the effect of the confidence threshold α separately.

---

## Score and Decision

This paper introduces a conceptually appealing framework for constraint satisfaction in inverse design, and the empirical results on SINN models are promising. However, the paper has three structural weaknesses that prevent acceptance in its current form: (1) Theorem 1, which motivates the SINN algorithm, is not correctly justified and contains an unbridged logical gap between enumerating extrema and computing the SDF; (2) the ReLU algorithm is presented without any correctness analysis or failure-mode characterization, and the experimental evidence (32.4% agreement on MNIST data-space) suggests it often fails; (3) the paper's central claim of boolean composability is only tested for intersection — union and negation are never demonstrated. These are not presentation issues; they are gaps in the core contributions.

The idea has merit and could form the basis of a strong paper, but it needs substantial revision before meeting the acceptance bar.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>