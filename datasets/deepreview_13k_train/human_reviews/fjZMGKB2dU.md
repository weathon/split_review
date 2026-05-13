# A neuro-symbolic framework for answering conjunctive queries

- Decision: Reject
- Scores: 3, 3, 6, 3, 3

## Abstract
The problem of answering logical queries over incomplete knowledge graphs is receiving significant attention in the machine learning community. Neuro-symbolic models are a promising recent approach, showing good performance and allowing for good interpretability properties. These models rely on trained architectures to execute atomic queries, combining them with modules that simulate the symbolic operators in queries. Unfortunately, most neuro-symbolic query processors are limited to the so-called _tree-like_ logical queries that admit a bottom-up execution, where the leaves are constant values or _anchors_, and the root is the target variable. Tree-like queries, while expressive, fail short to express properties in knowledge graphs that are important in practice, such as the existence of multiple edges between entities or the presence of triangles. 

We propose a framework for answering arbitrary conjunctive queries over incomplete knowledge graphs. The main idea of our method is to approximate a cyclic query by an infinite family of tree-like queries, and then leverage existing models for the latter. Our approximations achieve strong guarantees: they are _complete_, i.e. there are no false negatives, and  _optimal_, i.e. they provide the best possible approximation using tree-like queries. Our method requires the approximations to be tree-like queries where the leaves are anchors or existentially quantified variables. Hence, we also show how some of the existing neuro-symbolic models can handle these queries, which is of independent interest. Experiments show that our approximation strategy achieves competitive results, and that including queries with existentially quantified variables tends to improve the general performance of these models, both on tree-like queries and on our approximation strategy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
For a form of conjunctive queries (conjunction of binary predicates, projecting on all-but-one of the variables), this paper applies a technique that works for for the certainty case to reasoning under uncertainty that is inherent in learned models.

### Strengths
It is all plausible and I'm willing to accept works for the certainty case. (Except for the infinity claim).

### Weaknesses
This paper is trying to apply a technique that works for the certainty case to reasoning under uncertainty that is inherent in learned models. In particular, it is assuming that the probability of a disjunction is like the maximum probability of its components. Consider the cyclic CQ of Figure 1 (c): as the number of friends of someone goes to infinity, the probability that two of them are coworkers should approach 1. If you wanted a particular x,y and z, what you propose may be more sensible, but not when the query is for just one of them and the others are existentially quantified.

You need to convince us that the sort of queries you can handle is a useful class. (E.g., the valid path restrictions seems very restrictive.) Can it answer *all* queries on knowledge graphs (including when the knowledge graph has arbitrarily many reified relation)?. E.g., this seems to include many fewer queries than could be made with say Problog, which I don't think has any of the restrictions you embrace.

Page 3 "y and z are both existentially quantified" isn't true as it stands. They are universally quantified at the scope of the rule, and existentially quantified in the scope of the body.

I don't understand why "the number of approximations is infinite". If we ground a graph out to propositions (by replacing variables with the elements of the population of entities in all ways), the model is still finite. There is exponential explosion, but it's not infinite. This makes me suspicious. Surely, you can check for loops which would make it finite. However I suspect it is exponential in path length, so that is probably moot. Please give us the complexity.

What is the mean reciprocal rank of a set? How do you rank sets? If there are multiple witnesses for one x (e.g, multiple instance of y and z for a single x), how do you choose which one if the ground truth? What is the ground truth?

What is "the Spearman correlation rank between the total number of answers...."? Spearman rank correlation measures differences between ranks. Why is it appropriate for the total number of answers?

The MRRs for FB15k-237 seem particularly low. The methods don't seem to work. It seems like the modifications that were made to create  FB15k-237 from  FB15k are exactly what your are exploiting. The Spearman rank correlation seems particularly high. Can you explain these results?

I see the problem (one of them). You assume that you can treat a learned knowledge graph like a standard knowledge graph. I don't think you can; you need to see it as making probabilistic predictions, which need to be combined using the logic of probability, not the logic of Booleans. If the system is not sure about the truth of some relations/properties, it should not act like it does know the truth.

The paper says "we report the mean reciprocal rank (mrr) of the predicted answer set". That contradicts what you said in your answer (I know what the MRR is, just not the MRR of a set is).

There are lots more things not defined such as (1p/2p/3p/2i/3i/2in/3in/inp/pni/pin)

"Note that the unary part comes from the need to work with vector representation (which is currently the limit of neural methods)". Working with vectors does not imply unary. There is lots of work predicting higher-order relations (some going by the title of "knowledge hypergraphs").

### Questions
What is the mean reciprocal rank of a set? How do you rank sets? If there are multiple witnesses for one x (e.g, multiple instance of y and z for a single x), how do you choose which one if the ground truth? What is the ground truth?

What is "the Spearman correlation rank between the total number of answers...."? Spearman rank correlation measures differences between ranks. Why is it appropriate for the total number of answers?

The MRRs for FB15k-237 seem particularly low. The methods don't seem to work. It seems like the modifications that were made to create  FB15k-237 from  FB15k are exactly what your are exploiting. The Spearman rank correlation seems particularly high. Can you explain these results?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper deals with the problem of solving complex queries from knowledge graphs.

### Strengths
The idea of approximate a cyclic CQ by a family of tree-like CQs is interesting. The connection with respect to ensemble methods should be discussed. It is not clear how many tree-like queries are used to approximate a cyclic one. This should be stressed in the paper.

### Weaknesses
There are many concepts introduced in the paper that are already discussed in inductive logic programming literature. See for instance the definition of containement and homomorphism that are known as substitution in logic programming.

There is a lack of discussion of the related concepts and results known in statistical relational learning and in inductive logic programming. Furthermore, it should be interesting to introduce in the paper the notion of open world assumption that is not discussed.

Please note that the completeness property introduced in the paper corresponds to the notion of clause substitution introduced many years ago in the logic programming literature. The homomorphism introduced in the paper is already called substitution (see fo instance [1]).  

Finally, the experimental evaluation should be extended to include other approaches. It is not clear the contribution of the proposed approach.

### Questions
Stress the contribution and the experimental results

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a framework for answering arbitrary conjunctive queries over incomplete knowledge graphs. The main idea of the approach is to approximate a cycle query by an infinite family of tree-like queries, and leverage existing models for the latter. Such approximations come with strong guarantees, namely completeness and optimality.

### Strengths
- The paper was, for the most paper, well-written and easy to follow.
- In a neuro-symbolic setting, the authors are the first to tackle the problem of answering cyclic queries on incomplete knowledge graphs.
- The proposed approach is quite intuitive and simple, essentially a linear approximation of the logical query. This has the added benefit that, once approximated, the task of answering the logical query can be delegated to any state-of-the-art near-symbolic query processor.
- The approximation is guaranteed to be complete, as well as optimal for a given computational budget.

### Weaknesses
 - One apparent weakness seems to be the addition of yet another hyper-parameter $d$ which determines the depth of the tree to which the cyclic logical query is unraveled. The choice of this parameter is crucial, as too small values will lead to an under-approximation of the original cyclic query, while too large values can lead to a computational overhead without significant gain in accuracy. The paper does not provide a clear methodology for choosing this parameter, relying instead on empirical fitting, which might not generalize well across different datasets or query structures.

- The proposed approach seems to achieve a lower performance compared to the baseline when evaluated on anchored tree-like queries. This is concerning, as it suggests that the approximation method, while beneficial for cyclic queries, might actually degrade performance on simpler, more common query types. The fact that the method does not consistently outperform the baseline even on tree-like queries raises questions about its overall robustness and applicability.

### Questions
- Do you have any intuition as to why the proposed approach seems to perform worse, on average, compared to the baseline on anchored tree-like queries?

- In the experimental setup you mentioned that you "additionally provide a new set of training, validation and test queries...". Is this in addition to the unanchored set originally in the dataset? I was under the impression that your method could only handle unanchored queries?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a novel neuro-symbolic framework for approximating complex queries on knowledge graphs. The method uses tree-like queries to approximate complex conjunctive queries and is implemented on top of GNN-QE. Some experiment results on FB15K, FB15k-237, and Nell995 datasets outperform SOTA level.

### Strengths
not identified yet.

### Weaknesses
The presentation of the paper is poor. This prevents the understanding of the content. The motivation and the research question are not clear. The experiment results are not always better than the based-line. But, only experiments on benchmark datasets FB15K, FB15k-237 are not sufficient to support authors' second and third contribution claims. The core idea of approximating complex queries with tree-like queries lacks a strong theoretical justification. The paper does not clearly define the specific class of conjunctive queries being addressed, making it difficult to assess the scope and limitations of the proposed method. Furthermore, the notion of 'approximating' a query is not rigorously defined, leaving ambiguity about the quality of the approximation and how it relates to the original query's semantics. The claim that the method is 'neuro-symbolic' is not well-supported; it appears to be a neural network trained to predict query results, without a clear integration of symbolic reasoning.

### Questions
Why shall we be interested in the research of answering arbitrary conjunctive queries over incomplete knowledge graphs? 

Would this method also work for complete knowledge graphs? 

What is the intuition behind the idea of "approximating a cyclic query by an infinite family of tree-like queries"? 

What if a relation is self-reflective? 

What do you mean by "neuro-symbolic framework"?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses the challenge of answering logical queries over incomplete knowledge graphs (KGs). The authors argue that current approaches are limited in that they focus on monadic anchored tree-shaped queries, characterized by query dependency graphs with a tree structure and constant values as leaf nodes. To address this limitation, the paper claims the following contributions:

(C1) A technique for over-approximating arbitrary monadic CQs as tree-shaped CQs (without anchors). This means that, given a CQ q, the technique would generate a tree shaped q’ that subsumes q (meaning that each answer to q on any dataset is contained in the answer set for q’ on the same dataset) and which is “optimal” in some well-defined way

(C2) A proposal to adapt the method of Zhu et al. for anchored tree-shaped CQs to the unanchored setting

Additionally, the authors provide empirical results based on established benchmarks related to these tasks.

### Strengths
The topic of query answering over incomplete KGs has attracted significant attention in recent years. Hence, this submission is clearly relevant to ICLR. Furthermore, the problem of approximating CQs has also received attention within the database theory and knowledge representation research communities. The paper is also clearly written and the main formal claims in the paper appear correct. The paper does make a contribution to the current state-of-the-art, albeit one that I consider rather modest (for specific elaboration, please see below).

### Weaknesses
As previously mentioned, I find the claimed contribution rather limited. Specifically, Contribution (C1) is not directly related to the field of Machine Learning; the results it claims are strictly within the domain of database theory. Unravelling techniques are conventional in database theory and knowledge representation. Furthermore, the observation that the tree unraveling (to any depth) of a non-tree-shaped conjunctive query results in an over-approximation of the original query might be considered common knowledge within the community. Therefore, as a researcher with main background in database theory, logic, and knowledge representation, I regard the primary findings presented in Section 4.1 as straightforward observations that might not carry sufficient significance for publication.

The significance of (C1) in the context of the current machine learning-based query answering state-of-the-art is also not evident to me. As the authors have mentioned, existing approaches are unable to handle arbitrary monadic tree-shaped conjunctive queries (CQs) without the requirement of query anchoring. Consequently, most of these approaches cannot directly leverage the proposed approximation. This brings us to Contribution (C2), in which the authors introduce an expansion of Zhu et al.'s method to encompass unanchored queries. This extension is not sufficiently elaborated and it is unclear it what manner it enables the technique by Zhu et al to "support" arbitrary tree shaped CQs. Additionally, it is uncertain whether this extension can be applied to other methods, especially those dependent on the existence of embeddings for the anchors.  This doesn't seem straightforward in my view.

I also found the experimental results somewhat perplexing. Specifically, in the comparison between GNN-QE and its extension, \exists GNN-QE, applied to anchored queries, both systems are trained on distinct datasets; the significance of the reported results remains unclear to me in this context. Adding to the confusion, the experiments appear to include results for queries that may not strictly adhere to conjunctive queries (CQs) and may incorporate other first-order constructs, including negation. To the best of my knowledge, the results presented in the core technical sections of the paper are confined to CQs (and indeed, the seminal result by Chandra and Merlin only applies to CQs).

### Questions
- Please clarify the applicability of your results to queries involving disjunction and negation.

- Please clarify whether methods other than that by Zhu et al. can be easily extended to support CQs.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
