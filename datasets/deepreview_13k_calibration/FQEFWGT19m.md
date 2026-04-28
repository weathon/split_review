# Multi-task Learning for Heterogeneous Multi-source Block-Wise Missing Data

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Multi-task learning (MTL) has emerged as an imperative machine learning tool to solve multiple learning tasks simultaneously and has been successfully applied to  healthcare, marketing, and biomedical fields. However, in order to borrow information across different tasks effectively, it is essential to utilize both homogeneous and heterogeneous information. Among the extensive literature on MTL, various forms of heterogeneity are presented in MTL problems, such as block-wise, distribution, and posterior heterogeneity. Existing methods, however, struggle to tackle these forms of heterogeneity simultaneously in a unified framework. In this paper, we propose a two-step learning strategy for MTL which addresses the aforementioned heterogeneity. First, we impute the missing blocks using shared representations extracted from homogeneous source across different tasks. Next, we disentangle the mappings between input features and responses into a shared component and a task-specific component, respectively, thereby enabling information borrowing through the shared component. Our numerical experiments and real-data analysis from the ADNI database demonstrate the superior MTL performance of the proposed method compared to a single task learning and other competing methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors provide a two-stage algorithm for multi-source multi-task learning with blockwise missing data. The proposed method is assumption light, and allows for complex missingness structures and heterogeneity across sources. The authors demonstrate the effectiveness of their algorithm via simulations and a well-motivated application to a dataset from the Alzheimer's Disease Neuroimaging Initiative.

### Strengths
The paper addresses a well-motivated and pervasive problem in large-scale data analysis, namely the integration of block-wise missing data from distinct sources. The proposed imputation method is a novel application of the encoder-decoder framework that, to my knowledge, is new to the missing data literature. Numerical results indicate that this may be a promising approach for imputation.

### Weaknesses
The primary weakness of this work is in the evaluation of the proposed MTL-HMB method. The proposed simulation setting (described in Appendix A.2) is far too small and simple to necessitate the heavy machinery used by the proposed method and the STL and HTL methods also applied to the data.

1. The samples sizes are too small relative to the trained neural networks to draw meaningful conclusions from the simulations. This is most evident in Figure 5d: as n grows, the performance of the single-task learning method substantially improves, nearly mimicking the proposed method in the n = 600 setting. The relatively poor performance of STL in particular across the other settings may just be due to high estimation error in learning the neural network.

2. The data generating mechanism outlined in A.2 is a simple linear model. The authors should compare the STL, HTL, and MTL-HMB methods to analogous tools from the statistical literature, especially a standard least squares estimator, a multi-task learning estimator for hetereogenous tasks (such as the ARMUL framework proposed in Duan and Wang 2023 AoS), and a two-stage estimator for blockwise-missing data under linear models such as that provided by Xue, Ma, and Li 2021.

3. As the provided simulation results do not consider any imputation tools other than the proposed method in this paper, it is impossible to determine whether the MTL-HMB is effective at imputation+multi-task learning, or if imputation alone leads to the slight improvement in performance that we see in the paper. While the Ablation 2 experiment attempts to address this, it is still not clear if the use of the encoder-decoder framework is more effective than a simple linear imputation as used in Xue, Ma, and Li 2021. In general, the paper would benefit greatly from more extensive simulation studies that compare the proposed imputation+prediction method to the many methods already studied in the literature, including:

* Li, Y., Yang, X., Wei, Y., & Liu, M. (2024). Adaptive and Efficient Learning with Blockwise Missing and Semi-Supervised Data. arXiv preprint arXiv:2405.18722.
* Xue, F., Ma, R., & Li, H. (2021). Statistical inference for high-dimensional linear regression with blockwise missing data. arXiv preprint arXiv:2106.03344.
* Zhou, D., Cai, T., & Lu, J. (2023). Multi-source learning via completion of block-wise overlapping noisy matrices. Journal of Machine Learning Research, 24(221), 1-43.
* Song, S., Lin, Y., & Zhou, Y. (2024). Semi-supervised Inference for Block-wise Missing Data without Imputation. Journal of Machine Learning Research, 25(99), 1-36.

As it stands, I am unable to evaluate whether the proposed method is meaningful improvement over existing works in this field.

### Questions
How does the proposed method perform in larger-scale simulations, or under different (i.e. nonlinear) data-generating models?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Comments：
The manuscript introduces a novel two-step learning strategy for multi-task learning (MTL) that effectively addresses multiple forms of heterogeneity, including block-wise, distributional, and posterior heterogeneity. The proposed approach begins by imputing missing blocks using shared representations from homogeneous sources across different tasks, followed by the disentangling of mappings between input features and responses into shared and task-specific components.

Weaknesses:

1.	Why does Equation 1 minimize only L_pre?

2.	The authors utilize a bar chart to display qualitative results, however, quantitative results would be more appropriate, enabling the reader to make numerical comparisons.

3.	The experiments conducted by the authors were insufficient, resulting in an incomplete evaluation of the model's performance.

### Strengths
This paper is well-structured and coherent.

### Weaknesses
1. Why does Equation 1 minimize only L_pre?

2. The authors utilize a bar chart to display qualitative results, however, quantitative results would be more appropriate, enabling the reader to make numerical comparisons.

3. The experiments conducted by the authors were insufficient, resulting in an incomplete evaluation of the model's performance.

### Questions
1.Why does Equation 1 minimize only L_pre?

2.The authors utilize a bar chart to display qualitative results, however, quantitative results would be more appropriate, enabling the reader to make numerical comparisons.

3.The experiments conducted by the authors were insufficient, resulting in an incomplete evaluation of the model's performance.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel two-step strategy for Multi-Task Learning (MTL) addressing the challenges posed by block-wise missing data and various types of heterogeneity. The proposed method's strength lies in its systematic approach to tackling distribution and posterior heterogeneity through integrated imputation and sequential learning. The numerical experiments demonstrate the method's effectiveness across diverse scenarios, providing compelling evidence of its superiority compared to existing techniques. Additionally, the application to the ADNI real-world dataset highlights its practical relevance.

### Strengths
The authors conducted comprehensive numerical experiments, validating the efficacy of their method across various levels of heterogeneity. This adds robustness to their claims and provides confidence in the generalizability of the results.

The two-step approach is clearly defined, and the methods used for imputing missing data and disentangling mappings are appropriately justified.

### Weaknesses
1.The authors do not provide a detailed explanation of how the proposed method specifically addresses block-wise datasets in the paper.

2.The authors claim in the paper that they use a shared feature extraction encoder and a task-specific feature extraction encoder. What are the differences between these two, and how are they reflected in the methodology?

3.Why are some formulas numbered while others are not? The authors need to revise and check this.

4.The authors propose several loss functions. What is the relationship between these losses, particularly the reconstruction loss on page 5 and the loss function on page 7?

5.A detailed algorithm flowchart needs to be provided.

### Questions
See the above Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method to perform multi-task learning in a context of heterogeneous multi-source block-wise missing data. The authors propose a block-wise imputation method and then an algorithm designed for heterogeneous multi-task learning. The method is assessed on synthetic data and on the ADNI dataset. 

I'm a beginner in multi-task learning and I'm not able to have an opinion on how this article is positioned in this literature. However, I think this paper is well written and well presented, the experiments are complete (apart I find from the comparison with other methods), the proposed methodology is innovative and of interest.

I'm putting 6 as my initial score because I have a few questions.

### Strengths
- Main strenght: the paper is easy to follow, the methodology is clearly explained (Figures 2, 3, 4 are really helpful).

### Weaknesses
My major concern is on the experimental study (see Questions).

Main questions:
1. The whole pipeline can be decomposed into two steps: one imputation step and one prediction step. In the missing-data literature (out of the scope of MTL context), this is recommended to use a two-step procedure when the learning task is prediction but it has been recently shown that naive imputation is adequate. I wonder if here the authors can think about a "naive" imputation in the MTL context.
See for example: Le Morvan, Marine, et al. "What’sa good imputation to predict with missing values?." Advances in Neural Information Processing Systems 34 (2021): 11530-11540.

Experimental study:
1. The authors only compare their methodology to Single Task Learning (STL) and Transfer Learning for Heterogeneous Data (HTL).
- Can they describe more in details these existing methods ?
- For STL, how does it work ? Each task is handled independently and the results are aggregated after that ?
- I am not familiar with the MTL literature, but the authors cite some existing works in Section 2. I understand that there is no existing work which handle both the heterogeneity and the missing data problem, but the authors can for example assess the performance of their block-wise missing imputation method + an existing MTL algorithm or an existing block-wise imputation method + their MTL architecture.
2. How many sources and tasks can the method handle? 
3. For me, the validation set should not have block-wise missing data. If true, I think the validation set size is too big (20% for model selection and early stopping + 20% for test set size).
4. One thing that I wonder is how is the test set: does it have any block-wise missing data also or all the sources are observed ?


Some minor comments: 
- The notation $\mathcal{L}_{\mathrm{recon}}$ is not introduced in the main text
- In Figure 3, the final arrows are not clear. Why is there this orange arrow ? Why a white case for the third line (imputation case ?) ? And finally, the location of "G" and "D" is unclear for me (even though this is clear in the main text).

### Questions
Main questions:
1. The whole pipeline can be decomposed into two steps: one imputation step and one prediction step. In the missing-data literature (out of the scope of MTL context), this is recommended to use a two-step procedure when the learning task is prediction but it has been recently shown that naive imputation is adequate. I wonder if here the authors can think about a "naive" imputation in the MTL context.
See for example: Le Morvan, Marine, et al. "What’sa good imputation to predict with missing values?." Advances in Neural Information Processing Systems 34 (2021): 11530-11540.

Experimental study:
1. The authors only compare their methodology to Single Task Learning (STL) and Transfer Learning for Heterogeneous Data (HTL). 
- Can they describe more in details these existing methods ? 
- For STL, how does it work ? Each task is handled independently and the results are aggregated after that ? 
- I am not familiar with the MTL literature, but the authors cite some existing works in Section 2. I understand that there is no existing work which handle both the heterogeneity and the missing data problem, but the authors can for example assess the performance of their block-wise missing imputation method + an existing MTL algorithm or an existing block-wise imputation method + their MTL architecture. 
2. How many sources and tasks can the method handle? 
3. For me, the validation set should not have block-wise missing data. If true, I think the validation set size is too big (20% for model selection and early stopping + 20% for test set size).
4. One thing that I wonder is how is the test set: does it have any block-wise missing data also or all the sources are observed ? 


Some minor comments: 
- The notation $\mathcal{L}_{\mathrm{recon}}$ is not introduced in the main text
- In Figure 3, the final arrows are not clear. Why is there this orange arrow ? Why a white case for the third line (imputation case ?) ? And finally, the location of "G" and "D" is unclear for me (even though this is clear in the main text).

### Soundness
3

### Presentation
4

### Contribution
3
