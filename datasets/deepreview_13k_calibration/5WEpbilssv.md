# Contextualizing biological perturbation experiments through language

- Decision: Accept
- Avg Score: 4.60
- Scores: 6, 3, 5, 6, 3

## Abstract
High-content genetic perturbation experiments provide insights into biomolecular pathways at unprecedented resolution, yet experimental and analysis costs pose barriers to their widespread adoption. In-silico modeling of unseen perturbations has the potential to alleviate this burden by leveraging prior knowledge to enable more efficient exploration of the perturbation space. However, current knowledge-graph approaches neglect the semantic richness of the relevant biology, beyond simple adjacency graphs. To enable holistic modeling, we hypothesize that natural language is an appropriate medium for interrogating experimental outcomes and representing biological relationships. We propose PerturbQA as a set of real-world tasks for benchmarking large language model (LLM) reasoning over structured, biological data. PerturbQA is comprised of three tasks: prediction of differential expression and change of direction for unseen perturbations, and gene set enrichment. As a proof of concept, we present SUMMER (SUMMarize, retrievE, and answeR), a simple LLM-based framework that matches or exceeds the current state-of-the-art on this benchmark. We evaluated graph and language-based models on differential expression and direction of change tasks, finding that SUMMER performed best overall. Notably, SUMMER's outputs, unlike models that solely rely on knowledge graphs, are easily interpretable by domain experts, aiding in understanding model limitations and contextualizing experimental outcomes. Additionally, SUMMER excels in gene set enrichment, surpassing over-representation analysis baselines in most cases and effectively summarizing clusters lacking a manual annotation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a benchmark for evaluating LLM reasoning on biological perturbation experiments, and an LLM-based framework that uses knowledge graphs and prior data to outperform current methods in interpretability and performance on these tasks.

### Strengths
1. The method appears to be sound, combining RAG and COT prompting with knowledge graphs for handling complex biological relationships.
2. The proposed ramework emphasizes interpretable outputs, which is beneficial to biological research.
3. The evaluation was thorough, with both graph and language-centric baselines across multiple datasets.

### Weaknesses
1. The model focuses on discrete perturbation outcomes and does not address combinatorial perturbations, which are common in biological studies.
2. The interpretability of the method comes at the cost of additional complexity in prompt engineering, and it is not known how the performance is sensitive to the prompt design.
3. The paper acknowledges limitations in current evaluation metrics for enrichment tasks. It would be better to see the utilization of new, domain-specific metrics.

### Questions
1. How well does SUMMER generalize to new or sparsely annotated biological datasets? Are there performance drops when applied to less-studied cell lines or organisms?
2. Did the authors perform an error analysis to determine whether specific types of perturbations or gene functions are harder for SUMMER to predict accurately?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces PERTURBQA, focusing on prompting LLMs for gene perturbation and gene set enrichment. It also presents a reasoning method, SUMMER, designed for this task. Experiments demonstrate the effectiveness of the proposed approach.

### Strengths
The proposed task of using large language models (LLMs) to address gene-related tasks is innovative and engaging. 

The paper is clearly presented, well-written, and easy to follow.

### Weaknesses
Limited Experimental Insight: The experiments primarily conclude that SUMMER outperforms baselines but provide few additional insights into the new task. Given the novelty of using LLMs for this type of gene analysis, more extensive experiments and in-depth analysis would be valuable. Specifically, the paper lacks a thorough investigation into the types of errors the model makes, the conditions under which it fails, and the specific limitations of the approach. A more detailed error analysis, including examples of both successful and unsuccessful predictions, would be beneficial.

Insufficient Baselines and Model Comparisons: The baselines selected are not sufficiently comprehensive. Numerous studies have explored LLM reasoning with graph data or text retrieval, which are closely related to this method. Including these in the comparisons could yield deeper insights into the effectiveness of LLMs for gene-related tasks. The paper should compare against methods that explicitly model gene regulatory networks or use knowledge graph embeddings for reasoning, as these are more directly relevant to the task. Furthermore, the baselines lack diversity, focusing primarily on simpler methods, rather than state-of-the-art techniques in related fields.

Metrics for Gene Set Enrichment: The suitability of ROUGE-1 recall and BERT Score for measuring the accuracy of gene set enrichment results is questionable. These metrics, designed for text similarity, may not capture the nuances of biological relevance. Human evaluation or evaluations with LLMs may offer more reliable assessments. The paper needs to justify the use of these metrics or explore alternative metrics that are more appropriate for evaluating gene set enrichment, such as semantic similarity measures or functional enrichment scores.

### Questions
Retrieved Content for Reasoning: Is the retrieved content primarily focused on the gene's function? If so, could this lead to information leakage in the question? For example, if asked about the influence of gene A on gene C, and the retrieved content on gene A directly states that A turn on C, wouldn’t this turn the task into reading comprehension rather than genuine prediction?

Multi-Hop Reasoning: How does SUMMER handle multi-hop reasoning if it only retrieves information on the one hop neighbors of the perturbation and target gene?

### Soundness
2

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
3

### Summary
This paper introduces PERTURBQA, a benchmark suite for evaluating LLMs in reasoning over structured biological data from genetic perturbation experiments. The paper also presents SUMMER, a language-based framework designed to predict differential expression and direction of gene changes as well as to perform gene set enrichment. SUMMER combines knowledge graphs and retrieval-augmented generation to enhance interpretability, matching or surpassing state-of-the-art models on PERTURBQA tasks. The benchmark is designed to help researchers interpret outcomes in high-content genetic perturbation experiments and understand model limitations.

### Strengths
1. **Novel Application of Language-Based Reasoning in Pertburbation Task:** The paper offers a novel application of language-based reasoning to biological data, allowing PERTURBQA tasks to be approached in an interpretable way that benefits domain experts.
2. **Comprehensive Benchmark Design:** PERTURBQA includes real-world tasks relevant to differential expression, gene direction, and gene set enrichment, providing a holistic assessment of model reasoning on biological data.
3. **Interpretable Model Outputs:** SUMMER’s use of knowledge graphs and retrieval-augmented generation produces outputs that domain experts can readily interpret, addressing the limitations of black-box models in biological contexts.

### Weaknesses
1.**Insufficient Related Work Discussion:** The paper could better situate its contribution within the existing literature, especially regarding related work on several aspects: 1. graph-to-text works: such as [Zhao et al., 2023](https://arxiv.org/abs/2310.01089), [Chen et al., 2023](https://arxiv.org/abs/2307.03393), check the [survey](https://arxiv.org/pdf/2407.06564) for details. 2. graph RAG works, e.g. [GraphRAG](https://arxiv.org/pdf/2404.16130), [He et al., 2024](https://arxiv.org/abs/2402.07630), [Mavromatis et al., 2024](https://arxiv.org/abs/2405.20139) . Discussing these works would strengthen the contextual grounding of the proposed approach.

2.**Marginal Technical Contribution:** As stated in W1, both ideas of using LLM for graph tasks and graph RAG are widely studied before, which renders the contribution of this paper marginal.

3.**Limited Baselines:** A wider range of recent baselines, especially from the graph domain (e.g. those mentioned above in W1 and W2), should be included to provide a more comprehensive evaluation and enable better comparison of SUMMER's effectiveness.

4.**Potential Data Leakage Concerns:** Given that LLaMA3 might have been exposed to substantial amounts of biological data, including related gene interactions, there’s a risk of data leakage. A clearer evaluation of SUMMER’s performance independent of potential pre-trained biases could help clarify if its good performance stems from model design or from pre-existing knowledge in the model.

### Questions
NA

### Soundness
3

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
The paper introduces PERTURBQA, a benchmark for using language models to interpret genetic perturbation experiments. These experiments reveal gene functions but are expensive. The proposed SUMMER framework combines biological text data and experimental results, outperforming knowledge-graph-only models on tasks like predicting gene expression changes and gene set enrichment. SUMMER’s language-based outputs offer clearer insights for biologists, enhancing interpretability and accessibility in modeling biological data.

### Strengths
The paper is well-organized and easy to follow.

The paper proposed an interesting problem of using LLMs to predict gene pertubation.

### Weaknesses
1. The biggest concern of the proposed method is the problem itself. For example, SUMMER relies on the biology knowledge graph. However, the biology knowledge graph is built based on the experiments and analysis. Compared with the gene perturbation prediction from scRNA, the knowledge-building quiring updates the knowledge at once to build the possible links among genes. This indicates that this method has a risk of overfitting the known knowledge and being unable to discover new perturbation genes; it is more like a retrieval system for gene interactions we already know.

To further explain how the proposed method can generate more situations, my suggestion is to include more datasets to avoid overfitting. For example, in scGPT[1], the evaluation for perturbation is across 3 different perturbation datasets.

2. In the previous study of gene perturbation, one gene input can output several gene expressions, which are judged at one time. However, the LLM framework suggests that the source and target are a pair of data. This means that if we want to see every gene expression after perturbation, we should go through every combination of gene pairs with LLMs. This is really time-consuming in this setting. Besides, the experiments are really limited to a small size of genes.

In GEARS, scGPT, and CellPLM, they set the perturbation tasks for both 1 gene unseen and 2 genes unseen, and they can claim that the proposed method can handle different perturbation situations. However, in this paper, there are no such illustrations. Besides, in GEARS, the authors predict 102 genes at one time for novel gene perturbation analysis (Fig5a in GEARS). In scGPT, they predict 210 combinations (Fig3 in scGPT). In this paper, there is no evidence that the proposed method can do such things.

3. The authors should include gene pretrained methods such as scGPT[1] and Geneformer[2]. The text-based methods are pretrained on lots of textual information, the comparing method is unfair with only MLP, GAT, and GEARS.

As I mentioned before, the pretrained methods on the single-cell data are considered one of the most powerful methods in gene perturbation tasks at this moment. In scGPT, they report scGPT can achieve 50% higher than GEARS. Instead of training on lots of textual information, they trained directly from gene expressions. If the authors want to claim the textual-based pretrained method is more powerful than we predict genes from scRNA data, they need to discuss these models.

4. Compared with other work in gene expression from ML method, such as CellPLM[3], LanCell[4], CellSentence[5] this paper lacks biology analysis in bio view. This limited the application to further applications.

In scGPT and GEARS, they have a figure of predicted gene expression profiles of the perturbation conditions. Other papers are not perturbation-specific methods, but they are ai4biology papers that are published in the top AI conferences. They also show some biological analysis to strengthen their methods for their own contribution, such as marking genes on the cells to show the cell states.

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposed an in-silico approach to solving the biological perturbation experiment results prediction. The original idea is to enrich the graph-structure-based cellular responses textually. In terms of technique details, the authors proposed PertubQA as a pre-processing step and omitted minor changes in the gene expression level. Then, the authors adopted prompt engineering to retrieve the structured knowledge crossing gene-gene interaction result and gene description. Following a CoT manner, the LLM generates the final answers.

### Strengths
S1. Adopting LLM in biological analysis is an interesting topic. This study follows a combination of LLM-related tech fashion. 

S2. The authors developed a PertubQA dataset to validate the following research on textual enrichment of perturbation analysis. 

S3. Detailed examples and case studies are provided to show the effectiveness of the framework.

### Weaknesses
W1. Part of the technical contribution is related to GenePT, which adopted a textual description and gene expression value to extract the cell representation, and GEARs, which combined prediction on a genetic relation graph (gene-coexpression graph and GO graph).  

W2. The contributions of the proposed PerturbQA dataset are unclear. Why do we need a vague textual description of gene perturbation instead of a formalized graph structure with exactly numeric data? 

W3. Missing technical details. I couldn't find the setting (or formal definition) of the study problem. Those make this paper hard to follow.

### Questions
Q1. Please describe the distinct contributions of PerturbQA beside a RAG- or a meta-path-walk-like text description generation. How do you ensure the description is correct? For instance, PubmedQA is generated from many articles and certified by human experts. 

For the rest of the question, please refer to weak points.

### Soundness
2

### Presentation
1

### Contribution
2
