Now let me write the final review.

## Summary

The paper introduces Dig-DEC, a new model-free Decision-Estimation Coefficient that removes optimism and drives exploration purely through information gain. It is always ≤ optimistic DEC, and removing optimism enables handling adversarial/hybrid environments without explicit reward estimators. The paper obtains the first model-free regret bounds for hybrid MDPs (stochastic transitions, adversarial rewards) with bandit feedback, resolving the main open problem from [LWZ25]. It also improves online estimation procedures, achieving better regret rates in several settings.

## Strengths

1. **New complexity measure (Dig-DEC) that removes optimism**: Section 4 (Eq. 8) defines Dig-DEC with two information-gain terms (KL + $\overline{D}$), and Theorem 13 shows Dig-DEC ≤ optimistic DEC + η. Removing optimism is the key technical enabler for handling the hybrid adversarial setting without constructing explicit reward estimators — this directly solves the open problem from [LWZ25].

2. **First model-free regret bounds for hybrid MDPs with bandit feedback**: Table 2 reports regret bounds for hybrid bilinear classes and coverable MDPs under linear rewards with bandit feedback. This resolves the main open question from [LWZ25], who could only handle full-information feedback in their model-free algorithm.

3. **Improved estimation via unbiased cross-validation estimator**: Theorem 7 achieves Est ≲ N log|Φ| T^{1/2} using an unbiased estimator that splits τ episodes into two halves, improving the rate of [FGQ+23]'s biased estimator. The construction is clearly described at the bottom of Section 4.2.1.

4. **Constant estimation error under Bellman completeness**: Theorem 11 achieves Est ≲ log²|Φ| (independent of T) under Assumption 6, enabling √T regret for Bellman-complete MDPs (Table 1) — the first time a DEC-based method matches optimism-based approaches [JLM21, XFB+23] in this setting.

5. **Generalized AIR framework with flexible divergence**: Algorithm 1 and the analysis in Eqs. (5)–(6) connect to mirror descent via Bregman divergences, recovering prior AIR results [XZ23, LWZ25] more simply and accommodating general divergence measures beyond KL. The paper explicitly shows (Appendix C) that Est can avoid log|Φ| scaling entirely in the model-based hybrid full-information setting, which required a complex two-level algorithm in [LWZ25].

## Weaknesses

### Fatal
None.

### Major

1. **Numerical errors in abstract and introduction — off-policy "improvement" is actually a worsening.** The abstract states: "improving their regret bounds from $T^{\frac{3}{4}}$ to $T^{\frac{3}{5}}$ (on-policy) and from $T^{\frac{5}{6}}$ to $T^{\frac{7}{8}}$ (off-policy)." The on-policy change ($0.75 \to 0.6$) is indeed an improvement. However, the off-policy change ($0.833\ldots \to 0.875$) is a *worsening* — a larger exponent means larger regret. Similarly, the introduction (line 33) claims to improve "$T^{\frac{3}{2}}/T^{\frac{5}{8}}$" to "$T^{\frac{3}{2}}/T^{\frac{5}{6}}$", where $T^{5/8}\to T^{5/6}$ ($0.625\to 0.833$) is again a worsening. These are factual errors in the paper's most prominently displayed numerical claims. The off-policy comparison must be corrected and explained.

2. **Several entries in Table 2 show superlinear $T^{3/2}$ regret exponents, rendering the hybrid results uninterpretable from the main text.** The claimed regret for hybrid bilinear on-policy (with $\overline{D}_{\text{av}}$) is $d(H^5 \log|\Phi|)^{1/2} T^{3/2}$, and for coverable MDPs it is $d(H^3 \log^2|\Phi|)^{1/2} T^{3/2}$. A regret bound of $T^{1.5}$ is superlinear — not a meaningful guarantee. The caption states these bounds result from $T\cdot\text{dig-dec}_\eta + \textbf{Est}/\eta$ with optimal $\eta$, but plugging in $\text{dig-dec}_\eta = (H^5 d^3 \eta)^{1/2}$ and $\textbf{Est} = d\log|\Phi|\, T^{1/2}$ (Theorem 7) and optimizing $\eta$ yields a $T^{5/6}$ rate, not $T^{3/2}$. This discrepancy is unexplained. Additionally, Table 2 shows off-policy regret $T^{1/2}$ while on-policy shows $T^{3/2}$ for starred bilinear classes, contradicting the paper's own statement (page 8, line 255) that "the on-policy case has smaller regret." These issues make the hybrid results impossible to evaluate from the main text alone.

### Minor

1. **Theorem 14 (3-armed bandit separation) lacks any intuition in the main text.** The claim is very strong — $O(1)$ regret versus $\Omega(\sqrt{T})$ on a simple bandit — and the proof is entirely in Appendix J. A brief intuition in the main text (e.g., explaining how the KL information-gain term enables constant regret) would significantly increase reader trust.

2. **The relationship between Assumption 6 and Bellman completeness is asserted without explanation.** Lemma 12 states that Bellman completeness implies Assumption 6 (with $\xi_h$ as squared Bellman error and $B^2=1$ or $d$), but the variance-like inequality in Assumption 6 — $4B^2 \mathbb{E}[\xi_h(\phi',\phi)-\xi_h(\mathcal{T}_M\phi,\phi)] \ge \mathbb{E}[\xi_h(\phi',\phi)-\xi_h(\mathcal{T}_M\phi,\phi)]^2$ — is not immediate from completeness. A brief remark in the main text about why this follows (e.g., boundedness ⇒ sub-Gaussian tail ⇒ the inequality) would clarify an important step.

### Trivial
None.

## Nice-to-Haves

- A brief remark on whether the minimax problem (Eq. 3, Algorithm 1) is computationally tractable would be helpful for a theoretical paper.
- The paper discusses high-probability bounds for the stochastic setting but not for the hybrid setting; a brief comment on whether the same technique extends would be useful.

## Removed Points

These points were raised by the reviewers but are removed from the main weaknesses with justifications:

- **"Theorem 14 proof relegated to appendix"** (from Harsh Critic): Demoted from Major to Minor. Proofs in appendices are standard for theoretical papers. The retained concern is the lack of *any* intuition in the main text.
- **"Assumption 6 connection to Bellman completeness is a methodological gap"** (from Harsh Critic): Removed. Lemma 12 explicitly states the implication; proving it is what an appendix is for. The critic's speculation that "the inequality might fail" is not grounded in any specific counterexample or flaw in the paper's logic.
- **Missing related works, formatting/style nitpicks, computational complexity concerns, missing appendix content**: Removed per guidelines (parser strips appendices; formatting issues are parser artifacts; scope is appropriate for a theoretical paper).
- **Strength Finder generic strengths** (e.g., "important problem"): Removed. Not specific to the paper's evidence.
- **"off-policy/on-policy terminology clarification"** (from Harsh Critic): The paper already clearly states (line 255) these are subclasses of bilinear classes, not standard RL usage. The substance about Table 2 on-policy/off-policy contradiction is kept in Major weakness #2.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the numerical errors in the abstract and introduction.** The off-policy claims from $T^{5/6}$ to $T^{7/8}$ and from $T^{5/8}$ to $T^{5/6}$ are worsenings, not improvements. Verify the correct baseline and improved rates and fix all associated text.

2. **Re-examine and explain the $T^{3/2}$ entries in Table 2.** Either these are formatting errors, or a detailed derivation is needed showing how $T\cdot\text{dig-dec}_\eta + \textbf{Est}/\eta$ yields a superlinear $T^{3/2}$ rate after optimizing $\eta$. Clarify the on-policy vs. off-policy comparison in the hybrid setting and resolve the contradiction with the statement on line 255.

3. **Add a brief intuition for Theorem 14** in Section 6 explaining why $O(1)$ regret is possible on the 3-armed bandit.

4. **Add a brief remark** in Section 4.2.2 connecting the inequality in Assumption 6 to the bounded-squared-Bellman-error setting of Lemma 12.

## Round-1 bracket

Round-1 queries bracketed the paper between scores of 2.5–3.2 (weak band), 4.0–7.0 (middle band), and 8.0 (strong band). The paper is clearly not in the weak or strong bands, placing it in the 4.0–7.0 range.

## Round-2 narrowing

Round-2 anchors within the bracket:
- **aPNwsJgnZJ** (score 6.00, Accept): "Horizon-free RL in Adversarial Linear Mixture MDPs." Clean, correct theoretical results with no errors. The current paper has comparable theoretical ambition but verifiable numerical errors — weaker.
- **R4q3cY3kQf** (score 6.75, Accept): "MaxInfoRL." Strong empirical+theoretical work. Not directly comparable (empirical rather than theoretical).
- **0oWGVvC6oq** (score 6.50, Accept): "On Bits and Bandits." Clean information-theoretic results. Current paper has more significant errors.
- **GvsCOOPxoI** (score 6.17, Reject): "Provable Learning for DEC-POMDPs." Good theoretical contributions but rejected due to scope concerns. Current paper's errors are more directly verifiable.
- **w8Zo7jACq7** (score 5.20, Reject): "Model-Free, Regret-Optimal BPI in Online CMDPs." Strong assumptions but solid results. Current paper has broader contributions but verifiable errors in headline claims — comparable overall.
- **i8LCUpKvAz** (score 7.00, Accept): "Minimax Optimal RL with Quasi-Optimism." Clean, well-presented theoretical results with nice insights. Current paper has more significant presentational errors.

The paper sits below the clean, correct theoretical papers (scores 6–7) but above the incremental ones (scores 3–4). It is closest to w8Zo7jACq7 (5.20, Reject) in overall assessment — both have genuine contributions undermined by issues that prevent acceptance as-is. I place the paper at **5.0**.

## Score and Decision

The paper makes genuine theoretical advances (Dig-DEC, first model-free hybrid MDP bandit bounds, improved estimation). However, the numerical errors in the abstract and introduction, and the unexplained $T^{3/2}$ entries in Table 2, are factual errors in the paper's most prominent numerical claims. These are likely fixable, but in the current form they prevent a reader from evaluating the claimed contributions. The paper requires mandatory corrections before acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>