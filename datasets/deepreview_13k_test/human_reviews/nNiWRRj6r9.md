# ONLINE EPSILON NET & PIERCING SET FOR GEOMETRIC CONCEPTS

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
\emph{VC-dimension} (Vapnik and Chervonenkis, 1971) and \emph{$\varepsilon$-nets} (Haussler and Welzl, 1987) are key concepts in Statistical Learning Theory. Intuitively, \emph{VC-dimension} is a measure of the size of a class of sets. The famous \emph{$\varepsilon$-net theorem}, a fundamental result in Discrete Geometry, asserts that if the VC-dimension of a set system is bounded, then a small sample exists that intersects all sufficiently large sets.
    
    In online learning scenarios where data arrives sequentially, the VC-dimension helps to bound the complexity of the set system, and $\varepsilon$-nets ensure the selection of a small representative set. This sampling framework is crucial in various domains, including spatial data analysis, motion planning in dynamic environments, optimization of sensor networks, and feature extraction in computer vision, among others. Motivated by these applications, we study the \emph{online $\varepsilon$-net} problem for geometric concepts with bounded VC-dimension. While the offline version of this problem has been extensively studied, surprisingly, there are no known theoretical results for the online version to date. We present the first deterministic online algorithm with an optimal competitive ratio for intervals in $\mathbb{R}$. Next, we give a randomized online algorithm with a near-optimal competitive ratio for axis-aligned boxes in $\mathbb{R}^d$, for $d\le 3$. Furthermore, we introduce a novel technique to analyze similar-sized objects of constant description complexity in $\mathbb{R}^d$, which may be of independent interest. 
    
    Next, we focus on the continuous version of this problem (called \emph{online piercing set}), where ranges of the set system are geometric concepts in $\mathbb{R}^d$ arriving in an online manner, but the universe is the entire ambient space, and the objective is to choose a small sample that intersects all the ranges. Although \emph{online piercing set} is a very well-studied problem in the literature, to our surprise, very few works have addressed generic geometric concepts without any assumption about the sizes. We advance this field by proposing asymptotically optimal competitive deterministic algorithms for boxes and ellipsoids in $\mathbb{R}^d$, for any $d\in\mathbb{N}$.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This is a theoretical paper that gives algorithms to construct epsilon nets and piercing sets for geometric objects that appear in an online setting. The size of the nets and piercing sets are tight in terms of the competitive ratio i.e. the largest ratio of the size of the net returned by the algorithm to the optimal size of the net at any point in the online setting.

### Strengths
1) Epsilon nets are very important in the field of computational geometry and learning theory. It appears that very less work is done regarding construction of epsilon nets/piercing nets when the objects appear in an online manner. Hence the paper will be of interest to the community.

2) I tried to check the proofs in the main part of the paper to the best of my ability and the paper appears to be sound.

3) The techniques/insights described here might be useful to construct epsilon nets for other objects also. I appreciate the use of figures to convey certain ideas.

### Weaknesses
1) The writing and the presentation of the paper is very weak. Parts of the paper are very abstract. Certain words and concepts appear earlier and are explained later and that too in abstract manner. The writing is repetitive also. Here I give few specific examples:

i) In the Notation and Preliminaries section there is hardly any difference in the definition of online epsilon net and online piercing set. 

ii) Terms like ranges, range space are used in the introduction section without properly defining them.

iii) You can give simple examples for what can be $\mathcal{X}, \mathcal {R}$ etc. in the introduction itself. The final results can be abstract but at least some examples might help understand the terminology better.

iv) It would be better to bring the pseudo code of the algorithms in the main paper

The writing and presentation need to be improved a lot.  In the current state the paper will not be accessible to a broad audience.

2) It is not clear from the paper what are the technical challenges faced to maintain an epsilon net in the online setting. Please clarify as it will help highlight the novelty as to why the techniques of constructing the epsilon net differ from the offline case. For this you can add a small paragraph has to how epsilon nets can be constructed for similar object in the offline setting and why it is difficult to modify such algorithms for the online setting.

### Questions
See Weaknesses and address them

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper tackles the problems of online $\epsilon$-nets and online piercing sets for geometric concepts, specifically focusing on bounded VC-dimension and various types of geometric shapes such as intervals, axis-aligned boxes, and ellipsoids. The authors introduce several new algorithms that achieve optimal or near-optimal competitive ratios for these problems, marking the first known results in several of these areas.

### Strengths
1. This paper is one of the first to tackle online $\epsilon$-net and piercing set problems with a formalized approach, filling a noticeable gap in the existing literature.
2. The work provides clear proofs and establishes bounds on the competitive ratios of the proposed algorithms.

### Weaknesses
1. This paper mainly focuses on lower-dimensional cases (one-dimensional intervals and boxes in up to three dimensions). Many practical problems exist in higher dimensions, and the algorithms’ performance and applicability might not extend well to such cases.

### Questions
1. Can the authors extend their algorithms to work efficiently in higher dimensions, and if so, what are the expected challenges and potential solutions?
2. It would be beneficial if the authors could compare the performance of their online algorithms against existing offline methods to highlight the trade-offs and benefits more clearly.

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
The paper studies the online $\epsilon$-net problem and the online piercing set problem for geometrical objects. 

For the online $\epsilon$-net problem, the paper considers the range space of intervals in $\mathbb{R}^1$ and axis-aligned retangles in $\mathbb{R}^2$ and $\mathbb{R}^3$. For intervals, the paper gives an algorithm with asymptotically tight competitive ratio $O(\log(1/\epsilon))$. For axis-aligned rectangles, the paper gives an algorithm with nearly asymptotically tight competitive ratios ($O(\log(1/\epsilon))$ in $\mathbb{R}^2$ and $O(\log^3(1/\epsilon))$ in $\mathbb{R}^3$). 

For the online piercing set problem, the paper considers the range spae of axis-aligned boxes, ellipsoids, and fat objects in $\mathbb{R}^d$ for general $d$. For axis-aligned boxes and ellipsoids, the paper gives an algorithm with an asymptotically tight competitive ratio $O(\log(M))$, where $M$ is the length range of the geometrical objects. For $\alpha$-fat objects, the paper gives an algorithm slightly improving the existing $ O\left(\left(\frac{2}{\alpha}+2\right)^d \log M\right)$ competitive ratio to $O\left(\left(\frac{2}{\alpha}+\frac{7}{8}\right)^d \log M\right)$ for $\alpha \in [1/2,1]$

### Strengths
The paper studies fundamental problems (online eps-net and online piercing set). The problem settings considered(range spaces of intervals, rectangles, ellipsoids, and fat-objects) are interesting and natural. The paper makes good contributions on these problems. In some problems, the paper achieves asymptotically optimal competitive ratio. 

Overall, I believe the paper makes good contributions to a natural problem. Its contributions are worthy to publish.

### Weaknesses
The main weakness lies in the writing of the paper. The writing lacks rigor and causes distraction. Many concepts are not clearly defined. Some concepts are not clearly utilized. The connection between the existing results and this paper's result is not clearly stated. I have detailed these issues scifically in the Questions section below.

Overall, I believe the paper has the potential to be decent-to-good, provided that its writing is polished.

### Questions
1. The paper begins with an extensive discussion on VC-dimension; however, it does not utilize this concept in any of the subsequent analyses. All results depend solely on the Euclidean dimension, making the discussion of VC-dimension somewhat distracting for the reader. I recommend either removing this discusstion entirely or clearly articulating the relationship between the results and VC-dimension.

2. The connection between the paper's results and existing literature is not sufficiently clarified.

2.1. The authors claim that their results are asymptotically optimal. Could you specify which variable you are considering for the asymptotic limit?

2.2. The authors reference several existing lower bounds, some expressed in the forms $\log(n)$ and $\log(m)$. These bounds do not appear directly comparable to the results presented in this paper. Please elaborate on the relationships, similarities, and differences between these bounds and yours.

2.3. In line 132, the authors introduce a bound of the form $\log(M)$ without defining $M$, immediately following the introduction of the variable $m$. This lack of definition creates confusion, particularly regarding the similarity between uppercase $M$ and lowercase $m$. I suggest defining $M$ and potentially selecting a different variable to avoid this ambiguity.

3. Several terms and concepts lack formal definitions:

3.1. I recommend that the authors formally define $\epsilon$-nets in Section 2.

3.2. What is the definition of the hitting set problem? The authors frequently mention it and compare it to the piercing set problem without providing a clear definition. Since the paper does not focus on the hitting set problem, I suggest removing this discussion to maintain focus and coherence.

3.3. In line 42, the definition of a range space is missing.

3.4. The dual range space is introduced in line 75, but its definition is not provided until the following page.

3.5. The parameter $\alpha$ related to an object is not defined until later in the text (line 93).

3.6. In line 130 (and many other places ao, line 130 is just an example), the authors use the variables $P$ and $X$ interchangeably without defining $P$.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper addresses the online ε-net and online piercing set problems for geometric concepts in computational geometry.  Specifically, it proposes  randomized algorithms for axis-aligned boxes in two- and three-dimensional spaces, achieving near-optimal competitive ratios, and  online algorithms for the piercing set problem  for more complex structures like ellipsoids and axis-aligned rectangles, presenting competitive ratios.

### Strengths
1. Novelty in Online Setup: The transition from offline to online algorithms for ε-nets and piercing sets addresses a gap in existing research. This online focus adds significant value to applications in dynamic learning environments.
2. Comprehensive Theoretical Analysis: Each algorithm is rigorously analyzed for its competitive ratio, demonstrating tight bounds for several common geometric configurations.

### Weaknesses
1. The competitive ratios for higher dimensions grow rapidly, limiting the algorithms’ effectiveness in high-dimensional applications (e.g., for dimensions $d \ge 4$). This can restrict practical use in real-world, high-dimensional datasets.
2. The results are mainly for regular, axis-aligned geometric objects (boxes, ellipsoids), yet real-world applications often involve irregular or rotated shapes. Without additional adaptability, the proposed algorithms would struggle in cases where piercing sets are needed for non-standard objects.
3. In the randomized approach for axis-aligned rectangles, a binary search tree is constructed over a subset of points, dividing intervals repeatedly until only ε-heavy regions remain. While theoretically sound, constructing and updating such a binary tree might be impractical in real-time applications due to overhead. A practical complexity analysis or alternative for dynamic binary tree maintenance would make the algorithm more viable.
4. The paper is heavily theoretical, with limited discussion of empirical validation. Experiments comparing the proposed algorithms' performance to existing methods would strengthen the practical implications.
5. Overall, I think this is a good paper, but might not be quite suitable for ICLR. Maybe the computational geometry or theory conferences, like SoCG, are more appropriate.

### Questions
1. While the theoretical competitive ratios are well-established, there is little discussion on the real-world computational cost. Does the approach become impractical under frequent updates, and if so, what modifications could reduce the computational load?
2. The paper does not provide a sensitivity analysis on the effect of different random sample sizes P in Section 3.2, which could significantly affect performance. Without such an analysis, it’s unclear whether the algorithm can reliably achieve near-optimal competitive ratios across different datasets and problem scales. How robust is the algorithm for online ε-nets under varying sample sizes?

### Soundness
3

### Presentation
3

### Contribution
3
