### Summary

The authors propose a synthetic task to study stepwise inference in transformers. The task is a graph navigation problem where a model is given two nodes and needs to determine if there is a path between them. The authors show that stepwise inference improves performance, there is a diversity-accuracy tradeoff in sampling temperature, the model prefers to follow the shortest path, and the model can generalize to unseen combinations of motifs.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed synthetic task is interesting and relevant to the study of stepwise inference in transformers.
- The authors provide a comprehensive analysis of the proposed task, including the impact of stepwise inference, sampling temperature, and generalization to unseen combinations of motifs.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear motivation for the proposed synthetic task. It is not clear why this task is relevant to the study of stepwise inference in transformers. The authors should provide a more detailed explanation of the connection between the task and stepwise inference, and why this task is a good proxy for studying stepwise inference in real-world scenarios.
- The authors do not compare their results to any existing work on stepwise inference in transformers. It would be helpful to see how the authors' findings align with or differ from previous studies. The lack of comparison makes it difficult to assess the novelty and significance of the results.
- The authors do not provide a detailed analysis of the limitations of their approach. For example, it would be helpful to discuss the potential biases in the synthetic task and how these biases might affect the results. The authors should also discuss the generalizability of their findings to other tasks and datasets.

### Suggestions

The authors should begin by clearly articulating the motivation behind their synthetic graph navigation task. They need to explain why this specific task is a suitable model for studying stepwise inference in transformers. This explanation should go beyond a superficial connection and delve into the underlying mechanisms. For example, they could discuss how the graph structure relates to the internal representations of a transformer model and how the stepwise inference process might manifest in this context. A more detailed explanation of the task's relevance to real-world problems would also strengthen the paper. This could involve discussing how graph navigation problems are encountered in various domains, such as robotics, navigation systems, or knowledge graph reasoning, and how the proposed task can provide insights into the behavior of transformers in these scenarios. Furthermore, the authors should provide a more thorough justification for why this particular task is a good proxy for studying stepwise inference, rather than simply stating that it is a graph navigation problem.

To address the lack of comparison with existing work, the authors should conduct a more comprehensive literature review and explicitly compare their findings with relevant studies on stepwise inference in transformers. This comparison should not only highlight the similarities but also the differences in methodology, results, and conclusions. For example, if previous work has explored similar tasks or datasets, the authors should discuss how their approach differs in terms of the model architecture, training procedure, or evaluation metrics. They should also discuss how their findings align with or challenge previous results. This would help to establish the novelty and significance of their work and provide a more complete picture of the current state of research in this area. The authors should also consider including a discussion of the limitations of their approach in the context of existing work, highlighting any potential biases or assumptions that might limit the generalizability of their findings.

Finally, the authors need to provide a more detailed analysis of the limitations of their approach. This should include a discussion of potential biases in the synthetic task, such as the specific graph structures used and how they might influence the results. They should also discuss the generalizability of their findings to other tasks and datasets. For example, they could discuss whether the observed effects of stepwise inference, sampling temperature, and generalization to unseen combinations of motifs would be observed in more complex or real-world graph navigation tasks. The authors should also consider the computational cost of their approach and whether it is feasible to apply it to larger datasets or more complex models. A thorough discussion of these limitations would help to provide a more balanced and nuanced view of the paper's contributions and limitations.

### Questions

- What is the motivation behind the proposed synthetic task? How does it relate to stepwise inference in transformers?
- How do the authors' results compare to any existing work on stepwise inference in transformers?
- What are the limitations of the proposed approach? How might these limitations affect the generalizability of the findings?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
