### Summary

This paper introduces SPAR, a self-play framework designed to enhance the instruction-following capabilities of large language models (LLMs). SPAR uses a tree-search self-refinement process to create preference pairs, minimizing extraneous factors and focusing on key differences that drive effective learning. The framework iteratively trains an actor model to generate responses and a refiner model to evaluate and refine these responses. SPAR demonstrates significant improvements in instruction-following tasks, outperforming other self-improvement methods and even surpassing GPT-4-Turbo on the IFEval benchmark after three iterations. The authors also show that SPAR's performance scales effectively with increased model size and that test-time compute scaling can further enhance its capabilities.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel self-play framework, SPAR, that addresses the limitations of existing preference learning methods by focusing on key differences in responses rather than introducing extraneous factors.
- The paper demonstrates the effectiveness of SPAR through extensive experiments, showing significant improvements in instruction-following tasks and outperforming other self-improvement methods.
- The paper provides a thorough analysis of SPAR's performance, including ablation studies and comparisons with baseline methods, which strengthens the validity of its findings.
- The paper also explores the scalability of SPAR, showing that it can be effectively applied to larger models and that test-time compute scaling can further enhance its capabilities.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of SPAR, which could be a limiting factor for its practical application. Specifically, the paper lacks a breakdown of the time and resources required for each stage of the self-play process, including the tree search, refinement, and training of the actor and refiner models. This makes it difficult to assess the feasibility of deploying SPAR in resource-constrained environments.
- The paper does not explore the potential limitations of SPAR, such as its sensitivity to hyperparameter settings or its performance on more complex or ambiguous instructions. The paper should include a discussion on how the choice of the number of iterations, the size of the training dataset, and the specific tree search parameters might affect the final performance. Furthermore, the paper should investigate the model's behavior on instructions that are inherently difficult to follow or that involve nuanced interpretations.
- The paper does not provide a detailed comparison of SPAR with other self-play methods, such as self-refinement or self-rewarding approaches. While the paper mentions that SPAR focuses on key differences, it does not provide a clear explanation of how this approach differs from other self-play methods in terms of the learning process and the resulting model behavior. A more thorough comparison, including a discussion of the advantages and disadvantages of each approach, would be beneficial.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with SPAR. This analysis should include a breakdown of the time and resources required for each stage of the self-play process, such as the tree search, refinement, and training of the actor and refiner models. The authors should also investigate how the computational cost scales with the size of the model and the number of iterations. This analysis should be presented in a way that allows readers to assess the feasibility of deploying SPAR in resource-constrained environments. Furthermore, the authors should explore potential optimizations to reduce the computational cost of SPAR, such as using more efficient tree search algorithms or reducing the number of refinement steps.

To address the potential limitations of SPAR, the authors should conduct a more thorough analysis of its sensitivity to hyperparameter settings and its performance on more complex or ambiguous instructions. This analysis should include a systematic exploration of the impact of different hyperparameters, such as the number of iterations, the size of the training dataset, and the specific tree search parameters, on the final performance. The authors should also investigate the model's behavior on instructions that are inherently difficult to follow or that involve nuanced interpretations. This could involve using a dataset with more challenging instructions or conducting a qualitative analysis of the model's responses to ambiguous instructions. The authors should also discuss the potential limitations of SPAR in these scenarios and suggest possible solutions.

Finally, the paper should include a more detailed comparison of SPAR with other self-play methods, such as self-refinement or self-rewarding approaches. This comparison should include a discussion of the advantages and disadvantages of each approach in terms of the learning process and the resulting model behavior. The authors should also discuss how SPAR's focus on key differences differs from other self-play methods and why this approach is more effective for instruction-following tasks. This comparison should be supported by empirical evidence, such as experiments that directly compare SPAR with other self-play methods on a range of instruction-following tasks.

### Questions

- How does the computational cost of SPAR scale with the size of the model and the number of iterations? Are there any optimizations that can be applied to reduce the computational cost?
- How sensitive is SPAR to the choice of hyperparameters, such as the number of iterations or the size of the training dataset? Are there any guidelines for selecting optimal hyperparameters for different tasks?
- How does SPAR perform on more complex or ambiguous instructions? Are there any limitations or challenges in applying SPAR to such instructions?
- How does SPAR compare to other self-play methods, such as self-refinement or self-rewarding approaches, in terms of learning efficiency and final performance?

### Rating

6

### Confidence

3

**********
