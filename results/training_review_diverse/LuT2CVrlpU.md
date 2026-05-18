Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the final review.

## Summary

This paper extends behavioral entropy (BE) to continuous spaces, derives k-NN estimators with theoretical guarantees (consistency, finite-sample bias/variance bounds), develops a practical RL reward for maximizing BE, and experimentally evaluates BE-generated datasets for offline RL against Rényi entropy (RE), Shannon entropy (SE), RND, and SMM baselines. The core empirical claim is that offline RL on BE-generated datasets achieves superior performance to SE/RND/SMM on all tasks and to RE on 80% of tasks, while using only 5% of the data and 20% of the training steps of prior work.

## Strengths

- **Principled theoretical extension of BE to continuous spaces**: Definition 3 provides a rigorous continuous analogue of discrete BE, and Theorems 1–2 provide consistency and finite-sample bias/variance guarantees for the k-NN estimator. This goes substantially beyond prior discrete-only BE work (Suresh et al., 2024).

- **Large-scale controlled experimental comparison**: The paper evaluates 17 datasets (8 BE, 5 RE, 2 SE, 1 RND, 1 SMM) across 2 environments (Walker, Quadruped), 5 downstream tasks, 3 offline RL algorithms (TD3, CQL, CRR), and 5 seeds — 1,275 trained policies in total. This sweep enables systematic comparison across methods.

- **Demonstrated stability advantage of BE over RE**: Figure 4 shows that offline RL performance on BE-generated datasets varies smoothly with α, while RE performance is highly unstable across q values. This is a specific, practically meaningful advantage over the prior RE-based approach.

- **Novel use of PHATE plots for RL trajectory visualization**: The paper is the first to apply PHATE (vs. t-SNE) to visualize RL trajectory data, providing clearer qualitative evidence of state-space coverage differences.

## Weaknesses

### Fatal

None.

### Major

1. **Selection bias in the central comparison (BE vs. RE).** The headline claim — "superior" performance on 80% of tasks over RE — compares the *best* BE parameter value (out of 8 α values) against the *best* RE parameter value (out of only 5 q values used in offline RL). BE gets 60% more parameter settings in this comparison. While the paper provides per-parameter results in Figure 4 that partially mitigate this, and while the paper justifies omitting q ∈ {2.0, 3.0, 5.0} due to observed poor performance, the central claim in the abstract and conclusion ("superior over RE") is based on a comparison where BE had more chances to find a lucky configuration. A comparison reporting average performance over parameters or using matched parameter counts would be more persuasive. *This does not invalidate the results (Figure 4 shows the advantage is real for many parameter combinations), but it weakens the force of the headline claim.*

2. **Missing direct comparison table for the data/sample-efficiency claim.** The paper states: "Despite these limitations, we achieved comparable performance to that achieved in Yarats et al. (2022), indicating that using BE-generated data for subsequent offline RL leads to significant improvements in both data- and sample-efficiency." This is a key contribution claim, yet no table directly compares the paper's numbers to ExORL's published results for the same environments and tasks. Without side-by-side numbers, the efficiency advantage cannot be verified by the reader. This is an omission that should be straightforward to fix.

3. **Limited experimental generality.** All experiments use only two MuJoCo environments (Walker, Quadruped) and a single pretraining backbone (APT). The paper acknowledges this as a limitation, but the strength of the claims ("superior performance," "stabler objective") relative to this narrow scope is mismatched. APT itself is a nearest-neighbor-based method designed for SE/RE rewards, raising the possibility that observed benefits are partly artifacts of this specific framework. At minimum, the conclusions should be scoped more conservatively or a second environment family/backbone should be demonstrated.

### Minor

1. **Gap between theory and implemented reward.** The theoretical guarantees (Theorems 1–2) apply to the importance-sampling-corrected estimator in Equation 13, but the practical reward (Equation 24) involves several unquantified approximations: discarding the D_{k,n} term, setting dimension d=1 "for numerical stability," and introducing an additive constant c inside the logarithm. The paper does not empirically validate how well the learned policy actually maximizes the BE objective defined in Equation 16. That said, this same type of approximation chain is standard in the prior work the paper builds on (Liu & Abbeel, 2021; Yarats et al., 2021; Yuan et al., 2022), so this is a weakness shared with the field rather than unique to this paper.

2. **Undisclosed hyperparameters.** The specific k value used in the k-NN estimator and the constant c in Equation 24 are not reported. These directly affect the reward signal and are essential for reproducibility.

3. **No quantitative coverage metrics.** The PHATE and t-SNE visualizations are offered as evidence of "wider variety of coverage," but no numerical metrics (e.g., state coverage ratio, discretized entropy of visitation histograms, nearest-neighbor distance statistics) are provided to support this claim objectively.

### Trivial

- The paper's claim that BE yields "superior" performance "over RE on 80% of tasks" (abstract) is contradicted by the later statement that BE beats RE on 4/5 tasks (80%), which is consistent — but the phrasing could create confusion with the 13/15 task-algorithm combination result reported on page 8.
- Theorem 2's presentation has formatting issues in the extracted text (though these are likely parser artifacts).

## Nice-to-Haves

- A small-scale validation experiment (e.g., in a grid world) comparing the true BE of the learned policy's state occupancy (computed via discretization) against the proxy reward's predictions would bridge the theory-practice gap.
- Reporting average (not just best) performance over parameter values for BE vs. RE would address the selection-bias concern.
- An additional environment (e.g., DMControl's Humanoid or a different locomotion task) would strengthen generality claims.

## Removed Points

- **"Theorem 2 is garbled / ξ never defined"**: The formatting issues are parser artifacts, and ξ is likely defined in the appendix (which was stripped). Removed per formatting/appendix rules.
- **"PHATE/t-SNE not causally linked to performance"**: These visualizations are qualitative support, not causal evidence; the quantitative evidence is in Table 1 and Figure 4. The criticism overreaches what the paper claims. Removed.
- **"No MSE bound in Theorem 2"**: Separate bias and variance bounds are a standard technical approach; demanding MSE specifically is a taste preference. Removed.
- **"Single seed runs" / other reproducibility nitpicks**: The paper uses 5 seeds throughout, so this does not apply.

## Novel Insights

The reviews surface an interesting tension: the paper's theoretical contribution (continuous BE + k-NN estimation guarantees) is its most novel element, yet the experimental part — which makes the strongest claims — is evaluated against a standard where the same approximation-theory gap exists in prior work (RE, SE). None of the reviewers questioned whether BE itself is a worthwhile generalization; the debate is entirely about how convincingly the empirical advantage is demonstrated. This suggests the core idea is sound but needs a cleaner experimental design to substantiate the applied claims.

## Suggestions

1. **Add a direct comparison table** with ExORL's published numbers for the same environments/tasks at the same evaluation points. This is essential to substantiate the data-efficiency claim.
2. **Report average performance** over BE and RE parameter values (not just best-over-parameters) in addition to the current presentation, or at minimum include a statistical test comparing the two distributions.
3. **Disclose all hyperparameters**: the k value for k-NN and the constant c in Eq. 24.
4. **Add a second pretraining backbone** (e.g., directly optimizing the BE proxy reward with SAC/PPO without APT) for at least one environment to show the effect is not specific to APT.

## Score and Decision

The paper makes a novel contribution (continuous BE + estimators) and the core experimental results are suggestive. However, the two major weaknesses — (1) asymmetric parameter counts in the best-over-parameters comparison and (2) the unverifiable efficiency claim — meaningfully undermine the paper's strongest advertised conclusions. The work is a solid foundation but needs revision before the empirical claims can be accepted at face value.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>