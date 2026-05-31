## Human Reviewer 1

### Summary
This paper systematically investigates when and why graph structures benefit retrieval-augmented generation systems, introducing **GraphRAG-Bench** to evaluate GraphRAG models across hierarchical knowledge retrieval and deep contextual reasoning, and providing empirical insights and guidelines for their practical application.

### Strengths
1. This paper addresses the key research question of when graph structures truly improve RAG performance.
2. This paper provides extensive experimental evidence through the new GraphRAG-Bench benchmark.
3. This paper offers concrete recommendations and design principles for advancing the GraphRAG community.

### Weaknesses
1. **The implementation details of the evaluation metrics are not clearly specified.** It seems that both *Faithfulness* and *Evidence Coverage* rely on external judgment models, such as *LLM-as-a-Judge*, but the paper does not disclose the exact implementation of this component.

2. **The scale of retrieved content among methods appears inconsistent**. According to Section H.2 *Configuration*, the retrieval strategies of RAG and different GraphRAG variants are not aligned—for example, RAG restricts the Top-K to 5. This inconsistency may affect the fairness of performance comparisons.

3. **The potential mechanisms through which *Graph Indexing content* influences various tasks deserve further study**. Statistics in Table 15 show that different GraphRAG strategies employ distinct types of indexed content, such as text chunks, communities, entities, and relationships. For instance, could the inclusion of *community* information better support *contextual summarization* tasks?

4. **How corpus characteristics affect the choice of GraphRAG remains an open question**. Although the paper thoroughly investigates when to use GraphRAG from the perspective of task properties and performance, Sections C.1 and D further discuss the traits of the selected *Medical* and *Novel* corpora, as well as the yet-unexplored *Legal* and *Financial* domains. Extending the study of "When to use GraphRAG" to domain-specific corpora would significantly strengthen the work.

### Questions
As discussed above in Weakness.

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes GraphRAG-Bench, a comprehensive benchmark for systematically evaluating GraphRAG models in terms of hierarchical knowledge retrieval and deep contextual reasoning. 

This benchmark covers both tightly structured domain data (medical data from NCCN guidelines) and loosely organized texts (novels from Gutenberg library), and focuses on 4 tasks with different difficulty levels, from easy to difficult, including fact retrieval, complex reasoning, contextual summarize, creative generation. This paper provides an evaluation framework with clear quantitative metrics that assesses graph construction, retrieval, and generation performance. 

This paper conducted extensive experiments to evaluate multiple GraphRAG methods against RAG, with GPT-4o-mini and Qwen-2.5-14B as base LLMs. The experiments show that GraphRAG outperforms RAG in complex reasoning, summarization, and creative tasks, while it does not hold an advantage in simple retrieval. Based on the experimental results, the paper offers practical guidelines, indicating that GraphRAG is suitable for multi-hop reasoning and knowledge integration tasks, while it is not applicable for single-step retrieval or latency-sensitive scenarios.

### Strengths
- This benchmark focuses on tasks with different difficulty levels, reflecting real-world scenarios demanding complex logical synthesis.
- This benchmark provides a comprehensive evaluation for GraphRAG with clear quantitative metrics, including graph structure, retrieval performance, efficiency, and final output quality.
- Based on thorough experiments across multiple GraphRAG methods, LLMs, and tasks, this paper offers clear and practical guidelines on when GraphRAG outperforms traditional RAG.

### Weaknesses
- The calculation process for some evaluation metrics is simplistic and unclear. For example, the paper does not explain how it determines whether a claim $c$ is supported by the context $C$ when calculating EVIDENCE RECALL and FAITHFULNESS.
- The process of Logic and Evidence Extraction is not clearly described either in the main text or the appendix. While the use of GPT-4.1 is mentioned, the specific extraction procedure and output format are not illustrated clearly.

### Questions
Refer to Weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper systematically investigates when graph-based retrieval augmentation (GraphRAG) surpasses traditional RAG, revealing that GraphRAG excels in complex reasoning and structured knowledge integration while RAG remains more efficient for simple retrieval tasks.

### Strengths
This work tackles the key open question of when graph-based retrieval truly benefits RAG systems, bridging a major gap in empirical understanding. Through dense, well-controlled experiments across domains and tasks, it provides strong, data-driven evidence supporting its conclusions and design insights.

### Weaknesses
1. The proposed four-level task hierarchy is claimed that task difficulty increases along the retrieval difficulty and reasoning complexity. However, this paper do not provide formal or operational definitions for these levels—there are no explicit thresholds for evidence quantity, reasoning steps, or context length that determine the boundaries between levels.

2. The benchmark does not disclose the absolute corpus size for the Novel and Medical datasets. Consequently, it remains unclear how GraphRAG’s performance scales with corpus size. Without controlled experiments across small, medium, and large datasets, the current results cannot confirm whether the observed improvements stem from the graph structure itself or from differences in data volume and density.

3. The paper does not empirically analyze how different indexing contents—such as entities, relationships, phrases, or communities—affect GraphRAG performance. Although Table 15 summarizes the indexing types used by various implementations, these differences are only descriptive and intertwined with other design factors like retrieval strategies and graph density.

4. The paper does not evaluate GraphRAG on time-sensitive or temporally evolving datasets. The current study’s exclusive focus on static corpora (medical guidelines and classical novels) means it cannot assess how graph-based retrieval performs under temporal drift or continuous knowledge refresh.

### Questions
As discussed above in weakness.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper discusses and tests the advantages and disadvantages of GraphRAG compared to vanilla RAG. To achieve this goal, the authors discusses the limitations of existing benchmarking datasets for GraphRAG/RAG-related systems and propose GraphRAG-Bench, a benchmark on knowledge retrieval and contextual reasoning. GraphRAG-Bench not only focus on testing a model’s ability to correctly retrieve necessary information, but also tests the model’s ability to reason in complex scenarios. It contains 4 types of tasks: Fact Retrieval, Contextual Summarize, Complex Reasoning and Creative Generation. The process of constructing the dataset is also introduced, with 6-steps - Corpus collection, Logical Mining, Evidence Collection, Question Generation, Check, and Refinement. With this benchmark, authors systematically checked the condition when a series of GraphRAG works.

### Strengths
1.	This paper studied a fundamental and important problem. GraphRAG is trending, demonstrating good motivation. The proposed benchmark provides rooms to systematically examine the advantage of different GraphRAG systems.  

2.	This manuscript identifies key limitations of existing RAG benchmarking datasets, including neglecting the evaluation of logical reasoning, limited corpus coverage, and focusing only on end results.

3.	Apart from general QA, the proposed benchmark includes a set of tasks, including Fact Retrieval, Contextual Summarize, Complex Reasoning and Creative Generation, which allows users to comprehensively evaluate retrieval and reasoning capabilities of RAG systems from different perspectives.

### Weaknesses
1.	The dependence of GraphRAG on LLM ability. The authors tested two models (GPT-4o-mini and Qwen2.5-14B) on the benchmark. However, the analysis of how GraphRAG depends on the ability (size) of LLMs is missing. It would be nice if the author could give some analysis on the minimum size for a successful GraphRAG.

2.	Some of the multi-hop QA datasets, which contains QA pairs with various question types and different difficulties, such as CWQ, MuSiQue, and 2WikiMultihopQA, are not discussed in this manuscript. 

3.	This paper lacks a concrete explanation of how the raw text corpus is organized into an ontology by GPT-4.1. This task can be challenging, hence one may need to recognize entities and relations, and then perform necessary disambiguation procedures. 

4.	The proposed benchmark does not evaluate the efficiency of graph construction. Ignoring graph construction efficiency is justifiable only if the constructed graph can be reused across a wide range of scenarios.

### Questions
1.	This reviewer is interested to know the reason why some GraphRAG systems, such as ToG, ToG2.0, GNN-RAG, SubgraphRAG are not taken into comparison.

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
6

### Confidence
5