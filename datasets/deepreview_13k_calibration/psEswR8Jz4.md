# AmortizedPeriod: Attention-based Amortized Inference for Periodicity Identification

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Periodic patterns are a fundamental characteristic of time series in natural world, with significant implications for a range of disciplines, from economics to cloud systems. However, the current literature on periodicity detection faces two key challenges: limited robustness in real-world scenarios and a lack of memory to leverage previously observed time series to accelerate and improve inference on new data. To overcome these obstacles, this paper presents AmortizedPeriod, an innovative approach to periodicity identification based on amortized variational inference that integrates Bayesian statistics and deep learning. Through the Bayesian generative process, our method flexibly captures the dependencies of the periods, trends, noise, and outliers in time series, while also considering missing data and irregular periods in a robust manner. In addition, it utilizes the evidence lower bound of the log-likelihood of the observed time series as the loss function to train a deep attention inference network, facilitating knowledge transfer from the seen time series (and their labels) to unseen ones. Experimental results show that AmortizedPeriod surpasses the state-of-the-art methods by a large margin of 28.5% on average in terms of micro $F_1$-score, with at least 55% less inference time.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the periodicity detection problem with the proposed AmortizedPeriod method by considering Bayesian modeling and deep learning. The motivation is good, the literature review is comprehensive, and the proposed method has competitive experimental performance. On the other side, some concerns are raised about the paper writing and the technical design and illustration. For more details, please refer to the following sections.

### Strengths
- The literature review is quite comprehensive, including the periodic time series, Ramanujan subspaces, and different kinds of priors.

- The Bayesian modeling designed for periodicity identification seems novel and comprehensive.

- The experiments are extensive, and the provided results are very competitive.

### Weaknesses
 - The first and biggest concern raised by the reviewer is how the proposed two challenges get addressed by the proposed model. For the first challenge "robustness", how do the designed Bayesian modeling and encoder-decoder model address it? Specifically, the paper does not clearly articulate how the Bayesian framework inherently handles trends, noise, and outliers better than existing methods, especially given that these components are often modeled explicitly in other approaches. Furthermore, how does the proposed AmortizedPeriod solve the "memorylessness" challenge, i.e., the second challenge, especially when the experimental running time of the proposed AmortizedPeriod is superior? It's unclear how the model 'memorizes' past information to avoid iterative optimization, and the mechanism behind this 'memorization' is not explained with sufficient technical detail. The claim of superior running time needs more justification in the context of this memorylessness claim.


- Section 3.1 is somehow deep for some audiences and does not motivate Section 3.2 very well, the plain definition occupies much space but neither motivates the formulation proposal in Section 3.2 nor adds values for the statement of why it is sensitive to trends, noises, and outliers. The connection between the Ramanujan subspaces and the practical challenges of periodicity detection is not made explicit enough. The section lacks a clear explanation of why the properties of Ramanujan subspaces are crucial for addressing the limitations of existing methods. It also fails to illustrate how the sensitivity to trends, noise, and outliers arises from the formulation itself.


- The setting of semi-supervised learning in Section 3.5 is not very clear, e.g., what is the role of sub-period and how it works in the learning and classification. The paper introduces the concept of sub-periods but does not provide a clear explanation of how these sub-periods are utilized within the semi-supervised learning framework. The mechanism by which the model leverages the information from sub-periods to improve the learning process is not sufficiently detailed. The connection between the sub-periods and the overall periodicity detection is not clearly established, making it difficult to understand the practical implications of this semi-supervised approach.


- The symbols, notions, and indexing are somehow messy.

### Questions
Please refer to the first and the third points in the above section.

### Soundness
3 good

### Presentation
2 fair

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
The authors propose a new approach for identifying periodic patterns in time-series data. They introduce AmortizedPeriod, which integrates Bayesian statistics and deep learning using an attention-based amortized variational inference model. AmortizedPeriod is capable of capturing various components of time series data, including multiple and irregular periods, trends, noise, outliers, and missing data. They also present a self/semi-supervised learning framework for the inference model to leverage knowledge from previously observed time series. Extensive experiments on four datasets demonstrate that AmortizedPeriod outperforms existing state-of-the-art methods with significant computational efficiency gains.

### Strengths
(1) The proposed model has good robustness in dealing with a variety of data anomaly scenarios, and addresses the limitations of current methods in terms of memorylessness. The authors present sufficient mathematical proofs in the method and appendix. 
(2) The attention-based amortized variational inference model is innovative. The self/semi-supervised learning framework allows the inference model to leverage past knowledge, improving the inference efficiency on new data. 
(3) The experiments implemented are relatively complete. From the experimental results, AmortizedPeriod has achieved a very significant advantage compared with state-of-the-art methods. The experimental section demonstrates the effectiveness and computational efficiency of AmortizedPeriod.

### Weaknesses
(1) The structure of thesis, however, is a little bit unreasonable. The description of the method takes up a lot of space, resulting in a somewhat inadequate analysis of the experiments that follow (although some are also presented in the appendix). Specifically, the detailed mathematical derivations and explanations of the Ramanujan subspaces, while important, could be more concisely presented or moved to an appendix to allow for a more thorough discussion of the experimental results and their implications. The current structure leaves the reader with a strong understanding of the model but a weaker grasp on its practical performance and limitations.
(2) The baselines in this work may not be enough. It is better to supplement some methods proposed in recent years to baselines. (e.g., Robust Dominant Periodicity Detection for Time Series with Missing Data", published at ICASSP 2023). The current selection of baselines, while representative of common approaches, might not fully capture the state-of-the-art in handling time series with the specific challenges addressed by the proposed method, such as irregular periods and missing data. A more comprehensive comparison would strengthen the claims of the paper.
(3) To enhance the solidity of this work, it is suggested to add some public data sets (e.g., CRAN) to evaluate the performance on AmortizedPeriod and the baselines. The current evaluation relies on a limited number of datasets, which may not fully capture the generalizability of the proposed method across different types of time series data. Including a more diverse set of publicly available datasets would provide a more robust assessment of the method's performance and its applicability to real-world scenarios.

### Questions
(1) If CRAN is included, can it be described in two parts (single-periodicity detection and multi-periodicity detection) in the experimental analysis? I think that providing such an experimental analysis helps to further demonstrate the generalization of AmortizedPeriod.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To tackle the problems of limited robustness and lacking memory, the authors proposed AmortizedPeriod for Periodic patterns combining Bayesian statistics and deep learning. The proposed method can model the correlation of the periods, trends, noise, and outliers in time series, and take use of missing data and irregular periods at the same time. The authors also conduct several experiments to prove the effectiveness of the proposed framework.

### Strengths
S1. The periodicity detection task is essential and interesting.
S2. The authors provide rigorous theoretical analysis for their proposed methods.
S3. The authors have conducted several experiments to indicate the effectiveness of their proposed methods.

### Weaknesses
W1. The authors may include more preliminaries to explain the tasks, such as problem definition. This can be beneficial for readers without sufficient background of periodicity detection tasks to understand the paper. Specifically, the paper lacks a clear definition of what constitutes a periodic signal in the context of time series analysis, and how this differs from other forms of temporal patterns. The current introduction assumes a level of familiarity that may not be universal, and a more rigorous foundation would improve accessibility.
W2. The authors may include more error metrics to measure the performance of periodicity detection tasks like other classification tasks. While the paper presents some evaluation, it would benefit from a broader set of metrics to fully capture the nuances of performance, such as precision, recall, and F1-score, especially considering that periodicity detection can be framed as a multi-class classification problem where each period is a class. This would allow for a more comprehensive understanding of the strengths and weaknesses of the proposed method.
W3. The authors may add more downstream tasks to further evaluate the effectiveness of periodicity detection tasks. The paper focuses on the detection of periodic patterns but does not explore how these detected patterns can be used in downstream tasks. This limits the practical impact of the work, as the utility of a method is often demonstrated by its ability to improve performance in real-world applications.

### Questions
1.	Can the author include more preliminaries?
2.	Can the author include more error metrics?
3.	Can the author add more downstream tasks?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the periodicity detection problem, and proposed a model AmortizedPeriod which can address the limited robustness and memorylessness problems in SOTA by applying Bayesian paradigm and variational inference. Extensive experiments are conducted.

### Strengths
1. The paper is well organized and well presented.
2. A novel model AmortizedPeriod is proposed which can address the limited robustness and memorylessness problems in the existing works.
3. Extensive experiments are conducted to validate the model effectiveness, the results look promising.

### Weaknesses
1. Since the proposed model is trying to deal with time series data with self-attention, which also requires a lot of memory, there should be some experiments to compare the memories used by the proposed method and other methods.
2. In the experiment, the results of multiple periodicity scenarios should be provided, for example, when the data has multiple periodicity, irregular periods, noise, outliers, etc.

### Questions
Please address the questions above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
