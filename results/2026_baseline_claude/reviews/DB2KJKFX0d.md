## Summary

This paper proposes BDSB (Brain Disk Schrödinger Bridge), a framework that enhances 3T BOLD fMRI data to approximate 7T quality for visual retinotopic decoding. The key innovation is a two-stage pipeline: (1) conformally mapping brain surface meshes from different subjects/datasets onto a shared 2D parametric "brain disk" domain, and (2) applying an unpaired Schrödinger Bridge diffusion model to translate the 3T signal distribution toward 7T quality. Performance is validated across three experimental designs—synthetic downsampled data, a cross-dataset real setting (3T NOD → 7T NSD), and a small paired 3T/7T TDM experiment—using both image similarity metrics and downstream population receptive field (pRF) decoding accuracy.

---

## Strengths

- **Genuine novelty in the combination**: This is, to the reviewers' knowledge, the first application of Schrödinger Bridge diffusion models to fMRI signal enhancement, and the conformal parameterization strategy to create a shared 2D "brain disk" domain across subjects and datasets is a creative and principled approach to the domain alignment problem. Prior work addresses either domain separately.

- **Practically motivated and well-framed problem**: The scarcity of 7T scanners is a real bottleneck for neuroscience and BCI research. The paper identifies and addresses a concrete gap: learning unpaired cross-domain enhancement without requiring the same subject to be scanned at both field strengths. The framing as an unpaired image translation task enables using powerful generative frameworks that would otherwise be inaccessible.

- **Comprehensive baseline comparison**: Five 2D translation baselines (Cycle-GAN, OTT-GAN, OTE-GAN, SCR-Net, fast-DDPM) are adapted to the pipeline, and the proposed method outperforms all of them in most metrics across the synthetic and cross-dataset experiments. The inclusion of both pixel-level (SSIM, PSNR) and distributional (FID) metrics, plus a downstream functional metric (pRF R²), strengthens the evaluation.

- **Ablation study provides useful insights**: Table 3 systematically isolates the contributions of the conformal mapping step and each regularization term. The dramatic failure of direct cortical slicing (FID 226.8 → 34.23 with conformal mapping) is compelling evidence that the domain alignment is critical, not just the generative model.

- **Acknowledgment and honest discussion of limitations**: Section 4 explicitly discusses the lack of paired data, the synthetic data gap, and the limited scope of TDM, and frames these as community-level challenges. This intellectual honesty is commendable.

---

## Weaknesses

### Fatal
None.

### Major

1. **The strongest ground-truth evaluation (TDM) is underpowered and inconsistent with the paper's main claims.** TDM uses only 2 subjects, each with a single session (3 runs train, 3 runs test). On this dataset, the proposed BDSB does not achieve the best SSIM: OTT-GAN achieves 0.727 vs. BDSB's 0.718. Because TDM is the only setting where the *same subject* is scanned at both field strengths under actual (not simulated) conditions, this is the most scientifically valid paired comparison — and the paper's method is not clearly superior here. The abstract's claim of achieving "comparable to 7T quality" cannot be robustly supported from two subjects evaluated on a non-standard stimuli protocol. Critically, no pRF R² is reported for TDM (due to "simplified stimuli"), removing the most meaningful downstream metric from the one dataset with real ground truth.

2. **No statistical significance testing throughout.** All quantitative comparisons in Tables 2 and 3 report single point estimates with no confidence intervals, p-values, or bootstrap tests. Given sample sizes of 2 subjects (TDM) and 2 test subjects (synthetic), the numerical differences between methods could easily be within noise. For example, the difference between BDSB (SSIM=0.855, synthetic) and OTT-GAN (SSIM=0.803) may be meaningful, but this is not validated.

3. **Cross-dataset confounds make the R² improvement hard to interpret.** In the cross-dataset real experiment, LQ sources are 3T NOD subjects and HQ targets are 7T NSD subjects—different individuals, different scanners, different stimulus sets, and different experimental protocols. The model is not learning to "enhance neural signal" per se, but rather to shift the NOD distribution toward the NSD distribution. The improved pRF R² in the enhanced NOD data (25.91 vs. 20.26 raw) may reflect the model learning NSD-specific characteristics (e.g., smoother, more stereotyped BOLD patterns from a heavily curated high-resolution dataset) rather than genuine signal enhancement. Without access to actual 7T NOD scans, this interpretation cannot be ruled out.

### Minor

1. **The FID deterioration with regularization is unexplained.** In Table 3, adding PatchNCE and BD-SSIM regularization increases FID from 34.23 to 42.88 (worse distributional match), despite improving PSNR and R². This tension — regularization helps functional interpretability but hurts distributional similarity — deserves substantive discussion, as it suggests the two objectives may be in partial conflict.

2. **No analysis of hallucinated vs. recovered signals.** A qualitative concern with any generative enhancement model is that improved similarity/R² metrics may partially reflect hallucinated signal that happens to be predictable, rather than genuinely recovered neural activity. A decodability analysis (e.g., comparing the spatial layout of pRF maps at specific visual areas like V1/V2/V3 between enhanced and raw 7T) would partially address this for the synthetic setting.

3. **BD-SSIM structural regularization may reduce individual variability.** The BD-SSIM loss penalizes deviations from the fsaverage structural template, which by design biases outputs toward the population average. For applications that depend on individual cortical organization (as pRF mapping typically does), this could suppress genuine inter-subject differences. No analysis of inter-subject variability before/after enhancement is provided.

### Trivial

- Several figure captions appear duplicated consecutively in the text (Figures 2, 3, 4, 5, 6, 7) — likely a parser artifact.

---

## Nice-to-Haves

- A per-visual-area (V1, V2, V3, hV4) breakdown of R² improvement would be more informative than the global ROI average, since different visual areas have different SNR properties at 3T vs. 7T.
- Including the NSD 7T raw baseline in the pRF R² tables (as an oracle upper bound) would clarify how much of the gap BDSB actually closes.
- Evaluating the pRF eccentricity and polar angle maps (not just R²) for spatial coherence would more directly validate whether the enhancement yields neurobiologically plausible retinotopic structure.

---

## Novel Insights

The most genuinely novel conceptual contribution is the combination of conformal brain surface parameterization with unpaired domain translation. The "brain disk" representation is a mathematically sound way to convert a non-Euclidean signal domain (the cortical surface) into a 2D image that standard convolutional architectures can process, while preserving spatial structure through angle-preserving conformal maps. The demonstration that this representation outperforms direct cortical slicing by a very large margin (FID: 226.8 → 34.23) suggests the conformal structure is not merely convenient but functionally important for the translation task. More broadly, the paper suggests that the key bottleneck for 3T→7T fMRI enhancement is not the generative architecture per se, but the domain alignment strategy — a useful insight for the neuroimaging community.

---

## Suggestions

- Collect statistical error bars (e.g., subject-level standard deviations or leave-one-out resampling) for all metrics in Table 2, especially given the small test set sizes.
- For the synthetic experiment, show a side-by-side comparison of retinotopic angle and eccentricity maps (V1/V2/V3 overlaid) between LQ, enhanced, and 7T GT to demonstrate that pRF improvement reflects spatial map quality, not just R² inflation.
- Explore whether applying the model at inference time on multiple bootstrapped runs and averaging improves stability and reduces hallucination risk.
- In the cross-dataset real setting, consider a "sanity check" using the NOD 3T data of a subject for whom a higher-quality scan exists (e.g., more sessions) as an internal pseudo-ground-truth to partially validate the enhancement independently of the 7T label.

---

## Score and Decision

The paper tackles a genuine and important problem with a technically sound and novel combination of conformal brain surface parameterization and Schrödinger Bridge diffusion models. The approach is well-motivated and the experimental design covers multiple settings. However, the real paired evaluation (TDM) is extremely limited (2 subjects, non-standard stimuli) and shows only marginal advantage over a strong baseline, the cross-dataset experiment has inherent confounds that limit interpretability, and no statistical testing is provided. The central claim of achieving "7T quality" from 3T data is not adequately supported by the available evidence, particularly in the only matched-subject evaluation. These are significant concerns for a method paper making strong empirical claims, though the underlying technical contribution is real.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>