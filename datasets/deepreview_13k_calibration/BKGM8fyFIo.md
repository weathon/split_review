# GARLIC: LLM-Guided Dynamic Progress Control with Hierarchical Weighted Graph for Long Document QA

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 5, 6, 6

## Abstract
In the past, Retrieval-Augmented Generation (RAG) methods split text into chunks to enable language models to handle long documents.
Recent tree-based RAG methods are able to retrieve detailed information while preserving global context.
However, with the advent of more powerful LLMs, such as Llama 3.1, which offer better comprehension and support for longer inputs, we found that even recent tree-based RAG methods perform worse than directly feeding the entire document into Llama 3.1,
although RAG methods still hold an advantage in reducing computational costs.
In this paper, we propose a new retrieval method, called LLM-\underline{G}uided Dyn\underline{a}mic P\underline{r}ogress Contro\underline{l} with H\underline{i}erar\underline{c}hical Weighted Graph (\OurName), which outperforms previous state-of-the-art baselines, including Llama 3.1, while retaining the computational efficiency of RAG methods.
Our method introduces several improvements:
(1) Rather than using a tree structure, we construct a Hierarchical Weighted Directed Acyclic Graph with many-to-many summarization, where the graph edges are derived from attention mechanisms, and each node focuses on a single event or very few events.
(2) We introduce a novel retrieval method that leverages the attention weights of LLMs rather than dense embedding similarity. Our method allows for searching the graph along multiple paths and can terminate at any depth.
(3) We use the LLM to control the retrieval process, enabling it to dynamically adjust the amount and depth of information retrieved for different queries. %different queries to retrieve varying amounts and levels of information.
Experimental results show that our method outperforms previous state-of-the-art baselines, including Llama 3.1, on two single-document and two multi-document QA datasets, while maintaining similar computational complexity to traditional RAG methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work introduces a retrieval method, "GARLIC" (LLM-Guided Dynamic Progress Control with Hierarchical Weighted Graph), aimed at improving long document question answering. GARLIC operates through a multi-step process. First, it constructs a Hierarchical Weighted Directed Acyclic Graph (HWDAG) where each node represents a focused "Information Point" (IP) generated through LLM-based summarization. Second, GARLIC dynamically retrieves nodes from the graph, leveraging attention weights to assess relevance and terminate the search once sufficient information is collected. Third, it employs a Greedy Best-First Search to explore multiple graph paths, enhancing flexibility by allowing the search to stop at various levels based on the query's needs. This approach effectively balances retrieval precision and computational efficiency, outperforming existing methods in single and multi-document QA tasks.

### Strengths
S1. The proposed method employs a hierarchical weighted directed acyclic graph instead of a tree structure, utilizing multi-path dynamic retrieval and hierarchical summary nodes.
S2. It is an interesting idea to assign weights to the edges based on attention, which allows GARLIC to adjust the retrieval depth and information volume flexibly.
S3. Decent performance compared to other existing approaches for retrieval.

### Weaknesses
W1. An explanation of the edge weights in the directed acyclic graph needs further clarification: specifically, how the weights are calculated and how they function during the search process. The current presentation lacks intuitiveness.
W2. Detailed explanation on how KV caching is applied in the dynamic progress control is needed.
W3. The code should be made publicly available.
W4. Some baseline methods mentions in the article search down to the leaf nodes during retrieval, in other words, gather more information. However, why do they perform worse than the method presented in this paper, even though the proposed method may terminate the search early? Further analysis would be beneficial.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents GARLIC, a retrieval method that uses Hierarchical Weighted Directed Acyclic Graphs to improve long-document question-answering (QA) tasks. Unlike traditional retrieval-augmented generation (RAG) and tree-based models, GARLIC combines a unique two-stage process - Summary Graph Construction and Dynamic Graph Search.

### Strengths
By using dynamic stopping and attention-weighted paths, GARLIC avoids unnecessary computation, which is common in exhaustive retrieval methods.

Outperforms benchmarks like Llama 3.1 and recent methods on NarrativeQA, Qasper, HotpotQA, and MuSiQue.

Compatible with long-context LLMs (e.g., Llama 3.1), making it feasible for single GPU execution.

### Weaknesses
The attention normalization approach may limit scalability to larger graphs and complex attention patterns. Specifically, the method normalizes attention weights across all layers, which could lead to a loss of fine-grained attention information, especially in deeper networks or when dealing with very long documents. This normalization may also not effectively capture hierarchical attention patterns that could be crucial for understanding long-range dependencies.

While the retrieval stage is efficient, graph construction is relatively resource-intensive, especially for single-query documents. The process of creating the hierarchical weighted directed acyclic graph involves multiple summarization steps, which can be computationally expensive, particularly when the document is only queried once. This overhead might outweigh the benefits of the retrieval method for single-query scenarios, making it less practical in those situations.

Embedding similarity, although beneficial, introduces some redundancy when compared with pure attention-based retrieval. While the authors claim that removing embedding similarity results in only a minor performance drop, the fact that it is included at all suggests that the attention-based retrieval is not fully sufficient on its own. This raises questions about the necessity of including embedding similarity and whether it truly enhances the retrieval process or simply adds complexity.

### Questions
How does the system handle differences in event granularity? Specifically, do Information Points (IPs) for shorter events lead to inconsistencies in information distribution across the graph?

How does GARLIC scale when handling complex attention dependencies or queries that span multiple, disparate sections of a document? Is there a threshold at which the attention-guided search might encounter limitations?

Has dynamically adjusting the stop patience based on query complexity or node connectivity been considered? Could this approach optimize retrieval efficiency within larger graphs?

How does the efficiency of graph search vary in contexts with mixed single- and multi-query documents, particularly in cases with highly fragmented narratives, such as those in NarrativeQA?

GARLIC appears to extend ideas from both RAPTOR and MemWalker, borrowing sub-graph or informational-node stacking from RAPTOR and summarization from MemWalker. Could you clarify the main design distinctions and advantages of GARLIC compared to these methods (apart from using greedy search)?

Could you explain the choice to exclude LongT5 XL (Guo et al., 2022) and CoLT5 XL (Ainslie et al., 2023) as baselines (or any other baseline you feel may have given better performance similar to the base Llama3.1 on the benchmarked datasets), given their performance as open-source models? While ChatGPT’s closed-source nature makes its exclusion understandable, a rationale for omitting these alternatives would help clarify comparisons. Also, could you discuss the reported GARLIC performance alongside Table 5 in [1]?

From Table 1, it appears that a significant portion of GARLIC's performance boost is coming from the Llama-3.1 base model, as it already outperforms other baselines. How might results compare if Llama-3.1 were used with RAPTOR instead, considering RAPTOR's higher efficiency (0.5:1 on 1 datasets, and always below 1 on all remaining datasets)?

[1] Sarthi, Parth, et al. "Raptor: Recursive abstractive processing for tree-organized retrieval." arXiv preprint arXiv:2401.18059 (2024)."

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new retrieval method, GARLIC (LLM-Guided Dynamic Progress Control with Hierarchical Weighted Graph), which aims to improve information retrieval in long document question answering tasks. It replaces the traditional tree structure by building a hierarchical weighted directed acyclic graph and uses the attention weights of large language models (LLMs) to perform multi-path search and dynamically control the retrieval process. Experiments show that this method surpasses the existing state-of-the-art baselines, including methods that directly use Llama 3.1 to process the entire document, while maintaining the computational efficiency of the RAG method.

### Strengths
1. Overall, this paper is well-written and easy to read.
2. While existing RAG methods perform worse than directly feeding the entire document into Llama 3.1, the authors propose a new RAG method outperforms Llama 3.1 and retaining the computational efficiency of RAG methods. This approach can be used for reference by other researchers.

### Weaknesses
1. In line 292, the author mentioned that the node's attention is multiplied by the corresponding position information to track the earlier information in the sequence. I think the author should conduct experiments to explain whether other adjustment methods have been tried? Why is this adjustment method effective? Specifically, the authors should provide a more detailed justification for why multiplying the attention weights by the node's position is the optimal approach for tracking earlier information. It's unclear if this linear scaling is the most effective way to address the issue of later nodes assigning lower attention to the query. A comparison with alternative methods, such as exponential or logarithmic scaling, or even a learned positional encoding, would strengthen the argument for the chosen approach. Furthermore, a more thorough analysis of the attention distribution across different nodes and queries would be beneficial to understand the impact of this adjustment.
2. Lack of comparative analysis with other methods: Although the proposed model achieved excellent performance, the authors did not clearly explain why HWDAG is superior to the tree-based RAG method? Tree-based retrieval also seems to be able to summarize long documents and answer questions by selecting important nodes that are highly relevant to the query in a top-down manner through the GRAPH SEARCH method proposed by the authors. In addition, HWDAG seems to organize documents into a top-down hierarchy with different granularity, so low-level nodes seem to be a refinement and explanation of top-level nodes. As one of the main motivations of the article, I hope the author can explain why introducing refined information will hurt performance for some problems. The authors should elaborate on the specific limitations of tree-based RAG methods when compared to their proposed graph-based approach. It is not clear why a tree structure cannot effectively capture the relationships between different levels of information granularity. A more detailed analysis of how the graph structure enables a more nuanced representation of the document's content is needed. The authors should also provide a more concrete explanation of why introducing refined information can sometimes hurt performance, perhaps by illustrating with specific examples where the tree-based approach fails.
3. During the construction of the summary graph, the authors iteratively aggregate lower-level nodes by batching them and inputting them into the large language model (LLM) to generate higher-level nodes. However, the details of the iterative batching mechanism require further elaboration. Specifically, the authors should clarify the criteria used for determining the batch size at each level of the hierarchy. It is not clear how the token count is calculated, and whether it includes the prompt tokens. A more detailed explanation of how the batching strategy adapts to different document lengths and content complexity is needed. The authors should also discuss the potential impact of different batching strategies on the quality of the generated summaries and the overall performance of the retrieval method.

4. The authors argue that the information points (IPs) focus on “a single event or very few events”. It seems that the authors achieve this with just several instructions in the prompt. Is this approach sufficient to ensure the achievement of the intended objectives? The authors should provide a more rigorous justification for why the prompt-based approach is sufficient to ensure that IPs focus on single or very few events. It is not clear if the LLM consistently adheres to the instructions, and a more detailed analysis of the generated IPs is needed to validate this claim. The authors should also discuss the potential limitations of this approach and explore alternative methods for ensuring the desired granularity of IPs.

5. The authors average the token-level attentions to obtain the weights between information chunks (IPs). However, since these chunks represent higher-level, text-based content, is averaging token-level attentions an appropriate method for establishing relationships between these information chunks? The authors should provide a more detailed justification for why averaging token-level attentions is an appropriate method for establishing relationships between higher-level information chunks. It is not clear if this approach effectively captures the semantic relationships between IPs, and a more thorough analysis of the attention patterns is needed. The authors should also discuss the potential limitations of this approach and explore alternative methods for establishing relationships between IPs, such as using a separate model or a more sophisticated attention mechanism.

### Questions
Please refer to weakness, thanks.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a method using LLMs to summarize long text into key information points, organizing these points into a hierarchical structure through recursive processing. This results in a directed acyclic graph where edge weights between nodes are generated based on attention mechanisms. For QA tasks, the authors apply a weighted BFS to retrieve relevant information from the graph. An LLM dynamically controls the retrieval process by determining if the information collected so far is sufficient to answer the question.

### Strengths
1. The system uses a large language model to recursively generate key information from long texts, constructing an information structure graph. It employs the model's attention mechanism to assign weights to edges, introducing a new structure for information representation.

2. The authors propose using a priority-based breadth-first search to retrieve information points within the graph. The search process is controlled by the large language model, allowing retrieval to stop as soon as relevant information is found. This approach, compared to depth-first search, offers greater flexibility while maintaining efficiency. Final experimental results outperform recent benchmarks, including Llama 3.1.

### Weaknesses
1. The paper does not explain how edge weights between nodes are calculated using the attention mechanism of the LLM, lacking crucial algorithmic details.

2. In Section 3.2.2, the paper discusses calculating the relevance between the query and information points using attention. How is this calculation performed, especially if it needs to be precomputed? This method may have limited scalability for new queries and new documents.

3. No code is released, making it difficult for others to use the proposed method or reproduce the result.

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
3
