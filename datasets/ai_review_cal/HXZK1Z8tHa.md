- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6
## Summary

ShareFormer proposes sharing attention maps across neighboring Transformer blocks (SPSA — Shared Portion Stripe Attention) to reduce inference latency in image restoration, combined with residual connections on the Value pathway to maintain trainability, and a Combined Shared Attention Unit (CSAU) that merges gating with the shared attention. The paper evaluates on image super-resolution, denoising, and JPEG compression artifact reduction, reporting competitive PSNR/SSIM with substantially lower latency than prior Transformer-based methods.

## Strengths

- **Sharing attention maps across layers provides a genuine latency reduction while preserving competitive performance.** The paper reports ShareFormer achieving 1.8 ms latency on lightweight SR versus 5.4–13.6 ms for other Transformer methods (Table 1), and up to 7× speedup on high-resolution denoising (Table 4). On Urban100 ×4 SR, ShareFormer reaches 34.19 dB with 62% of SwinIR's parameters and over 2× faster inference. These cross-method comparisons, while not isolating the sharing mechanism alone, demonstrate that the overall system is efficient.

- **Residual connections on Value improve trainability without adding latency.** Section 4 provides lesion studies (Figs. 4, 5) showing that ShareFormer behaves as an ensemble of shallow Transformers. The ERF visualization (Fig. 7) shows a more concentrated receptive field with residual Value, and the NTK condition number drops from 42.1 to 33.9, indicating improved convergence properties. Figure 6 demonstrates that placing residuals on attention maps does not reduce latency, whereas Value residuals do.

- **CSAU reduces both compute and parameters.** Table 7 shows CSAU improves PSNR from 33.87 to 33.96 while cutting parameters from 1.68M to 1.58M and latency from 4.8 ms to 4.2 ms relative to SPSA+FFN.

- **The sharing mechanism is compatible with multiple attention designs.** Table 9 demonstrates SPSA works with window attention, multi-head depthwise attention, and sparse global stripe attention — all showing speed gains with competitive PSNR. This supports the generality of the approach.

- **Broad experimental validation across three restoration tasks.** The paper reports results on classical and lightweight SR (Tables 2–3), grayscale and color denoising (Tables 4–5), and JPEG CAR (Table 6), showing competitive or SOTA performance across benchmarks.

## Weaknesses

### Fatal
None.

### Major
- **Missing within-architecture ablation of the core claim.** The paper never compares a version of *the same architecture* with sharing turned on vs. off (separate attention maps per block vs. shared). Table 7 compares SPSA+FFN vs. CSAU, Table 8 varies the number of shared layers, and Table 9 tests different attention mechanisms — but none isolates the effect of sharing *itself* from other architectural components (PSA, residual Value, CSAU, ESA). Without this ablation, the reader cannot determine how much performance is sacrificed (if any) for the claimed speedup, or whether other components are doing most of the work. This directly weakens the paper's central thesis. The paper states: "Tab. 8 provides an overview of ShareFormer's performance and latency across different numbers of shared layers" (p. 8) — but the lowest-sharing condition is not a "no sharing" baseline, so the comparison is indirect.

- **The sharing policy for SPSA is not specified precisely enough for replication.** While the general concept (sharing attention maps between adjacent blocks) is conveyed, the paper does not define: (a) how many layers form a sharing group, (b) whether Q/K are computed only at "anchor" layers or at every layer, (c) whether the sharing pattern is regular or variable, and (d) which specific layers reuse which attention maps. The equations in §3.2 (Eq. 5) present the per-block logic but do not specify the grouping strategy over the full network. Table 8 varies "the number of shared attention layers" without defining what this quantity measures. This makes the method difficult to reproduce or adapt.

### Minor
- **The trainability analysis, while creative, remains largely qualitative.** The lesion studies (Figs. 4, 5) claim the MAE loss "increases smoothly" under random deletion/reordering, but no quantitative measure of smoothness (e.g., deviation from linearity, variance across trials) is provided. The ERF visualization (Fig. 7) shows a single example without indicating whether the pattern holds across different layers and inputs. The NTK condition number is reported for one task (lightweight ×2 SR) and one configuration. Training curves (loss vs. iterations) — which would directly support the claim of easier optimization — are not shown.

- **The "Can Transformer be faster than CNN?" comparison is incomplete.** The only CNN baseline compared is RCAN (2018). Modern efficient CNN-based methods such as NAFNet, HINet, or similar architectures that also target the latency-performance trade-off are absent. This weakens the generality of the claim that Transformers can match CNN speed.

- **No perceptual quality metrics.** The evaluation relies exclusively on PSNR and SSIM. Perceptual metrics (LPIPS, DISTS, or user studies) are now standard practice for image restoration and would help assess whether the shared-attention design produces over-smoothed or unnatural outputs.

- **No analysis of attention map similarity across layers.** Sharing is premised on the assumption that adjacent layers' attention maps are sufficiently similar. The paper does not measure cosine similarity, KL divergence, or any other metric between attention maps of neighboring blocks in a full-attention baseline to justify this premise. The conjecture about "homogeneous attention maps in lightweight Transformers" (Sec. 5.1.2) would benefit from direct evidence.

- **The derivation of Eq. 6 ("2(SPSA)=0.5(...)") is not fully explained.** The factor 0.5 and the grouping of terms (4HWC² vs. 2HWC²) presumably arise from sharing between two layers, but the step-by-step reduction from Eq. 3 to Eq. 6 is not shown. Adding a brief derivation would improve clarity.

### Trivial
- Figure axis labels for Figs. 4–6 are difficult to parse from the extracted text; clearer axis descriptions would help.

## Nice-to-Haves
- Training curves (loss vs. iterations) with and without residual Value for at least one task would provide more direct evidence for improved trainability than the NTK condition number alone.
- Reporting variance/confidence intervals over multiple runs would strengthen the reliability of the benchmark numbers, though single-run evaluation is the norm in this subfield.
- A comparison of attention map similarity across layers in a non-sharing baseline would empirically justify why sharing is reasonable.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Claim of 'optimal performance' is overconfident."** — This is a generic phrasing nitpick. The paper shows competitive results across tasks and the claim is clearly scoped as "optimal performance with lower latency and better trainability than other Transformer-based methods."
- **"Eq. 5 suggests model computes Q,K every layer then discards them."** — The extracted equation is garbled by the PDF parser. The original description intends the shared layer to *not* recompute Q/K for the attention map; the paper states "sharing Q, K, and V pairs" and "Attn_l = Attn_{l-1}," which indicates reuse. This criticism stems from parser corruption, not author error.
- **"N/A models are conveniently excluded."** — "N/A" is attributed to models being too heavy for the RTX 3090 GPU (OOM). Excluding models that cannot run under the test hardware is standard, not selective exclusion.
- **"Baseline models were not designed for 1280×720 resolution."** — The paper tests all models under identical resolution and hardware. Running with default window sizes is the standard evaluation protocol; optimizing each baseline's window size for the target resolution would introduce its own confounds.
- **"Table 8 does not report performance change with sharing number."** — The paper explicitly states it provides "an overview of ShareFormer's performance and latency across different numbers of shared layers," implying both are reported.
- **"HAT is cited but not compared in tables."** — HAT uses large-scale ImageNet pre-training, which is a fundamentally different regime from the DIV2K-only training used here. The paper acknowledges HAT as a related method with a different training strategy.
- **"No variance/confidence intervals."** — Single-run evaluation on established benchmarks is the community norm for this subfield; requiring multi-run statistics exceeds standard practice.
- **"Lesion study figures lack axis labels/values."** — This is a PDF-parser artifact; the original figures likely include proper labeling. The underlying evidence would be strengthened by quantitative smoothness metrics regardless.

## Novel Insights

None beyond the paper's own contributions. The main observations — that sharing attention maps across layers is viable for image restoration and that residual Value connections induce a locality bias that aids trainability — are the paper's own findings, not novel cross-review syntheses.

## Suggestions

1. **Add the missing within-architecture ablation.** Create a version of ShareFormer with no sharing (separate attention map per block, same architecture otherwise) and compare PSNR, latency, and FLOPs on Urban100 ×4. This single experiment would resolve the central ambiguity about what sharing contributes.
2. **Provide a pseudocode algorithm** specifying the sharing policy: how many layers per group, which layers compute attention maps vs. reuse, and how the residual Value connects across shared blocks.
3. **Show training curves** (loss vs. iterations) for at least one task, comparing ShareFormer with and without residual Value.
4. **Add a comparison of attention map similarity** (cosine similarity or KL divergence) between adjacent layers in a non-sharing baseline to justify the sharing premise empirically.
5. **Include at least one modern efficient CNN baseline** (e.g., NAFNet) when making the "Can Transformer be faster than CNN?" claim.
