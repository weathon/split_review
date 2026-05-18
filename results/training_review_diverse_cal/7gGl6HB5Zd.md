Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the final consolidated review, carefully verifying each claim against the paper text.

---

## Summary

This paper introduces a zero-shot detection framework for AI-generated images that uses score-function analysis of a pre-trained diffusion model to derive a computable detection criterion. The criterion is motivated geometrically: generated images are expected to lie near peaks of the learned probability manifold, characterized by high curvature and low gradient, and the paper derives an approximation to \(a\kappa - D\) that can be computed via spherical perturbations and noise predictions. Evaluated across 20 generative models, the method achieves an average AUC of 0.84, substantially outperforming existing zero-shot methods AEROBLADE (0.70) and RIGID (0.74). A mixture-of-experts extension with 1,000 labeled samples further improves few-shot performance. The paper is the first to leverage diffusion models for zero-shot generated image detection.

## Strengths

- **State-of-the-art zero-shot performance across diverse generators.** Table 1 reports an average AUC of 0.84 versus 0.70 (AEROBLADE) and 0.74 (RIGID). Fig. 5b shows the method achieves the highest or second-highest AUC on 17 out of 20 generative models spanning GANs, diffusion models, autoregressive models, and commercial tools (Midjourney, DALL-E). This is the single strongest piece of evidence for the paper's contribution.

- **First diffusion-model-based zero-shot detection framework.** Prior zero-shot methods for generated image detection (Ricker et al., 2024; He et al., 2024) use autoencoder reconstruction errors or representation similarity. This paper introduces a novel approach by analyzing score-function approximations from a diffusion model to derive a detection criterion, opening a new direction for the field.

- **Cross-technique generalization despite using only SD v1.4.** The method relies solely on Stable Diffusion 1.4 as its base model yet generalizes well to images from fundamentally different architectures (GANs, autoregressive models) and training sets. Fig. 5 demonstrates strong per-technique performance across GAN, diffusion, and commercial generator groups.

- **Theoretical motivation connecting manifold geometry to detection.** Drawing inspiration from Mitchell et al. (2023)'s curvature-based detection for text, the paper connects score-function analysis to a geometric criterion (curvature minus surface-averaged gradient) for images. The toy experiments in Fig. 3 validate the qualitative behavior of the curvature estimator on controlled low-dimensional data, showing unbiased estimation and exponential convergence.

## Weaknesses

### Fatal
None. The paper's core empirical contribution is not invalidated by any single issue.

### Major

- **The "few-shot" label is overstated.** The MoE experiment uses 1,000 labeled samples to train a lightweight classifier. While the comparison between methods is fair (all zero-shot methods receive the same 1K samples for MoE training), 1,000 examples does not satisfy standard definitions of "few-shot" in the detection literature (typically 1–100 per class). The paper repeatedly claims to "remain in the few-shot bounds" without justifying this threshold, and the axis title "Few-shot Performance" in Fig. 6 is misleading. The experiment is better described as exploring a "low-data regime," and the paper should either (a) evaluate with truly few-shot sample sizes (10–100) matching the baseline's operating regime, or (b) rebrand and contextualize this result honestly.

### Minor

- **Theoretical derivation contains uncontrolled approximations that weaken the claim of rigorous grounding.** The chain from curvature/gradient to the implementable criterion \(C(x_0)\) involves several steps where validity is asserted rather than justified for actual high-dimensional image manifolds: (1) replacing Gaussian noise \(\epsilon\) with uniform spherical variables \(u_d\) relies on norm concentration, but the *angular* behavior of the score function matters for the expectations being computed, and this gap is not discussed; (2) the approximation \(\mathbf{E}[\nabla\log p_\alpha / \|\nabla\log p_\alpha\|] \approx 0\) via "integration of normals over the sphere" assumes the normalized score is isotropic on the perturbed sphere, which is precisely what one would not expect for points near a real image \(x_0\); (3) the bias term (Corollary 3) is argued to be zero via MMSE unbiasedness but is not empirically verified. The paper uses "≈" throughout and validates on toy 2D examples, so this is not a fatal flaw — but the paper oversells its theoretical foundation. Reframing the criterion as **motivated by** geometric reasoning rather than **derived from** it would better match the evidence.

- **The LLaVA captioning pipeline is not ablated.** The diffusion model requires text prompts; the paper uses LLaVA 1.5 to generate captions for every input image. This introduces an uncontrolled source of variation — if LLaVA's caption quality systematically differs between real and generated images, the captioning model could confound the criterion. The paper does not ablate this (e.g., with constant prompts like "a photo") or discuss it as a potential confound. Without this ablation, the attribution of performance to the manifold-bias criterion alone is uncertain.

- **No error bars or confidence intervals on the main results (Table 1).** The reported AUC, AP, and Accuracy are point estimates. Given that the claimed margins over baselines are 2–5% (AUC 84.0 vs 70.0 and 74.0 — combining numbers from text descriptions), the reader cannot assess whether these differences are statistically significant without standard deviations or confidence intervals over multiple runs or data splits. Toy experiments (Fig. 3c) include error bars, but the main detection results do not.

- **No computational cost comparison.** The method requires 64 forward passes through Stable Diffusion (plus latent decoding and CLIP encoding) per test image. Competitors (AEROBLADE, RIGID) use substantially lighter pre-trained models. Inference time or FLOPs are not reported, which is relevant for practical deployment scenarios.

- **No direct verification of the "bumpy manifold" for real high-dimensional images.** The paper's central geometric narrative (generated images at probability peaks, real images elsewhere) is validated only on a 2D toy example (Fig. 3). There is no attempt to visualize or quantify the curvature or gradient properties of real vs. generated images in the actual high-dimensional space. The detection results serve as indirect validation, but the disconnect between the motivating geometric story and the empirical evaluation weakens the paper's narrative coherence.

### Trivial
None.

## Nice-to-Haves

- Ablate the LLaVA captioning step by testing with a fixed constant prompt (e.g., "a photo"). If performance is similar, the method becomes simpler and more reproducible; if performance drops, the captioning is a confound that must be discussed.
- Report inference time (seconds per image) and approximate FLOPs relative to AEROBLADE and RIGID to give practitioners a cost-benefit picture.
- Evaluate the MoE with truly few-shot sample sizes (10, 50, 100) to either substantiate or honestly bound the "few-shot" claim.
- Add standard deviations or confidence intervals to Table 1 via multiple evaluation runs or bootstrapping.
- Include a sensitivity analysis of the threshold calibration (mean + 1σ) to show how much the detection performance depends on this specific choice.

## Removed Points

These points from the reviews are removed per the filtering rules. They are recorded here for traceability but should not be counted as weaknesses.

1. **"The paper ignores the bias term in Corollary 3"** — Factually incorrect. The paper explicitly addresses this term in Corollary 3 (lines 178–195), discussing when it is zero (unbiased MMSE denoiser) and when it captures meaningful bias. The term is addressed, not ignored.

2. **"The paper does not discuss the LLaVA captioning as a confound"** — The paper states LLaVA is used to generate "text captions required as input by this model." It does not discuss it as a confound (this is a real weakness kept above), but the critic's phrasing overstated the omission.

3. **"The few-shot setting is incomparable to baselines because 1K is not few-shot"** — This is a framing issue, not an experimental incomparability. The MoE comparison is fair because all methods use the same 1K samples. The kept weakness is about the *label*, not about the comparison being invalid.

4. **Requests for missing appendix/proofs** — Removed per rule: parser strips appendix sections from all papers; they exist in the original submission.

5. **Stylistic/formatting nitpicks** — Removed per rule: parser artifacts are not author errors.

6. **"The paper should also cover Y domain" / scope creep demands** — Removed as not relevant to evaluating the paper as written.

## Novel Insights

The most interesting observation emerging from these reviews is the tension between the paper's strong empirical results (which are genuinely impressive — a +14–20% relative AUC improvement over existing zero-shot methods across 20 diverse generators using a single off-the-shelf diffusion model) and the overclaimed theoretical derivation. The paper would be *stronger*, not weaker, if it explicitly stated that the geometric derivation is a heuristic inspiration that produces a specific, computable inner-product criterion, and then let the comprehensive empirical validation speak for itself. The current framing attempts to claim both theoretical rigor *and* strong empirics, but the rigor claim does not survive scrutiny. Accepting the method as an empirically motivated, practically effective technique — without the pretense of a tight theoretical chain — is both more defensible and more useful to the community.

## Suggestions

1. **Tone down the theoretical overclaim.** Reframe the derivation as a geometric *motivation* for the criterion rather than a rigorous derivation. Acknowledge the uncontrolled approximations (uniform-sphere substitution, isotropic score assumption) and position the criterion as heuristically inspired by curvature-gradient analysis rather than provably equivalent.

2. **Fix the few-shot framing.** Either re-run the MoE with 10–100 labeled samples (matching Cozzolino et al.'s operating regime) or honestly rebrand the 1K-sample experiment as "low-data" rather than "few-shot."

3. **Ablate the captioning pipeline.** Add an experiment with a constant prompt to determine whether LLaVA is essential or is a potential confound.

4. **Add error bars to Table 1** to give readers confidence that the reported margins are not noise.

5. **Report inference costs** to help practitioners assess the method's practical viability.

6. **Add a direct (qualitative or quantitative) analysis** of whether the curvature criterion behaves as expected on real images — even a simple visualization of criterion distributions for real vs. generated images (beyond the scatter plot in Fig. 6 right) would substantially strengthen the connection between the geometric motivation and the empirical method.

## Score and Decision

This paper makes a genuine empirical contribution — a novel zero-shot detection method that demonstrably outperforms existing approaches by a significant margin across a broad set of generative models — and opens a new direction by leveraging diffusion model analysis for this task. However, the paper oversells its theoretical grounding and mislabels its few-shot evaluation, which weakens the presentation. With honest reframing of the theoretical claims and correction of the few-shot terminology, this is a solid paper. I recommend acceptance conditioned on the authors addressing the framing issues.

**Originality**: 7/10 — first diffusion-model-based zero-shot detection framework; novel application of score-function geometry.  
**Quality**: 6/10 — strong empirical evaluation but weakened by uncontrolled theoretical claims and missing error bars/ablations.  
**Clarity**: 7/10 — generally well-written; derivations are laid out step-by-step.  
**Significance**: 7/10 — addresses a timely and important problem with impressive results.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>