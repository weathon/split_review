### Summary

The paper proposes a synthetic graph navigation task to study the stepwise inference in transformers. The authors demonstrate that stepwise inference improves performance, there is a diversity-accuracy tradeoff in sampling temperature, the model prefers to follow the shortest path, and the model can generalize to unseen combinations of motifs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed synthetic task is interesting and relevant to the study of stepwise inference in transformers.
3. The authors provide a comprehensive analysis of the proposed task, including the impact of stepwise inference, sampling temperature, and generalization to unseen combinations of motifs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear motivation for the proposed synthetic task. It is not clear why this task is relevant to the study of stepwise inference in transformers. The authors should provide a more detailed explanation of the connection between the task and stepwise inference, and why this task is a good proxy for studying stepwise inference in real-world scenarios.
2. The authors do not compare their results to any existing work on stepwise inference in transformers. It would be helpful to see how the authors' findings align with or differ from previous studies. The lack of comparison makes it difficult to assess the novelty and significance of the results.
3. The authors do not provide a detailed analysis of the limitations of their approach. For example, it would be helpful to discuss the potential biases in the synthetic task and how these biases might affect the results. The authors should also discuss the generalizability of their findings to other tasks and datasets.

### Suggestions

The authors should elaborate on the specific mechanisms through which the proposed graph navigation task relates to stepwise inference in transformers. While the task is presented as a proxy, a more detailed explanation of how the model's internal representations and inference steps correspond to the graph traversal process is needed. For instance, how does the model's attention mechanism facilitate the step-by-step decision-making process, and how does the graph structure influence the model's ability to perform stepwise inference? A more thorough discussion of these aspects would strengthen the motivation for using this specific task and clarify its relevance to the broader field of stepwise inference.

Furthermore, the authors should conduct a more rigorous comparison of their findings with existing literature on stepwise inference in transformers. This comparison should not only highlight the similarities but also the differences in methodology, results, and conclusions. For example, if previous work has explored similar tasks or datasets, the authors should discuss how their approach differs in terms of the model architecture, training procedure, or evaluation metrics. This would help to establish the novelty and significance of their work and provide a more complete picture of the current state of research in this area. Additionally, a discussion of the limitations of the current study, such as the specific graph structures used and the potential biases introduced by the synthetic task, would be beneficial.

Finally, the authors should provide a more detailed analysis of the limitations of their approach, including potential biases in the synthetic task and the generalizability of their findings to other tasks and datasets. For example, how might the specific graph structures used in the synthetic task influence the results, and how might the findings differ if applied to more complex or real-world graph navigation tasks? A discussion of these limitations would provide a more balanced and nuanced view of the paper's contributions and limitations. The authors should also consider the computational cost of their approach and whether it is feasible to apply it to larger datasets or more complex models.

### Questions

See weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
