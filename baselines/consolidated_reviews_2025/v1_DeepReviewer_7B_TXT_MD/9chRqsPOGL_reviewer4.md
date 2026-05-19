### Summary

This paper proposes a self-play framework called SPAR, which iteratively trains an LLM to improve its instruction-following capabilities. SPAR addresses the issue of introducing irrelevant variations in preference pairs by using a tree-search self-refinement process. The authors demonstrate the effectiveness of SPAR through experiments on several benchmarks, showing that it outperforms other self-improvement methods and even surpasses GPT-4-Turbo on the IFEval benchmark.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective, and the experimental results show that it outperforms other self-improvement methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed explanation of the taxonomy-based prompt construction method. Specifically, it is unclear how the taxonomy is constructed, what specific criteria are used to define the categories, and how this structured approach ensures comprehensive coverage of complex instructions. The paper should elaborate on the process of selecting and combining constraints to form the taxonomy.
2. The paper does not provide a detailed explanation of the tree-search refinement method. It is unclear how the tree search is performed, what the branching factor represents, and how the search space is explored to find the optimal refinement. The paper should clarify the specific criteria used to evaluate the quality of refined responses at each node in the tree.
3. The paper does not provide a detailed explanation of the judgment and refinement capabilities of the refiner. It is unclear how the refiner is trained, what specific metrics are used to evaluate its judgment accuracy, and how it ensures that the refinement process is faithful to the original instruction. The paper should provide more details on the training data and the evaluation metrics used for the refiner.
4. The paper does not provide a detailed explanation of the training data. It is unclear how the training data is collected, what the size of the dataset is, and how the data is preprocessed before being used for training. The paper should provide more details on the data collection process and the preprocessing steps.
5. The paper does not provide a detailed explanation of the training process. It is unclear what the specific training algorithm is, what the hyperparameters are, and how the training is conducted. The paper should provide more details on the training procedure and the hyperparameter settings.
6. The paper does not provide a detailed explanation of the evaluation metrics. It is unclear what metrics are used to evaluate the performance of the model, and why these metrics are appropriate for the task. The paper should provide a clear definition of the evaluation metrics and justify their use.
7. The paper does not provide a detailed explanation of the evaluation benchmarks. It is unclear what benchmarks are used to evaluate the performance of the model, and why these benchmarks are appropriate for the task. The paper should provide a clear description of the benchmarks and justify their use.
8. The paper does not provide a detailed explanation of the limitations of the proposed method. It is unclear what the limitations of the method are, and what future directions could be explored to address these limitations. The paper should discuss the limitations of the proposed method and suggest potential avenues for future research.

### Suggestions

The paper would benefit from a more thorough explanation of the taxonomy-based prompt construction method. The authors should provide a detailed description of how the taxonomy is constructed, including the specific criteria used to define the categories. For example, if the taxonomy is based on semantic similarity, the paper should explain how semantic similarity is measured and how the categories are derived from this measure. Furthermore, the paper should clarify how the constraints are selected and combined to form the taxonomy. A concrete example of how different constraints are combined would be beneficial to illustrate the process. This would help the reader understand the structured approach and its potential for comprehensive coverage of complex instructions. Without this level of detail, it is difficult to assess the validity and generalizability of the proposed method.

The paper needs a more detailed explanation of the tree-search refinement method. The authors should clarify how the tree search is performed, including the branching factor and the search strategy. It is important to understand how the search space is explored and how the optimal refinement is found. The paper should also explain the specific criteria used to evaluate the quality of refined responses at each node in the tree. For example, is it based on a similarity metric, a reward signal, or some other measure? A clear explanation of these aspects is crucial for understanding the effectiveness of the refinement process. Furthermore, the paper should discuss the computational cost of the tree search and how it scales with the complexity of the instructions. This would help the reader understand the practical implications of the proposed method.

Finally, the paper should provide a more detailed explanation of the judgment and refinement capabilities of the refiner. The authors should describe how the refiner is trained, including the specific training data and the training algorithm. It is important to understand how the refiner is able to evaluate the quality of responses and provide feedback for refinement. The paper should also explain the specific metrics used to evaluate the judgment accuracy of the refiner. For example, is it based on a similarity metric, a reward signal, or some other measure? Furthermore, the paper should discuss the limitations of the refiner and how these limitations might affect the overall performance of the proposed method. A more detailed explanation of these aspects would help the reader understand the robustness and reliability of the proposed method.

### Questions

1. Could you provide a more detailed explanation of the taxonomy-based prompt construction method, including how the taxonomy is constructed, what specific criteria are used to define the categories, and how this structured approach ensures comprehensive coverage of complex instructions?
2. Could you provide a more detailed explanation of the tree-search refinement method, including how the tree search is performed, what the branching factor represents, and how the search space is explored to find the optimal refinement?
3. Could you provide a more detailed explanation of the judgment and refinement capabilities of the refiner, including how the refiner is trained, what specific metrics are used to evaluate its judgment accuracy, and how it ensures that the refinement process is faithful to the original instruction?
4. Could you provide a more detailed explanation of the training data, including how the training data is collected, what the size of the dataset is, and how the data is preprocessed before being used for training?
5. Could you provide a more detailed explanation of the training process, including what the specific training algorithm is, what the hyperparameters are, and how the training is conducted?
6. Could you provide a more detailed explanation of the evaluation metrics, including what metrics are used to evaluate the performance of the model, and why these metrics are appropriate for the task?
7. Could you provide a more detailed explanation of the evaluation benchmarks, including what benchmarks are used to evaluate the performance of the model, and why these benchmarks are appropriate for the task?
8. Could you provide a detailed explanation of the limitations of the proposed method, including what the limitations of the method are, and what future directions could be explored to address these limitations?

### Rating

6

### Confidence

4

**********
