# Unleashing the Potential of Temperature Scaling for Multi-Label Logit Distillation

- Decision: Reject
- Scores: 6, 6, 6

## Abstract
This paper undertakes meticulous scrutiny of the pure logit-based distillation under multi-label learning through the lens of activation function. We begin with empirically clarifying a recently discovered perspective that vanilla sigmoid per se is more suitable than tempered softmax in multi-label distillation, is not entirely correct. After that, we reveal that both the sigmoid and tempered softmax have an intrinsic limitation. In particular, we conclude that ignoring the decisive factor temperature $\tau$ in the sigmoid is the essential reason for its unsatisfactory results. With this regard, we propose unleashing the potential of temperature scaling in the multi-label distillation and present Tempered Logit Distillation (TLD), an embarrassingly simple yet astonishingly performant approach. Specifically, we modify the sigmoid with the temperature scaling mechanism, deriving a new activation function, dubbed as tempered sigmoid. With theoretical and visual analysis, intriguingly, we identify that tempered sigmoid with $\tau$ smaller than 1 provides an effect of hard mining by governing the magnitude of penalties according to the sample difficulty, which is shown as the key property to its success. Our work is accompanied by comprehensive experiments on COCO, PASCAL-VOC, and NUS-WIDE over several architectures across three multi-label learning scenarios: image classification, object detection, and instance segmentation. Distillation results evidence that TLD consistently harvests remarkable performance and surpasses the prior counterparts, demonstrating its superiority and versatility.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper discovers that the vanilla sigmoid does not offer significant practical benefits compared to the tempered softmax in multi-label logit distillation. Furthermore, it identifies that ignoring the temperature parameter is the fundamental bottleneck causing the vanilla sigmoid to yield poor results. Motivated by these findings, the authors introduce the tempered sigmoid and demonstrate its advantages both empirically and theoretically.

### Strengths
(1)The writing in this paper is clear and easy to understand.

(2)The quantitative and qualitative results are sufficient.

### Weaknesses
The experiments in this paper are primarily conducted on a smaller scale, making it difficult to convince that the method can be generalized to larger datasets, such as those with millions or tens of millions of data points.

### Questions
(1) Is the 𝜏 sensitive for different tasks and training sets?

(2) The method proposed in this paper is overly simple, which raises doubts about whether other literature and work has already proposed related or better approaches.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new Knowledge Distillation (KD) approach for multi-label learning, that aims at distilling the knowledge from the teacher model to a student model. The proposed approach, named Tempered Logit Distillation (TLD), is simple and uses a sigmoid with a temperature scaling to modulate the logit smoothness. The tempered sigmoid is applied on the model outputs, so it seems easy to use in practice. Then, the Kullback-Leibler (KL) divergence loss is applied on the sigmoid outputs to distill the knowledge from the teacher model to a student model. The proposed approach shows good performances on three standard datasets: COCO, PASCAL VOC, and NUS-WIDE. The paper contains results for several model architectures, and several tasks: image classification, object detection, and instance segmentation. The paper also contains an ablation analysis of the proposed approach.

### Strengths
- The paper introduces the Tempered Logit Distillation (TLD), a knowledge distillation loss for multi-label classification. First, a sigmoid with a temperature scaling is applied on logit outputs. Then, the Kullback-Leibler (KL) divergence loss is applied on the sigmoid outputs to distill the knowledge from the teacher model to a student model. The proposed Knowledge Distillation (KD) method is simple and seems easy to use in practice as it requires access to the model outputs only. It is not necessary to access intermediate feature maps. 
- The proposed approach is evaluated on three standard multi-label classification benchmarks: COCO, PASCAL VOC, and NUS-WIDE. The results with multiple model architectures show that the TLD outperforms existing approaches. 
- The paper shows that TLD works well on different tasks like object detection and instance segmentation. 
- The paper contains multiple analyses of the proposed approach. Table 1 shows an ablation study. Table 5 shows the relation between the student and teacher. Table 6 analyzes the activation function $\sigma$ regarding logit KD. Table 10 and Figure 4 analyze the impact of the temperature scaling.

### Weaknesses
 **Limited technical contributions.** The technical novelty of the paper seems quite limited. The paper introduces the Tempered Logit Distillation (TLD) that uses a sigmoid with a temperature parameter and a KL divergence loss. The tempered sigmoid is not novel and was used in published papers like [A]. The theoretical analysis section does not provide theoretical results. It just shows the gradient, and analyzes the impact of the temperature parameter on the learning. As the technical novelty of the paper is quite limited, the theoretical analysis should be improve to include results such as the theoretical convergence guarantees or convergence rate. It could be interesting to build novel analysis tools to better understand the impact of the temperature scaling. In other words, it could be valuable to answer the question: why does the model cannot learn the right scale for the output activations?

**Hard samples.** In the introduction, it is written: "we identify that tempered sigmoid with τ smaller than 1 provides an effect of hard mining by governing the magnitude of penalties according to the sample difficulty, which is shown as the key property to its success." The paper does not justify well this claim. It is not clear why focusing on hard examples is important. The paper should contain an experiment or theoretical result to support this claim. It could also be useful to give a definition of hard examples.

**Things to improve the paper that did not impact the score:**
- Table 1 and 2 show result, but these tables are before the experiment section so it is not possible to understand them well before to read the remaining of the paper. I would suggest to rethink the position of these tables so it is easier for the reader to understand them. For example, showing the an ablation study in the introduction may not be a good idea.
- Some table captions are not self content. For instance, Table 6 and 7 do not indicate the task which can be confusing as COCO is used for three different tasks.

### Questions
The questions are arranged in order of importance, with the first question being the most important.

- The paper or its appendix should explain the derivation of equation 8. The equation in the paper seems quite different from the standard KL gradient. It would be important to explain what is the meaning of $z_i$? $z_i$ is the output logit, but it does not have superscripts, so what is its connection with the teacher and student networks? 
- Why focusing on hard examples is important for TLD? 
- Why does the model cannot learn the right scale for the output activations and need the temperature scaling?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach to multi-label logit distillation by introducing a tempered sigmoid activation function with temperature scaling. The authors argue that both the traditional sigmoid and tempered softmax activation functions have intrinsic limitations in multi-label distillation. To address these issues, they propose Tempered Logit Distillation (TLD), a method that modifies the sigmoid activation function with temperature scaling, offering significant performance improvements across multi-label learning tasks such as image classification, object detection, and instance segmentation. Comprehensive experiments demonstrate the effectiveness of TLD on benchmarks like COCO, PASCAL-VOC, and NUS-WIDE, showing consistent gains in performance.

### Strengths
1. Tempered Sigmoid is novel and addresses key limitations in existing multi-label logit distillation methods.

2. The paper provides comprehensive experimental results, including a well-designed ablation study, which thoroughly evaluates the contribution of each component.

3. The proposed method achieves state-of-the-art (SOTA) performance on multiple benchmarks, demonstrating its effectiveness and broad applicability in multi-label learning tasks.

### Weaknesses
1. **Weak theoretical foundation**: The theoretical analysis in the paper primarily revolves around the choice of the hyperparameter $\tau$, but the reasoning behind different $\tau$ values lacks depth and conviction. While the paper presents justifications for the selection of $\tau$, it does not offer strong theoretical support that would convincingly validate these choices. Specifically, the analysis does not delve into how the tempered sigmoid's gradient behavior differs from the standard sigmoid, nor does it provide a rigorous mathematical explanation for why specific values of $\tau$ are optimal for different tasks. A more in-depth analysis of the loss landscape and the impact of $\tau$ on convergence would be beneficial.

2. **Weak motivation**: The motivation provided in the introduction feels somewhat forced. For example, the second point in the introduction's analysis seems weaker because the results in the table show that sigmoid performs quite well when combined with common tricks, which undermines the strength of the argument against sigmoid. The paper should more clearly articulate the limitations of existing methods, particularly in the context of multi-label learning, and demonstrate why the proposed approach is a necessary improvement.

3. **Method simplicity**: The proposed method can be viewed as a generalized version of sigmoid by simply adding a controllable temperature hyperparameter. As a reviewer, I generally appreciate methods that are simple but effective. However, this approach seems bound to outperform previous methods because it inherently expands the search space to include prior approaches, which raises questions about its novelty. The paper needs to more clearly demonstrate the novelty of the approach beyond simply adding a temperature parameter, perhaps by showing how this parameter interacts with the multi-label learning task in a unique way.

4. **Fairness of comparisons**: Given the point raised in 3, the method can be seen as akin to adding a regularization term. A more fair comparison would involve adding analogous regularization to competing methods, rather than purely comparing methods without such adjustments. More meaningful comparisons would include integrating this method with more tricks commonly used in the field, such as multi-scale training (as mentioned in the appendix). Demonstrating that this method can provide orthogonal improvements when combined with other techniques would make the contribution more significant. For instance, showing that the tempered sigmoid provides benefits when used with other distillation losses or data augmentation techniques would strengthen the paper.

### Questions
1. In classification tasks, the student model outperforms the teacher, as shown in Table 1. Is this improvement due to the benefits of knowledge distillation (such as self-distillation), or could it be attributed to the training paradigm, where the teacher's paradigm may not be as suitable for the task as the student's? What would be the effect of adapting the teacher to better fit the task?

2. In Table 10, the impact of $\tau$ on KL divergence is not fully explored. What happens to the method's performance when $\tau$ is closer to 4?

3. Different values of $\tau$ were used for classification and segmentation. Besides running all possible $\tau$ values, is there a more insightful way to analyze and determine the optimal $\tau$? In previous work with softmax, was τ treated as fixed or variable?

### Soundness
3

### Presentation
3

### Contribution
2
