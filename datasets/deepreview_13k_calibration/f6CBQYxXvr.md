# Project and Probe: Sample-Efficient Adaptation by Interpolating Orthogonal Features

- Decision: Accept
- Avg Score: 7.00
- Scores: 5, 8, 8

## Abstract
Transfer learning with a small amount of target data is an effective and common approach to adapting a pre-trained model to distribution shifts. In some situations, target data labels may be expensive to obtain, so we may only have access to a limited number of target data points. To make the most of a very small target dataset, we propose a lightweight, sample-efficient approach that learns a diverse set of features and adapts to a target distribution by interpolating these features. Our approach, Project and Probe (Pro$^2$), first learns a linear projection that maps a pre-trained embedding onto orthogonal directions while being predictive of labels in the source dataset. The goal of this step is to learn a variety of predictive features, so that at least some of them remain useful after distribution shift. Pro$^2$ then learns a linear classifier on top of these projected features using a small target dataset. Theoretically, we find that Pro$^2$ results in more sample-efficient generalization by inducing a favorable bias-variance tradeoff. Our experiments on four datasets, with multiple distribution shift settings for each, show that Pro$^2$ improves performance by 5-15% when given limited target data compared to prior methods such as standard linear probing.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper deals with the problem of transfer learning with a small amount of target data. It proposes Project and Probe, which first learns a liner projection that maps the pre-trained embedding onto orthogonal directions and then learns a linear classifier on top of the projected features on the small target dataset. The proposed method outperforms prior methods on transfer learning when given very limited target data.

### Strengths
- The paper is clearly written and organized.

- The enhanced sample-efficient generalization of the proposed method is supported by theoretical analysis.

### Weaknesses
 - A critical comparison is missing from the experiments: How does the proposed method perform compared to zero-shot transfer learning methods (i.e., no target training data), as cited in related work?

- For reproducibility, it is necessary to include the numerical values of the experimental results in addition to the line charts.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces Project and Probe (PRO^2), a transfer learning method designed for scenarios with limited target data due to distribution shifts. PRO^2 is based on a two-step approach: first, it projects pre-trained embeddings from the source dataset onto orthogonal directions to derive a diverse, non-redundant set of predictive features; next, it trains a linear classifier on these projected features using the target data. Theoretical analyses emphasize the method's favorable bias-variance tradeoff, and experimental results across four datasets demonstrate an improved performance by 5-15% compared to traditional linear probing methods.

### Strengths
- The paper stands out in terms of clarity, organization, and overall presentation. It also offers an extensive appendix that provides in-depth coverage of related topics, adding value for the reader.

- The authors have presented a robust theoretical framework that substantiates their approach. They effectively highlight the method's capability to achieve a desirable balance between bias and variance.

- The empirical experiments are detailed and present a wide range of scenarios. While there are certain reservations (addressed below), the breadth and depth of this section are commendable.

### Weaknesses
 - The study by Morwani et al. (2023) has previously explored orthogonal projections as a remedy for feature collapse and simplicity bias. This prior exploration somewhat diminishes the uniqueness of the approach presented in this paper.

- Some aspects of the empirical evaluation are unclear and require further details from the authors. See the "Questions" section for more details.

- The paper presents a rather limited set of baselines. Given that the experimental setup seems relatively straightforward, it would be advantageous to have a more comprehensive range of baselines. Specifically, a comparative analysis involving methods anchored in LDA and QDA (as pointed out in Shysheya et al., 2022) could enrich the paper.

### Questions
1) Regarding the empirical assessment, was a consistent hyper-parameter search strategy employed across all the evaluated baselines, or was it exclusively used for the proposed model?

2) There are approaches that exploits Linear Discriminant Analysis (LDA) and Quadratic Discriminant Analysis (QDA) for the adaptation of the head of a pretrained model with success (Shysheya et al. 2022). Can the authors comment on the differences between their method and these methods? While the paper covers the relation with respect to LDA, it does not seem to mention the relation with QDA. Adding those baselines to the empirical evaluation may be beneficial.

3) The authors briefly mention the relation with the previous work of Morwani et al. (2023) in the related work section. This section appears somewhat limited and would benefit from a more in-depth exploration. Could the authors elaborate on the parallels and distinctions between their work and Morwani et al. (2023)?

4) Would the authors be able to provide a detailed analysis of the complexity for the proposed method (e.g. FLOPs and/or MACs)? Understanding complexity is crucial as it essentially represents the computational budget. How does the method's time complexity stand in comparison to leading fine-tuning approaches, such as BiT by Kolesnikov et al. (2020), which adapt the entire model body or FiT (Shysheya et al. 2022), which adapt a subset of the body parameters?


References
-----------

Morwani, D., Batra, J., Jain, P., & Netrapalli, P. (2023). Simplicity bias in 1-hidden layer neural networks. arXiv preprint arXiv:2302.00457.

Kolesnikov, A., Beyer, L., Zhai, X., Puigcerver, J., Yung, J., Gelly, S., & Houlsby, N. (2020). Big transfer (bit): General visual representation learning. In Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part V 16 (pp. 491-507). Springer International Publishing.

Shysheya, A., Bronskill, J., Patacchiola, M., Nowozin, S., & Turner, R. E. (2022). Fit: Parameter efficient few-shot transfer learning for personalized and federated image classification. arXiv preprint arXiv:2206.08671.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose PROJECT AND PROBE, a lightweight framework consisting of 2 steps: (1) a projection step that extracts a diverse and predictive feature-space basis and (2) a probing step that interpolates between the projected features to efficiently adapt varying target distributions. The core idea is to ensure orthogonality among each component of the feature vector. Each component is utilized by an identical predictor but contains distinct information. Subsequently, these components are employed for predicting the target data. The proposed approach is supported by a theoretical analysis showing that the proposed approach improves sample efficiency.

### Strengths
- The paper is well-written and well-organized.
- Enforcing feature orthogonality is intuitive and seems suitable for learning features that remain invariant to distribution shifts.
- The proposed algorithm outperforms the baselines, especially when the sample size of the target data is relatively small.

### Weaknesses
 - One major limitation of this work is the fact that the project and probe processes are considered solely in the linear model regime due to the pre-trained feature extraction. Also, the theoretical analysis was conducted with a linear model. how would it  extended to large-scale problems?

- The authors only compare with projection-based baselines. I think comparisons with recent general unsupervised domain adaptation methods are needed. 

- While learning diverse/orthogonal features is novel in the context of domain adaptation. There is an active line of research that explores this idea in the standard supervised learning setting, such as [1-7]. I think these methods should be discussed in the related work.

### Questions
See Section above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
