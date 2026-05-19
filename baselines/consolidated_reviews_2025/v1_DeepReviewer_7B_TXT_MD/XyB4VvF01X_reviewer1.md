### Summary

This paper proposes a graph neural network (GNN) model, Graph2Tac, for theorem proving in Coq. The model is trained on a graph-based dataset of Coq terms and definitions, and can adapt to new definitions and theorems in real-time. The authors compare their model with other symbolic and machine learning solvers, and show that Graph2Tac performs well in proving theorems in new Coq packages.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper presents a novel approach to theorem proving in Coq by leveraging a graph neural network (GNN) model, Graph2Tac, which can adapt to new definitions and theorems in real-time. This is a significant contribution to the field of automated theorem proving, as it addresses the challenge of adapting to new concepts and definitions in a dynamic environment.
- The authors provide a comprehensive comparison of Graph2Tac with other symbolic and machine learning solvers, including CoqHammer, k-NN, and Transformer-GPU. This comparison highlights the strengths and weaknesses of each approach and provides insights into the potential of GNNs for theorem proving.
- The paper is well-written and organized, with clear explanations of the proposed model, the dataset, and the evaluation metrics. The authors also provide a detailed description of the experimental setup and the results, making it easy for readers to understand and replicate the findings.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as the computational cost of training and inference, the scalability of the model to larger datasets, and the generalizability of the model to different Coq environments.
- The paper could also benefit from a more in-depth analysis of the types of theorems and definitions that Graph2Tac can effectively prove or adapt to. This would provide a better understanding of the strengths and weaknesses of the model and guide future research in this area.
- The authors should also consider comparing their approach with other state-of-the-art theorem proving methods, such as those based on reinforcement learning or interactive theorem proving, to provide a more comprehensive evaluation of the proposed model.

### Suggestions

The paper would be significantly strengthened by a more thorough exploration of the practical limitations of the proposed Graph2Tac model. Specifically, the authors should provide a detailed analysis of the computational resources required for both training and inference, including memory usage and processing time, especially as the size of the Coq dataset increases. This analysis should go beyond just reporting overall times and should consider the scaling behavior of the model. For example, it would be beneficial to see how the training time and memory consumption scale with the number of definitions and theorems in the dataset. Furthermore, the authors should discuss the potential for parallelizing the training and inference processes to improve efficiency. This would provide a clearer picture of the practical feasibility of deploying Graph2Tac in real-world scenarios. Additionally, the authors should investigate the model's performance on different types of Coq environments, such as those with different libraries or proof styles, to assess its generalizability. This could involve testing the model on Coq projects from different domains or with different levels of complexity. Such an analysis would help identify potential weaknesses and areas for improvement, and would provide a more comprehensive understanding of the model's applicability.

To further enhance the paper, the authors should provide a more detailed analysis of the types of theorems and definitions that Graph2Tac can effectively handle. This analysis should go beyond simply reporting overall performance metrics and should delve into the specific characteristics of the theorems and definitions that the model finds challenging or easy to prove. For example, the authors could categorize the theorems based on their complexity, the number of premises, or the types of tactics used in their proofs. This would help identify the types of theorems that require further research and development. Furthermore, the authors should investigate the model's ability to generalize to new definitions and theorems that are significantly different from those seen during training. This could involve testing the model on theorems that require novel proof strategies or that combine multiple concepts in a non-trivial way. Such an analysis would provide a more nuanced understanding of the model's capabilities and limitations. The authors should also consider providing examples of theorems that the model can prove and those that it struggles with, along with a discussion of the reasons for these differences.

Finally, the paper would benefit from a more comprehensive comparison with other state-of-the-art theorem proving methods. While the authors compare their approach with CoqHammer, k-NN, and Transformer-GPU, they should also consider comparing with other relevant methods, such as those based on reinforcement learning or interactive theorem proving. This would provide a more complete picture of the current state of the art and help to position the proposed model within the broader context of theorem proving research. For example, the authors could compare their approach with methods that use large language models for theorem proving or with methods that use interactive theorem proving techniques to guide the search for proofs. This would help to highlight the unique strengths and weaknesses of Graph2Tac and would provide a more comprehensive evaluation of its potential. The authors should also discuss the trade-offs between different approaches, such as the computational cost, the interpretability of the model, and the level of human involvement required.

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
