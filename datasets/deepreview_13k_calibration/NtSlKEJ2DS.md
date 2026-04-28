# Optimal Flow Transport and its Entropic Regularization: a GPU-friendly Matrix Iterative Algorithm for Flow Balance Satisfaction

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The Sinkhorn algorithm, based on Entropic Regularized Optimal Transport (OT), has garnered significant attention due to its computational efficiency enabled by GPU-friendly matrix-vector multiplications. However, vanilla OT primarily deals with computations between the source and target nodes in a bipartite graph, limiting its practical application in real-world transportation scenarios.
In this paper, we introduce the concept of Optimal Flow Transport (OFT) as an extension, where we consider a more general graph case and the marginal constraints in vanilla OT are replaced by flow balance constraints. 
To obtain solutions, we incorporate entropic regularization into the OFT and introduce virtual flows for individual nodes to tackle the issue of potentially numerous isolated nodes lacking flow passages. Our proposition, the OFT-Sinkhorn algorithm, utilizes GPU-friendly matrix iterations to maintain flow balance constraints and minimize the objective function, and theoretical results for global convergence are also proposed in this paper.
Furthermore, we enhance OFT by introducing capacity constraints on nodes and edges, transforming the OFT problem into a minimum-cost flow problem. We then present the Capacity-Constrained EOFT-Sinkhorn algorithm and compare it with the traditional Minimum cost flow (MCF) algorithm, showing that our algorithm is quite efficient for calculation. 
In particular, our EOFT-Sinkhorn is evaluated on high-precision and integer-precision MCF problems with different scales from one hundred to five thousand size, exhibiting significant time efficiency and the ability to approximate optimal solutions. Source code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed efficient algorithms to address the minimum cost flow (MCF) problem with Sinkhorn iterations. The authors claim a problem named the Optimal Flow Transport (OFT) problem as an extension of OT to general graphs by replacing marginal constraints with flow balance constraints. They use entropic regularization and virtual flows to propose a GPU-friendly/matrix-based OFT-Sinkhorn algorithm. Furthermore, they apply capacity constraints on nodes and edges, transforming the OFT problem into a capacity-constrained MCF problem. Experiments demonstrate computational efficiency on various datasets.

### Strengths
This paper applied the entropic regularization and Sinkhorn iterations to the MCF problem and provided algorithms that can run on GPU. This is good for solving large flow problems more efficiently than the traditional method. The paper includes experimental evaluations demonstrating that the proposed algorithm can solve the problem efficiently on large-scale problems. In addition, this work provides the proof for the convergence of the proposed algorithms looks good to me.

### Weaknesses
My primary concern is about the novelty. This work claims to extend OT to general graphs with flow balance constraints, which is essentially a restatement of the classic minimum cost flow (MCF) problem. The MCF problem is well-studied, and applying entropic regularization is a common practice. Secondly, this paper needs further literature review of existing work that applies similar techniques to the MCF problem using GPU acceleration or matrix-based methods, such as [1][2]. Additionally, another concern is that this paper does not show how their proposed method benefits the machine learning community. There is a lack of discussion on the applications of MCF in machine learning tasks, and no such experiments are provided. Given these weaknesses, I tend to reject this paper.

### Questions
- How does the proposed algorithm compare with existing GPU-accelerated methods for solving the MCF problem? Including such comparisons within the experiment will strengthen this paper.
- Is there any machine learning problem that can apply the algorithms of this paper? 
- Have the authors evaluated the performance of their algorithm on CPUs? Will the code be public?

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
2

### Summary
The authors provide a Sinkhorn-like algorithm (hence involving parallelizable matrix multiplication) for the case of optimal transport on more general graphs than the bipartite graph.

### Strengths
The paper is well written and theoretically sound and possibly introduces a new interesting method that can leverage modern GPU infrastructure.

### Weaknesses
 The numerical experiments are not completely clear, and their relation to existing works could be slightly clarified.

In Table 1, there is an error in the 10kx10k line for the W/ edge+note constraints: the fastest method in 'Real" with 1425s not "ours" with 1462s.

In general, when there are constraints, the "Real" method has similar orders of magnitude results and still has a better solution quality in terms of objective. So what if the authors stop the compared algorithms at the same obj value their algorithm achieves? It is unclear which algorithm would be faster between "Real" and "ours"?

"However, these studies primarily rely on graph's shortest distances and do not directly compute transport couplings within the graph." -> How is that a problem? Is it slower? Not GPU friendly? Or is it not as generic as the authors' solution? Are there settings where the authors could compare their approach with theirs?

### Questions
In Table 1, there is an error in the 10kx10k line for the W/ edge+note constraints: the fastest method in 'Real" with 1425s not "ours" with 1462s.

In general, when there are constraints, the "Real" method has similar orders of magnitude results and still has a better solution quality in terms of objective. So what if the authors stop the compared algorithms at the same obj value their algorithm achieves? It is unclear which algorithm would be faster between "Real" and "ours"?

"However, these studies primarily rely on graph's shortest distances and do not directly compute transport couplings within the graph." -> How is that a problem? Is it slower? Not GPU friendly? Or is it not as generic as the authors' solution? Are there settings where the authors could compare their approach with theirs?

### Soundness
3

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
3

### Summary
This paper introduces the concept of Optimal Flow Transport (OFT) as an extension of vanilla OT, where the authors consider a more general graph setting and the marginal constraints in vanilla OT are replaced by flow balance constraints. Adding entropy regularization directly cannot derive an algorithm to obtain an approximate solution as directly as vanilla OT due to two reasons. First of all, there are many isolated points that do not have any flow passing through them in the exact solution, while under entropy regularization, flows are necessarily channeled through them, causing significant bias. Second, the flow balance constraint cannot directly form an alternating iterative algorithm like the marginal constraint. The authors address these issues by modifying the original problem formulation and proposing the new OFT-Sinkhorn algorithm. The new approach utilizes GPU-friendly matrix iterations and is guaranteed to converge globally (with the rate). The authors also extend their approach to a more general setting where the capacity constraints on nodes
and edges are avaliable. The encouraging empirical results are presented and discussed.

### Strengths
1. The authors extend the vanilla OT within a bipartite graph to a more general graph case, and thus propose optimal flow transport, in which the marginal constraints are replaced by flow balance constraints.

2. The authors propose the entropic OFT to get the GPU-friendly OFT-Sinkhorn algorithm to get the approximate solution of the OFT problem. The theoretical guarantee is also proposed for global convergence.

3. The authors incorporate node and edge capacity constraints into the OFT, and in this case our OFT is equivalent to the minimum-cost flow problem. By considering these constraints, the authors modify the OFT-Sinkhorn algorithm to ensure that the output satisfies capacity constraints. Experimental results on the minimum-cost flow problem showcase the superiority of the proposed algorithm.

### Weaknesses
1. The idea of extending the vanilla OT within a bipartite graph to a more general graph case is not new and have been investigated in the literature. While I agree that it is meaningful to replace the marginal constraints by by flow balance constraints on nodes, this idea is not novel by itself and the optimal flow transport problem in Eq. (2) is rather standard. The formulation itself, while adapting the concept of flow balance, does not introduce a fundamentally new optimization challenge beyond what is already present in network flow literature.

2. It is important to note that directly adding entropy regularization cannot derive an algorithm to obtain an approximate solution as directly as vanilla OT. However, I do not think addressing this issue would be difficult and the modified formulation is Eq. (5) is also based on some standard tricks from network flow literature. Specifically, the introduction of self-loops to handle isolated nodes, while practically useful, is a common technique in graph algorithms. Based on this formulation, the development of OFT-Sinkhorn algorithm is almost the same as that of Sinkhorn algorithm and handling node and edge capacity constraints would not significantly change the algorithmic scheme. The core algorithmic contribution appears to be a relatively straightforward adaptation of existing techniques.

I would like to say that I do not undermine the value of new methods but the contribution of this paper is a little bit incremental to me from a technical viewpoint. This is a good work by itself but does not offer too much insights.

### Questions
1. I encourage the authors to further clarify the difference between the current paper and the existing works. For example, you state that the previous studies primarily rely on graph’s shortest distances and do not directly compute transport couplings within the graph. In my understanding, these studies can compute transport couplings but need to precompute the shortest distances on the graph (please correct me if I am wrong). Then, why can you directly compute transport couplings within the graph? It seems counterintuitive to me if this is only because you use the entropy regularization. Would you like to provide me more details? 

2. You state that your EOFT-Sinkhorn is evaluated on high-precision and integer-precision MCF problems with different scales from one hundred to five thousand size, exhibiting significant time efficiency and the ability to approximate optimal solutions. The experimental results confirm that your method can achieve a solution of higher quality. It is a bit surprising since the vanilla implementation of Sinkhorn algorithm requires much time to converge to a high-accurate solution. Would you like to give me some reasons why your method could achieve the high-accurate solutions in practice?

### Soundness
3

### Presentation
3

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
This work extends optimal transport to network flow problems and formulated an entropic algorithm.

### Strengths
1. The writing is clear and clarity is good.

2. The numerical proposal is sound.

3. The contribution of this work is hard to gauge due to point 3,4,5 in the weakness section. So the result, while looking promising, is currently only a minor strength of this work.

### Weaknesses
1. The authors omitted connections to constrained optimal transport, such as Benamou et al 2014 (1412.5154) and Tang et al 2024 (2403.05054), which are both general-purpose algorithms with entropic regularization.

2. There are numerous instances of grammatical errors in this work. The authors are advised to change it. (This doesn't affect this reviewer's evaluation for the score.)

3. While OFT-Sinkhorn with edge/node/node&edge constraints is definitely a good contribution, it doesn't seem clear why one would not simply use Sinkhorn in the unconstrained case. The authors have not included numerical comparison to make this point across. What is better? Sinkhorn has more GPU acceleration and should be much better in the unconstrained case (say, you take the same regularization strength and compare results).

4. In the numerical experiments, the proposed OFT-Sinkhorn algorithm seems to do better than Gurobi, which is quite confusing as Gurobi should output the ground truth. The reviewer suspects that it is because the OFT-Sinkhorn solution is unfeasible, thereby giving a better objective. If this interpretation is correct, then the authors need to change to a better metric for comparison.

5. The benchmark ZKW and Real methods are exact methods and they do not seem to be up to date. The authors need to also consider state-of-the-art methods for comparison, and the authors need to consider approximate algorithms.

6. The conclusion section needs a rewrite. It seems to suggest that this method can solve NP-hard graph-based problems, which is why the wording needs to be refined.

### Questions
No questions. All are suggestions listed in weakness already.

### Soundness
3

### Presentation
3

### Contribution
3
