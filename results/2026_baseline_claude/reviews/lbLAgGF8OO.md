Now I have read the full paper. Let me write the review.

---

## Summary

This paper introduces **Dig-DEC** (dual information-gain decision-estimation coefficient), a model-free complexity measure for Decision Making with Structured Observations (DMSO) that replaces the optimism principle in prior work [FGQ+23] with two information-gain terms rooted in KL divergences. The key structural insight is that this removal of optimism enables the framework to naturally handle adversarial environments (hybrid MDPs: stochastic transitions, adversarial rewards), yielding the **first model-free regret bounds for hybrid MDPs with bandit feedback** under linear reward and several general transition structures, resolving the main open problem of [LWZ25]. In addition, the paper improves online function-estimation procedures for both average and squared estimation error, with the squared-error case lifting the prior T^{5/6} bound to √T in Bellman-complete MDPs, matching optimism-based methods for the first time.

---

## Strengths

- **Resolution of an explicit open problem.** [LWZ25] left model-free learning in hybrid MDPs with bandit feedback as an open problem; it is cleanly resolved here. The conceptual reason is compelling: optimism requires an explicit reward estimator under bandit feedback, whereas Dig-DEC drives exploration solely through information gain and needs no such estimator.

- **Cleaner and more general analysis technique.** The prior AIR-based analysis in [XZ23, LWZ25] relied on a "constructive minimax theorem" tied to strictly convex divergences. The new analysis routes through standard Bregman divergence / mirror-descent arguments (Eqs. 5–6), making it more flexible, easier to extend, and yielding a simpler derivation that also recovers prior results as special cases (Appendix C is cited as doing this).

- **Strict improvement over optimistic DEC with concrete witness.** Theorem 13 establishes Dig-DEC ≤ o-DEC + η (so Dig-DEC is always no worse), and Theorem 14 gives a 3-armed bandit where the optimistic E2D of [FGQ+23] suffers Ω(√T) regret while the proposed algorithm achieves regret ≤ 1. This is a meaningful separation, not just an asymptotic claim.

- **Improved estimation procedures with independent interest.** The switch from a biased to an unbiased split-sample estimator for average estimation error (Appendix F.1), and the redesigned two-timescale procedure for squared estimation error (Appendix F.2), both improve the **Est** contribution to regret. The squared-error improvement (from T^{1/2} to O(log²|Φ|)) is particularly impactful, matching optimism-based approaches on Bellman-complete MDPs for the first time in a DEC-based method.

- **Unified and extensible framework.** The general Algorithm 1 with a parameterized divergence D subsumes [XZ23] and [LWZ25] as special cases, and the same algorithm and analysis cover both stochastic and hybrid MDPs with a uniform presentation (Tables 1 and 2).

---

## Weaknesses

### Fatal
None.

### Major

- **Limitation of Assumption 3 in the hybrid setting.** The paper openly acknowledges (Section 3.2) that Assumption 3 (unique reward-to-value mapping given φ) fails to capture all learnable hybrid MDPs. Specifically, for hybrid low-rank MDPs with *unknown* reward features, the partition size |Φ| scales polynomially in the number of possible feature mappings, while [LMWZ24] achieves logarithmic scaling. The authors explicitly call this a limitation and defer resolution. While the acknowledgment is transparent, this gap may be significant in practice since low-rank MDPs with unknown reward features are an important and natural class.

- **Sub-optimal exponents in hybrid setting.** Table 2 shows T^{3/2} regret for hybrid bilinear on-policy and T^{13/8} for hybrid bilinear off-policy (under average estimation). These exponents are far from √T and considerably worse than the stochastic setting (T^{2/3} in Table 1). Whether these exponents are tight or can be improved remains unclear; no matching lower bounds for the hybrid setting are provided.

### Minor

- **Computational tractability.** Like all DEC/E2D algorithms, Algorithm 1 requires solving a minimax optimization (Eq. 3) over distributions on Π and Ψ at every round. This is not computationally tractable in general. The paper does not discuss complexity or approximation, which is expected for a complexity-theoretic framework but limits practical relevance.

- **Strict improvement of Dig-DEC over o-DEC in the stochastic setting beyond the constructed example.** Theorem 14 demonstrates strict improvement in a contrived 3-armed bandit. The paper discusses this theoretically in Section 6 (the KL information gain term captures distributional differences that mean-based divergences miss), but no natural MDP class is exhibited where the strict improvement is quantified in the main text.

### Trivial
None worth listing.

---

## Nice-to-Haves

- A comparison table or discussion of lower bounds for the hybrid setting would help contextualize whether T^{3/2}/T^{13/8} in Table 2 are tight or improvable.
- A brief discussion of practical approximate implementations (even pointing to the literature on computational approximations for DEC-based methods) would increase accessibility for practitioners.

---

## Novel Insights

The conceptually deepest insight in the paper is the **decomposition of the KL term in Dig-DEC** (Section 6) into a *regularization* component KL(ν_φ, ρ) and an *information gain* component E[KL(ν_φ(·|π,o), ν_φ)]. The regularization component is sufficient to recover the optimistic DEC bounds in the stochastic setting without using optimism, and the information gain component provides the strict improvement over optimistic DEC. This decomposition clarifies why optimism is not necessary (regularization suffices for stochastic) and why removing optimism is crucial (enabling hybrid/adversarial settings without reward estimators). The subsequent identification that prior mean-based divergences (bilinear, squared Bellman) are blind to distributional information that the KL term captures is a genuinely illuminating theoretical observation.

---

## Suggestions

- Include explicit lower bounds for the hybrid setting, or at least a discussion of what lower bounds [LWZ25] or related works provide, to help readers assess the tightness of Table 2.
- Clarify the precise relationship between the estimation error improvement claims in the abstract (T^{3/4} → stated improvement on-policy) and the bound T^{2/3} appearing in Table 1 by specifying which prior work and setting each comparison corresponds to.
- Section 4.2.2 introduces a two-timescale procedure claiming to improve [FGQ+23]'s T^{1/2} bound on Est to O(log²|Φ|). A brief intuition for why the redesigned procedure achieves this — distinct from the split-sample idea in Section 4.2.1 — would strengthen the presentation.

---

## Score and Decision

This paper makes three technically solid contributions to RL theory: it introduces Dig-DEC with an elegant and rigorous motivation, resolves an explicit open problem (model-free bandit regret in hybrid MDPs), and provides provably improved estimation procedures. The analysis is technically non-trivial, the generalization to a unified framework is valuable, and Theorem 14 provides a concrete separation. The limitations (Assumption 3, sub-optimal exponents in the hybrid setting, computational tractability) are acknowledged and are typical for this line of work. The paper advances the DEC/AIR line of research in a meaningful and well-executed way.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>