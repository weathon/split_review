Now I have all the information I need. Let me compile the final consolidated review.

---

## Summary

This paper compares Vision Transformer (ViT B32) with five CNN architectures (ResNet50, VGG16, InceptionV3, MobileNetV2, EfficientNetB0) on face identification and verification tasks across five datasets (VGGFace2, LFW, ROF, SCface, UPM-GTI-Face). It reports that ViT achieves higher accuracy on face identification, shows greater robustness to distance variation and occlusions, and has competitive inference speed. The paper provides a useful structured comparison but is weakened by unsupported claims, experimental design choices that may disadvantage the CNN baselines, and a mismatch between the scope of its conclusions and the baselines it compares against.

## Strengths

- **Quantified robustness to distance and occlusions**: The paper provides clear empirical evidence on the SCface dataset that ViT achieves meaningfully higher AUC than the CNNs at medium and long distances (Figure 4a,b), and on the ROF dataset that ViT handles both mask and sunglass occlusions better (Figure 5b–d). These results directly support the claim that ViT embeddings are more resilient to these real-world challenges.

- **Competitive inference speed with higher accuracy**: Table 2 shows ViT achieves the top test accuracy (99.18%) and 100% top-5 accuracy, while its inference time (0.26 sec/batch) is only 23.81% slower than the fastest CNN (MobileNet at 0.21 sec/batch), despite having 7× the parameters. This is a concretely measured trade-off.

- **Diverse, purpose-selected evaluation datasets**: The study uses five datasets that isolate distinct challenges — occlusions (ROF), distance and surveillance quality (SCface, UPM-GTI-Face), unconstrained conditions (LFW), and large-scale training (VGGFace2) — providing a reasonably broad evaluation framework.

- **Public code and data splits**: The paper states that the implementation and data splits are publicly available, supporting reproducibility.

## Weaknesses

### Fatal
None.

### Major

1. **Unsupported central claim about memory footprint**: The abstract and conclusion state that ViT has a "smaller memory footprint" than CNNs, yet the paper provides zero empirical measurements of GPU memory consumption, peak memory usage, or maximum batch size. Section 2.1 makes a qualitative argument comparing activation maps to tokens, but §3.4 reports only parameter counts and inference time — memory is never quantified. Given that this claim appears in the title-level framing and conclusion, its complete lack of experimental support is a significant gap.

2. **Uniform hyperparameters that may systematically disadvantage CNNs**: All six models are trained with the same optimizer (Adam, lr=0.0001), batch size (256), and for only 25 epochs. The paper acknowledges in §3 that "networks might indeed perform optimally with distinct hyperparameter settings tailored to their unique requirements," but then proceeds to draw strong conclusions about ViT superiority (abstract, conclusion) without testing whether these conclusions hold under settings better suited to the CNNs (e.g., SGD+momentum, learning rate schedules, longer training). Since the chosen settings are close to standard for ViT but atypical for many CNNs in face recognition, the results do not establish that ViT *outperforms* CNNs in general — only that it does so under this specific, potentially unfavorable configuration.

3. **Overclaimed scope relative to the baselines used**: The paper claims that ViT "outperforms CNNs for face recognition" but compares against generic image-classification backbones (ResNet50, VGG16, InceptionV3, MobileNetV2, EfficientNetB0) trained with vanilla softmax — not against standard face-recognition pipelines (e.g., ResNet+ArcFace, CosFace, FaceNet). The paper itself mentions ArcFace and CosFace as related work in §2 but does not use them. While the paper's scope is stated as comparing standard architectures, the conclusions are phrased as general claims about face recognition performance, which overstate what the experimental design can support.

### Minor

1. **Validation accuracy exceeding training accuracy is unexplained**: Table 1 shows ViT achieving 99.81% validation accuracy vs. 98.86% training accuracy (the "highest values obtained" during training). The paper interprets this as evidence that "overfitting has not occurred," but does not explain why validation systematically exceeds training — an unusual pattern that could stem from data distribution differences, regularization effects, or the metric being the *peak* at different epochs, none of which are analyzed. While not invalidating the results, the phenomenon warrants a clear explanation.

2. **UPM-GTI-Face dataset is too small to support distance-robustness claims**: This dataset contains only 11 subjects (484 images). The paper uses it to claim ViT maintains AUC 0.63 at 30 m while CNNs drop to 0.5. With 11 subjects, a single subject's embeddings can dominate aggregate metrics, and no confidence intervals or variance measures are reported. The SCface results (130 subjects) are more reliable; the UPM-GTI-Face findings should be treated as illustrative.

3. **No statistical rigor on small datasets**: ROC curves (Figures 4–7) are presented without confidence bands, and key metrics (accuracy, AUC) are reported as point estimates without standard deviations or significance tests. On the small datasets (ROF has 47 subjects with three categories; UPM-GTI-Face has 11 subjects), reported differences may be within noise.

4. **Marginal differences on LFW are treated as significant**: Figure 3 shows that all six networks achieve nearly perfect AUC/EER on LFW (a saturated benchmark). The paper highlights ViT's "slightly superior performance," but the differences are minuscule and no significance test is performed.

5. **Inference time measurement lacks detail**: Table 2 reports inference time per batch as a single number per model. It is not specified whether this is an average over multiple runs, whether preprocessing or I/O is included, or what the variance is.

### Trivial

- The VGGFace2 split numbers are inconsistent: 5% of 3.31M is ~165,500, but the paper reports 157,000 for both validation and test splits. The training split is reported as 2.83M rather than ~2.98M (90% of 3.31M).

## Nice-to-Haves

- Memory footprint measurements (peak GPU memory during training with the same batch size, or maximum batch size for each model under an OOM constraint).
- A broader hyperparameter search or, alternatively, per-model tuning with justification.
- Comparison against at least one modern face-recognition pipeline (e.g., a pretrained ResNet+ArcFace or FaceNet) to calibrate where the standard architectures fall relative to the face-specialized state of the art.
- Confidence intervals or standard deviations on all reported metrics, especially for small datasets.
- t-SNE/UMAP embedding visualizations to illustrate the intra/inter-class variance discussion.
- Ablation on ViT patch size (e.g., ViT B16) to explore sensitivity.

## Removed Points

These points were flagged by reviewers but removed or filtered per policy:

- **"Fair, controlled experimental setup" (Strength Finder)**: This strength — praising uniform hyperparameters as fair — directly conflicts with the verified major weakness that uniform hyperparameters may disadvantage CNNs. Per policy, when a strength and weakness disagree, the weakness wins. Removed.
- **"Diagnostic analysis of overfitting" (Strength Finder)**: The paper's interpretation of the validation > training phenomenon as simply "no overfitting" is precisely what the verified minor weakness (#1 under Minor) questions. The observation itself is noted in the weakness section rather than presented as an unqualified strength. Removed.
- **"Missing related works"**: Per policy, not included because I cannot independently confirm related work gaps.
- **Formatting/style/typo nitpicks**: Parser artifacts, not author errors.
- **Criticisms about reproducibility of cited models/tools/benchmarks**: Per policy, all cited entities are assumed to exist and be released.

## Novel Insights

The reviews surface a tension not fully discussed in the paper: the very design choice intended to make the comparison "fair" — uniform hyperparameters — is itself a source of unfairness, because CNNs and ViTs respond differently to optimizer choice, learning rate, and training length. This is a recurring challenge in cross-architecture comparisons: controlling for architecture while holding hyperparameters fixed conflates architectural merit with hyperparameter sensitivity. The paper's results on distance robustness (SCface) are less affected by this confound than its accuracy results (VGGFace2, LFW), because the distance experiments test representations learned under *these* training conditions rather than claiming globally optimal performance. The memory-footprint claim is the most easily addressable gap: it requires only a simple measurement, not a new experiment.

## Suggestions

1. **Add memory footprint measurements**: Report peak GPU memory during forward-backward pass for each model at the same batch size, or report the maximum batch size each model can sustain before OOM. This directly fixes the most glaring unsupported claim.
2. **Either tune per model or broaden the HP sweep**: If the claim is about ViT's *inherent* superiority, show that the advantage persists when each model is given near-optimal settings. At minimum, try a second optimizer (SGD) or a longer training schedule to demonstrate that the main results are not artifacts of the chosen configuration.
3. **Tighten the language in abstract and conclusion**: Qualify "outperforms CNNs for face recognition" to reflect that the comparison is against standard image-classification backbones with softmax loss, not face-specialized pipelines. The distance and occlusion robustness findings are the paper's strongest contribution and do not need overclaiming.
4. **Provide confidence intervals or error bars** on ROC curves and key metrics, especially on the small datasets (ROF, UPM-GTI-Face), to give readers a sense of variability.

---

## Score and Decision

**Originality**: Modest — the paper applies a known comparison (ViT vs. CNNs) to the face recognition domain with a reasonable set of datasets, but the experimental insights are incremental.  
**Importance of research question**: Good — understanding whether ViTs are suitable for face recognition is practically relevant.  
**Claims well-supported**: Partially. The distance/occlusion robustness claims are reasonably supported; the accuracy superiority and memory-footprint claims are not adequately supported.  
**Soundness of experiments**: The evaluation framework (five datasets, two tasks) is well-structured, but the uniform-hyperparameter design and absence of memory measurements undermine the conclusions.  
**Clarity of writing**: Adequate. The paper is clearly structured and readable.  
**Value to the research community**: Moderate — the distance and occlusion comparisons are useful reference points, but the paper would need stronger experimental grounding to be a definitive reference.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>