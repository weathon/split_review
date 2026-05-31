## Summary

This paper introduces **Constrained Mass Transport (CMT)**, a variational framework for learning molecular Boltzmann generators by constructing sequences of intermediate distributions that bridge a tractable base measure and the target. The core idea is to formulate each annealing step as a constrained optimization: a trust-region constraint bounding KL divergence between successive distributions (yielding geometric annealing paths with automatic schedule tuning), an entropy constraint limiting entropy decay (yielding tempered annealing paths), and a hybrid combining both (geometric-tempered paths). Analytical solutions to all three constrained problems are derived, and the framework is instantiated with normalizing flows. CMT consistently surpasses baselines (FAB, TA-BG) across four molecular benchmarks including a newly introduced ELIL tetrapeptide (d=219), achieving over 2.5× higher ESS on larger systems.

---

## Strengths

- **Clean theoretical derivations with analytical results.** Propositions 2.1–2.3 and Theorem 2.4 provide closed-form solutions to all three constrained variational problems, establishing a precise correspondence between constraint types and annealing path families. This is a satisfying unification: trust-region → geometric path, entropy → tempered path, both → geometric-tempered path.

- **Strong and consistent empirical results across scale.** Table 1 demonstrates improvements in EUBO, ESS, and RAM TV across alanine dipeptide (d=60), tetrapeptide (d=120), hexapeptide (d=180), and ELIL tetrapeptide (d=219) using the same budgets and architectures as baselines. On the two hardest systems, CMT achieves roughly 2× higher ESS and dramatically better EUBO versus FAB and TA-BG (e.g., hexapeptide ESS: 29.63% vs 18.22% for next-best TA-BG).

- **Principled ablation study.** Figure 2 and Figure 3 directly demonstrate why both constraints are necessary: no trust-region → rapid entropy collapse and mode collapse; entropy constraint only → unstable training with violated entropy decay; both together → stable entropy decay and highest ESS. The Ramachandran plots in Figure 3 make mode collapse visually concrete.

- **New benchmark contribution.** The ELIL tetrapeptide (d=219) is presented as the largest molecular system tackled with purely energy-based variational methods. The ground-truth MD data is publicly released, which is a tangible community contribution.

- **Practical scalability argument.** The paper argues (and supports in Appendix C.3) that the trust-region constraint keeps importance-weight variance approximately constant with respect to dimension d. The Lagrangian dual optimization cost is negligible (~0.01% of training on alanine dipeptide).

---

## Weaknesses

### Fatal
None.

### Major

- **Inconsistent performance on the flagship new benchmark.** On ELIL tetrapeptide (the paper's largest and most complex system), CMT achieves better EUBO and ESS but *worse* RAM TV than TA-BG (3.13 × 10⁻² vs. 2.54 × 10⁻²). The paper acknowledges this in the table boldface but does not analyze it. Since RAM TV directly measures mode coverage quality via comparison to MD ground truth, this discrepancy deserves substantive discussion: does better ESS not imply better mode coverage at d=219, or is this an artifact of the fixed computational budget?

- **Entropy constraint solution (Proposition 2.2) is independent of qᵢ.** The optimal intermediate density for the entropy constraint is $q_{i+1} \propto \tilde{p}^{1/(1+η)}$, which depends only on the target $\tilde{p}$ and not on the current iterate $q_i$. This means successive "tempered" steps are not truly sequential — they all independently find a tempering of $p$, making $\beta$ in $q_i \propto q_0^{1-\beta_i}\tilde{p}^{\beta_i}$ collapse to 0. The paper acknowledges the resulting instability (large KL between $q_0$ and $q_1$) but the theoretical framing as a "sequential constraint on entropy decay" is somewhat misleading since $q_i$ doesn't appear in the solution at all. A sharper discussion would clarify why the entropy-only variant is still useful and when it is preferred.

### Minor

- **Sensitivity analysis for ε_tr and ε_ent is absent in the main paper.** The method introduces two new hyperparameters. While the appendix contains some analysis, the main text leaves open how sensitive CMT is to their values, especially across different dimensionalities.

- **Forward KL baseline has an unfair data advantage** (uses MD samples). This is noted in the caption, but it mixes data regimes in the same table. A brief discussion of the performance gap this implies would be useful.

### Trivial
None worth mentioning.

---

## Nice-to-Haves

- A comparison showing training curves (not just final metrics) for CMT vs. TA-BG on ELIL tetrapeptide could clarify whether CMT converges faster or just converges to a different optimum.
- An experiment with the geometric-tempered path applied to non-molecular targets (e.g., Gaussian mixtures or funnel distributions) would strengthen the claim that CMT is a general sampling framework, not just a molecular BG method.

---

## Novel Insights

CMT makes a genuinely novel connection between constrained distributional optimization (via Lagrangian duality) and the *type* of annealing path generated: trust-region constraints induce geometric annealing paths (recovering the result of Blessing et al. 2025 in a new setting), entropy-decay constraints induce tempered paths, and combining both yields a new geometric-tempered path with independent automatic tuning of both the annealing schedule (β) and temperature schedule (α). The proof that the dual problems have unique, analytically tractable optima, and the demonstration that these jointly control mass teleportation and premature convergence, is a clean theoretical contribution. The practical consequence — that two lightweight scalar hyperparameters replace the entire schedule-tuning problem of geometric annealing — is directly validated by the ablation in Figure 2.

---

## Suggestions

- Discuss in the main text why CMT's ESS advantage does not translate to better RAM TV on ELIL tetrapeptide; this is the most important unresolved tension in the empirical results.
- Clarify in Section 2 that the entropy-constraint solution is independent of $q_i$, and explain why iterating it still produces a meaningful sequential path (i.e., through the dependence of $\eta_i$ on the Monte Carlo estimate under $q_i$, not through the functional form).
- Consider reporting confidence intervals or error bounds for the RAM TV metric more explicitly, since the difference between CMT and TA-BG on ELIL (3.13 vs. 2.54) could depend on MD sample quality.

---

## Score and Decision

CMT offers a well-motivated theoretical framework with clean analytical results and consistent empirical improvements on challenging benchmarks. The key results scale favorably with system complexity, the ablation is rigorous, and the new benchmark with public MD data adds lasting value. The main concerns — the RAM TV regression on ELIL and the somewhat ambiguous role of the entropy-only variant — are real but do not invalidate the core contribution. This is a solid, above-average paper.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>