# Capturing the Temporal Dependence of Training Data Influence

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Traditional data influence estimation methods, like influence function, assume that learning algorithms are permutation-invariant with respect to training data. However, modern training paradigms—especially for foundation models using stochastic algorithms and non-convergent, multi-stage curricula—are sensitive to data ordering, thus violating this assumption. This mismatch renders influence functions inadequate for answering some critical questions in current machine learning: How can we differentiate the influence of the same data contributing at different stages of training? More generally, how can we capture the dependence of data influence on the optimization trajectory during training? To address this gap, we formalize the concept of \emph{trajectory-specific leave-one-out (LOO) influence}, which quantifies the impact of removing a data point from a specific iteration during training, accounting for the exact sequence of data encountered and the model's optimization trajectory. However, exactly evaluating the trajectory-specific LOO presents a significant computational challenge. To address this, we propose \emph{data value embedding}, a novel technique enabling efficient approximation of trajectory-specific LOO. Specifically, we compute a training data embedding that encapsulates the cumulative interactions between data and the evolving model parameters. The LOO can then be efficiently approximated through a simple dot-product between the data value embedding and the gradient of the given test data. As data value embedding captures training data ordering, it offers valuable insights into model training dynamics. In particular, we uncover distinct phases of data influence, revealing that data points in the early and late stages of training exert a greater impact on the final model. These insights translate into actionable strategies for managing the computational overhead of data selection by strategically timing the selection process, potentially opening new avenues in data curation research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a new method called "Data value embedding" to approximate trajectory-specific Leave-One-Out (LOO) error for individual training samples, which encapsulates cumulative influence of training samples in a training trajectory. It gives some interesting insights of how influence of training batches change during a training process. The authors also provide several tips for reducing the computational cost of the method in practice.

### Strengths
The method introduces a novel concept by capturing data influence in a trajectory-specific manner rather than assuming permutation invariance, which is a common limitation in conventional influence estimation methods. It outlines assumptions and derives an approximation error bound, lending theoretical credibility to the approach. The approach is designed with computational efficiency, including several techniques to reduce the memory and computational cost. It enables identification of high-value data points at different stages of training, allowing practitioners to curate datasets more effectively.

### Weaknesses
The method is explicitly tailored for SGD and is not readily applicable to other popular optimizers like Adam. Although using SGD as a proxy is discussed, this limitation restricts the method's applicability to a broader range of models. The evaluation with ground truth focuses on specific datasets and model types (e.g., MNIST, MLP) due to the computational cost, which may limit the generalizability of the findings. 
Several assumptions are made in this paper, such as model layer independency, learning rate scheduling, which might not be satisfied and lead to reliability issue in such circumstances. Specifically, the assumption of layer independence, while simplifying calculations, may not hold true for complex architectures where cross-layer interactions are significant. Furthermore, the learning rate schedule assumption, while common, may not reflect the diverse schedules used in practice, potentially affecting the accuracy of the influence estimation. The method's reliance on a first-order Taylor expansion for loss change estimation also raises concerns, as this approximation may not be valid when parameter changes are large, particularly for highly influential samples.

### Questions
1. In Line 169, the loss change is estimated by the first-order Taylor expansion, which indicates the $\theta^{'}_T$ and $\theta_T$ should be close, however, when a sample is more important, $\theta^{'}_T$ and $\theta_T$ will be more dissimilar. How this approximation can be valid in such a case?
2. Is there any trajectory pattern of the Hessian $H_k$ observed during the training process?
3. If removing the samples with negative influence scores, will a model get better performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper develops computational tools to quantify the influences of individual data points in a training session, assuming the influences are sensitive to the data order. The authors formalize the idea of trajectory-specific leave-one-out error (TSLOO), accounting for the sequence of training data. To address the computational issue of TSLOO, authors propose an efficient approximation of TSLOO using Gauss-Newton approximation. By using this technique, authors reveal distinct sages of model training such as high-impact warmup phase, low-impact basin and gradual ascending and provide an explanation.

### Strengths
Quantifying data influence is an important task and is crucial active sample selection. However, existing method, the influence function, does not care the order of samples' arrival, making it unsuitable for vast majority of stochastic algorithms. This paper address an important research gap. 

This paper is mostly well-written. The mathematical ideas and their intuitions are clearly presented and is easy to understand. 

The discovery of stages of sample influence is potentially a significant contribution to the wider machine learning community. It reveals how SGD utilize each individual sample at different stages of the training and highlights the importance of selecting data at the right time.

### Weaknesses
Probably due to the lack of a dedicated related work section, it is not clear where does the authors' contribution begin. For example, has TSLOO been studied before or is it a novel concept proposed by  the authors? In Section 2, the first paragraph seems to suggest that this is authors' proposal. However, a later sentence says, "while the technique of unrolled differentiation Hara et al., 2019 explicitly aims to approximate TSLOO ..." It seems the idea of TSLOO already exists in earlier works. If this is true, authors should cite existing works when introducing TSLOO at the beginning of Section 2. 

Similarly, the approximation in Section 3.1 was also used by Hara et al., 2019 and is "well-established" in the literature. This makes me wonder how is the proposed work positioned among existing literature. For example, comparing to Hara et al., 2019, what is the **methodological innovation**? If everything before Data Value Embedding (DVE) is a part of literature review, the authors should make it clear. 

DVEmb in Theorem 2 is an interesting idea. However, the interpretation of this quantity is unclear to me. For example, 
on line 247, "this expression suggests that similar training points encountered in later iterations may have a stronger impact on the data influence score of earlier training points. " I am not sure I understand this statement.  z* are hand picked by the user so why do users care about influence score of earlier training points? Please provide a clearer explanation of this statement and why a practitioner should care about this interpretation. 

on line 252, if z' is identical or highly similar to z*, their gradients will be closely aligned, leading to a significant change in DVE... I don't understand the meaning of "change" here. I guess the authors are talking about **tracking the influence of samples over the training iterations**. However, this setting isn't made clear. I suggest the authors state the context and "setting the scene" before explaining the interpretation of Theorem 2.

### Questions
I suggest a dedicated related work section to clearly delineate authors' novel contributions from existing concepts in the literature (e.g., Hara et al., 2019).  

1. Judging from the line 127 to 134, I suppose authors consider learning of just one epoch? As in the second epoch, the counterfactual sample will again lead to the difference between theta and theta'. Do authors consider multiple epochs? and if it's just one, could authors explain why this is sufficient or how it might generalize to multiple epochs.
 
2. line 148, isn't Hessian H a function of the parameters? 

3. line 239, it isn't clear where does the product of Hessian go at a glance. I recommend authors write briefly about the derivation of Appendix C.3. 

4. Line 435, "This observation aligns with the well-established effect ..." Please cite, as it will also help a general reader (like me) to understand the background of model warm up/generalization. 

5. Figure 4, " the y-axis represents the influence score of selected data points on the model at each checkpoint." How are these data points selected? It would help with reproducibility as well as the representative of the phenomenon.  

also, what is the "green curve" mentioned on line 442.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes a novel data influence estimation method, Data Value Embedding, that captures temporal dependencies in data influence during model training. It addresses limitations of traditional influence functions by considering the order and timing of data exposure, enabling efficient real-time computation of influence scores in modern, non-convergent training settings, such as those used for large language models (LLMs).

### Strengths
1.	The motivation of this paper is clear: modern training paradigms—especially for foundation models using stochastic algorithms and non-convergent, multi-stage curricula—are sensitive to data ordering.
2.	It introduces a computationally efficient embedding method, making it feasible to apply influence estimation to large-scale models without retraining.
3.	Empirical results demonstrate high fidelity in data influence estimation and reveal nuanced phases in training that inform efficient data selection strategies.
4.	It provides insights on the training dynamics of foundation models: a very brief high-influence region at the start, a much longer low-influence basin, and a region in the later training stage with gradually increasing influence, resuming to a high level.

### Weaknesses
1.	Limited Real-World Validation: While the paper’s experiments demonstrate high fidelity on small datasets like MNIST and reduced subsets of larger datasets (e.g., 1% of the Pile), the method may not have been fully validated on more challenging, real-world datasets. This leaves questions about its robustness and scalability when applied to diverse, large-scale data used in production.
2.	Potential Overhead in Implementation: While the method reduces some computational costs, it still requires considerable storage and processing resources, particularly for storing per-sample gradient information and data value embeddings. For truly large models, such as those with billions of parameters, this may limit its practical utility without further optimizations.

### Questions
Could this method be applied to a closed-source model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies data influence for problems with training data not necessarily permutation invariant. Permutation invariant training data are commonly assumed in traditional data influence estimation methods. The authors proposed the concept of trajectory-specific leave-one-out (LOO) error and further proposed data value embedding to approximate trajectory LOO error. Fast computation was developed using simple dot-product between the data value embedding and the gradient of the given test data.

### Strengths
Many machine learning algorithms especially those for supervised learning typically assume the training data points are permutation invariant. Using such an assumption, one can divide the training data for both training and validation using strategies such as k-fold CV, leave-one-out CV etc. As the authors mentioned, many modern machine learning training paradigms especially for foundation models violate this assumption. The goal of this paper is to capture the dependence of data influence on the optimization trajectory during training. The authors proposed the trajectory-specific leave-one-out (LOO) error. Efficient computation was developed as well. Overall, the paper addresses an interesting and timely problem.

### Weaknesses
The problem considered in the paper is certainly interesting. However, it is important to make it clear regarding the type of CV considered in the paper. In supervised learning, CV such as LOO CV was mainly used to estimate the model performance such as prediction errors. The type considered in this paper instead is to quantify the loss change with versus without a particular data point. In this sense, it is perhaps more sensible to call it as influence of the point instead of error. The authors may reconsider the terminology to avoid confusion. If the term of LOO error remains, it is important to clarify the difference of this type and the traditional CV error.

Related to the previous point, in the traditional sense of CV error or LOO error, we would look for small CV error for model selection etc. In the sense of LOO error in the paper, the error is quantified as model’s loss change on a validation data when the training data point is removed from the training set. However, large change in the loss does not necessarily imply big differences in terms of the model performance between with versus without that particular training point. But the goal was to evaluate the model performance of that point on model trained on data without that training point. More discussion and justification are needed.
To address this issue, this review would like to suggest the authors to:

1. Explicitly compare and contrast their LOO error definition with traditional CV error
2. Discuss the implications of using loss change rather than model performance metrics
3. Provide examples or experiments showing how their LOO error relates to changes in model performance

### Questions
1.	How would the proposed data influence handle outliers in training data? For example, if one particular training point was an error or undesirable outlier, would the proposed influence indicate the outlier being very important since it may have big loss differences? That can be undesirable or misleading. It will be helpful if the authors could a). Conduct an experiment specifically examining the behavior of their method on datasets with injected outliers; b). Discuss potential mitigation strategies if outliers are indeed found to have outsized influence; c). Compare how their method handles outliers versus existing influence estimation techniques

2.	Using numerical examples, the authors show that early and late regions have high influence and can achieve similar performance improvements in comparison to using data from the entire process. This is quite interesting but also raises a lot of questions. Intuitively, the high influence of the early region is because one starts with nothing and the information on the early region is consequently high. After that, the added information slows down but builds up for the improvements for late region. Thus, it appears to this reviewer that one cannot simply use the early and late regions for the learning process without the middle region. Thus, more clarification and discussions on this is necessary.

3.	How would the proposed influence measure work for training time series data with seasonal and temporal dependence?

4.	Although quantification of temporal dynamics of training is interesting, the usefulness of this needs to be further explained. Can this help to detect undesirable outlier training points? Or more effective learning using a subset of training data?

### Soundness
3

### Presentation
3

### Contribution
3
