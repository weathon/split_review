- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 8, 5
Now I have all the verification I need. Let me produce the final consolidated review.

## Summary
This paper introduces Diffusion Active Learning (DAL), a framework combining pre-trained unconditional diffusion models with sequential experimental design for adaptive angle selection in X-ray computed tomography. The diffusion model serves as a learned prior to capture structured image distributions (e.g., integrated circuits, composite materials), and the active learning loop uses conditional posterior samples to estimate uncertainty and select the most informative next measurement angle. Experiments on three real-world CT datasets (chip, composite, lung) at 128×128 and 512×512 resolutions show that DAL reduces the number of measurements needed to reach a target PSNR compared to uniform acquisition and several Bayesian baselines (SWAG, Bootstrap, Laplace).

## Strengths
1. **Demonstrated data-efficiency gains on real-world CT datasets.** Table 1 shows that DAL achieves a target PSNR of 30 dB with up to 4.3× fewer measurements than the Laplace baseline (Barbano et al., 2022a) on the composite dataset. Figure 4 shows consistent PSNR improvements over uniform acquisition and competing generative models across all three datasets. These results support the paper's core claim of reducing X-ray dose via adaptive acquisition.

2. **Addresses a genuine limitation of prior Bayesian active learning for CT.** The paper correctly identifies that prior active-learning approaches for CT (Barbano et al., 2022a; Antoran et al., 2023) rely on Laplace approximations that are inherently unimodal (Section 1). The diffusion prior captures multi-modal, highly structured distributions, and the gains are largest on the Chip and Composite datasets—which exhibit strong directional structure—whereas the more isotropic Lung dataset shows smaller improvement, consistent with this motivation.

3. **Computational efficiency through Soft Data Consistency.** Section 3.1 introduces early stopping of gradient steps in the data-consistency optimization rather than solving to convergence. Figure 5 (right) shows DAL runs in under 2 minutes per active-learning step for 512×512 images, substantially faster than the Laplace-based method, making sequential acquisition practical given that micro-/nano-CT scans can take days (Aidukas et al., 2024).

4. **Evaluation across multiple resolutions and realistic datasets.** The experiments use three distinct real-world CT datasets at both 128×128 and 512×512 resolutions (Sections 4.1, 4.3), going beyond the synthetic toy example used in prior work (Barbano et al., 2022a). The pre-scan and no-pre-scan settings provide additional insight into practical deployment scenarios.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **The number of posterior samples k in the acquisition function is not reported or ablated.** The acquisition function (Eq. 3) depends on k samples from the posterior to estimate variance. The paper neither states what value of k was used in the experiments nor studies how performance and computational cost vary with k. This is a meaningful gap because a small k would give noisy uncertainty estimates and a large k increases cost, directly affecting both the quality of active learning and the reported runtime comparisons.

2. **Only a single image-quality metric (PSNR) is reported.** PSNR alone may not capture perceptual or structural fidelity, especially for the highly structured patterns in the chip and composite datasets. SSIM or LPIPS would strengthen the evidence that DAL improves reconstruction quality, particularly since the paper's central claim is about reconstruction quality improvement from better angle selection.

3. **Statistical significance is not fully assessed for the Lung dataset.** In Table 1, the confidence intervals for DAL and Laplace on the Lung dataset overlap (20–24 vs. 20–26 measurements), indicating that the advantage is not statistically significant there. While the paper honestly notes that the Lung dataset shows smaller gains (Section 4.3), it does not explicitly note this overlap.

4. **The diffusion model is trained on cropped/rescaled slices of reconstructed volumes, not on true object distributions.** As described in Section 4.1, the training data for the chip and composite datasets are derived from reconstructed 3D volumes (which themselves are products of reconstruction algorithms). This means the diffusion model learns the distribution of *reconstructed* images rather than ground-truth object slices. This is acknowledged implicitly in the conclusion but should be discussed as a limitation in the experimental setup.

5. **Gaussian noise is assumed but Poisson noise (more realistic for CT) is mentioned but not addressed.** Section 2 notes that noise is "often assumed to be Gaussian or Poisson distributed," yet the method and experiments assume Gaussian noise with known variance. Whether the method extends to Poisson noise (which is more physically realistic for X-ray CT) is not discussed.

6. **The runtime comparison (Figure 5, right) is per-step without controlling for per-method configuration.** The paper reports average running time per active-learning step, but the methods may use different numbers of posterior samples, ensemble members, or convergence iterations. Without specifying these settings, the computational advantage is difficult to interpret as a controlled comparison.

### Trivial
None.

## Nice-to-Haves
- Ablation study on the number of posterior samples k (e.g., k = 1, 5, 10, 20) for at least one dataset.
- Reporting SSIM and/or LPIPS alongside PSNR.
- A diagnostic plot showing whether the posterior sample variance (the acquisition criterion) correlates with actual reconstruction error across candidate angles.
- Total wall-clock time over the full active learning loop (Figure 5 reports per-step time only).

## Removed Points
*These points were flagged for removal per the filtering guidelines; treat them with caution.*

- **Uniform baseline (halving strategy) criticism.** The harsh critic claimed the halving strategy (0°, 90°, 45°, 135°, …) is non-standard and may disadvantage the baseline. **Reason for removal:** In a *sequential* setting where measurement sets are nested (each new angle is added to the existing set), equally-spaced re-sampling at each budget would discard previous measurements—a clearly unfair comparison. The halving strategy is a natural hierarchical non-adaptive baseline that provides good angular coverage at any stopping point. The critic's suggestion does not respect the sequential nature of the experimental design setting.

- **Conditional sampling (Soft Data Consistency) underspecified.** The critic noted the paper says "a predefined, limited number of gradient steps" without specifying step count or learning rate. **Reason for removal:** Per the review guidelines, missing implementation details that reside in the appendix (which the parser has stripped from all papers) should not be treated as weaknesses. The paper states that code is provided in the supplementary material.

- **Introduction "contradiction" about hallucinations.** The critic claimed the paper's remark about artifacts in sparse reconstruction contradicts its main thrust. **Reason for removal:** The paper is honestly acknowledging limitations of the sparse regime; this is not a contradiction but a nuanced caveat consistent with the stated scope.

- **Algorithm 1 mentioned but not shown.** **Reason for removal:** Algorithms, like appendices, are stripped by the PDF parser and exist in the original submission.

- **Related work coverage/style issues.** The critic's comments about disjoint coverage or unclear lineage are subjective and do not identify substantive gaps; the paper adequately situates itself in the diffusion-based inverse problems and active learning literatures.

- **Miscellaneous section-by-section nitpicks** (e.g., score vs. DDPM language, motivation for uncertainty sampling vs. BALD, mention of RL-based methods being beyond scope). These either misunderstand the paper's stated scope or reflect presentation preferences rather than substantive problems.

## Novel Insights
The most interesting observation emerging from the reviews is that DAL's advantage is strongly domain-dependent in a way that validates its design rationale: the gains are largest on datasets with highly directional structure (chips, composites) and minimal on isotropic structures (lung). This is not a weakness but an honest signal that the method works where it should. The reviews do not surface a genuinely novel insight beyond what the paper itself already provides (the combination of diffusion priors with sequential experimental design, the Soft Data Consistency approximation, and the empirical finding that structured data benefits more from adaptive acquisition).

## Suggestions
1. **Report the value of k used in Eq. (3)** and include a small ablation (e.g., k ∈ {1, 5, 10, 20} on one dataset) to show how it affects PSNR and runtime.
2. **Add a second metric (SSIM)** to Table 1 and Figure 4 to strengthen the image quality evaluation.
3. **Explicitly note in the text** that the Lung dataset confidence intervals overlap in Table 1, and qualify the claim accordingly.
4. **Acknowledge the reconstructed-slice training bias** explicitly in the experimental setup section, not only in the conclusion.
5. **Report total wall-clock time** for the full active learning loop (100 steps) in addition to per-step runtime, to give a fully interpretable computational cost picture.
