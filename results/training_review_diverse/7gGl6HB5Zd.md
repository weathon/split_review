Now I have all the information needed to write the consolidated review. Let me synthesize carefully.

---

## Summary

This paper introduces a zero-shot and few-shot method for detecting AI-generated images. The core idea is to analyze the curvature and gradient of the log-probability manifold of a pre-trained diffusion model (Stable Diffusion) using spherical perturbations around an input image, compute a criterion $C(x_0)$ that approximates a linear combination of curvature and gradient magnitude, and use this as a detection score. The method achieves 0.974 average AUC across 20 generative models—substantially outperforming existing zero-shot methods—and improves few-shot performance when combined with a mixture-of-experts framework.

## Strengths

- **Novel application of diffusion-model score-function analysis for zero-shot detection:** The paper is the first to leverage a pre-trained diffusion model's score function and manifold geometry for generated-image detection in a zero-shot setting, offering a genuinely new theoretical angle that differentiates it from prior work (autoencoder-based or representation-similarity approaches).
- **Strong and consistent empirical outperformance:** Across 20 generative models spanning GANs, diffusion models, and commercial tools, the method achieves 0.974 avg. AUC, 0.976 AP, and 0.947 accuracy—substantially exceeding AEROBLADE (0.874/0.919/0.814) and RIGID (0.856/0.899/0.777) (Table 1, Fig. 5). The advantage is consistent across all three generative-technique groups.
- **Effective few-shot integration:** When combined with Cozzolino et al. (2024) in a mixture-of-experts framework, the zero-shot criterion provides a larger improvement than other zero-shot baselines, demonstrating practical value beyond pure zero-shot settings (Fig. 6).
- **Robustness across configurations:** Sensitivity analysis (Table 2) shows stable performance across different base diffusion models (SD v1.4, SD v2, Kandinsky 2.1), varying perturbation counts, spherical noise levels, and common image corruptions (JPEG compression, Gaussian blur), with AUC drops ≤3.45%.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The theoretical derivation, while mathematically sound in its main steps, is terse at critical junctures.** The justification for Eq. (17)—that $\mathbf{E}[\nabla\log p_\alpha(x)/\|\nabla\log p_\alpha(x)\|_2]\approx 0$—is given in two sentences ("integration of normals over the sphere is zero, and $\nabla\log p_\alpha(x)$ approximates the uniform spherical noise"). The paper does rely on the concentration-of-measure argument (line 131, citing Laurent & Massart 2000) to establish interchangeability of $u_d$ and $\epsilon$ in high dimensions, and the score function's approximation to noise follows from the diffusion model's denoising objective. However, a reader unfamiliar with these connections will find the reasoning under-justified. The derivation does not invalidate the method—the empirical results stand independently—but the paper's framing as providing *theoretical grounding* is somewhat overclaimed given the brevity of the approximation justification. This is an expositional weakness, not a methodological flaw.

- **Gap between the theoretical motivation and the cross-technique evaluation.** The theory describes biases induced by a *specific* diffusion model's learned manifold, yet the method works well across diverse generative families (GANs, other diffusion models, commercial tools). The paper acknowledges this gap briefly in §6 and offers a hypothesis, but does not directly test the connection (e.g., by analyzing whether images from the same diffusion model exhibit higher curvature as predicted). This weakens the paper's claim to have *explained* why the criterion works, as opposed to simply having discovered a useful heuristic. The method itself is still a contribution, but the theoretical interpretation is partially untested.

- **No discussion of computational cost.** The method requires 64 forward passes of Stable Diffusion + decoder + CLIP embedding per image, which is orders of magnitude more expensive than the baselines (AEROBLADE uses a single VAE pass; RIGID uses a single forward pass of a pre-trained encoder). This is a practical concern for deployment that should be acknowledged.

- **No variance or confidence intervals reported in Table 1.** The large AUC gaps (0.974 vs. 0.874/0.856) are impressive, but without standard errors or interval estimates across techniques, the reader cannot assess whether the ranking is statistically robust. The per-technique breakdown in Fig. 5 partially addresses this, but Table 1 would benefit from variance reporting.

- **The CLIP mapping is not ablated.** The paper maps both the noise predictions and the input image to CLIP space before computing $C(x_0)$. Since CLIP is known to encode semantic content that can distinguish real from generated images (as exploited by prior work), it is unclear how much of the performance comes from the diffusion-model score analysis vs. the CLIP representation. An ablation comparing $C(x_0)$ in pixel space, latent space, and CLIP space would clarify the source of the gains.

### Trivial

- **The derivation introduces notation ($a$, $u(x)$, $\gamma$) that is defined but could be cleaner.** The variable $a$ is set to 1 at line 164, and $u(x)$ is $u_d(x)$ from line 135, but the notation shifts between $u_d(x)$ and $u(x)$ without comment, which can confuse careful readers.
- **MoE classifier details are omitted.** The paper mentions using a random forest but does not specify the number of trees, max depth, or other hyperparameters, which affects reproducibility of the few-shot results.

## Nice-to-Haves

- An ablation study evaluating $C(x_0)$ directly in pixel space or the diffusion model's latent space (without the CLIP mapping) would help disentangle the contribution of the score-based criterion from the CLIP representation.
- A comparison with smaller few-shot sample sizes (e.g., 100 or 500 instead of 1K) would strengthen the "few-shot" claim.
- An analysis of whether the criterion $C(x_0)$ actually correlates with true curvature $\kappa(x_0)$ and gradient $D(x_0)$ (computed via Monte Carlo on the score function) would directly validate the claimed geometric interpretation.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"d is never defined explicitly"** — The paper explicitly defines $d$ as "the data dimensionality" at line 54. Removed (factually wrong).
- **"Error bars in Figure 5 are not defined"** — The caption (line 220) states "Error bars represent variability in AUC between techniques within each group." Removed (factually wrong).
- **"The variable a is set to 1 without specifying its origin or why it must equal 1"** — The paper states "where $a=1$ for the choice of that $\gamma$" at line 164. Removed (misread).
- **"The term γ a u(x) appears without clear definition"** — $\gamma$ is defined at line 135, $a=1$ at line 164, and $u_d(x)$ at line 135. Removed (misread).
- **"Were the baselines tuned equally?"** — The paper states baselines used "publicly available code" with "strict adherence to the specifications detailed in their publications" (line 240). Removed (unfair criticism unsupported by evidence).
- **"Missing related works / compare to OOD detection methods"** — Hard rule: do not mention missing related works. Removed.
- **"The paper claims the method works for images generated by the same diffusion model but tests on diverse techniques — evidential gap"** — The paper explicitly acknowledges and discusses this in §6 as a limitation; it does not claim the theory explains cross-technique performance. The cross-technique generalization is presented as an empirical strength, and the gap is noted. This is reframed above as a minor weakness (the paper could test the connection more directly), but not removed entirely.

## Novel Insights

The most insightful observation to emerge from this review is that the paper's empirical contribution (a simple criterion comparing noise predictions to the input in CLIP space) may be more general than its theory predicts. The method works across diverse generative families despite being theoretically derived from a single diffusion model's manifold biases. This discrepancy suggests that the criterion may be capturing a broader statistical signature of generated images—perhaps related to how *any* imperfect denoiser responds to out-of-distribution inputs—that goes beyond the specific curvature/gradient framing. The paper's suggestive hypothesis (similar dataset training leads to similar manifold characteristics) points to an interesting open question: can the manifold-bias approach be unified with distribution-shift detection more broadly? The field would benefit from a study that explicitly tests whether the score-function criterion's effectiveness correlates with the training-data overlap between the detection model and the generative model, which the current paper does not provide.

## Suggestions

- Expand the justification for Eq. (17) with a clear statement connecting the score function approximation to the diffusion model's denoising objective and the concentration-of-measure argument. A single sentence clarifying that for a well-trained denoiser at small $\alpha$, $h(\tilde{x})\approx -(1/\sqrt{\alpha})u_d$, hence the normalized score's expectation vanishes by symmetry, would resolve most reader confusion.
- Add an ablation that removes the CLIP mapping (compute $C(x_0)$ in latent space or pixel space) to establish the independent contribution of the score-based criterion.
- Report per-technique AUC with confidence intervals or standard errors in Table 1, or at least add standard deviation across techniques.
- Add a brief discussion of computational cost and potential mitigations (e.g., reducing $S$, using a smaller diffusion model).
- Explicitly state the random forest hyperparameters used in the MoE experiment.

## Score and Decision

**Originality:** High — first application of diffusion-model score-function analysis for zero-shot detection; novel derivation connecting curvature to a computable criterion.

**Importance of research question:** Very high — detecting generated images is a timely and practically important problem, and zero-shot methods that generalize without data maintenance are especially valuable.

**Claims well supported:** The main empirical claim (outperformance of zero-shot baselines) is well supported by Table 1 and Fig. 5. The theoretical claim (that $C(x_0)$ approximates curvature-minus-gradient) is partially supported — the derivation is mathematically plausible but terse, and the geometric interpretation is not directly validated. The paper would benefit from softening its theoretical framing or adding validation experiments.

**Soundness of experiments:** Sound overall. The evaluation covers 20 generative models across three benchmark datasets. Baselines use publicly available code with published specifications. Sensitivity analysis demonstrates robustness. The main gap is the lack of variance reporting and the missing CLIP ablation.

**Clarity of writing:** Generally clear but dense in the theoretical sections. The derivation in §4.2 would benefit from more exposition.

**Value to the research community:** High. The method sets a new state-of-the-art for zero-shot detection with a wide margin, and the diffusion-model-based approach opens a new direction for detection research. Even if the theoretical interpretation is debated, the empirical contribution alone is significant.

The paper makes a strong empirical contribution with a novel approach. The theoretical framing is somewhat overclaimed given the brevity of the approximation justification, but the derivation is not fundamentally flawed—it is a valid mathematical framework supported by plausible approximations. The weaknesses identified (CLIP not ablated, no variance reporting, computational cost not discussed) are addressable and do not undermine the core empirical finding.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>