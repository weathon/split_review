# Double Equivariance for Inductive Link Prediction for Both New Nodes and New Relation Types

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 3, 8, 6

## Abstract
The task of inductive link prediction in \update{knowledge graphs} (KGs) generally focuses on test predictions with solely new nodes but not both new nodes and new relation types. 
In this work, we formally define the  concept of {\em double permutation-equivariant representations} 
that are equivariant to permutations of both node identities and edge relation types.
\update{We then show how double-equivariant architectures are able to self-supervise pre-train on distinct KG domains and zero-shot predict links on a new KG domain (with completely new entities and new relation types).}
We also introduce the concept of {\em distributionally double equivariant positional embeddings} designed to perform the same task.
\update{Finally, we empirically demonstrate the capability of the proposed models against baselines on a set of novel real-world benchmarks. More interestingly, we show that self-supervised pre-training on more KG domains increases the zero-shot ability of our model to predict on new relation types over new entities on unseen KG domains.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to address the so-called doubly inductive link prediction task, where both new nodes and new relation types can be found solely in test time. To this end, author proposes two different models, ISDEA and DEq-InGram, which all abides by the equivariance requirement. Finally, experiment results show the new method beats baseline empirically.

### Strengths
The result of the paper seems sound, the author provides the reader with many theorems and proofs for its theory and they seem plausible to me.

The experiments are good, including many baselines, and the empirical result shows that the new method is in general better (though it falls behind the baseline in some settings).

### Weaknesses
The design of ISDEA is very straightforward, however, it is purely brutal force and has very high complexity. I have checked the statistics of the dataset used for experiment evaluation and found these two newly crafted datasets are significantly smaller than commonly used datasets, like FB15k or even its subset FB15k-237. I believe one major motivation for the setting for inductive learning is to allow for scalability towards a larger knowledge graph, yet the model design seems to be in the opposite direction.

The core issue with ISDEA lies in its exhaustive search for isomorphic subgraphs, which leads to a combinatorial explosion in computation time as the graph size increases. The distance calculation between every pair of nodes for each relation type is particularly concerning. This approach is not only computationally expensive but also memory-intensive, making it impractical for larger knowledge graphs. The lack of any approximation or heuristic to reduce the search space is a significant drawback.

Furthermore, while the authors claim the datasets are designed for doubly inductive link prediction, the small size of these datasets raises concerns about the generalizability of the results to real-world scenarios. The inductive setting is often motivated by the need to handle large, evolving graphs, and the current experiments do not adequately address this challenge. The comparison to FB15k-237, even if the inductive versions are smaller, highlights the gap in scale between the experimental setup and the intended application of the method.

### Questions
What is the largest knowledge graph that can be computed by ISDEA, for example, with GPU memory of 32 GB?


Can the isomorphism requirement be reduced to some WL test to reduce the complexity yet maintain decent empirical results?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the task of  "doubly inductive link prediction'", where the objective is to be able to make inductive prediction on both novel nodes and novel relation types, which are not encountered during training. This is a highly challenging task, especially because the authors do not allow the use of any additional context regarding the unknown relations.   The authors propose a general framework ISDEA to generate "double permutation-equivariant" representations and further explore ways to augment the existing InGram architecture with "distributionally double equivariant positional embeddings". Two new real-world datasets are proposed for benchmarking "doubly inductive link prediction" and experiments are carried out to validate the theoretical findings.

### Strengths
- **Problem and setup**: Inductive link prediction is a very important task and authors generalise this task to also predict novel relation types. The paper provides an approach for modeling equivariant representations of nodes and relations. 
- **Motivation and study**: A clear motivation, including the study of different architectures.
- **Benchmarking**: New benchmarking datasets are introduced and assessed against prior methods, establishing a new context.

### Weaknesses
 - **Presentation and formal writing**: The writing of the paper is problematic and concepts are often unclear:
  - The text is very repetitive and contains many redundancies (i.e., the contribution of the paper is highlighted three times in the first page with paraphrased sentences), but when it comes to formal definitions, it does not make a rigorous treatment (see below).
  - Figure 1: This is crowded and does not explain much to me: why are the relations typed using conjunctions at this point? How does the logical description given in the beginning of page 3 in any way correspond to this figure? The use of conjunctions to represent relations is not standard and lacks clear motivation, making it difficult to understand the underlying relational structure being modeled. The figure also fails to clearly illustrate the doubly inductive setting, particularly how the training and test sets differ in terms of both nodes and relation types.
  - Multigraph: Authors seem to suggest a multigraph is more general than a knowledge graph. It is unclear to me what authors specifically mean by this? If they mean a directed, multi-relational graph then this is nothing more than a knowledge graph. Heterogenous networks are special instances with single relation types allowed between nodes etc. The authors need to clarify their definition of a multigraph and how it differs from standard knowledge graph representations, especially since the term is used to justify the proposed approach.
  - Doubly inductive: The naming is somewhat problematic, because the inductive prediction is either on the relation or on one of the entities at a time, but not both according to Def 1. The definition of the doubly inductive task is not clear, as it seems to imply simultaneous induction on both nodes and relations, while the actual task involves predicting either missing relations or missing nodes, but not both at the same time. This discrepancy needs to be addressed.
   - Isomorphic triplets: The definition of multigraph isomorphism and triplet isomorphism is a very odd one. I have no idea why, e.g., (Hans, Grand $\land$ Father, Bob) in train and (Hanna, Granny $\land$ Mother) should be considered isomorphic (and at this point we still do not know the role of logical conjunction in defining the relations). This is essential because everything builds on this notion of "isomorphism" which is completely unjustified. The notion of isomorphic triplets is not well-defined, especially with the use of conjunctions in relation types. The example provided does not clarify why such triplets should be considered isomorphic, and the connection to the overall framework remains unclear. The lack of formal justification for this definition undermines the theoretical foundation of the paper.
  - The paper is very hard to parse in general: in many cases, the statements of the results appear ambiguous to me, including the ones in the appendix.

- **New architectures**: The new architectures introduced in the paper appear to be somewhat incremental. IDSEA is a variant of DSS-GNN operating on relation-induced subgraphs, whereas DEq-InGram is a simple modification of InGram with bagging. The novelty of the proposed architectures is questionable. ISDEA seems to be a straightforward application of DSS-GNN to relation-induced subgraphs, and DEq-InGram appears to be a minor modification of InGram using a form of ensemble averaging. The authors need to better justify the novelty and significance of these architectural choices.

- **Empirical findings**: IDSEA seems to perform consistently worse than DEq-InGram in the task node prediction on PediaTypes, which does not seem to match what the theory suggests and is not being discussed in the paper. The experimental results are not fully aligned with the theoretical claims, particularly the observation that IDSEA performs worse than DEq-InGram in node prediction. This discrepancy raises concerns about the validity of the theoretical framework and the practical effectiveness of the proposed method. The authors need to provide a more thorough analysis of these results.

- **Train and test distribution**: The paper predominantly focuses on scenarios where the train and test graphs share a similar distribution. However, there exists a range of tasks involving unseen nodes and relations where the distribution significantly differs between the training and testing phases.  Further experimental validation on these tasks is required.

### Questions
Please refer to my review for clarifications and some more questions  here:

- In the experiments, why do the authors not compare with standard relational GNNs such as RGCN, CompGCN, NBFNets, etc?

- What are the differences between ISDEA, DEq-InGram, and InGram in terms of their runtime?

- Since both DEq-InGram and InGram produce distributionally double equivariant representations, why is there a substantial performance gap between these models on both datasets?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a theoretical framework for inductive link prediction over multi-relational graphs (knowledge graphs) where both entities and relations are unseen at test time. The framework includes the concepts of double permutation equivariance (to node permutation and edge type permutation) and its slight relaxation of distributionally double equivariance (to incorporate another existing model into the framework). Further, the authors introduce the first GNN implementation of the proposed framework – ISDEA as a double equivariant model, and DEq-InGram as a distributionally-double equivariant version of InGram. Experimentally, the authors devise a handful of new datasets and run experiments on relation prediction $(i, ?, k)$ and node prediction $(i, r, ?)$ tasks.

### Strengths
**S1.** Overall, I think it is a solid work that lays important theoretical foundations for the hardest of inductive link prediction tasks - dealing with both new entities and relations at test time requires more effort beyond learning relation embeddings. This is highly relevant for modern graph learning tasks, especially in low-data regimes without input node features.

**S2.** The experimental agenda is convincing - a handful of newly proposed datasets with relation prediction and entity prediction tasks. Perhaps the experimental section could have been even stronger if the evaluation was performed on all nodes/relations in the inference graph instead of 50 random negatives, but the authors acknowledge it is the scalability issues of the ISDEA model (not the framework in general) that are likely to be addressed in the future work.

### Weaknesses
The following ones are not the critical weaknesses but rather several discussion points I’d invite the authors to elaborate on: 

**W1.** The formalization in Section 2 assumes the existence of bijections (nodes-to-nodes, relations-to-relations) in training and test graphs. Basically, the framework posits the double equivariance only when training and test graphs have exactly the same number of nodes and edge types - which practically does not happen very often. On the other hand, the constructed datasets PediaTypes and WikiTopics all have different numbers of nodes and relations at training and test time (so there is no bijection possible). Could you please comment on the seeming discrepancy between the theory and what is measured in the experiments? 

**W2.** Section 5.2: “_relatively easier task of node prediction_” - I do not quite agree with this statement. The results might suggest the task is easier simply because you take 50 random negatives among _thousands_ of nodes in the inference graph, so those negatives are likely to be _easy_ negatives. On the other hand, the number of relations in the datasets is 50-150 in PediaTypes and <50 in WikiTopics, so the negative relation samples are likely to be harder. It was found that evaluation on small number of negative entities overestimates the performance, so I would hypothesize the numbers (and task impression) would change when the architecture would scale to ranking all nodes in the inference graph.

### Questions
**Q1.** What are the input features to standard GNN architectures reported in the experiments under GraphConv / GAT / GIN? Initialization of nodes with all ones or with random vectors? 

**Q2.** Since DEq-InGram is distributionally double equivariant (by means of averaging several runs with different random relation vectors initializations), would averaging NBFNet results across several runs with random relation initialization count as distributionally double equivariant as well?

**Q3.** The distributionally double equivariant idea posits equivariance in expectation, of which the easiest implementation is averaging over several runs (if we talk about drawing samples of relation vectors). Drawing parallels to group-equivariant CNNs, it is possible to achieve equivariance via augmentations such as frame averaging. I wonder if any such “augmentation” or frame averaging is possible within the double equivariance framework. If so, it might be a good idea to clearly state in the paper that distributionally-double equivariance is different from frame averaging

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates inductive link prediction for both new entities and new relations. It proposes an inductive structural double equivariant architecture that decomposes a knowledge graph into subgraphs containing different relations and encodes and aggregates them in the same way to eliminate the use of relation embeddings. The paper also constructs two datasets based on OpenEA and Wikidata5M. Extensive experimental results demonstrate the strong performance of ISDEA.

### Strengths
S1. This paper addresses an important and challenging task.

S2. It introduces a novel framework that avoids reliance on relationship embeddings.

S3. Good reproducibility - the paper provides code and detailed experimental settings.

### Weaknesses
W1. The proposed framework requires significant preprocessing and expensive encoding costs. This may be attributed to three factors: preprocessing costs, encoding for each relation, and separate scoring for each candidate entity.

W2. The 1 vs. 50 evaluation poses a risk as negative samples obtained from negative sampling are mostly easily distinguishable. This setup may not be sufficient to cover real-world scenarios.

W3. While ISDEA appears suitable for relation prediction, its performance on node prediction is not very good.

### Questions
Q1. As shown in Table 1(b), ISDEA's performance is not good and, in some datasets, even receives the lowest scores. Can you explain the reasons for this?

Q2. I am concerned about the efficiency of the proposed framework. Could you report training and inference times on some datasets?

Q3. It should be clarified that the multilingual KGs in the OpenEA library share the same schema. So many of the relations in these KGs overlap.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
