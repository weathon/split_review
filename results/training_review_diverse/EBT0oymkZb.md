Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper studies zero-shot generalization (ZSG) in offline reinforcement learning. It proposes two meta-algorithm frameworks — Pessimistic Empirical Risk Minimization (PERM, model-based) and Pessimistic Proximal Policy Optimization (PPPO, model-free) — that leverage per-environment pessimistic policy evaluation to enable generalization to unseen environments. Theoretically, the suboptimality gap is decomposed into a supervised learning error (controlled by the number of training environments) and an RL error (controlled by dataset coverage). Empirically, an approximation of PERM using multiple IQL value networks (IQL-nV) shows improved performance on Procgen over single-network IQL.

## Strengths

- **First provable theoretical framework for zero-shot generalization in offline RL.** The paper cleanly decomposes the ZSG suboptimality gap into an interpretable SL error term (depending on the number of training environments) and an RL error term (depending on dataset coverage via an uncertainty quantifier). This provides a conceptual scaffolding that was missing in prior purely empirical work (Mediratta et al., 2023). The paper explicitly states this claim (Section 1, line 26) and distinguishes its setting from multitask RL that requires downstream interaction.

- **Provides two complementary approaches with distinct trade-offs.** PERM (model-based, maintains n models/critics) and PPPO (model-free, maintains n policies) each offer different practicality guarantees: PPPO's SL error depends only on action-space size |𝒜| rather than a policy-class covering number, making it more scalable when maintaining many models is infeasible.

- **Formally identifies why vanilla offline RL without context information fails.** Proposition 4 proves that a merged multi-environment dataset is indistinguishable from an average-MDP dataset, and the Figure 1 counterexample concretely shows the gap. This formalizes a previously empirical observation (Mediratta et al., 2023) and motivates why context-aware algorithmic modifications are necessary.

- **Empirical validation demonstrates practical potential.** On Procgen, IQL-4V outperforms single-network IQL on both the 1M Expert and 1M Mixed datasets (Table 2), and the ablation on Miner shows monotonic improvement with more value networks (Table 3).

## Weaknesses

### Fatal
None.

### Major

- **The PPPO guarantee holds with only 2/3 probability (Theorem 14), which is too weak for a "provable" claim.** The authors fix δ = 1/8, yielding a bound that fails with probability 1/3. In theoretical RL, high-probability bounds (typically 1−δ with δ ≪ 1) are standard precisely because they control tail events in value estimation. A 2/3 guarantee per run is not reliable by conventional standards. Since the bound structure likely scales as O(log(1/δ)), this is fixable, but in its current form it undermines the strength of the claimed provable guarantee.

- **The empirical evaluation has a confound between stochastic policies and multiple value networks.** In the ablation (Table 3, Miner game), IQL-1V with a stochastic policy (SP: 5.6 ± 1.89) already far outperforms the deterministic default IQL (1V-DP: 1.66 ± 0.17). The additional improvement from 1V-SP to 4V-SP (6.36 ± 1.85) and 8V-SP (7.88 ± 0.71) is modest and partially within one standard deviation of the 1V-SP result. The paper lacks a controlled comparison — e.g., IQL-4V-DP (deterministic policy, 4 value networks) — to isolate whether the primary driver of improvement is the stochastic policy or the multiple value networks. This makes it difficult to attribute the gains to the paper's core theoretical idea (multiple per-environment evaluations) versus a simpler architecture change. Since the theory is about multiple evaluations and says nothing about stochastic vs. deterministic policy, this confound weakens the empirical support for the theory.

### Minor

- **Limited baseline comparisons.** The experiments compare only against BC and IQL from Mediratta et al. (2023). The paper itself mentions CQL (Kumar et al., 2020) in its discussion (line 93) as a method that may generalize worse than BC, yet does not include it or other offline RL baselines as empirical comparators. While the paper's main contribution is theoretical, stronger baselines would better calibrate the practical improvement.

- **Sensitivity to the number of environment groupings is not analyzed.** The implementation groups 200 training environments into m=4 groups for practical reasons, but Remark 12 offers no guidance on how performance scales with m, and no sensitivity analysis is provided. The theoretical bound depends on n (the number of environments), so the gap between n=200 and m=4 could be significant and is not discussed.

- **The impossibility result (Proposition 4), while valid, is not a substantial theoretical contribution on its own.** It formalizes an intuitive observation (merged data without context looks like an average MDP). The paper's novelty lies in the positive results (PERM/PPPO), and framing the negative observation as a key contribution overstates its depth. This does not harm the paper's main claims but inflates the contribution list.

- **The paper's claim of being the "first" could be better contextualized.** The paper distinguishes its zero-shot setting from the few-shot approaches of Bose et al. (2024) and Ishfaq et al. (2024), but does not provide a technical comparison of its bounds to existing multitask RL bounds to clarify why the zero-shot setting requires a different analysis. A more thorough comparison would strengthen the positioning.

### Trivial
None.

## Nice-to-Haves

- A high-probability version of Theorem 14 (parameterized by a tunable δ rather than fixing δ=1/8).
- Controlled ablation comparing IQL-nV-DP (deterministic) vs IQL-nV-SP (stochastic) on 3–5 games instead of just Miner to isolate the confound.
- Sensitivity analysis on the number of environment groupings (m).
- Baseline comparisons to CQL or ATAC from Mediratta et al. (2023).

## Removed Points

- **Criticism 1 (meta-theorems / no concrete instantiation in main text):** Removed per hard rule on missing appendix. The paper explicitly references a linear MDP instantiation with Algorithm 5 and theoretical guarantees (Section 5.3, line 205) and states "its specific realization in Section D" (Remark 6, line 118). The appendix is stripped by the parser but exists in the original submission. The critic's demand for main-text bounds outside the paper's scope is invalid given that deferred appendix content is standard in theoretical ML papers.

- **Figure 1 notation / garbled symbols criticism:** Removed (parser artifact). The figure is a LaTeX diagram that renders correctly in the original PDF; the extraction garbled it.

- **Table 1 being an image criticism:** Removed (parser artifact). The table is an image in the original PDF, included normally. Extracting as an image reference is standard parser behavior.

- **"Heavy and occasionally inconsistent notation":** Removed (subjective style nitpick, not a verifiable weakness).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Parameterize Theorem 14 by a confidence parameter δ** and present the bound as O(√(log(|𝒜|H²/δ)/n) + RL error), which is the standard form. This would immediately address the 2/3 probability concern.
2. **Add an ablation that controls for the stochastic policy confound:** compare IQL-4V-DP vs IQL-4V-SP (and ideally IQL-1V-DP vs IQL-1V-SP vs IQL-4V-DP vs IQL-4V-SP) on at least 3 games. This would cleanly separate the effect of multiple value networks from the effect of stochasticity.
3. **Include at least one additional baseline** (e.g., CQL or ATAC from Mediratta et al. 2023) to better calibrate the practical improvement of IQL-nV.
4. **Add a short discussion** relating the paper's bounds to those in Bose et al. (2024) and Ishfaq et al. (2024) to clarify why the zero-shot setting requires different analysis and how the results compare.

## Score and Decision

The paper addresses a timely and important problem — zero-shot generalization in offline RL — and makes a genuine theoretical contribution by providing the first provable framework with a clean error decomposition. The main theorems (Theorems 9 and 14) establish a meaningful structural insight. However, the 2/3 probability in Theorem 14 is unusually weak for a "provable" guarantee, and the empirical evaluation contains a confound (stochastic vs. deterministic policy) that prevents clean attribution of improvement to the core idea. These issues are addressable but nontrivial. The paper is a solid submission with a real theoretical contribution that, with revision, could be strong.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>