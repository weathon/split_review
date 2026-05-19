- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
I'll proceed with the review based on the paper content and the provided reviews.

Here is my final consolidated review:

---

## Summary

The paper proposes Add-it, a training-free method for inserting objects into images using pretrained diffusion models (FLUX). The core contribution is a weighted extended-attention mechanism that balances three information sources — the source image, the target image, and the text prompt — along with a structure transfer initialization and a subject-guided latent blending step to preserve fine details. The method also introduces a new "Additing Affordance Benchmark" to evaluate placement plausibility. Without any fine-tuning, Add-it achieves strong results on both automatic metrics and human evaluations (preferred in >80% of head-to-head comparisons), outperforming prior supervised and zero-shot methods.

## Strengths

- **Weighted extended-attention mechanism is well-motivated and convincingly analyzed.** The paper identifies a core failure mode in prior extended-attention approaches — that naively concatenating source image tokens causes source dominance and object neglect — and addresses it with an automatic root-finding procedure for the scaling factor γ that balances attention between source and target tokens. The analysis in Section 5 (Figure 4A/B) empirically validates that the auto-selected γ achieves a good trade-off between object inclusion and affordance, and the ablation across γ values is clean and informative.

- **Human evaluation evidence is strong and direct.** Head-to-head human preference studies on both real (EmuEdit) and generated (Additing Benchmark) images show Add-it preferred in ~80–90% of cases against each baseline, including supervised methods specifically trained for object insertion. This is the most compelling evidence that the method produces perceptually superior results and is not an artifact of any single metric.

- **New Affordance Benchmark fills an important evaluation gap.** The paper correctly identifies that existing CLIP-based metrics do not measure placement plausibility. The manually annotated "Additing Affordance Benchmark" (200 images with plausible-location bounding boxes) and the associated evaluation protocol are a useful contribution to the community, enabling future work to be assessed on placement quality.

- **Thorough ablation and analysis of design choices.** The paper systematically ablates the weight scale γ (Fig 4A), the structure transfer timestep (Fig 5), and the latent blending component (Fig 6), validating each design choice. The attention distribution visualizations (Fig 4B) provide insight into the mechanism's behavior.

- **Simple and practical inversion approach for real images.** The paper proposes a pragmatic noising technique for real images (instead of inversion), acknowledging its limitations honestly. This makes the method applicable to both generated and real images without complex inversion pipelines.

## Weaknesses

### Fatal
None.

### Major

- **Comparison with supervised methods is confounded by the base model.** The paper claims to "outperform supervised methods," but the trained baselines (InstructPix2Pix, MagicBrush, EraseDraw) use SD1.5/2.1 backbones, while Add-it operates on FLUX.1-dev — a newer, independently more powerful model. The zero-shot baselines (Prompt2Prompt, SDEdit) are re-implemented on FLUX for fair comparison, but the trained methods are not. This means a significant portion of the quantitative gap (Tables 1–2) may come from the base model upgrade rather than the proposed attention mechanism. The paper partially addresses this with the γ=1.0 ablation (standard extended attention on FLUX, Fig 4A), showing it performs worse than the auto-γ version, but this ablation is not evaluated as a standalone baseline on the main benchmarks. A proper FLUX-based "no weighted attention" baseline on the same benchmarks would isolate the contribution of the method from the contribution of the backbone. As it stands, the claim of "outperforming supervised methods" is overstated without controlling for this confound.

### Minor

- **Affordance metric conflates object detection and placement quality.** The Affordance score (Table 1) requires Grounding-DINO to first detect the object in the output. If a method frequently fails to insert the object at all, its Affordance score is automatically depressed regardless of placement quality. While this is a valid design choice (an undetected object cannot be plausibly placed), reporting Inclusion (Table 2) separately only partially addresses the concern — the two metrics are measured on different benchmarks. On the Affordance benchmark, no Inclusion scores are reported, making it difficult to disentangle whether the large gap (0.828 vs. next best 0.474) reflects better object insertion rates or better placement conditioning. The authors should either report Affordance conditioned on successful detection or provide Inclusion scores for the same benchmark.

- **It is not specified whether γ is computed per timestep, per layer, or just once.** The root-finding procedure for γ is described in terms of attention distributions at a single timestep/layer, but the paper does not clarify if a single γ is used across all timesteps/layers or if it is recomputed. This detail would aid reproducibility.

- **The real-image pipeline's reliance on random noise (rather than inversion) is acknowledged as weaker, but the potential artifacts from the noising procedure itself are not discussed.** The paper notes that real-image results are less effective, but does not analyze whether the noising process introduces high-frequency artifacts that the blending step cannot correct.

### Trivial
- The claim "improving affordance from 47% to 83%" (abstract, conclusion) is not clearly traceable in the tables; Table 1 reports absolute Affordance scores (0.828) and the 47% baseline is mentioned in the abstract but the source of the 47% number is not explicitly shown.

## Nice-to-Haves
- Reporting runtime (seconds per image on an A100) would help readers assess practical utility.
- Confidence intervals or bootstrap estimates for the automatic metrics would strengthen the quantitative claims, though the large margins in human evaluation make this less critical.
- The real-image noising procedure could be described with more formal detail (e.g., whether the same random seed is used for source noising and target denoising).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The teaser figure and the architecture figure (Fig. 1) are described but not visible in the text; I assume they exist in the original."* — Parsing artifact, not a paper weakness.
- *"The mask extraction procedure (which timesteps, which layers, how object token is identified) is relegated to the appendix"* — Missing appendix content is a parser artifact; the original submission contains these details.
- *Criticism that mixes benchmarks ("InstructPix2Pix has Inclusion=34% on EmuEdit vs. Affordance gap 0.276 vs. 0.828")* — The Inclusion and Affordance numbers cited come from different benchmarks (EmuEdit vs. Additing Affordance Benchmark), making the specific numerical comparison invalid. The general concern about the metric design is retained above as Minor.
- *"Statistical significance: The Tables report point estimates but no confidence intervals"* — Generic weakness; the large margins in human evaluation make this less critical and it is not standard practice for these benchmarks.
- *"Diversity of results: Qualitative figures show only a handful of examples"* — Generic request; 6 examples per figure is standard for qualitative comparison papers.

## Novel Insights

A genuinely novel observation emerges from comparing the two reviews: the harsh critic raises the base-model confound as a threat to the paper's central quantitative claims, while the strength finder treats the same comparisons as definitive evidence. The merger's direct reading of the paper confirms that (a) the human evaluations are indeed strong and largely immune to this critique (humans judge outputs, not model provenance), but (b) the automatic metric comparisons (Tables 1–2) indeed conflate method and backbone. The paper's own γ=1.0 ablation (standard extended attention on FLUX, Fig 4A) is the ideal control and shows worse performance than the full method, but this was not evaluated on the main benchmarks. The strongest version of the paper would add a single column to Tables 1–2: "Extended Attention on FLUX (γ=1.0)" — this would cleanly resolve the confound concern.

## Suggestions

1. **Add a FLUX-based "no weighted attention" baseline (γ=1.0) to Tables 1 and 2.** This single addition would directly address the base-model confound by showing what the same backbone achieves without the proposed mechanism. The ablation data in Fig 4A already suggests this baseline would underperform, making it a low-cost, high-impact addition.

2. **Report Inclusion scores on the Affordance Benchmark, or report Affordance conditioned on successful detection.** This would allow readers to distinguish whether Add-it's superior Affordance score is driven by better object insertion rates, better placement, or both.

3. **Clarify whether γ is computed per timestep/per layer or globally**, and add a sentence describing the noising procedure for real images more precisely.
