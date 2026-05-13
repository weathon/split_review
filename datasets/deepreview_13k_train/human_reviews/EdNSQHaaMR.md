# Selective Task Group Updates for Multi-Task Optimization

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Multi-task learning enables the acquisition of task-generic knowledge by training multiple tasks within a unified architecture. However, training all tasks together in a single architecture can lead to performance degradation, known as negative transfer, which is a main concern in multi-task learning. Previous works have addressed this issue by optimizing the multi-task network through gradient manipulation or weighted loss adjustments. However, their optimization strategy focuses on addressing task imbalance in shared parameters, neglecting the learning of task-specific parameters. As a result, they show limitations in mitigating negative transfer, since the learning of shared space and task-specific information influences each other during optimization. To address this, we propose a different approach to enhance multi-task performance by selectively grouping tasks and updating them for each batch during optimization. We introduce an algorithm that adaptively determines how to effectively group tasks and update them during the learning process. To track inter-task relations and optimize multi-task networks simultaneously, we propose proximal inter-task affinity, which can be measured during the optimization process. We provide a theoretical analysis on how dividing tasks into multiple groups and updating them sequentially significantly affects multi-task performance by enhancing the learning of task-specific parameters. Our methods substantially outperform previous multi-task optimization approaches and are scalable to different architectures and various numbers of tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a multi-task learning method that adaptively groups tasks based on proximal inter-task affinity and then sequentially updates each group. It provides a theoretical explanation of the benefits of sequentially updating task groups and the role of incorporating task-specific parameters in reducing conflicts. Experimental results demonstrate the method's superior performance across various benchmarks.

### Strengths
1. Solid analysis from a theoretical perspective: The paper provides theoretical insights to explain the effectiveness of the proposed method, including (i) the benefits of sequential updating of groups, and (ii) the role of incorporating task-specific parameters in reducing conflicts.

2. The paper is well-written and well-organized.

### Weaknesses
1. Based on proximal inter-task affinity, what principle do we use for task grouping? Discussion on other principles should be included. For example, in [1], they use the Fisher Information Matrix, grouping the most heterogeneous tasks to mitigate conflicts.

2. The motivation for introducing proximal inter-task affinity: After reading Appendix A.1, I still find it difficult to understand the motivation for introducing proximal inter-task affinity.

3. Sequential learning on tasks [1], domains [3,4], and mini-batches [2] for alignment has been studied previously. It would be beneficial to compare the different theoretical perspectives between the proposed method and these prior studies.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
2

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
The author proposes a method for addressing multi-objective problems by grouping objectives.
In the process of considering relations between tasks (objectives), the concept of inter-task affinity was introduced, but additional computation was reduced by focusing on the update of task-specific parameters.
Additionally, introducing the concept of affinity to group objectives is the author’s original idea and has been thoroughly analyzed both theoretically and experimentally.

### Strengths
1. Experimental Analysis
In the field of deep learning, the analysis of batch sequences has not been extensively explored. The author argues that grouping certain objectives in multi-objective problems can be significantly beneficial from a global perspective and has demonstrated this experimentally. In cases where the multi-task learning (MTL) results outperform those of single-task learning (STL), the author’s method consistently achieves the highest performance, which serves as strong empirical support for the validity of the proposed approach.

2. Logical Approach
The author’s approach to deriving proxy task affinity is reasonable.
By utilizing the loss after task parameter updates, the author effectively reduced additional computations
Also, the proposed method has been theoretically proven to remain useful.
Additionally, the explanation of the benefits of grouping derived from Theorem 2 is clearly written and easy to understand.

### Weaknesses
 In my understanding, some questions remain regarding the actual utility of certain theoretical approaches.
The author addresses the utility of multiple objectives in a local context, but optimization in the field of deep learning is far more complex.
In practice, grouping the same classes together for optimization in classification tasks may be optimal for the currently updated classes locally; however, it is challenging to reach a global optimum.
I would like to see additional experimental evaluation on this matter.

### Questions
As I mentioned in the weaknesses section, I do not interpret the author’s theoretical analysis as indicating that the proposed multiple-objective method can be effectively solved on a global scale.
However, I am not suggesting the necessity of a stringent theoretical foundation.
I would like to see evidence that the author’s method can consistently provide an optimal point.
Demonstrating that the proposed method is robust across different batch sizes, numbers of groups, and optimization hyperparameters would effectively support its consistency and reliability.

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
4

### Summary
This paper discusses the challenges of multi-task learning, where training multiple tasks together in one architecture can lead to negative transfer or performance degradation. Traditional solutions focus on optimizing shared parameters but neglect task-specific ones. The proposed solution involves grouping tasks selectively and updating them in each batch, along with an algorithm that adapts to determine effective task grouping. The concept of proximal inter-task affinity is introduced to track task relations during optimization. This approach is said to improve multi-task performance by enhancing the learning of task-specific parameters and is shown to outperform previous methods, being scalable to different architectures and task numbers.

### Strengths
1. This paper investigates an important problem of multi-task learning. 
2. This paper is well-written and easy to follow.
3.  Realizing that traditional solutions focus on optimizing shared parameters but neglect task-specific ones, the authors delve into the concept of proximal inter-task affinity, making this paper well-motivated.
4.  The proposed method is new to me and gives a fresh perspective to further improve the performance of MTL.
5. This approach is said to improve multi-task performance by enhancing the learning of task-specific parameters and is shown to outperform previous methods, being scalable to different architectures and task numbers.

### Weaknesses
1. The task grouping result in Figure 3c seems out of converge. Will the number of groups further increase as the iteration becomes larger? It's unclear if the observed fluctuations in the number of task groups are a stable behavior or if they might continue to increase indefinitely given more training iterations. This raises concerns about the practical convergence of the proposed method and whether the task groupings will stabilize or continue to evolve, potentially leading to instability.
2. Why Nash-MTL is not reported in Table 2? The absence of results for Nash-MTL in Table 2 is a significant omission, as it is a relevant baseline for multi-task learning. It's important to understand why this method was not included, especially since it is a well-established approach. The lack of comparison makes it difficult to fully assess the relative performance of the proposed method.
3. In the theoretical analysis (Section 4), the authors explain how this sequential update strategy can improve multi-task performance from an optimization standpoint. What about the generalization standpoint? I think the generalization of a model is more important. The theoretical analysis focuses on optimization but lacks a discussion of generalization. While optimizing training loss is important, it's crucial to understand how the proposed method affects the model's ability to generalize to unseen data. Without a generalization analysis, it's difficult to determine the practical value of the method.
4. In real-world applications, a typical MTL problem may have only a few tasks (e.g., 3). Will the proposed method work in such a circumstance? What is the task grouping result if there are only three tasks? The paper primarily focuses on scenarios with a large number of tasks, but it's unclear how the method performs with a smaller number of tasks, which is common in real-world applications. It's important to evaluate the method's effectiveness and task grouping behavior when dealing with only a few tasks.

### Questions
Please refer to the weaknesss section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel MTL method in which tasks are dynamically grouped according to the conflict of different tasks during the optimization process and the model is optimized based on these grouped tasks. The method introduces only a limited computation cost and the experiment results show strong performance of their method compared to several existing MTL methods

### Strengths
1. The paper proposes a novel optimization method to optimize the multi-task learning process from a new perspective.

2. The method demonstrates promising results on the NYUv2, PASCAL-Context, and Taskonomy datasets.

3. The paper provides a theoretical explanation of the advantages of sequential optimization of task groups and provides an analysis of convergence.

### Weaknesses
1. There are some incorrect statements in the article. For example, in Line 092, “This perspective is not addressed in traditional multi-task optimization, which typically focuses solely on the learning of shared parameters.” is wrong, because the learning of task-specific parameters is considered in IMTL [1].

2. The conclusion in Line 373-374, “This suggests that grouping tasks with proximal inter-task affinity and subsequently updating these groups sequentially result in lower multi-task optimization. sequentially result in lower multi-task loss compared to jointly backpropagating all tasks.” does not seem relevant to the theorem above. Can you give a more detailed explanation?

3. For the conclusion in Line 525-526, “We observe that the affinity decay rate ... within a reasonable range.”, there is a lack of experimental results on the performance of models with different $\beta$.

4.  The definition of 'heterogeneous' task grouping is unclear. It is stated that tasks are grouped based on disparity, but the specific metric used to measure this disparity and how it translates to task grouping is not well-defined. This makes it difficult to assess the validity of the experimental results.

5. The experimental results show that even when tasks are grouped to maximize conflict (heterogeneous grouping), the performance is still better than random grouping. This contradicts the core motivation of the paper, which is that task conflicts are the primary cause of poor multi-task learning performance. This raises questions about the validity of the proposed approach and its underlying assumptions.

6. The experimental results show a trend where performance degrades as the number of random groups increases. This phenomenon is not adequately explained, and it is unclear why increasing the number of groups leads to worse performance, especially since the method is designed to handle task conflicts.

### Questions
1. Why is the number of groups in Figure 3c not an integer?

2. Line 523, "Table 4c" means "Figure 4c"?

3. Can you compare the performance of random grouping during optimization?

### Soundness
3

### Presentation
2

### Contribution
3
