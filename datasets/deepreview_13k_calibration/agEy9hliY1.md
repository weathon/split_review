# Unveiling Neural Combinatorial Optimization Model Representations Through Probing

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Neural combinatorial optimization (NCO) models have achieved remarkable performance, yet their learned underlying representations remain largely unclear. This hinders real-world application, as industrial stakeholders may want a deeper understanding of NCO models before committing resources. In this paper, we make the first step towards interpreting NCO models by investigating embeddings learned by various architectures through three probing tasks. Specifically, we analyze representative and state-of-the-art attention-based models, including AM, POMO, and LEHD, on the representative Traveling Salesman Problem and Capacitated Vehicle Routing Problem. Our findings reveal that NCO models encode linear representations of Euclidean distances between nodes, while also capturing additional knowledge that help avoid making myopic decisions. Furthermore, we show that architectural choices affect the ability of deep models to accurately represent Euclidean distances and to incorporate non-myopic decision-making strategies. We also verify to what extent NCO models understand the feasibility of constraints. Our work represents an initial effort to interpret NCO models, enhance understanding of why certain architectures outperform others, and demonstrate probing as a valuable tool for analyzing their internal mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the novel use of probing techniques to interpret neural combinatorial optimization (NCO) models, particularly in the context of Traveling Salesman Problem (TSP) and Capacitated Vehicle Routing Problem (CVRP). The study aims to reveal the internal representations learned by three attention-based NCO models (AM, POMO, and LEHD). Through three distinct probing tasks, the authors assess each model's ability to perceive Euclidean distances, avoid myopic decisions, and handle capacity constraints. The findings highlight LEHD's superior performance in capturing decision-supporting information, which aligns with its structure featuring a light encoder and heavy decoder, as opposed to AM and POMO's heavy encoder-light decoder designs.

### Strengths
1)The application of probing techniques to NCO models is innovative, offering fresh insights into model interpretability.

2)The study is well-structured, with clear, contextualized findings that contribute to understanding NCO models.

3)The insights derived from probing tasks provide practical implications for NCO model design, particularly in enhancing decision-making and handling constraints.

### Weaknesses
W1. This paper can be considered as an analysis paper. In other words, this paper does not propose a novel idea for advancing NCO models.

W2. The probing tasks introduced in this paper mainly focuses on routing problems such as TSP (Traveling Salesman Problem), and CVRP (Capacitated Vehicle Routing Problem). However, there are many other CO problems like Knapsack and FFSP (Flexible Flow Shop Problem).

W3. Overall, this paper is well-written. However, it would be better to present more analysis results (in the Appendix) in the main sections, by slightly reducing the description of probing tasks.

### Questions
1)In the ablation study section of the original LEHD paper, the authors discuss the impact of different training methods on model performance. I suggest adding ablation studies to further support your experimental results.

2)In Section 2, Probing Task 1, what are the specific implementation details of the proxy embedding?

3)In Table 1, Task 1 w/o ints., the R2 scores for AM and POMO are around 0.2. However, this lacks a reference point, making it difficult to gauge the model's learning degree for the Euclidean distance perception task. I suggest including randomly initialized, untrained versions of these models or models at various stages of training as a baseline for comparison. This would help demonstrate how the model's ability to perceive distance evolves over the training process.

4)In Table 1, some values are missing for Task 3. What is the reason for this?

5)In Lines 364-369, the description of the input for Task 3 is unclear. For the w/ints input, is it only [ hi ⊙ hj ]or [ hi , hj , hi⊙hj ]? In Table 5, you indicate it is the latter, but the text seems to suggest the former.

### Soundness
2

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
This paper provides analysis results of state-of-the-art attention-based neural combinatorial optimization (NCO) models. Specifically, this paper investigates embeddings learned by various architectures by proposing tree probing tasks. Probing task 1 examines whether the embeddings of NCO models can encode the Euclidean distance between nodes. Probing task 2 checks if the embeddings of NCO models can enable the ability to avoid myopic decisions to fine a global optimal solution. Probing task 3 tests whether the embeddings of NCO models can capture constraints in CO problems. For each probing task, this paper constructs a dataset, and trains a probing model on each dataset. This paper mainly analyzes two NCO architectures: (1) AM and POMO, and (2) LEHD (light encoder heavy decoder). The experiment results show that LEHD provides higher probing scores than AM and POMO, meaning that it embeddings are better in terms of (1) perception of Euclidean distance, (2) avoidance of myopia, and (3) perception of constraints.

### Strengths
S1. It is very interesting that the authors empirically show that the embeddings of LEHD capture better information than AM and POMO models.

S2. It seems that the authors properly design three probing tasks to examine the important abilities of high-performing NCO models.

### Weaknesses
 - Chosen architectures can handle only Euclidean TSP and CVRP. As a result, the probing tasks are too simple. The most interesting question is how NCO models represent and handle constraints, but the only constraint in this study is the simple capacity constraint of CVRP in probing task 3. Even with this simple constraint, there is no clear answer - the conclusion is that NCO models "likely" rely on masking. It would be valuable to apply the same approach to more complex CO problems with additional constraints, such as CVRP with time windows or JSSP (to probe precedence constraints).

- The answer to probing task 2 "whether the NCO models exhibit the ability to avoid shortsighted decisions at a given step" is trivial. All NCO models perform better than a greedy search, so it is clear that they **have** the ability to avoid myopic decisions. However, the main question is **how** they do that, but this study does not provide an answer. This still remains inside a black box. I think these simple probing tasks are not sufficient to provide an answer; deeper analysis is required. This could involve analyzing attention patterns or investigating specific steps where the models significantly deviate from greedy choices.

- A simple linear connected layer may not be powerful enough to extract relevant knowledge from embeddings. If the fully connected layer does not accurately predict a probing task, it does not necessarily mean that there is no relevant knowledge — it could mean that it is difficult to detect the relationships between embeddings, and a more powerful network may find them. 

- Experiments show that there is no correlation between probing tasks and the final performance of the model.

### Questions
Q1. The datasets and models for probing tasks in this paper can help researchers and practitioners. Are the authors planning on making the datasets and models public?

### Soundness
2

### Presentation
2

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
This study explores the interpretability of neural combinatorial optimization (NCO) models by analyzing the embeddings learned by various architectures through three probing tasks. It reveals that the NCO models encode Euclidean distances between nodes while also capturing additional knowledge to avoid myopic decisions. Furthermore, this research demonstrates that probing is a valuable tool for analyzing the internal mechanisms of these models.

### Strengths
The paper effectively incorporates domain knowledge from the field of combinatorial optimization to construct probing tasks that assist in the interpretability analysis of NCO models.
2.  The paper successfully applies probing techniques from the NLP field to the study of NCO model interpretability.

### Weaknesses
Major Weaknesses:
1.	The manuscript lacks sufficient details about the applied probing models, making the experimental results unconvincing. For instance, in line 236, the authors indicate that they trained a simple linear fully connected network as a probing model. However, they do not provide information on the construction of the training set and specific training procedures. Additionally, there is no clarification on how the probing models accommodate inputs of differing dimensionalities.
2.	The experimental content is inadequate to support the authors' conclusions:
a)  The claim that LEHD outperforms HELD due to "LEHD’s recalculation of the embeddings" (line 407) is not substantiated. This is because Table 1 only includes the AM-Enc-w/c and AM-Enc-w/g cases and does not provide results for POMO-Enc-w/c and POMO-Enc-w/g.
b)  Regarding the impact of increasing model layers on performance, the analysis of the HELD models are limited to layers l1 and l3, neglecting results for layer l2.
c)  The conclusion that recalculation enhances the performance of the NCO model (line 409) is solely based on experiments with the LEHD model. However, there are no corresponding results provided for the HELD model.
Minor Weaknesses:
1.	In constructing the dataset for probing task 2, the authors introduce constraints to avoid multiple optimal solutions. However, in line 175, they state that "the new optimal solution obtained under this constraint is worse than the original solution without the constraint," which undermines the dataset's credibility.
2.	In the analysis of the TSP task, the authors conclude that "the ability of the embeddings to perceive Euclidean distances decreases as the number of attention layers increases in all three models" (line 432). Conversely, they also state that “deeper layers enhance the embeddings' ability to avoid myopic decision-making” (line 466).  This presents a contradiction regarding the effects of attention layer depth on embedding performance.
3.	Many evaluation metrics used in the experimental section, such as MSE, RMSE, and R², are unnecessary as their positive or negative correlations are evident.
4.	One of the primary models analyzed, AM, is cited from arXiv and dates back to 2018, making it relatively outdated (line 577).

### Questions
1.	How do you train and use a probing model on the regression and classification tasks?
2.	What’s the performance of POMO-Enc-w/c and POMO-Enc-w/g? Moreover, please compare it with the LEHD models.
3.	What’s the performance of AM-Enc-l2 and POMO-Enc-(l2-l5)?
4.	Can recalculating node embeddings methods enhance the performance of HELD models, i.e., AM and POMO?
5.	How does the domain constraints to probing task 2 affect the quality of constructed dataset?
6.	For the TSP task, what layer model should we use: a deeper one or a shallower one?

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
4

### Summary
The paper introduces the use of a well-known technique, probing, in the analysis of NCO models. Specifically, it introduces three probing tasks for Euclidean routing CO problems and applies them to analyze the embeddings of three NCO models applied to solving TSP and CVRP.

### Strengths
- Probing is novel in the NCO domain and could potentially help understand the internal mechanisms of NCO models.
- The idea of performing probing at different positions within the network seems very useful, it can help to understand how embeddings are transformed across layers.
- The paper is very well-written and easy to understand.

### Weaknesses
- Chosen architectures can handle only Euclidean TSP and CVRP. As a result, the probing tasks are too simple. The most interesting question is how NCO models represent and handle constraints, but the only constraint in this study is the simple capacity constraint of CVRP in probing task 3. Even with this simple constraint, there is no clear answer - the conclusion is that NCO models "likely" rely on masking. It would be valuable to apply the same approach to more complex CO problems with additional constraints, such as CVRP with time windows or JSSP (to probe precedence constraints).

- The answer to probing task 2 "whether the NCO models exhibit the ability to avoid shortsighted decisions at a given step" is trivial. All NCO models perform better than a greedy search, so it is clear that they **have** the ability to avoid myopic decisions. However, the main question is **how** they do that, but this study does not provide an answer. This still remains inside a black box. I think these simple probing tasks are not sufficient to provide an answer; deeper analysis is required. This could involve analyzing attention patterns or investigating specific steps where the models significantly deviate from greedy choices.

- A simple linear connected layer may not be powerful enough to extract relevant knowledge from embeddings. If the fully connected layer does not accurately predict a probing task, it does not necessarily mean that there is no relevant knowledge — it could mean that it is difficult to detect the relationships between embeddings, and a more powerful network may find them. 

- Experiments show that there is no correlation between probing tasks and the final performance of the model.

### Questions
Related to the concerns mentioned above, I have additional questions/remarks:

1. I suggest trying a more powerful network for the prediction of probing tasks and comparing the results with those obtained from simple linear models. This would certainly eliminate any doubt about the inefficiency of the FC network.

2. The variety of architectures should be enriched. POMO and AM, in fact, share the same architecture, while LEHD uses a very similar attention-based architecture with a difference in the decoder. This work would be much more impactful if it also applied probing techniques to some of the recent transformer-based models designed to handle edge features within the model, like [1], [2], or some similar approach for non-Eucledian routing problems. It will be valuable to how these models preserve (or forget) distance information, which is provided explicitly. Are there any limitations or challenges to applying your method to more complex architectures?

3. Experiments show that POMO performs worse than AM in capturing the capacity constraint (at the end of the encoder, R² values are 0.87/0.13 vs. 0.96/0.72, respectively). However, when we compare the overall results of POMO and AM (in terms of optgap), POMO performs twice as well as AM. Given this, what is the background for the claim in line 493 that "we should integrate the constraint-related information into deeper layers"? Will it really help in better decisions, or maybe degrade performance? Can we conclude from the experiments for POMO/AM/LEHD that "forgetting capacity constraints" is useful for decision-making or not? 

4. The motivation for using an interaction term in the experiments remains unclear to me. While it is true that "some NCO models concatenate embeddings..." none of the models in this study do so.

5. Why are some values missing from Table 1 / Probing task 3? Esp. POMO-Enc-l1,6 for 20 nodes are missing, while the same values for 100 nodes exist.

[1] Kwon et al. Matrix Encoding Networks for Neural Combinatorial Optimization, NeurIPS 2021

[2] Drakulic et al. GOAL: A Generalist Combinatorial Optimization Agent Learning, arXiv:2406.15079

### Soundness
2

### Presentation
3

### Contribution
2
