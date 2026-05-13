# Feature-Specific Coefficients of Determination in Tree Ensembles

- Decision: Reject
- Scores: 8, 3, 6, 3, 8

## Abstract
Tree ensemble methods provide promising predictions with models difficult to interpret. Recent introduction of Shapley values for individualized feature contributions, accompanied with several fast computing algorithms for predicted values, shows intriguing results. However, individualizing coefficients of determination, aka $R^2$, for each feature is challenged by the underlying quadratic losses, although these coefficients allow us to comparatively assess single feature's contribution to tree ensembles. Here we propose an efficient algorithm, Q-SHAP, that reduces the computational complexity to polynomial time when calculating Shapley values related to quadratic losses. Our extensive simulation studies demonstrate that this approach not only enhances computational efficiency but also improves estimation accuracy of feature-specific coefficients of determination.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Coefficients of determination, R2,  represents the total variation explained by a feature. However, its computation for the datasets with huge number of features is challenging due to the underlying quadratic loss. This study introduces the Q-SHAP algorithm, a novel approach for calculating Shapley values in tree ensembles to decompose R2 and  speed up its computation.  The goal is to reduce the computational complexity to polynomial time when calculating Shapley values related to quadratic loss terms. The proposed approach leverages tree structure, polynomial-based calculations and the Inverse Fast Fourier Transform (IFFT). 

Polynomial representation is computed by defining a polynomial based on the product of weights for features along the paths to leaves. Specifically, for each pair of leaves, calculate the union of their feature sets and the size of this union to identify the features involved in the paths to these leaves. To calculate the contribution for each feature in the combined feature sets, the algorithm considers a normalization coefficient to balance the contribution of each feature, proportional to the total number of features in the combined set. After applying a weight adjustment, the algorithm predicts each feature’s individual impact on the overall prediction by estimating the contributions through the coefficient polynomial, which aggregates these contributions to simplify the prediction process for the subset of features. 
The polynomial representation of feature contributions allows QSHAP to take advantage of IFFT, which is helpful for calculating the dot product of the polynomial representations of feature contributions. By applying IFFT, it  can quickly compute aggregated Shapley values over multiple leaves and trees, which is faster than directly summing or iterating over each possible combination. The paper has conducted experimentation on synthetic as well as real datasets.

### Strengths
Scalability of the proposed approach: QSHAP achieves polynomial-time complexity, making it computationally feasible to use in large datasets and high-dimensional models. This efficiency is particularly advantageous compared to previous Shapley value methods that are NP-hard in general. 

Theoretical foundation: The authors provide mathematical proofs, such as the use of polynomial forms.

### Weaknesses
Dependency on Tree Structure: The algorithm’s design leverages specific tree-based model properties, consequently, QSHAP may not directly generalize to non-tree ensemble methods. This is a significant limitation, as many state-of-the-art models are not tree-based, such as neural networks or support vector machines. The lack of adaptability to these models restricts the broader applicability of the proposed method. 

The authors need to simplify and better explain the part that they have computed the polynomial representation, using meaningful step wise flowchart, figures, etc. The current explanation is difficult to follow, especially regarding how the feature weights are derived and how they contribute to the final polynomial. The description lacks a clear, step-by-step breakdown of the process, making it hard to understand the core mechanics of the algorithm.

### Questions
The part that you explain about predicting polynomial representation needs a one paragraph summary in the beginning with a justification of the choices you have made, all in one place. The reader gets some ideas before going through all the formulas. Specially explaining how do you handle situations where features appear multiple times along the paths to the leaves? Does this affect the weight assignment for these features?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes an extension of Shapley values to decision tree ensembles for quadratic losses for the whole training set. Similar to TreeSHAP, it exploits the tree hierarchy in calculation. Experiments are performed on simulations studies and on a real genome data.

### Strengths
The is the first paper that adapts Shapley values for tree ensembles for quadratic losses, which can be used to estimate coefficient of determination globally for the whole training set.

### Weaknesses
1. The motivation of the paper is not clear. Shapley values by itself are quite controversial in terms of an interpretability tool, and using it globally to estimate coefficient of determination is not clear.
2. The paper is hard to follow. The actual algorithm is presented in Sections 3.3 and Section 4 which is only one page. It is not obvious how it is different from the previous work.

### Questions
Does the algorithm exactly estimate the Shapley values or approximately?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present Q-SHAP, a polynomial-time algorithm for computing Shapley-valued-based individual feature contributions to R^2 for tree ensemble models for a dataset in aggregate (as opposed to using Shapley to explain individual predictions). R^2 decomposition is expressed in terms of Shapley values for model predictions and squared model predictions for individual data points and then summed over the data. The authors leverage the piecewise-constant prediction surface of trees within individual leaves and apply the inverse fast fourier transform to achieve polynomial-time computation .Q-SHAP is shown to do a better job than 2 competing methods of estimating R^2 feature importance for a collection of toy problems of 3 variables where ground truth is known.  Q-SHAP is also illustrated on one real world bioinformatics gene expression problem where the number of features (17k) far exceeds the number of data points (551).

### Strengths
The work is original to the best of my knowledge. Given the large volume of ML papers in recent years, it's possible that there are other polynomial time methods for the same problem, but I'm not aware of them. 

I think the paper clearly has enough significance to merit acceptance at ICLR. Tree ensembles such as gradient boosting machines (XGBoost, etc) continue to be state of the art for tabular problems, as evidenced in their prevalence in winning Kaggle competitions. Feature importance is certainly a significant topic for such models. It's quite worthwhile to be able to do a Shapley decomposition at the dataset level to explain R^2 contributions of features for such models. 

The clarity of the paper could be improved (see my comments in weaknesses) but is near the adequate range for acceptance.

### Weaknesses
I think the experimental results are a little thin. There is only one real-world example in the paper. I realize that you can't really get ground-truth for feature importance for real world problems, so that does make it somewhat less important to have results on a large collection of real datasets than for a paper where predictive accuracy is the main contribution. Even so, I would have preferred to see the paper illustrated on at least one more problem. The gene expression problem seems quite extreme in terms of having number of features >>> number of data points. I realize that large feature sets may be the area where Q-SHAP shines, but results on a 2nd problem which is not such an outlier in terms of number of features would have been nice.

While I realize that there is plenty of interest in Shapley and that Shapley is the unique solution to a set of key desiderata, I also would have appreciated more illustration of the failings of a method like feature permutation importance, given how prominent that method is. I'm not familiar with the Ishwaran paper that is cited, but it's not in a well known ML journal (by the way Electronic Journal of Statistics has a misspelling in the citations.."Elecctronic" ).

I also have several typo/rewrite suggestions:

page 2

for any set of feature -> for any set of features

and dummy? "null player" is I think a more standard term for that Shapley criterion.

page 3

lies on the fact -> lies in the fact

Fig 2 caption hypothetic -> hypothetical

Page 8

maximum depth of Models -> maximum depth of models

Page 9
based the result-> based on the result

quadartic -> quadratic

### Questions
Do you have results on another real-world problem?

Can you explain in more detail the failings of permutation importance and how a Shapley approach would be better, with a concrete example?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new algorithm, Q-SHAP, designed to efficiently calculate feature-specific coefficients of determination in tree ensemble models. This algorithm addresses the computational challenges associated with Shapley values for quadratic loss, particularly in high-dimensional data contexts where calculating feature contributions becomes complex and computationally intensive. By leveraging tree structure, Q-SHAP reduces the time complexity to polynomial time, making it feasible for large datasets and models. The contributions of Q-SHAP include:

- Q-SHAP reduces complexity, enabling fast computation of feature-specific R^2.

- Extensive simulations show Q-SHAP's superiority in estimating feature-specific R^2 over existing methods.

### Strengths
- The paper introduces a novel algorithm, Q-SHAP, which specifically addresses the computational challenges of calculating feature-specific R^2 within tree ensembles.

- The paper explains the underlying motivation well and presents its contributions in a structured, sequential manner, making it easier for readers to follow.

- The authors conduct comprehensive simulations to test the algorithm's performance across various scenarios, demonstrating Q-SHAP’s accuracy and computational efficiency compared to well-known methods like SAGE and SPVIM.

### Weaknesses
 - While the paper acknowledges related methods like SAGE and SPVIM, it could better contextualize Q-SHAP's theoretical advantages over these approaches. Specifically, the paper could benefit from a more detailed comparison of the mathematical foundations and computational complexity of Q-SHAP versus these methods. Including a table or diagram that compares the key theoretical aspects, limitations, and unique benefits of each method would make Q-SHAP’s improvements clearer to readers.

- The paper mentions that Q-SHAP’s framework might be extendable to other quadratic loss functions, but it doesn’t explore this idea in depth. This is a missed opportunity to underscore the broader relevance of the algorithm, as generalizability can increase impact across various applications in machine learning and data science.

- Although the paper includes a real-data example (prostate cancer gene expression data), the experiments could further explore different types of datasets to stress-test Q-SHAP’s robustness across diverse scenarios. For instance, it would be informative to see how Q-SHAP performs in datasets with imbalanced classes, highly correlated features, or extreme high-dimensional spaces.

- While the paper demonstrates that Q-SHAP is computationally faster than SAGE and SPVIM, it lacks specific breakdowns of how time complexity is reduced in different stages of the computation. Additionally, it would be useful to know how Q-SHAP’s runtime scales with an increasing number of features or trees, beyond the static benchmarks shown.

### Questions
The main issues have been highlighted in the section addressing weaknesses, but additional questions remain:

- Could you provide more insights or a breakdown of how polynomial time complexity is achieved within Q-SHAP? Specifically, a step-by-step breakdown of the algorithm, highlighting which specific operations contribute most significantly to reducing time complexity compared to existing methods, would clarify where the computational gains arise. This detailed explanation would make the efficiency improvements more actionable and understandable.

- Given Q-SHAP's improvements in feature-specific R^2 calculations, how does this translate to increased interpretability or trust in model predictions? Concrete examples or case studies where the improved accuracy of Q-SHAP’s feature-specific R^2 calculations enhances decision-making or model interpretation in real-world scenarios would help readers understand the practical impact of the method. For example, demonstrating applications in high-stakes fields like healthcare or finance would illustrate how Q-SHAP’s outputs can directly benefit practitioners.

- Are there limitations of Q-SHAP that practitioners should be aware of when using it on different types of tree models? A specific section dedicated to discussing Q-SHAP's limitations and potential pitfalls would be helpful. This could include guidelines on when Q-SHAP might not be the best choice, as well as precautions users should take when applying it to various tree model variants. Such a section would provide practical insights and help manage expectations for different use cases.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors developed an algorithm Q-SHAP for fast and accurate
computation of Shapley features scores for regression problems, for
tree-based models like Gradient Boosted Machines. The algorithm is
evaluated using 3 synthetic and one real dataset, and is orders of
magnitude faster than comparator methods.

### Strengths
- important problem

- creative and computationally very efficient solution

- well-written manuscript

### Weaknesses
 - relatively limited evaluation (3 synthetic datasets, one real with
  somewhat discordant results - see Questions section)

### Questions
For the real data (Gleason score), there is a great match between top
15 features for Q-SHAP and SAGE, but mismatch between the two and
SPVIM. Can the authors comment on this discrepancy?

### Soundness
3

### Presentation
4

### Contribution
3
