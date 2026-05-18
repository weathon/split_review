Now I have a thorough understanding of the paper. Let me synthesize and write the consolidated review, carefully verifying each claim against the paper text.

---

## Summary

This paper proposes Behavior-Supported Policy Optimization (BSPO), a method to mitigate reward over-optimization in RLHF. The core idea is to define a "behavior policy" — the next-token distribution of the reward training dataset — and use it to construct a behavior-supported Bellman operator that penalizes Q-values for out-of-distribution (OOD) actions without affecting in-distribution (ID) ones. The paper provides contraction guarantees, fixed-point characterizations, and a monotonic improvement theorem for the resulting policy iteration. Empirically, BSPO achieves the highest gold reward across three proxy model scales (774M, 1.1B, 2.7B) and reduces the generation of OOD responses during RL compared to baselines (KL-penalty, CPPO, ensemble methods).

## Strengths

1. **Behavior-supported Bellman operator preserves ID action values.** The operator 𝒯ᵦ^π (Eq. 1) applies Q_min only to OOD actions while keeping the standard Bellman operator for ID actions. Corollary 2 shows that for any behavior-supported policy, Qᵦ^π(s,a) = Q^π(s,a) for ID actions. This directly addresses a limitation of prior regularization methods that distort ID values (Section 3.2, lines 69–105).

2. **Monotonic improvement guarantee to the optimal behavior-supported policy.** Theorem 3 (line 107) proves that the behavior-supported policy iteration yields strictly monotonic performance improvement until convergence. This provides a theoretical grounding that existing baselines (KL-penalty, CPPO, ensemble methods) lack.

3. **Consistent empirical outperformance across three model scales.** In Figure 3, BSPO achieves the highest gold reward across all three proxy model sizes (774M, 1.1B, 2.7B), while maintaining a monotonically increasing gold reward curve. The win-rate evaluation against the initial SFT model (Figure 4a, using the 2.7B proxy model) confirms BSPO outperforms all baselines.

4. **Empirical evidence linking OOD generation to over-optimization.** Figure 4(b) tracks the number of behavior-unsupported actions during RL. Baselines show a sharp rise coinciding with over-optimization, while BSPO maintains a consistently low count. This validates the core mechanism that BSPO reduces OOD generation.

5. **Lightweight implementation via ScoreLM.** The ScoreLM architecture retains the original language model head to predict behavior distribution alongside a reward head (Figure 2a), introducing negligible additional memory and computational overhead relative to standard PPO. Performance on the test set (Figure 2b) is comparable to standard reward models across three scales.

## Weaknesses

### Fatal
None.

### Major

1. **The β(a|s) > 0 condition is underspecified, creating a gap between theory and practice.** The behavior policy β is defined as a next-token distribution (softmax) from the ScoreLM model, trained via a cross-entropy loss (line 124). With a standard softmax, β(a|s) > 0 for *every* token in the vocabulary, making the "otherwise" (Q_min) branch of the behavior-supported Bellman operator (Eq. 1) unreachable in theory. This would collapse BSPO to standard PPO. Conversely, if a threshold or discretization is used in practice, the paper never says so. The empirical results (Figure 4b) show the method *does* distinguish supported from unsupported actions, so a practical mechanism clearly exists — but the paper provides no description of it.

   This is not a minor presentation issue: the entire theoretical framework (contraction guarantees, fixed-point theorems, monotonic improvement) depends on a binary partition of actions that is not specified for the practical algorithm. The reader cannot determine whether the reported empirical success is due to the claimed mechanism or to some other aspect of the implementation. The code (in supplementary material) may clarify this, but the paper itself should explain how β(a|s) > 0 is evaluated — what model output is thresholded, what threshold is used, and what fraction of actions are classified as supported in practice.

### Minor

2. **The theoretical guarantees concern the proxy MDP, not gold reward.** Theorem 3 guarantees monotonic improvement in "policy performance" J(π), which is defined with respect to the *proxy* reward r(s,a) (Section 2, line 31). The paper does not overclaim this — it never asserts the theory covers gold reward — but the framing could mislead readers into thinking the theory directly addresses over-optimization. Over-optimization is precisely the divergence between proxy and gold reward; the theory guarantees stable optimization of proxy reward, while the gold-reward benefits are purely empirical claims. The paper would benefit from explicitly stating that the theoretical results concern the proxy MDP and that closing the proxy-gold gap is an empirical finding.

3. **The main experimental results (Figure 3) lack error bars.** The paper reports "standard deviation of four repetitions" only for the ScoreLM validation accuracy (Figure 2b caption). For the central RL results in Figure 3, no confidence intervals, standard deviations, or measures of variability are shown. At the 774M scale, the gold reward of BSPO and ENS-WCO nearly overlap at step 80, making significance unclear. Error bars (or shaded regions) are needed to assess whether the reported differences are reliable.

4. **Win-rate evaluation is only reported for the 2.7B proxy model.** Figure 4(a) shows win rates against the initial SFT model using only the 2.7B proxy. Consistency would dictate reporting win rates for all three scales used in the main results.

5. **Hyperparameter details for baselines are not provided.** The paper does not state how KL penalty coefficients, CPPO thresholds, ensemble sizes, or BSPO's α (balancing the two ScoreLM losses) were chosen. Without this, there is a risk that BSPO's advantage stems from better tuning rather than the method itself.

6. **The claim of being "the first method that uses value regularization to address reward over-optimization" (line 23) is slightly overstated.** KL penalty with a learned value function already constitutes a form of value-adjacent regularization. The genuine novelty lies in *which* actions are penalized (behavior-supported vs. unsupported) and in modifying the Bellman operator specifically, not in using value regularization per se. The claim could be softened without diminishing the contribution.

### Trivial
None. (The minor points above are already at the appropriate granularity.)

## Nice-to-Haves

- An ablation where the behavior policy is derived from a different source (e.g., the pretrained LLM's own next-token distribution) to test how sensitive results are to the specific definition of β.
- A demonstration that the binary partition β(a|s) > 0 is robust to reasonable variations in any threshold that might be used.
- An analysis showing that the same response-level accuracy gap (75.91% vs. 58.10% in Figure 1c) holds when using the actual ScoreLM model for the partition, rather than the unspecified method used for Figure 1(c).

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper:

1. **"The definition of behavior policy conflates two senses of 'distribution' — in offline RL, a behavior policy is the policy that generated the data."** The paper explicitly states it is "inspired by offline RL" (line 47), not that it inherits offline RL properties. The paper develops its own theory (Theorems 1–4, Corollaries 1–3) from scratch, none of which depend on the behavior policy having generated the data. This criticism interprets the paper as making a stronger claim than it actually does.

2. **"Figure 4(b) y-axis up to 140 tokens is implausibly high for a 50-token response."** The paper does not state that the average response length is 50 tokens. This assumption is introduced by the reviewer and is not grounded in the paper. The figure description tracks "the average number of actions (tokens) that are not supported by the behavior policy for each response" — without knowing the actual response lengths from the UltraFeedback dataset, the magnitude is not assessable from this criticism.

3. **"The paper should not be accepted in its current form" / overall text suggesting rejection.** The paper makes a genuine contribution with clear theoretical analysis and consistent empirical results. The β(a|s) > 0 issue is real but addressable — the method empirically works (Figure 4b proves the mechanism functions), and the gap is in documentation, not in correctness of the core idea. This does not warrant rejection.

## Novel Insights

None beyond the paper's own contributions, and the cross-referencing of reviews does not surface a perspective that the paper itself does not already provide.

## Suggestions

1. **Clarify the β(a|s) > 0 condition.** State explicitly: (a) whether a numerical threshold ε > 0 is used to binarize the softmax outputs, (b) what that threshold is, (c) what fraction of (s,a) pairs encountered during RL fall on each side of the threshold, and (d) whether results are robust to the choice of threshold. This single clarification would resolve the paper's most significant weakness.

2. **Add error bars to Figure 3.** Show standard deviations or confidence bands (shaded regions) across multiple runs. If only single runs were conducted for the main RL results, this should be stated and multiple runs added.

3. **State explicitly that the theoretical guarantees apply to the proxy MDP.** Add a sentence in Section 3.2 or near Theorem 3 clarifying that "policy performance" refers to the proxy reward model's evaluations, and that the gold-reward improvements are empirical findings supported by the distributional alignment between the ID region and accurate reward prediction.

4. **Report win rates for all three proxy model scales** for consistency with the main results.

5. **Disclose how baseline hyperparameters were selected** (grid search ranges, fixed values from prior work, etc.) to address potential tuning-fairness concerns.

## Score and Decision

The paper presents a clean theoretical framework and consistent empirical results for an important problem. The main weakness — the underspecified β(a|s) > 0 condition — is real but addressable in revision: the empirical evidence (particularly Figure 4b) strongly suggests the implementation works, so the gap is in documentation, not correctness. The lack of error bars and partial win-rate reporting weaken the empirical contribution but do not invalidate it. The paper merits conditional acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>