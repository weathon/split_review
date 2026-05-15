Now I have a complete picture. Let me write the final consolidated review.

## Summary

This paper proposes diffusion Thompson sampling (dTS), a framework that uses pre-trained diffusion models as informative priors for contextual bandits. The key technical contributions are: (1) a recursive posterior decomposition enabling hierarchical sampling from the latent and action parameters, (2) efficient Gaussian approximations for these posteriors that become exact when both the diffusion link functions and reward likelihood are linear, and (3) a Bayes regret bound for the linear-linear case that highlights the statistical benefits of the diffusion structure. Experiments on synthetic and MovieLens data show dTS outperforming standard methods like LinTS, LinUCB, and GLM-TS across diverse settings.

## Strengths

- **First Bayes regret bound for diffusion-model-based Thompson sampling in contextual bandits (Theorem 4.1).** The bound scales as $\tilde{\mathcal{O}}(\sqrt{n(d K\sigma_1^2 + \sum_{\ell=1}^L d_\ell \sigma_{\ell+1}^2 \sigma_{\mathrm{MAX}}^{2\ell})})$ and includes a sparsity variant (Proposition 4.2) that cleanly separates the contributions of action-level and latent-level learning. The theoretical comparison to LinTS (Section 4.1) provides concrete scenarios (decreasing variances, sparsity) where dTS's structure provably reduces regret.

- **Principled posterior approximations with closed-form linear special case.** Section 3.1 derives recursive Gaussian approximations (Eqs. 8–12) that require only $\mathcal{O}((L+K)d^3)$ time and $\mathcal{O}((L+K)d^2)$ space per round, avoiding the $\mathcal{O}(K^3 d^3)$ cost of a joint posterior. The approximations are exact when both the diffusion link functions and reward likelihood are linear, and they retain the key property of matching the prior when no data is available.

- **Empirical demonstration that latent structure can matter more than reward accuracy.** In non-linear reward settings (Fig. 2, columns 2 and 4), dTS variants that use the correct diffusion prior but *incorrect* linear-Gaussian rewards still outperform methods like GLM-TS that use the correct reward distribution but ignore the latent structure. This is a clean, informative comparison that supports the core thesis.

- **Robustness to prior misspecification.** The paper includes misspecification experiments (Fig. 3c) where the diffusion prior parameters are corrupted, and non-diffusion environments (Swiss roll, MovieLens, Section 5.2) where dTS still outperforms LinTS. These settings partially address concerns about whether gains come from the diffusion structure versus simply having any prior.

- **Interpretable analysis of the effect of depth $L$.** Section 4 provides a clear discussion reconciling the theoretical prediction (regret increases with $L$ under a matching prior) with the empirical U-shaped curve (Fig. 4b), explaining that small $L$ underfits the true distribution while large $L$ adds unnecessary uncertainty.

## Weaknesses

### Fatal
None.

### Major

- **Baseline comparison does not isolate the value of the diffusion structure from the value of offline data.** dTS uses a pre-trained diffusion model built from offline estimates of action parameters. The main baselines (LinTS, LinUCB, GLM-TS, UCB-GLM) use no offline data at all. The reported gains could therefore stem from the offline data itself (any informative prior) rather than from the diffusion model's ability to capture correlations. The theoretical comparison in Section 4.1 discusses a version of LinTS that marginalizes the diffusion prior, but this baseline is not included in experiments. A controlled comparison — e.g., LinTS with an informative Gaussian prior using the same offline estimates — is needed to attribute improvement specifically to the diffusion structure. This does not invalidate the empirical results (dTS demonstrably outperforms the tested baselines), but it weakens the attribution of *why* it works.

### Minor

- **Posterior approximation is not directly validated in non-linear regimes.** The paper's core algorithmic contribution is an approximate posterior that becomes exact only for linear link functions and linear rewards. For non-linear cases (which appear in most experiments), the approximation is heuristic. The paper mentions validation in Appendix C.3 (stripped by the parser), but the critic's point about lacking a direct comparison to a more accurate posterior (e.g., MCMC) in a non-linear setting is reasonable. The strong empirical performance provides *indirect* evidence that the approximation is reasonable, but direct validation would strengthen the paper significantly.

- **Computational complexity claim glosses over MLE computation for non-linear rewards.** The paper claims $\mathcal{O}((L+K)d^3)$ time per round, but for non-linear rewards, computing the MLE $\hat{B}_{t,i}$ and Hessian $\hat{G}_{t,i}$ (Eq. 7) requires iterative optimization per action. The paper does not discuss this cost or report wall-clock times. This is not a fatal issue — the same concern applies to GLM-based baselines — but the complexity claim is incomplete without accounting for this subroutine.

- **No empirical runtime comparison.** Given the paper's emphasis on computational efficiency, reporting empirical wall-clock times as $K$ scales would substantiate the claimed advantage.

### Trivial
None.

## Nice-to-Haves

- A version of LinTS with an informative prior (built from the same offline data) as a baseline would substantially strengthen the empirical claims.
- Direct validation of the posterior approximation (e.g., KL divergence to a HMC-estimated posterior) for a small-scale non-linear problem.
- Guidelines or heuristics for choosing the diffusion depth $L$ in practice (beyond the empirical observation of a U-shaped curve).
- Extension of the regret analysis to non-linear link functions, perhaps via a bound on the approximation error.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

1. **"Overstated novelty vs Hsieh et al. (2023)"** — The critic claims extending from multi-armed to contextual bandits is "incremental." The paper clearly differentiates itself by (a) providing theoretical guarantees that Hsieh et al. lacked and (b) deriving exact closed-form posteriors. This is a fair and substantive extension.

2. **"Sparsity bound grows exponentially — paper does not comment"** — The paper does discuss this: Section 4.1 bounds $\sigma_{\mathrm{MAX}}^{2\ell}$ by $2^\ell$ and analyzes scenarios (decreasing variances, constant variances) showing how the exponential factor interacts with decreasing sparsity dimensions $d_\ell$ to produce net gains.

3. **"Posterior approximation is Laplace approximation"** — The paper explicitly distinguishes its approach (approximating only the likelihood, preserving the diffusion structure) from the standard Laplace approximation (approximating the entire posterior as Gaussian). This distinction is correctly articulated.

4. **"Not yet released / cannot be independently verified" style criticisms** — None present in the original input; noting this for completeness.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same strengths and weaknesses identified in the paper itself. The key tension — whether gains come from the diffusion structure or simply from having any informative prior built from offline data — is a genuine open question that the paper's experimental design partially addresses (via misspecification and non-diffusion environments) but does not fully resolve. Future work comparing against simpler informative-prior baselines could clarify this.

## Suggestions

1. **Add a controlled baseline:** Run LinTS with an informative prior (e.g., Gaussian with mean = offline estimate and covariance = sample covariance or Hessian-based) using the same offline data. This is the single most impactful addition — it would directly answer whether the diffusion structure adds value beyond just using the offline data.

2. **Validate the posterior approximation:** For a small-scale non-linear problem (small $d$, small $K$, $L=2$), compare the approximate posterior to an MCMC-estimated posterior and report the KL divergence or the impact on regret.

3. **Report wall-clock time:** For a scaling experiment ($K$ varying from $10$ to $10^4$), report the per-round runtime of dTS vs. baselines to substantiate the computational complexity claims.

4. **Clarify the scope of the complexity claim:** Explicitly note that for non-linear rewards, the $\mathcal{O}((L+K)d^3)$ figure covers the sampling/inference procedure, while MLE computation adds an iterative optimization cost per action that is standard for GLM-based methods.

## Score and Decision

**Overall assessment:** The paper addresses an interesting and timely problem (using diffusion models as informative priors for exploration in contextual bandits), provides a clean algorithmic framework with principled posterior approximations, and delivers a non-trivial regret analysis for the linear case. The empirical results are consistently positive but the main weakness — the lack of a baseline that controls for offline data usage — prevents full attribution of the improvement to the diffusion structure. This is not a fatal flaw (the paper still demonstrates that dTS works, just not precisely *why* it works relative to simpler uses of the same data), but it is a significant limitation that should be addressed. The paper would benefit from a focused revision adding one or two key baselines and validation experiments rather than major reworking.

**Originality:** Good — diffusion priors for contextual bandits are novel.
**Importance:** Good — correlated action spaces are common in practice.
**Claims supported:** Partially — empirical superiority is demonstrated but attribution is incomplete.
**Soundness:** Adequate — the theory is sound for its narrow scope; experiments are adequate but missing a key control.
**Clarity:** Good — the paper is well-structured and the algorithmic derivation is clear.
**Value:** Moderate — the framework and approximation techniques are useful, but the empirical gap limits impact.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>