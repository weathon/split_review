Now I will produce the final consolidated review.

## Summary

This paper studies multi-objective linear bandits and makes the novel observation that diversity among multiple objectives can serve as a substitute for explicit exploration, enabling near-greedy algorithms to achieve near-optimal regret. The authors propose MORR-Greedy (a round-robin greedy algorithm) and MORO-Greedy, prove an Õ(√(dT)/λ₀) Pareto regret bound under sufficient diversity (Assumption 2) and γ-regularity (Assumption 3), introduce an "objective fairness" criterion, and provide limited experiments.

## Strengths

- **Free exploration from objective diversity is a genuinely novel insight.** The paper identifies a sufficient condition under which multiple objectives drive exploration without requiring the context diversity that prior greedy bandit literature (Kannan et al., 2018; Bastani et al., 2021) relied on. Lemma 1 shows that the minimum eigenvalue of the Gram matrix grows linearly at rate proportional to λ₀ under the round-robin scheme, even in fixed-context settings. This formalizes the intuition that multiple objectives can simplify rather than complicate the bandit problem.

- **Simple algorithm without empirical Pareto front.** MORR-Greedy (Algorithm 1) is a clean round-robin greedy algorithm that avoids constructing an empirical Pareto front each round, unlike existing methods such as P-UCB and MOGLM-UCB. The design is elegant and the computational advantage is real.

- **Objective fairness criterion.** Definition 4 introduces a new evaluation metric for multi-objective bandits, measuring whether each objective's near-optimal arms are selected a balanced fraction of the time. Theorem 2 provides a formal guarantee, and the bound does not depend on the number of arms K. This fills a gap in the existing Pareto-front literature that lacks such guarantees.

## Weaknesses

### Fatal
None.

### Major

1. **The spanning condition (Assumption 2) requires M ≥ d, which is very restrictive.** The diversity index λ₀ is defined as the minimum eigenvalue of (1/M)∑θₘ*(θₘ*)ᵀ, which is positive only if M ≥ d and the θₘ* span ℝᵈ. In most practical multi-objective problems, the number of objectives M is small (2–5) while the feature dimension d can be much larger. The paper acknowledges a relaxation to the span of feature vectors (Section F), but this still requires M ≥ rank({x₁,…,x_K}), which is similarly restrictive when the arm features are rich. The paper provides no concrete example of a realistic problem instance where M ≥ d holds naturally, nor does it discuss how the bound degrades when the condition is violated. Since this assumption is the foundation for the entire regret analysis, its narrow applicability seriously limits the practical relevance of the theoretical contribution.

2. **MORO-Greedy is claimed as a contribution but not evaluated.** The paper's contributions (lines 11–13) list both MORR-Greedy and MORO-Greedy as proposed algorithms, and claims that both achieve the regret bound and satisfy objective fairness. However, only MORR-Greedy is described in the main text (Algorithm 1), and the experiments only evaluate MORR-Greedy, P-UCB, and MOGLM-UCB. MORO-Greedy is never instantiated, tuned, or compared. An algorithm claimed as part of the contribution should appear in the empirical evaluation or at minimum receive a worked example in the main text.

### Minor

3. **The regret bound depends inversely on λ₀, which can be arbitrarily small.** Even when the spanning condition holds (M ≥ d), the θₘ* could nearly lie in a lower-dimensional subspace, making λ₀ arbitrarily close to zero and the bound correspondingly large. The constant C₁ ∝ 1/λ₀. The paper does not characterize regimes where λ₀ is meaningfully large, and the experiments do not report λ₀ values, so the reader cannot tell whether the good empirical performance occurs in favorable regimes or whether the theoretical bound would predict poor performance elsewhere. This fragility weakens the advertised "Õ(√(dT)/λ₀)" guarantee.

4. **The claim about existing algorithms and fairness is unsubstantiated.** Remark 1 states that most existing Pareto-front algorithms "are unlikely to satisfy the objective fairness criterion, because the empirical Pareto front continuously changes over time." No proof, counterexample, or supporting reference is given. This assertion is used to motivate a new fairness definition, but without evidence it reads as speculation.

5. **Experimental evaluation is narrow.** Experiments cover only two small settings: (d,K,M) = (3,8,3) and (4,16,5). Baselines are limited to P-UCB (2013) and MOGLM-UCB (2019); more recent multi-objective linear bandit methods (e.g., Cheng et al. 2024, Kim et al. 2023) cited in related work are not compared. While the results show consistent outperformance, the scale is too limited to support the claim that MORR-Greedy "consistently outperforms existing multi-objective methods across a wide range of scenarios."

### Trivial

- Definition 3's description says "ϵ ≤ 0" which appears to be a typo (should be ϵ ≥ 0 for a suboptimality gap). The formal expression with ⊀ is correct given Definition 1, but the superscript inconsistency should be fixed.

## Nice-to-Haves

- Providing concrete synthetic examples where Assumptions 2 and 3 simultaneously hold, with reported λ₀ values, would help readers gauge the realism of the conditions.
- A relaxation of the regret bound that degrades gracefully when M < d (e.g., replacing d with the dimension of the subspace spanned by the θₘ*) would strengthen the paper considerably.
- Running-time comparisons (wall-clock time) would substantiate the claimed computational advantage over Pareto-front methods.

## Removed Points

These points were flagged by reviewers but are removed or downgraded after verification against the paper:

- **Pareto regret definition ambiguity (Critical Issue 4 from harsh critic).** The notation "⊀" is explicitly defined in Definition 1. The formal expression Δ_i = inf{ϵ | (μ_i+ϵ) ⊀ μ_{i'}, ∀i'} is well-defined. The "ϵ ≤ 0" in the text is a typo/parser artifact—the underlying definition is standard and not ambiguous.
- **Proof of Lemma 1 "only sketched" (Critical Issue 5).** The full proof is in the appendix (which the parser strips from all papers). The main text correctly states Lemma 1 and its probability guarantee.
- **γ-regularity threshold is "arbitrary" (part of Critical Issue 2).** The threshold γ₀ > 1−λ₀²/18 arises from the algebraic geometry of the eigenvalue argument. This is characteristic of sufficient-condition analyses in bandit theory—not a flaw. The paper also relates γ-regularity to Bayati et al.'s β-regularity, putting it in context.
- **α₀/ψ replacement criticism (part of Critical Issue 2).** The paper's logic is correct: if α₀ > ψ, replacing α₀ with the smaller ψ tightens the condition (smaller neighborhood), so γ-regularity still holds. If α₀ ≤ ψ, no replacement is needed. The paper's handling is mathematically sound.
- **Missing appendix content or incomplete bounds.** All grievances about deferred proofs, Algorithm D.3.2, or incomplete T₀ bounds correspond to content the parser has removed. These exist in the original submission.
- **Generic strengths from Strength Finder.** The claimed strengths are all backed by specific lemmas/theorems and are retained in the Strengths section above.

## Novel Insights

The key insight that emerges from both the paper and the reviews is that objective diversity can serve as a structural substitute for context diversity in greedy bandit algorithms. This inverts the usual intuition that more objectives make bandits harder. The idea that a simple round-robin greedy schedule across objectives yields eigenvalue growth without explicit exploration is genuinely novel and could inspire follow-up work that relaxes the stringent M ≥ d condition, perhaps by using projection or regularization techniques. However, the current paper's sufficient conditions are too narrow for the insight to be broadly applicable as-is.

## Suggestions

1. **Relax the spanning requirement quantitatively.** If the θₘ* span only a  ̃d-dimensional subspace, the regret bound should be expressed in terms of  ̃d rather than d, with the bound degrading gracefully as  ̃d increases. This would make the theory applicable when M < d.

2. **Report λ₀ for experimental instances** so readers can interpret the regret bound in context. Better yet, design experiments that vary λ₀ to show how performance degrades as diversity decreases.

3. **Either evaluate MORO-Greedy or remove it from the contribution list.** A second algorithm claimed but not tested undermines reproducibility claims.

4. **Expand experiments** to include at least one comparison with a recent Pareto-front method (Cheng et al. 2024 or Kim et al. 2023) and at least one setting where d > M to probe the theory's limits.

5. **Provide an explicit numerical example** (e.g., in a synthetic setting with known λ₀ and γ₀) demonstrating that Assumptions 2–3 can be satisfied simultaneously with non-trivial parameter values.

## Score and Decision

The paper introduces a genuinely novel theoretical perspective—that objective diversity can drive exploration without context diversity—and proposes a clean algorithm. These are real strengths. However, the theoretical analysis rests on a spanning condition that effectively requires the number of objectives to be at least the feature dimension, which is violated in most practical settings. The paper offers no empirical evidence that this condition is ever naturally met, nor does it gracefully handle the common M < d regime. Additionally, the experiments are too narrow to convincingly demonstrate broad superiority, and a claimed second algorithm (MORO-Greedy) is not evaluated. The core idea is interesting but in its present form the paper's main theoretical result applies only to a restricted regime whose practical relevance is unexamined.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>