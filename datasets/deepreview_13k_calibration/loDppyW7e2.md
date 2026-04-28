# Multi-Dimensional Conformal Prediction

- Decision: Accept
- Avg Score: 5.60
- Scores: 6, 6, 3, 8, 5

## Abstract
Conformal prediction has attracted significant attention as a distribution-free method for uncertainty quantification in black-box models, providing prediction sets with guaranteed coverage. However, its practical utility is often limited when these prediction sets become excessively large, reducing its overall effectiveness. In this paper, we introduce a novel approach to conformal prediction for classification problems, which leverages a multi-dimensional nonconformity score. By extending standard conformal prediction to higher dimensions, we achieve better separation between correct and incorrect labels. Utilizing this we can focus on regions with low concentrations of incorrect labels, leading to smaller, more informative prediction sets. To efficiently generate the multi-dimensional score, we employ a self-ensembling technique that trains multiple diverse classification heads on top of a backbone model. We demonstrate the advantage of our approach compared to baselines across different benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies a multi-dimensional non-conformity approach to conformal prediction. They introduce a novel method to identify high probability regions with low low false-to-true labels ratio, which requires to carefully design a calibration procedure with multiple stages, including partitioning the space, ranking different partitions, and selecting the high quality partitions.

### Strengths
This paper is very well-written and has a very clear flow. The multi-dimensional CP looks like a promising avenue of research. They provide a novel perspective of finding conformalized regions by ranking the false-to-true ratio and they also show sufficient experimental results to back up their claim about improving efficiency.

### Weaknesses
I believe this is a very good paper. Although I do have some suggestions to further improve both the theoretical and algorithmic perspectives.

- You break the dataset in two parts and then use the second part as a recalibration to ensure coverage. A natural way to improve the efficiency of your method and use all the data together is to use a leave-one-out method. At each time, you can use all the data but one (say X_i, Y_i), go through the partitioning and ranking and then find the smallest threshold (rank) such that the selected regions include the left-out sample (X_i, Y_i). Lets call that threshold (rank) tau_i. Then you can take (1-\alpha))-quantile of the ranks and use that as the final threshold (rank) to make the regions. There are some subtleties to make this work, you might want to look at https://arxiv.org/abs/1905.02928 for more details. 

- For the case of scalar scores there are some theoretical underpinnings that shows the optimal (think of it as the tightest possible) prediction sets are of the form of level-sets of a scalar function. (i.e., thresholding a scalar score) These results are considered classic in CP (look at https://www.stat.cmu.edu/~jinglei/LeiW14.pdf) and they have been also recently generalized to the more advanced case of CP with conditional coverage requirements (look at https://arxiv.org/pdf/2406.18814). These results and their insights also heavily contributed in the line of research around designing better scores. Therefore, I believe it is important to discuss whether a multi-dimensional score design has any fundamental theoretical underpinnings or not. For instance, it would be nice to think of a scenario where (in the population regime) the optimal prediction sets are actually characterized by a multi-dimensional score. Or maybe trying to show that in a (perhaps simplified) scenario the multi-dimensional perspective is provably a better approximation of the optimal prediction sets. These kind of results and discussions are more than just an effort for having some theory in the paper, but rather can bring useful insights for follow-up works in this line of research.

### Questions
I have no further questions. Might ask more once I see the authors response.

### Soundness
4

### Presentation
4

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
This paper proposes an extension to conformal prediction for classification tasks. Standard conformal prediction constructs prediction sets with guaranteed coverage by thresholding a nonconformity score, which measures the disagreement between the model and the ground truth class label. This work has two main contributions: (a) a variant of conformal prediction that is compatible with multidimensional nonconformity scores, and (b) a self-ensembling method for producing these multidimensional nonconformity scores using diverse classification heads. The proposed method partitions the multidimensional space and then selects a set of cells to include in prediction sets by thresholding the cells based on the relative frequency of false labels. The proposed approach is shown experimentally to lead to smaller prediction sets.

### Strengths
Strengths of the paper include the following:
- The main claims are supported with evidence. Theoretical justification for the proposed procedure is provided in Appendix A.1. Smaller prediction set sizes are also demonstrated in Figure 2 and Figure 3. However, see weaknesses below regarding multiple classification heads.
- There is a good amount of exploration performed, even beyond what is reported in the main paper. For example, results on standard ensembling, test-time augmentations, and size of $\mathcal{D}_\text{cells}$ are all useful.
- The paper is well-written. I thought the related work section in particular explored a good amount of relevant literature.

### Weaknesses
Weaknesses of the paper include the following:
- The empirical evidence provided in the paper is overall good, but the role of the multiple classification heads is still unclear. The best head baseline uses a network trained with multiple heads. How would the proposed approach compare to a vanilla conformal prediction baseline trained with a single head (i.e. the network prior to attaching the six additional classification heads)? It is unclear if the performance gains are due to the multidimensional approach or simply due to the increased capacity of the model with multiple heads.
- The contribution of the paper is fairly solid in terms of theoretical and empirical justification. However, from a practical perspective, it seems more likely that rather than investing time into using multidimensional nonconformity scores, a practitioner would likely simply focus on improving the underlying model generating the nonconformity scores. The cases in which the multidimensional approach succeed are those where the model is suboptimal, and fixing the model will remove the need to use multidimensional scores. This limits the significance of the proposed work. The authors should provide a more compelling argument for why a practitioner would choose this method over improving the base model.
- The benefits of the proposed approach are empirical in nature. There does not seem to be a way to know beforehand whether multidimensional nonconformity scores will help or not. In some sense, this is a modeling question that depends on the distribution of nonconformity scores in the multidimensional space. There will be some datasets where the modeling assumptions proposed here (analogous to a KNN variant with $K=1$) will be beneficial, and others where it will not be. This makes the method somewhat unpredictable in terms of its effectiveness, and it would be useful to have some guidelines on when to apply it.

### Questions
- Please see the first point under the weaknesses section about. How would the proposed approach compare to a vanilla RAPS/SAPS baseline with one classification head (i.e. before the six additional heads are attached)?
- In Figure 4, the nonconformity scores appear to be distributed in a pattern resembling a square. Would an L1 norm perform better than an L2 norm in this case?
- What is the effect on the algorithm as the dimensionality increases? Is there a curse of dimensionality effect here?
- In Algorithm 1 (line 6), when do the duplicate cells occur?

Minor comments:
- The cells in Figure 1 are difficult to understand.
- Figures 2 and 3 are small and therefore hard to read.
- Since Section 3.1 discusses background work, it should probably be moved out of Section 3, which is title "Proposed Method".

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
In this paper, the authors aim to improve the efficiency of conformal prediction sets with multiple non-conformity scores. In particular, they propose a multidimensional framework of conformal predictions, which uses a single score in one of the dimensions. They provide a theory to show the desired coverage can be guaranteed through the multidimensional selection. To obtain multiple diverse nonconformity scores, they employ a multi-head model and train it with a diversity regularization. The proposed method is validated on a CIFAR100, Tiny ImageNet, and PathMNIST to show the effectiveness.

### Strengths
1. The method is novel. To the best of my knowledge, this is the first work to utilize ensemble predictions as multidimensional score.
2. The empirical improvement is significant. The proposed method can produce smaller prediction sets compared to other baselines.

### Weaknesses
Major:
1. Why the multi-score conformal calibration can work better is not explained. The authors only provide a theorem to ensure the valid coverage of the proposed method, but do not elaborate about how it leads to efficient prediction sets. It could be better if they can provide convincing explanation in this aspect. Specifically, the paper lacks a clear explanation of how the proposed multidimensional approach leverages the diversity of the nonconformity scores to achieve tighter prediction sets. The theoretical guarantee of coverage is necessary but not sufficient to demonstrate the practical advantage of the method. The authors should provide a more intuitive explanation, perhaps through a toy example or a geometric interpretation, to illustrate how the multidimensional calibration space leads to more efficient prediction sets compared to using individual scores or their averages.

2, The multi-score setting seems different from previous works. Previous multi-score works aim to utilize multiple score functions to obtain better performance, but this work proposes the method to generate multiple scores with ensemble models. In my view, this problem should be CP for ensemble models instead of the multi-score setting. So it might be better for authors to rewrite the motivation (subsection 3.2) for avoiding misunderstanding. (Or the authors can show the method can also improve the setting of multiple score functions.) The current framing of the problem as a multi-score setting is misleading, as it primarily focuses on generating diverse scores from an ensemble rather than combining scores from fundamentally different sources. The authors need to clarify whether their method is intended to be a general approach for multi-score conformal prediction or specifically designed for ensemble models. If the latter is the case, the motivation should be rephrased to emphasize the ensemble aspect and its connection to existing ensemble CP methods. Furthermore, if the method is intended to be general, the authors should demonstrate its effectiveness in combining scores from different sources, such as different nonconformity measures, not just different heads of the same model.

3. The empirical comparison is not extensive. The authors should include ImageNet in the experiments, or it is hard to evaluate the effectiveness of the proposed method in large number of classes. The current experiments are limited to relatively small datasets, which might not fully reveal the potential and limitations of the proposed method. The authors should include experiments on a larger and more complex dataset like ImageNet to demonstrate the scalability and effectiveness of the method in a more realistic setting. This is particularly important given the method's reliance on high-dimensional calibration, which might behave differently with a larger number of classes and more complex data distributions.

Minor:
1. presentation: it is hard to read the information from Figures 2 and 3. Maybe the authors can simply provide tables to show the results.
2. It might be better to put some results in Appendix B in the main part, as there is almost one page left as blank.

### Questions
In figure 2, are all the compared methods employed on the multi-head model trained by the loss in Equation (11)?

### Soundness
1

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper tends to combine several different conformity score functions aiming to reduce the prediction set size. In short their approach is to combine different score functions per $(x, y)$ forming a vector of scores. Dividing the calibration set into two separate sets of re-cal and tuning set, they use the tuning set as the basis (centroids) in the mutli-dimensional scores space. They assign a rating to each of these centriods based on the proportion of false labels inside that area (this means 1 + set size if there is only one point at the place). During calibration they deactivate regions in decreasing order to the number of false predictions, as long as the $1 - \alpha$ coverage is satisfied. Each calibration point is assigned to the closest centriod. Similarly during test. they check the closest centiod and add the label to the prediction set if the centriod is active.

The propose different methods to build multi-dimensional score including using different classification heads, to simply using different score functions.

### Strengths
The method is simple yet effective. The paper is also easy to read and “to the point”. I do not see any major flaw or discouraging point in it. I also see that the authors tried to include a comprehensive evaluation by comparing with best head, uniform average and optimized weights.

### Weaknesses
1. Why the authors did not report worst slice coverage which is metric of adaptivity?
2. Why the authors used an unnecessarily large calibration set? I don’t think the evaluation setup is realistic with 16500 calibration points to predict 11000 test points. What is the gain of this large calibration set? Is there any statistical efficiency results that are missing?
3. Related to the previous problem, a fair comparison is to report paper’s best method in comparison with the normal best method where the tuning set is also added to the calibration set. The results are not expected to be significantly different but still this is important to be reported.
4. Why the authors did not report their result with APS and threshold prediction sets? Although there are adaptivity and efficiency constraints, still those result are important to be reported. RAPS and SAPS are ignoring informations in the logit space either by penalty, or just reporting the rank, and intuitively in a perfect classifier this should cause inefficiencies.
5. Is there any preference to have 0-1 assignment to the zones?, the author could also try soft probability assignment to each region and optimize for that. It is not a must, but either trying soft centroid assignment, or showing that the optimal is happening with the current 0-1 assignment would make the work stronger.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a multi-dimensional conformal prediction method for classification problems. A nonconformity measure is defined depending on the multiple scores, which leads to finer separation between correct and wrong labels. The proposed procedure mainly includes three steps: first, partitioning the score space into cells using $D_{cells}$; second, scoring and ranking the cells according to the ratio of false to true labels; and third, calibration-achieved by progressively adding top-ranked cells until the desired coverage level is reached.

### Strengths
The paper is well-organized. The problematic and approach are well introduced, and the concept concisely presented. The proposed method successfully extends conformal prediction into a multi-dimensional setting with enhanced separation between correct and incorrect labels, and it appears sufficiently general.

### Weaknesses
1. The experiments mainly focus on image classification datasets (e.g., CIFAR100, Tiny ImageNet, PathMNIST), limiting the demonstration of the other data types, such as text or tabular data.

2. While the paper is claimed to be cost-efficient, it still involves training and managing multiple classification heads, which could be computationally expensive for large-scale datasets or resource-constrained environments. Could you provide more insights into the computational cost? Specifically, how does it compare to other baseline methods?

### Questions
How sensitive is the method to hyperparameter choices, such as the number of classification heads or diversity regularization? And how do different configurations affect set size?

### Soundness
3

### Presentation
3

### Contribution
2
