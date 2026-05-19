- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 5, 5, 5, 3, 3, 3, 3
Now I'll produce the final consolidated review.

## Summary

SuperMark proposes a training-free image watermarking framework that exploits the symmetry between watermark embedding/extraction and the denoising/noising processes in diffusion models. It embeds watermarks into the Gaussian noise used by a pretrained diffusion-based Super-Resolution (SR) model, then extracts them via DDIM Inversion. The framework achieves 99.46% bit accuracy under normal distortions and 89.29% under adaptive attacks while maintaining competitive fidelity (PSNR 32.49, SSIM 0.93), without any training of the watermark encoder/decoder.

## Strengths

- **Training-free framework with frozen pretrained models.** The method requires no training of an encoder or decoder (Section 3.1, Figure 1). It uses a pretrained SR model with frozen parameters, in sharp contrast to every deep-learning baseline in Table 1 (StegaStamp, RoSteALS, Robust-Wide, etc.) which need expensive joint training of an encoder–noise layer–decoder pipeline.

- **Unmatched robustness against adaptive attacks.** Table 1 shows SuperMark achieves 89.29% bit accuracy under adaptive attacks (VAE-based and diffusion-based), whereas all other methods fall to near-random accuracy (e.g., SepMark 48.64%, DwtDctSvd 50.56%, StegaStamp 50.90%). No other baseline exceeds 55%.

- **Highest robustness under normal distortions.** Table 1 reports 99.46% average bit accuracy across JPEG compression, Gaussian noise, cropping, blur, and brightness changes — the highest among all 9 baselines. The next best (ZoDiac) reaches 94.80%.

- **Competitive fidelity while setting robustness records.** PSNR of 32.49 and SSIM of 0.93 (Table 1) match or exceed methods like SepMark (PSNR 32.50, SSIM 0.96) while far surpassing ZoDiac (PSNR 26.88, SSIM 0.79), directly supporting the claim of balancing robustness and fidelity.

- **Transferability across datasets, SR models, and injection methods.** Table 2 shows >99% bit accuracy on DiffusionDB, WikiArt, CLIC, and MetFACE. Table 3 demonstrates the SR model can be swapped (LDM-SR works comparably). Table 4 shows Tree-Ring injection works with the framework, enabling superior robustness against geometric distortions (99.7% WDR vs. ZoDiac's 80.4% under rotation).

## Weaknesses

### Fatal
None.

### Major

- **Questionable multi-bit comparison with ZoDiac (Table 1).** The paper describes ZoDiac as using Tree-Ring's ring-shaped watermark (Section 2.3), and explicitly states in Section 4.3 that "Tree-Ring is a 0-bit watermark method" — yet Table 1 lists ZoDiac with a 1000-bit payload and compares its bit accuracy against SuperMark's 32-bit system. No explanation is given for how ZoDiac was adapted for multi-bit extraction. This comparison is either invalid (if ZoDiac does not support multi-bit extraction) or insufficiently documented. The proper 0-bit comparison in Table 4 shows SuperMark also wins but with a narrower margin. The multi-bit entry in Table 1 inflates the apparent gap and should be removed or rigorously justified.

- **Non-uniform bit payloads across baselines (Table 1).** Methods in Table 1 use different bit payloads: ZoDiac with 1000 bits, StegaStamp with 100 bits, and most others with 30–32 bits. Since higher payloads are harder to recover accurately, comparing raw bit accuracy across different payloads is misleading. Either payloads should be standardized or a payload-normalized metric should be reported.

### Minor

- **No per-distortion breakdown of robustness.** Only average accuracy across "normal" and "adaptive" categories is reported. For a method claiming to be "robust," it is important whether the 99.46% average reflects uniformly high performance across all distortions or is driven by near-perfect results on some attacks while degrading on others (e.g., cropping, rotation). This limits assessment of the method's actual robustness profile.

- **Conditioning mismatch between embedding and extraction is not analyzed.** During embedding, the SR model conditions on the downscaled *original* image; during extraction, DDIM inversion conditions on the downscaled *distorted watermarked* image. These differ whenever the image is distorted. The paper attributes robustness to DDIM inversion's "inherent resilience" but does not analyze how much reconstruction error this mismatch introduces or how it varies with distortion strength. This is a gap in understanding the method's mechanism, though the strong empirical results suggest the mismatch is well-tolerated.

- **No computational overhead data.** The paper acknowledges substantial inference overhead from multiple diffusion steps and points to acceleration techniques (Section 3.5), but provides no concrete timing numbers (e.g., seconds per image for embedding and extraction). Without this, readers cannot assess practical feasibility.

- **No discussion of failure cases or limitations.** The paper is uniformly positive. The kinds of distortions or attacks that *do* degrade performance are not discussed. Acknowledging limitations would strengthen the paper's honesty and guide future work.

### Trivial

- **Confusing phrasing in Section 3.3.** The sentence "Due to the change in the size of the original image $I_{ori}$, caused by the SR model $\mathcal{M}$, the super-resolved image $I_{sr}$ cannot be directly used as the watermarked image" is confusing: the SR model changes the size of its *input*, not the original image. The actual procedure (downscale original → SR → residual correction) is correct and clear from the rest of the section, but this sentence should be reworded.

## Nice-to-Haves

- **Per-distortion breakdown table.** Reporting bit accuracy for each distortion type individually (JPEG at various quality factors, cropping at various ratios, etc.) would allow readers to identify specific strengths and weaknesses of the method.
- **Sensitivity analysis on $S_{low}$ and $f_s$.** These two hyperparameters directly control the robustness–fidelity trade-off claimed in Section 3.3. A simple Pareto plot would be strong evidence for the claimed "unified" handling of this trade-off.
- **Controlled experiment on the conditioning mismatch.** Measuring DDIM inversion reconstruction error (e.g., MSE between $Z_{wm}^T$ and $Z_{wm}'^T$) as a function of distortion strength would isolate the source of robustness more cleanly than adding more attack types.
- **Error bars or statistical significance.** Reporting standard deviations across the 500 test images would help assess whether the reported advantages are reliable.

## Removed Points

These points were raised in reviews but are removed with justification:

1. *Criticism that Section 4.1 does not justify $S_{low}=128$ and $f_s=0.4$ and references a missing Section 4.4.* **Removed** — The paper states these are explored in Section 4.4, which the parser strips (it likely existed in the original submission). Per the rules, missing appendix content is not a valid weakness.

2. *Criticism that the paper does not specify exact parameters of each distortion (JPEG quality factor, crop ratio, Gaussian blur kernel size, noise variance, etc.).* **Removed** — These details are standard experimental configuration and would reasonably appear in a supplementary/appendix section that was stripped by the parser.

3. *Criticism that baseline configurations are not described.* **Removed** — The paper states baselines are "open-source" (Section 4.2), and their original papers define their standard configurations. Requesting re-description here is scope creep.

4. *Criticism that the paper does not specify exact resolutions in Section 3.4 for handling spatially-varying distortions.* **Removed** — The extraction resolution procedure is clearly described: upscale to match $I_{sr}$ resolution, downscale to match $I_{low}$ resolution. The specific values (128 and 512) are given in Section 4.1.

5. *The critic's claim that the conclusion "improving capabilities of the SR model enhances robustness" (from Table 3) is weakly supported.* **Weakened and moved** — This is a straightforward conclusion from a valid experiment (stronger SR model → better results). It is not a weakness of the paper; it's a logical finding. Removed as a criticism.

6. *The critic's claim that the abstract's claim about limitations stemming from "entanglement between robustness and fidelity" is circular.* **Removed** — The paper does not claim to *prove* this insight from experiments alone; it presents it as a motivating observation supported by the results. This is standard framing, not circular reasoning.

## Novel Insights

None beyond the paper's own contributions. The reviews largely corroborate the paper's claimed strengths while identifying one substantively problematic comparison (ZoDiac multi-bit) and several areas where additional detail or analysis would strengthen the presentation. No reviewer identified a fundamental flaw in the core methodology or uncovered a finding the authors missed.

## Suggestions

1. **Address the ZoDiac comparison in Table 1.** Either (a) remove the multi-bit ZoDiac row entirely (Table 4 already provides a valid 0-bit comparison where SuperMark also wins), or (b) provide a detailed explanation of how ZoDiac was adapted for 1000-bit extraction and why that adaptation is valid. Current presentation is misleading.

2. **Standardize bit payloads across Table 1 baselines, or report payload-normalized accuracy.** At minimum, add a footnote explaining why payloads differ and whether accuracy comparisons across different payloads are valid.

3. **Add a per-distortion breakdown table** (potentially in the main text or appendix) showing bit accuracy for each distortion type individually, with parameters. This would greatly strengthen the robustness claim.

4. **Add a brief discussion of failure cases or limitations** (e.g., "performance degrades under X/Y/Z conditions") to improve the paper's completeness and honesty.

5. **Fix the unclear sentence in Section 3.3** about "change in the size of the original image caused by the SR model" to avoid reader confusion.
