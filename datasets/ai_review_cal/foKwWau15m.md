- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 6, 8
Now I have a complete picture. Let me construct the final consolidated review.

## Summary

CMC-Bench introduces the first dedicated benchmark for Cross-Modality Compression (CMC), the Image-Text-Image pipeline that cascades I2T and T2I models for ultra-low-bitrate image compression. The benchmark comprises 58,000 distorted images across 6 I2T and 12 T2I models, with 160,000 human preference annotations covering both consistency and perception dimensions. Four compression modes (Text, Pixel, Image, Full) are defined to span the spectrum of CMC pipelines. The paper demonstrates that top CMC combinations (GPT-4o+DiffBIR, GPT-4o+RealVis) outperform traditional codecs (VVC, HEVC, AVC, CDC) on most metrics at ~0.02 bpp.

## Strengths

- **Large-scale, multi-dimensional human-annotated dataset (58k images, 160k annotations)**: This is the first joint benchmark for I2T+T2I compression, covering consistency and perception across NSI, SCI, and AIGI content types (Table 1, Section 3.4). This is a concrete, reusable resource.

- **Systematic four-mode compression taxonomy**: The Text/Pixel/Image/Full modes (Section 3.2, Figure 2) provide a principled framework for comparing very different model paradigms (generative vs. restorative) across distinct bitrate regimes. This is a genuine methodological contribution.

- **Demonstrates CMC surpassing traditional codecs at ultra-low bitrates on most metrics**: Using specific complete pairs (GPT-4o+DiffBIR, GPT-4o+RealVis), the paper shows CMC outperforms VVC, HEVC, AVC, and CDC on 6 of 8 metrics at ~0.02 bpp (Section 4.4, Figure 3). This is the central empirical result and it is supported by evidence.

- **TOPIQ validated against human judgments with high correlation**: Table 2 shows fine-tuned TOPIQ achieves Spearman correlations of 0.943 (consistency) and 0.901 (perception) with human ratings on the held-out test set. This justifies its use as a proxy metric.

- **Per-image-type breakdown reveals specific, actionable weaknesses**: The finding that SCI consistently underperforms across both I2T and T2I models (Section 4.2, Tables 3–5) identifies a concrete gap ("text generation capabilities of recent T2I models are still limited" for SCI) that directly guides future work.

- **Nuanced analysis of restorative vs. generative tradeoffs**: The paper shows restorative models (DiffBIR, PASD) dominate consistency in Full/Image modes but are inapplicable to Text/Pixel modes, while generative models like PG25 excel in perception at the cost of consistency. This goes beyond simple ranking.

## Weaknesses

### Fatal
None.

### Major

- **TOPIQ metric fine-tuned on T2I-only variation data is applied to rank I2T models without validation.** The subjective annotations (Section 3.4) fix I2T to GPT-4o and vary only the T2I model. The fine-tuned TOPIQ is tested on 20% of this T2I-variation data (Section 4.1, line 147). However, Table 3 (`tab:i2t`) uses this same TOPIQ to rank I2T models (where T2I is fixed to RealVis and I2T varies). The metric has never been validated on I2T-induced distortion patterns. The paper does not acknowledge this distribution mismatch, and the I2T leaderboard's reliability is therefore uncertain. This does *not* undermine the paper's headline comparison with traditional codecs (which uses complete, explicitly evaluated pairs), but it does weaken the claim of a validated I2T ranking.

### Minor

- **Rate-distortion comparison has only 4 operating points per curve (one per mode).** The comparison in Section 4.4 (Figure 3) uses exactly one point per mode, which is sparse for a rigorous rate-distortion analysis. While the four modes are natural operating points for CMC, the traditional codecs could be evaluated at many more bitrate levels, making the comparison asymmetric. The conclusion about "surpassing" codecs would be stronger with denser sampling.

- **Pixel mode and bitrate calculations are underspecified.** The Pixel mode description ("Each 64×64 blocks from ground truth are merged and quantized into one pixel," line 86) lacks detail on the merging/quantization procedure. The bitrate calculations (CR of ~10,000, ~5,000, ~1,000) are stated only approximately, and the exact formulas for converting between CR, bpp, and bits are not provided. These may be in the supplementary (which is stripped), but this is a nontrivial methodological detail for a compression benchmark.

- **The claim that CMC has "surpassed the most advanced visual signal codecs" (abstract) is slightly too sweeping** given that (a) SSIM shows a large deficit (acknowledged by the authors as "purely pixel-based," line 299, but the abstract does not qualify this), (b) the lead in consistency is modest (~30% bitrate reduction at 0.02 bpp), and (c) only 4 operating points are compared. The body text is appropriately measured, but the abstract could be more precise.

### Trivial

- The paper states it evaluates "6 I2T and 12 T2I models," but in practice 4 of the 12 T2I models are restorative (IR) models that only apply in Full/Image modes, and 12 are listed in Table 1 (`tab:t2i-high`). The count is correct but the distinction could be clearer on first reading.

## Nice-to-Haves

- Validating a small number of full I2T×T2I cross-product pairs (e.g., top-3 I2T × top-3 T2I = 9 pairs) would strengthen the claim that separate ranking of I2T and T2I models yields the optimal combination. The paper already evaluates two full pairs (GPT-4o+DiffBIR, GPT-4o+RealVis); a few more would address the interaction concern directly.
- Providing the subjective validation results (or at least a brief discussion of expected generalization) for the I2T ranking context would significantly strengthen the paper's methodological rigor.

## Removed Points

- **"Never evaluates full cross-product pairs (e.g., ShareGPT + PG25)"** — Removed because the paper does evaluate specific complete pairs against traditional codecs (Section 4.4). The ranking experiments fix one side, which is a standard ablated evaluation design for multi-component systems. This is not a structural flaw; the paper's core claims about beating codecs rely on the specific pairs tested. The absence of *all* cross-product pairs is a limitation, but the harsh critic overstates this as a fatal flaw — it is better captured as a nice-to-have.

- **Criticism about pixel-mode description being "too vague to reproduce"** — Demoted from a claimed structural issue to a minor weakness (the description is underspecified but likely expanded in the supplementary).

- **"The paper does not acknowledge this limitation" (about I2T ranking)** — This is an observation, not a separate weakness. The underlying substantive issue (TOPIQ not validated on I2T variation) is retained as a Major weakness.

- **Generic "evaluation lacks rigor" phrasing** — Removed per filtering rules as it lacks a specific concrete anchor beyond what is already captured in the specific weaknesses above.

## Novel Insights

The most insightful observation from the reviews — and one not fully foregrounded by the paper itself — is the interplay between the evaluation design and the claims it can support. The paper separates the ranking of I2T and T2I models via fixed-side experiments, but the subjective calibration data is collected under only one fixed-I2T condition, creating a subtle but real asymmetry in how well the metric is validated for each ranking. This is not a fatal flaw (the paper's two headline complete-pair evaluations against codecs are unaffected), but it means the I2T leaderboard should be treated as a preliminary finding rather than a validated result. The reviewers also correctly identify that the SCI weakness finding and the restorative-vs-generative tradeoff analysis are the paper's most valuable specific insights for future CMC research, beyond the benchmark itself.

## Suggestions

1. **Acknowledge and address the I2T ranking limitation**: Either (a) collect a small set of subjective annotations for I2T variation and validate TOPIQ on that distribution, or (b) clearly qualify the I2T leaderboard as tentative and note that the metric has only been validated on T2I-variation data. This one change would substantially improve the paper's methodological soundness.

2. **Add a few full cross-product validation pairs**: Testing, e.g., the top/bottom I2T models with the top/bottom T2I models (a 2×2 or 3×3 grid) would directly verify that the separately identified rankings hold in combination and would silence the interaction concern.

3. **Provide more operating points for the rate-distortion comparison**: Even 2–3 additional bpp levels for each mode (e.g., varying the strength parameter or QP) would make the comparison with traditional codecs more rigorous.

4. **Clarify the Pixel mode and bitrate calculations** in the main text or ensure the supplementary covers these fully.
