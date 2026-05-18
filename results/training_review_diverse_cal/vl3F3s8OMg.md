Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper studies how Euclidean symmetry (rotations, reflections, translations) can benefit model-based reinforcement learning and planning. It defines "Geometric MDPs," shows that their linearized dynamics satisfy steerable kernel constraints leading to parameter reduction, and proposes an equivariant version of TD-MPC that uses G-steerable equivariant MLPs and a G-augmented action sampling strategy during MPPI planning. Experiments on 2D/3D point-mass, Reacher, and MetaWorld tasks show 2-3× faster learning compared to non-equivariant TD-MPC with similar parameter counts.

## Strengths

- **Novel theoretical framework linking MDP linearization to steerable kernel constraints**: Theorem 3 proves that the linearized dynamics matrices A(p) and B(p) of a Geometric MDP satisfy G-steerable kernel constraints, giving explicit parameter reduction (e.g., from 36 to 12 free parameters per orbit in a 3D PointMass). This provides a principled theoretical basis for understanding when and why symmetry benefits model-based RL, going beyond prior work on discrete grids.

- **Algorithmic extension of equivariance to sampling-based continuous control**: The paper extends equivariant RL from discrete grid-based planning (Zhao et al., 2022b) and model-free settings (van der Pol et al., 2020b; Wang et al., 2021) to continuous state/action spaces with sampling-based MPPI planning, using G-steerable equivariant MLPs and a G-augmented sampling strategy.

- **Empirical demonstration of sample-efficiency gains on symmetric tasks**: The equivariant method reaches near-optimal performance 2-3× faster than non-equivariant TD-MPC across multiple benchmarks (Reacher Hard, 3D PointMass with N=1,2,3 balls, MetaWorld Reach), tested with multiple discrete subgroups (D₄, D₈, C₈, Icosahedral, Octahedral) and 5 random seeds.

- **Honest discussion of task suitability**: The paper explicitly identifies when Euclidean symmetry does not help (e.g., locomotion tasks, kinematic chains with local coordinates), giving practitioners actionable guidance rather than overclaiming universality.

## Weaknesses

### Fatal
None.

### Major

1. **The equivariance guarantee for the planning procedure is proven only for a simplified case (K=1) that does not match the full algorithm.** Proposition 5 states that the G-augmented sampling procedure is G-equivariant only when K=1 (selecting a single best trajectory). The actual MPPI implementation in TD-MPC uses a soft-weighted combination of action sequences — a central element of the algorithm. The paper acknowledges this limitation explicitly (line 183: "the MPPI sample does not exactly preserve equivariance"), but the overall narrative still presents the algorithm as being "constructed to be equivariant" (line 21). The gap between the proven K=1 case and the practical soft-weighted implementation means the paper's primary algorithmic claim — an equivariant sampling-based planner — is not fully supported for the actual method used in experiments. An empirical study of whether this departure from exact equivariance materially affects performance (e.g., comparing K=1 planning against soft-weighted planning on the same tasks) would help, but is not provided.

2. **The experimental design does not isolate the source of improvement.** The comparison is equivariant TD-MPC vs. non-equivariant TD-MPC, but the equivariant version introduces two changes simultaneously: (a) G-equivariant network architectures, and (b) G-augmented action sampling during MPPI. The G-augmented sampling alone could explain observed improvements (effectively giving the planner access to transformed copies of trajectories — a form of test-time augmentation). The paper mentions ablation studies in the appendix (Sec F.3), but these are not part of the main results and their content is not described in the main paper. For the paper's central empirical claim, it is critical to distinguish whether gains come from architectural equivariance, planning-time augmentation, or their combination. Without this decomposition, one cannot tell whether the theoretical framing about steerable kernels (which relates to architectural equivariance) is actually explanatory of the results, or whether the method's success rests on a different mechanism entirely.

### Minor

3. **The connection between the linearization theory and the nonlinear algorithm is motivational but unvalidated.** Theorems 3-4 show that linearized dynamics and LQR solutions satisfy steerable kernel constraints. The algorithm, however, uses nonlinear equivariant MLPs and never linearizes the learned dynamics. The step from "the linearized system has steerable kernels" to "so we should build the nonlinear system with equivariant MLPs" is plausible but unsupported. The paper does not show that the learned equivariant dynamics network, when locally linearized, satisfies the predicted steerable kernel structure, nor does it compare the predicted parameter reduction against the reduction achieved in practice. The theory is presented as guidance, which is reasonable, but validating this connection would substantially strengthen the paper's narrative unity.

4. **The paper uses discretized subgroups (D₄, D₈, Icosahedral, Octahedral) for implementation, while the theoretical framing emphasizes continuous symmetry.** This is stated explicitly (line 214: "We use discretized subgroups... which are more stable and easier to implement"), but the disconnect remains. The theoretical benefits derived from continuous group actions (e.g., the "infinite reduction" claim, fiber bundle interpretations) do not directly apply to the finite subgroups used in practice. The paper would benefit from a clearer discussion of how the theoretical insights about continuous symmetry translate (or do not translate) to the discretized implementation.

### Trivial

- The paper's claim to be "the first method considering the importance of equivariance in sampling-based RL methods" (line 234) could be more carefully contextualized with respect to prior work on equivariant dynamics models and trajectory optimization.

## Nice-to-Haves

- An ablation comparing: (1) non-equivariant TD-MPC without augmentation, (2) non-equivariant TD-MPC with G-augmented sampling, (3) equivariant TD-MPC without augmentation, (4) equivariant TD-MPC with augmentation. This would cleanly isolate the source of improvement.
- A post-hoc check: compute the Jacobian of the learned equivariant dynamics model at various points and verify whether the resulting A and B matrices satisfy the steerable kernel constraints from Theorem 3, directly validating the theory.
- A data augmentation baseline (randomly rotating state-action pairs during training) to test whether the inductive bias of equivariant networks provides benefits beyond what augmentation alone achieves.

## Removed Points

- **"Infinite reduction" claim is imprecise / misleading** — REMOVED. The paper's claim about infinite reduction for continuous domains (line 14) is technically correct and non-trivial: on continuous state-action spaces, the unconstrained dynamics function is infinite-dimensional, while the steerable kernel-constrained space is finite-dimensional per orbit. This is distinct from the standard "equivariance reduces function class" property on discrete domains where both spaces are already finite-dimensional. The reviewer's comparison to discrete-group steerable kernels conflates finite-dimensionality of the representation space (which holds for any compact group) with the infinite-dimensionality of the function space on a continuous domain (which is specific to the continuous setting). The paper's claim is well-grounded.

- **Criticism that Theorem 2 uses "resembles" vaguely** — REMOVED. The paper explicitly states this extends prior results (Zhao et al., 2022b) from discrete groups to continuous groups. The word "resembles" is appropriate for an informal comparison; the formal claim is that value iteration on GMDPs is E(d)-equivariant, which is the substantive contribution.

- **Criticism about tasks being simple with modest results** — DOWNGRADED to trivial. The paper is transparent about scope and limitations. The 2-3× improvement in sample efficiency is practically meaningful for the task class studied (continuous control with global symmetry). The paper acknowledges locomotion tasks do not benefit.

## Novel Insights

The harsh critic's most valuable observation is the gap between the K=1 proven equivariance and the soft-weighted MPPI used in practice, and the strength finder's most useful framing is identifying the two distinct changes in the equivariant method (architecture + sampling augmentation). Neither reviewer fully explores an interesting tension: the paper's theory explains why *architectural* equivariance helps (parameter reduction in linearized dynamics), while the G-augmented sampling is a separate algorithmic fix for the *planning* procedure's lack of equivariance. These are addressing two different problems, and the empirical results conflate them. A deeper insight is that the G-augmented sampling could be viewed as a practical approximation to make the planning procedure approximately equivariant even when exact equivariance is not achievable due to the stochastic nature of MPPI — this reframes the contribution as "we make both the architecture and the planner approximately symmetry-aware" rather than achieving exact end-to-end equivariance.

## Suggestions

1. Add ablation experiments to the main paper distinguishing architectural equivariance from G-augmented sampling (the 2×2 design described in the nice-to-haves above). This would substantially strengthen the paper's claims about where the benefit comes from.
2. Include an empirical study comparing K=1 (exact equivariance) vs. soft-weighted MPPI (approximate) to show whether the departure from exact equivariance matters for final performance.
3. More explicitly state which components are proven equivariant (networks, K=1 planner) and which are only approximately equivariant (full soft-weighted planner) in a summary table or figure, so readers clearly understand the scope of the guarantees.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>