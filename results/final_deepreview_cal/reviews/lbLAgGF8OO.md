Now I have all the information I need. Let me produce the final review.

## Summary

The paper introduces Dig-DEC, an information-theoretic complexity measure for model-free decision making that removes the optimism principle from prior work and drives exploration purely through information gain. It presents a unified framework with general divergence measures, refines online function-estimation procedures, and applies the framework to both stochastic and hybrid MDPs. Key claimed contributions include: (1) first model-free regret bounds for hybrid MDPs with bandit feedback, (2) Dig-DEC ≤ optimistic-DEC + η (Theorem 13), with strict improvement in a constructed example (Theorem 14), and (3) improved regret rates for average and squared estimation error minimization.

## Strengths

- **Dig-DEC provides a cleaner, more general framework than prior DEC approaches.** The removal of optimism and the use of a general divergence D that subsumes both KL and D_av/D_sq terms yields a framework that "nicely connects to the standard analysis of mirror descent" (Section 4). The analysis recovers prior AIR results [LWZ25, XZ23] as special cases and even simplifies them (e.g., recovering model-based hybrid bounds without a two-level algorithm). Theorem 13 (dig-dec ≤ o-dec + η) formally shows the framework covers all settings handled by optimistic DEC.

- **Refined online estimation procedures with concrete technical novelty.** The paper introduces an unbiased cross-product estimator for average estimation error (Section 4.2.1) that improves over the biased estimator of [FGQ+23], and a two-timescale posterior update for squared estimation error (Section 4.2.2) that achieves constant-order Est, improving the T^{1/2} bound of prior work. These technical improvements are clearly motivated and could be of independent interest.

- **Addresses an open problem from [LWZ25].** The paper obtains the first model-free regret bounds for hybrid MDPs (stochastic transitions, adversarial rewards) with bandit feedback under linear reward and general transition structures. This directly addresses the open question stated in [LWZ25].

- **Theorem 14 exhibits a concrete separation** between Dig-DEC and optimistic DEC, showing the improvement can be arbitrarily large rather than merely asymptotic. While the proof is deferred to the appendix, the claim is clearly stated and motivated.

## Weaknesses

### Major

- **Inconsistency between claimed regret exponents in the abstract and Table 1.** The abstract (line 19) states that for average estimation error minimization, the paper improves from T^{3/4} to T^{3/5} (on-policy). However, Table 1 reports regret O(T^{2/3}) for on-policy bilinear and BE settings with D_av. The exponent 3/5≈0.6 differs from 2/3≈0.67. Similarly, the abstract's off-policy claim (T^{5/6}→T^{7/8}) does not match any entry in Table 1, which reports T^{2/3}. The introduction (line 39) contains further garbled exponents (T^{3/2} appears where T^{3/4} or T^{5/6} is clearly intended). The reader cannot determine which exponents are correct without reverse-engineering the derivations.

- **Table 2's hybrid regret exponents appear inconsistent with the stated dig-dec and Est bounds.** For the on-policy bilinear hybrid case with D_av, dig-dec = (H^5 d^3 η)^{1/2} and Est ≲ d log|Φ| T^{1/2}. A direct calculation from regret = T·dig-dec + Est/η with optimal η gives O(T^{5/6}), not O(T^{3/2}) as reported in Table 2. The same issue affects the off-policy D_av entry (reported as T^{13/8}) and the D_sq entries. Since the paper claims "the first sublinear regret for model-free learning in hybrid MDPs" but reports exponents T^{3/2} and T^{13/8} that are superlinear, this is a significant internal inconsistency that must be resolved. If the table entries are simply mis-typeset (e.g., the parser corrupted the superscripts), the authors must correct them and state the correct exponents explicitly.

- **The hybrid regret bounds' claimed "sublinear" nature is contradicted by Table 2 as printed.** The paper asserts "first sublinear regret for model-free learning in hybrid MDPs" (line 38), but Table 2 reports T^{3/2} and T^{13/8} — both superlinear (worse than the trivial O(T) a learner could achieve by picking a fixed policy and ignoring all observations). This contradiction between the textual claim and the table's numerical content is a critical problem that needs to be resolved in any revision.

### Minor

- **Theorem 14 (3-armed bandit with constant regret) cannot be evaluated** because the proof is deferred to Appendix J, which is stripped from the available text. The claim — constant regret where optimistic DEC suffers Ω(√T) — is strong and would benefit from a sketch or at least an explicit construction of the instance in the main text.

- **Computational tractability is not discussed.** Algorithm 1 requires solving a minimax problem over Δ(Π) and Δ(Ψ) each round. For large policy or function classes this is intractable, but the paper does not acknowledge this limitation or cite approximation schemes.

- **The hybrid setting has known limitations.** Assumption 3 does not capture cases such as hybrid low-rank MDPs with unknown reward features (as noted by the authors, citing [LMWZ24]), and Assumption 4 requires known linear reward features. These are honestly stated but should be discussed more prominently given that they restrict the scope of the "first model-free hybrid bounds" claim.

### Trivial

- The introduction's exponent "T^{3/2}" (line 39) is clearly a typo — it should be T^{3/4} or T^{5/6} depending on context.

## Nice-to-Haves

- Adding high-probability bounds for the hybrid setting would strengthen the contribution (the current high-probability variant is noted to not handle the hybrid setting).
- A brief discussion or reference regarding the computational feasibility of the minimax oracle in Algorithm 1 would help ground the contribution.

## Removed Points

- Harsh critic's point about the hybrid T^{3/2} bounds being "superlinear and therefore invalidating the sublinear claim" is preserved as a Major weakness because the table as printed indeed contradicts the claim. However, the critic's assertion that "the derivation in the body does not support these exponents" is correct based on the stated dig-dec and Est values, but the full derivation (in the appendix) may contain additional factors not visible in the main text. The criticism is kept at Major rather than Fatal because the inconsistency is between the textual claim and the table entries, and could potentially be resolved by the authors.
- Harsh critic's point about Theorem 14 being "too strong and unverifiable" is demoted to Minor because the proof is in the appendix (standard for theory papers) and the criticism is speculative ("would imply the instance is essentially trivial"). The claim does not violate any known lower bounds.
- Removed the criticism about "Assumption 3 limitations not discussed prominently enough" — the paper actually discusses this limitation explicitly in lines 121-125, so the criticism is factually incorrect.
- Removed the formatting/style nitpicks as per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reconcile all exponents.** Ensure that the abstract, introduction, and all tables report exactly the same regret exponents for each setting. If the abstract's T^{3/5} and Table 1's T^{2/3} refer to different sub-settings, clarify this explicitly. Fix the garbled T^{3/2} in the introduction.
2. **Correct Table 2 or verify the hybrid regret bounds.** Either the reported exponents (T^{3/2}, T^{13/8}) are wrong and should be replaced with the correct values (apparently T^{5/6} from a direct calculation), or the derivation in the paper should be updated to match the table. The term "sublinear" in the abstract and line 38 must be consistent with the actual bounds.
3. **Include a short sketch of the 3-armed bandit construction** for Theorem 14 in the main text or an accessible appendix subsection.
4. **Add a brief discussion** of the computational tractability of the minimax oracle in Algorithm 1, acknowledging that in many settings the optimization problem may be hard and citing approximation approaches where available.

## Score and Decision

**Round 1 bracket:** After inspecting the paper, I initially bracketed it between 4.5 and 6.5. The paper's theoretical framework is technically solid and addresses an open problem, which puts it above the VBMLE anchor (avg 4.25, rejected due to incremental contribution and strong assumptions). It has comparable ambition to the adversarial mixture MDP paper (avg 6.0, accepted) but has unresolved presentation issues that the latter lacked.

**Round 2 narrowing:** I compared against three anchors:
- *Adversarial Linear Mixture MDP* (avg 6.0, accepted): Clean paper with no major flaws. The current paper has stronger generality (unified framework covering multiple settings) but weaker presentation (exponent inconsistencies).
- *IIEFGs with Linear Approximation* (avg 5.75, rejected): Had strong assumptions and clarity issues. The current paper has more natural assumptions and a cleaner framework.
- *VBMLE for Linear MDPs* (avg 4.25, rejected): Had incremental contribution and hidden dependence on p_min. The current paper has stronger novelty (new complexity measure) and better-scoped assumptions.

The current paper sits between the rejected and accepted anchors — its technical contribution is solid and more general than the 6.0 anchor, but the exponent inconsistencies in the abstract, introduction, and Table 2 are significant presentation flaws that prevent acceptance as-is. A score of **5.0** reflects a paper with genuine technical merit that needs non-trivial corrections (especially to the hybrid table and exponent consistency) before it can be accepted.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>