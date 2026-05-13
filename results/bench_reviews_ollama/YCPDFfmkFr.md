## Summary
The paper introduces an Extended Conservative Jacobian (ECJ) framework for differentiating convex QP layers in both feasible and infeasible regimes, based on an augmented-Lagrangian / slack-variable reformulation (QP-H) whose KKT map is shown to be path differentiable. The authors derive forward/backward algorithms, prove consistency with the standard Jacobian under standard non-degeneracy and strict complementarity (Lemma 3), and release an open-source C++ implementation (QPLayer) built on ProxQP. The empirical contribution is a Sudoku learning experiment where QPLayer outperforms OptNet/CvxpyLayer and can train a layer with a learned equality constraint matrix that becomes feasible at test time.

## Strengths
- The change-of-variables in the KKT map $G$ (Eq. (2)) that absorbs the slack $s$ yields a tractable, path-differentiable system (Lemma 2), giving a clean handle on the infeasible regime that prior frameworks (OptNet, CvxpyLayer) cannot address.
- Lemma 3 provides a clean correctness check: under invertible KKT matrix of active constraints and strict complementarity, the ECJ recovers the standard Jacobian — so the new construction does not degrade the feasible case.
- The "learn A" Sudoku experiment (Sec. 4.1.2, Fig. 5b) is a genuinely interesting qualitative demonstration: by penalizing $s^\star$ during training, the learned $A$ converges to satisfying $Ax=1$ at test time, while OptNet's violation saturates around $10^{-3}$. This is concrete evidence that differentiating through infeasible QPs can drive a layer to feasibility.
- The C++ implementation built on ProxQP is a tangible deliverable enabling practical use.

## Weaknesses

### Fatal
None.

### Major
- **Theoretical contribution is admittedly incomplete in the regime that distinguishes the paper.** Section 3.4.3 explicitly states: "we have not proved that we could apply the chain rule to ECJs in the general case," "it should be confirmed that ECJ indeed reduces to CJ," and that IFT applicability in the infeasible setting is "one major unresolved gap." Assumption 2 of Section 3.4.1 simply *assumes* path differentiability of $x^\star, z^\star, t^\star$ rather than establishing it. Since Lemma 3 only covers the feasible, non-degenerate case (which is essentially Amos & Kolter), the headline "unified approach" is, by the authors' own admission, currently conjectural in the infeasible regime — exactly where the paper claims novelty.
- **Empirical support for the central claim rests on a single benchmark.** The abstract advertises "superior predictive performance in some conventional learning tasks" and motivates the work with "learning, control and robotics," but the main paper contains exactly one learning experiment (Sudoku, Sec. 4.1) — the same benchmark used by OptNet (Amos & Kolter, 2017). No control or robotics task appears in the main text. A single combinatorial problem cannot support a general expressiveness/predictive-power claim about infeasible-QP differentiation.
- **The "infeasibility" claim is not cleanly isolated.** Two distinct contributions are conflated in Fig. 4: (a) being able to learn an LP / degenerate QP (which already explains much of the gap with OptNet, since OptNet must add a PD regularizer), and (b) differentiating through infeasible QPs (only relevant in the "learn $A$" variant). The OptNet-learn-A baseline is structurally disadvantaged by the same PD regularization requirement that the authors themselves identify. Without an ablation that adds, e.g., a soft $\|Ax-1\|^2$ penalty in a standard formulation, it is hard to separate "ECJ machinery does real work" from "the slack penalty drives feasibility on its own."
- **Assumption 3 is very strong and never analyzed.** Sec. 3.4.1 requires $s^\star > 0$ ("all constraints are primal infeasible") plus $C$ full column rank and loss independent of $z^\star$. In any realistic learned QP, only a subset of constraints will be infeasible. The paper does not characterize backward-pass behavior when this assumption fails, even though the algorithm is deployed in experiments where it generically will fail.

### Minor
- **Speed claim is not at parity.** The "0.45 s vs 8.99 s per batch" comparison (end of Sec. 4.1.2) is between a C++ implementation and OptNet's Python/Qpth — language/implementation differences plausibly account for much of the gap. A C++-vs-C++ baseline or comparison against a compiled alternative (DiffOpt.jl, JaxOpt) would make the speedup informative.
- **No comparison to other infeasibility-capable frameworks on the "learn A" task.** CvxpyLayer, Alt-Diff, JaxOpt, and DiffOpt.jl are all named in Sec. 2 but only OptNet is compared on the infeasibility-handling task.
- **The $s^\star$ penalty weight is unspecified** and lacks sensitivity analysis — important since this is the actual mechanism driving feasibility at test time.
- **Assumption 1 (orthogonality of $g$ to the recession cone)** is never empirically checked for the learned-$C(\theta)$ setting where it is a non-trivial training-time condition.

### Trivial
- The abstract should explicitly flag the theoretical gaps that Sec. 3.4.3 candidly acknowledges; "unified approach" currently overstates the proven scope.

## Nice-to-Haves
- A second learning task — ideally a control or robotics problem aligned with the introductory motivation.
- Ablation: add a soft $\|Ax-1\|^2$ penalty in a feasibility-enforced QP and compare with the ECJ-with-$s^\star$-penalty approach to isolate the contribution of differentiating through infeasibility.
- Even a partial closing of the Sec. 3.4.3 gap (e.g., chain rule for the "$s^\star_i>0$ on a fixed active set" subclass).
- Trajectories of $\|s^\star\|$ during training across seeds to characterize the dynamics of driving toward feasibility.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Reviewer references to "parser-broken numerals" pointing to appendix sections** (e.g., "1 provides... 2 contains... 3 illustrates...") are parser artifacts, not author errors; concerns about the appendix content being absent should not be held against the paper.
- Generic strength claims about the problem being "important" / the framework being practically useful were filtered as they are not concretely paper-specific beyond what is already kept.

## Novel Insights
None beyond the paper's own contributions. The genuinely novel observation — that one can train a QP layer through *infeasible* iterates and recover a feasible model at test time by penalizing $s^\star$ — is the paper's own contribution.

## Suggestions
- Tighten Sec. 3.4.3: at minimum prove ECJ ⊃ CJ in the feasible case (likely already implicit in Lemma 3) and a chain rule on a restricted infeasible subclass.
- Add at least one non-Sudoku learning task (a small control benchmark would directly support the motivation).
- Provide an ablation isolating the $s^\star$ penalty from the ECJ derivative machinery.
- Run a C++-vs-C++ timing comparison so the 20× speedup is interpretable.
- Discuss / empirically probe behavior when Assumption 3 fails (mixed feasible/infeasible constraints).

---

**Overall.** Originality is real: differentiating through infeasible QPs via a slack-augmented KKT map is a fresh and useful idea, and the open-source artifact strengthens the contribution. The research question is well-motivated and of interest to the differentiable-optimization community. However, the claims are only partially supported: the theoretical justification in the infeasible regime is openly incomplete (Sec. 3.4.3), and the empirical case is limited to a single Sudoku setup against a structurally disadvantaged baseline. Soundness of experiments is adequate for what is shown but does not support the breadth of claims in the abstract/introduction. Clarity is reasonable. Value to the community is meaningful primarily through the released C++ library and the "learn $A$" qualitative finding. The paper has a real contribution but needs either tightened theory or substantially broader experiments to fully establish its central thesis.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>