# Differentially Private Range Subgraph Counting

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Subgraph counting is a fundamental problem in graph analysis. Motivated by the practical need to perform graph analytics on subgraphs defined by selected vertices (or edges) rather than the entire graph, as well as privacy concerns, we initiate the study of private range subgraph counting. Given an $n$-vertex graph $G$, where each vertex (or edge) has a $d$-dimensional attribute vector, a pattern graph $H$, and a set $Q$ of range queries $q$, our goal is to count the occurrences of $H$ in the subgraph of $G$ induced by vertices (or edges) whose attributes fall within $q$, all while preserving privacy. We give the first $\varepsilon$-differentially private algorithm for range subgraph counting, achieving near-optimal accuracy (up to a polylogarithmic factor of $n$) for constant privacy parameter $\varepsilon$ and dimension $d$, with no additional computational overhead compared to non-private algorithms. 
We also demonstrate that by relaxing to $(\varepsilon, \delta)$-DP, we can achieve smaller additive errors. Furthermore, our results generalize the subgraph counting results of the partially dynamic model in [FHO21]. Empirical evaluations demonstrate that our algorithm significantly outperforms baseline methods in accuracy while ensuring strong privacy guarantees.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies differentially private subgraph counting, but in a new interactive setting where each time, the algorithm outputs the count of subgraphs in a specific region of the graph induced by vertices. In particular, each vertex is associated with a $d$-dimensional real valued vector, and each query is a $d$-dimensional range query $q = [r_1, l_1],\cdots, [r_d, l_d]$. Then, the goal is to count the occurrences of some pattern $H$ in the subgraph decided by the given range query $q$.

To achieve this goal, they first map the graph to a $2d$-dimension grid based on ranked vertex attributes to translate the range subgraph counting problem into estimating the weighted sum of points in a high-dimensional range. Then, the authors are able to utilize the well-kown constructure of (Bentley & Saxe, 1978) to construct a binary tree for answering range query. 

The authors also generalized their results to counting subgraphs based on edge attributes, which similar techniques.

### Strengths
1. The subgraph counting problem with differential privacy is interesting and important, and I am glad to see new progress being made in this direction.
2. I believe the problem setting with range queries based on vertex/edge attributes is also kind of practical, although I understand that you may be considering this setting primarily for technical reasons.

### Weaknesses
I think there are some places of the construction and the proof of your algorithms that seem somewhat questionable. But this is very likely due to my misunderstanding, so I still would like to give a cautiously positive evaluation. But in any case, I think the way you describe the algorithm makes me very hard to evaluate the real technical contribution of your paper. 

In particular, when you highlighting the difference between your work with other DP interval or range query problems, I found the only interesting (and perhaps the only non-trivial) difference to me is that the subgraph counting problem is nonlinear. However, after reading your paper, I do not see how you specifically address the issue of nonlinearity, and thus I think there *may* be some issues about the correctness of the proof (please see "Questions").

I said in my initial review text that "the way you describe the algorithm makes me very hard to evaluate the real technical contribution of your paper". And indeed now I feel I overestimated your paper. In particular, to emphasize the contribution of your paper compared to previous similar works in interval or range query problems, you said:
> we address edge-DP in graphs, whereas (Dwork et al., 2015) focuses on differential privacy in tabular data

I think this can be effectively solved by your projection step, right? I believe it is a sweet trick but not surprising or extremly non-trivial.

>  unlike point counting, our subgraph counting problem is nonlinear

As you said in the rebuttal, this is also "effectively addressed during the subgraph counting projection".

>  a single edge change can affect many mapped points and significantly impact subgraph count

This difference is minor, and it seems you may be overstating its significance, especially since your final error bound includes $GS_{f_H}$ because of this issue.

Overall speaking, I take serious issue with the presentation of this paper, and I am not sure if the technical contribution of this paper merits the acceptance to ICLR. Therefore, I do not feel like to raise my score anymore, but I will stick to the conservative score I initially gave.

### Questions
In Fact 3.4 (Properties of Range Tree), you claim that "The **sum** of the values of the tree nodes **equals** the **sum** of the values of the left child **plus** the **sum** of the values of the right child". I believe this is the case in the basic Bentley & Saxe's construction, as well as DP-interval (and rectangle) query. But to me, it is not true when you consider subgraph counting. For example, consider a four-vertex graph where $V = \lbrace 1,2,3,4 \rbrace$ with attributes $s(1)<s(2)<s(3)<s(4)$, and a pattern $H$ where $H$ is a four-length path. Clearly for each range involving less than $4$ vertices (represented by some internal vertex of the tree), the count of $H$ is zero. But the value of the root node can be $1$, right?

In other words, I think the property you described in Fact 3.4 is kind of "linearity", so why you can apply Fact 3.4 to subgraph counting? If my understanding about this issue is correct, then I would instead suggest rejecting this paper. If my understanding about this issue is incorrect, then could you please explain how do you handle the non-linearity?

Actually I think it would be even okay if Fact 3.4 does not hold, as you can always recompute the sum of the values of the internal tree nodes and add Laplace noise, instead of considering it as the sum of its children. I think the real part that I feel there might be issue with the non-linearity is that when the range involving vertices that there is *no* non-leaf node whose value represents the answer of the range query on them. For instance, in the above 4-vertex graph example (which is also your Fig 1), can you describe how you algorithm handle the range query $[s(2), s(3)]$? (I understand how it works when asking $[s(1), s(2)]$, $[s(3), s(4)]$ and $[s(1), s(4)]$ since there are nodes to represent them in your Fig 1.)

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Given a graph with each node accompanied by a vector, this paper proposes an algorithm for counting a given graph in the subgraph induced by a rectangular range query. The algorithm has no dependence on the size of the query set; to achieve this, they map each occurrence of the given graph to the rectangle for which the graph exists in space, then use a range tree to perform the suitable aggregation to answer any query rectangle.

### Strengths
The algorithm is simple and easy to implement. The paper does a good job explaining it and its intuition. The algorithm is practical for small subgraphs because it adds little runtime overhead on top of counting the subgraphs.

The idea of reducing graph counting in a subset of the original graph to range queries in 2d-dimensional space is elegant.

### Weaknesses
Especially in graphs, it is often pessimistic to add noise scaling with the global sensitivity. A simple observation is that the degree of a real-world graph is usually much less than the number of users, and this will make the local sensitivity significantly less. This has been done in prior work [FHO21]; that paper proposes graph algorithms under continual observation, which is very related to this problem setup when d = 1, and it obtains error that scales with the maximum degree of the graph.

The algorithm is less efficient when counting larger graphs (which is to be expected) or when the vector dimension is large.

### Questions
The paper [FHO21] should be cited. They propose an algorithm for counting triangles; how does it compare to the proposed algorithm (e.g. with d = 1)?

A work-around to the maximum degree issue would be to compute a maximum degree over-estimate privately, and then to run the existing algorithm adding noise tailored to this estimate. How feasible is it to use this or a related idea in order to attain error scaling with the maximum degree instead of with n?

In the experiments, is it realistic to generate the vector for each node from a Gaussian? What is d in the experiments---can it be run with higher d to evaluate how high of a dimension it may be scaled to?

### Soundness
4

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
The paper is on the problem of private subgraph counting in graph analytics, in particular, the "range subgraph counting" problem.  Here, the set up is that each vertex has numeric attributes (in dimension d) and queries specify intervals that induces appropriate subgraphs.  The goal is to do subgraph counting with DP.  The problem is reasonably motivated and the paper tries to give some examples where it might arise.  

Applying DP to this problem naively would hurt utility (due to sensitivity & composition) and not exploiting the query overlap.  The idea in the paper is to leverage the work done in high-dimensional range counting, using trees, which can exploit overlapping queries and hence add lower noise.

The technical idea is to map the number of occurrences of a subgraph to a suitable range in 2d space (here for simplicity, say d=1, ie, each vertex has a scalar numeric attribute).  This way, the problem can be "reduced" to 2d range counting with trees.  

The paper provides experimental results in two public datasets.  The experimental results are as expected and do not throw any surprises.  

The Appendix contains interesting material about sensitivity and fractional edge cover.  But the main result actually follows in a straightforward way from the result of Atserias et al 2018.

The higher-dimensional extension (d>1) is straightforward.

### Strengths
* The paper proposes an interesting set up which is reasonably motivated from both graph analytics and privacy points of view

* The paper has a principled approach to the problem, with theoretical analysis

### Weaknesses
 * The paper is more of a theory paper with experiments as add-on.  Given this,  it is quite weak from a theoretical point of view.  The mapping (the paper calls is "registered") is itself straightforward and does not offer any new non-trivial insights.

+ The bells and whistles (utility analysis, privacy analysis for the Laplace noise, the tree properties, etc) all follow from standard DP literature.  This makes the novelty aspect of the paper, especially its solution part, low and the work itself unappealing.

### Questions
181: should it be a: V -> R?  (Or since you are defining it here, R^d, as you set d=1 only later)

207: X_i ~ Lap(b_i)?

233: what is "rank pair"?

239: what is "bound information"?

243-246: to make exposition clearer, these lines defining being "registered" could be moved earlier, say, before line 232.  Incorporing the definition of s(.) in text (instead of in Alg 1) will also be helpful to avoid going back and forth.  
Def 3.1  Is u = u_0, v = u_{|V_H|-1}?  Saying what "registered" at (u, v) means in words might be helpful.  Also giving intuition of why we need this notion (basically some canonical way of mapping an occurrence) will be helpful.  

265: This para could be moved much earlier for improved flow.

411: Might be useful to spell out the last step in the equation

Experiments: There are so many publicly available graphs with node attributes.  You didnt ahve to generate vertex attributes synthetically.

Is it possible to open up the subgraph counting algorithms to get a better solution to your problem?

### Soundness
3

### Presentation
3

### Contribution
2
