# Semantic Aware Representation Learning for Lifelong Learning

- Decision: Accept
- Scores: 8, 6, 3, 6

## Abstract
The human brain excels at lifelong learning by not only encoding information in sparse activation codes but also leveraging rich semantic structures and relationships between newly encountered and previously learned objects. This ability to utilize semantic similarities is crucial for efficient learning and knowledge consolidation, yet is often underutilized in current continual learning approaches. To bridge this gap, we propose Semantic-Aware Representation Learning (SARL) which employs sparse activations and a principled approach to evaluate similarities between objects encountered across different tasks and subsequently uses them to guide representation learning. Using these relationships, SARL enhances the reusability of features and reduces interference between tasks. This approach empowers the model to adapt to new information while maintaining stability, significantly improving performance in complex incremental learning scenarios. Our analysis demonstrates that SARL achieves a superior balance between plasticity and stability by harnessing the underlying semantic structure.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel approach for continual learning by utilizing sparse activations to capture semantic relationships between objects. The authors suggest that leveraging activation sparsity emulates the sparse coding observed in biological neural systems. Prototypes are introduced as a means to represent each object, thereby facilitating knowledge retention across tasks. Experimental evaluations are conducted on benchmark continual learning datasets, including Seq-CIFAR10, Seq-CIFAR100, and Seq-TinyImg, demonstrating the proposed method's performance.

### Strengths
- This paper is relatively well-motivated.
- The paper is easy to follow.

### Weaknesses
 - **Backbone Modifications**: It appears that the backbone architecture is altered (Section 3.3 on Sparse Coding) to incorporate sparse activations, which seem to increase similarities (as shown in Fig. 2). This modification, specifically the replacement of ReLU with k-WTA, could give the proposed method an advantage over other baselines by potentially altering the representational capacity of the network, and this needs further investigation to ensure a fair comparison.

- **Unjustified Claims**: 
  - Line 248: The claim that "sparse activations further enhance the model’s ability to distinguish between similar and dissimilar objects" lacks sufficient justification. The provided similarity matrices in Figure 2, while showing some differences, do not conclusively prove this claim. A more rigorous analysis, perhaps involving quantitative metrics on inter- and intra-class similarities, is needed to support this assertion.
  - Line 284: The statement that sparse coding "fosters stability in the model’s knowledge but also mitigates the risk of forgetting important semantic relationships established in earlier learning phases" is unsupported by clear evidence in the text. There is no direct analysis or experiment that demonstrates this stability or mitigation of forgetting.

- **Inconsistent Notation**: 
  - In Equation (3), symbols like \( S_c \) and \( C^t \) should use set notation for clarity, as they appear to represent sets of classes or samples. The current notation is ambiguous. 
  - There is inconsistency in interval notation (e.g., \( 0:t \) versus \( \{0:t\} \)). The notation should be consistent throughout the paper to avoid confusion.
  - Vectors are not visually distinct from scalars; for example, \( a_i \) and \( o_b^c \) are written in the same style as scalar values, which makes the notation confusing. Using boldface or arrows for vectors would improve readability.

- **Objective Complexity and Lack of Ablation**: The objective function comprises five different components, many of which rely on existing objectives, such as consistency regularization. However, no ablation study is provided, making it challenging to determine the contribution of each component to the model's performance. Specifically, the impact of the following components is unclear:
  - Regularization on object prototypes
  - Consistency regularization loss
  - Semantic-aware metric loss
  - Two cross-entropy losses—one for the current training batch and another for buffer samples. The interaction and individual contributions of these components are not well understood.

 - **Lack of recent sota baseline**

 [1] Meta continual learning revisited: implicitly enhancing online hessian approximation via variance reduction, ICLR 2024

 [2] Interactive Continual Learning: Fast and Slow Thinking, CVPR 2024

 [3] Bilateral memory consolidation for continual learning, CVPR 2023

### Questions
- Given that object representations are \( L_2 \)-normalized, why use the simple mean (Eq. 1) instead of considering a spherical manifold? Why not use similarity (sim) instead of \( L_2 \) distance in Eqs. 4 and 5?

- Some experimental details are missing. For example, the number of steps or epochs for the warm-up stage at each task is not specified. Additional details on the sparse backbone and its comparison with a regular backbone would also be beneficial.

- Memory requirements should be clarified, as different components are stored during training in addition to the buffer from previous tasks (e.g., object prototypes and logits from the previous model state).

### Soundness
3

### Presentation
2

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
This paper tries to strengthen continual learning methods' ability to utilize semantic similarities for efficient learning and knowledge consolidation. The authors propose Semantic Aware Representation Learning (SARL). SARL employs sparse activations and principled approaches to assess similarities between objects encountered in different tasks and subsequently uses them to guide representation learning. Experimental results show that SARL balances plasticity and stability by harnessing underlying semantic structure.

### Strengths
The paper is well-structured and easy to follow. The methodology section is thorough and provides detailed explanations.

### Weaknesses
1. The method appears to conflict with the problem setting. Specifically, the proposed method stores samples from previous tasks to update the model in future CIL tasks. It seems inconsistent with the CIL problem setting, where samples from previous tasks are not accessible, and storing old samples could lead to information leakage. Please provide a reasonable explanation for this discrepancy.
2. The comparison methods are somewhat limited. The authors only compare their approach with methods that are similar to their own, while overlooking other approaches that also address the CIL problem, such as those based on pre-trained models (e.g., L2P, DualPrompt, etc.). I suggest that the authors clarify their perspective in the “RELATED WORK” or “ANALYSIS” section if they believe these comparisons would not be fair.
3. The evaluations are insufficient. This paper relies solely on “average accuracy” as the evaluation metric, neglecting other important measures such as final accuracy and model forgetting. I recommend including metrics for “top-1 accuracy after the final stage” and “final forgetting” to ensure a comprehensive evaluation of the proposed method.
4. Conflicting notation. Below Eq. (3), the authors state, "... and $C^{0: t}$ represents the set of all object categories observed up to task $t$." Here, "$C^{0: t}$" should be corrected to "$C^{\{0: t\}}$". Please carefully proofread the entire paper to ensure consistency in symbols and notation.
5. Typos. In the first paragraph of Appendix A, there is an extra "I" in the last line. Please thoroughly proofread the entire paper to ensure it is free of similar errors.

### Questions
Please refer to Strengths and Weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a method to reduce catastrophic forgetting in continual learning by taking advantage of several aspects: 1) the semantic relationships between learned classes, 2) representation sparsity, and 3) prototype regularization and other losses. The method draws inspiration from the brain’s sparse coding approach and employs activation sparsity to facilitate semantic information encoding in representations to promote reusability and reduce forgetting.

### Strengths
1. The paper is clear and easy to read.
2. The combination of losses is interesting.
3. The performance results are very good.

### Weaknesses
1. The introduction could benefit from being more specific and quicker in presenting the problem, current limitations, and how the paper addresses these issues in the technical section. A more concise and more streamlined rewrite is recommended.

2. The novelty appears to be somewhat limited, as deep neural networks inherently build and use semantic representations. A clearer motivation for the novel use of Eqs. (1), (2), ..., (5) (6) would be beneficial. Additionally, an introduction to these losses/similarities should be provided to ensure the reviewer understands they are not being presented as novel contributions. Clarification is needed on how the proposed approach to semantic representations differs from or improves upon standard deep learning methods. Additionally, the motivation and novelty behind the specific formulations in Eqs. (1)-(6) should be explained, and it should be explicitly stated which components are novel contributions versus established techniques.

3. In the reviewer's opinion, the paper is a solid combination of well-established techniques that achieves good performance. However, it may be worth considering whether a different venue might be a better fit for this type of contribution. ICLR often prioritizes papers with some analytical theoretical analysis, while contributions that mainly involve combining established techniques with primarily empirical evidence may be less prioritized.

4. The content on lines 054 to 055 is somewhat generic and does not sufficiently characterize the current limitations and issues. A more detailed description, including a toy problem to demonstrate qualitatively how this affects catastrophic forgetting in practice, would be beneficial. The reviewer may not fully grasp all the details of the paper and the insights that led to the proposed approach; therefore, proposing a concrete toy problem may not be straightforward, as it typically depends on the specific effect intended to be demonstrated. One possible suggestion is to choose a small dataset, such as CIFAR-10, and represent it in a 2D or 3D feature space, or, if >3D, using a scatterplot of the feature distribution or a dimensionality reduction technique like t-SNE to illustrate how the semantic aspects contribute as proposed by the authors in the introduction. These papers present some classic methods for visualizing feature representations:

- Wen, Yandong, et al. "A discriminative feature learning approach for deep face recognition." Computer vision–ECCV 2016: 14th European conference, amsterdam, the netherlands, October 11–14, 2016, proceedings, part VII 14. Springer International Publishing, 2016.

- Pernici, Federico, et al. "Maximally compact and separated features with regular polytope networks." The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops. IEEE, 2019.

### Questions
Please refer to the weaknesses section.

### Soundness
3

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
2

### Summary
This paper introduces Semantic-Aware Representation Learning (SARL), a method aimed at mitigating catastrophic forgetting in lifelong learning. Inspired by human cognitive processes, SARL uses sparse activation and object prototypes to capture semantic relationships, employing semantic-aware metric learning to cluster similar objects while separating dissimilar ones. Experimental results show that SARL excels in Class-Incremental and Generalized Class-Incremental Learning, effectively retaining and transferring knowledge within a single-model setup. SARL’s integration of semantic structure and sparse representations offers a balanced approach to model stability and adaptability in lifelong learning.

### Strengths
The SARL method introduces an innovative approach by drawing inspiration from biological processes to incorporate semantic relationships into representation learning.

By employing semantic-aware metric learning, SARL effectively clusters similar objects while separating dissimilar ones, achieving a valuable balance between knowledge retention and adaptation to new information.

Validated across complex incremental learning tasks, such as Class-Incremental and Generalized Class-Incremental Learning, SARL demonstrates robust performance, minimizing task interference and enabling seamless knowledge transfer, highlighting its practical effectiveness.

The paper is well-written, with a clear structure that is easy to follow.

### Weaknesses
The objective function (7) of the proposed SARL method includes five loss terms, but the paper lacks a sensitivity analysis on the weights hyperparameter assigned to each term. Such an analysis would provide valuable insights into the impact of each loss term on the model’s performance. The current one in Appendix is not sufficient.

The introduction of object prototypes and semantic-aware metric learning may increase the model’s computational overhead and resource requirements compared to baseline method such as ER. The paper does not provide a detailed discussion on the model’s efficiency.

The experiments rely solely on the ResNet-18 backbone, lacking comparisons with other backbone models such as ViT, which could provide a broader evaluation of the method’s effectiveness.

### Questions
In the ablation study presented in Table 3, why is the performance in the first row so low? Is this row representing a traditional ResNet-18 classifier?

Do you have any insights into why the improvements for the Seq-CIFAR10 dataset are marginal compared to the more significant gains observed with Seq-CIFAR100 and Seq-TinyImageNet?

### Soundness
3

### Presentation
3

### Contribution
2
