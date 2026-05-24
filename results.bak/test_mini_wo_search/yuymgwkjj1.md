Now I have a thorough understanding of the paper and the review inputs. Let me construct the final consolidated review.

---

## Summary

This paper addresses the well-known likelihood bias in normalizing flows for OOD detection — the tendency of flow models to assign higher likelihoods to low-complexity OOD inputs. The authors propose generating synthetic low-complexity outliers from ID data (via CutPaste/CutMix/MixUp + Gaussian blur for images; sentence truncation + synonym replacement for text) and training with a softplus-based adverse likelihood objective that maximizes ID likelihood while penalizing likelihoods of synthetic outliers. Experiments across image benchmarks (CIFAR, iSUN, SVHN), high-dimensional medical/blur datasets, and text datasets show consistent AUROC improvements over the MLE baseline, with performance comparable to using a limited set of real outliers.

## Strengths

- **Consistent empirical gains across image and text domains with multiple base architectures**: Tables 2, 3, 5, and 6 report AUROC and FPR95 improvements over the MLE baseline across CIFAR-10/100, iSUN, SVHN, LSUN, CelebA, high-dimensional medical/blur datasets (CS-Flow, FastFlow), and text (IMDb/SST-2). The breadth of validation supports the generality of the approach. For instance, on CIFAR-10→SVHN, synthetic outlier training achieves 0.914 AUROC vs. 0.916 for real outliers; on SST-2, AUROC improves from 0.548 to 0.899.

- **Softplus-based OOD objective provides a principled solution to numerical instability without manual thresholding**: Section 2.3 derives the gradient modulation factor p/(1+p) which naturally approaches zero for very low-likelihood outliers. This contrasts favorably with the threshold-clamping approach of Schmier et al. (2022) and is backed by a visual comparison (Figure 1).

- **Transparent evaluation of complexity-adjusted scoring and documentation of its limitations**: The paper reports both raw likelihood and complexity-adjusted scores (Tables 2, 3) and explicitly notes cases where the adjustment is misleading (e.g., CIFAR-10 ID / iSUN OOD), showing awareness of the method's contextual dependencies.

- **Figures 3 and 4 directly visualize the intended bias correction mechanism**: The scatter plots showing the relationship between image complexity and assigned likelihood, before and after synthetic outlier training, provide direct evidence that the method reduces the correlation between low complexity and high likelihood that is the core problem being addressed.

## Weaknesses

### Fatal

None.

### Major

- **Missing experimental comparison against existing outlier-exposure methods for normalizing flows**: The paper cites Outlier Exposure (Hendrycks et al., 2018), VOS (Du et al., 2022), SANFlow (Kim et al., 2023), and others in the introduction (Section 1), yet provides no experimental comparison against any of them. SANFlow is particularly relevant as it also targets normalizing flows with synthetic outliers. The only baselines are "MLE" (no regularization) and "real outliers" (an underspecified variant of OE). Without benchmarking against the most directly comparable prior work, it is impossible to assess whether the proposed synthetic outlier strategy offers an improvement over existing approaches. This is the single most impactful gap in the experimental evaluation.

- **Insufficient ablation and analysis of the synthetic outlier generation pipeline**: The paper compares "Gaussian blur," "CCM" (the three augmentations collectively), and "Gaussian+CCM" as composite conditions, but never ablates the individual augmentations (CutPaste vs. CutMix vs. MixUp). Since the synthetic outlier methodology is a core contribution, isolating which components drive the improvement is essential. Additionally, there is no sensitivity analysis on the Gaussian blur kernel radius (fixed at 1 without justification or exploration) or the 0.5 outlier generation probability. As stated in Section 3.1: "The radius setting of the Gaussian filter is 1" — this single value is used throughout without experimental motivation.

- **The "real outliers" (RO) baseline is critically underspecified**: The paper states in Section 3.1 that RO comprises "10% of the ID data samples," but does not specify which dataset these outliers are drawn from, whether they are the same for all ID/OOD pairs, or how they were sampled. Without knowing whether the real outliers come from iSUN, SVHN, or some other source, the claim that synthetic outliers are "comparable to limited real outliers" is uninterpretable. The reader cannot tell whether this is a weak or strong baseline.

### Minor

- **No statistical variance reported for any result**: All tables report point estimates only. OOD detection metrics (AUROC, FPR95) are known to vary across random seeds, especially with evaluation on 1000 ID + 1000 OOD samples. Standard deviations or confidence intervals are needed for the reader to assess result stability.

- **Text modality experiments are underdeveloped relative to image experiments**: The text outlier generation (sentence truncation to length 20, WordNet synonym replacement) is presented without any analysis of the resulting text complexity (e.g., gzip compression ratio or likelihood correlation). The huge improvement on SST-2 (35.1% AUROC gain from 0.548 to 0.899) suggests the MLE baseline may be particularly weak, but no analysis of the likelihood distributions or complexity-likelihood correlation is provided to confirm that the bias is actually corrected. The text evaluation also uses only one ID dataset (IMDb).

- **Lipschitz constant analysis is correlational and the estimate is coarse**: Table 4 shows that synthetic outlier training increases the estimated Lipschitz constant. However, this is estimated as the maximum gradient norm over only 1000 ID samples — a coarse global approximation that does not capture local behavior on OOD regions. The paper claims this "supports the hypothesis" and "validates" the approach, but does not establish a causal link between the Lipschitz increase and improved OOD discrimination, nor does it show that the change is specific to low-complexity regions.

- **Missing ablation separating the contributions of synthetic outliers vs. the softplus objective**: The high-dimensional experiments (Table 5) compare "original CS-Flow" vs. "CS-Flow + synthetic outliers + dual likelihood" as a combined modification. Without an intermediate ablation (e.g., original method + softplus loss only, without synthetic outliers), the individual contribution of each component cannot be isolated.

- **The softplus objective is presented as a contribution but not ablated against the thresholding alternative it claims to improve upon**: Section 2.3 contrasts the softplus approach with the threshold-based clipping of Schmier et al. (2022), but no experiment directly compares the two. A small ablation would substantiate the claimed advantage.

### Trivial

- None.

## Nice-to-Haves

- Sensitivity analysis on the Gaussian blur kernel radius and the outlier generation probability (currently fixed at 0.5).
- Analysis of the method's computational cost: the dual likelihood requires forward passes for both ID and synthetic outliers per batch, roughly doubling computation.
- Discussion of whether the method scales to deeper flow architectures (experiments use 8 coupling layers).
- Analysis of failure cases, e.g., when ID and OOD have similar complexity.

## Removed Points

These points are flagged for removal. Treat them with caution.

1. **"Table 2 and 3 appear as images, so I cannot verify the exact numbers"** — This is a parser artifact from PDF extraction; the original submission's tables are not images.
2. **"Code release is not mentioned"** — Nitpick about reproducibility; code availability is a non-binding convention, not a requirement for evaluating a conference submission.
3. **"No analysis of failure cases"** — Generic; not a specific weakness of this paper.
4. **"Section 2.1 logical chain is unclear — conflates properties of a fixed model with changes across training"** — This criticism partially misinterprets the paper. Remark 2 states that *within a fixed model*, L_A increases as complexity decreases. The paper's argument is about how *training with* low-complexity synthetic outliers changes the model's L_A. The causal direction is distinct and the paper's framing is reasonable, though the connection could be stated more explicitly.
5. **"Theory in Osada et al. (2024) relates the Lipschitz constant to the complexity of the input under the model, not as a training objective"** — The paper does not claim the theory directly predicts the training effect; it uses the increase in L_A as supporting evidence, not as a proof. The criticism overstates the paper's claim.

## Novel Insights

The most distinctive finding to emerge across the two reviews is the tension between the paper's strong, consistent empirical results (improvements hold across CIFAR, iSUN, medical X-ray, blur images, and text) and the underdeveloped experimental grounding. The empirical pattern is clear and replicated across modalities — training on synthetic low-complexity outliers consistently improves OOD detection — but the mechanism remains underspecified. The harsh critic correctly identifies that the Lipschitz analysis is correlational rather than causal, and the ablation is incomplete. A concrete example: the paper shows that the bias is "corrected" in the complexity-vs-likelihood scatter plots (Figure 3), but does not quantify the residual correlation after training, nor does it compare the magnitude of correction against a method like SANFlow which was explicitly designed for the same problem. The strength finder's observation that complexity-adjusted scoring limitations are honestly documented is noteworthy — most papers would only report the version that looks best, but this paper reports both and flags the caveat. The weakness that most limits the paper's impact is not any technical flaw in the method, but the lack of a controlled comparison against the closest prior work, which would establish whether the proposed synthetic outlier strategy is a meaningful advance or simply reinventing outlier exposure for flows.

## Suggestions

1. **Add direct experimental comparison to SANFlow** (Kim et al., 2023) and preferably also OE with a standard OOD dataset (e.g., 80M Tiny Images or a curated set). This is necessary to establish the contribution relative to prior work.
2. **Specify the real outliers baseline**: state which dataset the 10% outliers are drawn from, and consider adding a stronger baseline (e.g., a large, diverse OOD dataset) to give the "comparable" claim meaningful context.
3. **Ablate the synthetic outlier generation components**: test CutPaste alone, CutMix alone, MixUp alone, and each with/without Gaussian blur. Add sensitivity analysis on blur kernel radius and outlier generation probability.
4. **Report standard deviations** across at least 3 random seeds for all main tables.
5. **Add an ablation in the high-dimensional experiments** (Table 5) separating the softplus objective from the synthetic outliers.
6. **For the text experiments, provide complexity analysis** (e.g., gzip compression ratio of synthetic vs. real text) and likelihood distribution plots to confirm the bias is being corrected.

## Score and Decision

The paper tackles a real problem and the core idea — training normalizing flows on synthetic low-complexity outliers to correct the likelihood bias — is sensible and supported by consistent empirical results across multiple domains. The softplus objective is a clean technical contribution. However, the experimental evaluation has two significant gaps: (1) no comparison against the most directly relevant prior methods (SANFlow, OE), making it impossible to assess whether the contribution is a meaningful advance, and (2) insufficient ablation of the synthetic outlier generation pipeline, which is central to the claimed contribution. These gaps prevent acceptance at a top venue in the current form. With revision addressing these comparisons and ablations, the paper could make a solid contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>