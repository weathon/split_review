### Summary

This paper proposes a retrieval-augmented reasoning method, FiDeLiS, to enhance knowledge graph question answering by anchoring responses to structured, verifiable reasoning paths. The method consists of two main components: Path-RAG, which retrieves chain of entities and relations from KGs, and Deductive-Verification Beam Search (DVBS), which conducts deductive-reasoning-based beam search to generate multiple reasoning paths leading to final answers. The method outperforms existing strong baselines in three datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is a training-free approach, which is a significant advantage in terms of computational efficiency and generalizability.
2. The method demonstrates superior performance compared to strong baselines across three datasets, highlighting its effectiveness in improving the reliability and interpretability of LLM reasoning in KGQA.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on the quality of the knowledge graph, which may not always be perfect or up-to-date. Errors or inconsistencies in the KG could propagate through the reasoning process, leading to incorrect answers.
2. The method's performance is heavily dependent on the quality of the initial keyword extraction. If the keywords are not representative of the query's intent, the retrieval process may fail to identify the relevant entities and relations, leading to poor performance.
3. The paper does not provide a detailed analysis of the computational cost associated with the proposed method, particularly in terms of the time and resources required for the retrieval and reasoning steps.

### Suggestions

To mitigate the reliance on a perfect knowledge graph, the authors should explore methods for incorporating uncertainty and confidence scores into the reasoning process. This could involve assigning confidence scores to the retrieved entities and relations based on their provenance or the reliability of the source. Furthermore, the method could be enhanced by incorporating techniques for detecting and resolving inconsistencies within the KG, such as using graph embedding methods to identify conflicting information. The authors should also consider incorporating a mechanism for identifying and handling cases where the KG does not contain the necessary information to answer a query, such as using a fallback mechanism or a query reformulation technique. This would make the method more robust to incomplete or inaccurate KGs.

To improve the robustness of the method to variations in keyword quality, the authors should conduct a more detailed analysis of the keyword extraction process. This analysis should include an evaluation of the types of keywords that are most effective for different types of queries, as well as an assessment of the potential for keyword ambiguity. The authors should also explore the use of LLMs to generate keywords directly from the query, which could be more effective than relying on a separate keyword extraction module. This could involve prompting the LLM to generate a set of keywords that are relevant to the query, and then using these keywords to retrieve entities and relations from the KG. The authors should also consider incorporating a mechanism for filtering out irrelevant or ambiguous keywords, such as using a semantic similarity measure or a keyword ranking algorithm. Furthermore, the authors should investigate the use of techniques for expanding the initial set of keywords, such as using a knowledge graph to identify related concepts or entities.

To address the lack of analysis of the computational cost, the authors should provide a detailed analysis of the time complexity of each step of the method, including the retrieval, reasoning, and scoring steps. This analysis should consider the impact of the beam size on the computational cost, as well as the size of the knowledge graph and the number of candidate reasoning paths. The authors should also provide empirical results on the runtime performance of the method on different datasets, including a comparison of the runtime performance of the method with different beam sizes. This analysis should also consider the trade-off between performance and efficiency, and provide guidance on how to choose the optimal beam size for different applications. The authors should also investigate the use of techniques for optimizing the computational cost of the method, such as using indexing techniques to speed up the retrieval process or using pruning techniques to reduce the number of candidate reasoning paths.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
