Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes the AC-DC denoiser, a three-stage mechanism (auto-correction via additive Gaussian noise, directional correction via conditional Langevin dynamics, and score-based denoising) to address the manifold mismatch problem when integrating score-based diffusion denoisers into ADMM plug-and-play frameworks. The authors provide convergence analysis establishing weakly nonexpansive fixed-point ball convergence (under constant step sizes and strongly convex losses) and fixed-point convergence under adaptive step sizes without convexity. Experiments on seven inverse problems across FFHQ and ImageNet show the method achieving best or second-best PSNR/SSIM/LPIPS compared to strong baselines.

## Strengths

- **Novel AC-DC denoiser design that directly addresses a known problem.** The three-stage procedure (Algorithm 1) is a principled architectural contribution targeting the geometry mismatch between ADMM iterates and the noisy manifolds on which score functions are trained. The AC stage adds Gaussian noise to push iterates toward $\mathcal{M}_{\sigma^{(k)}}$; the DC stage uses conditional Langevin dynamics with a Gaussian approximation to refine alignment before the final Tweedie denoising. This goes beyond simple noise injection in prior works like DiffPIR and RED-diff. The rationale is clearly illustrated in Figure 1.

- **First convergence theory for score-based denoisers in ADMM-PnP.** Theorem 1 generalizes Ryu et al. (2019) by relaxing strict contractiveness to weak nonexpansiveness (Assumption 1). Theorem 2 shows the AC-DC denoiser satisfies this weak nonexpansiveness with high probability, and Theorem 3 relaxes the strong convexity requirement on the data fidelity term to establish fixed-point convergence under an adaptive step-size schedule. These results extend the PnP convergence literature to the score-based setting.

- **Comprehensive empirical validation across diverse inverse problems.** Table 1 reports PSNR, SSIM, and LPIPS on FFHQ and ImageNet for seven tasks (super-resolution, random/box inpainting, Gaussian/motion deblurring, phase retrieval). Both variants (Ours-tweedie and Ours-ode) achieve best or second-best in nearly every setting, outperforming DPS, DDRM, DiffPIR, RED-diff, DAPS, and DCDP. The ablation in Figure 5 demonstrates that increasing DC steps $J$ directly improves reconstruction quality, confirming the DC stage's empirical importance.

- **Code release** provides reproducibility for the community.

## Weaknesses

### Major

1. **Gap between convergence theory and practical implementation.** Theorems 2 and 3 explicitly assume "the DC step reaches the stationary distribution for each $k$" — i.e., infinite Langevin steps. In practice, the algorithm uses $J=10$ Langevin steps, far from convergence to stationarity, especially in high-dimensional image space. A footnote (p. 5, 6) states that counterparts "removing this assumption" appear in Appendix E.2, but the main text presents the idealized results as the core theoretical contribution. Since the appendix is not accessible for verification, the reader cannot assess whether the practical finite-$J$ algorithm is actually covered by the theory. This disconnect means the convergence guarantees do not clearly apply to the evaluated algorithm.

2. **Missing statistical rigor in the experimental evaluation.** All metrics in Table 1 are reported as point estimates (averages over 100 images) without any measure of variance — no standard deviations, confidence intervals, or error bars. Given the 100-image test set size and the well-known variance of diffusion-based solvers, it is impossible to determine whether the reported improvements over the second-best baseline are statistically significant. This undermines the force of the claim that the method "consistently improves solution quality."

3. **No reporting of computational cost.** The number of score function evaluations (NFEs), runtime, or any efficiency metric is absent from the paper. The AC-DC denoiser requires $1 + J + 1$ score evaluations per ADMM iteration for Tweedie denoising (plus ODE steps for Ours-ode), and the x-subproblem uses Adam for up to 1000 inner iterations. Without NFE or runtime accounting, the comparison to baselines like DPS and DDRM conflates the benefit of the denoiser design with unaccounted computational budget. A fair comparison requires at least a runtime or NFE-matched evaluation.

### Minor

4. **The fixed-point ball convergence guarantees are weaker than they appear.** Theorems 1–2 guarantee convergence to a $\delta$-ball (Definition 2), not to a fixed point. The ball radius $r$ depends on $\delta_k$ (Eq. 16), which involves the dimension $d$ — which for $256\times256\times3$ images is large ($d=196608$). The paper schedules $\sigma^{(k)}\to0$ to make $\delta$ vanish, but the actual $\delta_k$ expression includes terms like $(\sigma^{(k)})^2(d + 2\sqrt{d\nu_k} + 2\nu_k)$ and $d\sigma_{s^{(k)}}^2/(1-M\sigma_{s^{(k)}}^2)\log(2/\nu_k)$, which may not shrink meaningfully under the linear schedule used in experiments. The paper acknowledges that the "theoretical results focus on fixed-point convergence, which is not the strongest form" (p. 6), but the practical significance of the ball radius remains unclear.

5. **Missing results and baselines in the experiments.** DPIR is listed as a baseline (p. 8) but does not appear in Table 1. "Deblurring under nonlinear blurring" is listed as task (g) (p. 8) but no results appear for it in the main table (presumably deferred to the appendix). The PMC rows in Table 1 contain repeated entries and blank cells across multiple tasks (super-resolution, inpainting, motion deblur, Gaussian blur, box inpainting, phase retrieval), which appears to be either duplicated rows or missing data. These omissions and formatting issues reduce confidence in the completeness of the reported comparisons.

6. **Strong convexity assumption limits the scope of Theorem 1–2.** The data fidelity term $\ell$ is assumed $\mu$-strongly convex, which excludes several inverse problems considered in the experiments (e.g., phase retrieval). Theorem 3 addresses this by using adaptive step sizes, but such schedules are acknowledged as "arguably less appealing in practice" (Limitations, p. 9), and the constant-step-size experiments on phase retrieval are not covered by the theory.

7. **The Gaussian approximation for the Langevin conditional score is not rigorously justified.** The DC step in Algorithm 1 uses $\nabla \log p(\mathbf{z}_{\text{ac}}^{(k)}|\mathbf{z}_{\sigma^{(k)}}) \approx -\frac{1}{\sigma_{\text{ac}}^{(k)}}(\mathbf{z}_{\sigma^{(k)}} - \mathbf{z}_{\text{ac}}^{(k)})$, justified by a sketch that the likelihood can be well-approximated by a locally quadratic form when $\text{Var}(\mathbf{s}^{(k)})^{1/2} \ll \sigma^{(k)}$. No analysis is provided for how well this approximation holds under the scheduled $(\sigma^{(k)}, \sigma_s^{(k)})$ values used in experiments, leaving the theoretical justification for the DC step incomplete.

### Trivial

8. Table 1 has PMC rows as duplicates with inconsistent entries across several tasks, and some rows are entirely blank, which suggests a formatting or data-entry issue that should be cleaned.
9. The paper lists "De-blurring under nonlinear blurring" in the introduction and task description but does not report results for it in the main body (the appendix may contain them, but this should be explicitly stated).

## Nice-to-Haves

- **Hyperparameter sensitivity analysis.** The schedules for $\sigma^{(k)}$, $\sigma_s^{(k)}$, $\eta^{(k)}$, and $J$ are described but not systematically ablated. A study of how performance varies with these parameters (especially $J$ and the $\sigma$ schedule) would strengthen the empirical contribution.
- **Manifold alignment validation.** The central motivation — that the DC step moves iterates closer to $\mathcal{M}_{\sigma^{(k)}}$ — could be directly validated by measuring distances (e.g., via FID or MMD) between $z_{\text{ac}}^{(k)}$, $z_{\text{dc}}^{(k)}$, and samples from $\mathcal{M}_{\sigma^{(k)}}$ across ADMM iterations.
- **Isolating the denoiser effect.** The inner x-subproblem uses Adam for up to 1000 iterations, while baselines like DPS and DDRM do not have a comparable inner loop. An ablation replacing the inner optimizer with a single gradient step would help isolate the AC-DC denoiser's contribution.

## Removed Points

- *"The assumption that ℓ is strongly convex excludes many inverse problems (e.g., phase retrieval...)"* — This is a minor point because Theorem 3 already handles nonconvex ℓ, and the paper acknowledges the limitation. Kept as Minor #6.
- *"No error bars"* — Kept as Major #2 (genuine concern).
- *"Several table entries appear erroneous (e.g., repeated 'PMC' rows)"* — Kept as Trivial #8. The repeated rows could be parser artifacts (merged cells in the original table), but the blank entries are genuinely suspicious.
- *"The ablation study (Fig. 5) only for phase retrieval"* — Moved to Nice-to-Have; a single-task ablation is still informative.
- *"The paper includes 'De-blurring under nonlinear blurring' but does not report results"* — Kept as Minor #5.
- *"Weaknesses about missing appendix, missing proofs"* — Removed per instructions; the appendix exists in the original submission.
- *"The proof is relegated to an unseen appendix, making it impossible to assess correctness"* — Removed per instructions; proof deferral to appendix is standard in this venue.
- *"The notation in Eq. (9) is garbled (parser issue)"* — Removed; this is a parser artifact.
- *"The claim that the DC step 'refines alignment without losing signal information' is an unverified assertion"* — Removed as overly strong; the paper provides a reasoning sketch (Eq. 9–10) and empirical evidence in Figure 5.
- *"Pure formatting/style nitpicks"* — Removed.
- *Strength Finder claims: "Comprehensive empirical validation"* — Kept as Strength #3 with caveats in the weakness section.
- *Strength Finder claims about "Theoretical convergence guarantees"* — Kept as Strength #2 with the theory-practice gap noted in Major #1.

## Novel Insights

None beyond the paper's own contributions. The key insight — that a three-stage correction (AC → DC → denoising) can bridge the manifold mismatch between ADMM iterates and score-trained manifolds — is well articulated in the paper itself and is the central contribution.

## Suggestions

1. **Add standard deviations or confidence intervals to all reported metrics.** The 100-image test set is large enough to compute meaningful error bars. Bootstrap confidence intervals over the test set would allow readers to assess whether the reported improvements are significant.
2. **Report NFEs and average runtime per image for all methods.** This is essential for a fair comparison, especially given the inner Adam loop in the x-subproblem and the multiple score evaluations per ADMM iteration in AC-DC.
3. **Clarify the relationship between the stationary-distribution assumption and the practical $J=10$ implementation.** Either (a) verify that the finite-$J$ counterparts in Appendix E.2 cover the empirical setup, or (b) provide a simplified argument for why $J=10$ is sufficient in practice.
4. **Complete the experimental table.** Include DPIR results, nonlinear deblurring results (or explicitly note they are in the appendix), and clean up the PMC rows.
5. **Add a hyperparameter sensitivity ablation.** A simple experiment showing PSNR vs. $J$ and vs. $\sigma^{(k)}$ schedule across 2–3 tasks would significantly strengthen the empirical claims.

## Score and Decision

### Round 1 Bracket

The initial bracketing placed the paper between the weak band (avg 3.0–3.2, papers with methodological flaws) and the strong band (avg 8.0, clear accepts), with the most topically similar anchors in the middle:

| Anchor | Avg Score | Notes |
|--------|-----------|-------|
| Prior Mismatch in PnP-ADMM (HXjXPQU3yJ) | 6.25 | Most topically similar; PnP-ADMM convergence + experiments; rejected despite 6.25 due to limited tasks and theory-practice gaps |
| A Variational Perspective (1YO4EE3SPB) | 5.50 | Diffusion inverse problems; accepted at ICLR; had theory concerns and missing comparisons |
| DiracDiffusion (bEDTZxwJjT) | 5.50 | Diffusion inverse solver; rejected; limited tasks |
| Fast/Noise-Robust (Z9Odi09Rv9) | 4.75 | Rejected; significant technical errors |
| What's in a Prior? (kNPcOaqC5r) | 5.75 | Accepted; learned proximal networks; some reviewers questioned experiments |
| Restoration Network as Implicit Prior (x7d1qXEn1e) | 6.25 | Accepted; strong theory + experiments |

**Bracket: [4.75, 6.25]** — the paper clearly sits between a weak 4.75 (paper with technical errors) and 6.25 (stronger PnP-ADMM theory paper).

### Round 2 Narrowing

Comparing against the anchors inside the bracket:

- **vs. Prior Mismatch in PnP-ADMM (6.25, Reject):** This paper has broader experiments (7 tasks vs. SR/deblurring) and a novel denoiser design, but has more significant evaluation gaps (no error bars, no NFE) and a larger theory-practice disconnect. **Slightly weaker.**

- **vs. A Variational Perspective (5.50, Accept):** Both have comparable experiment breadth. This paper has a more novel architectural contribution (AC-DC) but worse evaluation rigor. **Comparable.**

- **vs. DiracDiffusion (5.50, Reject):** This paper has broader tasks and does not require retraining per degradation (a significant advantage). **Stronger.**

- **vs. What's in a Prior? (5.75, Accept):** Both propose novel denoiser architectures with convergence theory. This paper's experiments are more comprehensive but its theory has a larger practice gap. **Comparable.**

### Final Score

The paper has genuine novel contributions — the AC-DC denoiser is a well-motivated design and the experiments show consistent improvements across many tasks. However, the evaluation lacks basic statistical rigor (no error bars, no NFE/runtime), and the convergence theory has a structural gap relative to the practical algorithm. These are significant but not fatal; they are addressable in revision. The paper is comparable to accepted anchors at 5.50–5.75 and stronger than rejected anchors at 4.75–5.50.

**Score: 5.5**

**Decision: Accept**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>