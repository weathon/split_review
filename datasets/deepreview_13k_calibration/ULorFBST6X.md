# Fair Submodular Cover

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Submodular optimization is a fundamental problem with many applications in machine learning, often involving decision-making over datasets with sensitive attributes such as gender or age. In such settings, it is often desirable to produce a diverse solution set that is fairly distributed with respect to these attributes. Motivated by this, we initiate the study of Fair Submodular Cover (FSC), where given a ground set $U$, a monotone submodular function $f:2^U\to\mathbb{R}_{\ge 0}$, a threshold $\tau$, the goal is to find a balanced subset of $S$ with minimum cardinality such that $f(S)\ge\tau$. We first introduce discrete algorithms for FSC that achieve a bicriteria approximation ratio of $(\frac{1}{\varepsilon}, 1-O(\varepsilon))$. We then present a continuous algorithm that achieves a $(\ln\frac{1}{\varepsilon}, 1-O(\varepsilon))$-bicriteria approximation ratio, which matches the best approximation guarantee of submodular cover without a fairness constraint. Finally, we complement our theoretical results with a number of empirical evaluations that demonstrate the effectiveness of our algorithms on instances of maximum coverage.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the fair submodular cover problem, where a submodular function is defined over a set of elements that are divided into disjoint classes. The objective is to select a minimum number of elements such that the selected subset meets a target submodular value threshold and the number of selected elements of each class is within a predefined interval.

Although prior work has addressed fair submodular maximization, fair submodular cover has not been previously studied. The authors first provide a reduction from fair submodular maximization to fair submodular cover. It is worth noting that there was a reduction for the non-fair case, which does not directly apply here. Additionally, they develop new algorithms for fair submodular maximization, achieving improved results when applied within their reduction framework. For designing those algorithms, they leverage the result by El Halabi et al. (2020), which converts instances of fair submodular maximization into submodular maximization problems under matroid constraints.

### Strengths
The authors present the first known algorithm for fair submodular cover, which achieves a near-optimal approximation ratio close to that of the greedy algorithm for the non-fair version, with the added benefit of increased diversity in the selected elements. Also, the paper includes experimental results that support the practical effectiveness of their proposed methods and highlight the benefits of their approach in selecting diverse elements across classes.

### Weaknesses
The difference between the authors' reduction and the existing reduction from general submodular maximization to submodular cover could be elaborated on further. This distinction is somewhat unclear, and understanding the technical differences would enhance the clarity of their contribution.

The paper could benefit from a more detailed comparison between their fair submodular maximization algorithms and existing algorithms for submodular maximization under matroid constraints, especially for their best algorithm which is based on multilinear extension that already has been used for submodular maximization.

### Questions
- Could you clarify the technical differences between your reduction from fair submodular maximization to fair submodular cover and the standard reduction used in the non-fair setting?
- How do your algorithms for fair submodular maximization differ technically from previous approaches for submodular maximization under matroid constraints, particularly the one based on the multilinear extension?

### Soundness
4

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
The paper studies the fair submodular cover problem. In this problem, we are given a set of ground elements and a monotone submodular function defined over them. All ground elements are partitioned into $N$ groups, each group $c$ having a corresponding interval $[p_c,q_c]$. The objective is to select as few elements as possible such that the value of the submodular function is greater than or equal to a given threshold $\tau$, while ensuring that the proportion of selected elements from each group falls between $p_c$ and $q_c$.

The authors consider bicriteria approximation algorithms, where the threshold constraint may be violated by a factor. By establishing a relationship between fair submodular cover (FSC) and fair submodular maximization (FSM), they show that given a $(\gamma,\beta)$-approximation algorithm for FSM, they can convert it to an algorithm for FSC with an approximation ratio of $((1+\alpha)\beta, \gamma)$. if the given FSM algorithm is continuous, they can yield an approximation ratio of $((1+\alpha)\beta, ((1-3\epsilon)\gamma-2\epsilon)/(1+3\epsilon +2\epsilon/\gamma))$. Furthermore, they present nearly feasible algorithms that can admit $((1+\alpha)/\epsilon, 1-O(\epsilon))$-approximation and $((1+\alpha)(\ln(1/\epsilon)+1), 1-O(\epsilon))$. Finally, the proposed algorithms are investigated experimentally.

### Strengths
- The fair submodular cover problem makes sense. The paper makes theoretical contributions. A nice relationship between FSM and FSC is established in the paper and several bicriteria approximation algorithms are proposed. The high-level algorithmic ideas are clean.

- Both theoretical analysts and empirical evaluations are provided.

### Weaknesses
 - The problem certainly holds theoretical interest. However, I am a bit concerned about whether it will engage the ICLR community. Could the authors provide some real-world applications?

- The authors did not compare the empirical running time of the proposed algorithms with the baselines. The theoretical running time looks horrible, so I wonder how long these algorithms will take in practice.

### Questions
See the weakness above.

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
4

### Summary
This paper studies a variant of the classical submodular cover problem, in which, given a monotone submodular function, the goal is to pick an element set with the smallest size so that the value of this set is larger than a given threshold. This paper studies the fairness version of the problem, in which the ground element set is partitioned into k groups, and each group has an upper $u$ and lower bound $l$. A fair solution should pick at least $l$ elements and, at most, $u$ elements from each group. The goal is still to pick a fair solution with a minimum size such that the value of the picked set is larger than a given threshold.

The main contribution of this work is a bicriteria algorithm that achieves $\ln n$-approximation with a slightly violating fairness constraint. This is the essentially best possible since the classical submodular cover admits the set cover problem as a special case.

### Strengths
1. The studied problem is theoretically interesting and the presentation of this paper is clear. I appreciate that the authors give an intuitive description, which helps understand the algorithm's high-level idea.

2. The obtained results are almost tight for a bicriteria approximation. Based on my knowledge, these kinds of fairness constraints (upper and lower bounds for each group) always improve the difficulty of a problem a lot. It is reasonable to study the bicriteria approximation in this case.

3. The authors also include the experimental result for the set cover instance, demonstrating the proposed algorithms' efficiency.

### Weaknesses
1. The studied problem is theoretically interesting, but it is a little incremental. One needs to provide convincing motivation for the problem. It looks that the studied problem only adds an extra constraint to the classical submodular cover problem. The introduction section does not give a specific motivation for the studied problem. Specifically, the paper lacks a discussion of real-world scenarios where the fairness constraints, with both upper and lower bounds on group sizes, are naturally present. It's not clear why a simple cardinality constraint on the overall set size would not suffice in many practical situations. The paper should elaborate on the necessity of these specific fairness constraints, perhaps by providing examples where these constraints are crucial for achieving a desirable outcome, and where other simpler constraints would fail.

2. There is no lower bound known in the paper. Namely, there is no lower bound for the bicriteria approximation. This may not be a big problem since these fair constraints are usually hard. But, one still needs to show how good is the trade-off obtained by the paper. The paper should discuss the tightness of the bicriteria approximation in the context of known hardness results for related problems. While the authors mention the hardness of the classical submodular cover, it is not clear how the fairness constraints impact the achievable approximation ratio. A more detailed discussion of the theoretical limitations, even if a tight lower bound is not available, would be beneficial. For example, it would be useful to analyze if the bicriteria approximation is tight under some specific assumptions or problem instances.

### Questions
I don't have any specific questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the submodular cover problem under the fairness constraint (FSC). The authors propose two algorithms, convert-fair and convert-continuous, which exploit the dual relationship between Fair Submodular Maximization (FSM) and FSC to transform bicriteria approximation algorithms for FSM into ones applicable to FSC. Next, they propose three algorithms for FSM that, when combined with their converting algorithms, produce approximate solutions for FSC. The discrete algorithms achieve approximation ratios of $(1 - O(\varepsilon),\frac{1}{\varepsilon})$ for FSM, while the continuous algorithm achieves a better ratio of $(1 - O(\varepsilon),\ln(\frac{1}{\varepsilon}) + 1)$ but needs more queries. By integrating these algorithms into their framework, they obtain improved FSC algorithms with better approximation ratios. The continuous algorithm for FSM with the converting algorithm achieves a $((1 + \alpha) \ln (n) + 1, 1 − 7/n)$ bicriteria approximation guarantee for an instance of FSC when  $\varepsilon = \frac{1}{n}$, which is close to the lower bound.

### Strengths
* The proposed algorithms are easy to follow.
* The proposed continuous algorithm approximately matches the theoretical lower bound, demonstrating its efficiency.

### Weaknesses
 * The motivation for considering FSC is unclear. The authors only say that FSM has been well studied while FSC has not. This can not be a good motivation. 
* The experiments demonstrate the advantages of the discrete algorithms on the FSC problem compared to the standard greedy algorithm; however, the solutions obtained by the discrete algorithms include many more elements. Moreover, the experiments lack the presentation of the effectiveness of the continuous algorithm. The lack of experimental results for the continuous algorithm is a significant omission, especially given its theoretical advantages. The paper would benefit from a more thorough empirical evaluation of all proposed algorithms.


### Questions
* What are the motivations for FSC, e.g., real-world applications?
* Compared to the conversion algorithms without fairness constraints, what is the novelty of the conversion algorithms proposed in the paper?
* In Theorem 2, the approximation ratio $\frac{(1 - 3\varepsilon)\gamma - 2\varepsilon}{1 + 3\varepsilon + \frac{2\varepsilon}{\gamma}}$ 'holds in expectation'. Is it sufficient to guarantee that the solution provided by the algorithm is close to feasible with high probability?
* The continuous algorithm proposed in the paper theoretically outperforms the discrete algorithms, while the experiments only showcase the performance of the discrete algorithms. Are there any experimental results available for the continuous algorithm?

### Soundness
2

### Presentation
2

### Contribution
2
