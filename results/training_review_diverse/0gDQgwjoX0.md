Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper proposes Stochastic Gradient Discrete Langevin Dynamics (SGDLD), the first practical algorithm for MCMC sampling from discrete probability distributions defined by expectations over large datasets. The method addresses two fundamental obstacles: (1) bias in naive stochastic gradient estimators for discrete Langevin dynamics (since the ratio of expectations does not equal the expectation of ratios), and (2) extreme variance in jump rate magnitudes across states and mini-batches. SGDLD introduces gradient caching (reusing mini-batch estimates when the state does not change, making the estimator asymptotically unbiased) and a Polyak-style state-dependent step size that normalizes simulation time by the local jump rate. Experiments on synthetic tasks (Gaussian-Bernoulli, Bayesian logistic regression) and three real-world applications (stochastic facility location, approximate computing, prompt tuning) demonstrate the method's effectiveness.

## Strengths

- **Novel and well-motivated algorithmic contributions.** The paper clearly identifies the two core obstacles to stochastic-gradient MCMC in discrete spaces — bias from non-exchangeability of the ratio and expectation (Section 3.2, Eq. 10), and variance in jump rate magnitudes (Figure 1 shows jump rates spanning 30 orders of magnitude) — and proposes clean, intuitive solutions for each. Gradient caching (Section 4.1) and Polyak step-size adaptation (Section 4.2) directly target these challenges.

- **Ablation studies cleanly isolate each contribution.** The variants SGDLD-noC (no caching) and SGDLD-noP (no Polyak step size) are evaluated across multiple tasks. Figure 2 is the most critical evidence: SGDLD's total variation decreases monotonically with step size (consistent with asymptotic unbiasedness), while SGDLD-noC fails to improve and even worsens — directly confirming that caching corrects the bias. SGDLD-noP is shown to underperform or fail entirely in multiple settings.

- **Diverse real-world applications.** The method is applied to three distinct practical problems — stochastic integer programming (facility location), approximate computing (AxC), and prompt tuning for text-to-image models — demonstrating impact beyond synthetic benchmarks. In the approximate computing task, SGDLD achieves comparable results to learned methods with 10k evaluations versus 100 million for training data alone.

- **Honest about limitations.** The discussion (Section 7) openly acknowledges that SGDLD is an unadjusted sampler requiring exact probability ratios for unbiasedness, and that variance reduction and MH correction steps are natural future work. This candor strengthens rather than weakens the contribution.

## Weaknesses

### Fatal

None.

### Major

- **Theoretical analysis of the caching scheme is incomplete in the main paper.** Proposition 4.1 asserts asymptotic unbiasedness as step size decreases to zero, but the paper provides no analysis of the non-Markovian dynamics introduced by the growing cache (which resets upon a jump) or the coupling between the cache size and the step size schedule. The remark that the process "has an equivalent form of memoryless Markov chain" (line 187) is asserted without any justification or sketch of the equivalence. While the proof may exist in the appendix, the main paper does not convey how the key technical challenges — the state-dependent memory, cache resetting, and interaction with the Polyak step size — are resolved. This gap weakens the paper's central theoretical claim.

- **Missing experimental details that affect reproducibility and evaluation.** Several critical parameters are not reported: (i) the dataset dimensions (number of features *d* and samples *m*) for the Bayesian logistic regression experiment (Section 6.2); (ii) the inverse temperature *β* values used to convert the facility location and approximate computing optimization problems into sampling problems (Sections 6.3–6.4); (iii) the concrete annealing schedule for *h<sub>t</sub>* in the Polyak step size (the paper only says "set a threshold *h\** and gradually decrease *h<sub>t</sub>*" without specifying the rule). The paper also contains a dangling claim: "We conducted extra experiments to show the fast mixing of SGDLD and demonstrate its advantage compared to more baselines, such as pseudo marginal MCMC" (line 279), but no results are shown.

### Minor

- **Limited baselines in several experiments.** The prompt tuning experiment (Table 3) compares SGDLD only to continuous relaxation and SGDLD-noC. Additional comparisons with random search, evolutionary methods, or other discrete MCMC samplers would strengthen the case. The facility location experiment (Table 1) compares against Gurobi with SAA and stochastic local search, but the claim that SGDLD "significantly outperforms" is not backed by statistical significance testing — the reviewer correctly notes that standard deviations appear to overlap for some settings. Confidence intervals or paired tests would be informative.

- **The calibration of computational cost in Figure 3 is not fully justified.** The paper calibrates steps as "320 updates for stochastic methods and 2 updates for DLMC" but provides no justification for this specific ratio (which presumably depends on the unreported dataset dimensions). Wall-clock time or total energy evaluations would be a more transparent and verifiable comparison metric.

- **No analysis of the Polyak step-size approximation error.** The method for computing *Z(x)* uses a gradient approximation (following Grathwohl et al., 2021), but the paper provides no analysis — theoretical or empirical — of how approximation errors in the jump rate affect the step-size schedule or mixing. The statement "we find this is sufficient to stabilize the sampling process" is an empirical observation without supporting sensitivity analysis.

- **The Gaussian-Bernoulli toy (Section 6.1, 16 states) uses a state space too small to stress-test the caching scheme** (the cache can easily saturate). While this experiment serves its purpose as a verification of asymptotic unbiasedness, a larger synthetic problem would strengthen the validation.

### Trivial

- The decomposition *N = N₁N₂* in Equation 9 is stated without explanation of the roles of *N₁* and *N₂* — this is explained in the subsequent text but the equation placement could be clearer.

## Nice-to-Haves

- A discussion of the memory overhead of the caching scheme in larger state spaces (neighborhood size grows linearly, and the cache persists across rejected steps).
- Reporting inverse temperature *β* values for the optimization-to-sampling transformations.
- A sensitivity analysis showing how the gradient approximation error in *Z(x)* affects mixing rates.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"First practical method" claim too strong.** The reviewer objected to "first practical method" given Zhang et al. (2022). However, the paper explicitly acknowledges Zhang et al. (2022) and explains why their assumption (unbiased estimator of the rate matrix exists) is generally unattainable. The claim is defensible in context.

2. **Notation confusion in Section 4.1 (Eq. 12).** The reviewer found the cache notation ambiguous, but the paper's description is logically consistent: the cache stores ψ(·, ξₖ) for all neighbors *z ∈ N(x)* for each mini-batch *ξₖ*, and the ratio averages over all cached mini-batches. The notation is dense but unambiguous.

3. **SGDLD-noP tuning may unfairly penalize it.** The reviewer argued that tuning SGDLD-noP to match SGDLD's jump distance could be unfair. Matching the average jump distance is a standard way to control for exploration rate, making this a fair comparison that arguably favors the baseline by giving it the same explorability.

4. **Missing related works (Titsias & Yau, 2017; Lyne et al., 2015).** Rule prohibits mentioning missing related works without external confirmation.

5. **Gibbs comparison "odd" in Section 6.1.** The comparison to a mini-batch-based Gibbs sampler is a reasonable baseline for a verification experiment; the small state space (16 states) is intentional for exact TV computation.

6. **Low variance in prompt tuning suggests saturated metric or non-independent runs.** This is speculation without evidence of flawed methodology.

## Novel Insights

The reviews surface a key tension that the paper itself partially acknowledges but does not fully resolve: the caching scheme introduces non-Markovian dynamics (memory through the cache that resets upon jumps), yet the paper claims asymptotic unbiasedness without a detailed analysis of how this resetting mechanism affects convergence. The remark comparing to Hamiltonian Monte Carlo (which also has state-dependent momentum variables) is an intriguing analogy but is not developed. The strongest evidence for the method's correctness is not the theoretical proposition but the empirical demonstration in Figure 2, where total variation decreases monotonically with step size for SGDLD but not for SGDLD-noC — this is a rare case where an ablation study effectively substitutes for a missing convergence proof. However, the field would benefit from a rigorous non-asymptotic analysis of the cached estimator's bias in terms of step size and cache size.

## Suggestions

1. **Provide the theoretical sketch in the main paper.** Even if the full proof is in the appendix, the main text should explain how the non-Markovian dynamics (growing cache, resetting on jumps) are handled and what the HMC analogy means formally.

2. **Report all missing experimental parameters** (dataset dimensions, β values, annealing schedule for hₜ) either in the main text or in the appendix that reviewers can access.

3. **Add wall-clock time or total energy evaluations** for the Bayesian logistic regression experiment to make the computational comparison more transparent.

4. **Include confidence intervals or statistical significance tests** for the facility location results.

5. **Conduct a sensitivity analysis** for the gradient approximation used in the Polyak step size, showing how approximation error affects mixing rates.

## Score and Decision

The paper addresses a well-motivated and important problem (scaling gradient-based MCMC to discrete spaces with large-data energy functions) with novel algorithmic contributions (gradient caching + Polyak step-size adaptation) that are clearly explained and supported by ablation studies across multiple domains. The empirical evidence strongly supports the core claims, particularly Figure 2 which directly validates the caching scheme. The weaknesses — incomplete theoretical exposition in the main text, some missing experimental details, and limited baselines in certain experiments — are addressable and do not undermine the paper's central contribution. This is a solid paper with clear practical value.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>