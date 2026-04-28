# Understanding Matrix Function Normalizations in Covariance Pooling from the Lens of Riemannian Geometry

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Global Covariance Pooling (GCP) has been demonstrated to improve the performance of Deep Neural Networks (DNNs) by exploiting second-order statistics of high-level representations. 
GCP typically performs classification of the covariance matrices by applying matrix function normalization, such as matrix logarithm or power, followed by a Euclidean classifier. 
However, covariance matrices inherently lie in a Riemannian manifold, known as the Symmetric Positive Definite (SPD) manifold. The current literature does not provide a satisfactory explanation of why Euclidean classifiers can be applied directly to Riemannian features after the normalization of the matrix power. To mitigate this gap, this paper provides a comprehensive and unified understanding of the matrix logarithm and power from a Riemannian geometry perspective. The underlying mechanism of matrix functions in GCP is interpreted from two perspectives: one based on tangent classifiers (Euclidean classifiers on the tangent space) and the other based on Riemannian classifiers. Via theoretical analysis and empirical validation through extensive experiments on fine-grained and large-scale visual classification datasets, we conclude that the working mechanism of the matrix functions should be attributed to the Riemannian classifiers they implicitly respect.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper provides a theoretical understanding of matrix function normalization in Global Covariance Pooling (GCP) from the perspective of Riemannian geometry, specifically addressing the use of matrix logarithm and power for classifying covariance matrices. By interpreting these matrix functions through Riemannian and tangent classifiers, the authors reveal that the efficacy of GCP is rooted in its respect for the Riemannian structure of Symmetric Positive Definite (SPD) matrices. Extensive experiments demonstrate that matrix power, often more effective in practical applications, implicitly respects a Riemannian classifier, justifying its empirical performance in GCP.

### Strengths
- The paper offers a unified theoretical explanation of the working mechnism of matrix functions which demonstrates that matrix functions in GCP are implicitly Riemannian classifiers. Based on the unified theoretical analysis, it also shows that the empirical advantages of matrix power over matrix logarithm in the GCP could be attributed to the characteristics of the underlying Riemannian metrics.
- The paper experimentally validates that the mechanism of matrix normalization should be attributed to Riemannian classifiers instead of tangent classifiers across different datasets and networks.

### Weaknesses
 - In sec. 5.3, the analysis shows that the matrix power function inherently offers better performance over the matrix logarithm based on its associated Riemannian metric ((θ, 1, 0)-EM). The description of (θ, 1, 0)-EM as a “balanced” alternative to LEM might be overly simplified. The analysis could benefit from a more nuanced discussion of the limitations of each metric, such as specific conditions where (θ, 1, 0)-EM may not perform as well as LEM. Specifically, the paper lacks a discussion on the potential for the power metric to introduce distortions in the feature space, especially when the power parameter is not carefully chosen. A more detailed analysis of how the choice of power affects the geometry of the embedding space would be beneficial. For example, how does the power parameter influence the geodesic distances between covariance matrices and the resulting classification performance?
- In sec. 6.1, although ScalePow-EMLR is claimed to be equivalent to Pow-EMLR under scaled settings, the analysis lacks a comprehensive justification for this equivalence. Exploring how different scaling factors impact performance would help. The paper should provide a more rigorous proof or empirical evidence to support the claim of equivalence. It is unclear if this equivalence holds under all conditions or if there are specific scenarios where the scaling factor might introduce variations in performance. Furthermore, the paper does not discuss the potential impact of the scaling factor on the optimization landscape, which could be relevant to the training process.
- The paper primarily evaluates ResNet-based architectures. How well would the findings generalize to other architectures, such as ViT. The study should include experiments on a wider range of architectures to demonstrate the robustness of the proposed theoretical framework. The current focus on ResNet limits the generalizability of the conclusions. It is important to assess whether the observed behavior of matrix power and logarithm functions is consistent across different network architectures, especially those with different inductive biases.

### Questions
See weakness

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
This paper analyzes classifiers for normalized covariance-pooled features. Specifically, the authors explore a rationale behind the effective linear classifier (Euclidean MLR) directly applied to square-rooted covariance features. By analyzing empirical performance results and theoretical formulations of Euclidean MLR and SPD MLR, this paper finds out that the Euclidean MLR of square-rooted covariance features is well explained by the SPD MLR on power-Euclidean metric. The experimental results on image classification using global covariance pooling (GCP) validates the claim on various settings.

### Strengths
+ The theoretical stuffs regarding SPD Riemannian geometry are insightful and the empirical performance comparison in Tab.3 is interesting.
+ Practical performance analysis is conducted on various types of datasets and networks.

### Weaknesses
- The discussion to induce SPD MLR in Sec.5 sounds a bit strange. In Sec.5, a Euclidean-MLR is reformulated as $\langle a,x\rangle - b \Rightarrow \langle a,x-p\rangle$ by re-parameterizing the bias as $b=\langle a,p\rangle$. If such re-parameterization is acceptable, one can more directly conclude that a Tangent-MLR is equivalent to the Euclidean-MLR by using the re-parameterization of TMLR: $\langle a,x-1\rangle -b \Rightarrow \langle a,x-p'\rangle$: EMLR, where $b=\langle a,p'-1\rangle$. It skips SPD-MLR and thus is a different conclusion from this paper. Therefore, the authors' claim seems to be less convincing.

- On the other hand, from a viewpoint of classifier formulation, Pow-EMLR is equivalent to Pow-TMLR since $\langle a,x\rangle -b=\langle a,x-1\rangle -b'$ with one-to-one correspondence between the parameters $(a,b)$ and $(a,b')$ via $b=b'+\langle  a,1\rangle$. Thus, the performance difference shown in Tab.3 comes from training dynamics only, especially in terms of the bias. This fundamental issue is not mentioned in this paper and is less connected to the classifier model (e.g., SDP-MLR) that this paper focuses on. As one could *guess* that disentanglement between classifier weights and a bias is preferable for training, it would be more interesting to delve into the training processes with much attention to the bias in the framework of covariance feature.

- This paper insists that an SDP-MLR is a fundamental classifier for covariance features. To validate the claim, it is necessary to compare the SDP-MLR with Tangent-MLR and practical EMLR for respective metrics of LEM and PEM (and optionally LCM). Related to the above-mentioned bias issue, the SDP-MLR would exhibit different training dynamics from the EMLR $\langle a,x\rangle -b$, resulting in different performance. Thus, Tab.5 should contain results of SDP-MLR directly applied to covariance features.

- The presentation of this paper is not so clear since it introduces less-relevant metrics in Sec.2, leading to messy notations (parameters) and rather complicated discussions. It would be enough to present three metrics of Log-Euclidean and Power-Euclidean; if this paper finds efficiency of Log-Cholesky metric for covariance features, it might be nice to contain LCM as an additional contribution.

### Questions
See the above-mentioned weak points.

### Soundness
2

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
3

### Summary
As global covariance pooling (GCP) becomes an increasingly important component in modern deep neural networks, a discrepancy remains between theoretical principles and practical applications of the normalization techniques used in GCP, especially regarding the matrix logarithm and matrix power. This work aims to bridge this gap by offering a theoretical understanding from a Riemannian geometry perspective. Through a combination of theoretical analysis and empirical evaluations, the study shows that the working mechanism of these matrix functions can be attributed to the Riemannian classifiers they implicitly respect.

### Strengths
1. This work identifies the discrepancy between the theory and practice of matrix normalization in GCP and addresses it by providing comprehensive theoretical explanations and underlying rationale for using Euclidean classifiers.
2. The study is technically sound, combining theoretical proof with empirical evidence.
3. Experiments on several real-world datasets are conducted to support the theoretical claims.
4. Overall, this paper is well-written and thoughtfully structured.

### Weaknesses
1. I am concerned that the theoretical contribution of this work appears to have a somewhat narrow application scope in its current presentation, as it focuses specifically on matrix normalization methods in GCP for deep neural networks, particularly on the matrix logarithm and matrix power. I suggest that the authors further clarify the practical significance of matrix normalization and the presented theories.
2. There are some other matrix normalization methods in GCP beyond matrix logarithm and matrix power. Popular choices [1] include matrix logarithm, element-wise power, matrix square-root and matrix power normalization. Is the element-wise power normalization applicable to the presented theories? Does it require additional analysis?
3. In Figure 1, in addition to showing the gap between LEM and PEM, it would be beneficial to highlight the consequences of this gap.

### Questions
1. I am concerned that the theoretical contribution of this work appears to have a somewhat narrow application scope in its current presentation, as it focuses specifically on matrix normalization methods in GCP for deep neural networks, particularly on the matrix logarithm and matrix power. I suggest that the authors further clarify the practical significance of matrix normalization and the presented theories.
2. There are some other matrix normalization methods in GCP beyond matrix logarithm and matrix power. Popular choices [1] include matrix logarithm, element-wise power, matrix square-root and matrix power normalization. Is the element-wise power normalization applicable to the presented theories? Does it require additional analysis?
3. In Figure 1, in addition to showing the gap between LEM and PEM, it would be beneficial to highlight the consequences of this gap.


[1] Wang, Qilong, et al. "What deep CNNs benefit from global covariance pooling: An optimization perspective." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper begins by exploring the motivation behind MPN-COV, focusing on how matrix power normalization (MPN) can be regarded as an approximation of geodesic distance (Log-E metric) for SPD matrices. Experimental results show there exist a significant discrepancy between MPN and Log-E metric.

Then, the authors try to study whether the theoretical framework used for matrix logarithmic normalization can explain matrix power normalization. They find that matrix power normalization maps SPD matrices to the tangent space (Euclidean space) at the identity matrix, and construct Pow-TMLR. But experiments reveals that Pow-TMLR shows spoor performance.

Finally, following by the works [Nguyen & Yang, 2023; Chen et al., 2024a;c] those expanded Euclidean MLR into SPD manifolds, this paper extends matrix logarithmic and matrix power normalization to SPD multinomial logistics regression. They construct ScalePow-EMLR based on this theory and demonstrate through experiments that this theoretical framework provides a coherent and unified explanation for the direct addition of Euclidean space classifiers after matrix power and logarithmic normalization.

### Strengths
The paper provides a different explanation on why matrix power normalization and matrix logarithmic normalization can be followed by a Euclidean space classifier.

This paper is well written.

### Weaknesses
1.	This paper provides an explanation based on SPD multinomial logistics regression for why matrix logarithmic normalization and matrix power normalization can be followed by Euclidean space classifiers. However, it seems not very clear why matrix power normalization significantly outperforms matrix logarithmic normalization under this framework. In other words, what are the significant performance differences between the two methods under the explanation framework of SPD MLR?

2.	As shown in Eqn. (15) and Eqn. (16), the authors extend matrix power normalization and matrix logarithmic normalization to SPD MLR. However, it seems not very clear why matrix power normalization and matrix logarithmic normalization can be regarded as Riemannian classifiers based on Eqn. (15) and Eqn. (16).

3.	As shown in Table 4, there only exists a difference of constant term between the formula of ScalePow-EMLR and one of Pow-TMLR. But, as compared in Tables 3, 5, and 6, there is a significant performance gap between ScalePow-EMLR and Pow-TMLR, where ScalePow-EMLR and Pow-EMLR are equivalent. For example, on the Cars dataset in Table 5, the Top-1 accuracy of ScalePow-EMLR is 80.31%, while that of Pow-TMLR is only 51.14%. I feel a bit confused why a constant term can bring significant performance gap? Could the authors give more explanation on this phenomenon?

### Questions
Please see paper weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
