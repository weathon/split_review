Now I have a clear picture from the calibration. Let me compile the final review.

---

## Summary
This paper proposes ADMM-PnP with the AC-DC denoiser, a three-stage denoiser that addresses the manifold mismatch between ADMM iterates and noise-trained score functions. The denoiser adds Gaussian noise (AC), runs conditional Langevin dynamics (DC) to steer iterates toward score-training manifolds, then applies score-based denoising. The paper provides convergence analysis establishing fixed-point ball convergence under strong convexity (Theorem 2) and convergence under adaptive step sizes without convexity (Theorem 3), extending prior ADMM-PnP theory to score-based settings. Experiments across six inverse problems on FFHQ and ImageNet demonstrate consistent improvements over recent diffusion-based baselines.

## Strengths
- **Novel, well-motivated three-stage denoiser design:** The AC-DC denoiser (Algorithm 1, Sec. 3) explicitly addresses manifold mismatch through auto-correction (Gaussian noise injection) and directional correction (conditional Langevin dynamics). The rationale that AC alone does not guarantee manifold alignment while DC refines toward the correct manifold is clearly argued, and the DC step is derived from first principles targeting the conditional distribution \(p(z_{\sigma^{(k)}}|z_{\text{ac}}^{(k)})\). This is a principled advance over prior noise-injection-only approaches (DiffPIR, SNORE).

- **Genuine theoretical contribution — convergence analysis for score-based denoisers in ADMM:** Theorems 1–3 extend ADMM-PnP convergence theory (Ryu et al., 2019; Chan et al., 2016) to score-based settings, which was previously an open challenge. Theorem 1 generalizes fixed-point results to weakly nonexpansive residuals (not requiring strict contractivity). Theorem 2 establishes high-probability weak nonexpansiveness of the AC-DC denoiser under smoothness and coercivity assumptions. Theorem 3 relaxes convexity via adaptive step sizes. The paper explicitly notes the stationary-distribution assumption and points to appendix results that relax it (footnote, line 217).

- **Consistent empirical improvements across diverse tasks:** Table 1 demonstrates that the two proposed variants (Ours-tweedie, Ours-ode) achieve either best or second-best PSNR, SSIM, and LPIPS on all six inverse problems (super-resolution, random/box inpainting, motion/Gaussian deblurring, phase retrieval) for both FFHQ and ImageNet. For example, on super-resolution (FFHQ), Ours-tweedie achieves 30.44 PSNR vs. 29.53 for the next-best method (DAPS). On phase retrieval, the margin is even larger (27.94 vs. 26.71).

- **Ablation validating the DC stage:** Figure 5 shows phase retrieval reconstructions with J=0 (AC only), J=10, and J=20 DC steps. Disabling DC leaves severe artifacts; increasing DC steps progressively yields cleaner images. This directly supports the claim that the Langevin-based directional correction is essential.

## Weaknesses

### Fatal
None.

### Major
- **Incomplete and inconsistent baseline reporting across tasks (Table 1):** The paper lists eight baselines (DPS, DAPS, DDRM, DiffPIR, RED-diff, DCDP, PMC, DPIR; line 306) but Table 1 presents only subsets per task. DDRM appears in only 2 of 6 tasks (super-resolution, random inpainting). DPIR is never shown in any table row. A method labeled "DDPM" appears in the Gaussian blur row (line 362) with no introduction or explanation. Several rows contain duplicated "PMC" entries with empty cells (lines 334-335, 344, 349-350, 365-366, 374-376). While the most important baselines (DAPS, DPS, DiffPIR) are present in most tasks and the method consistently outperforms them, the selective and unexplained reporting undermines the completeness of the empirical evidence and creates the appearance of cherry-picking. A fair comparison requires either running all baselines on all tasks or clearly justifying why some baselines are excluded from specific tasks.

- **No computational cost comparison:** The AC-DC denoiser performs J=10 Langevin steps per ADMM iteration plus an optional ODE solve, while baselines like DPS and DiffPIR also use score evaluations. The paper reports only quality metrics (PSNR, SSIM, LPIPS) without quantifying NFEs or wall-clock time. The authors acknowledge the desire to reduce NFEs in limitations (line 390), but this does not substitute for reporting the actual cost. For a method whose practical appeal partly rests on being an optimization-based PnP scheme, the omission prevents readers from judging whether quality improvements come from better design or simply more compute. This is a significant evaluation gap.

### Minor
- **Stationary-distribution assumption in Theorems 2–3:** Both theorems explicitly assume the DC stage's Langevin dynamics reaches the stationary distribution at each ADMM iteration. The main algorithm runs only J=10 DC steps. The paper acknowledges this with a footnote pointing to Appendix E.2 for relaxed results, but the body text theorems—and therefore the stated convergence guarantees—rest on this assumption. The disconnect between theory and practice should be discussed explicitly in the main text rather than deferred.

- **Heuristic DC approximation lacking analysis:** The DC step replaces the conditional likelihood gradient \(\nabla \log p(z_{\text{ac}}|z_{\sigma})\) with a simple attraction term \(-1/\sigma_{z_t}^2(z_{\text{ac}} - w)\), justified by a local quadratic approximation when residual noise is small (line 145-146). No analysis or empirical study quantifies the error from this approximation, and the convergence results depend on the behavior of the denoiser induced by the true conditional distribution. This is a gap between the algorithm's implementation and the theoretical model, though a common one in this literature.

- **No standard deviations on metrics:** The paper reports only mean PSNR/SSIM/LPIPS over 100 test images without any measure of variability. Given the relatively small test set, confidence intervals or standard deviations would help assess the significance of reported improvements.

### Trivial
- "DDPM" in the Gaussian blur row (line 362) is undefined and unexplained in the text.
- Duplicated "PMC" rows with empty entries throughout Table 1 are formatting artifacts that confuse readers.
- "DiPIR" is used consistently but differs from the more standard "DiffPIR"; this should be unified or noted.

## Nice-to-Haves
- A cost-quality trade-off plot (PSNR vs. NFEs or wall-clock time) for each method would let readers assess whether the AC-DC denoiser offers a favorable compute-accuracy trade-off.
- An ablation replacing the DC stage with a computationally equivalent alternative (e.g., repeating the denoising step) would isolate the benefit of conditional Langevin correction from the benefit of extra compute.
- An empirical study varying the Gaussian approximation's parameter or comparing against a more accurate likelihood model would help validate the DC approximation.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"DPS is missing from Gaussian blur"** — Factually incorrect. DPS appears in the Gaussian blur row of Table 1 (line 360) with PSNR 26.106 on FFHQ, 23.995 on ImageNet.
- **"This pattern looks like the authors reported only the strongest competitor for each task, which inflates the impression that 'Ours' dominates broadly"** — The claim of cherry-picking is overstated. The key competitors (DAPS, DPS, DiPIR) are present across nearly all tasks, and the method's margins are large enough that the missing baselines would not change the ranking. The real issue is sloppy/incomplete reporting, not deceptive selection.
- **"The proof sketch in the main text is plausible, but the missing appendix and the missing verification that the practical schedule aligns with theoretical requirements"** — The appendix is noted to be stripped by the parser; it exists in the original submission. The practical schedule discussion is already partially present (the paper notes the linear decay schedule in Sec. 6).
- **"The paper lacks any quantification of computational expense"** — This is kept as a Major weakness above but was originally framed as fatal; the paper acknowledges this in limitations and the core contribution (convergence theory + novel denoiser) does not depend on efficiency claims.
- **"DiPIR is likely a typo"** — The paper uses this consistently and it may be an intentional abbreviation. This is trivial at most.
- **Demand for comparing against "a baseline that replaces DC with a different correction"** — This is scope creep; the ablation study (J=0 vs J=10 vs J=20) already isolates the DC contribution.

## Novel Insights
The convergence analysis framework — establishing that a score-based denoiser with Langevin-based correction is weakly nonexpansive with high probability — is genuinely novel. Prior ADMM-PnP convergence theory (Ryu et al., 2019; Chan et al., 2016) assumed classical denoisers with known contractivity properties. Extending this to score-based denoisers, where the implicit regularizer is unknown and the denoiser's behavior is governed by a stochastic process (Langevin dynamics), required new analytical machinery (smoothness + coercivity assumptions on the data log-density, high-probability bounds). This bridges an important gap between the PnP convergence literature and the diffusion model literature.

## Suggestions
- Complete the baseline table by running all listed methods on all tasks, or clearly document per-task exclusions (e.g., DDRM does not support nonlinear inverse problems like phase retrieval).
- Add a figure or table with NFE counts or wall-clock times alongside quality metrics so readers can assess the efficiency-quality trade-off.
- Either move the stationary-distribution relaxation from Appendix E.2 into the main text, or add a paragraph discussing the gap between the idealized assumption and practical J=10 implementation.
- Remove the duplicated empty PMC rows from Table 1 and define "DDPM" in the text.

## Score and Decision

**Calibration anchors used across rounds:**

*Round 1 (bracketing):*
- `dAavOuxZvo` (3.00, Reject) — diffusion-based inpainting via variational inference; much weaker theory and narrower scope
- `1YO4EE3SPB` (5.50, Accept) — variational perspective on inverse problems with diffusion; similar topic but weaker theory and sparser experiments
- `bEDTZxwJjT` (5.50, Reject) — DiracDiffusion; novel method but narrower evaluation
- `DsEhqQTFAG` (6.50, Accept) — decomposed diffusion sampler; stronger evaluation than our paper
- `6EUtjXAvmj` (8.00, Accept) — variational diffusion posterior sampling with midpoint guidance; clearly stronger: tighter theory-practice connection, NFE-aware evaluation, more polished experiments

*Round 2 (narrowing):*
- `HXjXPQU3yJ` (6.25, Reject) — prior mismatch in PnP-ADMM; similar theoretical contribution level but only 2 tasks, weaker experiments, rejected due to narrow scope
- `x7d1qXEn1e` (6.25, Accept) — restoration network as implicit prior; similar quality level but only 2 tasks, less novel denoiser design
- `kNPcOaqC5r` (5.75, Accept) — learned proximal networks; comparable theory level but narrower
- `ANvmVS2Yr0` (6.25, Accept) — generalization in diffusion models; strong theory but different topic

**Bracket from Round 1:** This paper sits between the 6.25–6.50 middle-band papers and the 8.00 high-band paper. Compared to HXjXPQU3yJ (6.25, also PnP-ADMM with convergence analysis), our paper has broader experiments (6 tasks vs. 2), a novel denoiser design, and consistent empirical gains. Compared to 6EUtjXAvmj (8.00), our paper falls short on evaluation polish (missing NFE comparison, incomplete baseline reporting, no standard deviations). **Narrowed bracket: 6.0–7.0.**

**Final placement:** The paper is clearly stronger than the 6.25 anchors — it has more tasks, a more complete convergence analysis (both fixed and adaptive step sizes), and a novel denoiser design. But the evaluation gaps (incomplete baselines, no NFE comparison) are real and prevent it from reaching the 7.5+ tier where evaluations are more polished and theory-practice connections are tighter. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>