Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper proposes a Covariance-Adjusted Support Vector Machine (CSVM) for binary classification. The core idea is that traditional SVM uses Euclidean distance but data in the input space should be measured by Mahalanobis (statistical) distance. The authors apply class-specific Cholesky-based whitening transformations to map data into a Euclidean space where SVM is valid, then derive how margins in the input space depend on class covariance matrices. They propose the SM Algorithm — an iterative procedure that estimates population covariance from training data, runs SVM in both Euclidean and input spaces, and adjusts the classifier intercept to split the margin in proportion to class covariances. Experiments on five datasets compare CSVM against linear, RBF, polynomial, sigmoid SVMs and PCA/ZCA whitening.

## Strengths

- **Lemma 2.3 identifies a concrete relationship between margin allocation and class covariance**: The derivation showing that the margin ratio in the input space equals \(\sqrt{\theta^T(\Sigma_{y=-1})^{-1}\theta} / \sqrt{\theta^T(\Sigma_{y=1})^{-1}\theta}\) (Equation 14) provides a principled reason why covariance should influence where the decision boundary sits. This formalizes the intuition that higher-dispersion classes should get a wider margin.

- **The paper clearly identifies a genuine limitation of standard SVM**: Standard SVM assumes equal margins on both sides of the decision boundary regardless of class distribution. The observation that class covariance structure should affect margin allocation is well-motivated and connects to prior work (Tsang et al., Peng & Xu, Huang et al., Zafeiriou et al.) while attempting to resolve dimensional consistency issues the authors identify in those earlier formulations.

- **The SM Algorithm addresses a real practical obstacle**: Computing population covariance requires knowing test-data labels, which are unavailable. The iterative pseudo-labeling approach is a pragmatic attempt to estimate population-level covariance from finite training data, and the paper acknowledges its heuristic nature in the conclusion.

## Weaknesses

### Fatal

None. The theoretical core (Section 2) does not contain a mathematical error that invalidates the entire contribution.

### Major

- **Experimental comparison is confounded by test-data leakage**: The SM Algorithm iteratively adds test data points (with pseudo-labels) to the training sets to update covariance matrices (Steps 2f–2h). This means test-data features enter the training process, whereas all baseline SVMs are trained exclusively on the original training split. The comparison is fundamentally unfair: CSVM operates in a transductive/semi-supervised regime while baselines are purely supervised. Any observed improvement could stem from exploiting test-data structure rather than from the claimed covariance adjustment. Without a clean train/test separation for CSVM — e.g., using a separate unlabeled pool for iterative refinement and a held-out test set for evaluation — the experimental evidence does not support the paper's conclusions.

- **The SM Algorithm is heuristic with a weak connection to the theory of Section 2**: Step 2d of the algorithm runs standard linear SVM in the input space — the very space the paper's Lemma 2.1 declares invalid for SVM — to obtain \(\theta_{\text{Input}}\). Step 2e then shifts only the intercept \(\theta_0\) using a ratio derived from \(\theta_{\text{Euclidean}}\) and the sample covariance matrices. This intercept adjustment is not derived from any optimization principle or SVM-like objective. The paper acknowledges the algorithm is heuristic (Section 6), but the gap between the clean theoretical derivation of Section 2 and the ad-hoc correction in Section 3 is large. The reader is left uncertain whether the empirical gains (if real) come from the covariance adjustment or from the transductive pseudo-labeling mechanism.

### Minor

- **No statistical significance or variance estimates are reported**: Tables 1–4 present single-point estimates of accuracy, precision, recall, and F1 without confidence intervals, standard deviations, or cross-validation over multiple random splits. Many differences are small (e.g., CSVM 0.981 vs. linear SVM 0.979 on Pulsar accuracy) and may not be statistically meaningful. This makes it difficult to assess whether the claimed improvements are genuine or within noise.

- **Only 5 datasets, all relatively small and standard**: While the diversity of domains (healthcare, astronomy, quality, safety) is a positive, the scale is modest. The paper would benefit from a broader empirical evaluation, particularly since the claimed improvements are small in absolute terms.

- **No comparison against existing Mahalanobis-based or covariance-aware SVM variants**: The paper cites Tsang et al. (2006), Peng & Xu (2012), Huang et al. (2004), and Zafeiriou et al. (2007) as prior work incorporating covariance into SVM but does not compare against any of them empirically. This makes it impossible to assess whether CSVM advances the state of the art in covariance-adjusted classification or merely improves over standard kernels that don't use covariance at all.

### Trivial

- The paper's framing that SVM is "invalid" in non-Euclidean spaces is somewhat overstated. SVMs operate in inner-product spaces and can incorporate covariance through kernel design; the real contribution is about margin asymmetry, not about fundamentally invalidating SVM.

## Nice-to-Haves

- A transductive-SVM (TSVM) baseline would be appropriate given that the SM Algorithm uses unlabeled test data during training.
- An ablation study separating the effect of class-specific whitening from the effect of iterative pseudo-labeling would clarify which component drives performance.
- Derivation of the intercept adjustment in Step 2e from an optimization principle (e.g., a modified SVM that penalizes unequal margins) would strengthen the theoretical narrative.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic Point 1 (class-specific transformation destroys single Euclidean space)**: This criticism is factually incorrect. Both transformations \(\Psi^{-1}_{y=1}\) and \(\Psi^{-1}_{y=-1}\) map \(\mathbb{R}^n \to \mathbb{R}^n\). After transformation, all data points reside in the same \(\mathbb{R}^n\) with the standard Euclidean inner product. SVM operates on the union of these transformed points without any mathematical incoherence. The critic confuses different coordinate transformations with different vector spaces. The optimization in Equations (6)–(7) is well-defined: each constraint uses the appropriate transformation for its class, and \(\theta\) and \(\theta_0\) are shared parameters in \(\mathbb{R}^n\) and \(\mathbb{R}\) respectively.

- **Harsh Critic claim that the paper "misrepresents how SVMs work" (Abstract/Introduction notes)**: The paper's claim that SVM is derived from Euclidean distance and is therefore native to Euclidean space is a legitimate perspective — it's essentially arguing that standard SVM assumes isotropic covariance. This is a reasonable starting point, not a misrepresentation.

- **Harsh Critic claim about PCA/ZCA comparison missing the point (Section 4 notes)**: The paper explicitly acknowledges that PCA/ZCA use a single transformation on all data while CSVM uses class-wise transformations, and presents this as a deliberate point of differentiation. This is not a flaw.

- **Strength Finder point about "empirical validation across diverse datasets" as a core strength**: While the diversity of domains is positive, the experimental validation is compromised by the data leakage issue. This strength is therefore unreliable and dropped from the main review.

- **Strength Finder point about "clear theoretical foundation for covariance-adjusted SVM" as a core strength**: The derivation in Section 2 is presented but the transition to the SM Algorithm is weak. The theoretical foundation is partially valid but not fully realized.

## Novel Insights

The observation that class-specific whitening followed by SVM in the Euclidean space naturally produces an asymmetric margin allocation in the input space (Lemma 2.3, Equation 14) is a genuinely interesting geometric insight that does not appear to be widely discussed in the SVM literature. The idea that the margin-splitting ratio is determined by the ratio of inverse-covariance-weighted norms provides a clean geometric interpretation of why and how covariance should affect the decision boundary. This insight survives even if the practical algorithm and experiments need substantial revision.

## Suggestions

1. **Fix the experimental design**: Split data into train / unlabeled-pool / test. Run the SM Algorithm's iterative refinement on the unlabeled pool only, evaluate on the held-out test set. Compare against transductive SVM and semi-supervised baselines that also have access to the unlabeled pool.

2. **Add a transductive SVM baseline**: Since CSVM uses test features during training, the natural comparator is TSVM, not purely supervised SVM.

3. **Report statistical significance**: Use cross-validation with multiple random splits and report means with confidence intervals. Run paired tests (e.g., McNemar's test) for the claimed improvements.

4. **Strengthen the theory-to-algorithm connection**: Either (a) derive the intercept adjustment from a modified optimization problem that explicitly penalizes unequal margins, or (b) acknowledge the gap more explicitly and position the SM Algorithm as a practical approximation that is motivated by but not derived from the theory.

5. **Compare against prior covariance-aware SVM methods** (Tsang et al., Peng & Xu, Zafeiriou et al.) to establish where CSVM stands relative to the existing literature.

## Score and Decision

### Anchor comparison:

| Anchor | Avg Score | Decision | Comparison to paper under review |
|--------|-----------|----------|----------------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/bp9DOHb1mk.md` (GDA) | 5.00 | Accept (Poster) | Stronger: clean theory-to-algorithm connection, 27 datasets, proper evaluation. CSVM is weaker on all fronts. |
| `/home/wg25r/review_agent/human_reviews_2026/C0qgkcCehg.md` (Mini-batch kernel k-means) | 4.40 | Reject | Stronger: solid theory, clean algorithm, fair experiments, just seen as incremental. CSVM has worse experimental flaws. |
| `/home/wg25r/review_agent/human_reviews_2026/HuuCWjlJuQ.md` (Mahalanobis OOD) | 4.29 | Reject | Comparable in topic (Mahalanobis + classification) but stronger empirically (broader evaluation, statistical metrics). CSVM is weaker due to data leakage. |
| `/home/wg25r/review_agent/human_reviews_2026/ytbX1CRzah.md` (Geometric Moment Alignment) | 3.50 | Reject | Comparable: interesting geometric idea with experimental limitations. CSVM shares similar severity of issues. |
| `/home/wg25r/review_agent/human_reviews_2026/Pkm5u3OjRB.md` (Training-Free Diffusion) | 3.00 | Reject | Weaker: theory disconnected from practice, method reduces to heuristic. CSVM has a stronger theoretical core but similar algorithmic gap. |
| `/home/wg25r/review_agent/human_reviews_2026/nn5Vf6GEsV.md` (Kernel Regression Learning Curves) | 6.40 | Accept (Poster) | Much stronger: rigorous theory, strong empirical validation. CSVM is far below this standard. |

The paper's theoretical core (Section 2, Lemmas 2.1–2.3) has genuine merit as a geometric analysis of how covariance affects SVM margins. However, the practical algorithm is heuristic with a weak connection to the theory, and the experimental validation is fundamentally compromised by test-data leakage. These are not minor issues — the empirical claims cannot be trusted without a redesign, and the theory-to-practice gap is substantial.

Positioned against the anchors: this paper is clearly below the accepted GDA paper (5.00) and the rejected-but-solid mini-batch kernel k-means (4.40). It is comparable to the Geometric Moment Alignment paper (3.50) — an interesting geometric idea undermined by experimental limitations — and stronger than the Training-Free Diffusion paper (3.00) whose theory was largely decorative. I score it **3.5**.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>