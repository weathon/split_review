Now I have all the information needed to produce the final consolidated review.

---

## Summary

This paper proposes DC-DPSGD, a differentially private SGD method that handles heavy-tailed gradient noise by (1) using a random subspace projection to identify which per-sample gradients belong to the "heavy tail" vs. "light body," and (2) clipping these two groups with different thresholds (a large c₁ for tail gradients, a small c₂ for body gradients). The paper provides high-probability convergence bounds showing that the body portion's bound removes dependence on the heavy-tailed index θ, and presents experiments on four datasets (plus two heavy-tailed variants) where DC-DPSGD outperforms DPSGD, Auto-S/NSGD, and DP-PSAC by up to 9.72%.

## Strengths

- **First high-probability convergence analysis for DPSGD under heavy-tailed sub-Weibull noise.** Theorem 1 provides a high-probability bound for standard DPSGD with heavy-tailed gradients, and Theorem 4 (DC-DPSGD) shows that a (1−p) fraction of gradients can achieve a bound free of the heavy-tailed index θ, reducing the empirical gradient norm dependence from Õ(log^{max(0,θ−1)}(T/δ) log^{2θ}(√T)) to Õ(log(√T)). This goes beyond prior expectation-bound analyses for DPSGD.

- **Consistent and substantial accuracy improvements across all evaluated settings.** On normal datasets, DC-DPSGD outperforms DPSGD, Auto-S, and DP-PSAC by up to 5.42%; on heavy-tailed datasets (CIFAR10-HT, ImageNette-HT), the gains reach 8.34–9.72% (Table 2). These gains are consistent across architectures and privacy budgets, supporting the claim that the approach is effective in practice.

- **The approach does not require public data.** Unlike prior projection-based DPSGD methods (Zhou et al., Yu et al.) that rely on public datasets for subspace construction, DC-DPSGD operates entirely in the private setting. This is a meaningful practical advantage.

- **Theoretical and experimental guidance for choosing the large clipping threshold c₁.** The paper derives c₁ = Õ(log^{3/2}(1/δ))·c₂ based on the heavy-tailed index, yielding c₁ ≈ 10c₂ for CIFAR10, bridging the theory to a concrete hyperparameter rule (Section 6.3, Figure 4).

## Weaknesses

### Fatal
None.

### Major

1. **The subspace identification mechanism lacks a principled rationale and its connection to the theory is unvalidated.** The method projects *normalized* per-sample gradients (unit norm) onto a random k-dimensional subspace built from orthogonalized sub-Weibull vectors, then identifies the top-p by trace ||Vᵀĝ||². After normalization, all gradients are unit vectors, and for a random subspace the expected trace is k/d for every gradient regardless of whether it is heavy-tailed. The paper asserts that heavy-tailed gradients "amplify" in this subspace (lines 192–193) but provides no analysis showing that heavy-tailed gradient *directions* differ systematically from light-tailed ones. Theorem 3 bounds the error between empirical and population trace for a *single fixed vector*, which does not imply that sorting noisy traces correctly separates heavy from light tails. The theoretical threshold λ_max (defined with undefined symbols μ and I(λ) — see Minor weakness 1) is never connected to the algorithmic top-p selection: there is no proof that the set {i : λ_trⁱ ≥ λ_max} coincides with the top-p by noisy trace. The final bound (Theorem 5) simply assumes the classification is correct and weights two regimes by p. **Why this matters**: The subspace identification is positioned as a core novelty ("first work to rigorously address heavy tails in DPSGD"). Without a convincing justification — either theoretical or empirical via controlled ablation — the paper's central mechanism is unsupported.

2. **Missing controlled ablation that isolates the subspace identification component.** The paper compares against full DPSGD baselines, but never against a simpler variant that selects the top-p gradients by *pre-clipping gradient norm* (rather than subspace trace) and applies the same two-threshold scheme. Since the method has two components (identification + two-threshold clipping), this comparison is essential to determine whether the benefit comes from the identification step or simply from having two clipping thresholds. The ablation study (Table 3) varies k, ε split, and θ, but this does not address the fundamental question of whether the subspace projection adds value over a norm-based heuristic. **Why this matters**: If norm-based selection performs similarly, the claimed contribution of the subspace identification technique is not validated, and the paper's novelty is significantly weakened.

### Minor

1. **Undefined symbols in a key theoretical quantity.** The threshold λ_max = μ I(λ)/λ · aK² (Theorem 4) contains symbols μ and I(λ) that are never defined in the paper. The remark merely states λ_max is "correlated with the population variance" (citing Bakhshizadeh et al., 2023). This makes the threshold uncomputable from the paper alone and breaks the interpretability of Theorem 4's dichotomy.

2. **Privacy composition is stated but not justified.** Theorem 2 asserts the mechanism is (ε_tr + ε_dp, δ)-DP with standard noise multiplier formulas, but the derivation is omitted. The composition of trace queries (one noisy scalar per sample per iteration) with gradient queries follows from standard composition theorems (Abadi et al.'s moments accountant), and the data-dependent selection of top-p from *already noisy* traces is permissible post-processing. However, the paper does not walk through this accounting, leaving the DP guarantee stated rather than verified. This is a presentation gap, not a structural flaw — but given the centrality of DP to the paper, it should be addressed.

3. **Hyperparameter reporting is incomplete.** The heavy-tailed ratio p (stated to be in [0.05, 0.1]) and the subspace dimension k used in the main experiments (Table 2) are not reported. These are essential for reproducibility. The ablation for k shows accuracy improves with k, but the k value for Table 2 is unclear.

4. **Overclaimed inference from Theorem 3.** The remark after Theorem 3 states that the theorem "indicates that we can accurately identify and classify gradients with a high probability 1−δ'_m." Theorem 3 bounds |λ_tr − λ̂_tr + ζ_tr| for a single vector — it does not bound the probability that sorting B noisy traces by this quantity yields the correct heavy-tail subset. This is an overstatement.

### Trivial
None.

## Nice-to-Haves

- Report wall-clock time overhead relative to standard DPSGD (the subspace projection adds O(Bkd) per iteration).
- Describe the construction of the heavy-tailed datasets (CIFAR10-HT, ImageNette-HT) for reproducibility.
- Vary p (heavy-tailed ratio) and report sensitivity.
- Compare against a variant that selects top-p by gradient norm (pre-clipping) with same two-threshold scheme, as noted in Major weakness 2.

## Removed Points

The following points from the harsh critic are removed with justification:

- **"No prior DPSGD work has addressed heavy tails under non-convex settings"** (from "Other Observations"): This was listed as an observation about related work but is actually a strength that the paper itself claims. It's better stated in the Strengths section.
- **"The uniform bound is a simple weighted average of two regimes... almost tautological"**: This is a valid observation, but "almost tautological" is an overstatement that ignores that the weighted average structure itself is a nontrivial contribution (it's what removes the θ dependence from the dominant term). The bound is stated as a consequence of the assumed classification, which the paper acknowledges. This is better captured by Major weakness 1 (the disconnect between theory and algorithm) rather than a separate "it's too simple" criticism.
- **"The paper should also cover Y / domain Z / additional tasks"** type suggestions: Not present in the original review.
- **Any pure formatting/style nitpicks**: The critic had none.
- **Any "typos, spelling, grammar" criticism**: The critic had none.
- **Any "missing related works"**: The critic explicitly stated related work coverage is appropriate.
- **Reproducibility concern about heavy-tailed datasets**: The critic noted the modification process is not described — this is a valid Nice-to-Have, not a weakness. Moved to Nice-to-Haves.
- **"m₁, m₂ left unspecified"** in Theorem 2: These are standard constants in moments accountant analyses (Abadi et al.). Their exact values are not material to the paper's claims and are standard in the DP literature. This is a nitpick; the sensitivity argument is clear.

## Novel Insights

The harsh critic's analysis of the subspace identification mechanism exposes a genuine flaw that goes beyond presentation: after gradients are normalized to unit norm, the trace ||Vᵀĝ||² measures directional alignment with a random subspace, not heavy-tailedness of the gradient distribution. Because all normalized gradients have equal expected trace for an isotropic random subspace, the top-p selection by trace is effectively an alignment lottery. The paper's theoretical framework (λ_max based on tail behavior of sub-Weibull norms) is disconnected from the algorithmic implementation (sorting directional projections of normalized vectors). The critic correctly identifies that Theorem 3's per-vector trace bound does not aggregate to a correct classification guarantee. These points, taken together, suggest that either the subspace identification does not work as advertised and the empirical gains come from the two-threshold clipping alone, or there is a subtle statistical property of sub-Weibull random subspaces that the paper has not articulated. Either way, the paper's central claim requires stronger support.

The strength finder correctly identifies the paper's genuine contributions: the high-probability convergence analysis for DPSGD under heavy tails is valuable regardless of the subspace question, and the empirical gains are consistent and large. These give the paper a real floor.

## Suggestions

1. **Address the identification rationale directly.** Either (a) provide a theoretical argument that the distribution of ||Vᵀĝ||² differs between body and tail gradients (e.g., because heavy-tailed gradients have different directional concentration), or (b) replace the subspace identification with norm-based selection (which would still be novel as a two-threshold DP mechanism) and reframe the paper's contribution accordingly. If the subspace method is kept, analyze its separation margin and provide an end-to-end guarantee on correct classification probability.

2. **Add a controlled ablation (norm-based top-p).** Compare against a variant that sorts by per-sample gradient norm (pre-clipping, pre-normalization) instead of subspace trace, using the same two-threshold scheme and same p. If performance is similar, the contribution reduces to the two-threshold idea; if worse, the subspace method is validated.

3. **Define μ and I(λ) or replace λ_max with a data-driven quantity** so that the theoretical threshold is interpretable.

4. **Provide the privacy composition argument explicitly** (even in an appendix), accounting for the trace queries across all B samples per iteration and showing how ε_tr + ε_dp is obtained.

5. **Report p, k for all experiments** and disclose the exact procedure for generating orthogonal sub-Weibull vectors (distribution family, orthogonalization method).

---

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>