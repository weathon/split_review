## Summary

This paper studies observer uncertainty in deterministic FTRL dynamics for two-player zero-sum games, proposing covariance matrices as a measure of uncertainty alongside differential entropy. The authors derive concrete covariance growth rates for Euclidean-regularized FTRL under continuous, Euler (simultaneous), and symplectic (alternating) discretization (Theorem 5.1), showing exponential growth under Euler but at most polynomial or bounded growth under symplectic discretization. A Heisenberg-type inequality for general regularizers is also stated (Theorem 5.2), and experimental results on 2×2 games partially corroborate the growth rate claims.

## Strengths

1. **Sharp asymptotic covariance rates for Euclidean FTRL (Theorem 5.1).** The paper proves a clean distinction: Euler discretization yields exponential covariance growth ($\Theta(|\mu|^{2t})$), while symplectic/continuous FTRL yields at most polynomial growth ($\Theta(t^2)$) for singular $AA^\top$ and $\mathcal{O}(1)$ for non-singular $AA^\top$. This is the first concrete rate comparison between discretization schemes from an uncertainty perspective and is the paper's strongest theoretical contribution.

2. **Novel primal-dual discretization correspondence (Proposition 3.1).** The formal equivalence between Euler discretization of the Hamiltonian system and simultaneous GDA/MWU, and between symplectic discretization and alternating GDA/AltMWU, bridges numerical analysis (symplectic integrators) with game-theoretic update rules in a way that is both clean and useful.

3. **Differential entropy invariance under alternating MWU (Proposition 4.2).** Showing that differential entropy remains constant under alternating MWU while growing at least linearly under simultaneous MWU (Proposition 4.1) establishes a concrete limitation of the entropy-based approach in (Cheung et al., 2022) and motivates why finer-grained measures (covariances) are needed.

## Weaknesses

### Major

1. **Experimental validation is too narrow to support the central theoretical distinction in Theorem 5.1.** Every payoff matrix tested for continuous FTRL and symplectic discretization has singular $AA^\top$ (e.g., $A_1 = [[1,-1],[-1,1]]$, $A_2 = [[1.2,-1.2],[-1,1]]$, $B_1 = [[1,-1],[-1,1]]$, etc. — all have determinant zero). Theorem 5.1's most striking prediction is that *non-singular* $AA^\top$ yields $\mathcal{O}(1)$ covariances under symplectic discretization — a qualitatively different regime (bounded vs. growing uncertainty) that is never experimentally tested. The experiments also use only 2×2 games, a single initial covariance matrix, and track only one of four state components, with no error bars, random seeds, or statistical analysis. These are insufficient to validate asymptotic growth rate claims.

2. **Theorem 5.2's assumptions are not operationalized, limiting its usefulness.** The theorem depends on three quantities that the paper does not define in concrete terms relevant to game dynamics: (i) "higher order differentials of $\phi_t(\cdot)$ are bounded by some constant $K$" — no criterion is given for determining $K$ or checking this condition; (ii) "standard deviations at initialization are sufficiently small" — the footnote defers to a statistics textbook (Benaroya et al., 2005) without explaining how this translates to a condition on the covariance matrix in the game dynamics setting; (iii) the linear Gromov width $w_L(P(t_0))$ is named but **never defined or explained** — the paper only says it is "the linear Gromov width of the ellipsoid defined by the initial covariance matrix $P(t_0)$." Without a definition, the constant in the inequality cannot be computed for any concrete game, making the theorem a formal statement with no operational content as presented.

3. **The central concept of "prediction accuracy" is never operationalized.** The paper repeatedly states that covariances measure "accuracy of prediction" and that symplectic discretization "enhances the accuracy of prediction," but it never defines a concrete prediction task (e.g., predicting the strategy of player 1 at time $t$ given observations up to $t_0$), a loss function, or an operational notion of what it means for a prediction to be accurate. The jump from "covariance grows slower under symplectic discretization" to "symplectic discretization is superior for prediction" is an未经证实的 leap. For example, if the mean dynamics converge quickly while covariances grow, mean predictions could still be excellent. Without an operational definition, the paper's main qualitative conclusion rests on an assertion, not a demonstrated connection.

### Minor

1. **Proposition 4.1 claims "linear growth rate" but proves only a lower bound.** The paper states that differential entropy "has linear growth rate, i.e., $S \geq S_0 + ct$." A lower bound does not establish the rate — entropy could grow exponentially. The paper should say "at least linear" or provide matching upper bounds.

2. **The "deficiency" framing of differential entropy is overstated.** The paper titles Section 4 "DEFICIENCY OF DIFFERENTIAL ENTROPY" and treats entropy constancy under alternating play as a weakness of entropy itself. In reality, differential entropy is invariant under any volume-preserving/symplectic transformation (which alternating play is). This is mathematically natural — the two measures capture different aspects of uncertainty (full-distribution vs. second-moment). The real contribution is that covariances provide *complementary* information, not that entropy is "deficient."

3. **The quantity $|\mu|$ in Theorem 5.1 for Euler discretization is not specified.** The theorem states covariances are $\Theta(|\mu|^{2t})$ for some $|\mu|>1$, but does not explain how $|\mu|$ depends on the payoff matrix $A$ or step size $\eta$. This makes the result less precise than the continuous/symplectic parts of the same theorem.

## Nice-to-Haves

- The paper could strengthen its conclusions by testing the non-singular $AA^\top$ regime for symplectic discretization, where Theorem 5.1 predicts $\mathcal{O}(1)$ covariances. This is arguably the most practically interesting prediction and is completely unexplored in the experiments.
- Theorem 5.2 would be greatly strengthened by providing a definition of the linear Gromov width $w_L$, concrete bounds for it in terms of eigenvalues of $P(t_0)$, and a verifiable criterion for the "higher order differentials" bound.

## Removed Points

These points from the inputs are excluded with justification:

- *Harsh Critic claim that Theorem 5.2 does not imply $\Delta X \Delta y \geq$ constant.* **Removed (factually wrong).** From $(\Delta X \Delta y)^2 - (\text{Cov})^2 \geq c$ and $(\text{Cov})^2 \geq 0$, we directly get $(\Delta X \Delta y)^2 \geq c$, so $\Delta X \Delta y \geq \sqrt{c}$. The inequality does imply a lower bound on the product of standard deviations.
- *Criticisms about missing appendix content / deferred proofs.* **Removed (parser strips appendices from all submissions).**
- *Criticisms about missing code.* **Removed (reproducibility nitpick about artifacts impractical for submission).**
- *Missing baselines (Adam, RMSProp, Runge-Kutta, etc.).* **Removed (scope creep — the paper compares Euler vs. symplectic discretization of FTRL, not general optimizers).**
- *Formatting/typographical issues.* **Removed (parser artifacts).**
- *Complaints about step-size dependence, edge case A=0, practical implications for GANs.* **Removed (nice-to-haves, not core flaws).**
- *Strength Finder claim about "Experimental confirmation of asymptotic rates."* **Removed (conflicts with verified weakness that non-singular regime was never tested and experiments are too narrow).**

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's ambitious framing (Heisenberg uncertainty, prediction accuracy, GANs) and its actual technical contributions (sharp covariance rates for Euclidean FTRL, which are genuine but narrower than the framing suggests). Neither reviewer identified a novel synthesis beyond what the paper itself claims.

## Suggestions

1. **Expand experiments to test the non-singular $AA^\top$ regime for symplectic discretization.** Use an invertible $2\times 2$ payoff matrix (e.g., $[[2,1],[1,2]]$) and show that covariances remain bounded as Theorem 5.1 predicts. This is the most distinguishing and striking prediction of the paper.
2. **Define the linear Gromov width $w_L$** and explain how to compute or bound it from the eigenvalues of $P(t_0)$. Without this, Theorem 5.2's constant is a formal placeholder.
3. **Operationalize "prediction accuracy."** State a concrete prediction task (e.g., predicting $X_{i,\alpha}(t)$ given knowledge up to $t_0$) and show how covariance growth relates to mean-squared prediction error.
4. **Clarify Proposition 4.1** to say "at least linear growth" rather than "linear growth rate," or provide a matching upper bound.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>