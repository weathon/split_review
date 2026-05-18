Now I have all the information I need. Let me produce the consolidated final review.

---

## Summary

This paper addresses test-time adaptation (TTA) for regression, a setting where most existing TTA methods fail because they rely on classification-specific losses like entropy minimization. The authors observe that regression model features lie in a low-dimensional subspace (Table `subspace_dim`), making naive dimension-wise feature alignment unstable and ineffective. They propose **Significant-subspace Alignment (SAL)**, which (1) uses PCA to detect the feature subspace, (2) performs KL-divergence-based feature alignment within that subspace, and (3) applies dimension weighting to prioritize directions that affect the scalar output. Experiments on four datasets (SVHN→MNIST, UTKFace, Biwi Kinect, California Housing) show that SAL consistently outperforms adapted classification TTA baselines.

## Strengths

1. **First systematic treatment of TTA for regression.** The paper correctly identifies that existing TTA methods rely on classification-specific designs (entropy minimization, class prototypes) that are inapplicable when models output a single scalar. This gap is real, and the paper provides a tailored solution.

2. **Key empirical discovery—regression features are low-rank.** Table `subspace_dim` shows that the effective rank of feature covariance is far smaller than the feature dimension (e.g., 2048→32–40 for ResNet). This observation directly motivates why naive alignment fails and frames the problem clearly.

3. **Well-motivated and simple method with consistent gains.** SAL (PCA projection + KL alignment in subspace + weight-based prioritization) achieves higher R² than all baselines across every dataset and setting. Many baselines degrade below the no-adaptation Source, while SAL consistently improves. The feature reconstruction analysis (Figure 2) provides mechanistic evidence that SAL preserves the source subspace while baselines destroy it.

4. **Thorough ablations.** The paper separately ablates subspace detection and dimension weighting (Table `ablation_table`), showing that both contribute. It also analyzes sensitivity to the subspace dimension K (Table `ablation_table_k`), showing that performance peaks near the true subspace rank and degrades when K is too large. The analysis that projected features become approximately Gaussian (Figure 3, CLT argument in Eq. 10) justifies the use of KL divergence.

5. **Generalizes across input modalities.** SAL is evaluated on image data (SVHN, UTKFace, Biwi Kinect) and tabular data (California Housing), demonstrating it is not input-modality-specific.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No error bars or statistical significance reported.** All results are single numbers without confidence intervals, standard deviations, or multiple runs. Given that some gains are modest (e.g., Biwi Kinect roll from 0.52→0.55), it is unclear whether the improvements are statistically significant. This is the most substantive weakness—the paper would be stronger with means and standard deviations over at least 3 runs.

2. **Only R² is reported; practical impact is not calibrated.** Adding RMSE or MAE would help contextualize the magnitude of improvement. For example, on UTKFace with Gaussian noise, Source achieves R²=0.20 and SAL achieves 0.47—a large relative gain but still low in absolute terms. Without task-specific accuracy thresholds or human performance, the practical significance of some improvements is unclear.

3. **The baseline comparison, while reasonable, would benefit from one stronger regression-adapted baseline.** The paper acknowledges there are no off-the-shelf TTA methods for regression and adapts classification baselines. Several of these are expected to perform poorly (e.g., Prototype uses class prototypes). Including a simple but sensible regression-specific adaptation—such as Tent-style adaptation with a variance-based or energy-based surrogate loss in place of entropy—would set a higher bar and strengthen the empirical claims.

4. **Limited discussion of limitations and failure cases.** The paper has no explicit limitations section. It does not discuss when the subspace assumption might break (e.g., when source and target are very different), nor the restriction to models with a linear output layer. The linear regressor assumption is stated in Eqs. (1) and (6) but its implications for nonlinear output heads are not discussed. A brief limitations paragraph would strengthen the paper.

5. **Dimension weighting contributes modestly and lacks a principled derivation.** The ablation shows that dimension weighting adds a small increment over subspace detection alone. The formula α_d = 1 + |w^T v_d^s| is intuitive but heuristic; the "+1" is not justified, and the paper acknowledges that variance and weight correlate anyway. This is not a fatal issue, but a more principled weighting scheme (or a clearer explanation of why the simple form is sufficient) would be welcome.

6. **Adaptation dynamics and computational cost are not reported.** The paper does not report the number of gradient steps, convergence speed, or wall-clock time per batch. For a method intended for test-time use, computational efficiency matters.

### Trivial
- Code availability is not mentioned; releasing code would improve reproducibility.

## Nice-to-Haves
- A synthetic toy example demonstrating a case where a low-variance direction has high output weight, making the dimension weighting mechanism concretely visible.
- Principled, automatic criterion for selecting K (e.g., eigenvalue threshold or explained-variance ratio) rather than defaulting to K=100 and relying on the subspace rank.
- Ablation on which model parameters to update (affine only vs. full feature extractor) to test whether updating more parameters would break the subspace.

## Removed Points
These points were raised by the harsh critic but are removed after verification against the paper:

- **"Novelty is incremental / the core contribution is just PCA + alignment"** — The paper's contribution is appropriately scoped. It is the first TTA method designed for regression, identifies a real problem (low-rank features breaking alignment), and proposes a clean solution. The fact that the solution combines existing components in a novel way does not make it "incremental" in a negative sense; this is standard engineering research. Removed because it mischaracterizes the contribution's novelty.
- **"The phrase 'TTA does not train additional models nor access the target dataset for multiple epochs' overstates the difference from SFDA"** — This statement appears in the Related Work section describing the general TTA setting, not the paper's own method. Computing a covariance matrix from the source dataset at pre-training time is standard for feature-alignment TTA methods and does not constitute "training additional models" or "accessing the target dataset for multiple epochs." The reviewer's objection is based on a misreading. Removed.
- **"The KL divergence bound from Nguyen et al. (2022) was developed for classification UDA; its applicability to regression is not established"** — The paper cites Nguyen et al. as inspiration for using KL divergence, not as a formal theoretical guarantee for regression. The bound is general (any hypothesis class). The paper does not claim to prove a new theoretical result. This is a nitpick that misreads the purpose of the citation. Removed.
- **"Subspace detection is precomputed from source features and assumes the subspace does not change"** — The paper explicitly tests this via feature reconstruction analysis (Figure 2), which shows that SAL preserves the source subspace. The concern is already experimentally addressed. Removed.
- **"The baselines are weak by design, which inflates the apparent gain"** — The paper includes RSD (a regression UDA method), DANN (a classic UDA method), TTT (test-time training), and Oracle. These go beyond trivial baselines. The claim that baselines are "weak" is overstated and ignores that no regression-specific TTA baselines exist in the literature. Partially kept in Minor #3 as a suggestion for strengthening rather than as a weakness.

## Novel Insights

The reviews surface a useful tension that is not fully resolved in the paper: the subspace detection component does most of the work, and the dimension weighting contributes little because variance and weight are naturally correlated in the learned subspace. This suggests that the core insight is really about the *geometry* of regression features—their low effective rank—rather than the specifics of *weighting* by output sensitivity. A future direction implicitly suggested by this finding is to investigate whether any form of subspace-constrained alignment (not just PCA-based) suffices for regression TTA, and whether the low-rank property holds for other losses beyond MSE.

## Suggestions

1. **Add error bars/standard deviations** to all main results (at least 3 random seeds or bootstrapped estimates).
2. **Include RMSE or MAE** alongside R² to calibrate the practical magnitude of improvements.
3. **Add one stronger regression-adapted baseline** (e.g., Tent with a variance-based or negative-confidence surrogate loss) to raise the bar of comparison.
4. **Add a brief limitations section** discussing: (a) the linear output head assumption, (b) what happens when the source subspace is a poor prior for the target, and (c) potential failure cases.
5. **Report wall-clock time and convergence** (number of gradient steps per batch).

## Score and Decision

The paper is technically sound, addresses a genuine gap, and presents a well-engineered solution with thorough ablations. None of the weaknesses are fatal; the main issues (lack of error bars, single metric, limited limitations discussion) are addressable and standard for a good conference paper at this tier.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>