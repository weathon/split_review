Now I have a thorough calibration picture. Let me finalize.

**Round 1 bracket**: 5.5–7.0 based on the 6.0 anchor (horizon-free adversarial RL, similar type of contribution).

**Round 2 narrowing**:
- 5.50 anchor (en3NwykrHW — trajectory feedback RL): Our paper is stronger — broader scope, more contributions, resolves open problem.
- 6.50 anchor (0oWGVvC6oq — bits and bandits): Comparable technical depth but cleaner presentation and includes experiments. Our paper has more concrete RL results but significant presentation issues.
- 6.00 anchor (aPNwsJgnZJ — horizon-free adversarial RL): Most similar. Our paper has more breadth (stochastic + hybrid, multiple MDP classes) and resolves a stated open problem, but the 6.00 anchor has cleaner presentation and lower bounds. Comparable.

Our paper sits near 6.0: stronger than 5.50, comparable to 6.00, slightly below 6.50 due to the abstract/table rate inconsistency.

---

## Summary

This paper introduces Dig-DEC, a new model-free Decision-Estimation Coefficient that replaces the optimism principle of [FGQ+23] with information-gain-driven exploration. The framework yields (1) improved regret bounds for stochastic MDPs via better online function estimation (unbiased sample-splitting estimator and refined two-timescale procedure), (2) first model-free regret bounds for hybrid MDPs (stochastic transitions, adversarial rewards) with bandit feedback, resolving an open problem from [LWZ25], and (3) a unified Bregman-divergence-based analysis that recovers and extends prior AIR frameworks.

## Strengths

- **First model-free bandit regret bounds for hybrid MDPs.** By removing optimism and using information gain, Dig-DEC avoids explicit reward estimation, enabling the first sublinear regret for model-free learning in hybrid bilinear classes and coverable MDPs with bandit feedback (Table 2). Prior work [LWZ25] could only handle full-information reward feedback in the model-free hybrid case. This resolves a recognized open problem.

- **Matching √T regret for Bellman-complete MDPs within a DEC framework.** Theorem 11 establishes constant (in T) estimation error via a refined two-timescale procedure, which combined with Dig-DEC yields √T regret (Table 1, rows with ✓ completeness). This is the first time a DEC-based method matches the performance of optimism-based approaches [JLM21, XFB+23] for Bellman-complete MDPs — a meaningful technical advance.

- **Theorem 14 provides a clean separation result.** On a constructed 3-armed bandit, Dig-DEC achieves O(1) regret while optimistic DEC suffers Ω(√T). This concretely demonstrates that optimism is not fundamental and that the information-gain approach can yield arbitrarily large improvements, directly supporting the paper's central conceptual claim.

- **Generalized and simplified AIR analysis.** The framework with flexible divergence D^π (Eq. 2) and the Bregman-divergence-based regret decomposition (Eqs. 5–6) avoids the "constructive minimax theorem" of [XZ23] and unifies stochastic and hybrid settings under a single analysis. This is a genuine conceptual contribution that may facilitate future work.

- **Theorem 13 establishes dig-dec ≤ o-dec + η**, providing a formal guarantee that Dig-DEC subsumes the prior optimistic DEC complexity measure for any D̄, ensuring the new framework is never worse (up to an additive η).

- **Comprehensive instantiation.** Tables 1–2 demonstrate the framework across bilinear classes, Bellman-eluder dimension, and coverable MDPs in both stochastic and hybrid settings, with explicit dig-dec bounds and final regret rates.

## Weaknesses

### Fatal

None.

### Major

- **Inconsistent regret rates between abstract and main results.** The abstract (line 13) claims the average estimation error improvement yields regret bounds of T^{3/5} (on-policy) and T^{7/8} (off-policy), improving over [FGQ+23]'s T^{3/4} and T^{5/6}. However, Table 1 reports T^{2/3} for all non-Bellman-complete rows — a different rate. T^{3/5} = T^{0.6}, T^{7/8} = T^{0.875}, and T^{2/3} ≈ T^{0.667} are genuinely distinct numbers, not parser artifacts. Since these are the paper's headline quantitative improvements for the non-Bellman-complete case, the reader cannot determine which rates the paper actually proves. This inconsistency must be reconciled for the paper's claims to be credible.

### Minor

- **Source of regret improvements in RL settings is primarily estimation, not dig-dec.** The paper frames Dig-DEC as the central innovation, but for the canonical RL settings in Tables 1–2 (bilinear classes, BE dimension, coverability), the quantitative improvements over prior work come from the improved estimation procedures (Theorems 7 and 11), not from dig-dec being smaller than optimistic DEC. Theorem 13 shows dig-dec is essentially equivalent to o-dec (up to +η) for these settings. The one strict separation (Theorem 14) is on a 3-armed bandit, not an MDP. The framing would benefit from greater precision about where the gains originate. That said, Dig-DEC's removal of optimism is genuinely essential for enabling the hybrid bandit results (Section 5.2), which is a distinct and important contribution.

- **Several regret rates in Table 2 are corrupted or questionable.** Lines 291, 293, and 295 show T^{3/2} (T^{1.5}, implausible for regret), and line 292 shows T^{13/8} (T^{1.625}) — these appear to be parser corruptions of intended rates. The one clean-looking rate — T^{1/2} for hybrid off-policy Bellman-complete (line 294) — is difficult to reconcile with the stated dig-dec bound (~ η^{1/2}) and constant Est from Theorem 11, since a back-of-envelope optimization would suggest T^{2/3} rather than T^{1/2}. Clarification is needed for all Table 2 entries.

- **The nature of the estimation improvement is not crisply articulated in the main body.** Line 213 states the new estimator improves the Est rate "from √T to T^{1/2}" — expressions that appear identical in the parsed text due to rendering. While the unbiased cross-validation construction (splitting the τ-sample epoch into two halves) is clearly described, the paper does not state in the main body what the prior work's Est rate was numerically and how the improvement propagates to the final regret after optimizing η.

### Trivial

- The introduction (line 33) contains corrupted fractions (T^{3/2}, T^{5/8}) that, while parser artifacts in this rendering, would benefit from correction in the original manuscript.

## Nice-to-Haves

- **Lower bounds.** As a paper studying a complexity measure (dig-dec), discussion of whether the achieved upper bounds are tight, or whether dig-dec characterizes a lower bound, would substantially strengthen the contribution.
- **Computational considerations.** The minimax problem in Eq. (3) is solved at each round. A brief discussion of computational feasibility (or an explicit statement that results are information-theoretic) would help set reader expectations.
- **Assumption restrictions for hybrid setting.** The paper transparently acknowledges (lines 115–117) that Assumption 3 excludes settings like low-rank MDPs with unknown features, and Assumption 4 requires known linear reward features. While this is properly scoped, extending beyond these restrictions remains an important open direction.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"POSTERIORITYUPDATE is left completely unspecified / Algorithms 2, 3, 4 are only referenced by number."** These are appendix material; the parser strips appendices. The original submission contains these details.
- **"Derivations that produce specific Est bounds are deferred entirely to appendices."** Same — appendix stripping artifact.
- **"Theorem 14's proof is in the stripped appendix, cannot be evaluated."** Same — appendix content exists in the original submission.
- **Introduction line 33 "garbled rates" T^{3/2}, T^{5/8}.** These are parser corruptions (T^{3/2} = T^{1.5} is nonsensical for regret). The original PDF does not have these issues. The abstract vs. Table 1 inconsistency (T^{3/5}, T^{7/8} vs. T^{2/3}) is retained as a Major weakness since both sets of fractions are clean and distinct — this is not a parser issue.
- **"The dig-dec improvement over optimistic DEC is not demonstrated in the canonical RL settings the paper studies."** Partially subsumed under the Minor weakness about framing, but the harsh critic's version overstates: the removal of optimism IS demonstrated to be essential for the hybrid bandit setting (Section 5.2), which is one of the paper's main contributions.
- **"Line 213 claims Est improves from √T to T^{1/2} — which are identical."** This is a parser artifact where two different LaTeX expressions rendered identically. The original PDF differentiates them. The underlying concern about unclear articulation of the improvement is retained as a Minor weakness.
- **"The hybrid off-policy rate T^{1/2} is surprisingly fast and deserves scrutiny."** Demoted from the harsh critic's speculative framing to a Minor weakness with a concrete mathematical concern (back-of-envelope optimization suggests T^{2/3} with stated bounds).
- **"The hybrid bandit result applies to a restricted class (Assumptions 3–4)."** The paper openly acknowledges this (lines 115–117). Demoted to Nice-to-Haves as a scope limitation the paper already addresses.

## Novel Insights

The decomposition of the KL term in Dig-DEC into regularization and information-gain components (line 305 of Section 6) provides genuine insight into the mechanism: regularization alone recovers optimistic DEC bounds (explaining Theorem 13), while the information-gain term enables strict improvements in distribution-aware settings (motivating Theorem 14). This decomposition cleanly separates *why* Dig-DEC works across stochastic and hybrid regimes — regularization removes the need for optimism (enabling hybrid bandit results), and information gain captures distributional structure that mean-based divergences miss (enabling strict improvements). This is a conceptually elegant unification that was not present in prior DEC literature.

## Suggestions

- Reconcile the abstract's claimed rates (T^{3/5}, T^{7/8}) with Table 1's rates (T^{2/3}) for the average estimation error case. If T^{2/3} is correct, update the abstract; if the abstract is correct, correct Table 1 and surface the derivation. This is essential for the paper's credibility.
- Verify and correct the corrupted regret rates in Table 2 (lines 291–295) and clarify whether T^{1/2} for hybrid off-policy Bellman-complete (line 294) is correct given the stated dig-dec ~ η^{1/2} and constant Est.
- Add a sentence or short paragraph in Section 4.2.1 explicitly stating prior work's Est rate and how the unbiased estimator improves it, so the reader can follow the improvement without consulting the appendix.
- In the introduction or discussion, clarify that for the standard RL settings in Tables 1–2, the regret improvements come primarily from better estimation, while Dig-DEC's distinct value is (a) enabling the hybrid bandit setting and (b) the potential for strict improvement in distribution-aware settings (Theorem 14).

---

## Calibration Summary

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Horizon-free Adversarial Linear Mixture MDPs | aPNwsJgnZJ | 6.00 | R1 | Closest comparator: first result for an open problem in adversarial RL, similar technical depth. Our paper has more breadth but presentation issues. Comparable. |
| Model-Free BPI in Online CMDPs | w8Zo7jACq7 | 5.20 | R1 | Our paper is stronger — more contributions, broader scope, resolves an explicitly stated open problem. |
| Minimax Optimal RL with Trajectory Feedback | en3NwykrHW | 5.50 | R2 | Our paper is stronger — more coherent contributions, broader applicability, resolves open problem. The 5.50 anchor has conflicting reviews and questions about dominant terms. |
| On Bits and Bandits | 0oWGVvC6oq | 6.50 | R2 | This anchor has cleaner conceptual contributions and includes experiments. Our paper has more concrete RL results across more settings but notable presentation issues. Slightly below. |
| MaxInfoRL | R4q3cY3kQf | 6.75 | R2 | More empirical paper, harder to compare. Our paper is pure theory with broader scope. |
| Robust RL with Adaptive Defense | DFTHW0MyiW | 7.00 | R2 | Stronger paper — cleaner presentation and robust contributions. Our paper is below this level. |

**Final placement**: The paper is comparable to the 6.00 anchor (horizon-free adversarial RL) — both resolve open problems with novel technical frameworks, both have some limitations in scope/assumptions. The paper is clearly above the 5.50 anchor (trajectory feedback RL) which had conflicting reviews and presentation issues. It falls below the 6.50 anchor which had cleaner execution. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>