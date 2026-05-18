Now I have a clear picture of the calibration landscape. Let me write the review.

## Summary

This paper introduces GenDataAgent, a generative agent that augments vision training datasets with synthetic data on-the-fly during model fine-tuning. The method iteratively generates synthetic data targeting marginal real examples (those near the decision boundary), uses Llama-2 perturbation for caption diversity, and applies a Variance-of-Gradients (VoG) filter to remove out-of-distribution synthetic outliers. The paper evaluates on six image classification datasets across both synthetic-only and real+synthetic augmentation settings, reporting improvements in top-1 accuracy and worst-class disparity over static synthetic data methods.

## Strengths

- **On-the-fly iterative feedback between classifier and generator is a genuine novelty**: Unlike prior work that uses static synthetic data or a single offline feedback cycle (Hemmat et al., 2023), GenDataAgent continuously resamples marginal examples based on the current model state and generates new synthetic data at each fine-tuning iteration (§3.5, Algorithm 1). This dynamic interaction is clearly motivated and addresses a real limitation of prior approaches.

- **Component-level ablation (Table 3) provides clean evidence that each design choice contributes**: The break-down ablation shows that adding marginal score sampling (+0.19–1.47 accuracy), Llama-2 perturbation (+0.27–0.97), and VoG filtering (+0.32–1.99) provides consistent improvements across datasets. This is the strongest empirical evidence in the paper.

- **Content analysis (Section 5) offers useful insights beyond accuracy numbers**: The analysis showing that GenDataAgent generates more synthetic data for low-accuracy classes (Figure 5), reduces overfitting (Figure 6a), and that real and synthetic data play distinct roles at different training stages (Figure 6b) provides valuable qualitative understanding of the method's behavior.

- **Consistent results across multiple datasets and backbones**: The method is evaluated on IN100 and five fine-grained datasets, with both ResNet-50 and CLIP backbones, showing consistent improvements over static baselines (Real-Fake, ImageNetClone, CiP, SyntheticData).

## Weaknesses

### Fatal
None.

### Major

- **The Internet Explorer baseline comparison in the augmentation setting (Table 2) is unfair.** The paper compares against a modified version of their own method where "Marginal Sampling and VoG Filtering" are replaced with "15-NN similarity" (§4.1), rather than comparing against the original Internet Explorer method (Li et al., 2023a). The original Internet Explorer uses an expected-reward framework to rank internet-sourced images; substituting its selection mechanism with a simple nearest-neighbor heuristic produces a lower-bound baseline. The claim of "outperforming other SOTA methods" cannot be fully supported by this comparison. This is the most serious weakness because it directly affects the core claim of SOTA performance in the augmentation setting.

- **The VoG (Variance of Gradients) filter lacks quantitative validation of its core assumption.** The paper relies on the claim that "in-distribution data tends to own higher variances of gradients" (§3.4) but provides only qualitative t-SNE visualizations on a single dataset (Oxford-IIIT Pets) as evidence. There is no comparison with random filtering, no oracle experiment (real vs. synthetic outliers), no correlation analysis with distribution distance metrics, and no ablation where VoG filtering is replaced with a simpler baseline. Without such validation, it is unclear how much of the reported improvement is attributable to the VoG mechanism versus the overall pipeline. Additionally, the VoG formula (§3.4) has a dimensionality ambiguity: gradients are defined per-pixel (a vector), yet the formula treats them as scalars when computing variance, with no explicit aggregation step, making the operation non-reproducible.

### Minor

- **Missing hyperparameter and reproducibility details.** The synthetic data ratio (1×, 10×, or other) used in the main experiments (Tables 1 and 2) is not specified. The number of marginal samples *k* per dataset is not reported. While Section 4.3 explores different ratios, the main comparisons lack this information. Results are reported as single numbers without standard deviations or confidence intervals, making it impossible to assess statistical significance.

- **Unclear initialization of the synthetic-only setting.** In the synthetic-only protocol (§4.1), "we replace the initial real dataset τ with an equivalent number of synthetic training samples" — but the source of these initial synthetic samples is not disclosed. This is a reproducibility issue, though the criticism about "real data leakage" is incorrect: the paper explicitly states τ is replaced, so no real data is used in the synthetic-only setting.

- **Minor concerns about marginal score calibration and VoG checkpoint count analysis.** The marginal score uses predicted probabilities without calibration analysis, which could be unreliable for poorly calibrated models. The analysis of different VoG checkpoint counts (Table 5) shows "no significant difference," which raises the question of whether the VoG score is actually sensitive to the training dynamics it claims to measure.

### Trivial
- None.

## Nice-to-Haves
- Comparison with the original (unmodified) Internet Explorer baseline would make the augmentation-setting results fully convincing.
- Adding error bars (3+ seeds) would help assess significance given the magnitude of improvements reported.
- A random-filtering baseline for VoG would help validate the filtering mechanism's contribution beyond simply discarding some samples.

## Removed Points
- **Critical Issue 1 from the harsh critic ("Synthetic-only evaluation is unfair — real data leakage")**: Removed because the paper explicitly states (§4.1): "we replace the initial real dataset τ with an equivalent number of synthetic training samples." In the synthetic-only setting, no real data is used for SD adaptation, initial training, or marginal sampling. The criticism is factually incorrect.
- **Criticisms about missing appendix content, proof details, garbled text, formatting nitpicks, and "unreleased" references**: Removed per the meta-review guidelines — these are parser artifacts or review knowledge gaps.
- **Several generic section-by-section notes (e.g., "related work is high-level," "qualitative t-SNE could be cherry-picked," "expensive per-dataset step")**: Removed as they are either subjective or apply to the standard practice in this field.

## Novel Insights

The most interesting dynamic revealed by the reviews is that the paper's core innovation — iterative on-the-fly feedback — is also the source of its most significant evaluation challenges. The iterative nature makes it genuinely difficult to construct a fair "synthetic-only" baseline because any initialization inevitably uses some pre-existing data to start the feedback loop. This tension between methodological novelty and clean evaluation is characteristic of papers at the intersection of generative models and training pipelines. The reviews also highlight an unresolved tension: the VoG filter is presented as a principled mechanism but is validated only qualitatively, while the ablation (Table 3) shows it provides the largest single improvement. If the authors could provide a clearer mechanistic explanation for why VoG works (beyond the t-SNE plots), it would substantially strengthen the paper's theoretical contribution.

## Suggestions

1. **For the Internet Explorer comparison**: Compare against the original Internet Explorer method directly, or at minimum argue why the 15-NN approximation is a faithful stand-in. Without this, the SOTA claim for the augmentation setting should be softened.
2. **For VoG validation**: Add a controlled experiment comparing VoG-based filtering against (a) random filtering with the same淘汰 rate, (b) oracle filtering using real-vs-synthetic labels, and (c) an alternative OOD score (e.g., Mahalanobis distance). Clarify the dimensionality of the VoG computation in the formula.
3. **For reproducibility**: Report the synthetic data ratio and *k* (number of marginal samples) used in the main tables. Add error bars for at least 3 runs on a subset of datasets.
4. **Clarify the synthetic-only initialization**: Specify how the initial synthetic training samples are generated (e.g., using the same generation method as the baselines).

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `07yvxWDSla.md` (Synthetic continued pretraining) | 8.00 | Much stronger: clean theory + experiments, no evaluation flaws |
| `svIdLLZpsA.md` (Real-Fake) | 6.00 | Stronger: has theoretical grounding, cleaner evaluation; GenDataAgent's contribution is more novel but evaluation is weaker |
| `Xr5iINA3zU.md` (Collapse or Thrive) | 5.75 | Comparable overall: both have genuine contributions but evaluation issues; this paper has more methodological novelty |
| `XgklTOdV4J.md` (DualAug) | 5.67 | Comparable: both propose filtering mechanisms for augmentation; DualAug has cleaner evaluation, GenDataAgent has more novel pipeline |
| `nLlBLzPpeG.md` (AutoGenDA) | 4.75 | Slightly weaker: AutoGenDA's scope is narrower (imbalanced classification) and its novelty is more limited; GenDataAgent's iterative mechanism is more original |
| `MyAqAYCjP5.md` (Mousterian) | 3.83 | Weaker: purely empirical study with limited novelty; GenDataAgent has a clearer methodological contribution |
| `9aIlDR7hjq.md` (Augmented Conditioning) | 4.00 | Weaker: limited technical novelty; GenDataAgent's on-the-fly mechanism is more novel and the ablation is cleaner |

**Score rationale**: The paper has a genuine contribution in the iterative feedback mechanism and the component design, which is more novel than several papers scoring below 5. However, the unfair Internet Explorer comparison and the weakly-validated VoG filter prevent the SOTA claims from being fully substantiated. The paper sits between the mid-range rejected papers (~4.75) and the stronger accepted papers (~6.0) in terms of overall quality, with the evaluation issues being the primary limiter.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>