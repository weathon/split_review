Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes Stochastic Gradient Discrete Langevin Dynamics (SGDLD), a method for MCMC sampling in discrete spaces when the energy function involves an expensive expectation (e.g., over a large dataset). The paper identifies two key challenges: (1) naive stochastic gradients in discrete spaces are biased because the ratio estimator is not exchangeable with expectation, and (2) the stochastic jump rates vary by orders of magnitude across mini-batches, making fixed-step simulation unstable. SGDLD addresses these with two techniques: a **gradient caching scheme** that accumulates mini-batch statistics across repeated steps at the same state to asymptotically eliminate bias (Proposition 4.1, validated in Figure 2), and a **Polyak-inspired step-size adaptation** εₜ = hₜ/Z(xₜ) that normalizes simulation time by the local jump rate (validated in Figure 3). The method is evaluated on Bayesian logistic regression, stochastic facility location, approximate computing, and prompt tuning for text-to-image models, consistently outperforming baselines including full-data DLMC and ablated variants.

## Strengths

- **Cache-based bias correction is novel and empirically validated.** The paper clearly identifies why naive stochastic gradients fail in discrete spaces (Equation 10) and proposes a simple, effective caching scheme (Equation 12). Proposition 4.1 provides a theoretical guarantee of asymptotic unbiasedness, and the ablation study in Figure 2 directly validates this: SGDLD's total variation decreases with step size while SGDLD-noC's does not, confirming the cache corrects the bias.

- **Polyak step-size adaptation solves a real instability problem demonstrated with striking evidence.** Figure 1 shows jump rates varying by up to 10³⁰× across mini-batches — a concrete, dramatic visualization of why fixed-step simulation fails. The Polyak adaptation εₜ = hₜ/Z(xₜ) normalizes simulation time by the local jump rate, and Figure 3 shows that SGDLD (with Polyak) mixes faster and has lower variance than SGDLD-noP.

- **Systematic ablation study isolates each component's contribution.** The paper consistently compares SGDLD against SGDLD-noC (no cache) and SGDLD-noP (no Polyak step) across synthetic and real tasks. The consistent performance gaps (Figures 2-3, Tables 1-3) provide clear evidence that both techniques are necessary.

- **Strong and diverse empirical validation on three real-world applications.** SGDLD outperforms Gurobi and SLS on stochastic facility location (Table 1), matches/exceeds learning-based methods on approximate computing with orders-of-magnitude fewer function evaluations (10k vs. 100M+), and achieves higher CLIP similarity than continuous relaxation on prompt tuning (Table 3, Figure 4).

## Weaknesses

### Major

- **The interaction between caching and Polyak step size is not theoretically analyzed, leaving the combined algorithm without formal guarantees.** Proposition 4.1 only covers caching under fixed ε→0. The Polyak step makes ε state-dependent and noisy (via the gradient approximation to Z(x)). The paper asserts "with proper annealing, we can prove that SGDLD samples from the correct distribution" (Introduction) but provides no analysis of the combined system. For a paper whose central claim is producing correct samples, this is a significant gap. While the strong empirical evidence (especially Figures 2-3) partially compensates, the main text's theoretical justification is incomplete.

- **The procedure for converting SGDLD samples into a single solution is not specified for optimization tasks, impeding reproducibility.** In Sections 6.3 (facility location) and 6.4 (approximate computing), the paper states that the method "returns a configuration" and reports costs, but never describes *how* the configuration is extracted from the Markov chain sample path. Do the authors take the last sample? The mode? The sample with highest π(x)? A weighted average? This is essential for both reproducibility and for understanding why SGDLD outperforms optimization baselines (Gurobi, SLS) that return solutions directly. Without this, the reader cannot tell whether the advantage comes from the sampling method or the post-processing rule.

- **The computational cost calibration in Bayesian logistic regression (Figure 3) is not transparently justified.** The x-axis ratio of "320 updates for stochastic methods and 2 updates for DLMC" is stated without explanation of how this ratio was derived. It presumably reflects the dataset-to-batch-size ratio (D/B), but neither D nor B are reported. Without wall-clock time, total gradient evaluations, or the D/B ratio, the reader cannot verify that the comparison is fair. The claim that "SGDLD has a faster mixing rate than DLMC, as SGDLD requires less computation in each step" is only as credible as this calibration.

### Minor

- **The claimed "first practical method for stochastic distribution sampling in discrete spaces" is slightly overstated.** The paper itself cites Zhang et al. (2022) (which attempted this under unbiased-estimator assumptions) and pseudo-marginal MCMC with subsampling (Bardenet et al., 2017, mentioned in Section 6.2). The paper's contributions — removing the unbiasedness assumption via caching and stabilizing with Polyak steps — are genuine advances, but the "first practical" framing invites unnecessary criticism. Reframing as "the first stochastic-gradient approach that handles the inherent bias of naive estimators" would be both more precise and less vulnerable to challenge.

- **No discussion of how noisy Z(x̂) estimates interact with the caching mechanism.** The Polyak step uses a gradient-approximated Z(x) (Section 4.2), and the caching estimator accumulates over steps that stay at x. If Z(x̂) is an overestimate, ε becomes too small (potentially wasting computation); if an underestimate, ε is too large and the chain may jump before the cache accumulates. The paper acknowledges the approximation and notes it "is sufficient" empirically, but does not analyze the reliability of cache accumulation under noisy Z estimates. A simple experiment showing average cache size as a function of the schedule hₜ would strengthen this point.

### Trivial

- The notation "M" (total dataset size) in the Bayesian learning example (Equation 11) is used before being explicitly defined. It is clear from context but should be stated.
- The Polyak schedule hₜ and threshold h* are introduced but no concrete examples of valid schedules (e.g., hₜ = α/t, or geometric decay) are given. Heuristic guidelines would aid implementation.

## Nice-to-Haves

- Reporting wall-clock time or total gradient evaluations alongside the calibrated step count in Figure 3 would make the efficiency claim fully transparent.
- For the optimization tasks, clarifying whether the reported solution is the mode, the last sample, or the result of an annealing scheme would resolve the reproducibility concern.
- Adding a small experiment showing average cache size as the Polyak schedule hₜ decreases would empirically address the caching–Polyak interaction concern.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Proof is relegated to the appendix"** — Removed per hard rules: the parser strips appendix content from all papers; the proof exists in the original submission.
2. **"Gaussian Bernoulli model uses only 16 states" as a weakness** — Removed as a strawman: this is a synthetic validation experiment (not a claim about practical efficiency); the paper also evaluates on three real-world tasks.
3. **"Facility location results without standard deviations"** — Removed: the paper states "report the average cost with standard deviation in Table 1"; the table image was stripped by the parser.
4. **"Extra experiments mentioned but not presented"** — Removed per hard rules: these would be in the appendix, which was stripped by the parser.
5. **"The paper does not give a clear sketch of why caching works"** — The paper does give the reasoning (lines 164-181): as the chain stays in the same state, the cache grows and the averaged estimator improves, asymptotically approaching the true ratio. This is present, though compact.

## Novel Insights

Beyond the paper's own contributions, a genuinely novel observation emerges from the interaction of the two proposed techniques: the caching scheme exploits the *failure mode* of naive stochastic DLD (getting stuck at the same state for many steps) and turns it into a mechanism for bias reduction. In continuous SGLD, the state updates every step and this "stuck" behavior is seen as a bug; in discrete spaces, the paper converts it into a feature by accumulating a cache. The Polyak step size then provides fine-grained control over how long the chain stays at each state, making the cache accumulation rate programmable. This synergy — using state-dependent dwell time as a resource rather than a liability — is the paper's deepest insight and could generalize beyond this specific setting to other discrete MCMC methods with stochastic gradients.

## Suggestions

1. **Provide a theoretical sketch of the combined caching + Polyak algorithm in the main text.** Even a brief argument showing that under a decreasing schedule hₜ → 0, the chain asymptotically spends enough time at each state for the cache to converge, and the total process is asymptotically unbiased, would address the most serious weakness without requiring a full proof in the main body.

2. **Explicitly state the solution extraction procedure for optimization tasks.** A single sentence — e.g., "We run the chain for T iterations and return the state with the lowest objective value" — is sufficient. If different extraction rules are used for different tasks, state each.

3. **Disclose the dataset size D and batch size B used in the Bayesian logistic regression experiment**, or report results against total gradient evaluations instead of the calibrated step count. This makes the efficiency comparison transparent and reproducible.

4. **Tone down or qualify the "first practical" claim** to avoid unnecessary provocation. Emphasize that the novelty lies in handling bias and variance that prior stochastic-gradient approaches ignored.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>