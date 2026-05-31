I now have a thorough understanding of the paper and all reviewer claims. Let me write the consolidated review.

## Summary

This paper investigates diffusion models for unsupervised and semi-supervised anomaly detection on the ADBench benchmark (57 datasets). The authors observe that DDPM is competitive but computationally expensive for inference, and propose Diffusion Time Estimation (DTE), which estimates the posterior distribution over diffusion time (or noise variance) for a given input and uses its mode/mean as the anomaly score. The paper derives an analytical form for this posterior (approximately inverse Gamma), develops a non-parametric estimator that connects to kNN, and introduces parametric neural network variants (inverse Gamma and categorical) for fast inference. DTE achieves competitive AUC-ROC while being orders of magnitude faster than DDPM at inference time.

## Strengths

- **Dramatically faster inference than DDPM while matching or exceeding its performance**: Figure 1 plots average inference time vs. average AUC-ROC across all 57 ADBench datasets. DTE (Categorical) sits in the lower-right corner (fastest inference and highest AUC among diffusion methods), whereas DDPM is much slower with lower AUC. This directly supports the paper's central practical claim.

- **Theoretical derivation connecting diffusion time to the inverse Gamma distribution**: Section 3.1 derives the posterior \(p(\sigma^2_t \mid \mathbf{x}_s)\) for a single point at the origin as an inverse Gamma, and extends this to the dataset case using a log-sum-exp approximation (Eq. 5). This provides a principled starting point for interpreting diffusion-based anomaly scoring and motivates both the non-parametric and parametric approaches.

- **Comprehensive evaluation across 57 ADBench datasets with diverse baselines**: Figure 2 reports AUC-ROC means and standard deviations over five seeds for both semi-supervised and unsupervised settings, comparing DTE against 12 classical methods, 5 deep-learning baselines, and DDPM. The evaluation covers tabular, image, and natural language data.

- **Categorical model demonstrably reduces bias in diffusion-time prediction**: Figure 3 compares inverse Gamma, Gaussian, and categorical models across four datasets. The categorical model (7 bins) shows substantially less bias across the full timestep range (0–300) than the analytically-derived inverse Gamma model, which suffers from high bias at larger timesteps. This demonstrates a practical improvement over the parametric family suggested by theory.

- **Investigation of representation choice for image data**: Section 4 studies how different embedding types (raw pixels, pre-trained classification embeddings, self-supervised embeddings, fine-tuned embeddings) affect anomaly detection performance for DDPM, kNN, and DTE, providing practical guidance for applying diffusion-based methods to high-dimensional visual data.

## Weaknesses

### Fatal

None.

### Major

- **Overclaimed equivalence between non-parametric DTE and kNN rankings**: The paper states three times (lines 33, 182, 269) that the non-parametric DTE and kNN produce "identical" anomaly rankings. DTE uses the **average** distance to k-nearest neighbours (Eq. 6), while the kNN variant it compares to uses the **distance to the kth** nearest neighbour. The ordering induced by the mean of a set is not identical to the ordering induced by its maximum (or kth-largest) element in general — a simple counterexample demonstrates they can differ. The paper provides no proof of equivalence under any condition, nor does it report empirical rank correlation to support the claim. This is a factual inaccuracy that should be corrected. (The core contribution of DTE — fast and competitive anomaly detection — does not depend on this claim, but the claim as written is misleading.)

### Minor

- **"Significantly outperforming" claim lacks formal statistical support**: Line 245 states "our method outperforms all previous deep learning-based approaches in both settings significantly." The evidence consists of box plots (Fig. 2) showing mean AUC-ROC with standard deviations across 57 datasets. While DTE's mean is notably higher than most deep baselines, no formal significance test (e.g., Wilcoxon signed-rank test across datasets, critical difference diagram) is reported. Error bars overlap for several comparisons, and the paper does not rule out that performance differences could partly reflect variance. This is fixable with post-hoc analysis and does not undermine the paper's core contribution — the observed gap is substantial enough to be plausible — but the claim is stronger than the evidence currently supports.

- **Missing quantitative analysis of the DTE–kNN relationship**: Beyond the unsupported "identical rankings" claim, the paper does not provide any empirical measure (e.g., Spearman rank correlation across datasets, overlap in top-k anomalies) of how DTE's scores relate to kNN's scores. Since the connection to kNN is presented as a key insight, empirical quantification would strengthen this narrative and could replace the overclaimed identity.

### Trivial

None.

## Nice-to-Haves

- Add a critical difference diagram or Wilcoxon signed-rank test to formally compare methods across datasets, strengthening the significance claim.
- Report rank correlation (Spearman or Kendall) between DTE scores and kNN scores on ADBench datasets to substantiate the claimed connection.
- Include an ablation study on the number of bins in the categorical model in the main text (or reference it clearly if it already exists in the appendix).
- Add a brief discussion in the main text of training time / GPU hours for DTE across the benchmark (presently deferred to appendix).
- Identify datasets where DTE performs relatively poorly to give insight into method limitations.

## Removed Points

*These points were flagged to be removed; treat them with caution.*

- **Strength from Strength Finder #3 ("Non-parametric DTE yields same anomaly ranking as kNN")**: Removed because it conflicts with the verified Major weakness above — the claimed identity is not generally true and is unsupported.
- **Harsh critic's point about inverse Gamma training objective conflating conditionals**: The paper clearly acknowledges its approximations (lines 165, 171, 224) and trains the inverse Gamma model via standard MLE using the analytically motivated parametric family. The training loss (Eq. 4) directly follows from the inverse Gamma likelihood. This is a reasonable modeling approach, not an over-interpretation. Removed as factually inaccurate criticism.
- **Generic "the evaluation lacks rigor" / "could the metric be measuring a proxy?" style concerns**: These are area-of-concern sweeps without specific anchors in the paper text. Removed per filtering discipline.
- **Missing related works (DSVDD variants, CSI, SSD)**: Per instructions, missing related works are not permissible as weaknesses since I cannot verify their publication status from external sources.
- **Formatting/style nitpicks**: Per instructions, pure formatting issues from PDF parsing are excluded.

## Novel Insights

The two reviews together surface a clear pattern: the paper's core empirical contribution is solid (DTE is fast and competitive), but its weakest points are all about *framing* — claiming more than the evidence supports. The "identical rankings" claim and the "significantly outperforms" claim are both instances of the paper making strong categorical statements where the actual contribution (empirical competitiveness + fast inference) stands perfectly well on its own without them. The most useful insight from the review synthesis is that the paper would be *stronger*, not weaker, by backing off both claims: replacing "identical" with "strongly related" (with empirical rank correlation to show it), and replacing "significantly outperforms" with "achieves higher mean AUC" (with a statistical test for those who want it). The inverse Gamma training criticism, by contrast, is a misreading — the paper's derivation-to-model pipeline is standard and clearly scoped.

## Suggestions

1. Correct the "identical rankings" claim to something empirically defensible: either report Spearman rank correlation between DTE and kNN across ADBench datasets, or state the more precise relationship (e.g., "the non-parametric DTE uses a similar distance-based principle as kNN").
2. Add a formal statistical comparison (Wilcoxon signed-rank test or Nemenyi post-hoc) across the 57 datasets to support the claim of outperforming deep baselines.
3. Include empirical rank-correlation analysis of the DTE–kNN relationship in the main results.

## Score and Decision

This paper makes a genuine contribution: it proposes a principled, fast diffusion-inspired anomaly detector that achieves competitive results across a large, diverse benchmark while being orders of magnitude faster than DDPM at inference. The evaluation is extensive, the core idea (estimating diffusion time as a proxy for anomaly score) is novel and well-motivated, and the practical value is clear. The main weaknesses are overclaims in framing rather than structural flaws in the method or experiments — both can be corrected without changing the substance. The paper's contributions are significant enough to warrant acceptance.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>