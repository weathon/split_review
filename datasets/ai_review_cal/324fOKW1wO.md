- Decision: Reject
- Avg Score: 3.33
- Scores: 1, 3, 3, 3, 5, 5
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes SimDT, a Decision Transformer variant for autonomous driving that integrates three components: multi-token prediction (predicting multiple future actions in a single forward pass), an online imitative reinforcement learning pipeline that mixes offline expert data with online policy rollouts, and a prioritized experience replay mechanism adapted for Decision Transformers (using action loss as a proxy for TD-error). The method is evaluated on the Waymax benchmark using the Waymo Open Motion Dataset, achieving a 2.69% collision rate in closed-loop evaluation, which is the lowest among learning-based methods reported in the benchmark table.

## Strengths

1. **Consistent safety improvements demonstrated through controlled ablation (Table 3)**: The ablation study cleanly isolates each component's contribution. Adding PER to the base DT reduces off-road rate from 6.21% → 4.59% (26.1% reduction). Adding OPA reduces collision rate from 3.42% → 2.92%. Adding multi-token prediction further reduces collision rate from 2.92% → 2.65% (3-token) → 2.59% (5-token). These improvements, while incremental, are consistent across all metrics and supported by standard deviations over 3 seeds.

2. **Effective adaptation of PER to Decision Transformers**: Since DT does not compute TD-errors, the paper uses action loss as a proxy for transition importance. Table 3 shows concrete sample-efficiency gains (fewer off-road incidents and collisions), and Figure 8 shows accelerated learning convergence. The adaptation is well-motivated and the empirical evidence supports the claim.

3. **Best collision rate among learning-based methods in closed-loop evaluation (Table 1)**: SimDT achieves 2.69% collision rate vs. the best BC variant (4.59%), DQN with Playback (4.91%), and Wayformer (10.68%). The 0.00% kinematic infeasibility is also notable and matches expert performance. These results on the Waymax benchmark using real-world driving data provide credible evidence that the combined method improves safety.

4. **Practical real-time feasibility reported**: The paper reports inference latency of 1.63ms on an RTX 3090, demonstrating that the model can run at well above real-time rates, which is relevant for the claimed application to real-world driving.

## Weaknesses

### Fatal
None.

### Major

1. **"18% improvement in reaching the destination" is unverifiable from the presented data (undermines a headline claim)**: This claim appears in the abstract and introduction but cannot be mapped to any metric in the results tables. In the closed-loop benchmark (Table 1), SimDT's route progress ratio (106.47%) is *lower* than BC Bicycle(D) (129.84%). In the open-loop table (Table 2), SimDT achieves 105.63% vs. BC's 99.00%, which is approximately a 6.7% relative improvement — not 18%. "Reaching the destination" is not defined as a metric, and no table or figure supports the 18% figure. The authors should either clarify which baseline and metric this refers to, or remove the claim.

2. **Closed-loop benchmark (Table 1) mixes incompatible experimental configurations, obscuring attribution**: The table spans multiple action spaces (Delta, Bicycle, Bicycle Discrete) and training simulation agents (IDM, Playback) across methods. SimDT uses continuous Bicycle with Playback-trained policy, while DQN uses discrete Bicycle(D) with IDM or Playback, and BC variants span all combinations. The table caption states evaluation is "against IDM simulation agents," but the "Train Sim Agent" column shows different settings. This makes it impossible to determine whether SimDT's advantage is due to the proposed method or to differences in action space discretization and training simulator. A controlled comparison holding these factors constant is needed.

### Minor

3. **Multi-token prediction mechanism is ambiguously described**: Equation (2) defines multi-token loss as predicting multiple future actions conditioned on the *same* history context. The paper states this "simultaneously generates multiple actions in a single forward pass, while still respecting the autoregressive property," but does not clarify the implementation mechanism — whether actions are predicted in parallel from shared embeddings (which would violate autoregressive conditioning among the predicted actions) or via separate heads with causal masking across time offsets. Without this clarification, the novelty and correctness of the multi-token approach cannot be fully assessed.

4. **Reproducibility-critical details are missing**: Algorithm 1 specifies "train on sampled data" and "for k in range(1000)" but omits batch size, learning rate, optimizer, number of online rollouts per iteration, reward scale, and PER-specific hyperparameters (priority exponents, sampling probability formula, importance-sampling weighting). The PER algorithm (Algorithm 2) describes storing trajectories with $L_{single}$ and $L_{overall}$ but does not define how these priorities are computed, normalized, or sampled. These omissions prevent reproduction.

5. **The "Route Progress Ratio >100%" result is not adequately explained**: SimDT achieves 105.63% route progress in open-loop evaluation, meaning it drives *beyond* the expert trajectory length. The paper frames this as "discovering more efficient routes," but in open-loop evaluation the agent is non-reactive — this likely reflects deviation from the expert path rather than genuine efficiency. The paper does not clarify how Waymax computes this metric for off-reference trajectories or whether divergent routes could inflate the ratio.

6. **The median model does not clearly outperform the small model**: In Table 3, DT(median)+PER+OPA+3-token achieves 2.69% collision rate vs. DT(small)+PER+OPA+3-token at 2.65% — the larger model performs *marginally worse* on collision. The improvement in ADE (7.14m vs. 7.52m) and off-road rate (3.52% vs. 3.82%) is modest. This weakens the claim that scaling model size helps.

7. **No statistical significance tests**: Given overlapping standard deviations in several comparisons, it is unclear whether observed differences are statistically meaningful. This is a standard expectation for empirical papers.

### Trivial

8. **Inconsistent naming**: The conclusion refers to "SmiDT" while the title, abstract, and body use "SimDT."

9. **Minor notation ambiguity in Equation (1)**: The notation $s_{t:t-c}$ could be clarified to indicate the direction of the context window ($s_t, s_{t-1}, ..., s_{t-c}$), though the surrounding text does clarify this.

## Nice-to-Haves
- A controlled study varying only the number of future tokens (keeping all else fixed) with analysis of why 7 tokens cause degradation, rather than just the one-row ablation.
- Demonstration that varying the input return-to-go produces different driving behaviors (cautious vs. aggressive), which would validate that SimDT goes beyond behavior cloning.
- A failure analysis of the remaining 2.69% collisions (e.g., rear-ends vs. intersection violations) to guide future work.
- Ablation of the "ShuffleObstacleOrder" data augmentation to justify its use.
- Wall-clock time or total environment steps to substantiate the "sample-efficient" claim.

## Removed Points

These points from the inputs were checked against the paper and removed with justification:

- **"Cherry-picking the weakest-performing BC baseline" (Harsh Critic)**: Factually incorrect. BC Bicycle(D) has 4.59% collision rate — the **lowest** (best) among all BC variants in Table 1. The 41% improvement (4.59% → 2.69%) is computed against the strongest BC variant, not the weakest. If compared against BC Bicycle with the same continuous action space (11.20%), the improvement would be even larger (~76%). The action space mismatch is a real concern (addressed in Weakness #2 above), but the "cherry-picking" accusation is wrong.
- **"Makes the improvement trivial" (Harsh Critic)**: The critic's claim that using BC Bicycle (same continuous action space, 11.20%) as baseline would produce a "trivial" improvement contradicts arithmetic — a 76% reduction is larger, not trivial.
- **"Single-token prediction claim asserted without evidence" (Harsh Critic)**: The paper cites gloeckle2024better and provides a reasonable motivation; this is a standard literature-backed claim.
- **"Several comparisons in Related Work are inflated" (Harsh Critic)**: Too vague to verify against the paper; no specific examples given.
- **"Return-to-go not demonstrated" (Harsh Critic)**: Partially addressed in Section 3.3's discussion of how return-to-go is used with suboptimal data.
- **Compute cost / total environment steps**: The paper reports inference time (1.63ms) which partially addresses efficiency. Requesting additional cost metrics is a nice-to-have, not a weakness.
- **Missing limitations paragraph**: Not standard for all conferences; the paper does mention broader applicability in the conclusion.
- **Various formatting/style nitpicks**: Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The two independent reviews largely converge on the same picture: the paper's core technical contributions (PER for DT, multi-token prediction, online imitative pipeline) are reasonable and supported by clear ablation evidence, but the strength of the headline claims is undermined by opaque reporting and an experimental table that does not fully control for action space and training agent configuration. The "18% improvement" claim is the single most significant unaddressed issue — it cannot be verified from the paper as written.

## Suggestions

1. **Clarify or remove the "18% improvement in reaching the destination" claim.** If it refers to a specific metric, define it and point to the supporting table. Otherwise remove it from the abstract and introduction.
2. **Re-run or re-tabulate the closed-loop benchmark (Table 1) with all methods using the same action space and training simulation agent.** At minimum, add a row for BC(Bicycle, Playback) and DQN(Bicycle, Playback) so the comparison is controlled. If this is not feasible, clearly separate the comparison into groups with matched configurations.
3. **Provide implementation details for PER in the appendix or supplementary material:** priority computation formula, sampling probability calculation, importance-sampling weighting, priority update frequency, and the exponent values.
4. **Explain the Route Progress Ratio >100% result in open-loop.** State whether trajectories that leave the expert corridor are penalized or clipped, and whether the ratio can be inflated by path deviation.
5. **Clarify the multi-token prediction mechanism.** State whether predictions are made in parallel from shared context (multi-task prediction) or autoregressively with causal masking across time positions, and whether teacher forcing is used during training.
