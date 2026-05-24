Now I have all the calibration data I need. Let me synthesize the final review.

**Round 1 Bracket:** The paper sits between the 4.67 anchor (simple calibration+HCI study, limited contribution) and the 8.0 anchors (DRO with convergence proofs + multi-domain experiments). Narrower bracket: **5.5–7.5**.

**Round 2 Narrowing:** The 5.67 anchor (calibration metrics reassessment, one dataset) is clearly below this paper — our paper has far more substantial theoretical contributions. The 6.80 anchor (decision-focused UQ, diverse experiments + healthcare case study) has stronger experiments but comparable theoretical depth. This paper lands at approximately **6.5** — strong clean theory, elegant sharp-transition result, but limited experimental validation (d=1 only).

---

## Summary

This paper introduces a minimax robust decision-making framework for predictors that satisfy $\mathcal{H}$-calibration, a flexible family of partial calibration constraints. Given an $\mathcal{H}$-calibrated forecaster, the decision maker chooses an action policy that maximizes worst-case expected utility over all conditional outcome distributions consistent with those moment constraints. The central contributions are: (1) a saddle-point characterization of the optimal robust policy via duality (Theorem 3.1), (2) the discovery of a sharp transition — when $\mathcal{H}$ contains the decision-calibration indicators, the robust policy collapses to the plug-in best response (Theorems 4.1–4.2), upgrading known swap-regret bounds to minimax optimality, and (3) practical instantiations showing that self-orthogonality from squared-loss training and bin-wise recalibration yield naturally usable $\mathcal{H}$-classes (Propositions 4.4–4.5). Two 1D regression experiments demonstrate that the robust policy provides the predicted minimax protection.

## Strengths

- **Sharp theoretical insight on decision calibration.** Theorems 4.1–4.2 prove that when $\mathcal{H}$ contains the $|\mathcal{A}|$ decision-calibration indicators, the adversarial tilt vanishes ($q^*(v)=v$) and the robust rule collapses to the plug-in best response. This is a non-trivial upgrade from known swap-regret bounds to minimax optimality, and it identifies a tractable, task-specific threshold for trustworthy decision-making. The invariance argument (lines 195–199) — that the adversary cannot reduce the utility of $a_{BR}$ under the decision-calibration constraints — is clean and compelling.

- **General saddle-point characterization.** Theorem 3.1 gives a closed-form solution to the minimax problem for any finite-dimensional $\mathcal{H}$-calibration, expressing the optimal policy as a best response to a worst-case distribution $q^*(v)$ computed via dual multipliers $\lambda^*$. The pointwise computability (evaluating $a_{\text{robust}}$ at a given $v$ reduces to two low-dimensional optimizations) is a practically useful consequence.

- **Practical grounding through training-induced $\mathcal{H}$-classes.** Proposition 4.4 shows that any model with a linear final layer trained to a first-order stationary point of squared loss is automatically $\mathcal{H}$-calibrated for $\mathcal{H} = \{h(v) = v\}$ (and linear combinations thereof). Proposition 4.5 gives a closed-form robust policy under bin-wise calibration. These results connect the abstract framework to standard ML pipelines without requiring additional forecaster processing.

- **Clear conceptual framing.** The paper cleanly articulates how the robust policy interpolates between maximally conservative (empty $\mathcal{H}$) and maximally aggressive (full calibration) extremes as a function of $\mathcal{H}$-richness (Figures 1–2). The sharp transition at decision calibration is surprising and well-motivated.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Experiments limited to 1D outcomes.** The paper's motivation emphasizes that full calibration is intractable in high dimensions and that weaker notions like decision calibration are therefore essential. Yet all experiments use single-output regression ($d=1$), where full calibration is itself straightforward and the practical advantage of partial calibration is less compelling. The experiments test only the self-orthogonality case (Proposition 4.4), not the decision-calibration result that is the paper's most striking theoretical contribution. The experiments serve as a reasonable proof-of-concept, but they do not empirically validate the framework in the regime where it matters most. Adding even one multi-class or multi-output experiment would substantially strengthen the empirical case.

- **Adversary construction for the plug-in worst case is not described.** The paper states that adversarial evaluations use "a worst case tailored to the plug-in policy" and "a worst case induced by the robust dual," but does not explicitly describe how the plug-in adversary is computed. The robust adversary follows directly from Theorem 3.1, but the plug-in adversary (argmin over $q \in \mathcal{Q}$ of the plug-in's expected utility) requires a separate optimization that is not detailed. This makes the "Worst-case for plug-in" column of Table 1 difficult to reproduce without additional specification.

### Trivial

- Table 1 reports only point estimates (means) without any measure of variability across runs, seeds, or data splits. While the qualitative pattern is clear, reporting standard deviations would aid interpretation.

- The paper does not report the empirical $\mathcal{H}$-calibration moment violations on held-out data to verify how closely the approximate self-orthogonality condition (from finite-sample squared-loss training) holds. This would help readers gauge the gap between the theoretical assumption of perfect calibration and the experimental reality.

## Nice-to-Haves

- Evaluating the robust policy under a natural distribution shift (e.g., temporal split for Bike Sharing) in addition to the adversarial shifts would help characterize the practical cost-versus-protection trade-off, though the paper's focus on minimax guarantees makes this strictly optional.

- A brief discussion of computational complexity for the dual optimization when $d > 1$ and $|\mathcal{A}|$ is large, beyond the sketch in Section 4.2, would make the "efficiently computable" claim more concrete — though the current discussion is adequate for a theory paper.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No discussion of computational scalability beyond low dimensions"** (Harsh Critic Point 3): The paper does discuss this in Section 4.2, stating that for $d > 1$ the pointwise problem "remains a small convex program over $p \in [0,1]^d$" and "for finite $\mathcal{A}$ and linear utilities, it is again efficiently solvable." For a theory paper, this level of discussion is adequate.

- **"No evaluation under natural distribution shifts"** (part of Harsh Critic Point 2): This is scope creep. The paper's framework is explicitly about minimax/worst-case guarantees. Evaluating under natural shifts is a nice-to-have extension, not a weakness of the current work.

- **"The utility functions and action sets are chosen arbitrarily"** (Harsh Critic Section 5 note): The paper explicitly states that "The qualitative conclusions of this Section remain the same under other reasonable parameter choices." This is a reasonable robustness claim for a proof-of-concept experiment.

## Novel Insights

The most genuinely novel insight emerging from the synthesis of this work is the "sharp transition" phenomenon: the hierarchy of minimax-optimal decision rules does not vary continuously with the richness of $\mathcal{H}$ but instead collapses discontinuously at the level of decision calibration. Once $\mathcal{H}$ contains just $|\mathcal{A}|$ indicator functions (one per action's decision region), the robust policy becomes the plug-in best response and stays there for all richer $\mathcal{H}$. This is both mathematically clean (via the invariance argument in Theorem 4.2) and practically significant — it identifies a concrete, tractable target for forecaster design that is far cheaper than full calibration while delivering the same decision-theoretic trustworthiness under the minimax lens.

## Suggestions

- Add at least one experiment with $d \geq 2$ outcomes (e.g., multiclass classification with $|\mathcal{A}| = d$ actions, or multi-output regression) to demonstrate the framework in a setting where full calibration is genuinely difficult. This would directly support the paper's high-dimensional motivation.

- Explicitly describe how the "worst-case for plug-in" adversary is constructed (the optimization problem and how it is solved), or provide pseudocode for both adversaries. This would make the adversarial evaluation fully reproducible.

- Report empirical $\mathcal{H}$-calibration moment violations and standard deviations across runs in Table 1.

## Score and Decision

### Anchor comparison:
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| WoJzHQIIUk (MinMax BNN) | 1.50 | R1 | Far below — unreadable, no clear contribution |
| XM7INBbvwT (Calibration + Human Actions) | 4.67 | R1 | Below — simple method, limited HCI study |
| X0epAjg0hd (Reassessing Calibration) | 5.67 | R2 | Below — interesting theory but one dataset, less novelty |
| uuPkll6i7m (Certified Calibration) | 6.75 | R1 | Comparable/slightly above — stronger experiments, comparable theory |
| dIkpHooa2D (MixMax DRO) | 6.75 | R1 | Comparable — similar theory+experiment balance |
| iOMnn1hSBO (Decision-Focused UQ) | 6.80 | R2 | Slightly above — stronger experiments with healthcare case study |
| TTrzgEZt9s (DRO with Bias/Variance) | 8.00 | R1 | Clearly above — convergence proofs + comprehensive multi-domain experiments |

**Round 1 bracket:** 5.5–7.5. **Round 2 narrowed to:** ~6.5. The paper has genuinely novel and elegant theory (the sharp transition result is the highlight), but experiments are limited to 1D and do not test the decision-calibration result that is the paper's strongest theoretical contribution. This puts it slightly below the 6.75–6.80 anchors that pair strong theory with comprehensive experiments, and well above the 5.67 anchor with weaker theory and one-dataset experiments.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>