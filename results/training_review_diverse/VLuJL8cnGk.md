Now I have all the information needed to verify claims against the paper. Let me produce the consolidated review.

---

## Summary

This paper proposes a method for single-image novel view synthesis that integrates a pretrained 3D-based NVS model (Zero123++) as weak guidance within a 3D-free inference-time optimization pipeline (HawkI-style). The key addition is a viewpoint regularization loss that aligns the optimized CLIP embedding with an angle-specific text embedding. The method requires no 3D training data and is evaluated on two complex-scene datasets across four viewpoints, showing consistent improvements over baselines.

## Strengths

1. **Clear empirical motivation through controlled analysis experiments.** Section 3.1 shows that removing the guidance image causes CLIP-based generation to produce inconsistent viewpoints despite explicit angle text, and Section 3.2 shows that incorrect guidance images dominate over correct text instructions. These controlled experiments provide a principled rationale for why 3D priors must be integrated as weak guidance rather than relying on CLIP alone.

2. **Novel viewpoint regularization loss improves camera control consistently.** The L₂ regularization term between \(e_{view}\) and \(e_{target}\) (Table 2) yields improvements in 50 out of 56 metric-configuration comparisons across 8 angle-dataset combinations and 7 metrics. The gains are particularly notable in CLIP score (e.g., +1.4 to +3.5 points over no-regularization baselines) and in LPIPS at certain viewpoints (e.g., −0.0337 on HawkI-Real at (30°,270°) vs. Zero123++). The ablation demonstrates the loss is doing meaningful work beyond what the Zero123++ guidance alone provides.

3. **Qualitative results show genuine improvements in background and detail preservation.** Figures 4–5 (HawkI-Syn and HawkI-Real results) show that the proposed method retains background elements (Seine River behind the Eiffel Tower, shadow on the pyramid, natural rock textures in the waterfall scene) that Zero123++ loses or distorts. These qualitative advantages are consistent with the method's design goal of handling complex, non-object-centric scenes.

4. **The method achieves its results without 3D training data.** The entire pipeline runs at inference time using frozen pretrained components (Stable Diffusion, Zero123++, CLIP) plus lightweight LoRA fine-tuning. This is a genuine practical advantage over methods like Free3D that require large-scale 3D dataset training.

## Weaknesses

### Fatal
None.

### Major
1. **Narrow evaluation scope limits generalization claims.** The method is tested on only two datasets (HawkI-Syn and HawkI-Real) from the same source, with just four fixed viewpoints. While these datasets contain complex scenes, the evaluation does not probe generalization to significantly different scene types (indoor scenes, heavily occluded views, large viewpoint changes beyond the 4 angles tested), nor does it compare against recent data-efficient baselines like Free3D (discussed in related work but not compared quantitatively). The paper's title and abstract claim the method "excels in handling complex and diverse scenes," but the evidence for diversity across scene types is thin.

2. **Missing analysis and specification of the regularization loss.** The paper does not report the weight/λ of the regularization term \(L_{reg}\) in the combined loss (Equation 4), nor provide any sensitivity analysis for this hyperparameter. It is unclear whether this weight is constant across all experiments. Additionally, \(e_{target}\) is described as "the text embedding that includes elevation and azimuth information" but the paper never explicitly states how it is computed (presumably CLIP encoding of \(t_{target}\)). The paper also does not analyze whether the L₂ constraint pulls \(e_{view}\) in a semantically meaningful direction versus simply overwriting content information — an embedding-space analysis (e.g., PCA projection showing separation of angle information from content) would significantly strengthen the claimed contribution.

### Minor
1. **Quantitative margins are modest on several metrics, and counterexamples are not discussed.** The LPIPS improvements over Zero123++ on HawkI-Syn (30°,30°) and HawkI-Real (30°,30°) are 0.0033 and 0.0052 respectively — thin enough to raise questions about stability, especially without confidence intervals. The SSCD metric favors Zero123++ on 2 of 4 configurations (both (30°,30°) angles), and the ablation study has several cases where metrics slightly degrade with regularization (e.g., HawkI-Real (−20°,330°) LPIPS: 0.5925 vs. 0.5894; HawkI-Real (30°,30°) CLIP-I: 0.8152 vs. 0.8231; HawkI-Real (−20°,210°) DINO: 0.3610 vs. 0.3817). These counterexamples are not discussed in the paper, which weakens the overall narrative of consistent improvement.

2. **PSNR and SSIM values are uniformly low** (~9–11 and ~0.2–0.3 respectively), indicating that even the best method differs substantially from ground truth at the pixel level. The paper does not contextualize or discuss this, which would help readers calibrate expectations.

3. **No computational cost analysis.** The method requires per-scene, per-viewpoint optimization (embedding optimization + LoRA fine-tuning). Wall-clock time or GPU-hour comparisons against baselines are not reported, making it difficult to assess the practical trade-off versus simpler approaches.

### Trivial
- The regularization loss weight (balancing \(L\) and \(L_{reg}\) in Equation 4) is not reported.
- A few metric configurations where regularization slightly underperforms are identified above but not discussed in the paper.

## Nice-to-Haves
- **Confidence intervals or bootstrap estimates**: Would strengthen confidence in the reported margins, though this is not standard practice in NVS papers and is not required for the paper's claims to be credible.
- **Failure case analysis**: Showing a few representative failure cases (e.g., where the guidance image is too poor, or where regularization pulls content away) would improve the evaluation's credibility.
- **Broader viewpoint coverage**: Testing on more than 4 fixed viewpoints or continuous angle ranges would demonstrate the method's flexibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The paper also omits comparison with recent data-efficient NVS methods such as Free3D, which also claims single-image novel view synthesis without dedicated 3D training on large datasets."* — The paper explicitly discusses Free3D in Section 2 (line 40) and notes that it "still requires training on large-scale 3D datasets like Objaverse," so the characterization of Free3D as not requiring 3D training data is inaccurate. The paper's method requires no 3D training data at all, making the comparison apples-to-oranges in this respect. A quantitative comparison would be nice but is not a missing requirement.

- *"The analysis sections (3.1, 3.2) confirm known limitations of CLIP and the role of guidance images—these observations are not new and do not constitute a deep insight that drives the design."* — This undersells the analysis. While individual facts about CLIP may be known, the paper uses controlled experiments to specifically motivate the design choice of using Zero123++ as *weak* (rather than strong) guidance, which is a non-obvious design decision. The analysis is directly tied to the method's architecture.

- *"The paper also omits comparison with recent data-efficient NVS methods such as Free3D"* (from Section-by-Section Notes) — Duplicate of the first removed point; the paper discusses Free3D and explains why it is a different class of method.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent assessment: the paper proposes a sensible combination of existing components with a small novel regularizer, but the evidence for the claimed level of improvement is mixed — clear on some metrics (CLIP score, qualitative background preservation) and thin on others (LPIPS at certain angles, SSCD). The most useful insight from the reviews is the observation that the regularization loss's mechanism is under-analyzed: the paper would be significantly stronger with an embedding-space analysis showing that \(e_{view}\) moves toward \(e_{target}\) along angle-relevant directions while preserving content-relevant directions.

## Suggestions

1. **Report the regularization loss weight** and include a sensitivity analysis showing the trade-off between viewpoint alignment and content preservation as the weight varies.
2. **Expand the evaluation** to include at least one more dataset of a different type (e.g., indoor scenes, real-world object-centric datasets like CO3D) and more varied viewpoints beyond the four fixed angles.
3. **Discuss counterexamples** — the cases where regularization slightly hurts one metric (e.g., SSCD, DINO in certain configurations) should be acknowledged and explained, which would actually increase trust in the overall evaluation.
4. **Add embedding-space analysis** for the regularization loss: e.g., project \(e_{input}\), \(e_{view}\) (with and without regularization), and \(e_{target}\) into 2D PCA space to show that regularization moves \(e_{view}\) toward \(e_{target}\) along angle-relevant dimensions while preserving content directions.

## Score and Decision

The paper presents a clean, well-motivated method that combines existing ideas with a useful novel regularizer. The ablation convincingly shows that the regularization term contributes positively. However, the paper's weaknesses are real and non-trivial: the evaluation is confined to two datasets from one source with only four fixed viewpoints, the quantitative margins are modest on several metrics with counterexamples left unaddressed, a key hyperparameter (regularization weight) is unreported, and the mechanism of the main novel contribution is not analyzed in the embedding space. The contribution is incremental but directionally valuable. It sits at the borderline: the core idea is sound and the paper is clearly written, but in its current form the evidence does not rise to the level of a strong acceptance.

**Overall Assessment**: The paper would benefit significantly from expanded evaluation, hyperparameter reporting, and embedding analysis before it makes a compelling case for its claimed level of improvement.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>