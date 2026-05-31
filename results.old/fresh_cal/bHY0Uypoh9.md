Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes DREXEL and DREAM, two samplers that integrate replica exchange MCMC with gradient-based discrete samplers (GDS) to improve exploration in non-convex discrete energy landscapes. The method runs two GDS chains at different temperatures/step sizes and enables sample swaps via a custom mechanism (Equation 10) designed to preserve detailed balance in discrete spaces. DREAM additionally applies Metropolis-Hastings corrections. The paper provides a theoretical result (Theorem 1) on reversibility and asymptotic convergence for log-quadratic distributions, and evaluates the method on 2D synthetic tasks, Ising models, RBMs, and Deep EBMs.

## Strengths

- **First application of replica exchange to gradient-based discrete sampling.** The paper correctly identifies that replica exchange MCMC has not been studied in the context of discrete GDS (Section 2). The integration is a natural and well-motivated extension that addresses a real limitation of existing discrete samplers: stagnation in local modes.

- **Consistent and substantial empirical gains across multiple benchmarks.** Across four distinct task families, DREAM (the MH-corrected variant) achieves the best performance by all reported metrics. The improvements are particularly large on the Deep EBM task (Table 2): on Omniglot, DREAM (-88.47 nats) improves over DMALA (-95.13) by ~6.7 nats, and on Caltech Silhouettes by ~15 nats. The synthetic experiments (Table 1, Figure 2) show DREAM recovers modes that DMALA misses entirely. These results are consistent and non-trivial.

- **Computationally efficient design.** The method inherits the factorized coordinate-wise updates from prior GDS work (Equation 7→8), so per-iteration cost remains O(d). Running two chains instead of one is the primary overhead, which is modest relative to the exploration gains demonstrated.

## Weaknesses

### Major

- **The swap mechanism (Equation 10) lacks rigorous justification.** The paper introduces a non-standard swap probability that conditions on *both* the current and previous samples. The justification is one paragraph of intuition (lines 137–143): "we must maintain detailed balance not only between the low-temperature and high-temperature samplers but also between the current and next output samples." No formal proof of detailed balance preservation is provided, no counterexample shows why the standard swap (Equation 3) fails in discrete spaces, and the argument that "previous samples are treated as constants during the swap" (line 143) is asserted but not formally substantiated. Theorem 1 does not specifically verify the swap mechanism — it proves reversibility of the *overall* DREXEL chain on log-quadratic distributions, but does not isolate and validate the swap's role. Given that the swap is the central algorithmic novelty (listed as Contribution 2), this thin justification is a significant gap. Since neither the standard swap (Equation 3) nor the bias-corrected swap (Equation 9) under a standard detailed-balance analysis would condition on previous samples, the burden is on the authors to explain why the standard analysis breaks and how their fix restores it.

- **Theoretical claims outpace what is proven.** The abstract states that the samplers "exhibit faster mixing than a single GDS," and the conclusion repeats this (line 288). Yet Theorem 1 only shows (a) DREXEL is reversible for log-quadratic distributions, and (b) its stationary distribution converges weakly to the target as step sizes → 0. This is an asymptotic consistency result — it says nothing about *mixing rate*, let alone faster mixing relative to a single GDS. No quantitative bound, spectral gap analysis, or even empirical ESS/autocorrelation measurement is provided to substantiate the "faster mixing" claim. The paper should either prove a mixing bound or qualify the claim as an empirical observation.

- **Incomplete definition of the swap acceptance probability.** The paper states the swap probability is "ρ min{1, S̃(...)}" (line 58) and later refers to "probability ρS̃" (line 221), but never specifies whether ρ is the actual swap acceptance probability or a scaling factor, nor how ρ is set. The swap probability expression appears to be ρ·min{1, S̃(...)} based on the parallel with standard reMCMC, but the details matter for understanding the algorithm's behavior.

### Minor

- **Confusing notation in the synthetic experimental setup.** The paper defines the state space as Θ = {1,2,…,N}^d with N=256 and d=101×101 (line 235). A space of size 256^10201 cannot be exhaustively enumerated for KL/MMD computation as described. The "2D" problem description, the 101×101 value, and the visualizations (Figure 2) suggest the actual setup may be a discretized 2D grid, but the notation is inconsistent and the procedure for computing KL and MMD in such a space is not explained. This does not invalidate the results (the visualizations alone convincingly show mode recovery), but it hinders reproducibility and interpretation of Table 1.

- **"Log RMSE" in Ising experiments is undefined.** Figure 3 plots "log RMSE" over iterations, but RMSE relative to what ground truth is never stated, and no reference distribution or computation method is given. The metric should be explicitly defined.

- **bDREXEL/bDREAM consistently underperform their uncorrected counterparts** (Table 2), yet the paper introduces them in Section 4.2 as a design motivated by stochastic-gradient settings. The paper acknowledges the correction "is not strictly necessary" (line 135), which raises the question of why it is retained as a focal variant. This is not a fatal issue — ablations are useful even when negative — but the narrative treatment is slightly confusing.

- **Hyperparameter settings for baselines are not reported** (step sizes, temperatures, swap intensity ρ, etc.). While some of this detail may reside in a parser-stripped appendix, the paper as accessible lacks sufficient information to reproduce or fully assess the fairness of comparisons.

### Trivial

- None that are not already covered above.

## Nice-to-Haves

- A formal proof (even for a simplified case) that the swap in Equation 10 satisfies detailed balance.
- Effective sample size or autocorrelation time measurements to directly support the mixing claim.
- A simple 1D or 2D counterexample where the standard swap (Equation 3) provably fails but Equation 10 succeeds.

## Removed Points

These points from the reviewers are flagged for removal — treat them with caution:

- **"The swap mechanism is likely invalid"** (Harsh Critic Claim 1): The critic argues that conditioning on previous samples breaks the Markov property. The paper's argument is that previous samples *are* part of the current state in the joint chain (they are constants at swap time), so the mechanism may be valid, but the justification is indeed thin. The claim of "likely invalid" overstates what can be concluded from the paper alone; this is a gap in proof, not evidence of a flaw. **Removed as overstatement**; the weakness is reframed above as "lacks rigorous justification."

- **"The proof is omitted anyway (appendix stripped)"** and references to missing appendix content: Per instructions, parser-stripped content (proofs, appendix) is presumed to exist in the original submission. **Removed.**

- **"Synthetic experiments are likely invalid"** (Harsh Critic Claim 3): The critic asserts the experiments are uninterpretable. The confusion in notation is real (recast as a Minor weakness above), but the visualizations and quantitative results are interpretable and directionally meaningful — DREAM clearly captures modes that DMALA misses. "Likely invalid" is too strong. **Demoted to Minor weakness (notation confusion).**

- **"No code is provided for the main experiments"**: The paper provides a code link for synthetic tasks. Code for the full suite is a reasonable expectation but not a scientific validity concern. **Removed** per instruction to remove reproducibility nitpicks about "artifacts impractical to include in a submission."

- **"The bias-corrected versions... should have been omitted or better motivated"** (Harsh Critic): An ablation that underperforms is still informative. The paper explicitly states the correction is "not strictly necessary." This is not a weakness. **Removed.**

- **Strength Finder's "Theoretical guarantee of reversibility and asymptotic convergence"**: Theorem 1 is limited to log-quadratic distributions and asymptotic (α→0) — which is the discrete analogue of standard unadjusted Langevin convergence. Claiming this as a core strength overstates its significance. **Removed** — kept only as a factual statement in the Summary.

- **Strength Finder's "Bias-corrected swap variant"** and **"Factorized coordinate-wise updates"**: The bias correction hurts performance (so it is not a strength), and factorized updates are inherited from prior work (Zhang et al., 2022b), not a contribution of this paper. **Removed.**

- **Strength Finder's "Swap mechanism tailored to preserve detailed balance"**: This is describing the paper's own proposal, not an independent strength — especially given the weakness about insufficient justification. **Removed**; the assessment of novelty is already captured in Strength 1.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely converge on the same issues: the swap mechanism is interesting but under-justified, the theory doesn't match the claims, and the experimental evidence is strong but has some presentation gaps. No reviewer identified a perspective the authors had not considered.

## Suggestions

1. **Formally state and prove the detailed balance condition for Equation 10.** Even a short proof sketch (showing the joint chain satisfies detailed balance when previous samples are treated as part of the current state) would substantially strengthen the paper.

2. **Fix the synthetic experiment notation and define evaluation metrics.** Clarify d vs. grid resolution, and explain how KL and MMD are computed (e.g., discretization of the true density on the grid). Define "log RMSE" in the Ising experiment.

3. **Qualify the mixing claim.** Either remove "faster mixing" from the abstract/conclusion, or support it with direct mixing diagnostics (ESS, autocorrelation time). The empirical convergence curves are suggestive but not a rigorous substitute.

4. **Clarify the swap protocol.** Specify exactly how ρ and S̃ combine to determine swap probability, and report the values used in experiments.

5. **Report baseline hyperparameters** (step sizes, temperatures, ρ) either in the main paper or a public supplement.

## Score and Decision

**Score**: 5.5

**Decision**: Borderline — the core idea is novel and the empirical evidence is strong across multiple tasks, but the insufficient justification of the swap mechanism and the mismatch between theoretical claims and results are significant weaknesses. The paper would benefit from a major revision addressing these gaps before it meets the bar for a top venue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>