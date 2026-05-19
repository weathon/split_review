- Decision: Accept
- Avg Score: 5.71
- Scores: 3, 6, 6, 8, 6, 6, 5
I have read the full paper (210 lines extracted). Key observation: the results sections (toy_experiment.tex, multigoal_experiments.tex, mujoco_experiments_param) and figures are included via `\input` commands and are **stripped by the parser** — they existed in the original PDF submission. Per the rules, I must not penalize the paper for missing content that was stripped during extraction.

Now I will produce the final consolidated review.

---

## Summary

This paper proposes S²AC (Stein Soft Actor Critic), a maximum-entropy RL algorithm that models the policy as an SVGD-based sampler from an energy-based model over Q-values. The key theoretical contribution is a closed-form, computationally efficient entropy expression for SVGD-based policies (Theorems 1 and 2) that depends only on first-order derivatives and vector products, bypassing the intractable entropy of EBMs. The paper justifies the choice of SVGD over alternative samplers (SGLD, HMC) by proving its invertibility, and introduces a parameterized initialization to reduce the number of SVGD steps. Empirical results (toy experiments, multi-goal environment, MuJoCo) are claimed to show that S²AC outperforms SAC and SQL.

## Strengths

1. **Closed-form entropy for SVGD-based policies (Theorems 1 & 2)**: The paper derives a tractable entropy approximation (Eq. 9) that avoids costly matrix operations and depends only on first-order vector products. This directly addresses an open problem in MaxEnt RL — computing entropy of expressive EBM policies — and is the paper's central theoretical contribution. The formula is derived from the change-of-variable formula under the invertibility assumption, which is justified by Proposition 1 (SVGD invertibility under a mild condition).

2. **Invertibility analysis of EBM samplers (Propositions 1 & 2)**: The paper rigorously shows that SVGD is invertible (diagonally-dominant Jacobian under ε ≪ σ) while SGLD (stochastic noise) and HMC (requires velocity conditioning and Hessian computation) are not. This justifies the choice of SVGD and explains why the derived entropy formula would not be straightforwardly obtainable with other samplers — a clean theoretical contribution.

3. **Parameterized initialization bridging SVGD and SAC**: Modeling the initial SVGD distribution as a learned isotropic Gaussian (with L=0 reducing to SAC) is a practical design that connects expressivity to computational cost. The paper correctly notes that this enables amortized inference at test time.

4. **Sound motivation and clear positioning**: The paper clearly articulates the tension between policy expressivity and tractable entropy in MaxEnt RL, and positions S²AC as addressing both requirements simultaneously. The related work section thoroughly surveys alternatives (SAC-GMM, SSPG, SAC-NF, IAPO) and explains why they fall short.

## Weaknesses

### Fatal
None.

### Major

1. **Truncation-via-selection creates a mismatch between the entropy formula and the actual policy distribution**: The paper constrains particles to stay within \([-t\sigma_\theta, t\sigma_\theta]\) at every SVGD step by discarding those that exit the bounds and "sampl[ing] more particles than we need and select[ing] the ones that stay within the range" (line 99). The paper acknowledges this in a single sentence ("the constraint does not truncate the particles as it is not an invertible transformation"), but this acknowledgement does not resolve the issue. The surviving particles are a **conditional sample** from \(q^L\) given that the entire trajectory stayed within bounds. The entropy formula (Eq. 9) was derived for the untruncated \(q^L\), yet the actual policy uses a different distribution. The magnitude of this mismatch is neither quantified nor bounded. While a wide bound (\(t=3\)) likely makes the effect small for approximately-centered distributions, the paper provides no analysis (empirical or theoretical) of how many particles are discarded in practice, how this affects the entropy estimate, or what conditions make the approximation reliable. This undermines the theoretical justification of the entropy estimator used in the actor loss.

2. **Limited baseline comparisons**: The empirical evaluation compares S²AC only to SAC and SQL. The paper's own related work section discusses SSPG, SAC-NF, IAPO, and SAC-GMM as non-Gaussian alternatives that also aim to improve policy expressivity. The paper dismisses SSPG and SAC-NF as unstable (citing prior work), but the strongest evidence for S²AC's advantage would be a direct comparison showing it avoids those instabilities. The lack of even one non-Gaussian baseline (a GMM policy, for instance) weakens the claim that S²AC provides a "more optimal solution to the MaxEnt RL objective." (Note: the MuJoCo and multi-goal result sections were stripped by the parser; but even if they contained full tables, the missing baselines concern a methodological gap in the experimental design, not the reported numbers.)

### Minor

1. **Approximation error of Theorem 1 is not characterized**: The theorem states an \(O(\epsilon^2 d L)\) error term for the entropy approximation. The paper does not analyze this error numerically — no plot of error vs. \(\epsilon\), \(d\), \(L\), or kernel bandwidth is described in the main text. The Introduction mentions a "sanity check on target distributions with known entropy values" (stripped by the parser), but given that the tractable entropy is the paper's core contribution, a quantitative error analysis in the main paper (or accessible in the extracted text) would substantially strengthen the claims.

2. **Proof sketch for Theorem 1 is effectively empty**: The proof sketch (line 118) is just "~\eqref{eq:generic_entropy}" — a reference to the equation itself, not a sketch. While the full proof may be in the appendix (stripped by the parser), the main text should provide a meaningful sketch of the derivation (e.g., first-order Taylor expansion of the log-determinant). This is a presentation shortcoming in a paper whose main claim depends on this theorem.

### Trivial
- The proof sketch for Proposition 1 states "We use the explicit function theorem" — this should be "implicit function theorem."
- Line 99 has a grammatically tangled sentence ("Note that the constraint does not truncate the particles as it is not an invertible transformation which then violates the assumptions of the change of variable formula") that is difficult to parse and should be rephrased.

## Nice-to-Haves
- A sensitivity analysis of the truncation threshold \(t\) and how it affects both entropy accuracy and policy performance.
- Wall-clock time comparison between S²AC, SAC, and SQL to substantiate the "small overhead" claim.
- An ablation on the number of SVGD steps \(L\) (the paper uses \(L=3\) throughout) to understand the trade-off between expressivity and computational cost.

## Removed Points
These points are flagged to be removed; treat them with caution:

- **Criticism that results lack numbers/stds/learning curves and "insufficient evidence"**: The Results sections are included via `\input{Results/...}` commands — these were compiled into the original PDF but stripped by the parser. The paper explicitly states in the Introduction that it conducts toy, multi-goal, and MuJoCo experiments with quantitative evaluation; the tables, figures, and numeric claims existed in the original submission. Per the review guidelines, parser-stripped content should not be held against the paper.
- **Criticism about missing proof in appendix**: Proofs likely exist in the appendix (stripped by parser). The rule explicitly states to remove such criticisms.
- **Criticism that truncation issue "invalidates the theoretical foundation"**: Overstated. The paper acknowledges the issue; the concern is real but not fatal — it requires quantification, not a redesign. Downgraded from "fatal/structural" to Major.
- **Strength Finder claims #2 and #3 (MuJoCo and multi-goal results as direct evidence)**: These are based on claims from the Introduction that reference parser-stripped sections. They are genuine strengths of the original submission but cannot be directly verified from the extracted text alone.
- **Generic strengths about "important problem" and "well-motivated"**: Removed as generic/superficial; the strength finder's core strengths 1, 4, 5 (closed-form entropy, parameterized init, invertibility analysis) are retained as they are specific, concrete, and verifiable.

## Novel Insights
None beyond the paper's own contributions. The synthesis of reviews does not reveal a perspective on the paper that the authors themselves do not already articulate.

## Suggestions
1. **Quantify the truncation effect**: Provide an empirical analysis showing (a) the fraction of particles discarded per state throughout training, and (b) how much the entropy estimate changes when computed on the full \(q^L\) vs. the truncated (selected) distribution. If the discrepancy is small, this would justify the heuristic; if not, consider replacing the hard selection with a differentiable squashing function.
2. **Add at least one non-Gaussian baseline**: Run SSPG or SAC-NF on the multi-goal environment (or at minimum a GMM policy) to demonstrate that S²AC's improvements come from its specific design rather than simply having a more expressive policy than Gaussian.
3. **Characterize the \(O(\epsilon^2 d L)\) error**: Include a figure showing the relative entropy approximation error for a tractable target (2D/5D Gaussian, GMM) as a function of \(\epsilon\), \(L\), and kernel bandwidth.
4. **Expand the proof sketch for Theorem 1**: Provide a brief derivation in the main text showing how the log-determinant Taylor expansion leads to the trace expression.
5. **Clarify the constraint handling mechanism**: Rewrite the sentence about truncation to clearly explain why the selection step does not affect the entropy computation for \(q^L\), and discuss the regime where the approximation is accurate.
