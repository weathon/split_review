---

## Summary

ST-Diff proposes treating multivariate time series generation as a video task. It applies the Short-Time Fourier Transform (STFT) to convert each time series into a spectro-temporal video tensor (real/imaginary STFT coefficients + trend channel over three color channels, with frequency and covariate axes as spatial dimensions and STFT time-frames as the temporal axis). A custom video diffusion transformer with tri-axial factorized attention, anisotropic patching, and data-initialized bias matrices then generates new samples in this domain, with iSTFT converting back to the time domain. Experiments cover six datasets with four metrics for short sequences (L=24) and one dataset for long sequences (L∈{64,128,256}).

---

## Strengths

1. **Novel and well-motivated representation.** The STFT-video framing is a natural middle ground between time-domain and static-image approaches: it explicitly preserves the temporal axis while exposing spectral structure. This is concisely argued in Section 2 and technically detailed in Section 4.1.

2. **Strong short-sequence results where full comparisons exist.** On the Discriminative Score (all six datasets) and Predictive Score (most datasets), ST-Diff outperforms TimeGAN and TimeVAE by large margins, and beats the available DiffusionTS/ImagenTime entries (e.g., fMRI discriminative 0.021 vs. 0.167 from the next-best TimeGAN; Energy discriminative 0.009 vs. 0.040 from ImagenTime). These improvements are numerically substantial, not marginal.

3. **Compelling qualitative validation.** The t-SNE/KDE plots (Figure 3) and ACF/PSD analyses (Figure 4) show that generated samples closely match the real data manifold, temporal autocorrelation, and spectral characteristics. The PSD alignment is a particularly relevant diagnostic for a method that explicitly models spectral evolution.

4. **Clear scalability advantage in Table 2.** On ETTh at lengths {64, 128, 256}, ST-Diff's Discriminative Score remains stable at ~0.03 while TimeGAN degrades to 0.442 at length 256, and DiffusionTS degrades to 0.144. The Context-FID advantage at length 64 (0.031 vs. 0.631 for DiffusionTS) is striking. This provides concrete support for the temporal-axis-preservation argument.

---

## Weaknesses

### Fatal
None.

### Major

**1. No ablation study anywhere in the paper.**
ST-Diff bundles six independent design decisions: (a) STFT-video representation vs. time-domain or static-image, (b) anisotropic vs. isotropic patching, (c) tri-axial factorized attention, (d) data-initialized bias matrices B_C and B_F, (e) trend-residual EMA decomposition, (f) the cross-covariance loss on STFT magnitudes. The paper's central thesis—stated in the abstract—is that "the novel time-series-as-videos representation, together with its tailored architecture, allows ST-Diff to establish a new state-of-the-art." Without any ablation, there is no evidence for which component(s) drive the gains. A well-designed video transformer with the cross-covariance loss alone might replicate most results; or the data-initialized bias matrices might account for a large fraction of the improvement; or the gains could come entirely from the representation change. As written, the causal story the paper tells is unsupported by experimental evidence.

**2. The two strongest baselines are absent from half the reported metrics, making the "21/24" SOTA claim not fully verifiable.**
Table 1 explicitly shows "—" for both DiffusionTS and ImagenTime on Context-FID and Correlational Score across all six datasets, with the note that these were "not reported in the original papers." ST-Diff is therefore compared against only TimeGAN and TimeVAE for 12 of the 24 metric-dataset combinations. The claim in Section 5.1.1 that ST-Diff achieves "superior performance on 21 out of 24 metric-dataset combinations" conflates wins against all four baselines with wins against only two of them. The paper should either re-run DiffusionTS and ImagenTime for these metrics or acknowledge that the "21/24" count is computed against an incomplete comparison set.

**3. The scalability claim rests on a single dataset.**
Section 5.1.2 concludes that ST-Diff "unequivocally demonstrate[s] superior scalability" and "overcomes a key limitation of models that operate purely in the time domain." This is based entirely on Table 2 with ETTh at {64, 128, 256}. A scalability claim of this strength—presented as a defining advantage of the paradigm—requires more than one dataset. ETTh has a specific structure (electricity transformer temperature data with strong periodic components); whether the result generalizes to higher-dimensional (e.g., MuJoCo) or noisier (e.g., fMRI) datasets is unknown.

### Minor

**4. Possible failure case on Stocks/Predictive Score not discussed.**
The Predictive Score for Stocks is ambiguous due to table layout, but the table row for STDiff appears to contain a value of ~0.186 against DiffusionTS's 0.036. If correct, this is a roughly 5× degradation relative to the strongest baseline on this metric-dataset pair. The paper does not discuss this, and the conclusion that the model "establishes a new state-of-the-art" does not acknowledge potential failure cases. Even if this is a parser artifact that does not reflect the original table, the ambiguity alone warrants clarification. (Note: the paper claims 21/24 wins, implying 3 failures exist; the Stocks Predictive case may be one of them and should be discussed.)

**5. Spectrogram consistency of generated samples is not addressed.**
Section 3 states that "near-perfect reconstruction ensures that samples generated in the time-frequency domain can be losslessly converted back to the time domain." This is accurate for real data, whose STFT satisfies conjugate symmetry and overlap-add consistency constraints. During generation, however, the diffusion model samples arbitrary tensors from Gaussian noise with no guarantee of satisfying these constraints. The iSTFT will still produce an output, but it may introduce artifacts. In audio generation this is a well-known issue. The paper does not discuss whether this is a concern, nor whether the cross-covariance loss mitigates it. This does not invalidate the empirical results (the metrics used may be insensitive to such artifacts), but the claim of "lossless" conversion is overstated for the generative case.

**6. Data-initialized bias matrices as a potential informational asymmetry.**
Section 4.3 states that B_C is initialized from "the empirical cross-correlation matrix of the STFT covariates" and B_F from "the covariance of STFT log-magnitudes." These are dataset-specific statistics embedded as initialization, not as fixed priors. It is not discussed whether baselines receive an analogous informational advantage. If they do not, part of ST-Diff's performance gain may come from this initialization rather than from the architectural choice. This does not invalidate the comparison, but it should be acknowledged and ideally ablated alongside the representation study.

### Trivial

**7. Computational cost is acknowledged in the Conclusion ("higher computational and memory costs") but no concrete numbers (parameter count, wall-clock time, GPU memory) are given.** Without these, it is impossible to assess whether the performance gains partly reflect a larger model capacity relative to baselines.

---

## Nice-to-Haves

- A 2×2 ablation design would substantially strengthen the paper: (a) STDiff architecture on a static-image STFT representation (matching ImagenTime's setting), and (b) a standard video transformer without custom biases on the video representation. This 2×2 would isolate the representation contribution from the architecture contribution, directly substantiating the paper's central claim.
- Extending the scalability experiments (Table 2) to at least two additional datasets (e.g., MuJoCo for high dimensionality, fMRI for high noise) would transform a suggestive finding into a genuine demonstration.
- A standalone ablation of the cross-covariance loss is warranted: it directly encodes training-set statistics into the objective, and its contribution relative to the standard DDPM loss is uncharacterized.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Table formatting is ambiguous and inconsistent with standard practice" (Harsh Critic, Point 3 framing):** The rendering of Table 1 in the extracted text is a PDF parsing artifact—rows from different methods appear to be merged into single cells. The instruction to remove typographic/formatting artifacts applies here. The underlying substantive concern (a possible failure case on Stocks/Predictive) is retained as Minor weakness #4 on its merits, not as a formatting criticism.

- **Trend-channel mismatch across frequency dimension (Harsh Critic, Section 4.1 note):** The critic notes that broadcasting the trend across the frequency axis creates a mismatch because trend is not a spectral quantity. While technically accurate, this is not a flaw: the model must learn that the trend channel is frequency-invariant, and the paper explicitly designs C=3 channels for this purpose. The architecture has expressivity to handle this. This is a design choice that is stated but not fully justified, which is common in empirical papers. Not a substantive weakness.

- **Strength: "The method scales robustly to longer sequences" (Strength Finder):** Retained in Strengths above with appropriate caveat (single dataset).

- **Strength: "21 out of 24 metric-dataset combinations" (Strength Finder):** Partially retained but weakened by Major weakness #2 (partial comparisons inflating the count).

---

## Novel Insights

The STFT-video representation is the paper's genuinely original contribution: casting each STFT time-frame as a video frame (with frequency and covariate as spatial dimensions) is a natural but underexplored bridge between classical signal processing and spatiotemporal deep learning. The tri-axial factorization of attention along temporal, frequency, and covariate axes with axis-specific inductive biases (RoPE for time and frequency; learnable embeddings for the unordered covariate axis; data-initialized bias matrices for inter-covariate and inter-spectral dependencies) is a principled architectural design that reflects genuine domain knowledge about time series structure. The scalability result—Discriminative Score stable at ~0.03 across sequence lengths 64→256 while baselines degrade sharply—is the strongest empirical evidence for the paradigm's advantage, though it awaits validation on more than one dataset.

---

## Suggestions

1. **Re-run DiffusionTS and ImagenTime for Context-FID and Correlational Score** using the authors' evaluation code (or reproduce their published setups). This is necessary to make the SOTA claim verifiable.
2. **Add a targeted ablation:** at minimum, compare (a) full ST-Diff vs. (b) ST-Diff without the data-initialized bias matrices vs. (c) a standard video DiT on the STFT-video representation. This would characterize whether the gains come from the representation or the architectural customization.
3. **Qualify the "unequivocally superior scalability" claim** or extend Table 2 to 2-3 additional datasets with different structural properties.
4. **Add a brief analysis of spectrogram consistency** in generated samples—report, for instance, the mean overlap-add reconstruction error for generated samples, or discuss why this is not expected to be problematic for the metrics used.
5. **Report training time and parameter counts** relative to at least one competitive baseline (DiffusionTS), given the acknowledged higher computational cost.

---

## Score and Decision

**Originality:** The video-as-time-series paradigm via STFT is novel and well-motivated; the architectural inductive biases are thoughtfully designed. Score: 4/5.

**Importance of research question:** Unconditional multivariate time series generation is practically significant for simulation, imputation, and privacy-preserving data synthesis. Score: 4/5.

**Claims well-supported:** The "new state-of-the-art" and "unequivocal scalability" claims substantially outrun the evidence: two major baselines are absent from half the metrics, there is no ablation, and scalability is evaluated on one dataset. Score: 2/5.

**Soundness of experiments:** The evaluation protocol and datasets are standard and well-chosen; the experimental design itself (short + long, discriminative + predictive + correlational + FID) is thorough. The main gap is the missing ablation and missing baseline entries. Score: 3/5.

**Clarity of writing:** The method description is clear and the paper is well-organized; figures are informative; the conclusion is candid about computational limitations. Score: 4/5.

**Value to the research community:** The representation idea and tri-axial attention design are directly useful and will likely inspire follow-up work regardless of whether the current evidence is complete. Score: 3/5.

The paper presents a genuinely novel and technically sound idea with strong empirical results on the metrics where complete comparisons exist. However, for a top venue, the absence of any ablation study and the incompleteness of the main comparison table are significant gaps that prevent the paper from fully establishing its central claims. The idea deserves publication, but requires a revision that at minimum provides re-run baselines on all four metrics and a basic representation-vs.-architecture ablation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>