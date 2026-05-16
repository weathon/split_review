Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

## Summary

This paper tackles test-time adaptation (TTA) for regression, an underexplored setting where most existing TTA methods are classification-specific. The key insight is that regression features concentrate in a low-dimensional subspace, making naive full-dimensional feature alignment ineffective or harmful. The authors propose Significant-subspace Alignment (SAL), which uses PCA to detect the relevant subspace and weights dimensions by their impact on the scalar output. Experiments across four regression tasks (image-based and tabular) show SAL consistently outperforms baselines adapted from classification TTA.

## Strengths

- **Identifies a fundamental and novel failure mode:** The paper demonstrates empirically (Table subspace_dim) that regression model features occupy a small subspace (e.g., 40–60 dimensions out of 2048), and shows that aligning all feature dimensions indiscriminately—as classification TTA methods do—harms performance. This insight is well-supported and directly motivates the method.

- **Two well-motivated, regression-tailored components:** Subspace detection (PCA-based) focuses alignment on the relevant subspace, avoiding degenerate dimensions. Dimension weighting by $|\mathbf{w}^\top \mathbf{v}_d|$ prioritizes directions that affect the scalar output. Both components are explicitly designed for the regression setting and are not present in prior classification-oriented TTA methods.

- **Consistent outperformance across diverse tasks and shift types:** SAL achieves the highest R² scores on SVHN→MNIST, UTKFace (13 corruption types), Biwi Kinect (gender shift, 6 combinations), and California Housing, while most baselines from classification TTA often underperform Source. This demonstrates generalization across image and tabular data, synthetic and real shifts.

- **Ablations validate both components:** Without subspace detection, performance collapses to near or below Source (Table ablation). The ablation on K shows that $K=100$ works well across datasets without per-dataset tuning, and performance degrades predictably when K far exceeds the intrinsic subspace dimension.

- **Diagnostic analysis explains why SAL works:** Feature reconstruction error analysis (Figure 3) shows SAL preserves the source subspace structure during adaptation while baselines corrupt it. The histograms and central-limit-theorem argument (Eq. 12) show that subspace projection makes features more Gaussian, making the KL-divergence loss more appropriate and stable.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No limitations or failure-case discussion:** The conclusion (Section 6) is only four sentences and does not acknowledge any limitations. The paper would benefit from a discussion of when SAL might struggle—e.g., when the domain shift changes the covariance structure so substantially that the source subspace is no longer a good basis for target features, or why the gain on California Housing is modest (0.444 vs. 0.364).

- **No complementary evaluation metrics:** The paper reports only R². For tasks like Biwi Kinect head-pose estimation where the target range is bounded, R² can be misleadingly low even when absolute error is small. Reporting MAE or RMSE alongside R² would strengthen the evaluation.

- **Dimension weighting contribution is empirically marginal and insufficiently justified:** The ablation shows dimension weighting provides small gains (e.g., 0.698 vs. 0.692 on SVHN-MNIST). The paper acknowledges this is due to correlation between variance and weight, but does not construct a case where the weighting would be critical. A synthetic or controlled experiment demonstrating a scenario where a low-variance dimension has high output significance would justify keeping this component as more than a negligible add-on.

- **KL divergence theoretical grounding is cited for classification UDA, not specifically regression:** The paper cites Nguyen (2022) who proved the KL divergence bounds target error in UDA for classification, but does not discuss whether this bound transfers to the regression setting. The experiments show the approach works, so this is not a fatal gap, but the theoretical framing is weaker than claimed.

- **Missing pre-adaptation reconstruction error control:** The reconstruction error analysis (Figure 3) measures error after adaptation. Showing the reconstruction error *before* adaptation (i.e., with the unadapted source model) would provide a baseline to quantify how much SAL preserves vs. the baselines corrupt the subspace. This would strengthen the diagnostic claim.

### Trivial

- **Computational cost of PCA is not discussed:** The method requires computing a PCA on the full source feature matrix (potentially large for datasets like ImageNet-scale). A brief note on memory/time cost and when it could be a bottleneck would be helpful. The paper's TTA update is lightweight (affine parameters only), but the source-side PCA is a one-time cost worth acknowledging.

- **DANN comparison would benefit from clearer framing:** The paper separates DANN as a "method other than TTA" (line 214), which is correct and transparent. However, the abstract's phrasing "outperforms various baselines" is generic enough that a casual reader could include DANN in the comparison set. Explicitly stating in the abstract that DANN is compared only as a reference (not a TTA method) would prevent misinterpretation.

## Nice-to-Haves

- **Control: align all D dimensions using the naive KL divergence (Equation 2) in the ablation table.** The paper already explains that naive alignment fails (Section 3.1), but including it as a row in the formal ablation would directly quantify how much of the gain comes from simply avoiding degenerate dimensions vs. from the specific PCA-based subspace detection.

- **Synthetic case to demonstrate dimension weighting's value.** The paper acknowledges correlation between variance and weight; a controlled experiment where a low-variance, high-importance dimension exists would show the weighting component's necessity.

- **Pre-adaptation reconstruction error as a control baseline** in Figure 3.

- **More explicit guidance on selecting K:** The paper says to compute the rank of the source covariance, but providing a rule of thumb (e.g., "set K = rank + small constant" or "K = rank × 1.5") would make the method more usable by practitioners.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"SVHN-MNIST should not be used as a regression benchmark"**: The paper is transparent that these are digit datasets used for regression by training models to output scalar labels. Using them as a synthetic benchmark for domain shift is permissible. This is a scope-creep criticism. **(Removed: evaluates against the wrong class of expectations; the paper does not claim this is a realistic regression application.)**

- **"Prototype degrades performance relative to Source but does not update the feature extractor"**: Figure 3's caption states Source and Prototype are the same *in terms of reconstruction error* because both use the same feature extractor. Prototype adjusts the classifier head (prototypes), so its R² scores can differ from Source's even with the same feature extractor. This is not a contradiction. **(Removed: reviewer conflated reconstruction error analysis with R² performance.)**

- **"The paper does not discuss why Prototype degrades performance"**: Even if Prototype's R² scores differ from Source (which is not verified since tables are not visible), this is a very minor baseline-specific observation that does not affect the paper's contribution. **(Removed: does not affect the core claim.)**

- **"Comparing naive feature alignment (all D dimensions) as a control"**: The paper already establishes that naive alignment fails in Section 3.1 and shows this empirically via the ablation without subspace detection. The suggested control is already conceptually present. **(Moved to Nice-to-Haves.)**

## Novel Insights

Beyond the paper's own contributions, the reviews surface one worthwhile observation: the paper's central claim about regression features occupying a low-dimensional subspace is convincingly supported, but the weakest link in the argument chain is the dimension weighting component—the reviews correctly note that if variance and weight are naturally correlated, the weighting may be a non-essential add-on that happens not to hurt rather than a critical design choice. Future work on regression TTA should either find regimes where the correlation breaks down or drop the weighting for simplicity.

## Suggestions

1. Add a limitations paragraph to the conclusion acknowledging settings where SAL may struggle (e.g., when target distribution shift alters the covariance structure substantially).
2. Include MAE or RMSE alongside R², especially for bounded-range tasks like Biwi Kinect.
3. Either (a) construct a synthetic/controlled experiment showing the value of dimension weighting when variance-weight correlation breaks down, or (b) simplify the method by removing the weighting component and noting that the main gain comes from subspace detection.
4. Add pre-adaptation reconstruction error to Figure 3 as a baseline.
5. Mention the one-time computational cost of source-side PCA for transparency.
6. In the abstract, specify that the method outperforms TTA baselines (rather than "various baselines") to avoid ambiguity about the DANN comparison.

## Score and Decision

The paper addresses a genuinely underexplored problem (TTA for regression) with a simple, well-motivated, and experimentally validated method. The weaknesses are all minor: none threaten the core contribution, and most are addressable in a revision (adding complementary metrics, limitations, failure analysis). The evidence is sound, the experiments are thorough for a first work in this area, and the diagnostic analyses convincingly explain why the method works.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>