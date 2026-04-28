# ProtoReg: Prioritizing Discriminative Information for Fine-grained Transfer Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6

## Abstract
Transfer learning leverages a pre-trained model with rich features to fine-tune it for downstream tasks, thereby improving generalization performance. However, we point out the "granularity gap" in fine-grained transfer learning, a mismatch between the level of information learned by a pre-trained model and the semantic details required for a fine-grained downstream task. Under these circumstances, excessive non-discriminative information can hinder the sufficient learning of discriminative semantic details. In this study, we address this issue by establishing class-discriminative prototypes and refining the prototypes to gradually encapsulate more fine-grained semantic details, while explicitly aggregating each feature with the corresponding prototype. This approach allows the model to prioritize fine-grained discriminative information, even when the pre-trained model contains excessive non-discriminative information due to the granularity gap. Our proposed simple yet effective method, ProtoReg, significantly outperforms other transfer learning methods in fine-grained classification benchmarks with an average performance improvement of 6.4\% compared to standard fine-tuning. Particularly in limited data scenarios using only 15\% of the training data, ProtoReg achieves an even more substantial average improvement of 13.4\%. Furthermore, ProtoReg demonstrates robustness to shortcut learning when evaluated on out-of-distribution data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper pointed out an issue in fine-grained transfer learning, called the "granularity gap" , i.e., less-discriminative information is also transferred with the discriminative information from a pre-trained model to the downstream model and harmful to the performance of the downstream task. A method called ProtoReg is thus proposed to prioritize fine-grained discriminative information via crafted prototypes, consisting of several main steps including prototype initialization, prototype refinement, and prototype aggregation and separation. Overall, the proposed method sounds technical convincing. Although ‘simple’ is a strong advantage claimed by the authors, the proposed ProtoReg might also come up with some critical drawbacks, e.g., tending to overfit the fine-grained information due to the clustering nature of the proposed method. Besides, the improvement in the performance is not well convincing since the comparing methods are not very up-to-date and basically not focusing on fine-grained problem.

### Strengths
The key idea behind the proposed method is reasonable and the method itself is simple to implement.

### Weaknesses
· Class-wise prototype generation could lead to overfitting issues.
· Presentations on some key technical contents are not very clear, e.g., why and how exactly the equation (4) is formed.
· Experiments are not well supportive, e.g., the comparing methods are not very up-to-date and basically not focusing on fine-grained problem.

### Questions
· How to ensure the generality of the proposed method? To be specific, the discriminative is a relative concept. While the representative prototypes could preserve the main fine-grained information over each class, it does not necessarily preserve marginal fine-grained characteristics of the data, e.g., according to the theory of distributional clustering.
· Computational overhead should be also reported. Although the proposed method is simple to implement, its clustering nature (repeating to compute the 'similarity' between two data points) can make the complexity very high.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the problem of fine-tuning a pre-trained model for a fine-grained downstream task. The authors point out that there is a granularity gap between the information learned by the pre-trained model and the fined-grained downstream task, and then propose a fine-tuning approach by utilizing prototypes to prioritize the discriminative information. The experimental results show that the method is able to effectively improve the performance of the fine-grained classification tasks.

### Strengths
1. The topic this paper pays attention to is important. As fine-tuning a pre-trained model for a particular task has been a standard learning paradigm in computer vision, it is valuable to study how to deal with the case where the downstream task is fine-grained, which has not been studied deeply.
2. The motivation of this paper is clear. I agree with the authors' viewpoint that there is a granularity gap between the level of information learned by the pre-trained model and the semantic details required for a fine-grained downstream task, which is the main problem to solve in fine-trained transfer learning.
3. The proposed method based on prototype aggregation is straightforward and not difficult to realize.
4. The English writing of this paper is generally good.

### Weaknesses
1. The novelty of this paper is not so significant. The idea of exploiting prototypes to represent and adjust the feature distribution according to label information from samples has been studied in a lot of works. Although the idea of utilizing such mechanism to fine-tune a pre-trained model for downstream fine-grained tasks is new, I do not recognize significant difference between the key idea of this work and the previous ones. It does has some novelty, but I am not sure whether it is sufficient to meet the criterion of ICLR.
2. Although the motivation of solving the problem of granularity gap is interesting, I do not quite understand how the proposed mechanism with prototypes helps to eliminate such "gap" under the perspective of transfer learning. In more detail, it seems that this method can also be used to train a randomly initialized model for the fine-grained task, because I do not see a mechanism to "preserve" useful information from the original pre-trained model but only recognize the mechanism to make change to the model.
3. A minor problem: the last sentence of the comments of Figure 1 is confusing. Maybe the word "suffer from" is not correctly used.

### Questions
1. Considering the 2nd drawback listed above, please explain whether there is a mechanism to discover and  preserve useful information from the pre-trained model.
2. It is a common scene for real data that each class may have multiple prototypes. How do the authors deal with such a case?
3. Please explain why two different prototype updating strategies are used according to their initialization methods? What is the motivation or consideration of their designs, respectively?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed prototype-based regularization losses to improve transfer learning for fine-grained classification. To be specific, adaptively evolving prototypes for each class are first introduced. The aggregation loss, which aggregates features with their corresponding prototypes, and the separation loss, which enforces features away from prototypes of different classes, are jointly optimized with the cross-entropy loss for fine-tuning. Comprehensive experiments are conducted to validate the efficacy of the proposed method.

### Strengths
1. The paper is well-written, making it easy to follow.  
2. Sufficient experimental studies are provided.

### Weaknesses
1. The idea of prototype-based loss is not novel for dealing with the limited data scenario. Such an idea could be tracked back to the early few-shot research [1]. The proposed aggregation loss and the separation loss are same as the Eq. (2) in [1].

2. The challenge of fine-grained classification I think lies in its limited data for each class, tens of samples for each class in most benchmark datasets (Table 6 A.2). For CIFAR100, hundreds of samples for each class, the proposed method achieves insignificant perform gains compared to CE (Table 7). Therefore, I think the few-shot works are related and should be included in the literature review.

3. Some experimental results seem unfair. For the results in Figure 1 and Figure 3, the case where ProtoReg succeeds while others fails is picked up. A question arises here: whether the samples that ProtoReg mis-classify are mis-classified by CE? If so, the extra mis-classification by CE would indicate its deficiency. Otherwise, ProtoReg and CE possibly have different shortcuts. The results presented should be more statistical.

Minor:
1. The pseudo-code did not include the refinement for the prototypes based on linear classifier weights.

### Questions
See the above weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a prioritizing discriminative information method to handle the granularity gap challenge in fine-grained transfer learning. It first computes class-discriminative prototypes and then refines the prototypes to gradually capture more fine-grained details as well as aggregate features with corresponding prototypes.

### Strengths
1.	This paper points out a key challenge in fine-grained transfer learning, the granularity gap challenge, and proposes a novel ProtoReg approach to address this.
2.	Experimental results demonstrate the effectiveness of the proposed ProtoReg method on both inter-dataset and intra-dataset transfer learning.
3.	Delicate visualization results are provided as clear illustrations of the motivation and effectiveness of the proposed method.
4.	A valid appendix is provided to improve the completeness of this article.

### Weaknesses
1.	More details of ablation studies should be provided to further clarify the effectiveness of the proposed method. For example, the experiments with configurations “L_ce + L_aggr + L_step”, “L_ce + L_step + Refine” should be conducted to demonstrate the effectiveness of L_step when applied under different conditions. Specifically, it is unclear how the individual contributions of L_aggr and the Refine step interact with L_step, and whether their combination provides a synergistic effect or if one component dominates the performance gain. The absence of these specific ablations makes it difficult to fully understand the necessity of each component in the proposed framework.
2.	Some details of the proposed method should be stated more clearly. For example, in Equ (2), how \phi is defined and how the “argmax” value is computed with respect to the classification accuracy should be explicitly declared. The current description lacks sufficient detail regarding the initialization of \phi and the optimization process used to determine the argmax. It is not clear whether \phi is a learnable parameter or a fixed value, and the connection between the argmax operation and the downstream classification accuracy needs further elaboration. Furthermore, the specific optimization algorithm used to find the argmax should be stated.

### Questions
1.	Can ProtoReg outperform SOTA methods on other downstream tasks of transfer learning, such as semantic segmentation?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
