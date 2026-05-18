Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes EFMARL, which extends the epigraph form technique from single-agent safe RL to the multi-agent setting, targeting the multi-agent constrained optimal control problem (MACOCP) with zero constraint violation threshold. The method decomposes the problem into a centralized inner problem (training a z-conditioned policy via PPO) and a distributed outer problem (solving for the minimal cost-upper-bound z online via per-agent 1D root-finding). Experiments on MPE and Safe Multi-agent MuJoCo show that EFMARL with fixed hyperparameters achieves near-100% safety with low cost across environments, outperforming penalty and Lagrangian baselines that require per-environment tuning.

## Strengths

- **Consistent empirical performance with fixed hyperparameters.** Figure 3 demonstrates that EFMARL is closest to the top-left corner (low cost, near-100% safety) across all environments using one set of hyperparameters, while baselines require environment-specific tuning to avoid either unsafe behavior or excessive cost. This is the paper's strongest evidence.

- **Demonstrated training stability advantage.** Figure 5 shows EFMARL has smoother training curves than the Lagrangian variant InforMARL-L with increased λ learning rate, supporting the theoretical claim (Section 3.2) that the epigraph form avoids gradient scaling with λ. The connection between the gradient analysis and the empirical stability is clearly drawn.

- **Scalability to larger numbers of agents.** Figure 6 shows EFMARL maintains near-100% safety and low cost as the number of agents increases from 3 to 7 in Formation and Line environments, while baseline methods degrade. This supports the claim that the approach avoids the exponential joint-action-space problem.

- **Ablation studies provide practical utility.** Section 5.3 systematically investigates the effect of z_i communication (Table 1) and the safety margin ξ (Table 2). The finding that omitting z_i communication causes minimal performance loss is valuable for deployment, and the ξ analysis validates the design choice for compensating NN estimation errors.

## Weaknesses

### Fatal

None.

### Major

- **Theorem 1 is stated without sufficient logical justification in the main text and appears incomplete.** The theorem claims the outer problem of the epigraph form (finding minimal z such that min_π max{max_i V_i^h, V^l − z} ≤ 0) is equivalent to computing z = max_i z_i where each z_i solves a local problem that only enforces V_i^h(o_i; π(·,z')) ≤ 0. The gap is that the outer problem constraint requires **both** V_i^h ≤ 0 **and** V^l ≤ z, but the theorem's per-agent conditions only address the first. No argument is given in the main text for why V^l ≤ z would automatically follow from the per-agent safety conditions, nor is it obvious. Since this theorem is the stated foundation for the distributed execution claim (Contribution 2), the authors must either provide the full proof — which may have resided in the now-stripped appendix — or significantly revise the claim and clearly state any additional assumptions needed. If the theorem cannot be justified, the distributed execution component lacks theoretical grounding, though the empirical results would still stand as a practicable method.

### Minor

- **The inner MARL training procedure is underspecified for reproducibility.** The paper states that PPO is used with "advantage decomposition" and the total value function V = max{V_ψ^h(o_i,z), V_ϕ^l(x,z)−z}, but does not specify the exact per-step reward/cost signal used for GAE and return computation. While the approach follows So & Fan (2023) and MAPPO (Yu et al., 2022a), the multi-agent adaptation of the max-over-value-functions as a critic target is non-trivial and deserves a clearer description of how temporal-difference learning is applied to this composite objective. Adding one equation for the effective per-step "reward" in the z-augmented MDP would substantially improve clarity.

- **Mismatch between the homogeneity assumption and heterogeneous experimental settings.** The problem formulation (Section 3.1) assumes a homogeneous MAS where all agents share the same state/action spaces and dynamics. However, the Safe Multi-agent MuJoCo tasks (Coupled HalfCheetah 4x3) involve agents controlling different parts of a single robot with heterogeneous roles. The paper does not discuss whether the theory or algorithm extends to heterogeneous settings or what the consequences of this mismatch are. Given that the algorithm's GNN backbone and per-agent V_i^h/π_i naturally handle heterogeneity, a brief discussion would suffice.

### Trivial

None.

## Nice-to-Haves

- **Comparison with shielding-based safe MARL methods would broaden the empirical positioning.** The Related Work discusses shielding approaches and their limitations (domain expertise, scalability), but no shielding baseline appears in the experiments. While the paper's focus is on methods that solve the same MACOCP/CMDP formulation (penalty and Lagrangian methods), a single shielding comparison could strengthen the claims about practical applicability. This is a natural extension rather than a missing requirement.

- **Theoretical characterization of how NN estimation errors in V^h affect the outer problem solution.** The paper introduces ξ as a heuristic safety margin but does not analyze how approximation errors propagate through the root-finding procedure for z_i. An analysis or additional ablation (beyond the ξ sweep) would strengthen the theoretical framing.

## Removed Points

These points from the reviews were removed with justification:

- **"No proof of Theorem 1 in the main text"** — Removed per hard rules: the parser strips appendix content from all papers. The proof likely exists in the original submission's appendix. The retained Major weakness above concerns the substantive logical gap in the theorem as stated, not the absence of its proof.

- **Criticism that the reward function for inner PPO is completely unspecified** — Partially removed as overstatement. The paper does describe the approach (using max{V^h, V^l − z} as the total value, following MAPPO advantage decomposition). The retained Minor weakness captures the genuine clarity gap.

- **Strength claiming Theorem 1 as a core strength** — Removed because it conflicts with the verified Major weakness about the theorem's incompleteness. Per rules, when a strength and verified weakness disagree, the weakness wins.

- **"The paper should also cover additional tasks/domains"** — Removed as scope creep. The paper covers MPE and Safe Multi-agent MuJoCo with multiple configurations, which is a defensible range for a conference submission.

- **Pure formatting/style nitpicks** — Removed per hard rules about parser artifacts.

## Novel Insights

Beyond the paper's own contributions, the key insight from this review process is that the paper's practical contribution (a stable, zero-threshold-safe MARL algorithm with fixed hyperparameters) is stronger than its theoretical contribution. The empirical results are convincing and the algorithm design (epigraph form with z-conditioned policies) is well-motivated. However, the central theoretical claim about distributed decomposition (Theorem 1) rests on a logical step that is absent from the main text, creating a disconnect between the claimed theoretical guarantee and what is actually demonstrated. The paper would benefit from either a complete, verifiable proof or an honest weakening of the theoretical claim to an observed property rather than a proven equivalence.

## Suggestions

1. **Address the Theorem 1 gap explicitly.** Either reproduce the full proof from the appendix in a camera-ready version, or (if the proof has issues) weaken the claim to something defensible — e.g., "In practice, the distributed outer problem yields effective z values, and we provide intuition for why this works" — and clearly delineate what is proven versus observed.
2. **Specify the per-step learning signal for the inner PPO.** Add one equation defining the effective reward/cost in the z-augmented MDP (or clarify that the total value function V(x,z;π) is used as the critic target and how GAE is computed from it).
3. **Acknowledge the homogeneity assumption.** Add one sentence discussing whether and how the theory/algorithm extends to heterogeneous agents, or state that homogeneity simplifies the theoretical analysis but the algorithm itself applies without modification.
4. **Fix the theorem reference.** Theorem 1 references "the outer problem of EF-MACOCP (5a)" but equation (5a) is the general epigraph form; the actual MACOCP outer problem is (13a). Correct this cross-reference.

## Score and Decision

**Score:** 5.5

**Decision:** Weak Accept

*Rationale:* The paper addresses an important problem (zero-threshold safe MARL) and presents an algorithm with strong empirical support — consistent top-left-corner performance across environments with fixed hyperparameters is genuinely impressive. The core algorithmic idea (extending the epigraph form to CTDE) is well-motivated and the experiments are carefully designed. However, the paper's second claimed contribution — the theoretical distributed decomposition (Theorem 1) — has a significant logical gap as presented in the main text. Because this theorem is central to the distributed execution framing, this issue prevents the paper from being a strong accept. The empirical results are strong enough to warrant acceptance with the expectation that the theorem gap is addressed (either by providing the complete proof or by appropriately weakening the claim). The other issues (inner problem specification, homogeneity discussion) are minor and easily fixable.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>