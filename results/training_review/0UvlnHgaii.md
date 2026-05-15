Now I have a thorough understanding of the paper. Let me compile my final review.

## Summary

The paper tackles the ill-posed problem of Inverse Constraint Learning (ICL), where multiple constraints can equivalently explain expert demonstrations. Instead of targeting a single constraint (which is inherently unidentifiable), the authors propose **ExICL** (Exploratory ICL), which recovers a *set* of feasible constraints. The key methodological contributions are: (1) a **Generative Diffusion Verifier (GDV)** that uses guided denoising to efficiently test whether a candidate constraint can reproduce expert-like trajectories without solving a full forward CRL, (2) a **noise-robust constraint update** tailored for the diffusion process, and (3) a **contrastive exploration objective** that promotes diversity among discovered constraints. Experiments on PointMaze, MuJoCo locomotion tasks, and (via appendix) autonomous driving show that ExICL achieves lower constraint violations than several offline IL/IRL/ICL baselines while maintaining competitive rewards, and that its constraint set exhibits higher cost variance than random exploration alternatives.

## Strengths

- **Well-motivated problem formulation.** The paper correctly identifies that ICL is inherently ill-posed (multiple constraints can explain the same demonstrations) and reframes the goal from recovering a single unidentifiable constraint to recovering a diverse *set* of feasible constraints (Definition 3.1). This reframing is both principled and practically useful, as it gives practitioners the flexibility to select constraints suited to deployment needs.

- **Novel integration of diffusion models for efficient constraint verification.** Using guided denoising (inspired by Diffuser) to generate trajectories under a candidate constraint — without iterative policy updates — is a creative way to bypass the computational bottleneck of bi-level optimization in prior ICL methods. Theorem 4.1 (strong duality for CRL) provides theoretical grounding for the dual representation used in the guided sampling.

- **Consistently strong empirical performance on constraint satisfaction.** Across PointMaze (Table 1) and MuJoCo (Table 2) environments with spatial, dynamic, and kinematic constraints, ExICL achieves the lowest cumulative cost among all baselines (BC, LS-IQ, SMODICE, ICSDICE, OptiDICE-c, SMODICE-c) while maintaining competitive rewards. This is the paper's strongest empirical result.

- **Visual evidence of behavior diversity.** Figure 5 shows qualitatively distinct robot behaviors (varying movement distances, gait patterns, directions) emerging from different learned constraints, supporting the claim that the method produces meaningfully varied constraints, not just different parameter vectors.

## Weaknesses

### Fatal
None.

### Major

- **The GDV verifier is not validated against ground-truth constraint feasibility.** The paper defines a constraint as feasible if the expert policy πᴱ is optimal under the CMDP with that constraint (Definition 3.1). However, no experiment checks whether the GDV's assessment of feasibility actually aligns with this definition. Missing: (a) comparison of GDV verdicts against ground-truth feasibility determined by solving full CRL for a sampled set of candidate constraints, (b) analysis of false-positive/false-negative rates, and (c) sensitivity analysis of the Lagrange multiplier λ (whose value is never specified or discussed beyond its appearance in Equation 10, line 132). Since the entire pipeline for constructing the feasible set rests on this verifier, the lack of direct validation is a significant gap — the paper largely relies on the indirect evidence that downstream policies perform well, which is necessary but not sufficient.

- **Key components are not ablated.** Three claimed innovations — the noise-robust constraint update (Equation 11), the guided diffusion verifier, and the contrastive exploration objective (Equation 12) — are introduced as essential to the method, yet none is individually ablated. Critical missing comparisons include: (a) the noise-robust update vs. a standard MLE constraint update (Equation 2), (b) the GDV approach vs. running actual forward CRL for verification (in terms of accuracy, not just efficiency), and (c) the contrastive exploration vs. a simpler diversity-promoting baseline on a meaningful downstream metric beyond cost variance. Without these, the empirical results cannot be causally attributed to any specific design choice.

### Minor

- **Diversity evidence is primarily cost variance, which is a limited metric.** The quantitative evidence for constraint diversity (Figure 4) relies on the variance of predicted costs across trajectories. The paper's own definition of diversity (line 221) is that "constraints in the feasible set should assign different costs to the same trajectory" — cost variance directly measures this. However, cost variance does not capture whether constraints cover semantically distinct regions of the state-action space or represent qualitatively different safety criteria, which would be needed for the claim that practitioners have "meaningful choice." The visual evidence (Figure 5) partially addresses this, but a more rigorous diversity analysis would strengthen the paper.

- **The Lagrange multiplier λ is not addressed.** The dual representation (Equation 10) requires a Lagrange multiplier λ to convert the constrained problem into a penalty. The paper states only that "λ denotes the Lagrange multiplier" (line 135) but does not specify how λ is chosen, learned, or adapted. Since the quality of the guided trajectories depends on λ (if λ is too small, constraint satisfaction is not enforced; if too large, reward may be ignored), this is a non-trivial gap in the methodology description.

- **Autonomous driving results are deferred to the appendix.** The abstract and conclusion claim evaluation on "navigation, locomotion, and autonomous driving," but the main text only presents PointMaze and MuJoCo results, with a brief reference to "B.3" (line 187). Given that the appendix is not available in this format, the claim of broad validation across these domains is not verifiable from the main paper. This should either be moved into the main text or the claim should be qualified.

- **Missing comparison with a version of Malik et al. (2021) adapted to the offline setting.** The most closely related prior work is not included as a baseline; the paper compares against ICSDICE (Quan et al., 2024) and OptiDICE-c, but not against the offline adaptation of Malik et al. (2021), which would provide a stronger baseline to benchmark against.

### Trivial
None.

## Nice-to-Haves
- A study of how the regularization parameter δ affects the sparsity/diversity trade-off (number of constraints discovered, average size of infeasible regions, downstream reward/cost).
- A check for circularity: can the diffusion model generate expert-like trajectories under reward-only guidance (no constraint)? If so, the verifier may accept spurious constraints.
- Constraint heatmaps for PointMaze showing the learned infeasible regions overlaid with the ground-truth constraint.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"The description of the classic ICL loop (Figure 1) does not match typical implementations — most ICL methods do not require solving a full CRL from scratch."** — Factually incorrect. Malik et al. (2021) explicitly requires solving forward CRL in a bi-level optimization loop. The paper's contrast is accurate.
- **"The MLE gradient derivation assumes the normalizing constant Z_c is tractable."** — This is inherited from Malik et al. (2021) and is a known limitation of the maximum entropy framework; it is not a novel issue introduced by this paper and does not specifically harm the paper's claims.
- **"The sparsity term pushes φ toward 1, which is the opposite of what a constraint should do."** — The paper defines φ ∈ [0,1] where 1 = fully permissible (no constraint). In the ICL literature, "sparsity" means that *few* state-action pairs are constrained (infeasible), so φ → 1 for most pairs is consistent with this goal. The explanation could be clearer, but the design is not contradictory.
- **"Circularity analysis needed — the diffusion model may imitate experts without constraint."** — The paper acknowledges this (line 101: "there is no guarantee a trajectory generated under this model will be safe") and uses guided sampling with the constraint term specifically to generate *constrained* trajectories. The concern is reasonable but not fatal; it would be a nice validation to include rather than a structural flaw.

## Novel Insights
Beyond the paper's own contributions, a genuinely novel observation emerges from the interaction between the reviews and the paper: the GDV verifier operates as a *generative surrogate* for a bi-level optimization problem, but the paper never measures the surrogate gap — i.e., how often the GDV's verdict disagrees with the true CRL solution. In many inverse problems where a learned forward model replaces an expensive oracle, characterizing this gap (and its dependence on λ) is essential for trustworthiness. The paper's downstream task performance provides an aggregate sanity check, but without explicit verifier accuracy metrics, the core mechanism remains a black box. This suggests a broader methodological point for the community: generative surrogates for constrained optimization (inverse problems) need explicit validation of the surrogate before downstream claims can be evaluated.

## Suggestions
1. **Add a direct validation study of the GDV verifier:** Sample a set of random candidate cost functions, determine their true feasibility by solving the forward CRL (even approximately), and compare against the GDV's verdict. Report accuracy, precision, recall, and F1. This is the single most important addition.
2. **Add ablation experiments:** Compare ExICL against (a) a version using standard MLE update instead of noise-robust update, (b) a version where feasibility is verified by an approximate CRL solver instead of GDV, and (c) a version without the contrastive exploration term.
3. **Specify how λ is set** and provide a sensitivity analysis showing how the verifier's accuracy changes with λ.
4. **Strengthen the diversity evaluation** with a metric that captures semantic diversity (e.g., overlap of infeasible regions between constraint models, or coverage of different state-space regions).
5. **Include autonomous driving results in the main text** or qualify the claim.

## Score and Decision

The paper proposes a genuinely novel formulation (exploratory ICL) and a creative technical approach (diffusion-based verifier + contrastive exploration). The empirical results on constraint satisfaction are consistently strong across multiple environments. However, the paper has two significant gaps: (1) the GDV verifier — the linchpin of the method — is not directly validated against any ground-truth definition of feasibility, and (2) key components are not ablated, making it impossible to attribute performance to specific design choices. These weaknesses are addressable with additional experiments but are substantial in the current form. The paper's contribution is interesting and potentially impactful, but the evidence is incomplete.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>