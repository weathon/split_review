Now writing the consolidated review.

## Summary

AnyECG introduces a family of ECG foundation models (254M–1.7B parameters) with a two-stage self-supervised pretraining pipeline. Stage 1 trains a tokenizer with a vector-quantized rhythm codebook and a multi-view synergistic decoder (morphology reconstruction, DWT frequency reconstruction, and demographic attribute prediction). Stage 2 performs masked modeling over the discrete rhythm codes to learn cardiac event semantics. The models are evaluated on four downstream tasks — anomaly detection, arrhythmia detection, corrupted lead generation, and ultra-long ECG recognition — and consistently outperform existing methods.

## Strengths

- **Comprehensive multi-task evaluation spanning four distinct ECG applications.** The paper validates AnyECG on anomaly detection, arrhythmia detection, corrupted lead generation, and ultra-long ECG recognition (Tables 1–4). Prior ECG foundation models (e.g., ECG-FM) cannot be applied to lead generation or ultra-long ECG tasks (stated in Sections 4.3.3–4.3.4), making this breadth of evaluation a demonstrable advance.

- **Cross-Mask Attention (CMA) tailored to multi-lead ECG structure.** CMA (Equations 1–2, Section 3.1) restricts each patch to attend only to patches from the same lead or the same temporal position across leads, with a positional tolerance for conduction delays. This is a principled architectural inductive bias that leverages the complementary nature of ECG leads, going beyond the off-the-shelf Transformers used in prior ECG foundation models.

- **Multi-View Synergistic Decoder with three complementary proxy tasks.** The tokenizer jointly optimizes morphology reconstruction (time-domain), DWT-based frequency reconstruction (time-frequency domain), and demographic attribute prediction (Section 3.3, Equations 5, 7, 8). The frequency decoder via DWT provides a learning signal absent from prior tokenizers that rely solely on time-domain reconstruction, and the demography decoder explicitly targets the demographic shift challenge.

- **Consistent scaling behavior across three model sizes.** On anomaly detection, arrhythmia detection, and ultra-long ECG recognition, AnyECG-B → AnyECG-L → AnyECG-XL show monotonic improvement (e.g., anomaly accuracy: 0.8188 → 0.8241 → 0.8255; arrhythmia accuracy: 0.3339 → 0.3358 → 0.3449). This provides empirical evidence that the pretraining methodology scales productively with model capacity.

- **Rhythm Codebook vector quantization for noise-robust representations.** The learnable codebook with cosine-similarity nearest-neighbor assignment (Section 3.2, Equation 3) converts low-SNR continuous ECG features into high-SNR discrete tokens, directly targeting the low-SNR challenge identified in the introduction.

## Weaknesses

### Fatal
None.

### Major

- **Arrhythmia detection absolute performance is not contextualized, making the reported numbers uninterpretable.** AnyECG-XL achieves 0.3449 accuracy and 0.1635 AUC-PR on arrhythmia detection (Table 2). The paper does not state the number of classes, the class distribution, or what random-chance baselines are. Without this context, the reader cannot determine whether 0.3449 is meaningful or whether the task formulation itself is problematic (e.g., if this is a 4-class balanced problem, random is 0.25 and the result is modest but above chance; if it is an 8+ class problem, random is even lower). The paper frames "handles arrhythmia detection effectively" without explaining whether these absolute numbers are clinically meaningful. While the relative comparisons against baselines are valid, the omission of task specification prevents proper assessment of the results.

### Minor

- **Key hyperparameters of the rhythm codebook are not reported.** The codebook size *K* is never specified in the paper (it appears as an undefined variable in the codebook definition, Equation 3). Likewise, the commitment loss weight *β* (Equation 10) is introduced but never assigned a numerical value. These are critical hyperparameters: too small a codebook collapses distinct patterns into the same code; too large a codebook defeats the purpose of quantization. *β* controls the trade-off between codebook and commitment losses that stabilizes VQ training.

- **The claimed "hierarchical modeling approach" for ultra-long ECG signals is not actually described.** The paper states (line 342): "We proposed a hierarchical modeling approach that adapts to ultra-long ECG data by employing a sliding window method." A sliding window is a standard technique with no inherent novelty. There is no description of how window-level predictions are aggregated, how the hierarchy is structured, or how this differs from existing approaches. A claimed methodological contribution cannot be evaluated when it is not specified.

- **CMA is not ablated against standard full self-attention.** CMA's restriction (same-lead or same-temporal-position attention) is a strong inductive bias. The paper motivates it but does not compare it against standard self-attention in a controlled experiment. Without this, it is unclear whether the constraint helps, hurts, or is neutral — especially for detecting conditions that manifest as relationships across *different* leads and *different* time points.

- **Demography decoder implementation details are absent.** The paper does not specify which demographic attributes are available across the seven pretraining datasets, what proportion of data has these labels, or how missing attributes are handled. If demographic data are sparse or available only for some datasets, the loss term may contribute negligibly or introduce dataset-specific biases.

- **Architectural details for each model variant are not provided.** The paper reports model sizes (254M, 500M, 1.7B parameters) but does not specify the number of Transformer layers, attention heads, or hidden dimensions for AnyECG-B/L/XL. This makes it difficult for readers to understand the scaling and to reproduce the architecture.

- **Corrupted lead generation baselines are outdated.** The only baselines compared are CGAN (2014) and WGAN (2017). No diffusion-based or ECG-specific generative models are included, which is a missed opportunity to benchmark against more contemporary approaches. While the paper acknowledges that diffusion methods could be added in future work, the absence weakens the evaluation.

### Trivial

- **Notation inconsistency for variable *P*.** The paper defines *P* as the number of patches per lead (line 63: "divides each lead into *P* patches"). Later, *P* is redefined as the patch size (line 235: "patch size *P*=300"). These are different quantities and the reuse of the symbol is confusing.

## Nice-to-Haves

- Standard statistical significance tests (beyond reporting standard deviations) could clarify whether the improvements over baselines are significant given overlapping error bars on some metrics.
- Adding more recent generative baselines (e.g., diffusion models) for the lead generation task would strengthen that evaluation.
- Reporting model inference cost (latency, FLOPs) would help practitioners understand the practical trade-offs.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Missing ablation studies (promised Section 4.4 and 4.5):** Removed because the content may have been stripped by the PDF parser. The instruction accounts for stripped content.
- **Comparisons stacked in AnyECG's favor (non-pretrained baselines):** Removed per the hard rule: asymmetry favoring the author's method is not counted as a weakness. Most baselines are the standard SOTA in each task domain and the paper does include one pretrained baseline (ECG-FM).
- **PSNR/SSIM vs. MAE contradiction in lead generation:** Removed as factually incorrect — PSNR, SSIM, and MAE measure different error properties and can disagree without contradiction (e.g., a few large pixel errors hurt MSE/PSNR more than many small errors, while MAE weights all errors equally).
- **Undisclosed dataset as reproducibility concern:** Removed per the rule that cited datasets should not be questioned on existence or availability.
- **Preprocessing pipeline strength:** Removed as generic/standard ECG preprocessing (bandpass, notch, resampling, wavelet denoising) rather than a novel contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify the arrhythmia detection task specification: number of classes, class distribution, and random baseline for each metric. If the dataset is highly imbalanced, report per-class metrics or state why the combined datasets produce this distribution.
2. Report all missing hyperparameters (codebook size *K*, commitment loss weight *β*) and architectural details (layers, heads, hidden dimensions per model variant).
3. Provide a proper description of the "hierarchical modeling approach" for ultra-long ECG, including how sliding window predictions are aggregated.
4. Add an ablation comparing CMA against standard full self-attention, and ideally a two-stage pretraining ablation (with and without Stage 1 tokenizer pretraining).

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>