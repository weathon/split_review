### Summary

The paper introduces a novel method called FiDeLiS ( Faithful Reasoning in Large Language Model for Knowledge Graph Question Answering), which aims to enhance the reliability of large language models (LLMs) in generating accurate and verifiable reasoning paths for knowledge graph question answering. FiDeLiS addresses two main challenges: data sparsity and the complexity of query interpretation, by integrating a keyword-enhanced retrieval mechanism (Path-RAG) with a deductive-verification beam search (DVBS). The approach leverages structured knowledge from knowledge graphs (KGs) to guide LLM reasoning, ensuring that the generated reasoning paths are grounded in verifiable entities and relations. Through extensive experiments on three datasets, FiDeLiS demonstrates superior performance over state-of-the-art methods, achieving higher accuracy, generality, and computational efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. FiDeLiS introduces a novel approach to knowledge graph question answering by combining a keyword-enhanced retrieval mechanism with a deductive-verification beam search. This integration allows for more accurate and reliable reasoning paths compared to existing methods.
2. The paper provides extensive experimental results across multiple datasets, demonstrating that FiDeLiS outperforms established strong baselines in terms of accuracy, generality, and computational efficiency. The ablation studies further validate the effectiveness of each component of the proposed method.
3. The paper is well-structured and clearly written, making it accessible to a broad audience. The authors provide a detailed explanation of the methodology, including the Path-RAG and DVBS components, and the experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more in-depth discussion of the limitations of FiDeLiS, particularly in scenarios where the knowledge graph is incomplete or contains conflicting information. The current analysis does not sufficiently address how the method would perform under such conditions, which are common in real-world applications.
2. While the paper demonstrates the effectiveness of FiDeLiS on three datasets, it would be valuable to see how the method performs on a wider range of datasets, including those with different characteristics and complexities. The current evaluation is limited to datasets with relatively structured knowledge graphs, and it is unclear how the method would generalize to more unstructured or noisy data.
3. The computational efficiency claims of FiDeLiS are not fully supported by a detailed analysis of the computational complexity of the proposed method. The paper lacks a rigorous comparison of the computational costs of FiDeLiS with those of the baseline methods, especially in terms of memory usage and processing time. A more detailed analysis of the computational complexity of the Path-RAG and DVBS components would be beneficial.
4. The paper could provide more details on the sensitivity of FiDeLiS to the choice of hyperparameters, such as the beam size and the number of reasoning steps. The current analysis does not sufficiently explore how these parameters affect the performance of the method, and it is unclear how to choose the optimal values for different datasets.

### Suggestions

The paper should include a more thorough discussion of the limitations of FiDeLiS, particularly in scenarios where the knowledge graph is incomplete or contains conflicting information. The authors should explore how the method would perform under such conditions, which are common in real-world applications. For example, the paper could investigate the impact of missing entities or relations on the accuracy of the reasoning paths. Furthermore, the paper should discuss how the method would handle conflicting information within the knowledge graph, such as contradictory statements about the same entity. This analysis should include a discussion of potential strategies for mitigating the impact of incomplete or conflicting knowledge graphs, such as incorporating uncertainty measures or using ensemble methods to combine multiple reasoning paths.

To strengthen the empirical evaluation, the authors should consider expanding the range of datasets used to validate FiDeLiS. The current evaluation is limited to datasets with relatively structured knowledge graphs, and it is unclear how the method would generalize to more unstructured or noisy data. The authors should consider including datasets with more complex knowledge structures, such as those with hierarchical or relational data. Additionally, the paper should include a more detailed analysis of the performance of FiDeLiS on different types of questions, such as those that require multi-hop reasoning or those that involve complex logical operations. This analysis should include a discussion of the strengths and weaknesses of the method for different types of questions, and it should provide insights into how the method could be improved for more challenging tasks.

The paper should provide a more detailed analysis of the computational complexity of FiDeLiS, including a rigorous comparison of the computational costs of FiDeLiS with those of the baseline methods. The authors should provide a breakdown of the computational costs of the Path-RAG and DVBS components, and they should discuss how these costs scale with the size of the knowledge graph and the length of the reasoning paths. Furthermore, the paper should include a more detailed analysis of the sensitivity of FiDeLiS to the choice of hyperparameters, such as the beam size and the number of reasoning steps. The authors should provide a discussion of how these parameters affect the performance of the method, and they should provide guidelines for choosing the optimal values for different datasets. This analysis should include a discussion of the trade-offs between accuracy and computational efficiency, and it should provide insights into how the method could be optimized for different applications.

### Questions

1. How does FiDeLiS handle cases where the knowledge graph is incomplete or contains conflicting information? Are there any mechanisms in place to detect or mitigate the impact of such issues?
2. The paper mentions that FiDeLiS is computationally efficient. Could you provide a more detailed analysis of the computational complexity of FiDeLiS, especially in comparison to the baseline methods? How does the method scale with the size of the knowledge graph and the length of the reasoning paths?
3. The paper demonstrates the effectiveness of FiDeLiS on three datasets. How would the method perform on a wider range of datasets, including those with different characteristics and complexities? Are there any limitations to the types of datasets on which FiDeLiS can be effectively applied?
4. The paper discusses the use of a keyword-enhanced retrieval mechanism (Path-RAG) and a deductive-verification beam search (DVBS). Could you provide more details on the sensitivity of FiDeLiS to the choice of hyperparameters, such as the beam size and the number of reasoning steps? How do these parameters affect the performance of the method, and how should they be chosen for different datasets?

### Rating

6

### Confidence

4

**********
