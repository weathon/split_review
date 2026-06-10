## Summary

LD3 proposes learning the optimal time discretization for ODE-based sampling from pre-trained diffusion models by backpropagating through a differentiable ODE solver. The key innovation is a "soft teacher forcing" objective that relaxes exact input-output matching, allowing the student solver's initial noise to deviate within a small ball during training. This addresses an underfitting problem: with only ~NFE+1 learnable parameters, forcing exact matching is too restrictive. The method is lightweight (5–40 minutes on a single GPU, ~100 training samples) and consistently improves FID across 7 pre-trained models, 3+ solver types, and multiple datasets at low NFE regimes (4–10 steps).

---

## Strengths

1. **Well-motivated and practically useful method.** The idea of treating discretization points as learnable parameters and optimizing via backprop through the solver is clean and intuitive. The "soft teacher forcing" relaxation (allowing the student's input to deviate within an r-ball) is a principled solution to a genuine underfitting problem, and the ablation study (Table 3) empirically validates that $\mathcal{L}_{\mathrm{soft}}$ substantially outperforms $\mathcal{L}_{\mathrm{hard}}$ (e.g., 44% FID improvement on CIFAR10 at NFE=6).

2. **Broad and convincing empirical evaluation.** The paper evaluates across 7 pre-trained models (CIFAR10, AFHQv2, FFHQ, LSUN-Bedroom, ImageNet, Stable Diffusion v1.5, InstaFlow), 3+ solver types (iPNDM, Uni_PC, DPM_Solver++, Euler), and multiple NFE settings (2–10). LD3 consistently improves FID over default solvers and most baselines, especially at low NFE. For example, on AFHQv2 at NFE=4, iPNDM[LD3] achieves FID 9.96 vs 23.20 (default) and 12.89 (GITS). On CIFAR10 at NFE=10, iPNDM[LD3] achieves FID 2.38 vs 3.69 (default).

3. **Extreme training efficiency.** LD3 trains in 5–40 minutes on a single GPU using ~100 noise samples. Table 6 shows this contrasts sharply with distillation methods (PD: 1 day on 8 TPUs, CD: 8 A100s). This is a genuine practical advantage that makes the method accessible.

4. **Clean cross-evaluation experiment (Table 4).** The experiment shows that time steps optimized for DPM_Solver++ perform poorly on Euler (FID 42.44 vs 25.28) and vice versa. This convincingly validates the paper's claim that solver-adaptability is necessary and that LD3's solver-aware design is a meaningful feature, not a trivial addition.

---

## Weaknesses

### Major

1. **GITS baseline results are anomalously poor on latent diffusion, undermining the comparison.** In Table 2, GITS achieves catastrophically bad FID scores on LSUN-Bedroom (70–93 at NFE=4) and ImageNet (55–72 at NFE=4), far worse than the *default* solver (e.g., iPNDM default: 11.93 vs iPNDM[GITS]: 76.86 on LSUN-Bedroom at NFE=4). This strongly suggests GITS is being applied in a regime or setting for which it was not designed, or there is an evaluation mismatch. The paper offers no explanation for these anomalous results. This inflates LD3's apparent relative gains in these settings. Since GITS is a primary baseline, this needs to be addressed — either by explaining the discrepancy or re-evaluating under appropriate settings.

### Minor

2. **The theoretical guarantee is substantially narrower than the paper's presentation suggests.** Theorem 1 bounds KL divergence between teacher and student *only* under the condition that $\mathcal{L}_{\mathrm{soft}}$ attains an optimal value of *exactly zero* (line 143–144). It additionally requires both solvers to be invertible, and the bound includes an uncharacterized third term involving Jacobian determinants that the paper admits "it is hard to establish an analytic bound for" (line 150). The paper frames this as "confirm[ing]" that minimizing $\mathcal{L}_{\mathrm{soft}}$ leads to small KL divergence (line 138), but the actual result is a limiting-case consistency guarantee, not a general justification. The theoretical component should be scoped honestly.

3. **No uncertainty quantification on main FID results.** All larger comparison tables (Tables 1, 2, 3, 4) report FID as point estimates without standard deviations, confidence intervals, or significance tests. This matters because (a) training uses only 100 noise samples, so the learned discretization could vary across draws, and (b) some improvements are modest (e.g., DPM_Solver++[LD3] at NFE=10 on CIFAR10: 3.09 vs default 3.08 — actually *worse*). Without variance measures, the reader cannot assess whether reported gains are robust. The paper mentions "3 random seeds" for latent diffusion experiments but does not report the resulting statistics.

4. **The teacher ODE solver is not systematically specified per experiment.** The paper mentions "a teacher ODE solver that takes small step sizes" (line 17) and a figure caption references "100-step DDIM" (line 449), but it does not state what teacher solver/step-count was used for each of the 7 models and multiple datasets. This is a reproducibility gap.

5. **No ablation of the critical hyperparameter $r$.** The formula $r = \gamma \cdot d / \text{NFE}^2$ with $\gamma = 0.001$ (line 205) is a significant design choice. $r$ controls how much the student's input can deviate from the teacher's, and it scales with dimensionality $d$, meaning for latent-space models it can become quite large (e.g., for Stable Diffusion's latent space at NFE=4, $r \approx 1.0$). The paper provides no sensitivity analysis varying $\gamma$, which would help establish robustness and guide future users.

6. **Distribution mismatch between training and inference is not discussed.** During training, the student starts from perturbed inputs $\mathbf{x}'_T$ (within the $r$-ball), while at test time, it starts from the standard noise distribution $\mathcal{N}(\mathbf{0}, \sigma_T^2\mathbf{I})$. The theoretical bound only addresses the zero-loss case. The practical effects of this mismatch in the non-zero-loss regime are uncharacterized.

### Trivial

- At NFE=10 on CIFAR10, DPM_Solver++[LD3] (3.09) is marginally worse than DPM_Solver++ default (3.08), and DMN outperforms LD3 on two of three solvers. The claim "LD3 consistently improves generation quality across all solvers" (line 207) is slightly overstated for this specific setting.

---

## Nice-to-Haves

- Adding confidence intervals or error bars to FID tables (especially for the main results) would significantly strengthen confidence in the reported gains.
- A sensitivity analysis for $\gamma$ (the $r$ scaling factor) over, say, an order of magnitude range would demonstrate robustness.
- Specifying the teacher solver (type and step count) for each experiment in the main text would improve reproducibility.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"No comparison to simple schedule search (e.g., grid search over schedule families)"* — The paper already compares against 4 standard heuristic schedules (Time Uniform, Time Quadratic, Time EDM, Time LogSNR). Grid search over parametric families is not a standard baseline in this literature.
2. *"Table 1 conflates the claimed objective (global error optimization) with the actual objective (soft relaxation)"* — The soft objective is still a form of global truncation error optimization with relaxation; this is a overly nitpicky reading.
3. *"AYS/Watson comparison is not controlled (different pipelines)"* — The paper acknowledges using reported metrics (line 204), which is standard practice when code is unavailable.
4. *"Comparison to distillation methods is apples-to-oranges"* — Comparing best FID across methods at their respective operating points is standard; the comparison is clearly scoped.
5. Various formatting and presentation nitpicks removed per policy.

---

## Novel Insights

**The soft teacher forcing formulation reveals an underexplored trade-off in distillation-style training for ODE solvers.** Most distillation methods aim for exact input-output matching, but LD3 shows that allowing small deviations in the input can dramatically reduce the optimization burden when only a few parameters (time steps) are learnable. The cross-evaluation experiment (Table 4) provides unusually clean evidence that discretization learned for one solver type can be completely inappropriate for another — this is a finding that extends beyond the paper's own method and should inform future work on solver-adaptive sampling. None beyond the paper's own contributions.

---

## Suggestions

1. **Address the GITS anomaly.** Provide an explanation for why GITS performs so poorly on latent diffusion models, or re-evaluate under settings that respect GITS's intended usage. If the current GITS numbers are indeed valid, justify with analysis; otherwise, consider using a correctly-configured GITS as the baseline.

2. **Add error bars to the main FID tables.** At minimum, report FID with standard deviations over 3+ seeds for key results (e.g., Table 1 at NFE=4, 7, 10). This is critical for assessing the robustness of gains, especially where they are small.

3. **Honestly scope the theoretical claim.** State explicitly that Theorem 1 is a consistency guarantee (zero-loss bound) rather than a general justification that minimizing $\mathcal{L}_{\mathrm{soft}}$ minimizes KL divergence.

4. **Ablate the $r$ hyperparameter.** Show FID as $\gamma$ varies (e.g., 0.0001, 0.001, 0.01) for at least one experiment to demonstrate robustness.

5. **Specify the teacher solver** (type and step count) for each experimental setting in the main text or a clear appendix reference.

---

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>