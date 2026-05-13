# Learning-Augmented Streaming Algorithms for Correlation Clustering

- Decision: Reject
- Scores: 6, 6, 6, 6, 6

## Abstract
We study streaming algorithms for Correlation Clustering. Given a complete graph as an arbitrary-order stream of edges, with each edge labelled as positive or negative, the goal is to partition the vertices into disjoint clusters, such that the number of disagreements is minimized. In this paper, we introduce the first learning-augmented streaming algorithms for the problem, achieving the first better-than-$3$-approximation in dynamic streams. Our algorithms draw inspiration from recent works of Cambus et al. (SODA'24), and Chakrabarty and Makarychev (NeurIPS'23). Our algorithms use the predictions of pairwise dissimilarities between vertices provided by a predictor and achieve an approximation ratio that is close to $2.06$ under good prediction quality. Even if the prediction quality is poor, our algorithms cannot perform worse than the well known Pivot algorithm, which achieves a $3$-approximation. Our algorithms are much simpler than the recent $1.847$-approximation streaming algorithm by Cohen-Addad et al. (STOC'24) which appears to be challenging to implement and is restricted to insertion-only streams. Experimental results on synthetic and real-world datasets demonstrate the superiority of our proposed algorithms over their non-learning counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the correlation clustering problem, proposing a learning-augmented streaming algorithm for the problem. The proposed algorithm can achieve better-than 3-approximation in dynamic settings, and the structure of the proposed algorithm is simpler than previous algorithm. Experimental results are also presented in the paper to empirically testify the performance of the proposed algorithm.

### Strengths
S1. Correlation clustering is a fundamental and widely studied problem. The paper is well-motivated to study this problem and simplify previous algorithms. 

S2. The proposed algorithm can achieve better approximation results when the predictor works well. The empirical experiments also show the effectiveness of the proposed algorithm.

### Weaknesses
W1. I have concerns about the novelty and technical depth of the proposed algorithms. The core idea is largely based on existing approaches, and the main theoretical results are derived from previous work, which limits the paper’s novelty. Additionally, the theoretical improvement achieved by this work appears to be marginal; the proposed algorithm performs asymptotically better than previous results only when the predictor functions well. The reliance on a predictor for improved performance raises concerns about the practical applicability in scenarios where accurate predictions are not readily available or are computationally expensive to obtain. The paper does not adequately address the overhead associated with the predictor, such as training time and memory requirements, which could negate the benefits of the improved approximation ratio.

W2. The structure of the proposed algorithm is simpler than previous approaches, which is good. However, this simplification results in a loss of approximation quality (i.e., it does not achieve the 1.827-approximation), which weakens the paper’s contributions. While simplicity is a desirable trait, the trade-off with approximation quality needs more justification. The paper should provide a more detailed analysis of the specific scenarios where the proposed algorithm's simplicity outweighs the loss in approximation, and whether this trade-off is acceptable in practical settings. The lack of a rigorous comparison with the 1.827-approximation algorithm, particularly regarding the practical implications of the approximation gap, is a significant weakness.

W3. The paper’s presentation needs significant improvement. I recommend starting with a formal problem definition. Illustrative figures would also be helpful for explaining the correlation clustering problem to non-expert readers. The detailed review of related work in the Introduction could be moved to a separate Related Work section, leaving only a complexity comparison table in the Introduction to emphasize the technical improvements of this manuscript. Presenting high-level ideas first, followed by detailed technical proofs, would also improve readability.

### Questions
Could the authors further clarify the technical improvements of the proposed algorithms compared to the recent 1.847-approximation streaming algorithm by Cohen-Addad et al. (STOC ’24)?

### Soundness
3

### Presentation
2

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
The authors propose a learning augmented algorithm (LAG) for correlation clustering in the streaming setting. More specifically, the authors propose a min{(2.06\beta, 3)} + \eps algorithm for the problem. Further, they propose a sparsification scheme to approximate the clustering in the original graph to within (1 \pm \eps) to deal with memory constraints in the streaming setting.

### Strengths
The authors adapt two algorithms from prior work and extend it to the case where the algorithm has access to predictions on the pairwise dissimilarity between nodes in the graph.  They present a clean algorithm that clearly outperforms the best-known algorithm when the predictions are good.  This is an important use case of the LAG framework.  In fact, I am surprised that this was not studied earlier in the LAG framework.

The paper is well-written with corroborating empirical analysis that shows the efficiency of the proposed algorithms.

### Weaknesses
 The streaming setting and the use of graph sparsification is a bit weak, IMO.  By sparsification, I would think they have completely avoided the subtle issues that arise from the streaming setting (e.g., order of arrival of the edges, etc).


### Questions
How does one go back to the original clustering from the sparse clustering computed by the algorithm?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents new algorithms for correlation clustering in dynamic graph streams where both edge insertions and deletions are allowed. The algorithms leverage prediction models for the pairwise similarity between nodes. It is shown that under certain assumptions about the properties of the predictor, the algorithm can achieve better-than-3 approximation of the optimal correlation clustering cost. The main contribution is rigorous theoretical results for the approximation quality of the presented algorithms. Experimental results support the theoretical findings.

### Strengths
- The paper studies an important problem 
- An interesting paper exploring a promising direction, namely how to leverage prediction models for combinatorial hard optimization problems.
- Rigorous theoretical results.
- The algorithms are easy to implement yet the analysis uses advanced tools to derive the aforementioned theoretical results.

### Weaknesses
I have one main problem with the paper. Namely, the definition of a $\beta$-level predictor looks artificial and does not reflect some natural properties of the data. With this definition, the result essentially becomes something like "If we can predict similarities that could be used to obtain a good approximation of the optimal solution, then we can obtain a good approximation algorithm". Of course, I am oversimplifying but I think the authors should try to provide some connection between the formal definition and some intuitive properties of the data and the prediction algorithms. I realize this is challenging but even a special example would be helpful.

Furthermore, the pairwise similarities $d_{uv}$ should be thoroughly discussed and concrete examples of similarity functions should be presented. More specifically, the relation between the edge labels and $d_{uv}$ similarities should be discussed with concrete examples.

Some minor comments:
- The optimization objective is never formally defined.
- Algorithm 1 assumes that the number of nodes $n$ is known in advance. I guess this is not a real limitation but might add another logarithmic factor to the time and space complexity. Please comment on it.

### Questions
Comment on the above weaknesses. In particular, it would be great if you could provide some intuition with concrete examples about $d_{uv}$ and the optimal clustering.

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studied learning-augmented streaming correlation clustering. In this problem, a labeled complete graph $G=(V, E^+ \cup E^-)$ is given as a stream of edges (together with the labels at each point), and the goal is to minimize the *disagreement cost*, defined as the total number of $(+)$ edges crossing clusters and the number of $(-)$ edges in the same clusters are minimized. For the streaming setting, there exists an algorithm by CLPTYZ [STOC’24] that achieves $(2-2/13+\varepsilon)$ approximation with O(n log n) space (note that although this is claimed to be the sate-of-the-art, there actually exists an algorithm that gives $(1+\varepsilon)$-approximation with $\tilde{O}(n)$ space, albeit a very impractical one. See the ‘questions’ section for more on this). 

The algorithm in CLPTYZ [STOC’24] is fairly involved and hides a large constant. As such, motivated by the practical aspect of the problem, the paper considered correlation clustering with learning-augmented oracles. Specifically, it introduces a similarity oracle that, when queried for a vertex pair $(u,v)$, provides a rough estimate $d_{u,v}$, representing the "distance" between $u$ and $v$. The quality of the oracle is measured by the ‘$\beta$ level’, which is defined by an upper bound of $\beta\cdot \text{OPT}$ on total $d_{u,v}$​ values on $(+)$ edges and $(1 - d_{u,v})$ values on $(-)$ edges. Using such a predictor, the algorithm that achieves a $(\min\{2.06\beta, 3\}+\varepsilon)$-approximation in $O(n \log n)$ space. The space complexity is considered much more practical than the CLPTYZ [STOC’24] algorithm.

The paper further conducted experiments on both synthetic and real-world graphs. The performance is better than pivot-based algorithms and is comparable to the agreement decomposition-based algorithm of CLMNPT [ICML’21].

### Strengths
Learning-augmented correlation clustering is a natural problem, and I believe people have explored different notions of predictions to find the most ‘natural’ oracle to be used (and it has to be practical). This paper made a concrete step in the right direction. The oracle is sufficiently natural, although the quality notion of $\beta$-level is a bit artificial. The experiments have shown that the oracle could help improve the performances of pivot-based algorithms significantly. As such, I think the paper could be a good addition to the literature.

### Weaknesses
I do not believe I could strongly support the paper due to the following reasons.
- Novelty: although the paper claims to be technically novel and the analysis is very non-trivial, I believe the novelty of the algorithm is quite limited. The algorithm is essentially formed by the truncation during the stream and the post-processing part. For the streaming phase, the idea is mainly from CKLPU [SODA’24] (cf. CM [NeurIPS’23]), and I do not see anything that is substantially novel. The baseline (no worse than $3$ approximation) basically comes for free by running the algorithm of CKLPU [SODA’24], and the space analysis simply follows. The post-processing algorithm adapts the algorithm of CMSY [STOC’15], for which I will give some credit for novelty. However, the key insights for this part were not clearly articulated in the paper, and I had to go to page 18 in the appendix to see why the approximation guarantee holds. 
- The $2.06\beta$ approximation factor is also somehow weak: to outperform the pivot-based $3$-approximation, there has to be $\beta \leq \frac{3}{2.06}<1.5$, which means you need predictions with very high quality. This is also clear from your experiments that your algorithm only outperforms the agreement-based algorithm when $\beta$ is quite low. 
- I also have a criticism for the learning-augmented framework being used on *graph streaming* algorithms. The streaming model mainly aims to optimize space efficiency; however, for graph-related applications, if you train a model using ML, it’s most likely some variates of graph neural networks. To train these models you would naturally need to preserve almost all edges, which is a great cost in terms of space. I think for the oracle proposed in this paper, maybe you could train some ML model that is more ‘local’ and only answers pairs of vertices. However, in such a case, how do you ensure the triangle inequality? Anyway, I think some aspects related to this point should be discussed in the paper.

### Questions
- Do you have any responses to the weakness (especially the question about how to efficiently implement the oracle)?
- (A comment:) Note that if we just aim for low-space single-pass streaming algorithm correlation clustering, there is a deterministic algorithm in "Single-Pass Streaming Algorithms for Correlation Clustering" (BCMT [SODA’23]) that returns a $(1+\varepsilon)$-approximation, albeit with very terrible ($n^n$) time. The algorithm simply enumerates all possible clusterings and checks their costs to output the min one with the cut sparsifier. This algorithm has no way to be implemented in practice, but it is indeed unbeatable in terms of space complexity and approximation. This is related to the ‘practical’ aspects of your paper, and maybe you want to discuss that also in your paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes novel learning-augmented algorithms for correlation clustering, including algorithms in offline as well as dynamic and insert-only streaming settings. All these algorithms are associated with thorough theoretical analyses on approximation factors and complexities. Finally, experiments are conducted to evaluate the performance of the proposed algorithms.

### Strengths
S1. As a theoretical paper, this paper proposes novel learning-augmented algorithms with better approximation factors than existing algorithms for the classic correlation clustering problem, showing good originality and technical quality.

S2. This paper is well-written and well-organized.

S3. The theoretical analyses of t are generally sound, though I cannot check every detail of the proofs.

S4. Some experimental results are provided to verify the empirical performance of the proposed algorithms.

### Weaknesses
W1. My main concern is that the experimental results provided are quite concise and insufficient.
- The datasets used in the experiments are quite small (with only thousands of vertices). I wonder if streaming algorithms are necessary to process such small graphs since even an $O(|V|^2)$ algorithm can fit in memory.
- Both predictors, namely noisy predictor and spectral clustering, are essentially impractical in (dynamic) streaming. The prior one assumes that the optimal clustering is already available and the latter one should utilize the adjacency matrix as input. From the perspective of online learning, predictions should be made based on prior knowledge about vertices without using global information. Furthermore, the spectral clustering method requires computing eigenvectors of the Laplacian matrix, which is computationally expensive, especially for large graphs, and is not suitable for streaming settings where the entire graph is not available at once. The paper should clarify how these predictors can be adapted to a streaming context, or provide alternative predictors that are more realistic.
- How about the running time of the proposed algorithms compared to existing ones? Do predictors introduce additional overheads?
- Can the algorithms in offline and insert-only settings serve as baselines? I have had this question since these settings are less general than the dynamic settings. Thus, the proposed algorithms are deemed to be easily adapted to such settings.

W2. Some minor problems with the presentation details.
- The text in the figures is too small and hard to distinguish.
- Add a table to summarize the theoretical results of this paper and compare them with existing ones.

### Questions
See the problems in W1.

One additional question:

Q1. Can the proposed algorithms support other types of predictors, such as binary classification?

### Soundness
3

### Presentation
3

### Contribution
3
