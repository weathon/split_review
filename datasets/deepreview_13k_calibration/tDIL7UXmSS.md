# Quantum (Inspired)  $D^2$-sampling with Applications

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
$D^2$-sampling is a fundamental component of sampling-based clustering algorithms such as $k$-means++. 
Given a dataset  $V \subset \mathbb{R}^d$ with $N$ points and a center set $C \subset \mathbb{R}^d$, $D^2$-sampling refers to picking a point from $V$ where the sampling probability of a point is proportional to its squared distance from the nearest center in $C$.
Starting with $C = \{\}$ and iteratively $D^2$-sampling and updating $C$ in $k$ rounds is precisely $k$-means++ seeding that runs in $O(Nkd)$ time and gives $O(\log{k})$-approximation in expectation for the $k$-means problem.
We give a quantum algorithm for (approximate) $D^2$-sampling in the QRAM model that results in a quantum implementation of $k$-means++ that runs in time $\tilde{O}(\zeta^2 k^2)$. 
Here $\zeta$ is the aspect ratio ({\it i.e., largest to smallest interpoint distance}) and $\tilde{O}$ hides polylogarithmic factors in $N, d, k$.
It can be shown through a robust approximation analysis of $k$-means++ that the quantum version preserves its $O(\log{k})$ approximation guarantee.
Further, we show that our quantum algorithm for $D^2$-sampling can be {\em dequantized} using the {\em sample-query access} model of Tang~\cite{tang-thesis}. This results in a fast quantum-inspired classical implementation of $k$-means++, which we call {\em QI-$k$-means++}, with a running time $O(Nd) + \tilde{O}(\zeta^2k^2d)$, where the $O(Nd)$ term is for setting up the sample-query access data structure.
Experimental investigations show promising results for QI-$k$-means++ on large datasets with bounded aspect ratio.
Finally, we use our quantum $D^2$-sampling with the known $ D^2$-sampling-based classical approximation scheme ({\it i.e., $(1+\veps)$-approximation for any given $\veps>0$}) to obtain the first quantum approximation scheme for the $k$-means problem with polylogarithmic running time dependence on $N$.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides a quantum algorithm as well as a dequantized (i.e quantum inspired classical) version of it for the problem of $D^2$ sampling. This type of sampling is important for the kmeans++ algorithm and is defined as sampling points in $\mathbb{R}^d$ with probability proportional to the nearest center from a set $C$ of cluster centers in $\mathbb{R}^d$. The classical implementation, which gives a $O(log k)$ approximation guarantee, involves a preprocessing step that builds a sample-query access data structure in time O(Nd). Depending on the implementation, the running time after this data structure is set up is $\tilde{O}(\zeta^2k^2d)$ or $\tilde{O}(\zeta^6k^2)$, where $\zeta$ is the ratio between the largest and smallest pairwise distance in the pointset. The results are incomparable with prior work, since there is no algorithm that is the best in all parameter regimes. This work does asymptotically improve on all prior works for sufficiently small values of $\zeta$ and $k$ though. The authors also give a quantum fixed parameter approximation scheme to get a $(1+\varepsilon)$ approximation for the k-means problem for any $\varepsilon>0$. The k-means problem has been shown to be NP-hard to approximate below a 1.07 constant factor due to prior work and therefore, this approximation scheme has exponential dependence on $1/\varepsilon$, while it is efficient in terms of the other parameters. Finally, the authors provide experiments that verify the performance of the algorithms and make the comparison with the classical k-means++ algorithm.

### Strengths
The paper gives novel algorithms for k-means, which is a fundamental problem for machine learning. The paper is also fairly well written.

### Weaknesses
The performance of the algorithm is only better in certain parameter regimes compared to prior work.

Minor comments:
-Line 94: I would call it “result” instead of “observation”
-In many places throughout the paper, I believe the tilde notation is a bit abused. It should only be used to hide factors logarithmic in the function displayed, not arbitrary ones as in Theorem 1 for example.

### Questions
How can someone choose which algorithm to use between the ones in Theorem 2 and Theorem 3? For example, is there an efficient way to compute $\zeta$ in advance?

### Soundness
3

### Presentation
3

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
The present paper gives new algorithms; both quantum and classical, for  the $k$-means problem. $k$-means problem is a significant clustering problem with broad spectrum of applications. Given a set $V$ of points in ${\mathbf R}^{d}$, find a set $C$ of $k$ points, called centers, in $\mathbf{R}^d$, so that  the sum of squared distance from points in $V$ to the closest point in $C$ is minimized. Because of its foundational algorithmic nature, this computational problem has been of attention from researchers from several perspectives. 

The present paper investigates new quantum approaches to solving this problem. Given it is NP-hard, the goal is to develop approximation algorithms and an algorithm known as $k$-means++ (extending the well known $k$-means algorithm by Lloyd) by Arthur and Vassilvitskii has a $O(\log k)$ approximation guarantee in expectation. A basic ingredient of $k$-means++ algorithm is called $D^2$-$\mathit{sampling}$: a procedure that given a data set $V$ and a center set $C$, samples a point in $V$ with probability proportional to its squared distance from the nearest center in $C$. 

The main contribution of this paper is a new quantum algorithm for $D^2$-sampling and a subsequent de-quantization of it. This algorithm then leads to new implementation of  (both quantum and classical) of $k$-means++. While there are other known quantum implementation of  $D^2$-sampling, the present algorithm appears to have different efficiency parameters and hence appears to perform better in certain regimes than known ones. The main parameter that the  running time of the algorithm depends on is the ${\mathit aspect ratio}$ $\zeta$: the ratio between the largest and smallest inter-point distance in the dataset. In particular, the quantum algorithm that the author/s develop runs in time $\tilde{O}(\zeta^2k^2)$ with $\tilde{O}$ hiding the poly-log dependencies on relevant parameters. The author/s show how this can be de-quantized to get a classical algorithm with running time $O(Nd)+\tilde{O}(\zeta^2k^2d)$.   The paper also presents some initial experimental results.

### Strengths
The paper designs new algorithms for a classical and significant computational problem: the  $k$-means problem. Any new algorithm for classical problems such as $k$-means is a contribution to the field of ML and data science.   Thus the paper has broad applicability (in particular will be of interest to ICLR audience).  This is the main strength of the paper.

### Weaknesses
 The main weakness is  the algorithm's dependency on the aspect ratio. The algorithm has quadratic dependency on the aspect ratio. That makes one wonder whether it will be really  useful for broad applications. While the author/s briefly discuss this dependency in the paper, it is not at all clear why there needs to be a quadratic dependency. Is it possible to prove a lower bound (in a meaningful restricted model) showing that this dependency is needed? The authors cite a paper by Cohen-Addad et al that presents an algorithm that has closer to $\log$ dependency on $\zeta$ (at the expense of having a $N^{\theta(1)}$ factor in the running time) which appears to be much more attractive. The paper will be substantially stronger if it can bring more clarity on this issue. Following are concrete points that the authors may address to make the paper stronger. 

1. Provide a more detailed justification for why the algorithm presented has quadratic dependence on the aspect ratio.
2. Discuss whether the author/s  believe this dependence is fundamental or if there may be ways to improve it.
3. Consider proving a lower bound, to show whether this dependence is necessary (if the authors believe it is). 
4. Compare their aspect ratio dependence more thoroughly to other algorithms like the Cohen-Addad et al. result, analyzing the tradeoffs in more depth.

### Questions
The paper is nicely written, overall. However, the discussion through the prior work is not very clearly written. May be a table of relevant known results will be useful to understand the context of the algorithm in terms of efficiency. Also a more detailed discussion on aspect ratio and its relevance (and if there are fundamental obstacles in improving the running time in terms of this parameter) will be very useful. A table of relevant known results might include:

1. Key prior quantum and classical algorithms for k-means/k-means++
2. Their runtime complexities
3. Their approximation guarantees
4. Key parameters they depend on (e.g. aspect ratio)

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
2

### Summary
The paper discusses a novel quantum-inspired algorithm for the k-means problem. Theoretical guarantees of the new algorithm are provided, showing it outperforms classical algorithms in certain areas. Experiments compare runtime of the quantum inspired k-means++ versus the classical k-means++.

### Strengths
Starting from originality, the paper extends ideas in quantum machine learning (primarily the sample-access-query model of Tang) to the classical k-means problem, providing novel algorithms and results. Connections to existing literature are well-discussed, and discussions of the strengths and weaknesses of the new algorithm compared to classical algorithms are provided.

In terms of quality and clarity, it is quite clear that effort has been made to polish the text. The problem formulations, motivations, related work, and the design of the algorithm from a quantum-inspired perspective are all clearly stated. 

It is interesting to see that the new algorithm has better dependency in N but worse dependency in the aspect ratio and k. While this does not show a uniform improvement in all aspects, it is still a good contribution.

### Weaknesses
One of the downsides of the algorithm's runtime dependencies is the dependence of the preprocessing cost O(Nd), which is ignored when comparing against existing results. If we add in O(Nd) to the equation, then both the new algorithm and classical algorithms has a linear dependence on $N$. Perhaps it would be meaningful to have experiments that showcase runtime *after preprocessing* so the plots in Figures 2-3 can be more reflective of the runtime dependencies after preprocessing.

There are some (minor) questions about the results:

1. In page 4, there is discussion about dependencies in the *assumption-free* case but seems like there are no results for the cases with assumptions. What comparisons and improvements can be made in scenarios with assumptions?

2. Considering different algorithms appear to have quite different dependencies with regards to N, d, k, aspect ratio, matrix conditions, etc., what are some impossibility results available for the k-means problem and how does the algorithm's runtime dependencies compare with it?

3. Can you elaborate on whether there are methods to improve the dependency on the aspect ratio $\zeta$? It seems to be a bit counterintuitive. For example, if there are two clusters of points, and the two clusters are very well-separated, intuition might suggest that k-means with $k=2$ should be relatively straightforward and should be easier as the two clusters are separated out even more. But, in this case $\zeta$ grows and the bound on the runtime worsens. Additionally, $\zeta$ becomes very large if there is even a single pair of points that are close by. Do these observations suggest that the dependencies on $\zeta$ can be tightened?

### Questions
There are some (minor) questions about the results:

1. In page 4, there is discussion about dependencies in the *assumption-free* case but seems like there are no results for the cases with assumptions. What comparisons and improvements can be made in scenarios with assumptions?

2. Considering different algorithms appear to have quite different dependencies with regards to N, d, k, aspect ratio, matrix conditions, etc., what are some impossibility results available for the k-means problem and how does the algorithm's runtime dependencies compare with it? 

3. Can you elaborate on whether there are methods to improve the dependency on the aspect ratio $\zeta$? It seems to be a bit counterintuitive. For example, if there are two clusters of points, and the two clusters are very well-separated, intuition might suggest that k-means with $k=2$ should be relatively straightforward and should be easier as the two clusters are separated out even more. But, in this case $\zeta$ grows and the bound on the runtime worsens. Additionally, $\zeta$ becomes very large if there is even a single pair of points that are close by. Do these observations suggest that the dependencies on $\zeta$ can be tightened?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors give novel quantum and classical implementations of $k$-means++.
The main ingredient of their approach is a novel $D^2$-sampling method.

### Strengths
$k$-means++ is an important tool in ML, therefore this paper is significant as it gives novel quantum or classical implementations of it.

### Weaknesses
Page 1:
I find the abstract to have too much low-level information :)

Page 4:
Can you please expand on related work?
How about the connections of your work to computational complexity?

Page 5:
Please give some extra background knowledge in quantum computing and Dirac bra-ket notation :)

Page 6:
Can you please elaborate on the concept of dequantization and provide some examples?

Page 7:
I do not see why the states $(1),\ \dots,\ (4)$ are the right ones involved in the quantum $D^2$-sampling algorithm :)

Page 8:
I do not understand the Lines 412 -- 417.
What does pseudo approximate mean here?

Page 9:
I am not an expert with experiments :)

Page 10:
Where is the Conclusion? :) Can you please add a Conclusion and Future Work section?

### Questions
Page 1:
I find the abstract to have too much low-level information :)

Page 4:
Can you please expand on related work?
How about the connections of your work to computational complexity?

Page 5:
Please give some extra background knowledge in quantum computing and Dirac bra-ket notation :)

Page 6:
Can you please elaborate on the concept of dequantization and provide some examples?

Page 7:
I do not see why the states $(1),\ \dots,\ (4)$ are the right ones involved in the quantum $D^2$-sampling algorithm :)

Page 8:
I do not understand the Lines 412 -- 417.
What does pseudo approximate mean here?

Page 9:
I am not an expert with experiments :)

Page 10:
Where is the Conclusion? :) Can you please add a Conclusion and Future Work section?

### Soundness
3

### Presentation
4

### Contribution
4
