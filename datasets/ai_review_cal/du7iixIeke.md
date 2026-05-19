- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 6, 1, 8, 3
Now I have enough information to produce the consolidated review. Let me write it.

## Summary

This paper proposes DC-DPSGD, a method that uses a random subspace projection to distinguish "heavy-tailed" (tail) gradients from "light-tailed" (body) gradients in DP-SGD, then applies a larger clipping threshold to tail gradients and a smaller one to body gradients. The paper provides high-probability convergence bounds for heavy-tailed DPSGD (claimed as the first such analysis) and shows empirically that DC-DPSGD improves test accuracy by up to 9.72% over three baselines on heavy-tailed datasets.

## Strengths

1. **First high-probability convergence analysis for DPSGD under sub-Weibull heavy-tailed noise.** Theorem 1 (Section 4) provides an explicit high-probability bound for classical DPSGD under heavy-tailed gradients, and Table 1 situates this result against prior expectation-based bounds (NSGD, Auto-S) and heavy-tailed SGD bounds (Li et al. 2022). The bound's dependence on the tail index θ is explicitly derived and matches expectation bounds up to a high-probability log factor when θ = 1/2 (Remark 1).

2. **Theoretical decomposition showing the benefit of discriminative clipping.** Theorem 6 (Uniform Bound, Section 5.3) provides a weighted convergence bound that isolates the heavy-tail-dependent term to a p fraction (~5–10%) of gradients, replacing the O(log^{2θ}(√T)) dependence with O(log(√T)) for the remaining (1−p) fraction. This directly formalizes the advantage of using two thresholds.

3. **Subspace identification without requiring public data.** The paper constructs the projection subspace from random heavy-tailed vectors rather than relying on a public dataset (Section 2, Related Work), which distinguishes it from prior projection-based DP methods (e.g., Zhou et al. 2020, Yu et al. 2021).

4. **Consistent and non-trivial accuracy improvements across multiple datasets.** Table 2 shows DC-DPSGD outperforms DPSGD, Auto-S, and DP-PSAC by up to 4.57%, 5.42%, and 4.99% on standard datasets, and up to 8.34%, 9.72%, and 9.55% on heavy-tailed datasets. Improvements are reported with standard deviations.

## Weaknesses

### Fatal

None.

### Major

1. **The subspace identification operates on *normalized* gradients, discarding norm information — the paper does not justify why directional information alone can distinguish heavy-tailed from light-tailed gradients.** Algorithm 1 (lines 5–6) normalizes per-sample gradients before computing the trace λᵢ = ‖Vᵀĝ‖². After normalization, all gradients have unit norm, so the trace captures only directional alignment with the random subspace V. The paper states (Section 5) that "normalized gradients still retain directional information, which can be amplified when projected onto the subspace consistent with its underlying distribution," but provides no theoretical argument or empirical evidence that heavy-tailed gradients (characterized by their *large norm*) have systematically different directional structure from light-tailed ones. Since V is random, the expected trace is approximately k/d for any direction — the trace values will be near-random with respect to the original gradient norm. The method may still produce useful trace values for a different reason (e.g., if gradients in certain parameter directions are consistently larger), but the paper does not develop or support this alternative explanation. This is the most significant issue: it creates a gap between the claimed mechanism (identifying heavy-tailed gradients) and what the algorithm actually computes.

2. **The evaluation does not isolate the subspace identification component, so improvements cannot be attributed to the claimed mechanism.** No ablation compares subspace identification against a simpler alternative — e.g., randomly selecting the same proportion p of gradients for the larger threshold, or selecting the top-p by raw gradient norm. Without this, the observed improvements are consistent with a simpler hypothesis: applying a larger threshold to any subset of gradients (even a random one) reduces clipping loss for those gradients, and because p is small (5–10%), the additional DP noise is tolerable. The ablation study in Table 3 varies subspace dimension k and privacy budget split, but never removes the subspace itself (the "None" column shows the case without any subspace, which still uses discriminative clipping with some default assignment — it does not test random selection). This needs to be addressed for the paper's central claim to be supported.

3. **The algorithm's classification rule (top-p by noisy trace) and the theory's classification rule (λ_tr ≤ λ_max vs. λ_tr ≥ λ_max based on a population threshold) are not clearly connected.** Theorem 3 (DCDPSGD) defines two convergence regimes based on whether λ_tr is above or below λ_max (a threshold derived from sub-Weibull parameters), but Algorithm 1 selects the top-p fraction by sorted noisy trace. Theorem 4 (Uniform Bound) partially bridges this by introducing p and a probability δ'_m for identification error, but the relation between p (a hyperparameter set to ~5–10%) and λ_max (derived from distributional parameters) is not made explicit. The paper acknowledges this misalignment (Section 5.3: "this step incurs errors and losses, leading to a misalignment between Theorem 3 and the algorithm"), but the resolution is incomplete.

4. **Baseline hyperparameter tuning is not described, and the method has substantially more flexibility.** The paper does not state how the clipping thresholds for DPSGD, Auto-S, and DP-PSAC are selected per dataset, making it unclear whether the comparison is on even footing. Meanwhile, DC-DPSGD has two clipping thresholds (c₁, c₂), a proportion p, a subspace dimension k, and a privacy budget split (ε_tr, ε_dp) — offering substantially more degrees of freedom. A natural baseline would be a variant of DPSGD that uses a single larger threshold applied only to the top-p fraction of gradients identified via a cheap proxy (e.g., gradient norm), to isolate the benefit of the subspace technique from the benefit of having a two-threshold mechanism.

### Minor

1. **The description of the trade-off in Figure 1 is unclear.** The paper states that for heavy-tailed distributions, "the slower decay rate ... introduces extra clipping loss, while it simultaneously reduces the maximum divergence compared to the light-tailed distribution" (lines 22–23). The claim that a heavier tail *reduces* the maximum divergence between neighboring gradient distributions is not explained and is counterintuitive — a brief justification is needed for readers to follow the motivation.

2. **The construction of the heavy-tailed datasets (CIFAR10-HT, ImageNette-HT) is not described.** The paper cites references (Cao et al. 2019, Park et al. 2021) but does not explain how the heavy-tailed versions are created or what specifically makes them heavy-tailed. This affects reproducibility and the ability to assess whether the method is tested on realistic heavy-tailed scenarios.

3. **No analysis of whether the same gradients are consistently identified as "tail" across iterations.** If identification is essentially random (as the main concern suggests), gradients would not be consistently assigned — but the paper provides no analysis of trace distributions, consistency over time, or correlation between trace values and gradient norms. Such analysis would directly speak to whether the mechanism is working as claimed.

### Trivial

None.

## Nice-to-Haves

- An ablation replacing subspace identification with random selection (same p fraction assigned larger threshold) would cleanly separate the contribution of the subspace from the contribution of having two thresholds.
- A discussion of the computational cost of constructing the subspace O(dk) per iteration, which could be non-negligible for large d.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Table 1 comparison is difficult to parse":** Removed as too subjective and lacking a specific concrete anchor.
- **"Theorem 3 contains complex constants not instantiated":** Removed — theoretical constants in convergence bounds are typically left as general parameters; instantiation is not expected.
- **"No work has been done... claim is too strong":** Removed — this is a standard research claim; the paper cites relevant heavy-tailed SGD works.
- **"Random subspace vectors — how implemented for arbitrary θ?":** Removed as a reproducibility nitpick that would be addressed in the supplement (which is stripped by the parser).
- **"Standard deviations reported but number of runs not stated":** Weak but kept as minor — this is a minor reporting gap.
- **"Statistical significance tests missing":** Removed as beyond community norms for this type of empirical comparison.
- **"Limitations discussion missing":** Removed — limitations can be in a separate section commonly stripped by the parser.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the core mechanism gap head-on.** Either (a) provide a theoretical or empirical justification that heavy-tailed gradients have distinct directional structure that the subspace projection captures, or (b) modify the algorithm so that the trace is computed on un-normalized gradients (with appropriate sensitivity analysis for DP), or (c) reframe the contribution around discriminative clipping generally, with the subspace treated as a heuristic rather than the core identification mechanism. Without addressing this, the main claim of the paper is unsupported.

2. **Add the random-selection ablation.** This is the single most informative experiment for diagnosing whether the subspace is doing useful work. If random selection achieves similar results, the paper should acknowledge this and reframe the contribution accordingly.

3. **Describe the baseline tuning procedure explicitly.** State the search ranges and selection criteria for DPSGD/Auto-S/DP-PSAC on each dataset.

4. **Either align the theory and algorithm or explicitly discuss the gap.** If the algorithm selects top-p by trace, the convergence analysis should reflect this selection rule rather than a threshold-based partition.

5. **Describe the heavy-tailed dataset construction** in the main text (or cite existing work that fully specifies it) to improve reproducibility.
