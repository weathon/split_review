Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes Discriminative Clipping (DC)-DPSGD, a method for handling heavy-tailed gradient noise in differentially private SGD. The key idea is to use a random projection subspace constructed from heavy-tailed sub-Weibull vectors to separate gradients into a "light body" and "heavy tail," then apply different clipping thresholds to each group — a smaller threshold for body gradients and a larger one for tail gradients to reduce clipping loss. The paper provides the first high-probability convergence analysis for DPSGD under sub-Weibull noise, showing that the method reduces the empirical gradient norm's dependence on the heavy-tail index θ from O(log^max(0,θ-1)(T/δ) log^{2θ}(√T)) to O(log(√T)) for a (1-p) fraction of gradients. Experiments on four datasets (including two heavy-tailed variants) show consistent accuracy improvements of up to 9.72% over DPSGD, Auto-S, and DP-PSAC.

## Strengths

1. **Novel discriminative clipping mechanism with subspace identification tailored to heavy-tailed DPSGD.** The paper designs a two-threshold strategy (Algorithm 1) that uses random projection and the trace of the projected second moment to separate body from tail gradients. This is the first work to explicitly address heavy-tailed gradients in DPSGD with a dual-threshold approach, and the idea is well-motivated by the real phenomenon of heavy-tailed gradient noise in deep learning (Sec. 2 cites empirical evidence from multiple prior studies).

2. **First high-probability convergence analysis for DPSGD under heavy-tailed sub-Weibull noise.** Theorem 1 provides a high-probability bound for vanilla DPSGD with heavy-tailed gradient noise, and the paper claims (correctly, based on the comparison table in Table 1) to be the first to provide such an analysis. This is a genuine technical contribution — prior DPSGD theory relies on expectation bounds or sub-Gaussian assumptions.

3. **Quantifiable reduction in the dependence on the heavy-tail index θ.** Theorem 4 (Uniform Bound) shows that the convergence rate for DC-DPSGD is a p-weighted average where the body portion (1-p) is free from the heavy-tail index θ, reducing the bound from O(log^max(0,θ-1)(T/δ) log^{2θ}(√T)) to O(log(√T)) for that fraction. The theoretical analysis is further validated by providing practical guidance for threshold selection (c₁ = log^{3/2}(1/δ)·c₂, validated in Figure 4).

4. **Significant and consistent accuracy improvements across all datasets.** The experimental results (Table 1) show DC-DPSGD outperforming three baselines (DPSGD, Auto-S, DP-PSAC) on all four datasets. The gains are especially pronounced on heavy-tailed versions: +8.34% on CIFAR10-HT and +9.72% on ImageNette-HT. The ablation study (Table 2) shows that the method's performance degrades without the subspace component (k=None), providing evidence that the subspace identification contributes to the gains.

## Weaknesses

### Fatal
None.

### Major

1. **The subspace identification rationale lacks a clear theoretical or empirical justification.** The paper claims that normalizing gradients to unit norm and computing tr(V_k^T ĝ ĝ^T V_k) in a random heavy-tailed subspace can separate body from tail gradients (lines 192–193). However, it provides no argument — theoretical or experimental — for why the trace of a *normalized* gradient's projection should correlate with whether the *original* (unnormalized) gradient lies in the heavy tail of the norm distribution. After normalization, all gradients have unit L2 norm, so the trace measures alignment with the subspace, not norm magnitude. The paper asserts that "normalized gradients still retain directional information, which can be amplified when projected onto the subspace consistent with its underlying distribution" (line 192), but this claim is not substantiated. This is a significant gap because the subspace identification is the core technical novelty that the entire method rests upon. **Why it matters: Without a principled link between the subspace trace and heavy-tail status, the entire pipeline — identify heavy-tailed gradients → clip them differently — is operating on an unverified premise. The improvements could be coming from the two-threshold design alone, with the subspace serving as little more than a noisy random sorting mechanism.**

2. **The theory and the algorithm operate on different classification rules, with an unbridged gap.** The theoretical analysis (Theorems 3 and 4) classifies gradients using a threshold λ_max on the *population trace*, where λ_max depends on unknown distributional parameters (μ, I(λ), K) that are never instantiated. The algorithm, by contrast, uses a data-driven top-p selection on *noisy empirical traces* with a fixed hyperparameter p=0.1. The remark after Theorem 4 (line 265) acknowledges that λ_max is "correlated with the population variance" and that the trace empirically approximates it, but this informal connection does not constitute a rigorous bridge. The uniform bound (Theorem 4) partially addresses this by cutting over to a p-weighted average, but the mapping between p and the theoretical λ_max is never established. **Why it matters: The convergence guarantee in Theorem 4 may not apply to the actual algorithm as implemented, because the algorithm's classification rule (top-p on noisy traces) differs from the theory's classification rule (λ_max threshold on population trace).**

### Minor

3. **Missing ablation: comparison against a simple norm-based heuristic.** The paper ablates subspace dimension k, privacy budget split, and sub-Weibull index θ, but does not compare the subspace identification against a simpler alternative: clip gradients whose *raw norm* exceeds a percentile with the larger threshold c₁. The k=None case in Table 2 (which shows degraded performance) partially addresses this concern by demonstrating that the subspace projection matters, but it does not separate the effect of the *identification method* from the effect of the *two-threshold design itself*. A norm-based heuristic baseline would clarify whether the subspace machinery is necessary or whether the improvements come primarily from simply having two thresholds. **Why it matters: The paper's central technical novelty is the subspace identification step; if a simpler rule achieves comparable results, the novelty claims are weakened.**

4. **The heavy-tailed dataset construction is not described, making it hard to assess whether the heavy-tailed assumption is realistic.** The paper states that CIFAR10-HT and ImageNette-HT are created by "extracting through sub-Exponential distributions" (line 323) and cites earlier works (Cao et al. 2019, Park et al. 2021), but provides no details about the construction process. The non-DP baseline drops dramatically on these datasets (e.g., 71.74% → 39.91% on ImageNette-HT), suggesting the heavy-tailed versions may differ substantially from their standard counterparts, not just in tail index. **Why it matters: Without understanding the construction, reviewers cannot assess whether the heavy-tailed assumption is realistic or whether the method only works on artificially constructed datasets.**

5. **The privacy composition guarantee is stated but not argued.** Theorem 2 states the privacy guarantee but provides no derivation or explicit citation of composition theorems. While the composition of the trace-release mechanism (sensitivity 1, Gaussian noise) and the gradient-release mechanism (sensitivity depends on threshold assignment, which is post-processing of DP outputs) is indeed standard and likely correct, the paper does not walk through the reasoning. **Why it matters: The critic's concerns about adaptive composition, while ultimately incorrect, are not unreasonable to raise given the paper's brevity on this point. Explicitly addressing why the composition is valid would strengthen the paper.**

### Trivial
None.

## Nice-to-Haves

- A synthetic experiment or theoretical derivation establishing a formal link between the subspace trace (after normalization) and the gradient's heavy-tail status. A simple scatter plot of raw gradient norm vs. subspace trace for a representative training iteration would be very informative.
- A comparison against a norm-percentile baseline for identifying heavy-tailed gradients, to isolate the value of the subspace identification.
- More detail on the construction of the heavy-tailed datasets CIFAR10-HT and ImageNette-HT.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Privacy accounting is incomplete/likely invalid (Harsh Critic, Critical Issue 2).** The critic argues that adaptive composition isn't properly handled. This is incorrect. The noisy traces (line 10 of Algorithm 1) are DP with budget ε_tr (Gaussian mechanism, sensitivity 1). The top-p selection is post-processing of those DP outputs (post-processing immunity). The gradient release mechanism then uses thresholds assigned via post-processing, with its own DP budget ε_dp. By basic DP composition, the total is (ε_tr+ε_dp, δ)-DP. The composition is standard and valid; the critic's concern about "adaptive composition" reflects a misunderstanding of how post-processing immunity applies here.

- **d^{1/4} in Theorem 1 is unusual / "claim of matching is not obviously correct."** The paper's bound at θ=1/2 is O(d^{1/4} log^{5/4}(T/δ) log(√T)/(nε)^{1/2}), while Yang et al. (NSGD) gives O(⁴√(d log(1/δ))/(nε)^{1/2}). The d^{1/4} factor matches. The extra log terms are expected because high-probability bounds generally carry extra logarithmic factors compared to expectation bounds — the paper explicitly acknowledges this (line 162). The claim of matching is valid.

- **Theorem 3 mixes statistical error with DP noise / "error bound hard to interpret."** The bound in Theorem 3 (|λ_tr - λ̂_tr + ζ_tr| ≤ 4log(2d/δ_m)/k + σ_tr·log^{1/2}(2/δ)) cleanly separates the approximation error (first term) from the DP noise (second term). This is well-structured and standard.

- **Algorithm line 6: "Extract orthogonal vectors from sub-Weibull distributions" — reproducibility concern.** This is a minor implementation detail. Standard techniques exist (e.g., sample i.i.d. sub-Weibull vectors and orthogonalize via QR). The marginal distributions change after orthogonalization, but the resulting joint distribution remains valid for the subspace construction. This level of detail is routinely omitted in ML papers.

- **Fig. 1 does not support the approach / presentation nitpicks in Introduction, d^{1/4} questioning, Theorem 3 interpretation issues.** These reflect misunderstandings or presentation preferences rather than actual flaws in the paper.

- **Several strengths from Strength Finder that conflict with verified weaknesses** were checked and found to be consistent. All six strengths are retained as valid.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same core tension: the subspace identification is the paper's most novel element, but it is also the least justified. The reviewer correctly identifies that the link between the normalized-gradient trace and the heavy-tail property is asserted rather than argued or demonstrated. This is an insightful observation that points to a concrete path for improvement (a formal argument or even a simple empirical correlation plot), rather than a dismissal of the paper's value. The paper's main strengths — the first high-probability convergence analysis for heavy-tailed DPSGD and the consistent empirical gains — are genuine and survive scrutiny.

## Suggestions

1. **Provide a clear justification (theoretical or empirical) for why the subspace trace separates body from tail gradients.** At minimum, include a synthetic experiment or correlation plot showing that the trace of the normalized gradient's projection correlates with the gradient's position in the heavy tail of the norm distribution. Without this, the core mechanism is a black box.

2. **Bridge the gap between theory (λ_max threshold) and algorithm (top-p selection).** Either instantiate λ_max empirically (by estimating the unknown distributional parameters) or provide a formal argument that top-p approximates the theoretical λ_max dichotomy for some known p.

3. **Add a norm-percentile baseline** that clips the top p% of gradients (sorted by raw norm) with c₁ and the rest with c₂. This would isolate the value of the subspace identification from the value of having two thresholds.

4. **Expand the privacy composition analysis.** Walk through why the adaptive assignment of thresholds (via post-processing of DP noisy traces) does not invalidate standard composition, to preempt concerns like those raised in this review.

## Score and Decision

This paper makes a real contribution — it identifies an important problem (heavy-tailed gradients in DPSGD), provides the first high-probability convergence analysis for this setting, and demonstrates consistent empirical improvements. However, the core technical novelty (subspace identification) is not convincingly justified: the link between the trace of a normalized gradient projected onto a random heavy-tailed subspace and that gradient's "tail" status is asserted without evidence. The theory and algorithm also operate on different classification rules. These are significant gaps, but they are addressable (with additional analysis and experiments) rather than fatal flaws. The paper's contributions — the high-probability analysis for DPSGD under heavy tails and the discriminative clipping framework — are valuable even if the specific identification mechanism needs better justification.

**MY FINAL SCORE:** <pineapple>7.0</pineapple>  
**MY FINAL DECISION:** <orange>Accept</orange>