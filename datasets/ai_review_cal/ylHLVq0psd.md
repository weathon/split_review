- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 6, 8, 5, 5, 6
Now I have all the information needed to produce the consolidated review. Let me synthesize carefully.

---

## Summary

This paper rethinks noise scheduling in diffusion models from two sides. On the **training** side, it proposes the Weighted Signal-Noise-Ratio (WSNR) metric — a frequency-weighted SNR — which consistently quantifies noise levels across different image resolutions and latent spaces. This enables a WSNR-Equivalent training noise schedule that substantially improves FID on high-resolution FFHQ (e.g., 11.49→7.89 at 256×256) and shows promise in latent-space ImageNet generation. On the **sampling** side, it derives a data-driven heuristic for setting the ODE integration interval (σ_max ≈ average pairwise data distance) and proposes a dynamic scheme that switches between Runge–Kutta methods based on step size. The sampling-side improvements on pre-trained models are modest (CIFAR-10: 1.92→1.89; FFHQ-64: 2.45→2.25 at 35 NFEs).

## Strengths

- **WSNR provides a principled, resolution-agnostic noise metric.** The paper demonstrates experimentally (Fig. 2) that images with the same WSNR exhibit similar noise levels across different resolutions, whereas standard SNR does not. This observation is grounded in power spectrum analysis (Fig. 3) and is a clean conceptual contribution.

- **WSNR-Equivalent training schedule yields substantial gains at high resolution.** Table 1 shows FID improvements on FFHQ from 7.13→6.15 at 128×128 and 11.49→7.89 at 256×256, with equal FID (3.70) at 64×64 as a sanity check. These are meaningful improvements, and the at-each-resolution architecture is held constant between schedules (line 87 confirms: "share the same network architecture with the baseline models").

- **Data-driven σ_max heuristic is theoretically motivated.** The derivation from the ideal denoiser (Eq. 4–5) through Jensen's inequality and Chebyshev's inequality to the practical choice σ_max = ‖d‖ is sound. Fig. 6 empirically confirms >98% coverage across three datasets, providing a principled way to set the integration interval.

- **Analysis of λ-space vs. σ-space ODE truncation error.** Eq. 10 identifies that the Lagrange remainder in λ-space contains an exp(λ) factor, explaining why σ-space solvers can have smaller truncation error. Table 3 provides supporting evidence that the σ-space 3rd-order solver outperforms DPM-Solver at large NFE on CIFAR-10.

## Weaknesses

### Major

- **The dynamic NFE-guided schedule is evaluated against only classical Runge–Kutta baselines.** The dynamic scheme (Fig. 7) is compared only against Heun's method and midpoint. Modern few-step samplers such as DPM-Solver++ or DEIS are not included in this comparison. The paper itself acknowledges this gap in the limits section (line 197: "More advanced ODE solvers, such as DPM-Solver and DEIS Solver, are not involved in"). While DPM-Solver IS compared in Table 3 (in the context of σ-space vs. λ-space ODEs), that is a different experimental setup. For the core claim of "optimizing the acceleration of the ODE solver," the absence of these baselines in the dynamic schedule evaluation significantly weakens the evidence.

- **The ImageNet latent-space experiment conflates model size and schedule.** Table 2 compares UViT-M (with WSNR-Equivalent schedule) against UViT-L (with presumably the baseline schedule), where UViT-L has more than twice the parameters. A cleaner ablation — UViT-M with WSNR schedule vs. UViT-M with baseline schedule — is not provided, making it impossible to isolate the effect of the schedule from the effect of model capacity.

### Minor

- **No confidence intervals or multiple seeds are reported for any FID number.** Given that several reported improvements are small (e.g., CIFAR-10: 1.92→1.89, a 0.03 FID difference; dynamic schedule margins in Fig. 7), the lack of statistical significance measures makes it difficult to assess whether these differences are meaningful.

- **The σ_max heuristic, while principled, is not compared against alternative simple baselines.** The paper tests σ_max ≈ ‖d‖ against fixed σ values (e.g., σ=80) but does not compare against other natural heuristics such as the mean pairwise distance (without the Chebyshev margin), median distance, or a learnable threshold. This would strengthen the claim that the specific proposed heuristic is near-optimal.

- **WSNR uses a dataset-averaged power spectrum, not instance-adaptive estimates.** The paper acknowledges this (line 70: "the averaged power spectrum across the entire training dataset is used as a proxy"), but the limitation is not discussed. An image with an unusual spectrum may have a substantially different effective noise level than the WSNR-Equivalent schedule predicts for that σ.

- **Sampling-side improvements on pre-trained models are small.** The headline numbers (CIFAR-10: 1.92→1.89; FFHQ-64: 2.45→2.25 at 35 NFEs) are modest and, combined with the limited baseline set and lack of variance reporting, leave uncertainty about practical significance.

### Trivial

- **The limits section creates a minor contradiction.** It states "DPM-Solver and DEIS Solver are not involved in," yet Table 3 explicitly compares against DPM-Solver. The intended meaning is that these solvers are not in the dynamic schedule comparison, but the phrasing is ambiguous.

## Nice-to-Haves

- A controlled ablation for Table 2: UViT-M trained with the baseline schedule vs. UViT-M trained with WSNR-Equivalent schedule, at the same model size.
- A sensitivity analysis of FID vs. σ_max near the proposed value, to show that the heuristic is near-optimal.
- Comparison of the dynamic NFE-guided schedule against DPM-Solver++ or DEIS with matched NFE budgets.

## Removed Points

These points were raised by reviewers but are excluded from the main weaknesses for the following reasons:

- **"Architecture not held constant across resolutions"** — The paper states (line 87) that at each resolution, the same architecture is used for both schedules. Architecture depth varies across resolutions (necessary for different image sizes), but the comparison at each resolution is fair. REMOVED (misreading of the paper).
- **"EDM baseline is poorly tuned for high resolution"** — This is the paper's own starting observation, not a weakness. The WSNR schedule is proposed precisely to address this. REMOVED (strawman).
- **"The derivation is straightforward / standard"** — Simplicity is not a weakness. The value lies in connecting the standard derivation to a practical heuristic. REMOVED (not a valid weakness).
- **"The theoretical bound is not tight"** — The paper uses Chebyshev's inequality, which is standard for distribution-free bounds. The bound is validated empirically (>98% coverage in Fig. 6), which is sufficient for the heuristic choice. REMOVED (not a meaningful criticism given the practical validation).
- **Generic strengths from the Strength Finder** ("addressed an important problem," "this paper targeted an interesting question") — REMOVED as they are generic and lack specific anchors in the paper's content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. For the dynamic NFE-guided schedule, include at least DPM-Solver++ (or another widely-used few-step sampler) as a baseline at matched NFE budgets, even if only on one dataset. This would establish where the proposed method stands relative to current practice.
2. Add a controlled ablation on ImageNet latent-space: UViT-M + baseline schedule vs. UViT-M + WSNR schedule at the same model size. This would cleanly isolate the schedule effect.
3. Report FID with at least 3 random seeds (or bootstrap confidence intervals), particularly for the small-margin results (CIFAR-10 1.92→1.89, dynamic schedule comparisons).
4. Compare the σ_max heuristic against mean pairwise distance and median pairwise distance as alternative baselines, to demonstrate that the specific Chebyshev-motivated choice is better than simpler alternatives.
