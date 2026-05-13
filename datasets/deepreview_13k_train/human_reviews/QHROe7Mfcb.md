# Less is More: One-shot Subgraph Reasoning on Large-scale Knowledge Graphs

- Decision: Accept
- Scores: 3, 6, 5

## Abstract
To deduce new facts on a knowledge graph (KG), a link predictor learns from the graph structure and collects local evidence to find the answer to a given query. However, existing methods suffer from a severe scalability problem due to the utilization of the whole KG for prediction, which hinders their promise on large scale KGs and cannot be directly addressed by vanilla sampling methods. In this work, we propose the one-shot-subgraph link prediction to achieve efficient and adaptive prediction. The design principle is that, instead of directly acting on the whole KG, the prediction procedure is decoupled into two steps, i.e., (i) extracting only one subgraph according to the query and (ii) predicting on this single, query dependent subgraph. We reveal that the non-parametric and computation-efficient heuristics Personalized PageRank (PPR) can effectively identify the potential answers and supporting evidence. With efficient subgraph-based prediction, we further introduce the automated searching of the optimal configurations in both data and model spaces. Empirically, we achieve promoted efficiency and leading performances on five large-scale benchmarks. The code is publicly available at: https://github.com/tmlr-group/one-shot-subgraph.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new method for knowledge graph (KG) link prediction which they name reasoning. The method relies on (1) sampling the KG around the entities involved (not on e.g. computing embedding on the whole KG) and (2) reasoning on top of this subgraph. This two step process ensures efficiency as the subgraph reduces the neighborhood over which the reasoning (link prediction) is done. Step (1) involved a Page Rank based procedure that selected a subgraph based on the importance of the nodes in the KG.

### Strengths
* The paper proposes a simple, yet somewhat novel idea. While the idea is somewhat heuristic, it is nevertheless interesting to test out its performance on this problem. 

* The authors perform good literature review summarizing the different categories of KG link prediction methods. 

* The proposal is tested empirically through several experiments.

### Weaknesses
 * The paper appears to use terms and phrases that make it sound quite bombastic and somewhat unscientific (see below).

* Some of the language is vague and I feel like some of the technical details from the appendix would benefit the paper.

* Algorithm 1 is not clearly defined (see below).

* I feel like a bit more space can be allocated to the intuition behind some of the experiments (e.g. what does the degree distribution in Fig 4 imply about the method's performance qualitatively?)

* The use of the term 'KG Reasoning' is misleading, as the paper is solving the link prediction task. The term 'reasoning' is used only once in the whole paper, which is inconsistent with the paper's title and terminology.

* The repeated use of the word 'paradigm' is not justified. There is no fundamentally new theory in their proposal/approach, and the term is used excessively, making the writing sound less scientific.

* The use of the word 'blazes' on p.1 is inappropriate for academic writing.

* The connection between exploration/exploitation and the proposed algorithm is weak. While there is an analogy with exploration/exploitation, the algorithm does not formulate the problem using this analogy, and there is no way to trade/balance the two. This comparison relies on broad intuition, making this advantage a weak one at best.

* Algorithm 1 lacks definitions for Alpha, K, and the shapes of A and D. These are critical parameters for the algorithm, and their absence makes the algorithm difficult to understand and reproduce.

* The computation of the adjacency matrix A in the subgraph extraction part is not clear. Since this is a KG, not a homogenous graph, there are several adjacency matrices (one for each relation). The paper does not specify how these are combined, which is a crucial detail for understanding the method.

### Questions
* To the above point, re language usage, please fix these.
    * E.g. it uses the term KG Reasoning while in fact solving the link prediction task (a term used only once in the whole paper!).   
    * Repeated use of the word paradigm, even though there isn't anything that is fundamentally new theory in their proposal/approach. 
    * The use of the word 'blazes' on p.1 

* p. 3, Advantage 2. Why is the exploration/exploitation relevant for the proposed algorithms? While there is some intution behind the analogy with exploitaion/exploration the algorithm doesn't really formulate the problem using this analogy. For example there is no way to trade/balance the two. So this comparison relies on broad intuition, hence this advantage is a weak one at best. 

* Algorithm 1. define Alpha, K, define the shape of A and D.

* How is the adjacency matrix A computed in the subgraph extraction part. Since this is a KG, not a homogenous graph, there are several adjacency matrices (one for each relation). Are these combined somehow? 

* I think the paper would benefit from pulling some of the technical details from the supplement to the main paper, in favor of reducing some of the verbiage in the main paper. Please consider this modification.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the reasoning on large-scale knowledge graphs and proposes to extract only one query-dependent subgraph, then reasoning on this single subgraph. Specifically, the authors propose to use personalized PageRank to assign probabilities, and then extract the subgraph according to the probabilities. Three different query-dependent message functions are used in the reasoning step. The experiments are conducted on three common datasets.

### Strengths
1. The paper is well-motivated. It is reasonable to consider the one-shot subgraph reasoning problem.
2. The paper is well-written and easy to follow.
3. The paper provides a comprehensive literature review in preliminaries.

### Weaknesses
1. Although the problem is interesting, the proposed methodology is not surprising. The main idea is to use PPR to calculate probability and select the top of entities and relations. The reasoning on the subgraph is following the existing methods.
2. The paper emphasizes improved efficiency, but I did not find a comparison of efficiency between the proposed method and the existing ones.
3. The hyperparameter searching looks inefficient.

### Questions
1. The hyperparameter searching is not trivial. It would be helpful if the authors could explain more about hyperparameter searching when facing a new knowledge graph and how to select the best configuration.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to address the serious scalability problem of using the entire knowledge graph (KG) for inference. To this end, one-shot subgraph reasoning on large-scale KG is proposed. This method decouples the inference process into two steps, (i) extracting only one query-dependent subgraph and (ii) reasoning on this single subgraph. This method has higher training efficiency and stronger reasoning ability.

### Strengths
1.The motivation of model design is clear and reasonable. It is unnecessary to utilize the whole KG in reasoning, only a small proportion of entities and facts are essential for answering specific queries, which is also supported by the experiments.

2.Experiments cover several benchmarks. The model is tested on multiple datasets and shows very promising results.

3.The paper is well-written and generally easy to follow.

### Weaknesses
1.In the paper, there is some similar descriptions in the discussion. For example, in section 3, the first paragraph states, 'The design principle here is to first identify one subgraph, which is relevant to a given query and is much smaller than the original graph, and then effectively reason on this subgraph to obtain the precise prediction.' This is similar to Definition 1 in section 3, which states, 'Instead of directly reasoning on the original graph G, the reasoning procedure is decoupled into two-fold: (1) one-shot sampling of a query-dependent subgraph and (2) reasoning on this subgraph.' These are also similar to what is mentioned in the introduction, 'Thereby, the reasoning of a query is conducted by (i) fast sampling of one query-dependent subgraph with the one-shot sampler and (ii) slow reasoning on this single subgraph with the predictor.'

2.In sections 4.4, a significant number of symbols, abbreviations, and technical terms are employed. Some symbols are not adequately explained, which may potentially cause difficulties for readers during their reading. For example, the supp() in 4.4Theorem 1 does not provide an explanation.

3.The formulas in sections 4.3 and 4.4 are not labeled, such as (6) and (7).

### Questions
1.Given that the proposed method relies on a non-parametric heuristic (PPR) for sampling, how interpretable are the final predictions and reasoning steps? Can the method provide insights into why a certain answer was chosen for a given query?

2.How robust is the proposed method to noise or inaccuracies in the underlying knowledge graph? Are there any guarantees regarding the robustness of reasoning results in the presence of perturbations in the data?

3.What are the potential directions for future research or extensions of this work? Are there specific aspects or challenges within KG reasoning that remain open for investigation?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
