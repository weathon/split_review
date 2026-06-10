## Summary

This paper introduces Universally Quantized Diffusion Models (UQDM), a diffusion model variant designed for progressive image compression. The core idea is to replace the Gaussian noise channels of standard diffusion models with uniform noise channels, which allows the use of Universal Quantization (UQ) instead of computationally intractable Relative Entropy Coding (REC) for communicating latents between encoder and decoder. The paper provides theoretical grounding via moment matching to Gaussian diffusion and a continuous-time convergence argument, and demonstrates competitive rate-distortion-realism results against JPEG, JPEG2000, BPG, and the progressive neural codec CTC on CIFAR10 and ImageNet 64×64.

## Strengths

- **Elegant substitution of intractable REC with efficient UQ**: Prior diffusion-based progressive codecs (Theis et al., 2022) required Gaussian channel simulation via REC with exponential runtime in the information content. By replacing Gaussian noise with uniform noise, UQDM enables universal quantization whose complexity "is dominated by the evaluation of the denoising network … which scales linearly with the number of time steps" (line 143). This is a clean, principled solution to a well-known bottleneck.

- **Theoretical connection to established diffusion theory**: Section 3.1 (line 106) shows that UQDM's forward process converges in distribution to a Gaussian as \(T\to\infty\) via the Central Limit Theorem, establishing that the continuous-time limit matches that of VDM (Kingma et al., 2021). This provides a rigorous anchor for the proposed modifications.

- **Competitive rate-distortion-realism against strong baselines**: On CIFAR10, UQDM "consistently outperform[s] both JPEG and JPEG2000 over all bit-rates and metrics" (line 250). On ImageNet 64×64, results are "comparable to, if not slightly better than, CTC" (line 261), a recent progressive neural codec. At high bit-rates, the method continues to improve quality where other codecs plateau — all with a single model covering the full rate range.

- **Controlled ablation validates design choices**: The swirl toy-data experiments (line 174, Figure 2) systematically vary \(T \in \{3,4,5,10,15,20,30\}\) and demonstrate that learning the reverse-process variance significantly improves NELBO across all \(T\). This is not simply inherited from Nichol & Dhariwal (2021) — the paper shows its particular importance in the UQDM setting where optimal \(T\) is small.

- **End-to-end codec implementation validates the theoretical coding cost**: The authors report that "the actual file size [is] within \(3\%\) of the theoretical NELBO" (line 145), providing practical verification that the entropy coding pipeline faithfully realizes the ELBO-predicted codelength.

## Weaknesses

### Major

- **The performance gap to Gaussian diffusion (VDM) is large and its cause is unexplained**. On the swirl toy data, UQDM achieves ~8 bpd at optimal \(T\approx5\) while VDM converges to ~5.8 bpd — a ~40% relative gap (line 174). More concerningly, UQDM's compression performance *degrades* for \(T > 5\), directly contrary to the intuition from the continuous-time convergence argument (which suggests asymptotic approach to VDM). The paper acknowledges this behavior ("a higher T is not necessarily better", line 174) and notes that sample quality (not compression) improves with \(T\) (line 239), but provides no analysis of *why* compression worsens. This is not merely a "gap to close" — it is a structural discrepancy between theory and practice that remains unexamined. Understanding whether the gap stems from the uniform noise approximation itself, the limited optimal \(T\), the logistic+uniform density model, or some interaction among these would substantially strengthen the contribution.

### Minor

- **No runtime or throughput measurements despite tractability being the core claimed advantage**. The paper's headline motivation is that UQDM "avoids the generally exponential runtime of relative entropy coding" (line 19), but no encoding or decoding wall-clock times are reported for any method (UQDM, CTC, JPEG2000). While the theoretical complexity advantage over REC is clear, the practical question of how fast UQDM is relative to other *real* codecs (CTC, JPEG2000) is left unanswered. This would be a welcome addition without being a fatal omission — the theoretical claim stands on its own, but empirical grounding would strengthen the "practical" framing.

- **UQDM uses strictly more parameters than the VDM baseline**. The paper notes that "UQDM uses twice as many output dimensions for both the denoising prediction and learned reverse-process variance" compared to VDM (line 165). This makes the VDM-vs-UQDM comparison slightly asymmetric as a controlled experiment. The extra parameters are justified (learned variance), but the effect on the comparison should be acknowledged.

- **The CTC comparison on ImageNet 64×64 is described only qualitatively**. The paper states results are "comparable to, if not slightly better than, CTC" (line 261) without a numerical table of bpp-PSNR or bpp-FID values. While the rate-distortion curves in Figure 4 convey the comparison visually, a quantitative table would allow precise comparison and reproducibility. (Note: this is a minor presentation issue — the figures themselves are clear.)

### Trivial

- None beyond what is captured above.

## Nice-to-Haves

- A controlled experiment on the swirl data comparing UQDM to a VDM constrained to operate at the same small \(T\) (e.g., \(T=5\)) would help isolate whether the performance gap is due to the uniform noise substitution or simply the small number of timesteps.
- A breakdown of bits allocated across progressive steps would give insight into the coding dynamics and validate the progressive design.

## Removed Points

These points were considered but removed with justification:

- *"VDM comparison is 'hypothetical' and potentially misleading"* — Removed. The paper clearly labels VDM curves as "hypothetical performance of REC that is computationally intractable" (Figure 3 caption). This is a transparent presentation of an upper bound, not a misleading comparison.
- *"No lossless compression results on natural images"* — Removed. The NELBO *is* the lossless compression bound, and it is reported in the figures. The paper explicitly states actual file sizes are within 3% of the NELBO (line 145).
- *"No ablation of learned noise schedule"* — Removed. Line 108 reports that learning the noise schedule "did not yield significant improvements compared to using a linear noise schedule." This constitutes an ablation, albeit a brief one.
- *"Moment matching does not guarantee distributional closeness"* — Removed. This is a theoretical speculation without demonstrated impact on results in this paper. The paper does not claim distributional equivalence — it matches moments.
- *"Line 172 garbled text"* — Removed. Parser artifact, not an author error.

## Novel Insights

None beyond the paper's own contributions. The reviews surface primarily what the paper itself states — the reviews do not independently identify new structural issues beyond the timing/throughput gap and the unexplained VDM compression gap.

## Suggestions

1. Provide a controlled analysis of the VDM gap: compare UQDM against a VDM operating at the same small \(T\) (e.g., \(T=4\) or \(5\)) on the swirl data to disentangle the effect of uniform noise from the effect of limited timesteps.
2. Report encoding/decoding wall-clock times for UQDM and baselines (CTC, JPEG2000) on at least one dataset — this directly addresses the tractability claim.
3. Include a numerical table of rate-distortion/rate-realism values for the CTC comparison on ImageNet 64×64.

## Score and Decision

This paper makes a genuinely novel contribution: the insight that replacing Gaussian noise with uniform noise in the diffusion forward process turns an intractable REC problem into a tractable UQ problem, while maintaining competitive rate-distortion-realism performance. The method is clearly motivated, theoretically grounded, and supported by experiments on both toy and natural-image data. The main unresolved issue is the unexplained gap to Gaussian diffusion (especially the non-monotonic behavior with \(T\)), and the lack of runtime measurements leaves the "tractability" claim empirically unquantified. Nevertheless, the core idea is sound, the results against real codecs are competitive, and the paper is transparent about limitations. At a top venue, this is a solid contribution that presents a promising research direction.

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>