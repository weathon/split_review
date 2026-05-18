I have thoroughly read and analyzed the paper and all reviewer comments. Let me now construct the consolidated final review.

---

## Summary

SuperMark proposes a training-free image watermarking framework that embeds watermarks into initial Gaussian noise and uses a frozen pretrained diffusion-based super-resolution (SR) model to generate watermarked images. For extraction, it applies DDIM Inversion to recover the watermarked noise and extract the watermark. The key insight is an architectural symmetry between watermark embedding/extraction and diffusion denoising/noising processes. The method achieves strong empirical results: 99.46% bit accuracy under normal distortions and 89.29% under adaptive attacks on MSCOCO, with competitive fidelity (PSNR 32.49, SSIM 0.93).

## Strengths

- **Training-free framework with strong empirical robustness**: SuperMark requires no training or fine-tuning of any model component — it leverages a frozen pretrained SR model and existing noise-injection techniques. This is a genuine architectural advantage over methods that require expensive end-to-end training. The empirical results are striking: 99.46% average bit accuracy under normal distortions and 89.29% under adaptive attacks (Table 1), substantially outperforming nearly all nine baselines compared.

- **Novel conceptual contribution aligning watermarking with diffusion processes**: The paper identifies and operationalizes a symmetry between watermark embedding/extraction and denoising/noising in diffusion models. This insight is well-articulated in Section 3.1 and is central to the framework's design. It differentiates the work from prior post-processing watermarking approaches and opens a clear direction for future work.

- **Flexible and modular framework**: SuperMark supports multiple watermark injection methods (Gaussian Shading, Tree-Ring) and multiple SR models (SD-Upscaler, LDM-SR), with transferability validated across five datasets (MSCOCO, DiffusionDB, WikiArt, CLIC, MetFACE) in Section 4.3. This modularity is a genuine strength — the framework can improve as better SR models and injection techniques become available, as discussed in Section 3.5.

- **Competitive fidelity alongside robustness**: Despite its focus on robustness, SuperMark maintains PSNR of 32.49 and SSIM of 0.93 on MSCOCO (Table 1), comparable to baselines. This simultaneous achievement of high robustness and reasonable fidelity is non-trivial and well-demonstrated.

## Weaknesses

### Fatal
None identified. The empirical results are strong and the core claims are supported; no errors that invalidate the paper's conclusions.

### Major
- **Unexamined conditioning mismatch during DDIM Inversion extraction (Section 3.4)**: The extraction pipeline uses a downscaled version of the *distorted* watermarked image (I_wm'^↓) as the conditioning signal for DDIM Inversion. Under attack, this conditioning image differs from the original low-resolution image I_low used during embedding. The paper does not analyze whether or how this mismatch affects inversion accuracy. The cited works for DDIM Inversion robustness (Wen et al., 2024; Yang et al., 2024) operate under the assumption that the noising and denoising paths use the *same* conditioning image — which is not the case here unless the watermark embedding itself guarantees low-resolution content preservation. While the strong empirical results (99.46% accuracy) suggest the method is robust to this mismatch in practice, the paper's central explanatory claim — that robustness stems from the inherent properties of DDIM Inversion — is incomplete without analyzing this mechanism. This is a gap in scientific explanation, not in correctness of the results.

### Minor
- **Overstated framing of the robustness–fidelity "inherent unification"**: The paper claims SuperMark can "inherently achieve robustness and fidelity in a unified manner" (Section 1), but Section 3.3 explicitly acknowledges that the downscale factor S_low and strength factor f_s introduce a trade-off between robustness and fidelity ("This leads to a trade-off between the robustness and fidelity"). The trade-off has been relocated and made more controllable, but it has not been eliminated. The "inherent" language is overstated relative to what the architecture actually provides. (Note: the reference to "Sec. 4.4" for further exploration of this trade-off is not present in the extracted text — this may be a parser artifact, but the claim in the introduction/narrative remains somewhat stronger than the paper's own caveats support.)

- **Distortion parameters not specified in the main text**: Section 4.1 lists distortion types (JPEG compression, random cropping, Gaussian blur, Gaussian noise, brightness adjustments) and adaptive attacks, but does not specify key parameters such as JPEG quality factor, rotation angle range, noise standard deviation, or crop ratio. These details are essential for interpreting the reported bit accuracy numbers and for reproducibility. If this information exists only in the tables (which appear as image references due to parser stripping), it should be stated explicitly in the text.

- **Design choice of not storing the original low-resolution image I_low during extraction**: The paper does not discuss why the extraction uses a downscaled version of the *distorted* image (I_wm'^↓) as the conditioning signal rather than storing and reusing the original I_low computed during embedding. Using the stored I_low would eliminate the conditioning mismatch entirely. The paper should justify this design choice or acknowledge it as a limitation.

### Trivial
None.

## Nice-to-Haves
- A wall-clock time comparison or computational cost analysis (the method requires 25 denoising steps + 25 inversion steps per image, which is heavier than most baselines; Section 3.5 discusses future acceleration but does not quantify current overhead).
- Explicit confirmation that distortion parameters match when comparing against ZoDiac results "as presented in their paper" (Table 4) — current practice is standard, but explicit confirmation would strengthen the comparison.
- A controlled experiment isolating the effect of conditioning degradation on inversion accuracy, as suggested by the reviewer, would provide mechanistic validation for the robustness claims.

## Removed Points

These points were identified by the reviewers but are either factually incorrect, violate the rules, or are not valid weaknesses of this paper:

1. **"Section 4.4 does not exist"**: The reviewer complains about a missing Section 4.4 that the paper references. Per guidelines, sections may have been stripped by the parser; this criticism cannot be validated from the extracted text and is removed.
2. **Criticism about the ZoDiac comparison using results "as presented in their paper"**: This is standard practice across the field and not a valid weakness. The paper explicitly states the source. Removed as a strawman.
3. **Generic "should also cover Y" criticism**: The reviewer's question about why not store I_low is kept as Minor above; any broader "this paper should also cover domain Z" demands are scope creep and removed.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation emerging from the reviews is the conditioning mismatch problem itself. The fact that SuperMark works extremely well *despite* using a distorted conditioning signal for DDIM Inversion is actually more impressive and theoretically interesting than the paper acknowledges. If the SR model's DDIM Inversion is robust to conditioning-signal corruption (not just image corruption), that is a stronger property than what previous works on DDIM Inversion robustness have demonstrated. The paper could reframe this as a positive finding rather than an oversight: the conditioning mismatch robustness may itself be a novel contribution worth analyzing.

## Suggestions
1. Add a dedicated analysis (experiment or ablation) of how the conditioning mismatch during extraction affects inversion accuracy. A simple controlled experiment corrupting the low-resolution conditioning image separately from the high-resolution image would isolate this effect.
2. Tone down the "inherently unifies robustness and fidelity" language, or explicitly qualify it by distinguishing between the *architectural* trade-off of encoder–noise layer–decoder methods versus the *parametric* trade-off of S_low and f_s.
3. Provide distortion parameters (JPEG quality, rotation angle, noise std, crop ratio) explicitly in the experimental setup section for reproducibility.
4. Discuss the design choice of using I_wm'^↓ rather than stored I_low as the conditioning signal during extraction, or acknowledge it as a limitation.

## Score and Decision

This paper makes a genuine contribution: a training-free watermarking framework that achieves state-of-the-art robustness while maintaining competitive fidelity. The core idea is novel, well-motivated, and supported by strong empirical results. The main weaknesses are in explanatory depth (conditioning mismatch unexamined) and framing (overstated "inherent" claims), not in correctness or significance. The weaknesses are addressable with additional analysis and do not undermine the paper's central empirical contribution. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>