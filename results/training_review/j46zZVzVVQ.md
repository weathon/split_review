Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes Preference Control RL (PCRL), a framework for training a single preference-conditioned meta-policy that can adapt its multi-objective trade-off to different user preferences at inference time. The key technical contribution is PreCo, a gradient manipulation algorithm that combines standard objective gradients with a novel similarity gradient (Definition 4.1) designed to align the policy's value vector with the input preference while maintaining Pareto optimality. Experiments on Fruit Tree (3–6 objectives), MO-Ant, MO-Hopper, and MO-Reacher show that PreCo consistently achieves strong Hypervolume and Cosine Similarity, and the MO-Reacher heatmaps provide compelling visual evidence of preference-driven behavioral control where linear scalarization collapses.

## Strengths

- **Novel similarity function with clear geometric motivation (Definition 4.1).** The proposed Ψ(p, v) = -½‖max_i(v_i/p_i)p - v‖² is not simply cosine similarity; it penalizes deviation from the "preference ray" scaled to dominate the current value vector. This design explicitly encourages the policy to improve underperforming objectives relative to the preference, which is both interpretable and principled. The paper also provides geometric intuition about its gradient behavior.

- **Consistent empirical advantage over alternative gradient manipulation methods within the PCRL framework.** On Fruit Tree (3–6 objectives), PreCo achieves the highest HV and CS across all settings (Table 1). On MO-Reacher (4 highly conflicting objectives), PreCo attains the best HV and preference-responsive state-coverage heatmaps, while LS/SDMGrad/CAGrad all produce uniform, preference-unresponsive coverage (Fig. 8). On MO-Hopper, PreCo achieves the best HV and only slightly lower CS than EPO, which the paper plausibly attributes to soft vs. hard similarity constraints.

- **Ablation via SDMGrad comparison is well-designed.** SDMGrad uses the same min-norm structure as PreCo but replaces the similarity gradient with linear scalarization. PreCo's consistent outperformance over SDMGrad directly attributes the benefit to the novel similarity function rather than the min-norm machinery itself.

- **General-purpose framework.** PCRL works with both value-based (TD3) and policy-based (PPO) RL algorithms and can incorporate multiple MOO methods (LS, EPO, CAGrad, SDMGrad) as plug-in components, demonstrating versatility beyond just PreCo.

- **Clear identification of the controllability problem.** Figure 1 provides illustrative counterexamples showing LS failures even on convex Pareto fronts, motivating why similarity-based optimization (not just scalarization) is necessary for preference control.

## Weaknesses

### Fatal
None.

### Major

- **The policy-level gradient computation chain is critically underspecified, threatening reproducibility.** The paper defines gradients with respect to the policy output π_p (size m×B) rather than parameters θ (size m×M), claims a computational advantage from this, and solves the min-norm problem at this "policy level." However, it never explains how the resulting policy-level direction d* is converted into a parameter update. The paper says only that "the gradient can be obtained by conventional RL methods, such as the policy gradient and the deterministic policy gradient" (line 88), but this describes computing ∇_{π_p}v̂^{π_p}, not the mapping from d* back to θ. For discrete-action PPO (used in Fruit Tree and MO-Reacher), the score-function gradient is naturally computed at the parameter level, and a policy-level Jacobian is not well-defined without additional machinery (e.g., reparameterization or explicit output differentiation). Without specifying how d* updates the policy network weights, the algorithm as described cannot be reliably implemented. This is the single most important weakness: the paper's claimed efficiency advantage (solving a smaller min-norm problem) may be real, but the mechanism is not explained.

- **Section 4 (Theoretical Analysis) does not deliver what the abstract and introduction promise.** The abstract claims "convergence and controllability are theoretically justified" and Section 4 is titled "Theoretical Analysis," yet the visible main text contains only Definition 4.1 and a sentence stating convergence will be analyzed. No theorem, formal convergence rate, statement of assumptions, or even a proof sketch appears in the main body. The conclusion (line 199) claims "a comprehensive convergence analysis for stochastic optimization with non-convex smooth objective functions," but this analysis is not present in the visible text. Even if full proofs reside in the appendix (stripped by the parser), a paper's main text should state its central theoretical claim as a formal result. As it stands, the paper promises a theoretical contribution that it does not substantiate in the body.

- **No quantitative results reported for MO-Ant.** Section 5.2 describes the environment and references a scatter plot (Fig. 5), but reports no HV or CS numbers. This is the only environment where quantitative metrics are missing, making the evaluation incomplete for this task.

### Minor

- **The hyperparameter λ in the PreCo update (Eq. 3) is never discussed or ablated.** λ controls the trade-off between the similarity gradient and the objective gradients. No value is reported, no sensitivity analysis is conducted, and the paper provides no guidance on how to set it. Given that λ directly modulates the strength of preference control, this is a notable omission.

- **The similarity function (Definition 4.1) uses a non-differentiable max operation, but the conclusion assumes smoothness.** The definition contains max_i(v_i/p_i), which produces subgradients (not gradients) and violates the "non-convex smooth objective functions" assumption invoked in the conclusion. The paper does not address how the non-smoothness affects the claimed convergence guarantees.

- **PreCo's CS is lower than EPO's on MO-Hopper (Fig. 6).** The authors attribute this to soft vs. hard constraints, which is reasonable, but this explanation is not tested (e.g., by varying the similarity gradient coefficient or directly comparing constraint formulations). The claim of "consistent outperformance" is thus qualified by at least one counter-example on the CS metric.

- **The paper does not fully explain why PreCo succeeds on MO-Reacher where EPO and CAGrad struggle with HV (both below random baseline).** The paper mentions "conflicting objective gradients" and "high variance" (line 191), but since EPO also uses a similarity-based objective, a deeper analysis of why PreCo's design handles this better would strengthen the paper.

### Trivial

- The notation Ψ is used in Section 3 before it is formally defined in Definition 4.1 (Section 4). While the paper previews it in Section 2, the definition appears after its use.
- 5 random seeds is modest; standard deviations are reported but no statistical significance tests are provided.
- Table 1 presents HV and CS for Fruit Tree in a combined "HV|CS" format that is slightly dense.

## Nice-to-Haves

- Comparing against full MORL algorithms (e.g., Envelope MO-Q-learning, parameterized Q-networks from Xu et al.) would strengthen the claim of outperforming "existing approaches," though the current comparison against EPO, CAGrad, SDMGrad, and LS within the PCRL framework already provides a reasonable controlled evaluation of gradient manipulation methods.
- An ablation systematically varying the number of objectives in a controlled synthetic setting (e.g., known Pareto front shape) would clarify when LS breaks down and why PreCo scales.
- Measuring gradient conflict directly (e.g., cosine similarity between objective gradients during training) could quantitatively support the explanation for PreCo's advantage on MO-Reacher.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The critic training is not explained"** (harsh critic, Section 3.1 note): REMOVED — The critic q_θ is trained via standard TD learning across all states, which is conventional for MORL and does not need restating. The paper's estimate v̂^{π_p} = E_{S0}[q_θ(S0, π_p(S0))] correctly computes the value under the initial-state distribution by definition.
- **"Figure 4 showing LS collapse is not a discovery"** : REMOVED — The paper is not claiming this as a discovery; it is providing an empirical demonstration of a known phenomenon in its specific setting to motivate the method.
- **"Appendix is not available for review"** : REMOVED per policy — the parser strips appendix sections from all papers; they exist in the original submission.
- **Strength Finder's claim of "theoretical convergence guarantees in the paper"** : REMOVED — The visible main text does not contain theorems or convergence rates; this strength conflicts with the verified weakness that Section 4 is incomplete. If the appendix contains the analysis, the main text still fails to state its central theoretical result.

## Novel Insights

Beyond the paper's own contributions, a notable observation emerges from comparing PreCo and EPO across environments. On MO-Hopper, EPO achieves higher CS but lower HV (hard constraint on similarity restricts Pareto exploration); on MO-Reacher, EPO's HV falls below random baseline while PreCo maintains high HV and CS. This pattern suggests that the soft-constraint formulation in PreCo (adding a similarity gradient to the min-norm combination) may be inherently more robust to high gradient conflict than the hard-constraint mode-switching in EPO, because PreCo's update always balances similarity pursuit with Pareto improvement rather than toggling between them. This design principle — additive regularization rather than conditional constraint enforcement — could generalize to other multi-objective settings beyond RL.

## Suggestions

1. **Specify the full gradient computation chain.** Provide pseudocode or a clear description of: (a) how ∇_{π_p}v̂^{π_p} is computed for each RL algorithm used (value-based, policy-based with score function, policy-based with reparameterization), (b) how d* from the min-norm problem is used to update the policy network parameters (e.g., via ∂π_p/∂θ or a separate loss), and (c) the complete training loop including critic learning.

2. **State the main theoretical result in the body.** Even if full proofs are deferred, Section 4 should contain a theorem statement with the convergence rate, key assumptions, and a sketch of the proof. This is essential to deliver on the promise made in the abstract.

3. **Report λ and include an ablation.** State the value used in experiments and provide a sensitivity study (e.g., HV and CS vs. λ) to guide practitioners and validate robustness.

4. **Report quantitative HV and CS for MO-Ant.** This completes the evaluation across all environments.

5. **Address the smoothness issue.** Either modify the similarity function to be smooth (e.g., replacing max with a smooth approximation like LogSumExp) or relax the smoothness assumption in the convergence analysis to handle subgradients, and explain why the analysis still holds with the non-differentiable max.

## Score and Decision

This paper addresses a genuine and underexplored problem — training a single policy for controllable multi-objective trade-offs — and presents a novel, well-motivated algorithm (PreCo) with empirical support across several environments. The MO-Reacher heatmaps and consistent HV improvements over strong baselines within the PCRL framework provide convincing evidence that the approach works. However, the paper has two significant gaps that prevent it from being publishable in its current form: (1) the algorithm's gradient computation chain is underspecified to the point where implementation is ambiguous, and (2) the promised theoretical analysis is absent from the main text. These are addressable in a major revision but are not trivial fixes. The paper is on the right track and the core ideas are solid, but it is not ready for acceptance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>