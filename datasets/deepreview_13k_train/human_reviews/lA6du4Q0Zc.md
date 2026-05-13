# Neural-Symbolic Message Passing with Dynamic Pruning

- Decision: Reject
- Scores: 6, 5, 3, 1

## Abstract
Complex Query Answering (CQA) over Knowledge Graphs (KGs) is a fundamental yet challenging task. Given that KGs are usually incomplete, the CQA models not only need to execute logical operators, but aslo need to leverage observed knowledge to predict the missing one. Recently, a line of message-passing-based research has been proposed to re-use pre-trained neural link predictors to solve CQA. However, they perform unsatisfactorily on negative queries and fail to address the unnecessary noisy messages between variable nodes in the query graph. Moreover, like most neural CQA models, these message passing models offer little interpretability and require complex query data and resource-intensive training. In this paper, we propose a Neural-Symbolic Message Passing framework (NSMP), which integrates neural and symbolic reasoning. By re-using a simple pre-trained neural link predictor, NSMP generalizes to complex queries based on fuzzy logic theory, without requiring training on complex query datasets, while providing interpretable answers. Furthermore, we introduce an effective dynamic pruning strategy to filter out noisy messages between variable nodes during message passing. Empirically, our model demonstrates strong performance and offers efficient inference. Our code can be found at https://anonymous.4open.science/r/NSMP.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The research proposes a novel method for answering Complex Queries within knowledge graphs ($\text{EFO}_1$) through the use of Neura-symbolic  Message Passing with neural link prediction and fuzzy set theory for aggregation. The method is claimed to be computationally efficient as is does not require training on complex queries and can simply utilise a pre-trained link prediction on a given Knowledge graph. The method also allows dynamic pruning that filters the noise from the initial, un-updated layers during the message-passing process. The method shows competitive results on a set of Benchmarks from BetaE and FIT and provides ablations showcasing the need for dynamic pruning and impact of the hyperparameters.

### Strengths
The method suggests a novel method for answering Complex Queries($\text{EFO}_1$) over knowledge graphs that uses pretrained link predictors with Neura-symbolic message passing and fuzzy set theory for aggregation. The method allows the encoding of both local and global information along with both neural and symbolic representations during the message-passing process. This is coupled with an interesting dynamic pruning technique that filters out the impact/noise from the initial layers of un-updated variable nodes. The method is rather competitive on a set of benchmarks from BetaE and FIT and allows for more interpretable reasoning by analysing the fuzzy intermediate representations.

### Weaknesses
1. While the method is ripe with novel ideas I feel that the benefits it brings have already been explored in prior research. Methods like and stemming from CQD and CQD-A train only a single link predictor, thus circumventing the need to train on complex queries. They, along with GNN-QE and others, offer interpretable query answers by exposing the intermediate answers (top-k). The use of fuzzy logic is also explored within these papers. We see that for example, in NELL (both BetaE and FIT versions), other methods are only marginally different (CQD-A) or are on average, better (FIT) than the suggested framework. Can you please elaborate on the novel additions in NSMP and what do they exactly contribute?  Can you elaborate on the comparison in the amount of parameters w.r.t. other benchmarks are they comparable?

2. The novel idea of dynamic pruning is rather interesting; however, the ablation shows a sizable average increase only for queries sampled in FIT. Can you explain the reason for this? How much efficiency does dynamic pruning add to the overall network in terms of inference?

2.5. As direct link prediction is chosen along a product T-norm for fuzzy aggregation, the method is bound to have intermediate answers that do not interact together as outlined in CQD-A. This means that because the probability ranges of different intermediate answers are not homogenous aggregating with a product t-norm can cause massive discrepancies during message propagation. Has any analysis of intermediate answers been completed? 

3. The choice not to include "pni" is not justified, as Yin et al. (2024) includes that scheme with an $\text{EFO}_1$ definition (Example 10 and Property 12 in the paper) and just resamples w.r.t. their definition. The original version of "pni" proposed in BetaE is simply the universal quantifier version that is resampled in FIT w.r.t. their definition. Can you elaborate on the reasoning to not include "pni" ? Has it been tested on ?

4. The paper cited as the reason to not include FB15K (Toutanova & Chen, 2015)) does not claim test leakage but rather proposes a reconstruction of FB15 with the removal of "near-duplicate" or "inverse-duplicate" relations. While FB 15L does have some discrepancies bot BetaE  and FIT still include it in dataset construction and most of the CQA methods are benchmarked on it. Can you please elaborate on the choice of not using FB15K and if there is a stronger argument against the use of FB15K?

### Questions
**Question set Q1: For context, see Point 1 in weaknesses:**

*Can you please elaborate on the novel additions in NSMP and what do they exactly contribute?*  

*Can you elaborate on the comparison in the amount of parameters w.r.t. other benchmarks are they comparable?*

**Question set Q2: For context, see Point 2 in weaknesses:**

*Can you explain the reason for this?* 

*How much efficiency does dynamic pruning add to the overall network in terms of inference?*

**Question set Q2.5: For context, see Point 2.5 in weaknesses:**

*Has any analysis of intermediate answers been completed?* 

**Question set Q3: For context, see Point 3 in weaknesses:**

*Can you elaborate on the reasoning to not include "pni" ?* 

*Has it (pni) been tested on ?*

**Question set Q4: For context, see Point 4 in weaknesses:**

*Can you please elaborate on the choice and if there is a stronger argument against the use of FB15K ?*

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper discusses the neural symbolic approach to address the complex query answering over knowledge graphs by leveraging pretrained link predictor in a neuro-symbolic way. The proposed neuro-symbolic framework follows the message passing GNN framework. The key technique is to formulate the message passing and answer ranking module into the ensembles of both neural update (following previous logical message passing) and symbolic updates (following the fuzzy logic). The performance in many datasets for various query types demonstrated the effectiveness of the models. Notably, the framework is shown to be very efficient than previous fuzzy logic based methods.

### Strengths
1. The presentation is easy to follow.
2. The overall framework is somewhat novel and empirically significant.
3. the experiments is comprehensive on both different underlying knowledge graph and different query types.

### Weaknesses
My particular concern for this paper is whether it can achieves the real efficiency over the fuzzy logic inference approach, such as QTO and FIT. Because the updates on the internal states also includes an adjacency matrix $M_r$, which is $O(n^2)$ space and the fuzzy vector of $O(n)$ space, where $n=|V|$ is the cardinality of the entity set. The calculation of the neuro-symbolic message is of the same cost as (sparse) matrix multiplication, which is already at least quadratic. In that sense, I cannot see the reason in Figure 3, that the speed up of NSMP over FIT, which suggested at least 10 times speed up in NELL. The core issue is that while the message passing framework is conceptually elegant, the computational cost of each message passing step, involving sparse matrix operations on the adjacency matrix and fuzzy vectors, seems inherently quadratic in the number of entities. This raises questions about the practical scalability of the approach, especially when compared to methods that might have different computational bottlenecks. Furthermore, the empirical speedup observed in Figure 3, particularly the 10x improvement over FIT on NELL, is not adequately justified by the theoretical analysis presented, as both methods seem to have similar quadratic complexity in their core operations. It is unclear how the proposed method achieves such a significant speedup, given the similar computational costs of their respective steps.

### Questions
1. Could you please explain the complexity of FIT and your algorithm on both acyclic and cyclic query? in terms of the size of graph and the size of query.
2. Please address my weakness.
3. For the dynamic pruning of the message, I would like to know whether the total message to compute and total states to update can be significantly better than the original LMPNN without pruning, say $O(L m) = O(m^2)$, where $L$ is the total number of layers of message and $O(m)$ is the number of predicates in the query graph.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Neural-Symbolic Message Passing (NSMP) to integrates neural and symbolic reasoning for answering complex queries on knowledge graphs. It adopts pre-trained neural link predictors and fuzzy logic operations to estimate the embeddings and the fuzzy set for each variable in a given query respectively. NSMP doesn’t require to be trained on complex query datasets, and is claimed to provide interpretable answers. The authors further introduce a dynamic pruning strategy to filter out noisy messages in the message passing process. Empirically, NSMP achieves competitive performance on both BetaE and FIT datasets, even though most baselines are trained on complex queries.

### Strengths
- NSMP achieves competitive performance against state-of-the-art methods on complex queries, even though NSMP doesn’t require to be trained on complex queries. The results should be deemed as solid.
- The writing of this paper is generally good except for the abstract and the intro. It’s easy to comprehend most technical details of this paper.

### Weaknesses
 - The contributions of this paper are not clear. The authors claimed three challenges in the intro: bad performance on negative queries, noisy messages and interpretability, but there is no clear correspondence between the model components and the challenges.
- Most components of NSMP have limited novelty regarding the literature of complex queries. One-hop inference and message passing (Section 3.5 & 5) is almost identical to LMPNN[1]. Combining neural and symbolic representations (Section 4 & 5) is very close to EmQL[2], which the authors didn’t even cite in the paper. The idea of using non-parameteric fuzzy logic to avoid training shares many spirits with CQD[3], though the actual design is different.
- The usage of fuzzy logic in this paper is not standard compared to [3, 4, 5]. In [3, 4, 5], every entity has a probability to be bound to a variable, independent of other entities. This enables fuzzy logic operations to form a closure and satisfy logic laws (e.g. De Morgan’s laws). In this paper, all entities form a distribution to be bound to a variable and have to be normalized after every operation (Equation 7-15, 17). As a result, NSMP doesn’t satisfy De Morgan’s laws and has to resort to DNF to handle disjunctions.
- The authors claimed interpretability as an advantage of NSMP, but there are no supporting qualitative experiments. I would expect some experiments to visualize the intermediate variables in complex queries similar to [3, 4].

### Questions
- In my opinion, dynamic pruning refers to pruning strategies that depend on the learned representations. Here the pruning strategy only relies on the query graph and the layer index, which should be regarded as a static pruning strategy. A better alternative is to call it Bellman-Ford iteration or breath-first search. You may refer to [6, 7] for more insights.
- Line 473-475: It looks like that the hyperparameters of NSMP have to be tuned for each dataset. Could you provide an analysis on hyperparameter sensitivity? Do there exist some robust default hyperparameters?
- Line 20-23: The logic of this sentence is weird. How does “re-using a simple pre-trained neural link predictors” serve as an approach to “generalizes to complex queries based on fuzzy logic theory”?
- Line 132-133: What do you mean by “the more complex existential first order logic formulas”? Is it a disadvantage?
- Line 182: Is DNF really scalable for handling disjunction operators? I feel the opposite.
- Equation 9 & 10: What if we get negative values after subtraction?
- Typos:
    - Line 30: graph representation → graph representations
    - Line 34: A more straightforward → A straightforward
    - Line 261: symbolic representation → symbolic representations

[6] Neural Bellman-Ford Networks: A General Graph Neural Network Framework for Link Prediction. Zhu et al. NeurIPS 2021.

[7] Distance-Based Propagation for Efficient Knowledge Graph Reasoning. Shomer et al. EMNLP 2023.

### Soundness
2

### Presentation
4

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes a Neural-Symbolic Message Passing framework (NSMP) for complex logical query answering. NSMP uses the same components as many other baselines in the literature: a pre-trained link predictor (ComplEx-N3) as in CQD and FIT and the same message passing mechanism as in LMPNN. The only difference between NSMP and previous works is “dynamical pruning” which is a manual stop on message propagation from intermediate variables whose node states have not yet been updated. Experimentally, NSMP underperforms to GNN-QE and CQQ-A on BetaE datasets and underperforms to FIT on EFO-1 dataset while being somewhat faster than FIT.

### Strengths
N/A

### Weaknesses
The paper proposes a Neural-Symbolic Message Passing framework (NSMP) for complex logical query answering. NSMP uses the same components as many other baselines in the literature: a pre-trained link predictor (ComplEx-N3) as in CQD and FIT and the same message passing mechanism as in LMPNN. The only difference between NSMP and previous works is “dynamical pruning” which is a manual stop on message propagation from intermediate variables whose node states have not yet been updated. Experimentally, NSMP underperforms to GNN-QE and CQQ-A on BetaE datasets and underperforms to FIT on EFO-1 dataset while being somewhat faster than FIT.

### soundness:
 1

### presentation:
 1

### contribution:
 1

### strengths:
 N/A

### weaknesses:
 The paper is either a direct plagiarism of [1] or a poor attempt to sell a very marginal change using the same template as [1] with a few changed words and butchered phrases.

Below are some examples of the significant text overlap with several replaced words:

* **Section 1: Introduction**

[1] `Knowledge graphs (KGs) store factual knowledge in the form of triples that can be utilized to support a variety of downstream tasks`

[this work] `Knowledge graphs (KGs) store factual knowledge in the form of graph representation, which can be applied to various intelligent application scenarios`

-----

[1] `However, given that modern KGs are usually auto-generated [48] or built through crowd-sourcing [52], so real-world KGs [9, 11, 45] are often considered noisy and incomplete, which is also known as the Open World Assumption [24, 28].`

[this work] `However, given that modern KGs are usually auto-generated () or built through crowd-sourcing (), real-world KGs () often suffer from incompleteness, which is also known as the Open World Assumption (OWA) ().` - note that even citations are the same.

-----

* **Section 2: Related Work** (almost verbatim content copy of the same sections and paragraphs), some particular examples:

[1] `Reasoning over KGs with missing knowledge is one of the fundamental problems in Artificial Intelligence and has been widely studied`

[this work] `Reasoning over KGs with missing knowledge is one of the long-standing topics in machine learning and has been widely explored`

-----

[1] `Other methods for link prediction include rule learning [42, 69], text representation learning [43, 53, 55], and GNNs [50, 70, 72].`

[this work] `... other research lines for one-hop KG reasoning include rule learning (), text representation learning (), reinforcement learning (), and graph neural networks ().` - again, references are the same

-----

[1] `… they embed entities and relations into continuous vector spaces and predict unseen triples by scoring triples with a well-defined scoring function. Such latent feature models can effectively answer one-hop atomic queries over incomplete KGs.`

[this work] `… neural link predictors () have been proposed to answer one-hop atomic queries on incomplete KGs. These latent feature models learn a low-dimensional vector for each entity and relation. By employing a well-defined scoring function to assess link confidence, they can effectively predict unseen links.`

-----

* **Section 2.2** is a rephrased version of the same paragraph from [1]

* **Section 3.1** (Knowledge Graphs) copies the content from Section 3 (Model-Theoretic Concepts for Knowledge Graphs) from [1]

* **Section 3.2** (Existential First Order Queries With a Single Free Variable) is almost a verbatim copy of Section 2.2 (EFO-1 Queries and Answers) from the FIT paper [2]

* **Section 3.3** (Query Graph) re-phrases the same section in [1]:

[1] `Since disjunctive queries can be solved in a scalable manner by transforming queries into the disjunctive normal form, it is only necessary to define query graphs for conjunctive queries`

[this work] `As mentioned above, since a DNF query can be addressed by solving all its sub-conjunctive queries, it is only necessary to define query graphs for conjunctive formulas`

-----

And copies the definitions 1-6  from [2]

* **Section 3.4** (Neural Link Predictors) copies the same from [1] and just replaces the model name CLMPT with NSMP
* **Section 3.5** (Neural One-Hop Inference on Atomic Formulas) re-uses the same-named subsection from [1]:

[1] `On each edge, when a node is at the head position, its neighbor is at the tail position, and vice versa.`

[this work] `On each edge, when a node is at the head position, its neighbor is at the tail position, and vice versa`

-----

[1] *Specifically, a logical message encoding function $\rho$ is proposed to perform one-hop inference.*

[this work] *Specifically, a logical message encoding function $\rho$ is proposed to define this neural one-hop inference on edges.*

Then, Equations 3-6 are exactly the same as Equations 6-9 from [1]

-----


* **Section 4** (Neural-Symbolic One-Hop Inference on Atomic Formulas) is largely based on ENeSy [3] (Section 4.2, page 8) without citing it: including the derivation of negation as $\frac{\alpha}{|\mathcal{V}|} - p_tM_r^{\top}$ and defining the encoding function as a softmax after concat where concat *is a function mapping the similarity between all entities $e \in \mathcal V$ and $\mathbf{v}$ to a vector* (ENeSy) and *is a function that maps the similarities between all entities and the intermediate embedding inferred by $\rho$ to a vector* (this work).

* **Section 5.1** (Message Passing with Dynamic Pruning) almost rephrases Section 4.1 (Conditional Logical Message Passing) from [1], they even start with the same sentence:

[1] `A query graph contains two types of nodes: constant entity nodes and variable nodes. `

[this work] `A query graph contains two types of nodes: constant and variable nodes`

-----

Then, 

[1] `We decide whether to pass logical messages to a node based on its type.`

[this work] `we decide whether a variable node should pass messages to its neighboring variable nodes based on whether its state has been updated`


* **Section 5.2** (Node State Update Scheme) uses the same text and notation as Section 4.2 (Node Embedding Conditional Update Scheme) from [1] with small additions, eg,

[1] *Next, we discuss how to calculate the $z_e^a$ nd $z_v^l$ from the input layer $𝑙 = 0$ to latent layers $𝑙 > 0$*

[this work] *Next, we discuss how to compute these representations from the input layer $l = 0$ to latent layers $l > 0$*

-----

[1] For each neighbor node $n \in N(v)$, one can obtain information about the edge (i.e., the atomic formula) between $n$ and $v$, which contains the neighbor embedding $z_n^{(l −1)} \in D$, the relation $r_{nv} \in R$, the direction $D_{nv} \in \{ℎ \rightarrow 𝑡, 𝑡 \rightarrow ℎ\}$, and the negation indicator $Neg_{nv} \in \{0, 1 \}$

[4, LMPNN paper, Section 6.2] For each neighbor node $v \in N(n)$, one can obtain its embedding $z_v^{(l−1)} \in D$, the relation $r_{v \rightarrow n} \in R$, the direction $D_{v \rightarrow n} \in \{h2t, t2h\}$, and the negation indicator $Neg_{v \rightarrow n} \in \{0, 1\}$

[this work] For each neighboring node $n \in N_{DP} (v)$, one can obtain information about the edge between $n$ and $v$, which contains the neighbor mebdding $z_n^{(l-1)}$, the neighbor symbolic vector $s_n^{(l-1)}$, the relation embedding $r_{nv}$ , the relational adjacency matrix $M_{r_{nv}}$ , the direction $D_{nv} \in \{h \rightarrow t, t \rightarrow h\}$, and the negation indicator $Neg_{nv} \in \{0, 1\}$

It is obvious that [this work] just re-hashes the same content from [1] and [4] with a slightly different notation.

-----

Experimentally, the proposed NSMP underperforms well-established models on all benchmarks: worse than CQD-A on BetaE queries and worse than FIT on EFO-1 queries.

-----

Based on the above arguments, I do not see any scientific contribution in this manuscript, the issue has to be elevated to ACs, SACs, and PCs. It is sad that in this submission we have to measure the degree of plagiarism and deception instead of novel scientific contributions.

### Questions
N/A

### Soundness
1

### Presentation
1

### Contribution
1
