# Reflection on Knowledge Graph for Large Language Models Reasoning

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Recent studies have highlighted the potential benefits of supplementing Large Language Models (LLMs) with information retrieved from knowledge graphs to enhance their performance. However, current approaches often introduce additional noise in the pipeline process of knowledge retrieval and reasoning, leading to the accumulation of errors, impeding LLMs from effectively combining the external knowledge in answering complex multi-hop questions. To this end, we introduce RefKG, an innovative framework specifically crafted to enhance the reasoning capabilities of LLMs through reflective engagement with knowledge graphs. In particular, RefKG autonomously conduct retrieval and reflection on knowledge graphs. Its reasoning process includes four steps: decomposing complex queries, retrieving and pruning evidence subgraphs, generating textual evidence, and evidence-enhanced reasoning. To enhance the alignment of LLMs with external knowledge, we have developed a multi-task tuning strategy that not only infuses knowledge to LLMs but also teaches them how to utilize the knowledge in answering questions, thereby significantly improving their ability to handle knowledge-intensive tasks. Experimental results on fact verification and knowledge graph question answering tasks demonstrate that RefKG outperforms previous state-of-the-art models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on using large language models (LLMs) for knowledge graph question answering and fact verification tasks. The authors propose a framework that leverages an LLM to extract relevant reasoning paths from a knowledge graph and generate context based on these paths to reach the final answer. The framework involves three main steps: query decoupling, retrieval/construction/re-ranking of knowledge paths, and finally, context generation and question answering. They utilize GPT-3.5-turbo to generate training data for each of these steps and fine-tune smaller LLMs through multi-task learning.

### Strengths
- Overall, the proposed approach is straightforward and intuitive. Using an LLM to iteratively explore and retrieve reasoning paths from a knowledge graph is both novel and interesting.
- The method demonstrates strong empirical performance on two benchmark datasets, outperforming the baseline methods.
- A generated training dataset is provided, which could have potential value for future model training and evaluation.

### Weaknesses
 - The proposed method’s novelty may be limited. The approach of using LLMs to decompose knowledge-intensive questions and then iteratively retrieve relevant information for knowledge-based tasks has already been widely discussed in existing literature, such as in the "self-ask" framework and its subsequent works. Additionally, using closed-source models like GPT-3.5-turbo to generate data is also common practice.
- I believe the computational cost of this method is a concern. To answer a multi-hop question, the model requires multiple LLM calls, often at least four. This cost may pose scalability challenges.
- The baseline models used have limitations. To better demonstrate the effectiveness of the additional steps in the proposed approach, a useful comparison would be a simple baseline that trains or prompts an LLM to generate possible reasoning paths from the knowledge graph, retrieves relevant paths, and uses them as context to answer questions. This would provide a clearer comparison of the value added by the additional steps in the proposed method.

### Questions
Is there an average number of LLM calls required to answer each question or verify each fact?

### Soundness
3

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
4

### Summary
The paper introduces RefKG, a framework that enhances LLMs' complex reasoning capabilities through reflective engagement with knowledge graphs. The framework consists of three main components: query decoupling, evidence subgraph retrieval, and knowledge reconstruction inference. Additionally, it employs a multi-task tuning strategy to improve LLMs' performance on knowledge-intensive tasks. The framework was evaluated on three benchmarks - FactKG, MetaQA, and WebQuestionsSP - demonstrating superior performance over previous state-of-the-art models in both fact verification and knowledge graph question answering tasks.

### Strengths
- The innovative approach of leveraging knowledge graphs through reflective reasoning significantly enhances LLMs' reasoning capabilities, particularly for complex multi-hop questions.
- The multi-task tuning strategy effectively expands LLMs' capabilities, showing substantial improvements across different tasks.
- The empirical evaluation is comprehensive, with thorough comparisons against various baseline models across multiple benchmarks.

### Weaknesses
 - The error accumulation issue in the multi-step pipeline is not adequately addressed, potentially limiting the framework's effectiveness for more complex reasoning chains.
- The generalization capability across different domains is not thoroughly explored, lacking discussion on the framework's applicability to diverse knowledge domains.
- The interpretability aspects of RefKG, particularly regarding the decision-making process and reasoning paths during multi-task learning, could be better explained.

### Questions
This paper claims to address the noise and error accumulation issues in knowledge retrieval and reasoning pipelines. However, I have some concerns about this claim: (1) While decomposing complex queries into simpler sub-queries is interesting, this additional step could potentially introduce its own errors. The paper's ablation study shows that incorrect entity identification in this stage accounts for 62% of total errors. How do you ensure the reliability of this decomposition step, especially for queries with complex semantic dependencies? (2) The paper proposes using an expert model to score and filter evidence triplets. There's no analysis of how this refinement process handles conflicting or complementary evidence. (3) Can you provide quantitative analysis showing how the refinement process reduces noise propagation in multi-hop reasoning chains?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a framework called RefKG, designed to enhance the reasoning capabilities of LLMs by integrating them more effectively with KGs. The authors address the challenges faced by current approaches, which often introduce noise during knowledge retrieval and reasoning, leading to errors that hinder LLMs from effectively utilizing external knowledge for complex multi-hop questions.

RefKG operates through a three-step process: 
- Query Decoupling Module: Decomposes complex queries into simpler sub-queries that share common knowledge backgrounds, facilitating more targeted retrieval.
- LLM-Driven Knowledge Graph Exploration Module: Iteratively and reflectively retrieves relevant evidence subgraphs from the knowledge base, using an expert model to refine the knowledge and eliminate irrelevant information.
- Inference with Knowledge Reconstruction Module: Transforms structured knowledge from the KG into natural language that the LLM can easily understand, integrating it with the original question to derive the answer.

Additionally, the authors develop a knowledge-driven multi-task tuning strategy by fine-tuning the LLM on a specially synthesized corpus generated by LLMs themselves. This equips the model with foundational expertise in knowledge-intensive reasoning, enhancing its ability to handle advanced tasks.
Experimental results on fact verification and KGQA tasks demonstrate that RefKG outperforms previous state-of-the-art models, not only improving performance but also enhancing the explainability of the LLMs' reasoning processes.

### Strengths
- The organization of the paper is clear and easy to follow, although there are some typos should be polished. 
- RefKG presents an effective approach to integrating LLMs with KGs by leveraging reflective reasoning, addressing the limitations of previous methods. The framework's iterative retrieval and pruning effectively reduce noise in the retrieved knowledge, improving the accuracy of the reasoning process.
- The knowledge-driven multi-task tuning equips the LLM with initial expertise, improving its ability to handle knowledge-intensive tasks from the outset.
- The framework demonstrates superior performance on fact verification and KGQA tasks, validating its effectiveness over previous KG-augmented methods. Furthermore, RefKG is evaluated across various open-source LLMs, showing that it can be adapted to different models and settings.

### Weaknesses
 - Although effective, the RefKG framework lacks technical novelty. The pipeline is simple and not exciting enough. 
- The RefKG framework's effectiveness on tasks beyond fact verification and KGQA is not explored, limiting understanding of its broader applicability. Besides, the benchmarks are not sufficient enough. 
- The approach may not generalize well to domains with sparse or highly specialized KGs. Moreover, the performance may heavily rely on the completeness and accuracy of the underlying KGs, which may vary in different domains. 
- The iterative retrieval and reflection process may be computationally intensive, raising concerns about scalability for large-scale applications.
- The paper seems not go through a careful typos checking, as there are some typos.

### Questions
- Have you tested RefKG on other knowledge-intensive tasks or domains? If so, how did it perform compared to existing methods? 
- How does RefKG perform in terms of computational efficiency, especially with large-scale knowledge graphs, and have you considered methods to optimize it?
- What steps were taken to identify and mitigate potential biases in the LLM-generated corpus used for multi-task tuning?

Missing References
- KnowledgeNavigator: Leveraging Large Language Models for Enhanced Reasoning over Knowledge Graph (Complex & Intelligent Systems, 2024)
- Chain-of-Knowledge: Integrating Knowledge Reasoning into Large Language Models by Learning from Knowledge Graphs (2024)
- Paths-over-Graph: Knowledge Graph Enpowered Large Language Model Reasoning (2024)
- LightRAG: Simple and Fast Retrieval-Augmented Generation (2024)
- ……

Tyops:
- At line 040, “like knowledge graphs (KGs)(Luo et al.,”, there is a missing blank between “(KGs)” and “(Luo et al.,”. 
- In Table 1, “ToG(Sun et al., 2022)[ICLR24]”, the citation format of ToG should be latest, 2022 --> 2024. 
- At line 207, Evidence Subgraph retrieval. --> Evidence Subgraph Retrieval.
- At line 506, Impact of numbers of Top-K retrieval. --> Impact of Numbers of Top-K Retrieval.
- ……

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces RefKG, a new framework designed to enhance the reasoning capabilities of Large Language Models (LLMs) by improving their integration with knowledge from knowledge graphs. RefKG tackles the problems of noise and error accumulation in knowledge retrieval and reasoning processes, which previously impeded the effective use of external knowledge in answering complex questions. The framework employs a four-step process: decomposing complex queries, retrieving and pruning knowledge graphs to form evidence subgraphs, generating textual evidence, and performing evidence-enhanced reasoning. RefKG also incorporates a multi-task tuning strategy that not only feeds knowledge into LLMs but also trains them on effectively utilizing this information for question answering. Experimental results on tasks such as fact verification and knowledge graph question answering demonstrate that RefKG outperforms existing state-of-the-art models, indicating a significant improvement in LLMs' ability to handle knowledge-intensive tasks.

### Strengths
* The idea of using query decoupling, knowledge retrieval, and reconstruction is sound, and the paper is well written.
* The experiments are clean, and the figures in the paper are easy to follow.

### Weaknesses
W1: The idea of using query decoupling, knowledge retrieval, reconstruction is sound but not that interesting. Seems each step has already been acknowledged by other papers which may underscore the novelty of the proposed unified framework. Especially as the statement from lines 144-145, "the aforementioned methods do not filter the extracted triplets..." further underestimates the contribution compared to methods like Retrieve-Rewrite-Answer, KAPING. The issue of filtering extracted triplets has already been discussed in papers like ToG[2], FiDeLIS[3], etc. If the authors intend to discuss the solutions to this issue, the corresponding references should be involved.

W2: the table 1 comparison seems not fair, seems KG-GPT, KB-BINDER, and TOG are all training-free methods, only Retrieve-rewriter methods require training. However, the training phase in Retrieve-rewriter is only targeted to train the retriever and rewriter, where the target is different from the proposed RefKG. In that case, it's not very sound to compare properties like multi-task tuning and knowledge refinement. Otherwise, I suggest the authors should also consider more baselines requiring further training like RoG[1].

W3: the training process is quite similar to the existing method like RoG[1] and there is no comparison and analysis between these papers. Additionally, I'm quite curious whether the training process is necessary; it seems like the proposed method can be independent only with inference. In that case, considering adding another ablation study is necessary, especially using some advanced models like GPT-4o or o1. (btw, what is the model used in Table 5 ablation study?)

### Questions
Q1: What are the reflection capabilities explicitly referred to in lines 72 to 73? I suggest the authors should rephrase the definition of reflection of LLMs in case not all readers are familiar with the term in the context of LLMs.

Q2: How is the corresponding entity subset $E_{sub}$ collected as mentioned in Section 3.1? How to make sure the decoupled entities can be grounded to the corresponding KGs? If the subsets are provided in the dataset like FactKG, how is that method been adapted to dataset like WebQSP?

Q3: How to define the ending point of the chain $P_t$ mentioned in Section "Evidence subgraph retrieval"? Is the entire process controlled by the LLM itself?

Q4: What are the LLMs used across the entire method section? Have the LLMs been fine-tuned using the corpus mentioned in Section 3.4, or only the naive LLMs? Additionally, what is the LLM used for in the expert model mentioned from lines 238 to 250?

Q5: I have concerns about whether the knowledge reconstruction process may inadvertently introduce noise/hallucinations when leveraging LLMs to transform the retrieved KG triplets into some textual statements. Since this process is not under control and perhaps requires some curated designs or error analysis.

### Soundness
3

### Presentation
3

### Contribution
2
