Now I have a comprehensive understanding of the paper. Let me write the consolidated review.

## Summary

This paper studies the multi-play multi-armed bandit with shareable arm capacities (MP-MAB-SAC) problem under a **new reward model** where noise is additive (independent of the number of plays), unlike prior work where noise scales with usage. The authors prove tight sample complexity bounds (Ω(σ²/μ_k² log δ⁻¹) with a matching algorithm ActInfCap), the first instance-independent regret lower bound (Ω(σ√(TK))), a strengthened instance-dependent regret lower bound (Ω(∑ cσ²/μ_k² log T)), and an algorithm PC-CapUL with regret upper bounds. The core theoretical machinery and the sample complexity result are solid contributions.

## Strengths

- **Tight sample complexity bounds for the additive-noise model.** Theorem 1 proves a minmax lower bound of Ω(σ²/μ_k² log δ⁻¹), and Theorem 2 shows that ActInfCap achieves a matching upper bound. This is a clean, self-contained result that improves upon the trivial Ω(log δ⁻¹) lower bound implied by Wang et al.'s condition.

- **First instance-independent regret lower bound for this problem class.** Theorem 3 establishes Ω(σ√(TK)), filling a gap left by prior work which only provided instance-dependent bounds. The bound's independence from arm capacities m_k aligns with the sample complexity finding.

- **Strengthened instance-dependent regret lower bound.** Theorem 4 gives Ω(∑_{k=1}^K (cσ²/μ_k²) log T), which introduces a dependence on μ_k⁻² and removes dependence on m_k compared to the Ω(∑_k log T) lower bound of Wang et al. (2022a) under their restrictive condition. This is a genuine improvement in understanding which parameters govern learning difficulty.

- **Improved confidence intervals for capacity estimation.** The paper derives tighter UCB/LCB (Equations 10–11) that place the UE estimation error term above the denominator rather than in it, yielding narrower intervals and faster convergence compared to Wang et al. (2022a).

- **Algorithm PC-CapUL with well-motivated design principles.** The four design insights (preventing excessive UEs, balancing UE/IE, prioritizing favorable arms, stopping on convergence) are explicitly tied to the lower bound analysis, giving the algorithm a principled motivation.

## Weaknesses

### Fatal
None.

### Major

- **Framing overstates the connection to prior work.** The paper introduces a structurally different reward model (additive noise, R_k(a_k) = min{a_k,m_k}μ_k + ε_k) compared to Wang et al.'s scaling-noise model (R_k(a_k) = min{a_k,m_k}(μ_k + ε_k)), yet repeatedly claims to "close the sample complexity gap of Wang et al." The paper does acknowledge the model difference (Section 1: "we reduce the capacity information in the reward to the minimum"), but the framing throughout — including in the abstract, introduction, and conclusion — presents the results as resolving open problems from Wang et al.'s model rather than establishing tight bounds for a new, harder variant. Since capacity information resides only in the mean under the new model but in both mean and variance under Wang et al.'s, these are meaningfully different problems. The paper should be reframed as studying a harder variant and providing tight limits for it, not as closing gaps in prior work's model.

- **Experimental comparison is insufficiently controlled.** The baselines MP-SE-SA and Orch from Wang et al. (2022a) were designed for the scaling-noise model, where variance carries capacity information. They are applied to the additive-noise model without any reported adaptation or re-tuning. The performance gap observed in Figure 1 is therefore expected — baselines that relied on variance for capacity information will naturally struggle when that signal is removed. A more informative comparison would: (a) adapt the baselines to the additive-noise setting by modifying their confidence intervals accordingly, or (b) include a simple UCB-on-discretized-actions baseline or explore-then-commit baseline that is agnostic to the noise structure. Without this, the experiments do not convincingly isolate whether PC-CapUL's advantage comes from its specific design or simply from being designed for the right model.

- **Instance-independent upper bound does not cleanly match the lower bound.** The instance-independent regret lower bound (Theorem 3) is Ω(σ√(TK)), while the instance-independent upper bound (Theorem 6) is O(σ√(9216M³ + 128KM + 1152M²N)M(T log T)) plus additive terms in M, K, N, and m_k. These are not of the same form, and the paper's claim that they "match the lower bounds up to some acceptable model-dependent factors" is not justified. The bound does not simplify to σ√(TK) under natural conditions (e.g., M = O(K)), and the "model-dependent factors" are never characterized. The paper should either tighten the bound, provide explicit conditions under which the match holds, or honestly state that minimax optimality remains open for the instance-independent regret.

### Minor

- **Instance-dependent upper bound structural comparison is incomplete.** Theorem 5's upper bound contains terms like Σ_i (2304σ²m_i²/μ_i²) log T that are not directly comparable to Theorem 4's Σ (cσ²/μ_k²) log T. While both have μ_k² in the denominator, the presence of m_k² and M-dependencies in the upper bound is not discussed relative to the lower bound's absence of m_k dependence. A clearer itemized comparison of how the upper bound terms map to lower bound terms would help.

- **Notation clarity.** The definitions of ĉ_{k,t} and î_{k,t} (lines 124–128) depend on m_{k,s-1}^l and m_{k,s-1}^u, which are themselves iteratively defined. This circularity is standard in confidence-bound-based algorithms, but the main text could briefly explain why it does not break the argument (e.g., by noting that the event A_k guarantees correctness inductively). This is acceptable if the appendix proof covers this, but stating the inductive assumption explicitly in the main text would improve readability.

### Trivial
None.

## Nice-to-Haves

- Adding a naive rounding strategy (rounding estimated capacities to nearest integer) or explore-then-commit baseline would strengthen the empirical validation.
- Adapting the Wang et al. baselines to the additive-noise setting and re-running the experiments would make the comparison more informative.
- A more explicit discussion of when M = O(K) (e.g., when capacities are bounded) and what this implies for the instance-independent upper bound would clarify the claimed matching.

## Removed Points

These points (from the reviewer inputs) were removed or downgraded after cross-checking against the paper:

- **"The paper changes the reward model without adequately distinguishing this from prior work"** — Partially removed. The paper DOES acknowledge the model difference (lines 25–29). The substantive remaining point is about the framing/overclaim, which is kept in Major.
- **"The paper's writing is often unclear and contains notation that is defined only implicitly" (circular dependency complaint)** — Downgraded to Minor. The confidence-interval circularity is standard in the bandit literature and is resolved in the appendix; this is not a structural problem.
- **"No comparison against a naive rounding strategy or a simple explore-then-commit baseline"** — Moved to Nice-to-Haves. Useful additional baselines but not a flaw in the current comparison.
- **Strength: "Algorithm PC-CapUL with regret upper bounds that match lower bounds"** — Modified. The instance-dependent case has structural similarity, but the instance-independent case does not clearly match. The overclaim is noted as a weakness; the strength is retained only in a qualified form.

## Novel Insights

None beyond the paper's own contributions. The key novel insight identified by the reviewers is that the sample complexity of arm capacity estimation depends on per-unit reward mean μ_k rather than arm capacity m_k — but this is already the paper's own stated finding. The reviewer discussions do not surface an additional insight not present in the paper.

## Suggestions

1. **Reframe the contribution honestly.** The abstract and introduction should clearly state that the paper studies a **variant** of MP-MAB-SAC with additive noise (where capacity information resides only in the mean), and that tight bounds are established for this variant. The connection to Wang et al. should be described as "we consider a harder variant where the variance carries no capacity information, and provide tight bounds that contrast with the loose bounds in the prior model," not as "closing the gap of Wang et al."

2. **Adapt baselines or add model-agnostic ones.** Re-run experiments with baselines adapted to the additive-noise setting, or add baselines that do not rely on the noise structure (e.g., discretized-action UCB, explore-then-commit on rounded estimates).

3. **Clarify the instance-independent regret gap.** Either simplify Theorem 6 to a form comparable to Theorem 3 under explicit conditions (e.g., when m_k ≤ C for all k so M = O(K)), or state candidly that minimax optimality for instance-independent regret remains open.

4. **Add a structural comparison table for the bounds.** A table showing lower bound terms → corresponding upper bound terms for each of Theorems 3–6 would make the "matching" claim transparent and allow readers to assess which factors remain unclosed.

---

## Score and Decision

The paper makes genuine theoretical contributions: tight sample complexity bounds for the additive-noise variant and new regret lower bounds. However, the framing overstates the connection to prior work (claiming to close gaps in a different model), the experiments use non-adapted baselines that cannot produce a fair comparison, and the instance-independent upper bound does not cleanly match the lower bound as claimed. These issues are fixable with a major revision, but in its current form the paper's narrative is misleading and its empirical claims are not properly supported.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>