# A Region-Shrinking-Based Acceleration for Classification-Based Derivative-Free Optimization

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 1, 3, 6

## Abstract
Derivative-free optimization algorithms play an important role in scientific and engineering design optimization problems, especially when derivative information is not accessible. In this paper, we study the framework of classification-based derivative-free optimization algorithms. By introducing a concept called hypothesis-target shattering rate, we revisit the computational complexity upper bound of this type of algorithms. Inspired by the revisited upper bound, we propose an algorithm named ``RACE-CARS'', which adds a random region-shrinking step compared with ``SRACOS'' \cite{hu2017sequential}. We further establish a theorem showing the acceleration of region-shrinking. Experiments on the synthetic functions as well as black-box tuning for language-model-as-a-service demonstrate empirically the efficiency of ``RACE-CARS''. An ablation experiment on the introduced hyperparameters is also conducted, revealing the mechanism of ``RACE-CARS'' and putting forward an empirical hyperparameter-tuning guidance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors propose a novel algorithm RACE-CARS for derivate-free global optimization that adds a mechanism of region-shrinking and theoretically show how this allows them to obtain an upper bound that is tighter than bound obtain to SRACOS algorithm.

### Strengths
Well written with rigorous theoretical analysis with experimental evaluation comparing with other approaches. 

New theoretical bounds showing superiority of the proposed algorithm compared to the baseline and new general bound on complexity under assumptions of $\eta$-shuttering.

### Weaknesses
As I understood (correct me if am wrong) SRACOS and it's bound derived without assumption of Holder continuity which is the case of Theorem 3.2 for algorithms with shrinking, while sufficient conditions for $\eta$-shuttering in Theorem 3.3. are established only for Holder continuous, which makes results a bit less general as of SRACOS. Evaluation is done only on functions that satisfy this (even if we don't know their constants) -- it is interesting to see also evaluation on $f$ that do not satisfy Holder-continuity.

Specifically, the theoretical results for RACE-CARS rely on the assumption of dimensionally local Holder continuity to establish the $\eta$-shattering property, while the SRACOS algorithm and its bounds do not require this assumption. This discrepancy in the underlying assumptions makes a direct comparison of the theoretical guarantees challenging. The paper establishes sufficient conditions for $\eta$-shattering under Holder continuity, but this limits the generality of the theoretical results. Furthermore, the experimental evaluation focuses solely on functions satisfying Holder continuity, which does not provide a comprehensive picture of the algorithm's performance under more general conditions. It would be beneficial to see how RACE-CARS performs on functions that exhibit discontinuities or other non-Holder continuous behaviors.

### Questions
Since there is Holder-continuity assumed, then say SGLD with 0-th order gradient estimator should work (theoretically) [1] -- interesting to see what authors think about that.

[1] Niladri Chatterji, Jelena Diakonikolas, Michael I Jordan, and Peter Bartlett. Langevin monte carlo without smoothness.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a classification-based derivative-free optimization algorithm. It introduces the concept of hypothesis-target shattering rate and analyzes the computational complexity upper bound for the class of algorithms. By utilizing a random region-shrinking step and the revised upper bound, a new algorithm is presented.

### Strengths
It is very hard to read the paper.

### Weaknesses
The main results (i.e., numerical experiments) of the paper are not included in the main text of the submission. Note that reviewers are not required to read the appendix. This constitutes the primary rationale for my vote to reject the paper.

Moreover, the reviewer encounters difficulty in comprehending the algorithm descriptions due to the absence of several essential sub-procedure details, rendering the paper challenging to read.

### Questions
The paper is notably challenging to comprehend.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors revisit the upper bound of the classification-based derivative-free optimization algorithm "RACOS",  and provide a query complexity analysis under the Hypothesis-Target  $\eta$-Shattering assumption.   In addition, the authors propose a sequential “RACE-CARS” method by introducing an adaptive projection sub-procedure to the previous "SRACOS" algorithm.

### Strengths
1. The classification-based derivative-free optimization is an interesting alternative compared with Bayesian optimization, and zeroth-order optimization. 

2. Empirical results on four synthetic functions and black-box tuning for language-model-as-a-service on the SST2 dataset show faster convergence compared with baselines.

### Weaknesses
1. $\textbf{Exponentially Growing Complexity Bound}$

  The query complexity in Theorem 3.1 and 3.2 exponentially grows w.r.t. the problem dimension $n$. 
For example, consider $\Omega =[-1,1]^n$  and $f(\boldsymbol{x}) = ||   \boldsymbol{x} ||_1 $, where $||  \cdot ||_1$ denote the $l_1$-norm,  then $| \Omega  _ {\epsilon}  |= \mathbb{ P } ( \Omega  _ {\epsilon}  ) \le \epsilon^n$ .  As a result, the term  $\frac{1}{| \Omega  _ {\epsilon}  |}  $ in the complexity bound  equals to  $\frac{1}{| \Omega  _ {\epsilon}  |} =  (\frac{1}{\epsilon})^n $, which grows exponentially for $\epsilon < 1$. This exponential dependence on dimension severely limits the practical applicability of the theoretical results, especially in high-dimensional optimization problems where the volume of the $\epsilon$-solution domain shrinks rapidly.

2. $\textbf{Impractical Assumptions}$

 The Hypothesis-Target  $\eta$-Shattering assumption in Definition 3.1 together with the $\gamma$-Shrinking assumption in Definition 2.3 are too strong to be practical.  The Hypothesis-Target  $\eta$-Shattering assumption requires the classifier prediction to have at least a $\eta$ overlap with the true $\epsilon$-solution domain $\Omega  _ {\epsilon}  $.   In the above example,  the size of $\Omega  _ {\epsilon}  $ decay exponentially w.r.t. the dimension $n$ , which requires the classifier to be very accurate or to have high positive prediction percentage ($h(x) =1$). This assumption is particularly problematic in high-dimensional spaces where achieving a significant overlap with a rapidly shrinking solution space becomes increasingly difficult. The classifier would need to be extremely precise, which is unlikely with limited samples.

In addition, $\gamma$-Shrinking assumption requires the region of the positive prediction to have a $\gamma$-shrinking for all $t$.  As a result, the region of the positive prediction exponentially decays w.r.t. $t$,  i.e., $\gamma^t$.  However, the  Hypothesis-Target  $\eta$-Shattering assumption requires to have at least a $\eta$ overlap with the true $\epsilon$-solution domain $\Omega  _ {\epsilon}  $,  which requires a very strong classifier for high-dimensional problems. However, how to achieve a  strong classifier with limited training samples for high-dimensional problems is challenging. The interplay between these assumptions creates a very restrictive scenario that is unlikely to hold in practice.

3. $\textbf{No Convergence Guarantee}$.

The complexity analysis can not guarantee convergence as $t$ tends to infinity.   In Theorem 3.3, the left-hand side of the inequality decays exponentially fast w.r.t $t$. However,  the RHS of the inequality can not guarantee an exponential decay. This lack of a formal convergence guarantee makes it difficult to assess the long-term behavior of the algorithm. While the analysis provides insights into the query complexity, it does not ensure that the algorithm will eventually converge to a satisfactory solution.

4. In the black-box tuning task, only the SST2 dataset is employed. The evaluation on a single dataset is not convincing enough to support the claim. The results may not generalize to other datasets or tasks, limiting the practical impact of the findings.

5. The paper is not well-organized. The experimental results are placed in the Appendix instead of the main paper.

### Questions
Q1. Could the authors please clarify the concern in the weakness section above?  

Q2.  Could the authors please compare other datasets employed in (Sun et al. 2022) besides SST2 for better evaluation?  

Q3. How to sample $(x_t, y_t) \sim \boldsymbol{Y}_t$ in Algorithm 2, what is the computational complexity or running time in this step?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new algorithm for classification-based derivative free optimization (DFO). This type of algorithm learns a classifier on the domain that predicts optimality, and alternates between updating that classifier and updating the best solution found so far. The paper has two main contributions: 1) a novel learning theoretical analysis and 2) a modification of an existing algorithm with better learning bounds achieved by shrinking the region where the best solution may be found so far. Experiments on DFO benchmarks and LLMs show that the proposed algorithm RACE-CARS improves over the modified algorithm SRACOS and CMA-ES (which is computationally expensive). Ablations of the hyperparameters are also done.

### Strengths
# Originality
The paper uses the learning theoretic concept of shattering to derive bounds for classification-based DFO, which is novel as far as I know.

# Quality
Experiments are done on a fairly large-scale LLM problem in addition to standard DFO benchmarks. Their results confirm the theoretical results in the paper and RACE-CARS is able to significantly improve over the previous classification-based DFO algorithm SRACOS. I cannot speak to the quality of the theory as I am not familiar with the relevant literature.

# Significance
Zero-order optimization is an increasingly popular area of research, as it does not require gradient computation. It is particularly useful for hyperparameter optimization, a common task that practitioners need to perform.

### Weaknesses
 # Quality
There was no clear discussion of the computational complexity of the algorithms, only an observation that CMA-ES is more expensive than SRACOS or RACE-CARS. A more detailed analysis of the time complexity, including the dependence on problem dimensionality and the number of iterations, would be beneficial. Specifically, the number of function evaluations required by each algorithm should be explicitly stated, and the cost of each function evaluation should be considered. In addition, the LLM experiment only includes part of the baselines. The absence of DE and ZO-Adam in the LLM experiments makes it difficult to assess the relative performance of RACE-CARS against a broader range of optimization techniques.

# Clarity
For clarity and readability, I think that some of the experimental results' graphs should be moved to the main paper, as they would be of more interest to practitioners. The current placement of these graphs in the supplementary material makes it harder to assess the practical significance of the results. Furthermore, the description of the region shrinking process in RACE-CARS could be more detailed. A more precise explanation of how the shrinking is implemented, and how the shrinking rate is chosen, would be helpful. Minor: Line numbers are not visible in Algorithms 1 and 2, but they are referred to on page 6.

### Questions
1. Does the use of the shattering rate remove all issues of the previous bound discussed in Section 3.1? Is the bound now tight? I think it would improve the clarity to provide a more explicit explanation.
2. How expensive is RACE-CARS compared to SRACOS (and other algorithms)? Some discussion and empirical study of the computational complexity would be helpful?
3. Did you try a BO algorithm as a baseline in the experiments? In addition, why was DE and ZO-Adam not included in the LLM experiment?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
