# Diverse Graph-based Nearest Neighbor Search

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Nearest neighbor search is a fundamental data structure problem with many applications in machine learning, computer vision, recommendation systems and other fields. Although the main objective of the data structure is to quickly report data points that are closest to a given query, it has long been noted (Carbonell et al, 1998) that without additional constraints the reported answers can be redundant and/or duplicative. This issue is typically addressed in two stages: in the first stage, the algorithm retrieves a (large) number of points closest to the query, while in the second stage, the points are post-processed and a small subset is selected to maximize the desired diversity objective. Although popular, this method suffers from a fundamental efficiency bottleneck, as the set of points retrieved in the first stage often needs to be much larger than the final output. 

In this paper we present provably efficient algorithms for approximate nearest neighbor search with diversity constraints that bypass this two stage process. Our algorithms are based on popular graph-based methods, which allows us to ``piggy-back'' on the existing efficient implementations.  These are the first graph-based algorithms for nearest neighbor search with diversity constraints.   For data sets with low intrinsic dimension, our data structures report a diverse set of $k$ points approximately closest to the query, in time that only depends on $k$ and $\log \Delta$, where $\Delta$ is the ratio of the diameter to the closest pair distance in the data set. This bound is qualitatively similar to the best known bounds for standard (non-diverse) graph-based algorithms. Our experiments show that the search time of our algorithms is substantially lower than that using the standard two-stage approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the topic of diverse approximate nearest neighbor (ANN) search and focuses on solving this problem via graph-based approaches as opposed to locality-sensitive hashing (LSH). LSH has been better studied in this context of finding diverse points in previous work, which lead to positive results, showing that diversity can be guaranteed at the same time when choosing points from hashed data structures. This paper takes a pioneering step towards finding the first algorithms for graph-based ANN search, which has become popular tools in the last decade or so but has not been considered from this perspective.

The paper studies this problem from both "primal" and "dual" formulations: one is to find a given $k$ diverse points optimizing closeness satisfying diversity constraint; the other to find most diverse points satisfying closeness constraints (within a ball of some radius $R$). The paper focuses on the primal but also showed similar results for the dual. The problem formulation allows approximation for full diversity: any point is allowed to have up to $k'$ points judged to be close to it. The main algorithm is relatively straight-forward. It starts with a preprocessing algorithm, which basically picks $k/k'$ points, that are far away from each other, each with its own set of close neighbors. This relationship is represented with a (sparse) graph. The algorithm then takes an initialization step that finds $k$ points that satisfies a much weaker diversity constraint, and finally compares the initialized set to the sparse graph and refine them to satisfy the $(k', C/\alpha)$-diverse constraint. In experiment section, the paper compares the new algorithm to the state-of-the-art graph-based ANN implementation and showed promising improvements.

### Strengths
The problem studied in this paper is both interesting and important in practice. The authors have motivated this very well. Also, adding diversity guarantees to graph-based approaches is a crucial step in bridging the gap between the two mainstream methods and might make graph-based approaches more applicable, since it can be used for more general metrics compared to LSH. 

It is nice observation that the greedy algorithm in Gonzalez (1985), combined with an initialization, can lead to desirable results in diversity guarantees. The algorithm should also be easy to implement and likely could be used by practitioners. 

At least in the described experiment setting, the algorithm beats its major baseline algorithm, which makes it more promising.

### Weaknesses
The writing appears messy in many places. It can benefit from some proofreading. For instance, some notions such as OPT, OPT_k appeared without being defined in advance. The lemmas and propositions in Section 3 are ordered and referred to in weird order, and the flow of logic in that section is not very smooth. 

I haven't checked all the details, but the techniques used do not seem to be deep. In some places it feels that more sophisticated approaches might lead to better results. For example, I'm slightly disappointed that allowing a factor of $k'$ fuzziness in the diversity constraint only serves to reduce the running time linearly in $k'$. It makes sense to me judging from the way the algorithm works. However, in traditional ANN approaches, allowing approximation in distance can help us improve tremendously compared to exact nearest neighbor.  I'm not sure if similar improvements could be possible here.

The experiment design is more or less limited. The authors only uses the binary distance metric. I think it would be better to test it with other common graph-based metric that is not Euclidean. I'm also curious about how fast the running time scales with high dimensions in practice.

### Questions
Do the authors have any thoughts on how it would compare to LSH-based approaches, say, in Euclidean space using $\ell_2$ distance? It is unclear to me since this algorithm has exponential dependency on $d$.

I'm not sure if the $k'$-colorful design for distance metric is commonly used as a benchmark for this line of work, in some places it seems strange to me that if the distance is binary, the approximation in distance just disappears? In this case when $k'=1$ does it just become the nearest neighbor problem? If so, how does the running time of the algorithm given in this paper compare to the best you can do in that scenario?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies approximate nearest neighbor search with diversity constraints, where instead of just minimizing the dissimilarity from the query to a set of $k$ output vectors, we also want to maximize the pairwise dissimilarity $\rho$ between the output vectors. The paper presents provably efficient graph-based algorithms for both the standard setting and the radius search setting where the results lie approximately within a pre-defined radius $R$.

Inspired by their theoretical algorithms, for practical applications, the authors propose heuristic approximations for an algorithm in the special case where each point is associated with a "color" and no more than $k'$ results can have the same color. In the experiments, this method is superior to the baseline method (querying $rk$ nearest neighbors for some $r$ and then applying post-processing) for datasets with a very skewed color distribution.

### Strengths
- The theoretical results are to the best of my knowledge the first for graph-based methods for the diverse nearest neighbor problem and the obtained bounds are meaningful. The analyzed algorithms are graph-based methods that are currently viewed as state-of-the-art for approximate nearest neighbor search.
- The authors also propose a practical heuristic method based on DiskANN for the diverse nearest neighbor problem. The proposed method achieves a significant improvement over vanilla DiskANN on the real-world dataset used by the authors.
- The paper is well-written and the presented arguments are easy to follow.

### Weaknesses
Instead of studying the performance of a practical diverse nearest neighbor search algorithm, the authors design a provably efficient theoretical algorithm. The analysis is quite similar in parts to the earlier work of Indyk & Xu (2023) in studying graph-based ANN methods. While the diverse nearest neighbors problem is relevant in many use cases, I am not convinced that the theory here is particularly insightful enough to cover for the slightly lesser importance of the problem (given the relative lack of empirical work for the problem).

The authors mention that their heuristic algorithm is "based on the provable algorithms provided in the main paper". However, I do not see how the proposed heuristics in Algorithms 5-7 are based on the theoretical version presented in Algorithms 1 and 2. It would be helpful for the authors to explicitly clarify this connection. Instead, the proposed empirical algorithm seems to be a relatively straightforward modification of the DiskANN algorithm with diversity constraints included in the search and prune procedures. Moreover, the proposed heuristic algorithm is only applicable to the "colorful" special case, while the standard post-processing approach is of course applicable to any case.

Two of the three datasets used in the experiments use semi-synthetic data where the color distributions are perhaps unrealistically skewed, causing $r$ to be much higher for the baseline than it would typically need to be. For example, for the SIFT dataset the authors sample a dominant color with probability 0.8 and the the rest of the 999 uniformly (in this case, I would just build two indexes). Moreover, you would expect there to be some correlation between the distances and the colors of given points.

### Questions
- [Q1] Referring (line 146) to the difference between the main bound in the paper (Theorem 1.1) and the bound presented by Indyk & Xu (2023), you say that the latter does not depend on $k$ or $k'$ as these parameters do not exist in the standard NN formulation. Of course, $k$ exists in the standard $k$-NN formulation -- how do the bounds you refer to look for $k$-NN (at a glance, the paper by Indyk & Xu seems to state a bound for 1-NN)? Do they also have a $k^3$ term for the time complexity of each step?
- [Q2] Your results depend on the aspect ratio $\Delta$ which can grow arbitrarily high when the minimum distance between any two points gets closer to zero. However, with graph methods points that are very near each other should be easier for the algorithm. Is there an intuitive explanation for this discrepancy?
- [Q3] Roughly how much does the indexing time of your practical diverse indexing method differ from that of DiskANN?
- [Q4] What value of $r$ do you use for the baseline method in the experiments and is it the same for each dataset? How high does $r$ need to be with respect to $k$ to achieve a high recall on the different datasets?
- [Q5] Could you verify that the latencies you provide in Figures 2 and 3 are correct? They seem quite high given the experimental setup if you use 48 threads per run (e.g., I would expect the queries to take << 1 ms on SIFT).
- [Q6] Is 20 the total number of sellers in the real-world data set or are there more? Would it be possible to publish the data set?
- [Q7] On the semi-synthetic data sets, I would also expect vanilla DiskANN to perform relatively much worse when $k'$ = 1 compared to when $k'$ = 10. Can you hypothesize why that is not the case?
- [Q8] What is the rationale for choosing the distributions for the semi-synthetic datasets?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies the diversity-aware ANNS given a query q, a data set P, a distance measure D(), a diversity measure \rho().
Diversity-ANNS asks to report an approximate kNN S, |S| = k, that contains points closest to q given D(), and maximizes the diversity measurement \rho() which is the minimum value of \rho(p, p') for any pair p, p' \in S. 

The work proposes two different variants of diversity-aware ANNS, including 
(1) Primal version: Given a fixed diversity threshold C, guarantee to find a set (C/a)-diversity S where the kNN_dist(q, S) \leq kNN_dist(q, S*), where S* is the optimal solution.
There are two approximation factors here, including $a$ for diversity measure \rho(), and $c$ for distance measure D().
(2) Dual version: Given a fixed radius R, guarantee to find a set (C/a)-diversity S where kNN_dist(q, S) \leq cR and C is the maximum value among all subsets of size k of the ball B(q, R).

Indeed, there is an additional parameter k' that governs the maximum number of points in the returned kNN set S that violates the diversity constraint for each point in S.
The dual version has been studied with LSH-based solution (Abbar et al. 2013b) and the primal version is resolved in this work using graph-based index.

The main contribution is that the proposed solution for the primal version avoiding the approximation factor c is derived from from the graph-based index (Indyk & Xu 23, DiskANN). 
In the DiskANN indexing phase, the work adds one step on top of the graph-based index with diversity-aware algorithm (via the Gonzalets greedy algorithm that maximizes the minimum pairwise \rho() distance) to prune candidates in the list L (Line 12 - Alg 1).
In the querying phase, there is an initialization step that picks the diversity-aware seeds (Line 3 - Alg 2) together their neighbors as candidate points. The greedy search over the graph index iteratively keeps finding the kNN set S of the query q and diversifying S given \rho().

The main theoretical results (stated in Theorem 1.1) show how to guaratee the answer for the primal version with  a constant a, c = (\alpha + 1) \ (\alpha - 1) where \alpha is the parameter of the DiskANN index.
The query time complexity is independent on n and exponentially dependent on the doubling dimension d.
The indexing space complexity is linear in n and exponential in d.
Both graph-based querying time and indexing space are better than LSH-based approaches, in terms of the dependency on n.
Some empirical results on real-world data sets demonstrate the efficiency of the proposed indexing and querying solutions compared to standard graph-based index baselines (DiskANN + postprocess, DiskANN + diverse query) given the recall-latency tradeoff.

### Strengths
S1. The diversity-award ANNS is important in many recommendation applications, and the paper is the first work with graph-based index solution (to the best of my knowledge)

S2. The solutions comes with theoretical backing on the approximation factors in terms of diversity and distance measures.

S3. The graph-based indexes are versatile for several distance measures, so the proposed solution can piggy-back on industry released graph-based libraries on many distance measure D().

### Weaknesses
W1. I found the initialization step (Line 3 - Alg2) in the query phase will be the bottleneck since it might execute O(n) range queries given the \rho distance in the worst case. This step will dominate the query phase. However, there is no discussion on the complexity of this step. Since the initialization step requires C as input, so different values of C require to run the initialization step again, which is more troublesome.

W2. Though graph-based indexes show advantages compared to hash-based solutions on standard ANNS, it is not well-understood that graph-based solutions will be better than hash-based solutions on diversity-awared ANNS, especially given additional steps on querying phase over the graph-based indexes. The experiments do not contain hash-based baselines, which does not convince the advantage of the proposed solution given the diversity constraints.

W3. While the proposed theory (Theorem 1.1) works on a general \rho, the empirical results consider the specific \rho ('colorful' version), which clearly not align well to the theory. As stated in Line 152, there is no role of \rho in the practical implementation, which really weakens the contribution of theory.

W4. The emprical setting is not clearly described. For example, since standard greedy search on graph will be much faster than diverse search, one can set r much larger than k to expect get better recall with post-processing. Also, since we consider k = 100, I wonder why we only set L = 200 since this value seems to be the default settting of graph-based index for k = 10.

W5. The paper is very difficult to follow. Section 3 describes the indexing and quering algorithms without any intuitions to show why the author proposed modifications from DiskANN. While the paper builds on graph-based indexes, it is difficult the see the key differences in the manuscript, and it is hard to see the novelty in both indexing and querying phases. There are nearly 3 pages dedicating for the proof. It might be better to move the proof to the appendix to have room to explain the algorithms in high levels.

Minor things.

Line 125: OPT_k has not defined before. Is it the optimal kNN distance among all possible answered set for the value C?

Line 248: Lemma 3.1 ?

### Questions
Please address the weaknesses W1 - W4, and the following questions.

Q1. Could you provide a complexity analysis of the initialization step and discuss how it impacts the overall query time. How does your algorithm's performance change for different values of C, given that the initialization needs to be rerun?

Q2. Could you add hash-based solutions baselines for diversity-aware ANNS? This would provide a more comprehensive evaluation of the proposed method's advantages.

Q3. What is the value of r, and the fraction of running time of the post-processing step in the query time?

Q4. How sensitive are the emprical results when k = {10, 20} with L = 200, or k = 50, L = 500?

### Soundness
2

### Presentation
1

### Contribution
3
