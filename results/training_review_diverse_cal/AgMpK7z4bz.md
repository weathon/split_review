Now I have thoroughly verified the paper content against the reviewer's claims. Let me compile the final review.

---

## Summary

This paper proposes ARAM, a framework for action-constrained RL (ACRL) that combines (i) an acceptance-rejection method (ARM) to enforce per-step action constraints without QP projection, and (ii) an augmented two-objective MDP (AUTO-MDP) that adds self-loop transitions and a penalty signal for infeasible actions to improve the acceptance rate of the proposal policy. Using multi-objective SAC to handle the preference trade-off, ARAM achieves competitive rewards and constraint satisfaction while reducing QP operations by 2–5 orders of magnitude compared to projection-based and Frank-Wolfe baselines.

## Strengths

1. **Novel and practical combination of ARM with an augmented MDP**: The paper identifies the low-acceptance-rate problem of naive ARM and addresses it by constructing AUTO-MDP, which provides a learning signal (penalty + self-loop) that incentivizes the policy to move toward feasible regions. This is a clean, lightweight idea that avoids the architectural complexity of generative models.

2. **Dramatic reduction in QP operations**: Figure 4 shows ARAM uses 2–5 orders of magnitude fewer cumulative QP operations than projection-based methods (DPre+, SPre+) and Frank-Wolfe (NFWPO) across all domains. This is the strongest piece of evidence supporting the paper's efficiency claim.

3. **Low per-action inference time**: Table 3 reports ARAM's inference time (e.g., 0.01 ms in HalfCheetah vs. 1.44 ms for DPre+), an order of magnitude faster than all baselines. This is important for deployment in latency-sensitive applications.

4. **Multi-objective RL implementation avoids preference tuning**: The ablation in Figure 5 shows that MORL discovers policies with both high reward and high valid action rate, while fixed-preference variants fail on at least one criterion. This demonstrates a practical benefit of the design.

5. **Theoretical grounding via equivalence proof**: Proposition 1 shows that any optimal feasible policy under the original MDP remains optimal among all (including infeasible) policies under AUTO-MDP, providing formal justification that solving the augmented MDP does not sacrifice optimality.

6. **Comprehensive evaluation across multiple domains**: Experiments span MuJoCo locomotion (HalfCheetah, Ant, Walker2d, Humanoid) and resource allocation tasks (NSFnet, BSS3z, BSS5z), with comparisons against several strong baselines (NFWPO, DPre+, SPre+, FlowPG, FOCOPS).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The penalty constant κ is a free hyperparameter whose value and sensitivity are not reported.** The paper introduces κ > 0 (line 84) as the penalty magnitude for infeasible actions, but never states what value was used in experiments or whether results are sensitive to this choice. While the MORL approach handles the preference vector λ, κ is orthogonal and still needs to be set. This is a missing experimental detail that affects reproducibility.

2. **The auxiliary projection step's role for ARAM is underspecified.** The paper states that "during the testing of all the above algorithms, an auxiliary projection step is employed" (line 148) and later describes ARAM as "almost QP-free" (line 171). The paper should explicitly state how the fallback works: how many ARM trials are attempted before projection, and how often it actually triggers during evaluation. Without this, readers cannot assess how close ARAM is to being truly projection-free. That said, the QP counts in Figure 4 already validate the dramatic relative reduction — this is a reporting gap rather than a contradiction of the core claim.

3. **Generation of infeasible transitions could be described more explicitly.** The AUTO-MDP definition (Section 4.2) and the dual-buffer design (Section 4.3) together imply the data-flow: when ARM rejects an action, it is stored as an infeasible transition (self-loop state, penalty reward) in the augmented buffer. But the paper never states this step explicitly. Most readers will infer it correctly, but a brief walkthrough would improve clarity and reproducibility, especially since the reviewer mistakenly saw this as a "significant departure" from standard off-policy RL.

4. **Dual-buffer sampling ratio and how λ conditions the networks are unspecified.** The paper mentions a dual-buffer design and that the preference λ is drawn uniformly from the 2D simplex, but does not specify (i) the ratio of feasible to infeasible transitions used per update, (ii) whether λ is fed as an additional input to the policy/critic networks or handled differently, and (iii) how the preference is sampled at each update step. These details would aid reproducibility.

5. **Scope of constraint generality is untested.** The paper claims "we make no assumption on the structure of C(s)" (line 36) and that constraints can take "arbitrary forms of expression" (line 58). However, all tested environments use simple linear or box constraints. While consistent with the ACRL literature, the claim of handling arbitrary (e.g., non-convex) constraint sets is not validated experimentally. This does not invalidate the results, but the scope should be calibrated.

### Trivial

- The proof of Proposition 1 and the pseudo-code (Algorithm 1) are relegated to the (parser-stripped) appendix. A brief proof sketch in the main text would improve accessibility.

## Nice-to-Haves

- A learning curve of the action acceptance rate over training would directly confirm that AUTO-MDP increases acceptance rate as claimed.
- A sensitivity analysis of κ (or an argument for why its value is unimportant given the MORL coverage over λ) would strengthen the hyperparameter discussion.
- The FOCOPS comparison (Tables 4–5) could be replaced or supplemented with an ablation of the dual-buffer design or a study of the effect of buffer ratio.

## Removed Points

These points were flagged by the reviewer but are removed with justification:

1. **"Proposition 1 fails for λ_c=0"** — Removed because it is factually incorrect. Even when λ_c=0, the self-loop transition (not just the penalty) ensures that infeasible actions yield zero discounted return indefinitely, while feasible actions can achieve non-negative reward and transition to potentially better states. An optimal feasible policy therefore remains optimal for all λ ∈ Λ, including λ=(1,0). The reviewer overlooked the self-loop's role.

2. **"Synthetic infeasible transitions are a significant departure from standard off-policy RL"** — Downgraded from major to minor (point 3 above). The AUTO-MDP is the method's deliberate design, not a hidden trick. The paper clearly defines the transition and reward for infeasible actions; storing these as transitions follows directly. The reviewer's characterization as "simulated experience not grounded in real environment dynamics" misunderstands the construction — the AUTO-MDP is a modified MDP, and the learning signal comes from this modification by design.

3. **"The auxiliary projection step contradicts the central efficiency claim"** — Removed as a contradiction, kept as a reporting gap (point 2 above). The paper's language ("largely obviates," "almost QP-free") is accurate. Figure 4 already demonstrates orders-of-magnitude reduction. The auxiliary projection is applied to *all* methods equally for fair comparison, so it does not undermine the relative efficiency claim.

4. **"FOCOPS comparison does not add much"** — Removed. The authors explicitly state this comparison is for comprehensiveness. Whether to include it is the authors' judgment, not a weakness.

5. **"The MOSAC training details are too vague"** — Partially removed (preference distribution *is* specified in line 139 as uniform/Dirichlet). Kept as minor (point 4 above) regarding the dual-buffer ratio and network conditioning.

6. **Criticism about missing proof sketch / appendix** — Removed per rule about parser-stripped appendix content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Report the value of κ used in experiments, and ideally provide a sensitivity study or an argument for why κ can be absorbed into the MORL coverage over λ.
2. Explicitly describe the infeasible transition generation: when ARM samples an action a ∉ C(s), store (s, a, s, [0, −κ]) in the augmented replay buffer D_a, and indicate the sampling ratio between D_r and D_a.
3. Report how many ARM trials are attempted before the auxiliary projection step triggers during evaluation, and state the observed fallback frequency. This would fully resolve any ambiguity about the efficiency claims.
4. Clarify how the preference vector λ is incorporated into the policy and critic network architectures (e.g., as a concatenated input).
5. Calibrate the claim about handling "arbitrary" constraint shapes, or test at least one non-convex or non-linear constraint to back it up.

## Score and Decision

The paper presents a legitimate and practically appealing approach to ACRL that combines ARM with an augmented MDP to dramatically reduce QP overhead. The experimental evidence for the core claims is strong: orders-of-magnitude QP reduction, competitive rewards, and high valid action rates across multiple domains. The weaknesses are primarily about missing experimental details and clarity of exposition — none threaten the central contribution. The paper would benefit from a focused revision that fills in these details.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>