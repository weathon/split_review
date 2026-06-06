## Summary

Constrained Mass Transport (CMT) is a variational framework for learning molecular Boltzmann generators that constructs intermediate distributions via two sequential constraints: a trust-region KL bound on successive densities and an entropy-decay bound. The framework yields analytical solutions characterizing geometric, tempered, and geometric-tempered annealing paths. Instantiated with normalizing flows and trained exclusively from energy evaluations, CMT is evaluated on four molecular systems up to d=219 dimensions, introducing the ELIL tetrapeptide as a new benchmark.

---

## Strengths

1. **Analytical characterization of optimal intermediate densities under joint constraints** (Propositions 2.1–2.3, Theorem 2.4, eq. 10–12): The paper analytically derives the optimal intermediate densities for each constraint regime, directly connecting constrained variational subproblems to interpretable annealing paths. The entropy constraint component and the combined geometric-tempered path are genuinely novel extensions beyond prior work.

2. **Substantial empirical improvements on the hardest systems** (Table 1): CMT achieves 29.63% ESS vs. 18.22% (TA-BG) on hexapeptide (1.63× improvement) and 26.06% vs. 13.75% (TA-BG) on ELIL (1.89× improvement), with consistent gains in EUBO across all four systems. The margins over FAB are larger still (2–3.6×).

3. **Well-designed ablation study establishing necessity of both constraints** (Figures 2–3): The ablation demonstrates that omitting the trust-region constraint causes rapid entropy collapse and mode dropping, omitting the entropy constraint yields insufficient ESS between successive intermediates, and only the combined GT variant avoids mode collapse on the Ramachandran plots.

4. **Introduction of the ELIL tetrapeptide benchmark** (d=219): The paper provides a new challenging benchmark for energy-only Boltzmann generator evaluation at the largest scale studied to date, with ground-truth MD data publicly released.

---

## Weaknesses

### Fatal
None.

### Major

- **Misleading headline claim "more than 2.5× higher ESS"**: The abstract and conclusion both state CMT achieves ">2.5× higher effective sample size." Checking Table 1 directly: against TA-BG (the closest SOTA baseline), CMT achieves 29.63/18.22 = 1.63× on hexapeptide and 26.06/13.75 = 1.89× on ELIL. The >2.5× figure is only achieved against FAB on ELIL (26.06/7.21 ≈ 3.6×) — a baseline that performs much worse than TA-BG on all hard systems. Presenting this as the general headline improvement is misleading and will cause readers to overestimate the method's advance over the true state of the art.

- **Factually incorrect claim in Section 5.2**: The text states "Across all systems and metrics, our method outperforms the baselines while requiring the same or fewer target evaluations." However, Table 1 shows that CMT's RAM TV on ELIL tetrapeptide is 3.13×10⁻² compared to TA-BG's 2.54×10⁻², which the table correctly bolds as TA-BG's win. The paper's footnote that only 2/4 TA-BG runs succeeded may partially explain this (surviving runs may be systematically better-calibrated), but this caveat is not mentioned in the main text discussion — and the blanket "all metrics" claim is still wrong as written.

### Minor

- **The symmetric entry of λ and η in Proposition 2.3 is underdiscussed**: The combined optimal density (eq. 10) is $q_{i+1} \propto q_i^{1/(1+\lambda+\eta)} \tilde{p}^{1/(1+\lambda+\eta)}$, meaning both multipliers enter through the same exponent. The paper claims these constraints serve qualitatively different roles, which is true at the level of the constraints themselves, but the actual behavior of the GT path is entirely governed by the co-evolution of dual variables $(\lambda_i, \eta_i)$, which is not analyzed or illustrated on actual molecular systems.

- **Computation cost not quantified**: Section 5.1 correctly states that computational budget is equalized by fixing target evaluations, but CMT requires fitting a normalizing flow at each intermediate step, implying potentially higher gradient-step counts than FAB/TA-BG at equal target evaluation budgets. The conclusion acknowledges this limitation but provides no quantification — not even approximate relative training times. This is important for practitioners evaluating adoption costs.

### Trivial
- The ELIL tetrapeptide benchmark is described only as having "more complex side chain interactions compared to the alanine hexapeptide." Given that this is the flagship new benchmark, a more detailed characterization (number of local minima, landscape topology, degree of side-chain flexibility) would aid reproducibility and generalizability assessments.

---

## Nice-to-Haves

- Plots of the inferred $\beta_i$ and $\alpha_i$ trajectories (Theorem 2.4) on actual molecular benchmarks would make the theoretical mechanism concrete and directly observable, connecting the illustrated 1D toy in Figure 1 to real systems.
- Analysis of sensitivity to the number of annealing steps $I$ across systems of different dimensionality — the most natural hyperparameter of the framework, currently fixed without discussion in the main text.
- A brief sketch in the main text of why the trust-region constraint is generically active as an equality (Section 2 makes this claim verbally but defers entirely to Appendix A).

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: Novelty overlap with Blessing et al. (2025) as a major issue.** The paper explicitly addresses this in Related Work: "The first explicit link between trust-region optimization and geometric annealing paths was established by Blessing et al. (2025) for path space measures in the setting of stochastic optimal control." The paper's contribution is: (a) operating in density space rather than path space, and (b) introducing the entropy constraint and the GT combined path. This differentiation is clear enough. The critic's framing as a major unaddressed issue is not supported by what the paper actually says. *Demoted to minor / informational.*

- **Harsh Critic: Ablation T variant failure analysis as a missing distinction.** The paper (Section 5.2) does explain the instability of T when H(q_0) >> H(p) and connects it to Section 2's theoretical prediction. The critic's observation that T shows lower ESS but comparable EUBO (no mode collapse) is a useful additional distinction, but the paper's explanation is not wrong — it correctly describes the insufficient-overlap failure mode. *Removed as strawman.*

- **Harsh Critic: Dimension-independent variance claim requires strong assumptions.** This claim (Section 3) is cited to Appendix C.3. Per our filtering rule, criticisms about missing appendix proofs must be removed as the parser strips these sections. *Removed.*

- **Strength Finder: "Largest system studied to date without MD samples"** — retained in Strengths but scoped accurately to the ELIL benchmark rather than treated as a universal superiority claim.

---

## Novel Insights

The ablation reveals a qualitatively interesting asymmetry: the tempered-only (T) variant achieves comparable EUBO to GT (Figure 2c — ~533.06 vs ~533.49) but substantially lower ESS to target (~15% vs ~29.6%, Figure 2d). This suggests T successfully avoids mode collapse (EUBO-wise) while still producing poor importance weights — a different failure mode than mode dropping, consistent with insufficient initial overlap rather than premature convergence. This asymmetry directly motivates the GT combination in a way the paper partially explains but does not fully name. Explicitly labeling this as an "overlap failure" distinct from "mode collapse" would sharpen the paper's theoretical narrative considerably.

---

## Suggestions

1. **Correct the headline**: Replace ">2.5× higher effective sample size" with a claim anchored to the TA-BG comparison ("~1.9× over TA-BG on ELIL, up to 3.6× over FAB") to avoid misleading readers about the actual SOTA gap.
2. **Correct Section 5.2**: Replace "Across all systems and metrics, our method outperforms the baselines" with language that acknowledges the ELIL RAM TV exception, with explicit discussion of why the TA-BG comparison on that metric should be interpreted cautiously (2/4 runs succeeded).
3. **Add a paragraph on (λ, η) co-evolution**: Show how the dual variables evolve across training on a real benchmark — this would be the most direct empirical validation of the theoretical mechanism.
4. **Quantify relative gradient steps**: Add a single sentence (or a supplementary table) reporting approximate gradient steps for CMT vs. baselines at equal target evaluation budgets.

---

## Evaluation on Key Axes

- **Originality**: Good. The entropy constraint as a hard constraint on entropy decay, and the combined GT path, are novel. The trust-region-to-geometric-path connection builds on Blessing et al. (2025) with a clear, acknowledged extension to density space.
- **Importance of research question**: High. Energy-only Boltzmann generator training is a hard, practically important problem; improvements here directly impact computational chemistry workflows.
- **Claims well supported**: Partially. The core empirical claims (ESS and EUBO improvements on harder systems) are genuinely supported. However, the headline claim overstates the margin against the best baseline, and the "all metrics" claim in Section 5.2 is factually wrong.
- **Soundness of experiments**: Good. Controlled budget, identical architectures across methods, four-run averaging, multiple metrics, a new challenging benchmark, and a well-designed ablation.
- **Clarity of writing**: Adequate. The theory section is well-structured; however, the results presentation obscures the RAM TV exception and inflates the ESS headline.
- **Value to community**: High. The method is practical, the ELIL benchmark is a genuine addition, and the ablation is instructive for future work.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>