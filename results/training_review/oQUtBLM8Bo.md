Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper extends the epigraph form technique from single-agent safe RL to multi-agent settings (EFMARL), targeting the zero-constraint-violation problem (MACOCP). The key idea is to decompose the constrained problem into a centralized inner problem (solved during training via PPO with per-agent value decomposition) and a distributed outer problem (solved during execution via per-agent 1D root-finding on local constraint-value functions). Empirically, EFMARL achieves strong cost-safety Pareto fronts across MPE and Safe MuJoCo environments with a single set of hyperparameters, outperforming penalty and Lagrangian baselines that require per-environment tuning.

## Strengths

- **Novel and well-motivated extension of the epigraph form to MARL.** The paper correctly identifies that Lagrangian-based safe MARL methods struggle under zero-constraint-violation settings (Section 3.2, lines 73–85, supported by Figure 5 showing smoother training curves for EFMARL) and introduces a principled alternative that avoids gradient scaling with the multiplier.

- **Consistent superior empirical performance with fixed hyperparameters.** Across all six environments (MPE with N=3,5,7; Safe MuJoCo HalfCheetah 2x3, 4x3; Coupled HalfCheetah 4x3), EFMARL with a single hyperparameter configuration achieves near-100% safety rate and low cumulative cost, placing it closest to the top-left corner in Figure 3. No baseline achieves comparable trade-offs across all environments without per-environment tuning.

- **Training stability over Lagrangian methods.** Figure 5 directly demonstrates that EFMARL has significantly smoother cost and safety curves during training compared to InforMARL-L with increased learning rate. This empirically validates the paper's theoretical argument that the epigraph form avoids the unbounded multiplier growth problem.

- **Distributed execution capability.** Theorem 1 provides a framework for decomposing the outer problem into per-agent 1D root-finding, enabling distributed execution without requiring the centralized cost-value function V^l during deployment. The ablation in Table 1 shows that even without z_i communication, performance is maintained.

- **Scalability evidence and robustness tuning.** Figure 6 shows that EFMARL maintains top-left-corner performance as agents increase from 3 to 7. Table 2 demonstrates systematic safety improvements via the ξ margin parameter, giving practitioners a principled knob for safety–performance trade-offs without retraining.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 1's equivalence claim is not convincingly justified in the main text.** The theorem states that the outer problem (5a) is equivalent to solving per-agent problems z_i = arg min z' s.t. V_i^h(o_i; π(·,z')) ≤ 0 and taking z = max_i z_i. However, the original outer problem requires both V_i^h ≤ 0 and V^l ≤ z. While the policy π(·,z') used in the theorem is trained via the inner problem (which minimizes max{V_i^h, V^l − z'}) and thus implicitly considers V^l, the theorem's RHS criterion only explicitly enforces V_i^h ≤ 0. The equivalence claim requires additional reasoning about how the inner problem's training ensures that V^l ≤ z is automatically satisfied when all V_i^h ≤ 0 at the computed z. The paper does not provide this reasoning in the main text, and the proof was deferred to an appendix that was stripped during parsing. This gap weakens the paper's central theoretical claim of a "principled" CTDE decomposition. That said, the algorithm's empirical performance does not depend on this theorem being correct — it works as a heuristic regardless.

- **The inner problem training procedure uses a heuristic connection to the stated global objective.** The inner problem (13b) minimizes V = max_i V_i where V_i = max{V_i^h, V^l − z}. However, the training procedure (Section 4.2, line 148) computes each agent's PPO advantage using the *per-agent* value function V_i = max{V_i^h, V^l − z} rather than the global max over agents. The paper states it "follow[s] MAPPO to train the NNs with advantage decomposition (Gu et al., 2023)" but does not explain how optimizing per-agent objectives reduces the global max_i V_i. This is a standard MARL heuristic — each agent minimizing its own V_i minimizes an upper bound on the max — but the paper should explicitly acknowledge that this is an approximation rather than a principled optimization of the stated objective.

### Minor

- **The safety metric does not fully characterize worst-case violation behavior.** The paper reports safety rate (fraction of agents safe over the entire trajectory, averaged over episodes) and shows near-100% values. This is reasonable evidence but does not capture tail behavior (e.g., 95th percentile violations, maximum per-trajectory violation count). For the zero-constraint-violation setting the paper targets, worst-case or per-trajectory violation statistics would strengthen the empirical claims.

- **The ablation showing z_i communication is unnecessary partially undermines Theorem 1.** Table 1 shows that not communicating z_i has negligible performance impact, which the paper acknowledges in the limitations (line 287): "the theoretical optimality guarantee may not be valid." This is honest but leaves a tension: if the theorem's claimed equivalence is the theoretical foundation for distributed execution, but the algorithm works without following the theorem's prescription, the theoretical contribution is weakened.

- **Baseline hyperparameter sweep is limited.** The paper tests InforMARL penalty parameters β ∈ {0.02, 0.1, 0.5} and Lagrangian initial multipliers λ₀ ∈ {1, 5}. A broader sweep could alter the Pareto comparisons, though the paper's claim rests on EFMARL working *without tuning* while baselines need it — so the asymmetry in tuning effort is intentional.

### Trivial

- **Scalability experiments only go up to 7 agents.** While the trend is positive, the paper's framing discusses MAS with "tens or hundreds" of agents but does not test in that regime.

## Nice-to-Haves

- Reporting per-trajectory worst-case violation statistics (90th percentile, max violation count) would strengthen the safety claims.
- A study of sensitivity to the ξ and ν hyperparameters beyond Table 2 would improve reproducibility guidance.
- Visualizing how z_i and the global z evolve over a trajectory could provide intuition for how the outer problem works in practice.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that baselines are "designed for average constraints, not (6)"**: REMOVED. This misunderstands the paper's contribution. The paper's central claim is that existing Lagrangian methods (designed for CMDP-style average constraints) fail under hard-constraint settings (zero threshold). Testing them in this setting and showing they perform poorly is the intended comparison.
  
- **Criticism about missing appendix / proofs**: REMOVED per instruction — the parser strips these sections from all papers.
  
- **Criticism that "Theorem 1 completely discards the cost upper bound V^l ≤ z"**: REMOVED as oversimplified. The theorem uses π(·,z'), which is trained to minimize max{V_i^h, V^l − z'} through the inner problem. V^l is therefore baked into the policy. The theorem's claim may still be under-justified, but the specific accusation that V^l is "completely discarded" is inaccurate.
  
- **Criticism about Lagrangian baselines not being tested with zero threshold specifically**: REMOVED. The paper does test Lagrangian baselines in the zero-threshold setting and shows they fail (Figures 3, 5). The theoretical analysis in Section 3.2 explains why.

- **Pure presentation/formatting complaints**: REMOVED per instruction — these are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The key insight — extending the epigraph form to multi-agent settings via CTDE decomposition — is the paper's own, and the reviews do not surface an unrecognized observation beyond what the authors already articulate.

## Suggestions

- **Revise Theorem 1's claim from "equivalent" to "sufficient condition" or "heuristic."** The current phrasing overclaims. The RHS provides a way to compute z using only V_i^h, and the paper could present this as a practical approximation that works well empirically (which the experiments already demonstrate), rather than claiming formal equivalence without a complete proof. This would make the paper's framing match its evidence.

- **Explicitly acknowledge the heuristic nature of the per-agent value decomposition.** The paper should note that optimizing per-agent V_i values is an approximation to minimizing the global max_i V_i, justified empirically by the results, rather than presenting this as a direct optimization of the inner problem objective.

- **Add worst-case violation statistics** (e.g., 90th percentile violations, max per-trajectory count) to the evaluation to better support the zero-constraint-violation framing.

- **Discuss the tension between Theorem 1 and the z_i non-communication result more prominently.** The limitations section already acknowledges this, but bringing it into the main discussion (Section 4.3) would strengthen intellectual honesty.

## Score and Decision

This paper addresses a genuinely important problem (zero-constraint-violation in multi-agent RL) with a novel algorithmic approach. The empirical results are strong and consistent — EFMARL clearly outperforms baselines across environments with less tuning. The main weakness is that the theoretical framing (Theorem 1, principled CTDE decomposition) overclaims relative to what is established, and the training procedure uses a heuristic connection to the global objective without acknowledging it. These are substantive but not fatal: the empirical contribution stands independently of the theorem's correctness, and the algorithmic ideas are well-motivated. The paper would benefit from scaling back its theoretical claims to match what is actually shown, but the core contribution — a practical, empirically successful safe MARL algorithm for the hard-constraint setting — is solid.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>