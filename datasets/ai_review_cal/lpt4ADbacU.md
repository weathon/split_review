- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces MoSH, a framework for multi-objective optimization (MOO) that operationalizes soft and hard bounds on each objective via piecewise-linear utility functions (HSFs). The authors propose a two-step pipeline: (1) dense Pareto frontier sampling using Bayesian optimization with a UCB-based acquisition function composed with the HSF, and (2) sparsification of the sampled set via the SATURATE robust submodular optimization algorithm. The paper provides theoretical guarantees for both steps (Theorem 1 for convergence of the dense sampling, Theorem 2 citing Krause et al. for near-optimal sparsification) and evaluates on five domains including brachytherapy treatment planning, engineering design, LLM personalization, and neural network selection.

## Strengths

- **Novel soft-hard utility formulation (Section 2.2):** The HSF operationalizes a previously unmodeled yet practically ubiquitous notion in MOO — that decision-makers have both strict lower bounds (hard) and aspirational targets (soft) for each objective. The piecewise-linear form with -∞ below the hard bound, a linear region between hard and soft bounds, a concave diminishing-returns region above the soft bound, and a saturation cap is well-motivated by the brachytherapy example (Section 1) and clearly defined in Equation (1). This goes beyond prior work on level-set estimation and constraints in MOO (Section 6) by incorporating two-tier preferences per objective.

- **Solid theory for Step 2 sparsification (Section 4):** Lemma 4.1 correctly establishes that the utility ratio \(F_\lambda(C) = \max_{x\in C} s_\lambda(u_f(x)) / \max_{x\in D} s_\lambda(u_f(x))\) is normalized, monotone, and submodular for each fixed \(\lambda\). The application of SATURATE (Theorem 2, cited from Krause et al. 2008) to the maximin problem over these submodular functions is technically sound, and the theoretical guarantee — that the algorithm finds a set whose worst-case utility ratio is at least the optimal ratio, with cardinality at most a \(\psi\) factor larger — is correctly stated.

- **Broad empirical validation across diverse real-world domains (Section 5):** The evaluation spans five distinct settings: synthetic Branin-Currin, four-bar truss engineering design, LLM personalization via proxy tuning, real cervical cancer brachytherapy, and neural network selection. Each domain has different numbers of objectives (2–4), different acquisition requirements, and different real-world stakes. The brachytherapy experiment in particular (Section 5.3.4) uses real patient data and clinical dose constraints, and the end-to-end results (Figure 7) show MoSH achieving over 3% greater SHF utility ratio than the next-best method — a practically meaningful improvement in a high-stakes medical setting.

- **Novel evaluation metrics aligned with the contribution (Section 5.2.1):** The paper proposes four soft-hard metrics (fill distance, positive samples ratio, hypervolume, distance-weighted score) that directly measure diversity, coverage, and density within the soft and hard bounded regions. These metrics are more appropriate for the HSF-guided setting than standard MOO metrics alone.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical guarantee for Step 1 (Theorem 1) requires careful verification given the HSF composition.** The theorem states \(\mathbb{E}R_B(T) \leq \frac{1}{T}\mathbb{E}R_C(T) + o(1)\) and that the Bayes SHF utility ratio converges to 1 as \(T\to\infty\), and the paper says it "follows similarly to" Paria et al. (2020). However, the acquisition function is defined as \(s_{\lambda_t}(u_{\varphi(x)})\) where \(\varphi(x) = \mu_t(x) + \sqrt{\beta_t}\sigma_t(x)\) — i.e., the UCB of each objective is computed, then the HSF \(u\) is applied, then the scalarization. The true regret uses \(s_{\lambda_t}(u_f(x_t))\) which evaluates to \(-\infty\) if any objective falls below its hard bound. A standard failure event in GP-UCB — where the UCB lies above the hard bound while the true value lies below it — would cause the acquisition function to select a point whose true utility is \(-\infty\), producing unbounded instantaneous regret. The paper does not discuss how this disconnect is handled in the analysis. The bound may still hold asymptotically (e.g., if GP confidence bounds contract fast enough that such events have vanishing probability), but the paper provides no reasoning or conditions under which this follows from Paria et al. (2020). Since the theorem motivates the dense sampling step's convergence claim, this is a significant gap.

- **The evaluation of Step 1 compares MoSH-Dense against baselines that do not use the HSF, making the comparison asymmetric.** The paper compares MoSH-Dense against EHVI, ParEGO, MOBO-RS, and random sampling on metrics specifically designed to reward coverage of the soft and hard bounded regions. These baselines optimize the original objectives (or standard scalarizations) without the HSF transformation. The claim that MoSH "generally matches or surpasses" baselines on the soft-hard metrics is therefore expected: it is testing whether HSF-guided sampling outperforms non-HSF-guided sampling on HSF-specific metrics. A more informative comparison would either (a) also provide the baselines with the HSF (i.e., have them optimize \(s_\lambda(u_f(x))\)), or (b) report standard MOO metrics (e.g., non-constrained hypervolume, IGD) alongside the soft-hard metrics to demonstrate that HSF guidance does not degrade overall PF quality. Without this, the extent of the method's advantage over simply applying existing MOBO methods to the HSF-transformed objectives is unclear.

### Minor

- **No sensitivity analysis for key HSF parameters.** The saturation parameter \(\zeta\) is set to 2.0 (Section 2.2, footnote 5) and the slope parameter \(\beta\) to an unreported value with no ablation or sensitivity study. The paper acknowledges that "many functional classes" would work but tests only one specific piecewise-linear form. The impact of these choices on method performance is not characterized.

- **Standard MOO metrics are not reported for Step 1.** The paper exclusively uses its proposed soft-hard metrics for evaluating the dense sampling step. While these metrics are well-motivated, reporting unconstrained hypervolume or IGD would allow readers to verify that focusing sampling on the bounded regions does not inadvertently harm PF coverage overall. The paper notes that EHVI "is superior in some metrics" and that "our algorithm does not surpass the baselines in all four metrics" for neural network selection, but without standard metrics these relative comparisons are hard to interpret.

- **The \(\beta_t\) exploration rate warrants justification.** The acquisition uses \(\beta_t = \sqrt{0.125 \times \log(2t+1)}\). Standard GP-UCB theory uses \(\beta_t = O(\log t)\) (without the outer square root), and the square-root-of-log form is atypical. The paper states this "followed the optimal suggestion in" Paria et al. (2019), but the reasoning is not reproduced or summarized. If this choice leads to insufficient exploration, it could explain why MoSH-Dense sometimes underperforms on diversity metrics.

- **The discretization of \(\Lambda\) for SATURATE is not specified.** The SATURATE algorithm requires a finite set of weight vectors \(\Lambda\) of size \(m = |\Lambda|\) (Theorem 2). The paper does not describe how \(\Lambda\) is constructed (e.g., uniform grid, random sampling, number of samples), which affects both computational cost \(\mathcal{O}(|D|^2 m \log(m))\) and approximation quality. This is a practical implementation detail needed for reproducibility.

- **The LLM personalization experiment is a proof-of-concept without validation of the underlying PF.** The experiment treats proxy-tuning weights \(\theta_1, \theta_2\) as decision variables but does not validate that the two-dimensional objective space (conciseness vs. informativeness) forms a well-behaved Pareto frontier. While this does not undermine the main contribution, the experiment's evidential weight is limited compared to the brachytherapy case.

### Trivial
- The claim that the method allows the DM to reach ">99% of their maximum possible desired utility within validation of 5 points" appears in the abstract and introduction but is not explicitly highlighted in a dedicated table or annotated on the Step 2 figures. The line plots in Figure 7 show values near 0.98–0.99, but exact numbers should be reported in a table.

## Nice-to-Haves
- **Re-run baselines with HSF access:** Comparing MoSH-Dense against MOBO-RS, EHVI, etc. where those methods also optimize \(s_\lambda(u_f(x))\) would isolate the benefit of the two-step procedure from the benefit of the HSF itself.
- **Sensitivity analysis for \(\zeta\) and \(\beta\):** A small ablation showing how varying these affects convergence on a synthetic problem would strengthen the paper's methodological rigor.
- **Standard MOO metrics** (unconstrained hypervolume) alongside the soft-hard metrics for at least one experiment.
- **A discussion of computational cost** for the SATURATE algorithm, particularly how the dense set size \(|D|\) and the discretization size \(|\Lambda|\) scale with problem dimension.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that the algorithm "may confidently ignore points below the hard bound leading to arbitrarily poor utility" (Critical Issue 3):** This is conceptually subsumed by the Theorem 1 concern (Critical Issue 1) and not independently actionable. The UCB is optimistic by design; the same concern applies to any UCB-based method in the presence of constraints. The paper is not framed as a safe-BO contribution, and standard GP-UCB theory handles such events through confidence-bound contraction. Merged into the Theorem 1 concern above.

- **Criticism about \(\zeta=2.0\) being "arbitrary" without sensitivity (Section-by-Section notes):** Kept in Minor as a sensitivity analysis gap. The harsh critic's framing as a "methodological gap limiting generality" is overstated — every method has tunable parameters, and the paper acknowledges other functional classes would suffice.

- **Criticism about the simulation of \(\lambda^*\) being "reasonable but arbitrary":** The simulation uses a principled heuristic (\(\lambda = \mathbf{u}/\|\mathbf{u}\|_1\) where \(u_\ell \sim \mathcal{N}(\alpha_{\ell,S}, |\alpha_{\ell,H}-\alpha_{\ell,S}|/3)\)). This is a reasonable procedure for simulating preferences near the soft bounds. Downgraded to nice-to-have for sensitivity analysis.

- **Strength Finder's claim about "theoretical guarantees for both steps":** Partially inaccurate. Theorem 2 (Step 2) is sound and correctly cited. Theorem 1 (Step 1) has the validity concern noted above. I retain the Step 2 theory as a genuine strength but remove the blanket claim about "both steps."

- **Various formatting/style nitpicks and claims about missing appendix/proofs:** Removed per parser-stripping rule (the appendix exists in the original submission).

## Novel Insights

The harsh critic's framing of the Theorem 1 gap — specifically, that the -∞ region of the HSF creates a disconnect between the UCB-based acquisition function and the true utility that is non-trivial to analyze — is an insightful observation that goes beyond what the paper discusses. This is a structural issue: the composition of the GP posterior, the HSF (with its -∞ region), and the scalarization means that the optimism condition standardly used in GP-UCB regret analysis does not straightforwardly carry over. A proper analysis would need to account for the probability that the UCB exceeds the hard bound when the true value does not, and bound the contribution of these events to the cumulative regret. This is a genuine gap in the paper as presented.

## Suggestions

1. **Address the Theorem 1 gap explicitly.** Either (a) provide the missing argument showing how the -∞ region is handled in the regret analysis (e.g., using confidence-bound contraction to bound the probability of hard-bound violation), or (b) remove the claim of "formal guarantees" for Step 1 and instead provide empirical convergence analysis. The current reference to Paria et al. (2020) is insufficient given the non-trivial HSF composition.

2. **Add a controlled experiment clarifying the benefit of the two-step HSF-guided procedure.** This could be done by re-running at least one baseline (e.g., MOBO-RS) with the HSF applied, then comparing MoSH-Dense to this "MOBO-RS + HSF" variant on the soft-hard metrics. If MoSH still outperforms, that would directly evidence the value of the two-step design beyond the HSF itself.

3. **Include a table reporting standard MOO metrics** (e.g., unconstrained hypervolume, IGD) for at least the Branin-Currin and brachytherapy experiments, to show that the HSF-guided search does not degrade overall PF quality.

4. **Report the \(\Lambda\) discretization details** (size, construction method) used for SATURATE in each experiment, and briefly discuss computational cost.
