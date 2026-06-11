## Summary
This paper introduces Dig-DEC, a model-free decision-estimation coefficient that replaces optimism with KL regularization and an information-gain term, paired with improved online estimation procedures. The framework handles both stochastic and hybrid (stochastic-transition, adversarial-reward) MDPs, yielding the first model-free regret bounds for hybrid bilinear classes and Bellman-complete coverable MDPs under bandit feedback. It also improves on prior DEC-based bounds in several stochastic settings (e.g., from T^{5/6} to √T for Bellman-complete MDPs).

## Strengths
1. **First model-free bounds for hybrid MDPs with bandit feedback under DEC**: By replacing the optimism principle with KL regularization, Dig-DEC avoids explicit reward estimators, enabling the first model-free regret bounds for hybrid bilinear classes and Bellman-complete coverable MDPs under bandit feedback (Table 2). This resolves the open problem left by [LWZ25].

2. **√T regret for Bellman-complete MDPs with a DEC-based method**: The paper redesigns the two-timescale posterior update so that Est is bounded by log²|Φ| (Theorem 11), a constant independent of T. Combined with the Dig-DEC bounds (Table 1), this yields √T regret — matching optimism-based approaches and improving over [FGQ⁺23]'s T^{5/6}.

3. **Explicit strict separation from optimistic DEC**: Theorem 14 provides a 3-armed bandit instance where optimistic DEC suffers Ω(√T) regret while Dig-DEC achieves ≤ 1, demonstrating that the KL information-gain term captures distributional differences that mean-based divergences miss.

4. **More flexible analysis framework**: The regret analysis (Eqs. (5)–(6), Theorem 6) works with a general divergence D and connects to standard mirror descent analysis, avoiding the restrictive "constructive minimax theorem" of prior work (lines 152-155). This recovers prior model-based hybrid-MDP results without needing a complex two-level algorithm.

5. **Unbiased estimator for sharper concentration**: The split-sample technique (lines 213-214) constructs an unbiased estimator of the squared mean, improving concentration compared to [FGQ⁺23]'s biased plug-in estimator.

## Weaknesses

### Fatal
None.

### Major
1. **Inconsistent claimed improvement rates across abstract, introduction, and Table 1**: The abstract (line 13) claims improvements from T^{3/4}→T^{3/5} (on-policy) and T^{5/6}→T^{7/8} (off-policy) for average estimation error. The introduction (line 33) claims T^{3/2}/T^{5/8}→T^{3/2}/T^{5/6}. Table 1 shows T^{2/3} for the average-error settings. These three sets of numbers are mutually inconsistent, and several claimed "improvements" (T^{5/6}→T^{7/8}, T^{5/8}→T^{5/6}) are mathematically worsenings. Moreover, line 213 states that the estimator improves "from √T to T^{1/2}" — the same rate. While some of these discrepancies are likely PDF-parsing artifacts (fraction inversion in LaTeX), the paper's headline improvement rates cannot be reliably identified as written. This is a presentation issue that must be resolved before publication, as it directly impacts the paper's core claims.

### Minor
1. **Table 2 contains suspiciously superlinear T-exponents**: The on-policy hybrid bilinear bound under \overline{D}_{av} is reported as d(H^5 log|Φ|)^{1/2} T^{3/2}, which is superlinear (> T) and vacuous. Given the pervasive fraction-parsing issues in the extracted text, this is most likely a parser artifact (intended T^{2/3} rendered as T^{3/2}). However, the T-exponents in Table 2 should be verified and corrected before publication, as they currently appear implausible.

### Trivial
None.

## Nice-to-Haves
- Provide an intuitive explanation of why the unbiased split-sample estimator achieves better concentration than [FGQ⁺23]'s biased estimator, beyond the current algebraic description.
- Briefly sketch the 3-armed bandit construction of Theorem 14 in the main text to make the separation more accessible without requiring appendix access.
- Add a brief remark on whether the minimax optimization in Eq. (3) is computationally tractable for the settings considered.

## Removed Points
These points were flagged during review but removed during consolidation with brief justification:

1. **Theorem 14 proof deferred to appendix** (from Harsh Critic): The critic notes the proof is in Appendix J, which is standard practice for theory papers. The appendix exists in the original submission; the parser stripped it. Not a weakness.

2. **On-policy vs off-policy comparison in Table 2** (from Harsh Critic): The critic claims on-policy should not be harder than off-policy. However, "on-policy" and "off-policy" are non-standard technical subclasses (as noted at line 255), and the on-policy entries lack Bellman-completeness while some off-policy entries have it. The comparison is apples-to-oranges.

3. **All formatting/style nitpicks and parser artifact complaints**: Removed per hard rules about parser-induced artifacts.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Fix the inconsistency in the claimed regret improvement rates across the abstract, introduction, and Table 1. Identify which numbers are correct and ensure they match consistently. Pay special attention to the average-estimation-error improvements.
2. Verify and correct all T-exponents in Table 2, particularly the T^{3/2} entries that are likely parser artifacts.
3. Fix the self-contradictory statement on line 213 ("improves from √T to T^{1/2}").
4. Consider adding an intuitive explanation of the unbiased estimator's advantage over the biased one, and a sketch of the 3-armed bandit construction in the main text.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
- *Low band* (< 3.5): L143pPpIHv (avg 3.00), Zi1QNJKXAD (avg 3.20), lFzUHGebeb (avg 2.00), 5s1qpjrNvZ (avg 3.00) — all clearly weaker (rejected for being incremental, poorly motivated, or technically weak).
- *Middle band* (3.5–7.5): w8Zo7jACq7 (avg 5.20, Reject), 2h3m61LFWL (avg 4.25, Reject), 8eNLKk5by4 (avg 6.00, Accept), en3NwykrHW (avg 5.50, Reject).
- *High band* (> 7.5): A3YUPeJTNR (avg 8.00, Accept), stUKwWBuBm (avg 8.00, Accept), 5t57omGVMw (avg 8.00, Accept), WJaUkwci9o (avg 8.00, Accept) — substantially stronger papers (broader impact, cleaner presentation, no significant weaknesses).

**Initial bracket:** [5.0, 7.5]

**Round 2 — Narrowing:**
- S24zdyiWDT (avg 6.00, Reject) — IRL sample complexity. Has more fundamental conceptual issues (metric concerns, δ-dependence missing). The current paper is stronger.
- OmFlDvsvc3 (avg 6.00, Reject) — Error-regret mismatch in reward learning. Solid theory but narrow scope. Comparable quality.
- nIEjY4a2Lf (avg 6.00, Accept) — Misspecified sparse Q-learning. Clean matching bounds but computational intractability and niche setting. Comparable quality; current paper has broader contribution but notable presentation issue.
- lF2aip4Scn (avg 6.50, Accept) — Demonstration-regularized RL. Clean theory with practical relevance. Slightly stronger presentation.

**Final score:** 6.0

The paper makes a solid theoretical contribution (new complexity measure, first model-free hybrid bounds, improved estimation procedures) that is clearly stronger than papers scoring 4-5. However, the inconsistent improvement rates across the abstract, introduction, and Table 1 are a notable presentation issue that keeps it from reaching the 6.5-7 level. Fixing these numbers would significantly strengthen the paper.

### Decision
**Accept with minor revision** — the core technical content is sound and the contribution is significant, but the presentation of headline numbers must be corrected before publication.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>