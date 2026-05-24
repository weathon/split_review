Now I have all the calibration data I need. Let me synthesize my analysis and write the final review.

**Calibration summary:**
- Round 1 bracket: 7.0–8.5
- Round 2 narrowed: This paper is stronger than Improved Consistency Training (7.0) and Iterative Retraining Stability (6.75), comparable to CADS (8.0) and Shortcut Models (8.0), but with slightly more notable weaknesses (FID-only reliance, theory-empirical gap) that pull it down from a clean 8.0.

**Final score: 7.5**

Now let me write the review. I need to carefully cross-reference each harsh critic point against the paper, determine what to keep/remove/modify, and produce a clean consolidated review.

Let me go through each point systematically:

**Harsh Critic Point 1: Overreliance on FID**
The paper states: "We report FID as our primary metric using 10k/50k samples for hyperparameter search/final evaluation (Heusel et al., 2017), with Precision/Recall (Kynkaanniemi et al., 2019) at k=5 nearest neighbors." (Section 4, line ~183)

The paper does use Precision/Recall as complementary metrics (Figures 4, 6). But there's no IS, no CLIP-based metric, no human evaluation. The SOTA claim rests primarily on FID.

Verdict: KEEP as Major — this is a real limitation. But it's not fatal because precision-recall analysis provides complementary evidence, and FID is the standard metric in this subfield. The paper makes a strong case with consistent improvements across many settings.

**Harsh Critic Point 2: Theory-empirical disconnect**
The paper proves risk reduction (R_data) but evaluates with FID. No ELBO, NLL, or denoising score matching loss reported.

Checking the paper: Section 3.1 proves that under anti-alignment, R_data(θ_Neon) < R_data(θ_r). Section 4 evaluates with FID and precision-recall. The paper positions the theory as explaining the mechanism rather than directly testing it.

Verdict: KEEP as Major. This is a genuine gap between what the theory proves and what the experiments measure. While common in the field, it weakens the chain of evidence.

**Harsh Critic Point 3: Unverified A-MONO assumption**
From the paper (footnote 2, line ~165): "Assumes curvature-density coupling (A-MONO): the conditional expectation E[∑_k ‖∇_x f(X_{t_k}, t_k)‖²_{F_t} | X_0 = x_0] increases with log p_{θ_r}(x_0). See App. B.7."

This is explicitly stated as an assumption. The autoregressive case (Theorem 2 part i) doesn't need it — temperature, top-k, top-p are directly verifiable. Only diffusion/flow needs A-MONO.

Verdict: KEEP as Minor. It's an acknowledged limitation of the theory for diffusion/flow, but the empirical results don't depend on it, and the autoregressive case is fully covered.

**Harsh Critic Section Notes:**
- "The axes (ω_s, ω_o) are not defined in the main text" — The text defines w_s and w_o in equation (3). The figure uses ω (omega) variant. This is a minor notation inconsistency. Verdict: Trivial.

- "0.36% additional compute does not include hyperparameter selection cost" — The paper says the grid search is done at evaluation. The 0.36% is training compute only. This is a real point. Verdict: Minor.

**Missing Parts from Harsh Critic:**
- "Comparison with model-soup baselines" — The paper already rules out generic OOD data with CIFAR-10C. Model soup is not a standard comparison for synthetic-data improvement methods. Verdict: Nice-to-have.

- "Broader metric reporting" — Already partially addressed by precision-recall. Verdict: Nice-to-have.

- "Selection of w without grid search" — Verdict: Nice-to-have.

Now let me write the final review.## Summary

Neon introduces a simple, post-hoc parameter merge that improves generative models by reversing the degradation from brief self-training on the model's own outputs. Given a base model, Neon fine-tunes it on self-generated synthetic data, then extrapolates the weights *away* from the degraded checkpoint. The key insight — supported by theory and a toy study — is that mode-seeking inference samplers (CFG, low temperature, top-k) create an anti-alignment between synthetic and real-data gradients, so reversing the self-training update reduces true data risk. The method is architecture-agnostic, requires no additional real data, and works across diffusion, flow matching, autoregressive, and few-step models with less than 1% extra training compute, achieving a new SOTA FID of 1.02 on ImageNet-256 with xAR-L.

## Strengths

- **Simple, architecture-agnostic, and practically cheap**: Neon is a single parameter merge (Equation 2) requiring only a brief fine-tune on self-generated data and a scalar weight. The same recipe works across four model families (diffusion, flow matching, autoregressive, few-step) without auxiliary models, inference modifications, or likelihood computations (Section 4). The computational overhead is genuinely small — 0.36% for xAR-L, 0.64% for VAR-d16, 1.75% for EDM-VP on CIFAR-10.

- **Strong empirical FID improvements across diverse settings**: Neon consistently reduces FID: EDM-VP on CIFAR-10 from 1.78 → 1.38; xAR-L on ImageNet-256 from 1.28 → 1.02 (SOTA); VAR-d16 from 3.30 → 2.01; IMM 4-step from baseline quality to 1.69, nearly matching 8-step baseline (Figures 3, 5, 7). These gains hold with as few as 1k synthetic samples (xAR-L: 1.05) and across a wide range of base model qualities (Figure 9).

- **Well-developed theoretical framework**: Theorems 1–2 formalize why mode-seeking samplers induce anti-alignment, and the Taylor expansion of risk (Equation 4) proves that negative extrapolation reduces true data risk. The 2D Gaussian toy study (Figure 2) provides clean geometric intuition. The theory also correctly predicts the complementary *interpolation* regime for diversity-seeking samplers.

- **Convincing mechanism dissection via precision-recall**: Figures 4 and 6 cleanly show that Neon trades precision for recall — redistributing probability mass from over-represented to under-represented modes — exactly as the theory predicts. The U-shaped FID-vs-w curve matches the Taylor expansion prediction.

- **Thorough ablation studies**: Cross-architecture transfer (Figure 8), CIFAR-10C null control, robustness to synthetic data quality (Figure 10), and base-model-quality spectrum (Figure 9) are well-designed and effectively rule out alternative explanations. The cross-architecture transfer result is particularly valuable for practical deployment.

## Weaknesses

### Fatal
None.

### Major

- **SOTA claim rests almost entirely on FID**: The headline result (FID 1.02) and all primary comparisons use only FID. Precision-recall analysis (Figures 4, 6) provides complementary evidence of the mechanism, but no other quality metrics — Inception Score, CLIP-based metrics, or human evaluation — are reported for the conditional ImageNet experiments. In the very-low-FID regime, small numeric differences can be amplified by metric idiosyncrasies, and FID alone cannot rule out that the gain partially reflects a precision-recall redistribution that the metric favors without commensurate perceptual improvement. The paper would be strengthened by at least one additional quality dimension.

- **Gap between theoretical risk-reduction claims and empirical validation**: Section 3.1 proves that Neon reduces the true data risk R_data under anti-alignment, but the paper never reports any risk or risk-proxy metric on hold-out data (no ELBO, NLL, or denoising score matching loss). All experiments report FID, a distributional distance not directly tied to the risk the theory bounds. The theory is presented as an explanatory mechanism, which is valuable, but the connection between the theoretical prediction and the observed FID improvements remains correlational rather than verified. The precision-recall analysis and toy study provide indirect support but do not close this gap.

### Minor

- **Hyperparameter selection cost not included in the compute claim**: The "0.36% additional training compute" for xAR-L covers only the fine-tuning step. For autoregressive models, the method requires a joint grid search over extrapolation weight w and CFG scale γ to find the optimal FID (Section 4.2). For diffusion/flow models, a sweep over w is needed. These search costs — which involve repeated FID computation on a validation set — are not counted in the reported overhead. The method would benefit from a lightweight heuristic for selecting w without a full FID sweep.

- **A-MONO assumption for diffusion/flow models is unverified**: Theorem 2's guarantee for diffusion and flow matching relies on the A-MONO curvature-density coupling condition, which is explicitly stated as an assumption (footnote 2) and is never tested empirically. The autoregressive case (temperature, top-k, top-p) does not need this assumption and is directly verified. For diffusion/flow models, the theoretical guarantee is provisional, though the empirical results do not depend on it.

### Trivial

- Figure 2 axis labels use ω_s, ω_o while the corresponding equation (3) uses w_s, w_o — a minor notation inconsistency.

## Nice-to-Haves

- Adding Inception Score or a CLIP-based metric for the conditional ImageNet experiments would give a second quality dimension and strengthen the SOTA claim.
- A heuristic or cheap validation protocol for selecting w (e.g., based on the training loss on synthetic data during fine-tuning) would make the method more practically self-contained.
- Comparing against a simple checkpoint-averaging baseline (model soup) would rule out any benefit from generic parameter interpolation effects, though the CIFAR-10C null control already addresses the OOD-data confound.
- Testing or discussing how one might verify the A-MONO condition on a small diffusion model would make Theorem 2 less hypothetical.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic claim that the paper lacks "complementary assessment with Inception Score" and "no human evaluation"**: While factually true that these are not reported, IS has fallen out of favor for modern generative models (it is known to correlate poorly with visual quality at high FID regimes) and human evaluation is not standard practice for class-conditional ImageNet generation papers. The precision-recall analysis *is* a complementary assessment, and the harsh critic's framing overstates the gap. Moved the core concern (FID-only SOTA claim) to Major but stripped the demand for IS and human eval specifically.

- **Harsh critic claim that the paper "never reports any risk or risk proxy"**: Factually accurate, kept as a Major weakness, but the framing that this invalidates the theory is overstrong — the theory is presented as an explanatory mechanism, and the precision-recall analysis provides some indirect validation.

- **Harsh critic demand for "model-soup baselines"**: Model soup is not a standard comparison for self-training improvement methods. The paper already addresses the OOD confound with CIFAR-10C. Moved to Nice-to-Haves.

- **Harsh critic framing of the A-MONO issue as a serious theoretical gap**: The paper explicitly acknowledges this as an assumption (footnote 2). The autoregressive case needs no such assumption. Demoted from the harsh critic's implication of a theory-practice disconnect to Minor.

## Novel Insights

The most genuinely novel insight emerging from this work — beyond the paper's own contributions — is the reframing of model collapse / self-training degradation not as noise to be avoided, but as a *structured, harnessable signal*. The paper shows that the degradation direction from self-training is consistently anti-aligned with the true data gradient across architectures, making it a universal correction vector. This inverts the conventional wisdom that synthetic data training is dangerous and should be mitigated through careful mixing or external verifiers. The finding that this signal transfers across architectures (Figure 8) further suggests it captures something fundamental about the sampler's mode-seeking bias rather than architecture-specific artifacts.

## Suggestions

- The paper would benefit from reporting at least one additional metric (IS or a CLIP-based score) for the key ImageNet-256 results, even if only in a compact table. This would substantially strengthen the SOTA claim without requiring new experiments — the data is already generated and just needs scoring.
- Acknowledge explicitly that the reported "0.36% additional compute" is the training cost only and that hyperparameter selection (grid search over w and γ) incurs additional evaluation cost. Even a rough estimate would improve transparency.
- Consider a brief discussion of how practitioners might roughly set w without a full FID grid search — for instance, monitoring the loss on the synthetic set during fine-tuning to estimate when degradation has occurred enough to define a useful direction.

## Score and Decision

**Calibration anchors consulted:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Post-hoc Discriminator Guidance (JJH7m9v4tv) | 3.00 | R1 | Much weaker — GAN-specific, limited scope |
| Self-Supervised Pseudodata Filtering (2LhCPowI6i) | 2.33 | R1 | Much weaker — continual learning focus, limited scope |
| Synthetic Data for Transfer Learning (CjPt1AC6w0) | 6.25 | R1 | Weaker — fundamental fairness issue in comparison, narrower scope |
| Iterative Retraining Stability (JORAfH2xFd) | 6.75 | R2 | Weaker — limited experiments, single seed, assumptions hard to verify |
| Improved Consistency Training (WNzy9bRDvG) | 7.00 | R2 | Weaker — narrower (CIFAR-10/ImageNet-64 only), more engineering-focused |
| CADS (zMoNrajk2X) | 8.00 | R2 | Comparable — simple post-hoc method, SOTA FID, but diffusion-only and no theory |
| Shortcut Models (OlzB6LnXcS) | 8.00 | R1/R2 | Comparable — novel method, broad experiments, but 1-step quality lags distillation |
| REPA (DJSZGGZYVi) | 9.00 | R1 | Stronger — more novel insight, cleaner theory-empirical connection |

**Bracket:** Round 1 placed Neon between 7.0–8.5. Round 2 narrowed to 7.0–8.0, with Neon clearly stronger than the 7.0 anchors (Improved Consistency Training) and comparable to but slightly weaker than the clean 8.0 anchors (CADS, Shortcut Models) due to the FID-only reliance and theory-empirical gap. Score: **7.5**.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>