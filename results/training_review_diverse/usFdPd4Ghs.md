Now I have a thorough understanding of the paper and all the reviewer claims. Let me construct the consolidated review.

## Summary

The paper develops a deep α-stable kernel process (Dα-KP) arising as the infinite-width limit of a deep Bayesian neural network under infinite-variance prior weights. The key insight is that the limiting process admits a conditionally Gaussian representation given positive α/2-stable mixing variables, enabling a recursive formula (extending Cho & Saul 2009) for the stochastic covariance kernels. This yields a computationally tractable kernel-space method (O(Ln³)) that avoids the exponential complexity O(n^{I+2}) of the prior feature-space approach by Loria & Bhadra (2023), works for multi-layer networks, and produces a stochastic kernel whose posterior can be learned from data — without artificial noise injection as in DIWP. Experiments on discontinuous functions and UCI benchmarks show competitive predictive performance, uncertainty quantification, and substantial computational gains.

## Strengths

1. **Novel derivation of a deep α-stable kernel process with conditionally Gaussian representation.** Theorem 1 provides a recursive formula (extending Cho & Saul 2009) linking the stochastic covariance kernels across layers under infinite-variance priors. The conditionally Gaussian representation enables tractable posterior inference despite marginal infinite variance — a genuinely new synthesis of the stable-process and deep-kernel literatures.

2. **Clear theoretical and numerical demonstration of stochastic kernel learning (feature learning).** Proposition 2 proves that for α < 2 the posterior distribution of the features depends on the observed data, whereas the α = 2 (Gaussian) limit yields feature-data independence. Figure 3 empirically confirms heavy-tailed, non-Gaussian posterior feature distributions on the Boston data set, validating that the kernel is indeed stochastic and learnable.

3. **Dramatic computational improvement over the prior feature-space method (Loria & Bhadra 2023).** The paper reduces complexity from O(n^{I+2}) (exponential in input dimension I) to O(Ln³) (cubic in n), enabling application to 10-dimensional problems and UCI data sets where the Stable method is infeasible. This is a substantive practical contribution.

4. **Superior predictive performance on discontinuous functions and competitive UCI results.** Table 1 shows Dα-KP achieving lower RMSE/MAE than DIWP, NNGP, and GP methods in 1D, 2D, and especially 10D discontinuous settings. Table 3 shows Dα-KP best on Energy and Yacht UCI data sets and competitive on Boston. Figure 2 illustrates that α-stable methods capture jump discontinuities that GP methods smooth out.

5. **Full posterior predictive uncertainty quantification via MCMC.** Algorithm 1 provides a principled sampling scheme that yields predictive distributions with uncertainty intervals. Figure 2b shows 90% predictive intervals under Dα-KP correctly covering the discontinuous truth, unlike GP intervals.

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistency between the characteristic function and the conditionally Gaussian representation (scaling mismatch).** Theorem 1 states the limiting characteristic function as φ(t) = exp{-(t^T Σ t)^{α/2}} and the conditionally Gaussian representation as z | s_+, Σ ~ N(0, s_+ Σ) with s_+ ~ S⁺_{α/2}. However, the paper defines S⁺_{α/2} through the Laplace transform E[exp(-λS)] = exp(-λ^{α/2}) (Eq. from Uchaikin & Zolotarev, lines 22-25). Under this definition, integrating out s_+ yields E[exp(i t^T z)] = E[exp(-½ s_+ t^T Σ t)] = exp(-(½ t^T Σ t)^{α/2}), which differs from the stated φ(t) by a factor of 2^{-α/2}. This discrepancy is not acknowledged or addressed. One could absorb it into a redefinition of Σ or the positive stable distribution's scale parameter, but the paper does not do so, and the recursive formula (taken directly from Cho & Saul 2009 without rescaling) would need adjustment. The paper must resolve this: either correct the factor and show how the recursion propagates it, or clarify the parameterization convention that makes the statements consistent. As presented, the theoretical derivation is incomplete.

2. **GP baselines use different, unspecified kernels.** The paper compares against "GP Bayes (tgp)" and "GP MLE (mlegp)" without stating which covariance kernels these methods use (tgp defaults to treed GPs with separable squared-exponential kernels; mlegp uses separable Gaussian correlation). Meanwhile Dα-KP, DIWP, and NNGP use deep ReLU kernels (the Cho–Saul recursion with δ=1). Superior performance over the GP baselines may partly reflect kernel choice rather than the stable prior. Since the paper's central claim is about the benefit of the stable prior (not the kernel), this confound weakens the evidential support. The paper should either re-run comparisons with GPs using the same deep ReLU kernel or explicitly acknowledge and discuss this mismatch.

### Minor

1. **"Close second" characterization is overstated for the 2D synthetic setting.** Table 1 shows Dα-KP RMSE 0.86 (SD 0.09) vs. Stable method RMSE 0.57 (SD 0.08) in 2D — a ~50% relative gap. The paper describes Dα-KP as "generally a close second" (line 138), but this is only accurate for 1D (0.57 vs. 0.52). In 2D the gap is substantial and merits explanation (e.g., information loss in the kernel approximation, sensitivity to ReLU activation vs. sign activation, or MCMC mixing issues). The trade-off claim (accuracy vs. computational cost) would benefit from a discussion of why this gap occurs and whether it persists after tuning.

2. **No sensitivity analysis for α (fixed at 1 throughout all experiments).** The paper uses α = 1 for all simulations and UCI benchmarks without justification or robustness checks. Since α controls tail heaviness and the degree of non-Gaussianity, performance may be sensitive to this choice. A sensitivity analysis (e.g., α ∈ {0.5, 1.0, 1.5}) on at least one data set, or a cross-validation procedure for selecting α, would substantially strengthen the empirical claims.

3. **MCMC details are deferred to the appendix without sufficient description in the main text.** Algorithm 1 references sub-algorithms (alg:s_given_s, alg:s_given_y) that reside in the appendix. The main text should at minimum describe the proposal distribution, the form of the acceptance probability, and how the conditional dependencies among the scales are handled. Without this, the reproducibility of the MCMC is incomplete for a reader working from the main paper.

4. **No discussion of the scale of RMSE relative to the function range in 10D.** In Table 1, all methods achieve RMSE above 8 in the 10D setting, while the true function takes values spanning a wide range (from sums of sign functions with coefficients 6 and 8). Normalized RMSE (e.g., relative to the standard deviation of test targets) would help interpret whether these errors are meaningfully different from a practitioner's perspective.

### Trivial

1. **Proposition 1 notation:** Λ depends on Σ^{(L)}, which itself depends on all scales through the recursion. The proposition correctly conditions on all scales (line 74: {s_+^{(ℓ)}}_{ℓ=2}^L, S_+^{(1)}), so the conditioning is complete, but a brief clarifying sentence would help.

2. **Figure 1 (mutual information):** The caption states "this quantity is not well defined in our case, since there is no well-defined covariance" — the paper means the marginal covariance does not exist (infinite variance), not that mutual information is undefined. This could be clarified.

3. **Feature learning figure (Figure 3):** The scatterplot and q-q plots convincingly show heavy tails, which is a necessary condition for feature learning (per Proposition 2), but an additional sanity check (e.g., showing that posterior features change when the response is permuted) would make the "learning" claim more directly evident.

## Nice-to-Haves

- **Test on a function that genuinely requires depth** (e.g., a composition of several nonlinearities) to justify the "deep" aspect, since Table 2 shows negligible variation with depth.
- **Report effective sample sizes, trace plots, and autocorrelation** for the MCMC sampler on a representative data set.
- **Report actual runtimes** for the synthetic examples, not just asymptotic complexity.
- **Release code** to enhance reproducibility.
- **Stronger empirical verification of feature learning**, e.g., a response-permutation test on the Boston data set showing that posterior features change when y is shuffled.
- **Tune α via cross-validation or marginal likelihood** instead of fixing it arbitrarily.

## Removed Points

- **"Missing appendix / algorithms not visible":** The parser strips appendix sections from all papers; these exist in the original submission. The substantive point about MCMC detail in the main text is retained under Minor.
- **"Proposition 1 should list all latent variables":** The proposition (line 74) already conditions on all scales ({s_+^{(ℓ)}}_{ℓ=2}^L, S_+^{(1)}). The critic's point is factually incorrect.
- **"Y-axis label missing in Figure 1":** Parser artifact / formatting nitpick.
- **"The paper should also cover Y / additional tasks / domain Z":** Scope creep beyond the paper's stated focus.
- **"Mutual information is always well-defined" semantics:** The paper's meaning (marginal covariance does not exist) is clear in context.
- **Strength Finder's "provides full posterior predictive uncertainty quantification"** — generic phrasing lacking specific evidence citation; merged into Strength 5 with specific reference to Figure 2b.
- **Strength Finder's generic "important problem" phrasing** — dropped as superficial.
- **Requests to compare against methods the reviewer prefers when the paper's choices are defensible** — the paper's baseline set (DIWP, NNGP, GP Bayes, GP MLE, Stable) is already substantial.

## Novel Insights

The reviews surface a genuine mathematical tension: the paper's claims about the characteristic function and the Gaussian mixture representation rely on parameterization conventions from two different sources (Samorodnitsky & Taqqu for the characteristic function; Uchaikin & Zolotarev for the Laplace transform of the positive stable), and these conventions are not verified to be consistent with each other. This is not a trivial notation issue — the factor 2^{α/2} must be tracked through the recursion. However, the overall framework (conditionally Gaussian deep kernel process with a recursive formula) is not invalidated; it requires a scaling correction. This type of parameterization mismatch is common when working across different stable-distribution references and is fixable, but the authors must be explicit about it. The more interesting insight from the reviews is that the paper's core contribution — a computationally viable kernel-space method for deep stable processes — is strong enough conceptually that correcting this mathematical oversight would not change the main story, but leaving it uncorrected makes the theory unsound as currently written.

## Suggestions

1. **Resolve the scaling inconsistency.** Provide a clean derivation that makes explicit the relationship between the characteristic function, the conditional Gaussian representation, and the recursive formula. Either (a) state the characteristic function with the correct factor exp(-(½ t^T Σ t)^{α/2}) and propagate this through the recursion, or (b) define the positive stable distribution with a scale parameter such that the factor is absorbed into Σ, and show the recursion still holds. A small worked example (n=2, L=2, 1D input) with closed-form calculations would allow readers to verify the machinery end-to-end.

2. **Address the baseline kernel mismatch.** Either run GP Bayes and GP MLE using the deep ReLU kernel (same as Dα-KP) to isolate the effect of the stable prior, or explicitly acknowledge that the default kernels differ and discuss how this might affect the comparison. The DIWP and NNGP comparisons already help, but the GP baselines need the same clarification.

3. **Provide α sensitivity analysis.** Show results for at least one synthetic and one real data set across α ∈ {0.5, 0.75, 1.0, 1.25, 1.5} to demonstrate robustness or inform practitioners about sensitivity.

## Score and Decision

**Score:** 6.0

**Decision:** Accept

The paper makes a novel and potentially impactful contribution — a computationally viable deep α-stable kernel process with learnable stochastic kernels, derived from principled infinite-width BNN limits. The main weakness is a real but fixable mathematical inconsistency in the scaling between the characteristic function and the conditionally Gaussian representation. This is a major weakness (it must be corrected), but not a fatal one, as it does not invalidate the overall framework. The experimental evidence is generally supportive, and the computational gains over the prior feature-space method are substantial. With the scaling inconsistency resolved and the baseline comparison clarified, this would be a strong paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>