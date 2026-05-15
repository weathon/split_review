Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes Behavior-Supported Policy Optimization (BSPO) for mitigating reward over-optimization in RLHF. The key idea is to use the next-token distribution of the reward training dataset as a "behavior policy" to define the in-distribution (ID) region of the reward model, then apply a behavior-supported Bellman operator that penalizes out-of-distribution (OOD) actions in the value function without affecting ID ones. The paper provides theoretical analysis (contraction, fixed-point properties, monotonic improvement to the optimal behavior-supported policy) and empirical results across three proxy model scales showing BSPO achieves higher gold reward than five baselines.

## Strengths

- **Novel and well-motivated regularization that preserves ID evaluation while penalizing OOD actions**: The behavior-supported Bellman operator (Eq. 1) modifies only OOD actions (setting them to \(Q_{\min}\)) and leaves ID actions unchanged. Theorem 2 and Corollary 2 formally show that for behavior-supported policies, the regularized Q-value equals the standard Q-value for all in-distribution actions. This directly addresses the limitation that prior methods "also impact the evaluation of ID ones, potentially leading to suboptimal solutions" (Sec. 1).

- **Strong empirical results across multiple model scales**: In Figure 3, BSPO achieves the highest final gold reward and avoids the proxy/gold reward divergence seen in all five baselines (PPO, KL-Penalty, CPPO, ENS-UWO, ENS-WCO) at three model sizes (774M, 1.1B, 2.7B). The win-rate evaluation against the initial SFT model (Figure 4a) further confirms BSPO's advantage.

- **Empirical validation of the OOD detection mechanism**: Figure 1(c) shows that responses containing behavior-unsupported actions have sharply lower proxy-model accuracy (58.10% vs. 75.91% for supported responses), directly supporting the claim that the next-token distribution from the reward training dataset is an effective OOD indicator. Figure 4(b) further shows that BSPO maintains a consistently low count of unsupported actions, while over-optimization in baselines is preceded by a sharp rise.

- **Lightweight implementation with negligible overhead**: The ScoreLM architecture (Figure 2a) retains the original language model head to predict the behavior distribution alongside the reward head, requiring negligible additional memory and computational overhead relative to standard PPO.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical guarantee (Theorem 3) applies to proxy reward, not gold reward**: Theorem 3 proves monotonic improvement to the optimal behavior-supported policy under the regularized Q-function derived from the *proxy* reward. The paper's stated problem is reward over-optimization — the divergence between proxy and gold reward. The theorem does not establish any guarantee about gold reward improvement, nor does it prove that the optimal behavior-supported policy is optimal under gold reward. The paper connects the theory to the practical goal through reasoning that staying ID avoids extrapolation errors (empirically supported), but the formal claim is about the proxy reward's regularized value, not about the gold objective. This is not fatal — the paper's empirical evidence stands independently — but the theoretical framing would benefit from clearly delineating what the theory does and does not cover, rather than implying the theory directly supports the over-optimization mitigation claim.

### Minor

- **Corollary 1 overstates the theoretical guarantee**: The claim that the policy update in Eq. 3 "yields behavior-supported policy π ∈ Π_β" (where Π_β requires π(a|s) = 0 for unsupported actions) is stronger than what the policy optimization step strictly guarantees. The argmax over Π in Eq. 3 may yield a policy that assigns extremely small (but non-zero) probability to unsupported actions, especially under standard softmax parameterizations. A statement about asymptotic convergence to a supported policy would be more precise.

- **Synthetic evaluation setup creates a closed loop**: The gold model (Llama3-8B) generates the preference labels on which the proxy reward models are trained, and the final evaluation (gold reward, win rate) is against that same gold model. While this synthetic setup is the standard practice in the over-optimization literature (Gao et al., 2023; Coste et al., 2023) and the paper acknowledges it as a limitation, it remains a significant evidential gap: there is no evaluation on real human preferences or a held-out gold model unseen during proxy training. The claim that BSPO "mitigates reward over-optimization" is supported only under this synthetic approximation.

- **No ablation isolating the effect of value regularization from the OOD detection**: Figure 4(b) shows BSPO keeps unsupported actions low, but this could partly be an artifact of the behavior-policy-based action filtering rather than the value regularization specifically. A comparison to a variant that simply masks or zeroes out unsupported action probabilities during PPO (without the value penalty) would help isolate whether the value regularization itself is necessary.

### Trivial

- No reporting of variance across random seeds beyond the short vertical lines in Figure 2. The main results (Figure 3, Figure 4a) do not quantify statistical uncertainty.
- The paper does not discuss how Q_min is chosen or whether it is data-driven; it appears to be computed from the minimum reward in the training data.

## Nice-to-Haves

- Hyperparameter sensitivity analysis for α (ScoreLM loss weight) and the discount factor γ would strengthen the presentation.
- Case studies showing concrete examples of supported vs. unsupported responses that BSPO avoids compared to baselines would make the mechanism more interpretable.
- A theoretical discussion of how the behavior-supported policy iteration relates to the gold reward (even informally) would help bridge the gap between the theory and the practical goal.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about Q_min assumption in Theorem 2**: The critic claimed that the proof "relies on the assumption that Q_min ≤ Q^π(s,a) for all (s,a)" and that this "is plausible but not discussed." This is factually wrong — it follows directly from the definitions (Q_min = r_min/(1-γ) where r_min = min r(s,a), and every reward in the trajectory is ≥ r_min, hence Q^π(s,a) ≥ Q_min). There is no assumption; this is a trivial consequence.

- **Criticism about missing offline RL baselines (CQL, BRAC)**: The critic claimed the paper overlooks offline RL literature and that methods like CQL also use value regularization for OOD actions. CQL addresses offline RL distribution shift, which is a fundamentally different problem from reward over-optimization in the RLHF online RL setting. The paper is scoped to online RLHF; offline RL methods do not apply to this setting because there is no offline dataset for the RL phase. This is scope creep.

- **Criticism about Theorem 3 not defining J(π)**: The paper clearly defines the performance measure J(π) in Section 2 as the infinite-horizon discounted return under the proxy reward. The critic appears to have missed this definition.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the theoretical framing**: Explicitly state in Section 3.2 and the conclusion that Theorem 3 guarantees convergence to the optimal behavior-supported policy *under the proxy reward*, and explain how this relates to (but does not directly prove) gold reward improvement. This would prevent the mismatch identified above.

2. **Add a real-human or cross-model evaluation**: Even a small-scale human evaluation or an evaluation using a different gold model (not the one that generated proxy training labels) would significantly strengthen the evidence that the method transfers beyond the synthetic setup.

3. **Include an ablation without value regularization**: Compare BSPO to a variant that simply suppresses unsupported actions (e.g., by masking their logits during PPO) without the behavior-supported value regularization. This would disentangle whether the value regularization or the OOD detection alone drives the improvement.

4. **Report variance for main results**: Include error bars or confidence intervals for the gold reward curves and win rates in Figures 3 and 4(a).

## Score and Decision

This paper presents a genuinely novel approach to a well-recognized problem in RLHF. The core idea — using the behavior policy derived from the reward training data to define an ID region for value regularization — is clever and well-motivated. The empirical results are consistent and strong across multiple model scales, and the supporting ablations provide evidence for the claimed mechanism. The theoretical analysis (contraction, fixed-point equivalence) is technically sound.

The main weaknesses are: (a) the theoretical guarantee is about the proxy reward rather than the gold reward that defines the over-optimization problem (a gap the paper could address by clarifying the scope of its claims), and (b) the evaluation is entirely within a synthetic setup (a limitation common to the field and acknowledged by the authors). Neither weakness invalidates the contribution — the method works empirically, and the theory correctly characterizes the algorithm's convergence properties within the ID region.

The paper would benefit from a human or cross-model evaluation, a cleaner separation between what the theory guarantees and what the empirical results show, and an ablation isolating the value regularization from the OOD detection. With these revisions, the paper would be a strong contribution. In its current form, the contribution is solid but somewhat weakened by the misalignment between theoretical framing and empirical objective.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>