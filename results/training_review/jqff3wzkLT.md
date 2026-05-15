Now I have all the information I need. Let me produce the consolidated review.

## Summary

The paper introduces Variance-Covariance Regularization (VCReg), which adapts the variance and covariance losses from the self-supervised VICReg method to supervised learning by removing the invariance term and extending regularization to intermediate network layers. Through experiments on image and video transfer learning, long-tail classification, self-supervised learning, and hierarchical classification, the paper claims state-of-the-art performance and links VCReg's benefits to mitigating gradient starvation, neural collapse, and information compression.

## Strengths

- **Principled adaptation of self-supervised regularization to supervised learning.** The paper makes a clean modification to VICReg (removing the invariance term) and extends it to intermediate representations (Section 3.2), with practical engineering contributions including a spatial-location sampling strategy and a smooth L1 penalty for robustness. This is well-motivated and straightforward to implement.

- **Broad evaluation across architectures, modalities, and learning paradigms.** The experiments span ResNet-50, ConvNeXt-T, ViT-B/32 (images), VideoMAE/VideoMAEv2/ViViT (video), and settings including supervised transfer, self-supervised learning, long-tail learning, and hierarchical classification (Tables 1–5). This breadth supports the claim of broad applicability.

- **Consistent improvements across nearly all settings.** VCReg improves results in 8/8 downstream image datasets for ResNet-50, all 5 video backbones, both long-tail datasets, and all 6 hierarchical classification datasets. The direction of improvement is consistent even when magnitude varies.

- **Computational efficiency claim.** The fast backward-pass implementation claims ~5× speedup over naive VCReg with latency comparable to batch normalization (Section 3.3), addressing a practical concern for adoption.

## Weaknesses

### Fatal
None.

### Major

- **Asymmetric gains across architectures raise concerns about baseline quality.** VCReg yields dramatically larger gains on ResNet-50 (+5.63 pp average, driven by Cars +10.5 pp, Aircraft +15.7 pp, Flowers +10.9 pp) than on ConvNeXt-T (+0.96 pp) or ViT-B/32 (+0.99 pp). This asymmetry is consistent with the hypothesis that the ResNet-50 baseline is under-optimized and VCReg's effect is partially conflated with fixing that configuration. The paper states it uses "standard PyTorch recipes" (line 140), but the resulting ResNet-50 linear probing numbers (e.g., Cars 43.6%, Flowers 77.1%) are substantially below commonly reported ranges, making it difficult to disentangle VCReg's specific contribution from general training improvement. The core claim of "state-of-the-art performance" rests on comparisons against these baselines and is not convincingly supported without verification that the baselines are competitive with published practice.

- **Neural collapse analysis contains an internal inconsistency.** Table 6 reports NCC values of 0.99 (baseline) and 0.81 (VCReg), with a caption stating "Higher values in each metric for the VCReg model indicate reduced neural collapse." Since VCReg produces a *lower* NCC value, either (a) the caption is wrong about the direction of interpretation, (b) NCC is not an accuracy metric and the values mean something else, or (c) the computation is flawed. Additionally, the model achieves >60% linear probing accuracy, which is incompatible with 99% NCC error if NCC is error rate. The paper does not clarify what NCC numerically represents, and the CDNV/MI metrics lack experimental protocol details (dataset, number of classes, number of samples). This section does not provide credible evidence for the claimed mechanism.

- **No error bars or statistical significance reported for any experiment.** Every table reports single-run point estimates. Given that several reported gains are small (video: 0.3–0.8 pp; VICReg+VCReg: ~1 pp; long-tail: 1.6–3.0 pp; SSL: 1–2 pp), these could plausibly lie within run-to-run variation. Without multiple seeds or confidence intervals, the reader cannot assess whether improvements are robust or noise.

### Minor

- **Hyperparameter tuning is asymmetric.** For the video experiments, a grid search was performed to find optimal VCReg coefficients based on validation accuracy (line 175). For the image experiments comparing against DeCov and WLD-Reg, baseline regularizer hyperparameters were simply "sourced from [prior work]" (line 143) without adaptation. For the main VCReg-vs-baseline comparison in images, no hyperparameter search procedure is reported, though VCReg introduces at least three new hyperparameters (α, β, δ). While some asymmetry is unavoidable for a new method, the lack of sensitivity analysis or evidence that VCReg's advantage is robust to hyperparameter choices weakens the results.

- **Intermediate-layer application is not specified for the main supervised experiments.** Section 3.2 argues that extending VCReg to intermediate layers is crucial, but the supervised image transfer experiments (Table 1) never state whether VCReg was applied to intermediate layers, and if so, to which layers or how many. The video experiments explicitly use final-layer-only VCReg (line 175). The SSL experiments use intermediate VCReg (line 235). Without this detail for the main results, the central methodological claim about intermediate-layer regularization is incompletely specified.

- **Gradient starvation analysis is purely qualitative.** The two-moon experiment (Figure 2) shows a visual improvement, but no quantitative metric of gradient starvation (e.g., gradient norm histograms, rank of gradient matrix) is provided. Any well-tuned regularizer could produce similar visual effects.

### Trivial
None.

## Nice-to-Haves
- An ablation study comparing intermediate-layer vs. final-layer-only VCReg on one image dataset (e.g., ImageNet→Cars) would substantially strengthen the paper's central methodological claim.
- A hyperparameter sensitivity analysis for α, β, δ over a reasonable range would demonstrate robustness.
- Comparison against standard long-tail techniques (class-balanced sampling, re-weighting) in the long-tail experiments would better situate VCReg's contribution.

## Removed Points

The following points from the reviewers are removed as per policy:

- **"Does not cite recent supervised decorrelation methods"** — Per policy, missing related works should not be cited as a weakness.
- **"No comparison to standard long-tail techniques"** — Scope creep; the paper investigates VCReg's applicability, not state-of-the-art in long-tail learning.
- **"Standard superclass-trained ResNet on CIFAR-100 typically reaches ~65-68% subclass accuracy"** — The paper uses ConvNeXt, not ResNet, for these experiments; the claim is unfounded.
- **"The method is applied exclusively to the final output... contradicting the method section's emphasis on intermediate layers"** — The paper explicitly states this as a design choice "for simplicity" (line 175); there is no contradiction.
- **"Speedup claims (Table ? — not present) cannot be verified"** — Table ta:time exists in the original submission's appendix (stripped by parser); per policy, missing appendix content is not a valid weakness.
- **"VCReg is applied to intermediate representations here (unlike the supervised experiments), making the set of experiments inconsistent"** — Different experiments may use different configurations; this is noted transparently in the paper and is not an inconsistency.
- **"Missing experiments: ablation of intermediate vs. final-only VCReg"** — Valid as a nice-to-have but not a weakness; moved accordingly.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: VCReg's gains are largest on the weakest baseline (ResNet-50) and much smaller on stronger architectures (ConvNeXt, ViT). This pattern — if confirmed by properly controlled experiments — would shift the paper's claimed contribution from "state-of-the-art transfer learning" to "a regularizer that helps most when the baseline training is suboptimal," which is a materially different claim. The NCC inconsistency in Table 6 further weakens the mechanistic story connecting VCReg to neural collapse. A rigorous rebuttal would need to address both the baseline quality issue and the metric confusion.

## Suggestions

1. **Retrain the ResNet-50 baseline with stronger hyperparameters** (e.g., longer training, better learning rate schedule) to match commonly reported linear probing numbers, then re-evaluate VCReg's gains. If the gains shrink to ~1 pp (matching ConvNeXt/ViT), the paper's claims need to be recalibrated. If they remain large, the asymmetry warrants a dedicated analysis.

2. **Clarify the NCC metric**: explicitly state whether Table 6 reports accuracy, error rate, or some normalized score, and reconcile the reported values with the linear probing performance of the same model. Provide experimental details (dataset, classes, protocol).

3. **Report mean ± std over 3–5 seeds** for all experiments, particularly those with small gains (video, SSL, long-tail).

4. **Disclose which layers were used** for intermediate VCReg in the supervised image experiments, or add an ablation comparing intermediate vs. final-only on one dataset.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>