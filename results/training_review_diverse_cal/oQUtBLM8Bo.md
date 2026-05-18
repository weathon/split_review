Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes EFMARL, which extends the epigraph form technique from single-agent safe RL to multi-agent MARL, addressing the training instability of Lagrangian methods under zero-constraint-violation settings. The key idea is to decompose the constrained optimization into (1) a centralized inner problem that trains \(z\)-conditioned policies and value functions, and (2) a distributed outer problem solved via per-agent 1D root-finding during execution (Theorem 1). Empirical results on Multi-Particle Environments and Safe Multi-agent MuJoCo show that EFMARL, with fixed hyperparameters across all environments, achieves both near-100% safety and low cumulative cost, outperforming penalty-based and Lagrangian baselines that require per-environment tuning.

## Strengths

1. **Principled extension of the epigraph form to MARL with CTDE.** The paper provides a clean derivation from the MACOCP (Eq. 2) to the epigraph form (Eq. 11), identifying that the outer problem constraint involves \(\max\{V_i^h, V^l - z\}\) and decomposing this into per-agent total value functions \(V_i\). Theorem 1 then claims that the outer problem reduces to per-agent root-finding on \(V_i^h\) only, enabling distributed execution — a nontrivial extension of the single-agent result from So & Fan (2023) to the multi-agent setting.

2. **Strong and robust empirical performance across diverse environments.** In Figure 3, EFMARL consistently achieves the closest point to the top-left corner (low cost, near-100% safety) across all four environments (MPE Target, Spread, Formation; Safe MuJoCo HalfCheetah 2×3, 4×3) using a **single fixed set of hyperparameters**. Every baseline requires environment-specific tuning (different \(\beta\) or \(\lambda_0\)) and fails to match both objectives simultaneously. This directly supports the claim of hyperparameter robustness.

3. **Stable training dynamics.** Section 3.2 provides a clear theoretical explanation for why the epigraph form avoids the gradient-scaling problem of Lagrangian methods (the gradient \(\frac{\partial}{\partial\pi}J_z\) does not scale with \(z\), unlike the Lagrangian gradient which scales linearly with \(\lambda\)). Figure 5 empirically validates this, showing smoother training curves for EFMARL compared to MAPPO-Lagrangian with increased learning rate.

4. **Scalability to larger numbers of agents.** Figure 6 demonstrates that with \(N=5\) and \(N=7\) agents, EFMARL maintains its top-left-corner performance while baseline methods degrade — either violating safety or increasing cost.

5. **Useful ablation studies.** Table 1 examines the effect of disabling \(z_i\) communication (finding minimal degradation), and Table 2 studies the \(\xi\) robustness parameter (confirming the trade-off and recommending \(\xi \approx \nu\)). These provide practical guidance and are transparent about when the theoretical guarantee may not hold.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1 is stated without sufficient justification in the main text; the handling of the cost constraint \(V^l\) is unclear.**  
   The original outer constraint (13b) requires \(\min_\pi \max_i \max\{V_i^h, V^l - z\} \leq 0\), meaning *both* safety (\(V_i^h \leq 0\) for all \(i\)) *and* the cost bound (\(V^l \leq z\)) must hold simultaneously. Theorem 1 converts this to finding \(z = \max_i z_i\) where each \(z_i\) is defined purely via \(V_i^h(o_i; \pi(\cdot,z')) \leq 0\) — the \(V^l\) term does not explicitly appear. The paper does not explain in the main text how the cost constraint \(V^l \leq z\) is automatically satisfied under this construction, or under what assumptions the equivalence holds (e.g., exact optimality of the inner problem). While a proof may exist in the stripped appendix, the main text should at least sketch the reasoning. Without this, a core theoretical contribution of the paper — that the outer problem decomposes into independent per-agent subproblems — is presented as a claim rather than a justified result.

2. **The safety metric may overstate the true safety of the policies.**  
   The safety rate is defined as "the ratio of agents that remain safe over the entire trajectory … over all agents." Because this averages over agents, an episode where *some* agents violate constraints can still register a high safety rate. The MACOCP constraint (2b) is global — the state is unsafe if *any* agent violates. An episode-level metric (fraction of trajectories with zero constraint violation across all agents) would be stricter. Near-100% per-agent safety likely implies high episode-level safety, but the gap is not quantified. Given the paper's motivation of zero constraint violation, supplementing with episode-level rates would strengthen the claims.

### Minor

1. **The \(z\)-conditioned policy's generalization across the \(z\) range encountered at test time is not analyzed.**  
   During training, \(z^0\) is sampled randomly; during execution, the outer problem finds a specific \(z\) via root-finding on \(V_\psi^h\). The paper provides no evidence (e.g., sensitivity analysis, failure cases) that the learned \(\pi_\theta(o_i, z)\) generalizes reliably to the \(z\) values found at test time, or that the root-finding procedure is robust to estimation errors in \(V_\psi^h\). An analysis showing cost and safety rate under different initial guesses or perturbed \(z\) would close this gap.

2. **No runtime cost is reported for solving the outer problem online.**  
   Root-finding requires multiple evaluations of \(V_\psi^h\) per agent per time step, but the paper gives no timing statistics. This affects real-time feasibility assessments, especially for large \(N\).

### Trivial
None.

## Nice-to-Haves

- Compare against a **centralized epigraph form** that treats the MAS as a single agent (e.g., GNN pooling all observations). This would directly quantify the performance cost of the distributed decomposition and help isolate whether gains come from the epigraph form itself or the decentralized execution.
- Include a brief **intuition sketch** of how Theorem 1's proof works in the main text (e.g., showing that for \(z = \max_i z_i\), the inner problem's optimal policy yields \(V^h \leq 0\) and therefore, via the structure of the objective \(\max\{V^h, V^l - z\}\), forces \(V^l \leq z\) at optimality).

## Removed Points

These points were flagged by reviewers but are either factually incorrect, misunderstandings, parser artifacts, or scope-creep. They are recorded here for completeness but should not be weighed in the evaluation.

- **"The decomposition ignores the cost constraint" as a fatal flaw.** While the main text's justification is insufficient (kept as Major above), the paper's claim is that Theorem 1 holds under the optimal inner-problem solution. A proof may exist in the stripped appendix. The criticism that the theorem is *simply wrong* cannot be verified without the proof, so it is downgraded from a fatal claim to a presentation/motivation gap.
- **"The experimental observation that agents perform well without communicating \(z_i\) undercuts the theorem further."** The paper explicitly addresses this in both the ablation study (Table 1) and the Limitations section: "If the communication on \(z\) is disabled … the theoretical optimality guarantee may not be valid." This transparency is a strength, not a weakness.
- **"The constant hyperparameters claim should be softened because \(\xi\) is a hyperparameter."** The paper's claim is about *cross-environment consistency*, not being parameter-free. Using the same \(\xi=0.4\) across all environments supports the claim.
- **Missing comparison with centralized epigraph form.** This is scope-creep — the paper's baselines (InforMARL, MAPPO-Lagrangian) are the relevant safe MARL comparisons.
- **Generic formatting/style nitpicks and missing-related-work concerns.**
- **"The paper should show how cost and safety vary with different \(z\) initial guesses"** — useful but infeasible for the root-finding as described; the method solves for \(z\) deterministically.
- **Criticisms about missing appendix proofs or absent references** per the parser-strip rule.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one interesting tension: **Theorem 1 claims that the outer problem can be solved using only \(V_i^h\) (no \(V^l\)), but the inner problem that generates \(\pi(\cdot,z)\) is trained using both \(V^h\) and \(V^l\).** This means the cost constraint is implicitly encoded into the policy during training — the theorem's distributed outer problem works *because* the centralized inner problem has already baked the \(V^l \leq z\) requirement into the \(z\)-conditioned policy. This separation of concerns (centralized training handles the coupling; distributed execution leverages the trained policy) is the real insight, even though the paper does not articulate it this way. The reviewer's confusion about "where did \(V^l\) go" is understandable precisely because this relationship is not explained.

## Suggestions

1. **In the main text, add a paragraph sketching Theorem 1's logic.** Show that for \(z = \max_i z_i\), the optimal policy from the inner problem satisfies \(V^h \leq 0\) (by construction of \(z_i\)), and then argue that the inner objective \(\max\{V^h, V^l - z\}\) forces \(V^l \leq z\) at optimality — or state any additional assumptions needed for the equivalence.
2. **Supplement the per-agent safety metric with an episode-level safety rate** (fraction of trajectories where every agent is safe throughout). This is a one-line change in evaluation and would preempt concerns about metric overstatement.
3. **Add a brief analysis of the \(z\)-conditioned policy's sensitivity** — e.g., a histogram of \(z\) values encountered during execution, or a plot of cost/safety vs. a perturbed \(z\).
4. **Report the average number of \(V_\psi^h\) evaluations per time step** needed by the root-finding procedure, to establish real-time feasibility.

## Score and Decision

The paper makes a solid contribution: it identifies a real problem (Lagrangian instability at zero threshold), extends a principled single-agent technique to the multi-agent CTDE setting, and demonstrates strong empirical results with fixed hyperparameters. The main weakness is a presentation gap around Theorem 1's justification, which is addressable in revision. The paper should be accepted with minor revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>