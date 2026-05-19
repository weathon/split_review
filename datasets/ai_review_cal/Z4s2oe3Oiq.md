- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have thoroughly read the paper and verified claims against it. Let me write the consolidated review.

## Summary

This paper introduces normalized variants of error feedback algorithms (normalized EF21 and normalized EF21-SGDM) for nonconvex optimization under (L₀,L₁)-generalized smoothness. The core theoretical contribution is the first convergence analysis showing that normalized EF21 achieves an O(1/√K) rate in gradient norm and normalized EF21-SGDM achieves an O(1/K^{1/4}) rate, matching the rates of the original algorithms under classical smoothness. The analysis requires no data heterogeneity assumptions and uses stepsize rules that do not depend on smoothness constants for the deterministic case.

## Strengths

1. **First convergence analysis of error feedback algorithms under generalized smoothness.** The paper proves that normalized EF21 (Theorem 1) and normalized EF21-SGDM (Theorem 2) converge under (L₀,L₁)-smoothness at rates matching those of the originals under classical L-smoothness. The analysis covers distributed settings with contractive compressors, and the rates (O(1/√K) deterministic, O(1/K^{1/4}) stochastic) align with the known optimal rates for this class of methods.

2. **Analysis eliminates data heterogeneity assumptions and (for deterministic case) smoothness-dependent stepsizes.** The paper explicitly contrasts its assumptions against prior distributed analyses under generalized smoothness (Crawshaw et al. 2024, Liu et al. 2022) that require bounded data heterogeneity, almost-sure variance bounds, or symmetric noise assumptions. The normalized EF21 stepsize γ_k = γ₀/√(K+1) (Theorem 1) depends only on a positive constant γ₀ and total iterations K, not on L₀ or L₁. This removes a practical barrier — the original EF21 stepsize depends on the often-unknown classical smoothness constant L.

3. **Extension to stochastic momentum setting with matching rates and recovery of known methods.** Theorem 2 gives an O(1/K^{1/4}) rate for normalized EF21-SGDM, matching EF21-SGDM (Fatkhullin et al. 2024). The paper correctly shows that with α=1 (no compression), the result recovers a distributed version of NSGD-M, with a σ/√n noise reduction term that matches single-node NSGD-M results (Hubler et al. 2024) while extending to the multi-node setting.

4. **Well-designed logistic regression experiments.** In Section 6.1, EF21 is given its theoretically justified stepsize from Richtarik et al. (2021, Theorem 1), while normalized EF21 uses γ₀/√(K+1) with γ₀=1. This is a fair setup, and the results across three datasets show faster convergence and higher accuracy for normalized EF21, providing genuine empirical support for the advantage of larger allowable stepsizes.

## Weaknesses

### Fatal
None.

### Major

1. **ResNet-20 experiment uses a shared, unjustified stepsize that does not constitute a fair comparison.** The experiment (Section 6.2) runs both EF21 and normalized EF21 with constant stepsize γ=5, with no justification for why this value is appropriate for EF21. For deep networks under classical smoothness, EF21's theoretical stepsize would typically be on the order of 1/L (where L is large), making γ=5 potentially orders of magnitude too large. The comparison demonstrates that normalized EF21 can tolerate a large stepsize that causes EF21 to fail — which is consistent with the paper's claim about "larger allowable stepsizes" — but does not address the more informative question of whether normalized EF21 outperforms a well-tuned EF21. The paper's abstract states that normalized EF21 "outperforms EF21 on various tasks, including … ResNet-20 training," and the experiment as designed does not cleanly support this. This is fixable (e.g., by tuning each algorithm's stepsize or showing a sweep), but as presented it weakens a key empirical claim.

### Minor

2. **Theorem 1's bound contains an exponential factor that could become large.** The bound has a term exp(8c₁L₁ exp(L₁γ₀)γ₀²). While the paper immediately provides the clean bound obtained by choosing γ₀ = 1/(8cL₁) (line 134), the theorem statement itself presents the exponential-bound form as the main result. The presentation would be clearer if the corollary were more explicitly separated, or if the theorem stated the bound in its simplified form with the γ₀ restriction, noting that the more general form appears as a remark.

3. **No variance or confidence information reported across experiments.** The logistic regression and ResNet-20 experiments involve stochasticity (random initialization, mini-batch sampling), but all plots show single runs with no error bars, multiple seeds, or statistical characterization. Without this, it is difficult to assess whether the observed improvements are robust or within the noise of the experimental setup.

4. **The theoretical advantage of "stepsize independent of smoothness constants" is limited to the deterministic case.** The paper honestly notes (line 181) that Theorem 2's stepsize condition for normalized EF21-SGDM depends on L₁ and α. This is a genuine qualification to a claimed contribution itemized in the introduction.

5. **Stepsize schedule requires K to be known in advance.** The deterministic stepsize γ_k = γ₀/√(K+1) depends on the total iteration budget K, making it unsuitable for anytime algorithms. The paper acknowledges this only briefly in the future work section (line 236) rather than as a limitation of the current analysis.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing normalization versus clipping for EF21 under the same generalized smoothness setting would strengthen the specific claim about normalization being the crucial ingredient.
- A stepsize sweep or grid search for both algorithms on ResNet-20 would convert a questionable comparison into a convincing one.

## Removed Points

These points were flagged by one or both reviewers but are removed after verification against the paper:

1. **"First proof claim is overstated."** The critic argued the claim conflates error feedback with EF21 specifically. The paper clearly discusses normalized error feedback algorithms (EF21 and EF21-SGDM) and existing works on clipped/normalized gradient descent do not analyze error feedback mechanisms. The claim is technically correct and not misleading. → **Removed as not a genuine weakness.**

2. **"Paper does not discuss that normalized EF21 is worse under traditional smoothness (L₁=0)."** The paper explicitly states at line 156: "the convergence bound of normalized EF21 is slower by a factor of 2√2 than the original EF21 for nonconvex, L-smooth problems." → **Removed — paper already addresses this.**

3. **"Missing ablation comparing normalization to clipping."** This is not required for the paper's stated scope (introducing and analyzing normalization). → **Moved to Nice-to-Haves.**

4. **"No mention of K being known in advance."** The paper mentions this in the future work section (line 236) as motivation for adaptive stepsizes. While it could be more explicit as a limitation, the paper does not ignore it. → **Downgraded to Minor (#5 above) with acknowledgment of the paper's existing mention.**

5. **Harsh Critic's "Strengthening the Paper" paragraph about redesigning the ResNet-20 experiment.** This is an actionable suggestion, already reflected in the Major weakness. → **Consumed into Major weakness #1 and Nice-to-Haves.**

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the paper's strong theoretical contributions and a flawed experimental design decision, but neither reviewer identifies a conceptual blind spot or unexpected implication that the authors themselves do not discuss.

## Suggestions

1. **Redesign the ResNet-20 comparison.** Either (a) run EF21 with its theoretically justified stepsize (using an estimate of L) alongside normalized EF21 with its own stepsize, or (b) perform a stepsize sweep for both algorithms and report best-case performance, or (c) frame the experiment explicitly as a robustness test ("normalized EF21 can tolerate large stepsizes that cause EF21 to diverge") rather than as a head-to-head accuracy comparison.

2. **Add variance information.** Even two or three seeds with min-max bands would substantially strengthen the empirical claims, particularly for the stochastic ResNet-20 experiment.

3. **Restructure Theorem 1's presentation.** Consider stating the bound after choosing γ₀ = 1/(8cL₁) as the main theorem, with the more general (exponential) bound as a corollary or remark, since the latter is what supports the clean O(1/√K) rate.

4. **Explicitly acknowledge the anytime-algorithm limitation** (K must be known in advance) in a limitations paragraph rather than only in future work.
