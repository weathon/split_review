# Recent Link Classification on Temporal Graphs Using Profile Builder

- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 5, 5, 5, 1

## Abstract
The performance of Temporal Graph Learning (TGL) methods are typically evaluated on the  future link prediction task, i.e., whether two nodes will get connected and dynamic node classification task, i.e., whether a node's class will change. Comparatively, recent link classification is investigated much less even though it exists in many industrial settings. In this work, we first formalize recent link classification on temporal graphs as a benchmark downstream task and introduce corresponding benchmark datasets. Secondly, we evaluate the performance of state-of-the-art methods with a statistically meaningful metric Matthews Correlation Coefficient, which is more robust to imbalanced datasets, in addition to the commonly used average precision and area under the curve, and propose several design principles for tailoring models to specific requirements of the task and the dataset. We explore modifications on message aggregation schema, readout layer and time encoding strategy which obtain significant improvement on benchmark datasets. Finally, we propose  an architecture that we call Graph Profiler, which is capable of encoding previous events' class information on source and destination nodes. The experiments show that our proposed model achieves an improved Matthews Correlation Coefficient on most cases under interest. We believe the introduction of recent link classification as a benchmark task for temporal graph learning will be useful for the evaluation of prospective methods within the field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the "Recent Link Classification" task within the field of "Temporal Graph Learning," focusing on categorizing existing links based on source and destination entities. The authors evaluate baseline methods for future link prediction and temporal graph learning in recent link classification, employing the Mathews Correlation Coefficient as the evaluation metric. Their proposed Graph Profiler architecture consists of five components: profile encoder, message encoder, destination encoder, and a readout layer for information aggregation. The study delves into various strategies for the profile encoder, time encoder, and readout layer, demonstrating performance enhancements over baseline methods.

### Strengths
1. The proposed recent link classification task is practical and holds applicability for addressing real-world industrial problems.
2. The paper conducts a comprehensive investigation into the combination of different approaches from temporal graph learning literature.

### Weaknesses
1. The modeling decisions, such as the choice between learnable or fixed time encoding, appear ad-hoc and contingent on specific datasets. It would be beneficial to elucidate insights or provide general guidance for determining an optimal combination on new datasets. For instance, what factors contribute to the observed performance variation, and is there a rationale for the less effective performance of learnable time-encoding on the Wikipedia dataset? The paper should investigate the underlying characteristics of each dataset that lead to such different behaviors with respect to time encoding. For example, is there a correlation between the temporal density of events and the effectiveness of learnable time encodings? Are certain datasets more sensitive to the specific parameterization of the time encoding functions? A deeper analysis of these aspects is needed.
2. Given that the src-dst-msg-t configuration doesn't generally yield the best results, I am wondering about the necessity of introducing seemingly redundant components like the destination encoder. Additionally, the observed performance degradation in cases where time encoding is added to src-dst raises questions. Is there any explanation for that? The paper should provide a more detailed justification for the inclusion of the destination encoder, especially given its limited effectiveness in certain configurations. Furthermore, the performance degradation when time encoding is added to the src-dst embeddings requires further investigation. Are there interference effects between the different embedding spaces? Does the time encoding introduce noise or bias when combined with src-dst embeddings in a particular manner? The paper should explore the interaction between these components.
3. The presented task bears similarities to entity relationship classification in NLP. It would be interesting to discuss the similarities and differences between these two tasks. The paper should delve into the specific differences in the problem formulations, such as the temporal dynamics and the graph structure, and how they affect the choice of modeling techniques. A discussion on how existing techniques from entity relationship classification can be adapted or modified for the recent link classification task is also warranted.
4. The proposed method mainly combines several existing methods together, which makes the technical contribution of method design not very high. The paper should clearly articulate the novelty of the proposed method beyond a simple combination of existing components. What specific adaptations or novel combinations of these techniques lead to improved performance? What are the key insights gained from combining these methods in the proposed architecture? A more detailed discussion of the technical novelty is needed.

Minor comment:
1. The paper contains several typos, and certain sentences are challenging to comprehend.
2. The captions in the graph are too small to read.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new task, called Recent Link prediction, which calls for classifying a graph link that has already occurred. This comes in the context of various industrial applications such as predicting whether a transaction (user node interacting (via an edge) with a credit card node) is fraudulent. The authors formulate the learning task, propose an architecture, an evaluation metric and conduct several experiments.

### Strengths
Pros
* For the most part the paper is well written and provides intuition on the new setting proposed by the authors

* The proposal is backed by several experiments

* The idea is interesting, the contrast with current methods is discussed and the need for the new task is well justified.

### Weaknesses
Cons
* The technical details on the graph profiler are hard to follow, some notation is missing or assumed. Specifically, the dimensions of the weight matrices used in the graph profiler are not explicitly stated, making it difficult to understand the information flow. For example, the input to the profiler is described as a concatenation of node embeddings and edge features, but the transformation of this concatenated vector into the final profile vector is unclear without knowing the dimensions of the intermediate matrices. At the same time the authors explain more basic concepts such as edge homophily using more verbage.

* The evaluation (since it is a novel task) is a bit weak. The analysis relies primarily on the proposed metric, and while the authors discuss the limitations of comparing to other algorithms, the analysis could be enriched by exploring the model performance across different data subsets or by investigating the impact of different hyperparameter settings on the performance. This would provide a more comprehensive understanding of the model's behavior beyond the aggregate results.

* The edge homophily paragraph is dense with notation, which makes the formula hard to digest even though the idea is simple. The use of set notation without clear definitions of the sets involved makes the formula difficult to interpret. A clearer definition of the sets and a more detailed explanation of how the edge homophily is calculated would be beneficial. For example, it is not clear what the set of edges E represents in the context of the graph and how it relates to the set of nodes. 

*  How did you derive the formula for d_1, bottom of p. 4? The derivation is not clear and the motivation is not well explained. 

* Some typos need to be fixed: e.g.

     * p.2 "...temporal graph learning architectures divinding categorizing..."
     * p.4 "...In our specific instance... acting that acts..."

* What is the significance of the TGN modifications in Table 2? They don't seem to be directly related to the proposed method, and their inclusion without explanation makes it difficult to understand their relevance.

### Questions
* Given the datasets/tasks you are describing, it appears that these graphs are knowledge graphs (consisting of entities and relations connecting them). If my understanding is correct, how does this new task relate to the dynamic knowledge graph link prediction? 

* The edge homophily paragraph is dense with notation, which makes the formula hard to digest even though the idea is simple. Please include a sentence (in English) to supplement the formula when defining edge homophily, e.g. "the fraction of edges that connect nodes of the same
class". 

*  Are there other metrics beyond edge homophily that are useful here? Since you don't take the time dimension in the edge homophily, does any other metric make sense for the evaluation of the time component? 

* Please define the matrices you use (and their dimensions), they are sometimes only understood from the context, e.g. in the Profiler Encoder section on p.4 

* How did you derive the formulat for d_1, bottom of p. 4? 

* Some typos need to be fixed: e.g. 

     * p.2 "...temporal graph learning architectures divinding categorizing..."
     * p.4 "...In our specific instance... acting that acts..."
 
* What is the significance of the TGN modifications in Table 2? They don't seem to be directly related to the proposed method.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper formulates the problem of dynamic edge classification and proposes a method for this task and a specific metric for evaluating the performance of this task. Specifically, the proposed metric can handle the case of class imbalance, and the proposed model includes a novel message aggregation schema.

### Strengths
1. The problem of dynamic edge classification is important. 

2. The problem formulation is coherent and well-reasoned.

3. The experiments conducted are thorough, with the authors exploring a wide range of variants.

### Weaknesses
1. The model design is rather conventional and lacks novelty. It adheres to the traditional message-passing framework and introduces event and time-related elements as a simple extension.

2. While the proposed Matthews Correlation Coefficient is effective for assessing classification tasks, it may not fully account for the specific attributes of the problem, particularly in the context of temporal interaction classification. It remains unclear how well it aligns with the temporal and graph-based nature of the problem.

3. It is recommended that the authors provide equations for all modules in the paper to offer a comprehensive understanding of the model. This would be especially beneficial in elucidating model details.

### Questions
1. Is there any novelty in the method design, such as in a specific module or the whole framework?

2. Is there any specific design of the metric for temporal interaction classification?

3. What is the time encoder like?

Please elaborate on the above issues to ensure that I don't miss any contributions in the paper.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper works on edge classification (Recent Link Classification) on dynamic graphs. It uses a metric, Matthews Correlation Coefficient for imbalanced datasets and benchmarks TGN (Rossi et al.,2020) on message aggregation schema, readout layer, and time encoding strategy. It then proposes Graph Profiler, which has better model performance than TGN.

### Strengths
1. Edge classification is an important topic.
2. Introduced critical design principles look helpful for algorithm design.
3. Experiments show Graph Profiler performs better than TGN.

### Weaknesses
1. The reason why Graph Profiler performs better than TGN is unclear. The technical advancement of Graph Profiler is unclear.
2. These critical design principles are different for different datasets, which makes it morel like hyper-parameter tuning for specific datasets.
3. Extensive evaluation (e.g. larger datasets, other models) are needed for validating these critical design principles.

### Questions
1. The motivation of the paper is unclear. If the authors want to highlight the proposed method, it might be better to explain how the design of the Graph Profiler algorithm incorporates these critical design principles.
2. What is the key takeaway for these critical design principles?
3. Do these critical design principles also fit other settings like node classification and future link prediction?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduced recent link classification (RLC), a new inference task on dynamic graphs in addition to temporal link prediction (TLP) and dynamic node classification (DNC), and formalized it as a benchmark downstream task. A new graph profiler method was then introduce to tackle RLC. Moreover, the authors also proposed new quality metrics (e.g., edge homophily and Matthews correlation coefficient). Experiments on a set of dynamic graph datasets preliminaries validated the quality of the proposed method w.r.t. the RLC task.

### Strengths
S1. The idea of treating recent link classification (RLC) as a new benchmark task of temporal graph learning seems interesting.
  
S2. The authors introduced new quality metrics (i.e., edge homophily and Matthews correlation coefficient).

S3. The authors provided the source code of their experiments.

### Weaknesses
 **W1. The motivations of some statements and designs are unclear.**

In Section 1, why the fact that 'FLP is sensitive to non-architectural hyperparameters' can begs a question regarding DNC, i.e., 'in analogy to the dynamic node classification task, is there a temporal link classification task we can define?' From my perspective, the relationships between FLP and RLC are also not fully discussed. At the very beginning of the paper, it is highly recommended to add a toy running example (e.g., a simple dynamic graph) to illustrate what are FLP, DNC, and RLC, as well as their inherent relationships. The current introduction lacks a clear, intuitive connection between these tasks, making the motivation for RLC feel somewhat arbitrary. A concrete example would help clarify why RLC is a necessary addition to the existing landscape of temporal graph learning tasks.
  
In the design of profile encoder, what are the motivations to introduce metapaths? As I known, metapaths are usually used in the graph representation learning of heterogeneous graphs, but it seems that the authors only consider (dynamic) homogeneous graphs in this study. Moreover, metapaths are also not illustrated in Fig. 1 (i.e., the model architecture). The use of metapaths in a homogeneous graph setting is not well-justified, and the lack of visual representation in the model architecture further obscures their purpose. It is crucial to explain why metapaths are beneficial in this context and how they are implemented within the proposed framework.
  
There are no intuitive motivations regarding the proposed metrics of edge homophily and Matthews correlation coefficient (e.g., why Matthews correlation coefficient can handle the label-imbalanced issue). As a results, it is unclear what are their advantages beyond conventional quality metrics. The paper needs to provide a more detailed explanation of why these metrics are appropriate for evaluating RLC, especially in comparison to more established metrics. The advantages of MCC, particularly its ability to handle class imbalance, should be explicitly demonstrated with examples or references.
  
***
  
**W2. The problem statements in Section 3 are unclear and even confusing. Some presentation and statements seem to be inconsistent.**
  
In the 1st paragraph of Section 3, the availability of graph attributes (e.g., inputs of node and edge features) are not mentioned. However, as stated in the 2nd paragraph, edges attributes are treated as inputs of RLC. It is unclear that whether graph attributes (in terms of node attributes/features or edge attributes/features) are considered in this paper. If so, are they assumed to be static (for all time steps) or they are also dynamic? The inconsistent discussion of graph attributes creates confusion about the input data for the proposed method. The paper should clearly state whether node and edge attributes are used, and if so, whether they are static or dynamic. The lack of clarity on this point makes it difficult to understand the practical application of the method.
  
At the very beginning of Section 3, it is suggested to highlight which data model (i.e., discrete-time dynamic graph or continuous-time dynamic graph) that the authors adopted in this paper. The paper should explicitly state whether it is using a discrete-time or continuous-time dynamic graph model. This choice has significant implications for the design of the method and the interpretation of the results.
  
The formal definitions of FLP and DNC are not given. For both FLP and DNC, there are transductive and inductive settings. The formal definitions regarding the transductive and inductive of RLC are not given. It is also unclear that the authors only consider the transductive setting or both transductive and inductive settings. The lack of formal definitions for FLP, DNC, and RLC, as well as their transductive and inductive settings, makes it difficult to compare the proposed method with existing approaches. The paper should provide clear definitions for all tasks and specify the setting used in the experiments.

'Profile' is a significant concept in the proposed method, e.g., profile encoder, node profile, etc. However, there seems no definition regarding this concept (e.g., what are profiles in real dynamic graphs and in terms of what). The term 'profile' is used extensively but lacks a clear definition, making it difficult to understand its role in the proposed method. The paper should provide a formal definition of 'profile' and explain how it is derived from the dynamic graph data.

According to the statements in Section 3, each edge in a (dynamic) graphs should be associated with a time step. However, the graphs in Fig. 1 and Fig. 2 seem to be static. Furthermore, edge attributes are also not illustrated in Fig. 1 and Fig. 2. The figures do not align with the description of dynamic graphs, and the lack of edge attributes in the figures further contributes to the confusion.

***

**W3. Experiments are too simple. Some details regarding experiment settings are also unclear.**

In experiments, there are only two baseline methods (i.e., TGN and GraphMixer), which cannot fully validate the superiority of the proposed method. In addition to the two baselines, there are also some other dynamic graph representation learning methods (e.g., TGAT, DySAT, EvolveGCN, etc.) as mentioned in Section 2 that can be included in experiments. Experiment results of GraphMixer are not given in Table 3, Fig. 4, etc. The limited number of baselines makes it difficult to assess the performance of the proposed method. The paper should include a more comprehensive set of baselines, including those mentioned in Section 2, to provide a more robust evaluation. The absence of GraphMixer results in Table 3 and Fig. 4 is also a significant oversight.

In Table 1, the number of timesteps and the number of classed are not given for each dataset. The quality metric w.r.t. the results in Table 3 is not mentioned in the caption. The lack of detailed information about the datasets and the evaluation metrics makes it difficult to reproduce the experiments and interpret the results. The paper should provide complete information about the datasets, including the number of timesteps and classes, and clearly state the evaluation metric used in Table 3.
  
***

**W4. The major contributions of this paper are unclear and not fully verified.**
  
Although the authors claimed that they proposed a new temporal graph learning task (i.e., RLC) and new quality metrics (i.e., edge homophily and MCR), their advantages beyond existing techniques (e.g., what are the advantages of treating RLC as a new temporal graph learning task beyond FLP and DNC) are not fully discussed in the paper and not fully validated in experiments, due to the unclear motivations and insufficient experiments. The paper fails to clearly articulate the advantages of RLC over FLP and DNC. The lack of a clear motivation for RLC and the insufficient experimental validation make it difficult to assess the significance of the proposed task and metrics.

***

**W5. The overall presentation is poor. In addition to the inconsistent presentation mentioned before, there are also some grammatical errors and typos that need careful revisions.**

1) 'analyze the temporal graph learning architectures divindign categorizing the methods literature into two groups'

2) 'edges$\mathcal{E}$'

3) 'we construct derived graphs that'

4) 'connect a vertex acting that acts as a source to another that acts as a course through a shared destination vertex'

5) 'on abuse-like like datasets'

### Questions
See W1, W2, and W4.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
