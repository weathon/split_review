# Coresets for $k$-mean clustering of segments

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 5, 3

## Abstract
The $k$-means of a given set $\mathcal{S}\subseteq \mathbb{R}^d$ of $n$ segments is a set $X\subseteq \mathbb{R}^d$ of $|X|=k$ centers which minimizes their sum of squared distances $D(\mathcal{S},X):=\sum_{S\in \mathcal{S}}\min_{x\in X}D(S,x)$.
Here, the distance $D(S,x)$ between a segment $S$ and a point $x$ is the integral of its distances $\int_{s\in S}\|p-x\|$ over each point on the segment.
More generally, the farthest $m$ input points (outliers) may be ignored, other distance functions may be used, such as M-estimator or non-squared, and each distance may be multiplied by a function that depends on the size of its cluster, say, to obtain balanced clustering.
For a given $\varepsilon>0$, an $\varepsilon$-coreset $C\subseteq S$ for all these problems is a weighted subset $C\subset S$, that approximates $D(S,X)$ up to $1\pm\varepsilon$ multiplicative factor for every set $X\subseteq\mathbb{R}^d$ of (possibly weighted) $k$ centers. Such a coreset enables handling streaming, big, distributed input in parallel using existing techniques.
We suggest the first coreset construction that, with high probability, returns an $\varepsilon$-coreset $C$ for \emph{any} input set $\mathcal{S}$ of segments.
For constant $k,\varepsilon$, the size of the coreset is $|C|\in O \big(\log^2(n)\big)$ and is computed in time $O(nd)$.
Experimental results and real-time video tracking application demonstrate the applicability of our algorithm, the latter demonstrates that our method supports vectorized segments.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
Assume L as a set of n segments. The goal of k-mean clustering of segments is to find a weighted set (C, w) of size |C| = k that minimize \sum_{l \in L} loss(l, (C, w)), where loss(l, (C, w)) = \int_0^1 D( l(x), (C, w) ) dx. A coreset is a weighted set of small size that can approximate the loss function of any solution. For the k-mean clustering of segments, an (epsilon, k)-coreset for a segment l is a weighted set (S, w) such that for any weighted set (C, w'), we have | loss(l, Q) - \sum_{p \in S} w(p) D(p, Q) | <= epsilon loss (l, Q). Furthermore, (S, w) is an (epsilon, k)-coreset for a set L of n segments if it is an (epsilon, k)-coreset for all l in L.
In this paper, the author propose a deterministic algorithm SEG-CORESET that returns an (epsilon, k)-coreset for a segment l. In SEG-CORESET, the coreset (S, w) consists of all the epsilon' equally spaced points on l, where epsilon' = \ceil{ 4k (20k)^{r+1} / epsilon }. Then, they propose their second algorithm CORESET that generates an (epsilon, k)-coreset (P, w) for L. P has size k' log^2m / epsilon^2 * O(d* + log (1/delta)), where d* is the VC-dimension, m = 8nk (20k)^{r+1} / epsilon, and k' \in (k+1)^{O(k)}. In the CORESET algorithm, they first apply SEG-CORESET to generate an (epsilon, k)-coreset for every l in L, and then send them as the input of Feldman's coreset generation framework.
Furthermore, they generalize their result to convex shapes, and apply experiments to evaluate the quality of their approximation compared to the other methods.

### Strengths
The authors introduce a new problem, k-mean clustering of segments, in this paper, which may have its own interest in the future. They also proposed novel algorithm that generate coreset of small size, which transfer the problem into a transitional weighted k-means problem, which makes the problem easier to solve. They provide both rigor proof and empirical evaluation for their algorithm.

### Weaknesses
 - Both the coreset size and running time has a dependence on k^k

- One of the main technical step is a black-box use of Feldman & Schulman (2012), which limits the technical contribution. The reliance on this existing algorithm, while convenient, doesn't offer much in the way of novel techniques for this specific problem. The core idea of discretizing the segments into points and then applying a known coreset construction feels somewhat incremental.

- The writing needs to be improved, especially the introduction. For instance, I find little discussion of the motivation of the problem, and the introduction for coresets seem to be very brief (and makes it hard to understand for non-experts). The motivation for this specific distance metric, which integrates the distance along the segment, is not clearly explained. It's not immediately obvious why this integrated distance is more appropriate than, say, the Hausdorff distance or a simple average distance of endpoints. The introduction lacks a clear explanation of the practical scenarios where this particular problem formulation is relevant. Furthermore, the introduction to coresets is too brief, assuming prior knowledge and failing to clearly define the problem's context for a broader audience.

### Questions
1. Is k-mean clustering of segments problem a new problem? If this problem has been studied before, please present the related research in the paper. If this problem is a new problem, please present its importance.
2. Why the idea of using equally spaced points on a segment to approximate the segment itself is novel in this paper?
3. Why do you compare your algorithm with Feldman's algorithm, which focus on another problem?

### Soundness
3

### Presentation
1

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
The paper discusses the k-means type clustering problem for line segments. The distance of a point x from a line segment S is defined as D(S, x) = \int_{s \in S} ||p-x||ds. Given this distance measure, the problem is finding k centers to minimize the sum of distances. Here, partial assignment of contiguous pieces of a line segment is allowed. The main contribution of the paper is to suggest breaking a line segment into small pieces, replacing them with weighted points, and then using the coreset construction of Feldman and Schulman to obtain a weighted set of points such that a good center set for these points will also be a good center set for the line segments. Experimental results are given with real data sets.

### Strengths
Defines a new problem and extends the notion of coreset object to this problem.

### Weaknesses
- The problem is not well-motivated before starting the technical section. Even the experimental section does not discuss why this problem is relevant in the context of the experiments performed. Why is this problem the right mathematical problem in the context of the experiments conducted?
- The results in the paper are not surprising and obtained using a straightforward application of Feldman and Schulman.

### Questions
Question related to motivation is very important and has been mentioned above.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies a coresets for a version of segment k-means. The input is a set of line segments in R^d, and the goal is to find a set of k center points in R^d, such that the sum of (squared) distance to the distance D is minimized, where for a segment s and center set C, D(s, C) := \int_0^1  \min_{c \in C} \|s(x) - c\| dx. This is different to the standard distance from a point to a segment, and it takes an integration.

The main result is a coreset of size roughly poly(1 / eps) k^k log^2 n, and a generalization to multi-dimensional shapes. The main idea is to do a uniform sample/discretization for each line segments and take the union of them, which yields a point set, then take a coreset for the point set that preserves the distance D. The first coresets for line segments are only of size poly(k), but the second step needs to use an existing algorithm from Feldman & Schulman (2012), which is of size k^k.

Experiments are conducted on both synthesized and real datasets, and compared with several baselines including a previous coreset for lines (instead of segments). The experiments indicate that the proposed algorithm outperforms the baselines.

### Strengths
- The suggested clustering problem is well motivated and has fundamental difference to a similar line segment problem

- The framework seems to be general and not restricted to segment clustering

### Weaknesses
- Both the coreset size and running time has a dependence on k^k

- One of the main technical step is a black-box use of Feldman & Schulman (2012), which limits the technical contribution

- The writing needs to be improved, especially the introduction. For instance, I find little discussion of the motivation of the problem, and the introduction for coresets seem to be very brief (and makes it hard to understand for non-experts)

### Questions
- I think the title should say “k-means” instead of “k-mean”?

- Line 40, “union over every pair (C, W)” — this is not really a union, and probably you should say “the set/collection of all pairs (C, w)”

- Line 69, you said the coreset is a weighted subset of input points — It seems the input is a set of segments, so the sentence does not make perfect sense (and one needs to explain)

- Line 127, is t a function of r? Also, why do you say big-O of t? I think you should simply say the running time is t

- Line 138 - 139, shouldn’t it be {(S \cap \beta) \mid \beta \in B} (you missed the {})?

- Line 152 - 155, here you used D( (C, w’), p ), while in your Definition 2.3 the order of the arguments are different, which is D(p, (C, w))

- Definition 2.7, I suppose S is a subset in R^d? But this is not stated

- Line 1 of Algorithm 1, you said r is as in Definition 2.3. However, that r is with respect to a function and not a universal constant. So where is such a function in the context of Algorithm 1? In hindsight, I find this is stated in line 208 - 209, so I think you need to reorganize the description

- Line 3 of Algorithm 2, I’m not sure about the comment “see Definition 2.3” — Def 2.3 is about the distance function D, but here in the algorithm it is about the coreset

- General question: how do we set the value of d^*?

- General question: you said you focus on k-means, but where does the “square” of k-means objective appear in your definitions? I only see generic definition of D, and the sum of D is not squared?

- Line 369, you said you can skip Algorithm 2 and only use Algorithm 1 + known k-means algorithm — I don’t think this theoretically works, because your objective is not point k-means (and is a sophisticated k-means over segments, even if you reduce to a subset of points for the approximation)

- Line 379, I’m not sure the way you evaluate “OPT”, at least this is misleading — isn’t it still through your coreset? In my mind one needs to use a more direct brute-force for OPT

- FIg 3, middle row, I don’t understand the plot. Why there are both vertical and horizontal segments? Shouldn’t it be a line plot?

- FIg 3, what’s “Approx”? Is this a baseline? I don’t find where it was introduced

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a new clustering problem called segment clustering, and presents a reduction from the coreset construction for this problem to that of traditional (vanilla) clustering. For constant $k$ and $\varepsilon$, the coreset size achieved is $O(\log^2(n))$, where $n$ denotes the number of segments. The paper also extends the segment clustering problem to a more general setting by transforming the dataset of $n$ segments into $n$ well-bounded convex shapes and provides an algorithm to construct a coreset.

### Strengths
The topic of constructing a coreset for clustering problems is relevant. It is good to provide an algorithm with theoretical guarantee.

### Weaknesses
The motivation of the segment clustering problem is unclear. The paper does not provide applications or real-world scenarios for the studied problem.

The result is not very strong. The paper compares to the previous discrete result given by Har-Peled, but the size bound of $O(\log^2(n))$  does not improve over the previous bound of $O(\log n / \varepsilon^2)$ by Har-Peled.

The technique is not that interesting. To my understanding, it employs uniform sampling on each segment separately to obtain an intermediate set, which is then fed into Feldman's coreset construction method.

### Questions
- What motivates your investigation of the segment clustering problem? Also, why consider this coreset definition for the segment clustering problem? There is other choice, e.g., selecting a set of segments.

- Why is the distance function between a segment and a point defined as an integral? Is there a practical reason for choosing this formulation?

- The notion of $k$-segmentation in your cited works (Jubran et al., 2021 and Rosman et al., 2014) appears to differ from the one used in this study. Could you clarify the distinctions?

Minor issues:
- **Line 58 to Line 64**: The reference to "the right figure" in the text actually corresponds to the left figure, and "the left figure" corresponds to the right figure.

- **Line 287 to Line 294**: The reference to "Top right" in the text actually corresponds to the top left figure, and "Top left" corresponds to the top right figure. The same issue occurs with "Bottom left" and "Bottom right," which are also swapped.

- **Line 828 to Line 908**: The proof of Lemma B.2 employs notations that are only defined later in Theorem B.3, making the proof difficult to follow.

- **Line 1009, Inequality (43)**: Since the function $h$ is non-decreasing, we have $\min_{x \in I\_{j-1}} h(i) - \min\_{x \in I_j} h(i) \leq 0$. Thus, the inequality as stated is incorrect.

- **Line 1047**: The expression $\text{lip}\_{p'}( D(p', \tilde{x}) + D(l(x), l(\tilde{x})))$ should be corrected to $\text{lip}_{p'}(D(p', l(\tilde{x})) + D(l(x), l(\tilde{x})))$.

- **Line 1060 to Line 1063**: Change $\text{lip}\_{p'}(D(p', l(x)))$ to $\text{lip}_{p'}(D(p', l(\tilde{x})))$.

- **Line 1163**: The function should be written as $f(x) = D(Q, l(x))$ instead of $f(i) = D(Q, l(x))$. 

These revisions would enhance the clarity and accuracy of the manuscript.

### Soundness
2

### Presentation
2

### Contribution
2
