# Know2BIO: A Comprehensive Dual-View Benchmark for Evolving Biomedical Knowledge Graphs

- Decision: Reject
- Scores: 5, 6, 3, 1

## Abstract
Knowledge graphs (KGs) have emerged as a powerful framework for representing and integrating complex biomedical information. However, assembling KGs from diverse sources remains a significant challenge in several aspects, including entity alignment, scalability, and the need for continuous updates to keep pace with scientific advancements. Moreover, the representative power of KGs is often limited by the scarcity of multi-modal data integration. To overcome these challenges, we propose \bmkgname, a general-purpose heterogeneous KG benchmark for the biomedical domain. \bmkgname~integrates data from 30 diverse sources, capturing intricate relationships across 11 biomedical categories. It currently consists of \textasciitilde219,000 nodes and \textasciitilde6,200,000 edges. \bmkgname~is capable of user-directed automated updating to reflect the latest knowledge in biomedical science. Furthermore, \bmkgname~is accompanied by multi-modal data: node features including text descriptions, protein and compound sequences and structures, enabling the utilization of emerging natural language processing methods and multi-modal data integration strategies. We evaluate KG representation models on \bmkgname, demonstrating its effectiveness as a benchmark for KG representation learning in the biomedical field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Know2BIO is a biomedical Knowledge Graph that integrates multiple knowledge bases to create a big heterogenous KG with 219K nodes and 6.9M relationships.

### Strengths
The authors have done a good job in explaining the process of creating the knowledge graph for biomedical domain.

### Weaknesses
1. It would have been better if some examples were present that would explain the integration of specific similar entities with different names/representation in two KGs, and steps of resolving those.
2. Future work should provide concrete methods that could be tried.

### Questions
1. How did you integrate multiple knowledge graphs with different ontology?
2. What techniques did you use to perform entity resolution, entity disambiguation?
3. What challenges did you face while merging the different KGs?
4. Since you have mentioned the use of 30 KBs for your KG construction, how did you select these? What about other KGs present? Is there any significant KB not utilized?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors in this paper propose Know2BIO, a heterogeneous KG benchmark for the medical domain. The KG integrated data from several sources and its very large in size. It consists of multi-modal data where the node features contain text descriptions, protein and compound sequences and structures. The authors evaluated KG representation models on the proposed KG to demonstrate its effectiveness as a benchmark. The authors have clearly laid out the limitations of the KG as well as the future work.

### Strengths
Some of the strengths of Know2BIO are:

1. Know2BIO is larger and contains information from several sources (30 sources).
2. It represents 11 biomedical categories and other edges types that are typically absent in other KGs.
3. It is robust, up-to-date and can be extensible.
4. With the information it contains, it can support several real-world learning tasks.

### Weaknesses
Using the data source code URL provided in the abstract of this paper, the authors’ identity is visible in the README. This goes against ICLR’s anonymity policies (authors also checked “ I certify that there is no URL (e.g., github page) that could be used to find authors' identity.” But should have verified this before submitting.

### Questions
1. Are the edges for each of the categories homogeneous in nature? 
2. Can users easily query this KG? If yes, will the authors be extending support to using LLMs on this?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a large-scale heterogeneous knowledge graph benchmark named Know2BIO in the biomedical field, integrated from 30 data sources. The graph includes multi-modal data, including text descriptions, sequences of proteins and compounds, structures of proteins and compounds, etc. The authors compared several triple-based knowledge base completion models on the graph.

### Strengths
- The paper proposes a large-scale, heterogeneous, automatically updated biomedical knowledge graph with several multi-modal attributes, including texts, sequences of proteins and compounds, and their structures.
- Several methods are evaluated and compared on the proposed graph.

### Weaknesses
- Although the proposed graph is large and periodical update is important and needs considerable effort, constructing knowledge graphs from existing databases is not novel and the difficulty in constructing such KGs is limited. 
- The proposed graph has several multi-modal attributes, but they are not used in the evaluation and the compared methods are limited. 
- The paper misses several related works on heterogeneous KG.  
  - Wise et al., COVID-19 Knowledge Graph: Accelerating Information Retrieval and Discovery for Scientific Literature. In Proceedings of Knowledgeable NLP: the First Workshop on Integrating Structured Knowledge and Neural Networks for NLP, 2020.
  - Asada et al., Integrating heterogeneous knowledge graphs into drug–drug interaction extraction from the literature. Bioinformatics, 2023.

### Questions
See the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper discuss the building of clinical knowledge graph by aggregating several existing knowledge grpahs

### Strengths
-

### Weaknesses
I don't think the correct venue for this work, clinical/biology venues are a better fit

### Questions
Other than evaluation there are no ML aspects to this work, am I missing something?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
