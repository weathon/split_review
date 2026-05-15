Now I have a thorough understanding of the paper and can verify all claims against the actual content. Let me produce the consolidated review.

## Summary

This paper studies off-policy learning (OPL) in contextual bandits where the target reward is only partially observed (due to missing data, delays, censoring, etc.) but secondary rewards (clicks, dwell time, etc.) are fully observed. The authors propose HyPeR (Hybrid Policy Optimization for Partially-Observed Reward), a policy gradient estimator that combines the partially observed target reward with the fully observed secondary rewards in a tunable mixture. They prove unbiasedness of the target-reward gradient estimator, derive a variance reduction result, and introduce a data-driven procedure for strategically tuning the mixture weight \(\gamma\) to optimize the bias-variance trade-off. Experiments on synthetic data and the KuaiRec dataset show that HyPeR outperforms variants that use only target rewards (r-IPS/r-DR) or only secondary rewards (s-IPS/s-DR).

## Strengths

- **Theoretically grounded variance reduction:** Theorem 1 proves unbiasedness of the HyPeR target-reward gradient estimator under the full-support condition. Theorem 2 derives a variance comparison showing that HyPeR reduces variance relative to r-DR whenever the secondary-reward-conditioned estimator \(\hat{q}(x,a,s)\) predicts the target reward better than the unconditional \(\hat{q}(x,a)\). This formally justifies why secondary rewards can lower estimation variance without introducing bias.

- **Strategic weight tuning yields consistently better performance:** Section 4.1 introduces a data-driven procedure (using bootstrapped training data + held-out validation) to tune the mixture weight \(\gamma\) independently of the objective weight \(\beta\). Experiments in Figures 4–5 show that HyPeR(Tuned \(\hat{\gamma}^*\)) consistently outperforms HyPeR(\(\gamma=\beta\)) and all feasible baselines, validating the idea that intentionally using a "biased" weight can improve the bias-variance trade-off in finite samples.

- **Consistent empirical superiority across diverse conditions:** Figures 1–5 span variations in observation probability (0.1–0.9), sample size (500–10,000), target-secondary reward correlation (\(\lambda\) from 0 to 1), and objective weight \(\beta\). HyPeR achieves the highest combined and target policy values in nearly all settings, including on the KuaiRec real-world dataset.

- **Clear problem formulation unifying diverse practical scenarios:** Table 1 catalogues multiple real-world causes of partial reward observation (missing data, delayed rewards, censoring, data fusion, multi-stage rewards) under a single formal model, making the problem definition both general and actionable.

## Weaknesses

### Fatal

None.

### Major

- **Observation mechanism assumed context-dependent only, with no discussion of limitations.** The paper assumes \(p(o|x)\) — the observation indicator depends only on context, not on the action. While this is stated explicitly in Section 2.3, several motivating examples (conversion only observed after a click, censoring that varies with treatment arm) involve action-dependent observation \(p(o|x,a)\). When the true mechanism is \(p(o|x,a)\), the estimator using \(o/p(o|x)\) is biased, and the paper provides no discussion, robustness checks, or proposed extension. This limits the claimed generality of the framework. (This is a significant scope limitation but not fatal — the method is valid under its stated assumption; the paper should acknowledge the restriction and discuss an extension.)

### Minor

- **Unbiasedness claim lacks conditions for estimated nuisance functions.** Theorem 1 states unbiasedness "under Condition 1" (full support) without specifying whether the nuisance functions \(\hat{q}(x,a,s)\), \(\hat{q}(x,a)\), and \(\hat{p}(o|x)\) are assumed known or, if estimated, what conditions are needed (cross-fitting, independent sample, or consistency). The paper mentions estimating these models "using \(\mathcal{D}\)" (the same data), which creates a known gap between theory and practice. While this gap is common in the OPL literature, the paper's central theoretical claim would benefit from clarifying the required conditions. The paper also states "under the same conditions as r-DR," but HyPeR involves additional nuisance functions (\(\hat{q}(x,a,s)\)) beyond those in r-DR, so the conditions are not identical without further analysis.

- **Missing natural baseline: imputation-then-standard-OPL.** The paper compares against r-IPS/r-DR (target only) and s-IPS/s-DR (secondary only via aggregation \(F(s)\)). A natural baseline is to train \(\hat{q}(x,a,s)\) on observed data, impute \(r\) for missing samples, and then apply standard IPS or DR on the full imputed dataset. This baseline would isolate whether HyPeR's benefit comes from its specific hybrid design or simply from using secondary rewards to impute missing target rewards. The absence of this comparison makes it harder to attribute improvements to the HyPeR architecture itself.

- **Synthetic experiments use linear functional forms.** The expected secondary rewards \(f(x,a)\) and the target reward \(q(x,a,f)\) are both linear in the features. This favors methods that model the relationship linearly, which is exactly what HyPeR's \(\hat{q}(x,a,s)\) and \(\hat{q}(x,a)\) do. Testing non-linear dependencies would strengthen the evidence that the method is robust to model misspecification.

- **Real-world secondary rewards partially conflated with the target.** In the KuaiRec experiment, \(s_1\) is a deterministic thresholded version of \(r\) (\(s_1 = \mathbb{I}(r \geq 2.0)\)) and \(s_2\) is a deterministic function of \(r\) (\(-1\) if \(r < 0.5\)). Two other "secondary rewards" (upload time, video length) are context features rather than rewards from the interaction. While the paper shows that s-DR (using only \(s_1\)) performs poorly — indicating the proxy is imperfect — the experiment would be more convincing with secondary rewards that are naturally occurring (e.g., actual dwell time, clicks) rather than hand-crafted from the target. Reporting the correlation between secondary and target rewards would also help assess the difficulty.

### Trivial

- **Relative policy value formula has a typo.** The formula \((V(\pi^*) - V(\pi_\theta)) / (V(\pi_\theta) - V(\pi_{\mathrm{unif}}))\) does not yield 0 for the uniform policy and 1 for the optimal policy (the denominator would be zero when \(\pi_\theta = \pi_{\mathrm{unif}}\)). The intended formula is almost certainly \((V(\pi_\theta) - V(\pi_{\mathrm{unif}})) / (V(\pi^*) - V(\pi_{\mathrm{unif}}))\).

- **Potential stray formatting artifact in Eq. (5).** The r-DR equation in the paper includes a superscript "2" on the last term that appears to be a formatting artifact rather than part of the estimator.

## Nice-to-Haves

- An experiment with action-dependent observation \(p(o|x,a)\) to test robustness, or a discussion of how the method could be extended (e.g., by replacing \(p(o|x)\) with \(p(o|x,a)\) in the estimator).
- An imputation baseline (train \(\hat{q}(x,a,s)\), impute missing \(r\), apply IPS/DR on full data) to isolate the benefit of the hybrid architecture.
- Reporting actual gradient variance (e.g., via bootstrapping) to confirm the theoretical variance reduction in practice.
- Correlation statistics between secondary and target rewards in the real-world experiment to contextualize the difficulty.
- A cross-fitting or sample-splitting procedure for nuisance estimation to strengthen the theoretical guarantees.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The claim 'counter-intuitively...' is not counter-intuitive"** — This is the reviewer's opinion about phrasing, not a substantive weakness. The claim (that optimizing secondary rewards can improve target-only optimization) is defensibly non-obvious given that one might expect optimizing a secondary objective to distract from the primary one.
2. **"The paper does not justify why a linear weighted sum is appropriate"** — A linear weighted sum is the standard approach for multi-objective optimization and requires no special justification.
3. **"The paper does not discuss that r-IPS/r-DR require the observation propensity to be known or correctly modeled"** — This is standard knowledge in the OPL/IPS literature and applies equally to all methods, not a specific weakness of this paper.
4. **"Theorem 2 ignores variance introduced by model estimation"** — This is standard in the DR literature; the theorem compares fixed-model variance, consistent with how such results are presented throughout the field.
5. **"HyPeR(Tuned) matching HyPeR(Optimal) is suspicious"** — This is speculation without evidence; the tuning procedure is clearly described and the results are consistent with its intended behavior.
6. **"The logging policy is synthesized, not from the original platform"** — This is standard practice in OPL research when the original logging policy is unavailable.
7. **Missing appendix content criticisms** — The reviewer references "the proof (in the appendix, which we cannot inspect)" — weaknesses about missing appendix content are removed per policy (the parser strips appendices; they exist in the original submission).

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a fundamentally new perspective on the work that the paper's own analysis does not already cover.

## Suggestions

1. **Acknowledge the \(p(o|x)\) limitation explicitly.** State that the current framework assumes observation depends only on context, discuss which motivating examples satisfy this and which do not, and sketch a possible extension to \(p(o|x,a)\).

2. **Clarify the conditions for Theorem 1 with estimated nuisances.** Add a remark (or a short paragraph in the main text) explaining that the unbiasedness result holds when the nuisance functions are known or estimated on independent data, and note that cross-fitting or sample-splitting can be used in practice.

3. **Add an imputation baseline.** Train \(\hat{q}(x,a,s)\) on observed data, impute missing target rewards, and apply standard IPS/DR. This will help isolate whether HyPeR's advantage comes from its hybrid form or simply from using secondary rewards to fill in missing data.

4. **Test non-linear reward functions in synthetic experiments.** Even a simple non-linear extension (e.g., quadratic terms or a neural network parameterization) would strengthen the evidence that the method (and its linear models) are robust under misspecification.

5. **Correct the relative policy value formula** to \((V(\pi_\theta) - V(\pi_{\mathrm{unif}})) / (V(\pi^*) - V(\pi_{\mathrm{unif}}))\).

## Score and Decision

The paper addresses a practically important and genuinely underexplored problem. The HyPeR estimator is well-motivated, theoretically grounded (with unbiasedness and variance reduction results), and supported by broad empirical evaluation. The main weaknesses are: (1) the unacknowledged scope limitation of the context-only observation assumption, which restricts generality; (2) standard but unaddressed gaps in the theoretical treatment of estimated nuisance functions; and (3) a missing baseline and somewhat idealized synthetic data. None of these are fatal — they are addressable with revisions and additional analysis. The core contribution — combining partially observed target rewards with fully observed secondary rewards via a principled hybrid estimator with tunable bias-variance trade-off — is valuable and clearly demonstrated within the paper's stated assumptions. I recommend acceptance with the expectation that the authors address the major limitation and fill the gaps.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>