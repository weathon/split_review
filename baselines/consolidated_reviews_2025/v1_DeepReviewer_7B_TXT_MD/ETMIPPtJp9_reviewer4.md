### Summary

This paper proposes a retrieval-augmented reasoning method for KGQA. The method first retrieves the entities and relations that are relevant to the query from the knowledge graph. Then it uses a beam search algorithm to generate the reasoning path. The authors evaluate the proposed method on three datasets and show that it outperforms the baseline methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and easy to understand.
2. The proposed method outperforms the baseline methods on three datasets.
3. The authors provide a detailed description of the proposed method and the experimental setup.

### Weaknesses

#### Some Related Works

[1] Retrieval-Augmented Generation for Large Language Models: A Survey.
[2] RAG-QA: A Survey on Retrieval-Augmented Generation for Question Answering.

#### comment

1. The proposed method is very similar to the existing retrieval-augmented reasoning methods [1,2]. The authors should discuss the differences between the proposed method and these existing methods.
2. The authors should provide more details about the baseline methods used in the experiments. For example, what are the specific architectures of the LLMs used in the baseline methods? What are the specific training data used for the LLMs? What are the specific hyperparameters used for the LLMs?
3. The authors should provide more details about the datasets used in the experiments. For example, what are the characteristics of the datasets? What are the evaluation metrics used for the datasets? What are the statistics of the datasets?
4. The authors should provide more analysis of the experimental results. For example, what are the reasons for the performance differences between the proposed method and the baseline methods? What are the limitations of the proposed method? What are the future directions for the proposed method?

### Suggestions

The paper would benefit from a more thorough comparison with existing retrieval-augmented reasoning methods. While the authors mention that their method uses a beam search for reasoning path generation, they should provide a more detailed analysis of how this differs from the beam search used in other methods. Specifically, they should discuss the differences in the search space, the scoring function used for beam selection, and the stopping criteria for the search. A more detailed comparison would help to clarify the novelty of the proposed approach and highlight its advantages over existing methods. Furthermore, the authors should discuss the computational complexity of their method compared to other retrieval-augmented reasoning methods. This would help to understand the trade-offs between performance and efficiency.

To strengthen the experimental evaluation, the authors should provide more details about the baseline methods. Specifically, they should specify the exact LLMs used (e.g., model name, version), the training data used for the LLMs, and the hyperparameters used for the LLMs. This information is crucial for reproducibility and for understanding the performance differences between the proposed method and the baseline methods. For example, if the baseline methods use a different LLM than the proposed method, this should be clearly stated. Additionally, the authors should provide details about the training data used for the LLMs, including the size of the training data and the data augmentation techniques used. This would help to understand the performance of the baseline methods and to identify potential biases.

Finally, the authors should provide more analysis of the experimental results. They should discuss the reasons for the performance differences between the proposed method and the baseline methods. For example, they should analyze the types of questions where the proposed method performs better or worse than the baseline methods. They should also discuss the limitations of the proposed method, such as its performance on specific types of questions or its sensitivity to the quality of the knowledge graph. Furthermore, the authors should discuss the future directions for the proposed method, such as how to improve its performance on more complex questions or how to make it more robust to noisy knowledge graphs. This would help to guide future research in this area.

### Questions

See Weaknesses.

### Rating

6

### Confidence

3

**********
