# RAGGED: Towards Informed Design of Retrieval Augmented Generation Systems

- Decision: Reject
- Scores: 8, 3, 3, 6

## Abstract
Retrieval-augmented generation (RAG) can significantly improve the performance of language models (LMs) by providing additional context for tasks such as document-based question answering (DBQA). 
However, the effectiveness of RAG is highly dependent on its configuration.
To systematically find the optimal configuration, we introduce \methodname, a framework for analyzing RAG configurations across various DBQA tasks. 
Using the framework, we discover distinct LM behaviors 
in response to varying context quantities, context qualities, and retrievers.
For instance, while some models
 are robust to noisy contexts, monotonically performing better with more contexts, others are more noise-sensitive and can effectively use only a few contexts before declining in performance.
This framework also provides a deeper analysis of these differences by evaluating the LMs' sensitivity to signal and noise under specific context quality conditions.
Using \methodname, researchers and practitioners can derive actionable insights about how to optimally configure their RAG systems for their specific question-answering tasks

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies how the components of a retrieval-augmented generation (RAG) system impact its performance on a variety of tasks. They propose an evaluation framework called RAGGED that  evaluates the impact of more context, inclusion of irrelevant information, and the interaction between task type model performance. They compare combinations of three retrievers (BM25, ColBERT, Contriever) and four readers (FLAN, LLaMa, GPT, Claude) on multiple datasets and present a series of findings that make the case for designing RAG frameworks that are task-specific and tailored to their use case.

### Strengths
- With increasing adoption of RAG for a variety of tasks, this is a useful direction of research that helps researchers understand when and how to use this set up. These findings could be potentially useful for deciding how to configure a RAG framework based on the task.

- The RAGGED framework proposed in this paper is well-designed and addresses critical questions at each step of the pipeline. The authors aim to release the code for this framework which would enable easier replication and extension to include more models/experiments.

- The paper is well-written and the results are presented in a very easy to understand manner. I really appreciate how Table 1 and the figures that follow communicate the core findings succinctly. The appendix also provides useful additional details for the experiments.

### Weaknesses
 - The paper does not compare more state of the art closed-source models like GPT-4 and Claude 3 Opus. It’s understandable that cost may be a hindrance, but it would be helpful to conduct even a smaller set of experiments using stronger models so the takeaways from this paper are more broadly applicable.

- Unigram F1 doesn’t strike me as the ideal metric for evaluating reasoning quality in LLMs. Perhaps the authors could have explored semantic embedding-based approaches or by simply asking another LLM to verify the (output, label) pair for accuracy.

- While the takeaways are interesting, it would have been helpful to hear the authors’ thoughts on why certain models outperform others in different settings.

### Questions
- Did the authors try any kind of prompt engineering to see if it improves performance?
- The FanOutQA benchmark (Zhu et al., ACL 2024) strikes me as a particularly suitable Wikipedia-based testbed for this framework. Did the authors attempt to include it in their evaluation? 
- Another increasingly important factor in RAG systems in multilinguality, which impacts both retrievers and readers. It would be useful to include at least one multilingual dataset, like NoMIRACL (Thakur et al., EMNLP 2024), in this testing framework.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduce an analysis framework, RAGGED, for understanding RAG best practices, namely, whether RAG helps, how many passages to retrieve, which retrievers and reader models to choose, and how that varies across tasks. They conduct this analysis across the retrievers BM25, ColBERT, and Contriever and assess several reader models, evaluating these on NQ (general domain), HotPotQA (complex questions), and BioASQ (specialized domain). Overall, they find that readers vary (some benefit from higher recall at larger retrieval depths; others are sensitive to noise) and that improved retrieval delivers more noticeable gains in specialized domains.

### Strengths
1) The paper is very well-written and structured, and hence easy to follow. The research questions posed are clear and the findings are stated and discussed in a well-presented manner.
2) The work empirically identifies trends that are of interest to the community, serving as evidence, for instance, that RAG helps more in specialized domains and that improving the components of a RAG system separately does not guarantee higher end-to-end quality.
3) Thoughtful analysis of RAG systems, which have very quickly become ubiquitous, are very much needed.

### Weaknesses
While I admire a thoughtful analysis paper, the present work simply does not explore rich enough questions to balance the lack of novel insight nor does it have enough empirical support for the nuanced claims it tries to extract. To illustrate, the primary non-trivial aspect of the present study are interesting claims like "improved retrieval helps more in specialized domains". This is analytically self-evident (i.e., is not necessarily a new claim) but good empirical support for such claims is always valuable. Unfortunately, the work is essentially trying to support this post-hoc from results on NQ vs. BioASQ, two of the most standard, over-used, and overly-simplistic datasets. To be clear, NQ and BioASQ are still valid and interesting datasets, but the lack of novelty coupled with the factoid and short answer nature and small variety of datasets selected makes it very hard to position this work at ICLR in my current read.

To be very clear, I think work like this is necessary, but to publish this as a long research paper the bar to clear might involve something llike (i) innovating dramatically more on the evaluation front, e.g. assessing human evaluators against a large number of automatic metrics, not just F1 overlap, over a large set of (perhaps contributed) new evaluation benchmarks that vary certain axes more directly or (ii) testing a set of less overused claims and hypotheses, e.g., novel methods that counteract the challenges the authors have observed. Right now, the contribution is simply too small and too ephemeral of an addition to the literature in this (overcrowded) domain.

### Questions
N/A

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes RAGGED, aiming to study the impact of different readers, retrievers, and the number of retrieved documents. It reveals the different response patterns of the reader model to contexts and provides suggestions for deploying an RAG system.

### Strengths
This paper proposes the RAGGED framework with the comprehensive and systematic study of multiple key aspects of RAG configuration. It constructs a complete assessment system through four clear research questions (R1-R4).

### Weaknesses
# Limitations in Methodological Approach

### Retrieval Architecture Constraints

- Limited Exploration of Modern Retrieval Methods
  - The study did not incorporate state-of-the-art retrievers (e.g., BGE) and reranking mechanisms
  - Contemporary search engines and their potential impact were not evaluated
- Generalizability Concerns
  - The conclusion that "better searchers ≠ better RAG performance" may require reconsideration in light of recent empirical evidence using modern retrieval systems

### Architectural Paradigm Limitations

- Restricted RAG Implementation Scope
  - The investigation did not encompass emerging RAG variants (e.g., Self-RAG) and recent Large Language Model paradigms (e.g., OpenAI O1)
  - The impact of prompt engineering variations was not systematically explored (e.g., CoT and Self-Ask)
- Retrieval Source Considerations
  - Limited investigation into how different knowledge source types affect system performance

### Dataset and Task Coverage

- The study's conclusions are constrained by the limited variety of datasets and task types examined (only 3 datasets)
- A broader spectrum of use cases would strengthen the generalizability of the findings



# Limitations in Experimental Depth and Analysis

## Experimental Design Constraints

### Variable Control Inadequacies

- Noise Distribution Effects: The impact of noise location within documents remains unexplored
- Document Structure Variables
  - The influence of paragraph length variation was not systematically analyzed
  - Potential correlations between document structure and retrieval performance were not examined

### Analytical Depth Limitations

- Lack of analysis of the reasons why "Some retriever-reader combinations consistently benefit from RAG, while others only sometimes do for certain k’s, and a few never do regardless of k"
- The analysis lacks depth, only revealing obvious, common, and widely known conclusions without examining the underlying causes. I suggest analyzing the conclusions mentioned in the article from the perspective of how LLMs handle conflicts and integration between their internal knowledge and external information.

## Practical Implementation Constraints

- Configuration Guidelines
  - Lack of concrete, actionable implementation recommendations
  - Modern RAG systems include many other components, such as rerankers, scoring mechanisms, query routing, and query rewriting. **Your work appears to be limited to performing grid search on just a few hyperparameters.**
- The applicability/generalizability to other tasks cannot be guaranteed.

### Questions
- Q1: Why weren't modern retrievers like BGE and search engines considered? Would this affect the reliability of the main conclusions?
- Q2: How was the strategy for selecting noise paragraphs determined? Does this choice affect the validity of the experiments?
- Q3: Does the conclusion "better retrievers ≠ better RAG performance" still hold after incorporating rerankers and more modern retrievers?
- Q4: Do the improve-then-plateau and peak-then-decline behavior patterns still exist with different RAG and LLM paradigms?
- Q5: Why was unigram F1 chosen instead of other potentially more suitable evaluation metrics? The paper mentions that “many LMs respond correctly semantically but use inexact or more verbose wording.” which can be avoided by extracting the answer using the LLM. The effect of the Unigram-F1 assessment is not comprehensive enough.
- Q6: What are the criteria for selecting noise paragraphs in Section 6? 
- Q7: Was the impact of different retrieval passage lengths considered?
- Q8: Can you explain the underlying reasons why different models respond differently to RAG improvements?
- Q9: How do the quantity and scope of parametric knowledge correlate with performance variations across different LLMs? Additionally, could the authors explore the dynamics of knowledge conflicts and integration between an LLM's internal (learned during pre-training) and external (retrieved during inference) knowledge bases?
- Q10: The paper mentions providing "To provide more concrete suggestions of the best practices under various cases, we introduce an analysis framework, RAGGED," What are some efficient approaches to determine the optimal RAG configuration when working with new datasets or models? Specifically, how can practitioners rapidly identify the most effective combination of retrieval methods, LLMs, $k$, and other key parameters?

### Soundness
2

### Presentation
3

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
The paper introduces RAGGED, a framework for analyzing and evaluating RAG systems. While the work presents a comprehensive analysis framework, its contributions mainly focus on investigating how different components and configurations affect RAG performance across various tasks and domains. 
The main contributions include:
- A systematic analysis framework examining RAG components,
- Empirical findings on RAG performance characteristics,
- Investigation of retriever-reader relationships,
- Domain-specific insights for RAG applications.

### Strengths
- The study examines multiple dimensions of RAG systems with a systematic approach, using diverse models and configurations. This provides valuable empirical evidence about component interactions.
- The authors provide their code and framework publicly, with well-documented experimental setups and clear implementation details.
- The work challenges some common assumptions about RAG systems, particularly regarding the relationship between retriever and reader performance.

### Weaknesses
 - While the paper presents extensive empirical findings about RAG system performance, it lacks a theoretical framework that could explain the underlying patterns and relationships between reader model's architectures (e.g., parameter count, token limits) and their performance characteristics, which could have enabled broader generalizations about unexplored model families and helped predict optimal configurations based on architectural features rather than just empirical observations.
- The evaluation focuses narrowly on question-answering tasks with relatively small datasets (2837 queries for NQ, 5600 for HotpotQA, 3837 for BioASQ). This raises questions about the generalizability of findings to other applications/domains. Specifically, the datasets are limited in the diversity of question types, complexity, and the range of reasoning required, which may not fully capture the challenges of real-world RAG applications. The limited dataset size also makes it difficult to assess the robustness of the findings and the statistical significance of the observed performance differences.
- The paper could benefit from more rigorous comparison with existing RAG analysis frameworks or methodologies to better establish its unique contribution. The current comparison is superficial and does not delve into the specific methodological differences and advantages of the proposed framework compared to others.

### Questions
- Could the authors analyze how model characteristics (e.g., parameter count, architecture type, pre-training approach, token limits) correlate with RAG performance patterns? Have you observed any clustering of performance patterns based on model families or architectures that could suggest theoretical principles for predicting RAG behavior? Such analysis might help generalize findings to unstudied models and provide theoretical grounding for the empirical observations.
- The significantly different behavior observed in specialized domains (e.g., BioASQ) vs. open domain is intriguing. Could you elaborate on what characteristics of specialized domains lead to these differences? Have you analyzed if reader models pre-trained on domain-specific data show different RAG behavior patterns?
- Could you provide insights into how to predict whether a domain would benefit more from dense vs. sparse retrievers?

### Soundness
2

### Presentation
3

### Contribution
2
