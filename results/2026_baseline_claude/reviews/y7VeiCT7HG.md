## Summary

The paper proposes **Probability of Matching (PoM)**, a novel acquisition strategy for batch multi-objective Bayesian optimization (MOBO) that captures the likelihood that an acquired batch matches the true Pareto optimal set. The probability is factorized into two components: the probability that all batch points are Pareto optimal (approximated by normalized qEHVI) and the probability that they collectively cover the full Pareto set (approximated by a space-filling minimum-distance criterion). The resulting method, **qEHVI-SF**, multiplies the qEHVI acquisition value by the minimum pairwise distance within the batch and to previous observations, yielding a hyperparameter-free, diversity-promoting batch MOBO strategy. Empirical evaluation covers synthetic benchmarks and a real-world alloy inverse design task with up to six objectives, where qEHVI-SF consistently outperforms qEHVI and QSVGD.

---

## Strengths

- **Principled probabilistic decomposition.** The factorization P(X=X*) = P(X⊆X*)·P(X*⊆X | X⊆X*) provides a clean conceptual separation between candidate quality and Pareto-front coverage. This framing elegantly explains *why* hypervolume-maximizing methods like qEHVI tend to over-sample extreme Pareto solutions: they implicitly maximize P(X⊆X*) while neglecting the coverage term P(X*⊆X | X⊆X*).

- **Hyperparameter-free and simple final method.** Unlike QSVGD, which requires tuning a decaying schedule for the diversity weight η and is sensitive to this choice, qEHVI-SF avoids any additional hyperparameters. The multiplicative form in Eq. (8) is elegant, easy to implement, and adds minimal computational overhead (complexity analysis in Section 3.3 is clearly presented).

- **New design-space metric (EMD).** Expected Minimum Distance (Eq. 9) is a useful contribution: it evaluates coverage in the design space rather than the objective space, making it strictly tighter than IGD. The motivation—that covering the design-space Pareto set implies covering the Pareto front but not vice versa—is sound and practically relevant for inverse design applications.

- **Comprehensive real-world application.** The alloy inverse design case study (Section 4.2) with six material properties, six MOBO configurations (bi/tri/all objectives), and three batch sizes is genuinely thorough. Consistently superior rediscovery ratios across 20 independent trials provide strong empirical evidence.

- **Robustness to batch size.** The empirical observation that qEHVI-SF maintains stable performance across batch sizes 2, 5, and 10—while qEHVI and QSVGD show high sensitivity—is a practically significant finding.

---

## Weaknesses

### Fatal
None.

### Major

1. **The probabilistic framing is not tightly connected to the final algorithm.** The paper moves from P(X*⊆X | X⊆X*) → surrogate P(X*⊆A_X^r | X⊆X*) → maximize total volume of A_X^r → maximize minimum pairwise distance through a chain of approximations, each only loosely justified. The paper candidly acknowledges in the conclusion that "the precise relationship between pairwise distance and true coverage probability remains unclear." This is a significant gap: the probabilistic interpretation is the claimed theoretical novelty, yet the central approximation is an engineering heuristic. The method effectively reduces to **qEHVI × min_distance**, a product that could have been motivated more directly without the probabilistic scaffolding.

2. **Normalization of qEHVI as a probability proxy is unjustified.** The paper uses normalized qEHVI to approximate P(X⊆X*), but qEHVI measures expected *hypervolume improvement*, which has no direct probabilistic interpretation as the event "all batch points belong to the Pareto set." When normalized by its maximum, the quantity is dimensionless but still not a probability. This step—central to constructing the PoM—is not analyzed or bounded, and no ablation study isolates its effect.

3. **Narrow baseline comparison.** The experiments compare against only qEHVI and QSVGD. The related work (Section 2.2) explicitly mentions EMMI and IGD-NS as coverage-promoting MOBO methods, yet neither appears in any experiment. Including these would strengthen the empirical claims considerably; their absence makes the competitive landscape incomplete.

4. **Limited main-body benchmarks.** The core synthetic evaluation (Section 4.1) uses only two test problems. Standard MOBO benchmark families (ZDT, DTLZ) are relegated to the appendix. For a method contribution at a top ML venue, two problems in the main body is a thin empirical base, even if the results are consistent.

### Minor

1. **QSVGD is a user-adapted extension, not the original method.** The paper extends single-objective QSVGD to MOBO and adds a decaying η schedule. This adaptation is not standard, making it somewhat of a straw-man comparison; a reader cannot verify that this is a competitive MOBO instantiation without more details.

2. **EMD requires knowledge of the true Pareto optimal set X*.** In the synthetic and alloy benchmarks, X* is available, but the metric cannot be used for truly unknown black-box problems. A discussion of when EMD is applicable and how to estimate it approximately when X* is unknown would add practical value.

3. **Multiplicative coupling attenuates the space-filling term near initialization.** When qEHVI values are near zero early in optimization (before any good solutions are found), the coverage-promoting term in Eq. (8) contributes negligibly. Whether this causes problematic behavior in early iterations is not analyzed.

### Trivial
None worth raising.

---

## Nice-to-Haves

- An ablation study isolating the effect of the space-filling term (i.e., comparing qEHVI-SF to qEHVI alone and to a version that uses additive rather than multiplicative coupling) would clarify what the probabilistic framing actually buys over simpler diversity heuristics.
- Sensitivity analysis on the behavior of the coverage term when the Pareto set is a manifold (continuous) vs. discrete—since the surrogate P(X*⊆A_X^r) depends implicitly on the geometry of X*.

---

## Novel Insights

The most genuinely novel conceptual contribution is the explicit identification of a coverage-optimality asymmetry in existing MOBO acquisition functions: methods like qEHVI implicitly maximize P(X⊆X*) while ignoring P(X*⊆X | X⊆X*), and this asymmetry explains their observed tendency to concentrate samples on extreme Pareto solutions (where being non-dominated is easiest to ensure). This framing, though approximate in its realization, provides a crisp and communicable diagnosis of a real failure mode and suggests a principled remedy. The design-space diversity argument—that promoting coverage in the input space avoids the validity, bias, and noise-sensitivity issues that arise from diversity promotion in the objective space—is also a useful conceptual clarification, even if the idea has partial precedent.

---

## Suggestions

- Add at least EMMI or IGD-NS as baselines in the main experiments, since these are cited in Section 2.2 as the most relevant coverage-aware alternatives.
- Provide an ablation replacing the multiplicative form with an additive form (qEHVI + λ·min_dist) to assess whether the multiplicative coupling—motivated by PoM—is empirically superior.
- Analyze the early-iteration behavior where qEHVI values are near zero to determine whether the space-filling term is effectively inactive and whether a warm-up phase would help.
- Develop a more direct theoretical bound connecting min-distance to the coverage probability P(X*⊆A_X^r), even if only for structured Pareto sets (e.g., convex, Lipschitz).

---

## Score and Decision

The paper presents a meaningful and well-motivated contribution to batch MOBO. The Probability of Matching framework is conceptually clear and practically useful, and the resulting method is simple, robust, and hyperparameter-free. However, the gap between the probabilistic framing and the actual algorithm (acknowledged by the authors), the limited comparison to only two baselines, and the narrow set of main-body benchmarks prevent this from being a clear accept. The contribution is solid but not sufficiently theoretically tight or experimentally broad to merit an unconditional acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>