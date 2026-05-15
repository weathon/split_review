Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes Stochastic Gradient Discrete Langevin Dynamics (SGDLD), the first practical method for simulating discrete Langevin dynamics when the energy function depends on an expectation over a large dataset. Two key techniques are introduced: (1) a gradient caching scheme that reuses mini-batch evaluations across consecutive stays at the same state to reduce bias, and (2) a modified Polyak step size adaptation to handle the enormous variance in jump rates across states and mini-batches. Experiments span synthetic validation, Bayesian logistic regression, stochastic facility location, approximate computing, and prompt tuning.

## Strengths

- **Addresses an important and genuinely underexplored problem**: Stochastic MCMC in discrete spaces is a natural next step after the success of SGLD/SGHMC in continuous spaces, but the paper correctly identifies that naive migration fails due to non-exchangeability of the ratio estimator and the exploding variance of jump rates. The problem framing (Section 3) is clear and well-motivated.

- **Gradient caching is a creative and practical solution to the bias problem**: The cache (Equation 12) accumulates mini-batch estimates across consecutive rejected proposals, effectively expanding the batch size at no extra computational cost. The ablation study (Figure 2) confirms that SGDLD's total variation decreases with step size while the no-cache variant's does not, providing empirical evidence for asymptotic unbiasedness that is consistent with Proposition 4.1.

- **Polyak step size adaptation convincingly addresses the variance issue**: Figure 1 shows that jump rates across mini-batches can differ by a factor of 10^30, making fixed step sizes impractical. The adapted step size (Equation 14) demonstrably stabilizes sampling — SGDLD-noP fails to produce reasonable solutions in three of the five experimental settings (Section 6), which is a strong ablation result.

- **Consistent empirical outperformance across diverse real-world applications**: SGDLD outperforms Gurobi and SLS in stochastic facility location across all problem sizes (Table 1), achieves comparable or better results than learning-based methods in approximate computing with orders-of-magnitude fewer evaluations (Table 2), and obtains higher CLIP similarity than continuous relaxation in prompt tuning (Table 3).

- **Honest discussion of limitations**: Section 7 explicitly acknowledges that asymptotic unbiasedness requires exact probability ratios and that unbiasedness is not guaranteed when gradient approximations are used. This transparency is commendable.

## Weaknesses

### Fatal
None.

### Major

1. **Proposition 4.1 (asymptotic unbiasedness) is stated without substantive justification in the main text, and the remark about an equivalent memoryless Markov chain is unsupported.** The paper's central theoretical claim — that the caching scheme yields asymptotic unbiasedness as the step size goes to 0 — is presented as a proposition with a one-line statement and a brief unsupported remark. The claim is non-trivial because the caching scheme introduces history dependence in the transition kernel (the cache persists across stays at the same state). The remark that "the sampling process above has an equivalent form of memoryless Markov chain" is critical to the argument but receives no justification in the main text. While a full proof may exist in the appendix, the main text should at minimum sketch the key steps or intuition, given that this is the paper's core theoretical contribution.

2. **Experimental evaluation lacks wall-clock time comparisons and has gaps in baselines.** The Bayesian logistic regression experiment normalizes the x-axis as "320 updates for stochastic methods vs. 2 updates for DLMC" — this is informative as a computational budget calibration, but wall-clock time is the standard in the SGLD literature for establishing practical efficiency. The prompt tuning experiment (Table 3) compares SGDLD only to continuous relaxation, not to any discrete optimization or discrete MCMC baseline for prompt search. The approximate computing results (Table 2) are reported without variance or confidence intervals, unlike Table 1 and Table 3. These gaps weaken the empirical case that SGDLD is practically superior to alternatives.

### Minor

1. **The Polyak step size in practice uses a gradient approximation for Z(x) (line 206), but the impact of this approximation on sampling quality is not analyzed.** The paper acknowledges this gap and cites Grathwohl et al. (2021) for the approximation, and the main theoretical claim (Proposition 4.1) does not depend on the Polyak step. However, since the step size adaptation is advertised as a core contribution, understanding how the approximation affects the effective step size and whether it introduces systematic bias would strengthen the paper.

2. **The claim of being the "first practical method for stochastic distribution sampling in discrete spaces" is slightly overbroad.** The paper itself cites Zhang et al. (2022) as having attempted a stochastic generalization of DLP, and mentions pseudo-marginal MCMC as a comparison baseline (line 279). The contribution is genuinely novel — handling the case where no unbiased estimator of the rate matrix exists — but the "first" framing could be softened.

3. **The Gaussian-Bernoulli synthetic experiment uses a state space of size 2^4 = 16.** While this is appropriate for validating asymptotic unbiasedness against tractable ground truth, a larger synthetic problem (e.g., d=20) would better demonstrate scaling behavior and the effectiveness of caching as state space grows.

4. **The Polyak step size schedule (threshold h* and schedule h_t) is not discussed in terms of sensitivity.** It would be helpful to know how robust results are to the choice of these parameters, especially since the schedule is "hand designed" (line 200).

### Trivial
None.

## Nice-to-Haves
- A sketch of the proof of Proposition 4.1 in the main text, even if the full proof is in the appendix.
- Wall-clock time or number of data evaluations as the x-axis in Figure 3, rather than (or in addition to) normalized steps.

## Removed Points
- **"No proof is given for Proposition 4.1 (neither in the main text nor in the omitted appendix)"** — Removed per the rule that the parser strips appendix content; the proof exists in the original submission.
- **"The ratio of averages remains a biased estimator even as cache size m grows (Jensen's inequality applies to g inside the ratio)"** — Removed as factually incorrect: as m→∞, the cached ratio converges almost surely to the true ratio by the law of large numbers, and g is continuous, so g(π̂(y)/π̂(x)) → g(π(y)/π(x)). The estimator is consistent, even if biased for finite m.
- **"No comparison to pseudo-marginal MCMC or debiasing approaches"** — Removed because the paper explicitly states (line 279) that such comparisons were conducted (likely in the appendix, which was stripped).
- **"The gradient approximation for discrete spaces is stated without justification"** — Removed because it is standard in the literature and the paper cites Grathwohl et al. (2021).
- **"SGLD convergence derivation (Equations 2-4) is not rigorous"** — Removed because this is standard exposition in the SGLD literature (Welling & Teh, 2011) and not part of the paper's contribution.
- **"Missing related works"** — Removed per instructions (cannot confirm existence of external sources).
- **Various formatting/style nitpicks** — Removed per instructions (parser artifact issues).

## Novel Insights
The reviews surface a tension that the paper itself does not fully resolve: the caching scheme is intuitively plausible (accumulate more mini-batches → better estimate → asymptotically exact as ε→0), but making this rigorous requires handling the history-dependent transition kernel, which is non-trivial compared to the continuous SGLD case where the Wiener process dominates the noise. The paper's remark about an "equivalent memoryless Markov chain" is the key missing link. Additionally, the reviews highlight that the paper operates at two different levels of rigor — the theoretical framing assumes exact probability ratios, while the practical implementation (including the Polyak Z(x) approximation) operates with gradient approximations, and the gap between these is acknowledged but not analyzed.

## Suggestions
1. **Provide a proof sketch for Proposition 4.1 in the main text.** The key intuition is that as ε → 0, the probability of staying at the same state approaches 1, causing the cache size m to grow, and the law of large numbers drives the cached ratio to the true ratio. Explaining why the history dependence does not break convergence (or providing the equivalent memoryless chain construction) is essential.
2. **Add wall-clock time comparisons** for at least two of the real-world experiments (e.g., Bayesian logistic regression and facility location) to ground the efficiency claims in a practically meaningful metric.
3. **Include a larger synthetic experiment** (e.g., d=20 or d=50 Ising model) where ground truth can be approximated via long runs, to demonstrate scaling of the caching benefit.
4. **Soften the "first practical method" claim** to acknowledge that Zhang et al. (2022) and pseudo-marginal approaches are relevant prior work, and clarify the specific setting (no unbiased rate estimator available) where SGDLD is the first viable approach.
5. **Add variance/standard deviation to Table 2** for consistency with the other experimental tables.

## Score and Decision

The paper addresses a genuine gap — stochastic MCMC for discrete spaces — with a creative algorithm (caching + Polyak adaptation) and demonstrates consistent empirical improvements across diverse applications. The weaknesses are real but not fatal: the main theoretical claim is plausible but under-justified in the main text, and the experimental evaluation would benefit from wall-clock timing and a few additional baselines. The paper's core contribution is substantial enough that these issues can be addressed in a revision.

**Score: 6.0**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>