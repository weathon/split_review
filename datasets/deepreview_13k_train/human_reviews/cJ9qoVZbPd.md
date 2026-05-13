# Locate-then-Unlearn: An Effective Method of Multi-Task Continuous Learning for Large Language Models

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Nowadays large language models (LLMs) have achieved remarkable success in
various NLP tasks. However, they often misinterpret human instructions and generate incorrect or outdated responses, highlighting the need for more effective continual learning techniques. While recent efforts have introduced unlearning methods to remove erroneous knowledge, existing approaches still struggle in multi-task learning scenarios. To overcome these limitations, we propose Locate-then-unlearn, a new framework that identifies and selectively unlearns task-specific
neurons to enable efficient multi-task learning. We hypothesize that LLM neurons can be broadly categorized into task-specific neurons for handling individual
tasks, and general neurons to maintain the model’s foundational capabilities. To
accurately identify task-specific neurons, the locating process includes: (1) ranking task-related neurons based on their importance to each task, and (2) identifying
task-specific neurons by applying intervention to assess how neuron activity impacts task performance, isolating those most critical to each task. We conduct
comprehensive evaluations in two experimental setups: single-task specialization
and multi-task generalization. The results show that our method significantly improves performance across both settings. This indicates that our method effectively balances model efficiency and accuracy in multi-task continual learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes to unlearn task-specific neurons to enable more efficient multi-task learning. The proposed approach, locate-then-unlearn, first locates task-relevant neurons, deduplicates the neurons that are relevant for multiple tasks, subtracts the corresponding parameters to unlearn false answers, and relearns the objective tasks.

The proposed approach shows higher performance than five baseline methods on five datasets in the multi-task learning scenario, and improvements on three out of five datasets in the single-task setting (with the remaining two getting close performance with direct full fun-tuning).

### Strengths
* This work presents solid experimental results and ablation studies, showing the effectiveness of each component.

* The main novelty lies in finding task-specific neurons for more efficient re-learning.

### Weaknesses
 * The causal effect between the neurons and different tasks requires more careful examination. Although the approach shows empirical improvement,  the assumption that neurons are task-specific might require further evidence. Specifically, the method identifies task-specific neurons based on their activation patterns on a held-out set of data for each task. However, it's not clear if these neurons are truly specific to the task or if they are simply responding to some other underlying feature of the data. For example, if the datasets for different tasks have different distributions of input tokens, the identified neurons might be responding to these token distributions rather than the task itself. Further analysis is needed to disentangle the task-specific and data-specific factors influencing neuron activation.

* This approach is dependent on the selected data used to locate neurons (section 3.2.) and unlearn tasks (section 3.3). The authors provide several ablation studies on the method components, while it may be worthwhile to conduct ablations on the choice of data. The current study uses a fixed set of data for locating task-specific neurons, but the choice of this data could significantly impact the identified neurons. For instance, if the data used for locating neurons is not representative of the overall task distribution, the identified neurons might not be truly task-specific. Similarly, the data used for unlearning could also affect the effectiveness of the unlearning process. It is crucial to explore the sensitivity of the method to different data choices for both neuron location and unlearning.

### Questions
* What is the definition of “tasks” in this work? The distribution of data, even under the same tasks, seems to affect the selection of task-specific neurons. Thus, whether improvement will transfer to different datasets from the same tasks is unexamined.

* How are the toy datasets constructed in section 3.2? Are they a subsample of the underlying task data?

* Regarding the design of false answers in section 4.3., the false knowledge can be presented in multiple forms than what’s already in the dataset, which could thus not capture the potential wrong knowledge and influence the effect of unlearning. 

*Typos*

* Title: Continuous -> Continual

* L409-410: implement -> implementing; this sentence is difficult to parse.

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
This paper proposes locate-then-unlearn, to identify and unlearn task-specific neurons in transformer models for multi-task learning. Specifically, the authors propose to identify task-related neurons from top-k important scores for each task, and identify task-specific neurons by removing overlapping neurons shared by different tasks. Finally, the authors fine-tune the selected task-specific parameters with unlearning data, and remove the parameter offset (from fine-tuning) from the original parameters. Experiment results demonstrate that the proposed locate-then-unlearn outperform other knowledge editing baselines on five datasets. They also conduct extensive analysis to demonstrate that the setting of unlearning hyperparameter is important, task-specific neurons work the best on corresponding related tasks.

### Strengths
- The method is intuitively reasonable. By detecting task-related and task-specific neurons, the methods make multi-task learning more parameter-efficient.
- The experiment results show that the proposed method can outperform knowledge editing methods such as ROME and MEMIT on five datasets.
- The authors conduct extensive analysis. The unlearning hyperparameter has a best performing peak, while the threshold is rather robust. The task-specific neurons are important, and tuning them on unrelated tasks lead to worse results. Visualization shows that task-specific neurons are well-separated.
- The writing of the paper is quite clear.

### Weaknesses
 - Since the authors claim that their methods contribute to parameter-efficient multi-task learning, it would be better to compare with methods such as prompt-tuning, lora-hub.
- It would be better if the authors could release their code upon acceptance.

### Questions
- How does the method compare with other PEFT methods, such as prompt-tuning, lora-hub?
- It would be better if the authors can discuss for each new task, how many parameters need to be stored (the percentage of the whole transformer model)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes Locate-then-Unlearn framework to improve LLM continual learning by identifying and selectively unlearning task-specific neurons. By localizing neurons specific to individual tasks and unlearning them, the approach reduces interference between tasks and enhances model efficiency. Experiment results and analyses across multiple datasets demonstrate good performance in both single-task and multi-task settings.

### Strengths
1. The proposed approach is novel.  
2. The proposed approach is well-motivated.  
3. The results show good performance.

### Weaknesses
 1. One problem of LLM continual learning is catastrophic forgetting, it would be better if the authors can further discuss how the proposed approach handle the issue.  
2. For LLM continual learning, it would be better to compare model performance on the benchmark datasets before and after training, so the readers will learn the effect of the learning process on previously learnt task. Currently, the authors just report the performance after training. It would be a plus if the authors can include the model performance before training.  
3. The paper claims many times that the proposed approach "significantly" outperforms existing approaches, but it seems the significance test is missing. So, it is hard to justify whether the improvement is significant.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3
