- Decision: Accept
- Scores: 8, 8, 6, 6

## Merged Review

### Summary

The paper introduces a surrogate-loss-based framework for solving variational inequalities (VIs) with hidden monotone structure. An outer loop updates a target output \(z_t\), and an inner loop minimizes a surrogate square loss on model parameters to match \(z_t\). Under an \(\alpha\)-descent condition on inner-loop progress, the method achieves linear convergence in the deterministic and stochastic settings (to a neighborhood). The framework unifies prior methods (e.g., PHGD). Experiments demonstrate effectiveness on min-max games and RL value prediction (projected Bellman error), including a variant of TD(0) that improves sample and compute efficiency.

### Strengths

- **Originality and significance.** The extension of iterative surrogate optimization from scalar losses to VIs is a significant contribution. The framework is the first to reduce VI optimization (with hidden monotonicity) to black-box scalar optimization. ([R1, R2])
- **Nontrivial difficulty gap.** Proposition 3.3 provides a simple adversarial example showing that surrogate methods for VIs are qualitatively more complex than for scalar optimization (\(\alpha<1\) insufficient). ([R1, R2])
- **Rigorous theoretical analysis.** The paper provides thorough convergence guarantees in deterministic and stochastic settings, addresses an issue in prior analysis (Sakos et al. 2024), and explains how previous methods fit as special cases. ([R1, R2, R4])
- **Robustness of the framework.** The core reduction from VI to scalar optimization appears robust to choice of inner-loop optimizer, making the methodology broadly applicable. ([R2])
- **Promising experimental results.** The method shows strong performance on min-max games (where inner-loop optimizer choice matters) and on RL value prediction, where multiple inner iterations yield improvements in sample and wall-clock efficiency over TD(0). ([R1, R2, R3, R4])

### Weaknesses

- **Clarity and presentation issues.** The paper is challenging to follow, especially the transition from problem (1) to the surrogate model construction. Condition 2 in Theorem 3.2 (there exist \(C,p>0\) such that \(\alpha < C\eta^p\) for all \(\eta>0\)) is problematic—it is never satisfied as stated, indicating a missing dependency between \(\alpha\) and \(\eta\). Figure 1 is hard to read (methods hard to tell apart). The term “gradient step” is misleading for VIs where \(F\) is not a gradient. The PL condition is not defined in the main text. ([R3, R4]; [R1] for Fig 1)
- **The \(\alpha\)-descent condition is a major concern.** It requires a single constant \(\alpha\) uniform across all iterations, which is a stringent requirement. The condition cannot be verified directly (since \(\ell_t^*\) is unknown), and its practicality is questionable—it is not clear how it could be checked or set as a user parameter in the experiments. One reviewer argues the \(\alpha\)-descent condition is a red herring; the paper should instead emphasize the more general reduction from VI to scalar optimization, as the proofs likely work under weaker inner-loop guarantees. ([R1, R2, R3])
- **The finding that better inner-loop optimization does not necessarily improve outer-loop convergence** (e.g., more iterations can hurt) is noted but not examined in depth. No theoretical justification or further experimental investigation is provided. Questions remain: what makes a “good” inner solution? Has this been observed in scalar surrogate optimization? ([R1, R2])
- **Assumptions are overly restrictive.** The assumption that the constrained domain \(\mathcal{Z}\) is convex is unnecessarily limiting. The uniformity of \(\alpha\) over all iterations is unrealistic when surrogate accuracy varies during optimization. Sensitivity to the choice of \(\alpha\) is not discussed. ([R3])
- **Lack of larger-scale experiments.** The RL experiments use small (2-layer) networks; the 16-layer network experiment in the appendix does not convincingly demonstrate scalability because the task may not require such capacity. GAN training, a natural test for VIs, is not attempted. A comparison with standard optimizers like Adam in the supervised learning (scalar) case is missing. ([R4, R3, R2])

*Minority contrast:* Two reviewers rate the paper 8 (very positive) and emphasize the novelty and significance of the framework, while two rate it 6 (positive but with reservations) and focus on presentation and assumption issues. One minority reviewer (R2) sees \(\alpha\)-descent as a presentation weakness rather than a core flaw, arguing the reduction perspective is the key contribution; the other minority (R3 and R4) consider the assumptions and conditions to be serious weaknesses limiting practical applicability.