### Summary

This paper proposes a graph neural network (GNN) model, Graph2Tac, for theorem proving in Coq. The model is trained on a graph-based dataset of Coq terms and definitions, and can adapt to new definitions and theorems in real-time. The authors compare their model with other symbolic and machine learning solvers, and show that Graph2Tac performs well in proving theorems in new Coq packages.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel graph neural network (GNN) model, Graph2Tac, for theorem proving in Coq. The model is trained on a graph-based dataset of Coq terms and definitions, and can adapt to new definitions and theorems in real-time. This is a significant contribution to the field of automated theorem proving, as it addresses the challenge of adapting to new concepts and definitions in a dynamic environment.
2. The authors provide a comprehensive comparison of Graph2Tac with other symbolic and machine learning solvers, including CoqHammer, k-NN, and Transformer-GPU. This comparison highlights the strengths and weaknesses of each approach and provides insights into the potential of GNNs for theorem proving.
3. The paper is well-written and organized, with clear explanations of the proposed model, the dataset, and the evaluation metrics. The authors also provide a detailed description of the experimental setup and the results, making it easy for readers to understand and replicate the findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as the computational cost of training and inference, the scalability of the model to larger datasets, and the generalizability of the model to different Coq environments.
2. The paper could also benefit from a more in-depth analysis of the types of theorems and definitions that Graph2Tac can effectively prove or adapt to. This would provide a better understanding of the strengths and weaknesses of the model and guide future research in this area.
3. The authors should also consider comparing their approach with other state-of-the-art theorem proving methods, such as those based on reinforcement learning or interactive theorem proving, to provide a more comprehensive evaluation of the proposed model.

### Suggestions

The paper would be significantly strengthened by a more thorough investigation into the computational aspects of the proposed Graph2Tac model. Specifically, the authors should provide a detailed analysis of the training and inference times, including how these scale with the size of the Coq dataset. This analysis should include a breakdown of the time spent on different stages of the training process, such as graph construction, model training, and inference. Furthermore, it would be beneficial to explore techniques for optimizing the model's performance, such as model pruning, quantization, or distributed training. This would make the model more practical for real-world applications and allow for a better understanding of its limitations. The authors should also discuss the memory requirements of the model, especially when dealing with large datasets, and explore strategies for reducing memory footprint.

In addition to computational aspects, a more in-depth analysis of the types of theorems and definitions that Graph2Tac can effectively handle is needed. The authors should categorize the theorems based on their complexity, the number of premises, or the types of tactics used in their proofs. This would provide a more nuanced understanding of the model's strengths and weaknesses. For example, it would be valuable to know if the model performs better on theorems that involve simple logical connectives or those that require more complex proof strategies. Furthermore, the authors should investigate the model's ability to generalize to new definitions and theorems that are significantly different from those seen during training. This could involve testing the model on theorems from different Coq libraries or those that require novel proof strategies. Such an analysis would provide valuable insights into the model's ability to adapt to new concepts and definitions.

Finally, the paper should include a more comprehensive comparison with other state-of-the-art theorem proving methods. While the comparison with CoqHammer, k-NN, and Transformer-GPU is a good starting point, it would be beneficial to include a comparison with other relevant approaches, such as those based on reinforcement learning or interactive theorem proving. This would provide a more complete picture of the current state of the art and help to position the proposed model within the broader context of theorem proving research. The authors should also discuss the trade-offs between different approaches, such as the computational cost, the interpretability of the model, and the level of human involvement required. This would provide a more balanced and nuanced evaluation of the proposed model and highlight its unique strengths and weaknesses.

### Questions

1. How does the proposed model scale to larger datasets and more complex Coq environments?
2. What are the computational resources required for training and inference, and how can they be optimized?
3. How does the model generalize to new definitions and theorems that are significantly different from those seen during training?
4. How does the proposed approach compare with other state-of-the-art theorem proving methods, such as those based on reinforcement learning or interactive theorem proving?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
