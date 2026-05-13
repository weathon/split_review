# On the Price of Differential Privacy for Hierarchical Clustering

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Hierarchical clustering is a fundamental unsupervised machine learning task with the aim of organizing data into a hierarchy of clusters. Many applications of hierarchical clustering involve sensitive user information, therefore motivating recent studies on differentially private hierarchical clustering under the rigorous framework of Dasgupta's objective. However, it has been shown that any privacy-preserving algorithm under edge-level differential privacy necessarily suffers a large error. To capture practical applications of this problem, we focus on the weight privacy model, where each edge of the input graph is at least unit weight. We present a novel algorithm in the weight privacy model that shows significantly better approximation than known impossibility results in the edge-level DP setting. In particular, our algorithm achieves $O(\log^{1.5}n/\varepsilon)$ multiplicative error for $\varepsilon$-DP and runs in polynomial time, where $n$ is the size of the input graph, and the cost is never worse than the optimal additive error in existing work. We complement our algorithm by showing if the unit-weight constraint does not apply, the lower bound for weight-level DP hierarchical clustering is essentially the same as the edge-level DP, i.e. $\Omega(n^2/\varepsilon)$ additive error. As a result, we also obtain a new lower bound of $\tilde{\Omega}(1/\varepsilon)$ additive error for balanced sparsest cuts in the weight-level DP model, which may be of independent interest. Finally, we evaluate our algorithm on synthetic and real-world datasets. Our experimental results show that our algorithm performs well in terms of extra cost and has good scalability to large graphs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes several results furthering hierarchical clustering with differential privacy. The notion of privacy is weighted differential privacy, where the graph topology is public, and the weights of the edges are private. First, an efficient algorithm obtaining a \frac{n}{\epsilon} \log n approximation ratio for graphs in which the minimum edge weight is at least 1 is proposed. The authors show that in the worst case, the \omega(n^2 / \epsilon) additive error lower bound from previous work still holds for the weaker notion of weighted DP. They make the interesting observation that the lower bound carries over to DP balanced cut via a reduction. Finally, they run experiments showing that the proposed mechanism is indeed feasible.

### Strengths
The proposed algorithm is simpler and much more efficient than that in prior work. The multiplicative error is not too high for the graphs with edge weight at least 1, which is also a nice result and improvement over prior work. The reduction to balanced cut is an interesting new result.

### Weaknesses
The lower bound in a way misses the spirit of the proposed algorithm: It shows that there are adversarial graphs (with edge weights possibly zero) which require additive \Omega(n^2 / \epsilon) noise, but the upper bound applies to graphs whose edge weights are all at least 1. As these types of graphs are central to obtaining the upper bound, it would be more interesting to see what the lower bound is for graphs which also satisfy this property.

The utility of the proposed algorithm for graphs whose edge weights are close to zero is currently undefined, meaning the algorithm is not robust for graphs which fall even a little outside the constraints. This can be reconciled somewhat by combining this algorithm with previous work, but then the efficiency improvements do not hold. Furthermore, the analysis does not consider the case where a small number of edges have weights close to zero, which is a realistic scenario in many applications. The current utility guarantee only applies when *all* edge weights are at least 1, which is a strong and somewhat unrealistic assumption.

The experiments look interesting, though there is an unexplained phenomenon that the proposed algorithm barely shows any sensitivity to epsilon: it achieves nearly the same error on both the minimum \epsilon = 0.1 and maximum \epsilon = 2.0 tested. This is surprising, since typically epsilon dramatically affects the performance of any private algorithm, and typically as \epsilon becomes large, the cost should approach the cost of the best tree. Neither of these things is happening in the current plots; I think they should be double-checked.

### Questions
Can you develop a lower bound family of graphs on a fixed topology which all have edge weights above 1, and incur at least the stated multiplicative error?

Is it possible to obtain a stand-alone utility theorem for the proposed algorithm, which interpolates between \log n / \epsilon multiplicative error and n^2 / \epsilon additive error for graphs with edge weights at least 1 vs. arbitrary graphs? You might have to "unpackage" Proposition A.6 so that it can handle additive error.

For the experiments, what is the smallest value of epsilon for which the utility of the proposed algorithm becomes "bad"? What is the value of epsilon such that the utility approaches the optimal cost? Consider increasing the range of epsilons used in the plots.

### Soundness
3

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
This paper studies the challenge of achieving differential privacy in hierarchical clustering, under a model that assumes edge weights as sensitive information. The authors successfully show there exists an algorithm in this setting that achieves $O(\log^{1.5} n/\epsilon)$
multiplicative approximation.

### Strengths
1. Despite the complicated problem setting and technical components, this paper has a clear presentation.
2. In addition to establishing an upper bound, the authors also derive a matching lower bound that aligns with previous work, which presents an additive error of $\Omega(n^2/ \epsilon)$ and  a new lower bound of $\Omega(1/ \log ^{2}n \epsilon)$  for balanced sparsest cuts in the weight-level DP model. These findings offer valuable insights into the comparison between edge-level and weight-level differential privacy models.  The lower bound proofing technique is novel.

### Weaknesses
Currently, I do not see the reason why in the input graph G adding an extra additive weight of $ 10 \log \frac{n}{\epsilon} $ would be necessary, can the authors give some comments on this?

### Questions
Please see above.

### Soundness
2

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the challenge of performing hierarchical clustering (HC) on a graph while ensuring differential privacy (DP). Traditional approaches to differentially private clustering on graphs, particularly under edge-level DP, have recently been shown to incur high errors, which limits their practicality. To improve upon this, the paper proposes an alternative approach using weight-level DP, where only the edge weights (not the topology) represent sensitive information.

While weight-level DP is less commonly studied than edge-level DP, it is not entirely novel. Previous works have defined neighboring graphs under weight-level DP by assuming identical topologies but allowing edge weight differences up to an $\ell_1$ norm of 1. In this study, the standard weight-DP definition is adapted by adding a unit-weight assumption, requiring all edges to have weights of at least 1. For clarity, this adapted model will be referred to as “weight-DP-bis”. This adjustment enables significantly more practical error bounds, which are leveraged in the main contributions.

First, the paper introduces a polynomial-time algorithm that achieves an approximation of $O(\log^{1.5} n / \epsilon) $ for hierarchical clustering under the $\epsilon$-weight-DP-bis model. The paper further justifies the unit-weight assumption in weight-DP-bis by demonstrating that without it, an HC algorithm that satisfies $\epsilon$-weight-level DP must incur an additive error of at least $\Omega(n^2 / \epsilon)$.

As an additional contribution, new lower bounds are established for balanced sparsest cuts under weight-level DP, which may have implications for broader applications beyond HC. 

Finally, empirical results support the algorithm’s effectiveness on both synthetic and real datasets, showing performance close to non-private benchmarks and scalability across a range of graph sizes.

### Strengths
The paper addresses a significant and complex topic that holds potential benefits for the community. The work is well written, well organized and, based on my level of reading, presents a sound approach to the problem. The core concept is clearly presented, and the technical contributions do not look trivial to me. Overall, the presentation and flow of ideas make the paper engaging and accessible (with a small criticism that I provide below), providing a very nice reading experience.

### Weaknesses
I have a few points that could be regarded as potential areas for improvement or clarification in the paper. Please note that these comments are based on my understanding of the material, and they reflect my personal perspective. I do not claim to be a specialist specifically in hierarchical clustering (HC). It is possible that I have misunderstood some aspects, and I am certainly open to revisiting my viewpoint during the discussion phase if necessary.

- **(Minor)**: First, while the paper is quite well written, it may benefit from being more accessible to a general audience. Specifically, it would be helpful to provide brief reminders of key graph-theoretical concepts earlier in the paper. Some concepts, such as sparsest cuts, are not introduced in the main body, while others, such as HC and Dasgupta’s cost, are defined only on page 5. Given that the introduction spans four pages, it may help readers unfamiliar with these concepts to have them presented earlier or concisely defined within the introduction itself to avoid missing key discussions in the first half of the paper. Additionally, the introduction could be shortened to accommodate these clarifications.

- **(Important)**: Second, while I understand that the unit-weight assumption offers better error bounds from a technical standpoint, it may fundamentally modify the problem. Specifically, assuming the $\ell_1$ norm of differences is less than 1 and simultaneously that each edge has a minimum weight of 1, means that two graphs are neighboring only if their weight functions differ on a single edge. As I see it, this implicitly combines aspects of both the $\ell_1$ and $\ell_0$ norms in the privacy definition. The paper may benefit from contextualizing this adapted definition with practical scenarios beyond the initial one presented in [1] (and paraphrased on line 77), as these may no longer directly apply. Additionally, there are existing variations in weight-level DP definitions that might be interesting to discuss in the paper, where the $\ell_1$ norm is that replaced with the $\ell_\infty$ norm. Relevant references include [2,3,4,5].

- **(Important)**: Third, it seems that the paper does not compare to a closely related problem: computing minimum spanning trees under weight-level DP. This problem has been studied under both $\ell_1$ and $\ell_\infty$ norms in [1,2,3]. I believe that this line of work is relevant to this paper because, as far as I understand, computing a weighted minimum spanning tree can be closely related to the single linkage HC algorithm. Existing studies on this problem provide upper and lower bounds that may be highly relevant here, even if the metric used (e.g., not explicitly Dasgupta's cost) differs. For instance, [1,3] provide matching upper and lower bounds of $\Theta(n^2 / \epsilon)$ for the additive error in minimum spanning tree computation under weight-level DP with $\ell_1$ norm, which seems related to Theorem 3 in this paper. It think it would be nice if the paper could discuss this connection and, if relevant, compare these results. Similarly [2] adapts the initial definition to use an $\ell_\infty$ norm and shows that, similar results hold in the $\ell_\infty$ model, but can be circumvented by forcing the $\ell_\infty$ norm to be smaller than $\frac{1}{\vert E \vert}$ in the privacy definition. This scheme seems similar to the idea of modifying the neighborhood definition to obtain better errors, but as pointed out in [3], this can be considered as being an alchemical fix.

- **(Medium)**: Finally, the experimental section could be strengthened by including more comparisons to existing methods or baselines. Currently, it appears that the only baseline comparison is with iterative sparsest cut after input perturbation. It might be beneficial to consider additional comparisons, such as those in Imola (2023), which compares against single and average linkage.

- **(Minor)**: A brief stylistic note: while this is a personal preference, I would suggest avoiding exclamation points in scientific writing, as seen in lines 160 and 200. A more neutral tone may be more fitting for a formal context.

### Questions
Please comment an the above weaknesses (especially important ones).

### Soundness
3

### Presentation
3

### Contribution
2
