# Finding Equilibria in Bilinear Zero-sum Games via a Convexity-based Approach

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
We focus on the design of algorithms for finding equilibria in 2-player zero-sum games. Although it is well known that such problems can be solved by a single linear program, there has been a surge of interest in recent years, for simpler algorithms, motivated in part by applications in machine learning. Our work proposes such a method, inspired by the observation that the duality gap (a standard metric for evaluating convergence in general min-max optimization problems) is a convex function for the case of bilinear zero-sum games. To this end, we analyze a descent-based approach, variants of which have also been used as a subroutine in a series of algorithms for approximating Nash equilibria in general non-zero-sum games.  
In particular, we analyze a steepest descent approach, by finding the direction that minimises the directional derivative of the duality gap function and move towards that. Our main theoretical result is that the derived algorithms achieve a geometric decrease in the duality gap and improved complexity bounds until we reach an approximate equilibrium. Finally, we complement this with an experimental evaluation. Our findings reveal that for some classes of zero-sum games, the running time of our method is comparable with standard LP solvers, even with thousands of available strategies per player.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors bimatrix zero-sum games and provide a convex approach to provide a gradient-descent algorithm on the duality gap function (as a minmization problem, instead of minmax) and show that their method converges at rate $O(1/\varepsilon\log(1/\varepsilon))$ to a NE of the game.

### Strengths
1) The paper is generally well written and the methods are clearly explained.

2) The results are presented in an intuitive manner and the experiments are conducted that show the efficacy of their theoretical results.

### Weaknesses
1) The contribution of this paper with respect to the novelty (technically) and the problem they are trying to solve could be better explained.

2) For two-player zero-sum games which is the setting studied here it is well known from the equivalence to Linear Programs that one can obtain $O(poly(size).polylog(1/\varepsilon))$ convergence to the Nash equilibrium, which is polynomial in the size of the representation of the LP.  

3) An important point to note in the literature is that the algorithms for which last-iterate convergence is studied are predominantly *no-regret* (online) algorithms, which have numerous consquences even beyond two-player zero-sum games, for instance convergence to CE/CCE's in multiplayer games etc. Hence the challenge is obtain last-iterate for such algorithms, see for example [Golowich et al., 2020].

4) For example a direction that would be interesting (even empirically) is to investigate the time to converge to NE for very large zero-sum games and compare to algorithms such as OGDA, OMWU etc.

### Questions
Please see weaknesses

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
This paper studies the problem of approximating the Nash equilibrium in bilinear zero-sum games. In particular, the proposed algorithm applies a steepest descent approach, moving in the direction that minimizes the directional derivative of the duality gap at each timestep. Theoretically, the algorithm achieves an $O(\frac{1}{\rho\delta} log(\frac{1}{\delta}))$ iteration complexity (where $\rho$ is the $\rho$-approximation of the best response query) and converges to a $\delta$-approximate equilibrium. Moreover, the algorithm can be modified via decreasing the schedule to achieve an $O(\frac{1}{\rho} log(\frac{1}{\delta}))$ iteration complexity. Experimentally, the algorithm is shown to require increasing iterations to find an approximate equilibrium as the dimension of the game grows, though the number of iterations needed grows slowly. Moreover, comparisons in running time are made to standard solvers, showing speedups in some specific classes of games.

### Strengths
- The paper is well-written and clearly organized. The mathematical exposition is also clearly written. 
- The problem studied, namely how to speed up the solving of two-player zero-sum games, is certainly an interesting one at the interface of optimization and game theory.

### Weaknesses
 - While the running-time benefits of the algorithm seem to be discussed as the key motivation for introducing and analyzing it, the experiments do not seem extensive enough to conclude any beneficial properties of the proposed algorithm. For instance, how do other standard LP-based solver perform from the perspective of the number of iterations in Fig 1? The plots in Figs 2 and 3 also seem fairly arbitrary -- is there a theoretical analysis that can bound the percentage of strategies used as a function of $\delta$ and $\rho$? Specifically, it is unclear what the x-axis represents in Figures 2 and 3, and how the number of iterations relates to the approximation parameter $\delta$ or the best response approximation $\rho$. It would be beneficial to see a plot of the number of iterations as a function of $\delta$ for a fixed $\rho$ and vice versa.
- The claims made in the experimental section regarding comparability of performance are also not precise -- what games are the experiments in Table 1 run on? Are they specific to the class of block games described? What other classes of games are there where the algorithms proposed perform better than standard solvers? It is difficult to assess the practical impact of the proposed method without a clear understanding of the game classes where it excels and how these classes relate to real-world applications.
- Theorems 1 - 4 are known results/definitional, and thus should not be theorem statements (perhaps leaving them as observations or facts?) The inclusion of these theorems, especially without proper attribution, detracts from the perceived novelty of the work. It would be better to cite the original sources for these results and focus on the novel aspects of the proposed algorithm.
- Overall, while the exposition is nice and the proposed algorithm has its merits, the lack of depth in the analysis and the lack of clear strengths of the algorithm make it difficult to recommend acceptance.

### Questions
- In the FIND_DIRECTION algorithm, you re-solve the LP at every time step. Would it make sense to instead use a recursive approach and exploit the convexity of the duality gap to incrementally change $(x', y')$ instead? 
- Using learning algorithms with decreasing step-sizes has proven to be useful in the decentralized learning setting. Would such a modification to your algorithm provide any further improvements?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a new algorithm for finding equilibria in two-player zero-sum games by applying steepest descent to the duality gap/exploitability.  The authors show it achieves linear convergence in the exploitability/duality gap. Simulations demonstrate that its performance is comparable to the performance of LP solvers on at least some games.

### Strengths
The algorithm presented by the paper is interesting, and it is notable that linear convergence can be achieved on the exploitability. It is also interesting that the method appears to generate sparse support in practice.

### Weaknesses
While the contributions of the paper are interesting, it is not clear to me that the contributions meet the threshold for publication.

The motivation for the research itself is not very clear to me. It is interesting that the approximation algorithms for general-sum games that do descent on the max regret (and a sort of correction) can be specialized to the duality gap in the two-player zero-sum game case. As the author notes, those works focus on polytime approximation algorithms for general-sum games and don't focus on the descent case, so the work on the steepest descent on the duality gap is novel. And, of course, the setting in which it is realistic to use LPs to compute equilibria is when the matrices are relatively small.

However, for large-scale games, it is not clear how well they would work. If there is hope for it to scale to large-scale games, why restrict the matrix size to 1000, and why not compare to non LP based algorithms (e.g., regret minimization based algorithms)?  To be nitpicky, it seems misleading to mention that it scales to "thousands" of strategies, when you stop at 1000 (even though technically the statement is accurate). On the other hand, if the primary contribution is theoretical and the experimental work is just a proof of concept, the theoretical contribution, while interesting, doesn't seem to be an ICLR publication. 

A more thorough review of the literature might be useful for the paper. Additionally, the experimental section could be more thorough Some suggestions and questions are included in the following section.

### Questions
1. It seems appropriate to cite and discuss the linear convergence of EG/OG for bilinear saddle-point problems over polyhedral domains based on error bounds (e.g., *On linear convergence of iterative methods for the variational inequality problem* Tseng 1995, *Linear Last-iterate Convergence in Constrained Saddle-point Optimization* Wei et al. ). While you mention Gilpin et al.'s algorithm, the same has been known for VIP (again with a dependence on a condition number associated with the system), and so while it is true that the Cai et al. paper has the SOTA rate for condition-number-free rates for last iterate, the discussion in the optimization section is incomplete.

3. It seems that it would be good to mention explicitly the existence of a direction that minimizes the directional derivative; of course this follows from the fact that the steepest descent computation can be formulated as an LP over a compact polyhedral set. While it is mentioned in line 204 that the direction can be identified by solving an LP, it seems worth explicitly mentioning this after Theorem 4, before in Lemmas 1 and 3 you make references to a direction that minimizes the ($\rho$)-directional derivative.

4. Can you compare to work done using descent methods with the Nikaido-Isoda (NI) function? It seems to be that it might be relevant to mention in related work.

5. There should be more information on exactly what the family of block games looks like and how they are generated. It would be good to show running time results for the classes of games that the method does not do well on as well (seems odd to handpick the class for the timing results).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper designs an optimization algorithm for computing an $\delta$-approximate Nash equilibrium in two-player zero-sum games. Based on the observation that the duality gap function is convex, they develop a steepest gradient descent type algorithm that minimizes the duality gap. The algorithm needs to solve a linear program (LP) in each iteration to find the descent direction, where the LP is smaller than the generic LP that directly solves the Nash equilibrium. They give a convergence rate of $O(\frac{1}{\rho} \log \frac{1}{\delta})$ for their algorithm, where $\rho \in (0,1]$ controls the size of the LP in each iteration (when $\rho = 1$, the LP becomes the generic LP for NE). They also conduct numerical experiments on random matrices and compared their algorithms with standard LP solvers and found in certain cases; their algorithm is faster.

### Strengths
1 The idea of performing gradient descent directly on the duality gap is interesting. 
2. The presentation of the paper is clear.

### Weaknesses
1. The algorithm lacks a precise computational complexity analysis. Although a $O(\frac{1}{\rho} \log \frac{1}{\delta})$ iteration-complexity is given, this bound is not very informative: one may want to choose $\rho = 1$ to minimize the iteration number needed but it then becomes solve one LP for the NE, equivalent to the LP approach. How to choose $\rho$ is unclear since the per-iteration complexity depends on the $\rho$, which affects the size of LP. It is crucial to provide a precise time-complexity analysis of the algorithm, which helps to understand why this iterative approach by solving a series of smaller LPs might be better than solving a large LP once. The current analysis only provides an iteration complexity, but the actual runtime depends heavily on the size of the LP solved in each iteration, which is controlled by $\rho$. A more detailed analysis should consider the number of variables and constraints in the LP as a function of $\rho$ and how this impacts the overall runtime. Without this, it's difficult to assess the practical benefits of the proposed method compared to directly solving the full LP.

2. This paper focuses on the LP approach for solving NE in zero-sum games. Yet, recently, gradient-based first-order methods have become more popular for solving large-scale LPs and zero-sum games than interior-point methods. These algorithms include Extragradient, Regret Matching+ [1], and Primal-Dual Hybrid Gradient Methods [2]. These algorithms also have instance-dependent linear convergence and only require performing gradient steps in each iteration rather than solving an LP. It would be helpful to add experiments on these methods and compare their performances with the proposed algorithm on large-scale instances. The lack of comparison with these methods is a significant gap, as they represent the current state-of-the-art for solving large-scale zero-sum games. The paper should at least include a discussion of why these methods are not considered and what are the potential advantages of the proposed method over these gradient-based approaches.

Minor Comments
1. Page 3, Line 111: "The currently best rate is $O(\sqrt{1/T})$ in terms of the duality gap..." [3] has proposed an algorithm with an accelerated $O(1/T)$ convergence rate.

### Questions
See weakness for details.
1. Could you provide a time-complexity analysis of the proposed algorithm?
2. Could you add numerical experiments and compare other gradient-based algorithms?

### Soundness
3

### Presentation
3

### Contribution
2
