### Summary

The paper presents Tree-of-Table, a novel approach designed to enhance large language models' (LLMs) reasoning capabilities over large and complex tables. The method employs Table Condensation and Decomposition to distill and reorganize relevant data into a manageable format, followed by the construction of a hierarchical Table-Tree that facilitates tree-structured reasoning. The authors demonstrate the effectiveness of their approach on several datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed Tree-of-Table method is novel and well-designed to handle large-scale tables. The use of Table Condensation and Decomposition to distill and reorganize relevant data is a valuable contribution.
2. The authors conduct extensive experiments on multiple datasets to demonstrate the effectiveness of their approach. The results show that Tree-of-Table outperforms existing methods in terms of both accuracy and efficiency.
3. The paper is well-written and easy to follow. The authors provide clear explanations of their method and experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method still relies on the LLM's ability to perform reasoning and may be limited by the model's capabilities. The authors should discuss this limitation and potential solutions in more detail.
2. The authors should provide more details about the implementation of their method, such as the specific prompts used for each step and the hyperparameter settings. This would make it easier for other researchers to reproduce their results and build upon their work.
3. The authors should also discuss the potential limitations of their method, such as its performance on very large tables or its ability to handle complex reasoning tasks. This would provide a more balanced view of the method's strengths and weaknesses.

### Suggestions

The paper introduces a novel approach, Tree-of-Table, for enhancing LLMs' reasoning capabilities over large and complex tables. While the method shows promising results, several aspects could be improved to strengthen the paper. First, the reliance on the LLM's inherent reasoning capabilities is a significant limitation. The authors should delve deeper into how the method's performance is affected by the choice of LLM, including its size, architecture, and training data. For instance, how does the method perform with smaller, less capable LLMs, and what are the trade-offs between computational cost and reasoning accuracy? A more detailed analysis of the LLM's impact on the overall performance is needed. Furthermore, the authors should explore potential solutions to mitigate this dependency, such as incorporating external knowledge sources or using techniques like chain-of-thought prompting to improve the LLM's reasoning process within the Tree-of-Table framework. This would provide a more robust and generalizable approach.

Second, the paper lacks crucial implementation details that are necessary for reproducibility. The authors should provide specific examples of the prompts used for each step of the Tree-of-Table method, including the exact wording and any specific formatting requirements. This is particularly important for the table condensation and decomposition stages, where the prompts directly influence the quality of the distilled data. Additionally, the authors should specify the hyperparameter settings used for the LLM, such as the temperature, top-p, and any other relevant parameters. This information is essential for other researchers to replicate the results and build upon the proposed method. The authors should also clarify the specific hardware and software environment used for their experiments, including the type of GPUs, the version of the LLM library, and any other relevant dependencies. This level of detail is crucial for ensuring the reproducibility of the research.

Finally, the paper should include a more thorough discussion of the method's limitations. The authors should analyze the performance of the method on very large tables, exploring how the method's efficiency and accuracy are affected as the table size increases. This analysis should include a discussion of the computational cost of the method, especially in terms of memory usage and processing time. Furthermore, the authors should investigate the method's ability to handle complex reasoning tasks that require multiple steps of inference or the integration of information from multiple tables. This analysis should include a discussion of the types of reasoning tasks that the method is well-suited for and those where it may struggle. This would provide a more balanced view of the method's strengths and weaknesses and help guide future research in this area.

### Questions

1. How does the Tree-of-Table method compare to other table reasoning methods that do not rely on LLMs?
2. How does the method handle tables with missing or inconsistent data?
3. How does the method perform on tables with different structures, such as hierarchical tables or tables with complex relationships between columns?

### Rating

6

### Confidence

3

**********
