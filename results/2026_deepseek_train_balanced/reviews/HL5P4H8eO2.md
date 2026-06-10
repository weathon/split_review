## Summary

DiffTOP proposes using differentiable trajectory optimization (via the Theseus library) as a policy class, where the cost and dynamics functions are learned neural networks. The method is applied to both model-based RL (building on TD-MPC, adding a policy gradient term backpropagated through trajectory optimization) and imitation learning (learning a cost function such that test-time optimization yields actions matching expert demonstrations). Experiments span 15 RL tasks (DeepMind Control Suite) and 13 IL tasks (Robomimic, Push-T, ManiSkill).

## Strengths

- **Consistent IL improvements across diverse tasks**: DiffTOP+Diffusion Policy achieves the highest success rates on all 4 Robomimic tasks, and DiffTOP+BC consistently outperforms BC and BC+Residual on all 9 ManiSkill tasks (Tables 1-2). The improvement holds across two base policy classes (BC-RNN and Diffusion Policy), demonstrating the method's robustness as a refinement strategy.

- **Action refinement via trajectory optimization outperforms residual learning**: Controlled comparisons in both Robomimic and ManiSkill show that DiffTOP's test-time trajectory optimization consistently beats residual refinement on the same base policies, providing clean evidence for the relative value of the approach.

- **Training stability advantage over EBM-based implicit policies (IBC)**: The paper directly benchmarks IBC+Diffusion Policy alongside DiffTOP+Diffusion Policy (Table 1). IBC+Diffusion deteriorates the base policy on several tasks (e.g., ToolHang), while DiffTOP consistently improves it. This provides concrete evidence that differentiable trajectory optimization offers a more stable training procedure than the InfoNCE-based approach used by Florence et al. (2022).

- **Multimodal action capture with visual evidence**: Figure 5 shows that with a CVAE, different latent samples produce distinct objective function landscapes, yielding different optimized actions from the same state. This directly supports the claim that DiffTOP can model multimodal action distributions — a known challenge for MSE-based methods.

- **Clean integration of differentiable optimization at scale**: Using Theseus to backpropagate through Levenberg-Marquardt optimization with high-dimensional image and point cloud inputs is non-trivial, and the paper demonstrates it works in practice.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed "objective mismatch" framing contradicted by the paper's own ablation**: The paper repeatedly claims DiffTOP "addresses the objective mismatch issue" because it "directly maximizes task performance" by differentiating the policy gradient loss through trajectory optimization (abstract, Sections 1, 4.1, 6). However, the actual objective (Eq. 6) retains the full set of TD-MPC surrogate losses (reward prediction MSE, value TD-error, latent state consistency), and the ablation (Figure 4) shows that **removing the reward prediction loss causes DiffTOP to completely fail**. This is not a minor degradation — it is complete collapse. If the method genuinely learned dynamics to maximize task performance through the policy gradient pathway alone, removing a surrogate loss should degrade but not destroy performance. The paper's own comment ("These shows the necessity of using all the loss terms") confirms the surrogates are the backbone, not optional auxiliaries. The contribution is better described as **TD-MPC augmented with a differentiable planning gradient** — real and useful, but not a solution to objective mismatch. The paper needs honest reframing.

### Minor

- **No tabulated numerical results for RL experiments**: Figure 3 shows only learning curves. No table of final returns with standard deviations per task is provided. Given the paper claims state-of-the-art results across 15 tasks, this omission prevents readers from verifying the aggregate claim or assessing statistical significance, especially since individual-task error bars often overlap.

- **Framing of the Dreamer-v3 comparison is internally inconsistent**: The paper states DiffTOP "outperforms all compared baselines" (line 159) but then acknowledges it "achieves similar final performance" to Dreamer-v3 (line 159). The aggregate advantage is driven by faster learning, not higher asymptotic returns. These are different claims that should be distinguished. Faster learning is valuable, but conflating it with higher final performance is misleading.

- **No limitations section or discussion**: The paper does not discuss computational cost per step, sensitivity to planning horizon H, risk of local optima in Levenberg-Marquardt, or failure modes. This is a standard expectation for a method paper at a top venue.

- **Narrow baseline set for ManiSkill IL**: Table 2 compares DiffTOP+BC only against BC and BC+Residual. No diffusion-based or other recent IL methods are included, making the "state-of-the-art" claim on these tasks difficult to evaluate.

- **Incomplete RL ablation**: The ablation (Figure 4) removes one component at a time but never tests the most informative condition: training with **only** the policy gradient loss (removing all TD-MPC terms). Since the central claimed advantage is direct task-performance optimization, the condition without any surrogates is crucial.

### Trivial

- **Inconsistent notation for dynamics constraints**: Section 4.2 states Theseus does not support constraints, so dynamics are unrolled into the objective. However, Eq. 7 (IL formulation) writes "s.t. z_{t+1}=d_θ(z_t, a_t)" as an explicit constraint without clarifying that it too is unrolled in the same way. The notation is misleading.

## Nice-to-Haves

- Analysis of what the learned cost and dynamics functions capture (e.g., visualization or comparison to ground-truth dynamics)
- Wall-clock training and inference time comparisons against baselines
- Ablation on planning horizon H and number of Levenberg-Marquardt iterations

## Removed Points

- **Controller mismatch in Robomimic IL**: The harsh critic claimed evaluating Diffusion Policy with a velocity controller is unfair. The paper states ALL methods use the same Robomimic default velocity controller (lines 181, 191). The comparison is controlled and fair across methods. The disclosure about the Diffusion Policy's original-paper performance is just background context. REMOVED: criticism based on a misunderstanding of a controlled experiment.
- **IBC+Diffusion as "incompatible grafting"**: The critic argued IBC was not designed for action initialization. The paper is transparent about what IBC+Diffusion means and uses it as a controlled comparison to demonstrate DiffTOP's training procedure advantage, not as a primary baseline claim. This is valid ablation-style evidence. REMOVED: criticism overstates the issue.
- **Other removed**: Pure formatting/style nitpicks, missing related works concerns, and reproducibility doubts about cited entities — all removed per hard rules.

## Novel Insights

Beyond the paper's own contributions, the most informative observation from the review is the tension between the claimed RL framing and the empirical evidence. DiffTOP's genuine contribution — making trajectory optimization differentiable and using the gradient to augment model-based RL training — is obscured by the "addresses objective mismatch" narrative, which sets up a standard the method does not meet. The paper would be stronger if it presented DiffTOP as what it empirically is: a practical technique that combines surrogate objectives with a task-performance gradient pathway, where the surrogates remain essential. The IL contribution is cleaner and better supported; the RL half needs honest reframing.

## Suggestions

1. **Reframe the RL narrative**: Replace "addresses objective mismatch" throughout with an accurate description (e.g., "augments TD-MPC with a differentiable planning gradient that provides an additional task-performance training signal").
2. **Add a numerical results table** for all 15 RL tasks with final returns, standard deviations, and number of seeds.
3. **Add a limitations section** covering computational cost, horizon sensitivity, local optima risk, and when the method might fail.
4. **Run the missing ablation**: train with *only* the policy gradient loss (removing all TD-MPC surrogates) to directly test the "direct task-performance optimization" claim.
5. **Add stronger ManiSkill baselines** (e.g., diffusion-based methods) to substantiate the SOTA claim on those tasks.

## Score and Decision

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>