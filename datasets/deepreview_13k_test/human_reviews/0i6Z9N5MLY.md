# Variance Reduced Halpern Iteration for Finite-Sum Monotone Inclusions

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Machine learning approaches relying on such criteria as adversarial robustness or multi-agent settings have raised the need for solving game-theoretic equilibrium problems. Of particular relevance to these applications are methods targeting finite-sum structure, which generically arises in empirical variants of learning problems in these contexts. Further, methods with computable approximation errors are highly desirable, as they provide verifiable exit criteria. Motivated by these applications, we study finite-sum monotone inclusion problems, which model broad classes of equilibrium problems. Our main contributions are variants of the classical Halpern iteration that employ variance reduction to obtain improved complexity guarantees in which $n$ component operators in the finite sum are ``on average'' either cocoercive or Lipschitz continuous and monotone, with parameter $L$. The resulting oracle complexity of our methods, which provide guarantees for the last iterate and for a (computable) operator norm residual, is $\widetilde{\mathcal{O}}( n + \sqrt{n}L\varepsilon^{-1})$, which improves upon existing methods by a factor up to $\sqrt{n}$. This constitutes the first variance reduction-type result for general finite-sum monotone inclusions and for more specific problems such as convex-concave optimization when operator norm residual is the optimality measure. We further argue that, up to poly-logarithmic factors, this complexity is unimprovable in the monotone Lipschitz setting; i.e., the provided result is near-optimal.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper clearly presents two algorithms for monotone-inclusion problems in different conditions with the new analysis that improves oracle complexity.  In the cocoercive setting, the paper uses a single loop Halpern iteration with variance reduction to achieve the oracle complexity of O(n+ \sqrt{n}L/\epsion). In the Lipschitz case, the author uses the inexact Halpern iteration and computes the resolvent approximation by VR-FoRB method. It achieves the oracle complexity of $O(n+\sqrt{n}L/\mu)$.

### Strengths
1. The paper proposed two algorithms in the cocoercive case and the monotone Lipschitz case, respectively. 
2. The new algorithms improve oracle complexity by a factor of $\sqrt{n}$ compared with existing methods on some conditions.
3. Numerical experiments are presented to further show the improvement of the new algorithms.
4. The paper is clearly written and easy to follow.

### Weaknesses
1. Some concepts. E.g., monotonicity, maximal monotone, are not explicitly defined in the paper, which slightly impairs the completeness of the paper.
2. Both Algorithms 1 and 3 are variants of existing algorithms. The Algorithm 1 is a simpler version of Cai et al. (2022a), while there is not enough comparison to present the novelty and advantage of the new algorithm. The Algorithm 2 is a combination of inexact Halpern iteration and VR-FoRB (Alacaoglu & Malitsky (2022)), which still doesn’t present much novelty. Although there are improvements on the oracle complexity bound, it seems that they mainly come from the analysis side and assumptions side instead of the algorithm side. Also, it would be good to discuss whether the improvements stem from specific assumptions.
3. The new oracle complexity bound has an additional term of $n$. It may be beneficial to discuss why the new analysis introducing this term.

### Questions
1. Can the author propose a framework to unify the two algorithms? Two different algorithms for two different conditions are not concise enough.
2. Can the author describe the experiments more clearly? Like providing more details of matrix games and other tasks?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses game-theoretic equilibrium problems pertinent to adversarial robustness and multi-agent settings, by studying finite-sum monotone inclusion problems. The authors propose variants of the Halpern iteration with variance reduction, yielding improved complexity guarantees for problems where component operators are cocoercive or Lipschitz continuous and monotone on average.

### Strengths
In the paper's context, the authors claim an oracle complexity of \\( \mathcal{O}(n + \sqrt{n}L/\varepsilon) \\) under their studied conditions, providing a considerable (theoretical) improvement over prior methodologies.

### Weaknesses
*Due to confusing presentation, there is doubt on whether the improvements stem from an innovative analysis approach, or is predominantly artifacts of the specific assumptions employed in their  (restricted) settings.*

**Assumptions and Implications:**
- Considering the decomposition, $\mathbb{E}_{q \sim Q} \left[ \| F_q(u) - F_q(v) \|^2 \right] = \text{Var}_{q \sim Q} \left[ \| F_q(u) - F_q(v) \| \right] + \left( \mathbb{E}_{q \sim Q} \left[ \| F_q(u) - F_q(v) \| \right] \right)^2$, assumptions (particularly 2 and 3) concerning bounded second moment warrant a deeper discussion on their necessity -- *particularly since variance reduction is typically sought in scenarios with large or unbounded variance.* Could the authors provide a discussion of the implications of these assumptions, and whether these could be relaxed without compromising the results? 
- The paper suggests that the bounded second moment assumption holds as standard for analyzing variance-reduced algorithms, referencing works such as (Palaniappan & Bach (2016)); (Carmon et al. (2019)); and (Alacaoglu & Malitsky (2022)). While all referenced works are implied to operate under similar conditions, however, it is unspecified whether those works inherently assume boundedness, or *derive it as a result of variance reduction*. It's unclear given the different problem settings, and if they indeed support such an assumption as a given, or if they use variance reduction techniques to bound the second moment, which are significant distinctions. 
- Therefore, claiming that such assumptions are standard in the context of variance-reduced algorithms might be misleading. A deeper analysis of the references in question, and how they relate to the specific assumptions made in this paper would be beneficial.

**Presentation and Exposition:**
- The paper's presentation of the problem setting, such as "graph of maximal monotone operators" in Section 2 is unclear. More precise definitions, without obscured notations, would greatly aid in comprehension.
- The discussion post Lemma 3.1 could benefit from elaboration on what is meant by "going beyond" the deterministic setting. Clarification on the nature and implications of the "more complicated induction-argument" that is avoided may also add to the reader's understanding.
- A structured overview would facilitate a more transparent evaluation of the work's context and contributions. To aid in the accurate evaluation of the paper's contributions, a side-by-side comparison with the assumptions, techniques, and results of existing work would be invaluable. A table format could be the most effective way to present this information, providing a quick reference to understand the advancements made. Could the authors provide a table comparing this work to the literature regarding key assumptions and results, such as variance bounds, Lipschitz conditions, sample complexity, and optimality measures?

**Numerical Experiments:**
- The numerical experiments section requires a clearer articulation of its goals and outcomes. The interpretation of the numerical experiments, particularly in Section 5, Figure 1, is not immediately apparent. Could the authors elucidate the objective of these experiments and how they substantiate the paper's claims?

**Clarification on Algorithms:**
- Considering the significant overlap with prior works on Algorithms 1, 2 and 3, would it be possible for the authors to detail the specific analysis differences and their implications? A tabulated summary including convergence rates, settings (deterministic versus stochastic), and the role of approximation errors would be highly informative. This should include the pivotal details, ensuring that all terms are precisely defined. It would also clarify the stochastic elements in the context of the algorithms proposed and how these factors are managed or analyzed differently from the literature. 

**Originality:**
- The adaptation of Algorithms 1, 2, and 3 from existing literature and the application of martingale analysis proofs should be accompanied by a clear indication of the novel contributions of this work. Specifically, what is the new insight and proof technique that lead to the reported improvement in sample complexity? Currently, it seems to be mere artifact of the specific assumptions for this problem setting.

### Questions
Kindly address the points raised above, which are briefly summarized here:
1. **Clarity of Presentation:** The exposition is particularly convoluted and indirect. It could be re-structured for better comprehension. 

2. **Comparison with Existing Literature:** The paper should offer a clearer and more direct comparison with existing works. Such a comparison would be more insightful if it included a discussion on how the assumptions differ from those in the literature and the impact of these differences on the results. Additionally, the citations of relevant literature regarding expected Lipschitz continuity and variance reduction may require a review to ensure accurate representation. *The paper should address whether those cited works indeed operate under analogous assumptions or if there are misalignments which may affect the interpretation of the current work's contributions.*

3. **Assumptions and Implications:** The paper would benefit from a critical examination of its assumptions, particularly Assumptions 2 and 3. Since the paper aims to address variance reduction, *assuming bounded second moments could be contradictory.* It's crucial to investigate whether they overly constrain the scenarios the variance reduction aims to address. 

4. **Proof Methodology:** Besides the strict assumptions, it is not immediately clear what novel proof techniques or insights contribute to the improved sample complexity bound. A more explicit articulation of these novel aspects would help delineate the paper's contributions from existing work.

*Overall, I encourage the authors to meticulously delineate the parallels and distinctions, between the analysis, results, & proofs presented in this paper and those in prior studies. Clarifying this may enhance the perceived value of the work.*

$\textbf{[Update:]}$ After a thorough reflection on the merits and limitations, I have decided to bump up my score to a **6**. Still, I encourage the authors to refine their manuscript, including the nuanced discussions on $L$, spectral-norm & other dependencies, and the tail-bounds. (Ideally, mention important caveats in the early sections.)

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies finite-sum monotone inclusion problems. When assuming the operator is co-coercive, the paper proposes a direct single-loop algorithm combining PAGE and Halpern iteration that achieves $O(n+\sqrt{n}\epsilon^{-1})$ convergence rate. When assuming the operator is monotone and Lipschitz, the paper proposes an indirect inexact proximal point-based method with VR-FoRB as the inner-problem solver that also achieves $O(n+\sqrt{n}\epsilon^{-1})$ convergence rate. Both convergence rates are last-iterate guarantees on the operator norm.

### Strengths
The paper is well-written and explains every detail of the algorithms and their contributions. The discussions and comparisons to previous works clearly reflect their differences and improvements. Although the algorithms and techniques are based on previous works, the obtained last-iterate guarantees on the operator norm for finite-sum monotone inclusion problems are new in the related literature.

### Weaknesses
1. PAGE was originally designed for nonconvex minimization problems and SVRG/SAGA is a common choice for convex problems. Although the problem to be solved is monotone, Algorithm 1 chooses PAGE as the base algorithm. Could the authors explain why? What happens if SVRG is used?

2. I don't see any dependence and requirement on $L_F$ for both Algorithms 1 and 2. Is the assumption that $F$ is $L_F$-Lipschitz used anywhere in the analysis? Why is it required other than allowing easier comparisons with existing results? I also think the discussions on the relationship among $L_F$, $L$, and $L_Q$ should be clearly stated in the paper instead of just referring to existing works. It would be better if the paper just had one remark saying something like $L_F\leq L\leq\sqrt{n}L_F$. This allows a better understanding of the regime when the improvements happen.

3. I think a discussion about how and where the additional logarithmic factors in the convergence results of both algorithms come from would be great. I assume they come from different sources and thus require different techniques and efforts to get rid of (if possible).

4. I still have questions on how to check the stopping criteria for the inner-problems in Algorithm 2. Is $E\Vert e_k\Vert^2$ something computable since it requires the exact solution $J_{\eta(F+G)}(u_k)$?

5. What are the examples of operators that are non-monotone but co-monotone other than $F(x)=-x$?

6. In Figure 1(b), EAG and Algorithm 2 tend to have lots of oscillations but Algorithm 1 does not. Some explanations and discussions on this might be good.

7. (Minor) Although the results in the paper are new, I am not so surprised by their algorithms and technical analyses given the rich literature on the related topics. It seems standard that the deterministic version of some problem is first studied and then variance reduction can be applied to improve the rates for its finite-sum extension. The results in this paper are thus expected by combining existing knowledge, especially given its infinite-sum version in (Cai, 2022a). Another small concern is about the practical use of variance reduction methods. Even though they offer plenty of benefits in the theoretical analysis, there are works that report these methods do not have good performances in practice as the theory suggests, e.g., [arXiv:1812.04529]. There is even no official support for variance reduction methods in the popularly used machine learning packages like PyTorch and TensorFlow despite rich literature showing their theoretical advantages on both convex and nonconvex problems.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
