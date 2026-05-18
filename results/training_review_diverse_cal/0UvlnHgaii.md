Now I have a thorough understanding of the paper and all the reviewers' claims. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

Here is my consolidated review:

## Summary

This paper proposes Exploratory Inverse Constraint Learning (ExICL), which recovers a diverse set of feasible constraints from offline expert demonstrations rather than trying to identify a single, potentially non-identifiable constraint. The key technical contributions are (1) a Generative Diffusion Verifier (GDV) that uses guided denoising to efficiently assess whether a candidate constraint reproduces expert behavior without expensive policy updates, and (2) a contrastive exploration mechanism that actively diversifies the discovered constraint set. The paper evaluates ExICL across PointMaze navigation and MuJoCo locomotion tasks, showing improved reward and safety metrics over several ICL and IL baselines.

## Strengths

- **Novel problem formulation.** The paper formalizes the "feasible constraint set" problem (Definition 3.1), shifting ICL from recovering a single constraint to recovering a diverse set of constraints that all explain expert optimality. This directly addresses the well-known ill-posedness of ICL and is a principled conceptual advance over prior single-constraint approaches.

- **GDV enables parameter-free verification.** Section 4.1 derives a guided denoising process (Eq. 10) using the Lagrangian formulation of constrained RL to generate trajectories under a candidate constraint. Because this operates via guided diffusion rather than iterative policy updates, it is conceptually more efficient than the bi-level optimization used by prior ICL methods. Figure 6 provides empirical evidence of sample-efficiency gains over baselines.

- **The exploration mechanism demonstrably produces diverse constraints.** Section 4.3 introduces a contrastive regularization term (Eq. 12–13) based on InfoNCE loss. Figure 4 shows that ExICL yields substantially wider variance in predicted costs across trajectories compared to random-noise and random-initialization baselines, confirming that the mechanism generates distinct constraint candidates.

- **Strong empirical results across multiple domains.** Tables 1 and 2 show ExICL consistently achieves higher cumulative rewards and lower cumulative costs than baselines (BC, LS-IQ, ICSDICE, OptiDICE-Constraint, SMODICE-Constraint) across PointMaze and three MuJoCo tasks (HalfCheetah, Walker, Ant), with results averaged over multiple seeds and runs. The advantage is clearest on harder domains like HalfCheetah.

- **Noise-robust constraint update is well-motivated.** Section 4.2 extends the classic ICL loss to account for noisy trajectories across diffusion steps (Eq. 11), which is necessary for the constraint model to function correctly during the denoising process. This is a technically appropriate design choice given the GDV framework.

## Weaknesses

### Fatal
None.

### Major

- **The Lagrange multiplier λ in the GDV is not specified.** The entire GDV verification mechanism (Eq. 9–10) hinges on the Lagrangian formulation \(\tilde{p}(\tau) \propto p_\theta(\tau) e^{r - \lambda c + \lambda\epsilon}\), yet the paper never explains how λ is chosen, whether it is fixed or learned, or what its value is in the experiments. Since the quality of the guided trajectories directly depends on λ (a poor λ would yield trajectories that are not optimal under the constraint), this gap undermines reproducibility and leaves the core verification claim unsubstantiated. The paper also does not empirically show that the guided trajectories satisfy the intended cost constraints, nor compare them against trajectories from a standard CRL solver.

- **The feasible set \(\mathcal{Z}\) is not defined as an operational data structure.** The contrastive loss in Eq. 12 uses \(\mathcal{Z}\) (the set of previously discovered feasible constraints), but the paper never specifies how \(\mathcal{Z}\) is initialized, updated, or bounded—how many constraints are kept, what triggers adding a new constraint, whether constraints are ever removed, or when the process terminates. Without this, the exploration algorithm cannot be faithfully implemented.

- **No ablation studies isolate the contribution of individual components.** The paper compares ExICL against methods that learn a single constraint without a diffusion verifier, but never ablates: (i) ExICL without the GDV (using a standard CRL solver for verification), (ii) ExICL without the exploration mechanism (single constraint with GDV), or (iii) ExICL without the noise-robust objective. Consequently, it is impossible to determine whether the empirical gains come from the diffusion verifier, the contrastive exploration, the noise-robust loss, or simply the overall architecture. This is a significant gap for a paper making multiple technical claims.

### Minor

- **The efficiency claim lacks wall-clock or FLOPs comparison.** Figure 6 shows sample efficiency (data points used), and the paper acknowledges the upfront cost of training the diffusion model (orange ellipse). However, the central claim that GDV is "more efficient" than standard CRL solvers is never quantified in terms of wall-clock time, FLOPs, or iterations. Without this, the efficiency advantage is plausible but unverified.

- **No explicit feasibility verification after exploration.** The exploration objective (Eq. 12) combines the noise-robust ICL loss (which encourages feasibility) with the contrastive term (which encourages diversity), but there is no explicit check that the newly discovered constraint actually makes expert demonstrations optimal. While the first two terms of Eq. 12 push toward feasible constraints, a post-hoc verification step (e.g., checking GDV-generated trajectories against expert data) would strengthen confidence in the diversity claim.

- **The sparsity-diversity trade-off is not analyzed.** The regularization parameter \(\delta\) in Eq. 12 jointly controls sparsity and diversity, but the paper does not study how \(\delta\) affects the feasibility of discovered constraints or how to set it. Figure 4 and the cost-δ relationship are descriptive, not diagnostic of constraint quality.

- **The noise-robust objective's benefit is not ablated.** Equation 11 averages \(\log \phi_\omega(\tau^i, i)\) over diffusion noise levels, but no experiment shows that this noise-robust variant outperforms a simpler alternative (e.g., only evaluating \(\phi_\omega\) on clean trajectories). It is also unclear how \(\phi_\omega\) handles the diffusion step index \(i\) (e.g., step embeddings, separate heads), which affects reproducibility.

### Trivial

- The caption description "The decrease of cost value as regularization parameter δ increase in Figure 4, 7, 8 implies the enlarging sparsity of the constraints" is imprecise—cost values are log-permissibilities, and their magnitude is not directly interpretable as sparsity without additional context.

## Nice-to-Haves

- Report wall-clock time or iteration counts for GDV-based verification vs. standard CRL solvers (e.g., PPO-Lagrangian) to substantiate the efficiency claim.
- Provide an empirical comparison of GDV-generated trajectories against trajectories from a CRL solution under the true constraint, to validate that the guided denoising process produces optimal constrained behavior.
- Show that the discovered constraints in \(\mathcal{Z}\) produce behaviorally distinct policies (e.g., average pairwise trajectory distance) rather than merely having different cost predictions.
- Study the sensitivity of ExICL to the regularization parameter \(\delta\) in terms of both diversity and feasibility (not just cost variance).

## Removed Points

The following criticisms from the harsh reviewer are removed per the filtering rules:

- **Autonomous driving experiments not described in main text.** The paper states "The autonomous experiment setting can be seen in B.3," which is in the appendix (stripped by the parser). Per rule: remove weaknesses about missing appendix content.
- **Algorithm 1 not in main text.** The paper references Algorithm 1; the appendix containing the pseudocode was stripped by the parser. Per rule: remove weaknesses about missing appendix.
- **"A constraint that assigns zero cost everywhere would pass this check."** This is factually incorrect—the noise-robust ICL loss (first two terms of Eq. 12) explicitly distinguishes expert from non-expert trajectories and would not accept a uniform zero-cost model as a fixed point of optimization.
- **"No justification that guided generation works."** The paper provides theoretical justification via zero duality gap (Theorem 4.1) and Lagrangian relaxation (Eq. 9–10). Whether this justification is sufficient is debatable, but the claim of "no justification" is inaccurate. (The absence of *empirical* validation of the generated trajectories is kept as a real weakness above.)
- **"The paper provides no justification that this holds" regarding the equivalence of guided generation to constrained optimality.** The paper does include Theorem 4.1 and the dual formulation. The remaining concern (lack of empirical validation, unspecified λ) is preserved in the Major weaknesses.
- **Related works connection is superficial.** The paper discusses how prior feasible-set theory differs (reward vs. constraint, discrete vs. continuous, online vs. offline), which is a reasonable scope discussion, not a weakness.
- **Pure formatting/style nitpicks** (e.g., "autonomous exdpertiment" typo—parser artifact).

## Novel Insights

None beyond the paper's own contributions. The reviewers identified genuine issues (λ specification, Z management, missing ablations) but did not produce a novel observation that transcends what the paper itself presents.

## Suggestions

1. **Specify λ.** Clarify how the Lagrange multiplier is chosen (fixed, grid-searched, or learned via dual gradient descent). If fixed, show sensitivity analysis. If learned, describe the update procedure.
2. **Define \(\mathcal{Z}\) operationally.** Describe how the feasible constraint set is initialized, updated, bounded, and when exploration terminates.
3. **Add ablation experiments.** At minimum, compare: ExICL without exploration (single constraint + GDV), ExICL without GDV (exploration + standard CRL verification), and ExICL without the noise-robust loss. This would isolate the contribution of each component.
4. **Validate GDV trajectories.** Compare trajectories generated by GDV under a known constraint against trajectories from a CRL solver, showing that they achieve similar reward and cost distributions.
5. **Report wall-clock time.** Add a table or figure showing runtime of GDV-based verification vs. policy-update-based verification to ground the efficiency claim.

## Score and Decision

The paper makes a genuine contribution to a worthwhile problem: formulating ICL as recovery of a diverse feasible set and designing a diffusion-based verification mechanism. The empirical results are strong and support the overall claim that ExICL outperforms existing methods. However, the paper has significant gaps in reproducibility (λ unspecified, \(\mathcal{Z}\) undefined, no ablation studies) that prevent the community from building on this work as presented. These are addressable in a revision and do not invalidate the core contribution, but they are substantial enough to require attention before the work is fully convincing.

**Originality:** 7/10 — The feasible-set formulation is new to ICL, and the GDV verification is creative.
**Quality:** 6/10 — Strong empirical results but missing ablations and implementation details lower confidence.
**Clarity:** 5/10 — Well-organized but missing algorithmic details that are essential for understanding.
**Significance:** 7/10 — The problem is practically important and the approach is promising.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>