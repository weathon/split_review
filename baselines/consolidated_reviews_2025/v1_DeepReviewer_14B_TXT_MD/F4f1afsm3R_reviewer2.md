### Summary

The paper proposes SC-MCTS, a novel Monte Carlo Tree Search (MCTS) reasoning algorithm for Large Language Models (LLMs). The authors address the challenges of MCTS's dependence on reward model performance and its slower speed compared to Chain of Thought (CoT). They introduce a highly interpretable reward model based on contrastive decoding and achieve a 51.9% speed improvement per node using speculative decoding. Additionally, they improve the UCT node selection strategy and backpropagation, resulting in a 17.4% performance improvement over the o1-mini model on the Blocksworld dataset with Llama-3.1-70B.

### Soundness

2

### Presentation

1

### Contribution

2

### Strengths

1. The paper presents a novel reward model based on contrastive decoding, which is interpretable and doesn't require external tools, training, or datasets.

2. The paper achieves a significant speed improvement of 51.9% per node using speculative decoding, which is crucial for practical applications of MCTS in LLMs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's experimental evaluation is limited to the Blocksworld dataset, which raises concerns about the generalizability of the proposed method to other multi-step reasoning tasks. The Blocksworld environment, while useful for testing basic planning and reasoning, does not fully capture the complexities of real-world scenarios or more diverse reasoning challenges. The lack of evaluation on datasets with varying reasoning structures, such as those involving temporal reasoning, common-sense reasoning, or mathematical problem-solving, makes it difficult to assess the robustness of the proposed SC-MCTS algorithm.

2. The paper lacks a detailed analysis of the computational cost and resource requirements of the proposed method. While the authors mention a speed improvement per node, they do not provide a comprehensive analysis of the overall computational overhead, including memory usage and the impact of the reward model and speculative decoding on the total runtime. This makes it difficult to assess the practical feasibility of the method, especially when considering the computational demands of large language models. A detailed breakdown of the time spent on each component of the algorithm, such as node selection, expansion, simulation, and backpropagation, would be beneficial.

3. The paper's presentation could be improved. Some sections, particularly the description of the reward model and the experimental setup, are dense and difficult to follow. The lack of clear explanations and examples makes it challenging for readers to fully understand the proposed method and its implementation details. The paper would benefit from a more structured presentation, with clear definitions of key concepts and more intuitive explanations of the algorithm's steps.

### Suggestions

To address the limitations in generalizability, the authors should evaluate their SC-MCTS algorithm on a more diverse set of datasets that cover a wider range of reasoning tasks. This should include datasets that involve different types of reasoning, such as temporal reasoning, common-sense reasoning, and mathematical problem-solving. For example, datasets like the ARC challenge, which involves visual reasoning, or the MATH dataset, which focuses on mathematical problem-solving, could provide a more comprehensive evaluation of the algorithm's capabilities. Furthermore, the authors should analyze the performance of SC-MCTS across these datasets to identify any specific strengths or weaknesses of the approach. This would provide a more robust assessment of the algorithm's generalizability and its potential for real-world applications. The analysis should also include a discussion of any modifications or adaptations that might be necessary to apply SC-MCTS to different types of reasoning tasks.

To address the lack of detailed computational analysis, the authors should provide a comprehensive breakdown of the computational cost of their method, including memory usage, the time spent on each component of the algorithm, and the impact of the reward model and speculative decoding on the total runtime. This analysis should include a comparison with other MCTS-based methods and Chain of Thought approaches, providing a clear understanding of the trade-offs between performance and computational cost. The authors should also investigate the scalability of their method with respect to the size of the language model and the complexity of the reasoning task. This would help to identify the practical limitations of the approach and guide future research in this area. The analysis should also consider the impact of different hardware configurations on the performance of the algorithm.

To improve the presentation of the paper, the authors should provide a more structured and intuitive explanation of their method. This should include clear definitions of key concepts, such as the contrastive decoding reward model and the speculative decoding process, and more detailed examples of how the algorithm works in practice. The authors should also consider using diagrams or flowcharts to illustrate the different steps of the algorithm and the flow of information. The experimental setup should be described in more detail, including the specific hyperparameters used and the rationale behind their choices. This would make the paper more accessible to a wider audience and facilitate the reproducibility of the results. The authors should also consider adding an appendix with additional details and examples to further clarify the method.

### Questions

1. How does the proposed method perform on other multi-step reasoning datasets beyond Blocksworld? Are there any plans to evaluate the method on a more diverse set of tasks to assess its generalizability?

2. What is the computational cost of the proposed method compared to other MCTS-based methods and Chain of Thought approaches? How does the reward model and speculative decoding affect the overall runtime and resource requirements?

3. Can the authors provide more details on the implementation of the contrastive decoding reward model and the speculative decoding process? How were these components integrated into the MCTS framework?

### Rating

3

### Confidence

3

**********
