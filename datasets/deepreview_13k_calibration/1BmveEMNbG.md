# Rethinking Complex Queries on Knowledge Graphs with Neural Link Predictors

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Reasoning on knowledge graphs is a challenging task because it utilizes observed information to predict the missing one. Particularly, answering complex queries based on first-order logic is one of the crucial tasks to verify learning to reason abilities for generalization and composition.
Recently, the prevailing method is query embedding which learns the embedding of a set of entities and treats logic operations as set operations and has shown great empirical success. Though there has been much research following the same formulation, many of its claims lack a formal and systematic inspection. In this paper, we rethink this formulation and justify many of the previous claims by characterizing the scope of queries investigated previously and precisely identifying the gap between its formulation and its goal, as well as providing complexity analysis for the currently investigated queries. Moreover, we develop a new dataset containing ten new types of queries with features that have never been considered and therefore can provide a thorough investigation of complex queries. Finally, we propose a new neural-symbolic method, Fuzzy Inference with Truth value (FIT), where we equip the neural link predictors with fuzzy logic theory to support end-to-end learning using complex queries with provable reasoning capability. Empirical results show that our method outperforms previous methods significantly in the new dataset and also surpasses previous methods in the existing dataset at the same time.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses neuro-symbolic execution of knowledge graph queries. The authors use a graph representation of a symbolic (first order logic) query, and for potentially incomplete knowledge graphs, the authors propose FIT, an algorithm to compute the answer to a query in a message-passing type of algorithm over the query graph, with probabilities of all possible relations. They argue that tree-form queries cannot represent queries with existential leaves, so they cannot cover the full space of first order logic. They show experiments where FIT outperforms existing query graph execution approaches on 10 sampled query types from 3 KGs.

### Strengths
1. For incomplete knowledge graphs, proposed algorithm FIT is essentially a custom message-passing algorithm over nodes and edges computing the probability of every possible relation and updating the neighboring node probabilities accordingly to reach the answer set. It may have the advantage of staying faithful to the allowed relations or combinations from the query graph and KG, since it builds the solution by exploring only those combinations, and using back-propagation to update the values from the actual answer.

2. The experiments confirm improvements over existing first order logic neuro-symbolic methods for computing the answer set.

### Weaknesses
1. Baselines - Graph neural networks (based on message passing and backprop over the query graph) is likely a baseline to consider, since this follows a more controlled message passing approach to the solution. This was not considered in the paper. The overall performance in mean reciprocal rank is still low (~30) in two of the datasets. What would explain the difficulty or effectiveness in those cases?

2. Presentation - The computation of the Cu(node) from the probability of the relations, is not provided in the paper (It should be in the main paper, not the appendix, to allow for key aspects to be presented as a whole). The introduction could be clearer about how or why this fuzzy approach (or neural symbolic approach) is required for incomplete KGs. Are there other benefits of it?

3. The proof for tree-form not capturing all first order logic queries I am not sure about. The authors suggest that existential leaves cannot be represented, but that does not prove that any FOL query could not be converted into a potentially different tree form structure.

### Questions
See weaknesses section.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper has 2 main contributions:

1. Describing the gaps in EFO1 queries studied by past work
- Past work [1] has studied a subset of existential first-order logic queries on knowledge graphs (KGs). In particular, past work has studied tree-form queries with negated atomic relations
- Authors point out that the studied query types do not entirely cover the EFO1 query family and describe the missing families of query structures
- They create a dataset Real-EFO1 that consists of EFO1 query structures not studied by past work and benchmark competitive graph query execution approaches

2. Proposing a fuzzy-logic based approach for executing EFO1 queries on knowledge graphs
- Authors propose a fuzzy-logic based query execution algorithm Fuzzy Inference with Truth values (FIT)
- The algorithm extends QTO proposed by [2] in the following ways:
    - It extends QTO to handle cycles in the query graph
    - It sparsifies the neural link prediction matrices to improve the run-time complexity of the algorithm for certain query types
    - It demonstrates that the link predictor can be trained end-to-end directly with the query execution training data

[1] Hongyu Ren and Jure Leskovec. Beta embeddings for multi-hop logical reasoning in knowledge graphs. NeurIPS 2020
[2] Yushi Bai, Xin Lv, Juanzi Li, and Lei Hou. Answering Complex Logical Queries on Knowledge Graphs via Query Computation Tree Optimization. ICML 2023

### Strengths
1. The paper clearly describes differently query families and establishes the query structures that are missing from past work
2. The proposed Real-EFO1 dataset extends the family of query structures studied in the query execution literature with intuitive examples and connections to past work
3. The proposed FIT approach shows consistent improvement over the baseline approaches and is properly ablated
    - Experiments show that FIT reduces to QTO under the appropriate conditions and that the additional differences lead to performance improvements across all settings
    - Examples show how past approaches (designed for tree-form queries) cannot easily handle the new query structures while fuzzy inference can handle them

### Weaknesses
1. I believe that the paper misunderstands the definition of tree-form queries used by [1]
    - [1] explicitly limit their definition of tree-form queries to only consider the negation of individual atomic formulae (i.e. they consider queries can by build from a query tree using $r(x, y)$ and $\neg r(x, y)$. Therefore, the problem of introducing universal quantifiers is avoided by [1]
    - However, definition 8 in this paper uses a different (broader) definition of tree-form queries. Under this new definitions, tree-form queries could require universal quantification and fall outside the EFO1 category
    - I believe this mismatch shakes some of the grounded for Section 3 (Section 4 is still valid in my opinion, since it tries to describe EFO1 - TF)
    - Specifically, the paper claims that [1] does not cover all EFO1 queries, but this claim is based on a different definition of tree-form queries than the one used by [1]. The paper should explicitly acknowledge this difference in definitions and justify why their definition is more appropriate for the problem of EFO1 query execution, especially since [1] explicitly designed their approach to avoid universal quantification.
2. The connections between FIT and QTO are not sufficiently stressed in the main paper (and this analysis is pushed to the Appendix)
    - I believe that making this connection is important for a fair comparison to QTO
    - The paper should include a more detailed discussion of how FIT extends QTO in the main paper, highlighting the specific modifications and their impact on performance. This would help the reader understand the novelty of the proposed approach and its relationship to existing methods.


### Questions
Questions
---
1. I would like to reiterate Weakness 1 described above. I believe that the definition of tree-form queries used in this work differs from the definition used by past work and that the mismatch makes Section 3 obsolete. Please comment.

Typos
---
1. (Important) Definition 6: Missing definition of EFO1 query family

Suggestions
---
1. Eq 4: It would be good to have an intuitive definition of k here
2. Overall, the paper pushes a lot of context to the Appendix. It would be helpful if the main paper summarized the corresponding Appendix section rather than just point to it

### Soundness
2 fair

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper shares author's rethinking over complex queries on knowledge graph with neural link predictor especially towards answering EFO_1 queries. Authors discussed the difference between previous widely researched tree-form queries and EFO_1 queries and their relationships, and pointed out that the tree-form queries are with unrigorous formulations. Thus they propose to pull the complex query answering research back to answering EFO_1 queries with rigorous formulations, and propose a method with neural link predictor based on fuzzy logic theory, called FIT. FIT outperforms baselines significantly in the new EFO_1 query dataset and also surpasses baselines in the existing dataset at the same time.

### Strengths
1. Authors rethink complex queries on KGs with theoretical analysis. 
2. A new EFO_1 dataset are created to evaluate the EFO_1 query answering task. 
3. And the proposed method FIT shows good performance over EFO_1 datasets and existing tree-form datasets.

### Weaknesses
The basic idea of the new proposed method is based on fuzzy logics and neural link predictor. This general idea is also introduced in FuzzQE[1]. But the key difference between FIT and FuzzQE is not clearly discussed and FuzzQE is not compared in Table 2.  


### Questions
1. Should the $r_1$ and $r_2$ be exchanged in Equation (3)? i.e. Should Equation (3) be $\forall x. (r_3(b, y) ∧ ¬r_2(x, y)) ∨ (r_3(b, y) ∧ ¬r_1(a, x))$ ?
2. What is main difference between FuzzQE and FIT?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenging task of reasoning on knowledge graphs using neural link predictors. The prevailing method in this field is query embedding, which treats logic operations as set operations and has shown empirical success. However, the paper argues that many claims made in previous research lack a formal and systematic inspection. To address this, the authors characterize the scope of previously investigated queries, identify the gap between the formulation and the goal, and provide complexity analysis for the queries. They also introduce a new dataset with ten new types of queries and propose a new neural-symbolic method called Fuzzy Inference with Truth value (FIT) that combines neural link predictors with fuzzy logic theory. The empirical results demonstrate that FIT outperforms previous methods significantly in the new dataset and also surpasses previous methods in the existing dataset.

### Strengths
1. The paper shows many different opinions against previous series of works. The discussion firmly supports that TF query family is not even a subset of EFO1. In addition, the paper rethinks the traditional claim that “reasoning involves an exponential growth in computational time”. The proposition and analysis finally found that the Tree-Form EFO1 reasoning complexity is linear to the number of variables in the query.
2. The paper provides a comprehensive analysis of the prevailing method of query embedding and its limitations. It identifies the gap between the formulation and the goal, which adds clarity to the field and helps in understanding the limitations of existing approaches.
3. The introduction of a new dataset with ten new types of queries is a significant contribution. This dataset allows for a thorough investigation of complex queries and provides a benchmark for evaluating future methods.
4. The proposed method, FIT, which combines neural link predictors with fuzzy logic theory, is a novel approach. It addresses the limitations of previous methods and demonstrates improved performance in both the new and existing datasets.
5. The paper presents empirical results that support the superiority of FIT over previous methods. The significant improvement in performance in both datasets strengthens the credibility of the proposed method.

### Weaknesses
Lack of introduction to related works: The paper lacks a section on related works, making it difficult for readers who are not familiar with the definitions and concepts in previous research. This absence is particularly problematic given the paper's critique of existing methods; without a clear understanding of the established landscape, the significance of the paper's claims and contributions is diminished. The paper assumes a level of prior knowledge that may not be universal, hindering its accessibility and potentially limiting its impact. For instance, the paper discusses 'query embedding' and 'EFO1' without providing sufficient background, leaving readers unfamiliar with these concepts struggling to grasp the core arguments. This lack of context makes it challenging to evaluate the novelty and importance of the proposed approach.

### Questions
The paper could benefit from providing more examples and illustrations to aid in understanding the concepts and methodologies discussed.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
