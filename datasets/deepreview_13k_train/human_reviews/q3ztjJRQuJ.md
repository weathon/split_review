# Task Arithmetic in Trust Region: A Training-Free Model Merging Approach to Navigate Knowledge Conflicts

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Multi-task model merging offers an efficient solution for integrating knowledge from multiple fine-tuned models, mitigating the significant computational and storage demands associated with multi-task training. As a key technique in this field, Task Arithmetic (TA) defines task vectors by subtracting the pre-trained model ($\theta_{\text{pre}}$) from the fine-tuned task models in parameter space, then adjusting the weight between these task vectors and $\theta_{\text{pre}}$ to balance task-generalized and task-specific knowledge. Despite the promising performance of TA, conflicts can arise among the task vectors, particularly when different tasks require distinct model adaptations. In this paper, we formally define this issue as knowledge conflicts, characterized by the performance degradation of one task after merging with a model fine-tuned for another task. Through in-depth analysis, we show that these conflicts stem primarily from the components of task vectors that align with the gradient of task-specific losses at $\theta_{\text{pre}}$. To address this, we propose Task Arithmetic in Trust Region (TATR), which defines the trust region as dimensions in the model parameter space that cause only small changes (corresponding to the task vector components with gradient orthogonal direction) in the task-specific losses. Restricting parameter merging within this trust region, TATR can effectively alleviate knowledge conflicts. Moreover, TATR serves as both an independent approach and a plug-and-play module compatible with a wide range of TA-based methods. Extensive empirical evaluations on eight distinct datasets robustly demonstrate that TATR improves the multi-task performance of several TA-based model merging methods by an observable margin.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the concept of "knowledge conflicts," a static property between task-specific fine-tuned model parameters and base model parameters, identifying it as a key issue in Task Arithmetic. Through analysis, the authors propose a novel trust-region criterion for model merging, called Task Arithmetic in Trust Region (TATR), designed to effectively mitigate these knowledge conflicts. The proposed method can also be applied orthogonally to other Task Arithmetic-based approaches.

### Strengths
1. The paper is easy to follow, with "knowledge conflicts" serving as a clear and intuitive motivation. Researchers familiar with "gradient conflicts" between tasks will easily understand it, as the authors clearly differentiate these two concepts.

2. The proposed methods can enhance multi-task performance when used alongside existing Task Arithmetic (TA) methods, demonstrating the practical value of the approach.

### Weaknesses
1. The author argues that merging both gradient descent and ascent components would lead to negative performance across multiple tasks, as each component contributes differently—gradient descent causes knowledge conflicts, while gradient ascent leads to overshooting. This claim appears controversial, suggesting that other important criteria or metrics might also play a role in causing knowledge conflicts. If the performance degradation from merging the negative gradient descent is purely due to the large magnitude of the task-specific vectors, could reducing their magnitude make them usable?

2. The authors propose a practical approach by measuring the "Trust Region" through the inner product of task vectors and the gradient of loss, considering each task vector component's effect on merging performance. A question arises: according to Eq. (5), it appears that the inner product of each task pair is summed to calculate the trust region. However, intuitively, it seems that the trust region should vary for each task pair depending on the inherent relations between tasks. The proposed method, however, does not seem to account for this variability across task pairs, instead summing their magnitudes uniformly to determine the trust region.

3. The proposed method is reminiscent of PCGrad [1], which is used in multi-task optimization and projects task vectors to project task vectors into orthogonal space to better align them. Since achieving perfectly orthogonal vectors is impossible when handling multiple tasks, PCGrad randomly mixes gradients to assign priority. This raises a related question in the context of Question 2: When dealing with multiple tasks with distinct objectives, is it always possible to find orthogonal components for task vectors across various tasks? It’s unclear if this can always be guaranteed, and a theoretical analysis may be necessary to further validate the proposed methods and address these potential limitations.

### Questions
1. The authors provide informative figures (Figures 2, 5, and 6) to illustrate how updates of orthogonal components can reduce knowledge conflict. However, this effect appears dependent on the homogeneity of the task set, as most experiments are conducted on simple, domain-specific classification tasks, which are relatively homogeneous. This raises questions about the broader validity of Task Arithmetic in more diverse settings. Although most baselines, such as AdaMerging, also use these simpler setups, which explains the authors' choice to some extent, the proposed methods could be tested on benchmarks with heterogeneous task settings—such as Taskonomy, PASCAL-Context, or NYUD—that feature a wider variety of task relations and are commonly used in MTL research.

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
The paper presents a novel approach to task arithmetic aimed at addressing challenges in multi-task learning. It defines conflicts between tasks as "knowledge conflicts" and introduces a trust region to help mitigate these conflicts.

### Strengths
-The paper clearly presents the problem and the proposed method.
- It offers an extensive set of experiments across multiple datasets.
- The paper includes a comprehensive comparison with existing methods to demonstrate the performance of the proposed approach.

### Weaknesses
The experiments convincingly demonstrate the effectiveness of the proposed data augmentation method. However, the performance improvements are minimal in most cases.

### Questions
See the weakness.

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
This paper identifies the phenomenon of task conflict in multi-task model merging, primarily occurring in certain components of task vectors that are aligned with the direction of the task gradients. Based on this finding, this paper defines a trust region (i.e., the task vector components orthogonal to the gradient) and introduces the TATR method, which performs parameter merging only within this trust region to alleviate knowledge conflicts during model merging. As a plug-and-play approach, TATR can be combined with previous methods, and extensive evaluation on diverse datasets demonstrates its effectiveness.

### Strengths
1. The paper is well-written and easily understandable.

2. TATR demonstrates promising performance on ViT-B/32.

3. The method proposed in this paper is interesting and can be combined with existing methods, which enhance the practical value of this method.

### Weaknesses
1. The motivation does not seem to align with the proposed method. The method's motivation is to select components of task vectors orthogonal to other task gradients for model merging, but the approach instead selects components with smaller values (or norms) for merging.

2. The paper introduces a zero-shot version of TATR. Although Line 313 claims, "Although there may be estimation errors, this approach still offers performance improvements for TA-based methods ..." I observed in the experiments that this version of TATR in Table 1 for test-time training based methods does not yield performance gains. Therefore, I believe this sentence should be revised.

3. TATR uses an exemplar set to calculate the gradient, and I'm interested in whether the samples here are randomly sampled or selected in some way. If it is random sampling, can you analyze if the different samples have an effect on the selection of the trust region?

4. Despite promising results on the ViT-B/32 model, the performance of TATR is limited on the ViT-L/14.

5. Line 414, "Table 5 and Table 2" is wrong.

### Questions
1. Robustness analysis for different samples.

2. What is the difference between TATR and the direct removing components with large high magnitude of the task vector?

3. Can you analyze why there is a difference in performance on ViT-B/32 and ViT-L/4?

### Soundness
2

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
This paper introduces Task Arithmetic in Trust Region (TATR), a training-free approach for multi-task model merging. By defining a trust region, TATR restricts merging to parameters with minimal influence on task-specific losses, aiming to reduce knowledge conflicts. The method identifies that gradient-aligned task vector components are primary sources of conflict and manages the merging process within a controlled parameter subset. TATR is designed to integrate easily with existing merging methods like AdaMerging and Ties-Merging without additional training, providing an efficient approach to address knowledge conflicts in model merging.

### Strengths
- This paper proposes a method, called Task Arithmetic in Trust Region (TATR), that solves the issue of knowledge conflicts. It explores this issue from the dimensions in the model parameter space that cause only small changes in the task-specific losses.
- The paper with clear explanations about the motivation behind Task Arithmetic in Trust Region (TATR).
- The experiments covering multiple datasets demonstrate that TATR improves multi-task performance.

### Weaknesses
 - Regarding knowledge conflict, which has been previously explored in works such as [1] Cross-task Knowledge Distillation in Multi-Task Recommendation, [2] Multi-Task Distillation: Towards Mitigating Negative Transfer in Multi-Task Learning, [3] Conflict-Averse Gradient Descent for Multi-Task Learning, [4] Hacking Task Confounder in Meta-Learning, and [5] Parameter Competition Balancing for Model Merging, with the similar method (model merging from the parameter perspective). How does this work differ from these studies? Are there any new insights provided? **This is my biggest concern.**

- The paper employs an orthogonal component for model merging, intuitively, this approach might introduce task-irrelevant noise into the model, and I find it challenging to understand how such noise could enhance model performance theoretically.

- The proposed method performs poorly on the Cars dataset. Could the authors provide an analysis of why this might be the case?

- (Minor) In Table 1, the authors should highlight the best and second-best performance values, as their absence significantly affects readability. Additionally, indicating the number of datasets on which the proposed method achieved the best performance would facilitate a more straightforward quantitative assessment of its advantages.

### Questions
Please see **Weaknesses**.

### Soundness
2

### Presentation
3

### Contribution
2
