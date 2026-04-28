# Graph-based algorithms for nearest neighbor search with multiple filters

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 8, 3

## Abstract
We study nearest neighbor search with filter constraints (MultiFilterANN): given a query vector with a discrete set of labels $S$, retrieve the (approximately) closest vector from a dataset under the constraint that $S$ must be a subset of the labels of the retrieved vector. There has been a burgeoning interest in this problem on the practical side, due to its strong motivation from search and recommendation applications where vector labels correspond to real world attributes such as date, price, or color. On the theoretical side, this problem generalizes the subset query problem, which asks us to only determine if $S$ is a subset of some set in the dataset, without retrieving the closest vector.

In this work, we present a systematic study of MultiFilterANN,. Theoretically, we demonstrate the power of graph-based algorithms in two ways: 

-  We design provable algorithms with the best known space-time tradeoffs for \mfann in the large filter regime by carefully incorporating ANN algorithms into known subset query algorithms.% to incorporate nearest neighbor search using graph-based algorithms.
- We demonstrate lower bounds for popular algorithms for MultiFilterANN, showing that they can catastrophically fail even on simple data/label sets.

Our theoretical results inspire our empirical approach, where we extend practical graph indices for standard nearest neighbor search to MultiFilterANN by augmenting the (greedy) search procedure with a penalized distance function that captures filter constraints. Our empirical algorithm is competitive with existing state of the art solutions which are tailored for one or two filters, while also seamlessly generalizing to any number of filters without any modifications. Lastly we release multiple novel datasets for MultiFilterANN, filling in a noticeable gap in literature.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The article considers a task the authors call MultiFilterANN. MultiFilterANN extends standard approximate nearest neighbor (ANN) search by assuming that both the query point and the database points have labels from the discrete label space $[m]$, and setting a hard constraint that the label set of the query point must be a subset of any (approximate) nearest neighbor returned by the algorithm. The article proposes an algorithm that extends earlier work on graph-based filtered ANN search. Specifically, they propose searching a FilteredDiskANN graph (Gollabudi et al. 2023) by greedy penalty search (Wang et al., 2024), where the symmetric label distance used in the penalty computations is replaced by the asymmetric label distance. According to the empirical evaluation, the proposed method outperforms the earlier filtered ANN methods ParlayIVF$^2$ and ACORN in the special case of two filters. The article also discusses the limitations of earlier filtered ANN methods in the case of multiple filters, and provides toy examples where these methods perform badly. In addition, theoretical guarantees are presented for a different MultiFilterANN algorithm (that combines a graph or LSH index with a CIP data structure for a subset query problem).

Gollapudi, Siddharth, et al. "Filtered-diskann: Graph algorithms for approximate nearest neighbor search with filters." Proceedings of the ACM Web Conference, p. 3406-3416. 2023. 

Wang, Mengzhao, et al. "An efficient and robust framework for approximate nearest neighbor search with attribute constraint." Advances in Neural Information Processing Systems 36 (2024).

### Strengths
The idea of replacing the symmetric label distance with the asymmetric label distance on the greedy search of NHQ algorithm (Wang et al., 2024) is intuitive, and it self-evidently improves performance when the label constraint are subset queries ($S_q \subset S_v$) instead of exact matches ($S_q = S_v$). 

Wang, Mengzhao, et al. "An efficient and robust framework for approximate nearest neighbor search with attribute constraint." Advances in Neural Information Processing Systems 36 (2024).

### Weaknesses
The authors propose (in Section 6) a graph-based algorithm for MultiFilterANN problem (I explain my interpretation of the proposed method in Summary). However, it seems to this reviewer that the proposed algorithm is supported neither by (a) theoretical results, nor by (b) empirical evaluation. The theoretical results are for the different algorithm (described in Section 4) and it may be that the algorithm that is evaluated empirically in Section 7 is a yet different algorithm (described in Appendix E).

Specifically, the article starts by reviewing a CIP data structure (Charikar et al., 2002) for subset query problem and then proposing a MultiFilterANN algorithm that combines it with either a graph or LSH index structure. However, later in Section 6 it turns out that the authors propose a completely different graph-based empirical algorithm that does not use a CIP data structure at all. Thus it seems that theoretical analysis of Section 4 is disconnected from the rest of the article (except that MultiFilterANN problem is considered), and does not offer theoretical support for the proposed method. The authors should clarify what is the connection between the empirical algorithm and the theoretical discussion of Section 4.

Another part that must be clarified significantly is the empirical evaluation in Section 7. In particular, it is unclear whether the results are obtained by using the graph-based method proposed in Section 6 or the hybrid methodology described in Appendix E? According Appendix E, when the estimated number database points satisfying the constraints is small, either a brute force search after identification of these points, or a clustering-based approach is used instead of the graph-based method proposed in Section 6. If the hybrid methodology of Appendix E is used to generate the results of Section 7, this does not yet tell anything about the performance of the proposed graph method, since it is possible that the results are obtained using brute force search or a clustering-based approach.

You should include a direct comparison between the proposed graph method and the earlier filtered ANN methods (ParlayIVF$^2$ and ACORN) (assuming the results of Section 7 are for the hybrid method described in Appendix E). In particular, when the number of database points satisfying the constraints is small, I suspect that the brute force baseline is the fastest method, and if you enable this option for your method, but not for ParlayIVF$^2$ and ACORN, this distorts the results. In addition, you should include ablation experiments documenting in which regime your method outperforms this simple baseline (that has an additional benefit of producing exact results).

It is also not clear how relevant the studied problem (MultiFilterANN) is. I am not deeply familiar with literature on filtered ANN search, but it seems that the recent related works cited by the authors only consider the special cases of one or two filters. In particular, I suspect that when there are multiple filters (for instance, $|S_q| \geq 3$), the simplest possible ad hoc approach (brute force search after finding the database points with correct labels) would often outperform more complicated filtered ANN methods, since in this case the set of database points matching all of query labels is probably quite small.

Presentation is low quality. The article does not seem carefully finished. For instance, citations should be inside the parenthesis when the author names are not used as a part of the text. For instance, you should write "we may use Locality Sensitive Hashing (Indyk & Motwani 1998a)" instead of "we may use Locality Sensitive Hashing Indyk & Motwani 1998a". Just use citep-command if you are using natbib. As an another example, there is a list of 26 (!) consecutive citations in the beginning of Related work-section. It seems that the only relevance of these works is that they are connected to ANN search. You should be much more specific in Related work-section and do not use this kind of generic lists.

### Questions
Can clarify how the theoretical results of Section 4 are connected to the empirical algorithm you propose in Section 6? It seems to this reviewer that the algorithm considered in Section 4 (2-stage search where you first prune a candidate set on the label space $[m]$ with a CIP data structure, and then perform a nn-search on the continuous feature space $\mathbb{R}^d$ with either LSH or a graph) is completely different than the one you propose in Section 6 (FilteredDiskANN graph from earlier work (Gollabudi et al., 2023) combined with greedy search penalized by asymmetric label distance)?

Are the results of Section 7 for the graph-based approach of Section 6 or for the hybrid approach of Appendix E that also can use either brute force search or clustering?

Gollapudi, Siddharth, et al. "Filtered-diskann: Graph algorithms for approximate nearest neighbor search with filters." Proceedings of the ACM Web Conference, p. 3406-3416. 2023.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies a constrained variant of approximate nearest neighbor search where the labels of a query vector must be a subset of the labels of each retrieved vector. The authors prove theoretical bounds for the problem based on both earlier work on the subset query problem and earlier bounds for LSH and graph-based methods. The authors also propose an improved empirical algorithm based on FilteredDiskANN for the problem.

### Strengths
- The paper studies an important practical problem encountered in many real-world use cases of nearest neighbor search. Currently, the problem of incorporating multiple filters into the standard vector search problem is not addressed well by any of the existing methods.
- The paper makes fairly interesting novel contributions to the problem both in theory and in practice. In particular, the connection to the subset query problem and the analysis using the CIP data structure is quite interesting and the proposed penalty search method seems to work well in practice.

### Weaknesses
Instead of studying the performance of a practical multiple filter nearest neighbor search algorithm, the authors design a theoretical algorithm using (what the authors refer to as) the CIP data structure for the subset query problem but with the final groups in the structure replaced with ANN indexes. However, while connecting these is quite neat, the theory is not really insightful and I don't see how these results inspire the empirical algorithm presented in Section 6.

The authors write that there are two lessons to be learned from the theoretical analysis, the first one being that graph-based ANN algorithms are powerful for the multi-filter variant. However, just because you can get theoretical guarantees by using them in the last level of the CIP data structure (as you can with any ANN index), does not logically imply that purely graph-based methods would be specifically suited for the problem. The underlying hypothesis is actually simply that since graph-based methods are SOTA for standard ANN, they probably are also for the multi-filter variant. The second given lesson is that query planning is important. However, routing queries to relevant subsets is a natural part of any ANN algorithm and I do not see any specific connection between the routing in CIP and your proposed heuristic query planning method. It would be helpful for the authors to clarify any possible connections beyond these lessons.

Instead, the paper proposes a heuristic method building upon an existing method (FilteredDiskANN) by introducing the penalty search method and query planning to the algorithm. The penalty search is quite interesting, but in practice has to be approximated and refined in an ad hoc way, introducing two additional hyperparameters, $\lambda$ and $\tau$. The proposed query planning method is also very ad hoc and not studied well in detail (see below). The authors also provide instances where prior algorithms fail. In some cases studying such failure cases leads to further insight, but I do not find these particular cases to be interesting from the theory point of view and in practice the nature of ANN search is that we mostly do not really care about the worst case as long as the methods work on real-world datasets (for which many algorithms work well regardless of e.g. the curse of dimensionality).

For the experiments, the authors should be more clear as to why they do not compare against FilteredDiskANN (it does not work well for more than one filter?). There is an ablation on the effect of the penalty search on one data set, but you would need to compare against FilteredDiskANN on all data sets, and you also need to have an ablation study on the effect of the query planning. You can apply the query planning to any of the algorithms; right now I cannot tell which part of your method affects its performance the most. In contrast, I do not find the ablation studies for the query correlation or the query filter selectivity to be that interesting. Finally, you should analyze more deeply why your method works better than the other methods on the dataset you introduce as opposed to e.g. the Amazon data set where there is no improvement compared to ACORN. The provided new data set is quite interesting but in the abstract, the authors claim to introduce multiple novel datasets (I would not count the synthetic datasets here).

The paper is quite hard to read with multiple issues in the presentation. To improve the presentation, the authors should at least
  - Refer to the relevant Appendix where proofs can be found, e.g. for Lemmas 5.1-5.3.
  - Add "for every $\delta > 0$" to the statement of Theorem 4.1
  - Use \citep for citations, currently the lack of parentheses makes the text difficult to read
  - Explain properly how prior work relates to the paper instead of just giving a long list of citations (Section 3)
  - Give a name for your algorithm such that it is easier to refer to
  - Make sure figures that are next to each other are of the same size
  - Include a discussion section

### Questions
- Is your theory only applicable to $\ell_2$ as the proof of Theorem 4.1 would imply?
- How do you select the cut-offs for your proposed query planning method? Are they the same for each dataset?
- How difficult are the hyperparameters $\lambda$ and $\tau$ to set?
- Which data set is used for the ablation study on removing the penalty search?
- Why does ParlayIVF2 only have one instance on the Pareto frontier in two of the experiments?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studied the high-dimension nearest neighbor search problem with label constraints. The problem is defined as follows: we are given a dataset $X$ where each item is a vector and has a set of labels; we are required to build a data structure such that for every given query vector $q$ with a set of labels $S_q$, we should find a vector $v\in X$ that is approximately the closest and the labels $S_v$ is a subset of $S_q$. The problem is motivated by real-life search and recommendation applications, where we are usually required to return ‘similar queries’ with some properties specified by ‘filters’. 

There are both theoretical and practical results in this paper. On the theoretical side, the paper designed an algorithm that uses $o(2^m)$ memory and returns an approximation solution in $o(n)$ time, where $n$ is the number of elements in the dataset and $m$ is the maximum cardinality of $S_q$. The algorithm is based on the subset-query algorithm of CIP [ICALP’02] and the celebrated LSH. Furthermore, by substituting the LSH with graph-based structures, the paper obtained dimensionality-independent memory bound that scales with $1/\varepsilon^{O(\lambda)}$, where $\varepsilon$ is the parameter in the $(1+\varepsilon)$-approximation and $\lambda$ is the doubling dimension of the dataset. On the practical side, the paper used a host of heuristic methods inspired by their theoretical result and obtained state-of-the-art empirical performances.

The main techniques of the paper are quite straightforward: it combines the subset-query algorithm of CIP [ICALP’02] with LSH and graph-based nearest-neighbor search algorithms. It’s interesting to see that some decade-old results in algorithm design could be helpful for modern machine learning applications.

### Strengths
In general, I have a positive opinion of this paper: the problem it studied is extremely relevant to modern machine learning applications, the paper is well-written, and it contains a very cute connection between theory and practice. The ‘lessons’ listed in the paper are quite clear and should be easy to digest for practitioners (in my opinion, although I work on the more theoretical side), and the theory-inspired practical approach outperformed state-of-the-art empirical algorithms. I enjoyed a good read of the paper, and I would advocate for its acceptance.

### Weaknesses
W1. On theoretical side, the SQ problem only determines that there exists Sx such that Sq \subset Sx. It does not report **all** Sx such that Sq \subset Sx. Therefore, I think the claim of Theorem 4.1 and 4.2 are not correct.

A simple case for LSH is follows. 
Assume that there exists an cr instance x that is not in the reported group of the SQ's data structure, then LSH will report empty at the certain radius r. The algorithm then continues with larger c. In this case, you cannot guarantee (1+ \eps)-ANNS. 
Another sanity check is that all instances x \in X satisfies the constraint. Hence, reporting a group of n^\delta points by CIP (Charikar et al. 02) clearly affects the (1+\eps) guarantees.
Since SQ's data structure cannot guarantee to report all elements x such that Sq \subset Sx, there will be an uncontrolled probability that DIC & LSH fail to guarantee (1 + \eps)-ANNS. Unfortunately, I do not think the used technique CIP & LSH (or graph-based index) can fix this issue without increasing the time and space complexity.

W2. I found the theoretical analysis and the proposed algorithms are not aligned well though there are several raised issues (i.e. lessons) to connect them together. In the end, the proposed algorithm is a combination between FilteredDiskANN (Gollapudi et al. 2023) with new fused distance measure (inherited in NHQ - Wang et al. 2023).

W3. Since the proposed graph-based data structure is very similar to FilteredDiskANN and NHQ, these methods should be used as baselines. Unfortunate, there are no comparison with these works in the experiment sections. The key parameter \lambda used in the proposed penalty distance has not been investigated (the value setting, sensitivity).

W4. There are two new fused distances including dist' and \hat{dist}, which use Sq in the querying phase. Though it is not clear to me which measure are used for querying, it seems that the proof of Theorem 6.1 with dist' in the appendix is not correct. 
Given a large \lambda, the contribution of second term dominates dist'. How could it guarantee to answer MFANN according the distance in the first term? It looks to me the proof is an heuristic argument since given the graph index, filtering out point y such that Sq \notsubset Sy cannot bring you to the closet point x such that Sq \subset Sx.

W5. There are significant room to improve the paper. 

For example, Related work need to be rewritten. 
First half of the content is just listing the citations without any discussions.
The second half includes only claims. E.g. 
CAPS seems to suffer significantly as m increase --> By how it suffers?
SERF works with range queries --> MFANN is not designed for range queries as well
These ideas do not generalize to multi filters --> Reasons?
ACORN do not scale well to even simple AND predicates --> By how?

### Questions
- Do you have comments about the hidden constant in the exponent of $2^{O(m\sqrt{\delta}\log^{2}{m})}$?
- Also, in Theorem 4.2, the bound would hold only for $\varepsilon<1$ right? Say that if I only want a $10$ approximation, how would the bound scale? 
- For the definition of the doubling dimension of datasets, I would suggest having more discussions after the definition to help the readers understand the notion better (this is a MISC comment).
- The problem studied in this paper emphasizes that the labels of the required query vector $q$ have to be a subset of the given set $S_q$. If we instead only want $S_v \cap S_q \neq \emptyset$, or something like $|S_v \cap S_q|\geq  0.1\cdot |S_q|$, does the problem changes drastically?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies the problem called MultiFilterANN (MFANN for short) that extends the approximate nearest neighbor search (ANNS) with additional constraints. 
Such new constraints require a new label set Sx for each data point x, and ask to answer ANNS given a query q and label set Sq, such that Sq \subset Sx for the returned top-k nearest neighbors x.
This problem is of important in many applications in recommender system and vector search engines.

The paper first proposes to study the Subset Query problem (SQ for short) to deal with the constraint Sq \subset Sx.
In theory, the paper shows that combining the solution of SQ with popular (LSH-based or graph-based) data structures can solve MFANN, and points out that the complexity of MFANN is dominated by SQ (Theorem 4.1 and 4.2).
In practice, the paper shows a variant of graph-based data structure, called FilterDiskANN, with a new fused distance measure incorporating the contrainsts via a new embedding. 
Empirical results show that the proposed method is competitive with ACORN and clustering-based ParlayIVF2 in many real-world data sets.

### Strengths
S1. The paper studies an emerging problem MultiFilterANN (MFANN), a variant of ANNS with attribute contraints, which is important in many LLM-based applications and vector search engines.

S2. A theoretical analysis of the subset query (SQ) problem to MFANN is proposed.

S3. A practical graph-based solution to answer MFANN is proposed.

### Weaknesses
W1. On theoretical side, the SQ problem only determines that there exists Sx such that Sq \subset Sx. It does not report **all** Sx such that Sq \ subset Sx. Therefore, I think the claim of Theorem 4.1 and 4.2 are not correct.

A simple case for LSH is follows. 
Assume that there exists an cr instance x that is not in the reported group of the SQ's data structure, then LSH will report empty at the certain radius r. The algorithm then continues with larger c. In this case, you cannot guarantee (1+ \eps)-ANNS. 
Another sanity check is that all instances x \in X satisfies the constraint. Hence, reporting a group of n^\delta points by CIP (Charikar et al. 02) clearly affects the (1+\eps) guarantees.
Since SQ's data structure cannot guarantee to report all elements x such that Sq \subset Sx, there will be an uncontrolled probability that DIC & LSH fail to guarantee (1 + \eps)-ANNS. Unfortunately, I do not think the used technique CIP & LSH (or graph-based index) can fix this issue without increasing the time and space complexity.

W2. I found the theoretical analysis and the proposed algorithms are not aligned well though there are several raised issues (i.e. lessons) to connect them together. In the end, the proposed algorithm is a combination between FilteredDiskANN (Gollapudi et al. 2023) with new fused distance measure (inherited in NHQ - Wang et al. 2023).

W3. Since the proposed graph-based data structure is very similar to FilteredDiskANN and NHQ, these methods should be used as baselines. Unfortunate, there are no comparison with these works in the experiment sections. The key parameter \lambda used in the proposed penalty distance has not been investigated (the value setting, sensitivity).

W4. There are two new fused distances including dist' and \hat{dist}, which use Sq in the querying phase. Though it is not clear to me which measure are used for querying, it seems that the proof of Theorem 6.1 with dist' in the appendix is not correct. 
Given a large \lambda, the contribution of second term dominates dist'. How could it guarantee to answer MFANN according the distance in the first term? It looks to me the proof is an heuristic argument since given the graph index, filtering out point y such that Sq \notsubset Sy cannot bring you to the closet point x such that Sq \subset Sx.

W5. There are significant room to improve the paper. 

For example, Related work need to be rewritten. 
First half of the content is just listing the citations without any discussions.
The second half includes only claims. E.g. 
CAPS seems to suffer significantly as m increase --> By how it suffers?
SERF works with range queries --> MFANN is not designed for range queries as well
These ideas do not generalize to multi filters --> Reasons?
ACORN do not scale well to even simple AND predicates --> By how?

Given previous works on graph-based solutions (ACORN, FilteredDiskANN, NHQ) for MFANN, I do not think all raised lessons are important. Perhaps sticking on the key lesson directly influenced the design of your final algorithm might be better.

### Questions
Could you address the raised weaknesses W1 -- W4 above?

There are several claims on the paper that seem to be vague or need the contexts. So I raise following questions for clarification

Q1) What is the definition of space-time tradeoff of MultiFilterANN?
Q2) What are lower bounds of space or time complexity of algorithms for MultiFilterANN? 
Q3) In the query phase, the algorithm only uses \hat{dist}. The proposed dist' is only for theoretical interest. Is this correct?  
Q4) Could you report a sensitivity analysis for the λ parameter?

### Soundness
2

### Presentation
2

### Contribution
2
