### Summary

This paper proposes FiDeLiS, a retrieval-augmented reasoning method for knowledge graph question answering. FiDeLiS first retrieves the entities and relations that are relevant to the query from the knowledge graph, then uses a beam search algorithm to generate the reasoning path. The authors evaluate FiDeLiS on three datasets and show that it outperforms the baseline methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The experiments are comprehensive and the results are promising.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the limitations of the proposed method. For example, how does the method perform on questions that require multi-hop reasoning or questions that involve rare entities or relations? It would be beneficial to see a more thorough discussion of the scenarios where FiDeLiS might struggle, such as when the knowledge graph is incomplete or when the query is ambiguous.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to see a comparison of the runtime and memory usage of FiDeLiS with the baseline methods. Specifically, a breakdown of the time spent on each stage of the method (retrieval, beam search, verification) would be valuable to understand the bottlenecks and potential areas for optimization. Furthermore, the paper should discuss the scalability of the method with respect to the size of the knowledge graph and the length of the reasoning paths.
3. The paper does not provide a detailed analysis of the error cases. It would be helpful to see examples of the types of errors that FiDeLiS makes and how these errors relate to the limitations of the method. For instance, are there specific types of queries or knowledge graph structures that are more likely to lead to errors? A qualitative analysis of the errors would provide valuable insights into the strengths and weaknesses of the method.

### Suggestions

The paper would benefit from a more in-depth analysis of the limitations of FiDeLiS. Specifically, the authors should investigate the performance of the method on questions that require multi-hop reasoning. This could involve creating a subset of the datasets that specifically target multi-hop questions and evaluating FiDeLiS on this subset. The analysis should also consider the impact of rare entities and relations on the performance of the method. It would be useful to see a breakdown of the performance based on the frequency of entities and relations in the knowledge graph. Furthermore, the authors should explore the robustness of the method to ambiguous queries. This could involve introducing ambiguity into the queries and evaluating the performance of FiDeLiS on these modified queries. A detailed analysis of these limitations would provide a more complete understanding of the capabilities and weaknesses of FiDeLiS.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the runtime and memory usage of FiDeLiS. This should include a comparison of the runtime and memory usage of FiDeLiS with the baseline methods. The authors should also provide a breakdown of the time spent on each stage of the method (retrieval, beam search, verification) to identify potential bottlenecks. Furthermore, the paper should discuss the scalability of the method with respect to the size of the knowledge graph and the length of the reasoning paths. This could involve evaluating the performance of FiDeLiS on knowledge graphs of varying sizes and with different path lengths. A thorough analysis of the computational cost would provide a more complete picture of the practical applicability of FiDeLiS.

Finally, the paper should include a detailed analysis of the error cases. This should involve a qualitative analysis of the types of errors that FiDeLiS makes and how these errors relate to the limitations of the method. For example, the authors should investigate whether the errors are more likely to occur when the knowledge graph is incomplete or when the query is ambiguous. It would also be helpful to see examples of the types of queries that are most challenging for FiDeLiS. A detailed analysis of the error cases would provide valuable insights into the strengths and weaknesses of the method and guide future research directions.

### Questions

1. How does the method perform on questions that require multi-hop reasoning?
2. How does the method perform on questions that involve rare entities or relations?
3. How does the method handle ambiguous queries?
4. What is the computational cost of the proposed method compared to the baseline methods?
5. What are the error cases of the proposed method?

### Rating

6

### Confidence

3

**********
