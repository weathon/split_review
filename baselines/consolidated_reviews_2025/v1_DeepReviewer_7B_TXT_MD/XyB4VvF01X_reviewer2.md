### Summary

The paper presents a novel graph neural network (GNN) model, Graph2Tac, for theorem proving in Coq. Graph2Tac is designed to adapt to new definitions and theorems in real-time, addressing the challenge of adapting to new concepts and definitions in a dynamic environment. The authors evaluate Graph2Tac on a challenging set of theorems and compare it with other symbolic and machine learning solvers, including CoqHammer, k-NN, and Transformer-GPU. The results show that Graph2Tac outperforms these solvers in proving theorems in new Coq packages.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper introduces a novel graph neural network (GNN) model, Graph2Tac, for theorem proving in Coq. This is a significant contribution to the field of automated theorem proving, as it addresses the challenge of adapting to new concepts and definitions in a dynamic environment.
- The paper provides a comprehensive comparison of Graph2Tac with other symbolic and machine learning solvers, including CoqHammer, k-NN, and Transformer-GPU. This comparison highlights the strengths and weaknesses of each approach and provides insights into the potential of GNNs for theorem proving.
- The paper is well-written and organized, with clear explanations of the proposed model, the dataset, and the evaluation metrics. The authors also provide a detailed description of the experimental setup and the results, making it easy for readers to understand and replicate the findings.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as the computational cost of training and inference, the scalability of the model to larger datasets, and the generalizability of the model to different Coq environments.
- The paper could also benefit from a more in-depth analysis of the types of theorems and definitions that Graph2Tac can effectively prove or adapt to. This would provide a better understanding of the strengths and weaknesses of the model and guide future research in this area.
- The authors should also consider comparing their approach with other state-of-the-art theorem proving methods, such as those based on reinforcement learning or interactive theorem proving, to provide a more comprehensive evaluation of the proposed model.

### Suggestions

The paper would be significantly strengthened by a more thorough analysis of the computational demands of the proposed Graph2Tac model. Specifically, the authors should provide a detailed breakdown of the training time, inference time, and memory usage for different dataset sizes. This analysis should include a discussion of how these metrics scale with the number of definitions, theorems, and proof states. Furthermore, it would be beneficial to explore techniques for optimizing the model's performance, such as model pruning, quantization, or distributed training. This would make the model more practical for real-world applications and allow for a better understanding of its limitations. The authors should also investigate the impact of different hyperparameter settings on the model's performance and provide guidelines for selecting appropriate values for new datasets.

In addition to computational aspects, the paper should delve deeper into the types of theorems and definitions that Graph2Tac can effectively handle. A more granular analysis of the model's performance on different categories of theorems, such as those involving specific logical connectives, quantifiers, or mathematical concepts, would be valuable. For example, the authors could analyze the model's performance on theorems that require complex proof strategies or those that rely on specific libraries or definitions. This analysis should also include a discussion of the types of definitions that the model struggles with, such as those that involve complex data structures or non-standard mathematical concepts. Such an analysis would provide a more nuanced understanding of the model's capabilities and limitations and guide future research in this area. Furthermore, the authors should explore the model's ability to generalize to new definitions and theorems that are significantly different from those seen during training. This could involve testing the model on theorems from different Coq libraries or those that require novel proof strategies.

Finally, the paper should include a more comprehensive comparison with other state-of-the-art theorem proving methods. While the comparison with CoqHammer, k-NN, and Transformer-GPU is a good starting point, it would be beneficial to include a comparison with other relevant approaches, such as those based on reinforcement learning or interactive theorem proving. This would provide a more complete picture of the current state of the art and help to position the proposed model within the broader context of theorem proving research. The authors should also discuss the trade-offs between different approaches, such as the computational cost, the interpretability of the model, and the level of human involvement required. This would provide a more balanced and nuanced evaluation of the proposed model and highlight its unique strengths and weaknesses.

### Questions

- How does the proposed model scale to larger datasets and more complex Coq environments?
- What are the computational resources required for training and inference, and how can they be optimized?
- How does the model generalize to new definitions and theorems that are significantly different from those seen during training?
- How does the proposed approach compare with other state-of-the-art theorem proving methods, such as those based on reinforcement learning or interactive theorem proving?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
