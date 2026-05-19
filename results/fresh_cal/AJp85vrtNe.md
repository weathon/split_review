Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper introduces the VAE-AD Test, a method that applies conditional selective inference (CSI) to assign valid p-values to anomalies detected by a Variational Autoencoder. The core technical insight is that VAE-based anomaly detection (reconstruction error computation + thresholding) can be characterized as a piecewise-assignment function when the VAE uses piecewise-linear operations, which enables the application of CSI theory to control false positive rates. The paper provides theoretical development (Theorem 1, Lemma 1), an algorithm for computing truncation intervals via parametric programming and auto-conditioning, and preliminary experimental illustrations.

## Strengths

- **First principled statistical test for VAE-based AD with Type I error control.** The paper correctly identifies the double-dipping problem in VAE-based anomaly detection (the same data is used to select the anomaly region and to evaluate it) and develops a rigorous solution via selective inference. The related work section confirms no prior work provides theoretically-valid p-values for VAE-based AD. The illustrative example in Figure 1 demonstrates the practical benefit: the selective p-value correctly reports a true negative (0.668) where the naive p-value falsely flags 0.000.

- **Novel theoretical grounding of VAE-based AD in the CSI framework.** Lemma 1 and the analysis in §4.4 show that when a VAE uses piecewise-linear components (ReLU, convolution, max-pooling, etc.), the entire anomaly detection pipeline — reconstruction error computation plus thresholding — is a piecewise-assignment function. This bridges VAE-based AD with the existing CSI literature (Lee et al., 2016; Duy et al., 2022; Miwa et al., 2023), which had not previously addressed VAEs. Theorem 1 then provides the truncated normal distribution needed for valid selective p-values.

- **Flexibility to general test statistics beyond mean-difference.** Equation (6) formulates the null hypothesis for an arbitrary linear contrast ηᵀs, covering not only mean differences but also maximum differences, filtered differences, and other practically useful quantities. This generality is explicitly stated and widens the method's applicability.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed generality of the piecewise-linearity assumption without specifying admissible architectures.** The paper states (§4.4) that "most of basic operations and common activation functions... can be represented as piecewise-linear functions" and that this "applies to the majority of CNN-type deep learning models." However, common VAE components — sigmoid or tanh output layers (standard for bounding pixel values), and softplus/exp for variance parameterization — are not piecewise-linear. While Lemma 1 is conditionally correct ("which uses piecewise-linear functions in the encoder and decoder network"), the prose implies broader applicability than is justified. The paper never states exactly which VAE architectures are admissible, nor does it specify whether the experiments used a VAE with exclusively piecewise-linear activations (e.g., ReLU everywhere with linear output). This overclaiming weakens a core theoretical pillar; fixing it requires a clear, explicit characterization of the admissible model class rather than vague hedging.

- **No empirical or theoretical analysis of scalability.** The method's computational tractability is central to its practical value. Computing the truncation intervals Z requires walking along a line through the polytopes of a deep piecewise-linear network, whose number can grow exponentially with depth and width. The paper describes Algorithm 1 (parametric programming) and auto-conditioning but provides no runtime measurements, no analysis of how the number of traversal steps scales with image size or network depth, and no demonstration on architectures of realistic size (e.g., for medical images). Section 7 acknowledges the computational cost as a limitation, acknowledging it "increases" with network size, but does not quantify this or provide evidence that the method is feasible beyond minimal toy examples. Until scalability is demonstrated, the method's practical relevance for the motivating application (medical imaging) remains unsubstantiated.

### Minor

- **No discussion of power or the trade-off with naive p-values.** The paper shows that the naive p-value is anti-conservative (inflated Type I error) and the selective p-value controls it. But a selective test that trivially returns p=1 everywhere would also control Type I error. The paper does not report power under the alternative or compare the selective test's detection ability against the naive test. The illustrative example in Figure 1 is promising (p_selective=0.000 for the anomalous image) but this is a single instance, not a systematic evaluation. Reporting the empirical CDF of selective p-values under the null (for uniformity) and power curves under the alternative is standard for a statistical test paper and is currently missing from the extracted text.

- **Minimal description of covariance estimation.** The statistical model (§3) assumes X = s + ε with ε ~ N(0, Σ), and states only that Σ is "estimated using normal data different from that used for the training of the VAE." No details are given about whether Σ is assumed diagonal, how many images are used for estimation, what estimator is employed, or how estimation error affects the validity of the selective p-values. Since the truncated normal distribution in Theorem 1 directly depends on Σ, this is a non-trivial practical detail.

- **No discussion of multiple testing across multiple anomaly regions.** When several disjoint anomaly regions are detected in a single image, the paper does not clarify whether the proposed p-value controls per-region error or image-level error, or how multiplicity should be handled. This is a natural question for the intended application (medical imaging) and should be addressed.

### Trivial

- The Experiments section (lines 228–293) in the extracted text consists primarily of figure references, line numbers, and fragmented sentences. This appears to be largely a parser artifact, but even accounting for that, the textual description that remains (baselines "OC" and "Bonf" briefly named, two covariance structures mentioned without follow-up, no numerical results) is unusually thin for a paper making empirical claims. If the original submission had complete experimental content (calibration plots, power curves, runtime tables), the parser has removed it; the paper should ensure the experiments are fully present and self-contained in the main text.

## Nice-to-Haves

- A clear statement of whether the specific VAE used in experiments employs ReLU activations exclusively (including in the decoder output layer) or whether some smooth activations are present. If smooth activations are used, a justification or error analysis for the piecewise-linear approximation would strengthen the paper.
- A discussion comparing the proposed CSI approach with other principled uncertainty quantification methods for deep AD, such as conformal prediction.
- A theoretical or empirical bound on the number of polytope traversals during the parametric line search as a function of network depth/width, to give the reader a realistic sense of when the method is practical.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No discussion of power relative to naive p-values"** — *Retained in Minor above, not removed.*
- **Criticism that the paper does not "specify the architecture used in experiments"** — This is partially accurate (not in the extracted text), but the extracted Experiments section is clearly truncated by the parser; I cannot determine whether the original PDF contained this information. I have noted the parser issue as a Trivial point instead of a substantive weakness.
- **"The role of the variance output is never discussed"** — The paper does state at line 39 that the reconstruction uses μ_θ(μ_ϕ(x)), i.e., only the mean outputs at test time. This point is factually incorrect as a criticism; the role is described, albeit briefly. Removed.
- **Strength Finder point 3: "Efficient computation via parametric programming and auto-conditioning"** — The paper describes the approach as efficient but provides no empirical validation of efficiency. Without runtime data, this strength is unsubstantiated and conflicts with the verified weakness about missing scalability analysis. Removed.
- **Strawman about missing related works** — Removed per instructions.
- **Formatting/style nitpicks** — Removed per instructions.
- **Speculation about whether the paper "cannot be independently verified"** — Removed per hard rules about questioning existence of cited entities.

## Novel Insights

None beyond the paper's own contributions. The core insight — that VAE-based AD can be cast as a piecewise-assignment function for the purposes of selective inference — is the paper's main contribution, and the reviews do not surface any deeper or unexpected observations beyond what the paper itself claims.

## Suggestions

1. **Explicitly define the admissible VAE class.** Replace the vague "most common activation functions" language with a precise architectural specification: list exactly which operations are allowed (ReLU, leaky ReLU, linear/conv layers, max-pooling, etc.) and which are excluded (sigmoid, tanh, softplus, etc.), or justify why the latter can be omitted or approximated. State the exact VAE architecture used in experiments and confirm it satisfies the piecewise-linearity requirement.

2. **Provide systematic experimental evidence.** Report (a) the empirical CDF of selective p-values under the null (calibration plot) to verify uniformity, (b) power curves under alternative hypotheses at various signal strengths, (c) wall-clock time and the number of polytope steps for a range of image sizes (e.g., 16×16, 32×32, 64×64) to demonstrate scalability, and (d) the VAE architecture details (layers, activations, latent dimension).

3. **Provide details on covariance estimation.** Describe how Σ is estimated, whether it is diagonal or structured, and how estimation error propagates. If the method relies on a clean hold-out set of normal images for this purpose, state the size of that set.

4. **Address multiple testing.** Clarify whether the method controls per-region or per-image error, and discuss how the Bonferroni baseline relates to the proposed approach in the multi-region setting.

5. **Quantify the power/Type-I-error tradeoff.** Report both the selective p-value and the naive p-value under identical settings to illustrate the cost of controlling Type I error in terms of detection power.

## Score and Decision

The paper tackles an important and well-motivated problem — principled uncertainty quantification for VAE-based anomaly detection — and makes a genuinely novel theoretical connection between VAE-based AD and selective inference. The mathematical framework is sound under the stated assumptions. However, two major issues prevent acceptance: the paper overclaims the generality of the piecewise-linearity assumption without precisely specifying admissible architectures, and it provides no evidence that the computational procedure scales beyond toy examples. The experimental evidence in the extracted text is too incomplete to fully verify the empirical claims. These weaknesses are substantive and require resolution; they do not invalidate the core idea but do mean the paper is not ready for publication in its current form.

**MY FINAL SCORE: <score>5.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**