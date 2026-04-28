# Retrieval or Reasoning: The Roles of Graphs and Large Language Models in Efficient Knowledge-Graph-Based Retrieval-Augmented Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 6, 5, 8

## Abstract
Large Language Models (LLMs) demonstrate strong reasoning abilities but face limitations such as hallucinations and outdated knowledge. Knowledge Graph (KG)-based Retrieval-Augmented Generation (RAG) addresses these issues by grounding LLM outputs in structured external knowledge from KGs. However, current KG-based RAG frameworks still struggle to optimize the trade-off between retrieval accuracy and efficiency in identifying a suitable amount of relevant graph information for the LLM to digest. We introduce SubgraphRAG, extending the KG-based RAG framework that retrieves subgraphs centered on query/topic entities and leverages LLMs for reasoning. Our approach innovatively integrates a lightweight multilayer perceptron (MLP) with a parallel triple-scoring mechanism for efficient subgraph retrieval while encoding directional structural distances to enhance retrieval accuracy. The size of retrieved subgraphs can be flexibly adjusted to match the query's need and the downstream LLM's reasoning capacity. This design strikes a balance between model complexity and reasoning power, enabling scalable and generalizable retrieval processes. Notably, based on our retrieved subgraphs, smaller models like Llama3.1-8B deliver competitive results with explainable reasoning, while larger models like GPT-4o achieve comparable or better state-of-the-art accuracy compared with previous baselines—all without fine-tuning. Extensive evaluations on the WebQSP and CWQ benchmarks highlight SubgraphRAG's strengths in efficiency, accuracy, and reliability by reducing hallucinations and improving response grounding.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the SubgraphRAG framework for the first time, a knowledge-graph (KG)-based generation method specifically designed to optimize the efficiency and accuracy of large language models (LLMs) in retrieval-augmented generation (RAG) tasks. By incorporating a lightweight multilayer perceptron (MLP) and a parallel triple-scoring mechanism, SubgraphRAG efficiently retrieves subgraphs relevant to the query and improves retrieval precision through Directional Distance Encoding (DDE). This method effectively balances retrieval accuracy and computational complexity, achieving adaptive subgraph retrieval tailored to different LLM reasoning capabilities for the first time.

### Strengths
**Quality**: The experimental design is comprehensive, covering two major multi-hop datasets in KG-based question answering tasks (WebQSP and CWQ) and providing detailed comparisons with multiple baseline methods. Results show that SubgraphRAG outperforms existing baselines across several metrics, demonstrating higher retrieval efficiency and answer accuracy, particularly in multi-hop reasoning and complex structure retrieval tasks. Additionally, ablation studies validate the independent contributions and effectiveness of each component, such as DDE and MLP.

**Clarity**: The paper is well-structured, with clear explanations progressing from the background of KG-augmented generation tasks to the design of each module within SubgraphRAG. Not only does the paper provide a flowchart illustrating the SubgraphRAG framework, but it also explains each step’s design principles and implementation details in depth. Moreover, the experimental section offers a detailed analysis of different design variations, which helps readers understand the role of each component.

**Significance**: SubgraphRAG provides an innovative and efficient retrieval-reasoning method for KG-augmented generation tasks. Compared to existing methods, SubgraphRAG achieves strong generalizability and extensibility through flexible subgraph retrieval strategies and LLM reasoning without fine-tuning. It offers more robust support for knowledge-driven generation tasks, contributing to the broader and deeper application of KGs in practical generation tasks.

### Weaknesses
1. **Insufficient Exploration of LLMs’ Potential for Retrieval Support**: SubgraphRAG primarily relies on an MLP and Directional Distance Encoding (DDE) for subgraph retrieval, yet LLMs inherently excel in handling complex semantics and relational structures. The paper does not adequately explore the potential of directly leveraging LLMs for the retrieval process, which could offer more flexible multi-hop reasoning capabilities and adapt better to complex KG structures. This could involve using LLMs to generate embeddings for nodes and edges, or to directly score the relevance of subgraphs, potentially enhancing the framework’s ability to handle diverse and nuanced queries.

2. **The Limitation of Topic Entity Bias on Generalizability**: The paper assumes that all queries can be effectively guided by topic entity-induced inductive biases for retrieval. However, this topic-driven approach may restrict information coverage or introduce noise in cases involving ambiguous or polysemous queries. For instance, a query like "What are the applications of Python?" could refer to either the programming language or the snake, and relying solely on a single extracted topic entity might lead to suboptimal performance for non-topic-focused queries or queries with multiple valid interpretations.

3. **Limitations of Structured Triples**: SubgraphRAG presents triples to LLMs in structured form, i.e., (h, r, t), rather than transforming them into natural language descriptions. This misses an opportunity to leverage LLMs’ strengths in natural language understanding and reasoning. Converting triples to natural language, such as "head is related to tail via relation", may allow LLMs to more fully exploit the triple information and achieve more accurate reasoning by leveraging their pre-trained knowledge of language patterns and relationships.

4. **Lack of a Complete Retrieval Process Example**: Although the paper details the algorithmic flow of SubgraphRAG, it lacks a full example from query to retrieval and reasoning to answer generation. Providing a concrete example, such as with a typical query from WebQSP or CWQ, would enhance readers’ understanding of the procedural details, including how the topic entity is extracted, how DDE is applied, and how the final answer is generated from the retrieved subgraph.

5. **Limited Experimental Dataset Scope**: Experiments are conducted solely on WebQSP and CWQ datasets, leaving out other mainstream multi-hop KGQA benchmarks, such as HotpotQA. A broader range of dataset tests, including those with different knowledge graph structures and question types, could further verify the method’s generalizability and robustness across various KGQA tasks.

### Questions
1. Could LLM-driven retrieval better identify information required for multi-hop reasoning?

2. Does topic entity bias lead to misleading results in ambiguous queries, and is there a more generalized retrieval strategy available? 

3. Should triples be directly converted to natural language for LLMs to better understand and utilize them?

4. Could a complete example using a typical query illustrate the entire retrieval-reasoning workflow of SubgraphRAG?

5. How does SubgraphRAG perform on other mainstream KGQA datasets, and is it equally effective?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This manuscript introduces a framework called SubgraphRAG, which is a KG-based RAG system designed to enhance the reasoning capabilities of LLMs by integrating structured information from knowledge graphs.

-  The framework employs a lightweight multilayer perceptron (MLP) combined with a parallel triple scoring mechanism, proposing to adopt a retriever that allows for subgraph distribution factorization. This means that each triple can be optimized independently, which improves the efficiency of subgraph retrieval.
-  By encoding directional structural distances as structural features using DDE, the accuracy of retrieval is enhanced.

### Strengths
- Efficiency and Scalability: As the authors present in Table 1, SubgraphRAG demonstrates high efficiency and scalability in the retrieval process. Additionally, the flexible form of retrieved subgraphs, with adjustable sizes—subgraphs formed by top-triples can accommodate various LLMs with diverse reasoning capabilities.
- By combining DDE and MLP, SubgraphRAG surpasses more complex models, such as RoG and G-Retriever, in terms of covering key triples and entities.

### Weaknesses
 - I affirm: The optimization objective defined in the article states that the SubgraphRAG retriever distribution Qθ can be factorized into distributions over triples, which means that the retrieved subgraphs do not necessarily have to follow a fixed type (such as trees or paths). This design allows for efficient training, efficient subgraph retrieval, flexible subgraph types, and adjustable subgraph sizes, rather than relying solely on path retrieval. This differs from the methods widely discussed in the current research community for finding retrieval triples and performing graph RAG, such as RoG and G-Retriever, which the article compares.

  - However，The main experiments require more graph retrieval methods, especially path retrieval, for comparison. For example:

  > Haoran Luo,et al., ChatKBQA: A Generate-then-Retrieve Framework for Knowledge Base Question Answering with Fine-tuned Large Language Models. ACL (Findings) 2024

  > Guanming Xiong, et al., Interactive-KBQA: Multi-Turn Interactions for Knowledge Base Question Answering with Large Language Models. ACL (1) 2024


  - I am also curious as to why the ToG method is not reproducible, as it seems to be a strong contender in the Hit results. The calculation of ToG's hit@1 is actually based on ToG only finding the first match in the answer text, which is considered as the answer by the large model to calculate Hits@1. However, I do not believe this is the reason for the irreproducibility. Interactive-KBQA has reproduced ToG's results.


[Subtle weaknesses]

- It was not clearly stated whether the experimental results of comparison methods such as RoG and G-Retriever were reproduced a second time or referenced from the original text. This is because the referenced StructGPT missed many tests, while the results of baseline methods like RoG should have been reproduced by the authors themselves.

[Subtle weaknesses]

- Typos and Formatting Issues
  - Naming  Eq.3 and q)). 
  - line 052 ``
  - line 161 .
  - line 986 . 
  - line 966 ，968，970 .
- There are some grammar errors, not listed one by one

### Questions
- Some Ambiguous Expressions Lack Further Mathematical Definition or Explanation
  - What is ‘scalable’ and how to prove whether the method is ‘scalable’ or not?
  - What constitutes suitable prompting?

- The authors noted that baselines report Hit@1 but compute Hit, assessing if any correct answer is in the LLM's response. There's also confusion over metrics like extract match and Hit@1 in the research community. Clarification of these metrics in the appendix is needed, and defining another "Hit metric" is not advised.

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
This paper proposes SubgraphRAG, extending the KG-based RAG framework. To be specific, this method integrates a lightweight multilayer perceptron (MLP) with a parallel triple-scoring mechanism for efficient subgraph retrieval while enhancing retrieval accuracy by encoding directional structural distances. In addition, SubgraphRAG strikes a balance between model complexity and reasoning power as the size of retrieved subgraphs can be flexibly adjusted to match the query’s need and downstream LLM’s reasoning power. Extensive experiments demonstrate the effectiveness of the proposed methods.

### Strengths
1. The idea of employing lightweight models for retrieval and using large language models for reasoning is interesting, sensible, and intuitive.
2. The proposed method is efficient in terms of training time, requiring only the training of an MLP.

### Weaknesses
1. **May Lack novelty.** The novelty behind the proposed method may be insufficient as embedding-based retrieval methods for triplets [1] resemble existing approaches in the literature. Embedding-based retrieval methods for triplets utilize the embeddings of questions and triplets to retrieve the relevant triples. However, the proposed approach merely concatenates $z_\tau$ with the previous embeddings, which may lack sufficient innovation. The concatenation of embeddings, while simple, does not fundamentally address the challenge of capturing complex relationships between the query and the knowledge graph structure, potentially limiting its effectiveness in multi-hop reasoning scenarios.
2. **Baseline methods.** As the proposed methods follow the retrieved-based paradigms, they would be better compared to more retrieved-based methods, such as UniKGQA [2], Subgraph Retrieval (SR) [3], and GNN-RAG [4], which are relevant to the proposed method and derive new SOTA for this task. The absence of these direct comparisons makes it difficult to assess the true advancement of SubgraphRAG over existing state-of-the-art retrieval techniques.
3. **Experimental Results.** As shown in Table 1 for the evaluation for retrieval recall, it would be better to present the number of extracted triplets in a new column for each baseline to ensure fair comparison. The same for Table 3 to demonstrate the QA performance. Without this information, it is unclear whether the performance gains are due to superior retrieval or simply the use of more triples. This lack of transparency hinders a proper evaluation of the method's efficiency and effectiveness.
4. In line 226, the paper claims that "GNNs are known to have limited representation power," which is why GNNs were not chosen for the retriever. However, as shown in Table 5, the paper presents different variants of SubgraphRAG by incorporating various retrieval methods. Including a GNN-based retrieval method for comparison would strengthen the evaluation, such as RevRea [5] as a GNN-based retriever. The lack of a direct comparison with a GNN-based retriever leaves a gap in the evaluation, especially given the claim about GNN limitations.

### Questions
Please see in **Weaknesses** above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents SubgraphRAG, a graph retrieval method for Knowledge Graph Question Answering (KGQA). SubgraphRAG trains a retrieval module to score relevant triplets of the KG based on training questions. During inference, SubgraphRAG retrieves top-scored relevant triplets based on the question and uses them as additional context to the LLM for KGQA. Experiments are performs on WebQSP and CWQ benchmarks, evaluating retrieval and downstream KGQA performance.

### Strengths
The paper strengths are summarized below:

- S1) The retrieval module is lightweight pre-trained text encoder, followed by MLPs. This allows fast retrieval and does not incur significant latency during KGQA with LLMs.
- S2) The experimentation includes ablation studies in both retrieval and downstream KGQA performance, which are helpful to understand the benefits of each of the competing methods.
- S3) The paper reads nicely and is easy to follow.

### Weaknesses
The main weaknesses of the paper are summarized below:

- W1) SubgraphRAG emphasizes the necessity for  lightweight retrieval for KGQA. However, GNNs are already established as lightweight retrievers (as also shown in Table 1) and specifically designed for handling KGs. Although the paper references some GNN-based approaches [1,2], it does not compare SubgraphRAG with them. Without these comparisons, it is unclear why SubgraphRAG favors MLPs over GNNs and what the rationale behind this choice is. Furthermore, the performance differences between MLP, MLP+entity, and Subgraph in entity recall metrics are not significant, raising concerns about whether SubgraphRAG effectively leverages graph structure. Prior work has explored GNNs in KGQA [1], which can be extended to augment GNN predictions with an LLM.

- W2) The retrieval evaluation, as presented in Table 1, relies solely on the recall metric. However, SubgraphRAG retrieves a larger number of triplets (e.g., top-100), which should naturally achieve higher recall than the baselines. To ensure a fair comparison, additional metrics such as precision, F1 score, or recall @ k should also be included. Furthermore, in the KGQA results, SubgraphRAG utilizes more advanced LLMs, such as GPT-4o, compared to the baselines. This raises questions about the advantages of SubgraphRAG when using the same LLMs. For instance, SubgraphRAG combined with LLaMa 3.1-8B does not outperform RoG in the CWQ dataset. The paper proposes three retrieval metrics: path recall, GPT-4 triplet recall, and answer recall. However, there seems to be a mismatch in how these metrics are applied to the baseline methods (e.g., RoG in Figure 3). RoG and GNN-RAG achieve good answer recall, but their GPT-4 triplet recall is worse than GraphSAGE/cosine similarity. These inconsistencies suggest that certain metrics favor specific methods and the authors may need to evaluate retrieval precision.


### Questions
Please refer to the previous comments. Additionally, I have few further questions/comments:
- Q1) Could you provide some citations on what "locality-sensitive hashing, designed for similarity search" in Line 076 means?
- Q2) Line 101 (necessity for lightweight retrieval) and the final choice of MLP contradict Line 095 (LSTMs and GNNs are limited because their lightweight). 
- Q3) In Line 323, SubgraphRAG  continues to use shortest paths, despite their limitations noted in Line 097. 
- Q4) The prompt for GPT-4o scoring (Fig.7) does not include the ground-truth answer. Could the evaluation results change if we include the ground-truth answers?
- Q5) Line 429 mentions that RoG suffers from label leakage. However, SubgraphRAG utilized GPT-4o, whose training data is unknown and could also be affected by training leakage.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a novel KBQA method named SubgraphRAG. Instead of incorporating more powerful LLMs and/or advanced SFT techniques, SubgraphRAG focuses on the retrieval part. It extends the existing KG-based RAG framework with an MLP and a newly proposed triple-scoring mechanism, which shows to be effective and efficient. The retrieved subgraphs allow the proposed method to achieve SOTA performance on smaller LLMs without SFT.

### Strengths
1) The problem is clearly defined. (Section 3.1, equation 1 and 2)
2) The proposed method is easy to follow. It also includes several details for the reader to
reproduce the results, e.g. the initialization of embeddings, the introduction of DDE.
3) The proposed retrieval method is efficient and effective. Better retrievers enhance the
performance ceiling of RAG.
4) This paper includes detailed ablation study (Q1, Q2, and Q5), which proves the effective-
ness of the retriever part.
5) The proposed method achieves SOTA performance on low-scale pretrained LLMs.

### Weaknesses
1) This reviewer suggests the authors move the main results and related analysis to an earlier
subsection of the experiments part, and group the ablation studies together.
2) The WebQSP dataset does not include official explanations for its answers. However, the proposed method requires explanations to perform reliable in-context learning, which relies on external knowledge other than the dataset or the KG.

### Questions
1) As mentioned in Section 3.2, the authors mentioned that the designed prompt template is shown in Figure 2. In addition, this reviewer is interested to know some more *details* about the design of “in-context demonstrations”.
a) Does SubgraphRAG utilize the same “in-context demonstration” for all the questions?
b) How were these in-context demonstrations designed? Specifically, what are the criteria for the selection of these demonstrations? How do you generate the explanations? 

2) The authors raise concerns about the reproducibility issue of the ToG baseline. Since ToG relies on closed-source LLMs such as GPT4, this reviewer believes that the performance can be greatly affected by the specific versions of LLMs. SubgraphRAG also uses closed-source LLMs for evaluation. Which specific version of GPT4o is being used in this work? (Please also include this in the *implementation* part in the paper.)

### Soundness
4

### Presentation
4

### Contribution
3
