Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper addresses the problem of integrating score-based diffusion denoisers into the ADMM plug-and-play (PnP) framework, focusing on two challenges: (i) mismatch between ADMM iterate geometry and the noisy data manifolds on which score functions are trained, and (ii) lack of convergence guarantees for score-based denoisers within ADMM. The authors propose the AC-DC denoiser, a three-stage procedure (Auto-Correction via additive Gaussian noise, Directional Correction via conditional Langevin dynamics, and Tweedie/ODE denoising) designed to progressively align ADMM iterates with score manifolds. They provide fixed-point ball convergence guarantees under both constant and adaptive step-size schedules, extending prior ADMM-PnP theory (Ryu et al. 2019, Chan et al. 2016) to score-based denoisers. Experiments across six inverse problems on FFHQ and ImageNet (super-resolution, inpainting, deblurring, phase retrieval) show consistent improvements over nine baselines.

## Strengths

- **Novel three-stage denoiser targeting a genuine problem.** The AC-DC architecture meaningfully addresses the manifold-mismatch issue specific to ADMM-PnP, where dual variables distort iterate geometry beyond what prior noise-injection methods (DiffPIR, RED-diff) handle. The ablation study (Fig. 5) provides direct causal evidence: disabling DC (J=0) leaves severe artifacts while increasing J progressively improves reconstruction, confirming that the DC step delivers on its design goal.

- **First convergence guarantees for score-based denoisers within ADMM-PnP.** Theorem 1 extends Ryu et al. (2019) to weakly nonexpansive denoiser residuals (Assumption 1), which is strictly more general than the contractive requirement. Theorems 2–3 then prove, with high probability, that the AC-DC denoiser satisfies this weak nonexpansiveness (or boundedness) condition, yielding fixed-point ball convergence. This is a genuine theoretical advance in a setting where prior analysis did not apply.

- **Consistent empirical superiority across a broad range of tasks.** Table 1 shows that both Ours-tweedie and Ours-ode variants achieve best or second-best PSNR/SSIM/LPIPS across six inverse problems on two datasets, against nine strong baselines (DPS, DAPS, DDRM, DiffPIR, RED-diff, DCDP, PMC, DPIR). The gains are often substantial (e.g., +7.9 PSNR over DCDP on FFHQ phase retrieval). Qualitative results (Figs. 2–4) confirm the improvements are visually meaningful.

- **Application breadth includes nonlinear forward models.** Unlike many score-based PnP papers limited to linear operators, the method is validated on phase retrieval (nonlinear) and motion deblurring, demonstrating generalization beyond simple measurement operators.

## Weaknesses

### Fatal

None.

### Major

1. **No reporting of computational cost undermines the quantitative comparison.** The paper does not report number of score function evaluations (NFEs) or wall-clock time per reconstruction. With J=10 DC Langevin steps per ADMM iteration plus the denoising step (Tweedie or 10-step ODE), over K ≈ 100+ ADMM iterations, the total NFEs likely exceeds 1000 — comparable or greater than typical baseline budgets (DPS uses 1000, DAPS uses 1000, DDRM uses fewer). The paper acknowledges this in Limitations ("each iteration of AC-DC denoiser needs multiple score evaluations"), but the experiments do not control for computational budget. Without a compute-controlled comparison (PSNR vs. NFE), it is impossible to determine whether the reported improvements reflect genuine algorithmic superiority or simply additional computation. This is the single most consequential evidential gap.

2. **Convergence theory assumes idealized Langevin mixing not satisfied in practice.** Theorems 2 and 3 assume the DC Langevin chain reaches its stationary distribution at each ADMM iteration. The paper states this is "for notation conciseness" with a relaxed treatment promised in Appendix E.2. However, the evaluated algorithm uses J=10 Langevin steps in 256×256 image space (~65k dimensions) — far too few for mixing. The theory therefore characterizes an idealized denoiser, not the one actually deployed. The fixed-point convergence guarantees in the abstract and title are thus qualified by an assumption that is clearly violated in the experiments. While the paper is honest about this assumption, the framing as a "convergent framework" for the practical algorithm is overstated.

### Minor

3. **The Gaussian approximation in the DC step is heuristic and empirically unvalidated.** The DC Langevin dynamics requires the conditional score ∇log p(z_ac^(k)|z_σ^(k)), which is approximated as Gaussian under the condition Var(s̃^(k))^{1/2} ≪ σ^(k). This approximation is central to the algorithm's derivation, yet the paper provides no empirical evidence that this condition holds during optimization or that the approximation error is small. The condition is not a "foundational contradiction" as one reviewer claimed — the paper never claims ADMM iterates themselves are Gaussian, and the approximation governs a specific likelihood term after AC noise injection — but it is a genuine heuristic whose scope of validity in practice is unexamined.

4. **The DPS phase retrieval result (11.63 PSNR on FFHQ) is anomalously low.** While phase retrieval is a challenging nonlinear problem and other baselines also struggle (RED-diff 15.41, PMC 10.42), DPS at 11.63 PSNR is far below typical performance ranges for this method. This raises a question about whether DPS was properly configured for this task. The paper should either justify this result or note if DPS is not well-suited to phase retrieval. This does not undermine the paper's overall empirical case (which is strong across many tasks), but it weakens the specific phase retrieval comparison.

5. **Key hyperparameter W (decay window) is not specified.** The σ schedule is defined as σ^(k) = max(0.1, 10 - (10-0.1)·k/W) with K = W+10, but the value of W is never stated in the paper. This omission hinders reproducibility and computing the total iteration count.

6. **The ablation isolates DC but does not isolate AC.** The ablation (Fig. 5) varies J (number of DC steps) but J=0 corresponds to "AC-only" — there is no comparison to a "no-correction" baseline (direct Tweedie denoising without AC or DC). The main table indirectly provides this through comparisons to DiffPIR/RED-diff, but an explicit within-method ablation would strengthen the attribution.

### Trivial

7. **Undefined notation in Algorithm 1.** The Langevin step (line 5) uses `1/σ_{z_t}^2` but σ_{z_t} is never defined in the paper. It appears to correspond to the approximated likelihood variance (σ_ac^(k) in the derivation), but the mismatch between notation and definition should be resolved.

## Nice-to-Haves

- **NFE-controlled evaluation.** A plot of PSNR/LPIPS against total NFEs (or wall-clock time) across all methods would immediately resolve whether the improvements derive from the AC-DC mechanism or from additional compute. If held to equal NFE budgets, even a partial advantage would substantially strengthen the claims.
- **Sensitivity analysis for hyperparameters.** The schedules for σ^(k), η^(k), and σ_s^(k) are chosen heuristically. A brief sensitivity study (e.g., varying the decay rate or the σ range) would improve robustness claims.
- **Empirical validation of the Gaussian approximation.** Measuring the actual residual s̃^(k) during optimization and comparing Var(s̃^(k))^{1/2} to σ^(k) would directly verify the condition underlying the DC step derivation.
- **Explicit "no-correction" ablation.** Reporting a variant that skips both AC and DC (direct Tweedie on the raw ADMM iterate) would cleanly isolate the contribution of the full AC-DC pipeline.

## Removed Points

These points were raised by reviewers but are removed after verification against the paper:

- **"Foundational contradiction between motivation and DC derivation"** — Removed. The critic argued that modeling the DC likelihood as Gaussian contradicts the claim that ADMM iterates have non-Gaussian geometry. This misunderstands the paper: (i) the ADMM iterates (`z̃^(k)`) are what have problematic geometry, (ii) the AC step injects noise to make `z_ac^(k)` closer to the score manifolds, and (iii) the Gaussian approximation in the DC step applies to a *specific conditional likelihood term* in the score decomposition, under the condition Var(s̃)^(1/2) ≪ σ^(k). The paper never models the ADMM iterates themselves as Gaussian. The approximation is a heuristic, not a contradiction, and is downgraded to Minor weakness #3 above.
- **"Table formatting artifacts"** — Removed. Repeated "PMC" entries in the table are parser artifacts from PDF extraction, not author errors.
- **"Reproducibility concerns about undisclosed hyperparameters" beyond the missing W value** — Removed. The paper provides extensive hyperparameter details (σ schedule, η, σ_s, Adam settings, convergence detection). The only missing hyperparameter is W (kept as Minor #5).

## Novel Insights

None beyond the paper's own contributions. The review surfaces no critique or observation about the paper that was not already either stated in the paper or directly following from its content.

## Suggestions

1. **Report NFE and wall-clock time** for all methods in the main experiments, and ideally include a compute-controlled comparison (PSNR vs. NFE). This single change would resolve the main evidential weakness.
2. **State the value of W** explicitly and clarify the total number of ADMM iterations.
3. **Empirically verify the Gaussian approximation condition** (Var(s̃)^(1/2) ≪ σ^(k)) by measuring the residual statistics during optimization and showing that it holds across iterations.
4. **Justify or caveat the DPS phase retrieval result** — explain the configuration and, if DPS is known to struggle on phase retrieval, state that explicitly rather than leaving readers to infer a possible configuration error.
5. **Define σ_{z_t} in Algorithm 1** or replace it with a defined symbol (e.g., σ_ac^(k)) to resolve the notation gap.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>