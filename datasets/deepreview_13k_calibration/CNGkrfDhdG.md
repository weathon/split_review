# Integrating Relation Dependences and Textual Semantics for Coherent Logical Reasoning over Temporal Knowledge Graph

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Temporal knowledge graphs (TKGs) reflect the evolution patterns of facts, which can be summarized as logical rules and applied to forecast future facts. However, existing logical reasoning methods on TKGs face two limitations: 1) A lack of efficient strategies for extracting logical paths. 2) Insufficient utilization of structural and textual information. To bridge these gaps, we propose CoLR, a two-stage framework that mines relation dependencies and textual semantics for Coherent Logical Reasoning over TKGs. In the first stage, we construct a temporal relation structure graph (TRSG) composed of relations and cohesion weights between them. Besides, we define a novel time-fusion search graph (TFSG) along with TRSG to facilitate efficient and reliable temporal path searching. In the second stage,
the textual content and timestamp sequences from these paths undergo encoding via a pre-trained language model and a time sequence encoder to accurately capture potential logical rules. Additionally, for quadruplets missing paths, historical edges sampled based on relation cohesion are used as supplements. Given the limitations of existing benchmark datasets in evaluating accuracy, generalization, and robustness, we construct three new datasets tailored to transductive, inductive, and few-shot scenarios, respectively. These datasets, combined with four real-world datasets, are employed to evaluate our model comprehensively. Experimental results demonstrate that our approach significantly outperforms existing methods across all three scenarios. Our code is available at https://anonymous.4open.science/r/CoLR-0839

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces CoLR, a two-stage framework designed to improve logical reasoning over TKGs by integrating structural dependencies and textual semantics. The approach constructs a Temporal Relation Structure Graph to identify relations and their temporal cohesion, alongside a Time-Fusion Search Graph for reliable path searching. CoLR then encodes both the textual content and timestamp sequences with a pre-trained language model and a time sequence encoder, enhancing predictive reasoning on TKGs. Experiment results shows that CoLR significantly outperforms previous methods.

### Strengths
1.	The CoLR framework effectively combines structural dependencies and textual semantics, which improves logical reasoning over TKGs.
2.	By constructing new datasets tailored for specific reasoning challenges, the authors ensure a thorough evaluation of their model's capabilities in transductive, inductive, and few-shot scenarios.
3.	The TRSG and TFSG facilitate efficient pathfinding and extraction, reducing computational costs and enabling the model to handle complex reasoning tasks.

### Weaknesses
1.	The paper does not provide a detailed analysis of CoLR's computational complexity. Metrics such as runtime comparisons are not thoroughly discussed. The time-fusion path extracting process, especially with the addition of the TRSG and TFSG, might introduce computational bottlenecks. It's unclear how the proposed method scales with larger graphs or longer time windows. Specifically, the paper lacks a formal analysis of the time complexity of constructing the TRSG and TFSG, as well as the path retrieval process. The impact of the size of the temporal relation structure graph and the time-fusion search graph on the overall runtime is not quantified. Furthermore, the paper does not discuss the memory requirements of maintaining these graphs, which could be a limiting factor for very large TKGs.
2.	While an ablation study is presented, it might not comprehensively cover all components of the model. For example, the impact of different path lengths (L) or the number of paths (K) on performance is not explored. The ablation study should also investigate the sensitivity of the model to the choice of the pre-trained language model and the time sequence encoder. It is unclear how the performance varies when using different PLMs or time encoders. The study should also include an analysis of the impact of the time window size on performance, as this parameter could significantly affect the model's ability to capture long-range temporal dependencies.
3.	The framework’s reliance on cohesive relations may lead to suboptimal explanations for events connected by low-cohesion paths, affecting interpretability in sparse data scenarios. The paper does not discuss how the model handles cases where the most relevant paths are not the most cohesive ones. It is also unclear how the model would perform in scenarios where the TKG is very sparse, and the cohesive relations are not well-defined. The interpretability of the model's predictions is also limited by the fact that the path selection process is not transparent, and it is difficult to understand why certain paths are chosen over others.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a two-stage framework named CoLR for coherent logical reasoning over TKGs. The framework integrates relation dependencies and textual semantics to enhance the performance of link forecasting tasks. The key contributions include the construction of a temporal relation structure graph (TRSG) to capture structural dependencies, a time-fusion search graph (TFSG) to efficiently extract reliable temporal paths, and the encoding of textual and timestamp sequences using pre-trained language models and time sequence encoders. The authors construct three new datasets to comprehensively evaluate the model, demonstrating SOTA performance across transductive, inductive, and few-shot scenarios.

### Strengths
1. The approach of combining relation dependencies and textual semantics in a two-stage framework for TKG reasoning is novel. The TRSG and TFSG concepts, along with the path supplement strategy, are innovative contributions.
2. The methodology is rigorously designed and theoretically grounded. The proof for the cohesion matrix calculation and the algorithm for path extraction are well-documented.
3. The paper is well-structured and clearly written. Definitions, formulations, and algorithms are explained in detail, making the approach reproducible.
4. The proposed model achieves state-of-the-art results on multiple datasets, demonstrating its effectiveness and generalizability. The new datasets provide valuable resources for future research in this domain.

### Weaknesses
While the scalability of the approach is discussed, concrete experiments demonstrating its performance on larger TKGs are missing. The computational complexity of the TRSG construction and path extraction could become a bottleneck for very large graphs.
The authors could consider including visualizations of the TRSG and TFSG to intuitively illustrate their structures and how they facilitate path extraction.

### Questions
How sensitive is the model to the choice of pre-trained language model? Have you experimented with different language models to see the impact on performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors primarily address the shortcomings of rule-based reasoning methods in the field of temporal knowledge graph extrapolation. To this end, they propose two novel graph structures: the Time-Fusion Search Graph (TFSG) and the Temporal Relation Structure Graph (TRSG). Furthermore, they introduce the CoLR model, which employs a two-phase framework to mine relational dependencies and semantic structures within temporal knowledge graphs. The experimental results demonstrate the effectiveness of the proposed methods, validating their ability to make predictions and capture structural information in sparse data scenarios.

### Strengths
1. Innovatively Proposed the Temporal Relation Structure Graph (TRSG) Structure，which effectively captures stable structural information in temporal graphs.
2. Treated Rules as Text Sequences. By utilizing pre-trained text sequence encoders and time series encoders for learning, neural-symbolic integrated reasoning is achieved.
3. In the paper, three novel datasets are introduced, accompanied by comprehensive experiments designed to rigorously validate the performance of the proposed methods from multiple perspectives.

### Weaknesses
There are some issues in the main experimental results section.

1. The tasks in the field of temporal knowledge graph extrapolation vary. For instance, CENET uses triplet filtering for results and performs future predictions at any time point, whereas TiRGN employs quadruplet filtering for results and only predicts queries for the next time point. The authors' direct comparison of these two methods is obviously unreasonable. 

2. Additionally, the paper does not specify how the baseline results were obtained, and the provided code link is inaccessible. The authors need to specify the type of tasks performed for the results obtained using the CoLR model, as well as whether triplet or quadruplet filtering was applied to these results.

### Questions
See the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a time-fusion search method based on a temporal relationship structure graph to address the problem of existing TKGR models being difficult to effectively extract logical paths from temporal KGs. Afterwards, the joint pre-trained language model and GRU model is proposed to obtain more complete logical semantics in the logical path from the perspectives of logical context and time series, effectively improving the inference quality of the TKGR model. In addition, to better validate the effectiveness of the model, this paper constructs three new datasets to measure the inference accuracy, generalization, and robustness of the TKGR model in transitive, inductive, and few shot scenarios.

### Strengths
1.Solid theoretical analysis: The descriptions of constructing the temporal relation structure graph and reasoning path search algorithm are relatively clear.

2.Adequate experimental validation: The effectiveness of the model in reasoning accuracy and generalization performance was verified through transitive, inductive, and few shot scenarios.

3.The proposed new datasets expand the evaluation benchmarks in the TKGR field.

### Weaknesses
1.The description of challenge in the abstract and introduction does not correspond well. “Nonetheless, the majority of paths between the subject and object......lacking direct connectivity between subject and object entities” in the introduction seems to focus more on discussing the first challenge in the abstract, and the "Insufficient utilization of structural and textual information" in the abstract does not provide corresponding motivation and background analysis in the introduction.

2.The joint encoding method of time and text sequences seems a bit outdated. Although the experimental results demonstrate the effectiveness of this method, I would like to know if utilizing some more cutting-edge LLM based TKG learning models (e.g., [1], [2], [3]) can further improve the model's performance.

[1] Wang, Jiapu, et al. "Large Language Models-guided Dynamic Adaptation for Temporal Knowledge Graph Reasoning." arXiv preprint arXiv:2405.14170 (2024).

[2] Xia, Yuwei, et al. "Enhancing temporal knowledge graph forecasting with large language models via chain-of-history reasoning." arXiv preprint arXiv:2402.14382 (2024).

[3] Luo, Ruilin, et al. "Chain of history: Learning and forecasting with llms for temporal knowledge graph completion." arXiv preprint arXiv:2401.06072 (2024).

3.Omission in the experiment sections: (i)The window parameter w for the YAGO dataset was not provided. (ii)The value of δ in Formula 3 is not explicitly given. (iii)It seems that Figure 5 in the appendix is not described in the text and has no clear indication of the experimental dataset.

4. The quality of the presentation is below ICLR 2025 standards. For example, the format of the references should be consistent to ensure neatness and professionalism. For instance, the names of conferences should be uniformly presented either in abbreviations or full names, rather than a mixture of both.

### Questions
Besides the issues in weakness, there are a few other issues I would like to know:

1.For the PLM module in the joint coding model, does the authors verify the adaptability of the proposed model to different PLMs.

2.I would like to know if it is possible to consider training the model on a single dataset and evaluating it on different test sets in the context of inductive learning. For example, after training on ICEWS14, the model's performance on ICEWS18 and ICEWS05-15 can be on par with SOTA's baseline.

### Soundness
2

### Presentation
3

### Contribution
2
