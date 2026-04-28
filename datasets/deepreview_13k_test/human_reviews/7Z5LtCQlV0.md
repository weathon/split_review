# A near linear query lower bound for submodular maximization

- Decision: Reject
- Scores: 8, 5, 3

## Abstract
We revisit the problem of selecting $k$-out-of-$n$ elements with the goal of optimizing an objective function, and ask whether it can be solved approximately with sublinear query complexity.

For objective functions that are monotone submodular, [Li, Feldman, Kazemi, Karbasi, NeurIPS'22] gave an $\Omega(n/k)$ query lower bound for approximating to within any constant factor. We strengthen their lower bound to a nearly tight  $\tilde{\Omega}(n)$. This lower bound holds even for estimating the value of the optimal subset. 

When the objective function is additive (i.e.~$f(S) = \sum_{i \in S} w_i$ for unknown $w_i$s), we prove that finding an approximately  optimal subset still requires near-linear query complexity, but we can estimate the  value of the optimal subset in $\tilde{O}(n/k)$ time, and that this is tight up to polylog factors.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper considers the NP-hard problem of maximizing a monotone submodular objective $f$ with a cardinality constraint $k$. In the area of submodular optimization, generally the time bottleneck is regarded as the number of queries to $f$. It was previously shown by Li, Feldman, Kazemi, Karbasi [2022] that there is a $\Omega(n/k)$ lower bound for the number of queries to $f$ for an algorithm that gives a constant factor approximation guarantee.

The current paper strengthens this lower bound to $\tilde{\Omega}(n)$ for instances where $k=o(n)$ (Theorem 3.9), which is nearly tight since there exists linear time constant factor approximation algorithms e.g. one is given by Li et al.. They also consider the very restricted special case of objectives that are additive functions, and show that even this case finding a solution with constant approximation requires nearly linear query complexity (Theorem 3.7). They further prove this lower bound holds for the general case (but not the restricted linear case) even for just estimating the value of the optimal subset. In order to prove these lower bounds, the paper makes a connection between the number of queries required for submodular maximization and the communication complexity of the distributed set detection problem (a reduction is give in Algorithm 1). To this end, they prove that the distributed set detection problem requires $\tilde{\Omega}(n)$ communication cost (Theorem 3.2) by applying the distributed SDPI inequality of Braverman et al. (2016) (Lemma 3.4). On the other hand, for the case of linear functions, the algorithm LinearSum (Algorithm 2) is provided that estimates the value of the optimal solution closely in $\tilde{O}(n/k)$ queries (Theorem 4.1), and this is tight up to polylog factors (Theorem 4.7).

### Strengths
* Lower bounding the number of queries required for a constant factor approximation algorithm for submodular maximization is an important problem, and this paper makes a solid contribution beyond those of Li et al..
* The paper seems highly novel to me. Their technique of connecting submodular maximization with the distributed set detection problem is not an approach I have seen used in submodular optimization before.
* Paper is clear and well-written.

### Weaknesses
* Since the focus of the paper is on hardness results, one potential con is that the paper doesn't provide much in the way of solutions for applications, and may be highly theoretical relative to other papers featured at ICLR. They do provide the algorithm LinearSum for the restricted case where $f$ is linear and we seek to approximate the value of the optimal solution. This is interesting because it shows that finding the approximate value where the objective is linear is not as hard as the general case. But the linear setting is very restricted, and so I'm not sure that there is much value for this algorithm in applications.
* The paper is missing an important citation. Theorem 4 of Kuhnle [2021] (referenced below) actually gives the lower bound of $\Omega(n/k)$ before the work of Li et al..

Kuhnle, Alan. "Quick streaming algorithms for maximization of monotone submodular functions in linear time." International Conference on Artificial Intelligence and Statistics. PMLR, 2021.

### Questions
* Could you provide intuition for why the more complicated reduction to distributed set detection gives these stronger bounds, compared to approaches more similar to Li et al.?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper works on the problem of selecting $k$-out-of-$n$ elements, specifically focusing on submodular maximization problem. It improves the imapproximability result of query complexity from $\Omega(n/k)$ to $\tilde{\Omega}(n)$ for achieving any constant-factor approximation by relating submodular maximization to distributed set detection problem. Moreover, they prove that finding an approximately optimal subset of an additive function requires near-linear query complexity, though the value of the optimal subset can be estimated in $\tilde{O}(n/k)$ queries. Finally, they propose a sublinear algorithm for submodular maximization on additive function. The paper emphasizes on the inapproximability result and approximation algorithm for additive functions.

### Strengths
This paper proves inapproximability results of query complexity for both general submodular function and additive function by reducing from the distributed set detection problem. It seems novel. Also, it provides a sublinear time algorithm that approximates the optimal value within $(1\pm\epsilon)$ factor.

### Weaknesses
The paper's presentation is lacking in clarity. Some definitions are not as precise and formal as in other works. For example, the definition of submodular on Line136 is wrong. If $f$ is non-monotone and $C\subseteq B$, it is possible that $f_A(C) < 0$ and $f_B(C) = 0$. The actual definition should be as follows:

The set function $f$ is submodular if $f_S(u) \ge f_T(u)$ for every two sets $S\subseteq T\subseteq N$ and element $u\in N\setminus T$.

Moreover, the additional related work part is not detailed enough. The second paragraph, in particular, merely lists a collection of papers without further explanation.

The contribution of the paper seems limited. The inapproximability result on query complexity provided in Theorem 3.7 is $\Omega(\alpha^5n/log^2(n))$, with $k\le O(\alpha n)$. However, [1] proves that an $(\beta+\epsilon)$-approximation algorithm obeying $k = \beta n$ must use $\Omega(\frac{n}{\log n})$ value oracle queries, which is tighter than the one provided in Theorem 3.7. 

References

[1] Wenxin Li, Moran Feldman, Ehsan Kazemi, and Amin Karbasi. Submodular maximization in clean linear time. In Sanmi Koyejo, S. Mohamed, A. Agarwal, Danielle Belgrave, K. Cho, and A. Oh (eds.), Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022, 2022. URL http://papers.nips.cc/paper_files/paper/2022/ hash/6faf3b8ed0df532c14d0fc009e451b6d-Abstract-Conference.html.

### Questions
When the oracle is discussed on Line 031, it is unclear what the oracle model is. The formal definition of the value oracle model is that the value oracle returns $f(S)$ for any given set $S\in N$. However, the examples provided in the last sentence, "estimating the quality of prediction from a subset of features or samples by training a smaller model on them", are closer to the noisy value oracle model discussed in [1].

Typically, approximation algorithms find a subset with a constant approximation ratio for the objective value. In this paper, the algorithm approximates the optimal value. Its potential applications are not discussed.

References

[1] Horel, Thibaut, and Yaron Singer. "Maximization of approximately submodular functions." Advances in neural information processing systems 29 (2016).

### Soundness
2

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
This paper investigates discrete submodular and modular function optimization under a cardinality constraint. It establishes an improved lower bound on the query complexity for submodular maximization by linking it to the communication complexity of distributed set detection. Additionally, the paper proved that finding an approximately optimal subset for additive function maximization still requires
near-linear query complexity,  but the authors propose an algorithm that estimates the optimal value of additive function maximization in $\Omega(n/k)$ queries.

### Strengths
1. The topic of proposing query-efficient algorithms for submodular optimization problems is important and has many applications in the field of machine learning.
2. The proposed lower bound for monotone submodular maximization improved compared with existing results. The proof idea introduced in this paper seems interesting and can be useful for the submodular optimization community.

### Weaknesses
1. The algorithm for the additive function, presented as a one of the key result in the paper, is insufficiently explained. Additionally, the authors do not discuss any related work in this area, leaving questions about how their work compares with prior studies on similar problems. A comparison with relevant literature would strengthen the paper by situating this result within the broader context of related research.
2. Several theoretical contributions, including the final theorem, are not fully clarified. Without adequate explanations, readers may struggle to understand the implications and validity of these findings.
3. The presentation of proofs is unclear and challenging to follow.
4.  Although the authors present proofs for their main results, they do not discuss the technical innovations and challenges in sufficient depth. A clearer articulation of the novel aspects of their approach would help readers appreciate the paper's unique contributions.
5. It is claimed that this paper produces query-efficient algorithms for estimating the optimal value of the studied problem, but there is no experimental evidence to support the claim in the paper.
6. Typos: 
 * Line 093: "The studied of the query..."; 
 * Line 187-188: "for any $i\in[n]$, $X_{t,i}\sim \mathcal{D}_0$"

### Questions
1. The paper introduces an algorithm that estimates the optimal value of the problem of additive function maximization under cardinality constraint. What are the related work of this algorithm and how does this compare to existing results?
2. What are the major technical difficulties the authors overcome in proving the lower bound of the query complexity for the submodular maximization problem?

### Soundness
2

### Presentation
1

### Contribution
2
