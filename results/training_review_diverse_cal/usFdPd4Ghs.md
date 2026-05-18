I now have a thorough understanding of the paper and all the reviews. Let me produce the final consolidated review.

## Summary

This paper develops a deep α-stable kernel process (Dα-KP) that arises as the infinite-width limit of Bayesian neural networks with infinite-variance prior weights at each layer. The core contribution is a recursive formula (Theorem 1) linking conditional covariance kernels across layers by combining Cho & Saul's recursion with the conditionally Gaussian representation of elliptical α-stable vectors. This extends prior work by LoriaBhadra from shallow, exponentially complex computations to deep architectures with polynomial complexity in kernel space, and provides a principled stochastic kernel (for α < 2) that enables data-dependent feature learning without the artificial noise injection required by deep inverse Wishart processes. Empirical results on discontinuous functions (1d, 2d, 10d) and UCI datasets show competitive or superior predictive performance relative to GP, DIWP, and NNGP baselines.

## Strengths

- **Kernel-space recursion overcomes the exponential complexity bottleneck of prior stable methods.** The paper explicitly shows that LoriaBhadra has O(n^{I+2}) complexity (limited to shallow networks), while the proposed method works in kernel space with a recursive formula that avoids combinatorial enumeration (Section 1.1, lines 20-21). This enables scaling to ten-dimensional simulations and UCI datasets with I=13, where the Stable method is infeasible (Tables 1 and 3, lines 166-171, 212-217).

- **Provides a novel recursive formula for conditional covariance kernels under infinite-variance priors (Theorem 1).** Theorem 1 (lines 54-66) gives explicit expressions for Σ^{(ℓ)}_{k,h} as a function of Σ^{(ℓ-1)} and the positive stable scale s^{(ℓ-1)}_+, for activation functions g_δ (step and ReLU). This is a genuine extension of Cho & Saul (2009) to the infinite-variance regime, and the key enabler of the entire inference procedure.

- **Establishes that the kernel is stochastic for α < 2, enabling feature learning absent in deep GPs.** Proposition 2 (lines 106-113) proves that the posterior distribution of features depends on observations only when α < 2. Figure 4 (lines 227-240) confirms non-Gaussian posterior features via heavy tails and q-q plots for the Boston dataset, empirically supporting that representation learning occurs.

- **Provides a principled alternative to artificial noise injection methods (DIWP).** The paper argues (Section 1, lines 16-18) that the stochastic kernel arises naturally from infinite-variance priors rather than from ad hoc noise, resolving a conceptual weakness of DIWP while matching or exceeding its predictive performance.

- **Computational gains are substantial and demonstrated.** The Stable method is limited to 1d and 2d; Dα-KP scales to 10d with 300 training points and UCI datasets with n up to 769, achieving competitive or best predictive accuracy across settings (Tables 1 and 3).

## Weaknesses

### Fatal
None.

### Major

- **The "deep" framing is not supported by the empirical evidence.** Despite the title, abstract, and contributions emphasizing a *deep* kernel process, the principal numerical comparisons (Tables 1 and 3, Figures 2-3) all use L=2 (one hidden layer). Table 2 (lines 179-194) systematically investigates depth and finds no meaningful improvement: RMSE is nearly constant from L=2 through L=16 across all three simulation settings. The authors acknowledge this and conjecture the stable process captures a "function class rich enough" with one hidden layer. This interpretation may be correct, but it creates a clear mismatch between the paper's advertised novelty ("deep") and what is empirically demonstrated. The paper either needs (a) a problem setting where depth demonstrably matters, or (b) a recasting of its claims to reflect that the deep construction is theoretically valid but not essential for the tasks evaluated. As the paper stands, the empirical contribution effectively reduces to a shallow stable kernel process.

### Minor

- **Theorem 1 is stated without any derivation sketch in the main text.** The recursive kernel formula is the paper's central theoretical contribution, yet the main text provides only the statement (lines 54-66) and asserts it follows from Cho & Saul's formulas under the conditionally Gaussian representation. No sketch of how the positive stable scale s^{(ℓ-1)}_+ enters the recursion, or why the resulting Σ^{(ℓ)} is positive definite with probability 1, is given. While a full proof presumably exists in the supplementary material (stripped by the parser), the main text would benefit from at least a brief outline of the key step, so that a reader can assess the argument without consulting the supplement.

- **The feature learning claim lacks direct evidence.** Proposition 2 shows theoretically that the posterior of features depends on the data for α < 2, and Figure 4 shows non-Gaussian marginal distributions. However, the non-Gaussianity could arise entirely from the prior — the hierarchical stable construction produces heavy tails unconditionally. The paper does not compare the posterior features to the prior features, nor does it show that feature distributions adapt differently across datasets (e.g., different patterns under true data vs. shuffled labels). Demonstrating that the posterior of the features differs from the prior would substantially strengthen this claim.

- **No sensitivity analysis for the key hyperparameters α and δ.** All experiments fix α=1 and δ=1 (ReLU). Since α directly controls tail behavior and the degree of stochasticity (α=2 recovers the deterministic GP), the choice is likely important. Showing performance across α ∈ {0.5, 0.8, 1.0, 1.5, 1.9} on at least one synthetic function would clarify whether improvements are robust or specific to the chosen setting. Similarly, δ=0 (step) is theoretically covered but never used empirically.

- **MCMC details relevant to reproducibility are deferred to the supplementary.** Algorithm 1 (lines 85-101) calls subroutines "Algorithm s_given_s" and "Algorithm s_given_y" without describing them in the main text. MCMC diagnostics (acceptance rates, mixing, effective sample sizes) are absent. While these details likely exist in the appendix (stripped by the parser), the main text should provide at least a high-level description of how the conditional updates for the positive stable variables are implemented, since the sampling procedure is central to reproducibility.

- **The comparison to the Stable method is inherently limited.** The paper's main motivation is that the Stable method (LoriaBhadra) is infeasible beyond 1d/2d, and Dα-KP is shown to be competitive where both methods run (slightly worse in 1d/2d) and best in 10d where no competitor exists. This asymmetry makes the comparison informative but also means that for the higher-dimensional setting the paper emphasizes, there is no independent baseline from the same family.

### Trivial

- The half-Cauchy prior on σ² is mentioned (line 84) but its hyperparameters (scale parameter) are not specified.
- The running time comparison with the Stable method is referenced to the supplementary (line 138, supp:timing_results) but absent from the main text.

## Nice-to-Haves

- A sensitivity sweep over α (e.g., on the 1d jump function) to show how performance degrades as α → 2 (GP limit).
- A comparison of posterior vs. prior feature distributions to more convincingly demonstrate feature learning (e.g., using permuted labels).
- An experiment designed specifically to benefit from depth (e.g., a hierarchically composed function), to validate the "deep" aspect of the method.
- MCMC diagnostics such as trace plots or effective sample sizes for at least one representative run.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Mutual information analysis stands alone; not connected to posterior inference."** The mutual information analysis (Figure 1) is presented to illustrate the long-memory property of α-stable processes (slower decay for smaller α), which directly motivates the method's ability to capture distant relationships that GPs model as nearly independent. This is a supporting analysis, not disconnected. *Removed: the paper's own connection is coherent.*

- **"The Stable method's exponential complexity formula is stated without citation or derivation."** The paper provides both a citation to LoriaBhadra and an intuitive explanation in terms of combinatorial enumeration of separating hyperplanes (lines 20-21). *Removed: factually incorrect — the explanation is present.*

- **"The paper does not mention software availability or implementation plans."** This is a generic wish that applies to many papers; lack of a code release plan is not a substantive weakness of the contribution. *Removed: generic and not a core flaw.*

- **Criticism that Dα-KP's 10d results are "circular" because no competitor exists.** The paper transparently reports results, shows Dα-KP is competitive with Stable where both run, and then extends to settings where Stable cannot operate. This is exactly the scientific contribution — enabling computation where none was possible — not a circular argument. *Removed: mischaracterization of the contribution.*

## Novel Insights

Beyond the paper's own contributions, the reviews surface an important tension: the paper's theoretical machinery supports arbitrary depth, but the empirical evidence suggests the shallow version captures the benefits. This raises a genuine question for the community — whether deep stable kernel processes exhibit a "depth plateau" analogous to the "trainable depth" barrier in deterministic neural networks (Schoenholz et al., 2017), or whether there exist function classes (e.g., truly hierarchical compositions) where depth provides a clear advantage. The paper's honest reporting of this finding is itself valuable, even if it undercuts the "deep" branding. The feature learning critique — that non-Gaussianity of the posterior features is necessary but not sufficient evidence of data-dependent representation learning (since the prior already produces heavy tails) — is a sharp methodological point that applies broadly to work on stochastic kernel processes.

## Suggestions

1. Add a derivation sketch for Theorem 1 in the main text (2-3 lines explaining how the Cho-Saul formula adapts under the conditionally Gaussian representation).
2. Either add an experiment where depth matters (e.g., a hierarchically composed target function), or adjust the title/claims to more accurately reflect the empirical scope.
3. Include a sensitivity analysis for α on at least one synthetic dataset.
4. Compare posterior features to prior features (or to posterior under shuffled labels) to strengthen the feature learning demonstration.
5. Specify half-Cauchy hyperparameters and provide basic MCMC diagnostics.

## Score and Decision

This paper makes a genuine theoretical contribution — extending Cho & Saul's kernel recursion to infinite-variance priors — and achieves dramatic computational gains over the only prior viable stable process method. The empirical results are solid on discontinuous functions where GP-based methods are structurally misspecified. The main weaknesses are (a) the mismatch between "deep" framing and the empirical finding that depth provides no benefit, and (b) some presentation gaps (derivation sketch, feature learning evidence, hyperparameter sensitivity) that are addressable in revision. These are real but not fatal; the theoretical contribution and computational advances stand on their own.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>