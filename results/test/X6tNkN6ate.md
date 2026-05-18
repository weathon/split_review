Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper establishes a theoretical connection between denoising diffusion models and tractable information-theoretic quantities, deriving exact expressions for pointwise mutual information (PMI) and conditional mutual information (CMI) that can be decomposed per pixel due to the squared-error structure of the MMSE denoiser. The authors validate this framework across three tasks: (1) compositional understanding on the ARO benchmark, where their information-based score substantially outperforms both OpenCLIP and prior diffusion-based ITM methods; (2) unsupervised object segmentation, where information complements attention to improve mIoU; and (3) prompt intervention analysis, where CMI better predicts the effect of word modifications than attention.

## Strengths

1. **Novel theoretical link between diffusion models and tractable fine-grained information quantities.** The paper derives exact expressions for pointwise MI and CMI (Eqs. 5-6) that depend only on the denoiser's outputs, and shows they decompose per pixel (Eq. 8). This goes beyond average MI or attention-based methods and opens new possibilities for analyzing diffusion models at the sample and variable level.

2. **Substantial improvement on compositional understanding evaluation (ARO).** Using $\ii^o(\vx;\vy)$ as the alignment score, Stable Diffusion achieves 72.0% on VG-A (vs. 64.6% for OpenCLIP) and 69.1% on VG-R (vs. 51.4% for OpenCLIP) (Table 1). This decisively shows that prior diffusion-based methods using MMSE or attention scores underestimated compositional capabilities.

3. **CMI is measurably better than attention at predicting intervention effects.** On the prompt intervention task, CMI yields higher Pearson correlation with image changes at both image level (0.34 vs. 0.24) and pixel level (0.27 vs. 0.21) (Table in Fig. 5), validating that information flow captures dependence more reliably than attention.

4. **Information complements attention for unsupervised segmentation.** Adding pixel-wise CMI to attention ("Attention+Information") raises mIoU from 34.52% to 42.46% on COCO-IT (Table 2), demonstrating complementary value even though CMI alone underperforms attention.

5. **Architecture-agnostic framework.** The method requires only the denoiser outputs (not internal attention layers or specific network designs), making it applicable across diffusion architectures.

## Weaknesses

### Fatal
None.

### Major

1. **No validation of information estimates against known ground truth.** All experiments rely on the approximation that pretrained Stable Diffusion is an optimal MMSE denoiser, yet no calibration experiment is provided — neither on synthetic data with known MI (e.g., Gaussian sources) nor on a simple controlled setting. Lines 136-137 acknowledge that estimates are "neither upper nor lower bounds" but the paper never validates that the approximation is reliable. This is especially problematic for the ARO benchmark (Table 1), where claims about prior methods "underestimating" compositional understanding depend on the absolute accuracy of the information-based scores. Without a calibration experiment, it is unclear whether the reported numbers reflect genuine information-theoretic quantities or artifacts of approximation error.

### Minor

2. **Conceptual overclaiming about information decomposition (partially acknowledged).** The abstract states "a natural non-negative decomposition of mutual information emerges" (line 10), and the pixel-wise decomposition is treated as per-variable information contributions. The paper acknowledges the synergy/redundancy problem (line 120) and states the decomposition "does not explicitly separate unique and redundant components" (line 302), but the framing in the abstract and contributions list still implies a stronger information-theoretic decomposition than what is actually provided. The decomposition is a per-pixel split of the pointwise log-likelihood ratio that is coordinate-dependent and not invariant to invertible transforms — this limitation should be stated upfront rather than deferred to the related work section.

3. **Intervention correlations are modest, and L2 is a poor perceptual proxy.** The reported Pearson correlations (0.34 image-level, 0.27 pixel-level) show CMI outperforming attention, but the effect sizes are modest and no test for statistical significance of the *difference* between correlations is provided (the paper does report standard errors for each, which is good — the reviewer's claim that no uncertainty is reported is incorrect; see Fig. 5 lines 284-285). More importantly, using L2 distance in pixel space as the ground-truth "change" metric is known to be a poor proxy for perceptual change. The paper would benefit from using a perceptual metric (e.g., LPIPS) or at minimum discussing this limitation.

4. **ARO improvement source not fully disentangled.** The paper compares against DiffITM (MMSE-based score from the same Stable Diffusion model) and shows improvement, which partially isolates the benefit of the information-theoretic score. However, the paper does not ablate whether the improvement comes from the information decomposition itself or simply from using a generative likelihood-based score (e.g., comparing $\ii^o$ against $-\log p(\vx|\vy)$ directly, or against $\ii^s$ which has higher variance). Such an ablation would strengthen the attribution of the improvement to the specific estimator design.

### Trivial

5. The phrase "pointwise information" and "mutual information" are used somewhat interchangeably in the abstract and results discussion (e.g., line 10 vs. line 96-97), which may confuse readers about the average vs. sample-specific distinction. This distinction is made clearly in §2 but could be reinforced in the abstract.

## Nice-to-Haves

- A synthetic experiment validating the estimator (e.g., Gaussian sources with known MI) would substantially strengthen the paper.
- Analysis of the bias-variance tradeoff between $\ii^s$ and $\ii^o$ in the experimental settings would help practitioners choose between them.
- Exploring *why* information features help segmentation (e.g., whether CMI provides edge information or focuses on discriminative details) would deepen the contribution.
- Using LPIPS or a similar perceptual metric for the intervention experiment would make the quantitative claims more robust.

## Removed Points

- **"No confidence intervals or significance tests for intervention correlations"** — The paper does report standard errors (shown as ± values in Fig. 5). This sub-point is factually incorrect and removed.
- **"Method cannot be independently verified / not yet released"** — The paper cites open-source code and uses publicly available models. Removed per hard rule against questioning availability.
- **"Missing related works"** — Removed per hard rule against mentioning missing related works without external confirmation.
- **"Formatting/style nitpicks"** — Removed per hard rule.

## Novel Insights

The key insight that emerges from the reviews is that the paper's strength lies not in proposing a theoretically rigorous information decomposition (which it does not fully achieve — the decomposition is coordinate-dependent and heuristic), but rather in showing that the squared-error structure of diffusion models yields practical, usable estimators for fine-grained relevance attribution that consistently outperform attention across multiple tasks. The paper is best understood as an empirical demonstration of a useful heuristic grounded in a principled derivation, not as a formal resolution of the information decomposition problem. The most interesting finding cutting across the experiments is that CMI, unlike attention, correctly identifies when context renders a word uninformative — a property that is both theoretically grounded and practically useful for understanding model behavior.

## Suggestions

1. **Add a synthetic validation experiment.** Even a simple setup (e.g., Gaussian sources where the true MI is computable analytically, or a controlled image-text setup with known ground-truth dependencies) would address the most fundamental vulnerability.

2. **Clarify the status of the pixel-wise decomposition in the abstract and §1.** State upfront that this is a per-dimension attribution of the pointwise estimator exploiting the squared-error form, not a unique information decomposition in the formal sense (e.g., separating synergy/redundancy). This would prevent readers from overinterpreting the results.

3. **Add an ablation in ARO comparing $\ii^o$ against a direct likelihood score** (e.g., $-\log p(\vx|\vy)$ or $\ii^s$) to isolate whether the orthogonality-based estimator adds value beyond the generative model's likelihood.

4. **Replicate the intervention experiment with a perceptual distance metric** (LPIPS) alongside L2, and report the significance of the *difference* between CMI and attention correlations (e.g., bootstrap confidence interval on the gap).

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>