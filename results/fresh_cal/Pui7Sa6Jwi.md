Now I have a thorough understanding of the paper and both reviews. Let me construct the final consolidated review.

---

## Summary

This paper proposes CLEAR, an information-theoretic framework for learning distraction-free agent-centric representations in visual offline RL. It formalizes visual RL as an ExoPOMDP (POMDP with exogenous variables), identifies via an information decomposition why prior latent-dynamics methods inevitably learn representations containing superfluous task-irrelevant information, and introduces a method with separate encoders for state and exogenous factors regularized by an inverse-dynamics-based controllability objective. Experiments on the DeepMind Control Suite with synthetic distractions (video backgrounds, multi-agent grids) show that CLEAR maintains near-invariant task performance across distraction levels, unlike prior latent-dynamics methods.

## Strengths

- **Principled information-theoretic derivation of superfluous information**: Section 2.2 decomposes the predictive information objective (Equation 2) to isolate an irreducible term \(I_{\theta^*}(\hat{S}_{t-1},A_{t-1};O_t|S_t)\) that captures exogenous factors. This decomposition is cleanly derived and directly motivates why prior methods (SLAC, etc.) fail under distractions — a prediction confirmed empirically where SLAC collapses from ~98 (Clean) to single digits on harder distractions. The analysis is not heuristic; it follows from the ExoPOMDP graphical model.

- **Objective explicitly derived from the ExoPOMDP structure**: Equations (3)–(5) derive a principled ELBO that models both agent and exogenous latent variables, while Equations (6)–(7) add symmetric inverse-dynamics regularization (maximizing controllability of \(\hat{S}\), minimizing it for \(\hat{E}\)). The complete objective in Equation (8) follows rigorously from the variational bounds — this goes beyond the heuristic inverse-dynamics losses used in prior work (Iso-Dream, Denoised MDP).

- **Strong empirical performance on the hardest distraction (\(2\times2\) Grid)**: Table 1 shows CLEAR achieves near-invariant scores across Clean → Grid on Walker-Walk (~95→~94) and Cheetah-Run (~93→~92), while all latent-dynamics baselines collapse dramatically (e.g., SLAC from ~98 to ~10 on Walker). On this hardest setting — where the agent must identify which of four visually identical agents is controllable — CLEAR's success directly validates the controllability-based disentanglement. On Hopper, CLEAR is competitive with the strongest baselines (InfoGating) even though it does not achieve full invariance.

- **Qualitative evidence of disentanglement**: Figure 4 shows that CLEAR's reconstructed state component captures only the controllable agent (even isolating the correct quadrant in the \(2\times2\) Grid), while the exogenous component captures backgrounds and other agents. The ablation (Table 3, Figure 5) further confirms that without the inverse-dynamics regularization, the model converges to flipped or degenerate solutions (scores of 38.2 and 59.6 vs. 95.5 with the full objective), providing direct evidence that the regularization is necessary for correct separation.

- **Ground-truth state regression corroborates representation quality**: Table 2 shows CLEAR consistently achieves the lowest or near-lowest MSE in predicting the ground-truth state across all environments and distraction levels (e.g., Cheetah MV: 0.12 vs. SLAC 0.63), providing quantitative evidence that \(\hat{S}\) captures the true state rather than distractions.

## Weaknesses

### Fatal
None.

### Major

- **The compositional decoder's spatial separability assumption is stated but its limitations are not discussed.** The decoder combines state and exogenous reconstructions via a pixel-wise mask (\(\mu = m\mu_s + (1-m)\mu_e\)), which *assumes* that distractions are spatially additive — each pixel belongs entirely either to the agent or to the background. The paper acknowledges this assumption (line 134: "assuming the state variables and exogenous variables occupy different parts of the visual observation") but never discusses when it would fail (e.g., color shifts, lighting changes, partial occlusions, shadows, visual effects that alter the agent's appearance rather than add independent background content). Since the Ethics Statement and Introduction mention "real-world scenarios such as autonomous driving and robotics" — scenarios with non-spatially-separable visual effects — this undiscussed gap between the method's inductive bias and the hinted scope is the paper's most significant limitation. The paper would be substantially stronger by explicitly bounding this assumption, stating the class of distractions it handles, and acknowledging what it does not.

### Minor

- **Ablation is performed on only one environment (Cheetah, Multiple Videos).** Table 3 shows the full objective outperforms its components, and Figure 5 demonstrates informative failure modes. However, it is unknown whether the same pattern holds for other environments (Walker, Hopper) or distraction types (Grid). While the single ablation is informative, the paper's conclusion that "the inverse dynamics regularization term helps stabilize the training procedure" would be stronger with evidence from at least one more setting.

- **Several baselines (TiA, RePo, Denoised MDP) are repurposed outside their original design.** The paper acknowledges these were "originally proposed as model-based methods" and cites prior work (Wang et al., 2022) for the adaptation protocol, but provides no discussion of whether hyperparameters were tuned for the representation-extraction use case or whether the poor performance of these baselines (in some cases near-zero scores) reflects a genuine limitation of the methods vs. suboptimal adaptation. Adding the number of hyperparameter trials per baseline or a caveat about the adaptation would improve fairness.

- **The two KL constants in \(J_{\text{ELBO}}\) are mentioned but not analyzed.** Line 132 states that "using two different constants for the two KL terms...controls the amount of information that passes through each encoder and improves the performance." No sensitivity analysis or ablation is provided for these constants, despite them being potentially important for the information bottleneck trade-off.

- **The min-max optimization for \(J_{\text{InvDyn-E}}\) (Equation 7) lacks training stability analysis.** The paper states the optimization can be done "in an alternating fashion" but provides no details on update ratios, learning rates for \(\psi\) vs. \(\theta\), gradient clipping, or convergence behavior. Given that the ablation shows \(J_{\text{ELBO}}\) alone is unstable and the regularization is meant to stabilize it, evidence that the min-max actually achieves this would strengthen the paper.

- **Normalized scores are reported without raw ground-truth returns.** The paper normalizes so that "100 means that it performs as good as using the ground-truth state," but the absolute ground-truth performance is never reported. This makes it difficult to interpret whether a score of, say, 80 is near-optimal or far from it. Reporting raw returns alongside normalized scores would resolve this.

- **Qualitative failure modes (Figure 5) show only 3 seeds for one setting.** The paper identifies three failure types (desired, flipped, degenerate) with associated scores of 95.5, 38.2, and 59.6. Reporting the frequency of each failure mode across many seeds (e.g., 10–20) would give a more robust sense of the regularization's stabilizing effect.

### Trivial
None.

## Nice-to-Haves

- Analysis of the min-max training dynamics (convergence, sensitivity to update frequency) would be illuminating but is not required for acceptance.
- A computational cost comparison (parameters, training time) relative to baselines would help practitioners but is not needed for the paper's core claims.
- A scatter plot of ground-truth MSE vs. offline RL performance across methods/seeds could strengthen the discussion in Section 5.2.

## Removed Points

These points were flagged for removal. Treat them with caution; they may be inaccurate or irrelevant.

- **Criticism that the evaluation is too narrow (only 3 environments):** Three DMC environments with four distraction types each (12 conditions) is a standard evaluation breadth for this subfield. The paper acknowledges the Hopper limitation explicitly. This criticism overstates the issue. **Removed** — the evaluation scope is adequate for the paper's claims.

- **Criticism that the analysis in Section 2.2 conditions on unobserved \(S_t\) and is "purely conceptual":** The paper itself acknowledges that the superfluous term "cannot be computed nor minimized directly" (line 61). This is not a weakness — it is a stated property of the analysis that motivates the need for a practical method. **Removed** — not a genuine weakness.

- **Criticism that the linear probe (Section 5.2) is a "weak test":** Linear probing of learned representations is standard practice in representation learning for RL. The paper uses it appropriately to show correlation between representation quality and RL performance. **Removed** — not a valid weakness given field norms.

- **Criticism that the paper does not perform formal statistical tests:** Reporting standard errors over 5 seeds is the norm in this field. The request for bootstrap tests goes beyond standard practice and is not necessary for the paper's claims. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced no genuinely novel observation about the work that the paper itself does not already make.

## Suggestions

1. **Add a limitations paragraph** that explicitly states the decoder's spatial separability assumption and discusses the types of distractions the method is and is not designed to handle (e.g., additive background content vs. multiplicative appearance changes).
2. **Extend the ablation** to at least one more environment (e.g., Walker-Walk) and one more distraction type (e.g., Grid) to confirm the regularization's benefit generalizes.
3. **Report the ground-truth state raw returns** alongside the normalized scores so readers can interpret the absolute scale.
4. **Add a brief hyperparameter sensitivity analysis** for the two KL constants, or at minimum state the values used and note whether performance is robust to moderate variation.
5. **Include per-seed frequency of failure modes** (desired/flipped/degenerate) across many seeds to quantify the stabilizing effect of the regularization.

## Score and Decision

The paper presents a principled information-theoretic framework with a clear derivation, a well-motivated objective, and strong empirical results — particularly on the hardest distraction setting where prior methods collapse. The main limitation (the decoder's spatial separability assumption is acknowledged but its failure modes are not discussed) is real but does not invalidate the core contribution; it primarily narrows the scope of what the paper claims. The remaining issues (single-setting ablation, hyperparameter sensitivity, baseline adaptation transparency) are addressable. This is a solid paper with genuine contributions.

**Score:** 7.0  
**Decision:** Accept

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>