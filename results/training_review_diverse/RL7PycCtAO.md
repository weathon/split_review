I have thoroughly verified the paper content against each reviewer claim. Here is my consolidated review.

---

## Summary

This paper presents DiffPC, a two-stage image compression framework built on Stable Diffusion. Its contributions are: (1) a multi-feature compressor with importance-weighted MSE that allocates more bits to textured regions, (2) an IC-ControlNet with Time-Aware Decoupling (TAD) to prevent condition leakage, and (3) a semantic pre-embedding module (Q-Former) that fuses visual and textual semantics without costly iterative embedding. The paper claims state-of-the-art perceptual fidelity across DIV2K, CLIC2020, Kodak, and COCO30K.

## Strengths

1. **Well-motivated architecture design.** The two-stage training pipeline (Stage I: low-level compressor + IC-ControlNet; Stage II: semantic pre-embedding) is logical and avoids retraining the full diffusion model. The paper provides ablation evidence that each component (importance-weighted MSE, TAD, IC-ControlNet, pre-embedding, multi-feature fusion, text semantics) contributes positively — the ablations show degradation when any is removed.

2. **Multi-feature compressor with importance-weighted MSE (Eq. 6, Theorem 3.1).** The compressor fuses multi-scale features from the SD encoder and uses a variance-weighted loss that, as argued, allocates more bits to high-frequency regions (textures, edges). The theoretical motivation via KL divergence (Theorem 3.1) provides a formal grounding, even if the derivation makes simplifying assumptions.

3. **IC-ControlNet with Time-Aware Decoupling.** The paper identifies a genuine problem — condition leakage in compression-conditioned diffusion models — and proposes TAD to reformulate noise prediction as a residual task (Eq. 8). Ablation confirms that removing TAD or replacing IC-ControlNet with vanilla ControlNet degrades results.

4. **Comprehensive evaluation protocol.** The paper validates on four standard benchmarks (CLIC2020, DIV2K, Kodak, COCO30K) using both reference-based (LPIPS, DISTS) and no-reference (FID, KID, CLIP-IQA) metrics, comparing against a reasonable set of baselines (HiFiC, MS-ILLM, ELIC, CDC, DiffEIC, TACO, VQGAN, BPG).

5. **Practical insight on color correction.** The observation that the degraded representation retains accurate color information, enabling simple moment-matching color correction, is a practical contribution.

## Weaknesses

### Fatal

None.

### Major

1. **No numerical results in tables or text.** The paper claims state-of-the-art perceptual fidelity across multiple benchmarks and metrics, yet the entire body of text contains zero quantitative results — no FID, LPIPS, MS-SSIM, KID, or CLIP-IQA values at any bitrate. All results are deferred to figures (Figure 5, Figure 6, Figure 8), which are absent from the extracted text. For a paper making strong SOTA claims, this is insufficient. Even in the original submission, relying solely on figures without any summary table of key operating points forces readers to visually interpolate rate-distortion curves rather than inspect precise numbers. This undermines the verifiability of the core contribution. The paper should include at least one numerical results table in the main body.

2. **LSDIR training dataset is neither defined nor cited.** The paper states that baselines were retrained "on the LSDIR dataset" (line 159) and that LSDIR is 14× smaller than ImageNet, but LSDIR is never defined, described, or attributed to a citation. Even if it originates from Li et al. (2024b), this connection is not made explicit. Without knowing the dataset size, domain, and composition, the reader cannot assess whether the training data is appropriate or whether the baseline retraining is fair. This is a basic scholarly omission.

3. **VQGAN baseline comparison is acknowledged as unfair but not addressed.** The paper notes that VQGAN was trained on ImageNet (14× larger than LSDIR) while other baselines (presumably including DiffPC itself) were trained on LSDIR. This asymmetry favors DiffPC — if baselines underperform, it could be due to training on a smaller, less diverse dataset rather than method inferiority. The paper acknowledges the issue but neither explains why the comparison remains valid nor provides an additional comparison where VQGAN is retrained on LSDIR. This weakens the claimed advantage over VQGAN-based methods.

### Minor

1. **Missing training and inference details.** The paper omits standard reproducibility-critical information: batch size, learning rate, optimizer, number of training steps, hardware configuration, sampling steps T used at inference, and the specific image captioning model. These details can be added in a supplementary section.

2. **Theoretical derivation of importance-weighted MSE relies on a simplifying assumption that is partially contradicted by the paper's own framing.** The derivation (lines 100–103) assumes both p(z₀|x) and p_γ(ĉ|z₀) have equal isotropic variance Σ = σ²_{z₀}I. However, the paper later states that the VAE encoder "model[s] per-pixel variance" (suggesting spatial/channel-wise variation), and that "significant high-frequency regions ... are modeled with lower variances" — which directly implies non-isotropic, non-uniform variance. The variance is then collapsed into a single trainable scalar w. The relationship between the per-pixel variances and w is not explained. This leaves the theoretical grounding of the loss somewhat ambiguous. The ablation shows the loss helps, but the justification could be tightened.

3. **Color correction description is ambiguous.** The paper mentions two approaches: (a) normalizing the decoded image's mean/variance to match the degraded representation, and (b) a learnable decoder. It is unclear which was actually used for the reported results and whether the color correction step inflates certain perceptual metrics (e.g., CLIP-IQA). Disentangling these effects would strengthen the evaluation.

4. **COCO30K results are referenced but no data is shown.** The paper says it validates statistical fidelity on COCO30K but provides no results (neither text, table, nor figure) for this dataset.

### Trivial

None.

## Nice-to-Haves

- Report computational cost (training time, inference latency, model parameters). This is important for a compression method.
- Provide confidence intervals or multiple-run statistics for stochastic metrics (FID, KID).
- Report numerical values for at least a few representative bitrate operating points alongside figures, so readers can compare precisely.
- Specify the image captioning model and its prompt template.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing proof" — Proof.1 referenced but not shown:** The hard rules note that the parser strips appendix content; proofs in the appendix exist in the original submission. Removed.
- **"Q-Former source/training objective not specified":** The paper says "pre-trained Q-Former" — leveraging pre-trained components is standard and does not require a full re-description. Removed.
- **"Underspecified which cross-attention layers are unfrozen":** The paper states "unfreeze all cross-attention layers integrating semantic fusion within the denoising diffusion network" — this is sufficiently clear. Removed.
- **"Missing confidence intervals":** Not standard practice in this line of work for large-scale benchmarks. Moved to Nice-to-Haves.
- **"Figure 5/6 absence is a parser artifact, not a paper flaw":** The missing figures are indeed a parser issue; the criticism about the paper's reliance on figures vs. tables is kept in Major because it concerns the paper's presentation choices, not the parser. However, the specific complaint that "the extracted text provides no data" confuses parser failure with a paper flaw. The genuine issue is that the paper has no numerical tables at all — a design choice, not a parser error. The criticism is kept but framed as a presentation choice.
- **"Strawman about f1/f2 extraction not being explicit":** The paper says "intermediate features f1 and f2 are extracted" from the encoder, which is sufficient for readers familiar with the SD VAE architecture. Removed.
- **"Elaboration on IC-ControlNet architecture":** The paper provides a description and refers to Figure 3(b). While more detail would help, this is within the scope of normal novelty disclosure for a conference paper. Moved to Nice-to-Haves.
- **Strength Finder's claim about "state-of-the-art statistical fidelity on multiple benchmarks":** This is based on figures we cannot fully verify from the text. Kept as a claimed strength since the paper asserts it, but caveated.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any novel perspective that the paper itself does not already articulate.

## Suggestions

1. Add at least one numerical results table to the main text reporting FID, LPIPS, and MS-SSIM at representative bitrates across all validation sets, so the claimed SOTA can be verified without relying solely on figures.
2. Explicitly define and cite the LSDIR dataset, including its size, composition, and relationship to any prior work.
3. Either retrain VQGAN on LSDIR or explicitly restrict the claimed advantage to comparisons where all methods share the same training data, and caveat the VQGAN comparison.
4. Provide a reproducibility appendix with optimizer, batch size, learning rate schedule, sampling steps T, hardware, and the specific image captioning model.
5. Clarify which color correction procedure was used for the reported results and whether its effect is isolated from the main method.
6. Include COCO30K results in the main results section (or table).
7. Tighten the theoretical justification of the importance-weighted loss by explicitly connecting the per-pixel VAE variances to the scalar weight w, or characterize the gap introduced by the equal-variance assumption.

## Score and Decision

**Originality:** Good — the multi-feature compressor design, IC-ControlNet with TAD, and the two-stage training with Q-Former pre-embedding represent a reasonable combination of novel components within the diffusion-based compression space.

**Importance:** Important — low-bitrate image compression with high perceptual quality is a practically relevant problem, and leveraging pre-trained LDMs without expensive retraining is a worthwhile direction.

**Claims support:** Weak — the paper's central claim of SOTA perceptual fidelity is unverifiable from the text because no numerical results are reported. The supporting evidence exists only in figures that are not backed by tables or numeric values in the body.

**Soundness:** Moderate — the methodology is logically structured and the ablations show the intended behaviors, but the missing training details, undefined dataset, and acknowledged unfair baseline comparison raise concerns about how watertight the experimental setup is.

**Clarity:** Adequate — the method description is mostly clear, but the reliance on figures for all results and the ambiguity around color correction reduce clarity.

**Value to community:** Potentially useful, provided the experimental evidence can be verified. The architecture elements (IC-ControlNet with TAD, importance-weighted MSE for compressors) could have broader applicability.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>