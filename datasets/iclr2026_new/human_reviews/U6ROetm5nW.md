## Human Reviewer 1

### Summary
This paper proposes techniques to accelerate kernel sum estimation with LSH, an important theory problem in machine learning. 

### Background
The seminal work in this area is the "hashing-based estimator" (HBE) framework by Charikar and Siminelakis at FOCS'17, which at a high level computes the kernel sum by (1) hashing all of the points in the dataset into LSH buckets, (2) hashing the query into the same buckets, (3) computing the kernel values for all values in the buckets where the query lands, and (4) repeating this process several times to refine the estimate. The intuition is that since LSH sends nearby points to the same buckets, and kernel values are large only for nearby points, we can get most of the mass in the kernel sum by sampling from the LSH buckets.

There have been several improvements to the original HBE work, initially focused on improving the space requirements by sampling ("Space and time efficient KDE" at NeurIPS'19) and getting the scheme to work in practice ("Rehashing kernel evaluation" at ICML'19), with a later paper that extends the scheme to more general classes of kernels ("Multi-resolution hashing" at FOCS'20). One unavoidable source of inefficiency with the HBE idea is that for radial kernels, we may have points with similar kernel contributions go to different LSH buckets (e.g., because they are on opposite sides of the query - imagine a situation where the query is the midpoint between two data clusters). This leads to redundant kernel value calculations. The most recent progress on this method (Charikar 2020), addresses this issue by counting the number of points in spherical shells around the query. This newer method (1) uniformly downsamples the dataset into subsets of exponentially-smaller sizes - one for each spherical shell radius, (2) creates an LSH index for each subset, and (3) at query-time, looks through each bucket to find the number of points in the shell radius.

### Contribution of this paper
The critical design choices in the KDE algorithm by Charikar et. al. are the partitioning + subsampling algorithm and the construction of the LSH index for each subset. Charikar et. al. consider two LSHs - a symmetric LSH which yields $\mu^{-0.25}$ query time and a data-dependent LSH which yields $\mu^{-0.173}$ query time but is considerably harder to analyze.

This paper modifies the algorithm by using an asymmetric LSH function, which induces a space-vs-query time tradeoff. When the space complexity is set to be the same as previous algorithms, this paper has $\mu^{-0.1865}$ query time. When the space is allowed to increase dramatically (to $\mu^{-4.15}$!), this paper has $\mu^{-0.05}$ query time.

### Strengths
1. The problem is important. Kernel sum estimation is intimately related to important practical applications such as efficient attention design, partition function estimation, and density estimation For example, given an improved algorithm for KDE one can immediately obtain an improved algorithm for transformer inference.
2. It is an interesting that the well-known space-time tradeoffs in (Andoni 2017) result in a similar tradeoff for KDE

### Weaknesses
1. The space complexity of $\mu^{4.15}$ is extremely high. To contextualize this number, the main contribution of *"Space and Time Efficient Kernel Density Estimation in High Dimensions"* in NeurIPS 2019 was to reduce the space complexity of HBE from $\mu^{-1.5}$ to $\mu^{-0.5}$. 
2. This paper is a reasonably-interesting composition of two well-known techniques - the KDE algorithm from Charikar et. al. and the space-optimal LSHs from Andoni et. al. It would significantly add to the theory value if there were some modification / improvement to either method. 
3. The presentation of the algorithm could be significantly improved. Right now, the paper seems to present two separate algorithms, but these are really just hyperparameter configurations of the "Asymmetric LSH + Charikar2020" idea. It might be better to introduce the tradeoff first, and then show how the tradeoff can reproduce algorithms. It would also be very helpful to have diagrams showing how the algorithm works (e.g., showing spherical annuli with various downsampling rates). The presentation of the theorems / proofs can also be cleaned up a lot, since in many cases the analysis is inherited from Charikar 2020 and/or Andoni 2017.
4. Many of the results in the paper are obtained via numerical evaluations. While this does not invalidate the results, it does make the analysis less elegant / insightful and more complicated.

### Questions
Aside from addressing the weaknesses, I would like to understand:
1. Have you tried any strategies to mitigate the space complexity? It seems like this comes pretty directly from the near-neighbor space requirements of the asymmetric LSH that is used. However, the KDE problem is subtly different because we can typically use sampling to reduce the number of points that we store in each LSH table, at the cost of a constant factor increase to the estimator variance (this is not possible for near-neighbor, since there we must return a specific point). I wonder whether you could improve the space tradeoff by doing more sampling in each LSH table.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper presents a theoretical analysis of the space–time tradeoff for kernel density estimation (KDE) using hashing-based data structures. The work builds upon the framework of Charikar et al. (FOCS 2020), which reduced KDE to a density-constrained approximate nearest neighbor (ANN) problem. The authors propose replacing symmetric LSH with asymmetric LSH (Andoni et al., 2017) that was proposed to control the space-time trade-off of ANN to obtain the space-time trade-off for KDE, improving query exponents (e.g., $1/\mu^{0.05}$) at the cost of significantly increased space (e.g., $1/\mu^{4.15}$).

### Strengths
- Provides a clean integration of asymmetric LSH into the KDE framework of Charikar et al. (2020).

- Theoretical exposition follows the structure of the prior work, and the derivations appear internally consistent.

- The paper establishes a general tradeoff function ξ(δ) between query time and space, which could be useful for benchmarking future approaches.

### Weaknesses
**W1. Marginal Novelty / Lack of Theoretical Depth**

The main novelty lies in reusing the well-known data-independent asymmetric LSH time–space tradeoff (Equation 5) and substituting it into the existing reduction by Charikar et al. (2020). The result primarily reproduces a direct consequence of known ANN theory, with no fundamentally new KDE insights or analysis beyond reparameterization. When evaluating the paper as a theoretical work, I feel that it reads as a straightforward application rather than a conceptual advancement.

The improvement in query exponent (from $1/\mu^{0.173}$
 to 
$1/\mu^{0.05}$) comes at the cost of extremely high space ( $1/\mu^{4.15}$), which is impractical and makes the improvement largely theoretical. In the balanced regime (δ=0), the improvement over Charikar et al. (2020) is only marginal (from 0.173 to 0.1865) with no empirical validation or deeper interpretive insight.

**W2. Unclear Role of Constants $c_0, c_1$**

The paper restricts analysis to levels $j \in [c_0 J, (1- c_1) J]$ but provides no intuition for why these constants are necessary or how they influence the resulting tradeoff (L387–L390). This omission obscures the motivation for the “nice range” assumption and whether it affects the theoretical results.

**W3. Heavy Dependence on Prior Work (Charikar et al. 2020)**

The exposition assumes the reader has read and understood Charikar et al. (2020). Several definitions, assumptions, and remarks (e.g., Assumption 1, Remark 3, and various sampling arguments) are reused verbatim or near-verbatim, making this paper hard to parse independently. Some text sections (e.g., L052–053, L249–252) are almost identical to those in Charikar et al., suggesting insufficient self-containment and a lack of clarity for new readers.

**W4. Notation and Presentation Issues**

The paper introduces new notation in Page 3 (e.g., distance scales $x_j$ such that $\mu^{x_j} \approx 2^{-j}$) but then reverts to Charikar’s notation later in Section 3. The inconsistent reuse of notation and symbols significantly reduces readability and makes it difficult to follow how variables such as $x_j, y, J$ interact across sections.

**Typos:**

- L305, 2^{-J + 1} should be 2^{-j + 1}

- strucutre

- Recoveryis

### Questions
Could you please address the raised weakness above and the questions below?

**Q1. Under what assumptions does $K(p, q) = \mu^{\|p - q\|}$ hold (L107)?**

If this is derived from the Gaussian kernel, then $\mu = e^{-2\sigma^2}$. How can the parameter $\sigma$  of the kernel function depend on the approximation or computed value of $\mu$? Please clarify this mapping.

**Q2. Why is it necessary to retrieve all points at distance scale $x$ (L127, Remark 3, Definition 11)?**

Charikar et al. only sample points and estimate contributions probabilistically, whereas exact recovery of all points may require time proportional to output size $|L_j \bigcup P_j|$, which undermines the sublinear query claim.

**Q3. What are the roles of $c_0, c_1$ in restricting the range $j \in [c_0 J, (1- c_1) J]$?**

If they only simplify asymptotics, please justify why results do not depend critically on these constants.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper studies the following problem.
Given a point set $P$ in $\mathbb{R}^d$ and a query $q$ in $\mathbb{R}^d$, we would like to compute the kernel density estimation $(1/\lvert P \rvert)\sum_{p\in P} \exp(-\lVert p-q \rVert^2)$.
However, the exact computation requires a linear scan over the entire dataset which takes $n$ time and hence is prohibitive.
Therefore, the question is if we allow approximation up to a $1\pm \epsilon$ multiplicative factor, can we reduce the query time?
Previous result Charikar et al. (2020) showed that one can construct a data structure that its query time is $1/\mu^{0.173+o(1)}$ and its space complexity is $1/\mu^{1+o(1)}$ where $\mu$ is the minimum value of the ground truth kernel density estimation we are interested in. 
The authors provide a novel construction of data structures that allows a tradeoff between query time and space complexity.
More precisely, the authors construct a data structure that allows the tradeoff between the setup of query time being $1/\mu^{0.05+o(1)}$ and space complexity being $1/\mu^{4.15+o(1)}$ and the setup of query time being $1/\mu^{0.1865+o(1)}$ and space complexity being $1/\mu^{1+o(1)}$.

The main idea is to use locality sensitive hashing (LSH) and approximate nearest neighbor search (ANN).
First, one can set $J = \log (1/\mu)$ and construct $J$ sets that each set is a sampled subset of $P$ at different rates $p_j$ for $j = 1,2,\dots,J$.
For each sampled subset $P_j$, maintain a data structure that uses LSH and ANN to allow faster query time for returning points that are within an annulus of $q$, $L_j$.
Finally, return the sum $\sum_{j = 1}^J \sum_{p \in L_j} (1/p_j) e^{-\lVert p-q \rVert^2}$.

### Strengths
- The presentation is generally clear.
The authors manage to explain the problem definition and the approach clearly. 
Readers of different backgrounds should be able to understand the idea of the result.

- The result shows an interesting spectrum on the tradeoff between query time and space complexity. 
I believe the result can provide some insights in the field.

### Weaknesses
- Though the general presentation is good, the authors may want to provide more explanation on the novelties of the approach and result.
The authors attempted to point out the novelties in the technique overview such as the use of asymmetric ANN.
More highlights on the difference between the previous approach and the current approach helps readers to fully grasp the key technical improvement.

### Questions
- Section 1.1: When discussing the results between the previous work and the current work, it may be helpful to make a table to show the comparison clearly.

- Line 258: Is $X$ $\mathbb{R}^d$?

- What is the challenge of extending the result for other kernels?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes a data structure that improves query time at the expense of higher space complexity than existing methods. The proposed techniques provide known query-time vs. space trade-offs for KDE. The query time improves the best-known non-adaptive KDE bound and nearly matches the best-known bound.

### Strengths
S1. This paper presents strong theoretical contributions to a significant problem in theoretical ML.

S2. This paper introduces novel and sound techniques that improve upon existing methods.

S3. Although this paper contains dense mathematical results, its organization is clear and can be followed without delving into mathematical details.

### Weaknesses
W1. This paper is purely theoretical, with no empirical study. I suspect whether such a contribution is of enough interest to the ICLR community.

W2. Although the analysis procedure is claimed to be simpler, the query time does not match the best-known one ($1/\mu^{0.173}$ vs. $1/\mu^{0.1865}$) with the same space complexity.

### Questions
Q1. I am not sure which kernel functions are supported by the proposed technique. Gaussian kernel only or general kernels that can be reduced to LSH and ANN computations?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4
