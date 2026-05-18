Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper studies how model robustness behaves across different *degrees* of the same distribution shift type — an overlooked dimension in OOD generalization evaluation. Through experiments on NoisyMNIST, RotatedMNIST, LowLightCIFAR10, and ImageNet variants, the authors show that (1) models performing best under mild shifts can collapse under only slightly stronger shifts, (2) training on strong shifts does not guarantee robustness to milder shifts (and can even hurt), and (3) large-scale pre-trained models like CLIP can be surprisingly brittle to downstream distribution shifts that are rare in pre-training data.

## Strengths

- **Non-trivial empirical finding: best-at-one-degree ≠ robust-at-adjacent-degree.** Figure 2 (left) and Table 1 show that for NoisyMNIST and LowLightCIFAR10, models selected for top performance at D₄ drop sharply (e.g., 10%+ from D₄→D₅) at the next degree. The per-algorithm breakdown in Table 1 further confirms this pattern is not an artifact of a single selection criterion — VREx with a ResNet-50 drops 50.3% from D₄→D₅ and 73.1% from D₄→D₆. This directly supports the paper's core claim that single-degree evaluations can be misleading.

- **Non-obvious asymmetry: robustness at high degrees does not imply robustness at low degrees.** Section 4.3 shows that on RotatedMNIST and (partially) LowLightCIFAR10, models trained on strongly shifted data actually *underperform* models trained only on clean data when evaluated under mild shifts. This is counterintuitive and practically important — it means collecting strongly shifted training data is not a panacea.

- **CLIP brittleness under novel distribution shifts is demonstrated with concrete evidence.** Figure 5 shows CLIP adapted via linear probing on clean NoisyMNIST drops >40% more than a randomly initialized model when moving from D₀→D₁ on ResNet-50. The fact that this effect reverses for rotation (a shift better covered by CLIP's training data) provides a coherent explanation: pre-training coverage matters.

- **Multi-dataset, multi-architecture validation strengthens generality.** The paper tests across CNN, ResNet-50, EfficientNet-b0, ViT-B/32, on 5 datasets (3 synthetic + 2 ImageNet subsets), and compares ERM with >20 DG algorithms including VREx, IRM, Mixup, and CAD. The consistent pattern — brittleness across degrees — holds across this diversity.

## Weaknesses

### Fatal
None.

### Major
- **The model selection procedure in Figure 2 (left) conflates brittleness with selection-induced regression.** Selecting the top-5 models at each domain and then plotting those same models' performance at other domains almost guarantees a "collapse" pattern — this is the well-known phenomenon that models optimized for one operating point need not generalize to neighboring ones. While the paper's conclusion may still be correct, this particular plot is not clean evidence of brittleness. The per-algorithm results (Table 1, Figure 2 right panel) are less affected by this issue and provide better support. The authors should reframe or replace the left panel of Figure 2 with a less selection-biased analysis (e.g., showing average performance per algorithm, or the best model selected by a held-out degree).

- **LowLightCIFAR10 is under-specified.** The paper describes this dataset only as a "combination of brightness and shot-noise intensity" (line 127) without providing the exact parameters for each degree, how many degrees exist, or whether the degrees are perceptually uniform. Since one of the paper's three key empirical findings on brittleness (the "higher-to-lower" asymmetric pattern) depends critically on this dataset, the missing specification is a reproducibility gap that undermines confidence in those results. The authors should provide the full construction details.

### Minor
- **The CLIP experiment uses only linear probing, not fine-tuning.** The paper acknowledges this is by design ("following Radford et al., 2021"), but the claim that "CLIP models are sensitive to minute distribution shifts" (line 9) is then limited to the linear probing adaptation protocol. The authors' own \comment{} (lines 310–313) suggests fine-tuning gives different results, so the scope of the conclusion should be explicitly caveated in the main text.
- **The hypothesis about pre-training data coverage driving CLIP brittleness is asserted but not tested.** The paper suggests that Gaussian noise brittleness arises because noise is "rare in the pre-training data" (line 295), and supports this by contrast with rotation (more common in pre-training). But this remains a post-hoc explanation — no direct test (e.g., comparing to a model pre-trained on noisy data, or quantifying noise prevalence in CLIP's training set) is provided.
- **No statistical uncertainty estimates for key comparisons.** Many results are reported as point estimates (e.g., "more than 10% drop" in line 162). While Table 1 includes standard deviations and the pre-trained experiments use 3 runs, the Figure 2 left panel and Figure 4 results lack error bars or confidence intervals.

### Trivial
None.

## Nice-to-Haves
- Including fine-tuning results for CLIP (as the authors' preliminary experiments suggest) would significantly strengthen the pre-trained model analysis.
- The GradCAM analysis (Figure 3) is qualitative and for only two models; a quantitative feature-importance analysis across more models would add depth.
- A discussion of how the "degree" concept applies to natural (non-synthetic) distribution shifts where ordering may not be monotonic would improve the paper's honesty about scope limitations.

## Removed Points

- **"Missing algorithm descriptions and hyperparameter details"** — The paper's "Algorithms" header at line 131 appears to be a parser artifact (empty in extracted text). Table 1 names 8 representative DG algorithms, and the paper mentions "more than 20 DG algorithms." Hyperparameter details are typically relegated to appendix, which the parser strips. The paper provides enough information to understand the experimental design. [Removed per Hard Rule 9: parser-stripped content and nitpicking about trivial implementation details.]

- **"Missing 'Algorithms' subsection makes the paper irreproducible"** — Same as above. The algorithms are named in the text and Table 1. This is a parser artifact. [Removed per Hard Rule 9.]

- **"The paper should fix the model selection — show the best model overall or the typical model"** — The right panel of Figure 2 and Table 1 already provide the per-algorithm aggregation that the critic asks for. The left panel is one piece of evidence among several. Keeping it as a weakness would create a double standard (criticizing one plot while the others already address the concern). [Removed because the paper already partially addresses this via converging evidence in Table 1 and Figure 2 right panel.]

- **"The introduction claim about most benchmarks having fixed degree is too broad"** — This is a scope nitpick. The paper's claim is about "most benchmarks" exhibiting a "largely fixed degree" — this is factually true of standard DG benchmarks like DomainBed, WILDS, etc. [Removed per Hard Rule 5: style/subjective nitpick.]

- **"No analysis of variance or statistical tests"** — Table 1 already includes standard deviations. For an empirical analysis paper of this type, significance testing is not standard practice. [Removed per Soft Rule: methodology not standard in this setting.]

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Reframe Figure 2 (left).** Either replace it with per-algorithm averages (which already exist in the right panel) or re-analyze by showing that the *same model* selected via unbiased criterion (e.g., validation on held-out degree) also exhibits brittleness. This would silence the selection-artifact concern.
2. **Fully specify LowLightCIFAR10** — provide the exact parameters for brightness and shot-noise intensity at each degree, and the number of degrees used.
3. **Add error bars or confidence bands** to all point-estimate figures to help readers assess the reliability of observed patterns.
4. **Caveat the CLIP claim** in the abstract/introduction to specify that the brittleness is observed under linear probing adaptation, and that fine-tuning may behave differently.

## Score and Decision

**Calibration anchors used:**

| Path | Avg. Human Score | Comparison |
|------|:---:|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TPZRq4FALB.md` | 8.0 | Stronger paper — proposes a novel method + benchmarks for multi-modal TTA. Our paper is an empirical analysis only, with no new method. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KbetDM33YG.md` | 8.0 | Stronger paper — proposes a novel evaluation problem + metric for GNNs. Our paper makes observational contributions without a new technical framework. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pw2ssoOTpo.md` | 6.5 | Comparable — both are analysis/benchmark papers. CIFAR-10-Warehouse has more extensive benchmarking but less conceptual insight about degrees of shift. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/VTYg5ykEGS.md` | 6.5 | Comparable — both perform analysis that challenges existing evaluation practices. ImageNet-OOD has a dataset contribution; our paper has the multi-degree insight. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LixGd92Wri.md` | 5.67 | Slightly weaker — a benchmark with inconsistent execution and reviewer disagreement. Our paper has a cleaner, more focused thesis. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/it1zuzw7KF.md` | 4.0 | Much weaker — flawed experimental design and unclear contributions. Our paper has more rigorous methodology and clearer findings. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7LZjuA4AB2.md` | 3.0 | Much weaker — flawed experiments, unclear definitions, and weak theoretical grounding. Our paper's empirical observations are better-supported. |

Relative to these anchors, this paper is a solid empirical contribution with genuine insights, but has one consequential methodological weakness (the model selection procedure conflating multiple effects) and one reproducibility gap (LowLightCIFAR10 under-specified). These issues are addressable but non-trivial. The paper sits between the 6.5-level analysis papers (which have cleaner execution) and the stronger methods papers (8.0).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>