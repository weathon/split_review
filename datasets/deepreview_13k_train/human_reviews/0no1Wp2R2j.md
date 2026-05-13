# Going Beyond Feature Similarity: Effective Dataset distillation based on Class-aware Conditional Mutual Information

- Decision: Accept
- Scores: 6, 6, 6, 3

## Abstract
Dataset distillation (DD) aims to minimize the time and memory consumption needed for training deep neural networks on large datasets, by creating a smaller synthetic dataset that has similar performance to that of the full real dataset. However, current dataset distillation methods often result in synthetic datasets that are excessively difficult for networks to learn from, due to the compression of a substantial amount of information from the original data through metrics measuring feature similarity, e,g., distribution matching (DM). In this work, we introduce conditional mutual information (CMI) to assess the class-aware complexity of a dataset and propose a novel method by minimizing CMI. Specifically, we minimize the distillation loss while constraining the class-aware complexity of the synthetic dataset by minimizing its empirical CMI from the feature space of pre-trained networks, simultaneously. Conducting on a thorough set of experiments, we show that our method can serve as a general regularization method to existing DD methods and improve the performance and training efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new approach for dataset distillation by introducing a class-aware conditional mutual information (CMI) metric to address challenges in creating compact, representative synthetic datasets. Traditional dataset distillation methods often compress feature similarity without considering class-specific complexity, making it hard for models to generalize across different classes. This work leverages CMI as a regularization constraint, optimizes synthetic datasets and improves training efficiency as well as model performance.

### Strengths
1.	The idea of using CMI in dataset distillation to address the inherent class-aware complexity issue is interesting.
2.	The experiments are conducted based on multiple datasets and various model architectures, providing solid evidence for the method's effectiveness. 
3.	The proposed method CMI is a versatile, "plug-and-play" regularization component that can be applied to numerous dataset distillation methods, such as DSA, MTT, and IDC. This flexibility allows the approach to generalize across different scenarios and highlights its robustness.
4.	By controlling the complexity of the synthetic dataset, the CMI-enhanced loss achieves faster convergence and reduces the number of required training iterations, which is particularly beneficial for large-scale datasets and resource-intensive models.

### Weaknesses
1.	While the paper demonstrates the CMI constraint’s benefits clearly, this method also introduces additional computation overhead, especially when dealing with high-resolution datasets. Although the authors briefly mention several strategies for mitigating this cost (e.g., reducing CMI calculations frequency), a more thorough discussion on balancing cost and performance might strengthen the practical feasibility. Specifically, the paper lacks a detailed analysis of how the frequency of CMI calculation impacts both the final performance and the training time, and what are the trade-offs in terms of accuracy and computational cost when CMI is computed less frequently. 
2.	Although empirical evidence is strong, the theoretical basis for CMI as a regularization term could be expanded. Specifically, further details on how CMI inherently captures class complexity or why it is preferable over alternative complexity measures would provide deeper insight. The paper should delve into the mathematical properties of CMI that make it suitable for this task, and compare it with other information-theoretic measures, such as mutual information or KL divergence, in the context of dataset distillation. A more rigorous justification is needed to explain why CMI is the most appropriate metric for capturing class-specific complexity.
3.	While the experiments on Tiny-ImageNet and ImageNet-1K are promising, it remains unclear how the proposed method scales with even larger datasets or more complex models, such as those used in real-world applications with hundreds of classes. Additional experiments in such contexts would further show the robustness of this method. The paper should also investigate the performance of the method with different model architectures, especially those with a larger number of parameters, to ensure the generalizability of the approach.

### Questions
1.	The paper is well-organized and clearly presents the methodology, results, and analyses. Figures and tables are effectively used to convey improvements and insights. However, further explanation of certain key terms, such as "empirical CMI," might enhance accessibility for readers unfamiliar with the topic.
2.	The ablation studies conducted to assess the influence of the weighting parameter on the CMI constraint are informative. Still, a broader exploration of other hyperparameters affecting CMI estimation, such as the dimensionality of feature space and network depth, could reveal potential optimizations.
3.	The potential of CMI for real-world applications, such as federated learning or privacy-preserving tasks, is not discussed. Given the emphasis on dataset distillation's applications in these areas, an exploration of how CMI might support these domains would align well with the broader goals of dataset distillation research.

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
This paper proposes a Conditional Mutual Information (CMI) method as a plug-and-play loss function to enhance the performance of dataset distillation methods. Experiments conducted on multiple baseline methods demonstrate the effectiveness of the CMI loss.

### Strengths
1.	The proposed CMI method is a relatively simple yet effective approach that is plug-and-play in nature. It has demonstrated its effectiveness across multiple baseline methods.
2.	The motivation behind the method proposed in the paper is solid and is supported by a certain theoretical foundation.
3.	The experiments in the paper are comprehensive, conducted across various scales of datasets.

### Weaknesses
1.	There are now newer and more powerful methods available, such as "Towards Lossless Dataset Distillation via Difficulty-Aligned Trajectory Matching" (ICLR 2024). The authors could consider experimenting with their proposed method on these methods.
2.	The description of the method in the paper could be clearer, particularly regarding the explanation of the formula symbols, to better emphasize the key points of the approach. Currently, it appears somewhat ambiguous.
3.	In my view, using mutual information or KL divergence is not a particularly novel approach, as it has been employed in many works across various fields.

### Questions
Please kindly refer to the above weaknesses.

### Soundness
3

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
This paper introduces a novel regularization method for dataset distillation (DD) by minimizing both the distillation loss and Conditional Mutual Information (CMI) of synthetic datasets. It uses an efficient CMI estimation method to measure class-aware properties and combines CMI with existing DD techniques. Experiments show that the proposed CMI-enhanced loss significantly outperforms state-of-the-art methods, improving performance by up to 5.5%. The method can be used as a plug-and-play module for all existing DD methods with diverse optimization objectives.

### Strengths
The strengths of this paper lie in its comprehensive experimentation across diverse datasets and network architectures, which effectively demonstrates the versatility and robustness of the proposed method. Furthermore, the method's ability to be integrated as a plug-and-play module into existing dataset distillation techniques, regardless of their optimization objectives, showcases its innovation and flexibility, making it a significant contribution to the field.

### Weaknesses
The paper lacks a clear discussion of the limitations of the proposed method. Furthermore, the authors should consider using more intuitive explanations, visual aids, and pseudocode to help readers better understand the technical details of the method.

### Questions
Can you discuss any potential limitations of your proposed method and suggest directions for future work to address these limitations?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a plug-and-play method, termed CMI, designed to enhance existing DD techniques by minimizing conditional mutual information. By applying CMI, the distilled data is concentrated more effectively around the center of each class, thereby improving generalizability.

### Strengths
- The logic is clear.
- The experiments are comprehensive.
- The review of related works is thorough.
- The proposed method is theoretically sound.

### Weaknesses
 - The core ideas, methodology, and formulations in this paper draw substantially from the approach proposed in [1].
- If  \hat{Z}  contains excessive confusing or uninformative information related to  S , then  H(S | \hat{Z}, Y)  will not be reduced; rather, it could remain the same or even increase. This is because conditional entropy reflects the remaining uncertainty in  S  after observing both  \hat{Z}  and  Y . When  \hat{Z}  is noisy or irrelevant for predicting  S , it does not help in reducing this uncertainty. The paper does not adequately address how to ensure \hat{Z} is informative and not detrimental to the conditional entropy.
- Line 213 states that “minimizing the class-aware CMI reduces the uncertainty brought to  \hat{Z}  conditioned on  S ,” which should be  “minimizing the class-aware CMI reduces the uncertainty brought to S conditioned on  \hat{Z}”.
- The authors’ derivation of Equation 6 lacks an explicit explanation, making it challenging to fully understand the transition from previous formulations. Specifically, the connection between the expectation over the distribution of S and the final expression involving P(Z|s) is unclear. A more detailed step-by-step derivation is needed to ensure the mathematical rigor.
- Works like [2] and [3], which also target improvements in dataset distillation, are not adequately considered. The paper should discuss how the proposed method compares to these approaches, particularly in terms of performance and computational complexity.
- Equation 3 requires summing over all synthetic instances within class  y , how the authors adapt this approach to instance-based distillation methods like SRe2L. The paper does not provide sufficient detail on how the class-wise summation is implemented in the context of instance-based methods, where each instance is optimized individually. This lack of clarity makes it difficult to assess the practical applicability of the method.

### Questions
see weakness.

### Soundness
2

### Presentation
3

### Contribution
2
