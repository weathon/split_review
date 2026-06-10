## Summary

CMC-Bench introduces the first benchmark for evaluating Cross-Modality Compression (CMC), where images are compressed by cascading Image-to-Text (I2T) and Text-to-Image (T2I) models. The paper constructs a dataset of 58,000 distorted images from 1,000 ground-truth images spanning Natural Scene Images (NSI), Screen Content Images (SCI), and AI-Generated Images (AIGI), using 6 I2T and 12 T2I models in four compression modes (Text, Pixel, Image, Full). It collects 160,000 human MOS annotations for both consistency and perception dimensions, and fine-tunes TOPIQ as an objective metric that achieves σ > 0.9 correlation with human judgments. The key empirical finding is that at ultra-low bitrates (0.002–0.024 bpp), CMC combinations outperform traditional codecs (VVC, HEVC, AVC, CDC) on most perceptual and semantic consistency metrics, while pixel-level fidelity (SSIM) remains a weakness.

## Strengths

1. **First joint benchmark for I2T+T2I compression pipelines.** The paper explicitly identifies that existing benchmarks evaluate I2T or T2I in isolation, and systematically fills this gap by testing collaborative performance across 6 I2T and 12 T2I models in four compression modes (Tables 3–5, Figure 3, lines 33, 92–99). This is the paper's core and genuine contribution.

2. **Large-scale human annotation with dual dimensions across three image types.** CMC-Bench provides 160,000 MOS annotations from 20 expert raters per image, covering both consistency and perception — a combination absent from prior datasets (CLIC, SCID, CCT, AGIQA-3K, ImageReward), as shown in Table 1 (lines 40–56). The inclusion of NSI, SCI, and AIGI in a single dataset is a meaningful step forward.

3. **Evidence that CMC methods are competitive with traditional codecs at extreme bitrates.** Figure 6 (lines 274–295) compares two CMC combinations against VVC, HEVC, AVC, and CDC across 8 metrics (4 consistency, 4 perception) at four bitrates. CMC methods win on most metrics except SSIM. This is a well-evidenced, practically significant finding even though the framing could be more measured.

4. **TOPIQ fine-tuned on CMC data achieves σ > 0.9 correlation with human judgments.** Table tab:iqa (lines 133–147) shows Spearman correlations of 0.943 (consistency) and 0.901 (perception), substantially higher than eight alternative IQA methods (AHIQ 0.844, CLIPIQA 0.825, etc.). This provides a validated proxy for large-scale evaluation.

5. **Principled four-mode framework that formalizes the CMC design space.** Section 3.2 (lines 81–91) defines Text, Pixel, Image, and Full modes with distinct bitrates (CR ~1,000× to ~10,000×) and configurations (Figure 2), systematically decomposing the CMC pipeline into controllable factors. This goes beyond prior CMC works that each used a single fixed pipeline.

6. **Controlled ablation isolating I2T and T2I contributions.** The experimental design fixes RealVis when varying I2T models and fixes GPT-4o when varying T2I models (Section 3.3, lines 95–98), enabling clean attribution of which pipeline component drives performance differences.

7. **Identification of SCI as a specific bottleneck.** Section 4.2 (lines 242–243) documents that compression results on SCI lag behind NSI and AIGI in both perception and consistency, attributing this to text within SCIs that I2T models fail to encode. This is a concrete, actionable finding for future CMC research.

## Weaknesses

### Fatal
None.

### Major

1. **No uncertainty quantification for any benchmark result.** Tables 2–5 (lines 167–234) report single-valued scores without standard deviations, confidence intervals, or any measure of variability. With 1,000 images averaged per metric, there is variance across images and model runs. Differences between top models are often tiny (e.g., GPT-4o at 2.439 vs. ShareGPT at 2.432 in Table 5; DiffBIR at 2.647 vs. PASD at 2.494 in Table 2). Without error bars, it is impossible to assess which differences are meaningful. For a benchmark paper whose purpose is to establish a leaderboard, this is the most significant technical gap. The paper should provide bootstrap confidence intervals, standard errors, or at minimum indicate statistically significant differences.

2. **Bitrate accounting is not transparent enough for reproducibility.** The paper defines ULB at 0.024 bpp and ELB at 0.0024 bpp (line 159), and uses 10–20 word captions for I2T models (line 101). However, it never specifies how text is converted to bits — what tokenization scheme, vocabulary size, or encoding overhead is assumed? For Pixel mode (line 86), the operation "merged and quantized into one pixel" is underspecified: what type of merging (averaging? downsampling?), what quantization scheme, and what bit depth per pixel? Without this detail, the rate-distortion comparison with traditional codecs in Figure 6 cannot be independently verified or reproduced by other researchers.

### Minor

1. **Abstract overclaims the central finding.** The abstract states the paper "proves that the combination of some I2T and T2I models has surpassed the most advanced visual signal codecs." The body presents a more qualified picture: CMC wins on most perceptual and semantic metrics but loses on SSIM (pixel fidelity), and the consistency advantage is modest (≈30% bitrate reduction at 0.02 bpp, line 299). The conclusion properly hedges ("surpassed traditional codecs in multiple aspects," line 313). The abstract should be calibrated to match the nuanced evidence.

2. **Domain shift between TOPIQ training data and benchmark evaluation.** The subjective annotation set (4,000 images) was generated with random denoising strength (0.2–0.9), while the 58,000-image benchmark uses fixed strengths (0.5 for Full/Image, 0.8 for Pixel, 1.0 for Text, line 119). The paper validates TOPIQ on held-out data from the same random-strength distribution, then deploys it on the fixed-strength benchmark without re-validation. The claim that subjective and objective rankings "align closely" (line 271) compares rankings on the same limited set of models, not on the full diversity of the benchmark. The paper should either validate TOPIQ on a held-out set from the benchmark distribution or explicitly discuss this as a limitation.

3. **Inter-annotator agreement statistics are not reported.** The paper collected 160,000 subjective ratings from 20 annotators per image (line 118) but reports no agreement metrics (e.g., Krippendorff's alpha, ICC, or pairwise agreement). Without this, the quality of the human ground truth — which serves as the gold standard for training TOPIQ — cannot be assessed. This is standard practice for subjective annotation papers.

4. **The comparison with traditional codecs uses a single operating point for each codec.** VVC is used only at QP=53, targeting ~1,000× compression (line 106). While the four CMC modes provide multiple bitrate points, VVC's own rate-distortion curve across a range of QPs is not shown. Full RD curves would strengthen the comparison and is standard practice in compression papers.

5. **Results are contingent on specific anchor models.** Fixing RealVis for I2T evaluation and GPT-4o for T2I evaluation (lines 97–98) is a sensible design choice, but different anchors could produce different rankings if certain I2T+T2I pairs have synergistic interactions. This should be discussed as a limitation.

### Trivial

1. The "Pixel" mode description ("Each 64×64 blocks from ground truth are merged and quantized into one pixel," line 86) should specify the exact merging operation and quantization scheme.

2. The 400/300/300 split (NSI/SCI/AIGI) for ground truth images (line 66) is not justified by real-world distribution proportions. The justification ("most mainstream," "increasing on the Internet") is reasonable but could be more precise.

## Nice-to-Haves

- **Include CMC baselines from prior work.** The paper discusses prior CMC methods (M-CMC, MISC, Text+Sketch) in Section 2 but does not benchmark them, justifying that they use "relatively outdated" models (line 31). While this scope choice is defensible — the paper's purpose is benchmarking latest LMMs — including even one representative prior CMC pipeline would anchor the improvements and help connect to existing literature.

- **Sensitivity analysis for the 2×FR + 1×NR weighting.** The overall score weighting (line 128) is justified by TOPIQ-FR's smaller floating range, but the paper could show whether rankings are robust to alternative weights (e.g., 1:1, 3:1).

- **Full rate-distortion curves for traditional codecs** across multiple QP values, rather than a single point, would strengthen the comparison with CMC methods.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"SSIM dismissal" framing (Harsh Critic).** The paper says "Given that SSIM is purely pixel-based, the performance drop due to generative compression is expected" (line 299). This is a reasonable technical explanation for why a generative method underperforms on a pixel-level metric, not a dismissal. The paper is transparent about CMC's weakness on SSIM. REMOVED: misleading characterization.

- **"FR→Consistency, NR→Perception mapping insufficiently defended" (Harsh Critic).** This mapping (FR = consistency, NR = perception) is a standard operationalization in IQA literature, used widely without separate defense. The paper's subjective annotation protocol separately annotates both dimensions, providing construct validity. REMOVED: overdrawn criticism of a standard design choice.

- **"Ground truth proportions unjustified" framing (Harsh Critic).** The paper provides explicit justification: NSI is "most mainstream" (400), SCI and AIGI are increasing online (300 each) (line 66). This is reasonable for a benchmark covering three content types. REMOVED: the justification exists and is adequate.

- **"Circularity" framing for TOPIQ validation (Harsh Critic).** The paper performs a standard 80/20 train/test split on its annotated data. Calling this "circularity" is inaccurate — the actual issue is the distribution shift between training and evaluation data, which is a domain generalization concern (retained as Minor weakness #2 above). The "circularity" label itself is removed.

## Novel Insights

The most interesting observation from the review synthesis is that the paper's methodology has an internal tension: it claims to be a benchmark for the compression community (which would demand rigorous rate-distortion analysis with uncertainty quantification) while simultaneously functioning as an LMM evaluation benchmark (where rankings without error bars and controlled ablations are standard). The paper falls between these two traditions — it borrows the dataset-scale and annotation protocols from IQA/LMM benchmarking but applies them to a compression framing that requires RD curves, transparent bitrate accounting, and statistical rigor. Bridging this gap cleanly (rather than satisfying each community's conventions partially) would significantly strengthen the paper.

## Suggestions

1. Add standard errors, confidence intervals, or bootstrap uncertainty to all benchmark tables. Even a simple ± notation for per-metric standard deviations across the 1,000 images would transform the interpretability of the rankings.

2. Provide a precise specification of bitrate calculation: how are I2T outputs (words/tokens) converted to bits? What overhead (tokenization, encoding) is included? For Pixel mode, specify the exact merging operation and bit depth.

3. Calibrate the abstract to match the evidence: "CMC methods are competitive with or surpass traditional codecs on perceptual and semantic consistency metrics at ultra-low bitrates, while pixel-level fidelity remains a weakness."

4. Validate TOPIQ on a held-out set drawn from the same distribution as the full 58,000-image benchmark (fixed denoising strengths), or clearly discuss the domain shift as a limitation.

5. Report inter-annotator agreement statistics for the subjective annotations.

6. Add full rate-distortion curves for VVC across multiple QPs to strengthen the codec comparison.

7. Include a discussion of how results might depend on the specific anchor models chosen for ablation studies.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>