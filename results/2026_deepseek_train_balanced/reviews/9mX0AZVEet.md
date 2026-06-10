## Summary

This paper provides a unified interpretation showing that four recent zero-shot diffusion-based inverse problem solvers (DPS, ΠGDM, DDNM, DiffPIR) all correspond to isotropic Gaussian approximations of the intractable denoising posterior. Building on this insight, the paper proposes three methods for optimizing the posterior covariance via maximum likelihood estimation: (1) converting pre-trained reverse variances, (2) Monte Carlo estimation when reverse variances are unavailable, and (3) learning covariance in an orthonormal transform basis (DWT) for scalability. Experiments on FFHQ and ImageNet across inpainting, deblurring, and super-resolution tasks show consistent improvements over baselines.

## Strengths

- **Novel unified theoretical framework (Section 3, Table 1):** The observation that DPS, ΠGDM, DDNM, and DiffPIR — methods developed from seemingly distinct motivations (likelihood score approximation, proximal solutions, range-nullspace decomposition) — all correspond to specific isotropic Gaussian approximations of \(p_t(\mathbf{x}_0|\mathbf{x}_t)\) is genuinely insightful. This unification directly motivates the paper's core contribution: replacing hand-crafted isotropic covariances with optimized ones. The derivation linking DiffPIR's proximal problem to the mean of a Gaussian posterior under isotropic approximation (Eq. 14–16) and the connection between DDNM's range-nullspace decomposition and the \(\sigma \to 0\) limit (Proposition 3, Eq. 20) are clean and well-drawn.

- **Theorem 1 establishing a closed-form conversion between reverse variances and posterior variances (Section 4.1):** The result that \(\mathbf{v}_t^{*2}(\mathbf{x}_t) = \tilde{\beta}_t + \bigl(\frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}{1-\bar{\alpha}_t}\bigr)^2 \cdot \mathbf{r}_t^{*2}(\mathbf{x}_t)\) provides an analytical way to leverage reverse variance predictions already available in pre-trained DDPM models without any retraining. This directly enables the Convert method.

- **Scalable O(d) posterior covariance via orthonormal transforms (Section 4.3):** Parameterizing the covariance as \(\Sigma_t(\mathbf{x}_t) = \mathbf{\Psi}\,\mathrm{diag}[\mathbf{r}_t^2(\mathbf{x}_t)]\,\mathbf{\Psi}^T\) using DWT reduces complexity from \(O(d^2)\) to \(O(d)\), making learned covariance prediction practical for high-resolution images. The paper correctly contrasts this with prior high-order denoising score matching methods that were limited to small-scale datasets.

- **Consistent and often large quantitative improvements (Table 2):** The proposed methods rank first or second across nearly all 12 metric-task combinations on FFHQ and ImageNet. The gains are substantial in several cases — e.g., FFHQ inpainting FID drops from 49.46 (DPS) and 49.89 (ΠGDM) to 25.90 (Convert); ImageNet inpainting FID drops from 293.80 (TMPD) and 64.96 (ΠGDM) to 29.14 (Convert). These are not marginal improvements.

- **Practical Monte Carlo estimation for models without reverse variances (Section 4.2):** The Analytic method (Eq. 9) is simple yet effective — it requires only pre-computing the expected reconstruction error on 5% of the dataset at 1000 time steps, yet consistently ranks second-best across tasks in Table 2.

- **Compatibility with existing heuristic improvements (Table 3, Figure 5):** The proposed covariance refinement improves even the heuristic versions of ΠGDM (adaptive weight) and DPS (with various \(\zeta\) values), demonstrating orthogonality to existing engineering tricks and suggesting broad applicability.

## Weaknesses

### Major

- **The claim of "eliminating hyperparameter tuning" is overstated and contradicted by the experimental design.** The abstract, introduction, and conclusion all state the methods require no hyperparameter tuning. However, for Convert and Analytic, the paper reports that using the proposed spatial variance at all steps "results in poor performance" and resorts to a heuristic switching mechanism: use the proposed covariance only when \(\sigma_t < 0.2\) (12 out of 50 steps) and fall back to ΠGDM's isotropic covariance otherwise (lines 332–333). Even DWT-Var is used only when \(\sigma_t < 1\) for efficiency. The thresholds 0.2 and 1, the choice of ΠGDM as the fallback, and the number 12/50 are design choices that require empirical tuning. The core contribution (better covariance at low-noise steps) is valuable, but the "tuning-free" framing should be corrected to describe what the paper actually demonstrates: that replacing the isotropic covariance at low-noise steps with the proposed learned/determined covariance improves results, while existing heuristics are retained at high-noise steps.

- **Incomplete evaluation of Type II guidance.** Type II results are shown only as LPIPS on FFHQ (Figure 3), with no table providing SSIM, LPIPS, and FID scores across datasets and tasks. The paper claims "DWT-Var outperforms optimally-tuned DiffPIR by a significant margin" (line 340), but this claim rests on a single figure. Furthermore, DDNM — one of the four methods the paper unifies in Section 3 and a Type II method — is completely absent from the experimental comparison. Given that the paper's thesis is that better posterior covariance improves all four unified methods, the absence of DDNM from the evaluation is a notable gap. A full comparison with SSIM, LPIPS, and FID on both FFHQ and ImageNet is needed to give Type II claims the same evidentiary weight as Type I claims.

### Minor

- **DPS baseline in Table 1 uses a non-standard configuration.** The caption notes that "DPS here uses the step size of \(1/(2\sigma^2)\) for pure covariance comparisons." The standard DPS uses a heuristic step size \(\zeta_t = \zeta / \|\mathbf{y} - \mathbf{A}D_t(\mathbf{x}_t)\|_2\), which its authors found necessary for good performance. By evaluating DPS without its signature heuristic in the headline quantitative table, the comparison is not the one practitioners would consider representative. The paper partially addresses this with Figure 6 (comparisons against DPS with various \(\zeta\)), and the framing as "pure covariance comparisons" is transparent. However, the main text (lines 339–340) states "our methods achieve the best results in almost all tasks" based on this table without flagging the caveat prominently enough.

- **The DWT-Var learning procedure is underspecified.** The paper does not describe: (a) what neural network architecture predicts \(\mathbf{r}_t^2(\mathbf{x}_t)\) in the transform domain, (b) what loss function is used for training (presumably Eq. 7's KL objective, but this should be explicit), (c) what dataset the predictor is trained on, (d) whether it is trained per timestep or across timesteps, and (e) how many additional parameters / FLOPs it requires. This is the most practically promising of the three proposed methods (it works across more noise levels), so its incomplete specification hinders reproducibility.

### Trivial

- None.

## Nice-to-Haves

- An ablation of the switching mechanism: show results when the proposed covariance is used at all steps (the failure case), at the last \(k\) steps for varying \(k\), and with fallback to different baseline covariances. This would clarify how much of the gain comes from the covariance itself versus the switching heuristic.

- Error bars or confidence intervals on the main quantitative results. Some improvements are modest (e.g., FFHQ Gaussian deblur SSIM: 0.7905 vs 0.7890 for ΠGDM), and it would be helpful to know whether these differences are within the noise of evaluation.

## Removed Points

*These points were flagged in the inputs but removed after verification against the paper:*

1. **"Convert method's numerical instability is a meaningful practical limitation"** — REMOVED: The paper already thoroughly documents this in the Sanity Check (Section 5.1, lines 293–294), including the explanation of the 0/0 limit and diagnostic figures showing where the conversion works. The paper is transparent about this limitation; the critic's framing as a hidden weakness is inaccurate.

2. **"Plug-and-play framing at odds with actual usage"** — REMOVED: Convert and Analytic genuinely require no retraining (they operate on pre-trained models' outputs). The switching mechanism is a practical accommodation for the diagonal approximation's breakdown at high noise, not a retraining requirement. The paper clearly distinguishes DWT-Var as requiring learning, which is consistent with the framing.

3. **"Theorem 1 proof not shown"** — REMOVED: Per the review guidelines, proofs deferred to the appendix should not be counted as a weakness, as the parser strips appendices from all papers. Parameters \(\tilde{\mu}_t, \beta_t, \bar{\alpha}_t\) are standard DDPM notation and defined in the DDPM literature the paper references.

4. **"Statistical significance not reported"** — REMOVED: Single-run evaluation on standard benchmarks (SSIM, LPIPS, FID) without error bars is the norm in this subfield. Demanding confidence intervals here applies a standard not used in comparable works.

5. **"CG solver not described"** — REMOVED: Trivial implementation detail not central to the paper's contribution.

6. **Strength: "This paper addressed an important problem"** — REMOVED (from Strength Finder output): generic and superficial; not specific to this paper's content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Reframe the "tuning-free" claim to match what is actually demonstrated: the proposed covariance refinement improves results when replacing isotropic covariance at low-noise steps, while retaining existing methods' covariances at high-noise steps. This is still a compelling contribution.

2. Add a full Type II evaluation table with SSIM, LPIPS, and FID on both FFHQ and ImageNet for all Type II methods, including DDNM as a baseline and showing improvements from the proposed covariances.

3. Either include the standard DPS (with its heuristic step size) alongside the "pure covariance" DPS in Table 1, or clearly state in the main text that Table 1 compares covariances under a simplified DPS, and defer the fair comparison to Figure 6.

4. Provide full specification of the DWT-Var training procedure: architecture, loss function, training data, timestep handling, and parameter count.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>