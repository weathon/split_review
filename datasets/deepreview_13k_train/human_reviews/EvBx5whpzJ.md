# Con4m: Unleashing the Power of Consistency and Context in Classification for Blurred-Segmented Time Series

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Blurred-Segmented Time Series (BST) has emerged as a prevalent form of time series data in various practical applications, presenting unique challenges for the Time Series Classification (TSC) task. The BST data is segmented into continuous states with inherently blurred transitions. These transitions lead to inconsistency in annotations among different individuals due to experiential differences, thereby hampering model training and validation. However, existing TSC methods often fail to recognize label inconsistency and contextual dependencies between consecutive classified samples. In this work, we first theoretically clarify the connotation of valuable contextual information. Based on these insights, we incorporate prior knowledge of BST data at both the data and class levels into our model design to capture effective contextual information. Furthermore, we propose a label consistency training framework to harmonize inconsistent labels. Extensive experiments on two public and one private BST data fully validate the effectiveness of our proposed approach, Con4m, in handling the TSC task on BST data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors study the blurred segmented time series (BST) data prediction problem. The authors theoretically clarify the connotation of valuable contextual information. Based on these insights, prior knowledge of BST data is incorporated at the data and class levels into the model design to capture effective contextual information. Moreover, the authors also propose a label consistency training framework to harmonize inconsistent labels. The authors have performed extensive experiments on real datasets to demonstrate the effectiveness of the proposed method in handling the time series classification task on BST data.

### Strengths
1.	The authors propose a new framework to handle the time series classification task on blurred segmented time series data.

2.	The authors provide some theoretical analysis about the connotation of the valuable contextual information.

3.	In the proposed framework, prior knowledge of the BST data at both the data and class levels are incorporated into the proposed model to capture the effective contextual information.

4.	The authors have performed extensive experiments on 3 real datasets to demonstrate the effectiveness of the proposed method.

### Weaknesses
1.	Some assumption of the proposed method seems a little strong. In Section 3.2, for the prediction behavior constraint, it is assumed that consecutive time segments span at most 2 classes within a suitably chosen time interval. The time interval may have a big impact on the model performance. However, it is not clear how to choose a suitable time interval for each dataset. The authors also need to perform experiments studying the impacts of the time interval on different datasets. Specifically, the assumption that only two classes exist within a time interval is quite restrictive and may not hold for many real-world datasets, particularly those with rapid transitions between multiple classes. The paper lacks a discussion on the sensitivity of the model to violations of this assumption. Furthermore, the method for selecting the time interval is not clearly defined, and the impact of different time interval selection strategies on the final performance needs to be thoroughly investigated. It is not sufficient to simply state that a 'suitably chosen' interval is required; a more rigorous approach is needed.

2.	The experimental analysis seems not consistent enough. In Figure 3(b), the analysis about random disturbance is studied on fNIRS and Sleep datasets. In Table 3, the ablation studies are performed on Sleep and SEEG datasets. The lack of consistency in the datasets used for different experiments makes it difficult to draw general conclusions about the method's performance. For example, the random disturbance analysis should ideally be performed on all datasets to ensure that the method is robust to such disturbances across different data characteristics. Similarly, the ablation studies should also be performed on all datasets to provide a comprehensive understanding of the contribution of each component of the model. The current experimental design makes it difficult to compare the results across different experiments and datasets.

3.	The experimental analysis is not sufficient. Compared with existing methods, one advantage of the proposed method is to exploit the prior information at both the data and class levels. The authors are suggested to perform experiments studying the performance of the proposed method with only considering the prior information at data level and class level respectively. The ablation study in Table 3 does not fully address this issue, as it only removes the Con-Transformer module and the label consistency modules, but it does not isolate the impact of each type of prior information. Specifically, it is necessary to evaluate the model's performance when only the data-level prior is used, and when only the class-level prior is used, to understand the relative importance of each type of information. This would provide a more detailed understanding of the model's behavior and the effectiveness of each component.

### Questions
As discussed in Section 3.2, the time interval may have a big impact on the model performance. How to choose a suitable interval for each dataset?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Blurred-segmented time series (BST) data has continuous states with inherently blurred transitions, leading to annotation noise. Existing time series classification methods do not consider label inconsistency and contextual dependencies between consecutive classified samples. To address these issues, the paper first theoretically identifies the value of contextual information, and then proposes a transformer-based model that incorporates contextual information from BST data. Moreover, the paper adopts curriculum learning techniques to train the model under annotation noise. Experiments show the proposed method achieves better classification accuracy than baseline methods on three datasets under different levels of label noise.

### Strengths
+ The problem setting is new and realistic. The paper consider time series classification on the new blurred-segmented time series data which has inherent contextual dependencies between classified samples. Without relying on the common i.i.d. assumption on samples, the proposed method boosts classification accuracy by explicitly exploiting the neighboring samples of a target sample. 

+ The proposed method exploits both contextual information and noisy labels and can be applied to many realistic time series classification problems.

+ The experiments are well-designed and extensive. Results show that the proposed method outperforms baselines on the three datasets with different levels of label noise. Ablation studies show that each of the proposed components are effective in improving the time series classification accuracy.

### Weaknesses
 - The clarity of the paper can be improved.
  Proposition 1 is a basic mutual information inequality. It is unclear how the mutual information $I(y_t;x_t,x_{\mathbb{A}_t})$ relates to the performance of a model. The paper states that a larger mutual information indicates stronger correlation between variables, but it is not clear how this translates to improved model performance. Specifically, in the context of classification, it is not clear how a stronger correlation between input samples and labels implies that input samples are more easily distinguishable by their labels. The paper needs to clarify the connection between mutual information and the model's ability to discriminate between samples.

- The proof of Theorem 1 mismatches with the claim.
  The proof only analyzes in what cases can $I(y_t;x_{\mathbb{A}_t}|x_t)$ be increased. It does not clearly define what predictive capability means in this context. The paper claims that contextual information enhances predictive capability, but it does not provide a clear definition of predictive capability, nor does it explain how the increase in mutual information translates to enhanced predictive capability. Furthermore, the connection between predictive capability and the mutual information gain is not clearly established. The paper needs to provide a more rigorous and detailed explanation of these concepts.

- The motivation for the proposed method is not clear. For example, why using a Gaussian kernel function can better align with  $p(x_{\mathbb{A}_t}|x_t)$ and $p(y_t|x_t, x_{\mathbb{A}_t})$? The paper states that the Gaussian kernel helps to capture temporal persistence and smoother representations, but it does not provide a clear justification for why the Gaussian kernel is the optimal choice. The paper needs to provide a more detailed explanation of how the Gaussian kernel aligns with the underlying data distribution and how it contributes to improved model performance.

### Questions
1. In Proposition 1, how the mutual information $I(y_t;x_t,x_{\mathbb{A}_t})$ relates to the performance of a model.

2. In Theorem1, how the predictive capability for the labels is defined? How do we know the contextual information enhances the predictive capability? And what is the connection between predictive capability and the mutual information gain?

3. What is the computational complexity of the proposed method? Can the proposed method scale to longer time series?

4. Why using a Gaussian kernel function can better align with $p(x_{\mathbb{A}_t}|x_t)$ and $p(y_t|x_t,x_{\mathbb{A}_t})$?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on a time series classification problem in a novel setting of "blurred segmented" time series where each time series is exhaustively segmented and each segment is labeled with one of the given states. The notion of "blur" stems from the blurry transition boundaries between the two consecutive states in a given time series. The ultimate goal (to my understanding) is to train a Time Series Classification (TSC) model which can automate the segmentation and labeling process on such time series.  To train such a TSC model, the training data is comprised of labeled BS time series where the labels of all segment are manually annotated by multiple domain experts. The key feature of the proposed solution  is a novel deep learning attention-layer based architecture which is capable of leveraging the contextual dependencies between adjacent segments of time series. The proposed approach is evaluated against multiple baselines on three real-world datasets  (two public and one private) from healthcare and neuro-science domain which also appear to be the key applications of such work. The evaluation results seem to indicate better performance of the proposed approach in comparison to the baselines.

### Strengths
1. The problem setting of time series classification on blurred segmented time series is quite relevant for many domains. 
2. The proposed approach seems to be outperforming the state-of-the-art time series classification baselines on multiple real-world datasets. 
3. Ablation studies seem to justify the value of various components of the approach.

### Weaknesses
1. The paper is not written well and a bit difficult to follow. To begin with, the term "blurred segmented time series" is not concretely defined throughout the manuscript. To the best of my knowledge, this term is not ubiquitous in ML community. Further, the introduction does not clearly define the problem formulation.  In particular, it is not clear whether the end result is to classify the individual segments or classify an entire time series which comprises of multiple segments. The problem formulation is not mathematically defined even in subsequent sections which keeps a reader busy guessing. Further, several terms like samples vs segments vs timestamps , state vs labels are confusingly used at several places which makes it super difficult to understand the exact problem formulation. It is also not clear whether a segment is of fixed length or varying length.

2. The motivation regarding too much noise in the labels in the segments due to label inconsistencies on boundary segments is also not super convincing. For instance, why can't one simply get rid of  such boundary segments and train the model only on cleaner samples?

3. The theoretical justification section also lacks rigor and not quite convincing. In particular, the authors use mutual information definitions to make arguments in support of choosing augmented features from a neighborhood segment window. However, those arguments are very superficial and lack rigor (see detailed comments below).

4. The description of proposed approach is also quite difficult to follow. Several key notations are not well defined (e.g. what are V_s and V_t) and I had to read the papers in related work (e.g. Xu et al. 2022) in quite detail from where the ideas are borrowed. Even then, certain components of the approach such as neighbor class consistency discrimination are yet not clear to me.

### Questions
Specific comments/questions: 
1. Page 3, line 86-87: This statement doesn't sound quite valid to me. What does it mean to say that we need to increase p(x_{A_t}|x_t)? We aren't talking about one specific value of x_{A_t} here, it's a distribution, right?  And ultimately all the terms are being summed up over all possible values of x_{A_t}. Similar concern for KL divergence argument. Basically, the justification given  in the support of design of proposed approach is not convincing and needs more rigor. 

2. Page 3, lines 87-88: What do you exactly mean by "easier to predict"? Do you mean adding small noise to the samples? Perhaps being more specific here along with some citations will help.

3. A mathematical problem statement is dearly missing in Section 3. 

4. Section 3.1: What is meant by a "smoother representation"? Perhaps you meant to say that the representation function should be "temporally smooth" so that the neighboring segments get embedded close-by in the embedding space? 

5. Section 3.3, Lines 235 - 238: What is the significance of every group? How are you exactly getting 12 and 6 cross-validation results? 

6. In section 4.5 (case study), what is the length of each segment? Is it fixed to 2 s? If so, how come SREA and MiniRocket has sub-segments of labels of lengths<2s? Or are we not labeling the entire segment with the same label?

7. Section 4.2, In lines 266-272: Is the noise coming due to challenging boundary disturbances similar to random noise as introduced in this experiment?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a blurred-segmented time series classification framework, Con4m, that forces label coherence and prediction behavior between two consecutive predictions. It also incorporates curriculum learning and gradual label change to cope with label inconsistency in transitions. Con4m shows its superiority in two public dataset and one private dataset with ablation studies for each component.

### Strengths
1. This paper covers a novel time-series data, blurred-segment time series.
2. Proposes practical framework for time series classification with noises.

### Weaknesses
1. Model degradation by label inconsistency in transition is not validated. The number of timestamp where transition occurs is very small comparing to the length of a whole time series. Does it really harm the model performance significantly? Plus, when annotating SleepEDF, multiple doctors are already recruited to make an agreement in their annotations, which can reduce inconsistency in state transition regions.

2. Methods seem to be a heuristic without enough justification and not novel. In neighbor class consistency discrimination, there could be so many ways to achieve it but there is no explanation on the design choice the authors made. Also, the theory does not support the reason why $\ell_2$ loss should be used.

3. Experiment setting is not convincing. The labels are disturbed synthetically and one of three datasets is a private dataset, which cannot be reproducible.

### Questions
1. What is the dimension of $x_t$? Is it different from $x_1,\ldots,x_L$? Is $x_t \in \mathbb{R}^{L \times d}$ where $d$ is the number of feature?

2. The function fitting incurs more computations in training loop. Can you elaborate on computational complexity?

3. At which layer $\ell_1$ and $\ell_2$ is applied?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
