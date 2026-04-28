# Enhancing Logits Distillation with Plug&Play Kendall's $\tau$ Ranking Loss

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 5, 6

## Abstract
Knowledge distillation typically employs the Kullback-Leibler (KL) divergence to constrain the output of the student model to precisely match the soft labels provided by the teacher model. However, the optimization process of KL divergence is challenging for the student and prone to suboptimal points. Also, we demonstrate that the gradients provided by KL divergence depend on channel scale and thus tend to overlook low-probability channels. The mismatch in low-probability channels also results in the neglect of inter-class relationship information, making it difficult for the student to further enhance performance. To address this issue, we propose an auxiliary ranking loss based on Kendall’s $\tau$ Coefficient, which can be plug-and-play in any logit-based distillation method, providing inter-class relationship information and balancing the attention to low-probability channels. We show that the proposed ranking loss is less affected by channel scale, and its optimization objective is consistent with that of KL divergence. Extensive experiments on CIFAR-100, ImageNet, and COCO datasets, as well as various CNN and ViT teacher-student architecture combinations, demonstrate that the proposed ranking loss can be plug-and-play on various baselines and enhance their performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes an enhancement to the knowledge distillation process by introducing a plug-and-play ranking loss based on Kendall’s τ Coefficient, which aims to mitigate the limitations of Kullback-Leibler (KL) divergence. The proposed ranking loss addresses issues like the neglect of low-probability channels and the inability of KL divergence to fully capture inter-class relationships. Extensive experiments on CIFAR-100, ImageNet, and COCO datasets demonstrate the effectiveness of the approach, showing consistent improvements when applied to various teacher-student architecture combinations in CNN and Vision Transformer (ViT) models.

### Strengths
1. Novelty and contribution: The use of Kendall’s τ ranking loss in the context of knowledge distillation appears to be novel and provides a promising way to complement traditional KL divergence-based losses. The ranking-based approach helps the student model better capture inter-class relationships.
2. Plug-and-Play nature: The ranking loss is designed to be plug-and-play, which increases its practicality. It can be easily integrated into existing logit-based distillation frameworks without modifying the underlying architecture.
3. Intensive experiments: The paper provides a wide range of experiments on different datasets and architecture combinations, demonstrating the robustness and generalizability of the proposed ranking loss.
4. Addressing suboptimal points: The paper provides convincing arguments about how ranking loss helps in avoiding suboptimal solutions often seen in KL divergence optimization. The experimental results back up these claims, particularly in the analysis of accuracy and loss curves.

### Weaknesses
1. limited ablation study on hyperparameters. The author only discuss the effect of hyper-parameter k in the ranking loss. there is limited analysis of how sensitive the model is to different values of α, β, and γ in the overall loss function. 
2. Relation with other different distillation loss is not clear. The paper gives some explanations on why ranking loss works through its gradient form. However, I think since this loss is not used for its own. The author should discuss its relation with KD loss. KD constrains the logits after the softmax, however, ranking loss gives the constraint before the softmax, is it really necessary? I am not convinced by this.
3. Some of the derivations involving the ranking loss (e.g., differentiable form of Kendall’s τ coefficient) are challenging to follow due to their dense notation and lack of intermediate steps. Please consider adding more explanation or flowchart to increase the readablity.

### Questions
1. For the experiments involving different values of k and the comparison of different ranking loss forms, have you considered the effect of different initializations of the student model? The stability and sensitivity of the results with respect to different initial conditions could provide additional insights.
2. RKD is another important loss for distillation. Have you ever tried to combine with RKD (relation knowledge distillation).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper highlights the issues with using KL divergence in knowledge distillation and introduces a ranking loss based on Kendall's τ, which can be integrated into existing methods, enhances low-probability channel focus, and maintains inter-class relationships. Experimental results across various datasets and model architectures demonstrate that this approach consistently enhances performance.

### Strengths
1. The proposed method is designed for straightforward integration into existing logit-based distillation frameworks, increasing its relevance and utility.
2. Multiple experiments conducted on a variety of datasets and architectures provide evidence of the proposed approach's effectiveness

### Weaknesses
1. The KL divergence optimization is a relatively common scheme for the logit distillation task. Could the authors elaborate on the main novelty of this integration?
2. More ablation experiments and analysis are required for discussion; please see the Questions.

### Questions
1. What strategies could be implemented to minimize the computational overhead associated with the proposed ranking loss?
2. This article mentioned that the proposed method balances the model’s attention to larger and smaller-valued channels. Could the ranking loss also offer advantages in scenarios with class imbalance?
3. Are there any adverse effects when combining the proposed method with others? Could you provide relevant ablation experiments?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This study presents an auxiliary ranking loss based on Kendall’s Tao Coefficient to improve knowledge distillation. The proposed ranking loss addresses the issue of KL divergence’s neglect of low-probability channels by incorporating inter-class relationship information and enhancing focus on low-probability channels. It can be integrated into any logit-based distillation method and demonstrates consistent optimization objectives with KL divergence. Experiments on three datasets across various CNN and ViT teacher-student combinations show that the ranking loss effectively improves performance across multiple baselines.

### Strengths
1. This paper proposes a plug-and-play ranking loss to address the suboptimization issues in knowledge distillation optimization.
2. This paper demonstrates that Kullback-Leibler divergence is influenced by channel scale.

### Weaknesses
1. The paper claims that the proposed ranking loss primarily addresses KL divergence's tendency to overlook low-probability channels. However, based on the proposed formula, the main objective appears to be enforcing ranking consistency between the teacher and student models, with no clear indication of increased emphasis on information from smaller channels. The ranking loss, as formulated, seems to equally penalize deviations in ranking, regardless of the magnitude of the logits. A more detailed analysis of how the loss function specifically targets low-probability channels is needed. It is recommended that the author explain this aspect, perhaps by showing the gradients with respect to the student logits, and how they differ for high and low probability channels.
2. In the experimental section, it is recommended to include visualization experiments to highlight the primary contribution—improved attention to low-probability channels. For example, visualizing the attention maps or feature maps of the student network before and after applying the ranking loss, specifically focusing on the channels with initially low probabilities, would be beneficial. This would provide direct evidence of the method's effectiveness in shifting focus to these channels. Without such visualizations, the claim remains somewhat unsubstantiated.
3. Since LSKD shows superior performance in Tables 1 and 2, further explanation of this result is advised. The paper should delve deeper into why LSKD outperforms the proposed method in certain scenarios, especially since the proposed method is intended to address a specific limitation of KL divergence, which LSKD does not explicitly target. A more thorough discussion of the interplay between the proposed ranking loss and the temperature scaling mechanism in LSKD is necessary.

### Questions
Please refer to the Strengths and Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problem of knowledge distillation by highlighting the limitations of traditional KL divergence. The proposed method introduces an auxiliary loss based on Kendall’s τ Coefficient, which enhances the learning of inter-class relationships and low-probability channels. Experiments conducted on three image classification datasets demonstrate the effectiveness of this approach.

### Strengths
- The proposed method is straightforward and can be seamlessly integrated with logits-based knowledge distillation techniques.
- Experiments are conducted using both CNNs and ViTs across three different datasets. The ablation studies offer valuable insights into the proposed method.

### Weaknesses
 - Some claims lack adequate justification. For instance, it remains unclear how the proposed method resolves the suboptimal problem depicted in Figure 1. Including visual comparisons of logits with and without the ranking loss could enhance clarity and understanding.

- The proposed method includes multiple hyperparameters; however, the observed performance improvements are limited. Furthermore, the proposed method is evaluated against several straightforward baseline methods for knowledge distillation.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2
