Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces Dig-DEC (dual information gain decision-estimation coefficient), a new model-free complexity measure that replaces the optimism principle used in prior DEC-based methods with pure information-gain (KL regularization + a divergence term $\overline{D}$). This conceptual shift allows the framework to handle adversarial environments without explicit reward estimators. The paper establishes (i) improved regret rates over [FGQ⁺23] in stochastic settings via refined online estimation procedures, (ii) the first model-free regret bounds for hybrid MDPs with bandit feedback (resolving an open problem from [LWZ25]), and (iii) a clean general algorithmic framework (Algorithm 1 with Theorem 6) that unifies and simplifies prior AIR-based approaches.

## Strengths

1. **Conceptually novel complexity measure (Dig-DEC, Eq. (8)).** Dig-DEC removes the optimism term from [FGQ⁺23]'s optimistic DEC and replaces it with KL information gain. Theorem 13 shows Dig-DEC ≤ optimistic DEC + η, and Theorem 14 exhibits a 3-armed bandit where the improvement is arbitrarily large (constant vs. Ω(√T) regret). This is a genuine theoretical advance that makes the framework applicable to adversarial settings where explicit reward estimators are infeasible.

2. **First model-free regret bounds for hybrid MDPs with bandit feedback (Section 5.2, Table 2).** Under Assumptions 2–4 (linear reward with known features), the paper obtains sublinear regret for hybrid bilinear classes and coverable MDPs. This resolves the open problem left by [LWZ25], who could only handle full-information feedback. The achievement is clearly scoped and the assumptions are explicitly acknowledged.

3. **Improved online function estimation (Section 4.2, Theorems 7 and 11).** For average estimation error, the paper constructs an unbiased estimator via sample-splitting (two halves per epoch), achieving **Est** = O(N log|Φ| √T). For squared estimation error under Bellman completeness, a two-timescale posterior update yields **Est** = O(log²|Φ|). These refinements directly translate to improved regret rates (e.g., √T in Bellman-complete MDPs vs. the prior T^{5/6}).

4. **Clean, general framework unifying prior approaches (Section 4, Algorithm 1, Theorem 6).** The analysis diverges from [XZ23]'s constructive minimax theorem and connects naturally to mirror descent (Eqs. (5)–(6)), allowing flexible choice of the divergence $D$. The framework recovers earlier results (e.g., [LWZ25]'s model-based hybrid bounds) with simpler analysis, showing genuine analytic economy.

## Weaknesses

### Fatal
None.

### Major

1. **Exponent inconsistencies between the abstract, introduction, and tables.** The abstract (line 19) claims improvements from T^{3/4}→T^{3/5} (on-policy) and T^{5/6}→T^{7/8} (off-policy) for average estimation error. The introduction (line 39) states different numbers: T^{3/2}/T^{5/8}→T^{3/2}/T^{5/6}. Table 1 shows the paper's achieved regret for the stochastic no-completeness case as T^{2/3} for both on-policy and off-policy. While some of these discrepancies may stem from PDF parsing artifacts (particularly the T^{3/2} and T^{13/8} entries in Table 2, which produce super-linear exponents that cannot be correct for a regret bound), the abstract and introduction give genuinely different claimed improvements even when read as LaTeX. This makes it difficult for a reader to determine what exactly the paper achieves relative to baselines. The authors must reconcile these numbers in a revision and present them consistently.

### Minor

1. **The hybrid open-problem framing could be sharper.** The paper states it "resolves the main open problem left by [LWZ25]" — i.e., model-free learning in hybrid MDPs with bandit feedback. This requires Assumption 4 (linear reward with known features), which is the same assumption [LWZ25] used for their full-information results. The paper acknowledges this limitation (lines 121–124) and notes that more general settings (e.g., unknown reward features) remain open. The framing is accurate, but the main text could more explicitly state the precise relationship between the open problem and the assumptions required to resolve it, to avoid any reader confusion.

2. **The computational tractability of Algorithm 1 is not discussed.** The minimax optimization in Eq. (3) is a large convex-concave problem over Δ(Π)×Δ(Ψ). While this is standard for AIR-type algorithms, a brief remark on whether this optimization is tractable (or when it can be solved efficiently, e.g., for structured Φ) would strengthen the paper's practical relevance. This is not a flaw in the theory but a notable omission.

### Trivial
- The notation in Tables 1 and 2 is dense. A separate column showing only the T-exponent (suppressing H, d, log|Φ| factors) would help readers quickly grasp the main improvements.
- The "on-policy/off-policy" terminology for bilinear subclasses differs from standard RL usage; the paper warns about this (Section 5.1, line 261) but a brief reminder in the table captions would help.

## Nice-to-Haves
- A discussion of lower bounds for the hybrid setting with bandit feedback, to contextualize whether the achieved T^{3/5} or √T rates are optimal.
- A brief intuitive explanation of why the average-estimation-error case requires batching while the squared-error case does not (Section 4.2).

## Removed Points

- **Insufficient algorithmic details in main text (Harsh Critic Point 2):** The main text sketches the unbiased estimator and two-timescale update in a few sentences with references to the appendix. This is standard practice for theory papers at top venues (ICLR, NeurIPS). The paper provides the key ideas (lines 217–220 for the unbiased estimator, lines 249–250 for two-timescale) and defers full proofs to the appendix. This is not a weakness; it is the norm.

- **Assumption 4 being restrictive for the open problem (Harsh Critic Point 3):** The paper already acknowledges this limitation explicitly (lines 121–124). The criticism misunderstands the framing: LWZ25's own full-information result used the same assumption structure, so the paper's extension to bandit feedback within that framework legitimately resolves the stated open problem.

- **Missing lower bounds / optimality discussion for hybrid setting:** This is a nice-to-have, not a weakness. The paper's contribution is the first upper bounds for this setting, which is valuable regardless.

- **General formatting/presentation nitpicks:** These are standard for any paper and don't affect the technical evaluation.

- **Weaknesses from Strength Finder that were generic or contradictory:** Several strengths from the Strength Finder were generic ("addressed an important problem") — these are already reflected in the evaluation and don't need separate mention.

## Novel Insights

The most insightful observation across the reviews is that Dig-DEC's two-part information gain (KL regularization + divergence $\overline{D}$) plays distinct roles: KL regularization (specifically the marginal KL(ν_φ, ρ)) replaces the optimism mechanism, while the conditional KL information gain (over observations) provides additional tightening that yields strict improvements over optimistic DEC even in stochastic settings. This decomposition, explained in Section 6 (lines 311–312), explains both why optimism can be discarded and why strict improvement is possible, and is the conceptual heart of the paper that none of the reviews fully articulated independently.

## Suggestions

1. **Fix the exponent inconsistencies.** Unify the abstract, introduction, and all tables so that the claimed improvement and achieved regret exponents are consistent. If the T^{2/3} in Table 1 is correct, update the abstract accordingly; if T^{3/5} is correct, explain why the table shows a different exponent. Given that the hybrid Table 2 exponents appear corrupted by PDF extraction, these should be carefully verified.

2. **Add a simplified row to each table** showing the T-only exponent (e.g., "T^{2/3}") to complement the full bound.

3. **Add a brief remark on computational complexity** of the minimax optimization in Algorithm 1.

4. **Explicitly restate the relationship** between the LWZ25 open problem and Assumption 4 in Section 5.2.

## Score and Decision

**Calibration anchors (retrieved from the human-review corpus):**

| Anchor | Path | Avg Score | Comparison to this paper |
|--------|------|-----------|-------------------------|
| High | R1hIXdST22.md (General-purpose model-free RL) | 7.50 | Empirical RL paper; broader experiments but less theoretical depth. Current paper is stronger in theoretical novelty but has presentation issues the anchor paper does not. |
| High | jOm5p3q7c7.md (Optimal sample complexity for avg reward MDPs) | 6.50 | Theory paper resolving an open problem with matching bounds. Noted as limited novelty (synthesis of existing techniques). Current paper is more novel (new complexity measure) but has exponent inconsistencies. Comparable quality. |
| Medium | aPNwsJgnZJ.md (Horizon-free RL in adversarial linear mixture MDPs) | 6.00 | Theory paper with clean results and a clear contribution. Similar style and depth. Current paper introduces a more general framework (Dig-DEC) and covers more settings. |
| Medium | w8Zo7jACq7.md (Model-free BPI in CMDPs) | 5.20 | Mixed evaluation; some methodological concerns. Current paper is clearly stronger in both contribution and technical depth. |
| Low | 2h3m61LFWL.md (Value-biased MLE for linear MDPs) | 4.25 | Rejected due to overlooked assumption in regret bound and novelty concerns. Current paper avoids such issues and has stronger novelty. |
| Low | 4jzjexvjI7.md (Continuous-time bandit regret measure) | 2.33 | Very weak presentation, unclear contribution. Incomparable to the current paper. |

Relative to these anchors, the paper sits comfortably in the 6.0–6.5 band. Its conceptual contributions (Dig-DEC, first model-free hybrid bandit bounds) are stronger than the 6.00 anchor (aPNwsJgnZJ.md), but the exponent inconsistencies prevent it from reaching the 7.0+ level of the top anchors, which had no such presentation issues. I score it at the lower end of this band to reflect that the exponent inconsistencies need correction.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>