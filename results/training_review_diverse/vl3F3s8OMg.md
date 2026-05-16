Now I have a thorough understanding of the paper and the reviews. Let me synthesize the final review.

## Summary

This paper studies reinforcement learning and planning under Euclidean symmetry. It introduces Geometric MDPs (GMDPs) — MDPs where state and action spaces carry continuous group actions from the Euclidean group. The paper shows that linearized dynamics of GMDPs satisfy $G$-steerable kernel constraints, yielding a clean parameter-count reduction analysis (e.g., a $6\times6$ matrix reduced to 12 free parameters for 3D PointMass). Guided by this theory, the paper proposes an equivariant version of TD-MPC that uses $G$-steerable equivariant MLPs for all learned components and a $G$-augmented action sampling strategy to make the MPPI-based planner equivariant. Empirical results on several continuous-control tasks (2D PointMass, Reacher, MetaWorld Reach, 3D PointMass variants) show that the equivariant version achieves 2–3× sample-efficiency gains over non-equivariant TD-MPC with controlled parameter counts.

## Strengths

- **First equivariant sampling-based planning algorithm for continuous state/action spaces.** The paper extends prior work on discrete-group value-based planning (Zhao et al., 2022b) and model-free equivariant RL to continuous spaces with sampling-based MPPI planning. This is a genuine algorithmic contribution.

- **Clear theoretical link between continuous MDP symmetry and steerable kernel parameterization.** Theorem 3 shows that linearized dynamics of GMDPs satisfy $G$-steerable kernel constraints (Equation 5), providing a principled, quantitative connection to equivariant ML theory that yields concrete parameter-reduction estimates.

- **Unified formalism for symmetric MDPs.** Definition 1 (Geometric MDP) subsumes prior discrete and continuous symmetric MDP models under a single formalism, clarifying that continuous $G$-action is the key requirement for the theoretical benefits.

- **Consistent empirical sample-efficiency gains across multiple tasks.** The equivariant TD-MPC reaches near-optimal performance 2–3× faster on 5+ tasks spanning different symmetry groups ($D_4$, $D_8$, $C_8$, Icosahedral, Octahedral). The result that gains hold across different discrete subgroups strengthens the claim.

- **Demonstrated robustness to hyperparameter sensitivity.** The paper notes that TD-MPC is sensitive to the `seed_steps` hyperparameter, while the equivariant version is more robust — a practical benefit that goes beyond sample efficiency.

## Weaknesses

### Fatal
None.

### Major

- **The MPPI equivariance proof covers only the K=1 (argmax) case, not the full weighted-average procedure.** Proposition 5 is stated for $K=1$ ("Assuming we only select the best trajectory"). However, standard MPPI (as used in TD-MPC) selects actions via importance-weighted averaging over all sampled trajectories, not argmax over top-K. The paper never analyzes whether the $G$-augmented sampling strategy remains equivariant under the weighted-average action selection. Without this analysis, the core algorithmic claim — that the full planning procedure is equivariant — is not fully supported for the actual multi-trajectory mechanism. This is the most significant gap in the paper. *(Note: the authors acknowledge the $K=1$ simplification, and extending the reasoning to weighted averaging is conceptually straightforward if returns are invariant and the sampling distribution is equivariant, but the paper must provide this analysis.)*

- **Missing critical baselines.** The empirical evaluation compares only against non-equivariant TD-MPC. Two missing comparisons weaken the attribution of gains to the equivariant architecture: (1) **Data augmentation** (e.g., applying random symmetry transformations to replayed states during training) is a simpler, complementary approach to exploiting symmetry. Without this baseline, it is unclear whether the architectural equivariance matters or merely the increased data diversity from the group action. (2) Prior equivariant RL methods adapted to continuous control (e.g., van der Pol et al., 2020b's equivariant policy networks) are not compared.

- **Statistical reporting is insufficient.** Results are shown as mean curves across only 5 seeds with no error bars, confidence intervals, or measures of variance. Given the known high variance of TD-MPC across seeds, it is impossible to assess whether the reported 2–3× speedups are statistically significant. This is particularly important because some gains (e.g., 2D PointMass) appear small.

### Minor

- **The parameter count matching method is described but not validated.** The paper divides hidden dimensions by $\sqrt{N}$ to keep parameters "roughly equal" but reports no actual parameter counts. The reader cannot verify the match. Furthermore, equivariant layers have structured sparsity that interacts differently with optimization than dense layers, so parameter-count matching alone does not fully isolate the equivariance effect. Reporting actual parameter counts per network would be straightforward and informative.

- **Limited discussion of discrete vs. continuous group approximation.** The theory assumes continuous $G$-action (Section 2.1), but the implementation uses finite discretized subgroups ($D_4$, $D_8$, Icosahedral, Octahedral). The paper acknowledges this ("We use discretized subgroups... which are more stable and easier to implement") but does not discuss the approximation error: e.g., $D_8$ guarantees equivariance only for $45^\circ$ rotations. The mismatch between the continuous theory and the discrete implementation should be discussed as a limitation, especially since the theoretical parameter reduction is derived for continuous groups.

- **The theory-algorithm connection is motivational, not operationalized.** The theory shows parameter reduction for *linearized* dynamics, while the algorithm uses *nonlinear* $G$-steerable MLPs. The paper does not test whether the predicted linearized parameter reduction correlates with empirical sample-efficiency gains, nor does it measure how well the learned nonlinear dynamics satisfy the steerable kernel constraints in practice. This does not invalidate the algorithm (equivariant networks are standard tools), but the claim that the theory "guides" the algorithm is softer than the paper suggests.

- **Reproducibility details for escnn representations are not specified.** The paper does not state which group representations ($\rho_S$, $\rho_A$, $\rho_Z$) are used for each network component, how many channels per irrep, or how the latent representation type is chosen. These details are needed for exact reproduction.

### Trivial

- None.

## Nice-to-Haves

- A negative control experiment on a task where symmetry is deliberately broken (e.g., by obstacles or non-symmetric rewards) would strengthen the causal claim that gains come from leveraging symmetry rather than from some other property of equivariant networks.
- Wall-clock training time comparison would help assess the practical trade-off, since equivariant networks can be slower due to structured operations.
- Extending the Proposition 5 analysis to the weighted-average case (as discussed in the major weakness above).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Theorem 1 and 2 are stated without proof and the paper provides no sketch."* — Proofs exist in the appendix, which the parser strips. A proof sketch in the main text would be nice but this is not a missing content issue.
- *"The derivation of steerable kernel constraints... is not shown. A reader unfamiliar with steerable kernels would not see why this follows."* — The paper states the constraints explicitly (Equation 5). The derivation from the equivariance condition is written in the text. This criticism overstates the gap for a reader familiar with the steerable kernel literature.
- *"The theory predicts parameter reduction for continuous groups, but the algorithm uses discrete subgroups — the paper should acknowledge this mismatch."* — The paper *does* acknowledge this (Section 5: "We use discretized subgroups... which are more stable and easier to implement"). The criticism is partially addressed already. I have retained a softened version in Minor.
- *"The tasks are either very simple or custom 3D extensions designed to be highly symmetric... The paper should justify that these modifications do not break the original task's structure."* — The tasks are appropriate for testing the paper's claims about Euclidean symmetry. Locomotion tasks are explicitly noted as not benefiting. The modifications to MetaWorld (centering at origin) are described. This criticism overreaches into scope-creep territory.
- *"The paper does not provide its MDP specification (state/action space dimensions, reward function, transition noise)"* — These details likely appear in the appendix (stripped). The main text provides a reasonable description of each task.
- *"The paper should discuss how the discrete subgroup approximation determines the resolution of equivariance."* — Partially addressed; the paper notes that higher-order groups plateau in performance. I have retained a softened version.
- *"The paper should discuss limitations of discrete subgroups for continuous symmetry."* — The paper does mention using discretized subgroups and why. The softened version is retained in Minor.

## Novel Insights

The most interesting insight from the review is that the $G$-augmented sampling strategy (augmenting the sampled action set with group-transformed copies) provides a clean way to enforce equivariance in sampling-based planners even when the base action distribution is not state-conditioned. This decouples the equivariance requirement from the sampling distribution itself, which is a nontrivial design contribution. However, this insight is already presented in the paper; the reviews surface that the $K>1$ extension is needed to fully nail it.

## Suggestions

1. **Extend the MPPI equivariance analysis** to the full weighted-average case. Argue that if (a) each trajectory's return is $G$-invariant (which follows from the $G$-invariant reward and $G$-equivariant dynamics), (b) the $G$-augmented sampling produces a trajectory set that is closed under group transformations, and (c) the importance weights (softmax of returns) are invariant under simultaneous transformation of all trajectories, then the weighted-average action is $G$-equivariant. Provide this reasoning or a formal proof.
2. **Add a data-augmentation baseline** (random symmetry transforms applied to replayed data) to distinguish architectural equivariance from invariance induction via training data.
3. **Report actual parameter counts** for each network in the main text or appendix to verify the $\sqrt{N}$ matching strategy.
4. **Add error bars** (standard error over seeds or bootstrapped confidence intervals) to all result figures.
5. **Enumerate the specific escnn representations** used for the encoder, dynamics, reward, value, and policy networks (input/output representation types, channel counts per irrep) in the main paper.
6. **Explicitly discuss** the approximation gap between the continuous-group theory and the discrete-subgroup implementation, noting that equivariance only holds for the discretized rotations.

## Score and Decision

The paper makes a genuine contribution: it is the first to combine equivariant neural networks with sampling-based model-based RL in continuous spaces, provides useful theoretical motivation, and demonstrates consistent 2–3× sample efficiency gains. The weaknesses are real but manageable: the MPPI proof gap is the most significant, but the extension is conceptually straightforward; the missing baselines and statistical rigor are addressable without altering the core contribution. The paper would be strengthened considerably by addressing the major issues above, but even as-is, the contribution is clear and the results are practically meaningful.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>