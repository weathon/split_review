Now I'll write the final consolidated review.

**Final Calibration Report (all rounds):**

**Round 1 — Bracketing:**
- Weak band (<3.5): aMXVp1QK2Q (2.50), ularVAZFjX (2.00), teFnaEdG2j (3.33), NNqi3tBcZr (3.00)
- Middle band (3.5–7.5): mhJ9jO7ue8 (4.00), OPZ2f3MnrQ (4.50), aTxnsFFO7t (5.33), EkTm1JCUEH (5.00)
- Strong band (>7.5): Ahdsg2nkNH (8.00), oBXfPyi47m (8.00), VaS6xcDrTb (8.50), qOyF214xmg (8.00)

**Round 1 bracket: [3.0, 5.0]**

**Round 2 — Narrowing within bracket:**
Read in full: OPZ2f3MnrQ (4.50 — weight clipping for WCP, rigorous theory but strong assumptions, Reject), YM6KIpl6aR (5.00 — transductive CP bounds, interesting theory but limited experiments, Reject), qG6O3jMkCj (4.80 — SurvHTE-Bench, solid benchmark with minor novelty issues, Accept Poster), hau96a8YO5 (3.50 — flow matching for conformal regression, poor presentation, Reject), EkTm1JCUEH (5.00 — PPI through CP, interesting but conservative, Reject)

**Comparison:** The paper under review has a more serious theoretical flaw (derivation error visible in main text) than any of the 4-5 point anchors, but has stronger empirical evaluation and addresses a more novel problem than the 2-3.5 point anchors. It is closest to the OPZ2f3MnrQ (4.50) paper in having a theoretical contribution with a significant gap, but the gap here is more fundamental. Compared to the 3.50 anchor (flow matching for conformal regression), the paper has a worse theoretical issue but better empirical work and a more important problem.

**Final score: 3.0**

Now let me write the review.

I need to be careful about removing noise from the harsh critic's review while keeping the valid points. The harsh critic's main point about the inequality direction is valid. But some of the other criticisms (like the tower property not applying to probabilities) need to be verified.

The harsh critic says: "The tower property applies to expectations, not to probabilities." This is technically correct - the tower property is E[Y] = E[E[Y|Z]]. But in probability, P(A|Z) = E[I(A)|Z], so it can be applied indirectly. However, the specific claim that the tower property gives P(T ≤ d | X, W=w) * 1/p(e=1|...) is not correct, as I analyzed.

Let me write the review now.## Summary

This paper proposes a conformal prediction method for constructing lower prediction bounds (LPBs) for counterfactual survival times under different treatments in the general right-censored setting. The core idea is a reweighting scheme that aims to transform the coverage probability into a weighted conformal inference problem, enabling an LPB with a claimed exact marginal coverage guarantee (as opposed to the PAC-type guarantees of prior work). The method is evaluated on synthetic data and a real lung-cancer dataset with multiple radiochemotherapy regimens.

## Strengths

- **Addresses an important and well-motivated problem.** Providing statistically rigorous lower prediction bounds for counterfactual survival times under general right censoring is a genuinely open challenge. Prior work (Candès et al. 2023, Gui et al. 2024, Davidov et al. 2025) either assumes Type-I censoring or only provides PAC-type guarantees. The paper correctly identifies this gap and targets it.

- **Empirically thorough evaluation.** The experiments cover six synthetic settings with varying censoring/treatment rates, outlier perturbations, and a real clinical dataset of 541 lung-cancer patients. The method consistently achieves empirical coverage near the 90% nominal level while producing competitive LPB lengths (Figs. 1, 3). The real-data analysis (Fig. 4, 5) shows clinically plausible patterns (VMAT > IMRT, induction/concurrent chemo benefits), and the covariate-adaptive LPB plots demonstrate practical interpretability.

- **Outlier robustness demonstration.** In the outlier experiment (Fig. 3), the proposed method maintains near-nominal coverage when 10% of the data are corrupted with normal noise, while the Focus and Fused baselines (Davidov et al. 2025) show marked degradation. This robustness is notable and practically relevant.

- **Doubly robust property attempt.** Theorem 4.2 attempts to provide a doubly robust guarantee, which, if correctly established, would be a meaningful advance over existing methods.

## Weaknesses

### Major

- **The core derivation chain (Equation 1) has a mathematically incorrect inequality direction, undermining the central theoretical claim.** The derivation attempts to show that the miscoverage probability α is bounded above by a reweighted expectation over uncensored treated observations, which then justifies the weighted conformal calibration. However, the inequality from step (ii) to step (iii) in Eq. (1) is wrong. Specifically:

  Step (ii): E_X[ P(T ≤ d | X, W=w) · 1/p(e=1|X,W=w) ]  
  Step (iii): E_X[ P(T ≤ d, e=1 | X, W=w) · 1/p(e=1|X,W=w) ]

  Since P(T ≤ d, e=1 | …) ≤ P(T ≤ d | …) always (by monotonicity of probability), we have (ii) ≥ (iii). The paper claims (ii) ≤ (iii). Because the paper needs to establish α ≤ (iv) for the method's theoretical guarantee, and the chain as written relies on this incorrect inequality direction, the central theoretical justification is unsupported by the main-text derivation.

  The paper states that "(iii) is derived by the proof of Lemma A.1" (in the appendix, which is stripped by the parser and thus cannot be verified). However, basic probability is unambiguous: P(A, e=1) ≤ P(A) for any event A, so no lemma can change the relationship P(A)/p(e=1) ≥ P(A,e=1)/p(e=1). The inequality in the main text is simply wrong.

- **The "tower property" justification for step (ii) of Eq. (1) is not correctly explained.** The paper states that step (ii) "comes from the tower property." Applying the tower property to P(T ≤ d | X, W=w) would give a convex combination of P(T ≤ d | X, W=w, e=1) and P(T ≤ d | X, W=w, e=0) weighted by p(e=1|…) and p(e=0|…), respectively — not the expression P(T ≤ d | X, W=w) × 1/p(e=1|…) that appears in the paper. The correct inverse-probability-of-censoring (IPCW) identity is P(T ≤ d | X, W) = E[ I(T ≤ d, e=1) / p(e=1|X,W) | X, W ], which is structurally different from what the paper writes.

- **The target distribution in Theorems 4.1 and 4.2 does not match the paper's stated goal.** The paper's stated target (Section 3, "Goal") is marginal coverage P_{X,T(w)}(T(w) ≥ LPB) ≥ 1-α. However, Theorem 4.1 states coverage with respect to P_X × P_{T(w)|X, e=1}, and Theorem 4.2 similarly conditions on e=1. Conditioning on the uncensored subpopulation (e=1) is a byproduct of the flawed derivation and is not the unconditional marginal coverage claimed in the introduction. The paper does not clearly explain how or whether the (iv) step in Eq. (1) properly bridges this gap.

  These two issues — the incorrect inequality and the target distribution mismatch — mean that the paper's central claim of an "exact marginal coverage guarantee" is not supported by the presented theoretical analysis. The method may still work empirically (and the experiments suggest it does), but the theoretical foundation provided is insufficient.

- **The per-test-point τ optimization raises data-splitting concerns.** The LPB optimization chooses τ*(x) per test point to maximize q̂_τ^{(w)}(x) - c_{1-α}^{(w)}(τ)(x), where c_{1-α}^{(w)}(τ) is estimated from the calibration data. If τ is chosen adaptively per test point, then c_{1-α}^{(w)}(τ) is no longer a fixed quantile but is evaluated at a data-dependent threshold. The paper does not discuss whether this adaptive selection breaks the exchangeability or the conformal guarantee.

### Minor

- **The baseline comparison is asymmetric.** The paper highlights that Focus and Fused (Davidov et al. 2025) provide only PAC-type guarantees while the proposed method claims exact coverage. Yet in the non-outlier settings, all methods achieve similar empirical coverage near 90%. The outlier experiment is where the baselines visibly fail, but the theoretical flaw in the proposed method makes it unclear whether its robustness there is principled or coincidental. The paper would benefit from more detailed discussion of how the baselines were re-implemented.

- **The weight estimation procedure is not central to the evaluation.** The method relies on estimating γ(x) = p(W=w, e=1 | x) via Random Forest classifiers, but there is no systematic ablation showing how the quality of this estimate affects coverage. Theorem 4.1 quantifies this via the L1 error of the estimated density ratio, but the experiments do not include a controlled study varying the weight estimation quality.

- **"Exact" versus asymptotic.** The paper claims an "exact" marginal coverage guarantee, but Theorem 4.1 includes an error term that depends on the density-ratio estimation error (which only vanishes asymptotically), and Theorem 4.2 is asymptotic. The "exact" language in the abstract and introduction is somewhat overstated.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- Clarify whether the per-test-point τ optimization is justifiable within the weighted conformal framework, or whether a held-out selection procedure is needed.
- Include an ablation study where the quality of the weight estimate γ̂(x) is explicitly varied (e.g., by using misspecified propensity/censoring models) to validate Theorem 4.1's bound empirically.
- Provide additional intuition or a corrected version of the main derivation (Eq. 1) that the authors believe holds, perhaps using standard IPCW identities rather than the problematic tower-property argument.

## Removed Points

1. **"The tower property applies to expectations, not probabilities" (Harsh Critic).** While technically correct that the tower property is formally an expectation identity, P(· | Z) = E[I(·) | Z] bridges this gap, so this framing alone is not a weakness. The actual weakness is that the *specific expression* in step (ii) does not follow from the tower property as claimed. This is subsumed into the Major weakness above.

2. **"Missing appendix / unverifiable Lemma A.1."** Per the rules, the paper's appendix exists in the original submission and was stripped by the parser. The criticism about the inequality direction is retained because it is a visible mathematical error in the main text, not because the appendix is missing.

3. **Strength Finder claims about "exact marginal coverage" being a core strength.** This strength is factually what the paper claims, but it is undermined by the derivation issue. It is retained as a stated contribution but with the caveat that the theoretical support is insufficient.

4. **Several generic strengths from the Strength Finder** (e.g., "the paper addresses an important problem," "the reweighting scheme is interesting") — these are generic and are either merged into the evaluation above or removed as superficial.

## Novel Insights

The harsh critic correctly identified that the inequality direction in Eq. (1) from (ii) to (iii) is reversed relative to what basic probability dictates. What is less obvious but equally important is that the "tower property" step itself cannot produce the claimed expression — the paper appears to conflate a standard IPCW identity (E[ I(T ≤ d, e=1) / p(e=1|X,W) | X, W]) with the non-IPCW expression P(T ≤ d | X, W) × 1/p(e=1|X,W). These are different quantities, and the derivation uses the wrong one. The empirical results suggest the method *may* still work, but the theoretical path presented is not recoverable with cosmetic fixes — it would need to be substantially re-derived.

## Suggestions

1. **Re-derive the reweighting step correctly.** Use the standard IPCW identity: under T ⟂⟂ C | X, W (which follows from Assumption 3.1), we have P(T ≤ d | X, W) = E[ I(T ≤ d, e=1) / p(e=1|X,W) | X, W ]. This directly connects the marginal miscoverage probability to an expectation over uncensored observations without the problematic tower-property or inequality-direction issues. From there, the weighted conformal calibration follows naturally.

2. **Clarify the target distribution.** State explicitly in Theorem 4.1 and 4.2 whether the coverage guarantee is for P_X × P_{T(w)|X} (marginal) or P_X × P_{T(w)|X, e=1} (conditional on being uncensored). If the latter, explain why this is meaningful and how it relates to the stated goal.

3. **Address the τ-optimization issue.** Either show that the per-test-point selection of τ is valid within the weighted conformal framework (e.g., the coverage guarantee holds simultaneously for all τ), or restrict τ to be chosen from the calibration data alone.

4. **Add an ablation on weight estimation quality.** Simulate settings with misspecified γ(x) to verify that coverage degrades gracefully as predicted by Theorem 4.1.

## Score and Decision

**Anchors used (all rounds):**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| aMXVp1QK2Q | 2.50 | 1 | Lower quality, withdrawn paper on similar survival + CP topic — our paper is stronger empirically |
| ularVAZFjX | 2.00 | 1 | Unrelated CP pitfall paper — not comparable |
| teFnaEdG2j | 3.33 | 1 | Bayesian CP approach, sound but limited — our paper tackles a harder problem but has a worse theoretical gap |
| NNqi3tBcZr | 3.00 | 1 | Conformal risk-averse decision making — similar quality tier, our paper better motivated |
| mhJ9jO7ue8 | 4.00 | 1 | DML for survival under poor overlap — rigorous theory, less novel — our paper has a more serious flaw |
| OPZ2f3MnrQ | 4.50 | 1,2 | Weight clipping for WCP — rigorous theory with strong assumptions; our paper has a more fundamental issue |
| aTxnsFFO7t | 5.33 | 1 | Privacy-protected causal survival — solid theory, accepted — our paper is well below this |
| EkTm1JCUEH | 5.00 | 1,2 | PPI through CP — interesting but conservative; our paper has a more significant error |
| Ahdsg2nkNH | 8.00 | 1 | Unrelated topic — not comparable |
| oBXfPyi47m | 8.00 | 1 | Unrelated topic — not comparable |
| VaS6xcDrTb | 8.50 | 1 | Unrelated topic — not comparable |
| qOyF214xmg | 8.00 | 1 | Unrelated topic — not comparable |
| YM6KIpl6aR | 5.00 | 2 | Transductive CP bounds, theory-only, limited experiments — our paper has more empirical work but a worse theoretical flaw |
| hau96a8YO5 | 3.50 | 2 | Flow matching for conformal regression, poor presentation — similar quality tier, our paper has worse theory but better experiments |
| qG6O3jMkCj | 4.80 | 2 | SurvHTE-Bench — solid benchmark, accepted poster — our paper has a more significant theoretical gap |
| xnA1OpoAze | 3.60 | 2 | Dependent censoring test — not directly comparable |

**Round 1 bracket: [3.0, 5.0]**  
**Narrowing pass:** The paper is weaker than the 4.5-5.0 anchors (which have correct theory but different gaps) and comparable to or slightly weaker than the 3.5 anchor (flow matching for conformal regression). The derivation error in the main text is a genuine mathematical mistake, not a matter of taste or scope. This pulls the score toward the bottom of the bracket.

**Final score: 3.0**

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>