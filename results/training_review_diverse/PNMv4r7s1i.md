Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes Behavior-Supported Policy Optimization (BSPO), a method to mitigate reward over-optimization in RLHF. The key idea is to learn a "behavior policy" (the next-token distribution of the reward training dataset) to detect out-of-distribution (OOD) actions and penalize their Q-values via a behavior-supported Bellman operator, while leaving in-distribution (ID) values unaffected. The paper provides contraction and fixed-point theorems, monotonic improvement guarantees, and empirical results across three proxy model scales showing BSPO outperforms PPO, KL-Penalty, CPPO, and ensemble baselines on gold reward.

## Strengths

- **Novel value-regularization approach with theoretical guarantees**: The behavior-supported Bellman operator (Theorem 1: γ-contraction; Theorem 2/Corollary 2: unbiased ID evaluation; Theorem 3: monotonic improvement to optimal behavior-supported policy) provides a rigorous foundation that no baseline method matches. This is a distinctive contribution that cleanly formalizes the intuition of restricting policy search to the reward model's ID region.

- **OOD detection via next-token distribution is well-motivated and empirically validated**: Using the next-token distribution of the preference dataset as a behavior policy (Section 3.1) is a natural and elegant way to characterize the ID region of the reward model. Figure 1(c) provides compelling evidence: proxy model accuracy drops from 75.91% (supported responses) to 58.10% (unsupported responses), directly linking OOD actions to reward model extrapolation errors.

- **Consistent empirical improvement across multiple scales**: BSPO achieves the highest gold reward across three proxy model scales (774M, 1.1B, 2.7B) while maintaining increasing proxy rewards, outperforming PPO, KL-Penalty, CPPO, ENS-UWO, and ENS-WCO (Figure 3). The win-rate evaluation against the SFT model (Figure 4a) further corroborates this.

- **Lightweight single-model architecture**: ScoreLM jointly predicts rewards and the behavior distribution with negligible overhead (Section 4), and Figure 2(b) shows its reward accuracy is comparable to standard reward models, demonstrating no degradation from the auxiliary LM objective.

- **Explicit connection between OOD generation and over-optimization**: Figure 4(b) tracks behavior-unsupported actions during training and shows over-optimization in baselines coincides with a sharp rise in unsupported tokens, while BSPO suppresses them — providing direct evidence linking the proposed mechanism to observed outcomes.

## Weaknesses

### Fatal
None.

### Major

- **Support definition ambiguity — how is β(a|s) > 0 realized in practice?** The paper defines a behavior-supported action strictly as β(a|s) > 0 (Definition 1) and builds the entire operator around this binary condition. However, the behavior policy β is learned via a neural network (ScoreLM) with a softmax output layer over the vocabulary — a standard architecture that assigns positive probability to every token at every state. Under this implementation, β(a|s) > 0 holds for all (s, a) pairs, the penalty branch of Equation 1 never fires, and the operator reduces to the standard Bellman operator. The paper does not clarify how this tension is resolved: whether a probability threshold is applied (and if so, what value), whether empirical support from the training data is used, or whether some other mechanism produces actual zeros. Since the entire method hinges on distinguishing supported from unsupported actions, this is not a minor clarity issue — it is the linchpin of the contribution. The empirical results clearly work, so there *is* a practical solution; but the paper does not disclose it, making the mechanism underspecified and impossible to reproduce without guessing.

- **ScoreLM confounds the effect of the core regularization**. BSPO uses ScoreLM, which jointly trains a reward head and a language model head. The baselines (PPO, KL-Penalty, CPPO, ENS-UWO, ENS-WCO) presumably use standard reward models without the auxiliary LM objective. The multi-task training could improve feature representations or generalization in ways that benefit downstream RL independently of the behavior-supported regularization. The paper shows ScoreLM's reward accuracy is comparable to standard reward models (Figure 2b), which rules out better reward prediction as a confound, but does not rule out other benefits from joint training (e.g., better learned representations that help the critic). Without a control experiment using a separate (non-ScoreLM) reward model paired with an independent behavior policy, the gains attributed to the value regularization remain partially confounded with the architecture choice.

### Minor

- **No error bars or variance reporting for main results (Figure 3)**. The training curves in Figure 3 are shown without confidence intervals or standard deviations across seeds. Given the well-known variance of RLHF training, readers cannot assess the reliability and statistical significance of BSPO's advantage over baselines. Standard deviations appear only in Figure 2(b) (reward model accuracy).

- **Unclear which tokens are used for behavior distribution training.** Equation 5 trains the behavior distribution via the term E_D[log β(a_t|...)], but D contains preference pairs (chosen and rejected responses). The paper does not specify whether the LM loss is computed over chosen responses only, both responses, or all tokens in the dataset. This affects what the behavior policy actually models (the chosen-only distribution vs. the full preference data distribution) and consequently changes the ID region it defines.

- **Figure 4(b) analysis is partly circular.** Tracking behavior-unsupported actions during training shows BSPO maintains a low count and baselines show a rise at over-optimization. However, BSPO's value regularization is *designed* to penalize unsupported actions, so observing that it reduces them is expected and does not, by itself, demonstrate that this reduction *causes* the avoidance of over-optimization. The correlation is informative but the causal link would be stronger with a more direct analysis (e.g., showing that the *onset* of over-optimization in baselines is preceded by a rise in unsupported actions, or that interventions specifically on unsupported actions reproduce the BSPO effect).

- **Reward structure ambiguity in token-level MDP.** The paper acknowledges (Section 2) that in standard RLHF "the reward model assigns a reward to the final token of the sequence" (EOS token), but the theoretical development (token-level MDP, r(s,a) at every step) and the Bellman operators in Equations 1, 7, and 8 implicitly assume dense per-token rewards. The standard adaptation (r=0 for non-terminal steps, with value bootstrapping) is well-known in the LLM RL literature, so this is not a structural flaw, but the paper should explicitly state this bridging assumption to connect theory to practice.

### Trivial
None.

## Nice-to-Haves

- **Sensitivity analysis for the support threshold**: If a threshold ε > 0 is used in practice, a sensitivity study would help readers understand how results vary with this choice.
- **Reporting the α hyperparameter value** in Equation 5 (balancing reward and LM losses) and its sensitivity.
- **Comparison with an uncertainty-based baseline** (e.g., Zhang et al., 2024) would strengthen positioning.
- **Quantified computational cost** (training time, FLOPs) rather than the qualitative "negligible" claim.
- **Statistical significance** for the Figure 1(c) accuracy gap (75.91% vs 58.10%).

## Removed Points

- *Missing appendix/hyperparameters, missing proofs*: The parser strips supplementary material; these are known to exist in the original submission.
- *Criticism about missing CQL / offline RL comparison*: This is a reasonable suggestion for the "Nice-to-Haves" section but not a weakness — connections to offline RL are already briefly acknowledged (Section 3.1 cites Levine et al., 2020; Wu et al., 2022), and the paper targets online RLHF, not offline RL.
- *"The paper should include an additional behavioral cloning baseline" or similar demands for broader evaluation*: These would make the paper a different, broader evaluation study rather than a stronger version of its current contribution.
- *Generic formatting/style nitpicks*: Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the support definition** as the highest priority. Explicitly state whether β(a|s) > 0 is computed via a threshold (and what value), empirical support in training data, or another mechanism. Show sensitivity to the threshold if applicable. Without this, the core mechanism is underspecified.
2. **Address the ScoreLM confound** by either running a control experiment with a separate reward model + behavior policy, or clearly discussing this as a limitation and explaining why the Figure 2(b) evidence (comparable accuracy to standard RMs) mitigates the concern.
3. **Add error bars to Figure 3** from multiple seeds (at least 3) to establish statistical reliability.
4. **Clarify Equation 5**: specify whether the LM loss uses chosen responses only, both responses, or all tokens.
5. **Explicitly connect the sparse terminal reward** (standard in RLHF) to the token-level MDP formulation in Section 2.

## Score and Decision

The paper tackles an important problem with a novel, theoretically grounded approach, and the empirical evidence (across three scales, against five baselines) is promising. However, two significant issues prevent full evaluation: (1) the underspecified binary support criterion — the entire method hinges on the ability to distinguish supported from unsupported actions, but the paper never explains how a softmax-based neural network can produce the strict zeros or thresholds needed for this distinction; and (2) the ScoreLM architecture confound, which makes it unclear whether the observed gains stem from the behavior-supported regularization or from the multi-task training of the reward model itself. These are fixable in revision, but in the current form the contribution cannot be fully assessed. A carefully revised version with these clarifications and controls would be a strong paper.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>