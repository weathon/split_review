# From Isolated Conversations to Hierachical Schemas: Dynamic Tree Memory Representation for LLMs

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Recent advancements in large language models have significantly improved their context windows, yet challenges in effective long-term memory management remain. We introduce \textbf{\ours}, an algorithm that leverages a dynamic, tree-structured memory representation to optimize the organization, retrieval, and integration of information, akin to human cognitive schemas. \ours organizes memory hierarchically, with each node encapsulating aggregated textual content, corresponding semantic embeddings, and varying abstraction levels across the tree's depths. Our algorithm dynamically adapts this memory structure by computing and comparing semantic embeddings of new and existing information to enrich the model’s context-awareness. This approach allows \ours to handle complex reasoning and extended interactions more effectively than traditional memory augmentation methods, which often rely on flat lookup tables. Evaluations on benchmarks for multi-turn dialogue understanding and document question answering show that \ours significantly enhances performance in scenarios that demand structured memory management.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes MemTree, a dynamic tree-structured memory representation algorithm designed for managing the storage, updating, and retrieval of external information. The authors' motivation is that existing memory management methods do not consider the intrinsic structure of external information, with individual information units being stored independently. The core of this work lies in the tree-based memory updating process, which involves tree traversal, leaf node expansion, and parent node aggregation updates. The work is validated across four benchmark datasets with different characteristics, showing particularly notable results in long-term dialogue scenarios.

### Strengths
S1. Clear Algorithm Characteristics. The work presents a clear and well-defined algorithm without making excessive claims. Both the algorithm description and the experimental design are straightforward and easy to follow.

S2. Experimental results effectively support the Authors' Claims.

S3. The primary contribution of this work lies in developing a tree-structured memory representation algorithm, with a focus on the processes of tree construction (node expansion) and updating.

### Weaknesses
W1. From another perspective, the generalizability of this work is limited, as its performance improvements are not as pronounced on non-long-term dialogue data.

W2. Although the work does not make excessive claims, its retrieval processes adopt methods from prior work. The retrieval process prioritizes performance by flattening the memory tree, which overlooks the structural characteristics of the information stored.

W3. Does the aggregation process rely heavily on the performance of the LLM? The paper does not provide sufficient discussion on this aspect. Since a substantial amount of information is abstracted and summarized during tree construction, it raises the question of whether semantic similarity-based matching remains accurate in this context.

### Questions
Minor Comment:
There is a typo in line 154: the first $C_v$ should be  $c_v$.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors aim to address the challenge of long-term memory management in LLMs. Inspired by human cognitive patterns, they propose an algorithm named MemTree, which organizes information through a dynamic tree structure.

The authors evaluate the algorithm on conversational and document question-answering tasks and compare it with both online and offline knowledge representation methods. Their experimental results demonstrate that MemTree outperforms the various baselines presented.

### Strengths
- The paper includes extensive experiments and analysis.

- The performance of the proposed method surpasses most baselines.

### Weaknesses
 - The paper frequently claims the efficiency of the proposed method but lacks specific experiments comparing the update and retrieval times with those of the baselines.

- The paper lacks details on how the memory is constructed for these evaluation datasets. Lines 303–306 indicate that the primary difference between MemTree and RAPTOR is that MemTree operates as an online algorithm, dynamically updating the tree memory representation with incoming knowledge, while RAPTOR applies hierarchical clustering on a fixed dataset. If this is the case, does it imply that MemTree’s memory size is typically smaller than RAPTOR’s during evaluation?

- It is unclear why the approach in Section 3.2, which flattens the hierarchical structure, ensures more efficient retrieval. How does the mentioned retrieval process differ from directly traversing the entire memory to search for the closest node?

- It would be beneficial to conduct experiments demonstrating the impact of varying similarity thresholds, as this value influences the width of the tree.

- It is unclear what aspect of MemTree resembles human cognitive schemas—the dynamic memory updates or the tree structure? Human cognitive schemas appear to align more closely with a graph-like structure rather than a tree.

### Questions
- It is unclear why the approach in Section 3.2, which flattens the hierarchical structure, ensures more efficient retrieval. How does the mentioned retrieval process differ from directly traversing the entire memory to search for the closest node?

- It would be beneficial to conduct experiments demonstrating the impact of varying similarity thresholds, as this value influences the width of the tree.

- It is unclear what aspect of MemTree resembles human cognitive schemas—the dynamic memory updates or the tree structure? Human cognitive schemas appear to align more closely with a graph-like structure rather than a tree.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a knowledge organization method called MemTree for long-term memory storage. The main idea of MemTree is to hierarchically store information through a tree structure, enabling hierarchical organization and dynamic updating of memory.

The MemTree construction process resembles the concept of B-Trees in traditional computer science. First, the information to be stored is encoded into a vector. Starting from the root node of the tree, the most similar child node is selected based on LLM embedding similarity. If the similarity between the stored information and the closest child node exceeds a predeﬁned threshold, the process continues downwards until a leaf node is reached. Otherwise, the leaf node is expanded, and the information of the new node is summarized and propagated to its parent node. Experimental results conﬁrm that this method eﬀectively organizes memory content, which is beneﬁcial for tasks requiring knowledge retrieval.

### Strengths
Strengths:

1. The use of a tree structure eﬀectively organizes memory content, mimicking how humans summarize and store knowledge in higher-level memory constructs.

2. Experiments on MSC and MSC-E demonstrate the method’s strong and stable performance in longcontext memory tasks, while results on QuALITY show that MemTree can match or even surpass oﬄine methods (e.g., GraphRAG) with better update eﬃciency.

3. Compared to oﬄine methods such as GraphRAG and RAPTOR, MemTree oﬀers higher update eﬃciency while achieving comparable performance.

### Weaknesses
1. Collapsed Tree Retrieval for Knowledge Extraction: The paper adopts a Collapsed Tree Retrieval approach, presumably to retrieve not only leaf nodes but also aggregated, summary-based non-leaf nodes. However, this raises two questions:

Although non-leaf nodes summarize all descendant knowledge, this summarization could lead to information loss. How is this issue addressed?

If required knowledge spans nodes under diﬀerent parent nodes, would this tree structure still support retrieval of the complete set of needed information?

2. Tree Balance: While statistical analysis shows that MemTree remains generally balanced, there appears to be no explicit mechanism to enforce balance. And the observed balance may be due to the context not being suﬃciently long. More eﬀective operations for maintaining tree balance should be proposed, as the balance of the tree could theoretically impact the summarization quality of non-leaf nodes during MemTree construction.

3. Error Analysis for RAG Tasks: Could the paper provide a more detailed error analysis of MemTree’s performance on speciﬁc Retrieval-Augmented Generation (RAG) tasks? Speciﬁcally, is the source of errors due to inaccuracies in embedding similarity calculations, incomplete retrieved knowledge, or errors introduced by the summarization process?

4. Longer Context Retrieval: Could this method be extended to longer context retrieval tasks to further showcase its strengths in handling extensive knowledge storage and retrieval scenarios?

### Questions
see weaknesses

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
4

### Summary
The paper proposes MemTree, an online algorithm for tackling the long-term memory issue of LLM inference. The approach, as shown in its name, builds a tree structure for managing chat history. The dynamic feature and hierarchical structure make MemTree effective and efficient.

### Strengths
The design of MemTree is reasonable and resembles the human cognition process in managing memory. Moreover, the retrieval mode of MemTree simply flattens the tree structure, making the retrieval more efficient than other traditional tree-based methods, and the dynamic feature of MemTree makes the approach work seamlessly with LLMs. Lastly, MemTree performs fairly well among the baseline methods.

### Weaknesses
- **More baseline models**: The paper only experiments with two models: GPT-4o and LLaMA2. As the design of MemTree is related to LLM (e.g., updating the parent nodes needs LLM-based operations), more baseline models are needed to better demonstrate the effectiveness of the proposed approach. Specifically, the experiments should include a wider range of model sizes and architectures to ensure the generalizability of the method. The current selection does not fully explore the performance of MemTree across different LLM capabilities and limitations.

- **More details in efficiency comparison**: the paper claims that the proposed method closes the gaps between online and offline memory methods. What are the efficiencies of all the methods mentioned in the paper, including the naive one? How long is the inference time per instance? The paper should provide a detailed breakdown of the computational costs associated with each method, including memory usage, processing time, and the number of operations required. This analysis should also consider the impact of different input lengths and memory sizes on the overall efficiency.

- **Cost of using GPT-4o**: As the experiment tables are mostly about using GPT-4o, the cost of GPT-4o should also be considered as one aspect of the efficiency probation. The paper needs to quantify the financial cost of using GPT-4o, especially when compared to other models. This cost analysis should include the number of API calls, token usage, and the overall expense of running the experiments, which is crucial for practical applications.

-**More human study**: More human study on comparing MemTree with different methods are needed, especially for ``human annotated evidence``. This could help demonstrate why MemTree is better and how it could be further improved. The human study should not only focus on the alignment of MemTree's structure with human intuition but also evaluate the quality of the retrieved information and its impact on task performance. It is important to understand how humans perceive the relevance and coherence of the information retrieved by MemTree compared to other methods.

### Questions
- **What is the reason for using GPT-4o as your baseline model as there are some other long-context LLMs, like long-lora, LongLLaMA, etc.?**

- **How is the MemTree compared to the prompt-compression methods, which aim at discarding the noisy information in the long contexts? For example, [1]**

[1] [LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression](https://aclanthology.org/2024.acl-long.91) (Jiang et al., ACL 2024)

### Soundness
3

### Presentation
3

### Contribution
3
