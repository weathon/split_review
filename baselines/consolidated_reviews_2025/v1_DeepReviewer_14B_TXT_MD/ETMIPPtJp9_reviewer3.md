### Summary

This paper proposes a retrieval-augmented reasoning method, FiDeLiS, to enhance knowledge graph question answering by anchoring responses to structured, verifiable reasoning paths. The method includes a keyword-enhanced retrieval mechanism to fetch relevant entities and relations from a vector-based index of KGs, and a Deductive-Verification Beam Search (DVBS) to generate multiple reasoning paths. The method outperforms established baselines across three datasets, demonstrating its effectiveness in improving the reliability and interpretability of LLM reasoning in KGQA.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is a training-free approach, which is a significant advantage in terms of computational efficiency and generalizability.
3. The method demonstrates superior performance compared to strong baselines across three datasets, highlighting its effectiveness in improving the reliability and interpretability of LLM reasoning in KGQA.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on the quality of the knowledge graph, which may not always be perfect or up-to-date. Errors or inconsistencies in the KG could propagate through the reasoning process, leading to incorrect answers. Specifically, the method's reliance on a vector-based index of the KG for retrieval means that any inaccuracies in the entity and relation embeddings within this index could lead to the retrieval of irrelevant or incorrect information, thereby compromising the entire reasoning process. Furthermore, the method does not explicitly address how to handle cases where the KG contains conflicting information, which could lead to ambiguous or incorrect reasoning paths.
2. The method's performance is heavily dependent on the quality of the initial keyword extraction. If the keywords are not representative of the query's intent, the retrieval process may fail to identify the relevant entities and relations, leading to poor performance. The paper does not provide a detailed analysis of the keyword extraction process, including the types of keywords that are most effective and the potential for keyword ambiguity. This lack of analysis makes it difficult to assess the robustness of the method to variations in keyword quality. Moreover, the method does not consider the potential for the LLM to generate its own keywords, which could be more effective than relying on a separate keyword extraction module.
3. The paper does not provide a detailed analysis of the computational cost associated with the proposed method, particularly in terms of the time and resources required for the retrieval and reasoning steps. The method's reliance on a vector-based index of the KG and the beam search algorithm could lead to significant computational overhead, especially for large KGs. The paper should include a detailed analysis of the time complexity of each step of the method, as well as empirical results on the runtime performance of the method on different datasets. This analysis should also consider the impact of the beam size on the computational cost and the trade-off between performance and efficiency.

### Suggestions

To address the limitations related to the quality of the knowledge graph, the authors should explore methods for incorporating uncertainty and confidence scores into the reasoning process. This could involve assigning confidence scores to the retrieved entities and relations based on their provenance or the reliability of the source. The method could also be enhanced by incorporating techniques for detecting and resolving inconsistencies within the KG, such as using graph embedding methods to identify conflicting information. Furthermore, the authors should investigate the use of multiple KGs or knowledge sources to mitigate the impact of errors or inconsistencies in a single KG. This could involve combining information from different KGs using a weighted average or a more sophisticated fusion technique. The authors should also consider incorporating a mechanism for identifying and handling cases where the KG does not contain the necessary information to answer a query, such as using a fallback mechanism or a query reformulation technique.

To improve the robustness of the method to variations in keyword quality, the authors should conduct a more detailed analysis of the keyword extraction process. This analysis should include an evaluation of the types of keywords that are most effective for different types of queries, as well as an assessment of the potential for keyword ambiguity. The authors should also explore the use of LLMs to generate keywords directly from the query, which could be more effective than relying on a separate keyword extraction module. This could involve prompting the LLM to generate a set of keywords that are relevant to the query, and then using these keywords to retrieve entities and relations from the KG. The authors should also consider incorporating a mechanism for filtering out irrelevant or ambiguous keywords, such as using a semantic similarity measure or a keyword ranking algorithm. Furthermore, the authors should investigate the use of techniques for expanding the initial set of keywords, such as using a knowledge graph to identify related concepts or entities.

To address the lack of analysis of the computational cost, the authors should provide a detailed analysis of the time complexity of each step of the method, including the retrieval, reasoning, and scoring steps. This analysis should consider the impact of the beam size on the computational cost, as well as the size of the knowledge graph and the number of candidate reasoning paths. The authors should also provide empirical results on the runtime performance of the method on different datasets, including a comparison of the runtime performance of the method with different beam sizes. This analysis should also consider the trade-off between performance and efficiency, and provide guidance on how to choose the optimal beam size for different applications. The authors should also investigate the use of techniques for optimizing the computational cost of the method, such as using indexing techniques to speed up the retrieval process or using pruning techniques to reduce the number of candidate reasoning paths.

### Questions

1. How does the method handle cases where the knowledge graph contains errors or inconsistencies?
2. How does the method perform when the initial keyword extraction is not accurate or representative of the query's intent?
3. Can the method be extended to handle more complex reasoning tasks that require multiple hops or more intricate logical inferences?
4. How does the method compare to other retrieval-augmented reasoning methods in terms of computational efficiency and scalability?
5. What are the limitations of the method, and how can they be addressed in future work?

### Rating

6

### Confidence

4

**********
