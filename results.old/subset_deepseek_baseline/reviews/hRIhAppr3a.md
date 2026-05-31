## Summary
The paper proposes xImagand-DKI, a multi-view conditional diffusion model that takes SMILES and protein sequences as inputs and jointly generates nine pharmacokinetic (PK) properties and three drug-target interaction (DTI) values. The model integrates domain knowledge from Gene Ontology (via PO2Vec embeddings) and molecular fingerprints (via FPFormer) to improve the fidelity of synthetic data. The work is motivated by the widespread data overlap sparsity in drug discovery datasets and aims to provide a unified generative framework for filling these gaps.

## Strengths
- **Well-motivated problem.** Data overlap sparsity is a real and underexplored challenge in computational drug discovery. The paper clearly documents the limited overlap between PK and DTI datasets (e.g., only 0.7% of DTI molecules have any PK value) and positions the generative approach as a practical solution.
- **Multi-view domain knowledge infusion.** The incorporation of Gene Ontology (via PO2Vec) and multiple molecular fingerprints (via FPFormer) alongside standard SMILES and protein sequence embeddings is a thoughtful design that leverages complementary biological and chemical information.
- **Comprehensive evaluation dimensions.** The paper evaluates synthetic data quality through univariate (Hellinger distance), bivariate (differential pairwise correlations), and downstream utility (Machine Learning Efficiency) metrics, providing a reasonably thorough assessment.

## Weaknesses
### Fatal
None identified.

### Major
- **Insufficient technical detail on the diffusion model and conditioning mechanism.** The paper states that “1D patches are computed from the classifier-free guidance of SMILES and protein embeddings,” but never explains how classifier-free guidance is implemented, how the conditional and unconditional models are trained, or what guidance scale is used. The conditioning of the diffusion process on the embeddings is not formally specified. This obscures the core methodology and makes reproducibility difficult.
- **Machine Learning Efficiency (MLE) experiment is under-specified and raises serious concerns.** The paper does not state what regression model is used for MLE evaluation (e.g., random forest, linear regression, neural network). The “Real” column in Table 3 shows implausible R² values (e.g., -3.2 for Caco-2, -4.2 for CIH), which are worse than a constant mean predictor. Without knowing the model, it is impossible to interpret whether the synthetic data is genuinely useful or whether the real model was pathologically underfit. This undermines the central claim that synthetic data can “outperform real data.”
- **Limited ablation of domain knowledge infusion.** Only one ablation (No DKI vs. Ours) is presented. The contributions of the Gene Ontology embedding and the fingerprint embedding are not separated. Moreover, the improvement from DKI is marginal in several properties (e.g., Aq: 0.07 vs. 0.07, HL: 0.15 vs. 0.15), making it unclear whether the complexity is justified.
- **DTI generation shows no practical improvement.** In Table 3, the generated DTI data achieves nearly identical MLE results as real data and baselines (e.g., Kd mse = 0.11 for all models, R² ~0.22). The paper acknowledges this but does not provide a satisfying explanation or any evidence that the DTI generation is valuable. Given that DTI is half of the model’s output, this weakness significantly reduces the claimed contribution.

### Minor
- **Unclear model terminology.** The paper mentions “DeBERTa” in Figure 1 but “ChemBERTa” in the text for SMILES encoding. It is ambiguous which encoder is actually used in the final model.
- **Missing inverse transform details.** The paper applies a Gaussian quantile transform and min-max scaling to [-1,1] before diffusion, but does not describe how generated values are inverse-transformed back to meaningful units, nor whether the MLE evaluation uses the same preprocessing pipeline.
- **Outlier removal is not justified for evaluation.** The paper removes outliers based on IQR before training and testing, which can artificially improve distributional metrics and may not reflect the real data distribution encountered in practice.
- **Baseline selection is narrow.** Only cGAN and two variants of the authors’ own prior work are compared. Including established tabular generative models (e.g., CTGAN, TVAE) would strengthen the evaluation.

### Trivial
- The code link is listed as “TBD” – acceptable in a double-blind submission but should be resolved in the final version.

## Nice-to-Haves
- Provide per-component ablation (GO only, fingerprints only) to isolate the contribution of each knowledge infusion module.
- Include standard deviations or confidence intervals for all reported metrics (HD, MLE) to assess statistical significance.
- Clarify the architecture of the diffusion backbone (number of layers, attention heads, patch size, etc.) and the training procedure (learning rate, batch size, number of noise steps).

## Novel Insights
None beyond the paper’s own contributions – the paper is a straightforward application of diffusion models to tabular drug discovery data with added domain embeddings, but does not introduce new theoretical understanding or surprising empirical findings.

## Suggestions
- **Specify the MLE regression model** and report results for multiple models (e.g., random forest, XGBoost, MLP) to demonstrate robustness.
- **Provide a clear mathematical description of the conditioning mechanism** – how are the concatenated embeddings (PK/DTI class tokens, SMILES, protein, GO, fingerprint) incorporated into the diffusion transformer? Is classifier-free guidance used, and if so, what is the guidance scale?
- **Separate the ablation of GO embeddings and fingerprint embeddings** to demonstrate that each contributes meaningfully.
- **Include a comparison with a non-generative multi-task regression model** to show whether the generative approach adds value over direct prediction.

## Score and Decision
The paper tackles an important problem and proposes a reasonable architecture, but the lack of key technical details, an under-specified MLE evaluation with questionable results, and the weak DTI generation prevent the contribution from being convincingly established. Major revisions are required.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>