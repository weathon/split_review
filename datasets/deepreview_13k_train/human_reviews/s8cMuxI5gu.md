# Towards Eliminating Hard Label Constraints in Gradient Inversion Attacks

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Gradient inversion attacks aim to reconstruct local training data from intermediate gradients exposed in the federated learning framework. Despite successful attacks, all previous methods, starting from reconstructing a single data point and then relaxing the single-image limit to batch level, are only tested under hard label constraints. Even for single-image reconstruction, we still lack an analysis-based algorithm to recover augmented soft labels. In this work, we change the focus from enlarging batchsize to investigating the hard label constraints, considering a more realistic circumstance where label smoothing and mixup techniques are used in the training process. In particular, we are the first to initiate a novel algorithm to simultaneously recover the ground-truth augmented label and the input feature of the last fully-connected layer from single-input gradients, and provide a necessary condition for any analytical-based label recovery methods. Extensive experiments testify to the label recovery accuracy, as well as the benefits to the following image reconstruction.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
paper describes a simple method on label inference and also input reconstruction via analysis on one layer. this can be extended recursively to multiple layers.

### Strengths
the method is simple.

Eq.2 is a key equation. It can be checked with some algebra to be correct. from this equation, other things follow.

### Weaknesses
Eq.(3), there is a term (g_i/x^*), since g_i is a vector and x* is a vector this makes no sense.

the same goes for the term g_i/g_r which is 'vector divide by vector'.

Eq.(5) the authors said "top two entries" but does not precisely define what it means. could it be the two items in y_i with highest values?

table 1, table 2, table 3, table 4 and other results, error bars will be needed. otherwise it makes no sense to say one number has higher values than another.  repeated experiments e.g. using differently trained networks.

section 4.3 line 5, there is a typo.

### Questions
I am not very sure if this work would be of practical value if all the gradients and parameters needed to be known. for white box attack, parameters are known. however gradients should be known for this work to be valid. in practise, do we usually know gradients for each instance?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel algorithm to reconstruct training data in a more realistic scenario where augmented soft labels are utilized during training. Specifically, this paper focuses on the recovery of ground-truth augmented label and last-layer features in gradient inversion attacks instead of those with hard label constraints. Through the analysis of the gradients of cross-entropy loss and introduced variance loss, the proposed algorithm can tackle the recovery of soft labels. Extensive evaluations on various datasets demonstrate the effectiveness of the proposed algorithm.

### Strengths
1. The paper is well-organized and easy to follow.
2. The problem of soft label recovery can be challenging and interesting.
3. The proposed variance loss seems simple and natural.
4. The image reconstruction results of FCN regardless of the bias term seem promising.

### Weaknesses
1. The reason why the proposed variance loss can lead to the global minimum is not well-explained. The intuition behind why minimizing the variance of the gradient with respect to the soft label parameter $\lambda_r$ would lead to the recovery of the ground truth soft label is not clear. A more rigorous analysis, potentially involving the properties of the loss landscape, is needed to support this claim. Specifically, the paper lacks a theoretical justification for why the variance loss would not converge to a local minimum that does not correspond to the correct soft label.
2. The authors should include more comparison with other baselines besides iDLG in label recovery evaluations, such as Table 1. While iDLG is a relevant baseline for hard label recovery, the paper lacks a comparison with other methods that might be adaptable to soft label recovery or that use similar techniques for gradient inversion. The absence of these comparisons makes it difficult to assess the relative performance of the proposed algorithm.
3. Lack details of the metrics to measure the correctness of soft label recovery. The paper mentions using a metric to measure the closeness of two vectors, but it does not provide a clear definition of this metric. The specific formula or the type of distance used (e.g., L1, L2, cosine similarity) should be explicitly stated. Furthermore, it is unclear how this metric is used to evaluate the quality of the recovered soft labels. A more detailed explanation is needed to ensure reproducibility and allow for comparison with future work.
4. The designing of searching procedure needs more explantation, such as the starting point of $\pm 1$. The paper mentions a searching procedure with starting points of $\pm 1$ for the soft label parameter $\lambda_r$, but it does not explain why these values were chosen. A more detailed explanation of the search space and the rationale behind the chosen starting points is needed. It is unclear if these starting points are optimal or if they were chosen arbitrarily. The paper should also discuss the sensitivity of the algorithm to the choice of starting points.

### Questions
1. Please provide more discussion of variance loss.
2. Please provide more comparisons in label recovery evaluation.
3. Please explain the metrics in soft label recovery.
4. Please provide more discussion of the searching procedure in Section 3.3.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a framework designed to address the label recovery problem while incorporating features such as label smoothing and mixup. Their experimental results demonstrate the adaptability of their gradient inversion attacks in practical, real-world scenarios.

### Strengths
Seems that the performance is good compared with previous methods.

### Weaknesses
The introductory background and algorithm derivation may lack clarity, potentially causing individuals unfamiliar with this field to become confused.

### Questions
Why the label vector can be viewed as a function of the gradient in equation (3)?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for gradient inversion attack with relaxation from hard labels to soft labels. The proposed method is based on a variance loss function and corresponding analysis is presented.

### Strengths
1. This paper identifies an interesting gap for gradient inversion attack, i.e., the hard label constraints, and proposes a soft label recovery method that is closer to realistic scenarios.

2. Although the proposed method is simple, it is intuitive and effective. Its simplicity also adds value to its applicability.

3. Effectiveness is shown by the experimental results quantitatively and qualitatively.

4. Code is provided in the supplementary.

### Weaknesses
My major question is about the assumption made regarding the label format. Does the proposed method assume the label format is known in advance or not?

- First, does the method assume it is known whether a hard label or soft label is used? 
- Second, does the method assume it is known whether label smoothing or mixup is used as the format for the soft label? 

If they are all known, I am curious about other versions of the results in Table 3 when the label format is unknown, corresponding to the above two settings. One setting is that we don't know whether the label is hard or soft. The other setting is that we don't know the specific format of the soft label. I think these two settings are closer to the real-world cases.

Minors:
- In Figure 2, it is better to also zoom in and visualize the global minimum similarly.
- In Table 2 caption, experiences > experiments.

### Questions
Please refer to the Weaknesses. I would appreciate comments on the assumption of the label formats and additional results if applicable.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
