# FragSel: Fragmented Selection for Noisy Label Regression

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
As with many other problems, real-world regression is plagued by the presence of noisy labels,  an inevitable issue that demands our attention. 
Fortunately, much real-world data often exhibits an intrinsic property of continuously ordered correlations between labels and features; where data points with similar labels are also represented with closely related features.
In response, we propose a novel approach named FragSel wherein we collectively model the regression data by transforming them into disjoint yet contrasting fragmentation pairs. This allows us to train more distinctive representations, enhancing our ability to tackle the issue of noisy labels.
Our FragSel framework subsequently leverages a mixture of neighboring fragments to discern noisy labels through neighbor agreement within both the prediction and representation spaces.
To underscore the effectiveness of our framework, we extensively perform experiments on four benchmark datasets of diverse domains, including age prediction, price prediction, and music production year estimation.
Our approach consistently outperforms thirteen state-of-the-art baselines, being robust against symmetric and random Gaussian label noise.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Built upon the assumption that samples with similar labels tend to share relevant features, the authors propose a novel framework to model regression data collectively. They achieve this by transforming the data into disjoint yet contrasting fragmentation pairs, which utilize a mixture of neighboring fragments to identify noisy labels. This identification is carried out through an agreement among neighbors within both the prediction and representation spaces. Experimental results, demonstrated on four benchmark datasets, underscore the efficacy of the proposed framework in handling synthetic label noise.

### Strengths
(1) The exploration of the problem concerning noisy-labeled regression is both intriguing and practically significant.

(2) The proposed method organizes data samples into clusters and capitalizes on neighborhood information, which is well-grounded for identifying noisy labels.

(3) Tailored for noisy regression labels, the authors introduce a new metric called Error Residual Ratio for evaluating selected or refurbished samples.

(4) Empirical efforts showcased the effectiveness of the proposed method, as well as evaluated the performance of certain baseline methods (previously applied in robust classification tasks) in addressing noisy label regression.

### Weaknesses
(1) The presentation could be further improved to help readers capture the proposed method. Specifically, the rationale behind splitting fragments based on equal length rather than equal size is not immediately clear. Additionally, the process for completing the graph in step 2 of the contrastive fragmentation algorithm, particularly the choice of edge weight based on the distance between the closest samples of two fragments instead of the distance between two centroids, requires further clarification.

(2) When checking the empirical performances of the proposed method (FragSel-R v.s. FragSel-D), it seems that the role of classification-based feature extractor has much larger effect on the performance than the regression based method. The performance of FragSel-R is not consistently better than baselines. This raises questions about the practical advantages of the regression-based approach in this specific context, and whether the observed performance differences are statistically significant across different datasets and noise levels.

(3) The authors state that the sole hyperparameters are the number of fragments (F), the parameter K for KNN-based prediction, and the extent of jittering (J). However, the influence of each hyperparameter on the results presented in Table 1 is not thoroughly discussed. A more detailed analysis of the hyperparameter space and their individual and combined effects on performance would strengthen the paper.

### Questions
(Q1) Is there a rationale behind the authors' choice to split fragments based on equal length rather than equal size? For instance, considering the age distribution of heart disease, it may be less common in children, resulting in fewer cases. Would splitting the data in intervals of 0-10, 10-20, etc., be suitable given such disparities?

(Q2) In step 2 of the proposed contrastive fragmentation algorithm, for completing the graph, could authors explain a bit more about the whole process, i.e., why the edge weight is decided by the distance between the closest samples of the two fragments, instead of the distance between two centroids.

(Q3) Regarding the performance of FragSel-R,-D, it seems that the classification-based feature extractor has much better effect than the regression based method. And the performance of FragSel-R is not consistently better than baselines.

(Q4) In Appendix Figures 7 and 8, visualizing the baseline performance, i.e., F=1 (without employing FragSel), alongside the other results could provide a more direct understanding of how the number of fragments impacts performance. This comparison could offer more insightful conclusions.

(Q5) While the authors assert that the sole hyperparameters of the framework are the number of fragments (F), the parameter K utilized for KNN-based prediction, and the extent of jittering applied for regularization, the influence of each on the results presented in Table 1 remains unclear. Could the authors provide additional insight into how these hyperparameters affect the outcomes?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This papaer solves the problem of noisy label for regression task. It focuses on sample selection methodologies. It solves noisy label regression more well by (1) pairing samples with contrastive features, (2) considering neighbor agreement, and (3) neighborhood jittering. Additionally, this paper suggests new benchmark dataset for noisy label regression.

### Strengths
- Curate a new benchmark dataset for regression task, and evaluate current benchmarks. 
- Apply graph structure to find the constasting pairs of dataset.
- Suggest a new metric called Error Residual Ratio (ERR).

### Weaknesses
 - Figure 1 is hard to understand. It includes too much information that has not yet been explained.
- I think it is already quite well known that samples with similar features tend to exhibit similar labels, and many studies have assumes that properties; the validity of Semi supervised learning, pseudo labeling stems from this assumption. Therefore, I think that the novelty of this paper may be limited from several previous sample selection based methods, since I think the method proposed in this paper is the combinations of the previous studies (suggested in the classification task).
- I cannot understand yet why the method the authors suggests fits especially for the regression task. Can't it be applied to classification task?

### Questions
- It is known that data points with similar features tend to exhibit similar label values. However, including noisy labeled data samples, it corrupts these similarity the model learns because the model tries to fit all data samples, which is also the problem of learning noisy data. Therefore, for managing noisy data, can we use the similar feature-similar label property as it is? Or should we use additional tricks for managing the problem? 
- Why should we select samples with framentation? (empirically, okay. Any theoretical idea?)
- Number of fragmentation would matter...
- Selecting the clean subset of the data, I think some bias can be included (e.g. maybe samples whose features are severely biased to one class will be easily sampled, and if samples are located between two fragments, it may not be selected although it is clean.). Can we mitigate it?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents FragSel, a method for improving regression methods in the presence of noisy labels. This method uses a simple technique to learn better representations by training over maximally distance subsets, and the authors shown strong performance on an array of standard benchmarks for label noise.

### Strengths
- The overall communication is clear and straightforward, and the framing of the paper is evident and easy to understand throughout.
- The presented method FragSel is novel yet relatively simple, leading to an effective method for improving regression in the context of label noise that is straightforward to reproduce.
- The evaluation section is quite thorough, using a wide variety of benchmarks, noise methods, and evaluation metrics to assess the quality of their method.

### Weaknesses
 - No real concerns are present, though I am not particularly well-versed in the literature on this topic so it is hard for me to assess if this work is sufficiently different from previous works.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studied regression learning with noisy labels, which is a seldom explored but important problem for machine learning. To address the problem, this paper proposed a novel noise-robust method by performing sample selection via a characteristic that data points similar in the feature space are likely to have similar labels. In addition, a neighborhood jittering regularization is used to improve the robustness. Experimental results confirmed the superiority of the proposed method.

### Strengths
1. The studied problem is highly valuable in real-world applications while seldom explored. This work used noisy regression benchmarks from various domains, which fully demonstrated the application potential of the proposed method.
2. The proposed method is a reasonable solution that makes use of the orderly relationships within the label and feature spaces.
3. The discussions and ablation analyses are thorough, making the effectiveness of the proposed method convincing.

### Weaknesses
1. Some important baselines are missing. For example, [1] is a nice baseline for regression learning with noisy labels. [2] performed bounding box correction by minimizing the discrepancy between two classifiers. Besides, I think there are some other works in noise-robust object detection that consider regression learning with noisy labels. Specifically, methods that leverage region proposal networks to generate bounding box proposals and then selectively choose clean labels or re-weight training samples should be considered. Also, methods that use the object detector's classifier to update or assess the quality of bounding boxes by evaluating the confidence or consistency of the bounding box through the classification output should be explored as relevant baselines.
2. Some highly related references in noisy label learning are missing. For example, the transition matrix methods [3-5], and the hybrid methods [6,7]. It is important to include methods that explicitly model the noise transition probabilities, as these are fundamental to understanding and mitigating the impact of noisy labels. Furthermore, hybrid methods that combine different noise-handling strategies should also be considered.
3. The description of the proposed algorithm procedure and the experiment setting can be introduced more clearly. I have some questions and suggestions: 1) Are the prediction-based or representation-based sample selections used together in the proposed method? If not, when to use the prediction-based sample selection, and when to representation-based one? It is unclear how these two selection mechanisms interact. 2)  How to inject symmetric label noise in regression labels? The standard approach for classification may not be directly applicable to regression. 3) The pseudo-code of the proposed algorithm will help a lot for the readers who want to understand the detailed design. The current description lacks the necessary detail for reproducibility and thorough understanding.

### Questions
I think this work is a nice work if the authors can address my concerns above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
