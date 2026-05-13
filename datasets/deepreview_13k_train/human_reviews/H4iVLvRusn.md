# SelKD: Selective Knowledge Distillation via Optimal Transport Perspective

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Knowledge Distillation (KD) has been a popular paradigm for training a (smaller) student model from its teacher model. However, little research has been done on the practical scenario where only a subset of the teacher's knowledge needs to be distilled, which we term selective KD (SelKD). This demand is especially pronounced in the era of foundation models, where the teacher model can be significantly larger than the student model. To address this issue, we propose to rethink the knowledge distillation problem from the perspective of Inverse Optimal Transport (IOT). Previous Bayesian frameworks mapped each sample to the probabilities of corresponding labels in an end-to-end manner, which fixed the number of classification categories and hindered effective local knowledge transfer. In contrast, IOT calculates from the standpoint of transportation or matching, allowing for the flexible selection of samples and their quantities for matching. Traditional logit-based KD can be viewed as a special case within the IOT framework. Building on this IOT foundation, we formalize this setting in the context of classification, where only selected categories from the teacher's category space are required to be recognized by the student in the context of closed-set recognition, which we call closed-set SelKD, enhancing the student's performance on specific subtasks. Furthermore, we extend the closed-set SelKD, introducing an open-set version of SelKD, where the student model is required to provide a ``not selected" response for categories outside its assigned task. Experimental results on standard benchmarks demonstrate the superiority of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper discusses the knowledge distillation (KD) problem from the perspective of inverse optimal transport (IOT), introducing a selective KD (SelKD) framework tailored for classification tasks. Specifically, closed-set SelKD allows the student model trained exclusively on the data relevant to specific tasks, while open-set SelKD enables the student model to identify non-selected knowledge to unassigned tasks. Experimental results on image datasets showcase the superior performance of proposed SelKD over the state-of-the-art methods.

### Strengths
This paper formulates the KD problem as a bi-level optimization through the perspective of IOT. Building on the IOT-based formulation, this paper further proposes novel closed-set and open-set SelKD methods that allow the student model to learn specific knowledge from assigned tasks, making SelfKD well-suited for real-world, resource-constrained environments.

### Weaknesses
However, there are several weaknesses where this paper can improve:
1.  The advantages of the proposed SelKD over vanilla KD are unclear in Figure 1. What are the benefits of training multiple students, each tailored to a specific task, when a general student model showcases consistently strong performance across all tasks in vanilla KD? SelKD could involve higher computational costs due to the need for training multiple task-specific student models. It is not clear if the computational cost of training multiple specialized student models is justified by a significant performance gain over a single, general student model, especially if that general model already performs well across all tasks.

2. To strengthen the justification for the proposed SelKD in resource-constrained environments, the paper should include additional motivation experiments or theoretical analysis demonstrating that a student model cannot fully receive the knowledge from the teacher model, or in other words, that the teacher fails to transfer essential task-specific knowledge to the student. The paper needs to empirically demonstrate the limitations of vanilla KD in transferring task-specific knowledge, particularly in resource-constrained scenarios. This could involve showing that a single student model trained with vanilla KD struggles to achieve optimal performance across diverse tasks, thus motivating the need for task-specific student models.

3. How are the teacher and student models practically deployed/trained? It is challenging to simultaneously train a cumbersome teacher and student on resource-constrained edge device. The paper should clarify the practical deployment scenario, especially given the resource constraints. If the teacher model is trained offline on a powerful machine, this should be explicitly stated, along with details on how the distilled knowledge is transferred to the edge device.

4. In Eqn (11), why is the cost matrix calculated through the multiplication of $f(\cdot)$ and $g(\cdot)$? Is there a specific reason or advantage for using this multiplicative form? The paper needs to provide a more detailed explanation of the rationale behind using the multiplicative form for the cost matrix calculation. What are the implications of this choice, and are there any alternative cost functions that could be considered?

5. The data storage and computational capacity are often limited in resource-constrained environments. Thus, the proposed SelKD is expected to exhibit strong robustness against insufficient training data, while also ensuring efficient computational cost and resource utilization. The paper should include an analysis of the proposed method's performance under limited data conditions, and also provide a detailed breakdown of the computational cost and resource utilization of SelKD compared to vanilla KD, especially in resource-constrained environments.

6. How are subtasks determined? Can the proposed SelKD consistently maintain superior performance when the categories within the same subtask significantly differ from each other? The paper should elaborate on the subtask definition process and provide a discussion on the impact of subtask composition on the performance of the proposed method. It is important to understand whether the method is robust to variations in subtask similarity.

7. Some multi-task KD studies [1-3] should be considered as baselines in the experiments.

### Questions
Please refer to the weaknesses mentioned above.

### Soundness
2

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
3

### Summary
The paper proposes Selective Knowledge Distillation (SelKD) for transferring only selected parts of a teacher model’s knowledge to a student model, framed within the Inverse Optimal Transport (IOT) perspective. This method is relevant for scenarios with resource constraints, where distilling only relevant subsets of knowledge is more practical than full-model distillation. The authors present closed-set and open-set SelKD, where the student learns a subset of categories or can reject classes outside its training scope. Experiments on CIFAR and Tiny ImageNet demonstrate SelKD’s advantages over traditional KD techniques, with improved efficiency and comparable performance on targeted tasks.

### Strengths
The paper addresses a practical challenge in knowledge distillation, particularly relevant to deploying models on edge devices with limited resources. By reinterpreting KD within an IOT framework, the authors introduce an innovative approach to selective knowledge transfer that has potential for efficient model adaptation in constrained environments. The experiments on CIFAR and Tiny ImageNet datasets validate the method’s utility, showing that SelKD can effectively focus on specific subtasks with lower computational costs.

### Weaknesses
1. The experimental validation is somewhat limited, with results provided only on relatively small datasets (CIFAR and TinyImagenet). The model used in the study is relatively small (ResNet50), with significantly fewer parameters than current large-scale pretrained models. I recommend the authors add experiments using larger backbone models such as ViT. The current experiments do not fully demonstrate the scalability of the proposed method to more complex scenarios.
2. Since SelKD relies on label information, it is challenging to extend it to semi-supervised and unsupervised settings. The method's reliance on explicit class labels limits its applicability in scenarios where labeled data is scarce or unavailable. This is a significant limitation, as many real-world datasets lack comprehensive annotations.
3. The open-set SelKD formulation, while promising, lacks guidance on how it could be adapted to real-world scenarios with dynamically changing categories. The paper does not provide a clear mechanism for handling the addition or removal of categories over time, which is a common requirement in practical applications. The current formulation assumes a static set of categories, which is not always realistic.
4. Lack of theoretical guarantee. The paper does not provide a theoretical analysis of the convergence or optimality of the proposed method. This lack of theoretical grounding makes it difficult to understand the method's behavior and limitations.

### Questions
Would the authors consider exploring SelKD in semi-supervised or unsupervised settings where labeled data for all categories may not be available?

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
This paper introduces Selective Knowledge Distillation (SelKD), a novel approach that allows student models to learn only selected subsets of knowledge from teacher models. The authors reformulate knowledge distillation through the lens of Inverse Optimal Transport (IOT) and propose both closed-set and open-set variants of SelKD.

### Strengths
**Originality**: The paper offers a fresh perspective on selective knowledge distillation by using optimal transport (OT) to map logit relationships between image and text features. This new approach allows the student model to learn only the relevant subset of knowledge, making it distinct from traditional, full-transfer methods. This new perspective opens up important new research directions.

**Clarity**: The paper is well-structured, with a clear motivation and related work sections that are easy to follow. The optimal transport concepts are complex, but most parts are presented clearly.

**Significance**: Great motivation: enabling selective transfer for specific tasks. The open-set extension further adds value by allowing the model to handle unknown categories, making it versatile for real-world applications.

### Weaknesses
 **Clarity and Notation**: The notation, especially in the optimal transport section, could be clearer. Key terms and symbols, like 
$z$ in Eq. 2 and $\tilde{P}$ in Eq. 7, should be introduced. Additionally, Algorithm 1 may be challenging for readers unfamiliar with classic OT methods. Providing some background or simplifying this section would improve accessibility. The description of the inner and outer optimization in Eq. 8 lacks sufficient detail, specifically regarding the precise loss function being minimized in the outer loop. It is unclear if it is KL divergence or cross-entropy, and this inconsistency needs to be addressed.

**Computational Complexity**: The paper doesn’t explain the computational cost of the OT-based approach, which may be high given the framework. Information on computation complexity would be helpful to fully understand the method’s practicality and limits. The analysis should include not just training time, but also the memory footprint of the OT calculations, which could be a bottleneck for large-scale datasets or models.

**Performance**: The impact of random seed on results is not shown. Further testing here could demonstrate robustness and validate improvements. The lack of sensitivity analysis regarding the hyperparameters of the OT algorithm, such as the regularization parameter, also raises concerns about the stability and generalizability of the results.

**Feature-level Transport Potential**: The paper briefly mentions feature-level transport but doesn’t explore it. Expanding this aspect could reveal further benefits and justify using OT for representation learning.

### Questions
1. If each subtask requires a separate teacher model, it naturally raises concerns about parameter count and memory costs. Tables presenting parameter counts should clearly explain any dependencies on task splits to avoid misleading impressions.

2. Could you clarify if KL divergence or cross-entropy is minimized in the outer optimization of Eq. 8? The description seems inconsistent.

3. In Figure 2, the green line is shown but not illustrated. Could you clarify this?

4. Switching Tables 2 and 3 order might improve flow.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel method called Selective Knowledge Distillation (SelKD), which enhances student model performance by transferring only partial knowledge. The integration of Optimal Transport (OT) methods is applied to both closed-set and open-set classification tasks, demonstrating that SelKD outperforms traditional knowledge distillation methods. Overall, the paper offers new insights and practical solutions for the knowledge distillation field.

### Strengths
1. The introduction of SelKD allows for effective partial knowledge transfer, reducing redundant learning seen in traditional KD.
2. The method shows high potential for real-world applications, particularly in resource-constrained environments.

### Weaknesses
1. The paper lacks concrete details regarding the derivation and experimental implementation. It would be beneficial to provide specific derivations and related code for the experiments to facilitate reproducibility. The description of the Optimal Transport (OT) based knowledge selection process is not sufficiently detailed, making it difficult to understand the exact mechanisms of the proposed method. Specifically, the paper should clarify how the cost matrix for OT is constructed and how the partial transport is implemented in the context of knowledge distillation.
2. The analysis of experiments is somewhat superficial, particularly concerning parameter impacts. Given that optimal transport (OT) can be heavily influenced by parameters, providing visual analyses of how these parameters affect the results would enhance understanding. The paper does not explore the sensitivity of the method to the choice of the entropic regularization parameter in OT, which is a crucial hyperparameter that can significantly impact the performance of OT-based methods. A more thorough investigation into how this parameter affects the knowledge transfer process is needed.
3. The paper does not include any experiments related to the efficiency of the proposed method. It would be valuable to assess and report the computational efficiency of SelKD in comparison to traditional methods. The computational overhead of calculating the optimal transport plan should be analyzed and compared with the computational cost of standard knowledge distillation techniques. This analysis should include both training and inference time.
4. The experiments primarily focus on ResNet architectures, which restricts the generalizability of the findings. Incorporating more recent distillation methods from 2023 or 2024, as well as testing on different model architectures and datasets, would better demonstrate the effectiveness and versatility of the proposed method. A broader range of experiments, including transformer-based architectures and more diverse datasets, would strengthen the paper’s claims regarding SelKD's applicability.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
3
