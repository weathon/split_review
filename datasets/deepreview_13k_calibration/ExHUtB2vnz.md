# INFER: A Neural-symbolic Model For Extrapolation Reasoning on Temporal Knowledge Graph

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Temporal Knowledge Graph(TKG) serves as an efficacious way to store dynamic facts in real-world. Extrapolation reasoning on TKGs, which aims at predicting possible future events, has attracted consistent research interest. Recently, some rule-based methods have been proposed, which are considered more interpretable compared with embedding-based methods. Existing rule-based methods apply rules through path matching or subgraph extraction, which falls short in inference ability and suffers from missing facts in TKGs. Besides, during rule application period, these methods consider the standing of facts as a binary 0 or 1 problem and ignores the validity as well as frequency of historical facts under temporal settings.
In this paper, by designing a novel paradigm for rule application, we propose INFER, a neural-symbolic model for TKG extrapolation. With the introduction of Temporal Validity Function, INFER firstly considers the frequency and validity of historical facts and extends the truth value of facts into continuous real number to better adapt for temporal settings. INFER builds Temporal Weight Matrices with a pre-trained static KG embedding model to enhance its inference ability. Moreover INFER adopts a rule projection module which enables it apply rules through conducting matrices operation on GPU, which improves the efficiency of rule application. This feature also facilitates potential integration with existing embedding-based methods.
Experimental results show that INFER achieves state-of-the-art performance on three datasets and significantly outperforms existing rule-based models on our modified, more sparse TKG datasets, which demonstrates the superiority of our model in inference ability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces INFER, a neural-symbolic approach to temporal knowledge graph extrapolation.  INFER  uses a Temporal Validity Function that captures how frequently facts occur, as well as their validity over time using continuous values. INFER uses pre-trained static knowledge graph embeddings to construct Temporal Weight Matrices. A rule projection module that reformulates rule application as matrix operations. 
The paper evaluates INFER's effectiveness using three ICEWS datasets. When tested on modified sparse temporal knowledge graph datasets, INFER shows promising inference capabilities. These results highlight that INFER's combination of continuous temporal validity scoring and GPU-optimized rule application offer useful techniques for temporal knowledge graph reasoning.

### Strengths
1. The paper introduces a new scoring mechanism for temporal rule validity.  Alternate techniques in the literature appear to be more complicated.

2. The paper evaluates differentiable rule-based inference systems across several ICEWS datasets, providing a demonstration of these systems on temporal knowledge graphs that represent time in event "timestamp" form.

### Weaknesses
1. The author's claimed novelty rests on acceleration of rule-based processing using matrix operations on a GPU.  This is common in differentiable rule-learning systems, apparently first introduced as TensorLog, with associated inductive learning system Neural-LP, see e.g. [1].

2. The paper claims: "Experimental results show that INFER achieves state-of-the-art performance on three datasets and significantly outperforms existing rule-based models on our modified, more sparse TKG datasets, which demonstrates the superiority of our model in inference ability." The authors should consider that both embedding based and rule based systems can perform quite well relative to the methods they compare against.  For instance, consider the following comparison with TimePlex [2]:

| | ICEWS14 | ICEWS14 | ICEWS14 | ICEWS05-15 | ICEWS05-15 | ICEWS05-15 |
|--------|---------|-----|---------|----------|---------|-----|
| Method | MRR | HITS@1 | HITS@10 | MRR | HITS@1 | HITS@10 |
| TimePlex | **60.40** | **51.50** | **77.11** | **63.99** | **54.51** | **81.81** |
| INFER | 44.09 | 34.52 | 62.14 | 48.27 | 37.61 | 68.52 |

The table below illustrates the methods similar to those compared in this paper evaluated on wikidata and yago data sub-sets.  The table also includes a rule-based method (TILP [3]) that is demonstrated to perform on par with Timeplex, illustrating that the performance gap between TimePlex and INFER show above may not be limited to embedding based methods.                                                                                   

| | WIKIDATA12k | WIKIDATA12k | WIKIDATA12k | YAGO11k | YAGO11k | YAGO11k |
|--------|---------|-----|---------|----------|---------|-----|
| Method | MRR | HITS@1 | HITS@10 | MRR | HITS@1 | HITS@10 |
| TLogic | 0.2536 | 0.1754 | 0.4424 | 0.1545 | 0.1180 | 0.2309 |
| ComplEx | 0.2482 | 0.1430 | 0.4890 | 0.1814 | 0.1146 | 0.3111 |
| TA-ComplEx | 0.2278 | 0.1269 | 0.4600 | 0.1524 | 0.0936 | 0.2626 |
| DE-SimplE | 0.2529 | 0.1468 | 0.4905 | 0.1512 | 0.0875 | 0.2674 |
| TimePlex | **0.3335** | 0.2278 | **0.5320** | 0.2364 | **0.1692** | 0.3671 |
| TILP | 0.3328 | **0.2342** | 0.5289 | **0.2411** | 0.1667 | **0.4149** |

### Questions
1. How does your acceleration method differ in nature from TensorLog and Neural-LP?
2. Many methods have developed from the Neural-LP approach.  How does your method compare to those?
3. Why do you not compare to TimePlex as the state of the art method that has been demonstrated on these ICEWS datasets?
4. Can the gap in performance with TimePlex and rule-based sysetsms be explained in terms of the differences between timestamp and interval-time objectives of different temporal knowledge graph methods?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The article presents a detailed neuro-symbolic model addressing the task of Temporal Knowledge Graph Completion, particularly focusing on the challenge of extrapolation. This task aims to infer knowledge for a given Knowledge Graph at time T using only past data. The authors propose a well-structured solution, providing an extensive evaluation that compares their model to current state-of-the-art symbolic and neural methods.

### Strengths
1. Comprehensive Evaluation: The paper includes a thorough evaluation of the proposed model, supplemented by an ablation study and an efficiency analysis, making it easy to understand the model's effectiveness.
2. Efficient Model Design: The model circumvents the common complexity issue of creating separate matrices per timestamp, resulting in a compact, efficient design.
3. Clear and Reproducible Description: The methodology is well-articulated, allowing for straightforward reproduction of the results.

### Weaknesses
1. Minor Typos and Inconsistencies:
   - Line 451/452: The term "INFER(Temp)" is used instead of "INFER(Temp Val)."
   - Line 515: The rule quantity is stated as 40, while Table 1 lists it as 60, which could lead to some confusion.
2. Efficiency Study Observations: The conclusions drawn in the efficiency study are somewhat unclear. Specifically, a competing model achieving a similar score while exploring fewer candidates might suggest that the alternative approach is better optimized in its candidate selection process. The paper does not sufficiently analyze why exploring significantly more candidates leads to better performance, especially given the increased computational cost. A more in-depth analysis of the trade-offs between candidate exploration and computational efficiency is needed.
3. Completeness of Graph Argument: The argument concerning graph completeness and the slope behavior appears overstated. While the authors suggest their method is more robust to missing facts, the trend lines for the three methods in Figure 4 are quite similar, showing comparable performance degradation as the graph completeness decreases. The claim that the slope of the proposed method is significantly gentler, especially on ICEWS18, needs more rigorous justification, possibly with statistical significance tests.
4. Ambiguity in Section 4.3.3: The fourth paragraph lacks clarity regarding "variable constraints in rules," which limits the reader's understanding of the approach. The explanation is too abstract, and a concrete example illustrating how these constraints are implemented and affect the rule matching process is missing. This makes it difficult to assess the novelty and impact of this aspect of the model.

### Questions
1. In Section 4.3.2, the function $V(s, r, o, t_c)$ is introduced. However, it is unclear how the model handles $t_{last}$ if the fact $<s, r, o>$ was never previously observed. Is the value set to 0, potentially conflicting with timestamp 0, or is another value assigned?
2. Could the authors elaborate on the benefits of examining a significantly higher number of candidates (100x), especially given the notable increase in runtime (an additional 500 seconds)? Understanding the trade-offs would be helpful.

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
To solve the problem that rule-based methods in the field of temporal knowledge graph inference have insufficient reasoning ability when graph facts are missing, and the fact state is simply considered as binary, ignoring the validity and frequency of historical facts, this paper proposes the neural symbol model of INFER, which quantifies fact credibility in time dimension by introducing a time validity function. At the same time, the time weight matrix is introduced so that the model can infer the missing facts and deal with the incompleteness of the map. And to improve the efficiency of rule reasoning, a rule projection module is proposed, which uses GPU-based matrix operation instead of traditional path matching.

### Strengths
(1) This paper introduces effective means such as the time validity function to quantify fact credibility in the time dimension and proves its effectiveness through experiments, which provides ideas for how to improve the reasoning ability of rule-based methods in dealing with incomplete graphs.
(2) The average performance of the experiment is good on multiple datasets, and the self-made TKG data with sparse facts is obtained. The experimental results show that the INFER model is significantly better than other methods when the facts are sparse.
(3) The chart is clear, the paper is completed with a high degree, and it is easy to interpret.

### Weaknesses
 (1) The Design of the time validity function: The time validity function proposed in this paper calculates the time weight of historical facts based on the time interval and frequency of fact occurrence. Although the above two terms are considered at the same time, the function form is relatively fixed and more dependent on experience. The specific form of the square root decay and the linear frequency term lacks a strong theoretical basis, and the model's sensitivity to the parameters of this function is not discussed. Adapting the attenuation rate using data-driven methods may enhance the model's adaptability. 
(2) The performance of the model on the ICEWS05-15 dataset does not exceed that of TECHS, and there is no detailed analysis of the results in this paper. It is unclear whether the rule learning process or the rule application process is the bottleneck on this dataset. Furthermore, the paper does not discuss the impact of data sparsity on the performance of the proposed method, which is particularly relevant given the long time span of the ICEWS05-15 dataset.
(3) The rule projection module used by INFER loses the ability to directly model the sequence of facts to a certain extent, which may affect the accuracy in scenarios requiring strict time order or multi-jump reasoning. The paper lacks a detailed analysis of how the model performs with rules of varying lengths, and whether the model's performance degrades as the rule length increases. Additional experiments are needed for evaluation, especially for long rule samples with variable constraints. 
(4) INFER introduces neural network embedding and complex matrix operations, and although the authors show entity scores when the rules are applied, it still damages the interpretability of the traditional rule model to some extent. The paper does not provide a clear mechanism to trace back the reasoning path and identify which specific facts contribute to the final prediction, which is a key aspect of interpretability in rule-based systems.

### Questions
(1) Is the use of the square root form of the time decay term in the time validity function based on the conclusions obtained from experiments?
(2) What is the additional overhead if you replace the static embedded model with a time-embedded model? And What's the performance boost?
(3) When calculating the rule confidence, the INFER model adopts the rule learning algorithm in TRRules. The rule base retains only cyclic rules and filters out acyclic rules. TR-Rules uses acyclic rules and proves its effectiveness. What is the reason for filtering acyclic rules here? Is there any experimental support?
(4) Does the static embedding model provide the same level of confidence for the same fact at different time points?
(5) How does INFER's rule projection module perform when dealing with rules of different lengths?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces INFER, a neural-symbolic model designed for Temporal Knowledge Graph (TKG) extrapolation reasoning. Traditional rule-based methods for TKGs, though interpretable, struggle with temporal reasoning as they treat facts as binary and ignore temporal frequency and validity. NFER addresses these issues through a Temporal Validity Function, which enables continuous truth values and models the frequency and validity of historical facts for better temporal adaptation. Additionally, INFER incorporates Temporal Weight Matrices with a pre-trained static KG embedding model to improve inference quality. A rule projection module enhances computational efficiency by leveraging GPU-optimized matrix operations, allowing INFER to scale effectively and integrate with embedding-based approaches. Experiments show that INFER achieves state-of-the-art results on several datasets, demonstrating enhanced inference capabilities over existing models, particularly in sparse TKG settings.

### Strengths
1.   Temporal Knowledge Graph (TKG) reasoning is an important  research topic.
 2.   The proposed method shows better results compared to existing rule-based methods.

### Weaknesses
1.  The motivation behind the method design is unclear, and the description lacks clarity. For example, in Section 4.3.3, the rationale for the rule projection strategy is not well-explained, and the meanings of terms like “Ans_i” and “Ans” are not clarified.
2.  Limited novelty. The techniques used in the proposed method do not introduce significant innovations.
3.  The temporal and spatial complexity of the inference process appears high, which might impact practical applicability. It would be beneficial to provide an analysis of the computational complexity.
4.  Some experimental details are insufficiently explained. For example, in Line 426, the phrase “traditional binary truth values for historical facts” needs further clarification. It is unclear what specific criteria or methods are used to assign these binary truth values to historical facts.
5.  The dataset coverage is insufficient. The paper only uses the ICEWS dataset, which belongs to a specific category of TKG data. It would be valuable to include additional datasets like WIKI or GDELT to demonstrate the method’s generalizability across different data types.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
