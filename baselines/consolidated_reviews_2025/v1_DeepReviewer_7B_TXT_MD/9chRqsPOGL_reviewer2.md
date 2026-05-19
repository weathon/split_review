### Summary

This paper introduces a self-play framework, SPAR, which integrates tree-search self-refinement to yield valid and comparable preference pairs for preference learning. SPAR shows promising results after three iterations, surpassing GPT-4-Turbo on the IFEval benchmark without losing general capabilities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper is well-written and easy to follow.
2. The proposed method is simple yet effective. The experimental results show that the proposed method outperforms baselines.

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

The paper would benefit from a more detailed explanation of the taxonomy-based prompt construction method. Specifically, the authors should elaborate on the process of selecting and combining constraints to form the taxonomy. For example, how are the constraints chosen, and what criteria are used to ensure that they are diverse and relevant? What is the structure of the taxonomy, and how does it ensure comprehensive coverage of complex instructions? Providing concrete examples of how different constraints are combined would also be beneficial. Furthermore, the paper should discuss the limitations of the taxonomy and how these limitations might affect the performance of the proposed method. A more detailed explanation of the taxonomy would significantly improve the clarity and reproducibility of the proposed method.

The paper should also provide a more detailed explanation of the tree-search refinement method. The authors should clarify the specific criteria used to evaluate the quality of refined responses at each node in the tree. For example, what metrics are used to determine if a refinement is better than the original response? How does the tree search explore the search space, and what is the branching factor? What is the depth of the tree, and how does this affect the computational cost of the method? A more detailed explanation of the tree search algorithm would help the reader understand the method and its potential limitations. Additionally, the paper should discuss the computational cost of the tree search and how it scales with the complexity of the instructions.

Finally, the paper should provide a more detailed explanation of the judgment and refinement capabilities of the refiner. The authors should provide more details on the training data and the evaluation metrics used for the refiner. For example, what is the size of the training dataset, and what are the specific metrics used to evaluate the refiner's judgment accuracy? How does the refiner ensure that the refinement process is faithful to the original instruction? What are the limitations of the refiner, and how might these limitations affect the overall performance of the proposed method? A more detailed explanation of the refiner would help the reader understand the method and its potential limitations. The paper should also discuss the potential biases in the refiner and how these biases might affect the results.

### Questions

See the weakness part.

### Rating

5

### Confidence

4

**********
