# A few-shot Label Unlearning in Vertical Federated Learning

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 5, 8

## Abstract
This paper addresses the critical challenge of unlearning in Vertical Federated Learning (VFL), an area that has received limited attention compared to horizontal federated learning. We introduce the first approach specifically designed to tackle label unlearning in VFL, focusing on scenarios where the active party aims to mitigate the risk of label leakage. Our method leverages a limited amount of labeled data, utilizing manifold mixup to augment the forward embedding of insufficient data, followed by gradient ascent on the augmented embeddings to erase label information from the models. This combination of augmentation and gradient ascent enables high unlearning effectiveness while maintaining efficiency, completing the unlearning procedure within seconds. Extensive experiments conducted on diverse datasets, including MNIST, CIFAR10, CIFAR100, and ModelNet, validate the efficacy and scalability of our approach. This work represents a significant advancement in federated learning, addressing the unique challenges of unlearning in VFL while preserving both privacy and computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper aims to address the label unlearning problem in vertical federated learning (VFL). It demonstrates the lable leakage issue with applying traditional techniques in lable unlearning in VFL and proposes a few shot unlearning method to address mitigate this issue. Extensive experiments on 4 datasets and 2 model architectures show that the proposed method is effective and effcient while preserving good utility.

### Strengths
- The paper is well structured and generally easy to follow
- The proposed method is intuitive and seems to be technically sound
- Extensive experiments on 4 datasets and 2 model architectures demonstrate the effectiveness of the proposed method

### Weaknesses
 - As mentioned in the introduction, VFL is mostly used in finance, healthcare, or ecommerce scenarios, but this work mostly validated the proposed method on simple vision datasets.
- The discussion and presentation of experiment results can be improved. e.g., the paper discusses utility in Sec 5.2.1 but also mentioning effectiveness in Figure 4 in Sec 5.2.2. It is not intuitive to compare different methods on these two aspects easily. 
- Figure 1 is not easy to understand and interpret the label leakage risk.
- VFU seems to be used without definition

### Questions
- Can the proposed method be applied to non-vision datasets or other vision tasks other than classification?

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
This paper focuses on the unlearning problem in vertical federated learning (VFL). The authors leverage a limited amount of data for unlearning to mitigate the label leakage risk of existing unlearning methods. In particular, the authors propose to mixup feature embeddings during the learning process. Then during the unlearning process, the mixup scheme can be utilized to augment the limited data. The unlearning is finally achieved by gradient ascent on the augmented data. Experiments conducted on diverse datasets validate the performance of the proposed framework.

### Strengths
* The discussed topic, unlearning in VFL, is important.
* The writing is clear.
* The proposed mixup augmentation is simple yet effective.
* The empirical results demonstrate the effectiveness of the proposed framework. The model after unlearning demonstrate high accuracy and low attack success rate.
* The ablation is extensive and helpful.

### Weaknesses
As shown in Equation (3), the feature size of the active party increases quadratically as the number of clients increases. Therefore, the scalability of the framework is relatively limited.

The effeciency of the proposed method is still doubted.
The authors did not correct their submission.
I will maintain my score.

### Questions
As shown in Figure 4, the ASR of Amnesiac is abnormally high (up to 96.1) on CIFAR-100 with Resnet 18 architecture while ASR of Amnesiac on other datasets or architectures is only up to 3.1. Could the authors provide more explanations?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a few-shot label unlearning method specifically designed for Vertical Federated Learning (VFL) to mitigate privacy leakage risks associated with traditional unlearning approaches. In VFL, multiple organizations collaborate on model training by sharing some sample IDs while differing in feature sets, making it particularly suitable for sensitive fields such as banking and healthcare. This method leverages a small amount of private data and manifold mixup to augment embeddings, employing gradient ascent to remove labels from the active party’s model and transferring inverse gradients to the passive party to ensure independent label removal from both models. Experimental results demonstrate that this approach achieves rapid and effective label unlearning across various datasets, significantly reducing privacy leakage risks.

### Strengths
1. **Introducing the first method for label unlearning in Vertical Federated Learning (VFL)**: This paper pioneers a novel approach specifically tailored for the removal of label information in VFL settings, addressing a critical gap in existing federated learning literature. Unlike prior work focused on feature-based unlearning, this method uniquely targets the secure and efficient unlearning of labels across collaborative models, enhancing data protection compliance in sensitive domains.

2. **Detailing potential privacy leaks in traditional unlearning methods**: The paper systematically examines the vulnerabilities of conventional unlearning techniques when applied to VFL, especially the risk of sensitive label information being inadvertently exposed to other parties during the unlearning process. By identifying specific points of leakage, this study highlights the importance of secure information flow between the active and passive parties in VFL.

3. **Proposing an effective few-shot unlearning approach that uses limited data and enhances unlearning with manifold mixup**: To minimize data exposure, this approach relies on a small subset of private data, significantly reducing privacy risks. Through manifold mixup, the method augments data embeddings, allowing for robust and efficient unlearning with minimal information. This few-shot strategy achieves a balance between privacy preservation and computational efficiency, making it practical for real-world applications.

4. **Demonstrating superior unlearning performance on benchmark datasets like MNIST, CIFAR-10, CIFAR-100, and ModelNet**: Extensive experiments validate the method's effectiveness and speed in removing target labels, outperforming traditional unlearning techniques on widely used datasets. The results illustrate the approach’s scalability and adaptability across diverse data types, affirming its potential for high-performance unlearning in federated settings.

### Weaknesses
1. The paper lacks a preliminary section to help readers understand the meaning of each mathematical symbol. Some symbols are not explained, making it difficult for me to follow the methodology. Please clarify the definition of each variable in the paper.

2. While the paper’s motivation is clear and innovative, it lacks explanations regarding specific methods, such as why gradient ascent and inverse gradient can remove label information. Additionally, I am uncertain whether the proposed method guarantees convergence. Please provide an analysis or discussion on the forgetting functionality and convergence of this method.
(1). provide a theoretical justification for why gradient ascent and inverse gradients are effective for label removal
(2). Include a convergence analysis or discussion of the conditions under which convergence is guaranteed
(3). Offer more detailed explanations of the forgetting mechanism and how it ensures complete removal of label information

3. The experimental setup lacks sufficient detail, including which categories were selected for forgetting in each dataset, the number of clients, and how data attributes were assigned. Please add a more detailed description of the experimental setup.
(1). A table or list of the exact categories chosen for forgetting in each dataset
(2). The number of clients/parties involved in each experiment
(3). A description of how data attributes were distributed among the parties This level of detail would allow for better reproducibility and understanding of the experimental conditions.

### Questions
See weakness

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper explores the unlearning process in vertical federated learning (VFL), a topic that has been relatively underexplored in prior research. The authors highlight the risk of label leakage during the unlearning phase and propose a solution to address this issue. Their method utilizes a small set of labeled data, combined with feature mixup and gradient ascent, to mitigate the leakage of label information from VFL systems.

### Strengths
1. The proposed method is simple and intuitive, approaching the unlearning process from a few-shot perspective and utilizing feature mixup to handle limited sample sizes.
2. The method demonstrates broad applicability.
3. Extensive experimental results indicate that the method not only performs consistently across various datasets and models with different numbers of clients but can also be effectively integrated with differential privacy and gradient compression methods. Furthermore, the proposed method exhibits the lowest unlearning cost compared to its competitors.

### Weaknesses
1. The label leakage described in Sec. 3.2 would only occur if both active and passive clients share the same label space. However, in most VFL scenarios, clients have distinct label spaces. Therefore, this assumption of label leakage is questionable.
2. In the introduction, the statement that "... the passive party holds the features, ... the active party possesses the labels." is inaccurate. The active party also holds its own features.
3. Some notations are unclear. For instance, in line 152, "{x^u_k}" is used, but the variable "u" is not defined. I assume it refers to samples for unlearning.
4. The figures are difficult to interpret, particularly Fig. 1 and Fig. 6.
5. The mix rate lambda is crucial to the method. However, the authors neither provide a thorough analysis of this hyperparameter nor clarify whether lambda remains consistent across different clients.

### Questions
Please check the weakness part for details.

### Soundness
3

### Presentation
3

### Contribution
3
