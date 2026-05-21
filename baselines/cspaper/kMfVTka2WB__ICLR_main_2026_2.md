---
job_id: 0757240a-79dc-4c5a-a1f9-5476e64a01c8
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: kMfVTka2WB.pdf
paper: An Algorithm to Perform Covariance-Adjusted Support Vector Classification in Non-Euclidean Spaces
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The submission is squarely about kernel methods, SVMs, geometry, and learning in non-Euclidean spaces, which fits ICLR topics including metric/kernel learning, learning theory, and learning on other geometries.

## Minimum Quality
Pass ✅. The paper contains the core ingredients of a research submission, namely abstract, introduction with related-work discussion, methodology, algorithm description, experiments/results, and conclusion, although several of these parts are weak and underdeveloped.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious instructions to reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper argues that standard SVM margin geometry is only valid in Euclidean space, and proposes a covariance-adjusted SVM for binary classification in what the authors call non-Euclidean input/statistical space. The method performs class-wise Cholesky-based whitening, derives a margin ratio depending on class covariance, and introduces an iterative SM algorithm to estimate covariance-adjusted classifiers when test labels are unknown. Experiments on five binary datasets compare the proposed CSVM-Cholesky approach against several standard SVM kernels and PCA/ZCA-whitened linear SVMs.

## Strengths
The paper tackles an intuitively meaningful question, namely whether margin geometry should account for different class covariances rather than treating the two sides of the margin symmetrically. Even though I am not convinced by the current derivation, the motivation is understandable and the authors are trying to connect geometric assumptions, covariance structure, and classification boundaries in a concrete way.

The method is easy to describe at a high level. Section 3 gives a procedural algorithm, and the use of Cholesky factors makes the construction computationally straightforward when class covariance matrices are well-conditioned. The paper also makes an effort to compare against multiple baselines rather than only a linear SVM.

The empirical section at least covers several datasets from different domains. In **Tables 1 to 4** on Pages 7, the proposed method is consistently competitive and often numerically best among the reported methods. For example, in **Table 1**, CSVM-Cholesky has the top reported accuracy on Breast Cancer, Diabetes, Red Wine, and Pulsar; in **Table 4**, it also has the top reported F1 on four of the five datasets. Those gains are not large, but they do suggest the method is not completely arbitrary.

The figures do provide a visual summary of the reported behavior. In **Figure 1** and **Figure 2** on Page 8, the ROC curves for Breast Cancer, Pulsar, Red Wine, and OSHA broadly match the tables in the sense that CSVM is among the strongest curves, especially for Breast Cancer and Pulsar. This at least supports the claim that the method can be competitive in ranking quality, not only thresholded accuracy.

## Weaknesses
1. **The central theoretical framing is overstated, and key claims are not justified by the derivations presented.**  
   The strongest issue is the repeated claim that SVM principles, including max-margin classification and KKT boundary conditions, are valid only in Euclidean space, and that in non-Euclidean spaces one obtains one classifier per class or per class-specific input space. This is asserted in **Lemma 2.1, Lemma 2.2, and Lemma 2.3** on Pages 3 to 4, but the paper does not provide proofs, only informal manipulations. KKT conditions are optimization conditions, not a geometric privilege exclusive to Euclidean spaces. If the authors optimize a constrained convex problem written in transformed coordinates, KKT still applies to that optimization problem. Saying they are "not valid" in the input space is far stronger than what the presented derivation supports. This matters because the paper's claimed contribution rests almost entirely on these lemmas. If those claims are not established, the work becomes a heuristic covariance-aware preprocessing plus bias adjustment method, which is a much narrower contribution.

2. **The mathematical derivation confuses coordinate transformation, metric choice, and existence of distinct class-specific spaces.**  
   In **Equation (2)** and **Equation (3)** on Page 3, the paper defines separate transformations
   \[
   X^{\text{Euclidean}}_{y=1}=\Psi_{y=1}^{-1}X^{\text{Input}}_{y=1},\qquad
   X^{\text{Euclidean}}_{y=-1}=\Psi_{y=-1}^{-1}X^{\text{Input}}_{y=-1}.
   \]
   This means the two classes are mapped by two different linear operators. Once this is done, the data are no longer represented in one common transformed feature space where a single linear SVM can be naturally defined. Yet **Equations (4) to (7)** immediately proceed as if one common Euclidean-space classifier \(\theta^T X^{\text{Euclidean}} + \theta_0 = 0\) applies uniformly. That step is exactly where the argument needs to be most careful, and it is not. A classifier trained after applying different class-dependent transforms to different samples is not the same object as a standard linear SVM in a single shared representation space. This is a foundational inconsistency, not a cosmetic notation issue.

3. **The margin formulas in the input space are presented as if they directly justify a new optimization problem, but the logic is incomplete.**  
   In **Equation (9)** on Page 4, the paper writes the margin for class \(y=1\) as
   \[
   \frac{1}{\sqrt{\theta^T \Sigma_{y=1}^{-1}\theta}}.
   \]
   Then **Equations (10) to (13)** define separate optimization problems for the two classes. But this step is not rigorously derived from a well-defined primal objective over a shared classifier, and there is no proof that solving these separate objectives is equivalent to the claimed transformed-space SVM. In fact, if the transform is class-dependent, the induced decision function should be defined carefully for unseen points whose label is unknown. The paper never specifies a single coherent prediction function derived from a single optimization objective. Instead, Section 3 introduces an iterative heuristic that effectively assigns labels and recomputes covariances, which is quite different from having established a principled SVM formulation. This gap matters because the submission markets the method as a theoretically grounded correction to SVM geometry, whereas the actual executable method is heuristic.

4. **The proposed SM algorithm appears to use test inputs during iterative relabeling, which makes the evaluation protocol problematic and risks transductive leakage.**  
   In **Section 3, Steps (f) to (h)** on Pages 4 to 5, the algorithm explicitly labels test datapoints using the current classifier, adds them to the class-specific training sets, recomputes covariances, and repeats until convergence. This means the method is not a standard inductive classifier trained on the training set and then evaluated once on held-out data. It is using the full test input set at training/adaptation time. That can be acceptable if the paper clearly frames the method as transductive learning and compares against transductive baselines under the same access pattern. But that is not what happens here. In **Section 5**, the method is described as splitting data into 80:20 train/validation and then comparing CSVM to ordinary SVM kernels, yet the baselines do not seem to receive analogous access to unlabeled test inputs. This is a serious fairness issue in the empirical comparison, because the proposed method can adapt to the test distribution while the baselines cannot.

5. **The experimental setup is underspecified to the point that reproducibility and interpretation are both weak.**  
   The paper does not report several details that are essential for assessing the results: how hyperparameters for linear/RBF/sigmoid/polynomial SVMs were selected, what values of \(C\), kernel bandwidth, degree, and coef0 were used, whether features were standardized, whether the reported numbers are from one split or averaged over multiple random seeds, how class imbalance was handled, and what convergence threshold was used in the SM algorithm. On **Page 6**, the text says the dataset was split 80:20 into training and validation data, but later the algorithm refers to test data, and the distinction between validation and test is not maintained clearly. Without these details, the results in **Tables 1 to 4** are difficult to trust as evidence of superiority.

6. **The empirical gains are modest and not analyzed statistically.**  
   Looking at **Table 1** on Page 7, many improvements are tiny, for example 0.981 vs 0.979 on Pulsar and 0.744 vs 0.731 on Red Wine. Similar small deltas appear in **Tables 2 to 4**. There are no standard deviations, no confidence intervals, no repeated-split results, and no significance tests. On datasets like Breast Cancer and Pulsar, where several methods already achieve strong scores, a 0.002 absolute gain in accuracy is not enough to support broad claims about correcting a fundamental flaw in SVM geometry. The rhetoric of the paper is much stronger than the experimental evidence.

7. **The baseline set is not convincing relative to the paper's own claims.**  
   The method is positioned against "traditional SVM kernels" and generic whitening, but the introduction itself cites multiple variance-aware or covariance-aware SVM variants, including weighted Mahalanobis kernels, minimum class variance SVM, and Mahalanobis-based TSVM variants on **Page 2**. None of those methods appear in the experiments. If the paper claims to rectify gaps in prior covariance-adjusted SVM formulations, those are precisely the methods it should compare against. Otherwise, the reader cannot tell whether CSVM is actually better than prior covariance-aware approaches, or merely slightly better than untuned standard kernels on a handful of datasets.

8. **The paper's positioning against prior work is too sweeping and insufficiently evidenced.**  
   On **Page 2**, the authors state that analysis of prior optimization problems revealed "gaps in application of appropriate vector spaces and dimensional inconsistencies." That is a serious criticism of several prior papers, but no concrete examples are given in the main paper. Which equations are dimensionally inconsistent, and why? Without that, the paper reads as if it is dismissing prior work without doing the necessary scholarly work of precise differentiation. Relatedly, there is relevant prior literature on SVMs under alternative geometries and covariance-adjusted linear classification that would need tighter discussion if the paper wants to claim a new conceptual foundation rather than an implementation variant.

9. **The treatment of multi-class classification is speculative.**  
   **Lemma 2.2** on Page 4 states that an \(N\)-class problem yields \(N\) input spaces and \(N\) linear classifiers. But there is no multi-class method, no derivation of a training objective for \(N>2\), and no experiment beyond binary classification. Since the claim is presented as a general consequence of the theory, the lack of support matters. At present it reads as a conjectural extension rather than a demonstrated result.

10. **There are notation inconsistencies and mathematical sloppiness that make already-fragile arguments harder to follow.**  
   The paper switches between \(\Psi\) and \(\psi\) in **Equation (9)** on Page 4, uses \(\theta_{\text{Euclidean}}\) to compute a margin ratio but then applies it to shift the intercept of an input-space classifier in **Section 3**, and never clearly states whether \(\theta_{\text{Input}}\) and \(\theta_{\text{Euclidean}}\) are related by a fixed linear map. The algorithm also says "perform support vector classification on Train\(_1\) and Train\(_{-1}\) data in the Euclidean space," even though those two sets have been transformed differently. These issues are not merely stylistic; they obscure what model is actually being trained.

11. **Some of the figures raise interpretability questions rather than strengthening the case.**  
   In **Figure 2** and **Figure 3** on Page 8, the ROC curves for Red Wine, OSHA, and Diabetes are fairly close across multiple methods, and some curves look piecewise coarse, suggesting small sample effects or threshold granularity. Yet the paper draws strong conclusions such as validating the lemmas from these results. The figures support competitiveness, but they do not support the much stronger geometric claims. In other words, the visual evidence is being over-interpreted.

12. **The paper conflates “non-Euclidean space” in a broad geometric sense with standard vector spaces equipped with covariance-induced metrics.**  
   The submission repeatedly refers to the input space as non-Euclidean because Mahalanobis distance is more appropriate there. But a Euclidean vector space with a different inner product or a whitened coordinate representation is not the same as manifold-valued non-Euclidean data in the sense usually discussed in modern ML. This framing overstates the scope. It may mislead readers into thinking the paper addresses general learning on non-Euclidean domains, whereas the actual setting is ordinary tabular feature vectors with covariance-aware metric structure.

## Questions
1. The paper's empirical protocol is the single biggest issue for me. Is the proposed method intended to be **transductive**? In **Section 3**, the algorithm iteratively labels test datapoints and adds them to the training sets before recomputing covariances. If yes, please state this explicitly and compare against transductive baselines or at least transductive variants of the SVM baselines. If not, please explain how the reported experimental evaluation avoids test-time leakage.

2. Please provide a precise, unified decision function for an unseen sample \(x\). Given class-specific transforms \(\Psi_{+}^{-1}\) and \(\Psi_{-}^{-1}\), what exactly is the classifier that maps \(x\) to \(\{-1,+1\}\)? Right now the paper alternates between a transformed-space hyperplane and an input-space hyperplane with adjusted intercept, but the relationship is not rigorously defined.

3. Can the authors give an actual proof, or at least a much more careful derivation, for **Lemma 2.1** and **Lemma 2.3**? In particular, please justify the statement that KKT boundary conditions are "not valid" in the input space. A weaker and more defensible statement may be that using a covariance-aware metric changes the induced geometry of the margin, but that is different from invalidating KKT.

4. How were the baseline hyperparameters selected for the methods in **Tables 1 to 4**? Were all methods tuned by the same validation protocol? Please report \(C\), kernel parameters, preprocessing, and whether results are averaged across multiple random seeds. Without that, the current tables are hard to interpret.

5. Why are the covariance-aware SVM methods cited in the introduction not included in the experiments? A direct comparison against at least one Mahalanobis-distance or covariance-adjusted SVM baseline would materially increase my confidence.

6. The main claims are about geometry and margin structure. Can the authors add a simple synthetic 2D experiment showing how the proposed classifier differs from a standard SVM when class covariances are anisotropic? A figure of decision boundaries and margins would be much more diagnostic than only reporting scalar metrics on five datasets.

7. What happens when the sample covariance matrices are singular or ill-conditioned, which is common in high dimensions or with correlated features? Does the method use regularization, such as \(\Sigma + \lambda I\), before Cholesky decomposition? This is currently missing from the method description.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper itself. My concerns are scientific rather than ethical, especially around evaluation fairness and methodological clarity.

## Soundness Rating
2: fair. The paper has a plausible high-level idea and some empirical support, but the central theoretical claims are not adequately justified, and the evaluation protocol raises important validity concerns.

## Presentation Rating
2: fair. The paper is readable at a broad level, but the exposition is imprecise in the crucial mathematical parts, notation is inconsistent, and the experimental protocol is not described with enough detail.

## Contribution Rating
1: poor. The submission raises an interesting question, but the main claims are overstated relative to what is actually established, comparisons to the most relevant covariance-aware baselines are missing, and the empirical gains do not convincingly support the broader conceptual conclusions.

## Overall Rating
2: Reject, not good enough. The paper has an interesting intuition and some competitive numbers, but the current version does not provide a sound enough theoretical foundation or a fair enough empirical evaluation to support its main claims at ICLR standard.

## Reviewer Confidence
4: confident. I am confident in this assessment, though it is still possible I missed some intended interpretation because the paper's notation and geometric setup are not always precise.