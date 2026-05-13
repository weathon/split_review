# Categorical Features of entities in Recommendation Systems Using Graph Neural Networks

- Decision: Reject
- Scores: 6, 3, 3, 3

## Abstract
The paper tackles the challenge of capturing entity attribute-specific preferences in recommender systems, with a particular focus on the role of categorical features within GNN-based user-item recommender engines. Despite the significant influence of categorical features such as brand, category, and price bucket on the user decision-making process, there are not many studies dedicated to understanding the GNN's capability to extract and model such preferences effectively. The study extensively compares and tests various techniques for incorporating categorical features into the GNN framework to address this gap. These techniques include one-hot encoding-based node features, category-value nodes, and hyperedges. Three real-world datasets are used to answer what is the most optimal way to incorporate such information. In addition, the paper introduces a novel hyperedge-based method designed to leverage categorical features more effectively compared to existing approaches. The advantage of the hyperedge approach is demonstrated through extensive experiments in effectively modeling categorical features and extracting user attribute-specific preferences.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to leverage the categorical information of items for graph neural networks-based recommendation. Differently from previous similar approaches in the literature, the authors do not address the task of session recommendation, which is the main scenario where categorical information is usually injected in recommendation. Specifically, the paper introduces three possible variants of graph-based recommender systems exploiting the categorical information, namely: 1) one-hot encoding of the categorical information as items’ node features, 2) tripartite graphs where categories represent another type of nodes besides users and items, and 3) items’ categories regarded as hyperedges. The authors’ proposal involves the latter setting, where a neighborhood and hyperedge aggregation are performed through a GCN layer and a UniSAGE aggregation, respectively. Finally, the loss function is the common Bayesian personalized ranking one (i.e., BPR). The proposed approach is tested against three GCN architectures having: 1) no categorical information, 2) category information as extra nodes in the graph, and 3) category information as extension of the node features. The evaluation is run on three popular recommendation datasets which include two types of category accounting for either the products’ price or category or both. Results on all such settings demonstrate the efficacy of the hyperedge-based solution, whose trends are further confirmed by evaluating the proposed model against similar state-of-the-art recommendation approaches.

### Strengths
+ The proposed approach is simple.
+ The adoption of hyperedges in graph-based recommendation is quite recent in the literature.
+ The authors outline the differences with respect to the existing literature in a sufficient manner.
+ A wide range of evaluation settings are proposed.

### Weaknesses
- While proposing a simple approach is not generally criticisable, it might need further discussions regarding the actual novelty of the solution.
- No code is released at review time; this might have been helpful to further assess the efficacy and effectively of the proposed approach.
- Some evaluation choices are not common in the literature and require further justifications.

**After the rebuttal.** The answers provided by the authors addressed the outlined weaknesses quite sufficiently.

### Questions
* Can the authors further elaborate on why the proposed approach should represent a novelty to the existing similar approaches? Indeed, it seems that the presented solution makes use of other graph neural networks layers without any specific new techniques introduced.
* Is there any specific reason why the recommendation metrics are calculated with high cut-offs (i.e., at 50-100)? Did the authors try to evaluate the recommendation performance at 10-20? And if so, are the observed trends still confirmed?

**After the rebuttal.** The answers provided by the authors answered my questions quite sufficiently.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study investigates the integration of categorical features of items into collaborative filtering. Its main idea involves connecting nodes with same attributes through hyperedges and leveraging a hypergraph neural network for encoding. The proposed model is tested across three publicly available datasets, demonstrating a notable improvement over existing benchmarks.

### Strengths
1. The paper studies one important task, i.e., collaborative filtering with item attributes.
2. Experiments are conducted on three public datasets.
3. Experiments show that the proposed method outperforms several existing baselines.

### Weaknesses
1. Limited novelty. The idea of connecting nodes that share the same attributes with hyperedge is not new and has been explored [1]. As a result, the whole paper seems to be a straightforward application of it on collaborative filtering task, limiting the novelty. Although the performance is promising, providing new insights for the community could be more important for an academic paper.
2. The proposed method considers only two specific attributes, i.e., price and category, which makes the model less generalizable. It could be better if the proposed method describes how it will deal with general single attributes and multiple attributes (e.g., will it be better if we model some combinations of attributes?).
3. Code is not available, making it difficult to reproduce the work in the reviewing phase.
4. The paper lacks robustness in its experimental validation, as there is no evidence of repeated experiments or statistical tests such as paired t-tests, which are crucial for ensuring the reliability of the results.
5. Presentation issue. Figure 2 is not a vector graph and is in low resolution.


[1] Wu et al. Dual-view hypergraph neural networks for attributed graph learning. Knowledge-Based Systems 2021.

### Questions
For the "Pricae and Category" setting in Table 2, do you use only $h_{cp}$ or use $h_{cp}$, $h_c$, and $h_p$?

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors studied the problem of how to properly incorporate categorical features into graph neural models. The authors' contribution is mainly in two folds:
The authors compared with multiple commonly used baselines to estimate which way to incorporate categorical features worked better
The authors proposed a new model to represent categorical features as hyper edges in the graphs.

### Strengths
Strength
- The paper is in general well written and easy to follow

- The experiments are conducted on 3 public dataset which is easy to follow and repeat the experiment

### Weaknesses
Concerns
- My major concern is the lack of technical contribution. As pointed out by the authors, using hyperedges in recommender engines is a very straightforward idea and is not novel. The authors' argument of  "It is to be noted that our examination focuses on user-item recommender systems and does not extend to session-based recommender systems." Does not justify well for the novelty or technical contribution of this paper, which leads to my major concern.

- The author only compared 2 commonly used ways of representing categorical features which is far from being comprehensive, which further decrease the contribution of the paper.

### Questions
When building the hyper edges for the proposed model, the authors used secondary interaction between categorical features. What's the time and storage complexity for the proposed algorithm? Will it explode the system if there are a lot of categorical features available for the users and items?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on how to efficiently model categorical attributes within user-item graph networks for recommender systems. The authors first compare existing methodologies based on 1) one-hot-encoding of binary features for the entities, 2) creation of nodes representing an attribute linked to entities possessing the attribute and 3) creation of hyperedge between any entities sharing the same attribute. Then, they proposed a new model where categorical attributes were handled as hyperedges.

### Strengths
Different ways of handling the categorical features in GNN are well described.  
Experiments are made on 3 real-world datasets. 
The hyperedge trick to handle categorical features seem to provide the best results according to Table 1 for the 3 tested datasets: Amazon Grocery, Amazon Tools and Yelp.

### Weaknesses
This is clearly stated by the authors, the proposed approach is only for user-item recommender systems and not session-based ones and does account for item or user features independently only, not interaction categorical features. 

By the way, I think the paper would benefit from a quick explanation on why extension of the concept of hyperedges for session-based recommender systems to user-item recommender systems is not straightforward, to justify the novelty of the approach here (which is unclear to me). 

“it is noteworthy that there is limited research dedicated to understanding how to incorporate categorical features best“. However, reading the related work, it seems rather clear the limitations of one-hot-encoding and attribute nodes: “some authors have pointed
out the limitations of the binary-encoded category method“.  

“For all baselines, we used the publicly available original implementations with their default parameters.” I don’t think this is the correct way to proceed. Each baseline needs to be optimized for the use case for fair comparison. 

Some comments:

-In Equation (1), \tilde{d}_j, \tilde{d}_i  are not defined and I would also mention that N(v) stands for the neighborhood of node v. 

-z_u and z_i are not mathematically defined in p.5. 

Minor, typos:

p.3, “use-item-attribute graph”.

p.4. “Another way…” sentence needs to be rewritten.

p.7 “each datasets”

### Questions
Can you please explain why the extension of the concept of hyperedges for session-based recommender systems to user-item recommender systems is not straightforward, to justify the novelty of the approach here? 

How are the experimental results after tuning the hyperparameters of each competing approach?

Did you study the benefit of the approach with more categorical attributes and not only price level and brand category to describe the items? 

What is the effect of the number of different valuations for each categorical feature?

=== AFTER REBUTTAL ===

I thank the authors for taking the time to answer our questions. Unfortunately I don't upgrade my score because I think the novelty is too limited and the proposed setup (with 2 types of categorical features) too restrictive.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
