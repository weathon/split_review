# Improving Deep Regression with Tightness

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
For deep regression, preserving the ordinality of the targets with respect to the feature representation improves performance across various tasks. However, a theoretical explanation for the benefits of ordinality is still lacking. This work reveals that preserving ordinality reduces the conditional entropy $H(Z|Y)$ of representation $Z$ conditional on the target $Y$. However, our findings reveal that typical regression losses do little to reduce $H(Z|Y)$, even though it is vital for generalization performance.  With this motivation, we introduce an optimal transport-based regularizer to preserve the similarity relationships of targets in the feature space to reduce $H(Z|Y)$. Additionally, we introduce a simple yet efficient strategy of duplicating the regressor targets, also with the aim of  reducing $H(Z|Y)$.  Experiments on three real-world regression tasks verify the effectiveness of our strategies to improve deep regression.  Code will be released upon paper acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work addresses the fundamental yet underexplored problem of regression, arguing that limited research attention has been devoted to it compared to classification tasks. The authors posit that conditional entropy H(Z|Y) , which is extensively studied in information bottleneck, is important for regression problem. They term this entropy measure “tightness” and argue that minimizing it is essential for regression tasks.  Towards tighter representations, the authors propose two strategies, which are multi-target and an optimal transport-based regularize. Experimental results show that both of the proposed strategies can improve the regression performance.

### Strengths
+ The proposed method achieves superior performance compared to prior deep regression techniques on two benchmark datasets, demonstrating its effectiveness.

+ The authors provide an interesting analysis on why ordinal feature spaces are not naturally learned under typical regression loss functions, highlighting a crucial aspect often overlooked in regression tasks.

+ The authors offer a comparison between classification and regression, explaining why classification losses tend to better constrain (or “tighten”) representations, which may help readers understand the distinct requirements of these tasks.

### Weaknesses
Although the authors discuss why minimizing Mean Squared Error (MSE) may fail to learn ordinal feature spaces, they do not provide empirical results or visualizations, such as t-SNE plots, to support this claim. Comparative visualizations between the proposed method and RankSim would strengthen the discussion

Inconsistency between Eq 3 and Eq 5 – Should both of them be from the batch level? For example, change N to b?

The rationale for employing multiple regressors is unclear. Why is a multi-regressor approach potentially better than a single one? Is this analogous to an ensemble method? Additionally, will the different ranges of Y affect the selection of M?

In [1], the authors discuss the neural collapse phenomenon can be similarly achieved by deep networks when minimizing MSE, which seems somewhat contradictory to statements made in the current paper. Is this contrast due to the nature of the target label (discrete versus continuous)? Expanding on this point with further discussion and comparison would add clarity.

### Questions
Please see the weakness.

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
1

### Summary
The paper proposes enhancing deep regression by preserving the ordinality of target values within the feature representation space, which is linked to reducing the conditional entropy between the learned representation and the taget. Given typical regressors struggle to naturally reduce the conditional entropy, they propose two solutions for the problem. The first is to use augmenting for the target to mimic training in classifition, so that the model parameters can be with more flexible and diverce updating directions. The second is to use ptimal transport to encourage the similarity between target and feature spaces. Results in some real-world tasks demonstrate the effectiveness of their solutions.

### Strengths
1. The paper is overall well-written. The proposal of linking conditional entropy with ordinality preserving  in regression also seems new and interesting.

2. The authors propose the ROT Regularizer and a multi-target learning strategy, both of which are innovative methods for improving regression. These techniques address the limitations of standard regression by refining the feature space structure and better preserving relationships among targets, enabling more robust and accurate predictions.

### Weaknesses
I have limited knowledge in this specific area and currently lack the expertise to identify any potential weaknesses in the paper. The overall manuscript appears satisfactory to me. The authors may gain additional insights for refinement through feedback from reviewers more experienced in this topic.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a deep regression method focusing on the tightness of features.
The authors found that the tightness of features is important but not sufficiently optimized in normal regression training 
because the updated directions of features are limited in normal regression training.
Based on this finding, the multiple target (MT) strategy and regression optimal transport regularizer (ROT-Reg) are proposed to promote tightness during training.
MT increases the number of regression heads so that features are updated toward various directions.
ROT-Reg closes the topology gap between features and targets via self-entropic optimal transport.
Experimental results show that the proposed methods improved the tightness of features and regression performance.

### Strengths
- S1: The finding that the updated directions of the features are limited in normal regression training is intriguing.
- S2: The finding is theoretically supported.
- S3: The paper is well-organized and easy to follow.

### Weaknesses
 - W1: The difference between the global and local tightness is ambiguous. While $\mathcal{H}(\mathbf{Z}|\mathbf{Y})$ is called tightness, formulating the global and local tightness would strengthen the theoretical analysis.
- W2: The justification of design choices of the proposed methods needs to be clarified.     
  - For MT, is there a possibility that the multiple regressors will collapse into a single solution? Are the solution spaces $S_y$ orthogonal?   
  - For ROT-Reg, is the self-entropic optimal transport the best choice? For example, one may simply minimize the gap of affinity matrices in Eq. (9).
- W3: The performance improvement by the proposed method is marginal. For instance, in Tab. 2, why did incorporating MT and ROT-Reg underperform MT?
- W4: It would be beneficial to visualize the improvement of tightness not only in toy datasets but also in real-world datasets with e.g., PCA.
- W5: Displaying the regression performance in Tab. 4 would be helpful to strengthen the efficacy of tightness on the performance.
- W6: There are many typos. For instance,    
  - L185: $\partial$ is missing in partial derivative   
  - L113: differentiable entropy -> differential entropy?   
  - L252: "$"="$ -> "$\in$" ?   
  - L317: "performance the performance"

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
