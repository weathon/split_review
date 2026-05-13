# GPU-Accelerated Counterfactual Regret Minimization

- Decision: Reject
- Scores: 5, 3, 3, 5, 5

## Abstract
Counterfactual regret minimization is a family of algorithms of no-regret learning dynamics capable of solving large-scale imperfect information games. We propose implementing this algorithm as a series of dense and sparse matrix and vector operations, thereby making it highly parallelizable for a graphical processing unit, at a cost of higher memory usage. Our experiments show that our implementation performs up to about 401.2 times faster than OpenSpiel's Python implementation and, on an expanded set of games, up to about 203.6 times faster than OpenSpiel's C++ implementation and the speedup becomes more pronounced as the size of the game being solved grows.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a GPU-accelerated approach for Counterfactual Regret Minimization (CFR), a class of no-regret learning algorithms widely used in solving large-scale imperfect information games like poker. Traditionally, CFR algorithms rely on recursive tree traversal, which limits their efficiency. This work proposes a restructured CFR algorithm that converts the operations into a series of dense and sparse matrix and vector computations, making it highly parallelizable on GPUs at the cost of increased memory usage.

The study concludes that the proposed approach could serve as a foundational step for highly scalable CFR on supercomputing infrastructures, enabling faster solutions to complex game-theoretic problems.

### Strengths
Originality: The paper introduces a creative approach by reformulating Counterfactual Regret Minimization (CFR) as matrix operations suitable for GPU processing. This novel restructuring allows a highly parallelizable version of CFR, which has not been extensively explored in existing CFR literature.

Efficiency in Design: By avoiding recursive tree traversal, the implementation achieves substantial speed gains, especially in larger games, demonstrating an efficient design choice that effectively leverages GPU hardware.

Thorough Empirical Evaluation: The paper evaluates the new approach on a diverse set of games with varying complexity and size, rigorously benchmarking it against established OpenSpiel baselines in both Python and C++. This experimental breadth strengthens the validity of its claims about speedup and scalability.

Significant Potential for Scalability: The approach is well-suited for large-scale games, with experiments showing up to 352.5 times faster performance than OpenSpiel’s Python baseline and 22.2 times faster than its C++ counterpart, especially promising for future work on supercomputing platforms or even more extensive imperfect information games.

### Weaknesses
Originality Limitations: Although innovative, the paper applies GPU parallelization to the vanilla CFR algorithm, which is somewhat limited in novelty given the existence of other CFR variants that incorporate modern enhancements (e.g., CFR+ or discounting techniques). A broader implementation encompassing these would increase the relevance of this work. Specifically, the paper does not address how the matrix-based approach would handle the dynamic updates to regret and strategy profiles that are characteristic of CFR+ or similar algorithms, which often involve per-node adjustments based on accumulated regrets. This lack of consideration limits the immediate applicability of the work to state-of-the-art game-solving scenarios.

Limited Exploration of Advanced CFR Variants: The paper does not explore compatibility with modern CFR variants, such as sampling-based or discounting techniques, which are widely used in state-of-the-art game-solving algorithms. For example, the paper does not discuss how the proposed matrix operations would integrate with Monte Carlo CFR (MCCFR), which samples trajectories through the game tree, or how it would accommodate discounting, which prioritizes recent regrets over older ones. This omission significantly reduces the approach’s applicability in advanced game AI contexts.

High Memory Requirements: The matrix-based reformulation, while speeding up calculations, results in high memory consumption, especially for larger games. This trade-off is not thoroughly analyzed or discussed, particularly regarding potential bottlenecks for memory-constrained systems, which limits practical usability. The paper does not provide a detailed analysis of memory scaling with respect to the number of game states or the branching factor, which is crucial for understanding the practical limits of the approach. Furthermore, it does not explore techniques such as sparse matrix representations or memory-mapping to mitigate these issues.

Narrow Application Scope: The results indicate that this GPU implementation is unsuitable for small games, where it can actually perform worse than CPU implementations due to overhead. This could reduce its perceived impact and limits its practicality in domains that deal with a wide range of game sizes. The paper does not provide a clear threshold for game size where the GPU implementation becomes advantageous, nor does it analyze the overhead costs associated with data transfer between CPU and GPU memory, which is a critical factor in determining the overall performance.

### Questions
N/A

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
This paper aims to frame the CFR algorithm as a sequence of matrix operations (Think GraphBlas).

### Strengths
This paper is interesting because it tries to solve two problems at the same time:
- APIs like [GraphBLAS](https://graphblas.org/) have successfully represented graph algorithms as a sequence of BLAS-like operations over semirings. This paper tries to do the same for CFR.
- It's not obvious how GPUs, the powerhouse of deep learning, can be used to accelerate game solving (other than calling neural networks). This paper tries to solve this gap.

### Weaknesses
Overall, this paper tries to aim for a best-of-both-worlds approach: low coding effort and high performance. Instead, it ends up with an exposition that is somehow less clear than the original CFR paper, benchmarks that don't inspire confidence, and the resulting algorithm seems to be not very flexible and requires major efforts to do the simplest changes like going from simultaneous to alternating variants of CFR.

- The open spiel codebase is not an example of a performant CFR implementation, it is meant to be extremely generic. Comparing with more reasonable implementations is necessary (for instance the Cepheus codebase for Leduc, there are other codebases as well).
- The games tested are extremely tiny. The largest game (tic tac toe) takes less than 3 seconds to traverse on a pure Python implementation and is a perfect information game. It's not clear what a perfect information game is doing there. The number of nodes in Appendix A is the number of infosets + terminals (i.e., there is only one node per infoset), and looking at the code, `tic_tac_toe.py` is not a dark variant of tic-tac-toe.
- The updates are batched and masked. Effectively, for each depth $d$, a (sparse) matrix multiply is done but only the output at depth $d$ is stored. As a matter of efficiency, this method becomes more and more wasteful as the depth of the game increases. For example, in a game with a branching factor of 10, at depth 5, you are updating 10 times more nodes than needed. This suggests that the performance gains might be less pronounced in deeper, more complex games.
- Modifying the algorithm seems extremely expensive and cumbersome. (see  line 515)
- The computations presented here are probably not very GPU friendly and a lot of FLOPS are probably wasted (Yet this has not been analyzed). Specifically, the reliance on sparse matrix operations, while efficient for memory, may lead to significant thread divergence on GPUs. This is because threads within a warp (or wavefront) execute the same instruction at the same time. When dealing with sparse data, threads often diverge, leading to wasted computation and reduced performance. Profiling the code to identify such bottlenecks would be beneficial.
- The paper does not include any exploitability results. Exploitability is a standard metric in the field to evaluate the convergence of CFR algorithms. While the paper focuses on performance, including exploitability results would provide a more complete picture of the algorithm's effectiveness and allow for a direct comparison with existing CFR implementations.

### Questions
- What was the inspiration for using CuPy?
- Why are there no exploitability results?
- How long does it take to setup the game tree?
- Were 32 or 64-bit floats used? Were tensor cores enabled?

- 022- The abstract is used in the introduction
- 037- GPU is defined twice
- 062- What is the philosophical reason for making the nature player have infosets? I find this very nonstandard
- 163- While CFR can find approximate coarse correlated equilibrium, the formulation presented in this paper does not. The reason is that it is not the product of average strategies that converges to the set of CCEs, but rather the average product.
- 175- The introduction should include the CFR theorem ($r^{(T)}(i_{+,j}\in\mathbf{I}_{+})$ is bounded by the sum of the local regrets)
- 201- Case in point in that this paper tries to inflate its notation, $l\in[1, D]\cap \mathbf{Z}$ is just weird.
- 292- Hadamard product was not defined. I would argue that it is not a common notation and should be defined explicitly.
- 397- It is not clear what purpose Figure 1 serves in the paper.
- 432- Why is there no error bar on the time measurements?
- 515- I understand that pruning the tree may be expensive (surely a very big downside) but why is alternating CFR hard to implement?
- 523- "Our approach is also much easier (and likely more efficient) to be run on supercomputers compared to previous methods" This statement is not backed by anything in this paper, see Weaknesses.
- 651- the number of infosets for liars_dice seems to be wrong, it should be 24576 not 24583 (or 12288 if we remove infosets with only one action).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
1

### Summary
This paper studies hardware acceleration for counterfactual regret minimization.

### Strengths
The acceleration seems quite significant as the author claimed.

### Weaknesses
Well, it is unclear to me if this paper fits well for ICLR since there is no new algorithm / methodology / theory proposed. It may fit more to ML system venue. The benchmark selected (Game in OpenSpiel) is less known. I will suggest show improvements on more common benchmarks. I have to admit I do not have sufficient GPU hardware background to evaluate this paper.

### Questions
see above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a GPU implementation of the CFR algorithm. It stores the game tree structure in matrices and performs a series of matrix operations to compute reach probabilities, expected payoffs, and other relevant information level by level, thereby avoiding the costly tree traversal process. By leveraging GPU acceleration for these matrix operations, the approach significantly enhances CFR’s speed, albeit at the expense of increased memory usage.

### Strengths
* The paper is well-written, and the notations are clearly defined.
* The GPU implementation significantly boosts the speed of the CFR algorithm, and the difference from the OpenSpiel implementation grows as the game size increases.
* The code is open-sourced, making it easy to apply to games in OpenSpiel.

### Weaknesses
This is not the first approach to implementing CFR on GPUs. For example, the thesis by Reis [1] and the report by Weng [2] also present GPU implementations of CFR. Additionally, DeepStack [3] [4] constructs the look-ahead tree and runs CFR on GPUs. These works and this paper use a similar approach, computing relevant information in CFR level by level and accelerating it with GPUs. However, the paper does not compare or discuss these related works. Specifically, the paper fails to acknowledge that the core idea of level-by-level computation and parallelization on GPUs has been explored in prior work. The primary contribution of this paper appears to be a specific formulation of these computations using matrix and vector operations, which, while potentially offering performance benefits, is not a fundamentally new algorithmic approach. The paper also does not provide a detailed comparison of the performance gains achieved by their matrix-based implementation compared to the more direct implementations found in prior work. This makes it difficult to assess the practical significance of their specific approach beyond the general idea of GPU-accelerated level-by-level CFR.

### Questions
* What is the space complexity of the method?
* Can this method be used to accelerate the calculation of exploitability?

Minor Suggestions:

* It will help to improve clearity by adding a symbol table and an example figure.
* It will help to enhance readability by keeping the symbol descriptions consistent with CFR literatures, such as using $I$ for an information set and $h$ for a history node.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript discussed about how to leverage GPU’s computation power on sparse matrix multiplication to improve the computation speed for large scale games.

### Strengths
* Leveraging GPUs to improve the computation for game solving is still under-explored and this manuscript has a solid step towards it.

### Weaknesses
 * This is a more engineering-driven paper without lots of scientific contribution.
* I’m not quite sure about where the benefit is from. See the questions.
* Is OpenSpiel’s implementation paralleled? I think this can have a lot of differences in the performance. Only comparing with the benchmark implementation can be limited.
* You showed there is a trade-off for memory efficiency and computation time. However I don’t see there are any reasons on this if we store every sparse matrix within the corresponding format. Can you further explain this?

### Questions
* Is OpenSpiel’s implementation paralleled? I think this can have a lot of differences in the performance. Only comparing with the benchmark implementation can be limited.
* You showed there is a trade-off for memory efficiency and computation time. However I don’t see there are any reasons on this if we store every sparse matrix within the corresponding format. Can you further explain this?

### Soundness
2

### Presentation
2

### Contribution
2
