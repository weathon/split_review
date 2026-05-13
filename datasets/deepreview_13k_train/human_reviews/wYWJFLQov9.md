# ST-GCond: Self-supervised and Transferable Graph Dataset Condensation

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
The increasing scale of graph datasets significantly enhances deep learning models but also presents substantial training challenges. Graph dataset condensation has emerged to condense large datasets into smaller yet informative ones that maintain similar test performance. However, these methods require downstream usage to match the original dataset and task, which is impractical in real-world scenarios. Our empirical studies show that existing methods fail in "cross-task" and "cross-dataset" scenarios, often performing worse than training from scratch. To address these challenges, we propose a novel method: Self-supervised and Transferable Graph dataset Condensation (ST-GCond). For cross-task transferability, we propose a task-disentangled meta optimization strategy to adaptively update the condensed graph according to the task relevance, encouraging information preservation for various tasks. For cross-dataset transferability, we propose a multi-teacher self-supervised optimization strategy to incorporate auxiliary self-supervised tasks to inject universal knowledge into the condensed graph. Additionally, we incorporate mutual information guided joint condensation mitigating the potential conflicts and ensure the condensing stability. Experiments on both node-level and graph-level datasets show that ST-GCond outperforms existing methods by 2.5% to 18.7% in all cross-task and cross-dataset scenarios, and also achieves state-of-the-art performance on 5 out of 6 datasets in the single dataset and task scenario.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This manuscript studies graph dataset condensation from a different perspective. It proposes a method for condensing the graph dataset in a cross-dataset and cross-task manner. The proposed ST-GCond condenses the dataset while preserving the most universal/general information, which is task-agnostic.  Specifically, there are two components of the method. The first is task-disentangled meta optimization which makes the condensed dataset aware of the task difference. The second is multi-teacher self-supervised optimization which makes the dataset hold some uniserval information. Experiments and ablation studies are well-done with nontrivial performance gain.

### Strengths
- It is great to see that the proposed method improves under the setup even in the single dataset and task. The performance gain under the setup of cross-dataset and cross-task is indeed nontrival. 

- The proposed method is applicable for both node-level and graph-level tasks, making it more general. 

- The proposed method makes it work with the combination of multi-task learning and self-supervised learning on the dataset condensation, which might inspire more researchers on this research topic.

### Weaknesses
 - For the "Mutual Information Guided Joint Condensation", it is unclear why the performance is dropped when we use both the hard label from the supervised condensation and the soft label from the self-supervised condensation. The author argues that this is due to the conflict

- The cross-task and cross-dataset dataset condensation settings are indeed interesting and are more applicable in real scenarios. However, such settings are a little bit overlap with that of the graph model pertaining. The pertaining of the model can also achieve faster adaption to the new task or dataset. Can the authors provide a more detailed discussion of the differences?

- From the ablation studies, it is shown that the proposed method can even achieve the best performance with either only the "self" part or the "meta" part. Why do the authors say that "ST-GCond w/o self and ST-GCond w/o meta perform poorly on both datasets"?

- It is a little bit unfair for the comparison as the proposed method utilizes much more information during the dataset condensation. For example the multi-label information (for the meta-training part) and self-supervised models (for the self-training part).

- What if we do not have the multi-task information for the dataset we would like to condense?

### Questions
Please refer to the weaknesses part.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel graph dataset condensation method termed ST-GCond that enhances transferability across tasks and datasets using a multi-teacher self-supervised optimization strategy. ST-GCond effectively condenses large graph datasets, which can maintain high performance in varied applications by leveraging multiple pre-trained models and self-supervised learning. Experiments demonstrate ST-GCond's effectiveness in both single-task/single-dataset and cross-task/cross-dataset scenarios.

### Strengths
ST-GCond performs well across different tasks and datasets and overcomes the limitations in traditional graph condensation methods.

By using multiple pre-trained models as teachers, the proposed method captures a wide range of features and knowledge, and thereby improving its ability to generalize.

### Weaknesses
The proposed ST-GCond method introduces substantial computational overhead due to task-disentangled meta optimization and multi-teacher self-supervised optimization. Given the iterative updates for each sub-task and multiple self-supervised models, the overall training time could be significantly increased. It would be beneficial if the authors could provide detailed analysis of computational cost.

The proposed method would benefit from a thorough exploration of hyperparameter tuning, such as the number of sub-tasks and learning rates.  Including a sensitivity analysis or providing guidelines on hyperparameter selection based on different types of graph datasets could be beneficial.

Significant disparities between tasks may limit the condensed graph's ability to capture all relevant information, and thereby reducing the effectiveness.

The power of the multi-teacher strategy relies on the quality of pre-trained models. Will low-quality or irrelevant models impair the performance?

The effectiveness of the multi-teacher self-supervised optimization strongly hinges on the optimal configuration of the weights  assigned to each teacher model's output. However, this paper does not provide a clear illustration for how these weights are optimized during the training process.

### Questions
Can you provide a detailed analysis of the computational costs and compare them with conventional methods?

What strategies are used for tuning hyperparameters like the number of sub-tasks and learning rates? Could you include guidelines for hyperparameter selection?

How does the quality of pre-trained models affect the performance of ST-GCond?

Can you explain how the weights assigned to each teacher model's output are optimized during training?

### Soundness
3

### Presentation
3

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
This work addresses the challenge of the transferability of condensing graph datasets in graph condensation, which is an important topic. The authors propose ST-GCond, a self-supervised and transferable graph dataset condensation method with a carefully designed loss function.

### Strengths
1. The transferability of condensed graphs is an important topic. The authors make the first effort to deal with it.
2. Some results are promising.
3. The motivation is clear and the writing in the introduction is good.

### Weaknesses
Please see the Questions below.

I'm willing to increase my rating as long as the authors can adequately address my concerns.

### questions:
 1. I suggest the authors to provide some visualization of condensed graphs, together with some discussion on some statistical characteristics of them to make the results more credible.  
2. In the Appendix D, the authors only provide and compare the running time of the proposed method together with one baseline method. Since this is an efficiency-oriented field, more comparison is needed. For example, the VRAM (GPU memory usage) during training. The proposed method introduced too many models (e.g., multiple teacher models), I'm wondering whether this will make the GPU memory usage of the proposed method even higher.
3. In cross-dataset and cross-task scenario, a finetune step on the original downstream data is needed, what if we do not undergo this step? It's weird to use the actual training data plus the condensed data to train, which leads to a downgrade of the contribution to the work .
4. What is the actual value of \alpha and \beta and other hyperparameters in the final loss function/in the main result tables? I notice the authors provide the search space of them, but did not provide the actual value / their changing trajectory during training.
5. The authors provide an ablation study on each loss terms. What's the reason for causing such results?
6. In Line 222, the author claim that "The most important step is to utilize fast adaptation in Gs." What makes it the most important step?
7. In the Appendix G.1, Line 799, the final matrix is minus by a \delta term, which comes out of no where. The authors give no explanations.

Some typos:
1. Line 396: A dot is missed at the end of the caption.
2. Line 214:  ”global minimum”  ->  "global minimum"

### Questions
1. I suggest the authors to provide some visualization of condensed graphs, together with some discussion on some statistical characteristics of them to make the results more credible.  
2. In the Appendix D, the authors only provide and compare the running time of the proposed method together with one baseline method. Since this is an efficiency-oriented field, more comparison is needed. For example, the VRAM (GPU memory usage) during training. The proposed method introduced too many models (e.g., multiple teacher models), I'm wondering whether this will make the GPU memory usage of the proposed method even higher.
3. In cross-dataset and cross-task scenario, a finetune step on the original downstream data is needed, what if we do not undergo this step? It's weird to use the actual training data plus the condensed data to train, which leads to a downgrade of the contribution to the work .
4. What is the actual value of \alpha and \beta and other hyperparameters in the final loss function/in the main result tables? I notice the authors provide the search space of them, but did not provide the actual value / their changing trajectory during training.
5. The authors provide an ablation study on each loss terms. What's the reason for causing such results?
6. In Line 222, the author claim that "The most important step is to utilize fast adaptation in Gs." What makes it the most important step?
7. In the Appendix G.1, Line 799, the final matrix is minus by a \delta term, which comes out of no where. The authors give no explanations.

Some typos:
1. Line 396: A dot is missed at the end of the caption.
2. Line 214:  ”global minimum”  ->  "global minimum"

### Soundness
3

### Presentation
2

### Contribution
3
