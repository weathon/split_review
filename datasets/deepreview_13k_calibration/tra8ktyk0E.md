# Dynamic Similarity Graph Construction with Kernel Density Estimation

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 6, 5, 3

## Abstract
In the kernel density estimation (KDE) problem, we are given a set  $X$ of data points in $\mathbb{R}^d$, a kernel function $k: \mathbb{R}^d \times \mathbb{R}^d \rightarrow \mathbb{R}$, and a query point $\mathbf{q} \in \mathbb{R}^d$, and the objective is to quickly output an estimate of $\sum_{\mathbf{x} \in X} k(\mathbf{q}, \mathbf{x})$.
In this paper, we consider $\textsf{KDE}$ in the dynamic setting, and introduce a data structure that efficiently maintains the estimates for a set of query points as data points are added to $X$ over time.
Based on this, we design a dynamic data structure that maintains a sparse approximation of the fully connected similarity graph on 
$X$, and develop a fast dynamic spectral clustering algorithm.
We further evaluate the effectiveness of our algorithms on both synthetic and real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper develops a technique to maintain the kernel density estimates arising from a set of data points X at a set of query points Q, as updates occur dynamically to X and Q. Using this, they design a dynamic data structure that can maintain a sparse approximation to the "kernel weighted" similarity graph for a set of points X (as X changes). 

The main idea is to adapt the approach of Charikar, Kapralov, Nouri, and Siminelakis (CKNS) to handle dynamic updates to both the X and the Q. For the application to approximating similarity graphs, the paper builds off the recent work of Macgregor & Sun (2023).

### Strengths
- Kernel density estimation is a ubiquitous problem in data analysis, and dynamic models are also interesting to study. The update guarantees that the paper obtains are quite strong.

- In spite of being based on prior work, there is sufficient technical novelty in the algorithms.

- The application to dynamic similarity matrix estimation is also interesting.

### Weaknesses
No significant weaknesses; please see the questions below.

- The paper cites the work of Macgregor and Sun 2023 for dynamic similarity matrices (and the algorithm is based on that work), but I didn't notice experimental comparison to that work. I may have missed it, but if the authors can provide a clear comparison (both experimentally and theoretically), it would make the paper stronger.

- About the n^{1/4} time required for the KDE step for Gaussian kernels (which is what leads to the final update time), are there any lower bounds suggesting that the time cannot be improved?

### Questions
- The paper cites the work of Macgregor and Sun 2023 for dynamic similarity matrices (and the algorithm is based on that work), but I didn't notice experimental comparison to that work. I may have missed it, but if the authors can provide a clear comparison (both experimentally and theoretically), it would make the paper stronger.

- About the n^{1/4} time required for the KDE step for Gaussian kernels (which is what leads to the final update time), are there any lower bounds suggesting that the time cannot be improved?

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
Overview: The paper presents efficient dynamic data structures for two kernel problems over a dynamic set of points X and a kernel function k(.,.):
-	Kernel density estimation (KDE) problem, where the goal is to maintain a set of points X and a set of queries Q so that for each q in Q the data structure holds an estimate of the sum_{x in X} k(x,q), and
-	Kernel sparsification, where the goal is to maintain X and a sparse weighted graph G with vertices in X such that clustering the graph G produces approximately the same result as clustering the fully connected graph with edge weights induced by k(.,.).

Techniques:  Both data structures use recently developed algorithms for the *static* KDE problem. The KDE data structure is obtained by “dynamizing” the algorithm of Charikar et al, 2020, while the kernel sparsification data structure follows the algorithm of Macgregor and Sun, 2023. 

The authors complement the theoretical development with empirical evaluation of their algorithms. For KDE, the proposed algorithm is compared on a few benchmark data sets, to the following baselines:

 (a) EXACT: an algorithm that recomputes the kernel values after every update to X using the naive (quadratic-time) algorithm.

 (b) DYNAMICRS: an algorithm that (I am guessing) solves the static problem exactly on a random sample containing 10% of the points, after every update.

(c) CKNS: an algorithm that recomputes the estimates after every update using the static algorithm of Charikar et al 2020.

For each data set and each algorithm, the authors report running times and estimation errors.

### Strengths
S1: Both problems have been studied extensively, and they have many applications in machine learning. The dynamic variants of those problems have been studied less, but they are well-motivated and important as well.

S2: see below.

### Weaknesses
W1: The experimental design is a good starting point, but it makes it impossible to answer the following important question: for a given data set and a given error bound, which algorithm is the fastest? For example, for the GLOVE data set, the proposed algorithm is twice as fast as DYNAMICRS, but it also has a much higher error, so it is plausible that DYNAMICRS with a smaller sampling rate would be faster *and* have smaller error. Overall, the experimental section demonstrates that the proposed algorithm is implementable, but it is unclear whether it improves empirically over the state of the art. The comparison to DYNAMICRS is particularly problematic because the sampling rate is fixed at 10%, which may not be optimal for all datasets or error tolerances. A more thorough comparison would involve varying the sampling rate of DYNAMICRS and plotting the trade-off between runtime and error, allowing for a fair comparison against the proposed method across different operating points. Furthermore, the error metric used should be clearly defined, and it should be made clear if it is an absolute or relative error. The current presentation makes it hard to assess the practical significance of the observed differences in error.

W2/S2: Converting static algorithms into dynamic data structures does not seem to require significantly new ideas, but it is not trivial either.

### Questions
What are the main new algorithmic ideas needed to dynamize the static algorithms of Charikar et al and Macgregor-Sun ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies the problem of approximately maintaining a dynamic similarity graph using kernel density estimation. A similarity graph over a set of points in $R^d$ weighs the edge between every pair of points $x,y$ by a similarity measure like the gaussian kernel $\exp(-|x-y|^2)$. Since the full graph is costly to compute and store, there is work on sparse approximations with approximate edge weights. Recently this line of work has focused on utilizing progress on hashing-based estimators for KDE. 

This paper continues this line of work by allowing the similarity graph to be maintained dynamically under insertion and deletion of points.

### Strengths
Efficient construction of similarity graphs is an important problem, and the empirical results are favorable.

### Weaknesses
The paper seems technically somewhat incremental, in that there is not a lot of novelty needed in order to adapt existing work on the problem to the dynamic setting. The hashing-based estimators for KDE are naturally dynamically maintainable (just a point can simply be added or removed from its bucket in the hash table) and the paper basically builds this property into the Macgregor-Sun construction. Furthermore, the experimental evaluation does not provide a direct comparison between the proposed method and existing approaches. Specifically, the trade-off between running time and accuracy is not clearly explored or controlled. In the presented results, the DynamicRS algorithm often achieves significantly lower error than the proposed method, albeit with a higher running time. However, it is unclear how the parameters of each algorithm were chosen to achieve this trade-off, and whether a different parameter selection could lead to a different conclusion. The lack of a clear methodology for parameter selection makes it difficult to assess the practical viability of the proposed method compared to existing alternatives. The paper also does not address the challenge of hyperparameter selection, which is a significant practical concern for the proposed method.

### Questions
N/A

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
This paper studies the kernel density estimation problem, in which we are given a set $X$ of data points in $\mathbb{R}^d$, a kernel function $k : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$, and a query point $q \in \mathbb{R}^d$, and the objective is to quickly output an estimate of $\sum_{x \in X} k(q, x)$. In particular, they consider the dynamic setting, where both points in the dataset $X$ and the queries in the query set $Q$ can change over time and the goal is to maintain $(1+\varepsilon)$-multiplicative approximations to the queries. 

The paper gives a data structure for approximation of KDE queries that uses $\varepsilon^{-2} \cdot n^{1+o(1)} \cdot \text{cost}(k)$ initialization time and dynamic data point updates with time $\varepsilon^{-2} \cdot n^{o(1)} \cdot \text{cost}(k)$ per update. The paper also gives a data structure for sparse similarity graph approximation that uses $n^{1+o(1)} \cdot \text{cost}(k)$ time to initialize, as well  $n^{o(1)} \cdot \text{cost}(k)$ expected amortised update time. For both settings, $\text{cost}(k)$ is a function of the kernel function that measures how far points can be while still only contributing a certain amount to the KDE query.

### Strengths
+ KDE estimation is a well-motivated problem that would be of interest to multiple areas of the ML community
+ The dynamic setting is a specific direction that has recently received attention
+ The main statements of the paper are prove with mathematically rigorous claims
+ The experiments are comprehensive and shows good performance in practice

### Weaknesses
 - Similar qualitative results for both the initialisation time and the update time were achieved by Liang et. al. (2024). It seems the techniques are reasonably similar too, looking to sample points in various distance levels around the queries. Although this paper cites the Liang et. al. paper and although it is true the latter paper does not handle dynamic updates of the query set, this paper fails to mention that the qualitative results of the Liang et. al. paper are similar to this paper, and it fails to compare the techniques between the papers.

Jiehao Liang, Zhao Song, Zhaozhuo Xu, Danyang Zhuo: Dynamic Maintenance of Kernel Density Estimation Data Structure: From Practice to Theory. CoRR abs/2208.03915 (2024)

- Though the claim is that the update time is sublinear, the cost function depends on the value of the smallest query. For many reasonable kernels such as the Gaussian kernel, these queries have very small value, in which case the resulting update time is not small. On the other hand, for queries with large value, sampling is a standard KDE technique. Given these points, it is not clear what are the technical novelties of this paper. Furthermore, the paper does not adequately address the practical implications of this dependence on the smallest query value, especially given that many kernels can produce extremely small values for distant points, potentially negating the sublinear update time in practice. The paper also does not discuss how the choice of kernel affects the practical performance of their method, which is a significant omission given the dependence on the smallest query value.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2
