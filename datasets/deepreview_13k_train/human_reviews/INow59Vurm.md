# Towards Explaining the Power of Constant-depth Graph Neural Networks for Linear Programming

- Decision: Accept
- Scores: 5, 3, 6, 8

## Abstract
Graph neural networks (GNNs) have recently emerged as powerful tools for solving complex optimization problems, often being employed to approximate solution mappings. Empirical evidence shows that even *shallow* GNNs (with fewer than ten layers) can achieve strong performance in predicting optimal solutions to linear programming (LP) problems. This finding is somewhat counter-intuitive, as LPs are *global* optimization problems, while shallow GNNs predict based on *local* information. Although previous theoretical results suggest that GNNs have the expressive power to solve LPs, they require deep architectures whose depth grows at least polynomially with the problem size, and thus leave the underlying principle of this empirical phenomenon still unclear. In this paper, we examine this phenomenon through the lens of distributed computing and average-case analysis. We establish that the expressive power of GNNs for LPs is closely related to well-studied distributed algorithms for LPs. Specifically, we show that any $d$-round distributed LP algorithm can be simulated by a $d$-depth GNN, and vice versa. In particular, by designing a *new* distributed LP algorithm and then unrolling it, we prove that constant-depth, constant-width GNNs suffice to solve sparse binary LPs effectively. Here, in contrast with previous analyses focusing on *worst-case* scenarios, in which we show that GNN depth must increase with problem size by leveraging an impossibility result about distributed LP algorithms, our analysis shifts the focus to the *average-case* performance, and shows that constant GNN depth then becomes sufficient no matter how large the problem size is. Our theory is validated by numerical results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a connection between GNNs and existing distributed LP algorithms, suggesting that the iterations of distributed LP algorithms correspond to message-passing steps in GNNs. Additionally, the authors use existing results on iteration bounds in distributed LP algorithms to infer bounds on the number of GNN layers.

### Strengths
Existing theoretical results on the representational power of GNNs for optimization problems often rely on strong assumptions about problem size, leaving the complexity of GNN size for these problems largely unexplored. This paper advances this area by drawing connections to existing results from LP algorithms for specific types of LPs.

### Weaknesses
1. The title may overstate the contributions by referring to GNNs for "linear programming," as the authors actually draw on results specific to packing and covering LPs. While these capture certain classes of combinatorial optimization problems, they do not encompass general LPs.

2. The connection between GNN message passing and factorization-free LP algorithms is straightforward. GNN message passing involves matrix-vector multiplications, allowing any convergence results from first-order LP algorithms that consist of matrix-vector multiplications to be applied here. The results presented in this paper represent only a subset of these. In this respect, the theoretical contribution of this paper appears limited.

3. The authors emphasize throughout the paper that shallow GNNs are practically effective. However, the specific value of "constant number of layers" suggested remains unclear. My understanding is that for the theories to hold, this constant would likely be very large, rendering it impractical. If so, the theory borrowed from existing distributed LP algorithms may not fully explain the practical utility of shallow GNNs.

4. The absence of experimental results, even with toy examples, to validate this proposed number of GNN layers is unusual for a machine learning paper. This raises further questions about the practical applicability of the proposed result.

### Questions
See weakness.

### Soundness
3

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
This paper analyzes the depth and width of graph neural networks for linear programs, based on existing results for distributed algorithms.

### Strengths
1. This paper is in general clearly written and is easy to follow.

2. This paper connects GNNs with distributed algorithms for solving LPs.

### Weaknesses
1. I do not see much novelty in the theory. In particular, I feel that this paper is just translating known results for distributed algorithms to GNN language.

2. If you fix $\epsilon$ and $\eta$, then Theorem 2 and Theorem 3 are direct corollaries of Chen et al. (2023). The results have to be more quantitative if you want to have something new. Specifically, the bounds on depth and width should be analyzed with respect to the problem parameters, not just as a function of the desired accuracy $\epsilon$ and $\eta$. The current analysis lacks a clear connection between the network architecture and the specific characteristics of the linear program being solved.

3. There are no numerical experiments.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the expressive power of GNNs in representing LPs. The gap between theoretical and practical insights in this area is notable: theoretically, there are no tight upper bounds on the required GNN size (in terms of depth or width) for representing LPs, with upper bounds typically depending on the problem size. However, in practice, GNNs with minimal depth are often sufficient. This study aims to bridge this gap. Focusing on a specific class of LPs (sparse binary LP), it connects GNNs with a distributed algorithm. For this type of LP, the distributed algorithm’s iteration achieves constant steps, suggesting that a GNN with constant depth can reach a certain accuracy level.

### Strengths
1. The theoretical exposition is clear and rigorous. In the constant-depth analysis, the authors employ the big-O notation O(xxx) with actual constants rather than constants implicitly tied to the LP size. This precision in presentation is commendable, as many similar papers tend to obscure critical constants within the big-O notation, which can be misleading. This paper avoids that pitfall.

2. The analysis focuses specifically on sparse, binary-coefficient LPs. This approach is sensible, as constructing a constant-size GNN for all LPs would be overly ambitious. Additionally, their analysis highlights the conditions and assumptions required for a constant-size solution—namely, sparsity and boundedness of the maximum values in A. This adds valuable insights for the field.

### Weaknesses
My primary concern with this paper is the applicability of its theoretical findings to practical GNNs. Specifically, if one were to train a GNN to solve packing/covering LPs, would the trained model align with the theoretical framework presented here? Do the theoretical observations in this paper truly correspond with practical outcomes?

### Questions
refer to "weakness"

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the expressive power of constant-depth GNNs for approximatively solving sparse, binary linear programs (LPs), specifically packing/covering LPs. Specifically, the paper embeds a [recent distributed LP algorithm](https://arxiv.org/abs/2409.16168) into a GNN such that $d$ layers amount to running  $d$ rounds of the algorithm. They then show that while the lower bound of [Kuhn 2016](https://dl.acm.org/doi/abs/10.1145/2742012?casa_token=axoJjWtNII0AAAAA:GRCjUb2MDG1nvsEH5FOwiboPhll-JbEfJaN2ObfeanJbgQvDy7WAW1s4UD4Orown_Alaw0RvTMbBifAA) rules out these constant depth GNNs performing well in the worst case on all LPs, the _average_ case can be achieved with a probabilistic bound (which is the meat of the contribution).

### Strengths
- originality: to my knowledge and google scholar skills, the first such proof => original
- quality+ clarity:  very crisp presentation, while I do not feel 100% solid in my verification, i feel I could at least follow the proof,and it appears correct to me. 
- important result if correct, as it gives _an_ upper bound (it remains to be evaluated how tight) on the depth required for a given LP-heuristic GNN

### Weaknesses
 - I think some basic numeric would have rounded off the results and helped readers and practitioners judge the tightness of the bound.
- additionally, I think the question of learnability with standard algorithms would have been interesting to study in the specific setting studied

both of these could be addressed with some small scale numerics given the constructive arguments used

additionally, I think making the chain of reduction in generality from "generic LP => sparse LP= > sparse binary LP" + the generality of packing coverage vs other types of LP clearer would additional help non-experts judge the relevance of the work.

### Questions
my main question is: have you implemented an run your LP? i think numerical issues like precision could play an additional role. additionally, are you aware of an explicit counter example? this + a randomized average case numerical evaluation could really round of this paper in my eyes

### Soundness
3

### Presentation
4

### Contribution
3
