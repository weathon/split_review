## Summary

The paper claims to prove that neural policy ensembles are inherently sub-optimal compared to linear policy ensembles, both theoretically and empirically. It presents three main theorems: (1) neural ensemble suboptimality for linear systems, (2) stability violation in neural ensembles under time-varying weights, and (3) a convexity advantage showing that non-convex (e.g., neural) mixing of policies is sub-optimal. Empirical experiments on linear and nonlinear dynamical systems are provided to support these claims.

## Strengths

- The paper tackles a practically relevant question: whether neural network ensembles are suitable for control tasks, which has implications for RL, MoE, and agentic AI.
- The attempt to provide a theoretical framework for comparing linear and neural policy ensembles is a worthwhile direction.
- The empirical study includes multiple experimental conditions (switching patterns, diversity levels) and attempts to measure convexity violations.

## Weaknesses

### Fatal

- **The core theoretical claims are either trivial or unsupported.** For linear-quadratic regulator (LQR) problems, the optimal controller is known to be linear; therefore any nonlinear policy (including neural ensembles) is sub-optimal by definition. Theorem 1 essentially restates this fact under artificial conditions, but does not provide a general proof of sub-optimality for nonlinear systems. The proofs are relegated to a missing appendix, so the theoretical results cannot be evaluated.
- **The empirical comparisons are fundamentally unfair.** The linear ensemble uses analytically computed optimal LQR gains, while the neural ensemble is trained via gradient descent with no evidence of convergence to optimality. The observed performance gap is therefore likely due to insufficient training or sub-optimal neural network solutions, not an inherent property of neural ensembles. The paper does not control for training budget, architecture search, or hyperparameter tuning.
- **The paper overclaims the generality and magnitude of the results.** Claims of "2 orders of magnitude" sub-optimality are not supported by the data (figures show factor 2–3 differences). The stability theorem (Theorem 2) is a well-known result in switched systems (fast switching can destabilize stable subsystems) and is presented as novel without proper attribution or proof.

### Major

- **The theoretical results are not properly connected to the empirical setting.** Theorem 1 assumes a linear system, but the paper later claims implications for nonlinear systems without extending the theory. The stability experiments do not actually demonstrate instability (unbounded trajectories); they only show higher cost.
- **Experimental details are severely lacking.** The neural network architecture, training procedure, hyperparameters, and convergence criteria are not described. The statistical tests are mentioned but not specified (e.g., which test, sample size, assumptions). The figures are poorly labeled and some subplots are unreadable.
- **The policy mixing experiments (Section 6) compare convex mixing of optimal LQR policies against a neural mixer, but the neural mixer is not described.** The results show high variance and the claim that neural mixing is sub-optimal is not convincingly supported.

### Minor

- The paper uses "sub-optimal" loosely; it compares neural ensembles to a specific linear ensemble, not to the true optimal policy. The linear ensemble itself may not be optimal for the overall multi-regime problem.
- The "diversity" experiments (Figure 3) show that neural ensemble cost decreases with diversity, but the gap to linear ensemble remains large. This is consistent with the neural policies being poorly trained rather than a fundamental limitation.

### Trivial

- The paper states "p < 10^{-5}" without reporting the test statistic or confidence intervals.
- The caption of Figure 1 is repeated verbatim in the text.

## Nice-to-Haves

- A comparison against other neural ensemble methods (e.g., ensemble of trained neural controllers with proper tuning) would strengthen the claims.
- A theoretical analysis for nonlinear systems beyond the linear case would be valuable.
- Providing the proofs in the main text or a clearly accessible appendix is essential for a theory paper.

## Novel Insights

None beyond the paper's own contributions. The observation that neural networks are sub-optimal for LQR is well-known, and the stability result is standard in control theory. The paper does not provide a new insight that advances the field.

## Suggestions

- Clearly separate the trivial case (LQR where linear is optimal) from the non-trivial case (nonlinear systems). Provide theoretical results for nonlinear dynamics or remove the claim of generality.
- Ensure fair comparison: train neural policies to convergence with extensive hyperparameter tuning, and report training curves to demonstrate optimality. Compare against neural ensembles that are also trained end-to-end, not just against analytically optimal linear controllers.
- Provide complete proofs for all theorems in the main text or a supplement that is included in the submission.
- Describe experimental details fully: network architecture, optimizer, learning rate, number of training steps, seeds, and statistical test methodology.

## Score and Decision

**Score:** 3

**Decision:** Reject

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>