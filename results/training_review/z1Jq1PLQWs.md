Now I have all the information needed to produce a thorough, verified review. Let me produce the final consolidated review.

## Summary

This paper addresses adversarial online linear optimization with preference (dueling) feedback under a logistic (sigmoid) preference model. It proposes Double-Scrible, a mirror-descent algorithm that achieves Õ(d√T) regret by adapting the Scrible algorithm (originally for value feedback) to the weaker preference feedback setting. The paper also extends to batched pairwise feedback (BaBle-Scrible) and ranking feedback (MNL-Scrible), each with matching lower bounds. The core technical contribution is a gradient estimation procedure that extracts signal from binary preference comparisons.

## Strengths

- **First computationally efficient gradient-descent algorithm for adversarial preference feedback with theoretical guarantees.** The paper proposes Double-Scrible and proves an Õ(d√T) regret bound (Theorem 1). This directly addresses the computational intractability of prior UCB/Thompson-sampling methods for preference-based online learning, which the paper documents in Section 1 (e.g., requiring confidence set optimization or posterior sampling over high-dimensional spaces). The O(dT) runtime requirement (Remark 5) is a concrete advantage.

- **Matching lower bounds across all settings.** The paper proves lower bounds for the dueling (Theorem 3: Ω(d√T)), batched (Theorem 6: Ω(d√T/√min{B,d})), and ranking (Theorem 9: Ω(d√T/√m)) settings, establishing tightness up to logarithmic factors. These are derived from first principles of information theory.

- **Extensions to batched and ranking feedback with regret analysis.** Sections 4 and 5 generalize the pairwise setting to batched pairwise feedback (BaBle-Scrible, achieving √B improvement) and top-m ranking feedback (MNL-Scrible, achieving √m improvement). These address realistic constraints in RLHF deployment, such as communication delays and partial ranking feedback.

## Weaknesses

### Fatal

None.

### Major

1. **Overclaimed scope: the abstract promises trajectory-level RLHF policy optimization that the paper never delivers.** The abstract states "we extend our results to policy optimization in the RLHF framework with trajectory preferences and design no-regret RL policies using a variant of mirror descent." The paper body contains no MDP, no state space, no policy gradient, no trajectory-level analysis, and no connection to the RLHF setting of Rafailov et al. (2024) or Xie et al. (2024) beyond a best-arm bandit framing. The paper is about bandit-level action selection under a linear utility model. This claim mismatch between the abstract and the actual content is a significant overstatement that misrepresents the contribution.

2. **Experiments lack any baselines and have incomplete setup descriptions.** No existing algorithm (UCB-based, random, or otherwise) is compared against. The adversarial environment descriptions (Inst-1 and Inst-2, Section 6) are cut off/incomplete — "we choose θ_t" without specifying how. Without baselines, the experiments demonstrate only that the algorithm runs, not that it performs competitively. For a paper claiming computational efficiency as a key advantage, the absence of any runtime comparison against prior methods is a critical gap. No error bars or measures of variance are reported despite claiming "100 runs."

3. **The "optimality" claim is misleading: the upper bound depends on an uncharacterized problem-dependent constant H_{D,ψ} that the lower bound lacks.** Theorem 1 gives Õ(d√T / H_{D,ψ}), while Theorem 3 gives Ω(d√T) without this constant. The bounds only match when H_{D,ψ} = Θ(1). Remark 3 gives examples where H²_{D,ψ} = 2 or d, which would create up to a √d gap between upper and lower bounds. Claiming the algorithm is "optimal" without properly characterizing this gap is imprecise.

### Minor

1. **No statistical significance reported.** Despite averaging over 100 runs, the paper provides no error bars, confidence intervals, or variance measures in any of the experiments (Section 6). This is standard practice for empirical ML papers.

2. **The k-subset construction in MNL-Scrible requires k to be a power of 2** (Section 5(i): S_t = 2^{ℓ_k} ≤ k with ℓ_k = ⌊log k⌋). The paper does not address how to handle subset sizes that are not powers of 2.

3. **The claim that top-m ranking yields "m independent pairwise preferences" (Lemma 14, deferred to appendix) is non-trivial.** In the Plackett-Luce model, the top positions are not independent of lower positions. The main text provides no justification for this independence claim, which is central to the reduction to the batched setting.

4. **The derivation of sample complexity from regret (Remark 2, lines 79–81) contains notational sloppiness** that makes the algebra difficult to follow. The inner summation index reuses t rather than a fresh index, and the vector/scalar operations are conflated in the displayed equation.

### Trivial

None.

## Nice-to-Haves

- A sensitivity/ablation analysis for the key parameters γ_t and η would help establish that the theoretical parameter choices work robustly in practice.
- A simple sanity-check baseline (e.g., uniform random play) would strengthen the empirical section considerably.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Core algorithmic content deferred to missing appendices":** REMOVED. Per guidelines, the appendix sections exist in the original submission — the PDF parser strips them. The main text contains narrative algorithm descriptions, the gradient estimator formulas, and all theorem statements.
- **"MNL-Scrible gradient estimator has a sign error":** REMOVED. The formula g_t^ℓ = (d/(2γ_t))√(λ)v is consistent with the dueling case g_t = (d/γ_t)(o_t-1/2)√(λ)v. In the MNL reduction, the extracted pairwise preferences are deterministic (o_t^ℓ = 1 always), so o_t^ℓ - 1/2 = 1/2, making both formulas identical. No error exists.
- **"Remark 1 inequality stated without proof":** REMOVED. The inequality θ^T(x*-x)/4 ≤ σ(θ^T(x*-x))-1/2 ≤ θ^T(x*-x) is a standard property of the logistic sigmoid (its derivative at 0 is 1/4, and the function is 1-Lipschitz). This requires no proof in the main text, and the "time-varying θ*" concern is irrelevant since the inequality holds pointwise for any fixed argument.
- **"Sample Complexity objective never used":** REMOVED. This is factually incorrect — Corollaries 2, 5, and 8 explicitly derive sample complexity bounds.
- **"Linear-in-parameters assumption is unrealistic for LLMs":** REMOVED. This is scope creep — the paper explicitly studies linear utility models, which is the standard starting point for bandit theory. Criticizing this assumption is demanding the paper solve a problem outside its stated scope.
- **"Missing related works":** REMOVED. Per guidelines, I cannot verify the existence of cited works.
- **Formatting/style nitpicks:** REMOVED. Issues like garbled text, missing labels on figures, etc., are parser artifacts or presentation points that carry no weight in evaluation.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective not already present in the paper.

## Suggestions

1. **Honestly rescope the claims.** Remove or substantially qualify the abstract's claim about "policy optimization in the RLHF framework with trajectory preferences" since the paper contains no such analysis. The contribution is about bandit-level preference feedback, which is valuable in its own right.
2. **Add baseline comparisons.** At a minimum, compare against a uniformly random policy and, where feasible, against a simplified UCB-based dueling bandit (e.g., Saha et al. 2023) on small problem instances.
3. **Complete the experimental description.** Specify the adversarial θ_t generation process for Inst-1 and Inst-2. Add error bars or shaded regions to all regret plots.
4. **Clarify the optimality claim.** Explicitly discuss the dependence on H_{D,ψ} and state whether the bounds match when this constant is accounted for, or if a gap remains.
5. **Fix the Remark 2 derivation.** Use a fresh summation index for the inner sum and ensure the algebra is dimensionally consistent.

## Score and Decision

The paper has genuine theoretical value: it provides the first gradient-descent algorithm for adversarial preference feedback with near-optimal regret guarantees, matching lower bounds, and practically motivated extensions. However, the paper significantly overclaims its RLHF/trajectory connection (promising policy optimization it never delivers), presents experiments without any baselines (making empirical validation uninformative), and uses an "optimality" label that is qualified by an uncharacterized constant. These shortcomings are substantive enough that the paper in its current form cannot be accepted. With major revisions — particularly honest re-scoping, proper baselines, and complete experimental reporting — the underlying work could form the basis of a stronger submission.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>