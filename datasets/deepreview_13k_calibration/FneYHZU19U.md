# Constrained Graph Clustering with Signed Laplacians

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
Given two weighted graphs $G = (V, E, w_G)$ and $H = (V, F, w_H)$ defined on the same vertex set, the constrained clustering problem asks to find a set $S\subset V$ that minimises the cut ratio between $w_G(S, V\setminus S)$ and $w_H(S, V\setminus S)$. We develop a Cheeger-type inequality that relates the solution of the constrained clustering problem to the spectral properties of $G$ and $H$. To reduce computational complexity, we use the signed Laplacian on $H$, simplifying the calculations while maintaining accurate results. By solving a generalized eigenvalue problem, our algorithm provides improvements in performance, particularly in scenarios where traditional spectral clustering methods face difficulties. We demonstrate its practical effectiveness through experiments on both synthetic and real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the constrained clustering or semi-supervised clustering problem. The authors propose a novel Cheeger-type inequality that relates the solution of the constrained clustering problem to the spectral properties of the graphs. Moreover, the signed Laplacian trick is used to simplify calculations and improve computational efficiency. The paper presents an algorithm that solves a generalized eigenvalue problem to achieve this, and demonstrates its effectiveness through experiments on synthetic and real-world datasets.

### Strengths
1. The use of signed Laplacian and the development of a Cheeger-type inequality for constrained clustering is a novel approach that has not been explored in the literature to my knowledge.
2. The paper demonstrates the practical effectiveness of the proposed algorithm through empirical studies on both synthetic and real-world datasets, showing significant improvements over classical spectral clustering methods.
3. The proposed method is theoretically grounded. (disclaimer: I didn't carefully verify the proofs)

### Weaknesses
1. The contribution is unclear. Constrained clustering is an old and well-explored topic, and the paper does not provide a clear explanation of how the proposed method differs from existing approaches. The major contribution seems to be the optimization algorithm for problem (1), but this is not explicitly stated.
2. The paper does not provide a comprehensive comparison with widely-known baselines in the field of constrained clustering, which would strengthen the claims of the proposed method's superiority. Essentially, the authors surveyed a lot in the introduction, but it's a pity that they didn't compare with them.

### Questions
1. Summarize the main contribution and the key difference between the proposed method and existing constrained clustering methods.
2. Empirically compare with other well-known constrained clustering baselines.

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
3

### Summary
The paper studies a version of the constrained clustering problem. Given two graphs representing MUST-LINK and CANNOT-LINK constraints, respectively, the goal is to find a set of vertices along with associated cuts in each graph, minimizing the cut ratio.

The main result is an cheeger-type inequilty and the corresponding algorithm to find the cut. The paper also provides experiments to demonstrate the practical effecttiveness.

### Strengths
- The Cheeger-type inequality proposed in this paper for the constrained clustering problem looks strong, as it includes only one additional denominator term ($\lambda_2(\Delta^H)$) compared to the original Cheeger inequality.

- The technique proposed in the paper is similar to the known sweep-set algorithm of the Cheeger inequality, but combining existing techniques and obtaining interesting results in the new model is also a solid contribution.

- I checked the main proof, and aside from a few details I don’t fully understand, it looks correct to me.

### Weaknesses
 - I suggest the authors spend more passages to properly motivate the study of this version of the constrained clustering problem. In the paper, the motivation for the constrained clustering problem and why using the cut ratio between two graphs as a target seems lacking. The authors could provide real-world examples where this particular formulation of constrained clustering is useful, or explain how the cut ratio relates to clustering quality.

- The experiments use two graphs, but the baseline spectral clustering algorithm can only consider one graph, which seems to give an advantage to the proposed algorithm. The authors could include additional baselines that can handle two graphs, or discuss how the performance gap relates to the additional information provided by the second graph.

- Although the results of (Koutis et al., 2023) cannot be directly compared with this paper, the two results are similar in form (with perhaps just a difference between $\Phi(G)$ and $\Phi(H)$). So what is the advantage of this paper? The authors could provide a more detailed comparison with Koutis et al. (2023), highlighting specific technical or practical advantages of their approach. 

- In the proof of Theorem 1 (at line 244), why are the events independent? My understanding is that the probabilities and expectations here are with respect to $t$, so the cuts on $G$ and $H$ are likely dependent.

### Questions
- Although the results of (Koutis et al., 2023) cannot be directly compared with this paper, the two results are similar in form (with perhaps just a difference between $\Phi(G)$ and $\Phi(H)$). So what is the advantage of this paper? The authors could provide a more detailed comparison with Koutis et al. (2023), highlighting specific technical or practical advantages of their approach. 

- In the proof of Theorem 1 (at line 244), why are the events independent? My understanding is that the probabilities and expectations here are with respect to $t$, so the cuts on $G$ and $H$ are likely dependent.

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
4

### Summary
The authors propose a new  approach to graph clustering that integrates MUST-LINK and CANNOT-LINK constraints through the use of signed Laplacians. It introduces an algorithm that modifies edge weights and adds self-loops to align degree sequences across graphs, employing a generalized eigenvalue problem to improve computational efficiency and maintain clustering accuracy. A key theoretical contribution is the development of a Cheeger-type inequality which relates the clustering problem to the spectral properties of two graphs. Empirical evaluations on both synthetic and real-world datasets illustrate the method.

### Strengths
The approach proposed allowing to incorporate user constraints into a clustering algorithm is interesting and the solution seems to be quite efficient and theoretically interesting.

### Weaknesses
There are a few weaknesses, some of which could be addressed in an improved version of the paper (see questions below).

The method is not sufficiently well motivated in terms of primary objective and proxy for the objective. Specifically, the paper does not adequately justify why the extended cut ratio is a suitable objective function for constrained clustering. The connection between minimizing this ratio and achieving high-quality clusters that respect MUST-LINK and CANNOT-LINK constraints is not clearly established. It's unclear how this proxy directly translates to the desired clustering outcome, especially when the constraints are noisy or conflicting. The paper needs a more thorough discussion on the theoretical and practical implications of using this specific proxy.

The complexity of the method is not really addressed properly:  finding the eigenvector of the signed Laplacian can be extremely prohibitive for large graphs? The paper lacks a detailed analysis of the computational cost associated with the proposed algorithm. While the use of a generalized eigenvalue problem is mentioned, the practical implications for large-scale graphs are not explored. The computational bottleneck of finding the leading eigenvector of the signed Laplacian, especially for sparse graphs, needs to be discussed in detail. Furthermore, the paper does not provide any benchmarks or comparisons with other methods for large-scale graph clustering, making it difficult to assess the scalability of the proposed approach.

The experiments are a bit misleading (see below).

The proof of the main Theorem is not readable in current its state and in general the wording could be improved significantly. The proof lacks clarity and is difficult to follow. The probability space and the events defined in the proof are not clearly explained, making it hard to understand the underlying logic. The steps in the proof are not presented in a way that is easy to verify, and the connections between different parts of the proof are not well-established. The notation is also not consistent, which further complicates the understanding of the proof.

### Questions
1)  It is not sufficiently justified why the criterion given (extended cut ratio) is a good proxy for graph clustering with constraints. A more involved discussion explaining this point would be welcomed. Also I did not understand the discussion on the scaling of the graph, why would you need a priori to order the degrees of H and G?
Please provide a more detailed explanation of why the extended cut ratio is an appropriate proxy for constrained graph clustering and
clarify the purpose and necessity of ordering the degrees of H and G in the graph scaling discussion.

2) The upper bound provided by Theorem 1 could be extremely loose? 

3) The proof of the main theoretical result is not clearly written. 
Provide a more detailed explanation especially about the probability space defined and events, (line 241 and in the Appendix).
Include a step-by-step breakdown of the proof, clearly defining all terms and concepts used.


4) Discuss the computational complexity of finding the main eigenvector for large graphs.
Explain how the method might be extended to handle more than 2 clusters.
Address the performance of the algorithm on imbalanced clusters.
Provide benchmarks or comparisons with other methods for large-scale graph clustering.

5) I do not really understand the setting of the SBM in the experiments. The graphs G and H are generated independently?  That would not reflect at all the initial problem?
Please discuss how well this experimental design reflects real-world constrained clustering scenarios.
Consider adding an experiment that more closely mimics the initial problem formulation.

### Soundness
2

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
This paper addresses the constrained clustering problem, which involves partitioning data into k disjoint clusters, subject to both "must-link" constraints (represented by a graph G) and "cannot-link" constraints (represented by a graph H). The objective is to minimize the number of G-edges across clusters while maximizing the number of H-edges within clusters. Several variants of this problem exist, depending on the specific settings, such as noisy versus hard constraints. The authors focus on a restricted version where k=2 and the constraints are hard. They propose a relaxation of the ratio-cut formulation, which leads to a generalized eigenvalue problem. In addition, they derive a Cheeger-type inequality for this ratio cut.

### Strengths
The numerical results provided in the paper are promising and suggest that the proposed approach performs well in practice. The idea of adding negative self-loops appears to significantly decrease the running time.

### Weaknesses
 * Given the extensive literature on clustering with signed graphs and constrained clustering, the related work section is underdeveloped. The authors should provide a more detailed explanation of how their approach differs from existing methods in constrained spectral clustering, particularly in comparison to the algorithm presented in [1].

* The proof of Theorem 1 contains significant flaws, which must be addressed.

* The numerical evaluation lacks a strong baseline comparison.  Indeed, the authors only compare against an algorithm that uses only G (and not H). Including a comparison with other constrained spectral clustering methods (for example from references [1,2,3]), would convince the algorithm of the paper (which I believe compared to [1], the main difference is the addition of negative self-loops).

* Using spectral clustering as the baseline on geometric graphs is not entirely appropriate. The model presented in Section 4.2 is an instance of the Geometric Block Model (GBM), which has gained popularity in recent graph clustering literature. However, as shown in [4], when the distance between cluster centers is 0, standard spectral clustering using the second eigenvector fails to cluster geometric graphs. But, alternative algorithms, such as triangle counting or those using different eigenvectors, can succeed in such settings. Therefore, the accuracy drop observed in Figure 2b may be attributed to the choice of spectral clustering, while another clustering algorithm might have succeeded by using only G. Specifically, even when the distance between centers is 0, the communities may still be recoverable from GG alone, given that $r_{inter} \ne r_{intra}$.


Specific Issues:

*    Line 226: The phrase "we prove this implies that..." lacks clarity, as I believe the proof of this implication is not given anywhere.
*    Line 241: The probability mentioned here is unclear. The authors should specify what this probability refers to.
*    Line 243: The claim that "the events are independent" requires clarification—what specific events are being referenced?
*    Line 248: The term "we define a distribution" is vague. The authors should clarify what distribution is being defined and its relevance to the analysis.
*    Line 272: The statement "Combining equation 4 with equation 5 proves the result" is incorrect. Even if the equations were correctly proven, this would yield a ratio of expectations rather than the ratio cut. Moreover, the expectation of a ratio is not necessarily equivalent to the ratio of expectations.
*    Line 322: I am unsure where does the inequality $\lambda_1(\Delta^{H'}_{\alpha}) \le \lambda_2(\Delta^H)$ comes from?


Additional Comments:

*    The proof of Theorem 1 is repeated in the appendix.
*    Line 57: The statement "the running time of our algorithm is close to traditional spectral clustering methods" is misleading. Figure 1b indicates a substantial deviation in running time between CC++ and SC when n becomes large. Additionally, the figure should display results for larger values of n to assess the evolution of the gap between the running times. 2000 vertices still correspond to small graphs. 
*    Line 277: The phrase "to find the cut with guaranteed approximation" is ambiguous: what approximation guarantee is being referenced?
*   Line 278: "n sweep sets": what does a sweep set mean?
*    Line 290: It would be helpful for the authors to provide more details on how the generalized eigenvalue problem arises, even if it is not a novel contribution (I believe this has already been addressed in previous work, such as in [1], but this is missing from the related work section).

### Questions
Specific Issues:

*    Line 226: The phrase "we prove this implies that..." lacks clarity, as I believe the proof of this implication is not given anywhere.
*    Line 241: The probability mentioned here is unclear. The authors should specify what this probability refers to.
*    Line 243: The claim that "the events are independent" requires clarification—what specific events are being referenced?
*    Line 248: The term "we define a distribution" is vague. The authors should clarify what distribution is being defined and its relevance to the analysis.
*    Line 272: The statement "Combining equation 4 with equation 5 proves the result" is incorrect. Even if the equations were correctly proven, this would yield a ratio of expectations rather than the ratio cut. Moreover, the expectation of a ratio is not necessarily equivalent to the ratio of expectations.
*    Line 322: I am unsure where does the inequality $\lambda_1(\Delta^{H'}_{\alpha}) \le \lambda_2(\Delta^H)$ comes from?


Additional Comments:

*    The proof of Theorem 1 is repeated in the appendix.
*    Line 57: The statement "the running time of our algorithm is close to traditional spectral clustering methods" is misleading. Figure 1b indicates a substantial deviation in running time between CC++ and SC when n becomes large. Additionally, the figure should display results for larger values of n to assess the evolution of the gap between the running times. 2000 vertices still correspond to small graphs. 
*    Line 277: The phrase "to find the cut with guaranteed approximation" is ambiguous: what approximation guarantee is being referenced?
*   Line 278: "n sweep sets": what does a sweep set mean?
*    Line 290: It would be helpful for the authors to provide more details on how the generalized eigenvalue problem arises, even if it is not a novel contribution (I believe this has already been addressed in previous work, such as in [1], but this is missing from the related work section).

### Soundness
1

### Presentation
3

### Contribution
2
