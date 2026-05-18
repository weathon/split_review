I now have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper studies the multi-play multi-armed bandit with scarce sharable arm capacities (MP-MAB-SAC). It introduces a new reward model (Eq. 5) where noise is additive and independent of the action, in contrast to prior work (Wang et al. 2022a) where noise scaled with the number of plays. Under this model, the paper proves: (1) a matching sample complexity lower bound $\Omega(\sigma^2/\mu_k^2 \log \delta^{-1})$ and algorithm ActInfCap that achieves it; (2) the first instance-independent regret lower bound $\Omega(\sigma\sqrt{TK})$ and a strengthened instance-dependent lower bound; (3) a novel algorithm PC-CapUL with both instance-dependent and instance-independent regret upper bounds. The paper claims to "close the sample complexity gap" left by Wang et al. (2022a).

## Strengths

- **Matching sample complexity bounds under the new model.** Theorem 1 proves a lower bound $\Omega(\sigma^2/\mu_k^2 \log \delta^{-1})$ for learning an arm's capacity, and Theorem 2 provides ActInfCap with an upper bound matching it exactly (up to a universal constant). This is a clean theoretical contribution — the lower bound uses Le Cam's method with careful tracking of UE/IE counts, and the algorithm achieves matching complexity.

- **First instance-independent regret lower bound for this setting.** Theorem 3 establishes $\Omega(\sigma\sqrt{TK})$, which was absent from prior work. The bound reveals that the minmax difficulty scales with $\sqrt{TK}$ and has no dependence on arm capacities $m_k$, a non-trivial insight.

- **Novel algorithm PC-CapUL with theoretical guarantees.** Algorithm 2 introduces four design principles (preventing excessive UEs, balancing UE/IE, favoring higher-mean arms, stopping on convergence) and comes with both instance-dependent (Theorem 5) and instance-independent (Theorem 6) regret upper bounds. The algorithm is structurally novel compared to prior work.

- **Tighter confidence intervals.** The paper derives new confidence intervals (Eqs. 10–11) that place the UE estimation error in the numerator rather than the denominator, yielding faster convergence than Wang et al. (2022a)'s intervals. This is a concrete technical improvement.

## Weaknesses

### Fatal
None. The core theoretical results are technically valid under the stated model.

### Major

- **Framing overclaim: the paper states it "closes the gap of Wang et al. (2022a)" but studies a different reward model.** Wang et al.'s model was $R_k(a_k) = \min\{a_k,m_k\}(\mu_k + \epsilon_k)$ (noise scales with action), while the paper's model is $R_k(a_k) = \min\{a_k,m_k\}\mu_k + \epsilon_k$ (constant noise). The sample complexity gap in Wang et al. existed under their noise model; the paper proves matching bounds under a *different* noise model. While the paper clearly states the model change (lines 25–31, Eq. 5) and argues the new model is "harder" and "more fundamental," the central rhetorical claim — appearing in the abstract, Section 1.1, and conclusion — that this "closes the sample complexity gap of Wang et al. (2022a)" conflates the two problems. The paper never shows the gap can be closed under the original model. This is a fixable framing issue but undermines how the contribution is currently positioned. The honest framing would be: "We study a harder variant that strips variance information and provide tight bounds that were not achievable under the original model."

- **Substantial gap between upper and lower bounds in parameter dependence.** Theorem 3's instance-independent lower bound is $\Omega(\sigma\sqrt{TK})$ — free of $M$ (total capacity), $N$ (plays), and $m_k$ (arm capacities). Theorem 6's instance-independent upper bound includes terms like $\sqrt{(9216M^3 + 128KM + 1152M^2N)M \cdot T\log T}$ — with $M^3$ and $N$ inside the square root. The paper's claim that these "match up to some acceptable model-dependent factors" is not adequately justified; the gap in parameter dependence ($M^3$ vs. no $M$) is structural. Similarly, the instance-dependent bounds (Theorems 4 vs. 5) show $m_k^2$ and $N$ factors in the upper bound absent from the lower bound. The paper should either explain why these factors are unavoidable or acknowledge the gap honestly.

- **Thin experimental evaluation.** Only one experimental configuration is shown: varying $K$ (10–40) in Figure 1. Key parameters that appear in the theory ($\mu_k$, $\sigma$, $c$, $N$, $M$) are listed in the experiment setting (Section 6.1) but results for their variation are not reported. No ablation isolates the four design principles of PC-CapUL. No experiment verifies the claimed sample complexity of ActInfCap. Additionally, the values of $\mu_k$ and $\sigma$ used in experiments are not specified, making the results difficult to interpret or reproduce. While a theory paper need not have exhaustive experiments, the current evidence is too narrow to support the claim that the algorithm is "data efficient" across the settings the theory covers.

- **Pseudocode inconsistency in Algorithm 2.** Lines 319–320 of Algorithm 2 set and then immediately overwrite the same variable $w_k$ for all arms. Line 319 implements "preventing excessive UEs" (principle 1): $w_k \leftarrow \mathbb{I}\{\hat{\tau}_{k,t-1} \leq \hat{\iota}_{k,t-1}\}$. Line 320 then resets $w_k \leftarrow \mathbb{I}\{Cndt_k = 0\}$ for all $k$, completely discarding the computation from line 319. For unconverged arms ($Cndt_k = 1$), this forces $w_k = 0$ (i.e., always do UE), contradicting the described principle. This appears to be a bug or an error in the pseudocode that would prevent a reader from correctly implementing the algorithm as described in the text.

### Minor

- **Model realism unargued for stated applications.** The paper motivates MP-MAB-SAC with LLM inference serving and edge intelligence. However, the noise model $\epsilon_k$ (constant, independent of the number of plays) is not justified for these settings. If per-query noise is independent, the aggregate noise variance should scale with the number of plays. The paper's only justification — "finds its root in the reward model of conventional linear bandits" — is a theoretical analogy, not an application-based argument. This does not invalidate the theory but weakens the connection to the claimed applications.

- **Non-standard confidence intervals without explanation.** The function $\phi(x,\delta) = \sqrt{(1+1/x) \cdot 2\log(2\sqrt{x+1}/\delta)/x}$ appears in Lemma 1's confidence intervals but its origin and tightness are not discussed. While the derivation would presumably appear in the appendix (which is stripped by the parser), the main text should at least sketch why this particular form yields tight bounds and how it compares to standard sub-Gaussian concentration inequalities.

- **Unspecified experimental parameters.** The sub-Gaussian parameter $\sigma$ and per-unit reward means $\mu_k$ used in the experiments are not reported. Without these, the experimental results cannot be reproduced or compared against the theoretical bounds.

- **Asymmetry between instance-dependent and instance-independent lower bounds on $c$.** The instance-dependent bound (Theorem 4) scales with movement cost $c$, while the instance-independent bound (Theorem 3) does not. The paper notes this but does not explain the intuition. If $c$ is very small, the instance-dependent bound can be arbitrarily small while the instance-independent bound remains positive — this apparent tension deserves discussion.

### Trivial
- None of significance beyond presentation issues attributable to the PDF extraction parser.

## Nice-to-Haves
- A discussion of what would change under the original Wang et al. (2022a) reward model (Eq. 1). Even a brief qualitative comparison would help position the contribution.
- Empirical verification of ActInfCap's sample complexity (Theorem 2), e.g., a plot of estimation error vs. number of samples for various $\mu_k$ and $\sigma$.
- Ablation study isolating the four design principles of PC-CapUL to quantify the benefit of each.
- Varying $c$, $N$, and $M$ in the experiments, since these appear in the theoretical bounds.

## Removed Points

The following points from the input reviews were removed or downgraded per the meta-review rules:

- *Criticism that proofs are missing from the main text (appendix-stripped sections)* — Per rules, removed as appendix-stripping is a parser artifact.
- *Criticism about the failure event handling in confidence intervals* — This is standard practice in bandit papers and was removed as a nitpick that does not affect the validity of the results.
- *Strength Finder's claim #1 as stated ("Closes the sample complexity gap left by Wang et al.")* — Weakened and reframed because the paper changes the reward model; see Major Weakness #1.
- *Strength Finder's supporting strength #1 ("A cleaner reward model that isolates capacity information")* — Weakened because the same model change that the strength praises is also the source of the framing overclaim (Major Weakness #1). It is kept as a qualified strength (the model is theoretically harder) but the accompanying weakness about the framing is what prevails.
- *Generic/redundant strengths from the Strength Finder* — Removed as they either conflict with verified weaknesses or lacked specific content.
- *The harsh reviewer's comment about the regret values being "enormous" as evidence of implementation issues* — Removed as speculative without knowledge of the (unreported) $\mu_k$ values.

## Novel Insights

None beyond the paper's own contributions. The reviews largely surface the same core tension: the paper makes a legitimate technical contribution under a new model, but the rhetorical framing of "closing gaps" in prior work conflates distinct problem settings. The most interesting meta-point is that changing the noise model (from variance-scaling to constant) fundamentally changes which lower bound techniques apply and which parameters matter — removing the variance signal makes the mean $\mu_k$ the sole carrier of capacity information, which is both a theoretical purification and a practical departure from the motivating applications.

## Suggestions

1. **Reframe the contribution.** Replace "closes the sample complexity gap of Wang et al. (2022a)" with language like "under a stricter reward model that removes variance information, we prove matching bounds that are tighter than those achievable under the original model." This honestly positions the contribution without conflating two distinct problem settings.
2. **Fix the pseudocode bug in Algorithm 2, lines 319–320.** The overwriting of $w_k$ makes the algorithm unimplementable as written. Either use separate variables or clarify the intended control flow (e.g., only override $w_k$ for converged arms).
3. **Acknowledge and discuss the upper/lower bound gap.** Provide a paragraph explaining which terms in the upper bound arise from which algorithmic components (e.g., confidence interval width, forced IE rounds, finite-time corrections) and whether the $M^3$ dependence is fundamental or an artifact of the analysis.
4. **Report $\mu_k$ and $\sigma$ values in experiments.** These are essential for reproducibility and for readers to interpret the regret scales.
5. **Run at least one additional experimental configuration** varying a parameter other than $K$ (e.g., $c$ or $N$) and include an ablation of the four design principles.

## Score and Decision

This paper has genuine theoretical contributions — matching sample complexity bounds, the first instance-independent lower bound under the studied model, and a novel algorithm with guarantees. However, the framing overclaim about "closing gaps" in prior work (under a different model), the structural gap between upper and lower bounds on key parameters, the thin experimental validation, and a concrete pseudocode bug collectively prevent the paper from being accepted in its current form. The core theory is salvageable, but a major revision that honestly reframes the contribution, fixes the algorithmic description, and strengthens the experimental evidence is needed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>