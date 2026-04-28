# A Bi-metric Framework for Efficient Nearest Neighbor Search

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 3

## Abstract
We propose a new bi-metric framework for designing nearest neighbor data structures. Our framework assumes two dissimilarity functions: a ground-truth metric that is accurate but expensive to compute, and a proxy metric that is cheaper but less accurate. In both theory and practice, we show how to construct data structures using only the proxy metric such that the query procedure achieves the accuracy of the expensive metric, while only using a limited number of calls to both metrics.  Our theoretical results instantiate this framework for two popular nearest neighbor search algorithms: DiskANN and Cover Tree. In both cases we show that, as long as the proxy metric used to construct the data structure approximates the ground-truth metric up to a bounded factor, our data structure achieves arbitrarily good approximation guarantees with respect to the ground-truth metric. On the empirical side, we apply the framework to the text retrieval problem with two dissimilarity functions evaluated by ML models with vastly different computational costs. We observe that for almost all data sets in the MTEB benchmark, our approach achieves a considerably better accuracy-efficiency tradeoff than the alternatives, such as re-ranking.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a bi-metric framework for nearest neighbor search. It well abstracts a widely used technique for nearest neighbor search, but with several assumptions. The experimental results demonstrate its effectiveness.

### Strengths
S1. This paper studies an important problem. 

S2. The method proposed seems sound. 

S3. The experimental results are good to support the effectiveness.

### Weaknesses
W1. The main contribution (Tm 3.4) is built on top of existing works, which makes the novelty insufficient. 

W2. The method is applicable to the case where two embedding models are generated for the same data source. However, there still exist another case where a simple embedding model is generated for another expensive embedding for the sake of nearest neighbor search. For example, product quantization for high-dimensional vectors in DiskANN. 

W3. The method assumes that d(x, y) ≤ D(x, y) ≤ C · d(x, y), which may not be practical.

### Questions
Q1. Could it be possible to extend the results on PQ vs high-dimensional vectors ?

### Soundness
3

### Presentation
3

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
This paper aims to build a nearest neighbors index over a cheap-to-compute metric $d$, which approximates nearest neighbor search over an expensive, but more accurate, metric $D$. In practice, this means the paper aims to make retrieval over embeddings produced by a small, cheap model emulate retrieval over embeddings produced by a much more expensive model.

The paper proposes using the cheap $d$ to create the index, and then starting each query's search with $d$ before transitioning to using $D$ in distance computations (albeit still leveraging the same index and graph connectivity, which was created on $d$).

### Strengths
Extensive suite of datasets and models are benchmarked.
Theory on using a graph built on one metric to navigate a related metric is novel.

### Weaknesses
1. Contrived and unrealistic setup: critical to the paper's thesis is the belief that the embedding for $x\in X$ is computed every time the ANN algorithm accesses $x$. It therefore implies that using a cheaper embedding model makes queries cheaper, because these embeddings are re-computed for every query. This is unrealistic because in practice, retrieval systems generally embed all $x\in X$ offline during the indexing phase, so model size has no impact on query latency or throughput. Embedding the entire dataset offline is far more practical because it makes embedding a fixed cost, rather than one linear in the number of queries. For example, if each query involved 1000 embedding calls, then just 1000 queries would lead to the same embedding cost as embedding 1M elements offline. Furthermore, offline indexing can often achieve >10x throughput gains from batching, which makes the computation much more amenable to ML accelerator hardware. This tilts the decision even further in favor of embedding during indexing.
2. Main result from Theorem 3.4 result has a poorly described connection to your proposed metric in the experiments, and the choice of $Q/2$ seems quite arbitrary and isn't explored until the end of the paper (but this isn't described in Section 4.1).
3. Figures are poorly described: "Single metric (limit)" is not described anywhere. I'm assuming the x-axis is $Q$, but $Q$ isn't in the x-axis label despite being extensively referenced in the body text, and I have to infer.
4. Poorly structured: for example, Algorithm 1 is mentioned casually several times in Section 3, but only appears in the appendix, with no indication it could be found there. Theorem 3.4 is the main theorem in the section but is not formatted to emphasize its importance.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a general bi-metric framework for efficient nearest neighbor search by combining an expensive, accurate ground-truth metric $D$ and a cheap, approximate proxy metric $d$. The framework constructs data structures based on the proxy metric $d$ for efficiency, while using limited calls to metric $D$ in query and retaining the accuracy of the ground-truth metric $D$. The authors demonstrate this framework with DiskANN and Cover Tree algorithms and apply it to text retrieval tasks, indicating improvements in the accuracy-efficiency trade-off compared to existing re-ranking or bi-metric methods.

### Strengths
1. Theoretical guarantees of the approximation quality (accuracy) are provided.

2. Although methods that combine a cheap metric $d$ with an expensive metric $D$ already exist, the proposed method addresses the limitations of existing methods: (1) The proposed method achieves the accuracy of the expensive metric $D$; (2) The proposed method requires only a sub-linear number of evaluations of $d$ and $D$ during the query stage. These two points represent significant improvements in the nearest neighbor search problem.

3. Extensive experiments across 15 MTEB retrieval datasets were conducted and showed consistent performance gains.

### Weaknesses
 1. The proposed framework is applicable only to algorithms that use the concept of an $r$-net (where, given a parameter $r$, an $r$-net is a small subset of the dataset that ensures every data point is within distance $r$ to the subset in the net).
For nearest neighbor algorithms that do not rely on $r$-net, the proposed framework is likely inapplicable.

2. The proposed framework lacks a clear explanation, making it difficult to assess the novelty of the algorithm.
The paper does not provide pseudocode in the main text or use toy examples to help readers understand the algorithm.
The proposed algorithm is only partially described in Section 4, while Section 3 mainly focuses on theoretical analysis, leaving readers somewhat lost, as they do not fully grasp the proposed method at this point.

3. The experiment results show only the number of calls to metric $D$, while the number of calls to metric $d$ is not shown.
Since a key claimed improvement over existing bi-metric methods is the reduction (or even sub-linear scaling) in calls to metric $d$, it would be valuable to report the number of calls to $d$ as well.

4. It would be valuable to evaluate across datasets with varying intrinsic dimensionalities.
Since the bi-metric framework depends on the proxy metric $d$ closely approximating the ground-truth metric $D$, datasets with higher intrinsic dimensionality may introduce greater approximation error, making it more challenging to achieve accurate results.
Additionally, higher intrinsic dimensionality could increase query complexity and reduce the efficacy of the $r$-net structure used in the method, potentially impacting both accuracy and efficiency.
Testing the framework across datasets with different intrinsic dimensionalities would clarify its robustness and scalability under diverse data conditions.

5. In several places, such as line 98 (Equation 1) and line 279 (Algorithm 1), the main text references equations or algorithms that appear much later or only in the appendix.
This disrupts the continuity and can cause confusion for readers.
It would be helpful if the authors could either move these elements earlier in the text or provide clearer guidance to improve readability and flow.

### Questions
1. Could you please discuss how your proposed framework applied to other commonly used data structures like Locality-Sensitive Hashing, Proximity Graph, K-d Tree, and Product Quantization? (W1)

2. Could you consider reorganizing the content (including pseudocode in the main text) to improve clarity and provide a more cohesive flow? (W2)

3. Moreover, could you provide a step-by-step explanation of the proposed algorithm, possibly with a toy example, to enhance clarity and help readers fully understand the method before delving into the theoretical analysis? (W2)

4. The paper states that only a sub-linear number of evaluations of both $d$ and $D$ are required during querying. However, it seems that the sub-linear evaluations of $d$ are neither illustrated nor proven, and this is not immediately clear. How does the proposed algorithm achieve a sub-linear number of distance computations? (W3)

5. How does the proposed framework handle datasets with different intrinsic dimensionalities, particularly regarding the accuracy of the proxy metric and the effectiveness of the $r$-net structure under these conditions? (W4)

6. Could the authors consider restructuring the placement of key equations and algorithms, or provide additional guidance to improve readability and continuity throughout the paper? (W5)

### Soundness
2

### Presentation
2

### Contribution
3
