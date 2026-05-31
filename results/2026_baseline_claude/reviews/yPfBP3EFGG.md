## Summary

This paper proposes STNAdam (Stochastic Two-track Nesterov-accelerated Adaptive Momentum Estimation), an enhanced Adam variant for solving "nonconvex + weakly-convex" composite optimization problems. The core novelty is a two-track iteration framework that maintains two interleaved trajectories—an extrapolation track driven by Nesterov momentum and a regular update track using Adam-style adaptive conditioning. Under the Kurdyka-Łojasiewicz (KL) property, almost-sure global convergence and explicit convergence rates are established for iterates driven by arbitrary variance-reduced gradient estimators (SVRG, SAGA, SARAH). Empirical evaluation is conducted exclusively on low-light image enhancement (LIE) tasks.

---

## Strengths

- **Generalized problem class:** The analysis addresses the "nonconvex + weakly-convex" composite structure (equation 1), which subsumes purely nonconvex problems and indicator-constrained problems. This is a meaningful generalization over existing Adam-convergence results that focus on strongly convex or purely nonconvex settings.

- **Flexible variance-reduction interface:** The abstract Lemma 1 (MSE bound, geometric decay, and estimator convergence) provides a clean unified interface that accommodates SAGA, SARAH, and SPIDER simultaneously, without duplicating proofs for each estimator. This design is practically valuable and conceptually tidy.

- **Explicit convergence rates under KL:** Theorem 2 provides three rate regimes depending on the KL exponent $\vartheta$—linear convergence for $\vartheta \in (0, \tfrac{1}{2}]$, sublinear for $\vartheta \in (\tfrac{1}{2}, 1)$, and finite identification for $\vartheta = 0$. This mirrors established KL-rate theory, but the derivation for the adaptive two-track setting requires non-trivial energy-function construction (equation 9).

- **Empirical ordering is internally consistent:** Within the LIE domain, the relative ordering STNAdam-SARAH > STNAdam-SAGA > STNAdam-SGD consistently holds across PSNR, SSIM, and LPIPS on both the main table and the noisy-image ablation (Tables 2–3), lending credibility to the variance-reduction benefit.

---

## Weaknesses

### Fatal
None identified that fully invalidate the theoretical claims.

### Major

1. **Experiments restricted to a single niche domain and one dataset.** STNAdam is presented as a general-purpose optimizer, yet the entire empirical section is devoted to LIE on the LOL dataset with a specific Retinex-Net training setup. ICLR readers will expect demonstrations on canonical ML benchmarks (e.g., image classification on CIFAR-10/ImageNet, language modeling, or graph learning) to assess whether the optimizer generalizes. Without this, it is unclear whether the gains on LIE stem from the optimizer's general properties or from its interaction with the particular LIE loss structure.

2. **Apples-to-oranges comparison inflates apparent advantage.** Table 2 mixes general-purpose optimizers (SGD, SAdam, SNAdam, STNAdam) with specialized LIE algorithms (NPE, DeHz, LIME, Retinex-Net, LR3M). Specialized methods are designed around fundamentally different objective formulations and inference-time procedures, not around minimizing equation (14) using gradient descent. Showing that a general optimizer outperforms a tailored Retinex decomposition method does not demonstrate optimizer superiority; it primarily shows that model (14) with STNAdam provides a good training signal. The comparison should be restricted to other optimizers applied to the same model and training setup.

3. **Missing comparison rates vs. existing methods.** Theorem 2 establishes convergence rates, but the paper does not compare these rates explicitly with those of NAdam, SNAdam, or other Adam variants in an equivalent setting (same problem class, same assumptions). The reader cannot determine whether the two-track framework actually yields a faster theoretical rate, which would be the key scientific payoff of the analysis.

4. **Practical complexity of adaptive parameter intervals.** The lower bounds in equations (6)–(8) depend on $V_1, V_\Upsilon, \rho, M, s, L, \tau$—quantities that require knowledge of Lipschitz constants, weak-convexity moduli, and gradient estimator constants. The claim in contribution (ii) that parameters "can be dynamically scheduled... removing hand-tuning" is overstated: computing these bounds in practice requires either knowing or estimating these constants, which is at least as burdensome as hand-tuning for most practitioners.

### Minor

1. **Missing Step 4 in Section 3.** The convergence analysis labels Steps 1, 2, 3, and 5, skipping Step 4 entirely. This appears to be either a numbering error or a missing intermediate result.

2. **"SAdam" attribution inconsistency.** Table 2 labels the Adam baseline as "SAdam" and cites Kingma & Ba (2014), but the introduction defines SAdam as the Wang et al. (2019) strongly-convex variant. The two are different algorithms; this mismatch may mislead readers.

3. **Assumption of convergence in Theorem 2.** Theorem 2 opens with "Let $\{\tilde{x}^k\} \to \tilde{x}^*$," treating convergence of the output sequence as a premise, whereas Theorem 1 establishes convergence for $\{\bar{x}^k\}$. The relationship between the two sequences and why $\{\tilde{x}^k\}$ must also converge is not made explicit in the main text.

### Trivial

- Termination criterion ($\|\tilde{x}^{k+1} - \tilde{x}^k\| \leq 10^{-6}$) in Remark 1(ii) is stated without justification for the specific constant.

---

## Nice-to-Haves

- Provide ablation experiments isolating the two-track mechanism from variance reduction: compare (a) single-track STNAdam (collapsing to NAdam) vs. (b) two-track STNAdam, both with the same estimator, to quantify the contribution of each component.
- Report convergence curves (loss vs. iteration) to illustrate that the two-track framework converges faster, not just to a better final value.
- Include at least one standard deep learning benchmark (e.g., ResNet on CIFAR-10) to demonstrate general applicability and comparison with AdamW.

---

## Novel Insights

The two-track coupled iteration design—where the output iterate $\tilde{x}^{k+1}$ is computed from a weighted interpolation of the current iterate and the previous output, while the "shadow" iterate $x^{k+1}$ maintains momentum for the next step—is a structurally interesting generalization of Nesterov's look-ahead idea. When combined with an adaptive step size, it attempts to exploit a larger neighborhood for each proximal update without fully committing to the extrapolated point, which may offer implicit regularization benefits in nonconvex landscapes. However, because the paper's empirical scope is narrow, whether this mechanism provides genuine advantages beyond standard Adam variants on representative ML tasks remains an open question.

---

## Suggestions

- Add at least one optimizer benchmark experiment (e.g., training a ResNet on CIFAR-10 or a Transformer on a text task) comparing STNAdam-SARAH against AdamW and NAdam under identical hyperparameter search budgets.
- Fix the Step 4 numbering gap in Section 3.
- Clarify the "SAdam" labeling inconsistency across the paper.
- Restrict Table 2's comparison to general-purpose optimizers applied to the same LIE model, and move the specialized LIE method comparison to a separate table explicitly framed as "application-specific baselines."
- Explicitly state and prove (or cite) that $\{\tilde{x}^k\}$ converges before invoking its limit in Theorem 2.

---

## Score and Decision

The paper provides a technically competent convergence analysis for a novel two-track Adam variant in the "nonconvex + weakly-convex" composite setting, which is a meaningful theoretical contribution. However, for ICLR—a venue where the ML community expects general optimizer claims to be validated across representative learning tasks—the empirical contribution is insufficient: a single niche application (LIE on LOL) with a methodologically flawed comparison framework cannot support the broad claims made. The missing theoretical rate comparison and the practical inaccessibility of the adaptive parameter bounds further weaken the case for acceptance.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>