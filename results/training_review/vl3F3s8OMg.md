Now I have a thorough understanding of the paper and all the review claims. Let me write the consolidated final review.

## Summary

This paper studies whether Euclidean symmetry (rotations, reflections, translations) can improve reinforcement learning and planning. It defines "Geometric MDPs" — MDPs with continuous group actions on state-action spaces — and shows their linearized dynamics satisfy G-steerable kernel constraints, theoretically reducing parameter counts. The paper then proposes an equivariant version of TD-MPC that enforces symmetry in all learned components (encoder, dynamics, reward, value, policy networks) and introduces a G-augmented sampling strategy for the MPPI planner. Empirical results on 2D and 3D continuous control tasks (PointMass, Reacher, MetaWorld, custom 3D N-ball tasks) show 2–3× faster learning compared to the non-equivariant baseline.

## Strengths

- **Novel formal framework connecting continuous-symmetry MDPs to steerable kernel constraints.** Theorem 3 shows that linearized dynamics of Geometric MDPs satisfy G-steerable kernel constraints, extending prior discrete-group results (Zhao et al., 2022b) to continuous groups. This provides a principled way to predict parameter reduction (e.g., the 6×6 matrix in 3D PointMass reduces to 12 free parameters per orbit) and offers theoretical grounding for why equivariance can improve sample efficiency.

- **Consistent empirical gains across diverse control tasks.** Figures 5 and 6 show that the equivariant algorithm achieves 2–3× faster learning (reward vs. environment steps) on 2D PointMass, Reacher (easy and hard), MetaWorld Reach, and several 3D N-ball PointMass tasks. Improvements hold across different symmetry groups (D4, D8, C8, Icosahedral, Octahedral) with multiple random seeds, demonstrating generality.

- **Extension of equivariant methods to sampling-based planning with continuous state/action spaces.** Prior work focused on value-based planning on discrete 2D grids (Zhao et al., 2022b) or model-free RL (van der Pol et al., 2020b; Wang et al., 2021). This paper adapts equivariant architectures to the MPPI-based continuous-control setting and identifies — and proposes a fix for — the non-equivariance of stochastic sampling in MPC.

- **Controlled experimental setup.** The paper divides hidden dimensions by √N (where N is group order) to roughly equalize parameter counts between equivariant and non-equivariant versions, and mentions ablation studies in the appendix (Sec. F.3) that disable/enable individual equivariant components.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The analysis of planning equivariance is limited to a simplified case (K=1) that does not fully match the implemented algorithm.** Proposition 5 proves equivariance only for best-trajectory selection (K=1) with a single-step simplification, but the actual MPPI procedure used in TD-MPC involves sampling multi-step trajectories and returns a control sequence via a more complex selection (top-k or weighted averaging). The paper correctly identifies that standard MPPI sampling is not equivariant and proposes G-augmented sampling as a fix, but does not analyze whether the full multi-step, top-k (or weighted) procedure preserves equivariance. This leaves a gap between the theoretical claim of an "equivariant planning algorithm" and what is formally established. (The extension to weighted averaging with invariant return weights is natural due to linearity of the group action, but the paper does not make this argument, and the multi-horizon case adds further complexity.)

- **No comparison against data augmentation baselines.** A natural competing hypothesis for the observed gains is that data augmentation (randomly rotating states/actions during training, as in RAD or DrQ) provides similar or better sample efficiency. Such a baseline would directly test whether explicit equivariant architectures are necessary or merely helpful. Without it, the paper cannot fully attribute improvements to the equivariance mechanism over a simpler symmetry-enforcing technique.

- **The claim of being "the first method considering the importance of equivariance in sampling-based RL methods" is not well-situated relative to cited prior work.** Park et al. (2022) is cited as studying "equivariance of the transition model in sampling-based approaches to machine learning," and the scope of overlap is not clarified. The contribution is still solid (extending to the MPPI planning loop with G-augmented sampling), but the "first" claim should be more carefully scoped.

- **No parameter count table.** The paper states it divides hidden dimensions by √N to keep parameters "roughly equal" but reports no actual parameter counts. A table comparing trainable parameters for each component (encoder, dynamics, value, policy) in equivariant vs. non-equivariant versions would strengthen the claim of fair comparison.

- **No discussion of computational overhead.** Both the equivariant networks (via escnn) and the G-augmented sampling (multiplying the action set by |G|) incur computational costs. For large groups (Icosahedral: order 60), this could be substantial. The paper does not report wall-clock time or discuss this trade-off.

### Trivial

- The paper mentions that Table 1 parameter reduction numbers (e.g., "infinite" for continuous tasks) are stated without a formal derivation linking the steerable kernel basis dimension to specific tasks. The intuition is clear, but a brief calculation or reference would help.
- The 3D PointMass example's parameter count (12 per orbit = 4×3) is described somewhat unclearly ("2×2 blocks of 3×3 sub-matrices"); the derivation could be expanded for clarity.
- No qualitative demonstration that rotating an input state produces a correspondingly rotated action sequence (as suggested by Figure 1).

## Nice-to-Haves

- Ablation comparing equivariant networks + G-augmented sampling vs. equivariant networks + standard (non-augmented) MPPI sampling, to quantify the contribution of the planning modification versus the architecture alone.
- Application to tasks with continuous SO(2) or SO(3) symmetry via steerable filters (rather than finite subgroups), to assess whether the theoretically predicted infinite parameter reduction translates to further practical gains.
- Qualitative validation (e.g., rotate input state, show planned action rotates accordingly) to directly verify the equivariance claim of Figure 1.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"Section 3.2 theory is disconnected from algorithm design — steerable kernel parameterization is never used."* — Removed because this overstates the issue. The theory motivates why equivariance yields parameter reduction, and the algorithm implements G-steerable equivariant MLPs (via escnn), which directly encode the same steerable kernel constraints. This is a standard theory-to-practice flow; the theory does not need to be mechanically applied.

2. *"Theorem 3 is just 'derivative of equivariant map is equivariant.'"* — Removed because the contribution is in the *interpretation*: connecting this mathematical fact to steerable kernel constraints and using it to predict parameter reduction for GMDPs, which is novel framing even if the underlying theorem is standard.

3. *"Table 1 parameter reduction numbers lack derivation."* — Removed as the paper provides the key intuition and references (Lang & Weiler, 2020b). A full formal derivation would be disproportionate for a table.

4. *"The equal-parameter comparison (divide by √N) is nonstandard."* — Removed because this is actually a standard method for fair comparison between equivariant and non-equivariant networks, widely used in the equivariance literature.

5. *"100k steps may not be enough for baseline to converge."* — Removed because the paper's contribution is precisely that equivariance accelerates learning; if the baseline hasn't converged in the same budget, that reinforces the paper's point.

6. *"The '2x or 3x faster' claim is visual inspection, not a defined metric."* — Removed because this is common practice in RL papers and the improvement is clearly visible in the learning curves.

7. *Several formatting/style nitpicks and claims about missing appendices* — Removed per instructions.

8. *Strength Finder's claim that Proposition 5 "solves the key technical challenge"* — Modified/wrapped into the actual (limited) scope of the proposition rather than kept as an unqualified strength.

## Novel Insights

The most interesting observation emerging from this review is the tension between the paper's theoretical framing (equivariance of the planning procedure) and what the empirical results actually demonstrate. The G-augmented sampling strategy may be less critical than the equivariant networks themselves for the observed gains — the paper's own analysis admits the sampling is not equivariant without augmentation, but does not disentangle the two sources of improvement. This suggests a potentially simpler story: that making the learned model components (encoder, dynamics, value, policy) equivariant is what drives sample efficiency, while the G-augmented sampling is a relatively minor correction. If this is the case, the paper's core contribution is robust even without a complete analysis of planning equivariance, and the "equivariant planning algorithm" framing could be de-emphasized in favor of the stronger empirical finding that equivariant model-based RL architecture yields substantial gains.

## Suggestions

1. Provide a full analysis (or at least a clear argument) that the multi-step, top-k / weighted MPPI procedure with G-augmented sampling preserves equivariance, or explicitly state that the equivariance guarantee applies to the action sampling and return computation but not to the full action-selection pipeline.
2. Add a data augmentation baseline to the experiments to isolate the benefit of explicit equivariant architectures over symmetry-agnostic data augmentation.
3. Report actual parameter counts in a table, and include wall-clock time comparisons to quantify computational overhead.
4. Soften the "first method" claim regarding sampling-based RL methods, given the existence of related work (Park et al., 2022).

## Score and Decision

This paper makes a solid empirical contribution: it is the first to systematically adapt equivariant architectures to a modern sampling-based model-based RL algorithm (TD-MPC + MPPI) and demonstrates clear and consistent sample-efficiency gains. The theoretical framework connecting GMDPs to steerable kernels, while building on known mathematics, provides useful conceptual grounding. The main weaknesses are incomplete analysis of the planning equivariance (Proposition 5 covers only K=1) and the absence of a data augmentation baseline — both addressable but leaving some claims less well-supported than they could be. The core empirical finding — that equivariant networks in model-based RL yield 2–3× faster learning — is convincing and valuable. I recommend acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>