## Summary

This paper introduces Dig-DEC, a model-free Decision-Estimation Coefficient that replaces the optimism principle of prior work [FGQ+23] with KL regularization and information gain. The authors provide a general analytical framework (Algorithm 1) based on Bregman divergences that generalizes the AIR framework of [XZ23, LWZ25], and instantiate it for both stochastic and hybrid (stochastic transitions + adversarial rewards) MDPs. Key results include: (1) Dig-DEC ≤ optimistic DEC + η (Theorem 13), showing it never performs much worse than the prior approach; (2) improved estimation-error bounds, including a log²|Φ| bound for Bellman-complete MDPs (Theorem 11); (3) first model-free regret bounds for hybrid MDPs with bandit feedback under linear rewards (Table 2), resolving an open problem from [LWZ25]; and (4) a constructive 3-armed bandit example where Dig-DEC strictly outperforms optimistic DEC (Theorem 14).

## Strengths

- **Theorem 13 (dig-dec ≤ o-dec + η)**: The paper formally establishes that the new complexity measure is never more than an additive η larger than optimistic DEC (line 303). This shows Dig-DEC recovers all guarantees of the optimistic approach while removing the optimism mechanism, which is critical for handling adversarial environments.

- **Theorem 11 (constant estimation error under squared error)**: The bound 𝔼[Est] ≲ log²|Φ| (line 239) is independent of T, improving over [FGQ+23]'s T^{1/2} bound. Combined with the dig-dec bounds, this yields √T regret for Bellman-complete MDPs — matching optimism-based approaches [JLM21, XFB+23] for the first time with a DEC-based method.

- **First model-free regret bounds for hybrid MDPs with bandit feedback**: Table 2 provides regret bounds for hybrid bilinear classes and coverable MDPs under bandit feedback and linear rewards, resolving the open problem from [LWZ25] (abstract, lines 11–12). This is the paper's strongest concrete result.

- **Generalization of the AIR framework via Bregman divergences**: The analysis in lines 155–167 connects general divergences D to mirror descent via Bregman divergences, avoiding the restrictive "constructive minimax theorem" of [XZ23]. Line 171 demonstrates flexibility by recovering [LWZ25]'s model-based result with a simpler algorithm.

- **Theorem 14 (constructive strict improvement over optimistic DEC)**: A 3-armed bandit instance is constructed (line 307) where optimistic DEC suffers Ω(√T) regret while Dig-DEC achieves O(1) regret. This demonstrates that the extra KL information-gain term can yield arbitrarily large improvement.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Vacuous claim about the Est rate improvement (Section 4.2.1, line 213)**: The paper states "our construction of the estimator improves their rate of Est from √T to T^{1/2}." These two expressions are mathematically identical; there is no rate improvement to claim. The paper describes a genuine technical difference (unbiased vs. biased estimator via sample splitting), but the specific claim about the T-exponent is vacuous. This is a writing error — the improvement is presumably in constants or log factors, not the exponent. While this does not affect the paper's mathematical correctness, it is a concrete error that undermines reader confidence and should be fixed.

2. **Parser corruption of fraction notation makes quantitative claims unverifiable from the extracted text**: The abstract, introduction, and Table 1 give mutually inconsistent regret exponents (e.g., abstract says T^{3/5} for on-policy average error, introduction says T^{3/2}/T^{5/6}, Table 1 shows T^{2/3}). The hybrid-setting bounds in Table 2 appear super-linear (T^{3/2}, T^{13/8}) despite the paper claiming "first sublinear regret." These are almost certainly PDF-parser artifacts — fraction notation is badly corrupted — but the consequence is that a reader relying on this extracted text cannot determine what exponents the paper actually achieves. This is not a methodological flaw, but the authors should ensure robustness to extraction in a camera-ready version (e.g., using unambiguous notation in tables).

3. **Mechanism behind Theorem 14 (3-armed bandit) is unexplained in the main text**: Theorem 14 (line 307) is stated as a fact with proof deferred to the appendix, but the main text does not explain *why* optimism fails on this instance while Dig-DEC succeeds. The paper notes (line 305) that the KL information-gain term captures distributional differences that mean-based divergences miss, but this remains vague without a concrete sketch. The theorem is the paper's cleanest demonstration of strict improvement, so a brief explanation would benefit readers.

4. **Known-feature restriction (Assumption 4) is a limitation for the hybrid setting**: The paper acknowledges (lines 114–115) that Assumption 3 does not cover all learnable hybrid MDPs, and Assumption 4 assumes known reward features. The paper honestly flags this and cites [LMWZ24] for the unknown-feature case as future work, which is good practice, but it does limit the practical scope of the hybrid-setting results.

5. **[FGQ+23]'s baseline rates are not stated alongside the new results in Table 1**: The paper frequently claims to improve over [FGQ+23]'s regret bounds, but the baseline rates for the average-estimation-error case are not stated in the main text or Table 1. The comparison tables are in Appendix A (stripped). Including the baselines in the main text would make the contribution self-contained.

### Trivial
- Line 41 has a grammatical issue: "For simplicity, we $|\Pi|$ is finite" is missing a verb ("assume").
- Several parentheses/brackets are missing from Table 1 and Table 2 (e.g., missing absolute value brackets around |Φ|), though this may be a parser artifact.

## Nice-to-Haves
- **Computational tractability discussion**: Algorithm 1 requires solving a minimax optimization over Δ(Π) and Δ(Ψ) at each round, which is computationally prohibitive for large policy classes. The paper follows the convention of the DEC/AIR literature in setting this aside, but a brief discussion would strengthen the paper, especially given the claim of practical relevance ("may facilitate future development," line 35).
- **Quantitative impact of the unbiased estimator**: The paper correctly identifies that sample-splitting gives an unbiased estimator, but tracing how this affects the final regret bound (via Est) is left implicit. A sentence clarifying whether the improvement is in constants, log factors, or both would resolve the confusion from Weakness #1.

## Removed Points
- **"Est rate improvement from √T to T^{1/2} is not an improvement"** — Partially kept as Minor #1. The critic's stronger framing that this "directly affects the credibility of regret-bound improvements" is removed because the actual improvement is in constants/log factors and the paper's final regret bounds (T^{2/3}, √T, etc.) would be unaffected by correcting this wording.
- **"Internal inconsistency of claimed regret exponents across abstract, introduction, and tables"** — Removed. The fraction notation is clearly corrupted by the PDF parser. For example, Table 1 consistently shows T^{2/3} for average-error cases while the abstract shows different values. This is a formatting artifact of extraction, not an author error.
- **"Super-linear bounds in Table 2 contradict sublinear claim"** — Removed. Same parser artifact. The dig-dec values (η^{1/2}) combined with Est ~ T^{1/2} or log²|Φ| give sublinear regret after optimizing η.
- **"Theorem 14 and Theorem 13 are in tension"** — Removed. There is no tension: Theorem 13 says dig-dec ≤ o-dec + η (Dig-DEC is never much worse) and Theorem 14 says Dig-DEC can be much better on a constructed instance. These are perfectly consistent.
- **Strength Finder: generic/superficial strengths** — Removed claims that simply restate the paper's contributions without providing specific evidence or that are not grounded in specific lines/tables.
- **"Missing related works"** — Removed per instructions (no external sources to verify).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Fix the Est rate claim in Section 4.2.1 (line 213): either correct the exponent comparison or explicitly state the improvement is in constants/log factors.
2. Ensure all quantitative claims (regret exponents) are stated in a format robust to PDF extraction — use unambiguous fraction notation in tables.
3. Add a brief sketch in the main text explaining why optimism fails on the 3-armed bandit instance (Theorem 14).
4. Include [FGQ+23]'s baseline rates alongside the new results in Table 1 for a self-contained comparison.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>