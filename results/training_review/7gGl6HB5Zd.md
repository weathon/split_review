Now I have a thorough understanding of the paper and have verified the reviewer claims against the actual content. Let me produce the final consolidated review.

## Summary

This paper introduces a zero-shot and few-shot framework for detecting AI-generated images, grounded in the geometry of a pre-trained diffusion model's learned probability manifold. The authors derive a scalar criterion \(C(x_0)\) combining curvature and gradient statistics (Eq. 18) via score-function analysis and Gauss divergence theorem, and evaluate it across 20 generative techniques. The method achieves higher average AUC, AP, and Accuracy than AEROBLADE and RIGID in zero-shot settings, and improves performance when combined with Cozzolino et al. (2024) in a mixture-of-experts framework.

## Strengths

- **Novel theoretical grounding for zero-shot detection**: The paper is the first to derive a mathematically principled detection criterion from diffusion model manifold geometry, connecting score-function approximations (Eq. 5) to curvature and gradient quantities (Eqs. 7–8) via Gauss divergence theorem (Claim 1, Corollaries 2–3). This directly addresses the gap of missing theoretical foundations in prior zero-shot image detectors.

- **State-of-the-art empirical performance across 20 generative models**: In zero-shot evaluation (Table 1, Fig. 5), the method achieves higher average AUC, AP, and Accuracy than AEROBLADE and RIGID. Per-technique results (Fig. 5b) show the proposed method scores highest on the majority of the 20 techniques, spanning GANs, diffusion models, and commercial tools.

- **Robustness to image corruptions and hyperparameter variations**: Sensitivity analysis (Table 2) shows only modest AUC drops under JPEG compression (−3.45%) and Gaussian blur (−1.2%), and little variation when changing the base diffusion model (SD v1.4, v2 Base, Kandinsky 2.1), perturbation count \(S\), or noise level \(\alpha\).

- **Practical threshold calibration using only real images**: The paper recommends calibrating the decision threshold on a small set of real images (mean + one standard deviation, Fig. 4a), avoiding any reliance on generated data. This makes calibration feasible in truly zero-shot deployment.

- **Toy-data validation of theoretical assumptions**: Simulations (Fig. 3a) confirm that reverse diffusion trajectories converge to local maxima of the learned probability manifold. The curvature estimator \(\kappa\) is shown to be empirically unbiased and consistent (Fig. 3b–d), bridging theory and practice on low-dimensional data.

## Weaknesses

### Fatal

None.

### Major

- **The CLIP mapping severs the theoretical connection.** Section 4.3 states: "We map data and noise predictions to CLIP before calculating \(C(x_0)\)." The entire theoretical derivation (Section 4) operates on the diffusion model's learned probability manifold in its native space. The curvature and gradient criteria \(a\kappa - D\) are integrals involving \(\nabla\log p_\alpha\), which exists in that space. Mapping to CLIP changes the geometry arbitrarily, and the paper provides no argument — theoretical or empirical — that CLIP embeddings preserve the relevant manifold properties (local maxima, curvature, gradient norms). This means the actual algorithm is not guaranteed to implement the mathematical framework. The criterion computed in CLIP space is a heuristic whose relationship to the derived quantities is unknown. This is the most significant weakness because it undermines the paper's central claim of a theoretically grounded method. While strong empirical results are presented, the theoretical contribution is partially decoupled from the implementation.

### Minor

- **Same-model vs. cross-model separation is not explicit.** The test set includes images from Stable Diffusion (Rombach et al. 2022), which is the same model used as the backbone. While Fig. 5b does provide per-technique AUC, the paper does not explicitly label which technique corresponds to Stable Diffusion, nor does it separately aggregate same-model vs. cross-model performance. Given that only 1 of roughly 20 techniques is the backbone model, this is unlikely to drive the aggregate results, but the omission is a clarity issue that should be addressed.

- **Missing a natural ablation baseline: reconstruction error from the same diffusion model.** The method computes noise predictions \(h(\tilde{x})\) via the diffusion model and uses a specific inner-product criterion. A straightforward baseline would be to use \(\|x_0 - f(\tilde{x})\|^2\) or \(\|h(\tilde{x})\|\) from the same SD model as a zero-shot detector. AEROBLADE uses VAE reconstruction error (a different architecture), so it does not control for the backbone choice. Including this baseline would isolate whether the curvature/gradient derivation in the criterion adds value beyond a simple denoising-based signal.

- **The "few-shot" regime uses 1K labeled samples.** While the zero-shot method itself requires no generated data, the mixture-of-experts evaluation trains a lightweight classifier on 1K labeled samples. This is on the high end of what is conventionally considered "few-shot" (which typically involves tens of samples per class). Reporting results at standard few-shot sizes (e.g., 1, 5, 10, 20, 50 per class) would better substantiate the "few-shot" claim and enable direct comparison with Cozzolino et al. (2024) under their standard protocol.

- **Key mathematical approximations are validated only on synthetic 2D data.** The derivation relies on (a) interchangeability of \(\tilde{x}\) with Gaussian forward-diffusion samples \(x_t\) (concentration of measure), (b) \(\mathbf{E}_{x\sim\tilde{x}|x_0}\langle \nabla\log p/\|\nabla\log p\|, x_0\rangle \approx 0\), and (c) choosing \(\alpha\) small enough for smoothness yet large enough for the perturbation to be meaningful. These are justified with references and toy examples (Figs. 3, 4b), but empirical verification on actual image data (e.g., showing that \(\kappa\) and \(D\) behave as predicted for real vs. generated images, or that the Monte Carlo estimate correlates with the true \(a\kappa-D\)) is absent. The method remains partially heuristic in high-dimensional image space.

### Trivial

- The derivation from Equations 12–16 contains abbreviated algebraic steps; the transition from Equation 12 to Corollary 2 could be expanded for clarity.

## Nice-to-Haves

- Evaluate the method without the CLIP mapping (in the diffusion model's native latent space) to see whether the theoretical derivation holds up empirically. If performance degrades, the theoretical connection needs to be re-established; if it remains strong, the CLIP stage may be unnecessary but harmless.
- Test the diffusion model backbone on a model that was not part of the training-data generators at all (e.g., an open-source model not used by any test generator) for a cleaner test of cross-technique generalization.
- Add the diffusion-model reconstruction error as a baseline.
- Report few-shot results at smaller sample sizes (1, 5, 10, 50 per class).

## Removed Points

These points were flagged by reviewers but removed after verification against the paper. Treat them with caution.

- **"The paper reports only aggregate results across all 20 techniques, making it impossible to determine whether generalization is real or driven by the within-model subset."** — Factually incorrect. Fig. 5b provides per-technique AUC. The paper explicitly says "Plot b details AUC per technique." Removed.
- **"The 'first-of-its-kind curvature-based zero-shot framework' claim is overstated because Mitchell et al. already used curvature."** — Mitchell et al. (2023) worked on generated **text** detection, not images. The paper's claim is specifically about **image** detection, where no prior curvature-based zero-shot method existed. Removed.
- **"The definition of B0 with radius sqrt(dα) has no justification and the perturbation magnitude grows with d."** — The paper justifies this via concentration of measure (Laurent & Massart 2000), noting that \(\|\epsilon\|\) concentrates around \(\sqrt{d}\) in high dimensions, making \(u_d\) and \(\epsilon\) interchangeable. Fig. 4b–c illustrates this. The criticism ignores this justification. Weakened to trivial and moved here.
- **"The paper should not be accepted in its current form."** — This is a decision recommendation, not a weakness. Judgments about acceptance are outside the scope of weakness identification.

## Novel Insights

The reviewer who identified the CLIP mapping problem made an important observation that goes beyond what the paper itself acknowledges: the theoretical derivation is both the paper's main novelty and its weakest link, because the implementation discards the space in which the theory operates. This is not a typical "theory-practice gap" — it is a case where the theory is rigorous in one space and the algorithm runs in another without any bridging argument. The review also draws attention to the non-triviality of the approximation \(\mathbf{E}[\langle \nabla\log p/\|\nabla\log p\|, x_0\rangle] \approx 0\), which the paper treats too casually given that \(\tilde{x}\) contains a deterministic \(x_0\) component. These observations suggest the paper would benefit from either (a) a deeper theoretical justification for the CLIP mapping (e.g., showing it preserves angle-based ordering), or (b) reframing the contribution as an empirically motivated heuristic with a suggestive but ultimately separate theoretical motivation.

## Suggestions

1. **Address the CLIP-theory gap.** Either provide a rigorous argument (or empirical evidence) that CLIP mapping approximately preserves the relative ordering of the curvature-gradient criterion, or evaluate the method in the diffusion model's native space. If performance in native space is comparable, the theoretical contribution is restored. If not, the paper should honestly reframe itself as presenting a well-motivated heuristic whose theoretical derivation provides intuition but not a rigorous guarantee.

2. **Explicitly separate same-model and cross-model results** in the per-technique analysis (Fig. 5b), even if only in a supplementary table. This would preempt concerns about the backbone model contaminating the evaluation.

3. **Add the diffusion-model reconstruction error baseline** (e.g., \(\|x_0 - f(\tilde{x})\|^2\) or the norm of the noise prediction). This is a lightweight experiment that would strengthen the paper by isolating what the curvature/gradient criterion contributes.

4. **Test at genuine few-shot sizes** (e.g., 1, 5, 10, 20 samples per class) in the MoE setup. If performance degrades, the claim should be softened; if it holds, the claim is strengthened considerably.

5. **Validate the key approximations on real images.** Show that \(\kappa\) and \(D\) individually behave as predicted for real vs. generated images, or that the Monte Carlo estimate of \(C(x_0)\) correlates with ground-truth \(a\kappa - D\) on controlled synthetic data with known geometry. This would significantly bolster the theoretical claims.

## Score and Decision

The paper makes a genuine contribution by introducing a novel, theoretically motivated approach to zero-shot generated image detection and demonstrating strong empirical results across a wide range of generative techniques. The main weakness — the unjustified CLIP mapping — creates a disconnect between the theory and the implementation that the authors can address in revision. The remaining issues (missing baselines, few-shot terminology, abbreviated derivations) are manageable. The paper advances the field's understanding of manifold-based detection and provides a practical method with robust performance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>