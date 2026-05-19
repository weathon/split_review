### Summary

The paper proposes a Tree-of-Table method to enhance LLMs' reasoning capabilities over large and complex tables. The method employs Table Condensation and Decomposition to distill and reorganize relevant data into a manageable format, followed by the construction of a hierarchical Table-Tree that facilitates tree-structured reasoning. The authors demonstrate the effectiveness of their approach on several datasets.

### Soundness

2

### Presentation

3

### Contribution

2

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

The paper would benefit from a more thorough discussion of the limitations imposed by the underlying large language model (LLM). While the Tree-of-Table method introduces a novel approach to handling tabular data, its performance is inherently tied to the reasoning capabilities of the chosen LLM. The authors should explore how the method's performance varies across different LLMs, including models with varying sizes and architectures. For example, it would be valuable to analyze the method's sensitivity to the context window size of the LLM, especially when dealing with large tables that may require truncation or summarization. Furthermore, the authors should investigate the impact of the LLM's training data on the method's performance, particularly in cases where the table data is from a domain not well-represented in the LLM's training corpus. A detailed analysis of these factors would provide a more comprehensive understanding of the method's robustness and generalizability.

To enhance the reproducibility of the work, the authors should provide a more detailed description of the implementation. Specifically, the prompts used for each step of the Tree-of-Table method should be clearly specified, including the exact wording and any specific formatting requirements. The authors should also provide details about the hyperparameter settings used for the LLM, such as the temperature, top-p, and any other relevant parameters. Furthermore, the authors should describe the specific hardware and software environment used for their experiments, including the type of GPUs, the version of the LLM library, and any other relevant dependencies. This level of detail is crucial for other researchers to replicate the results and build upon the proposed method. The authors should also consider releasing their code and data to further facilitate reproducibility and adoption of their work.

Finally, the authors should delve deeper into the limitations of their method, particularly concerning its scalability and ability to handle complex reasoning tasks. The paper should include a discussion of the computational cost of the Tree-of-Table method, especially in terms of memory usage and processing time. The authors should also analyze the method's performance on very large tables, exploring how the method's efficiency and accuracy are affected as the table size increases. Furthermore, the authors should investigate the method's ability to handle complex reasoning tasks that require multiple steps of inference or the integration of information from multiple tables. This analysis should include a discussion of the types of reasoning tasks that the method is well-suited for and those where it may struggle. This would provide a more balanced view of the method's strengths and weaknesses and help guide future research in this area.

### Questions

1. How does the Tree-of-Table method compare to other table reasoning methods that do not rely on LLMs?

2. How does the method handle tables with missing or inconsistent data?

3. How does the method perform on tables with different structures, such as hierarchical tables or tables with complex relationships between columns?

### Rating

6

### Confidence

4

**********
