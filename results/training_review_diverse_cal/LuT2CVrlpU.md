I have now thoroughly verified all reviewer claims against the paper content. Here is my synthesized final review.

---

## Summary

This paper extends behavioral entropy (BE), previously defined only for discrete spaces, to continuous domains by introducing differential BE (Definition 3). It develops k-NN estimators with asymptotic and finite-sample guarantees (Theorems 1–2), derives a practical RL reward from these estimators (Equation 24), and uses the resulting BE-maximizing policies to generate offline RL datasets. Experiments on MuJoCo tasks (Walker, Quadruped) across three offline RL algorithms (TD3, CQL, CRR) compare BE-generated datasets against those from Shannon entropy (SE), Rényi entropy (RE), RND, and SMM.

## Strengths

1. **Novel continuous-space formulation of behavioral entropy.** The paper provides a clean mathematical extension of BE (Definition 3) and its Prelec-weighted specialization (Equation 8) to continuous domains, which is the first such extension and is necessary for RL applications. (Section 2)

2. **Theoretical guarantees for k-NN BE estimators.** The paper proves both asymptotic consistency (Theorem 1) and finite-sample bias/variance bounds (Theorem 2) for the proposed k-NN estimator under general probability weighting functions. This is a non-trivial extension beyond the Shannon/Rényi k-NN estimation literature. (Section 3)

3. **Practical reward bridging theory to RL.** The derivation from the k-NN estimator to a tractable per-state reward (Equation 24), while approximate, produces a reward function that can be plugged into standard RL algorithms (via APT). The reward follows the same derivation pattern used in prior work (Liu & Abbeel, 2021; Yarats et al., 2021; Yuan et al., 2022) for SE and RE, making the approach methodologically consistent with the literature. (Section 4)

4. **Extensive empirical evaluation.** The paper evaluates 255 task-dataset-algorithm combinations across 5 seeds (1,275 trained policies), covering 3 offline RL algorithms, 2 environments with 5 total tasks, and systematic sweeps over α and q. The PHATE visualizations (Figure 3) provide interpretable qualitative evidence of BE's coverage diversity. (Section 5)

5. **Data- and sample-efficiency potential.** Using only 5% of the data (500K vs. 10M elements) and 20% of training steps (100K vs. 500K) compared to ExORL baselines is a practically meaningful result if verified. (Section 5, Experimental Setup)

## Weaknesses

### Major

1. **Differential BE's mathematical definition is incomplete for densities exceeding unity.** Definition 3 substitutes Prelec's function w(x) = e^{−β(−log x)^α} into the differential entropy formula. This function is defined only for x ∈ (0,1], but a continuous density f can exceed 1 (and does so in concentrated regions). For f(x) > 1 and non-integer α (5 of the 8 values in the sweep: 0.2, 0.5, 0.7, 0.9, 1.5), the term (−log f(x))^α is not a real number, making the integrand in Equation 8 ill-defined. The paper acknowledges this (line 86: "w must be generalized to w:[0,∞)→[0,∞)") but provides no actual generalization — this is a hand-wave, not a fix. Since the Prelec-weighted BE is the paper's core object, this gap undermines the theoretical foundation. The theorems and estimators inherit this issue because they assume w is well-defined on the range of f.

2. **Unfair experimental comparison: best-of-sweep vs. fixed baselines.** The paper sweeps 8 α values for BE and 5 q values for RE, then reports "best offline RL performance across all datasets" (Table 1). SE, RND, and SMM are each evaluated at only a single default setting. The central claim — "BE datasets lead to superior performance over SE, RND, SMM on all five tasks" — compares the best of 8 BE-generated datasets against a single SE/RND/SMM dataset. By a selection bias argument, the maximum over 8 draws is expected to exceed a single draw even if the underlying methods are equally capable. Figure 4 partially mitigates this by showing distributions, but Table 1 and the abstract's headline claims are based on the best-over-sweep comparison. A fairer evaluation would report performance across the full sweep (e.g., median or distribution) or fix α to a principled value. The RE comparison (also sweeping multiple q) is fairer, though RE's q sweep (5 values) is smaller than BE's (8 values).

3. **Unsupported data- and sample-efficiency claims.** The paper states that "Despite these limitations, we achieved comparable performance to that achieved in (Yarats et al., 2022)" (Section 5, Experimental Setup). However, it provides no table, figure, or numeric comparison showing the ExORL baseline performance. Without these numbers, the efficiency claim is unverifiable. This is a significant omission for what is presented as a key practical advantage.

### Minor

4. **Gaps in the reward derivation chain.** The derivation from the k-NN estimator (Equation 13) to the final reward (Equation 24) involves several unquantified approximations: (i) the term D_{k,n} is dropped from Equation 21 to Equation 22 with the claim that its contribution is "negligible under suitable conditions on n,k" — but no conditions are specified and no error analysis is provided; (ii) the exponent d is set to 1 (Equation 23→24) "for numerical stability" without discussing how this changes the objective, even though the k-NN density estimate (Equation 9) depends directly on d; (iii) a constant c is inserted inside the logarithm without studying its effect. While similar approximations appear in prior SE/RE reward derivations, the paper would benefit from bounding or at least discussing these gaps.

5. **Theoretical assumptions not verified for experimental settings.** Theorem 1 requires f to be bounded below by a positive constant (c₁ > 0) and above by a finite constant over its entire support. This is unrealistic for state occupancy measures in RL, which can have arbitrarily low density in unexplored regions. Additionally, the Lipschitz condition on w is stated without connecting it to the domain of f; the Prelec function is not Lipschitz on [0,1] for α < 1, though it is Lipschitz on any [δ, 1] with δ > 0 (which the c₁ > 0 condition would ensure, if the range of f is within [c₁, c₂] ⊆ (0,1] — but c₂ could exceed 1, creating the Issue-1 problem again). These assumptions are standard in the nonparametric estimation literature but should be acknowledged as restrictive for the RL setting.

6. **Missing experimental hyperparameters.** The paper does not specify the k value used in k-NN estimation, the buffer size, or how the state-space dimensionality was handled for the k-NN during APT training. These details are necessary for reproducibility.

7. **No direct coverage measurement.** The paper reports only downstream offline RL performance, not any direct measure of state-space coverage (e.g., estimated entropy values, state visitation counts). This makes it difficult to attribute performance differences specifically to BE's coverage properties rather than to confounding factors like reward scale or optimization dynamics.

8. **Admissibility of BE for all α values in the sweep.** The condition β = e^{(1−α) log(log(M))} from Suresh et al. (2024) ensures BE is an admissible generalized entropy for discrete distributions with M states. The paper does not verify whether this condition transfers to the continuous setting, nor whether BE remains admissible for extreme α values (e.g., α = 0.2) in the experimental regime.

### Trivial

- The notation ≲ in Equation 22 is used without defining its meaning.
- The paper states "Equation 22 is approximately proportional to Ĥ" but uses ≲ (less-than-or-approximately) rather than ∝.
- Several figure references in the body are incomplete or point to parser-stripped content.

## Nice-to-Haves

- A sensitivity analysis showing the effect of the constant c and the d=1 simplification on the learned policies would strengthen the reward derivation.
- Direct coverage metrics (e.g., empirical entropy of visited states) would help disentangle whether BE's advantage is due to coverage diversity or other factors.
- Applying BE to a broader set of environments (e.g., Ant, Humanoid) and offline RL algorithms would increase the generality of the findings.
- A fixed-α comparison (e.g., α=1 as a single "default" BE analogous to SE) would complement the best-of-sweep results and provide a fairer comparison.

## Removed Points

These points were removed from consideration; treat them with caution if encountered elsewhere.

- **"Drops a factor β" (Issue 5 sub-point):** The reviewer claimed the final reward (Eq. 24) drops a β factor from Eq. 22. This is factually wrong — β appears inside the exponential in both equations (e^{−β(…)}) and the leading β from Eq. 20 is absorbed into the proportionality constant (∝). β is not dropped. (Removed: factually incorrect)

- **Missing appendix / proofs:** The paper's appendix was stripped by the PDF parser; it exists in the original submission. (Removed: parser artifact)

- **"w is not Lipschitz" (part of Issue 4):** The reviewer claimed Prelec's function is not Lipschitz for α<1. While true on [0,1], this is irrelevant because Theorem 1 assumes f(x) ≥ c₁ > 0, restricting w's evaluation to [c₁, c₂]. On any compact subinterval of (0,1], w is C¹ and hence Lipschitz. The condition is reasonable given the theorem's own assumptions. However, the c₂ could exceed 1, creating the Issue-1 domain problem. The Lipschitz concern is secondary to the real issue (domain mismatch). (Downgraded: the core concern is addressed by Issue 1)

## Novel Insights

None beyond the paper's own contributions. The reviews raise legitimate methodological concerns but do not surface a new conceptual insight about the paper's direction.

## Suggestions

1. **Fix the differential BE definition.** Provide an explicit extension of Prelec's function to [0,∞) that preserves real-valuedness, smoothness, and the admissibility properties. One possibility is using w(x) = e^{−β|log x|^α} (absolute value inside the exponent) for x > 0, which is real for all x > 0 and all α. Analyze how this changes the theoretical properties.

2. **Rerun the experimental comparison fairly.** Either: (a) fix α to a single principled value (e.g., α=1, which recovers SE-like behavior, or a value selected by a validation criterion) and compare all methods at single settings; or (b) report the full distribution of offline RL performance across the α sweep and avoid "best-of" claims against single-default baselines. The abstract and conclusion should be updated to reflect the qualified nature of the comparison.

3. **Provide ExORL baseline numbers.** Either include a column in Table 1 showing ExORL 10M/500K performance, or provide a separate comparison table, so the claimed data/sample efficiency is verifiable.

4. **Quantify the reward approximation gaps.** Provide error bounds or empirical sensitivity analysis for: the D_{k,n} omission, the d=1 simplification, and the constant c. Show at least one environment where you compare policies trained with d=1 vs. the true d (or d=2 as a middle ground).

5. **Report coverage metrics directly.** Include empirical estimates of the state occupancy entropy (Shannon and/or BE) achieved by each exploration policy, so the link between coverage and offline RL performance can be directly examined.

6. **Specify all hyperparameters.** State the k value for k-NN, buffer size, the β value used (which was not reported in the available text), and how the state dimension d was handled for the k-NN estimator during APT training.

## Score and Decision

The paper tackles an interesting and well-motivated problem (extending BE to continuous RL settings). The theoretical framework (k-NN estimators with guarantees) and the experimental scope (255 algorithm-task-dataset combinations) represent genuine effort and partially support the paper's claims. However, a **major** mathematical gap in the core definition (differential BE is not well-defined for densities exceeding unity with non-integer α), combined with a **major** experimental methodology issue (best-of-sweep compared against single baselines), means the central claims cannot be accepted as currently formulated. The data-efficiency claim is also unverifiable due to missing baseline numbers. These problems require structural changes to fix, not minor revisions.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>