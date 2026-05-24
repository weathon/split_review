Now I have verified the key claims against the paper. Let me produce the consolidated review.

## Summary

WATER-GS proposes a watermarking method for 3D Gaussian Splatting (3DGS) that fine-tunes a pre-trained 3DGS model using a fixed watermark decoder (trained on COCO via a HiDDeN-style pipeline) to embed imperceptible binary messages into rendered images from any viewpoint. The key novelty is the introduction of **3D distortion layers** (Gaussian noise, point dropout, cropping) applied to the Gaussian point cloud during fine-tuning, which substantially improves robustness to real-world point-cloud degradations. The method is evaluated on three standard 3DGS datasets, compared against adapted image-watermarking and attribute-concatenation baselines, and shown to transfer to 2DGS and a compressed 3DGS variant. This is the first dedicated watermarking method for 3DGS.

## Strengths

- **3D distortion layers yield large, well-documented gains**: Table 3 shows extraction accuracy under Gaussian noise improves from 74.38% to 95.14% (a 20.76 percentage point gain) when 3D distortion layers are used during fine-tuning. This directly supports the paper's central robustness claim and is verified by comparing "w/o DL" and full-method rows.

- **Clean, principled approach that works where naïve baselines fail**: The idea of treating the 3DGS rendering pipeline as a watermark encoder by optimizing its parameters for a fixed decoder is sound. Table 1 shows WATER-GS achieves BER < 3% across three datasets, while HiDDeN+3DGS and MBRS+3DGS both yield BER ≈ 50% (random guessing), confirming that 2D image watermarking patterns are destroyed during 3DGS training — validating the need for the proposed approach.

- **Demonstrated generality across 3DGS variants**: Table 5 shows successful transfer to 2D Gaussian Splatting (2DGS) and a compressed 3DGS variant (Compact3D, 90.15% extraction accuracy), supporting the claim that the decoder is pluggable into different 3DGS pipelines without architectural modification.

- **Systematic ablation of embedding positions**: Table 4 investigates fine-tuning only position parameters, only SH coefficients ($h_{dc}$ or $h_{rest}$), or all parameters, showing that only full fine-tuning achieves both low BER (2.3%) and high PSNR (32.0 dB). This provides practical guidance for practitioners.

- **Qualitative validation of the problem**: Figure 5 shows residual images pre- and post-rendering, visually demonstrating that watermarks from HiDDeN/MBRS are disrupted by the 3DGS rendering process.

## Weaknesses

### Fatal

None.

### Major

- **Missing numerical specifications for 3D distortion layers**. The paper defines Gaussian noise (width σ), dropout (fraction p), and crop (fraction p) but never states the actual values of σ or p used in experiments. Without these, results cannot be reproduced. These are not complex details — a simple table would suffice — and their absence is the single largest barrier to reproducibility in the paper.

- **No ablation of the trade-off parameter γ**. The total loss is $\mathcal{L}_{tot} = \mathcal{L}_{rgb} + \gamma \cdot \mathcal{L}_m$, where γ balances rendering quality against message accuracy. No sensitivity analysis is provided. Since this parameter directly controls the core robustness–imperceptibility trade-off the paper claims to optimize, omitting its exploration is a significant gap.

- **No statistical reporting (standard deviations or error bars)**. The paper reports only point estimates (averages across viewpoints and scenes) for BER, PSNR, MS-SSIM, and LPIPS, with no variance measures. Given stochastic training and variation across scenes (e.g., "Doerner" vs. "Garden" in Table 1 show large differences), the significance of reported improvements cannot be assessed. Multiple runs or per-scene standard deviations are needed.

### Minor

- **Robustness evaluation, while useful, is narrow relative to the claims made.** The paper tests only three distortion types (Gaussian noise, dropout, crop). Real-world 3D file distortions also include quantization, coordinate scaling, bit truncation, and non-uniform downsampling. More importantly, the paper does not test against any adversarial attempts to remove the watermark (e.g., fine-tuning on clean renderings, adding small learned perturbations to parameters). The claims should be scoped to "robustness against the three tested distortion types" unless the evaluation is expanded.

- **The "up to a 20% improvement in accuracy rate" in the abstract** refers specifically to the Gaussian-noise case in the ablation (74.38% → 95.14%), which is correct but the abstract presents it as a generic headline without qualifying the distortion type. A small clarification would prevent misinterpretation.

- **No explicit Limitations section.** Given that this is the first method in its sub-area, a limitations paragraph discussing scope (e.g., requiring per-scene fine-tuning, narrow distortion testing, potential attack vectors) would strengthen the paper and is expected at this venue's standard.

### Trivial

- In Section 3, the description of the Gaussian Noise layer says "applies a Gaussian kernel with width σ to blur $\tilde{\Theta}$" — this appears to describe adding noise to parameter values, not blurring with a kernel. The phrasing is slightly ambiguous.

## Nice-to-Haves

- A controlled comparison with CopyRNeRF at the same message length (e.g., 16-bit for both) would be cleaner, though the current comparison (WATER-GS at 48 bits vs. CopyRNeRF at 16 bits) already favors the proposed method since longer messages are harder to embed. This is a methodological purity point, not a weakness.
- Visual examples of watermarked images side-by-side with unwatermarked originals (beyond residual images multiplied by 10) would help the reader assess imperceptibility directly.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Comparison with CopyRNeRF is unfair due to different message lengths"** — The critic claims 16-bit (CopyRNeRF) vs. 48-bit (WATER-GS) is unfair because shorter messages are easier. However, since WATER-GS uses *longer* messages (harder task) and *still* achieves better BER, the comparison actually **favors** the proposed method. This is not a weakness; it is additional evidence of WATER-GS's effectiveness. Removed as factually incorrect as a criticism.

2. **"Plug-and-play characterization is misleading"** — The critic claims fine-tuning for 10k–30k iterations is not plug-and-play. However, the paper clearly applies "plug-and-play" to the *decoder* (Section 3.1: "This decoder features a plug-and-play capability, enabling seamless incorporation into the existing 3DGS framework"), not to the entire fine-tuning process. The decoder is pre-trained and fixed; it plugs into any 3DGS pipeline. This is a reasonable and standard use of the term. Removed as a misunderstanding.

3. **"Baselines (HiDDeN+3DGS, MBRS+3DGS) are strawman / guaranteed to fail"** — The paper presents these baselines precisely to demonstrate *why* existing 2D image watermarking approaches fail when applied to 3DGS, which is a standard and informative experimental practice. They are not presented as competitive baselines but as evidence that the problem requires a new approach. The paper is explicit about this (Section 4.3: both "completely fail"). Removed.

4. **"Section 2.1 and Section 2.2 structure notes"** — Generic section-by-section commentary about what "should" be included. Most points are either already addressed in the paper or are subjective preferences. Removed.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths and differ mainly on whether to characterize certain standard experimental choices as weaknesses.

## Suggestions

1. Add a table specifying the exact numerical values for σ (Gaussian noise width) and p (dropout/crop fraction) used in the 3D distortion layers.
2. Add a small ablation plot or table showing BER and PSNR as γ is varied, so readers can assess the trade-off sensitivity.
3. Report per-scene or per-viewpoint standard deviations (or at minimum per-scene results alongside averages) for the main tables.
4. Broaden the robustness evaluation to at least one additional distortion (e.g., quantization of Gaussian parameters to 8-bit) and explicitly scope robustness claims to the tested distortions, or expand testing to include a simple adversarial perturbation.
5. Add a brief Limitations paragraph to the conclusion discussing the scope of robustness, the per-scene fine-tuning requirement, and potential attack vectors.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>