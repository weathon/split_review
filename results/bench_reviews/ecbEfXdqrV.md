Now I have all the information I need to write the consolidated review. Let me synthesize everything carefully.

---

## Summary

This paper investigates whether the "counterintuitive phenomenon" — where deep generative models assign higher likelihoods to out-of-distribution data than in-distribution data — occurs in tabular anomaly detection. The authors propose a domain-agnostic definition of this phenomenon based on relative AUROC comparison against baseline detectors, then benchmark a NICE-based normalizing flow likelihood test (NF-SLT) against 12 baselines across all 47 tabular and 10 CV/NLP embedding datasets from ADBench. They find NF-SLT achieves the best average AUROC (0.8575) and lowest fail ratio (0.02), concluding the phenomenon is rare in tabular data. They explain this via two mechanisms: lower dimensionality (with a theoretical analysis linking dimension to likelihood inversion) and weaker feature correlation (quantified via a novel d-Ratio metric comparing intrinsic to ambient dimension).

## Strengths

- **Comprehensive large-scale benchmarking**: The paper evaluates 13 models on all 47 tabular and 10 CV/NLP embedding datasets from ADBench without selection bias, providing per-dataset AUROC tables and aggregate metrics. This is a substantial empirical contribution to the tabular anomaly detection literature.
- **Novel d-Ratio metric for quantifying feature correlation**: Section 5.2 introduces d-Ratio (intrinsic dimension / ambient dimension) as a principled way to quantify overall feature correlation. The autoregressive-covariance toy example (Figure 1) validates the metric, and the comparison between image datasets (d-Ratio ~0.002-0.019) and tabular datasets (d-Ratio ~0.39-0.81 in Table 4) provides genuine insight into structural differences between domains.
- **Strong empirical performance of NF-SLT**: NF-SLT achieves the highest average AUROC (0.8575), highest AUPRC (0.6398), best average rank (3.43), and lowest fail ratio (0.02) among 13 models. Even the yeast dataset where NF-SLT underperforms shows only a 0.02 minimum performance gap from the next model, consistent with the paper's argument that genuine counterintuitive failures are absent.
- **Multi-pronged explanatory framework**: The paper combines theoretical analysis (Theorem 5.4, Corollary 5.6), synthetic experiments (Figures 2-3 showing AUROC degradation with dimension), dimensionality-reduction experiments (Tables 2, 5), and feature-correlation analysis (Section 5.2, Table 4) to explain why tabular data avoids the phenomenon. The synthetic experiments in Appendix C.3 showing AUROC→0.5 as dimension increases, and the histogram analysis of latent norms becoming identical in high dimensions, are well-executed supporting evidence.

## Weaknesses

### Fatal

None. The core empirical finding — that simple likelihood tests with normalizing flows are effective anomaly detectors on tabular data — is well-supported by the experiments.

### Major

- **The redefinition of the "counterintuitive phenomenon" changes what is being measured.** The original phenomenon (Nalisnick et al., 2019a) is about likelihood inversion: OOD data receiving higher estimated likelihoods than in-distribution data. Definition 3.3 instead defines the phenomenon via relative AUROC: the flow model must be outperformed by a majority of comparison models with a significant margin. The paper argues for this redefinition (lines 68-82), noting that direct likelihood comparison would "consider any result outside 100% AUROC as counterintuitive" and that "likelihood inversion can arise from intrinsic dataset difficulty." However, these are different constructs — a flow could exhibit likelihood inversion (the original phenomenon) yet still outperform other detectors if those detectors are weak, or a flow could be a poor anomaly detector without likelihood inversion. The paper never directly measures whether anomaly samples receive higher likelihoods than normal samples in tabular data. The main claim that "the counterintuitive phenomenon rarely occurs in tabular data" therefore refers to the paper's own redefined phenomenon, not the original one. The experiments more accurately support the claim that "NF-SLT is a strong anomaly detector on tabular data."

- **The definition's parameters β and γ are never instantiated.** Definition 3.3 requires thresholds β (proportion of outperforming models) and γ (minimum performance gap), but these are never assigned values in the experimental section. The experiments instead use aggregate metrics like Fail Ratio (rank ≥ 9) and Top2 Ratio, which are related but not equivalent to the definition's conditions. For the definition to be testable, the paper should specify β, γ and apply them per-dataset.

### Minor

- **The theoretical analysis in Section 5.1 assumes independent marginals** (Theorem 5.4 requires P and Q to factorize as products of per-dimension densities). The paper acknowledges this limitation in the context of Table 3 experiments ("independence between pixels is not guaranteed, so the theorem presented in Appendix D cannot be applied"), and supplements the theory with PCA/ICA experiments that relax the independence assumption. However, the gap between the idealized theoretical conditions and real tabular data (which has arbitrary feature dependencies) means the theory provides intuition rather than a direct explanation for the ADBench results.

- **The conflation of OOD detection and anomaly detection is acknowledged but brief.** Appendix A treats the two tasks as equivalent, but the original counterintuitive phenomenon was observed with entirely different datasets as in/out-of-distribution (CIFAR-10 vs. SVHN), while ADBench splits a single dataset into normal and anomalous classes. The behavior of likelihood-based tests can differ meaningfully between these settings, and the paper's conclusions rest on the assumption that the phenomenon should be expected to transfer. A more thorough discussion of when and why this transfer is justified would strengthen the argument.

- **The feature correlation analysis in Table 4 uses only 4 image and 4 tabular datasets.** While the d-Ratio differences are stark (~0.002 vs. ~0.39-0.81), the sample is small, and the claim that this generalizes to the broader tabular domain would benefit from reporting d-Ratios for more ADBench datasets.

### Trivial

- Tables 2, 3, 5, 6, and 7 display identical numeric values across all dimension/component columns in the extracted PDF — this is a parser artifact that obscures the dimensionality-reduction evidence. The surrounding text clearly describes trends that should be visible, but the rendered numbers do not vary. This is a presentation artifact, not an author error.

## Nice-to-Haves

- Directly measuring likelihood inversion on selected ADBench datasets (e.g., histograms of log-likelihood for normal vs. anomalous test samples, or reporting the proportion of datasets where median anomaly likelihood exceeds median normal likelihood) would complement the relative-performance analysis and directly connect to the original phenomenon.
- Specifying and justifying concrete β, γ values for Definition 3.3 and reporting per-dataset results would make the definition fully testable.
- Extending the d-Ratio analysis to more than 4 tabular datasets would strengthen the feature-correlation argument.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Experiments do not apply the paper's own definition to individual datasets"** (Harsh Critic #2): The paper provides complete per-dataset AUROC tables (Table 17, Appendix I) from which Definition 3.3 could in principle be computed. While the paper does not systematically tabulate β/γ results, the aggregate fail ratio analysis combined with per-dataset tables provides substantial evidence. The yeast example demonstrates the paper is aware of the definition's conditions. This is partially addressed by the "β, γ never instantiated" weakness listed above.

- **"Dimensionality reduction experimental tables contain identical numeric entries"** (Harsh Critic #4): This is a PDF parser artifact. The paper's text describes clear trends ("AUROC increases as the dimensionality decreases") that require varying numbers. The original submission does not have this issue. This is covered as a Trivial note above.

- **"The statement that images have three dimensions ignores flattened pixel dimensionality"** (Harsh Critic, Section-by-Section): The paper explicitly addresses this: "CIFAR-10, one of the image datasets with small dimensions, has a dimension of 3072" (line 107). Fact 1.1 is a structural description, not a quantitative claim about feature count.

- **"Theory is disconnected from real data and independence assumption is contradictory with feature correlation discussion"** (Harsh Critic #3, partially): The paper uses independence for the theoretical bound in Section 5.1 and separately discusses feature correlation in Section 5.2 without claiming the theory applies directly. The paper acknowledges the limitation for Table 3. This point is weakened and partially preserved in the Minor weakness above.

- **"Missing baseline comparison / unfair hyperparameter tuning"** (removed): The paper provides a thorough hyperparameter sensitivity analysis (Table 12) showing NF-SLT has the *smallest* AUROC difference under optimal vs. uniform tuning — meaning the comparison actually disadvantages the baselines more than NF-SLT.

- **All Strength Finder items about generic importance** ("this paper addressed an important problem," "this paper targeted an interesting question"): Removed as superficial/not concrete.

## Novel Insights

The d-Ratio metric combining intrinsic dimension estimation (via TwoNN/MLE) with ambient dimension provides a genuinely novel quantitative lens for comparing feature correlation across domains. The finding that tabular datasets exhibit d-Ratios orders of magnitude higher than image datasets (~0.40-0.81 vs. ~0.002-0.019) offers a principled way to think about why architectural inductive biases (CNN locality vs. MLP flexibility) interact differently with data from different domains. The paper's empirical observation that NICE (volume-preserving) slightly outperforms RealNVP (affine coupling) on tabular anomaly detection (Table 13), despite lower expressive power, is an intriguing result that could motivate future architectural research.

## Suggestions

- Reframe the paper's central claim to match what the experiments actually demonstrate: "Simple likelihood tests with normalizing flows are effective anomaly detectors on tabular data, unlike in the image domain." This retains the paper's contribution without overclaiming about the counterintuitive phenomenon.
- Add a direct likelihood-inversion measurement (e.g., proportion of datasets where median anomaly log-likelihood exceeds median normal log-likelihood, or AUROC based purely on likelihood ordering) to complement the relative-performance analysis and connect to the original Nalisnick et al. findings.
- Instantiate β and γ with concrete values and report how many datasets satisfy Definition 3.3 under those thresholds.
- Extend the d-Ratio analysis to a larger sample of ADBench datasets to strengthen the feature-correlation argument.
- Clarify in Section 5.1 that the independence assumption provides theoretical intuition rather than a direct model of real tabular data, and explicitly state what the PCA/ICA experiments add beyond the theory.

## Score and Decision

**Anchor comparison:**
- `/home/wg25r/review_agent/human_reviews_2026/UFwgg44VZq.md` (ReTabAD, avg 5.50, Accept): A benchmark paper with clean contribution but narrow scope. The paper under review is comparably strong empirically (larger scale: 47 vs. 20 datasets) but has a framing issue with its central definition.
- `/home/wg25r/review_agent/human_reviews_2026/73QNa7rAgm.md` (TCAD, avg 4.00, Reject): A method paper with solid experiments but concerns about assumptions and novelty. The paper under review surpasses this in scale, theoretical depth, and contribution.
- `/home/wg25r/review_agent/human_reviews_2026/JdbqDiguyO.md` (NRDE, avg 3.33, Reject): A normalizing flow paper for tabular AD with fundamental assumption issues and poor writing. The paper under review is substantially stronger in every dimension.
- `/home/wg25r/review_agent/human_reviews_2026/jCQVjd4vrX.md` (Likelihood Paradox, avg 4.00, Reject): Had a fundamental conceptual issue (circular reasoning). The paper under review's definitional issue is less severe and does not invalidate the core empirical findings.
- `/home/wg25r/review_agent/human_reviews_2026/0eEtTsnmyo.md` (USF, avg 4.00, Reject): Incremental novelty with modest empirical gains. The paper under review offers broader experiments, a novel metric, and richer analysis.

The paper under review offers a substantial empirical contribution (47 datasets, 13 models), a novel feature-correlation metric, and well-executed synthetic experiments supporting the dimensionality argument. The central weakness is the redefinition of the "counterintuitive phenomenon," which creates a gap between the claimed contribution and what the experiments measure. However, the underlying empirical finding — that NF-SLT is a strong anomaly detector on tabular data — is robust and valuable. The paper falls above the 4.00-level rejected papers and is comparable to ReTabAD (5.50) but slightly below due to the framing issue. I score it at 5.0, reflecting a borderline-accept paper with a solid empirical contribution that would benefit from reframing.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>