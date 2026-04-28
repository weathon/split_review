# Explaining Hypergraph Neural Networks: From Local Explanations to Global Concepts

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Hypergraph neural networks are a class of powerful models that leverage the message passing paradigm to learn over hypergraphs,
a generalization of graphs well-suited to describing relational data with higher-order interactions.
However, such models are not naturally interpretable,
and their explainability has received very limited attention.
We introduce \name, the first model-agnostic post-hoc explainer for hypergraph neural networks that provides both local and global explanations.
At the instance-level, it performs input attribution by discretely sampling explanation subhypergraphs optimized to be faithful and concise.
At the model-level, it produces global explanation subhypergraphs using unsupervised concept extraction. 
Extensive experiments across four real-world and four novel, synthetic hypergraph datasets demonstrate that our method finds high-quality explanations which can target a user-specified balance between faithfulness and concision, improving over baselines by 25 percent points in fidelity on average.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies a relatively unexplored problem of hypergraphs neural networks explanation for the task of node classification, both from the local and global perspective. The authors describe two methods they use for local and global explanations. They
then benchmark the methods on synthetic and real-world datasets against current baselines, notably with an updated fidelity metric.

### Strengths
- The topic is interesting, and still in unexplored territory.
- The paper is well written, the experiments seem to yield good results and the experimental design looks solid.

### Weaknesses
 - There is not a lot of theory in this paper, and the methods used are pretty straightforward. 
- The literature could be a bit more developed (the one other baseline on the problem, global explanations of GNNs, mean field approximation in the hypergraphs context).
- The local and global explanations techniques are completely decoupled, with the global
explanation in particular being transposed from a method already studied for GNNs. This is a liitle surprising, as the titled implied a deeper relationship.
- There should be more local and global explanations derived from this work and derived
from the GNNs explanation literature: benchmark different global explainer heuristic
based on the local explanation (as opposed to just one); for the local explanation, an
approximation technique with a more refined method, or at least explain why other
methods would not work.

Overall the paper needs a major revision.

### Questions
- Line 212 you use a mean-field approximation, can you justify this more, add some
literature that justifies such approximations for hypergraphs? Why can you do that
(specially in the context of hypergraphs)? Are there other approximations you explored
or considered? This is a pretty strong assumption.
 
- Please define a concept line 251; it seems to be specific to a GNN, and to be a cluster
of points in the GNN embedding space, and its ”representative” is the node closest to
the geometric center in the embedding space, is that correct?

- Line 249: Can you specify what the latent embedding space is for a node? Is it the
final layer’s output before the softmax?

- The local and global explainer seem to be two completely decoupled methods; please
point this out in the paper. How are they related?
 
- Have you tried other types of global explanations (e.g., GLGex-
plainer [1]) based on this local explainer? 

- Have you tried other local explanations techniques (there are plenty of work [2])?

- Has a similar sampling method for local explanations been used in GNN explanations?

Some minor comments:

– Equation (3) line 209 is not clear, I would write it differently.

– Some typos: “explainiability” line 75, “P r(v ∈ esub = 0)” line 206

– “coherent explanations” line 80: please clarify what this means.

– What is “InfoNCE” line 106? add context about noise-contrastive estimation.

– Line 259, GCExplainer is mentioned in the method, but there has not been a
reference since the introduction. It should be added on line 244 along with the
Magister paper.

– For the results, it would be helpful to separate the local from the global explanations.

– The paragraph starting line 259 compares GCExplainer with the method of the
paper, this is not clear, as it is never explained what GCExplainer does.

[1] Azzolin, Steve, Antonio Longa, Pietro Barbiero, Pietro Liò, and Andrea Passerini. "Global explainability of gnns via logic combination of learned concepts." arXiv preprint arXiv:2210.07147 (2022).

[2] Kakkad, Jaykumar, Jaspal Jannu, Kartik Sharma, Charu Aggarwal, and Sourav Medya. "A survey on explainability of graph neural networks." arXiv preprint arXiv:2306.01958 (2023).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces SHypX, the first model-agnostic post-hoc explainer for hyperGNNs that provides both local and global explanations. 
At the local level, it finds salient subhypergraphs to explain individual predictions using Gumbel-Softmax sampling, while balancing faithfulness and concision. 
For global explanations, it extracts concepts by clustering network representations and visualizing representative examples.

In experiments, the paper introduces four synthetic hypergraph datasets and generalized fidelity metrics for proper evaluation. 
Through experiments on both synthetic and real datasets, SHypX demonstrates superior performance over existing baselines while maintaining architecture independence, making it a significant contribution to hypergraph machine learning interpretability.

### Strengths
The paper presents multiple novel contributions: 
1. The first to provide both local and global explanations for hyperGNNs. 
2. Introduces a new sampling-based approach for local explanations that avoids using attention mechanisms. 
3. It develops techniques specifically designed for hypergraph structures. 
4. The synthetic datasets also represent an original contribution by creating structure-dependent tasks for evaluating hypergraph explainability.
5. This work addresses an important gap in making hyperGNNs more interpretable.

### Weaknesses
 **Insufficient Analysis of Graph-to-Hypergraph Explainability**

The paper provides some reasons why hypergraphs need specialized explainers, such as larger search spaces and structural differences. However, it lacks an in-depth analysis of what specifically would fail if traditional GNN explainers were used on constructed hypergraphs, which can be represented as graphs. Including a comparative study that illustrates concrete failure cases when applying regular GNN explainers to hypergraphs would significantly strengthen the motivation for developing specialized hypergraph explainers.

**Constrained Real-World Evaluation**

- The real-world datasets used in the paper are relatively small, which limits the ability to generalize the results. 
- Moreover, the paper acknowledges that the selected datasets may not sufficiently test the model's ability to understand hypergraph structure, given that even simple MLPs achieve competitive performance. While the inclusion of synthetic datasets partially addresses this limitation, it would be more compelling to include more complex real-world hypergraph datasets that present a greater challenge. Such datasets would better demonstrate the practical utility and robustness of the proposed method. - Furthermore, the constrained real-world evaluation raises the question: does the limited complexity and availability of these datasets indicate that the problem lacks substantial practical applications?

### Questions
**1.Insufficient Analysis of Graph-to-Hypergraph Explainability**
The paper provides some reasons why hypergraphs need specialized explainers, such as larger search spaces and structural differences. However, it lacks an in-depth analysis of what specifically would fail if traditional GNN explainers were used on constructed hypergraphs, which can be represented as graphs. Including a comparative study that illustrates concrete failure cases when applying regular GNN explainers to hypergraphs would significantly strengthen the motivation for developing specialized hypergraph explainers.

**2. Constrained Real-World Evaluation**
- The real-world datasets used in the paper are relatively small, which limits the ability to generalize the results. 
- Moreover, the paper acknowledges that the selected datasets may not sufficiently test the model's ability to understand hypergraph structure, given that even simple MLPs achieve competitive performance. While the inclusion of synthetic datasets partially addresses this limitation, it would be more compelling to include more complex real-world hypergraph datasets that present a greater challenge. Such datasets would better demonstrate the practical utility and robustness of the proposed method. - Furthermore, the constrained real-world evaluation raises the question: does the limited complexity and availability of these datasets indicate that the problem lacks substantial practical applications?

Minor Comment: In Figure 1, what does the "concept-to-class decision tree" icon represent? Providing a brief explanation would help improve clarity.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper addresses the post-hoc explainability of hypergraph neural networks (HyperGNNs) for the task of node classification in hypergraphs. The authors propose a method for providing both instance-level and global-level explanations for these models. The core idea of their approach is to sample node-hyperedge pairs in the computation graph of a specific node in a way that minimizes the loss function. Additionally, they introduce a set of synthetic hypergraphs to evaluate their method. Their experimental results demonstrate that the proposed method outperforms existing baselines.

### Strengths
- The paper is well-written and clearly presented.
- The authors address both instance-level and global-level explainability for HyperGNNs while latter has not been addressed previously.

### Weaknesses
 - My main concern is that this paper only addresses explainability for the task of node classification in hypergraphs, which is a less interesting and important problem compared to (hyper)graph classification.
- The baselines used in this paper are not sufficient. While there might not be many related works on explainability in hypergraphs, explainability methods for graph neural networks could be applied and compared with the proposed method.
- The quantitative evaluation on real-world datasets shows very low performance, and the differences between the various baselines are minimal, making it difficult to determine if the proposed method performs significantly better than the other baselines.
- While having synthetic datasets for an explainability method is crucial, it is not clear how the proposed synthetic datasets are particularly useful in this setting.
- For the task of node classification, what would happen if a method returns only the first immediate neighbors of a node as the most important sub-hypergraph? Specifically, how would the fidelity metrics mentioned in this paper perform in this scenario? My main point is that having only an explainability model for node classification may not be of significant importance.
- Could you present a hypergraph as a bipartite graph and apply graph-based explainability models to compare their performance with your method? It would be particularly useful to try GNNExplainer, as this method is very intuitive, and it is not immediately clear why it would not perform well in your setting.
- For the global explainer, you are introducing yet another black-box, despite mentioning that SHypX "doesn’t rely on additional black-box networks." Could you clarify this contradiction?
- It is necessary to visualize the results of the explanations for at least the synthetic datasets to visually assess which sub-hypergraphs SHypX identifies as important.
- Figure 4 is very confusing, and the results you are trying to convey are not clear. Is there an alternative way to evaluate global explanations that might be more effective?
- I still believe the best approach to using GNN explainers for hypergraphs is to treat them as bipartite graphs. While the authors have shown results for GNNExplainer, they convert the hypergraph to a graph, which is a lossy approach and could indeed result in poor outcomes.
- Furthermore, I would like a more thorough discussion on why it is necessary to have an explainability approach specifically for hypergraph neural networks and why GNN-based approaches (with minimal changes) are not sufficient. I am not convinced by the authors' discussion so far.
- Additionally, it seems like SHypX performs well on Fid -, but not as well on Fid+. This discrepancy needs further investigation. I would also like to see the results for Fid+ using GNNExplainer for a more comprehensive comparison.
- Regarding GNNExplainer, I believe that the adaptation you mentioned might be contributing to the poor results observed. I am particularly interested in seeing the results when you convert the hypergraph to a bipartite graph. In this representation, you would have one set of nodes representing the original nodes and another set representing the hyperedges, with the adjacency matrix constructed accordingly. This approach would allow you to maintain the use of a hypergraph for your hyperGNN while providing GNNExplainer with a bipartite representation.
- Additionally, I noticed that you reported a fid-acc of 0.00 and a fid-kl of almost 0.00 for most datasets in your comparison with GNNExplainer. These results are quite difficult to interpret. Although you mentioned that Fid+ is not an appropriate metric, including it might still offer some insights.

### Questions
- For the task of node classification, what would happen if a method returns only the first immediate neighbors of a node as the most important sub-hypergraph? Specifically, how would the fidelity metrics mentioned in this paper perform in this scenario? My main point is that having only an explainability model for node classification may not be of significant importance.

- Could you present a hypergraph as a bipartite graph and apply graph-based explainability models to compare their performance with your method? It would be particularly useful to try GNNExplainer, as this method is very intuitive, and it is not immediately clear why it would not perform well in your setting.

- For the global explainer, you are introducing yet another black-box, despite mentioning that SHypX "doesn’t rely on additional black-box networks." Could you clarify this contradiction?

- It is necessary to visualize the results of the explanations for at least the synthetic datasets to visually assess which sub-hypergraphs SHypX identifies as important.

- Figure 4 is very confusing, and the results you are trying to convey are not clear. Is there an alternative way to evaluate global explanations that might be more effective?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an explainer for hyperGNNs at both instance-level and global-level, which is called SHypX. At both instance-level and global-level, they extract salient subhypergraphs as the explanation. Four synthetic datasets were introduced in this paper, although none of them are open-sourced.

### Strengths
1. This paper is the second work on hyperGNN explainability. 
2. They introduce a new benchmark that contains four synthetic datasets to evaluate hyperGNN explanations.

### Weaknesses
1. Related work is not thoroughly reviewed, and more recent studies should be discussed. The limitations of existing approaches for GNN explainability in the context of hyperGNNs are not clearly addressed. Since most existing methods are model-agnostic, they should be able to provide explanations for hyperGNNs too. 
2. The newly introduced datasets are not provided. 
3. The presentation is not very good. For example, the caption of Fig 2 is confusing. 
4. The performance improvements on real world datasets seems minimal. 
5. The evaluation on the global-level explainability is too few. It doesn't seem that this explainer actually produce global-level explanations.  
6. Some concerns about motivation and metrics. See questions.

### Questions
1. In Line 171, it says "our goal is to produce an explanation subhypergraph" for the local explainer. However, a single subhypergraph may not be enough to fully explain the prediction. Why do you only consider to produce a single explanation subhypergraph for each graph sample? 
2. The proposed method doesn't look to be specifically designed for hyperGNNs. For example, modules like Gumbel-Softmax samplers and global clustering. Why don't apply your method also to traditional GNNs? And why not use the explainers for those traditional GNNs, (which didn't use Gumbel-Softmax samplers, but some other methods to pick crucial subgraphs) to explain hyperGNNs? 
3. For the Fidelity evaluation, why do you only evaluate the Fidelity-, how about Fidelity+?

### Soundness
2

### Presentation
2

### Contribution
2
