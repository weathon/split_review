### Summary

The paper introduces SPaR, a self-play framework that enhances LLMs' ability to follow complex instructions. Unlike conventional methods that sample independent responses, SPaR uses tree-search for self-refinement, creating more effective preference pairs for training. In experiments, a LLaMA3-8B model trained with SPaR surpasses GPT-4-Turbo on the IFEval benchmark, while maintaining general capabilities and demonstrating promising scalability with larger models like LLaMA3-70B. The authors also analyze the impact of inference scaling on model performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-structured, with clear explanations of the SPaR framework, including its components like tree-search refinement and iterative training.
2. The proposed SPaR framework is novel, using tree-search to generate comparable preference pairs, which reduces irrelevant variations and enhances focus on key differences in instruction-following.
3. The paper demonstrates SPaR's effectiveness through extensive experiments on multiple models and benchmarks, showing improvements in instruction-following without degrading general capabilities.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of SPaR's computational efficiency. Given that SPaR involves iterative training and tree-search refinement, it would be helpful to understand the computational costs associated with the framework, especially in comparison to other methods. Specifically, the paper should provide a breakdown of the FLOPs required for each stage of the SPaR framework, including the tree search, refinement, and training phases. This should include the computational cost of the BFS and DFS strategies, and how these costs scale with the number of iterations and the size of the language model. Furthermore, the paper should quantify the inference time scaling when using tree search during inference, comparing it to standard greedy decoding.
2. While the paper demonstrates SPaR's effectiveness on instruction-following tasks, it would be beneficial to see an analysis of how well the framework generalizes to other NLP tasks beyond instruction-following. The current evaluation focuses primarily on instruction-following benchmarks. It is unclear how SPaR would perform on tasks such as text summarization, machine translation, or question answering, which have different characteristics and requirements. The paper should include experiments on a broader range of NLP tasks to demonstrate the generalizability of the proposed framework.

### Suggestions

The paper should include a detailed analysis of the computational costs associated with the SPaR framework. This analysis should include a breakdown of the FLOPs required for each stage of the framework, such as tree search, refinement, and training. The authors should provide a comparison of the computational costs of SPaR with other methods, including a discussion of how these costs scale with the number of iterations and the size of the language model. Furthermore, the paper should quantify the inference time scaling when using tree search during inference, comparing it to standard greedy decoding. This analysis should include a comparison of the computational costs of the BFS and DFS strategies used in the tree search. This detailed analysis will help readers understand the practical implications of using SPaR and its resource requirements, which is crucial for assessing the feasibility of the approach.

To demonstrate the generalizability of the SPaR framework, the authors should include experiments on a broader range of NLP tasks beyond instruction-following. This could include tasks such as text summarization, machine translation, and question answering. The paper should analyze the performance of SPaR on these tasks and compare it to existing methods. This analysis should include a discussion of the strengths and weaknesses of SPaR on different types of tasks, and how the framework can be adapted to different task settings. This will help readers understand the applicability of SPaR to different NLP problems and its potential for broader impact.

Finally, the paper should provide a more detailed explanation of the tree search algorithm used in SPaR. This should include a discussion of the specific implementation details of the BFS and DFS strategies, and how these strategies are used to generate comparable preference pairs. The paper should also discuss the criteria used to determine when to stop the tree search, and how this stopping criterion affects the quality of the generated preference pairs. A more detailed explanation of the tree search algorithm will help readers understand the inner workings of SPaR and its key design choices.

### Questions

1. Could the authors provide more details on the computational requirements of SPaR, especially in comparison to other methods?
2. How does SPaR perform on tasks outside of instruction-following?

### Rating

6

### Confidence

3

**********
