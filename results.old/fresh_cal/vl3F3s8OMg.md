Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper studies the role of Euclidean symmetry in model-based reinforcement learning. It defines *Geometric MDPs* (GMDPs) — MDPs with continuous group actions on state and action spaces — and shows that their linearized dynamics satisfy G-steerable kernel constraints, yielding principled parameter reduction. Motivated by this theory, the paper proposes an equivariant version of TD-MPC that enforces symmetry via G-equivariant/invariant networks for all learned components (dynamics, reward, value, policy, encoder) and a G-augmented sampling strategy (G-sample) to enforce equivariance in the MPPI planner. Empirical results on PointMass, Reacher, and MetaWorld tasks show that the equivariant method reaches good performance 2–3× faster than the non-equivariant baseline.

## Strengths

1. **Principled theoretical foundation.** Theorem 3 shows that linearizing a Geometric MDP yields matrix-valued functions \(A(p), B(p)\) that satisfy G-steerable kernel constraints, providing a clear theoretical rationale for parameter reduction. Theorem 4 extends this to the LQR feedback and value matrices. This connects geometric deep learning to continuous-control MDPs in a formally grounded way.

2. **Novel mechanism for equivariant sampling-based planning.** Proposition 5 identifies that vanilla MPPI is not G-equivariant and proposes a G-augmented sampling procedure (G-sample) that provably restores equivariance. This is a genuine extension beyond prior work that was limited to value-based planning on 2D discrete grids (Zhao et al., 2022b) or model-free equivariant RL.

3. **Clear empirical gains.** Figures 5 and 6 demonstrate that the equivariant version of TD-MPC reaches near-optimal performance 2–3× faster than the non-equivariant baseline across multiple tasks (2D PointMass, Reacher Easy/Hard, MetaWorld Reach, 3D multi-ball PointMass tasks) with matched parameter counts. These results support the claim that symmetry exploitation yields measurable sample-efficiency benefits.

4. **Comprehensive formalization.** Definition 1 (Geometric MDP) unifies prior work on symmetric MDPs under a common framework with continuous group actions, and Table 1 provides concrete examples connecting the abstract theory to specific tasks with explicit group actions, quotient spaces, and orbit dimensions.

## Weaknesses

### Fatal
None.

### Major

1. **Unquantified bridge between continuous theory and discrete implementation.**  
   The theoretical analysis (Theorems 3, 4) is developed for continuous symmetry groups and emphasizes "infinite" parameter reduction. However, the implementation uses finite subgroups (D₄, D₈, C₈, icosahedral, octahedral) — a standard practical choice acknowledged in the paper ("more stable and easier to implement"). But the paper never quantifies what parameter reduction is actually obtained with these *specific finite subgroups* compared to the continuous ideal. The concrete example in Section 3 (3D particle, 12 free parameters on each orbit) is for the continuous SO(3) case; it is unclear how this maps to the icosahedral (order 60) or octahedral (order 24) subgroups used in experiments. This gap weakens the connection between the theory's motivating promise and the actual implemented method. A table showing actual free-parameter counts for the equivariant vs. non-equivariant networks used would directly address this.

2. **Narrow experimental comparison.**  
   The only baseline in the main paper is the non-equivariant version of TD-MPC with matched parameter counts. While this is appropriate for isolating the effect of equivariance within the TD-MPC framework, the paper does not situate the reported gains against the broader literature (e.g., Dreamer, SAC, DDPG, or other model-based methods). The paper mentions a planning-free baseline (similar to DDPG) only in the appendix. Without broader context, it is difficult for a reader to assess whether "2–3× faster than non-equivariant TD-MPC" represents a major advance in absolute terms. Additionally, the claim that the baseline "may have been run with suboptimal settings" is speculative (the authors state they "mostly follow the original hyperparameters except for seed_steps"), but the paper would be strengthened by a sensitivity analysis or at least a statement about how baseline hyperparameters were selected.

3. **Evaluation scope lacks negative or partial-symmetry cases.**  
   All four task families (PointMass, Reacher, MetaWorld Reach, 3D multi-ball PointMass) have strong global Euclidean symmetry. The paper acknowledges in the conclusion that locomotion tasks "do not greatly benefit" from Euclidean symmetry, but does not include any such task as a negative case, nor any task where symmetry is partially broken (e.g., with obstacles, uneven terrain, or local coordinates). Including even one such task — even as a null result that the method does no worse than the baseline — would substantially strengthen the paper's claim that it understands *when* its method is and is not beneficial. As submitted, the evaluation tests only favorable cases.

### Minor

1. **Limited statistical rigor.**  
   Results are reported with only 5 random seeds. For the inherent noisiness of TD-MPC training curves, more seeds (e.g., 10) and explicit reporting of confidence intervals or individual runs would help establish that the observed gains are statistically significant. The figures appear to show mean curves with thin or absent shading, making it difficult to assess variance.

2. **Proposition 5 stated without proof or derivation.**  
   The claim that G-augmented sampling yields strict equivariance (even for \(K=1\)) is asserted but not derived. Since this is a key algorithmic component, a brief justification in the main paper would help the reader understand the conditions under which equivariance holds.

3. **Compact theoretical presentation.**  
   Several nontrivial claims in Section 3 (e.g., "if infinitesimal group actions on state-action space exists, the symmetry of the nonlinear GMDP is equivalent to G-steerable constraints of the linear dynamics") are stated without proof or sketch. While the paper's main contribution is algorithmic, a slightly expanded exposition of the key theoretical steps would improve accessibility.

### Trivial
None.

## Nice-to-Haves
- Quantify the actual parameter savings for the finite subgroups (D₄, D₈, icosahedral) used in experiments, e.g., a table showing free parameters in equivariant vs. non-equivariant dynamics and policy matrices.
- Include a partial-symmetry or negative task (e.g., PointMass with an obstacle or a locomotion task) to test the method's gracefulness under symmetry breaking.
- Report how the method's sensitivity to seed_steps compares to the baseline quantitatively.
- Soften the "first method" claim to acknowledge potential prior work on equivariant model-predictive control.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Missing ablation of G-sampling (Harsh Critic #3):** The critic asserts that the main paper "does not isolate the effect of G-sampling from the effect of equivariant networks" and that "the paper references an appendix section (F.3) for ablation studies, but that material was stripped." Per the meta-review rules, weaknesses about missing appendix content (stripped by the parser) are to be removed. The original submission includes these ablation studies in Sec F.3.
- **Criticism about √N justification:** The paper does justify the √N factor ("to keep the number of parameters roughly equal"). This is a reasonable approach.
- **Reproducibility nitpick about undisclosed hyperparameters:** The paper states it follows TD-MPC hyperparameters except seed_steps; this is sufficient for a research paper.
- **"The paper does not warrant the generality of the results":** Generic framing without concrete anchor to a specific claim.

## Novel Insights
None beyond the paper's own contributions. The combination of the Harsh Critic and Strength Finder reveal a paper that has genuine theoretical and algorithmic novelty, but whose empirical case is narrower than its framing suggests. The most striking tension is between the continuous-group theory (which promises infinite parameter reduction) and the discrete-subgroup implementation (where the actual reduction is finite and unquantified). This gap is not unique to this paper — it is endemic in geometric deep learning — but the paper would be substantially strengthened by explicitly measuring it.

## Suggestions
1. Add a table quantifying actual parameter counts (free parameters) for the equivariant and non-equivariant networks used in each experiment, together with the ratio of reduction. This would directly connect the theoretical framework (parameter reduction via steerable kernels) to the algorithm.
2. Include at least one task where the symmetry assumption is violated or partially broken (e.g., PointMass with a fixed obstacle, or a locomotion task) as a negative control. This would strengthen the paper's characterization of when the method is and is not useful.
3. Provide confidence intervals or individual-run plots for the main experimental results. With only 5 seeds, the reader needs more information to assess statistical significance.
4. Expand the theoretical exposition slightly in the main paper with a brief sketch of why Proposition 5 holds, and why the continuous-to-discrete transition is justified.

## Score and Decision

**Originality:** Good — the connection between steerable kernel constraints and linearized GMDPs is novel, and the G-augmented MPPI sampling strategy is a new contribution.  
**Importance of research question:** High — understanding when and why symmetry helps in model-based RL is a timely question.  
**Claims supported:** Partially — the theoretical claims are sound, but the empirical support is limited by narrow comparison and evaluation scope.  
**Soundness of experiments:** Adequate but improvable — matched parameter counts and multiple tasks are good practices, but more baselines, more seeds, and negative cases would strengthen.  
**Clarity of writing:** Good — the paper is clearly structured, though the theory section is compact.  
**Value to community:** Moderate — the theoretical framing and algorithm design are useful contributions, but the empirical evidence is not yet comprehensive enough to be a definitive reference.

The paper makes a genuine contribution: it provides a principled theoretical framework connecting geometric deep learning to continuous-control MDPs and proposes a novel equivariant sampling-based planning algorithm. The empirical results consistently show improvement over the direct baseline. However, the evaluation is narrow (single baseline, no negative cases, limited statistical reporting), and the connection between continuous-group theory and discrete-subgroup implementation is unquantified. These issues are addressable but, as submitted, prevent the paper from being fully convincing. The paper is between borderline and weak accept — leaning toward reject given current weaknesses, but could be a strong paper with the suggested additions.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>