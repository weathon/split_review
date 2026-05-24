Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper introduces the concept of "calibration attacks" — adversarial examples designed to degrade a model's calibration (confidence reliability) while preserving its prediction accuracy, making the attacks stealthy. The paper proposes four attack types (underconfidence, overconfidence, maximum miscalibration, and random confidence attacks), evaluates them on ResNet-50 and Vision Transformer across three image datasets (CIFAR-100, Caltech-101, GTSRB), analyzes their detectability, and proposes two defenses (Compression Scaling and Calibration Attack Adversarial Training).

## Strengths

- **First systematic framework for calibration-targeting attacks**: The paper is, to the best of my knowledge, the first to comprehensively study adversarial attacks that aim specifically to miscalibrate a model while preserving accuracy, including a taxonomy of four distinct attack types (Section 3.2). This fills a genuine gap: prior adversarial attack work focuses almost exclusively on misclassification, not calibration degradation.

- **Comprehensive empirical evaluation across multiple architectures and datasets**: The attacks are tested on both convolutional (ResNet-50) and transformer (ViT) architectures across three datasets (CIFAR-100, Caltech-101, GTSRB) in both black-box (Square Attack-based) and white-box (PGD-based) settings (Section 4, Table 1). Results show that calibration attacks can increase ECE and KS error by over 10× the original amount.

- **Systematic defense evaluation with two proposed defenses**: Section 5 compares 11 defense methods spanning post-calibration (temperature scaling, splines), training-based (DCA, SAM), and adversarial defenses (PGD-AT, AAA, RobustBench). The proposed Compression Scaling (CS) achieves the lowest post-attack ECE across several configurations, and the analysis reveals interesting tensions (e.g., RobustBench models compromise heavily on clean-data calibration).

- **Parameter sensitivity and query efficiency analysis**: Figure 2 examines the impact of perturbation budget ε and attack iterations on ECE, showing attacks are effective even at low ε with plateaus at higher values. Table 3 compares query efficiency of underconfidence vs. overconfidence attacks, revealing underconfidence attacks are consistently more query-efficient.

- **Detection difficulty evidence**: Table 2 shows that calibration attacks reduce detection AUC/accuracy for LID, Mahalanobis Distance, and SpectralDefense compared to standard attacks, with decreases of over 20 percentage points in some cases (e.g., SA-based calibration attack detection accuracy drops from 72.4% to 44.2% on CIFAR-100 using MD).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions are sound; the issues below are addressable presentation gaps or scope limitations.

### Minor

- **Formal inconsistency in Eq. (1)**: Equation (1) includes the constraint $\hat{y} \neq y$, which requires misclassification. This directly contradicts the paper's central premise that calibration attacks preserve prediction accuracy. The text in Section 3.2 ("adversarial examples are crafted to try to keep predicted class label $\hat{\pmb{y}}(\pmb{x}) = \hat{\pmb{y}}(\tilde{\pmb{x}})$") and Algorithm 1 (line 14, checking `argmax(f(x_new)) = k`) correctly enforce label preservation. The phrasing "For completeness of the paper, we include the details of adversarial constraint to be satisfied" (line 49) suggests Eq. (1) is intended as background on the standard adversarial constraint, but its placement within the calibration-attack objective section is confusing and creates an apparent contradiction. The equation should either be removed or explicitly labeled as the general adversarial constraint for context, with the calibration-specific constraint stated separately.

- **Post-attack accuracy could be more explicitly verified**: The paper repeatedly asserts that calibration attacks preserve accuracy (abstract, Figure 1 caption, Section 4.1), and Table 1 includes accuracy figures. However, the paper would significantly strengthen its core claim by explicitly stating post-attack accuracy alongside pre-attack accuracy for each attack type and dataset in the main text, rather than requiring the reader to infer it from tables. Table 4 does report accuracy before and after attack in the defense context, which partially addresses this, but the primary attack results (Table 1) would benefit from the same explicitness.

- **Detection analysis is limited in scope**: The claim that calibration attacks are "more difficult to detect than standard attacks" (Section 4.2) is based on experiments using only one architecture (ResNet-50) and three detection methods (LID, MD, SpectralDefense). While the results are indicative, testing on at least one additional architecture (e.g., ViT) would substantially strengthen the generality of this claim. The current setup leaves open the possibility that the detection difficulty is architecture-specific.

- **Compression Scaling (CS) defense parameters lack justification**: The CS defense (Section 3.3) uses parameters such as 15 bins with the top 3 (or 4) selected as the high-confidence target, without ablation or sensitivity analysis. The choice of bin count and the top-k selection strategy are critical to the method's performance and should be justified or ablated to demonstrate robustness.

### Trivial
None.

## Nice-to-Haves

- Directly compare calibration attacks to standard attacks (SA, PGD) at the same perturbation budget in terms of both calibration degradation (ECE/KS) AND accuracy drop, to quantify the trade-off.
- Report calibration plots or confidence histograms for each attack type to clarify phenomena like the overconfidence attack's low ECE but flattened confidence distribution.
- Test the CS defense against each attack type separately (not just maximum miscalibration) to understand its limitations.
- Discuss the computational cost of generating calibration attacks (query counts during attack vs. standard attacks) since this is relevant for practitioners assessing threat feasibility.

## Removed Points

*These points are flagged to be removed; treat them with caution if reading them.*

- **"Tables are garbled/unreliable"** — Removed because the garbled tables are a parser artifact of the extracted PDF text. The original submission has clean tables. Per instructions, formatting artifacts are not author errors.
- **"Algorithm 1 footnote paste error"** — The footnote text contains strangely spaced irrelevant content about IoT/backscatter. This is a parser artifact (spaces between every character, nonsensical in context). Per instructions, formatting/garbled text artifacts are not author errors.
- **"Overconfidence attack danger claim is unsupported speculation"** — Removed. The paper reports that overconfidence attacks raise confidence to ~99% and argues that flattening confidence scores renders them meaningless for decision-making. This is a reasonable interpretation of the reported experimental observation, not unsupported speculation.
- **"No discussion of computational cost"** — Removed as a generic/one-size-fits-all criticism. The paper does report query efficiency (Table 3), which is the relevant metric for black-box attacks.
- **"Prior work claim is unverified"** — Removed. Per instructions, missing related work should not be mentioned.
- **"Missing hyperparameter details"** — Removed per instructions about reproducibility nitpicks.
- **Strength: "This paper addressed an important problem"** — Removed as generic/superficial. The concrete strengths (taxonomy, evaluation breadth, defense comparison) are retained.
- **Strength: "Multi-architecture evaluation"** — This IS concrete and specific; I've retained it in the strengths list above.

## Novel Insights

The Harsh Critic's observation that the paper does not directly compare calibration attacks to standard attacks at the same perturbation budget in terms of both ECE and accuracy is an insightful framing — this comparison would cleanly quantify whether calibration attacks are truly a distinct threat or merely a byproduct of standard attacks under different loss functions. The paper provides the pieces for this comparison (standard SA baseline is discussed but not directly compared on calibration metrics) but does not assemble them. Additionally, noticing that Algorithm 1 checks label preservation only for underconfidence (line 14) but not for overconfidence (line 16) is a subtle but real algorithmic detail that neither reviewer explicitly flagged.

## Suggestions

1. **Correct Eq. (1)** by either removing the $\hat{y} \neq y$ constraint entirely or explicitly labeling it as the general adversarial constraint and adding a separate equation for the calibration attack's constraint ($\hat{y}(\tilde{x}) = \hat{y}(x)$).
2. **Add a table column or explicit sentence** in Section 4.1 reporting post-attack accuracy for each attack type, to explicitly verify the paper's central premise.
3. **Expand the detection analysis** to at least one additional architecture (ViT) to support the general claim of stealthiness.
4. **Add an ablation study for CS parameters** (bin count, top-k selection) and test CS against each attack type individually.
5. **Add a direct comparison** between calibration attacks and standard attacks (SA, PGD) at the same ε, measuring both ECE and accuracy, to quantify the distinctiveness of calibration attacks.

## Score and Decision

**Originality**: Good. The formulation of attacks that target calibration (rather than accuracy) is novel and the four-type taxonomy provides a useful organizational framework.

**Importance of research question**: High. Calibration is critical for trustworthy AI, and the stealthiness aspect (accuracy unaffected) makes this a genuinely concerning threat.

**Claims well-supported**: Mostly. The core demonstration that calibration can be severely degraded is well-supported. The claim of stealthiness (harder to detect) is supported but has limited scope (1 architecture). The Eq. (1) inconsistency undermines the formal framing but not the experimental conclusions.

**Soundness of experiments**: Adequate. Broad across datasets and architectures, with parameter sensitivity analysis. Some gaps: detection scope limited, no explicit accuracy verification in attack tables, CS parameters unablated.

**Clarity of writing**: Adequate but could be improved. The formal definition has an inconsistency (Eq. 1), and some figure references are unclear (e.g., "Subfigure-1, Subfigure-2" without explicit mapping).

**Value to the community**: Moderate. This opens a new direction in adversarial robustness research and provides a useful benchmark for future work on calibration-specific defenses.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>