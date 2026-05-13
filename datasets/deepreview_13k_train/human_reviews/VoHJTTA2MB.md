# Mixing It Up:  The Cocktail Effect of Multi-Task Fine-Tuning on LLM Performance - A Case Study in Finance

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
The application of large language models (LLMs) in domain-specific contexts, including finance, has expanded rapidly. Domain-specific LLMs are typically evaluated based on their performance in various downstream tasks relevant to the domain. In this work, we present a detailed analysis of fine-tuning LLMs for such tasks. Somewhat counterintuitively, we find that in domain-specific cases, fine-tuning exclusively on the target task is not always the most effective strategy. Instead, multi-task fine-tuning - where models are trained on a cocktail of related tasks - can significantly enhance performance. We demonstrate how this approach enables a small model, such as Phi-3-Mini, to achieve state-of-the-art results, even surpassing the much larger GPT-4-o model on financial benchmarks. Our study involves a large-scale experiment, conducting over 200 training experiments using several widely adopted LLMs as baselines, and empirically confirms the benefits of multi-task fine-tuning. Additionally, we explore the use of general instruction data as a form of regularization, suggesting that it helps minimize performance degradation. We also investigate the inclusion of mathematical data, finding improvements in numerical reasoning that transfer effectively to financial tasks. Finally, we note that while fine-tuning for downstream tasks leads to targeted improvements in task performance, it does not necessarily result in broader gains in domain knowledge or complex domain reasoning abilities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents extensive empirical results comparing the performance of various LLMs fine-tuned for a specific task to the performance of these LLMs fine-tuned on various combinations of tasks. The paper suggests that there often exists a combination of tasks that can improve performance on a downstream task of interest while also outperforming frontier models such as GPT-4o.

### Strengths
If code and all models are released, it could be a valuable resource for researchers studying topics such as data selection and model merging.

### Weaknesses
 - It seems unfair to compare best-of-200 models evaluated on the test set vs a single model when arguing that multi-task training is beneficial. A comparable budget should be given to the single-task fine-tuning. You could, for example, perform fine-tuning for a single task with varying number of epochs (or using early stopping), learning rate, data shuffling, etc., to have an equivalent of 200 models and then report the best test performance.
- There is very little insight into how one should select the tasks for fine-tuning (besides that general instruction tuning with Orca datasets seems to help). There are also prior works that study similar problems which would be interesting to consider:

[1] Data Selection for Language Models via Importance Resampling. Xie et. al, 2023 

[2] LESS: Selecting Influential Data for Targeted Instruction Tuning. Xia et. al, 2024

### Questions
When comparing to GPT-4o, did you verify that the gains of the smaller fine-tuned models are due to improved performance or because they follow the format better? GPT-4o may provide correct responses in the wrong format, leading to lower performance when using rule-based evaluation. Using LLM judge as you did for FinanceBench, could help to alleviate potential biases of rule-based evaluation (i.e. the judge compares LLM response to ground truth).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors investigate the effectiveness of multi-task fine-tuning as a method to enhance the performance of large language models (LLMs) on downstream tasks. 

They claimed that they conduct extensive experiments with over 200 models and demonstrate that combining training data from multiple related financial tasks results in a "cocktail effect," which significantly boosts performance. They argue that their approach even enables smaller models, such as Phi-3-Mini, to outperform larger counterparts like GPT-4-o in specific benchmarks. The authors also state the benefits of this training strategy, emphasizing the synergistic advantages gained from leveraging inter-task relationships.

### Strengths
The paper is well-written, featuring a clear structure and logical flow, although it potentially omits some important details, as noted in the Weaknesses section.

The evaluation metrics established by the authors for different types are reasonable and appropriate but could be more comprehensive.

The presentation of visualizations is informative and insightful.

### Weaknesses
1. Given the author mention multiple times in abstract, introduction and conclusion sections that they have trained 200+ models, however, there is no relevant details about it in the main body of the paper. It would be necessary to include critical information such that what is the full implemented model list and how the model selection is conducted as the author seem to eventually choose Phi-3 Mini to present their research outcomes.

2. Although the authors fine-tuned their models on multi-purpose datasets, they selected a dataset with limited variety and evaluated their models on a relatively narrow range of financial tasks, which is even fewer than some previous studies [1]. This raises concerns about the novelty and comprehensiveness of their work. It could further undermine the soundness of their training approach. Could you please elaborate on the advancements made by your research?

[1] Xie, Q., Li, D., Xiao, M., Jiang, Z., Xiang, R., Zhang, X., ... & Ananiadou, S. (2024). Open-finllms: Open multimodal large language models for financial applications. arXiv preprint arXiv:2408.11878.

3. The model comparison is based solely on various types of accuracy metrics. The paper lacks detailed statements regarding repeated experiments and does not provide error bars or significance levels for most of the experiments. Given that some accuracy results, such as those in Table 2 comparing their fine-tuned Phi-3 small with other models, are closely matched, it would be beneficial to include such evaluation metrics to ensure a more robust analysis.

### Questions
Please refer to the question proposed in the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a detailed analysis of fine-tuning large language models (LLMs) for domain-specific tasks, with a focus on finance. The authors propose a multi-task fine-tuning approach, where models are trained on a combination of related tasks, and demonstrate its effectiveness by achieving state-of-the-art results on financial benchmarks. They compare the performance of a smaller model, Phi-3-Mini, with a larger model, GPT-4-o, and show that multi-task fine-tuning allows Phi-3-Mini to surpass GPT-4-o. The authors also explore the use of general instruction-following and mathematical data during fine-tuning and analyze the impact of different datasets on model performance.

### Strengths
1. The paper presents a thorough analysis of multi-task fine-tuning for domain-specific LLMs, including an extensive experimental setup involving over 200 models.
2.  The authors provide strong empirical evidence for the benefits of multi-task fine-tuning, demonstrating significant performance gains on financial benchmarks.
3. The paper explores the use of general instruction-following and mathematical data during fine-tuning, which adds valuable insights into the regularization and numerical reasoning abilities of the models.
4. The authors use an incremental approach for fine-tuning the model, which allows them to isolate the impact of individual datasets and explore the interactions between datasets when fine-tuned together.

### Weaknesses
1.While the paper provides strong empirical evidence, it lacks theoretical insights into why multi-task fine-tuning is effective.
2.The paper only compares multi-task fine-tuning with single-task fine-tuning and does not consider other fine-tuning strategies such as adapter-based fine-tuning or prompt-tuning. The proposed finetuning method is similar to multi-task deep neural networks (MT-DNN), see Liu et al. 2019, ACL.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
