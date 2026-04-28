# GUMP: Alleviating Oversquashing with Unitary Message Passing

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
Message passing mechanism contributes to the success of GNNs in various applications, but also brings the oversquashing problem. Recent works combat oversquashing by improving the graph spectrums with rewiring techniques, disrupting the original graph connectivity, and having limited improvement on oversquashing in terms of oversquashing measure. Motivated by unitary RNN, we propose Graph Unitary Message Passing (GUMP) to alleviate oversquashing in GNNs by applying a unitary adjacency matrix for message passing. To design GUMP, a transformation is first proposed to equip general graphs with unitary adjacency matrices and keep their original graph connectivity. Then, the unitary adjacency matrix is obtained with a unitary projection algorithm, which is implemented by utilizing the intrinsic structure of the unitary adjacency matrix and allows GUMP to be permutation-equivariant. In experiments, GUMP is incorporated into various GNN architectures and the extensive results show the effectiveness of GUMP on various graph learning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the oversquashing problem in GNNs by introducing Graph Unitary Message Passing , which uses a unitary adjacency matrix for message passing. Unlike previous methods that rely on rewiring and disrupt original graph connectivity, GUMP maintains the graph’s structure while alleviating oversquashing. The approach involves a transformation to equip graphs with unitary adjacency matrices and a unitary projection algorithm, ensuring permutation-equivariance. Extensive experiments show that incorporating GUMP into various GNN architectures improves performance across multiple graph learning tasks, demonstrating its effectiveness in tackling oversquashing.

### Strengths
Novelty:
The idea is innovative, building upon unitary RNNs to create Graph Unitary Message Passing (GUMP) as a solution to the oversquashing problem in GNNs. The approach is grounded in a solid theoretical foundation, demonstrating a reasonable and well-motivated extension to graph learning.

Empirical Results:
The paper demonstrates strong empirical results, showing significant improvements across multiple datasets compared to prior methods. This highlights the practical effectiveness of GUMP in addressing oversquashing and enhancing graph learning tasks.

Clarity and Analysis:
The Jacobian measure is clearly presented, and the results show that it does not decrease, providing robust evidence of the method's impact. The ablation study is well-executed, delivering clear and actionable insights into the contributions of various components of the method.

Novel Construction Approach:
The paper introduces a novel and elegant method to construct equivalent graphs and compute unitary adjacency matrices. This approach maintains the original graph connectivity while ensuring permutation-equivariance, representing a creative and impactful contribution to the field.

### Weaknesses
The paper would benefit from a clearer introduction to unitary matrices, their role in RNNs, for the readers without enough background.

### Questions
Theorem 2.1 is highly important. Could you also briefly clarify the differences between the informal theorem and the formal version presented in the main content?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper explores the unitary message passing for alleviating oversquashing in GNNs. It first looks at the adjacency matrix of the line graph and then aims to find a unitary matrix with the same support as the line graph adjacency matrix. There are also some experiments to show the effectiveness of the proposed method.

### Strengths
Modification of a message passing matrix to be unitary is well motivated. The line graph approach seems novel and interesting.

### Weaknesses
1. There is some disconnection between Proposition 2.2 that the adjacency matrix of the line graph has the same support of some unitary matrix and the proposed method which finds the projection of a weighted adjacency matrix to the set of unitary matrices. It is unclear to me if the result in Proposition 2.3 has the same support as the adjacency matrix of the line graph.
2. The computational complexity of the proposed method is very high as it involves taking the square root of a matrix of the size $2e \times 2e$ where $e$ is the number of edges in the graph. Though the block matrix structure can be exploited, but there is no guarantee how many blocks can be found in the matrix. For example, it's likely that the proposed method cannot perform on all of the LRGB datasets.
3. The experiments are not very convincing. They only compared with the one-hop variant of some models that aims to solve the oversquashing problem. Note that the oversquashing problem is intrinsically multi-hop and I don't see the rationale weakening the baseline models to one-hop.
4. The preprocessing time that involves the computation of the block matrix is not reported.
5. It's unclear why there is a base layer GNN encoding in the proposed method. An ablation study on the necessity of the base layer GNN encoding would be helpful.
6. On the Peptide dataset, the GCN can easily achieve the accuracy of the proposed method by some proper data preprocessing or normalization. The authors should provide a comparison following [1].

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The work proposes to substitute the adjacency matrix of the graph with a related unitary adjacency matrix to alleviate issues such as over-squashing — in a permutation equivariant manner. The authors theoretically show the advantage of this method in terms of over-squashing sensitivity bounds and show experimentally its good performance.

### Strengths
I enjoyed the approach of the work. Many works that tackle over-squashing have a pretty similar flavour and usually propose to modify the connectivity of the graph. I think that this approach instead is quite novel and well-motivated. I enjoy the connection the work has to well-established ideas from the RNN literature and overall I found the idea to be quite sound. 

The work also compares against a large number of baselines and overall has a very good range of experiments. 

The presentation is also good with a lot of implementation details as well and a number of interesting discussions.

### Weaknesses
This is a small nitpick, but I believe that the “Jacobian measure” should be formally defined before the introduction of Theorem 2.1. It might be also better to leave the theorem more formally as I don’t think it’s too long to write out. 

Please see questions.

### Questions
(Q1) I would like to have more clarity on the mathematical contributions of the work. For instance, is Proposition 2.2 a novel result or is this already known? More precisely, I am interested in understanding whether the propose idea of taking an adjacency matrix and constructing a related unitary matrix is a new idea in itself. 

(Q2) Would it be possible to share the runtimes of GCN-GUMP against regular GCN? I read in the limitations that GUMP incurs a high computational cost, but I would be interested in understanding what this means in practice. I do not see the scalability as a weakness as I think that the idea is sufficiently interesting in itself, but I am curious to see the effiency of the implementation.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors propose to address oversquashing in GNNs by imposing message-passing with a unitary matrix. Observing that most previous works modify the underlying connectivity of the graph, they propose a method that first consist in transforming the graph into its line graph, for which a theoretical result exists stating that there exists weighted adjacency matrices that are unitary. Then, they compute a new weighted adjacency matrix with attention mechanisms, then project it onto the set of unitary matrices by putting its singular values to 1. They give an efficient method for the last part if the adjacency is block-diagonal.

### Strengths
- an interesting idea
- good experimental results

### Weaknesses
The principles behind the method left me thoroughly confused. It seems immensely complicated, and just "obtaining unitarity" is not enough of a justification for all the steps involved in the method.

- Mainly, the authors remark that transforming a graph into its line graph proves that **there exists** unitary adjacency matrices with the same support than the original one. But, unless I am missing something, the projection of $\bar A$ onto the set of unitary matrices has no reason to respect this support condition. And vice-versa, if the support condition is not crucial, why go to the line graph at all, which is costly? One could have simply computed $A(A^\top A)^{-1}$ with the original adjacency matrix, resulting in also a unitary matrix.

- I don't get why we need the attention coefficients here. Could the simple adjacency matrix be used? (or maybe, one could imagine that computing weights allows to precisely find the unitary matrix that respect the support, but some kind of iterative projection algorithm must be envisioned here)

** Edit after rebuttal **
The authors response makes sense. I still have doubts about the method and some points would really deserve more clarity, but I raised my initial score.

- Concerning the efficient algorithm to put the singular values to 1, it would be good to describe how the line graph matrix is guaranteed to be block diagonal. Also, the algorithm requires to find a permutation to find the block diagonal structure, can this be done efficiently?

### Questions
See above, I have questions about the method itself, maybe I am missing something.

### Soundness
2

### Presentation
3

### Contribution
1
