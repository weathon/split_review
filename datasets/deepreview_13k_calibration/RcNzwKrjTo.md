# Conformal Prediction Sets with Improved Conditional Coverage using Trust Scores

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3, 5

## Abstract
Standard conformal prediction offers a marginal guarantee on coverage, but for prediction sets to be truly useful, they should ideally ensure coverage conditional on each test point. However, it is impossible to achieve exact, distribution-free conditional coverage in finite samples. In this work, we propose an alternative conformal prediction algorithm that targets coverage where it matters most---in instances where a classifier is overconfident in its incorrect predictions. We start by dissecting miscoverage events in marginally-valid conformal prediction, and show that miscoverage rates vary based on the classifier's confidence and its deviation from the Bayes optimal classifier. Motivated by this insight, we develop a variant of conformal prediction that targets coverage conditional on a reduced set of two variables: the classifier's confidence in a prediction and a nonparametric trust score that measures its deviation from the Bayes classifier. Empirical evaluation on multiple image datasets shows that our method generally improves conditional coverage properties compared to standard conformal prediction, including class-conditional coverage, coverage over arbitrary subgroups, and coverage over demographic groups.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on the issue of covariate-conditional properties of conformal prediction methods. They build upon the method introduced by [Gibbs et. al. 2023] by introducing a function class that can be optimized for improving conditional validity. The main guiding principle is to estimate a low dimensional function from data such that it indicates the covariates that are more likely to have poor uncertainty quantification. They propose the discrepancy between the bayes optimal classifier and the predictor at hand as a proxy for poor uncertainty quantification, hence they build their function class based on trust scores which captures this discrepancy. They also have some empirical evidence for the good performance of their approach.

### Strengths
- The issue of conditional validity is central in study of conformal prediction methods. This issue particularly becomes severe in high dimensions (input dimension), which is the exact focus of the paper where they try to learn low dimensional signals as proxies for poor uncertainty quantification.
- The paper is well-explained and well-positioned within the recent advancements in the CP community.

### Weaknesses
 - Despite the motivations, it is not clear if the notion of trust scores can effectively capture the complexities of miscoverages of different covariate points. In particular, it would have been very helpful to see some theory, at the very least in the large data regimes, that the trust scores are sufficient to capture (at least approximately) conditional coverage. The field of conformal prediction has always been developed with strong theoretical underpinnings that ensures reliable uncertainty quantification.
- With the lack of theoretical support, the extent of empirical evaluation is very important. I believe there should be a larger scale comparison with other existing approaches in the literature. For instance, one straightforward method that is an immediate rival to yours is to pick the function class of Gibbs et. al. to be a linear head on top of the representation layer of the trained classifier. Similarly, one can also use a linear head on top of any foundational model (like CLIP). These methods also bring down the dimension of the problem to low dimensional rep. layer and might actually work very well in practice. 
- In regards of related works coverage, there are some holes that are good to be covered. For instance, this idea of learning features from the data (like trust scores) that are beneficial for conditional coverage is not entirely new. For instance, https://arxiv.org/abs/2404.17487 also looks at the problem from the same angle, and this is just an example! There should be at least a paragraph to cover works like this and distinguish the difference in their methodologies and yours.

### Questions
No further question. Might ask some after seeing the authors response.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper "Conformal Prediction Sets with Improved Conditional Coverage Using Trust Scores" presents a novel method to enhance conformal prediction by targeting conditional coverage where it is most needed. Standard conformal prediction provides a marginal guarantee on coverage but may fail to deliver meaningful coverage for individual predictions, especially for cases where a model is overconfident in incorrect predictions. To address this, the authors propose a new conformal prediction approach that incorporates a model's confidence and a nonparametric trust score as variables to approximate conditional coverage. This modified approach adapts prediction sets based on the classifier's deviation from the Bayes optimal classifier, ensuring that high-uncertainty cases receive more reliable coverage. The approach is validated through experiments on multiple datasets, including ImageNet and a clinical dataset for skin condition classification, where it improves conditional coverage properties across various subgroups.

### Strengths
The paper effectively addresses a significant limitation in standard conformal prediction by focusing on cases where a model's confidence may not be trustworthy. This targeted approach for conditional coverage enhances the practical utility of prediction sets, especially in high-stakes applications where overconfident errors can lead to critical consequences.

By incorporating trust scores as an indicator of the model's agreement with a Bayes-optimal classifier, the authors introduce a practical, interpretable method to approximate conditional coverage. This is a valuable innovation, providing a robust alternative to exact conditional coverage, which is often infeasible in high-dimensional settings.

The method is tested across diverse datasets, including ImageNet, Places365, and Fitzpatrick 17k, demonstrating its effectiveness in various contexts and its robustness in improving conditional coverage, even in settings with significant class imbalance or demographic subgroups.

### Weaknesses
The method's reliance on confidence and trust scores may limit its applicability in settings where these measures do not align well with true conditional coverage. Trust scores, while intuitively appealing, may not fully capture cases where model predictions deviate from true labels, particularly in datasets with noisy or ambiguous labels, or in cases where the model's errors are not well-correlated with the distance to class prototypes. For instance, if a model consistently misclassifies a specific subset of a class due to a subtle feature it fails to learn, the trust score might not reflect this systematic error, leading to under-coverage for those instances. 

The algorithm requires calculating trust scores and confidence measures across potentially large datasets, which may limit scalability, especially when dealing with high-dimensional feature spaces. While the authors mention using FAISS for nearest neighbor search, the computational cost of constructing the index and performing searches for each sample, particularly with higher-degree polynomial functions in the function class, could still be substantial. The practical implications of this computational overhead, especially in real-time or resource-constrained environments, are not fully addressed. 

The chosen conditional coverage thresholds and sub-intervals for confidence and trust scores could be difficult for practitioners to interpret or set in a new application context. The method relies on binning samples based on confidence and trust scores, and the choice of bin sizes and boundaries can significantly impact the resulting conditional coverage. The paper lacks clear guidance on selecting these thresholds, and the sensitivity of the method to these choices is not fully explored. This makes it challenging to apply the method effectively without extensive experimentation. 

Although the method is well-tested on image datasets, its performance in non-image domains (e.g., NLP or tabular data) is unexplored. This limits the generalizability of findings, especially since confidence and trust scores might behave differently in these contexts. For example, in text classification, the notion of a 'nearest neighbor' in the embedding space might not be as semantically meaningful as in image space, and the relationship between confidence and misclassification may be less direct. 

While the use of multiple metrics provides detailed insights into conditional coverage, it may be cumbersome for practitioners to apply all of these metrics in practice, especially when assessing model performance quickly. The paper presents several metrics, such as coverage within different bins, and overall conditional coverage, which may require significant effort to compute and interpret, potentially hindering the practical adoption of the method.

### Questions
How would you recommend adapting this approach if confidence or trust scores are not reliable indicators of miscoverage in a specific domain?


Could you provide more detail on how the bins for confidence and trust scores are chosen? Are there recommended strategies for selecting bin thresholds for different datasets?

Have you considered evaluating the method on datasets from non-image domains, such as text classification or structured tabular data? How do you expect the trust score approach to generalize to these contexts?

Have you performed any benchmarks on the computational complexity of the method, particularly when calculating trust scores and confidence thresholds in high-dimensional datasets?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a conformal prediction approach for classification aimed at improving conditional coverage properties. While achieving finite-sample X-conditional coverage guarantees is nearly impossible, the authors propose a method that provides V-conditional coverage guarantees, where V is a simplified representation of X. This representation partitions the instance space into regions based on model confidence (mode of the predicted probability distribution) and the rank of the true label. Since the rank of the true label is unknown for unobserved test instances, the authors use a reliability or trust score to approximate the model’s performance relative to the Bayes predictor.

### Strengths
The paper is well-written, easy to follow, and addresses an important challenge in conformal prediction: the lack of conditional coverage. The proposed method is theoretically sound and practically applicable, as demonstrated by the experimental results.

### Weaknesses
1. Although the trust scores were intended to be a proxy of rank function, experimental results—comparing the coverage gaps between the Conf×Trust and Conf×Rank columns in all tables—indicate this was not achieved. Additionally, the proposed method’s improvement over the Naive approach in terms of the Conf×Rank coverage gap is consistently negligible, suggesting that the method may not be particularly effective.

2. The comparison of the average set size between the Naive approach and the proposed method suggests that the proposed approach becomes overly conservative in many cases while offering only a minimal benefit in terms of the desired conditional coverage.


3. Even though the current evaluation metrics in Section 4 are interesting, given the paper's aim to improve X-conditional coverage, it would have been helpful to include additional metrics used in other studies, such as WSC from the APS paper or SSCV from the RAPS paper.

### Questions
The proposed approach requires discretization of the space V. Have the authors explored the effect of different discretization methods?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on a fundamental limitation in conformal prediction: while providing marginal coverage guarantees, it lacks conditional coverage properties critical for reliable uncertainty quantification. The authors propose a novel approach that leverages model confidence and trust scores to achieve approximate conditional coverage, particularly targeting instances where classifiers exhibit overconfidence in misclassifications. Their method demonstrates superior empirical performance on large-scale vision datasets while maintaining theoretical guarantees, advancing the practical applicability of conformal prediction in high-stakes applications.

### Strengths
- The paper's motivation is clear and the writing is well-organized, making it easy to follow.
- The extensive reproducibility of the experiment is greatly appreciated.
- The proposed method improves conditional coverage significantly, though at the cost of larger prediction set sizes.

### Weaknesses
 - The Proposition 1 is strict. As shown in  Proposition 1, higher temperature has larger prediction sets. However, this seems inconsistent with prior works [1] where the relationship between temperature and set size is not monotonic. Moreover, Proposition 1 implies that as temperature approaches infinity, the set size would converge to the total number of classes. Could the authors provide a more comprehensive discussion on how different temperature values (both small and large) affect the method's performance? Specifically, the constraint on \hat{q} in Proposition 1 seems unrealistic, as \hat{q} should vary with temperature. My own experiments show that at high temperatures, the average set size decreases as temperature increases, which contradicts the claim that overconfident models concentrate probability mass on fewer classes, leading to smaller sets. Overconfident predictions can exhibit long-tailed probabilities, resulting in larger prediction sets for APS. Furthermore, the paper should clarify the purpose of comparing coverage probabilities at different temperatures in Proposition 1, as it is unclear how this relates to the overall work. It would be more useful to compare coverage probabilities of two samples under a fixed temperature, similar to the results in Figure 1.
- The experiments are limited. While the proposed method achieves better conditional coverage, it comes at the cost of larger prediction set sizes. For a fair comparison, the authors should include results from relevant baselines such as Cluster CP [2] and Mondrian CP [3]. Additionally, experiments on datasets with fewer classes (like CIFAR10 and CIFAR100) would be valuable, especially since Mondrian CP has demonstrated strong class-conditional coverage performance on these datasets. Next, the ablation analysis about k of k-NN radius in trust score computation would be helpful.

### Questions
- Are authors using the non-randomized version of RAPS in Appendix C.4, similar to how authors implemented APS?
- For the long-tailed datasets (ImageNet-LT and Places365-LT), do the test sets maintain the same imbalanced distribution? If so, this could lead to unreliable evaluation metrics for minority classes due to insufficient test samples. Have authors considered this potential bias in evaluation?
- Since the trust score is computed using features from the model's penultimate layer, could we explore using alternative encoders for trust score calculation? A better encoder might provide more discriminative features, potentially leading to more accurate trust scores and consequently smaller prediction sets.

### Soundness
3

### Presentation
3

### Contribution
2
