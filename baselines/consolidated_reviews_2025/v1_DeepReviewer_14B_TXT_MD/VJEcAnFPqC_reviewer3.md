### Summary

This paper proposes a synthetic graph navigation task to study stepwise inference in transformers. The authors find that transformers can learn to perform stepwise inference and identify several phenomena observed at scale, such as the stepwise inference reasoning gap, the diversity-accuracy tradeoff, and the simplicity bias. They also explore the model's navigation preferences and their controllability through in-context exemplars, and examine length generalization and responses to longer contexts with conflicting exemplars.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel synthetic graph navigation task to study stepwise inference in transformers, which is a significant contribution to the field of natural language processing.
2. The authors identify several phenomena observed at scale, such as the stepwise inference reasoning gap, the diversity-accuracy tradeoff, and the simplicity bias, which are important for understanding the behavior of transformers.
3. The paper explores the model's navigation preferences and their controllability through in-context exemplars, and examines length generalization and responses to longer contexts with conflicting exemplars, which are important for understanding the model's ability to generalize and adapt to new situations.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of the motivation behind the proposed synthetic graph navigation task, and how it relates to real-world natural language processing tasks. It is unclear how the specific structure of the graph navigation task, with its directed acyclic graph (DAG) structure, directly translates to the complexities of natural language understanding and generation. The connection between navigating a graph and the sequential, often ambiguous nature of language is not well-established.
2. The paper does not provide a detailed analysis of the results, and it is difficult to draw meaningful conclusions from the findings. For example, the paper does not provide a clear explanation of the stepwise inference reasoning gap, the diversity-accuracy tradeoff, and the simplicity bias. The analysis lacks a deeper dive into the underlying mechanisms causing these phenomena. For instance, the 'simplicity bias' is observed, but the paper does not explore why the model favors shorter paths, or how this relates to the model's architecture or training process. The diversity-accuracy tradeoff is also presented without a clear explanation of the factors influencing this relationship, such as the specific sampling strategies used.
3. The paper does not provide a thorough evaluation of the proposed method, and it is unclear how well it performs compared to existing methods. The paper lacks a comparison to established baselines or alternative approaches for graph navigation or similar tasks. Without such comparisons, it is difficult to assess the significance of the reported results. The evaluation also does not explore the limitations of the proposed method, such as its performance on more complex graph structures or with different types of input data.

### Suggestions

The paper would benefit significantly from a more detailed explanation of how the synthetic graph navigation task relates to real-world NLP challenges. The authors should provide concrete examples of how the graph navigation problem maps to specific NLP tasks, such as question answering or text summarization. For instance, they could explain how the nodes in the graph represent different concepts or entities in a text, and how the edges represent the relationships between them. This would help clarify the relevance of the proposed task and make the findings more applicable to practical NLP problems. Furthermore, the authors should discuss the limitations of the graph navigation task in capturing the full complexity of natural language, acknowledging the differences between the structured nature of graphs and the more ambiguous nature of language.

To improve the analysis of the results, the authors should provide a more in-depth explanation of the observed phenomena. For example, the 'simplicity bias' should be analyzed in terms of the model's internal representations and decision-making processes. The authors could investigate whether the model is learning a shortest-path heuristic, or if there are other factors contributing to this bias. Similarly, the diversity-accuracy tradeoff should be analyzed by varying the sampling temperature and other hyperparameters, and by examining the resulting changes in the model's output. The authors should also provide a more detailed explanation of the stepwise inference reasoning gap, including a discussion of the factors that contribute to this gap and how it relates to the model's ability to perform multi-step reasoning. A more thorough analysis of these phenomena would provide a deeper understanding of the model's behavior and its limitations.

Finally, the paper needs a more comprehensive evaluation of the proposed method. The authors should compare their method to existing approaches for graph navigation or similar tasks, and they should also evaluate the method on a wider range of graph structures and input data. This would help to establish the significance of the reported results and to identify the limitations of the proposed method. The evaluation should also include an analysis of the model's performance on more complex graph structures, such as those with cycles or multiple paths between nodes. The authors should also explore the model's sensitivity to different types of input data, such as noisy or incomplete graphs. This would provide a more complete picture of the model's capabilities and limitations.

### Questions

1. Can you provide more details on the synthetic graph navigation task and how it relates to real-world natural language processing tasks?
2. Can you provide a more detailed analysis of the results, and explain the stepwise inference reasoning gap, the diversity-accuracy tradeoff, and the simplicity bias in more detail?
3. Can you provide a more thorough evaluation of the proposed method, and compare it to existing methods?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
