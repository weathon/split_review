## Summary

This paper develops a dynamic generalization of the R-learner for estimating the difference of Q-functions, τ(s) = Q^π(s,1) − Q^π(s,0), in offline RL. The key methodological contribution is an orthogonal (Neyman-orthogonal) squared-loss objective whose estimation error for τ depends only on *product* errors of nuisance functions (Q, behavior policy, m), so that slower n^{-1/4} convergence of each nuisance suffices for n^{-1/2} convergence of τ. The paper further proves (Theorem 3) that this framework yields convergent policy optimization under a margin condition, even though the nuisance functions are policy-dependent. Experiments on synthetic DGPs with sparse τ and on CartPole-with-distractors illustrate the method.

---

## Strengths

1. **Product-error rates for difference-of-Q estimation (Theorems 1–2):** The analysis formally establishes that the MSE of the estimated Q-function contrast scales with product errors of nuisances (Equation 7). This is the first application of this orthogonal-learning property to the sequential difference-of-Q estimand, and the paper correctly identifies that this relaxes nuisance convergence requirements relative to direct Q-function differencing.

2. **Policy optimization bound handling dependent nuisances (Theorem 3):** The main technical novelty — showing that estimation error from *policy-dependent* nuisance functions (which arise because the estimated optimal policy changes across timesteps) is higher-order relative to τ-estimation error — is a non-trivial extension. The induction argument with the margin condition (Assumption 7) is a genuine contribution beyond applying Foster & Syrgkanis (2019) to the new estimand.

3. **Empirical adaptation to different graphical structures:** Figure 2 demonstrates that the proposed τ-TL method (ℓ₁-regularized orthogonal loss) achieves stable performance across three DGPs with very different conditional independence structures (reward-filtered, exogenous-endogenous, nonlinear main effects), while the structure-specific baselines (FQE-RewF) fail when the graphical assumptions are violated. This validates the paper's central motivation that targeting the contrast function is more robust than designing methods for specific graphical models.

4. **Clean squared-loss implementation:** The reduction of difference-of-Q estimation to a weighted squared-loss minimization (Equation 5) allows practitioners to use any black-box regression method (LASSO, neural nets, etc.), as Algorithm 1 makes concrete.

---

## Weaknesses

### Major

1. **Policy optimization (Theorem 3 / Algorithm 2) is not empirically validated.** The paper's main claimed novelty over prior orthogonal learning work is the policy optimization analysis that handles policy-dependent nuisances. Yet every experiment tests only *policy evaluation* (MSE of τ for a fixed evaluation policy). There is no experiment implementing Algorithm 2 or validating that the greedy policy derived from the estimated τ converges to the optimal policy's value. This is a serious disconnect between the paper's headline theoretical contribution and the evidence provided.

2. **The policy evaluation experiments do not consistently demonstrate advantage over simpler alternatives.** In the 1d validation (Table 1), OrthDiff-Q has MSE 2×10⁻³ vs FQE's 4×10⁻⁴ at n=5000 — the proposed method is *worse*. The paper never addresses this. In the main Figure 2 experiments, FQE-Ridge (the baseline) is acknowledged to "diverge," which undermines the informativeness of the comparison: beating a diverging baseline is not meaningful evidence. A controlled comparison against a well-behaved direct Q-difference estimator (e.g., differencing two FQE estimates) on a simple MDP where orthogonality's benefit can be isolated is absent.

3. **The claim of structural adaptivity is only partially supported.** While Figure 2 shows τ-TL working under three DGPs, the paper does not explain *why* the orthogonal loss enjoys this adaptivity in terms of convergence rates under these specific structures. The connection between the DAGs in Figure 1 and sparsity of τ is asserted but not formally proven. A rigorous argument linking the graphical assumptions to τ-sparsity would strengthen this claim considerably.

### Minor

4. **The FQE-Ridge divergence in Figure 2 is not properly diagnosed.** The paper mentions that the DGP "introduce[s] mild instability in the exogenous component" but does not verify whether the divergence is due to Bellman residual non-convergence, spectral radius > 1 in the linear system, or some other cause. Since the orthogonal τ method uses the same Ridge Q-estimates as nuisances and still performs well, understanding why FQE-Ridge diverges would clarify whether the proposed method is genuinely robust or just avoids the problem by estimating a different quantity. A simple ablation (e.g., tuning ridge regularization) would address this.

5. **The CartPole experiments (Table 2) are preliminary.** The mutual information regularization (MINE) is known to be unstable, no sensitivity analysis is given for λ_m and λ_r, and the high variance (standard errors overlapping across methods at most n) makes it difficult to draw conclusions. This experiment is presented as a proof-of-concept but the evidence is too weak to support the claim that the loss-function framework "permits more complex parametrizations."

6. **Estimation of m_t is discussed only briefly.** Algorithm 1 specifies m̂_t(s) = E_{π^b_t}[R_t + γ Q̂^π_{t+1} | S_t = s], but the paper does not discuss the practical challenges of this regression (e.g., how to average over the behavior policy's action distribution, or the fact that m_t estimation error itself affects rates). The analysis implicitly assumes m_t can be estimated at the same rate as Q, which may not hold in practice.

### Trivial

7. **Lemma 2 contains a typesetting error:** The expression "O(n^{-b_*} (2+α)/(2+α))" simplifies to O(n^{-b_*}) since the fraction equals 1, which cannot be the intended rate. This appears to be a PDF extraction artifact.

8. **Theorem 1 uses π^π to denote the evaluation policy**, which is notationally confusing (especially since π also denotes the behavior policy in other contexts).

---

## Nice-to-Haves

- Design a controlled experiment comparing τ from the orthogonal loss against τ from direct Q-differencing (subtracting two FQE estimates) under controlled nuisance misspecification, to isolate the benefit of orthogonality.
- Add a small finite-horizon policy optimization experiment (e.g., a gridworld with sparse τ differences) implementing Algorithm 2, validating that policy value converges as predicted by Theorem 3.
- Diagnose the FQE-Ridge divergence to clarify whether it reflects a real pathology or a hyperparameter issue.

---

## Removed Points

These points from the inputs were removed with justifications:

- **Harsh critic: "The experiments do not evaluate the proposed method" / "τ-TL is a two-stage heuristic, not the orthogonal loss minimization."** — Factually incorrect. The paper states (line 328): "For our methods, we solve the loss function minimization exactly with CVXPY (and ℓ₁ norm regularization)." τ-TL minimizes the orthogonal loss (Equation 5) with ℓ₁ regularization; the "reward-based thresholding" language refers to support recovery via this ℓ₁-regularized minimization, not a separate procedure. The experiments *do* implement the proposed Algorithm 1.

- **Harsh critic: "Lemma 1 is not proven or sketched, and not used anywhere."** — The proof is in the appendix (which the parser stripped). The lemma *is* referenced in the analysis (line 223: "excess risk will be an approximation error incurred from the proxy loss issue described in Lemma 1").

- **Harsh critic: "Paper does not discuss how to estimate m_t."** — Algorithm 1, step 2, specifies m̂_t(s) = E_{π^b_t}[R_t + γ Q̂^π_{t+1} | S_t = s], and line 105 mentions several standard approaches for Q-function estimation that can be adapted. The discussion is brief but present.

- **Harsh critic: "The identification and method are straightforward extensions — limited novelty."** — The paper is transparent about this, noting it is "broadly a generalization of the so-called residualized R-learner." The novelty lies specifically in the policy optimization analysis (Theorem 3) which handles policy-dependent nuisances, and in the empirical demonstration of adaptivity to multiple graphical structures. Incrementality on well-known methods is not a fatal flaw when the extension is non-trivial and well-executed.

- **Strength Finder: generic strengths** ("important problem," "addressed an interesting question") and the CartPole MI strength — the CartPole experiment is too preliminary to be a core strength; generic statements about problem importance were removed as they lack specific evidentiary anchors.

- **Strength Finder: "Extension to multiple actions and infinite horizon"** — This is a standard extension of the R-learner and the infinite-horizon variant (Algorithm 3) is described without analysis; keeping it would inflate the contribution.

---

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the experiments test τ-estimation (evaluation) rather than policy optimization is the most penetrating insight from the review process, but it is a criticism of the paper's scope, not a novel observation about the content. The calibration exercise did not surface any substantive re-interpretation of the paper's results.

---

## Suggestions

1. **Add a policy optimization experiment** implementing Algorithm 2 on a small finite-horizon MDP (e.g., a modified gridworld with sparse differences) and show that the greedy policy's value converges as n increases. Without this, Theorem 3 is a theoretical exercise disconnected from the empirical claims.

2. **Replace or explain the FQE-Ridge divergence** in Figure 2. Either tune the ridge regularization to produce a stable baseline, or provide a rigorous diagnosis of why it diverges and why the τ method avoids the problem. This would turn a confusing artifact into a genuine insight about the method's robustness.

3. **Add a direct comparison** between τ from the orthogonal loss and τ from naive FQE-differencing (same Q nuisances, no orthogonal loss) in a simple setting where the true τ is known. This would isolate the benefit of orthogonality and address the most important unresolved question about the method.

4. **Fix the Lemma 2 rate expression** and the π^π notation in Theorem 1 for clarity.

---

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| GrRo9uV3OH | 4.0 (3,5,5,3) | 1 | Weaker (no experiments); paper under review is stronger |
| iMRhuFS0Uz | 5.25 (5,5,6,5) | 1,2 | Comparable — both have good ideas with gaps in validation |
| p5o0sbE5kY | 5.5 (5,5,6,6) | 1,2 | Stronger empirically but weaker theoretically |
| 1Akd36hG9z | 5.33 (3,5,5,6,8,5) | 1 | Comparable — both have theory + experiments with gaps |
| qkVsGBff9s | 5.25 (3,6,6,6) | 2 | Better experiments, similar overall quality |
| cMIUwcEEVw | 5.0 (3,6,8,3) | 2 | Similar — interesting insight but validation limited |
| 38BBWrXUhP | 6.67 (6,8,6) | 2 | Stronger — accepted poster with well-supported claims |

**Round 1 bracket:** 4.0–6.5. The paper is clearly above the weak band (avg ~2–3) but below the strong band (avg ~8).

**Round 2 narrowing:** Anchors at 5.0–5.5 show that papers at this level have solid contributions but gaps in validation. The paper under review fits this profile: genuine theoretical contributions (product-error rates, policy optimization bound) but a significant disconnect between its main novel claim (policy optimization) and the experimental evidence (which tests only policy evaluation). It is comparable to iMRhuFS0Uz (5.25) and qkVsGBff9s (5.25) but weaker than 38BBWrXUhP (6.67, accepted), which has a clean, fully validated story.

**Final score:** 5.0 — marginally below acceptance threshold. The core ideas are sound and the paper is well-written, but the central experimental gap (untested policy optimization) and the absence of a controlled comparison demonstrating the benefit of orthogonality prevent it from being a complete contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>