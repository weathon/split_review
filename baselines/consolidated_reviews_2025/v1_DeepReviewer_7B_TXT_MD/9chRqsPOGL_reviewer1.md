### Summary

This paper proposes a self-play framework, SPAR, to improve the instruction-following capabilities of LLMs. SPAR integrates tree-search self-refinement to yield valid and comparable preference pairs for preference learning. SPAR shows promising results after three iterations, surpassing GPT-4-Turbo on the IFEval benchmark without losing general capabilities.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The motivation is clear and the method is well-motivated. 
- The experimental results show promising performance after three iterations, surpassing GPT-4-Turbo on the IFEval benchmark without losing general capabilities.

### Weaknesses

#### Some Related Works


#### comment

 - The paper claims that previous methods sample multiple independent responses from the model to construct preference pairs. However, the paper does not provide a detailed comparison of the proposed method with previous methods, nor does it discuss the advantages of the proposed method.
- The paper lacks a comparison of the proposed method with other self-improvement methods, such as Self-Instruct and Reinforced Self-Training.
- The paper does not provide a detailed explanation of the taxonomy-based prompt construction method, which is a key component of the proposed method.
- The paper does not provide a detailed explanation of the tree-search refinement method, which is another key component of the proposed method.
- The paper does not provide a detailed explanation of the judgment and refinement capabilities of the refiner, which is another key component of the proposed method.
- The paper does not provide a detailed explanation of the training data, which is another key component of the proposed method.
- The paper does not provide a detailed explanation of the training process, which is another key component of the proposed method.
- The paper does not provide a detailed explanation of the evaluation metrics, which is another key component of the proposed method.
- The paper does not provide a detailed explanation of the evaluation benchmarks, which is another key component of the proposed method.
- The paper does not provide a detailed explanation of the limitations of the proposed method.
- The paper does not provide a detailed explanation of the future work.

### Suggestions

The paper needs to provide a more thorough comparison with existing self-improvement methods. While the authors mention that previous methods sample multiple independent responses, they do not elaborate on the specific limitations of this approach, nor do they provide a detailed analysis of how their method addresses these limitations. A more detailed discussion of the advantages of the proposed method over existing methods is needed. For example, the authors could discuss the computational cost of sampling multiple responses versus the tree-search refinement approach, and how this impacts the scalability of the method. Furthermore, the paper should include a more comprehensive comparison with other self-improvement techniques, such as Self-Instruct and Reinforced Self-Training, to demonstrate the novelty and effectiveness of the proposed approach. This comparison should not only focus on performance metrics but also on other aspects such as data efficiency and computational resources.

The paper should provide a more detailed explanation of the taxonomy-based prompt construction method. The authors should explain how the taxonomy is constructed, how it is used to generate diverse and complex prompts, and how this approach ensures that the generated prompts are relevant to the instruction-following task. A concrete example of how the taxonomy is used to construct a prompt would be beneficial. Additionally, the paper should provide a more detailed explanation of the tree-search refinement method. The authors should explain how the tree search is performed, how the refinement process is guided, and how the method ensures that the refined responses are accurate and faithful to the original instructions. The paper should also discuss the computational cost of the tree search and how it impacts the overall efficiency of the method. Furthermore, the paper should provide a more detailed explanation of the judgment and refinement capabilities of the refiner. The authors should explain how the refiner is trained, how it is able to evaluate the quality of the responses, and how it is able to refine the responses to improve their accuracy and faithfulness to the instructions. The paper should also discuss the limitations of the refiner and how these limitations might impact the overall performance of the method.

Finally, the paper should provide a more detailed explanation of the training data, the training process, the evaluation metrics, and the evaluation benchmarks. The authors should explain how the training data is collected and preprocessed, how the training process is conducted, what metrics are used to evaluate the performance of the model, and which benchmarks are used to assess the instruction-following capabilities of the model. The paper should also discuss the limitations of the evaluation metrics and how these limitations might impact the conclusions of the paper. Furthermore, the paper should provide a more detailed explanation of the limitations of the proposed method and suggest directions for future work. This discussion should include potential areas for improvement and future research directions that could address the limitations of the proposed method.

### Questions

- How does the proposed method compare to other self-improvement methods?
- How does the proposed method address the limitations of previous methods?
- How does the proposed method ensure the quality of the generated preference pairs?
- How does the proposed method ensure the generalizability of the model?
- How does the proposed method ensure the robustness of the model?
- How does the proposed method ensure the fairness of the evaluation?
- How does the proposed method ensure the reproducibility of the results?

### Rating

5

### Confidence

4

**********
