# SATCH: Specialized Assistant Teacher Distillation to Reduce Catastrophic Forgetting

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3, 5

## Abstract
Continual learning enables models to learn new tasks sequentially without forgetting previously learned knowledge. Knowledge distillation reduces forgetting by using a single teacher model to transfer previous knowledge to the student model. However, existing methods face challenges, specifically loss of task-specific knowledge, limited diversity in the transferred knowledge, and delays in teacher availability. These issues stem from self-distillation, where the teacher is a mere snapshot of the student after learning a new task, inheriting the student’s biases and becoming available only after learning a task. We propose Specialized Assistant TeaCHer distillation (SATCH), a novel method that uses a smaller assistant teacher trained exclusively on the current task. By incorporating the assistant teacher early in the learning process, SATCH provides task-specific guidance, improves the diversity of transferred knowledge, and preserves critical task-specific insights. Our method integrates seamlessly with existing knowledge distillation techniques, and experiments on three standard continual learning benchmarks show that SATCH improves accuracy by up to 12% when combined with four state-of-the-art methods. Code is available in supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new class incremental continual learning framework. It uses an assistant teacher network to diversify knowledge but also be task-specific. The logits from the assistant teacher is stored in the memory buffer which is used to diversify the knowledge during the knowledge distillation process. It also uses a buffer selection strategy to keep representative samples in the memory buffer. The experiments show that these steps improve the accuracy and reduce catastrophic forgetting.

### Strengths
- The proposed idea sounds and improves multiple baseline models.
- The paper is clearly written, especially Figure 2 is very informative. 
- Grad-CAM visualization and the ablation study show the benefit of the proposed method.

### Weaknesses
1. Since the proposed method has an additional model (assistant teacher), this adds additional parameters to the framework. Ideally, the total model size should match all models for a fair comparison. What is the total model size for all models? I suggest the authors report the current parameter counts and provide the comparison with equal total model size for all methods if possible—enlarge the models to match total parameter counts.

2. The paper claims that combining the logits of the replay buffer and the teacher diversifies the knowledge. It is unclear how this step helps diversify knowledge. Could authors explain this? Also, I ask the authors to provide quantitative metrics or visualizations that demonstrate increased diversity in the combined knowledge compared to using only the main teacher or replay buffer logits.

3. To understand how good the proposed method is, I suggest authors provide the upper and lower bounds --- training all tasks jointly (upper bound) or sequentially (lower bound) without any techniques. 

4. Figures 3 and 5 results are with a buffer size of 1000, and Tables 2-4 are with a buffer size of 5000. Could the authors either provide results for both buffer sizes consistently across all experiments or explain their rationale for using different buffer sizes in different analyses?

5. The choice of backbone: The backbones the authors tested are ResNet-18 and 3-layer convnet. Are there any potential challenges or modifications needed to apply SATCH to transformer-based architectures? Could the authors provide preliminary results with a transformer-based architecture like ViT if feasible? 

6. Also, it would be better to compare with more recent SOTA and other class incremental learning methods such as [1-3].

### Questions
See the weaknesses.

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
The paper presents SATCH (Specialized Assistant Teacher Distillation), a novel approach designed to address catastrophic forgetting in continual learning through a specialized assistant-teacher mechanism. This assistant teacher is trained on individual tasks before the student learns them, providing diverse, task-specific guidance that enhances memory retention and reduces the forgetting of previously learned tasks. Key contributions include (1) guiding new task learning with task-specific soft labels, (2) refining buffer selection to prioritize representative samples, and (3) diversifying knowledge distillation by combining the assistant teacher's specialized knowledge with the main teacher’s generalized knowledge. Experiments on benchmarks like CIFAR-100, TinyImageNet, and MiniImageNet demonstrate significant improvements in continual learning accuracy, particularly in settings with noisy data.

### Strengths
1. By introducing a specialized assistant teacher that learns each task individually, SATCH diversifies and enhances knowledge distillation, addressing a significant limitation in existing continual learning frameworks.
   
2. The buffer selection refinement effectively filters noisy samples, enhancing stability and making the method robust to real-world scenarios with label noise.

3. The paper provides thorough experimental validation across multiple datasets, benchmarking SATCH against established methods. It demonstrates consistent accuracy improvements and provides evidence for reduced catastrophic forgetting.

4. SATCH is designed to integrate seamlessly with various continual learning methods, enhancing its practicality and potential adoption.

### Weaknesses
1. While SATCH improves accuracy, it introduces additional computation through the assistant teacher and buffer operations. The paper would benefit from a clearer comparison of the memory and runtime efficiency with alternative methods, especially on larger-scale tasks or models. Specifically, the overhead of training a separate assistant teacher for each task, including the forward and backward passes, needs to be quantified and compared against methods that do not rely on such a mechanism. The memory footprint of storing assistant teacher logits in the buffer should also be explicitly detailed, particularly in scenarios with a large number of classes or tasks.

2. The assistant teacher’s architecture is described as a scaled-down ResNet-18, which may not generalize well across diverse models or tasks. An analysis of SATCH’s scalability with more complex backbones, such as larger ResNet variants or transformer-based architectures, or with larger task sequences would add value. It is unclear how the performance of SATCH would be affected if the student model is significantly different from the assistant teacher in terms of architecture or capacity. The paper should investigate the sensitivity of SATCH to the architectural differences between the student and assistant teacher models.

3. Although the assistant teacher provides task-specific knowledge, the long-term retention of this information across tasks remains under-explored. It would be helpful to see additional studies or visualizations that clarify the assistant teacher’s impact on task-specific feature preservation over extended sequences. For example, analyzing the feature space of the student model after learning multiple tasks, with and without the assistant teacher, would provide insights into how well task-specific features are retained. It is also important to understand if the assistant teacher's knowledge degrades over time, and if so, how this affects the overall performance of the continual learning system.

4. The ablation study does not fully explain the contributions of each component in isolation, especially under noisy conditions. More detailed component-wise evaluations would make it easier to understand the relative impact of each part (e.g., buffer selection refinement, diverse knowledge). Specifically, the ablation study should include a more granular analysis of how the buffer selection refinement performs under varying levels of label noise, and how the diverse knowledge distillation strategy contributes to the overall performance gain compared to a standard knowledge distillation approach.

### Questions
1. How does the assistant teacher impact memory and runtime compared to single-teacher methods on larger datasets?

2. Please consider comparing SATCH with multi-teacher approaches that focus on task-specific retention.

3. It is suggested to evaluate if SATCH handles larger, real-world datasets beyond CIFAR100 and MiniImageNet.

4. It is recommended to perform experiments if SATCH manages cases with overlapping tasks or undefined task boundaries.

5. Is it possible to expand ablation studies to show SATCH’s component performance under varying noise levels and buffer sizes?

6. It is better to add more analysis on how SATCH preserves task-specific knowledge?

7. How sensitive is SATCH to settings like distillation weight and buffer size?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a more sophisticated knowledge distillation method using an assistant teacher to help transfer knowledge and mitigate catastrophic forgetting in class incremental learning.

### Strengths
S1. The proposed method seems to be new and can improve knowledge distillation for class incremental learning. 

S2. The writing is generally clear, though, in some places, the paper assumes the reader has prior knowledge of some existing distillation methods.

### Weaknesses
W1. The proposed approach is not too novel, as knowledge distillation-based methods are already widely explored, and like this method, do not achieve SOTA performance.

W2. The related work section primarily focuses on distillation-based methods. However, as the proposed approach competes with all existing methods, a more comprehensive review is necessary. The current section may give the impression that the authors are not fully up-to-date with the latest advancements in continual learning.

W3. Paper [a] suggests that catastrophic forgetting may not be the only challenge in class incremental learning. The issue of inter-task class separation is also, maybe more, critical. How can the proposed method deal with that?

W4. The baseline methods are weak and not diverse enough. Other SOTA approaches should also be compared. Please compare with [a, b, c, d]. It appears that the results in [a] are significantly better than those of your proposed method (“ours”), and [a] achieves this without saving any replaying data. The other three systems seem to be strong too.

W5. Nowadays, it’s more appropriate to use a pre-trained model, as it can yield significantly better results. When a pre-trained model is used, knowledge distillation may be less effective because the main feature knowledge is already in the pre-trained model.

### Questions
No questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method for continual learning that addresses key challenges of existing knowledge distillation based class-incremental strategies used in them. Traditional methods often struggle with the loss of task-specific knowledge, limited diversity in knowledge transfer, and delays in teacher model availability. SATCH proposes the use of a smaller assistant teacher trained on the current task to offer task-specific guidance early in the learning process. This approach diversifies and enhances the knowledge transferred to the student model while refining sample selection in noisy environments. Experimental results on standard continual learning benchmarks, such as CIFAR100, TinyImageNet, and MiniImageNet, show that SATCH improves accuracy by up to 12% compared to state-of-the-art methods. The paper highlights SATCH’s robust integration with existing frameworks and emphasizes its contributions to mitigating catastrophic forgetting through improved knowledge diversity and task-specific retention​.

### Strengths
1. Improved Knowledge Diversity: By combining the specialized knowledge of the assistant teacher with the generalized knowledge of the main teacher, SATCH effectively diversifies the knowledge transfer process. This approach enriches the learning experience for the student model and mitigates the limitations of using a single teacher model.

2. Integration with Existing Methods: The method is designed to work seamlessly with established distillation based class-incremental learning methods

### Weaknesses
1. Limited Discussion on Computational Overheads: The assistant teacher’s additional computations may raise concerns for resource-constrained environments and by makes existing methods computationally inefficient. In additition, the assistant teacher training followed by the distillation performed, makes the knowledge transfer process cumbersome. Adding a detailed analysis of the computational complexity and runtime of SATCH compared to baseline methods. Quantifying the impact on memory and processing time across various settings would clarify the scalability of the approach. Additionally, consider exploring potential optimizations to make the process more efficient, such as parallel training strategies, etc.

2. Lack of Broader Comparisons: The contributions in the paper are limited to a particular kind class-incremental paradigm, therefore its applicability in a broader context remains limited. The paper could also have strengthened its argument by comparing SATCH against a wider variety of lifelong learning or parameter isolation methods. This omission weakens the case for its effectiveness. To strengthen the argument for SATCH’s effectiveness, The authors could expand the comparative study to include more diverse continual learning approaches, such as parameter isolation techniques (e.g., Progressive Neural Networks or Elastic Weight Consolidation). This would help assess the general applicability and robustness of SATCH across various scenarios. Furthermore, a discussion on the adaptability of SATCH to task-agnostic or domain-incremental learning settings would broaden its impact.

3. Risk of Overfitting: The assistant teacher’s narrow focus on individual tasks may risk overfitting to specific task features. This might limit the generalization of the student model across a sequence of tasks, particularly if the approach is applied in less controlled or highly variable environments. To strengthen this argument, the authors can add in experiments to measure the generalization capabilities of the student model when SATCH is applied to more complex and variable task sequences. Additionally, consider discussing possible regularization techniques or adjustments to the assistant teacher’s training to mitigate this risk.


4. Gaps in Theoretical Analysis and Interpretability: The paper could benefit from a stronger analysis of interpretability. The assistant teacher introduces additional decision-making layers that could obscure the interpretability of the student model’s predictions. The reliance on visualizations alone may not provide sufficient insights into the assistant teacher’s effect on the knowledge transfer process. Incorporating quantitative metrics for interpretability, such as measuring feature attribution consistency, would add depth to the understanding of SATCH’s impact. A discussion on the trade-offs between interpretability and model complexity introduced by the assistant teacher would also be valuable.

5. Overall presentation clarity: The overall process-flow is hard to follow, it's unclear what process follows what. For example in Fig. 1 the buffer selection for task t is done prior to learning the about the task t in (c). The following figure makes it confusing. The authors can think about reorganizing the description of the methodology to improve clarity. For example, a step-by-step walkthrough of the process, along with a more intuitive depiction in the figures, would be helpful. Explicitly labeling the sequence of operations and ensuring that all components are described in a logical order would enhance comprehension.


Minor typo:
In Line 191-192, ''allows us to maintain'' is repeated.

### Questions
1. The proposed SATCH framework is evaluated primarily in class-incremental learning settings where task boundaries are well-defined. However, in many real-world continual learning scenarios, tasks can be overlapping or not strictly disjoint. Could you elaborate on how SATCH handles such situations where task-specific distinctions blur? Specifically, how does the assistant teacher adapt to or mitigate the challenges of overlapping feature distributions, and what impact does this have on the model’s ability to prevent catastrophic forgetting and maintain effective knowledge transfer?

2. The choice of architecture for the assistant teacher is a critical design decision in SATCH, given its role in capturing task-specific knowledge. Could you provide more details on how the architecture of the assistant teacher is selected? How sensitive is the overall performance of the model to this architectural choice, particularly in terms of balancing efficiency and effectiveness? For practitioners aiming to implement SATCH in different environments, what guidelines or heuristics would you recommend for choosing an appropriate assistant teacher architecture?

3. The title emphasizes the goal of mitigating catastrophic forgetting, but the analysis of forgetting prevention appears less explicit in the main text. Could you clarify or point out where the paper quantifies or analyzes the extent of forgetting reduction achieved by SATCH? For example, do you provide a forgetting metric or compare how much past knowledge retention improves relative to baseline methods? An explicit section or metric-based analysis on forgetting would strengthen the paper’s claims.

4. In Equations 1 and 2, the hyperparameter 𝜆 controls the influence of the assistant teacher’s knowledge transfer through Kullback-Leibler divergence. How do you determine the optimal value for 𝜆 in practice? Is there a systematic approach or empirical method that you suggest for tuning this parameter, especially given the diverse nature of continual learning datasets and tasks? Understanding this would aid practitioners in effectively implementing your method in different settings.

### Soundness
1

### Presentation
1

### Contribution
1
