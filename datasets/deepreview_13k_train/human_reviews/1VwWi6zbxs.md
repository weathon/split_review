# Mastering Task Arithmetic: $\tau$Jp as a Key Indicator for Weight Disentanglement

- Decision: Accept
- Scores: 8, 5, 6, 5

## Abstract
Model-editing techniques using task arithmetic have rapidly gained attention. Through task arithmetic, simply through arithmetic operations on the weights of pre-trained and fine-tuned models create desired models, such as multi-task models, models with specific tasks unsolvable, or domain-transferred models. However, task arithmetic faces challenges, such as low reproducibility and the high cost associated with adjusting coefficients in the arithmetic operations on model parameters, which have limited its practical success. In this paper, we present three key contributions in the context of task addition and task negation within task arithmetic. First, we propose a new metric called $\tau$Jp which is based on the product of the task vector ($\tau$) and the Jacobian of the pre-trained model with respect to its weights. We show that $\tau$Jp has a causal relationship with the interference that occurs from arithmetic operations. Second, we show that introducing regularization to minimize $\tau$Jp significantly mitigates interference between task inferences, which leads to eliminating coefficient tuning and better accuracy on each task. Third, in the context of incremental learning, we confirmed that our $\tau$Jp regularization demonstrates more robust performance in environments where future tasks to be learned are not accessible, validating the scalability of the approach. Finally, we demonstrate that the $\tau$Jp regularizer further reinforces the performance of task arithmetic by leveraging publicly available fine-tuned models, offering practical benefits for real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper tackles the task of task arithmetics, i.e. how to combine *task vectors/parameters* to form a multi-task model. A key issue is to determine the best combination weights as to minimise interference between tasks, and maximise sharing of information / positive transfer.
More specifically, the authors make use of two previously introduced notions: **(i)** the notion of **weight disentanglement** which was  proposed as a measure of task interference in task arithmetic. And **(ii)** the Neural Tangent Kernel (NTK) which designates a training regime where parameter updates can be expressed with a linearised approximation.
Previous works have suggested that performing task arithmetics under the NTK regime can lead to better MTL performance. the authors investigate this behaviour in more depth. Based on this analysis, they also propose a regularisation technique to further reduce task interference when performing task arithmetic, which involves slightly fine-tuning the task vectors themselves.

### Strengths
* The paper is well motivated and grounded in previous related work
* The proposed method is simple and could adapt to different task arithmetic variants
* Interesting insights on the link between the proposed regularisation and weight disentanglement
* A more efficient implementation of the method is proposed for handling larger number of tasks (Equation 11)

### Weaknesses
 * Missing baselines on more recent task arithmetic work: The main tables should include some recent task arithmetic results (e.g. TIES-Merging and AdaMerging) as well as standard single task and MTL baselines (although it is in the appendix), if only to better understand the existing gap in performance.
* Missing discussion about the extra cost: The paper briefly mentions efficiency of the method (e.g. equation 11 or line 364), however I think this could be discussed in more depth: On the one hand, the proposed method seems more robust to task coefficients $\alpha$, which could save on hyper parameter tuning; On the other hand, it involves a fine-tuning procedure which requires knowledge/access to all tasks simultaneously (Equation 10) as opposed to directly combining task vectors obtained independently from one another.
* I find the notion of "One-shot" and "fine-tuned" experimental setting could be improved; First because the notion of fine-tuning can become confusing between the coefficients $\alpha$ vs the model parameters $\theta$ fine-tuning. Second, because it is not clear if it is referring to a specific method/objective for fine-tuning the task coefficients (e.g. AdaMerging or others) or simply hyperparameter search.

### Questions
* I find the notion of "One-shot" and "fine-tuned" experimental setting could be improved; First because the notion of fine-tuning can become confusing between the coefficients $\alpha$ vs the model parameters $\theta$ fine-tuning. Second, because it is not clear if it is referring to a specific method/objective for fine-tuning the task coefficients (e.g. AdaMerging or others) or simply hyperparameter search.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a new metric called $\tau$Jp ($\tau$-Jacobian product) for measuring weight disentanglement in task arithmetic operations on neural networks. The authors theoretically analyze the relationship between $\tau$Jp and interference between tasks, and introduce a regularization method based on minimizing $\tau$Jp during fine-tuning. Experiments on image classification tasks demonstrate improved performance and reduced need for hyperparameter tuning compared to existing methods.

### Strengths
1. The paper provides a comprehensive theoretical and empirical study of the relationship between the proposed $\tau$Jp metric and task interference in neural networks.

2. The introduction of $\tau$Jp as a new metric for weight disentanglement is novel and well-motivated.

3. The proposed regularization method eliminates the need for tuning inference-time hyperparameters ($\alpha$), which is a practical advantage.

### Weaknesses
1. The method requires access to data from all other tasks during training, which is often unavailable in realistic task arithmetic scenarios. This limits the practical applicability of the approach.

2. The computational cost of calculating τJp is likely very high, as it involves multiple Jacobian-vector products. The paper does not report runtime or resource requirements, making it difficult to assess scalability.

3. Experiments are limited to image classification tasks. Evaluation on other domains like language tasks would strengthen the claims of generality.

4. The derivation of Equation 7 from the weight disentanglement definition is non-trivial and should be explained more clearly.

### Questions
- How does the computational cost of the proposed method compare to existing approaches?
- Can the method be adapted to work with limited or no access to data from other tasks?
- How well does the approach generalize to other domains beyond image classification?

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
2

### Summary
The paper introduces a novel metric, $\tau \text{Jp}$ ($\tau$-Jacobian product), to improve understanding of weight disentanglement in task arithmetic. It demonstrates that τJp inversely correlates with normalized accuracy, suggesting it as an indicator for weight disentanglement. A regularization technique is proposed to minimize τJp during fine-tuning, effectively reducing the need for coefficient adjustments in task addition and negation. It also proves valuable in incremental learning scenarios where future tasks are unknown.

### Strengths
1.The paper addresses an important and timely topic: in an era where foundation models are prevalent, better understanding weight disentanglement is particularly valuable for enhancing the practical applicability of these models.

2.The proposed metric offers a deeper understanding of weight disentanglement, and the regularization method effectively reduces task interference, minimizing the need for coefficient adjustments.

3.The success of the proposed method in incremental learning scenarios aligns well with real-world applications, demonstrating its scalability and practical relevance when future tasks are unknown.

### Weaknesses
1.While the paper introduces the $\tau \text{Jp}$ metric and explains its relationship with weight disentanglement, the theoretical justification for why $\tau \text{Jp}$ regularization effectively reduces task interference could be further elaborated. Specifically, the paper lacks a detailed explanation of the underlying mechanisms through which minimizing the $\tau \text{Jp}$ metric leads to improved orthogonality between task vectors and output gradients. A more rigorous analysis, perhaps drawing connections to established theories of interference in neural networks, would strengthen the argument.

2.The proposed regularization method lacks a comparison with other existing regularization techniques, which makes it difficult to fully assess its relative strengths and weaknesses. Without empirical comparisons against methods like L2 regularization, elastic net, or other task-specific regularization approaches, it is unclear whether the proposed method offers a significant advantage or if its benefits are simply due to a general regularization effect. The absence of such comparisons limits the ability to contextualize the contribution of the proposed method.

3.The paper mentions task addition, task negation, and task analogies in the introduction and background sections as key operations in task arithmetic, but there are no experiments evaluating task analogies. This inconsistency weakens the completeness of the experimental validation. The lack of experimental results for task analogies leaves a gap in the evaluation, making it difficult to assess the general applicability of the proposed method across all claimed task arithmetic operations.

### Questions
Suggestions：

1.The related work section could be improved by explicitly connecting prior studies to this paper's contributions, emphasizing how the proposed method addresses existing limitations.               
2.Consider moving the related work section after the methods section, especially since the current structure delays the introduction of the proposed method until page 5. This change would allow readers to quickly understand the proposed approach before diving into comparisons, enhancing readability and engagement.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents a novel approach to task arithmetic in neural networks, which leverages a novel metric that quantifies the relationship between task vectors and the Jacobian of pre-trained models. The authors claim that by minimizing this metric through regularization, they can significantly reduce interference between task predictions and enhance the accuracy of task arithmetic operations. The experimental results demonstrate substantial improvements in performance for both task addition and task negation.

### Strengths
+ This paper is well-written and easy to follow.
+ The experiments are extensive, and the results sound good.
+ The design of metric τJp is reasonable and interesting.

### Weaknesses
 - The novelty of this paper may be limited. My consideration is that this paper seems to fundamentally align with the approach proposed by Ortiz-Jimenez et al. (2023) [1], which also emphasizes fine-tuning models in the tangent space. Although using the specific regularization term, this paper does not sufficiently differentiate itself from this existing work.
- While the empirical results are compelling, the paper lacks a thorough theoretical explanation for why the proposed regularization leads to better performance compared to other methods, such as those discussed in Ortiz-Jimenez et al. (2023). I am confused about why a simple and soft regularization results in such improvement compared to [1]. A deeper theoretical analysis could strengthen the paper's contributions.
- The authors briefly mention tuning the regularization strength but do not provide sufficient details on how this hyperparameter was selected. The sensitive analysis of this hyperparameter is also necessary for the paper.

### Questions
Could the proposed regularization affect the model's plasticity? Specifically, how might the addition of this regularization impact the fine-tuning performance, potentially influenced by the strength of the regularization?

### Soundness
2

### Presentation
3

### Contribution
2
