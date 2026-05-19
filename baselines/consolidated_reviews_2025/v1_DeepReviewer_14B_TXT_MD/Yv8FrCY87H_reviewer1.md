### Summary

The paper introduces a Tree-of-Table method to enhance large language models (LLMs) for large-scale table understanding tasks. This approach employs Table Condensation and Decomposition to distill and reorganize relevant data into a manageable format, followed by the construction of a hierarchical Table-Tree that facilitates tree-structured reasoning. The authors evaluate the method on multiple benchmarks, and the results show that Tree-of-Table sets a new benchmark with superior performance.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and the motivation is reasonable.
2. The paper is well-written and easy to understand.
3. The authors conduct multiple experiments to evaluate the performance of Tree-of-Table and show that it achieves SOTA results.

### Weaknesses

#### Some Related Works


#### comment

1. The authors mention that the Tree-of-Table method is intended to address the challenges posed by large-scale relational tables for LLMs, but the tables in the evaluated datasets are not large in scale, especially for WikiTQ and TabFact.
2. The authors evaluate the method on multiple LLMs, but they only provide the results for LLaMA 2 in Table 4. It would be better to provide results for other LLMs as well.
3. The paper lacks a failure analysis, which would provide insights into the limitations of the proposed method.

### Suggestions

The paper would benefit from a more rigorous evaluation of the proposed Tree-of-Table method on datasets that truly represent large-scale relational tables. While the method is motivated by the challenges of such tables, the experiments on WikiTQ and TabFact do not adequately demonstrate its effectiveness in this context. These datasets are relatively small and do not fully capture the complexities of real-world large-scale relational data. To strengthen the paper, the authors should consider evaluating their method on datasets with a significantly larger number of rows and columns, as well as more complex relationships between tables. This would provide a more compelling demonstration of the method's ability to handle the intended use case. Furthermore, the evaluation should include a detailed analysis of the method's performance with respect to the size of the tables, showing how the performance scales as the table size increases. This would provide a more nuanced understanding of the method's strengths and limitations.

To address the lack of comprehensive results across different LLMs, the authors should provide a more detailed analysis of the method's performance on various models. While the paper mentions experiments with multiple LLMs, the detailed results are only provided for LLaMA 2. It is crucial to understand how the method performs on other models, such as GPT-3.5 and PaLM2, to assess its generalizability and robustness. The authors should include a comparative analysis of the method's performance across these models, highlighting any differences in performance and providing insights into the reasons behind these differences. This would also help to identify the specific characteristics of LLMs that are most suitable for the proposed method. Additionally, the authors should explore the impact of different hyperparameter settings on the performance of the method for each LLM, to ensure that the method is optimized for each model.

Finally, the paper should include a detailed failure analysis to provide a deeper understanding of the method's limitations. This analysis should go beyond simply stating that the method fails in certain cases. Instead, it should provide a detailed explanation of the specific reasons why the method fails, including the types of questions or tables that pose the most challenges. For example, the authors could analyze the cases where the method fails to correctly identify the relevant columns or rows, or where it fails to correctly aggregate or compare data. This analysis should also include examples of the failure cases, along with a discussion of the underlying causes. This would provide valuable insights into the method's limitations and suggest potential directions for future research.

### Questions

1. What are the maximum depth and degree of the Table-Tree?
2. What are the main reasons for the method's failure? Are there any challenging questions that the method cannot address?

### Rating

5

### Confidence

3

**********
